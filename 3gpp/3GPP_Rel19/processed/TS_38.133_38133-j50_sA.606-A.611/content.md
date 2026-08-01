---
type: spec
aliases:
  - 38.133_38133-j50_sA.606-A.611
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.606-A.611/content.md"
---
# TS 38.133 38133-j50_sA.606-A.611

## A.6.6Measurement procedure

## A.6.6.1Intra-frequency Measurements

## A.6.6.1.1SA event triggered reporting tests without gap under non-DRX

## A.6.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.1.1.1-1 and A.6.6.1.1.1-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.1.1.1.2-1: Supported test configurations

Table A.6.6.1.1.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.1.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.2SA event triggered reporting tests without gap under DRX

## A.6.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.2.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.1.2.2-1, A.6.6.1.2.2-2 and A.6.6.1.2.2-3 below. In the measurement controlinformation, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.1.2.2-1: Supported test configurations

Table A.6.6.1.2.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

Table A.6.6.1.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.6.6.1.2.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.3SA event triggered reporting tests with per-UE gaps under non-DRX

## A.6.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.6.6.1.3.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.1.3.1-1 and A.6.6.1.3.1-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.6.6.1.3.2-1: Supported test configurations

Table A.6.6.1.3.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

Table A.6.6.1.3.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

## A.6.6.1.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.4SA event triggered reporting tests with per-UE gaps under DRX

## A.6.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.6.6.1.4.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.1.4.2-1, A.6.6.1.4.2-2 and A.6.6.1.4.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.1.4.2-1: Supported test configurations

Table A.6.6.1.4.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with DRX

Table A.6.6.1.4.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with DRX

Table A.6.6.1.4.2-4: Void

Table A.6.6.1.4.2-5: Void

## A.6.6.1.4.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.5SA event triggered reporting tests without gap under non-DRX with SSB index reading

## A.6.6.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.6.6.1.5.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.6.6.1.5.2-1 and A.6.6.1.5.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.1.5.2-1: Supported test configurations

Table A.6.6.1.5.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.6.6.1.5.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.6.6.1.5.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.6SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading

## A.6.6.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.6.6.1.6.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.6.6.1.6.2-1 and A.6.6.1.6.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.6.6.1.6.2-1: Supported test configurations

Table A.6.6.1.6.2-2: General test parameters for SA intra-frequency event triggered reporting with gap for FDD PCell in FR1 with SSB index reading

Table A.6.6.1.6.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with gap for FDD PCell in FR1 with SSB index reading

## A.6.6.1.6.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.7SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16

## A.6.6.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for UE configured with highSpeedMeasFlag-r16. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.7.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.1.7.2-1, A.6.6.1.7.2-2 and A.6.6.1.7.2-3 below. In the measurement controlinformation, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.1.7.2-1: Supported test configurations

Table A.6.6.1.7.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX for UE configured with highSpeedMeasFlag-r16

Table A.6.6.1.7.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX for UE configured with highSpeedMeasFlag-r16

## A.6.6.1.7.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 5120 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.8SA event triggered reporting tests without gap under DRX for UE configured with highSpeedMeasCA-Scell-r17

## A.6.6.1.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for UE configured with highSpeedMeasCA-Scell-r17. This test will partly verify the intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.6.6.1.8.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), a FR1 deactivated SCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the SCell (Cell 2). The test parameters for PCell are given in table A.6.6.1.8.21, A.6.6.1.8.2-2 and A.6.6.1.8.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.1.8.2-1: Supported PCell test configurations

Table 6.6.1.8.4.1-1A: Supported SCell test configurations

Table A.6.6.1.8.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for deactivated SCell in FR1 with DRX highSpeedMeasCA-Scell-r17

Table A.6.6.1.8.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for deactivated SCell in FR1 with DRX highSpeedMeasCA-Scell-r17

## A.6.6.1.8.3Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 5760 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.9SA event triggered reporting tests with MUSIM gap configured

## A.6.6.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event on an intra-frequency layer based on measurement performed without measurement gaps when the UE is also configured with MUSIM gaps. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.9.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.1.9.2-1 and A.6.6.1.9.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.1.9.2.2-1: Supported test configurations

Table A.6.6.1.9.2.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.1.9.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.1.9.3Test requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.10SA event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP

## A.6.6.1.10.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of an event when CD-SSB is outside active BWP. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

The test environment is the same as in clause A.6.6.1.1 with following exceptions in table Table A.6.6.1.1.2-3.

Table A.6.6.1.1.2-3: Test environment exceptions

## A.6.6.1.10.2Test Requirements

The test requirements are the same as in clause A.6.6.1.1.3.

## A.6.6.1.11SA event triggered reporting tests without gap under non-DRX with NCD-SSB

## A.6.6.1.11.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements when NCD-SSB is configured in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.11.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.1.11.1-1 and A.6.6.1.11.1-2 below. The CD-SSB is configured outside active DL BWP and NCD-SSB is configured fully within active DL BWP of FR1 PCell. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.1.11.1.2-1: Supported test configurations

Table A.6.6.1.11.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.1.11.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.1.11.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.12SA event triggered reporting tests without gap under non-DRX with SSB index reading and 12 PRB SSB

## A.6.6.1.12.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 makes correct reporting of an event when the intra-frequency target cell is transmitting 12 PRB SSB. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2 for 3 MHz Channel Bandwidth configured with SSB time index detection when DRX is not used and with 15 PRB PDCCH configuration.

## A.6.6.1.12.2Test parameters

The test procedure in clause A.6.6.1.5.2 applies for this test. Supported test configurations are specified in table A.6.6.1.12.2-1. General test parameters as specified in table A.6.6.1.5.2-2 with config 1 apply to this test, except those specified in table A.6.6.1.12.2-2. Cell specific test parameters as specified in table A.6.6.1.5.2-3 with config 1 apply to this test, except those specified in table A.6.6.1.12.2-3.

Table A.6.6.1.12.2-1: Supported test configurations

Table A.6.6.1.12.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.6.6.1.12.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.6.6.1.12.3Test Requirements

The test requirements in clause A.6.6.1.5.3 applies to this test, except that the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 940 ms from the beginning of time period T2.

## A.6.6.1.13SA event triggered reporting tests without gap under Cell DTX

## A.6.6.1.13.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2 under Cell DTX configuration.

## A.6.6.1.13.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.1.13.2-1 and A.6.6.1.13.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. During time duration T2, NW triggers the Cell DTX.

UE is allocated with PUSCH resource at every Cell DTX cycle.

Table A.6.6.1.13.2-1: Supported test configurations

Table A.6.6.1.13.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1 with Cell DTX

Table A.6.6.1.13.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1 with Cell DTX

## A.6.6.1.13.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 + 160 = 1080 ms from the beginning of time period T2, while 160 ms is the Cell DTX cycle length, which is the delay uncertainty for next available PUSCH for L3 MR reporting during cell DTX. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.14Deactivated PSCell measurement test with 12 PRB SSB bandwidth in FR1

## A.6.6.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of deactivated PSCell measurement results when the PSCell is configured with 12 PRB SSB bandwidth. This test verifies the deactivated PSCell measurement period requirements specified in clause 9.2.5.1.

## A.6.6.1.14.2Test Parameters

The supported test configurations are given in table A.6.6.1.14.2-1. Only 15kHz FDD cases are considered. The test scenario comprises 2 NR cells – PCell (Cell 1) and target PSCell (Cell 2).

Cell 1 is on radio channel 1 in FR1. Cell 2 is on radio channel 2 in FR1. Test parameters are given in Tables A.6.6.1.14.2-2, A.6.6.1.14.2-3 below. Note that for Cell 2 the SSB configuration refers to SSB pattern 13 in FR1: SSB allocation for SSB SCS=15kHz in 3 MHz. In the test, the SSB is configured with 12PRB bandwidth.

The test consists of two successive time periods, with time duration of T1, and T2 respectively.

At the start of T1, the UE is in connected mode to Cell 1. During time duration T1, the UE is configured to add Cell 2 as PSCell so that Cell 1 and Cell 2 serve UE under NR-DC operation. Meanwhile the UE is configured to measure on both Cell 1 and Cell 2 serving carrier frequencies. The UE is configured to read the SSB index for measurement of PSCC.

At the end of T1, the UE deactivates Cell 2. T2 starts exactly when the UE receives deactivation command for Cell 2. During T2, Cell 2 remains detectable to the UE.

Measurement gap or DRX is not configured.

The UE is required to make correct and timely reporting during T2. This test case verifies that the UE reporting is within the delay requirement and measurement accuracy is tested in other test cases.

Table A.6.6.1.14.2-1: Supported test configuration

Table A.6.6.1.14.2-2: General test parameters for deactivated PSCell measurements when PSCell is configured with 12 PRB SSB bandwidth

Table A.6.6.1.14.2-3: Cell specific test parameters for deactivated PSCell measurement with 12 PRB SSB bandwidth

## A.6.6.1.14.3Test Requirements

The UE shall send one measurement report for the deactivated PSCell, with a measurement reporting delay less than 2720 ms from the beginning of time period T2.

The UE is required to successfully detect PSS/SSS for Cell 2 within

Ceil(5 x Kp) x measCyclePSCell x CSSFintra;

The UE is required successfully read the SSB index for Cell 2 within

Ceil(7 x Kp) x measCyclePSCell x CSSFintra;

The UE is required to successfully measure on Cell 2 within

Ceil(5 x Kp) x measCyclePSCell x CSSFintra;

Where

-measCyclePSCell = 160 ms,

-Kp = 1,

-CSSFintra = 1.

This sums up as 2720 ms in total, consisting of 800 ms of PSS/SSS detection, 1120 ms of SSB index detection and 800 ms of measurement time.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.15SA event triggered reporting test without gap under non-DRX with SSB index reading and 12 PRB SSB for a deactivated SCell

## A.6.6.1.15.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 makes correct reporting of an event on an intra-frequency layer measurement performed without measurement gaps when the UE is also configured deactivated SCell. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.1.15.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1) on Carrier 1, FR1 Neighbouring cell (Cell 2) and a FR1 SCell (Cell 3) on Carrier 2. Carrier 2 is on a different frequency than the PCell.

The test parameters for PCell, SCell and neighbour cell are given in table A.6.6.1.15.2-1, A.6.6.1.15.2-2 and A.6.6.1.15.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and the SCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.1.15.2-1: Supported test configurations

Table A.6.6.1.15.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1 with 12 PRB SSB for SCell

Table A.6.6.1.15.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1 with 12 PRB SSB for SCell

## A.6.6.1.15.3Test requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2720 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.16OD-SSB based deactivated SCell measurement under non-DRX mode in FR1 (OD-SSB Case 1)

## A.6.6.1.16.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based deactivated SCell measurement are within the requirements stated in clause 9.17.5.3 and 9.17.5.4.

The supported test configurations are shown in table A.6.6.1.16.1-1 below. The test parameters are given in table A.6.6.1.16.1-2 and cell-specific parameters in table A.6.6.1.16.1-3 below.

There are two NR carriers, each with one cell. Both cells have constant signal levels and the SCell activation command is not configured throughout the test.  Measurement gap or DRX is not configured, and measCycleSCell is configured as 160 ms.

At the start of T1, the UE is in connected mode to Cell 1. During time duration T1, the UE is configured to add Cell 2 as a deactivated SCell without a first SSB transmission, and then the first activation of OD-SSB transmission is indicated on Cell 2. At the end of T1, OD-SSB transmission is indicated to be deactivated.

During T2, after processing of OD-SSB deactivation command, UE does not measure on Cell 2. UE only needs to pass one of the two cases (case A and B) depending on the duration of T2. At the end of T2 and before the start of T3, UE is indicated the second activation of OD-SSB transmission at slot n.

During T3, after the slot n+ when UE completes the command of OD-SSB activation, UE performs the deactivated SCC measurement as follows. THARQ+3ms+TprocessingNR slot length

-Case A: T2 is 320ms (less than 5*measCycleSCell in FR1)

For Case A, during T3, UE performs the legacy deactivated SCC measurement and report (based on TPSS/SSS_sync_intra_ODSSB, TSSB_time_index_intra_ODSSB, TSSB_measurement_period_intra_ODSSB given in table 9.17.5.3-3, 9.17.5.3-5 and 9.17.5.4-2 for FR1), until UE is indicated the second deactivation of OD-SSB transmission.

The test under case A consists of 3 successive time periods, with duration of T1, T2 and T3, respectively.

-Case B: T2 is 960ms (larger than 5* measCycleSCell in FR1)

For Case B, during T3, UE performs the deactivated SCell measurement during FMW (based on TPSS/SSS_sync_intra_ODSSB, TSSB_time_index_intra_ODSSB, TSSB_measurement_period_intra_ODSSB given in table 9.17.5.3-1, 9.17.5.3-2 and 9.17.5.4-1 for FR1), until UE reports the deactivated Scell measurement results.

After that, during T4, UE performs the legacy deactivated SCC measurement and report (based on TPSS/SSS_sync_intra_ODSSB, TSSB_time_index_intra_ODSSB, TSSB_measurement_period_intra_ODSSB given in table 9.17.5.3-3, 9.17.5.3-5 and 9.17.5.4-2 for FR1), until UE is indicated the second deactivation of OD-SSB transmission.

The test under case B consists of 4 successive time periods, with duration of T1, T2, T3, and T4, respectively.

The UE is required to make correct and timely reporting during T3 and T4. This test case verifies that the UE reporting is within the delay requirement and measurement accuracy is tested in other test cases.

In addition, this test also verifies the requirements of PCell interruption due to measurements on deactivated Scell during T3 and T4. The UE is only allowed to cause interruptions on PCell at the first SSB burst and the last SSB burst within FMW specified in clause 8.2.2.2.3. The interruption length shall not exceed requirements in table 8.2.2.2.3-1.

Table A.6.6.1.16.1-1: Supported test configurations

Table A.6.6.1.16.1-2: General test parameters for deactivated SCell measurements in FR1

Table A.6.6.1.16.1-3: Cell specific test parameters for NR PCell

Table A.6.6.1.16.1-4: Cell specific test parameters for NR SCell

## A.6.6.1.16.2Test Requirements

For Case A, the UE shall send one measurement report for the deactivated SCell, with a measurement reporting delay less than 2080 ms from the beginning of time period T3.

The UE is required to successfully detect PSS/SSS for Cell 2 within

Ceil(5 x Kp) x measCycleSCell x CSSFintra;

The UE is required successfully read the SSB index for Cell 2 within

Ceil(3 x Kp) x measCycleSCell x CSSFintra;

The UE is required to successfully measure on Cell 2 within

Ceil(5 x Kp) x measCycleSCell x CSSFintra;

Where

-measCyclePSCell = 160 ms,

-Kp = 1,

-CSSFintra = 1.

This sums up as 2080 ms in total, consisting of 800 ms of PSS/SSS detection, 480 ms of SSB index detection and 800 ms of measurement time.

During T3, the same test requirements for interruptions on PCell during measurements on deactivated SCell can apply, as defined in clause A.6.5.2.1.2.

For Case B, the UE shall send one measurement report for the deactivated SCell, with a measurement reporting delay less than 130 ms from the beginning of time period T3. The UE shall send another measurement report for the deactivated SCell, with a measurement reporting delay less than 2080 ms (as calculated for Case A above) from the beginning of time period T4.

The UE is required to successfully detect PSS/SSS for Cell 2 within

Ceil(M x Kp) x OD-SSB periodicity x CSSFintra;

The UE is required successfully read the SSB index for Cell 2 within

Ceil(3 x Kp) x OD-SSB periodicity x CSSFintra;

The UE is required to successfully measure on Cell 2 within

Ceil(M x Kp) x OD-SSB periodicity x CSSFintra;

Where

-OD-SSB periodicity = 10 ms,

-Kp = 1,

-CSSFintra = 1.

-M = 5.

The sums up as 130 ms in total, consisting of 800 ms of PSS/SSS detection, 480 ms of SSB index detection and 800 ms of measurement time

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

During T3, the interruption on PCell shall not exceed requirement in table 8.2.2.2.3-1. The UE shall be continuously scheduled on PCell after the first SSB burst and before the last SSB burst within FMW.

During T4, the same test requirements for interruption on PCell during measurements on deactivated SCell can apply, as defined in clause A.6.5.2.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.1.17SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB

## A.6.6.1.17.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event based on OD-SSB measurement on deactivated SCell. This test will partly verify the FR2 intra-frequency cell identification for deactivated SCell requirements as defined in clause 9.17.5 and interruption requirements at OD-SSB activation as defined in clause 8.2.2.2.22. Supported test configurations for NR PCell are shown in table A.6.6.1.17.1-1. Supported test configurations for NR SCell are shown in table A.6.6.1.17.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

Table A.6.6.1.17.1-1: supported test configurations for NR PCell

Table A.6.6.1.17.1-1A: supported test configurations for NR SCell

There are two cells in the test, PCell (Cell 1) and a FR1 Sell (Cell 2). The test parameters for the Cell 1 and Cell 2 are given in table A.6.6.1.17.1-2 and A.6.6.1.17.1-3 below.

In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A1 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. Before T2, Cell2 is added as SCell via SCell addition and remains deactivated. During time duration T1, the UE shall not have any timing information of Cell 2. TE sends OD-SSB activation from the start of T2 and Cell 2 is detectable from the start of T2.

The test equipment also verifies that potential interruption by monitoring ACK/NACK sent in PCell during T2.

Table A.6.6.1.17.1-2: General test parameters for intra-frequency event triggered reporting for deactivated SCell based on OD-SSB

Table A.6.6.1.17.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for deactivated SCell based on OD-SSB

## A.6.6.1.17.2Test Requirements

In the test, the UE shall send one Event A1 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is THARQ+3+ OD-SSB post processing time + 200.

The interruption of PCell due to activation of OD-SSB shall not be more than the values specified for NR SA in clause 8.2.2.2.22.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.18SA event triggered reporting tests without gap under non-DRX based on OD-SSB

## A.6.6.1.18.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for UE indicated by od-ssb-config TS 38.331[2] or by a MAC CE TS 38.321[7], activation of transmission for OD-SSB in a configured DL BWP of an SCell TS 38.300[10] if UE supports On-demand SSB operation. This test will partly verify the intra-frequency cell search requirements in clause 9.17.5.1 and 9.17.5.2.

## A.6.6.1.18.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), a FR1 activated SCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the SCell (Cell 2). The test parameters for PCell are given in table A.6.6.1.18.2-1, A.6.6.1.18.2-2 and A.6.6.1.18.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3. During the time duration, an OD-SSB transmission, which cannot be used to obtain SIB1, is activated in a configured DL BWP of the SCell (Cell 2).

Table A.6.6.1.18.2-1: Supported PCell test configurations

Table A.6.6.1.18.2-1A: Supported SCell test configurations

Table A.6.6.1.18.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for activated SCell in FR1 with non-DRX baed on OD-SSB

Table A.6.6.1.18.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for activated SCell in FR1 with non-DRX based on OD-SSB

## A.6.6.1.18.3Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.1.19SA event triggered reporting test for a UE configured with LB CA via switching

## A.6.6.1.19.1Test purpose and Environment

The purpose of this test is to verify that a UE supporting LB CA via switching and configured with lowBandCA-Switching-r19 performs correct event triggered reporting for intra-frequency measurements on the FDD PCell and SDL SCell. This test will partly verify the intra-frequency measurement period requirements as specified in Clauses 9.2.5.1 and 9.2.5.2. In this test configuration, DRX and measurement gaps are not configured.

## A.6.6.1.19.2Test parameters

In this test setup, three FR1 cells are deployed. Cell 1 is the PCell, operating on FDD Carrier 1. Cell 2 is an intra-frequency neighbouring cell, also on FDD Carrier 1. Cell 3 is an SCell, operating on Carrier 2, which is on a different frequency than the PCell and is configured as a supplementary downlink (SDL) SCell.

In the measurement control information, a measurement object (MO) is configured for both the PCell frequency and the SCell frequency. The UE is instructed to perform event-triggered reporting using:

-Event A3 for the MO of the PCell

-Event A6 for the MO of the SCell

The test consists of two successive time periods, with durations T1 and T2, respectively. During T1, the UE shall not have any timing information for Cell 2. Before start of the T1, SCell is configured and activated.

Table A.6.6.1.19.2-1: Supported test configurations

In the test,

-the switching from PCell to SCell shall end at the end of the last slot from a sequence of consecutive slots with bit value ‘0’ and the switching to SCell shall not start N1 symbols before the last symbol of the last slot in that sequence.

-the switching from SCell to PCell shall end at the end of the last slot from a sequence of consecutive slots with bit value ‘1’ and the switching to PCell shall not start N2 symbols before the last symbol of the last slot in that sequence.

Table A.6.6.1.19.2-2: Test parameters for LB CA switching

Table A.6.6.1.19.2-3: General test parameters for SA intra-frequency event triggered reporting

Table A.6.6.1.19.2-4: NR Cell specific test parameters for SA intra-frequency event triggered reporting

## A.6.6.1.19.3Test requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.1.20SA event triggered reporting tests without gap under non-DRX in FR1 for UE supporting [FR1 only CA and FR1 only NR-DC 3-searcher capability]

## A.6.6.1.20.1Test purpose and Environment

The purpose of this test is to partly verify the intra-frequency cell search requirements in clause 9.1.5.1, clauses 9.2.5.1 and 9.2.5.2 for UE supporting [FR1 only CA and FR1 only NR-DC 3-searcher capability] makes correct reporting of an event.

## A.6.6.1.20.2Test parameters

In this test, NR cell 1 as PCell in FR1 on NR RF channel 1, NR cell 2 as SCell in FR1 on NR RF channel 2, NR cell 3 as SCell in FR1 on NR RF channel 3, where NR RF channel 1, NR RF channel 2 and NR RF channel 3 are in different bands, furthermore, NR cell 4 as neighbour cell in FR1 on NR RF channel 2 same as NR cell 2.

In the measurement control information, SCells with only SSB based L3 measurement are configured, and a measurement object is configured for the frequency of the neigbor cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. For UE support inter-RAT measurement, a measurement object is configured for the frequency of the LTE neighbour cell, it is indicated to the UE that event-triggered reporting with Event A6 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 4.

Supported test configurations of tess are shown in table A.6.6.1.20.2-1.

Table A.6.6.1.20.2-1: Supported test configurations

The test parameters of tests are shown in table A.6.6.1.20.2-2 and A.6.6.1.20.2-3 below.

Table A.6.6.1.20.2-2: General test parameters for intra-frequency event triggered reporting for FR2 without SSB time index detection

Table A.6.6.1.20.2-3: Cell specific test parameters for intra-frequency event triggered reporting for FR2 without SSB time index detection, for test case 1

## A.6.6.1.20.3Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 1600 for UE supporting power class 1, or

## 960 for UE supporting other power class.

In this test UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2Inter-frequency Measurements

## A.6.6.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.6.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.2.1.1-1, A.6.6.2.1.1-2 and A.6.6.2.1.1-3.

Measurement gap pattern configuration is defined in table A.6.6.2.1.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.6.6.2.1.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.6.6.2.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.6.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.2.2.1-1, A.6.6.2.2.1-2 and A.6.6.2.2.1-3.

Measurement gap pattern configuration is defined in table A.6.6.2.2.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.2.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.2.2.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.6.6.2.2.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.6.6.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 1 and 2, UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.3Void

## A.6.6.2.4Void

## A.6.6.2.5SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.6.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.2.5.1-1, A.6.6.2.5.1-2 and A.6.6.2.5.1-3.

Measurement gap pattern configuration is defined in table A.6.6.2.5.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.6.6.2.5.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

Table A.6.6.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.6.6.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.6.6.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.6SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.6.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.2.6.1-1, A.6.6.2.6.1-2 and A.6.6.2.6.1-3.

Measurement gap pattern configuration is defined in table A.6.6.2.6.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.2.6.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

Table A.6.6.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.6.6.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.6.6.2.6.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 1 and 2, UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.7Void

## A.6.6.2.8Void

## A.6.6.2.9SA event triggered reporting tests with additional mandatory gap pattern

## A.6.6.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when mandatory gap pattern with 3 ms MGL is configured.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.2.9.1-1, A.6.6.2.9.1-2 and A.6.6.2.9.1-3.

Measurement gap pattern configuration defined in table A.6.6.2.9.1-2 does not depend on per-FR gap capability of UE.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.6.6.2.9.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

Table A.6.6.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

## A.6.6.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.10SA event triggered reporting tests for FR1 when DRX is used

## A.6.6.2.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE which supports interFrequencyMeas-Nogap-r16 makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search without measurement gap requirements in clause 9.3.9.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters are given in tables A.6.6.2.10.1-1, A.6.6.2.10.1-2 and A.6.6.2.10.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.2.10.1-1: SA event triggered reporting tests when DRX is used for FR1-FR1

Table A.6.6.2.10.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.6.6.2.10.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.6.6.2.10.1-4: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting when DRX is used

## A.6.6.2.10.2Test Requirements

In test config 1, UE is required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1120  ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test config 2 and 3, UE is not required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.6.6.2.11SA event triggered reporting tests for FR1 without gap when DRX is not used

A.6.6.2.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.9.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters are given in tables A.6.6.2.11.1-1, A.6.6.2.11.1-2 and A.6.6.2.11.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.6.6.2.11.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.11.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without gap

Table A.6.6.2.11.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without gap

A.6.6.2.11.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

The UE is not required to read the neighbour cell SSB index in this test.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.12SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17

## A.6.6.2.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when UE is configured with highSpeedMeasInterFreq-r17. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.2.12.1-1, A.6.6.2.12.1-2 and A.6.6.2.12.1-3.

Measurement gap pattern configuration is defined in table A.6.6.2.12.1-2. In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.6.6.2.12.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.12.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection for UE configured with highSpeedMeasInterFreq-r17

Table A.6.6.2.12.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection for UE configured with highSpeedMeasInterFreq-r17

## A.6.6.2.12.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.13SA event triggered reporting tests for FR1 with measurement gap with priority and periodic MUSIM gap configured

## A.6.6.2.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event on an inter-frequency layer based on measurement performed within measurement gap when UE is also configured with MUSIM gaps. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4. In addition, the test will verify that UE makes correct transmission/reception during occasions of measurement gaps and MUSIM gaps that are dropped due to collision handling as defined in clause 9.1.10.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.2.13.1-1, A.6.6.2.13.1-2 and A.6.6.2.13.1-3.

Measurement gap and MUSIM gap pattern configurations defined in table A.6.6.2.13.1-2 are provided to the UE.

NOTE:The signaling procedure to trigger the UE to request MUSIM gaps before the test equipment configures MUSIM gaps to the UE is left to comformance test implementation.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1 and T3, the UE shall not have any timing information of NR Cell 2. During T1 and T2, MUSIM gap is configured with lower priority than the measurement gap. At the beginning of T3, test equipment reconfigures the priority of MUSIM gap such that MUSIM gap is configured with higher priority than the measurement gap during T3 and T4.

The TE schedules continuous DL data on PCell throughout the test.

Table A.6.6.2.13.1-1: Supported test configurations

Table A.6.6.2.13.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.2.13.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.6.6.2.13.2Test Requirements

During T1 and T2, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the measurement gap occasions.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

During T3 and T4, after UE sends RRC ReconfigurationComplete message for the reconfiguration of MUSIM gap priority, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with

-MUSIM gap occasions, and

-measurement gap occasions that are not colliding with MUSIM gap.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T4. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

UE is not required to report SSB time index.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.14SA event triggered reporting tests for FR1 with measurement gap without priority and periodic MUSIM gap configured

## A.6.6.2.14.1Test Purpose and Environment

The purpose of this test is to verify that the MUSIM gap capable UE makes correct reporting of an event when MUSIM gap collides with measurement gaps without assigned priority. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4. This test is conducted assuming that the measurement gap is configured as Gap(s) configured via GapConfig without suffix, and the MUSIM gap parameters are configured as requested by UE.

NOTE:The signaling procedure to trigger the UE to request MUSIM gaps before the test equipment configures MUSIM gaps to the UE is left to comformance test implementation.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.2.14.1-1, A.6.6.2.14.1-2 and A.6.6.2.14.1-3.

Measurement gap pattern configuration defined in table A.6.6.2.14.1-2 is provided for a UE.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.6.6.2.14.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.2.14.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 measurement gap and periodic MUSIM gap with partially partial overlapping scenario for SSB-based measurements in inter-frequency layers

Table A.6.6.2.14.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 measurement gap and periodic MUSIM gap with partially partial overlapping scenario for SSB-based measurements in inter-frequency layers

## A.6.6.2.14.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.15SA event triggered reporting tests for FR1 with 3 MHz Channel Bandwidth configured with SSB time index detection when DRX is used

## A.6.6.2.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4 for 3 MHz Channel Bandwidth configured with SSB time index detection when DRX is used and with 15 PRB PDCCH configuration.

Supported test configurations are specified in table A.6.6.2.15.1-1. General test parameters as specified in table A.6.6.2.2.1-2 with config 1 apply to this test, except that the time duration T2 is set as 2s for test 1 and 15s for test 2. Cell specific test parameters as specified in table A.6.6.2.2.1-3 with config 1 apply except those specified in table A.6.6.1.13.1-2. DRX-Configuration and TimeAlignmentTimer -Configuration specified in table A.6.6.2.2.1-4 and table A.6.6.2.2.1-5, respectively, apply to this test case.

The test environment specified in A.6.6.2.2.1 applies to this test.

Table A.6.6.2.15.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

Table A.6.6.2.15.1-2: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.6.6.2.15.2Test Requirements

Test requirements specified in clause A.6.6.2.2.2 apply to this test, except that the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms and 14080 ms from the beginning of time period T2 in test 1 and test 2, respectively.

In both test 1 and test 2, UE is required to report SSB time index.

## A.6.6.2.16SA event triggered reporting tests with SSB adaptation without SSB time index detection without gap under non-DRX

## A.6.6.2.16.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct measurement when SSB adaptation happens for an SCell and reporting of an event. This test will partly verify the intra-frequency cell search requirements for serving cell in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.2.16.2Test parameters

There are two carriers and one cell on each carrier in the test, NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as SCell in FR1 on NR RF channel 2. The testing configurations for NR cells are in table A.6.6.2.16.1-1. The test parameters for the Cell 1 and Cell 2 are given in table A.6.6.2.16.2-1, table A.6.6.2.16.2-2 and table A.6.6.2.16.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A2 is used. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At the starting of T2, the UE receives DCI format 2_9 in the PCell, and the SSB adaptation of SCell is indicated by the DCI format 2-9. As long as UE receives the indication of SSB adapatation of SCell, UE follows the transition requirements defined in Clause 9.1.6 and the transition period ends at the end of T2. At the starting of T3, the channel condition changes and the condition of Event A2 meets.

Table A.6.6.2.16.1.2-1: Supported test configurations

Table A.6.6.2.16.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.2.16.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.2.16.3Test Requirements

The UE shall send one Event A2 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.17SA event triggered reporting tests under non-DRX

## A.6.6.2.17.1Test purpose and Environment

The purpose of this test is to partly verify the inter-frequency cell search requirements in clause 9.1.5.1 and 9.3.9 for UE supports interFrequencyMeas-Nogap-r16 and/or NeedForGapsInfoNR-r16 and fr1-CA-NR-DC-r19 or fr1-FR2-CA-r19 via threeCarrierMeasWithoutGap-r19 makes correct reporting of an event.

The UE is only required to pass one of the three tests in A.4.6.2.10 for FR1 EN-DC, A.6.6.2.17 for FR1 CA, A.7.6.2.25 for FR1 and FR2 CA.

## A.6.6.2.17.2Test parameters

In this test, NR cell 1 as PCell in FR1 on NR RF channel 1, NR cell 2 as SCell in FR1 on NR RF channel 2. NR cell 3 as neighbour cell in FR1 on NR RF channel 3 which is in the same band as NR Cell 1. The SSB of Cell 3 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 3 should be different in frequency location within the cell bandwidth. Supported test configurations are shown in table A.6.6.2.17.2-1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.6.6.2.17.2-1: Supported test configurations

Table A.6.6.2.17.2-2: General test parameters for inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.2.17.2-3: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.6.6.2.17.3Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of time period T2.

UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.2.18SA event-triggered reporting tests for FR1 without SSB time index detection when DRX is not used for UE configured with measurement gap cancellation

## A.6.6.2.18.1Test Purpose and Environment

The purpose of this test is to verify that the UE, which is configured with measurement gap cancellation according to clause 9.1.14, makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test configurations and parameters are the same as in tables A.6.6.2.1.1-1, A.6.6.2.1.1-2 and A.6.6.2.1.1-3 in clause A.6.6.2.1.1, except the parameters listed in table A.6.6.2.18.1-1.

Measurement gap pattern configuration is as defined in table A.6.6.2.1.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and shall provide its capability in enableTx-RxDuringMeasGap-r19 [2]. During time duration T2, the test equipment randomly selects which measurement gap occasions will be cancelled via DCI indication, so that Lcancel,PSS/SSS measurement gap occasions are cancelled during T2_1, and Lcancel,meas measurement gap occasions are cancelled during T2_2, where T2, T2_1, T2_2, Lcancel,PSS/SSS, and Lcancel,meas are given in table A.6.6.2.18.1-1. If a measurement gap occasion is determined to be cancelled, the test equipment sends the DCI indication latest X ms before the start of the measurement gap occasion to be cancelled using DCI format 1-1, where X is 3ms or 5ms as given by the UE capability minimumTimeOffset-r19 [2].

During time duration of T2, the UE is scheduled with DL data on PCell on all the slots overlapping with the cancelled measurement gap occasions.

Table A.6.6.2.18.1-1: General test parameters for SA inter-frequency event triggered reporting

## A.6.6.2.18.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2, assuming Lcancel,PSS/SSS=5 and Lcancel,meas=3. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

During time T2, the UE shall send valid ACK/NACK for all the scheduled transmissions in all the slots overlapping with the cancelled measurement gap occasions.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.3Inter-RAT Measurements

## A.6.6.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1

## A.6.6.3.1.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.6.6.3.1.1-1. General test parameters are provided in table A.6.6.3.1.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.3.1.1-3 and A.6.6.3.1.1-4, respectively.

Table A.6.6.3.1.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.3.1.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.3.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.3.1.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.3.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.3.2SA NR - E-UTRAN event-triggered reporting in DRX in FR1

## A.6.6.3.2.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3. There are two test cases. In test 1 the UE shall be configured with DRX cycle of 40 ms. In test 2 the UE shall be configured with DRX cycle of 640 ms.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indctated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

In each test the UE shall be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.6.6.3.2.1-1. General test parameters are provided in table A.6.6.3.2.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.3.2.1-3 and A.6.6.3.2.1-4, respectively.

Table A.6.6.3.2.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.6.6.3.2.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.6.6.3.2.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1

Table A.6.6.3.2.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

## A.6.6.3.2.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

In test 2, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 12.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.3.3SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16

## A.6.6.3.3.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements for UE configured with highSpeedMeasFlag-r16 in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3.

In the test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

The UE shall be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.6.6.3.3.1-1. General test parameters are provided in table A.6.6.3.3.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.3.3.1-3 and A.6.6.3.3.1-4, respectively.

Table A.6.6.3.3.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1 for UE configured with highSpeedMeasFlag-r16

Table A.6.6.3.3.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1 for UE configured with highSpeedMeasFlag-r16

Table A.6.6.3.3.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1 for UE configured with highSpeedMeasFlag-r16

Table A.6.6.3.3.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1 for UE configured with highSpeedMeasFlag-r16

## A.6.6.3.3.2Test Requirements

In the test, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 4.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.4L1-RSRP measurement for beam reporting

## A.6.6.4.1SSB based L1-RSRP measurement when DRX is not used

## A.6.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.1.1-1.

Table A.6.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.1.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.1.2-1 and table A.6.6.4.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.1.2-1: General test parameters

Table A.6.6.4.1.2-2: SSB specific test parameters

## A.6.6.4.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.2SSB based L1-RSRP measurement when DRX is used

## A.6.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.2.1-1.

Table A.6.6.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.2.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.2.2-1 and table A.6.6.4.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.2.2-1: General test parameters

Table A.6.6.4.2.2-2: SSB specific test parameters

## A.6.6.4.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.3CSI-RS based L1-RSRP measurement when DRX is not used

## A.6.6.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.6.6.4.3.1-1.

Table A.6.6.4.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.6.6.4.3.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.3.2-1 and table A.6.6.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.6.6.4.3.2-1: General test parameters

Table A.6.6.4.3.2-2: CSI-RS specific test parameters

## A.6.6.4.3.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at the 8th slot from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.20.1.1 and relative accuracy requirement in clause 10.1.20.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.4CSI-RS based L1-RSRP measurement when DRX is used

## A.6.6.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.6.6.4.4.1-1.

Table A.6.6.4.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.6.6.4.4.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.4.2-1 and table A.6.6.4.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.4.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.6.6.4.4.2-1: General test parameters

Table A.6.6.4.4.2-2: CSI-RS specific test parameters

## A.6.6.4.4.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.20.1.1 and relative accuracy requirement in clause 10.1.20.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.5SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r16

## A.6.6.4.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when UE is configured with highSpeedMeasFlag-r16. This test will partly verify the L1-RSRP measurement requirements for UE configured with highSpeedMeasFlag-r16 in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.5.1-1.

Table A.6.6.4.5.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.5.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.5.2-1 and table A.6.6.4.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.5.2-1: General test parameters for UE configured with highSpeedMeasFlag-r16

Table A.6.6.4.5.2-2: SSB specific test parameters for UE configured with highSpeedMeasFlag-r16

## A.6.6.4.5.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.6Inter-cell SSB based L1-RSRP measurements on FR1 PCell when DRX is used

## A.6.6.4.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement for SSB of a cell with additional PCI. This test will partly verify the L1-RSRP measurement requirements in clause 9.13.4.1, with the testing configurations for NR serving cells in table A.6.6.4.6.1-1.

Table A.6.6.4.6.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.6.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and a cell with additional PCI (Cell 2). The test parameters for the Cell 1 are given in table A.6.6.4.6.2-1. The test parameters for Cell 2 are given in table A.6.6.4.6.2-2 below.

SSB#0 and SSB#1 are transmitted on Cell 1 and Cell 2. In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSB#0 and report measurement results periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. At the beginning of T2, SSB#1 starts transmission and the UE is configured for L1-RSRP measurement on SSB#1. The test has higher layer parameter timeRestrictionForChannelMeasurements configured in CSI-ReportConfig and additionalPCIList configured in CSI-SSB-ResourceSet.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the the SSB#0 for Cell 1.

Table A.6.6.4.6.2-1: General test parameters

Table A.6.6.4.6.2-2: SSB specific test parameters

## A.6.6.4.6.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than X ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of SSB#1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2, where X is

-680 for Config 1&2

-660 for Config 3

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.7SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.6.6.4.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.1.1-1.

The test environment is the same as in A.6.6.4.1 with following exceptions in table A.6.6.4.1.2-1.

Table A.6.6.4.1.2-1

## A.6.6.4.7.2Test Requirements

The test requirements are the same as in A.6.6.4.1.3.

## A.6.6.4.8CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.6.6.4.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.6.6.4.3.1-1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in A.6.6.4.3.

The test environment is the same as in A.6.6.4.3.2 with following exceptions in table Table A.6.6.4.3.2-1.

The value of parameter “Dedicated BWP configuration” is DLBWP.1.2 and ULBWP.1.2.

NOTE:The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in A.6.6.4.3.3.

## A.6.6.4.9SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used

## A.6.6.4.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.9.1-1.

Table A.6.6.4.9.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.9.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.9.2-1 and table A.6.6.4.9.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. During time duration T1, the UE shall not have any timing information of NR Cell 2.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.9.2-1: General test parameters

Table A.6.6.4.9.2-2: SSB specific test parameters

## A.6.6.4.9.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than [620]ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.10OD-SSB based L1-RSRP measurement when DRX is not used

## A.6.6.4.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement based on OD-SSB and AO-SSB for SCell. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.6.6.4.10.1-1, and also verify the scheduling availability during the L1-RSRP measurement in clause 9.5.6.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement based on the OD-SSB and AO-SSB, and report periodically for SCell. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. The UE shall be continuously scheduled in the PCell throughout the whole test.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.10.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.6.4.10.2Test parameters

There are two carriers and one cell on each carrier in the test, NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as SCell in FR1 on NR RF channel 2. The test parameters for the Cell 1 and Cell 2 are given in table A.6.6.4.10.2-1, table A.6.6.4.10.2-2 and table A.6.6.4.10.2-3 below.

Table A.6.6.4.10.2-1: General test parameters for SSB based L1-RSRP measurement in FR1

Table A.6.6.4.10.2-2: Cell specific test parameters for PCell

Table A.6.6.4.10.2-3: Cell specific test parameters for SCell

Table A.6.6.4.10.2-4: SSB specific test parameters

## A.6.6.4.10.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%. UE shall or not send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell based on the requirements defined in clause 9.5.6.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.11Event Triggered Reporting for UE initiated beam management without eventDetectionTimeWindowLength-r19

## A.6.6.4.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes the correct reporting of event triggered L1-RSRP measurement for the UE initiated beam management. This test will partly verify the L1-RSRP reporting requirements in clause 9.5.3.4, with the testing configurations in table A.6.6.4.11.1-1.

Table A.6.6.4.11.1-1: Supported test configurations

## A.6.6.4.11.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.11.2-1 and table A.6.6.4.11.2-2 below.

In CSI resource configuration, UE is indicated to perform L1-RSRP measurement on the resourcesForChannelMeasurement and the resourcesForChannelMeasurement consists of SSB. In the CSI report configuration, UE is configured with event-triggered reporting, with the event 2 and Mode-A, and without eventDetectionTimeWindowLength-r19 configuration. The test consists of two successive time periods, with time duration of T1 and T2, respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

During test period T1, the UE receives from SSB#0 which is the current beam. During T1, SSB#1 is not detectable. At the beginning of T2, SSB#1 becomes stronger than the SSB#0 and the event entering condition is met.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.11.2-1: General test parameters

Table A.6.6.4.11.2-2: SSB specific test parameters

## A.6.6.4.11.3Test Requirements

In the test, the UE shall send a first PUCCH message using the new UCI type, no later than 20 ms + X slots from the beginning of T2, where:

-Config 1 and 2: X = 5

-Config 3: X = 8

The UE shall not send event triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.6.4.12Event Triggered Reporting for UE initiated beam management with eventDetectionTimeWindowLength-r19

## A.6.6.4.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes the correct reporting of event triggered L1-RSRP measurement for the UE initiated beam management, when eventDetectionTimeWindowLength-r19 is configured. This test will partly verify the L1-RSRP reporting requirements in clause 9.5.3.4, with the testing configurations in table A.6.6.4.12.1-1.

Table A.6.6.4.12.1-1: Supported test configurations

## A.6.6.4.12.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.12.2-1 and table A.6.6.4.12.2-2 below.

In CSI resource configuration, UE is indicated to perform L1-RSRP measurement on the resourcesForChannelMeasurement and the resourcesForChannelMeasurement consists of SSB. In the CSI report configuration, UE is configured with event-triggered reporting, with the event 2 and Mode-A, and with eventDetectionTimeWindowLength-r19 configuration. The test consists of two successive time periods, with time duration of T1 and T2, respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

During test period T1, the UE receives from SSB#0 which is the current beam. During T1, SSB#1 is not detectable. At the beginning of T2, SSB#1 becomes stronger than the SSB#0 and the event entering condition is met.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.6.6.4.12.2-1: General test parameters

Table A.6.6.4.12.2-2: SSB specific test parameters

## A.6.6.4.12.3Test Requirements

In the test, the UE shall send a first PUCCH message using the new UCI type, no later than 60 ms + X slots from the beginning of T2, where:

-Config 1 and 2: X = 5

-Config 3: X = 8

The UE shall not send event triggered measurement reports as long as the reporting criteria with eventDetectionTimeWindowLength-r19 and eventInstanceCount-r19 according to the configuration in Table A.6.6.1.Y.2-1 is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.6.4.13Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR1 when DRX is not used

## A.6.6.4.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event based on L1-RSRP measurement . This test will partly verify the event triggered reporting for UE initiated beam management in clause 9.13.3.4 configured with event2-r19, modeA-r19 and without eventCountWindow-r19 configuration.

Table A.6.6.4.13.1-1: Applicable NR configurations for inter-cell SSB based Event triggered reporting for UE initiated beam management in FR1

## A.6.6.4.13.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a cell with different PCI from Cell 1 (Cell 2). The test parameters are given in table A.6.6.31.1.2-1and table A.6.6.31.1.2-2 below.

SSB#0 is transmitted on Cell 1. SSB#1 is transmitted on Cell 2. In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSB#1. SSB#0 is for current beam measurement and SSB#1 is for new beam measurement. The test consists of two successive time periods, with time duration of T1 and T2 respectively. At the beginning of T2, SSB#1 starts transmission and the UE is configured for L1-RSRP measurement on SSB#1, and the RSRP configuration of SSB#1 is better than SSB#0 to trigger the event-2 reporting. The test has higher layer parameter timeRestrictionForChannelMeasurements configured in CSI-ReportConfig and additionalPCIList configured in CSI-SSB-ResourceSet.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the the SSB#0 for Cell 1.

Table A.6.6.4.13.2-1: General test parameters

Table A.6.6.4.13.2-2: SSB specific test parameters

## A.6.6.4.13.3Test Requirements

The UE shall send a first PUCCH message using the new UCI type, no later than 20 ms plus X slot from the beginning of time period T2.

-X is 4 slots for Config 1 and 2.

-X is 8 slots for Config 3.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.6.4.14SSB based L1-RSRP measurement on SDL SCell for UE supporting LB CA via switching

## A.6.6.4.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting featureSetCombinationLowBandSwitching-r19 which is configured with LowBandCA-Switching-r19 makes correct reporting of L1-RSRP measurement on SDL SCell. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1. There are two cells in the test, the FR1 FDD PCell (Cell 1) and FR1 SDL SCell. The supported test configurations for NR PCell are shown in table Table A.6.6.4.14.1-1. Supported test configurations for NR SDL SCell are shown in table Table A.6.6.4.14.1-1A.

Table A.6.6.4.14.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for NR PCell

Table A.6.6.4.14.1-1A: Applicable NR configurations for FR1 SSB based L1-RSRP test for NR SLD SCell

## A.6.6.4.14.2Test parameters

The test parameters are given in table A.6.6.4.14.2-1 and table A.6.6.4.14.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically on the SDL SCell. The switching pattern is partially overlapped with SSBs resource occasions on SDL SCell. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs on the SDL SCell.

Table A.6.6.4.14.2-1: General test parameters

Table A.6.6.4.14.2-2: SSB specific test parameters on SDL SCell

## A.6.6.4.14.3Test Requirements

The UE shall send L1-RSRP report on SDL SCell every 40 slots. No later than 640 ms plus 40 slots from the beginning of time period T2, UE shall send L1-RSRP report on SDL SCell including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.4.15CSI-RS based L1-RSRP measurement when DRX is not used for SBFD aware UE with DU configuration

## A.6.6.4.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.6.6.4.15.1-1.

Table A.6.6.4.15.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.6.6.4.15.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.4.15.2-1 and table A.6.6.4.15.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot 0 of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.4.15.2-1. In the test, UE is configured to report L1-RSRP for SBFD symbols.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.6.6.4.15.2-1: General test parameters

Table A.6.6.4.15.2-2: CSI-RS specific test parameters

## A.6.6.4.15.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at the 8th slot from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for CSI-RS resource occasions on SBFD symbols only while meeting the absolute accuracy requirement in clause 10.1.19.2.1 and relative accuracy requirement in clause 10.1.19.2.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.5Inter-RAT UTRAN FDD measurements

## A.6.6.5.1SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1

## A.6.6.5.1.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT UTRAN FDD measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clause 9.4.6.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT UTRAN FDD neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.6.6.5.1.1-1. General test parameters are provided in table A.6.6.5.1.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.5.1.1-3 and A.6.6.5.1.1-4, respectively.

Table A.6.6.5.1.1-1: Supported test configurations in SA inter-RAT UTRAN FDD event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.5.1.1-2: General test parameters for SA inter-RAT UTRAN FDD event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.5.1.1-3: PCell specific test parameters for SA inter-RAT UTRAN FDD event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.5.1.1-4: UTRAN neighbour cell specific test parameters for SA inter-RAT UTRAN FDD event triggered reporting in non-DRX with PCell in FR1

## A.6.6.5.1.2Test Requirements

The UE shall send one Event B1 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 2.4 s from the start of period T2, i.e. when Cell 2 becomes detectable. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.6CLI measurements

## A.6.6.6.1SRS-RSRP measurement with DRX

## A.6.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SRS-RSRP measurement. This test will verify the SRS-RSRP measurement requirements in clause 9.7.2.5 with the testing configurations for NR cells in table A.6.6.6.1.1-1.

Table A.6.6.6.1.1-1: Applicable NR configurations for FR1 SRS-RSRP test

## A.6.6.6.1.2Test Parameters

One cell is deployed in the test, which is FR1 PCell (Cell 1). The test parameters for PCell is given in table A.6.6.6.1.2-1 and A.6.6.6.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system transmits SRS resource for measurement in the DL slot according to the SRS configuration in table A.6.6.6.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A. 6.6.6.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

Table A.6.6.6.1.2-1: General test parameters for SRS-RSRP event triggered reporting for PCell in FR1

Table A.6.6.6.1.2-2: NR Cell specific test parameters for SRS-RSRP event triggered reporting for PCell in FR1

Table A.6.6.6.1.2-3: NR Cell specific test parameters for SRS-RSRP event triggered reporting for neighbour cell UE

Table A.6.6.6.1.2-4: SRS configuration for measurement reporting

## A.6.6.6.1.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 1920 ms from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.6.2CLI-RSSI measurement with DRX

## A.6.6.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of CLI-RSSI measurement. This test will verify the CLI-RSSI measurement requirements in clause 9.7.3.5 with the testing configurations for NR cells in table A.6.6.6.2.1-1.

Table A.6.6.6.2.1-1: Applicable NR configurations for FR1 CLI-RSSI test

## A.6.6.6.2.2Test Parameters

One cell is deployed in the test, which are FR1 PCell (Cell 1). The test parameters for PCell is given in table A.6.6.6.2.2-1 and A.6.6.6.2.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI measurement resource and on 1 data symbol before. The CLI-RSSI measurement resource configuration is in table A.6.6.6.2.2-3.

Table A.6.6.6.2.2-1: General test parameters for CLI-RSSI event triggered reporting for PCell in FR1

Table A.6.6.6.2.2-2: NR Cell specific test parameters for CLI-RSSI event triggered reporting for PCell in FR1

Table A.6.6.6.2.2-3: CLI-RSSI measurement resource configuration for measurement reporting

## A.6.6.6.2.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 640 ms from the beginning of time period T2. The nominal RSSI used to evaluate the requirement shall be based on Io.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.7NR measurements with autonomous gaps

## A.6.6.7.1SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.6.6.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of intra-frequency CGI identification of an NR neighbour cell in FR1 with autonomous gaps. This test shall partly verify the measurement requirements in clause 9.11.

## A.6.6.7.1.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is an FR1 neighbour cell on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.7.1.1-2 and A.6.6.7.1.3-2 below. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable.  A measurement object is configured for the frequency of the PCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The UE is expected to detect and send a measurement report with Event A3.

A new RRC message triggering CGI identification shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying CGI identification is sent to the UE.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell during T3 untill a measurement report with CGI is sent.

Table A.6.6.71.1.2-1: Supported test configurations

Table A.6.6.7.1.2-2: General test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

Table A.6.6.7.1.2-3: NR Cell specific test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.6.6.7.1.3Test Requirements

The UE shall send a measurement report containing the CGI of Cell 2 within 255 ms from the start of time period T3.

Test requirement = RRC Procedure delay + Tidentify_CGI + TTI insertion uncertainty.

= 10 + 240 + 2 ms from the start of T3

= 252 ms, allow 255 ms

The UE shall be scheduled continuously throughout the test. From the start of T3 until 252 ms, the interruption on PCell shall not be more than the values specified for SA in clause 8.2.2.2.14.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.7.2Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA

## A.6.6.7.2.1Test Purpose and Environment

This test is to verify the requirement for identification of a new CGI of E-UTRA cell with autonomous gaps in NR SA in clause 9.4.7.

The test scenario comprises of one NR carrier and an E-UTRA carrier and two cells as given in tables A.6.6.7.2.1-1, A.6.6.7.2.1-2, A.6.6.7.2.1-3 and A.6.6.7.2.1-4. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would have ACK/NACK sending during identifying a new CGI of E-UTRAN cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report.

A RRC message implying SI reading shall be sent to the UE during period T2, after the UE has reported Event B2. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying SI reading is sent to the UE.

Table A.6.6.7.2.1-1: Supported test configurations of inter-RAT E-UTRAN cell using autonomous gap in SA

Table A.6.6.7.2.1-2: General test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA

Table A.6.6.7.2.1-3: PCell specific test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR

Table A.6.6.7.2.1-4: Cell specific test parameters for inter-RAT E-UTRAN cell for identification of a new CGI of E-UTRA cell using autonomous gaps

## A.6.6.7.2.2Test Requirements

The UE shall transmit a measurement report containing the cell global identifier of Cell 2 within 200 milliseconds from the start of T3.

Test requirement = RRC Procedure delay with additional margin + Tidentify_CGI,E-UTRAN + TTI insertion uncertainty.

= 15 + 30 + 150 + 2 ms from the start of T3

= 197 ms, allow 200 ms.

-The UE shall be scheduled continuously throughout the test, and from the start of T3 until 200 ms at least the number of ACK/NACK specified in NOTE 2 shall be detected as being transmitted by the UE.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE 1:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

NOTE 2:The overall ACK/NACK number is caused by two parts. Firstly, at least X ACK/NACK shall be sent during identifying the cell global identifier of Cell 2, where X is defined in table 8.2.2.2.15-1. Secondly, given that continuous DL data allocation, additional 43, 14 and 34 ACK/NACK shall be sent for FDD 15 kHz, TDD 15 kHz and TDD 30 kHz, respectively, from the start of T3 until 200 ms excludes 150 ms for identifying the cell global identifier of Cell 2.

## A.6.6.8L1-SINR measurement for beam reporting

## A.6.6.8.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used

## A.6.6.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.1, with the testing configurations for NR cells in table A.6.6.8.1.1-1.

Table A.6.6.8.1.1-1: Applicable NR configurations for FR1 CSI-RS based L1-SINR test

## A.6.6.8.1.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.8.1.2-1 and table A.6.6.8.1.2-2 below.

In the CSI-RS measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.6.6.8.1.2-1: General test parameters

Table A.6.6.8.1.2-2: CSI-RS specific test parameters

## A.6.6.8.1.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.27.1.1 and relative accuracy requirement in clause 10.1.27.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.8.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used

## A.6.6.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.2, with the testing configurations for NR cells in table A.6.6.8.2.1-1.

Table A.6.6.8.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.6.6.8.2.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.8.2.2-1 and table A.6.6.8.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.6.6.8.2.2-1: General test parameters

Table A.6.6.8.2.2-2: SSB specific test parameters

Table A.6.6.8.2.2-3: CSI-RS specific test parameters

## A.6.6.8.2.3Test Requirements

The UE shall send L1-SINR report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-SINR report including results of both SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 while meeting the accuracy requirement in clause 10.1.27.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.8.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used

## A.6.6.8.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR cofigured in clause 9.8.4.3, with the testing configurations for NR cells in table A.6.6.8.3.1-1.

Table A.6.6.8.3.1-1: Applicable NR configurations for FR1 L1-SINR test with CMR and dedicated IMR

## A.6.6.8.3.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.8.3.2-1 and table A.6.6.8.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-IM as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. UE is also configured to measure L1-SINR based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-IM as IMR.

Table A.6.6.8.3.2-1: General test parameters

A.6.6.8.3.2-2: CSI-RS specific test parameters

## A.6.6.8.3.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 as CMR + CSI-IM#0 as IMR and CSI-RS#1 as CMR + CSI-IM#1 as IMR while meeting the accuracy requirement in clause 10.1.27.3.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.8.4L1-SINR measurement with SSB based CMR and dedicated IMR for SSB adaptation

## A.6.6.8.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting ssb-BurstPeriodicityAdaptation-r19 makes correct reporting of L1-SINR measurement when SSB periodicity changes due to SSB adaptation. This test will verify the L1-SINR measurement requirements in clause 9.8.4.2 and 9.8.7, with the testing configurations for both NR FR1 PCell and NR FR1 SCells in table A.6.6.8.4.1-1.

Table A.6.6.8.4.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR for SSB adapatation

## A.6.6.8.4.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and FR1 SCell (Cell 2). The test parameters are given in table A.6.6.8.4.2-1 and table A.6.6.8.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources on SCell, and report periodically.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, NZP-CSI-RS resource configured as dedicated IMR is scheduled with the same periodicity as SSB configured as CMR (i.e., 80ms). At the beginning of T2, RRC reconfigures the periodicity of the CSI-RS resource configured as dedicated IMR (i.e., 20ms). At the beginning of T3, DCI format 2_9 that indicates a change in SSB burst periodicity of the SSB transmission on SCell is indicated. At the same time, the transmit power of the SSB as CMR on SCell is changed. The periodicity of SSB configured as CMR is the same as the periodicity of resource configured as dedicated IMR in T2. The transmit power of the CSI-RS resource configured as IMR on SCell is unchanged during T1, T2 and T3. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.6.6.8.4.2-1: General test parameters

Table A.6.6.8.4.2-2: SSB specific test parameters

Table A.6.6.8.4.2-3: CSI-RS specific test parameters

## A.6.6.8.4.3Test Requirements

During T1, the UE shall send L1-SINR report every 20 slots. At the beginning of T3, when UE receives DCI format 2_9 that indicates a change in SSB burst periodicity of the SSB transmission, UE shall send L1-SINR report every 20ms with a value distinct from the one reported during T1 from the first SSB burst after the time point as defined in TS 38.213 plus 2 ms, while meeting the accuracy requirement in clause 10.1.27.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.8.5L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD

## A.6.6.8.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement when UE supports sbfd-Aware-r19 and SBFD is configured by the network. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.2, with the testing configurations for NR cells in table A.6.6.8.5.1-1.

Table A.6.6.8.5.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.6.6.8.5.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.8.5.2-1 and table A.6.6.8.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.6.6.8.5.2-1: General test parameters

Table A.6.6.8.5.2-2: SSB specific test parameters

Table A.6.6.8.5.2-3: CSI-RS specific test parameters

## A.6.6.8.5.3Test Requirements

The UE shall send L1-SINR report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-SINR report including results of both SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 while meeting the accuracy requirement in clause 10.1.27.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.9Idle Mode CA/DC Measurements

## A.6.6.9.1SA Idle mode CA/DC measurement for FR1

## A.6.6.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the required measurements on the serving cell and the configured inter-frequency carrier for idle mode measurement reporting after the UE has entered Idle mode. This test will partly verify the Idle mode CA/DC measurements requirements in clause 4.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.9.1.1-1, A.6.6.9.1.1-2, A.6.6.9.1.1-3 and A.6.6.9.1.1-4.

The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE is connected to Cell 1 only and shall not have any timing information of Cell 2. UE is configured with early measurement reporting with channel 2. Beam level reporting for early measurements is not configured. The connection is released at the end of T1. T2 starts when the connection is released. During the time periods T2 UE is in Idle mode. At T3 the UE is paged for connection setup and requested by the network to send idle mode measurements.

Table A.6.6.9.1.1-1: supported test configuration

Table A.6.6.9.1.1-2: General test parameters for SA Idle mode CA/DC measurement for FR1

Table A.6.6.9.1.1-3: Cell specific test parameters for connected mode for SA Idle mode CA/DC measurement for FR1

Table A.6.6.9.1.1-4: Cell specific test parameters for idle mode for SA Idle mode CA/DC measurement for FR1

## A.6.6.9.1.2Test Requirements

The UE behaviour during time durations T2 and T3 shall be as follows:

During the time period T2 the UE is in Idle mode and the signal level of Cell 2 is changed. The UE shall not perform reselection. The UE shall perform Idle Mode CA measurement according to section 4.4.

At the start of T3 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for Cell 2. The UE shall send early measurement report to the PCell.

After receiving the requested early measurement report, the test equipment verifies the accuracy of measurement reported for Cell 2 meets the requirements in section 10.1.4B for SS-RSRP and in section 10.1.8B for SS-RSRQ and test ends.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.9.2Idle mode fast CA/DC eEMR measurement for FR1 without valid reporting

## A.6.6.9.2.1Test Purpose and Environment

The purpose of this test is to verify UE measurement reporting behaviour as specified in clause 4.7 when the UE supports measValidationReportEMR-r18. This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7 when measIdleValidityDuration-r18 is configured for the test case when there are no measurement results to report at RRC connection setup.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as inter-frequency neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.9.2.1-1, A.6.6.9.2.1-2, A.6.6.9.2.1-3.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During T1, the UE is connected to Cell 1 only and shall not have any timing information of Cell 2. UE is configured with early measurement reporting for Cell 2 in measIdleCarrierListNR-r16. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. Signal level of Cell 2 is set to the value given in table A.6.6.9.2.1-3. The time when T331 timer expires defines the ending point of T2.

At the beginning of T3, the signal level of the neighbour cell is set to turned off.  The duration of the T3 equals to measIdleValidityDuration-r18.

The time when TE sends the paging message is defined as the starting point of T4. During T4, in this test the UE shall not send measurement report.

Table A.6.6.9.2.1-1: supported test configuration

Table A.6.6.9.2.1-2: General test parameters for Idle mode fast CA/DC eEMR measurement for FR1

Table A.6.6.9.2.1-3: Cell specific test parameters for Idle and connected mode for fast CA/DC eEMR measurement for FR1

## A.6.6.9.2.2Test Requirements

During the period T2 and T3, the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for Cell 2.

The UE shall NOT send early measurement report to the PCell in this test.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.9.3Idle mode fast CA/DC cell reselection measurement for FR1 without valid reporting

## A.6.6.9.3.1Test Purpose and Environment

The purpose of this test is to verify UE measurement reporting behaviour as specified in clause 4.7 when the UE supports measValidationReportReselectionMeasurements-r18. This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7 when  measReselectionValidityDuration-r18 is configured for the test case when there are no measurement results to report at RRC connection setup.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as inter-frequency neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.9.3.1-1, A.6.6.9.3.1-2, A.6.6.9.3.1-3.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During T1, the UE is connected to Cell 1 only and shall not have any timing information of Cell 2. UE is configured with inter-frequency measurement reporting for Cell 2 in MeasReselectionCarrierListNR-r18. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. Signal level of Cell 2 is set to the value given in table A.6.6.9.3.1-3. The duration of T2 is set to fixed value according to the Table A.6.6.9.3.1-2.

At the beginning of T3, the signal level of Cell 2 is set to turned off. The duration of the T3 equals to measReselectionValidityDuration-r18.

The time when TE sends the paging message defined as the starting point of T4. During T4, in this test the UE shall not send measurement report.

Table A.6.6.9.3.1-1: supported test configuration

Table A.6.6.9.3.1-2: General test parameters for Idle mode fast CA/DC cell-reselection measurement for FR1

Table A.6.6.9.3.1-3: Cell specific test parameters for Idle and connected mode for fast CA/DC cell re-selection measurement for FR1

## A.6.6.9.3.2Test Requirements

During the period T2 and T3, the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for Cell 2.

The UE shall NOT send early measurement report to the PCell in this test.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.9.4Idle mode fast CA/DC cell reselection measurement for FR1 with valid reporting

## A.6.6.9.4.1Test Purpose and Environment

The purpose of this test is to verify UE measurement reporting behaviour as specified in clause 4.7 when the UE supports measValidationReportReselectionMeasurements-r18 . This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7 when measReselectionValidityDuration-r18 is configured for the test case when there are measurement results to report at RRC connection setup.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.6.6.9.4.1-1, A.6.6.9.4.1-2, A.6.6.9.4.1-3.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During T1, the UE is connected to Cell 1 only and shall not have any timing information of Cell 2. UE is configured with inter-frequency measurement reporting for Cell 2 in MeasReselectionCarrierListNR-r18. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. Signal level of Cell 2 is set to the value given in table A.6.6.9.4.1-3. The duration of T2 is set to fixed value according to the Table A.6.6.9.4.1-2.

At the beginning of T3, the signal level of Cell 2 is set to another value according to the Table A.6.6.9.4.1-3. The duration of T3 equals to measReselectionValidityDuration-r18 .

The time when TE sends the paging message is defined as the starting point of T4. During T4, in this test the UE shall send measurement report within the duration of T4.

Table A.6.6.9.4.1-1: supported test configuration

Table A.6.6.9.4.1-2: General test parameters for Idle mode fast CA/DC cell-reselection measurement for FR1

Table A.6.6.9.4.1-3: Cell specific test parameters for Idle and connected mode for fast CA/DC cell re-selection measurement for FR1

## A.6.6.9.4.2Test Requirements

During the period T2 and T3 the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for Cell 2.

The UE shall send early measurement report to the PCell with valid measurement results.

After receiving the requested early measurement report, the test equipment verifies the accuracy of measurement reported for Cell 2 meets the requirements in section 10.1.4B for SS-RSRP and in section 10.1.8B for SS-RSRQ and test ends. In the test case, the reported measurements are considered valid if they fulfil measurement accuracy requirements according to Cell 2 signal level during T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.9.5SA Idle mode CA/DC measurement for FR1 with 12RB SSB

## A.6.6.9.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the required measurements on the serving cell and the configured inter-frequency carrier for idle mode measurement reporting after the UE has entered Idle mode, with 12 RB SSB on the target carrier. This test will partly verify the Idle mode CA/DC measurements requirements in clause 4.4.

The test environment in clause A.6.6.9.1.1 apply to this test, except that beam level reporting for early measurements is configured. Supported test configuration is given in table A.6.6.9.5.1-1. General test parameters as specified in table A.6.6.9.1.1-2 with config 1 apply to this test. Cell specific test parameters as specified in table A.6.6.9.1.1-3 with config 1 apply to this test, except those specified in table A.6.6.9.5.1-2.

Table A.6.6.9.5.1-1: supported test configuration

Table A.6.6.9.5.1-2: Cell specific test parameters for connected mode for SA Idle mode CA/DC measurement for FR1

## A.6.6.9.5.2Test Requirements

The test requirements in clause A.6.6.9.1.2 apply to this test.

## A.6.6.10CSI-RS based intra-frequency Measurements

## A.6.6.10.1SA event triggered reporting tests without gap under non-DRX

## A.6.6.10.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA CSI-RS based L3 intra-frequency requirements in clauses 9.10.2.

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.10.1.1-1 and A.6.6.10.1.1-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.10.1.1-1: Supported test configurations

Table A.6.6.10.1.1-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.10.1.1-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.10.1.2Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.11CSI-RS based inter-frequency Measurements

## A.6.6.11.1 SA event triggered reporting tests with gap under DRX

## A.6.6.11.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA CSI-RS based L3 inter-frequency measurement requirements in clause 9.10.3.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.6.6.11.1.1-1, A.6.6.11.1.1-2 and A.6.6.11.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.6.6.11.1.1-2 is provided for UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #4 as defined in table A.6.6.11.1.1-2 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #4, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE is allocated with PUSCH resource at every DRX cycle.

NOTE:TAT= infinite based on the DRX configuration used in test.

Table A.6.6.11.1.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.11.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1

Table A.6.6.11.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.6.6.11.1.2Test Requirements

In test 1 with per-UE gap and test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 20480 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

The UE is required to read the SSB index indicated by associatedSSB in the neighbour cell in this test

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.12RSTD measurements

## A.6.6.12.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA

## A.6.6.12.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.6.12.1.1-1.

Table A.6.6.12.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.6.6.12.1.1-2, and cell specific test parameters are listed in table A.6.6.12.1.1-3.

Table A.6.6.12.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.1.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049

## A.6.6.12.2NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA

## A.6.6.12.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when dual positioning frequency layers are configured.

The supported test configurations are specified in table A.6.6.12.2.1-1.

Table A.6.6.12.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. Cell 3 is on a different RF channel with Cell 1 and Cell 2.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.6.6.12.2.1-2, and cell specific test parameters are listed in table A.6.6.12.2.1-3.

Table A.6.6.12.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.6.6.12.3NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR1 SA

## A.6.6.12.3.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement with the reduced samples meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.6.12.3.1-1.

Table A.6.6.12.3.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.6.6.12.3.1-2, and cell specific test parameters are listed in table A.6.6.12.3.1-3.

Table A.6.6.12.3.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.3.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.3.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.3.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration X1 specified in section 9.9.2.5 starting from the beginning of time interval T2, where X1 is 320 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.6.6.12.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA without measurement gap

## A.6.6.12.4.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the gapless RSTD measurement period requirement specified in clause 9.9.2.7 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured. Reporting delay test for gapless PRS measurement is conducted assuming that the PRS has higher priority, i.e., state 1, than all other DL signals/channels and is transmitted within active DL BWP of UE. Two sub-tests are defined, sub-test 1 is for Nsample = 4 and sub-test 2 is for Nsample = 1. For sub-test 2 LMF indicates UE to perform PRS measurement with Nsample = 1. The cell specific parameters for sub-test 1 and sub-test 2 are defined in table A.6.6.12.4.1-4.

The supported test configurations are specified in table A.6.6.12.4.1-1.

Table A.6.6.12.4.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first PPW instance containing the PRS resources.

The UE is configured with PPW before start of T2.

The general test parameters are listed in table A.6.6.12.4.1-2, and cell specific test parameters are listed in table A.6.6.12.4.1-3.

Table A.6.6.12.4.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.4.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.4.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.4.2Test Requirements

The RSTD measurement time fulfils the gapless RSTD measurement period requirements specified in clause 9.9.2.7.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.2.7 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.6.6.12.5NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state with Rx TEG

## A.6.6.12.5.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the Rx TEG based measurement period requirements specified in clause 9.9.2.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.6.12.5.1-1.

Table A.6.6.12.5.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The test applies to the UE supporting Rx TEG indicated via NR-UE-TEG-Capability and is requested to provide the Rx TEG in the test via nr-UE-RxTEG-Request-r17 in NR-TDOA-RequestLocationInformation. In the location request measureSameDL-PRS-ResourceWithDifferentRxTEGs-r17 is set to n0. The UE shall perform and optionally report the Rx TEG based RSTD measurements.

The general test parameters are listed in table A.6.6.12.5.1-2, and cell specific test parameters are listed in table A.6.6.12.5.1-3.

Table A.6.6.12.5.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.5.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.5.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.5.2Test Requirements

The RSTD measurement time fulfils the Rx TEG based RSTD measurement period requirements specified in clause 9.9.2.5. The UE shall perform and report the Rx TEG based RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.6.6.12.6NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode

## A.6.6.12.6.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement by aggregating PRS resources from two positioning frequency layers (PFLs) meets the measurement period requirements specified in clause 9.9.2.10 in an environment with AWGN propagation conditions in FR1.

The supported test configurations are specified in table A.6.6.12.6.1-1.

Table A.6.6.12.6.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, all cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS resources on two positioning frequency layers during T2.

Note:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. The UE is capable of performing RSTD measurements by aggregating PRS resources from two PFLs and is configured by the LMF to perform measurements by aggregating the PRS resources from two positioning frequency layers via nr-DL-PRS-JointMeasurementRequestedPFL-List. The NR-DL-TDOA-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first measurement gap instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or measurement gap pattern ID # 0 before T2.

The general test parameters are listed in table A.6.6.12.6.1-2, and cell specific test parameters are listed in table A.6.6.12.6.1-3.

Table A.6.6.12.6.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.12.6.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.6.12.6.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.6.12.6.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.10.

The UE shall perform and report the RSTD measurements by aggregating PRS resources from multiple positioning frequency layers for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.2.10 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.3, i.e., between RSTD_000000000 and RSTD_126083073.

## A.6.6.13 PRS-RSRP measurements

## A.6.6.13.1PRS-RSRP reporting delay test case for single positioning frequency layer

## A.6.6.13.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements specified in clause 9.9.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.6.13.1.1-1.

Table A.6.6.13.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.13.1.1-2, and cell specific test parameters are listed in table A.6.6.13.1.1-3.

Table A.6.6.13.1.1-2: General test parameters

Table A.6.6.13.1.1-3: Cell specific test parameters

## A.6.6.13.1.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time limit above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.13.2PRS-RSRP reporting delay test case for dual positioning frequency layer

## A.6.6.13.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements specified in clause 9.9.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.6.13.2.1-1.

Table A.6.6.13.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell on NR RF channel #1 in FR1. Cell 2 is a neighbour cell on a different NR RF channel #2 in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.13.2.1-2, and cell specific test parameters are listed in table A.6.6.13.2.1-3.

Table A.6.6.13.2.1-2: General test parameters

Table A.6.6.13.2.1-3: Cell specific test parameters

## A.6.6.13.2.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time limit above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.13.3PRS-RSRP reporting delay test case for reduced number of samples

## A.6.6.13.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements for reduced number of samples specified in clause 9.9.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.6.13.3.1-1.

Table A.6.6.13.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.13.3.1-2, and cell specific test parameters are listed in table A.6.6.13.3.1-3.

Table A.6.6.13.3.1-2: General test parameters

Table A.6.6.13.3.1-3: Cell specific test parameters

## A.6.6.13.3.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit for reduced number of samples specified in clause 9.9.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.13.4PRS-RSRP reporting delay test case for single positioning frequency layer outside MG

## A.6.6.13.4.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement outside MG meets the delay requirements specified in clause 9.9.3.6 in an environment with AWGN propagation conditions. There are two sub-tests in the test, sub-test 1 is to verify the delay requirements with Nsample=1, and sub-test 2 is to verify the delay requirements with Nsample=4.

The supported test configurations are specified in table A.6.6.13.4.1-1.

Table A.6.6.13.4.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In sub-test 1, reducedDL-PRS-ProcessingSamples shall be included in the location information request and set to ‘requested’.

During T1, a PPW shall be configured for the PCell and be activated via DL MAC CE. The last PDSCH containing the MAC CE shall be transmitted before slot #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first PPW instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.13.4.1-2, and cell specific test parameters during T2 are listed in table A.6.6.13.4.1-3.

Table A.6.6.13.4.1-2: General test parameters

Table A.6.6.13.4.1-3: Cell specific test parameters during T2

A.6.6.13.4.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.3.6, starting from the beginning of time interval T2, with Nsample=1 for sub-test 1 and Nsample=4 for sub-test 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.14UE Rx-Tx time difference measurements

## A.6.6.14.1UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA

## A.6.6.14.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.6.14.1.1-1.

Table A.6.6.14.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.1.1-2 and table A.6.6.14.1.1-3 respectively.

Table A.6.6.14.1.1-2: General test parameters

Table A.6.6.14.1.1-3: Cell specific test parameters

Table A.6.6.14.1.1-4: Void

## A.6.6.14.1.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.6.14.2UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA

## A.6.6.14.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR1 in standalone scenario when dual positioning frequency layers are configured.

The supported test configurations in listed in table A.6.6.9.2.1-1.

Table A.6.6.14.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Cell 1 and Cell 2 are on different RF channels in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.2.1-2 and table A.6.6.14.2.1-3 respectively.

Table A.6.6.14.2.1-2: General test parameters

Table A.6.6.14.2.1-3: Cell specific test parameters

Table A.6.6.14.2.1-4: Void

## A.6.6.14.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.6.14.3UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with reduced sample number

## A.6.6.14.3.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 with Nsample = 1 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.6.14.3.1-1.

Table A.6.6.14.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. reducedDL-PRS-ProcessingSamples shall be included in the location information request and set to ‘requested’. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.3.1-2 and table A.6.6.14.3.1-3 respectively.

Table A.6.6.14.3.1-2: General test parameters

Table A.6.6.14.3.1-3: Cell specific test parameters

## A.6.6.14.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5 with Nsample=1.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.6.14.4UE Rx-Tx time difference measurement without gaps in FR1 SA

## A.6.6.14.4.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.6 in AWGN propagation condition in FR1 in standalone scenario. There are two sub-tests in the test, sub-test 1 is to verify the delay requirements with Nsample=1, and sub-test 2 is to verify the delay requirements with Nsample=4.

The supported test configurations in listed in table A.6.6.14.4.1-1.

Table A.6.6.14.4.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of PRS processing window containing the PRS resources.

The UE is configured with PRS processing window before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.4.1-2 and table A.6.6.14.4.1-3 respectively.

Table A.6.6.14.4.1-2: General test parameters

Table A.6.6.14.4.1-3: Cell specific test parameters

## A.6.6.14.4.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.6.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.6.14.5UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with multiple RxTx TEGs

## A.6.6.14.4.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured, and when UE is requested to measure a PRS resource with multiple RxTx TEGs.

The supported test configurations in listed in table A.6.6.14.4.1-1.

Table A.6.6.14.4.11: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request. In nr-Multi-RTT-RequestLocationInformation, measureSameDL-PRS-ResourceWithDifferentRxTEGs-r17 shall be set to ‘n2’.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.4.1-2 and table A.6.6.14.4.1-3 respectively.

Table A.6.6.14.4.1-2: General test parameters

Table A.6.6.14.4.1-3: Cell specific test parameters

## A.6.6.14.4.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5, with =2 if UE does not support or indicate value ‘n1’ for measureSameDL-PRS-ResourceWithDifferentRxTEGsSimul, and  =1 otherwise.kmultiTEGkmultiTEG

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.6.14.6UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA

## A.6.6.14.6.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 9.9.4.9 for UE Rx-Tx measurements with PRS bandwidth aggregation. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR1.

The supported test configurations are listed in table A.6.6.14.6.1-1.

Table A.6.6.14.6.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The general test parameters and cell specific test parameters are as given in table A.6.6.14.6.1-2 and table A.6.6.14.6.1-3, respectively.

Table A.6.6.14.6.1-2: General test parameters

Table A.6.6.14.6.1-3: Cell specific test parameters

## A.6.6.14.6.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.9.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25A.3.

## A.6.6.15Idle Mode measurements of inter-RAT DC candidate cells for early reporting

## A.6.6.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly retains the detected cell status for the idle mode CA/DC measurement when UE transitions from RRC Connected mode to Idle mode, when the UE has entered Idle mode. Additionally, test that the UE performs the required measurements on the serving cell and the configured inter-RAT carrier for idle mode measurement reporting. This test will partly verify the Idle mode CA measurements in clause 4.4. In the test, connected mode DRX configuration is not configured in either PCell or PSCell.

Additionally, the purpose of this test is to verify that the SS-RSRP, SS-RSRQ, RSRP and RSRQ measurement accuracy is within the specified limits. This test will verify the accuracy requirements in sections 10.1.2B and 10.1.7B for intra-frequency measurements and section 10.2.2 and 10.2.3 for the inter-RAT measurements for the supported test configurations in tables A.6.6.15.1-4 and A.6.6.15.1-5.

The supported test configurations are given in table A.6.6.15.1-1. The test parameters are given in tables A.6.6.15.1-2, A.6.6.15.1-3, A.6.6.15.1-4 and A.6.6.15.1-5 below. In the test there are two cells, Cell 1, which is the PCell in connected, and serving cell in idle mode, on radio channel 1 in FR1, and Cell 2, which is the PSCell in connected, and measured LTE inter-RAT cell in idle mode, on radio channel 2 in LTE.

For the purpose of testing absolute accuracy in idle mode in this set of test cases the cells in idle mode are on different carrier frequencies (NR FR1 and LTE).  The absolute accuracy of RSRP and RSRQ inter-RAT measurements are tested by using the parameters in table A.6.6.15.1-4 and table A.6.6.15.1-5. In all test cases, Cell 1 is the serving and Cell 2 the target cell.

The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. During T1 Cell 2, the PSCell, shall be configured.

Time duration T2 starts when UE has transmitted random access preamble on the PSCell. During T2, the UE is configured with idle mode CA measurements with the PSCell carrier as the target carrier. The connection is released 500 ms after T2 when the UE has sent random access preamble on the PSCell.

T3 starts when the connection is released. During the time periods T3 and T4 the UE is in Idle mode with the serving cell on the FR1 carrier. The UE is configured to perform inter-RAT idle mode CA/DC measurements on Cell 2 carrier. After the connection release and during T3, 1000 ms after T3 is started, the signal level of the inter-RAT carrier configured for idle mode CA/DC measurements is changed at which time T4 starts. T5 starts 65 s after T4, when the UE is paged for connection setup and UE is requested by the network to report idle mode CA/DC measurements.

Table A.6.6.15.1-1: Supported test configurations for Idle Mode measurements of inter-RAT DC candidate cells for early reporting

Table A.6.6.15.1-2: General test parameters for Idle Mode measurements of inter-RAT DC candidate cells for early reporting

Table A.6.6.15.1-3: Cell specific test parameters for NR cell for Idle Mode measurements of inter-RAT DC candidate cells for early reporting

Table A.6.6.15.1-4: Cell specific test parameters for LTE cell for Idle Mode measurements of inter-RAT DC candidate cells for early reporting

Table A.6.6.15.1-5: General idle mode test parameters for Idle Mode measurements of inter-RAT DC candidate cells for early reporting

## A.6.6.15.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During time durations T1 the UE shall start transmitting preamble on PSCell. During T2 the UE perform intra-frequency measurements on the PCell and the PSCell.

During the time-period T3 the connection is released, and UE enters idle mode. During the time period T3 and T4 the UE is camped in Idle mode and at T4 the signal level of Cell 2 is changed. The UE shall not perform reselection. The UE shall perform Idle Mode CA measurement according to section 4.4.

At the start of T5 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report. The UE shall send early measurement report to the PCell including idle mode CA/DC measurement from Cell 2.

After receiving the requested early measurement report, the test equipment verifies that the accuracy of measurement reported for serving Cell 1 and Cell 2 meets the requirements in sections 10.1.2B and 10.1.7B and sections 10.2.4 and 10.2.5, respectively and test ends.

## A.6.6.16PRS-RSRPP measurements

## A.6.6.16.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state

## A.6.6.16.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the delay requirements specified in clause 9.9.6.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.6.16.1.1-1.

Table A.6.6.16.1.11: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.16.1.1-2, and cell specific test parameters are listed in table A.6.6.16.1.1-3.

Table A.6.6.16.1.1-2: General test parameters

Table A.6.6.16.1.1-3: Cell specific test parameters

## A.6.6.16.1.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.6.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.16.2PRS-RSRPP reporting delay test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state

## A.6.6.16.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the reduced sample measurement delay requirements specified in clause 9.9.6.5 in an environment with AWGN propagation conditions for reduced number of samples. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-CONNECTED is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.6.6.16.2.1-1.

Table A.6.6.16.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.6.16.2.1-2, and cell specific test parameters are listed in table A.6.6.16.2.1-3.

Table A.6.6.16.2.1-2: General test parameters

Table A.6.6.16.2.1-3: Cell specific test parameters

## A.6.6.16.2.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.6.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.16.3PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state without measurement gap

## A.6.6.16.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the delay requirements specified in clause 9.9.6.6 in an environment with AWGN propagation conditions. Reporting delay test for gapless PRS measurement is conducted assuming that the PRS has higher priority, i.e., state 1, than all other DL signals/channels and is transmitted within active DL BWP of UE. Two sub-tests are defined, sub-test 1 is for Nsample = 4 and sub-test 2 is for Nsample = 1. For sub-test 2 LMF indicates UE to perform PRS measurement with reduced number of samples  via reducedDL-PRS-ProcessingSamples. The cell specific parameters for sub-test 1 and sub-test 2 are defined in table A.6.6.16.3.1-3.NsampleNsample

The supported test configurations are specified in table A.6.6.16.3.1-1.

Table A.6.6.16.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first PRS processing window instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured with PPW before start of T2.

The general test parameters are listed in table A.6.6.16.3.1-2, and cell specific test parameters are listed in table A.6.6.16.3.1-3.

Table A.6.6.16.3.1-2: General test parameters

Table A.6.6.16.3.1-3: Cell specific test parameters T2

## A.6.6.16.3.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.6.6, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.17SA event triggered reporting tests with Pre-MG

## A.6.6.17.1SA event triggered reporting tests with autonomous activation/deactivation Pre-MG

## A.6.6.17.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3. And this test will also jointly verify Pre-configured measurement gap activation/deactivation delay in clause 8.19.2.

## A.6.6.17.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.17.1.2-1 and A.6.6.17.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

During the duration of T1,

-UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

-BWP-1 includes bandwidth of the initial DL BWP and SSB. UE is expected to deactivate the Pre-MG when this BWP is active.

-BWP-2 does not include bandwidth of the initial DL BWP and SSB. UE is expected to activate the Pre-MG when this BWP is active.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

-At the start of time duration T2, the serving gNB can trigger Pre-MG activation starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2. And UE is expected to complete the Pre-MG activation within T2.

-At the start of time duration T3, the UE may not have any timing information of neighbor cell to be measured (e.g. Cell 2). And UE was expected to complete the measurements of SSBs with the activated Pre-MG within T3.

There are two BWPs configured in Cell 1, BWP-1 which contains the cell defining SSB, and BWP-2 which does not contain any SSB of Cell 1.

Table A.6.6.17.1.2-1: Supported test configurations

Table A.6.6.17.1.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

Table A.6.6.17.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

## A.6.6.17.1.3Test Requirements

During T1 the UE shall report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions, starting from the 1 st complete Pre-MG occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) + 5 ms as defined in clause 8.19.2.

During T3, the UE shall NOT be able to receive PDSCH and report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T3.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.17.2SA event triggered reporting tests with pre-configured measurement gaps and network-controlled activation/deactivation

## A.6.6.17.2.1Test purpose and Environment

The purpose of this test is to verify that the UE correctly activates and deactivates the pre-MG and makes correct measurement and reporting of an event with activated and deactivated pre-MG. This test will partly verify the pre-MG activation and deactivation delay requirements in clause 8.19.2 and the intra-frequency cell search requirements in clause 9.2.6.2 and 9.3.4.

## A.6.6.17.2.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The supported test configurations are listed in table A.6.6.17.2.2-1, general test parameters are listed in table A.6.6.17.2.2-2, and cell specific test parameters are listed in table A.6.6.17.2.2-3.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. A pre-MG is configured before the test.

The UE is configured with 2 dedicated BWPs, BWP-1 and BWP-2. BWP-1 includes bandwidth of the SSB, and preConfGapStatus for BWP-1 is set to ‘0’; BWP-2 does not include bandwidth of the SSB, and preConfGapStatus for BWP-2 is set to ‘1’.

The test consists of 3 successive time periods, with time duration of T1, T2, and T3 respectively. Before the test starts, UE is switched to BWP-1.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2 and complete pre-MG activation during T2.

During T3, UE shall perform intra-frequency measurement with pre-MG activated.

During time duration T1 and T2, the UE shall not have any timing information of Cell 2.

Table A.6.6.17.2.2-1: Supported test configurations

Table A.6.6.17.2.2-2: General test parameters for SA intra-frequency event triggered reporting with with pre-configured measurement gaps and network-controlled activation/deactivation

Table A.6.6.17.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with with pre-configured measurement gaps and network-controlled activation/deactivation

## A.6.6.17.2.3Test Requirements

During T1, UE shall report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots overlapped with the pre-MG occasions.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T3. During T3, UE is not required to report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots overlapped with the pre-MG occasions.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.17.3Void

## A.6.6.17.3.1Void

## A.6.6.17.3.2Void

## A.6.6.17.3.3Void

## A.6.6.18SA event triggered reporting tests with concurrent gaps

## A.6.6.18.1SA event triggered reporting tests for FR1 concurrent gaps with non-overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.18.1.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gaps capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR cell 3 as neighbour cell in FR1 on NR RF channel 3.  The test parameters are given in tables A.6.6.18.1.1-1, A.6.6.18.1.1-2 and A.6.6.18.1.1-3.

Two measurement gap patterns (MeasGapId #1 and MeasGapId #2) are configured with the gap pattern ID #0 and #1 as defined in table A.6.6.18.1.1-2. MeasGapId #2 is configured with a higher priority than MeasGapId #1. MeasGapId #1 and MeasGapId #2 are associated with the MOs for RF channel numbers #2 and #3, respectively.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used for both frequency layers. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR cell 3.

Table A.6.6.18.1.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.18.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gaps with fully non-overalpping scenario for SSB-based measurements in both inter-frequency layers

Table A.6.6.18.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gaps with fully non-overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.18.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than 920 ms for Cell 2 and 1280 ms for cell 3 from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.18.2SA event triggered reporting tests for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.18.2.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gap capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR cell 3 as neighbour cell in FR1 on NR RF channel 3.  The test parameters are given in tables A.6.6.18.2.1-1, A.6.6.18.2.1-2 and A.6.6.18.2.1-3. The TE schedules continuous DL data on PCell throughout the test.

Two measurement gap patterns (MeasGapId #1 and MeasGapId #2) are configured with the gap pattern ID #0 and #1 as defined in table A.6.6.18.2.1-2. MeasGapId #2 is configured with a higher priority than MeasGapId #1. MeasGapId #1 and MeasGapId #2 are associated with the MOs for RF channel numbers #2 and #3, respectively.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used for both frequency layers. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR cell 3.

Table A.6.6.18.2.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.18.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers

Table A.6.6.18.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gap with partially-partial overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.18.2.2Test Requirements

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.18.3SA NR - E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in FR1

## A.6.6.18.3.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of concurrent inter-RAT E-UTRAN and NR FR1 measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2, 9.4.3, 9.3.4 and 9.3.5.

In each test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the NR PCell, Cell 2 is an Inter-frequency NR FR1 neighbour cell on NR RF channel 2 and Cell 3 is an inter-RAT E-UTRAN neighbour cell on LTE RF channel 3.

In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used for the E-UTRAN cell (cell 3). In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used for the NR FR1 cell (Cell 2).

Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2 and Cell 3.

In the test two concurrent per-UE measurement gap pattern configurations # 0 as defined in table A.6.6.18.3.1-2 are provided for a UE. Two measurement gap patterns (MeasGapId #1 and MeasGapId #2) are configured with the gap pattern ID #1 as defined in table A.6.6.18.3.1-2. MeasGapId #2 is configured with a higher priority than MeasGapId #1. MeasGapId #1 and MeasGapId #2 are associated with the MOs for NR RF channel numbers #2 and LTE RF channel #3, respectively.

Supported test configurations are shown in table A.6.6.18.3.1-1. General test parameters are provided in table A.6.6.18.3.1-2 below. Test parameters for Cell 1, Cell 2 and Cell 3, valid for both time duration T1 and T2, are provided in tables A.6.6.18.3.1-3 and A.6.6.18.3.1-4, respectively.

The test parameters and configurations are given in tables A.6.6.18.3.1-1, A.6.6.18.3.1-2, and A.6.6.18.3.1-3.

Table A.6.6.18.3.1-1: Supported test configurations in SA concurrent inter-RAT E-UTRAN and NR FR1 inter-frequency event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.18.3.1-2: General test parameters for SA concurrent inter-RAT E-UTRAN and NR FR1 inter-frequency event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.18.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.18.3.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.18.3.2Test Requirements

In this test with per-UE gap, the UE shall send one Event A4 triggered measurement report for Cell 2, with a measurement reporting delay less than 1280ms from the beginning of time period T2.

The UE shall send one Event B2 triggered measurement report for Cell 3 to the PCell, with a measurement reporting delay less than 7.68s from the start of period T2.

The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.18.4SA event triggered reporting tests for PRS and SSB measurement in FR1 without SSB time index detection when DRX is not used

## A.6.6.18.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA NR measurements with concurrent gaps requirements in clause 9.2.6(when one of concurrent gaps in same frequency layer of serving cells), 9.3.6(when one of concurrent gaps in the different frequency layer of serving cells) and 9.9.2(when one of concurrent gaps used for PRS measurement).

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR1 on NR RF channel 2 and NR cell 3 as neighbor cell in FR1 on NR RF channel 1.  The test parameters are given in tables A.6.6.18.4.1-1, A.6.6.18.4.1-2 and A.6.6.18.4.1-3.

Two measurement gap patterns (MeasGapId #1 and MeasGapId #2) are configured with the gap pattern ID #0 and #24 as defined in table A.6.6.18.4.1-2. MeasGapId #2 is configured with a higher priority than MeasGapId #1. MeasGapId #1 is associated with the MOs for RF channel numbers #2 and MeasGapId #2 is associated with the PRS measurement for RF channel numbers #1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR cell 3. Cell 1 and cell 3 transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance of MeasGapId #2 containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

Table A.6.6.18.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.18.4.1-2: General test parameters for SA inter-frequency event triggered reporting for concurrent gaps with partially partial overalpping scenario for SSB-based measurements and PRS measurement

Table A.6.6.18.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gap with partially-partial overalpping scenario for SSB-based measurements and PRS measurement

## A.6.6.18.4.2Test Requirements

The UE shall send one Event A3 triggered measurement report for Cell 2, with a measurement reporting delay less than 1280ms  from the beginning of time period T2.

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 3 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in section 9.9.3.5 starting from the beginning of time interval T2.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

IUE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.19SA event triggered reporting tests with NCSG

## A.6.6.19.1SA event triggered reporting tests with NCSG under non-DRX in FR1

## A.6.6.19.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.7.1 and 9.2.7.2, and also verify the scheduling availability during intra-frequency measurement with NCSG in clause 9.2.7.3.

The serving frequency should be selected for which UE reports ‘ncsg’.

## A.6.6.19.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.19.1.2-1, A.6.6.19.1.2-2 and A.6.6.19.1.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

During T2, the UE is continuously scheduled with data on the PCell.

The UE is capable of NCSG and report ‘ncsg’ through NeedForGapNCSG-InfoNR for PCell.

NCSG pattern configuration # 0 as defined in table A.6.6.19.1.2-2 is provided for UE regardless of UE capable or incapable of supporting per-FR NCSG.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.6.6.19.1.2-1: Supported test configurations

Table A.6.6.19.1.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

Table A.6.6.19.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with NCSG for PCell in FR1

## A.6.6.19.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

During T2, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.19.2SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement

## A.6.6.19.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.10.

The serving frequency and the target frequency should be selected such that UE reports ‘ncsg’ for the target frequency given the serving frequency.

## A.6.6.19.2.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. NR RF channel 1 and NR RF channel 2 should be selected such that UE reports ‘ncsg’ for the target frequency on NR RF channel 2.

The test parameters are given in tables A.6.6.19.2.2-1, A.6.6.19.2.2-2 and A.6.6.19.2.2-3.

NCSG pattern configuration # 0 as defined in table A.6.6.19.2.2-2 is provided for UE regardless of UE capable or incapable of supporting per-FR NCSG.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

During T2, the UE is continuously scheduled with data on the PCell.

Table A.6.6.19.2.2-1: SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement

Table A.6.6.19.2.2-2: General test parameters for event triggered reporting for FR1 with NCSG for inter-frequency measurement

Table A.6.6.19.2.2-3: Cell specific test parameters for SA event triggered reporting for FR1 with NCSG for inter-frequency measurement

## A.6.6.19.2.3Test Requirements

In test 1 and 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

During T2, UE shall send HARQ-ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern.

The rate of correct events observed during repeated tests shall be at least 90%.

In test 1 and 2, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.19.3SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 with NCSG

## A.6.6.19.3.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements based on NCSG when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3.

The serving frequency and the target frequency should be selected such that UE reports ‘ncsg’ for the target frequency given the serving frequency.

## A.6.6.19.3.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.6.6.19.3.2-1. General test parameters are provided in table A.6.6.19.3.2-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.19.3.2-3 and A.6.6.19.3.2-4, respectively.

Table A.6.6.19.3.2-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.19.3.2-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.19.3.2-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.19.3.2-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.19.3.3Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

During T2, UE shall send HARQ-ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.19.4Event triggered reporting on SCC with deactivated SCell test with per-UE NCSG under non-DRX

## A.6.6.19.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the cell search requirements on SCC with deactivated SCell in clauses 9.2.7.1 and 9.2.7.2.

## A.6.6.19.4.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), FR1 SCell (Cell 2) and FR1 neighbour cell (Cell 3) on the same frequency as the SCell. The SCell is deactivated during the test. The test parameters for PCell, the SCell and the neighbour cell are given in table A.6.6.19.4.2-1 and A.6.6.19.4.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3. The PCell shall continuously scheduled with data in the DL starting from T1 until the UE has sent the measurement report during T2.

Table A.6.6.19.4.2-1: Supported test configurations

Table A.6.6.19.4.2-2: General test parameters for event triggered reporting on SCC with deactivated SCell with per-UE NCSG for FR1

Table A.6.6.19.4.2-3: NR Cell specific test parameters for event triggered reporting on SCC with deactivated SCell with per-UE NCSG for FR1

## A.6.6.19.4.3Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall be scheduled on PCell continuously throughout the test. From the start of T1 until the measurement report is received during T2, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

For a test to be considered successful requirements on both Event A6 detection and percentage of transmitted ACK/NACKs have to be fulfilled simultaneously.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.20UE Rx-Tx time difference measurement for propagation delay compensation

## A.6.6.20.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement for RTT-based PDC meets the requirements specified in clause 9.12.4.1 for measurement delay and clause 10.1.39.2 for measurement accuracy in AWGN propagation condition in FR1 in standalone scenario.

The supported test configurations in listed in table A.6.6.20.1-1.

Table A.6.6.20.1-1: Supported test configurations

The test is considered with one cell (Cell 1) in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. If the test is based on PRS, the Cell 1 mutes PRS transmission during T1 and transmits PRS during T2.

If the test is based on PRS, the MeasObjectRxTxDiff-r17 with prs-Ref-r17 , measObject  with measObjectRxTxDiff-17, and NR-DL-PRS-PDC-Info as defined in TS 38.331 shall be provided to the UE during T1.

The last TTI containing the RRC configuration shall be provided to the UE T ms before the start of T2, where T = 10 ms.

The beginning of the time interval T2 shall be aligned with the beginning of the first PRS resources.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.20.1-2. The test parameters for PRS are given Table A.6.6.20.1-3.

Table A.6.6.20.1-2: General test parameters

Table A.6.6.20.1-3: Cell specific test parameters

## A.6.6.20.2Test requirements

If the test is based on PRS, the UE Rx-Tx time difference measurement time fulfils the requirements specified in 9.12.4.1.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

The reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.39.2 for Cell 1.

## A.6.6.21UE Rx-Tx time difference measurement with TRS for RTT-based PDC in FR1 SA

## A.6.6.21.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with TRS for RTT-based PDC meets the requirements specified in clause 9.12.4.2 for measurement delay and clause 10.1.39.3 for measurement accuracy in AWGN propagation condition in FR1 in standalone scenario.

The supported test configurations in listed in table A.6.6.21.1-1.

Table A.6.6.21.1-1: Supported test configurations

There is a single cell in the test: PCell (Cell 1) on RF channel 1 in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 does not have TRS transmission during T1 and transmits TRS during T2.

The measurement control information with MeasObjectRxTxDiff set to ‘csi-RS-Ref’ as defined in TS 38.331 [2], shall be provided to the UE during T1. The last TTI containing the RRC message shall be provided to the UE T ms before the start of T2, where T = 10 ms is the maximum processing time of the measurement request.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.6.21.1-2 and table A.6.6.21.1-3 respectively. The test consists two sub-tests with different TRS BW.

Table A.6.6.21.1-2: General test parameters

Table A.6.6.21.1-3: Cell specific test parameters

## A.6.6.21.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.12.4.2.

The UE shall perform and report the UE Rx-Tx time difference measurement for Cell 1 within the specified UE Rx-Tx time difference measurement time starting from the beginning of T2.

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.39.3

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%.

## A.6.6.22SA event triggered reporting tests for concurrent measurement gaps with Pre-MG

## A.6.6.22.1SA event triggered reporting tests for FR1 concurrent gap with Pre-MG with partially partial overalpping scenario for SSB-based measurements in both intra-frequency and inter-frequency layers

## A.6.6.22.1.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gap with Pre-MG capable UE makes correct reporting of events. This test will partly verify the SA intra-frequency and inter-frequency NR cell search requirements in clauses 9.2.6 and 9.3.4/9.3.5, respectively. Also, this test will also jointly verify pre-configured measurement gap autonomous activation/deactivation delay in clause 8.19.2.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as intra-frequency neighbour cell in FR1 on the same frequency as the PCell, and NR cell 3 as neighbour cell in FR1 on NR RF channel 2. There are two BWPs configured in Cell 1, BWP-1 which contains the cell defining SSB, and BWP-2 which does not contain any SSB of Cell 1. The test parameters are given in tables A.6.6.22.1.1-1, A.6.6.22.1.1-2 and A.6.6.22.1.1-3. The TE schedules continuous DL data on PCell throughout the test.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. Before the test starts, the UE shall not have any timing information of NR Cell 2 or NR Cell 3.

Before the test starts,

-For Cell 1, the UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

-BWP-1 includes bandwidth of the initial DL BWP and SSB. UE is expected to deactivate the Pre-MG when this BWP is active.

-BWP-2 does not include bandwidth of the initial DL BWP and SSB. UE is expected to activate the Pre-MG when this BWP is active.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used.

During T1, UE active DL BWP is BWP-1, and the pre-configured gap (MeasGapId #1) is deactivated. Cell 3 is switched ON from the beginning of T1, and UE is expected to search for Cell 3 in MeasGapId #2.

At the start of time duration T2, Cell 3 is switched OFF and the serving gNB can trigger Pre-MG activation starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2. The UE is expected to complete the Pre-MG activation within T2. Cell 2 is switched ON from the beginning of T2, and UE is expected to search for Cell 2 in MeasGapId #1.

Two measurement gap patterns (MeasGapId #1 (Pre-MG) and MeasGapId #2) are configured with the gap pattern ID #1 and #0 as defined in table A.6.6.22.1.1-2. MeasGapId #1 is configured with a higher priority than MeasGapId #2. MeasGapId #1 and MeasGapId #2 are associated with the MOs for RF channel numbers #1 and #2, respectively.

Table A.6.6.22.1.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.22.1.1-2: General test parameters for SA intra-frequency and inter-frequency event triggered reporting for FR1 concurrent gap with Pre-MG with partially partial overalpping scenario for SSB-based measurements in both intra-frequency and inter-frequency layers

Table A.6.6.22.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gap with Pre-MG with partially-partial overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.22.1.2Test Requirements

For UE supporting dynamicCollision-r18:

During T1, the UE shall report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the MeasGapId#2 occasions. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms for cell 3 from the beginning of time period T1. The measurement reporting delay is derived based on the requirements for inter-frequency measurement in clause 9.3.4 and 9.3.5.

For UE not supporting dynamicCollision-r18:

During T1, the UE shall report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the non-dropped MeasGapId#2 occasions. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms for cell 3 from the beginning of time period T1. The measurement reporting delay is derived based on the requirements for inter-frequency measurement in clause 9.3.4 and 9.3.5.

For both UE supporting dynamicCollision-r18 and not supporting dynamicCollision-r18:

During T2, the UE shall report ACK/NACK for PDSCHs scheduled in the slots that are not overlapped with the MeasGapId #1 occasions or non-dropped MeasGapId #2 occasions after MeasGapId #1 is activated, i.e. starting from the 1 st complete MeasGapId #1 occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) +  as defined in clause 8.19.2.5NR slot length

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than 1080 ms for Cell 2 from the beginning of time period T2. The measurement reporting delay is derived based on the requirements for intra-frequency measurement in clause 9.2.6 plus 80 ms, considering that the frist MeasGapId #1 occasion in T2 may collide with the pre-configured gap activation delay.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%. UE is not required to report SSB time index.

NOTE 1:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.22.2SA event triggered reporting tests for concurrent gap with pre-configured gaps and network-controlled activation/deactivation

## A.6.6.22.2.1Test purpose and Environment

The purpose of this test is to verify that the UE correctly activates and deactivates the pre-MGs and makes correct measurement and reporting of an event with activated and deactivated pre-MG. This test will partly verify the multiple Pre-MG activation/deactivation delay in clause 8.19.5.2, the intra-frequency cell search requirements in clause 9.2.6 and inter-frequency cell search requirements in clause 9.3.4 and 9.3.5..

## A.6.6.22.2.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1) in FR1 on NR RF channel 1 and a neighbour cell (Cell 2) in FR1 on NR RF channel 1 and a neighbour cell (Cell 3) in FR1 on NR RF channel 2. The supported test configurations are listed in table A.6.6.22.2.2-1, general test parameters are listed in table A.6.6.22.2.2-2, and cell specific test parameters are listed in table A.6.6.22.2.2-3.

Two Pre-MG gaps (MeasGapId #1 and MeasGapId #2) are configured with the Pre-MG gap pattern ID #0 and #1 as defined in table A.6.6.22.2.2-2. MeasGapId #2 is configured with a higher priority than MeasGapId #1.

In the measurement control information, two measurement objects (MOs) are configured, the measurement object #1 (MO1) for NR RF channel 1 is associated with MeasGapId #1, and measurement object #2 (MO2) for NR RF channel 2 is associated with MeasGapId #2. And it is indicated to the UE that event-triggered reporting with Event A3 is used.

Before the test, UE is connected to Cell 1 (PCell) on radio channel 1. The UE is configured with two dedicated BWPs for Cell 1 (PCell), BWP-1 and BWP-2. BWP-1 includes bandwidth of the SSB, and preConfGapStatus of the pre-MG (MeasGapId #1) for measurements on BWP-1 is set to ‘0’, preConfGapStatus of the pre-MG (MeasGapId #2) for measurements on BWP-1 is set to ‘1’; BWP-2 does not include bandwidth of the SSB, and preConfGapStatus of the pre-MG (MeasGapId #1) for measurements on BWP-2 is set to ‘1’, preConfGapStatus of the pre-MG (MeasGapId #2) for measurements on BWP-2 is set to ‘0’.

The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively.

During T1, UE active DL BWP is BWP-1, and the pre-configured gap (MeasGapId #1) is deactivated, pre-configured gap (MeasGapId #2) is activated. Cell 3 is switched ON from the beginning of T1, and UE is supposed to search Cell 3 in MeasGapId #2.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its DL active BWP from BWP-1 to BWP-2, and the pre-configured gap (MeasGapId #1) is activated and pre-configured gap (MeasGapId #2) is deactivated. Cell 3 is switched OFF.

At the beginning of T3, Cell 2 is switched ON, and UE is supposed to search Cell 2 in MeasGapId#1.

During T1, UE shall perform inter-frequency measurement with pre-MG (MeasGapId #2) activated.

During T3, UE shall perform intra-frequency measurement with pre-MG (MeasGapId #1) activated.

The TE schedules continuous DL data on PCell throughout the test.

Table A.6.6.22.2.2-1: Supported test configurations

Table A.6.6.22.2.2-2: General test parameters for SA intra-frequency event triggered reporting with  concurrent gap with pre-configured gaps and network-controlled activation/deactivation

Table A.6.6.22.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with concurrent gap with pre-configured gaps and network-controlled activation/deactivation

## A.6.6.22.2.3Test Requirements

During T1, UE shall report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the pre-MG occasions of MeasGapId #2; and

The UE shall send one Event A3 triggered measurement report of cell 3 on RF channel 2, with a measurement reporting delay less than 1280 ms from the beginning of time period T1.

During T2 and starting from the 1 st complete Pre-MG occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) +  as defined in clause 8.19.5.2,  the UE shall report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the pre-MG occasions of MeasGapId #1.7NR slot length

The UE shall send one Event A3 triggered measurement report of Cell 2 on RF channel 1, with a measurement reporting delay less than 800 ms from the beginning of time period T3.

During T3, the UE shall report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the pre-MG occasions of MeasGapId #1.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.23SA event triggered reporting tests for concurrent measurement gaps with NCSG

## A.6.6.23.1SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [one MG + one NCSG]

## A.6.6.23.1.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gaps with NCSG capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.10.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 3. The test parameters are given in tables A.6.6.23.1.1-1, A.6.6.23.1.1-2 and A.6.6.23.1.1-3.

One measurement gap and one NCSG are configured to UE with measurement gap pattern #0 and NCSG pattern #1 respectively. Measurement gap with pattern #0 is associated with inter-frequency measurement on NR Cell 2, and NCSG with pattern #1 is associated with inter-frequency measurement on NR Cell 3 as defined in table A.6.6.23.1.1-2.

NCSG is configured with higher priority than measurement gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used for both frequency layers. The test consists of two successive time periods, with time duration of T1, and T2 respectively.

During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

During T2, the UE is continuously scheduled with data on the PCell.

Table A.6.6.23.1.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.23.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 concurrent NCSGs with partially partially overalpping scenario for SSB-based measurements in both inter-frequency layers

Table A.6.6.23.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 Con-NCSG gaps with partially partially overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.23.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than 1280 ms for Cell 2 and 1280 ms for Cell 3 from the beginning of time period T2.

During T2, UE shall send HARQ-ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern and the non-dropped measurement gap occasions after considering the collision between NCSG and measurement gap.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.23.2SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [two NCSG]

## A.6.6.23.2.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gaps with NCSG capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.10.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 3. The test parameters are given in tables A.6.6.23.2.1-1, A.6.6.23.2.1-2 and A.6.6.23.2.1-3.

Two NCSG patterns (NCSGId #0 and NCSGId #1) are configured with the NCSG pattern ID #0 and #1 as defined in table A.6.6.23.2.1-2. NCSGId #1 is configured with a higher priority than NCSGId #0.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used for both frequency layers. The test consists of two successive time periods, with time duration of T1, and T2 respectively.

During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

During T2, the UE is continuously scheduled with data on the PCell.

Table A.6.6.23.2.1-1: SA event triggered reporting tests for FR1-FR1

Table A.6.6.23.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 concurrent NCSGs with partially partially overalpping scenario for SSB-based measurements in both inter-frequency layers

Table A.6.6.23.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 Con-NCSG gaps with partially partially overalpping scenario for SSB-based measurements in both inter-frequency layers

## A.6.6.23.2.2Test Requirements

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than 1280 ms for Cell 2 and 1280 ms for cell 3 from the beginning of time period T2.

During T2, UE shall send HARQ-ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of non-dropped NCSG patterns after considering the collision between NCSGs.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.23.3Event triggered reporting on SCC with deactivated SCell test with per-UE Con-NCSG under non-DRX

## A.6.6.23.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the cell search requirements on SCC with deactivated SCell in clauses 9.2.7.1 and 9.2.7.2.

## A.6.6.23.3.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1) on NR RF channel 1, FR1 SCell (Cell 2) and FR1 neighbour cell (Cell 3) on the same frequency as the SCell on NR RF channel 2.

The SCell is deactivated during the test. The test parameters for PCell, the SCell and the neighbour cell are given in table A.6.6.23.3.2-1 and A.6.6.23.3.2-2 below.

One measurement gap patterns (MeasGapId #1) and one NCSG pattern (NCSGId #1) are configured with the gap pattern ID #0 and NCSG pattern ID #0 as defined in table A.6.6.23.3.2-2. [NCSGId #1 is associated with the MO for RF channel numbers #2, respectively.]

In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3. The PCell shall continuously scheduled with data in the DL starting from T1 until the UE has sent the measurement report during T2.

Table A.6.6.23.3.2-1: Supported test configurations

Table A.6.6.23.3.2-2: General test parameters for event triggered reporting on SCC with deactivated SCell with per-UE Con-NCSG for FR1

Table A.6.6.23.3.2-3: NR Cell specific test parameters for event triggered reporting on SCC with deactivated SCell with per-UE Con-NCSG for FR1

## A.6.6.23.3.3Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall be scheduled on PCell continuously throughout the test. From the start of T1 until the measurement report is received during T2, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern and MGL of MG pattern.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

For a test to be considered successful requirements on both Event A6 detection and percentage of transmitted ACK/NACKs have to be fulfilled simultaneously.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.24SA event triggered reporting tests with NeedForGap in FR1

## A.6.6.24.1SA event triggered reporting tests without gaps, with interruptions, under non-DRX

## A.6.6.24.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event, and to verify that the interruption ratio does not exceed the limits for the NR PCell during the measurement without gaps and with interruptions. This test will partly verify the cell search requirements in clauses 9.2.5.1 and 9.2.5.2 for measurements performed without gaps and with interruptions. This test will also verify the interruption ratio for PCell in standalone NR specified in clause 8.2.2.2.19. The test will measure that the measurement delay is within the specified boundaries.

The serving frequency should be selected for which UE reports ‘no-gap’ in NeedForGapsIntraFreq-r16 and ‘no-gap-with-interruption’ in interruptionIndication-r18.

## A.6.6.24.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.6.6.24.1.2-1, A.6.6.24.1.2-2 and A.6.6.24.1.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE is capable of measurements without gaps with interruption and report ‘no-gap’ through NeedForGapsIntraFreq-r16 and ‘no-gap-with-interruption’ in interruptionIndication-r18 for PCell. UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment.

Table A.6.6.24.1.2-1: Supported test configurations

Table A.6.6.24.1.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 without DRX

Table A.6.6.24.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 without DRX

## A.6.6.24.1.3Test Requirements

The UE shall be continuously scheduled on PCell during the entire length of T1 and T2.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

During 1000 ms from the beginning of time period T2, the UE shall transmit ACK/NACK in PCell and the rate of missed ACK/NACK shall no more than 2.5%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.24.2SA event triggered reporting tests for FR1 without gap with interruption for inter-frequency measurement with SSB time index detection when DRX is not used

## A.6.6.24.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.9 and interruption requirements during measurement without gap in clause 8.2.2.2.19.

The serving frequency and the target frequency should be selected such that UE reports ‘no-gap’ via needForGapsInfoNR-r16 and ‘no-gap-with-interruption’ via NeedForInterruptionNR-r18 for the target frequency given the serving frequency.

## A.6.6.24.2.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. NR RF channel 1 and NR RF channel 2 should be selected such that UE reports ‘no-gap-with-interruption’ for the target frequency on NR RF channel 2. The test parameters are given in tables A.6.6.24.2.2-1, A.6.6.24.2.2-2 and A.6.6.24.2.2-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

During T2, the UE is continuously scheduled with data on the PCell.

Table A.6.6.24.2.2-1: SA event triggered reporting tests for FR1 for inter-frequency measurement without gap with interruption

Table A.6.6.24.2.2-2: General test parameters for SA event triggered reporting tests for FR1 for inter-frequency measurement without gap with interruption

Table A.6.6.24.2.2-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without gap

## A.6.6.24.2.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1520 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

During 1520 ms from the beginning of time period T2, the UE shall transmit ACK/NACK in PCell and the rate of missed ACK/NACKs shall no more than 2.5%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.24.3SA event triggered reporting tests for FR1 with ‘no-gap-with-interruption’, without measurement gap or DRX

## A.6.6.24.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.9.

The serving frequency and the target frequency should be selected such that UE reports ‘no-gap-with-interruption’ for the target frequency given the serving frequency.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. Supported test configurations are shown in table A.6.6.24.3.1-1. The general test parameters are given in tables A.6.6.24.3.1-2, and cell specific test parameters are given in table A.6.6.24.3.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

The TE schedules continuous DL data on PCell during the test duration.

Table A.6.6.24.3.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.24.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.6.6.24.3.1-3: Cell specific test parameters for inter-frequency event triggered reporting without SSB time index detection

## A.6.6.24.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2560 ms from the beginning of time period T2, where 2560 ms is derived based on inter-frequency measurement requirements in clause 9.3.9.

In the test, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots with an interruption ratio between number of interrupted slot over the total number of slots no larger than 1.25%.

In the test UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.24.4SA event triggered reporting tests for FR1 NeedForGaps without gap without interruption when DRX is not used

## A.6.6.24.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.9 and also verify the interruption during inter-frequency measurement with NeedForGaps.

The serving frequency and the target frequency should be selected for which UE supports NeedForInterruptionInfoNR-R18 measurements and indicates ‘no-gap-no-interruption’ for the target frequency given the serving frequency.

## A.6.6.24.4.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. NR RF channel 1 and NR RF channel 2 should be selected such that UE reports ‘no-gap-no-interruption’ for the target frequency on NR RF channel 2.

The test parameters are given in tables A.6.6.24.4.1-1, A.6.6.24.4.1-2 and A.6.6.24.4.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

During T2, the UE is continuously scheduled with data on the PCell.

Table A.6.6.24.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.6.6.24.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with NeedForInterruption ‘no-gap-no-interruption’

Table A.6.6.24.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with NeedForInterruption ‘no-gap-no-interruption’

## A.6.6.24.4.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

During T2, UE shall send HARQ-ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots.

The rate of correct events observed during repeated tests shall be at least 90%.

The UE is not required to read the neighbour cell SSB index in this test.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.24.5SA event triggered reporting tests without gap under non-DRX for UE indicating no-gap-no-interruption

## A.6.6.24.5.1Test purpose and Environment

The purpose of this test is to verify that the UE which supports ‘no-gap’ makes correct reporting of an event and the UE performs intra-frequency measurement without gap without interuption when the UE indicates ‘no-gap’ via intraFreq-needForGap and the UE indicates no-gap-no-interruption via NeedForInterruptionInfoNR-r18. This test will partly verify the intra-frequency cell search requirements in clauses 9.2.5.1 and 9.2.5.2.

## A.6.6.24.5.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.6.6.24.5.2-2 and A.6.6.24.5.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.6.6.24.5.1.2-1: Supported test configurations

Table A.6.6.24.5.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.6.6.24.5.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.6.6.24.5.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

UE is not allowed to cause interruption during intra-frequency measurement without gap.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.25SA NR - E-UTRAN event-triggered without measurement gaps

## A.6.6.25.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1

## A.6.6.25.1.1Test Purpose and Environment

The purpose of this set of tests is to verify that when UE reports “nogap-noncsg” via NeedForGapNCSG-InfoEUTRA-r17 and the UE is configured with measurement gap, UE doesn’t cause scheduling restriction due to the measurement as defined in clause 9.4.8.3.5 or 9.4.8.4.5, and the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clause 9.4.8.

The serving frequency and the target frequency should be selected such that UE reports ‘nogap-noncsg’ via NeedForGapNCSG-InfoEUTRA-r17 for the target frequency given the serving frequency and ‘eutra-MeasEMW-r18’.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.6.6.25.1.1-1. General test parameters are provided in table A.6.6.25.1.1-2 below. EMW is not configured and measurement gap is configured. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.25.1.1-3 and A.6.6.25.1.1-4, respectively.

Table A.6.6.25.1.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.1.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.1.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.25.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria are not fulfilled.

During the T2, UE shall be able to report ACK/NACK for all slots with PDCCH/PDSCH on PCell excluding those slots within measurement gap.

The rate of correct events observed during repeated tests shall be at least 90%

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.25.2SA NR - E-UTRAN event-triggered reporting without gap under non-DRX in FR1

## A.6.6.25.2.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements without gap as there are vacant RF chains available for UE measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clause 9.4.8, and also verify the scheduling availability during inter-RAT E-UTRAN measurement without gap in clauses 9.4.8.3.5 and 9.4.8.4.5.

The serving frequency and the target frequency should be selected such that UE reports ‘nogap-noncsg’ via NeedForGapNCSG-InfoEUTRA-r17 for the target frequency given the serving frequency and ‘eutra-MeasEMW-r18’.

## A.6.6.25.2.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT E-UTRAN neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are given in Table A.6.6.25.1.1-1 and for EMW configuration in table A.6.6.25.2.2-1 with EMW configuration specified in table 9.4.8.2-1. General test parameters are provided in Table A.6.6.25.2.2-2. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A. A.6.6.25.1.1-3 and A. A.6.6.25.1.1-4, respectively.

Table A.6.6.25.2.2-1: EMW configuration test parameters for SA inter-RAT E-UTRA without gap event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.2.2-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.25.2.3Test Requirements

The actual overall measurement delay test requirements can refer to the requirements in A.6.6.3.1.2. And during T2, for the two subtests regarding to EMW configuration, UE shall or not send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell based on the requirements defined in clauses 9.4.8.3.5 and 9.4.8.4.5.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.25.3SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for UE capable of inter-RAT EUTRAN measurement without gap when CRS is contained within UE’s active DL BWP

## A.6.6.25.3.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE which supports inter-RAT E-UTRAN measurement without gap when CRS is contained within UE’s active DL BWP makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clause 9.4.8, and also verify the scheduling availability during inter-RAT E-UTRAN measurement in clauses  9.4.8.3.5 and 9.4.8.4.5.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. The CRS of Cell 2 is completely within UE’s active BWP BW.

In the measurement control information from the PCell, it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT E-UTRAN neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.6.6.25.3.1-1. General test parameters are provided in table A.6.6.25.3.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.6.6.25.3.1-3 and A.6.6.25.3.1-4, respectively.

Table A.6.6.25.3.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.3.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.3.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.6.6.25.3.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.6.6.25.3.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

During T2, UE does not cause interruption due to inter-RAT E-UTRAN measurement without gap.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.26LTM Intra-frequency L1-RSRP measurement

## A.6.6.26.1Intra-frequency SSB based L1-RSRP measurement in FR1

## A.6.6.26.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SSB based intra-frequency L1-RSRP measurement on neighbor cell in FR1. This test will partly verify the requirements for SSB based intra-frequency L1-RSRP measurement on neighbor cell specified in clause 9.14, with the testing configurations for NR cells in table A.6.6.26.1.1-1.

Table A.6.6.26.1.1-1: Applicable NR configurations for SSB based intra-frequency L1-RSRP LTM measurement test in FR1

## A.6.6.26.1.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Measurement period [and measurement accuracy] is tested by using the parameters in table A.6.6.26.1.2-1, and A.6.6.26.1.2-2.

There are two tests in the test case, test 1 and test 2:

In test 1, time offset between cells is within CP length.

In test 2, time offset between cells is larger than CP length.

If a UE does not support multiCellL1-measRTD-greaterThan-CP-r18, it is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different.  No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an odd SFN.

Table A.6.6.26.1.2-1: General test parameters for SSB based intra-frequency L1-RSRP LTM measurement test in FR1

Table A.6.6.26.1.2-2: Cell specific test parameters for SSB based intra-frequency L1-RSRP LTM measurement test in FR1

## A.6.6.26.1.3Test Requirements

The UE shall send L1-RSRP report every 20 slots. The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 20 ms plus 20 slots from the beginning of time period T2. UE shall send L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.26.2Intra-frequency SSB based L1-RSRP measurement in FR1

## A.6.6.26.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SSB based intra-frequency event triggered L1-RSRP measurement on neighbor cell in FR1. This test will partly verify the requirements for SSB based intra-frequency event triggered L1-RSRP measurement on neighbor cell specified in clause 9.14.3.4.

The testing configurations and parameters are as specified in tables A.6.6.26.1.11, A.6.6.26.1.21, and A.6.6.26.1.22, except for the LTMCSIReportConfig. Specifically, the LTMCSIReportConfig provided in table A.6.6.26.2.21 is used in place of the LTMCSIReportConfig defined in table A.6.6.26.1.21.

The UE which passes this test case can skip the test case in A.6.6.26.1.

## A.6.6.26.2.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Measurement period and measurement accuracy is tested by using the parameters in table A.6.6.26.2.2-1.

There are two tests in the test case, test 1 and test 2:

In test 1, time offset between cells is within CP length.

In test 2, time offset between cells is larger than CP length.

If a UE does not support multiCellL1-measRTD-greaterThan-CP-r18, it is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different.  No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and event triggered L1-RSRP measurement reports on candidate cell (Cell 2) without any special SR configuration.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an odd SFN, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.6.6.26.2.2-1: General test parameters for SSB based intra-frequency L1-RSRP LTM measurement test in FR1

## A.6.6.26.2.3Test Requirements

The UE is scheduled with UL grant in every slot from the start of time T2.

The UE shall send L1-RSRP report within the 20ms from the start of T2. UE shall send L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.26.3CSI-RS based L1 RSRP measurement for neighbour cell in FR1 with event triggered reporting or periodic reporting

## A.6.6.26.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event triggered L1-RSRP measurement or periodic L1-RSRP measurement for FR1.

This test and its sub-tests cases will partly verify the requirements for CSI-RS based intra-frequency L1-RSRP measurement on neighbor cell specified in clause 9.14a (CSI-RS based Intra-frequency L1-RSRP measurements for neighbor cell), with the testing configurations for NR cells in table A.6.6.26.3.1-1.

Table A.6.6.26.3.1-1: Applicable NR configurations for CSI-RS based intra-frequency L1-RSRP LTM measurement test in FR1

## A.6.6.26.3.2Test Parameters

There are two intra-frequency cells in the test, FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2). The cell 1 and cell 2 are on the same frequency.

The test parameters for PCell and neighbour cell are given in table A.6.6.26.3.2-1 and A.6.6.26.3.2-2.

In the test, the time offset between cells shall be within CP length.

In CSI measurement configuration, the UE is configured to perform L1-RSRP measurement on the FR1 CSI-RS and the UE shall not be configured to perform L1-RSRP measurements for the FR1 SSB specified in the section 9.14.

There are two sub-test cases in this test, Test 1 and Test 2. No gap patterns are configured in the test cases.

Test 1: Periodic L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is configured.

Test 2: Event triggered L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is configured.

If a UE supports both periodic reporting (Test 1) and event triggered reporting (Test 2), UE needs to pass only event triggered reporting test (Test 2).

Test 1 and Test 2 consists of two successive time periods T1 and T2. At the beginning of T2, CSI_RP of Cell 2 changes to a different value from T1, hence CSI_RP of Cell 2 in T1 and T2 are different. Prior to the start of the time duration T1 for both test cases:

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A L3 measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has performed SSB based L3 measurement on Cell 2 and transmitted a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-LTM-NZP-CSI-RS-ResourceSet-r19 is provided to the UE to configure periodic L1-RSRP on CSI-RS or event triggered L1-RSRP on the CSI-RS.

In Test 2, the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.6.6.26.3.2-1: General test parameters

Table A.6.6.26.3.1-2: NR Cell specific test parameters

## A.6.6.10.1.2Test Requirements

In Test 1:

-The UE shall send first CSI-RS L1-RSRP report within 320 slots from the beginning of T1.

-From the start of T2, the UE shall report higher RSRP values for cell 2 at least after 320 slots from the start of T2.

-The UE shall send CSI-RS L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

In Test 2:

-The UE shall send one event LTM3 triggered measurement report, with a measurement reporting delay less than 20ms + 10ms uncertainty to transmit SR from the beginning of time period T2.

-The UE shall send CSI-RS L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

The rate of correct events observed during repeated tests shall be at least 90%

## A.6.6.27LTM Inter-frequency L1-RSRP measurement with measurement gap

## A.6.6.27.1Inter-frequency SSB based L1-RSRP measurement with measurement gap

## A.6.6.27.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of inter-frequency L1-RSRP measurement with measurement gap on candidate neighbour cell. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.5, with the testing configurations for NR cells in table A.6.6.27.1.1-1.

Table A.6.6.27.1.1-1: Applicable NR configurations for SSB based inter-frequency L1-RSRP LTM measurement with MG test in FR1

## A.6.6.27.1.2Test parameters

There are two carriers and one cell on each carrier in the test, NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters for the Cell 1 and Cell 2 are given in table A.6.6.27.1.2-1 and table A.6.6.27.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform inter-frequency L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively.

Measurement gap pattern configuration defined in table A.6.6.27.1.2-1 is provided.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1.

Table A.6.6.27.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with MG test in FR1

Table A.6.6.27.1.2-2: Cell specific test parameters for SSB based inter-frequency L1-RSRP LTM measurement with MG test in FR1

## A.6.6.27.1.3Test Requirements

During T1 The UE shall send inter-frequency L1-RSRP report every 80 slots. No later than 80 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report of Cell 2. The RSRP report during T2 shall be larger than that during T1. These reported measurement report shall meet the absolute accuracy requirement in clause 10.1.19E. The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.27.2Inter-frequency SSB based L1-RSRP measurement with measurement gap with event triggered reporting

## A.6.6.27.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of inter-frequency L1-RSRP measurement with measurement gap on candidate neighbour cell. This test will partly verify the L1-RSRP event triggered reporting requirements in clause 9.15.3.4, with the testing configurations for NR cells in table A.6.6.27.1.1-1.

## A.6.6.27.2.2Test parameters

There are two carriers and one cell on each carrier in the test, NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters for the Cell 1 and Cell 2 are given in tables A.6.6.27.1.2-1 and table A.6.6.27.1.2-2 , except for those defined in Table A.6.6.27.2.2-1 below.

In CSI measurement configuration, UE is indicated to perform inter-frequency L1-RSRP measurement on the SSBs and event-triggered reporting with Event LTM3 is used. The test consists of two successive time periods, with time duration of T1 and T2 respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and event-triggered reporting with Event LTM3 on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.6.6.27.2.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with MG with event triggered reporting test in FR1

## A.6.6.27.2.3Test Requirements

The UE shall send one Event LTM3 triggered measurement report less than 170 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

These reported measurement report shall meet the absolute accuracy requirement in clause 10.1.19E. The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.28LTM Inter-frequency L1-RSRP measurement without measurement gap

## A.6.6.28.1Inter-frequency SSB based L1-RSRP measurement without measurement gap

## A.6.6.28.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting inter-frequency L1-RSRP measurements without gap makes correct reporting of inter-frequency L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.6, with the testing configurations for NR serving cells in table A.6.6.28.1.1-1.

Table A.6.6.28.1.1-1: Applicable NR configurations for SSB based inter-frequency L1-RSRP measurement without measurement gap in test

## A.6.6.28.1.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) on NR RF channel 1 and Cell 2 as neighbour cell in FR1 on NR RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters are given in table A.6.6.28.1.2-1 and table A.6.6.28.1.2-2 below.

There are two tests in the test case, test 1 and test 2:

In test 1, time offset between cells is within CP length.

In test 2, time offset between cells is larger than CP length.

UE not capable of multiCellL1-measRTD-greaterThan-CP-r18 is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. There is no measurement gap configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an even SFN.

Table A.6.6.28.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP measurement without measurement gap in test

Table A.6.6.28.1.2-2: Cell specific test parameters for SSB based inter-frequency L1-RSRP measurement without measurement gap in test

## A.6.6.28.1.3Test Requirements

The UE shall send L1-RSRP report every 20 slots. No later than 20 ms plus 20 slots from the beginning of time period T2, UE shall send L1-RSRP report of Cell 2 while meeting the absolute accuracy requirement in clause 10.1.19E.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.28.2Inter-frequency SSB based L1-RSRP measurement without measurement gap with event triggered reporting

## A.6.6.28.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting inter-frequency L1-RSRP measurements without gap makes correct reporting of inter-frequency L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.3.4, with the testing configurations for NR serving cells in table A.6.6.28.1.1-1.

## A.6.6.28.2.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) on NR RF channel 1 and Cell 2 as neighbour cell in FR1 on NR RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters for the Cell 1 and Cell 2 are given in tables A.6.6.28.1.2-1 and table A.6.6.28.1.2-2, except for those defined in Table A.6.6.28.2.2-1 below.

There are two tests in the test case, test 1 and test 2:

In test 1, time offset between cells is within CP length.

In test 2, time offset between cells is larger than CP length.

UE not capable of multiCellL1-measRTD-greaterThan-CP-r18 is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. There is no measurement gap configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and event-triggered reporting with Event LTM3 or periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an even SFN, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.6.6.28.2.2-1: General test parameters for SSB based inter-frequency L1-RSRP measurement without measurement gap with event triggered reporting in test

## A.6.6.28.2.3Test Requirements

The UE shall send one Event LTM3 triggered measurement report less than 50 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.6.6.29RSCPD Measurements

## A.6.6.29.1NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state

## A.6.6.29.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD measurement reported together with the RSTD measurement meets the requirements specified in clause 9.9.7 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured to the UE.

The supported test configurations are specified in table A.6.6.29.1.1-1.

Table A.6.6.29.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

Note:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. In NR-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources to be measured within the configured time window.

The UE is configured with measurement gap pattern ID # 24 or # 0 before T2.

The general test parameters are listed in table A.6.6.29.1.1-2, and cell specific test parameters are listed in table A.6.6.29.1.1-3.

Table A.6.6.29.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.6.29.1.1-3: Cell-specific test parameters for RSCPD with RSTD measurement reporting delay during T1

Table A.6.6.29.1.1-4: Cell-specific test parameters for RSCPD with RSTD measurement reporting delay during T2

## A.6.6.29.1.2Test Requirements

The RSCPD reported together with RSTD measurement time fulfils the requirements specified in the clause 9.9.7.

The UE shall perform and report the RSCPD and RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 9.9.7 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for DL RSCPD measurement for each neighbour cell observed during the repeated tests shall be at least 90%. The reported DL RSCPD measurement shall be within the DL RSCPD reporting range specified in the clause 10.1.43 and the reported RSTD measurement shall be within the RSTD reporting range specified in the clause 10.1.23.

## A.6.6.30RSCP Measurements

## A.6.6.30.1DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA

## A.6.6.30.1.1Test purpose and environment

The purpose of the test is to verify that the DL RSCP and UE Rx-Tx time difference measurements meet the requirements specified in clause 9.9.8.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured for both DL RSCP measurement and UE Rx-Tx time difference measurement.

The supported test configurations are listed in table A.6.6.30.1.1-1.

Table A.6.6.30.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-Multi-RTT-ProvideAssistanceData message and NR-Multi-RTT-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE during T1. In NR-Multi-RTT-RequestLocationInformation, the UE is configured to perform DL RSCP measurement via nr-DL-PRS-RSCP-Request. The UE is configured to perform both DL RSCP and UE Rx-Tx time difference measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources to be measured within the configured time window.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are listed in table A.6.6.30.1.1-2 and table A.6.6.30.1.1-3.

Table A.6.6.30.1.1-2: General test parameters

Table A.6.6.30.1.1-3: Cell specific test parameters

## A.6.6.30.1.2Test requirements

The DL RSCP with UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.8 with Nsample=4 for UE Rx-Tx time difference.

The UE shall perform and report the DL RSCP and UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified DL RSCP with UE Rx-Tx time difference measurement time specified in clause 9.9.8 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%. The reported DL RSCP measurement shall be within the DL RSCP reporting range specified in clause 10.1.44 and the reported UE Rx-Tx measurement shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.

## A.6.6.31CJT calibration measurements and accuracy

## A.6.6.31.1CJTC Delay offset measurement period and accuracy in FR1

## A.6.6.31.1.1Test Purpose and Environment

The purpose of this test is to verify that the CJT Calibration Delay Offset (CJTC-Dd) report measurement period and accuracy are within the specified limits outlined in the test requirements section. The configurations used for the test are defined in Table A.6.6.31.1.1-1.

The test consists of two tests, Test 1 and Test 2. Each test further consists of two subtests Test 1, and Test 2.

Test 1: 15 kHz SCS FDD + Delay offset between TRP 4.7µs + MD is 256 levels

Test 2: 30 kHz SCS TDD + Delay offset between TRP 2.35µs + MD is 256 levels

Relevant parameters for each test are provided in the table A.6.6.31.1.2-1. UE needs to pass Test 1 and 2.

Table A.6.6.31.1.1-1: Applicable NR configurations for CJTC Delay offset

The test procedure consists of two successive time periods, denoted as T1 and T2, with durations defined as following.

-During T1, the UE is configured to perform CJTC-Dd reporting. Throughout this period, the UE continuously calculates the CJTC delay offset based on the configured TRS periodicity.

-T2 begins when the UE receives a DCI command from the test equipment (TE), requesting the CJTC-Dd report. The DCI command is sent on the next slot of the TRS burst is transmitted.

The test equipment evaluates the CJTC delay by counting the number of slots between the transmission of the DCI command and the reception of the corresponding CJTC-Dd report from the UE.

To verify CJTC delay offset accuracy, the test equipment compares the expected CJTC-Dd index level with the reported delay offset index. A match between the expected and reported values indicates correct CJTC delay offset reporting behavior.

## A.6.6.31.1.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.6.31.1.2-1. CJTC Delay offset measurement period, and accuracy is tested by using the parameters in table A.6.6.31.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured with 1 TRS set with the TRS resources in the set are configured in adjacent slot. UE is configured to perform L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.6.6.31.1.2-1: FR1 CJTC Delay offset test parameters

## A.6.6.31.1.3Test Requirements

For Test 1 and 2, UE should send the CJTC Delay offset measurement report as per the UL grant sent in the DCI for the 90% of the times over repeated tests.

For Test 1, the reported CJTC Delay offset measurement accuracy index shall be smaller than or equal to 74ns for the UE supporting cjtc-DdReportHighAccuracy-r19, otherwise shall be smaller than or equal to 258ns, 90% of the times over repeated tests.

For Test 2, the reported CJTC Delay offset measurement accuracy index shall be smaller than or equal to 46ns for the UE supporting cjtc-DdReportHighAccuracy-r19, otherwise shall be smaller than or equal to 166ns, for the 90% of the times over repeated tests.

## A.6.6.31.2CJTC frequency offset measurement period and accuracy in FR1

## A.6.6.31.2.1Test Purpose and Environment

The purpose of the test is to verify that frequency offset (CJTC-F) measurement for CJT calibration meets the requirements specified in clause 9.16 for measurement period and clause 10.1.45 for measurement accuracy in FR1 standalone scenario.

The supported test configurations are specified in table A.6.6.31.2.1-1.

Table A.6.6.31.2.1-1: Supported test configurations

In the test there is one active serving cell, the FR1 PCell (Cell 1), configured with two TRPs. The frequency offset between the TRPs is 0.1ppm. The CJT configurations of MFO = 256 and AFO=0.2ppm are used in the test by the test equipment (TE) to configure the UE with CJTC-F reporting.

The test consists of two time periods T1 and T2. During T1, the UE is configured to perform CJTC-F measurement and calculates the frequency offset based on the configured TRS periodicity. T2 starts when the UE is triggered via DCI to report CJTC-F measurement results and ends when the TE receives the corresponding report in the UL grant.

The test parameters for the Cell 1 are given in table A.6.6.31.2.1-2 and table A.6.6.31.2.1-3 below.

Table A.6.6.31.2.1-2: General test parameters

Table A.6.6.31.2.1-3: Cell specific test parameters

## A.6.6.31.2.2Test requirements

The UE shall send CJTC-F measurement report at the configured UL grant from the reception of DCI triggering for at least 90% rate of correct events observed during repeated tests.

If the UE support high accuracy capability cjtc-FO-ReportHighAccuracy-r19 high accuracy reporting level 1, the CJTC-F measurement accuracy shall fulfil the requirements specified in clause 10.1.45, Table 10.1.45-2, for at least 90% rate of correct events observed during repeated tests. Otherwise, the CJTC-F measurement accuracy shall fulfil the requirements specified in clause 10.1.45.3, Table 10.1.45.3-1, for at least 90% rate of correct events observed during repeated tests.

## A.6.6.32L1 CLI measurements

## A.6.6.32.1L1-SRS-RSRP measurement with DRX with SBFD

## A.6.6.32.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SRS-RSRP measurement when configured with SBFD in DU operation. This test will verify the L1-SRS-RSRP measurement requirements in clause 9.18.2 with the testing configurations for NR cells in table A.6.6.32.1.1-1.

Table A.6.6.32.1.1-1: Applicable NR configurations for FR1 L1-SRS-RSRP test

## A.6.6.32.1.2Test Parameters

One cell is deployed in the test, which is FR1 PCell (Cell 1). The test parameters for PCell is given in table A.6.6.32.1.2-1 and A.6.6.32.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SRS-RSRP measurement on SRS-RSRP-MeasurementResourceSet configured in a CSI-ResourceConfig and report aperiodically. The higher layer parameter timeRestrictionForChannelMeasurements is configured to UE in the test.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. During the test, the test system transmits SRS resource for measurement in the SBFD slot according to the SRS configuration in table A.6.6.32.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A.6.6.32.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

At 640ms after the beginning of time period T2, the DCI triggering L1-SRS-RSRP reporting is sent to UE and UE provides the report back based on the reporting configuration.

Table A.6.6.32.1.2-1: General test parameters for L1-SRS-RSRP reporting for PCell in FR1

Table A.6.6.32.1.2-2: NR Cell specific test parameters for L1-SRS-RSRP reporting for PCell in FR1

Table A.6.6.32.1.2-3: FR1 test parameters for aggressor UE

Table A.6.6.32.1.2-4: SRS configuration parameters

## A.6.6.32.1.3Test Requirements

Within 650 ms from the beginning of time period T2, the UE shall send L1-SRS-RSRP report.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.32.2L1-CLI-RSSI measurement with DRX with SBFD

## A.6.6.32.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-CLI-RSSI measurement with UE configured with two DL subbands in SBFD DUD operation. The RSSI resource CLI-RSSI-MeasResource is configured across two DL subbands. This test will verify the CLI-RSSI measurement requirements in clause 9.18.3 with the testing configurations for NR cells in table A.6.6.32.2.1-1.

Table A.6.6.32.2.1-1: Applicable NR configurations for FR1 L1-CLI-RSSI test

## A.6.6.32.2.2Test Parameters

One cell is deployed in the test, which are FR1 PCell (Cell 1). The test parameters for PCell is given in table A.6.6.32.2.2-1 and A.6.6.32.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-CLI-RSSI measurement on CLI-RSSI-MeasResource and report aperiodically. The test consists of two successive time periods, with time duration of T1 and T2, respectively. The higher layer parameter timeRestrictionForChannelMeasurements is configured to UE in the test. At 640ms after the beginning of time period T2, the DCI triggering L1-CLI-RSSI reporting is sent to UE and UE provides the report back based on the reporting configuration.

There is no measurement gap configured in the test. The L1-CLI-RSSI measurement resource CLI-RSSI-MeasResource configuration is in table A.6.6.32.2.2-3.

Table A.6.6.32.2.2-1: General test parameters for L1-CLI-RSSI reporting for PCell in FR1

Table A.6.6.32.2.2-2: NR Cell specific test parameters for L1-CLI-RSSI reporting for PCell in FR1

Table A.6.6.32.2.2-3: CLI-RSSI-MeasResource measurement resource configuration for measurement reporting

## A.6.6.32.2.3Test Requirements

Within 650 ms from the beginning of time period T2, the UE shall send L1-CLI-RSSI report. The nominal RSSI used to evaluate the requirement shall be based on Io. The UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.33LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation

## A.6.6.33.1Inter-frequency SSB based L1-RSRP measurement with measurement gap cancellation

## A.6.6.33.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of inter-frequency L1-RSRP measurement with measurement gap cancellation on candidate neighbour cell and correct behaviour for scheduling within cancelled measurement gap. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.5, with the testing configurations for NR cells in table A.6.6.27.1.1-1.

## A.6.6.33.1.2Test parameters

There are two carriers and one cell on each carrier in the test, NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters for the Cell 1 and Cell 2 are given in table A.6.6.27.1.2-1 and table A.6.6.27.1.2-2 with additional changes in table A.6.6.33.1.2-1 below.

In CSI measurement configuration, UE is indicated to perform inter-frequency L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. The time duration T2 is divided in 2 phases, T2-1 and T2-2.During time duration T2-1, the test equipment randomly selects Lcancel gap occasions to be cancelled via DCI indication. During time duration T2-2 there is no cancelled gap occasions. T2, T2-1, T2-2 and Lcancel are given in Table A.6.6.33.1.2-1. If a measurement gap occasion is determined to be cancelled, the TE sends the DCI indication latest X ms before the start of the measurement gap occasion using DCI format 1-1, where X is 3ms or 5ms as given by the UE capability minimumTimeOffset-r19.

Table A.6.6.33.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with MG test in FR1

The UE is scheduled with DL data on PCell on all the slots overlapping with the cancelled measurement gap occasions.

## A.6.6.33.1.3Test Requirements

During T1 The UE shall send inter-frequency L1-RSRP report every 80 slots.

From the beginning of time period T2, UE shall send L1-RSRP report of Cell 2 no later than 120 ms plus 80 slots. These reported measurement report shall meet the absolute accuracy requirement in clause 10.1.19E.

During T2, the UE shall send ACK/NACK for the scheduled new transmissions within cancelled measurement gap.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.6.34DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state

## A.6.6.34.1Test Purpose and Environment

The purpose of the test is to verify that the DL AI/ML positioning reporting delay meets the requirement specified in clause 9.9E.5 in an environment with TDL-A propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.6.34.1-1.

Table A.6.6.34.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells start transmitting PRS from the beginning of time period T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-AIML-ProvideAssistanceData and nr-DL-AIML-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.13.5], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL AI/ML assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.6.6.34.1-2, and cell specific test parameters are listed in table A.6.6.34.1-3.

Table A.6.6.34.1-2: General test parameters for DL AI/ML positioning reporting delay

Table A.6.6.34.1-3: Cell-specific test parameters for DL AI/ML positioning reporting delay during T1

Table A.6.6.34.1-4: Cell-specific test parameters for DL AI/ML positioning reporting delay during T2

## A.6.6.34.2Test Requirements

The DL AI/ML positioning reporting delay fulfils the requirements specified in clause 9.9E.1 and clause 9.9E.5.

The UE shall perform and report its infered position within the time duration specified in clause 9.9E.1 and clause 9.9E.5 from the beginning of time interval T2 provided that the PRS resources are transmitted during that time period.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The UE reports its infered location in NR-DL-AIML-LocationInformation as specified in TS 37.355 [34].

## A.6.7Measurement Performance requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause 10 for at least 90% of the reported cases.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.6.7.1SS-RSRP

## A.6.7.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.1.1 and 10.1.2.1.2 for intra-frequency measurements.

## A.6.7.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.6.7.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.6.7.1.1.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

Table A.6.7.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.6.7.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.2.1.2.

## A.6.7.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.1.1 and 10.1.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.6.7.1.2.1-1.

Table A.6.7.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.6.7.1.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.6.7.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.6.7.1.2.2-1: SS-RSRP inter-frequency test parameters

## A.6.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1.4.1.1 and relative requirement in clause 10.1.4.1.2.

## A.6.7.1.3Void

## A.6.7.1.4SA inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for UE configured with measurement gap cancellation

## A.6.7.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits for the UE, which is configured with measurement gap cancellation according to clause 9.1.14. This test will verify the requirements in clauses 10.1.4.1.1 and 10.1.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.6.7.1.2.1-1 in clause A.6.7.1.2.1.

## A.6.7.1.4.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and an FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.6.7.1.2.2-1 in clause A.6.7.1.2.1. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.1.2.2-1 in clause A.6.7.1.2.1. The inter-frequency measurements are supported by measurement gaps.

The UE shall provide its capability in enableTx-RxDuringMeasGap [2] before the beginning of the test. During the test time, for each measurement gap occasion the test equipment randomly determines whether the measurement gap is to be configured for cancellation at the UE via DCI indication, and if so, configures the DCI indication no later than X ms before the start of the measurement gap occasion to be cancelled, where X is indicated by the UE by minimumTimeOffset-r19 [2]. The total number of cancelled measurement gap occasions shall be at least 30% of the total number of configured measurement gaps during the entire test duration. DCI format 1_1 is used for the DCI indication.

During the entire test duration, the UE is scheduled with DL data on PCell on all the slots overlapping with the cancelled measurement gap occasions.

## A.6.7.1.4.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1.4.1.1 and relative requirement in clause 10.1.4.1.2.

During the entire test duration, the UE shall send valid ACK/NACK for all the scheduled transmissions in all the slots overlapping with the cancelled measurement gap occasions.

## A.6.7.2SS-RSRQ

## A.6.7.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.1.1.

## A.6.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.6.7.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.6.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.6.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.6.7.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.1.1.

## A.6.7.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

## A.6.7.2.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.6.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.6.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.6.7.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.6.7.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

## A.6.7.3SS-SINR

## A.6.7.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.1.1.

## A.6.7.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.6.7.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.6.7.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.6.7.3.1.2-2: SS-SINR Intra frequency test parameters

## A.6.7.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.1.1.

## A.6.7.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.1.1 and 10.1.14.1.2.

## A.6.7.3.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.6.7.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.6.7.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.6.7.3.2.2-2: SS-SINR Inter frequency test parameters

## A.6.7.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.1.1 and 10.1.14.1.2.

## A.6.7.4L1-RSRP measurement for beam reporting

## A.6.7.4.1SSB based L1-RSRP measurement

## A.6.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5.2 and clause 10.1.19.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.6.7.4.1.1-1.

Table A.6.7.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.6.7.4.1.2Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.6.7.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.6.7.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1.19.1.

## A.6.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.6.7.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5.3 and clause 10.1.19.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.6.7.4.2.1-1.

Table A.6.7.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.6.7.4.2.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.6.7.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.6.7.4.2.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1.19.2.

## A.6.7.5E-UTRAN RSRP

## A.6.7.5.1SA: inter-RAT measurement accuracy with FR1 serving cell

## A.6.7.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2.2 for SA inter-RAT E-UTRAN RSRP measurements.

## A.6.7.5.1.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.6.7.5.1.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRP are tested by using the parameters in A.6.7.5.1.2-2 and A.6.7.5.1.2-3.

Table A.6.7.5.1.2-1: Inter-RAT E-UTRAN RSRP supported test configurations with FR1 serving cell

Table A.6.7.5.1.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

Table A.6.7.5.1.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

## A.6.7.5.1.3Test Requirements

The SA inter-RAT E-UTRAN RSRP measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 10.2.2.

## A.6.7.6E-UTRAN RSRQ

## A.6.7.6.1SA: inter-RAT measurement accuracy with FR1 serving cell

## A.6.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2.3 for SA inter-RAT E-UTRAN RSRQ measurements.

## A.6.7.6.1.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.6.7.6.1.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRQ are tested by using the parameters in A.6.7.6.1.2-2 and A.6.7.6.1.2-3.

Table A.6.7.6.1.2-1: Inter-RAT E-UTRAN RSRQ supported test configurations with FR1 serving cell

Table A.6.7.6.1.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

Table A.6.7.6.1.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

## A.6.7.6.1.3Test Requirements

The SA inter-RAT E-UTRAN RSRQ measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 10.2.3.

## A.6.7.7E-UTRAN RS-SINR

## A.6.7.7.1SA: inter-RAT measurement accuracy with FR1 serving cell

## A.6.7.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2.4 for SA inter-RAT E-UTRAN RS-SINR measurements.

## A.6.7.7.1.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.6.7.7.1.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RS-SINR are tested by using the parameters in A.6.7.7.1.2-2 and A.6.7.7.1.2-3.

Table A.6.7.7.1.2-1: Inter-RAT E-UTRAN RS-SINR supported test configurations with FR1 serving cell

Table A.6.7.7.1.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RS-SINR test parameters

Table A.6.7.7.1.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RS-SINR test parameters

## A.6.7.7.1.3Test Requirements

The SA inter-RAT E-UTRAN RS-SINR measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 10.2.4.

## A.6.7.8CLI measurements

## A.6.7.8.1SA SRS-RSRP measurement accuracy with FR1 serving cell

## A.6.7.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the SRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.1.1 with the testing configurations for NR cells in table A.6.7.8.1.1-1.

Table A.6.7.8.1.1-1: Applicable NR configurations for FR1 SRS-RSRP accuracy test

## A.6.7.8.1.2Test parameters

In this set of test cases there is one cell in the test, FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.8.1.2-1 below. The test parameter for the (virtual) neighbor cell UE transmitting SRS are given in table A.6.7.8.1.2-2.

Before the test UE is configured to perform SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in the DL slots according to the SRS configuration in table A.6.7.8.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

Table A.6.7.8.1.2-1: FR1 test parameters for SRS-RSRP accuracy for PCell

Table A.6.7.8.1.2-2: FR1 test parameters for SRS-RSRP accuracy for neighbour cell UE

Table A.6.7.8.1.2-3: SRS configuration parameters for FR1 SRS-RSRP accuracy

## A.6.7.8.1.3Test Requirements

The SRS-RSRP measurement accuracy shall fulfil the requirements in clauses 10.1.22.1.1.

## A.6.7.8.2SA CLI-RSSI measurement accuracy with FR1 serving cell

## A.6.7.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.2.1 with the testing configurations for NR cells in table A.6.7.8.2.1-1.

Table A.6.7.8.2.1-1: Applicable NR configurations for FR1 CLI-RSSI accuracy test

## A.6.7.8.2.2Test parameters

In this set of test cases there is one cell in the test, the FR1 PSCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.8.2.2-1 below.

Before the test UE is configured to perform CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI resource and on 1 data symbol before. The CLI-RSSI measurement resource configuration is in table A.6.7.8.2.2-2.

Table A.6.7.8.2.2-1: FR1 test parameters for CLI-RSSI accuracy

Table A.6.7.8.2.2-2: CLI-RSSI measurement resource configuration for FR1 CLI-RSSI accuracy

## A.6.7.8.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the requirements in clauses 10.1.22.2.1.

## A.6.7.9L1-SINR measurement for beam reporting

A.6.7.9.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

A.6.7.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8.4.1 and clause 10.1.27.1 for L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.6.7.9.1.1-1.

Table A.6.7.9.1.1-1: Applicable NR configurations for FR1 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

A.6.7.9.1.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.9.1.2-1 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.6.7.9.1.2-1: FR1 CSI-RS based L1-SINR test parameters

A.6.7.9.1.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.27.1.

## A.6.7.9.2L1-SINR measurement with SSB based CMR and dedicated IMR

## A.6.7.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8.4.2 and clause 10.1.27.2 for L1-SINR measurements with SSB based CMR and dedicated CSI-RS based IMR, with the testing configurations for NR cells in table A.6.7.9.2.1-1.

Table A.6.7.9.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.6.7.9.2.2Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.9.2.2-1 below. The absolute accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-RS resource set with two CSI-RS resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.6.7.9.2.2-1: FR1 SSB based L1-SINR test parameters

## A.6.7.9.2.3Test Requirements

The L1-SINR measurement accuracy for SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 of Cell 1 shall fulfil the requirements in clauses 10.1.27.2.

## A.6.7.9.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR

## A.6.7.9.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8.4.3 and clause 10.1.27.3 for L1-SINR measurements based on CSI-RS as CMR and CSI-IM as IMR with the testing configurations for NR cells in table A.6.7.9.3.1-1.

Table A.6.7.9.3.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

## A.6.7.9.3.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.9.3.2-1 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources and one CSI-IM resource set with two CSI-IM resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as CMR and CSI-IM as IMR.

Table A.6.7.9.3.2-1: FR2 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

## A.6.7.9.3.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0+CSI-IM#0 and CSI-RS#1+CSI-IM# of Cell 1 shall fulfil the requirements in clause 10.1.27.3.

## A.6.7.10CSI-RSRP

## A.6.7.10.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.10.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.3.1 and 10.1.2.3.2 for CSI-RS intra-frequency measurements.

## A.6.7.10.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.10.1.2-1. Both absolute and relative accuracy of CSI-RSRP intra-frequency measurements are tested by using the parameters in A.6.7.10.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.6.7.10.1.2-1: CSI-RSRP intra frequency supported test configurations

Table A.6.7.10.1.2-2: CSI-RSRP intra frequency test parameters

## A.6.7.10.1.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.3.1 and relative requirement in clause 10.1.2.3.2.

## A.6.7.10.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.10.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.3.1 and 10.1.4.3.2 for CSI-RS inter-frequency measurements with the testing configurations for NR cells in table A.6.7.9.2.1-1.

Table A.6.7.10.2.1-1: Applicable NR configurations for FR1 inter-frequency CSI-RSRP accuracy test

## A.6.7.10.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.6.7.10.2.2-1 below. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.10.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.6.7.10.2.2-1: CSI-RSRP inter-frequency test parameters

## A.6.7.10.2.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.4.3.1 and relative requirement in clause 10.1.4.3.2.

## A.6.7.11CSI-RSRQ

## A.6.7.11.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.11.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.2.

## A.6.7.11.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.6.7.11.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.11.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.6.7.11.1.2-1: Intra frequency CSI-RSRQ supported test configurations

Table A.6.7.11.1.2-2: CSI-RSRQ Intra frequency test parameters

## A.6.7.11.1.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.2.

## A.6.7.11.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.11.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

## A.6.7.11.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.6.7.11.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.11.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.6.7.11.2.2-1: CSI-RSRQ Inter frequency CSI-RSRQ supported test configurations

Table A.6.7.11.2.2-2: CSI-RSRQ Inter frequency test parameters

## A.6.7.11.2.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

## A.6.7.12CSI-SINR

## A.6.7.12.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.12.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.2.1.

## A.6.7.12.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.6.7.11.1.2-1. The absolute accuracy of CSI-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.11.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.6.7.12.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

Table A.6.7.12.1.2-2: CSI-SINR Intra frequency test parameters

## A.6.7.12.1.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.2.1.

## A.6.7.12.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.6.7.12.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.2.1 and 10.1.14.2.2.

## A.6.7.12.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.6.7.12.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.12.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.6.7.12.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

Table A.6.7.12.2.2-2: CSI-SINR Inter frequency test parameters

## A.6.7.12.2.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.2.1 and 10.1.14.2.2.

## A.6.7.13RSTD measurements

## A.6.7.13.1RSTD measurement accuracy test case for single positioning frequency layer

## A.6.7.13.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.7.13.1.1-1.

Table A.6.7.13.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR1. GP#24 is configured if UE supports MG#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

Table A.6.7.13.1.1-2: RSTD accuracy test parameters

## A.6.7.13.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.7.13.2RSTD measurement accuracy test case for dual positioning frequency layer

## A.6.7.13.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.7.13.2.1-1.

Table A.6.7.13.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell on NR RF channel #1 in FR1. Cell 2 is a neighbour cell on a different NR RF channel #2 in FR1. GP#24 is configured if UE supports MG#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

Table A.6.7.13.2.1-2: RSTD accuracy test parameters

## A.6.7.13.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.7.13.3RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state

## A.6.7.13.3.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements for reduced number of samples specified in clause 10.1.23.2 in an environment with AWGN propagation conditions. In this test UE that supports supportedDL-PRS-ProcessingSamples is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.6.7.13.3.1-1.

Table A.6.7.13.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR1. GP#24 is configured if UE supports MG#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be longer than the UE measurement period as defined in clause 9.9.2.7.

Table A.6.7.13.3.1-2: RSTD accuracy test parameters

## A.6.7.13.3.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.7.13.4RSTD measurement accuracy test case with Rx TEG

A.6.7.13.4.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement when the measurements of reference cell and neighbor cell are within the same Rx TEG meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.7.13.4.1-1.

Table A.6.7.13.4.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. GP#24 is configured if UE supports GP#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

The UE is requested to provide the Rx TEG in the test via nr-UE-RxTEG-Request-r17 in NR-TDOA-RequestLocationInformation.

The test applies to the UE supporting Rx TEG defiend in NR-UE-TEG-Capability and reporting the same Rx TEG for the measurements of reference cell and neighbour cell.

Table A.6.7.13.4.1-2: RSTD accuracy test parameters

A.6.7.13.4.2Test Requirements

The RSTD measurement for Cell 1 and Cell 2 should fulfil the absolute accuracy requirements with same Rx TEG in clause 10.1.23.2.

## A.6.7.13.5NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode

## A.6.7.13.5.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement by aggregating PRS resources from multiple positioning frequency layers (PFLs) meets the measurement accuracy requirements specified in clause 10.1.23A.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.7.13.5.1-1.

Table A.6.7.13.5.1-1: Supported test configurations for PRS aggregation

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, all cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

GP#24 is configured if UE supports GP#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The UE is capable of performing RSTD measurements by aggregating PRS resources from two PFLs and is configured by the LMF to perform measurements by aggregating the PRS resources from two positioning frequency layers via nr-DL-PRS-JointMeasurementRequestedPFL-List. The NR-DL-TDOA-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

Table A.6.7.13.5.1-2: RSTD accuracy test parameters for PRS aggregation

## A.6.7.13.5.2Test Requirements

The RSTD measurement accuracy shall fulfil the requirements defined in clause 10.1.23A.2.

## A.6.7.14PRS-RSRP measurements

## A.6.7.14.1SA: measurement accuracy with PRS in FR1

## A.6.7.14.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.6.7.14.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.14.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.6.7.14.1.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.7.14.1.2-1: PRS-RSRP supported test configurations

Table A.6.7.14.1.2-2: PRS-RSRP test parameters

## A.6.7.14.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

## A.6.7.14.2SA: measurement accuracy with PRS in FR1 with reduced sample number

## A.6.7.14.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with reduced sample number is within the specified limits provided that PRS is transmitted within the active BWP of the UE. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.NsampleNsample

## A.6.7.14.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.14.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.6.7.14.2.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.7.14.2.2-1: PRS-RSRP supported test configurations

Table A.6.7.14.2.2-2: PRS-RSRP test parameters

## A.6.7.14.2.3Test Requirements

In the test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

## A.6.7.14.3Void

## A.6.7.14.3.1Void

## A.6.7.14.3.2Void

## A.6.7.14.3.3Void

## A.6.7.15UE Rx-Tx time difference measurements

## A.6.7.15.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA

## A.6.7.15.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.7.15.1.1-1.

Table A.6.7.15.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE before the start of the test.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.7.15.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.6.7.15.1.2-1.

Table A.6.7.15.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

Table A.6.7.15.1.2-2: Void

## A.6.7.15.1.3Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.6.7.15.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR1 SA

## A.6.7.15.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with reduced number of samples is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.7.15.2.1-1.

Table A.6.7.15.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE before the start of the test.

The UE is configured to measure UE Rx-Tx time difference using reduced number of samples via requestedDL-PRS-ProcessingSamples in NR-Multi-RTT-RequestLocationInformation during the test.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.7.15.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.6.7.15.2.2-1.

Table A.6.7.15.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.6.7.15.2.3Test requirements

The UE Rx-Tx time difference measurement with reduced number of samples fulfils the UE Rx-Tx measurement accuracy.

## A.6.7.15.3UE Rx-Tx time difference measurement accuracy with RxTx TEG

## A.6.7.15.3.1Test purpose and environment

The purpose of the test is to verify that the relative UE Rx-Tx time difference measurement accuracy when the two measurements are within the same RxTx TEG is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations is listed in table A.6.7.15.3.1-1.

Table A.6.7.15.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE before the start of the test.

The UE is requested to provide the RxTx TEG in the test via nr-UE-RxTxTEG-Request-r17 in NR-Multi-RTT-RequestLocationInformation.

The test applies to the UE supporting RxTx TEG defiend in NR-UE-TEG-Capability and reporting the same RxTx TEG for the two UE Rx-Tx measurements.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The UE Rx-Tx time difference is derived by the difference of the receiving timing and the transmit timing for each cell.

## A.6.7.15.3.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.6.7.15.3.2-1. y requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

Table A.6.7.15.3.2-2: UE Rx-Tx time difference measurement accuracy test parameters

## A.6.7.15.3.3Test requirements

The relative accuracy is derived by the difference of the UE Rx-Tx measurements on the two cells.

The UE Rx-Tx time difference measurements for Cell 1 and Cell 2 fulfil the relative UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.x.

## A.6.7.15.4UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA

## A.6.7.15.4.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25A. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR1.

The supported test configurations are listed in table A.6.7.15.4.1-1.

Table A.6.7.15.4.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData 37.355 [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

The general test parameters and cell specific test parameters are as given in table A.6.7.15.4.1-2 and table A.6.7.15.4.1-3 respectively.

Table A.6.7.15.4.1-2: General test parameters

Table A.6.7.15.4.1-3: Cell specific test parameters

## A.6.7.15.4.2Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25A for both Cell 1 and Cell 2.

## A.6.7.16PRS-RSRPP measurements

## A.6.7.16.1SA: measurement accuracy with PRS in FR1

## A.6.7.16.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.

## A.6.7.16.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.16.1.2-1. Both absolute accuracy of PRS-RSRPP measurements are tested by using the parameters in A.6.7.16.1.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.7.16.1.2-1: PRS-RSRPP supported test configurations

Table A.6.7.16.1.2-2: PRS-RSRPP test parameters

## A.6.7.16.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2.

## A.6.7.16.2SA: measurement accuracy with reduced PRS samples in FR1

## A.6.7.16.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy with  = 1 in FR1 is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.Nsample

The UE under test should support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the TE indicates the UE to perform positioning measurements with reduced number of samples. The PRS bandwidth is contained within the active BWP and the power difference between the serving cell SS-RSRP and neighbour cell PRS-RSRP is within 6 dB, so that = 1 is assumed.Nsample

## A.6.7.16.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.7.16.2.2-1. In all test cases, Cell 1 is the PCell.

Table A.6.7.16.2.2-1: PRS-RSRPP supported test configurations

Table A.6.7.16.2.2-2: PRS-RSRPP test parameters

A.6.7.16.2.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2.

## A.6.7.17LTM L1-RSRP measurement

## A.6.7.17.1SSB based Inter-frequency L1-RSRP accuracy requirements for neighbour cell in FR1

## A.6.7.17.1.1Test Purpose and Environment

The purpose of this test is to verify that the inter-frequency L1-RSRP measurement accuracy on neigbor cell is within the specified limits. This test will verify the requirements in clause 9.15.5 and clause 10.1.19E for inter-frequency L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.6.7.17.1.1-1.

Table A.6.7.17.1.1-1: Applicable NR configurations for FR1 SSB based inte-frequency L1-RSRP test

## A.6.7.17.1.2Test parameters

In this set of test cases there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters for the Cell 2 are given in table A.6.7.17.1.2-1 below. The absolute accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.17.1.2-1.

Measurement gap pattern configuration defined in table A.6.7.17.1.2-1 is provided. Before the test,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC)

-UE is configured one SSB resource set with one SSB resource on Cell 2

-A measurement object is configured for the RF channel 2, and it is indicated to the UE to reprort periodica reporting with with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

Table A.6.7.17.1.2-1: FR1 inter-frequency SSB based L1-RSRP test parameters

## A.6.7.17.1.3Test Requirements

The inter-frequency L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 of Cell 2) shall fulfil the requirements in clauses 10.1.19E.

## A.6.7.17.2CSI-RS based intra-frequency L1-RSRP accuracy requirement for neighbour cell

## A.6.7.17.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RS based L1-RSRP measurement accuracy on neighbour cell is within the specified requirements in clause 9.14a.5 and clause 10.1.19D.2 with the testing configurations for NR cells in table A.6.7.17.2.1-1.

Table A.6.7.17.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.6.7.17.2.2Test parameters

In this set of test cases there are two cells: NR Cell 1 as PCell and NR Cell 2 as neighbour cell. All cells are on the same frequency. The absolute and relative accuracy of CSI-RS based L1-RSRP measurement are tested with the parameters in table 6.7.17.2.2-1.

There is no measurement gap configured in the test. Before the test,

-UE is connected to Cell 1 (PCell) (PCC)

-UE is configured one CSI-RS resource set with two CSI-RS resources on Cell 2.

-A measurement object is configured indicating the UE to do periodic reporting.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with CSI-RS L1-RSRP measurement and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

Table A.6.7.17.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.6.7.17.2.3Test Requirements

The intra-frequency L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1.19D.2.

## A.6.7.18TDCP amplitude measurement accuracy

## A.6.7.18.1TDCP amplitude measurement accuracy in FR1

## A.6.7.18.1.1Test Purpose and Environment

The purpose of this test is to verify that the TRS based TDCP amplitude measurement accuracy is within the specified limits in the test requirements section. The cofigurations for the test are specified in table A.6.7.18.1.1-1.

The test consists of two tests, Test 1 and Test 2. Each test further consists of two subtests Test 1A, 1B and Test 2A, 2B.

Test 1A: 10 Hz doppler + 15 kHz SCS FDD + 20 dB SNR

Test 1B: 10 Hz doppler + 30 kHz SCS TDD + 20 dB SNR

Test 2A: 300 Hz doppler + 15 kHz SCS FDD + 10 dB SNR

Test 2B: 300 Hz doppler + 30 kHz SCS TDD + 10 dB SNR

Relevant parmeters for each test are provided in the table A.6.7.18.1.2-1. UE needs to pass Test 1A, 1B, 2A, 2B.

Table A.6.7.18.1.1-1: Applicable NR configurations for FR1 TRS based TDCP test

## A.6.7.18.1.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.18.1.2-1. Ampliutude of TDCP is tested by using the parameters in table A.6.7.18.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured with 1 TRS set with the TRS resources in the set are configured in adjacent slot. UE is configured to perform L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.6.7.18.1.2-1: FR1 TRS based TDCP test parameters

## A.6.7.18.1.3Test Requirements

For Test 1A, the reported TDCP index shall be smaller than or equal to 6 for the 80% of the times over repeated tests

For Test 1B: the reported TDCP index shall be smaller than or equal to 5 for the 80% of the times over repeated tests

For Test 2A: the reported TDCP index shall be lrager than 8 for the 80% of the times over repeated tests

For Test 2B: the reported TDCP index shall be larger than  6 for the 80% of the times over repeated tests

## A.6.7.19RSCPD Measurements

## A.6.7.19.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_CONNECTED

## A.6.7.19.1.1Test purpose and environment

The purpose of the test is to verify that accuracy of RSCPD measurement reported with RSTD measurement is within the specified limits. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.6.7.19.1.1-1.

Table A.6.7.19.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP [34] as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC CONNECTED, shall be provided to the UE before the start of the test. The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

## A.6.7.19.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.6.7.19.1.2-1.

Table A.6.7.19.1.2-1: RSCPD with UE RSTD measurement accuracy test parameters

## A.6.7.19.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy requirements specified in clause 10.1.43.2 for Cell 2.

## A.6.7.20RSCP Measurements

## A.6.7.20.1RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA

## A.6.7.20.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCP measurement with UE Rx-Tx time difference measurement is within the specified limits. This test will verify the requirements in clause 10.1.44.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.7.20.1.1-1.

Table A.6.7.20.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData , NR-Multi-RTT-RequestLocationInformation with nr-DL-PRS-RSCP-Request from LMF via LPP and NR-Multi-RTT-MeasurementCapability as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCP in RRC CONNECTED, shall be provided to the UE before the start of the test.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.7.20.1.2Test parameters

The RSCP with UE Rx-Tx time difference accuracy test parameters are given in table A.6.7.20. 1.2-1.

Table A.6.7.20.1.2-1: RSCP with UE Rx-Tx time difference measurement accuracy test parameters

## A.6.7.20.1.3Test requirements

The RSCP reported with UE Rx-Tx time difference measurement fulfils RSCP measurement accuracy specified in clause 10.1.44.2 for both Cell 1 and Cell 2.

## A.6.7.21L1 CLI measurements

## A.6.7.21.1SA L1-SRS-RSRP measurement accuracy with FR1 serving cell with SBFD

## A.6.7.21.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SRS-RSRP measurement accuracy in SBFD operation is within the specified limits. This test will verify the requirements in clauses 10.1.47.1.1 with the testing configurations for NR cell in table A.6.7.21.1.1-1.

Table A.6.7.21.1.1-1: Applicable NR configurations for FR1 L1-SRS-RSRP accuracy test

## A.6.7.21.1.2Test Parameters

In this set of test cases there is one cell in the test, FR1 PCell (Cell 1) with SBFD operation. The test parameters for the Cell 1 are given in table A.6.7.21.1.2-1 below. The test parameters for the (virtual) aggressor UE transmitting SRS are given in table A.6.7.21.1.2-2.

Before the test UE is configured to perform L1-SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in UL subband in SBFD slots according to the SRS configuration in table A.6.7.21.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted, and OCNG/Noc is transmitted additionally in PRBs in UL subband.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. At the beginning of T2, the test equipment sends a DCI to trigger UE to report L1-SRS-RSRP.

Table A.6.7.21.1.2-1: FR1 test parameters for L1-SRS-RSRP accuracy for PCell

Table A.6.7.21.1.2-2: FR1 test parameters for L1-SRS-RSRP accuracy for aggressor UE

Table A.6.7.21.1.2-3: SRS configuration parameters for FR1 L1-SRS-RSRP accuracy

## A.6.7.21.1.3Test Requirements

The L1-SRS-RSRP measurement accuracy shall fulfil the requirements in clauses 10.1.47.1.1. The rate of correct L1-SRS-RSRP measurement accuracy observed during repeated tests shall be at least 90%.

## A.6.7.21.2L1-CLI-RSSI measurement accuracy in FR1 with SBFD

## A.6.7.21.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.47.2.1 with the testing configurations for NR cells in table A.6.7.21.2.1-1.

Table A.6.7.21.2.1-1: Applicable NR configurations for FR1 L1-CLI-RSSI accuracy test

## A.6.7.21.2.2Test parameters

In this set of test cases there is one cell in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.6.7.21.2.2-1 below.

Before the test UE is configured to perform L1-CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for L1-CLI-RSSI resource. The L1-CLI-RSSI measurement resource configuration is in table A.6.7.21.2.2-2.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. At the beginning of T2, the test equipment sends an DCI to trigger UE to report L1-CLI-RSSI.

Table A.6.7.21.2.2-1: FR1 test parameters for L1-CLI-RSSI accuracy

Table A.6.7.21.2.2-2: L1-CLI-RSSI measurement resource configuration for FR1 L1-CLI-RSSI accuracy

## A.6.7.21.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the requirements in clauses 10.1.47.2.1.

## A.6.8Measurement procedure in RRC_INACTIVE

## A.6.8.1RSTD measurements

## A.6.8.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state

## A.6.8.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6.2.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.8.1.1.1-1.

Table A.6.8.1.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 1.28 s.

The general test parameters are listed in table A.6.8.1.1.1-2, and cell specific test parameters are listed in table A.6.8.1.1.1-3 and table A.6.8.1.1.1-4.

Table A.6.8.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.8.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.8.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.8.1.1.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 5.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.6.8.1.2NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA

## A.6.8.1.2.1Test Purpose and Environment

## A.6.8.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive.

The supported test configurations are specified in table A.6.8.1.2.1-1.

Table A.6.8.1.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2. PRS resources from all three cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The nr-DL-TDOA-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to requested.

The general test parameters are listed in table A.6.8.1.2.1-2, and cell specific test parameters are listed in table A.6.8.1.2.1-3 and table A.6.8.1.2.1-4.

Table A.6.8.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.8.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.8.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.8.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in section 5.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.6.8.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_INACTIVE state

## A.6.8.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation in RRC_INACTIVE state meets the requirements specified in clause 5.6.2.6 in AWGN propagation condition in FR1 in standalone scenario when two intra-band contiguous positioning frequency layers (PFL) are configured.

The supported test configurations are listed in table A.6.8.1.3.1-1.

Table A.6.8.1.3.1-1: Supported test configurations

There are 6 synchronous cells in the test: Cell 1, Cell 2, Cell 3 Cell 4, Cell 5 and Cell 6. Cell 1 is the PCell on NR RF channel 1 in FR1. Cell 2 and Cell 3 are neighbour cells on the same RF channel as Cell 1. Cell 4, Cell 5 and Cell 6 are the neighbour cells on a different NR RF channel, i.e., RF channel 2, in FR1. Cell 1 and Cell 4, Cell 2 and Cell 5, Cell 3 and Cell 6 are respectively intra-band contiguous and PRS resources are transmitted by the same Tx chain for each combination.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2, Cell 3, Cell 4, Cell 5 and Cell 6. During T2 UE shall be in RRC_INACTIVE state and all 6 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

In NR-TDOA-ProvideAssistanceData, there are three NR-linkedDL-PRS-ResourceSetID-PRS-AggregationList. The first list indicates aggregation of PRS resource sets from Cell 1 and Cell 4, and the second list indicates aggregation of PRS resource sets from Cell 2 and Cell 5. The third list indicates aggregation of PRS resource sets from Cell 3 and Cell 6. In NR-TDOA-RequestLocationInformation, the IE nr-DL-PRS-JointMeasurementRequestedPFL-List is included and indicates aggregation of PFLs on RF channel 1 and RF channel 2.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 1.28s.

The general test parameters are given in table A.6.8.1.3.1-2, and cell specific test parameters for T1 and T2 are listed in tables A.6.8.1.3.1-3 and A.6.8.1.3.1-4, respectively.

Table A.6.8.1.3.1-2: General test parameters for RSTD measurement with PRS aggregation reporting delay

Table A.6.8.1.3.1-3: Cell-specific test parameters for RSTD measurement with PRS aggregation reporting delay during T1

Table A.6.8.1.3.1-4: Cell-specific test parameters for RSTD measurement with PRS aggregation reporting delay during T2

## A.6.8.1.3.2Test requirements

The RSTD measurement time with PRS aggregation in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.2.6.

The UE shall perform and report the RSTD measurements by aggregating PRS resources from Cell 2 and Cell 5, Cell 3 and Cell 6 respectively with respect to the Cell 1 and Cell 4 from which the transmitted PRS resources are also aggregated, within the time duration specified in section 5.6.2.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events observed during repeated tests shall be at least 90%, where the reported RSTD measurement with PRS aggregation for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.3.

## A.6.8.1.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for non-RedCap UE

## A.6.8.1.4.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6.2.5 when the configured eDRX cycle is longer than 10.24s in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.8.1.4.1-1.

Table A.6.8.1.4.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. The UE is configured to report positioning measurements every 20s via reportingInterval in nr-DL-TDOA-RequestLocationInformation such the value of reportingInterval  is set to "ri20". The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 is not limited to PTW.

The UE is configured with eDRX cycle of 40.96s.

The general test parameters are listed in table A.6.8.1.4.1-2, and cell specific test parameters are listed in table A.6.8.1.4.1-3 and table A.6.8.1.4.1-4.

Table A.6.8.1.4.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.8.1.4.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.8.1.4.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.8.1.4.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of the correct events for each neighbour cell observed during the repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in the clause 10.1.23.3, i.e., between RSTD_000000000 and RSTD_126083073.

## A.6.8.2PRS-RSRP measurements

## A.6.8.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE

## A.6.8.2.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_INACTIVE meets the delay requirements specified in clause 5.6.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.8.2.1.1-1.

Table A.6.8.2.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.8.2.1.1-2, and cell specific test parameters are listed in table A.6.8.2.1.1-3.

Table A.6.8.2.1.1-2: General test parameters

Table A.6.8.2.1.1-3: Cell specific test parameters

## A.6.8.2.1.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.2.2PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE

## A.6.8.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements specified in clause 5.6.3.5 in an environment with AWGN propagation conditions when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive .

The supported test configurations are specified in table A.6. 8.2.2.1-1.

Table A.6. 8.2.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2. PRS resources from both cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-AoD assistance data and location information request.

The nr-DL-AoD-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to m1.

The general test parameters are listed in table A.6.8.2.2.1-2, and cell specific test parameters are listed in table A.6.8.2.2.1-3.

Table A.6.8.2.2.1-2: General test parameters

Table A.6.8.2.2.1-3: Cell specific test parameters

## A.6.8.2.2.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.2.3PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 with eDRX cycle > 10.24s

## A.6.8.2.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_INACTIVE with eDRX meets the delay requirements specified in clause 5.6.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.8.2.3.1-1.

Table A.6.8.2.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.8.2.3.1-2, and cell specific test parameters are listed in table A.6.8.2.3.1-3.

Table A.6.8.2.3.1-2: General test parameters

Table A.6.8.2.3.1-3: Cell specific test parameters

## A.6.8.2.3.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.3UE Rx-Tx time difference measurements

## A.6.8.3.1UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA

## A.6.8.3.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement in RRC_INACTIVE state meets the requirements specified in clause 5.6.4 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.8.3.1.1-1.

Table A.6.8.3.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.8.3.1.1-2 and table A.6.8.3.1.1-3 respectively.

Table A.6.8.3.1.1-2: General test parameters

Table A.6.8.3.1.1-3: Cell specific test parameters

## A.6.8.3.1.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.4.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.8.3.2UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR1 SA

## A.6.8.3.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 5.6.4.5 in AWGN propagation condition in FR1 in standalone scenario when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive.

The supported test configurations in listed in table A.6.8.3.2.1-1.

Table A.6.8.3.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2. PRS resources from both cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The nr-Multi-RTT-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to m1.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.6.8.3.2.1-2 and table A.6.8.3.2.1-3 respectively.

Table A.6.8.3.2.1-2: General test parameters

Table A.6.8.3.2.1-3: Cell specific test parameters

## A.6.8.3.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.8.3.3UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA

## A.6.8.3.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.4.5 for UE Rx-Tx measurements in RRC_INACTIVE with eDRX. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements on a single positioning frequency layer (PFL) in FR1.

The supported test configuration in listed in table A.6.8.3.3.1-1.

Table A.6.8.3.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The general test parameters and cell specific test parameters are as given in table A.6.8.3.3.1-2 and table A.6.8.3.3.1-3, respectively.

Table A.6.8.3.3.1-2: General test parameters

Table A.6.8.3.3.1-3: Cell specific test parameters

## A.6.8.3.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.6.8.3.4UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA

## A.6.8.3.4.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.4.6 for UE Rx-Tx measurements with PRS bandwidth aggregation. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR1.

The supported test configurations are listed in table A.6.8.3.4.1-1.

Table A.6.8.3.4.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData TS 37.355 [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The general test parameters and cell specific test parameters are as given in table A.6.8.3.4.1-2 and table A.6.8.3.4.1-3 respectively.

Table A.6.8.3.4.1-2: General test parameters

Table A.6.8.3.4.1-3: Cell specific test parameters

## A.6.8.3.4.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.6.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25A.2.

## A.6.8.4PRS-RSRPP measurements

## A.6.8.4.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state

## A.6.8.4.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the delay requirements specified in clause 5.6.5.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.8.4.1.1-1.

Table A.6.8.4.1.1-1: Supported test configurations

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and all both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.8.4.1.1-2, and cell specific test parameters are listed in table A.6.8.4.1.1-3.

Table A.6.8.4.1.1-2: General test parameters

Table A.6.8.4.1.1-3: Cell specific test parameters

## A.6.8.4.1.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.5.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.4.2PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state for reduced number of samples

## A.6.8.4.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the delay requirements specified in clause 5.6.5.5 in an environment with AWGN propagation conditions for reduced number of samples. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-Inactive is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.6.8.4.2.1-1.

Table A.6.8.4.2.1-1: Supported test configurations

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.8.4.2.1-2, and cell specific test parameters are listed in table A.6.8.4.2.1-3.

Table A.6.8.4.2.1-2: General test parameters

Table A.6.8.4.2.1-3: Cell specific test parameters

## A.6.8.4.2.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.5.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.4.3PRS-RSRPP reporting delay in RRC_INACTIVE with eDRX

## A.6.8.4.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement meets the delay requirements specified in clause 5.6.5.5 in an environment with a 2-tap channel propagation conditions in RRC_INACTIVE when configured with eDRX. The supported test configurations are specified in table A.6.8.4.3.1-1.

Table A.6.8.4.3.1-1: Supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and all both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34], shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.8.4.3.1-2, and cell specific test parameters are listed in table A.6.8.4.3.1-3.

Table A.6.8.4.3.1-2: General test parameters

Table A.6.8.4.3.1-3: Cell specific test parameters

## A.6.8.4.3.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.5.5 with Tavailable_PRS = 1.28s, starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.8.5RSCPD Measurements

## A.6.8.5.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state

## A.6.8.5.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD reported with RSTD measurement meets the requirements specified in clause 5.6.7.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The test environment is the same as in clause A.6.8.1.1 with the following additional configuration in table A.6.8.5.1.1-1 and description.

In NR-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE also is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s) to be measured within the configured time window.

Table A.6.8.5.1.1-1: Time window configuration

## A.6.8.5.1.2Test Requirements

The DL RSCPD reported with RSTD measurement time fulfils the requirements specified in clause 5.6.7.5.

The UE shall perform and report the DL RSCPD and DL RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3 and the reported RSCPD measurement for each correct event shall be within the RSCPD reporting range specified in clause 10.1.43.3.

## A.6.8.6RSCP Measurements

## A.6.8.6.1DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA

## A.6.8.6.1.1Test purpose and environment

The purpose of the test is to verify that the DL RSCP and UE Rx-Tx time difference measurements in RRC_INACTIVE state meet the requirements specified in clause 5.6.8.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured for both DL RSCP measurement and UE Rx-Tx time difference measurement.

The supported test configurations are listed in table A.6.8.6.1.1-1.

Table A.6.8.6.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData message and NR-Multi-RTT-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE during T1. In NR-Multi-RTT-RequestLocationInformation, the UE is configured to perform DL RSCP measurement via nr-DL-PRS-RSCP-Request. The UE is configured to perform both DL RSCP and UE Rx-Tx time difference measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig but the time window periodicity is not configured. The last slot containing the two messages for the multi-RTTI assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 shall be aligned with the start of the configured time window containing the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are listed in table A.6.8.6.1.1-2 and table A.6.8.6.1.1-3.

Table A.6.8.6.1.1-2: General test parameters

Table A.6.8.6.1.1-3: Cell specific test parameters

## A.6.8.6.1.2Test requirements

The DL RSCP with UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.8.

The UE shall perform and report the DL RSCP and UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified DL RSCP with UE Rx-Tx time difference measurement time specified in clause 5.6.8 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported DL RSCP measurement for each correct event shall be within the DL RSCP reporting range specified in clause 10.1.44 and the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.

## A.6.9Measurement performance requirements in RRC_INACTIVE

## A.6.9.1RSTD measurements

## A.6.9.1.1RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_INACTIVE state

## A.6.9.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.9.1.1.1-1.

Table A.6.9.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

Table A.6.9.1.1.1-2: RSTD accuracy test parameters

## A.6.9.1.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.9.1.2RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_INACTIVE state

## A.6.9.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-Inactive is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.6.9.1.2.1-1.

Table A.6.9.1.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

Table A.6.9.1.2.1-2: RSTD accuracy test parameters

## A.6.9.1.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.9.1.3RSTD measurement accuracy for PRS aggregation in FR1 in RRC_INACTIVE state

## A.6.9.1.3.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation on two PFLs meets the accuracy requirements specified in clause 10.1.23A.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.9.1.3.1-1.

Table A.6.9.1.3.1-1: Supported test configurations

In the test there are four synchronous cells: Cell 1, Cell 2, Cell 3 and Cell 4. Cell 1 is the reference as well as the PCell on NR RF channel #1 in FR1. Cell 2 is a neighbour cell on the same NR RF channel as Cell 1. Cell 3 and Cell 4 are neighbor cells in a different NR RF channel #2 in FR1. Cell 1 and Cell 3 are intra-band contiguous, and PRS resources from Cell 1 and Cell 3 are transmitted by the same Tx chain. Cell 2 and Cell 4 are intra-band contiguous, and PRS resources from Cell 2 and Cell 4 are transmitted by the same Tx chain.

The UE is configured with DRX cycle of 1.28 s.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.6.

In NR-TDOA-ProvideAssistanceData, there are two NR-linkedDL-PRS-ResourceSetID-PRS-AggregationList. The first list indicates aggregation of resource sets from Cell 1 and Cell 3, and the second list indicates aggregation of resource sets from Cell 2 and Cell 4. In NR-TDOA-RequestLocationInformation, nr-DL-PRS-JointMeasurementRequestedPFL-List is included, and indicates aggregation of PFLs on NR RF channel #1 and NR RF channel #2.

Table A.6.9.1.3.1-2: RSTD accuracy test parameters

## A.6.9.1.3.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23A.2.

## A.6.9.2PRS-RSRP measurements

## A.6.9.2.1SA: measurement accuracy with PRS in FR1 in RRC_INACTIVE

## A.6.9.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.6.9.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.9.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.6.9.2.1.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.9.2.1.2-1: PRS-RSRP supported test configurations

Table A.6.9.2.1.2-2: PRS-RSRP test parameters

## A.6.9.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

## A.6.9.2.2SA: measurement accuracy with PRS in FR1 with reduced number of samples in RRC_INACTIVE state

## A.6.9.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy is within the specified limits provided that PRS is transmitted within the initial BWP of the UE. UE can support supportedDL-PRS-ProcessingSamples-RRC-Inactive, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.NsampleNsample

## A.6.9.2.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.9.2.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.6.9.2.2.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.9.2.2.2-1: PRS-RSRP supported test configurations

Table A.6.9.2.2.2-2: PRS-RSRP test parameters

## A.6.9.2.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

## A.6.9.3UE Rx-Tx time difference measurements

## A.6.9.3.1.1UE Rx-Tx time difference measurement accuracy in FR1 SA

## A.6.9.3.1.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario.

The supported test configurations in listed in table A.6.9.3.1.1.1-1.

Table A.6.9.3.1.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE before the start of the test.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.9.3.1.1.2 Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.6.9.3.1.1.1-1.

Table A.6.9.3.1.1.1-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.6.9.3.1.1.3Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.6.9.3.2UE Rx-Tx time difference measurement accuracy with reduced number of samples

## A.6.9.3.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with reduced number of samples in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.6.9.3.2.1-1.

Table A.6.9.3.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.12.1], shall be provided to the UE before the start of the test. The UE is configured to measure UE Rx-Tx time difference using reduced number of samples via requestedDL-PRS-ProcessingSamples in NR-Multi-RTT-RequestLocationInformation.

UE shall be configured to enter into RRC_INACTIVE state before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.9.3.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.6.9.3.2.2-1.

Table A.6.9.3.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.6.9.3.2.3Test requirements

The UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE state fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.6.9.3.3UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA

## A.6.9.3.3.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25A. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR1.

The supported test configurations are listed in table A.6.9.3.3.1-1.

Table A.6.9.3.3.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData TS 37.355 [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

The general test parameters and cell specific test parameters are as given in table A.6.9.3.3.1-2 and table A.6.9.3.3.1-3, respectively.

Table A.6.9.3.3.1-2: General test parameters

Table A.6.9.3.3.1-3: Cell specific test parameters

## A.6.9.3.3.2Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25A for both Cell 1 and Cell 2.

## A.6.9.4PRS-RSRPP measurements

## A.6.9.4.1SA: PRS-RSRPP measurement accuracy in FR1 in RRC INACTIVE

## A.6.9.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in FR1 in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.

## A.6.9.4.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.9.4.1.2-1. In all test cases, Cell 1 is the PCell.

Table A.6.9.4.1.2-1: PRS-RSRPP supported test configurations

Table A.6.9.4.1.2-2: PRS-RSRPP test parameters

## A.6.9.4.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2.

## A.6.9.4.2SA: measurement accuracy with reduced PRS samples in FR1 in RRC INACTIVE

## A.6.9.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy with  = 1 in FR1 in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.The UE under test should support supportedDL-PRS-ProcessingSamples-RRC-Inactive, and the TE indicates the UE to perform positioning measurements with reduced number of samples. The PRS bandwidth is contained within the initial DL BWP and the power difference between the serving cell SS-RSRP and neighbour cell PRS-RSRP is within [6]dB, so that = 1 is assumed.NsampleNsample

## A.6.9.4.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.9.4.2.2-1. Both absolute and relative accuracy of PRS-RSRPP measurements are tested by using the parameters in A.6.9.4.2.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.9.4.2.2-1: PRS-RSRPP supported test configurations

Table A.6.9.4.2.2-2: PRS-RSRPP test parameters

## A.6.9.4.2.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2.

## A.6.9.5RSCPD Measurements

## A.6.9.5.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_INACTIVE

## A.6.9.5.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCPD measurement reported with RSTD measurement accuracy in RRC_INACTIVE. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.6.9. 5.1.1-1.

Table A.6.9. 5.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC_INACTIVE shall be provided to the UE before the start of the test. The UE is configured with DRX cycle of 1.28s.

## A.6.9.5.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.6.9.5.1.2-1.

Table A.6.9. 5.1.2-1: RSCPD with UE RSTD measurement accuracy test parameters

## A.6.9.5.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy requirements specified in clause 10.1.43.2 for Cell 2.

## A.6.9.6RSCP Measurements

## A.6.9.6.1RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA

## A.6.9.6.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCP measurement reported with UE Rx-Tx time difference measurement in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clause 10.1.44.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.6.9.6.1.1-1.

Table A.6.9.6.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData , NR-Multi-RTT-RequestLocationInformation with nr-DL-PRS-RSCP-Request from LMF via LPP and NR-Multi-RTT-MeasurementCapability as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCP in RRC INACTIVE, shall be provided to the UE before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.6.9.6.1.2Test parameters

The RSCP with UE Rx-Tx time difference accuracy test parameters are given in table A.6.9.6.1.2-1.

Table A.6.9.6.1.2-1: RSCP with UE Rx-Tx time difference measurement accuracy test parameters

## A.6.9.6.1.3Test requirements

The RSCP with UE Rx-Tx time difference measurement fulfils RSCP measurement accuracy specified in clause 10.1.44.2 for both Cell 1 and Cell 2.

## A.6.10Measurement Procedure in RRC_IDLE

## A.6.10.1RSTD Measurements

## A.6.10.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE

## A.6.10.1.1.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 4.5.2.5 for RSTD measurements in RRC_IDLE without eDRX. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR1.

The supported test configurations are listed in table A.6.10.1.1.1-1.

Table A.6.10.1.1.1-1: Supported test configurations

There are three cells in the test: Cell 1 (PCell and RSTD reference cell), Cell 2 (neighbor cell) and Cell 3 (neighbor cell). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and released to RRC_IDLE state before the start of T2. All cells transmit PRS only during the second time interval of duration T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the start of the first PRS resource instance received after the UE has transitioned to RRC_IDLE.

The general test parameters are listed in table A.6. 10.1.1.1-2 and cell specific test parameters are listed in table A.6.10.1.1.1-3 and table A.6.10.1.1.1-4.

Table A.6.10.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.10.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.10.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.6.10.1.1.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 4.5.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3.

## A.6.10.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s for non-RedCap UE

## A.6.10.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_IDLE state meets the requirements specified in clause 4.5.2.5 when eDRX cycle is longer than 10.24s in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.6.10.1.2.1-1.

Table A.6.10.1.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_IDLE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. The UE is configured to report positioning measurements every 20s by setting the value of reportingInterval to "ri20" in nr-DL-TDOA-RequestLocationInformation. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 is not limited to PTW.

The general test parameters are listed in table A.6.10.1.2.1-2, and cell specific test parameters are listed in table A.6.10.1.2.1-3 and table A.6.10.1.2.1-4.

Table A.6.10.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.6.10.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.6.10.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2.

## A.6.10.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 4.5.2.5. The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 4.5.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during the repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in the clause 10.1.23.3, i.e., between RSTD_000000000 and RSTD_126083073.

## A.6.10.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_IDLE state

## A.6.10.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation in RRC_IDLE state meets the requirements specified in clause 4.5.2.6 in AWGN propagation condition in FR1 in standalone scenario when two intra-band contiguous positioning frequency layers (PFLs) are configured.

The test environment and configurations reuse the test case for RRC_INACTIVE state defined in clause A.6.8.1.3 except that UE shall be in RRC_IDLE state and all 6 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP during T2.

## A.6.10.1.3.2Test requirements

The RSTD measurement time with PRS aggregation in RRC_IDLE state fulfils the requirements specified in clause 4.5.2.6.

The UE shall perform and report the RSTD measurements by aggregating PRS resources from Cell 2 and Cell 5, Cell 3 and Cell 6 respectively with respect to the Cell 1 and Cell 4 from which the transmitted PRS resources are also aggregated, within the time duration specified in clause 4.5.2.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events observed during repeated tests shall be at least 90%, where the reported RSTD measurement with PRS aggregation for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.3.

## A.6.10.2PRS-RSRP Measurements

## A.6.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR1

## A.6.10.2.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE state meets the delay requirements specified in clause 4.5.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.10.2.1.1-1.

Table A.6.10.2.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34], shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_IDLE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.6.10.2.1.1-2, and cell specific test parameters are listed in table A.6.10.2.1.1-3.

Table A.6.10.2.1.1-2: General test parameters

Table A.6.10.2.1.1-3: Cell specific test parameters

## A.6.10.2.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 4.5.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in section 4.5.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.6.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s

## A.6.10.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE with eDRX meets the delay requirements specified in clause 4.5.3.5 in an environment with AWGN propagation conditions.

The supported test configurations in table A.6.8.2.3.1-1 apply for this test.

The test procedure in clause A.6.8.2.3.1 apply for this test, except that during T2, UE is in RRC_IDLE state.

The general test parameters as specified in table A.6.8.2.3.1-2 apply for this test, except those specified in table A.6.10.2.2.1-1.

The cell specific test parameters as specified in table A.6.8.2.3.1-3 apply for this test.

Table A.6.10.2.2.1-1: General test parameters

## A.6.10.2.2.2Test Requirements

The test requirements in clause A.6.8.2.3.2 apply for this test, except that the time limits are specified in clause 4.5.3.5.

## A.6.10.3RSCPD Measurements

## A.6.10.3.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state

## A.6.10.3.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD reported with RSTD measurement meets the requirements specified in clause 5.6.7.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The test environment is the same as in A.6.8.1.1 with the following additional configuration in table A.6. 10.3.1.1-1 and description.

In NR-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE also is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s) to be measured within the configured time window.

Table A.6.10.3.1.1-1: Time window configuration

## A.6.10.3.1.2Test Requirements

The DL RSCPD reported with RSTD measurement time fulfils the requirements specified in clause 5.6.7.5.

The UE shall perform and report the DL RSCPD and DL RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3 and the reported RSCPD measurement for each correct event shall be within the RSCPD reporting range specified in clause 10.1.43.3.

## A.6.11Measurement Performance Requirements in RRC_IDLE

## A.6.11.1RSTD Measurements

## A.6.11.1.1NR RSTD measurement accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE

## A.6.11.1.1.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement in RRC_IDLE state without eDRX meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are listed in table A.6.11.1.1.1-1.

Table A.6.11.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

The RSTD accuracy test parameters are listed in table A.6.11.1.1.1-2.

Table A.6.11.1.1.1-2: RSTD accuracy test parameters

## A.6.11.1.1.2Test requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.11.1.2RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_IDLE state with eDRX>10.24s for non-RedCap UE

## A.6.11.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement performed by UE in RRC_IDLE state with eDRX > 10.24s meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.6.11.1.2.1-1.

Table A.6.11.1.2.1-1: Supported test configurations.

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with eDRX cycle of 40.96s. The UE is configured to report positioning measurements every 20s by setting the value of reportingInterval to "ri20" in nr-DL-TDOA-RequestLocationInformation. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.5.2.5.

Table A.6.11.1.2.1-2: RSTD accuracy test parameters.

## A.6.11.1.2.2Test Requirements

The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval. The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.6.11.1.3NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_IDLE state

## A.6.11.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement results with PRS aggregation in RRC_IDLE state meets the requirements specified in clause 10.1.23A.2 in AWGN propagation condition in FR1 in standalone scenario when two intra-band contiguous positioning frequency layers (PFLs) are configured.

The test environment and configurations reuse the test case for RRC_INACTIVE state defined in clause A.6.9.1.3, except that UE shall be in RRC_IDLE state and all 4 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP during T2.

## A.6.11.1.3.2Test requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23A.2.

## A.6.11.2PRS-RSRP measurements

## A.6.11.2.1PRS-RSRP measurement accuracy test case for non-RedCap UE in FR1 in RRC_IDLE state

## A.6.11.2.1.1Test Purpose and Environment

The purpose of this test is to verify accuracy of PRS-RSRP measurement performed by UE in RRC_IDLE mode in FR1.

## A.6.11.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.6.11.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.6.11.2.1.2-2. In all test cases, Cell 1 is the PCell.

Table A.6.11.2.1.2-1: PRS-RSRP supported test configurations

Table A.6.11.2.1.2-2: PRS-RSRP test parameters

## A.6.11.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

## A.6.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s

## A.6.11.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE with eDRX meets the accuracy requirements specified in clauses 10.1.24.2.1 and 10.1.24.2.2 in an environment with AWGN propagation conditions.

## A.6.11.2.2.2Test parameters

The supported test configurations in table A.6.9.2.1.2-1 apply for this test.

The test procedure in clause A.6.9.2.1.2 apply for this test, except that UE is in RRC_IDLE state.

The test parameters as specified in table A.6.9.2.1.2-2 apply for this test, except those additionally specified in table A.6.11.2.2.2-1.

Table A.6.11.2.2.2-1: PRS-RSRP test parameters

## A.6.11.2.2.3Test Requirements

The test requirements in clause A.6.9.2.1.3 apply for this test.

## A.6.11.3RSCPD Measurements

## A.6.11.3.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_IDLE

## A.6.11.3.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCPD measurement reported with RSTD measurement in RRC_IDLE. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.6.11.3.1.1-1.

Table A.6.11.3.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC_IDLE shall be provided to the UE before the start of the test. The UE is configured with DRX cycle of 1.28s.

## A.6.11.3.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.6.11.3.1.2.-1.

Table A.6.11.3.1.2-1: RSCPD with UE RSTD measurement accuracy test parameters

## A.6. 11.3.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy specified in clause 10.1.43.2 for Cell 2.
