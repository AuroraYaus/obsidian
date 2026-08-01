---
type: spec
aliases:
  - 38.133_38133-j50_sA.706-A.711
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.706-A.711/content.md"
---
# TS 38.133 38133-j50_sA.706-A.711

## A.7.6Measurement procedure

## A.7.6.1Intra-frequency Measurements

## A.7.6.1.1SA event triggered reporting test without gap under non-DRX

## A.7.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.1.1-1.

Table A.7.6.1.1.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.1.1-2, A.7.6.1.1.1-3 and A.7.6.1.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Figure A.7.6.1.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.2SA event triggered reporting test without gap under DRX

## A.7.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.2.1-1.

Table A.7.6.1.2.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.2.1-2 ~ 6.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.1.2.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.1.2.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.1.2.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.1.2.1-5: Void

Table A.7.6.1.2.1-6: Void

## A.7.6.1.2.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-7.2 s for a UE supporting power class 1,

-4.32 s for a UE supporting power class 2, 3 and 4

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-51.2 s for a UE supporting power class 1,

-30.72 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.3SA event triggered reporting test with per-UE gaps under non-DRX

## A.7.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.3.1-1.

Table A.7.6.1.3.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.3.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.3.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Table A.7.6.1.3.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Table A.7.6.1.3.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Figure A.7.6.1.3.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.3.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3.2 s for a UE supporting power class 1,

-1.92 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.4SA event triggered reporting test with per-UE gaps under DRX

## A.7.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.4.1-1.

Table A.7.6.1.4.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.4.1-2, A.7.6.1.4.1-3 and A.7.6.1.4.1-4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.1.4.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.7.6.1.4.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.7.6.1.4.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.7.6.1.4.1-5: Void

Table A.7.6.1.4.1-6:Void

## A.7.6.1.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-7.2 s for a UE supporting power class 1,

-4.32 s for a UE supporting power class 2, 3 and 4

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-51.2 s for a UE supporting power class 1,

-30.72 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.5SA event triggered reporting test without gap under non-DRX for UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17 in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.5.1-1.

Table A.7.6.1.5.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.5.1-2, A.7.6.1.5.1-3 and A.7.6.1.5.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.5.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.5.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.5.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Figure A.7.6.1.5.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.5.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1140 ms from the beginning of time period T2.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.6SA event triggered reporting test without gap under non-DRX for FR2-2

## A.7.6.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.6.1-1.

Table A.7.6.1.6.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.6.1-2, A.7.6.1.6.1-3 and A.7.6.1.6.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.6.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.7.6.1.6.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.7.6.1.6.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Figure A.7.6.1.6.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.6.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

-2.4 s (60*20 ms+60*20 ms)for a UE supporting power class 1,

-1.44 s (36*20 ms+36*20 ms) for a UE supporting power class 2 and 3

For Configuration 2，

-3.6 s (120*20 ms+60*20 ms) for a UE supporting power class 1,

-2.16 s (72*20 ms+36*20 ms) for a UE supporting power class 2 and 3

For Configuration 3，

-4.8 s (180*20 ms+60*20 ms) for a UE supporting power class 1,

-2.88 s (108*20 ms+36*20 ms) for a UE supporting power class 2 and 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.7SA event triggered reporting test without gap under DRX for FR2-2

## A.7.6.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.7.1-1.

Table A.7.6.1.7.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.7.1-2 ~ 6.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.1.7.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap with DRX

Table A.7.6.1.7.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap with DRX

Table A.7.6.1.7.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap with DRX

## A.7.6.1.7.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

-7.2 s (60*40 ms*1.5 +60*40 ms*1.5) for a UE supporting power class 1,

-4.32 s (36*40 ms*1.5 + 36*40 ms*1.5) for a UE supporting power class 2 and 3

For Configuration 2,

-10.8 s (120*40 ms*1.5 +60*40 ms*1.5) for a UE supporting power class 1,

-6.48 s (72*40 ms*1.5 + 36*40 ms*1.5)  for a UE supporting power class 2 and 3

For Configuration 3,

-14.4 s (180*40 ms*1.5 + 60*40 ms*1.5) for a UE supporting power class 1,

-8.64 s (108*40 ms*1.5 + 36*40 ms*1.5)  for a UE supporting power class 2 and 3

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

-76.8 s (60*640 ms +60*640 ms) for a UE supporting power class 1,

-46.08 s (36*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

For Configuration 2,

-115.2 s (120*640 ms +60*640 ms) for a UE supporting power class 1,

-69.12 s (72*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

For Configuration 3,

-153.6 s (180*640 ms + 60*640 ms) for a UE supporting power class 1,

-92.16 s (108*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.8SA event triggered reporting test with per-UE gaps under non-DRX for FR2-2

## A.7.6.1.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.8.1-1.

Table A.7.6.1.8.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.8.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.8.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Table A.7.6.1.8.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Table A.7.6.1.8.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Figure A.7.6.1.8.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.8.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1，

-4.8 s (60*40 ms+60*40 ms) for a UE supporting power class 1,

-2.88 s (36*40 ms+36*40 ms) for a UE supporting power class 2 and 3

For Configuration 2，

-7.2 s (120*40 ms+60*40 ms) for a UE supporting power class 1,

-4.32 s (72*40 ms+36*40 ms) for a UE supporting power class 2 and 3

For Configuration 3，

-9.6 s (180*40 ms+60*40 ms) for a UE supporting power class 1,

-5.76 s (108*40 ms+36*40 ms) for a UE supporting power class 2 and 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.9SA event triggered reporting test with per-UE gaps under DRX for FR2-2

## A.7.6.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.9.1-1.

Table A.7.6.1.9.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.9.1-2, A.7.6.1.9.1-3 and A.7.6.1.9.1-4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.1.9.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps with DRX

Table A.7.6.1.9.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps with DRX

Table A.7.6.1.9.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps with DRX

## A.7.6.1.9.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

-7.2 s (60*40 ms*1.5 +60*40 ms*1.5) for a UE supporting power class 1,

-4.32 s (36*40 ms*1.5 + 36*40 ms*1.5) for a UE supporting power class 2 and 3

For Configuration 2,

-10.8 s (120*40 ms*1.5 +60*40 ms*1.5) for a UE supporting power class 1,

-6.48 s (72*40 ms*1.5 + 36*40 ms*1.5) for a UE supporting power class 2 and 3

For Configuration 3,

-14.4 s (180*40 ms*1.5 + 60*40 ms*1.5) for a UE supporting power class 1,

-8.64 s (108*40 ms*1.5 + 36*40 ms*1.5) for a UE supporting power class 2 and 3

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

-76.8 s (60*640 ms +60*640 ms) for a UE supporting power class 1,

-46.08 s (36*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

For Configuration 2,

-115.2 s (120*640 ms +60*640 ms) for a UE supporting power class 1,

-69.12 s (72*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

For Configuration 3,

-153.6 s (180*640 ms + 60*640 ms) for a UE supporting power class 1,

-92.16 s (108*640 ms + 36*640 ms) for a UE supporting power class 2 and 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.10SA event triggered reporting test with SSB time index detection without gap under non-DRX for FR2-2

## A.7.6.1.10.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.10.1-1.

Table A.7.6.1.10.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.10.1-2, A.7.6.1.10.1-3 and A.7.6.1.10.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.10.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.7.6.1.10.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.7.6.1.10.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Figure A.7.6.1.10.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.10.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-6.24 s (180*20 ms + 60*20 ms +72*20 ms) for a UE supporting power class 1,

-3.84 s (108*20 ms + 36*20 ms +48*20 ms) for a UE supporting power class 2 and 3

The UE is required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.11SA event triggered reporting test with SSB time index detection with per-UE gaps under non-DRX for FR2-2

## A.7.6.1.11.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.11.1-1.

Table A.7.6.1.11.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.11.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.11.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Table A.7.6.1.11.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Table A.7.6.1.11.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 with per-UE gaps without DRX

Figure A.7.6.1.11.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.11.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-12.48 s (180*40 ms +60*40 ms) for a UE supporting power class 1,

-7.68 s (108*40 ms + 36*40 ms) for a UE supporting power class 2 and 3

The UE is required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.12SA event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP

## A.7.6.1.12.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of an event when CD-SSB is outside active BWP. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.1.1-1.

The test environment is the same as in A.7.6.1.1 with following exceptions in table A.7.6.1.1.1-3.

Table A.7.6.1.12.1-1: NR Cell specific test parameters for intra-frequency event triggered reporting without gap under non-DRX when CD-SSB is outside active BWP

## A.7.6.1.12.2Test Requirements

The test requirements are the same as in A.7.6.1.1.2.

## A.7.6.1.13SA event triggered reporting test without gap under non-DRX with NCD-SSB

## A.7.6.1.13.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements when NCD-SSB is configured in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.13.1-1.

Table A.7.6.1.13.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.13.1-2, A.7.6.1.13.1-3 and A.7.6.1.13.1-4 below.

The CD-SSB is configured outside active DL BWP and NCD-SSB is configured fully within active DL BWP of FR1 PCell. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.13.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.13.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.13.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Figure A.7.6.1.13.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.13.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-9.6s for a UE supporting power class 1,

-5.76s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.14SA event triggered reporting test without gap under non-DRX for power class 6 UE supporting measEnhCAInterFreqFR2-r18

## A.7.6.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the FR2 power class 6 UE makes correct reporting of an event. This test will partly verify the SA SCC intra-frequency NR cell measurement requirements specified in clause 9.2.5 for FR2 power class 6 UE supporting measEnhCAInterFreqFR2-r18 and configured with highSpeedMeasFlagFR2-r17.

Three cells are deployed in the test: one FR2 PCell (Cell 1) on NR RF channel 1, one FR2 SCell (Cell 2) on NR RF channel 2, and one neighbouring cell (Cell 3) on NR RF channel 2. The supported test configurations are given in table A.7.6.1.14.1.1-1. The test parameters are given in tables A.7.6.1.14.1.1-2 and cell-specific parameters in A.7.6.1.14.1.1-3 below.

In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used.

This test consists of two successive time periods, with time durations of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.7.6.1.14.1-1 Test configuration

Table A.7.6.1.14.1-2: General test parameters

Table A.7.6.1.14.1-3: Cell specific test parameters

## A.7.6.1.14.2Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.15SA event triggered reporting test without gap for SCell under non-DRX based on OD-SSB

## A.7.6.1.15.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements for OD-SSB based measurement in clauses 9.17.5.1 and 9.17.5.2. Supported test configurations are shown in table A.7.6.1.15.1-1.

Table A.7.6.1.15.1-1: supported test configurations

There are three cells in the test, which are PCell (Cell 1), FR2 neighbour cell (Cell 2) and a FR2 SCell (Cell 3) on the same frequency as the PCell(Cell 1). The test parameters for the Cell 1, Cell 2 and Cell 3 are given in tables A.7.6.1.15.1-2, A.7.6.1.15.1-3 and A.7.6.1.15.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.15.1-2: General test parameters for intra-frequency event triggered reporting for SA with both TDD PCell and SCell in FR2 without gap without DRX

Table A.7.6.1.15.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with both TDD PCell and SCell in FR2 without gap without DRX

Table A.7.6.1.15.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with both TDD PCell and SCell in FR2 without gap without DRX

Figure A.7.6.1.15.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.15.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.16SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB

## A.7.6.1.16.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event based on OD-SSB measurement on deactivated SCell. This test will partly verify the TDD intra-frequency cell identification for deactivated SCell requirements as defined in clause 9.17.5 and interruption requirements at OD-SSB activation as defined in clause 8.2.2.2.22. Supported test configurations are shown in table A.7.6.1.16.1-1.

Table A.7.6.1.16.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 Sell (Cell 2). The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.16.1-2, A.7.6.1.16.1-3 and A.7.6.1.16.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A1 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. Before T2, Cell2 is added as SCell via SCell addition and remains deactivated. During time duration T1, the UE shall not have any timing information of Cell 2. TE sends OD-SSB activation from the start of T2 and Cell 2 is detectable from the start of T2.

The test equipment also verifies that potential interruption by monitoring ACK/NACK sent in PCell during T2.

Table A.7.6.1.16.1-2: General test parameters for intra-frequency event triggered reporting for deactivated SCell based on OD-SSB

Table A.7.6.1.16.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for deactivated SCell based on OD-SSB

Table A.7.6.1.16.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for deactivated SCell based on OD-SSB

## A.7.6.1.16.2Test Requirements

In the test, the UE shall send one Event A1 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-THARQ+3+ OD-SSB post processing time + 800 for a UE supporting power class 1

-THARQ+3+ OD-SSB post processing time +480 for a UE supporting power class 2, 3, 4

The interruption of PCell due to activation of OD-SSB shall not be more than the values specified for NR SA in clause 8.2.2.2.22.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.17SA event triggered reporting test under non-DRX on Rx BSF optimization for SSB based intra-frequency measurement without MG

## A.7.6.1.17.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting fastRx-BSF-MeasDelayReduction-r19 makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements based on reduced RX beam sweeping factor reported by fastRx-BSF-MeasDelayReduction-r19 in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.1.17.1-1.

Table A.7.6.1.17.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.17.1-2, A.7.6.1.17.1-3 and A.7.6.1.17.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.1.17.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.17.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.1.17.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

## A.7.6.1.17.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-Tidentify_intra_without_index as defined in clause 9.2.5.1 based on Nreduced_Rx_BSF by UE capability fastRx-BSF-MeasDelayReduction-r19 for a UE supporting power class 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.18SA event triggered reporting test with per-UE gaps under DRX for UE supporting multi-Rx based L3 measurement in FR2

## A.7.6.1.18.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting fastRx-BSF-MeasDelayReduction-r19 makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6. Supported test configurations are shown in table A.7.6.1.18.1-1.

Table A.7.6.1.18.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.18.1-2, A.7.6.1.18.1-3 and A.7.6.1.18.1-4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 1 RSRP will not below the fbs-ThresholdP-r19 value. At the beginning of the T2, the RSRP value of Cell 1 and Cell 2 will be changed as given in Table A.7.6.1.18.1-4.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.1.18.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.7.6.1.18.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.7.6.1.18.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

## A.7.6.1.18.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 1002 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 2.

## 1422 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 4.

## 2162 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 6.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 7682 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 2.

## 15362 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 4.

## 23042 ms for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 6.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.1.19SA event triggered reporting test without gap under non-DRX for UE configured with cssf-Config

## A.7.6.1.19.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2 based on the enhanced CSSFoutside,gap by measuring one serving carrier per FR2 band. Supported test configurations are shown in table A.7.6.1.19.1-1.

Table A.7.6.1.19.1-1: supported test configurations

There are four cells in the test, one FR1 PCell (Cell 1), two FR2 SCells (Cell 2 and Cell 3) and a FR2 neighbor cell (Cell 4). All the FR2 cells i.e. Cell2, Cell3 and Cell4 are on the same band. The FR2 neighbor cell is on the same frequency as one FR2 SCell (Cell 2). The test parameters for Cell 1 are defined in A.6.6.1. The test parameters for the Cell 2, Cell 3 and Cell 4 are given in table A.7.6.1.19.1-2, A.7.6.1.19.1-3 and A.7.6.1.19.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell and two SCells respectively, and it is indicated to the UE that event-triggered reporting with Event A3 is used. In addition, UE is indicated to perform the measurement on the SCC corresponding to Cell 2 via cssf-MeasMO-List.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. At the beginning of T1 the UE receives an RRC message by which the SCells (Cell 2 and Cell 3) becomes configured on NR. UE is indicated to perform enhanced measurement by measuring the SCC as indicated by cssf-MeasMO-List per band. During time duration T1, the UE shall not have any timing information of Cell 4.

Table A.7.6.1.19.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR1 without gap without DRX

Table A.7.6.1.19.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR1 without gap without DRX

Table A.7.6.1.19.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR1 without gap without DRX

Figure A.7.6.1.19.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.1.19.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2Inter-frequency Measurements

## A.7.6.2.1SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR2)

## A.7.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.1.1-1, A.7.6.2.1.1-2, and A.7.6.2.1.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.1.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.1.1-1.

Table A.7.6.2.1.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

The  UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.2SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR2)

## A.7.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.2.1-1, A.7.6.2.2.1-2, and A.7.6.2.2.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.2.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.2.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.2.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting without SSB time index detection

## A.7.6.2.2.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2  the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.3SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR2)

## A.7.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.3.1-1, A.7.6.2.3.1-2, and A.7.6.2.3.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.3.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.3.1-1.

Table A.7.6.2.3.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.7.6.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.7.6.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

## A.7.6.2.3.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

The UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.4SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2)

## A.7.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.4.1-1, A.7.6.2.4.1-2, and A.7.6.2.4.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.4.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.4.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.4.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.7.6.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.7.6.2.4.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting with SSB time index detection

## A.7.6.2.4.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.5SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1)

## A.7.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.5.1-1, A.7.6.2.5.1-2, and A.7.6.2.5.1-3.

In test 1 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.5.1-2 is provided for a UE that does not support per-FR gap and in test 2 no gap pattern is configured as defined in table A.7.6.2.5.1-2. If the UE supports per-FR gap, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.5.1-1.

Table A.7.6.2.5.1-1 SA event triggered reporting tests without SSB index reading for FR1-FR2

Table A.7.6.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.5.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

In test 2, without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 2560 for UE supporting power class 1, or

## 1600 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.6SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR1)

## A.7.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.6.1-1, A.7.6.2.6.1-2, and A.7.6.2.6.1-3.

In test 1&2 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.6.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 no gap pattern is configured as defined in table A.7.6.2.6.1-2. If a UE supports per-FR gap it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.6.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.6.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR2

Table A.7.6.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.6.2Test Requirements

In test 1 with per-UE gap and in test 3 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.7SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1)

## A.7.6.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

n this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.7.1-1, A.7.6.2.7.1-2, and A.7.6.2.7.1-3.

In test 1 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.7.1-2 is provided for a UE that does not support per-FR gap and in test 2 measurement no gap pattern is configured as defined in table A.7.6.2.7.1-2. If the UE supports per-FR gap, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.7.1-1.

Table A.7.6.2.7.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR2

Table A.7.6.2.7.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.7.6.2.7.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

## A.7.6.2.7.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

In test 2 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 3360 for UE supporting power class 1, or

## 2080 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.8SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1)

## A.7.6.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.8.1-1, A.7.6.2.8.1-2, and A.7.6.2.8.1-3.

In test 1&2 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.8.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 measurement no gap pattern is configured as defined in table A.7.6.2.8.1-2.If a UE supports per-FR gap , it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.8.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.8.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR2

Table A.7.6.2.8.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.7.6.2.8.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

## A.7.6.2.8.2Test Requirements

In test 1 with per-UE gap and in test 3 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.9SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17)

## A.7.6.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.9.1-1, A.7.6.2.9.1-2, and A.7.6.2.9.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.9.1-1.

Table A.7.6.2.9.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection (GP17)

Table A.7.6.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection (GP17)

## A.7.6.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 5120 ms (PC1) or 3200 ms (other than PC1) from the beginning of time period T2.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.10SA event triggered reporting test without gap under non-DRX

## A.7.6.2.10.1Test Purpose and Environment

The purpose of this test is to verify that if UE supports interFrequencyMeas-NoGap-r16 and the flag interFrequencyConfig-NoGap-r16 is configured by the network, the UE makes correct reporting of an event. This test will partly verify the inter-frequency without gap cell search requirements in clause 9.3.9. Supported test configurations are shown in table A.7.6.2.10.1-1.

Table A.7.6.2.10.1-1: supported test configurations

There are two cells in the test, NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from cell 1 and cell 2 should be different in frequency location within the cell bandwidth.  The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.2.10.1-2, A.7.6.2.10.1-3 and A.7.6.2.10.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.2.10.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.2.10.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.2.10.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

## A.7.6.2.10.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.11SA event triggered reporting test without gap under DRX

## A.7.6.2.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD inter-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.2.11.1-1.

Table A.7.6.2.11.1-1: supported test configurations

There are two cells in the test: PCell (Cell 1) on NR RF channel 1 and a FR2 neighbour cell (Cell 2) on NR RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from cell 1 and cell 2 should be different in frequency location within the cell bandwidth. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.2.11.1-2 ~ 6.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.11.1-2: General test parameters for inter-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.2.11.1-3: NR Cell specific test parameters for inter-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.2.11.1-4: NR OTA Cell specific test parameters for inter-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

## A.7.6.2.11.2Test Requirements

In test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-51.2 s for a UE supporting power class 1,

-30.72 s for a UE supporting power class 2, 3 and 4est

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.12SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR2-2)

## A.7.6.2.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.1.12-1, A.7.6.2.12.1-2, and A.7.6.2.12.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.12.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.12.1-1.

Table A.7.6.2.12.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.2.12.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

Table A.7.6.2.12.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

## A.7.6.2.12.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

## 7.68 s (96*40 ms + 96*40 ms) for UE supporting power class 1, or

## 4.8 s (60*40 ms +60*40 ms) for UE supporting other power class.

For Configuration 2,

## 11.52 s (192*40 ms + 96*40 ms) for UE supporting power class 1, or

## 7.2 s (120*40 ms +60*40 ms) for UE supporting other power class.

For Configuration 3,

## 15.36 s (288*40 ms + 96*40 ms) for UE supporting power class 1, or

## 9.6 s (180*40 ms +60*40 ms) for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.13SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR2-2)

## A.7.6.2.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.63.2.13.1-1, A.7.6.2.13.1-2, and A.7.6.2.13.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.13.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2132.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.13.1-1: SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.2.13.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

Table A.7.6.2.13.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting without SSB time index detection

## A.7.6.2.13.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

For Configuration 1,

## 11.52 s (96*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 7.2 s (60*40 ms*1.5 + 60*40 ms*1.5) for UE supporting other power class.

For Configuration 2,

## 17.28 s (192*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 10.80 s (120*40 ms*1.5 + 60*40 ms*1.5) for UE supporting other power class.

For Configuration 3,

## 23.04 s (288*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 14.40 s (180*40 ms*1.5 + 60*40 ms*1.5)  for UE supporting other power class.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

For Configuratiojn 1,

## 122.88 s (96*640 ms + 96*640 ms) for UE supporting power class 1, or

## 76.80 s (60*640 ms + 60*640 ms) for UE supporting other power class.

For Configuratiojn 2,

## 184.32 s (192*640 ms + 96*640 ms) for UE supporting power class 1, or

## 115.20 s (120*640 ms + 60*640 ms) for UE supporting other power class.

For Configuratiojn 3,

## 245.76 s (288*640 ms + 96*640 ms) for UE supporting power class 1, or

## 153.60 s (180*640 ms + 60*640 ms) for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.14SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR2-2)

## A.7.6.2.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.14.1-1, A.7.6.2.14.1-2, and A.7.6.2.14.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.14.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.14.1-1.

Table A.7.6.2.14.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.7.6.2.14.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

Table A.7.6.2.14.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

## A.7.6.2.14.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

## 10.56 s (96*40 ms + 96*40 ms+72*40 ms) for UE supporting power class 1, or

## 6.72 s (60*40 ms+60*40 ms+48*40 ms) for UE supporting other power class.

For Configuration 2,

## 14.4 s (192*40 ms + 96*40 ms+72*40 ms) for UE supporting power class 1, or

## 9.12 s (120*40 ms+60*40 ms+48*40 ms) for UE supporting other power class.

For Configuration 3,

## 18.24 s (288*40 ms + 96*40 ms+72*40 ms) for UE supporting power class 1, or

## 11.52 s (180*40 ms+60*40 ms+48*40 ms) for UE supporting other power class.

The UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.15SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR2-2)

## A.7.6.2.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.15.1-1, A.7.6.2.15.1-2, and A.7.6.2.15.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.15.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.15.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.15.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.7.6.2.15.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

Table A.7.6.2.15.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting with SSB time index detection

## A.7.6.2.15.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

For Configuration 1,

## 15.84 s (96*40 ms*1.5+96*40 ms*1.5+72*40 ms*1.5) for UE supporting power class 1, or

## 10.08 s (60*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

For Configuration 2,

## 21.6 s (192*40 ms*1.5+96*40 ms*1.5+72*40 ms*1.5) for UE supporting power class 1, or

## 13.68 s (120*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

For Configuration 3,

## 27.36 s (288*40 ms*1.5+96*40 ms*1.5+48*40 ms*1.5) for UE supporting power class 1, or

## 17.28 s (180*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

For Configuration 1,

## 168.96 s (96*640 ms+96*640 ms+72*640 ms) for UE supporting power class 1, or

## 107.52 s (60*640 ms+60*640 ms+48*640 ms) for UE supporting other power class.

For Configuration 2,

## 230.4 s (192*640 ms+96*640 ms+72*640 ms) for UE supporting power class 1, or

## 145.92 s (120*640 ms+60*640 ms+48*640 ms) for UE supporting other power class.

For Configuration 3,

## 291.84 s (288*640 ms+96*640 ms+72*640 ms)  for UE supporting power class 1, or

## 184.32 s (180*640 ms+60*640 ms+48*640 ms)  for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.16SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR1)

## A.7.6.2.16.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.16.1-1, A.7.6.2.16.1-2, and A.7.6.2.16.1-3.

In test 1 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.16.1-2 is provided for a UE that does not support per-FR gap and in test 2 no gap pattern is configured as defined in table A.7.6.2.16.1-2. If the UE supports per-FR gap, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.16.1-1.

Table A.7.6.2.16.1-1 SA event triggered reporting tests without SSB index reading for FR1-FR2

Table A.7.6.2.16.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

Table A.7.6.2.16.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

## A.7.6.2.16.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,2,3

## 7.68 s (96*40 ms+96*40 ms) for UE supporting power class 1, or

## 4.8 s (60*40 ms + 60*40 ms) for UE supporting other power class.

For Configuration 4,5,6

## 11.52 s (192*40 ms+96*40 ms) for UE supporting power class 1, or

## 7.2 s (120*40 ms + 60*40 ms) for UE supporting other power class.

For Configuration 7,8,9

## 15.36 s (288*40 ms+96*40 ms) for UE supporting power class 1, or

## 9.6 s (180*40 ms + 60*40 ms) for UE supporting other power class.

In test 2, without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,2,3

## 3.84 s (96*20 ms+96*20 ms) for UE supporting power class 1, or

## 2.4 s (60*20 ms + 60*20 ms) for UE supporting other power class.

For Configuration 4,5,6

## 5.76 s (192*20 ms+96*20 ms) for UE supporting power class 1, or

## 3.6 s (120*20 ms + 60*20 ms) for UE supporting other power class.

For Configuration 7,8,9

## 7.68 s (288*20 ms+96*20 ms) for UE supporting power class 1, or

## 4.8 s (180*20 ms + 60*20 ms) for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.17SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR1)

## A.7.6.2.17.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.17.1-1, A.7.6.2.17.1-2, and A.7.6.2.17.1-3.

In test 1&2 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.17.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 no gap pattern is configured as defined in table A.7.6.2.17.1-2. If a UE supports per-FR gap  it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.17.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.17.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR2

Table A.7.6.2.17.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

Table A.7.6.2.17.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

## A.7.6.2.17.2Test Requirements

In test 1 with per-UE gap and in test 3 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

For Configuration 1,2,3

## 11.52 s (96*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 7.2 s (60*40 ms*1.5 + 60*40 ms*1.5)  for UE supporting other power class.

For Configuration 4,5,6

## 17.28 s (192*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 10.80 s (120*40 ms*1.5 + 60*40 ms*1.5) for UE supporting other power class.

For Configuration 7,8,9

## 23.04 s (288*40 ms*1.5 + 96*40 ms*1.5) for UE supporting power class 1, or

## 14.40 s (180*40 ms*1.5 + 60*40 ms*1.5) for UE supporting other power class.

In test 2 with per-UE gap and in test 4 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

For Configuration 1,2,3

## 122.80 s (96*640 ms + 96*640 ms) for UE supporting power class 1, or

## 76.80 s (60*640 ms + 60*640 ms) for UE supporting other power class.

For Configuration 4,5,6

## 184.32 s (192*640 ms + 96*640 ms) for UE supporting power class 1, or

## 115.20 s (120*640 ms + 60*640 ms) for UE supporting other power class.

For Configuration 7,8,9

## 245.76 s (288*640 ms + 96*640 ms) for UE supporting power class 1, or

## 153.60 s (180*640 ms + 60*640 ms) for UE supporting other power class.

In test 1, 2, 3 and 4 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.18SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR1)

## A.7.6.2.18.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

n this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.18.1-1, A.7.6.2.18.1-2, and A.7.6.2.18.1-3.

In test 1 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.18.1-2 is provided for a UE that does not support per-FR gap and in test 2 measurement no gap pattern is configured as defined in table A.7.6.2.18.1-2. If the UE supports per-FR gap, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.18.1-1.

Table A.7.6.2.18.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR2

Table A.7.6.2.18.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

Table A.7.6.2.18.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

## A.7.6.2.18.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,2,3

## 10.56 s (96*40 ms+96*40 ms+72*40 ms) for UE supporting power class 1, or

## 6.72 s (60*40 ms + 60*40 ms+48*40 ms) for UE supporting other power class.

For Configuration 4,5,6

## 14.4 s (192*40 ms+96*40 ms+72*40 ms) for UE supporting power class 1, or

## 9.12 s (120*40 ms + 60*40 ms+48*40 ms) for UE supporting other power class.

For Configuration 7,8,9

## 18.24 s (288*40 ms+96*40 ms+72*40 ms) for UE supporting power class 1, or

## 11.52 s (180*40 ms + 60*40 ms+48*40 ms) for UE supporting other power class.

In test 2 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,2,3

## 5.28 s (96*20 ms+96*20 ms+72*20 ms)for UE supporting power class 1, or

## 3.36 s (60*20 ms + 60*20 ms+48*20 ms) for UE supporting other power class.

For Configuration 4,5,6

## 7.2 s (192*20 ms+96*20 ms+72*20 ms) for UE supporting power class 1, or

## 4.56 s (120*20 ms + 60*20 ms+48*20 ms) for UE supporting other power class.

For Configuration 7,8,9

## 9.12 s (288*20 ms+96*20 ms+72*20 ms) for UE supporting power class 1, or

## 5.76 s (180*20 ms + 60*20 ms+48*20 ms) for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.19SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR1)

## A.7.6.2.19.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 2 and NR cell 2 as neighbour cell in FR2-2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.19.1-1, A.7.6.2.19.1-2, and A.7.6.2.19.1-3.

In test 1&2 per-UE measurement gap pattern configuration # 0 as defined in table A.7.6.2.19.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 measurement no gap pattern is configured as defined in table A.7.6.2.19.1-2. If a UE supports per-FR gap , it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.19.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.19.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR2

Table A.7.6.2.19.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

Table A.7.6.2.19.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 with SSB time index detection

## A.7.6.2.19.2Test Requirements

In test 1 with per-UE gap and in test 3 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

For Configuration 1,2,3

## 15.84 s (96*40 ms*1.5+96*40 ms*1.5+72*40 ms*1.5) for UE supporting power class 1, or

## 10.08 s (60*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

For Configuration 4,5,6

## 21.6 s (192*40 ms*1.5+96*40 ms*1.5+72*40 ms*1.5) for UE supporting power class 1, or

## 13.68 s (120*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

For Configuration 7,8,9

## 27.36 s (288*40 ms*1.5+96*40 ms*1.5+72*40 ms*1.5) for UE supporting power class 1, or

## 17.28 s (180*40 ms*1.5+60*40 ms*1.5+48*40 ms*1.5) for UE supporting other power class.

In test 2 with per-UE gap and in test 4 without the gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

For Configuration 1,2,3

## 168.69 s (96*640 ms+96*640 ms+72*640 ms) for UE supporting power class 1, or

## 107.52 s (60*640 ms+60*640 ms+48*640 ms) for UE supporting other power class.

For Configuration 4,5,6

## 230.4 s (192*640 ms+96*640 ms+72*640 ms) for UE supporting power class 1, or

## 145.92 s (120*640 ms+60*640 ms+48*640 ms) for UE supporting other power class.

For Configuration 7,8,9

## 291.84 s (288*640 ms+96*640 ms+72*640 ms) for UE supporting power class 1, or

## 184.32 s (180*640 ms+60*640 ms+48*640 ms) for UE supporting other power class.

In test 1, 2, 3 and 4 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.20SA event triggered reporting tests for FR2 with measurement gap with priority and two periodic MUSIM gaps configured

## A.7.6.2.20.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event on an inter-frequency layer based on measurement performed within a measurement gap when the UE is configured with two periodic MUSIM gaps. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.20.1-1, A.7.6.2.20.1-2, and A.7.6.2.20.1-3.

The three gaps, including a measurement gap and two periodic MUSIM gaps, are configured with different priority levels. In this test, the measurement gap has the lowest priority level, and the 2nd MUSIM gap has the highest priority level (i.e., priority of 2nd MUSIM gap > 1 st MUSIM gap > measurement gap) as defined in table A.7.6.2.20.1-2.

NOTE: the signaling procedure to trigger the UE to request MUSIM gaps before the test equipment configures MUSIM gaps to the UE is left to comformance test implementation.

Measurement gap pattern configuration defined in table A.7.6.2.20.1-2 is provided for a UE.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.20.1-1.

Table A.7.6.2.20.1-1: Supported test configurations.

Table A.7.6.2.20.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.20.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.20.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 10240 for UE supporting power class 1, or

## 6400 for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.21SA event triggered reporting tests for FR2 with measurement gap without priority and periodic MUSIM gap configured

## A.7.6.2.21.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event on an inter-frequency layer based on measurement performed within measurement gaps, when UE is also configured with MUSIM gaps. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters are given in tables A.7.6.2.21.1-1, A.7.6.2.21.1-2 and A.7.6.2.21.1-3.

Measurement gap and MUSIM gap pattern configurations defined in table A.7.6.2.21.1-2 are provided to the UE. When UE does not support per-FR gap, measurement gap pattern configuration is provided for a per-UE gap. When UE supports per-FR gap, measurement gap pattern configuration is provided for a per-FR2 gap. MUSIM gap is configured with shorter MGRP than the configured measurement gap.

NOTE:The interaction between the test equipment and UE before configuring the MUSIM gap to the UE is left to comformance test implementation.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.7.6.2.21.1-1 Supported test configurations

Table A.7.6.2.21.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.21.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.21.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-10240 for a UE supporting power class 1,

-6400 for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.22SA event triggered reporting tests with SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.2.22.1Test Purpose and Environment

The purpose of this test is to verify that the PC6 UE makes correct reporting of an event when UE supporting measEnhCAInterFreqFR2-r18 is configured with highSpeedMeasInterFreq-r17. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR carrier 1(RF channel 1) and NR cell2 as neighbor cell in FR2 on NR carrier 2(RF channel 2). The test parameters and configurations are given in tables A.7.6.2.22.1-1, A.7.6.2.22.1-2, and A.7.6.2.22.1-3.

Measurement gap pattern configuration defined in table A.7.6.2.22.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Supported test configurations are shown in table A.7.6.2.22.1-1.

Table A.7.6.2.22.1-1: SA event triggered reporting tests with SSB index reading for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

Table A.7.6.2.22.1-2: General test parameters for SA inter-frequency event triggered reporting with SSB time index detection for R2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

Table A.7.6.2.22.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.2.22.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is 2160 ms according to the requirements defiend in table 9.3.4-9 and table 9.3.4-10 in clause 9.3.4

The UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.23SA event triggered reporting tests without SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.2.23.1Test Purpose and Environment

The purpose of this test is to verify that the FR2 power class 6 UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements specified in clause 9.3.4 for a FR2 power class 6 UE supporting measEnhCAInterFreqFR2-r18 and configured with highSpeedMeasFlagFR2-r17.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.23.1-1, A.7.6.2.23.1-2, and A.7.6.2.23.1-3.

The measurement gap pattern configuration defined in table A.7.6.2.23.1-2 applies to a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured to a UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are specified in table A.7.6.2.23.1-1.

Table A.7.6.2.23.1-1 Test configuration

Table A.7.6.2.23.1-2: General test parameters

Table A.7.6.2.23.1-3: Cell specific test parameters

## A.7.6.2.23.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1 s from the beginning of time period T2.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.24SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (FR1+FR2 CA and LTE+ FR2 EN-DC) for UE supporting [CSSF enhancement for one CC measurement per-band]

## A.7.6.2.24.1Test Purpose and Environment

The purpose of this test is to verify that if UE supports interFrequencyMeas-NoGap-r16 and the flag interFrequencyConfig-NoGap-r16 is configured by the network, the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4 for UE supporting [CSSF enhancement for one CC measurement per-band].

In this test, there are two tests with different configurations, the UE is only required to pass one of the two tests. The two tests are:

-Test 1: FR1+FR2 CA configuration:  NR cell 1 as PCell in FR1 on NR RF channel 1, NR cell 2 and NR cell 3 as SCells in FR2 on NR RF channel 2 and NR RF channel 3, where NR RF channel 2 and NR RF channel 3 are in one same band, furthermore, NR cell 4 as neighbour cell in FR2 on NR RF channel 4.

-Test 2: FR2 EN-DC configuration: LTE cell 1 as PCell in FR1 on LTE RF channel 1, NR cell 1 as PSCell in FR2 on NR RF channel 1 and NR cell 2 as SCells in FR2 on NR RF channel 2, where NR RF channel 1and NR RF channel 2 are in one same band, furthermore, NR cell 3 as neighbour cell in FR2 on NR RF channel 3.

In the measurement control information, SCells with only SSB based L3 measurement are configured, and a measurement object is configured for the frequency of the neigbor cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Supported test configurations of tests are shown in table A.7.6.2.24.1-1.

Table A.7.6.2.24.1-1 Event triggered reporting tests without SSB index reading

The test parameters of tests are shown in table A.7.6.2.24.1-2, A.7.6.2.24.1-3 and A.7.6.2.24.1-4 below.

Table A.7.6.2.24.1-2: General test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.24.1-3: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection, for test case 1

Table A.7.6.2.24.1-4: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection, for test case 2

## A.7.6.2.24.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6400 for UE supporting power class 1, or

## 3840 for UE supporting other power class.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 3200 for UE supporting power class 1, or

## 1920 for UE supporting other power class.

In test 1 and test 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.25SA event triggered reporting tests for FR2 under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r19

## A.7.6.2.25.1Test purpose and Environment

The purpose of this test is to partly verify the intra-frequency cell search requirements in clause 9.1.5.1 and 9.3.9 for UE supports interFrequencyMeas-Nogap-r16 and/or NeedForGapsInfoNR-r16 and  fr1-FR2-CA-r19 via threeCarrierMeasWithoutGap-r19 makes correct reporting of an event.

The UE is only required to pass one of the three tests in A.4.6.2.10 for FR1 EN-DC, A.6.6.2.17 for FR1 CA, A.7.6.2.25 for FR1 and FR2 CA.

## A.7.6.2.25.2Test parameters

In this test, NR cell 1 as PCell in FR1 on NR RF channel 1, NR cell 2 as SCell in FR2 on NR RF channel 2. NR cell 3 as neighbour cell in FR2 on NR RF channel 3 which is in the same band as NR Cell 2. The SSB of Cell 3 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 2 and Cell 3 should be different in frequency location within the cell bandwidth.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.25.2-1: Supported test configurations

Table A.7.6.2.25.2-2: General test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.25.2-3: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.2.25.3Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

2.4s for UE supporting power class 1, or

1.44s for UE supporting other power class.

UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.26SA event triggered reporting tests without gap under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r19

## A.7.6.2.26.1Test purpose and Environment

The purpose of this test is to partly verify the intra-frequency cell search requirements in clause 9.1.5.1, clauses 9.2.5.1 and 9.2.5.2 for UE supporting  fr1-FR2-CA-r19 via threeCarrierMeasWithoutGap-r19 makes correct reporting of an event.

## A.7.6.2.26.2Test parameters

In this test, there are two tests with different configurations, The capability rule is: if the UE supports inter‑RAT measurement, it must pass Sub‑test 2; otherwise, it only needs pass Sub‑test 2.

-Sub-test 1: NR cell 1 as PCell in FR1 on NR RF channel 1, NR cell 2 as SCell in FR2 on NR RF channel 2, NR cell 3 as SCell in FR2 on NR RF channel 3, where NR RF channel 1, NR RF channel 2 and NR RF channel 3 are in different bands, furthermore, NR cell 4 as neighbour cell in FR2 on NR RF channel 2 same as NR cell 2.

-Sub-test 2: NR cell 1 as PCell in FR1 on NR RF channel 1, LTE Cell 2 is an inter-RAT E-UTRAN neighbour cell on LTE RF channel 1, NR cell 2 as SCell in FR2 on NR RF channel 2, where NR RF channel 1 and NR RF channel 2 are in different bands. NR cell 4 as neighbour cell in FR2 on NR RF channel 2, same as NR cell 2.

In the measurement control information, SCells with only SSB based L3 measurement are configured, and a measurement object is configured for the frequency of the neigbor cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. For UE support inter-RAT measurement, a measurement object is configured for the frequency of the LTE neighbour cell, it is indicated to the UE that event-triggered reporting with Event A6 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 4.

Supported test configurations of test are shown in table A.7.6.2.26.2-1.

Table A.7.6.2.26.2-1: Supported test configurations

The test parameters of tests are shown in table A.7.6.2.26.2-2, A.7.6.2.26.2-3 and A.7.6.2.26.2-4 below.

Table A.7.6.2.26.2-2: General test parameters for intra-frequency event triggered reporting for FR2 without SSB time index detection

Table A.7.6.2.26.2-3: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection, for sub-test case 1

Table A.7.6.2.26.2-4: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection, for sub-test case 2

## A.7.6.2.26.3Test Requirements

In sub-test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 1600 for UE supporting power class 1, or

## 960 for UE supporting other power class.

In sub-test 2, the UE shall send one Event A3 triggered measurement report and one Event A6 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 1600 for UE supporting power class 1 for A3 event, or

## 960 for UE supporting other power class for A3 event.

## 5760 from the beginning of time period T2 for A6 event.

In sub-test 1 and sub-test 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.27SA serving cell quality triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2)

## A.7.6.2.27.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting fastRx-BSF-MeasDelayReduction-r19 makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.7.6.2.27.1-1, A.7.6.2.27.1-2, and A.7.6.2.27.1-3.

Measurement gap pattern configuration is defined in table A.7.6.2.27.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used, serving cell’s RSRP-triggered activating/deactivating multi-Rx for L3 measurement is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.2.27.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.27.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.7.6.2.27.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.7.6.2.27.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting with SSB time index detection

## A.7.6.2.27.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 1562 for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 2.

## 3122 for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 4.

## 4682 for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 6.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 16642 for UE supportingfastRx-BSF-MeasDelayReduction-r19, the values of which are 2.

## 33282 for UE supportingfastRx-BSF-MeasDelayReduction-r19, the values of which are 4.

## 49922 for UE supporting fastRx-BSF-MeasDelayReduction-r19, the values of which are 6.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.2.28SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used

## A.7.6.2.28.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct measurement and reporting of an event, during the measurement, measurement gap cancellation happens and relevant measurement extension is expected. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4 and 9.3.5. Meanwhile, this test also verify the scheduling availability in clause 9.2.5.3.

In this test, there are three cells: NR Cell 1 as PCell in FR2-1 on NR RF channel 1, NR Cell 2 as neighbour cell in FR2-1 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.2.2.1-1 and A.7.6.2.2.1-2 for Test 1 in clause A.7.6.2.2, except:

-the parameters in Tables A.7.6.2.28.1-1,

-SMTC configuration in PCell is the same as in Cell 2.

The UE is configured with measurements on Cell 1 and Cell 2. Measurement gap pattern configuration is defined in table A.7.6.2.28.1-1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 associated with NR RF channel 2 is used and event-triggered reporting with Event A1 associated with NR RF channel 1 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

If a measurement gap occasion is determined to be cancelled, the test equipment sends the DCI indication latest X ms before the start of the measurement gap occasion using DCI format 1-1, where X is 3ms or 5ms as given by the UE capability minimumTimeOffset-r19 [2]. 10 measurement gap occasions are canceled for the UE of power class 1 or 5, and 10 measurement gap occasions are canceled for the UE of power class 2, 3, or 4. The UE is scheduled with DL data on PCell on all the slots overlapping with the cancelled measurement gap occasions.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.2.28.1-1: General test parameters for SSB based inter-frequency L1-RSRP measurement with measurement gap test in FR2

## A.7.6.2.28.2Test Requirements

In T2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 5440 for UE supporting power class 1 or power class 5, or

## 8320 for UE supporting other power class.

During T2, the UE shall send valid ACK/NACK for all the scheduled transmissions within cancelled measurement gap occasions.

In T1 and T2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

Neither interruption nor scheduling restriction happens on the canceled measurement gap occasions, as defined in clause 9.2.5.3.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.3L1-RSRP measurement for beam reporting

## A.7.6.3.1SSB based L1-RSRP measurement when DRX is not used

## A.7.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.3.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.6.3.1.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.1.2-1 and table A.7.6.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.1.2-1: General test parameters

Table A.7.6.3.1.2-2: SSB specific test parameters

## A.7.6.3.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-1680 for UE supporting power class 1

-1200 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.2SSB based L1-RSRP measurement when DRX is used

## A.7.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.3.2.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.6.3.2.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.2.2-1 and table A.7.6.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.2.2-1: General test parameters

Table A.7.6.3.2.2-2: SSB specific test parameters

## A.7.6.3.2.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used

## A.7.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.7.6.3.3.1-1.

Table A.7.6.3.3.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.6.3.3.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.3.2-1 and table A.7.6.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.7.6.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.7.6.3.3.2-1: General test parameters

Table A.7.6.3.3.2-1: CSI-RS specific test parameters

## A.7.6.3.3.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.6.3.3.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.6.3.3.3-1: L1-RSRP absolute accuracy test requirement

## A.7.6.3.4CSI-RS based L1-RSRP measurement when DRX is used

## A.7.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.7.6.3.4.1-1.

Table A.7.6.3.4.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.6.3.4.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.4.2-1 and table A.7.6.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 1440 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.7.6.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.7.6.3.4.2-1: General test parameters

Table A.7.6.3.4.2-1: CSI-RS specific test parameters

## A.7.6.3.3.3Test Requirements

After 1440 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.6.3.4.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.6.3.4.3-1: L1-RSRP absolute accuracy test requirement

## A.7.6.3.5SSB based L1-RSRP measurement when DRX is used for power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the power class 6 UE makes correct reporting of L1-RSRP measurement when highSpeedMeasFlagFR2-r17 is configured. This test will partly verify the L1-RSRP measurement requirements for power class 6 UE configured with highSpeedMeasFlagFR2-r17 in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.5.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.3.5.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test for power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.6.3.5.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.5.2-1 and table A.7.6.3.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.5.2-1: General test parameters

Table A.7.6.3.5.2-2: SSB specific test parameters

## A.7.6.3.5.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 480 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -5 to [+44] dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.6Inter-cell SSB based L1-RSRP measurements on FR2 SCell when DRX is not used

## A.7.6.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.13.4.1, with the testing configurations for NR serving cell in table A.7.6.3.6.1-1.

The AoA setup of FR2 cell for this test is Setup 3 as defined in clause A.3.15.

Table A.7.6.3.6.1-1: Applicable NR configurations for inter-cell SSB based L1-RSRP test in FR2

## A.7.6.3.6.2Test parameters

There are two cells in the test, Cell 1 is the serving cell in CA, including a FR1 PCC and FR2 SCC. Cell 2 is a FR2 cell with different PCI from Cell 1. The test parameters for Cell 1 are given in table A.7.6.3.6.2-1. The test parameters for FR2 Cell (Cell 2) are given in table A.7.6.3.6.2-2 and table A.7.6.3.6.2-3.

SSB#0 and SSB#1 is transmitted on Cell 1 FR2 SCC and Cell 2.In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on SSB#0, and report measurement results periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. At the beginning of T2, SSB#1 starts transmission and the UE is configured for L1-RSRP measurement on SSB#1. The test has higher layer parameter timeRestrictionForChannelMeasurements configured in CSI-ReportConfig and additionalPCIList configured in CSI-SSB-ResourceSet.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD on Cell 1 in FR1 and perform L1-RSRP measurements on the SSB#0in FR2.

Table A.7.6.3.6.2-1: Cell specific test parameters for FR1 PCell

Table A.7.6.3.6.2-2: Cell specific test parameters for FR2 SCell

Table A.7.6.3.6.2-2: SSB specific test parameters for FR2 SCell

## A.7.6.3.6.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-2160 for UE supporting power class 1

-1680 for UE supporting power class 2, 3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.7SSB based L1-RSRP measurement for FR2-2 when DRX is used

## A.7.6.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.7.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.3.7.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.6.3.7.2Test parameters

There is one cells in the test, the FR2-2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.7.2-1 and table A.7.6.3.7.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.7.2-1: General test parameters

Table A.7.6.3.7.2-2: SSB specific test parameters

## A.7.6.3.7.3Test Requirements

The UE shall send L1-RSRP report every TBD slots. No later than X ms plus TBD slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-TBD for UE supporting power class 1

-TBD for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.8CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP

## A.7.6.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.7.6.3.3.1-1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in A.7.6.3.3.

The test environment is the same as in A.7.6.3.3 with following exceptions in table A.7.6.3.3.2-1.

The value of parameter “Dedicated BWP configuration” is DLBWP.1.2 and ULBWP.1.2.

NOTE:The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in A.7.6.3.3.3.

## A.7.6.3.9SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.7.6.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.1.1-1.

The test environment is the same as in A.7.6.3.1 with following exceptions in table A.7.6.3.1.2-1.

## A.7.6.3.9.2Test Requirements

The test requirements are the same as in A.7.6.3.1.3.

## A.7.6.3.10SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used

## A.7.6.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.7.6.3.10.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.3.10.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.6.3.10.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.10.2-1 and table A.7.6.3.10.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. During time duration T1, the UE shall not have any timing information of NR cell 2.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.10.2-1: General test parameters

Table A.7.6.3.10.2-2: SSB specific test parameters

## A.7.6.3.10.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-[3360] for UE supporting power class 1

-[2080] for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.11SSB based L1-RSRP measurement when DRX is used for power class 6 UE supporting simultaneousReceptionTwoQCL-r18

## A.7.6.3.11.1Test Purpose and Environment

The purpose of this test is to verify that the power class 6 UE supporting simultaneousReceptionTwoQCL-r18 makes correct reporting of L1-RSRP measurement when highSpeedMeasFlagFR2-r17 is configured, and when highSpeedDeploymentTypeFR2-r17 is configured as bidirectional. This test will partly verify the L1-RSRP measurement requirements for power class 6 UE configured with highSpeedMeasFlagFR2-r17 for FR2 in clause 9.5.4.1 with the testing configurations for NR cells in table A.7.6.3.11.1-1.

Table A.7.6.3.11.1-1: Test configurations

## A.7.6.3.11.2Test parameters

There is one cell in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.11.2-1 and table A.7.6.3.11.2-2 below.

There are two SSBs configured in Cell 1. In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on two different QCL Type D SSBs simultaneously and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.11.2-1: General test parameters

Table A.7.6.3.11.2-2: SSB specific test parameters

## A.7.6.3.11.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 880 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0, SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -5 to +44 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.12SSB based L1-RSRP measurement when DRX is not used

## A.7.6.3.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting ssb-BurstPeriodicityAdaptation-r19 makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells (NR FR1 PCell and NR FR2 SCell) in table A.7.6.3.12.1-1 and in table A.7.6.3.12.1-2.

Table A.7.6.3.12.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

Table A.7.6.3.12.1-2: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.6.3.12.2Test parameters

There are two cells in the test, FR1 PCell (Cell 1) and FR2 SCell (Cell 2). The test parameters for the Cell 2 are given in table A.7.6.3.12.2-1, table A.7.6.3.12.2-2 and table A.7.6.3.12.2-3 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. The UE is configured to provide periodic L1-RSRP reports.

At the beginning of T2, DCI format 2_9 that indicates a change in SSB burst periodicity of the SSB transmission on SCell is received, and the periodicity of SSB #0 is changed from 20 ms to 80 ms. At the beginning of T3, DCI format 2_9 that indicates a change in SSB burst periodicity of the SSB transmission on SCell is received, the periodicity of SSB #0 is changed from 80 ms to 40 ms. The DCI format 2_9 is indicated at the time point of DCI processing time as defined in TS 38.213 plus 3ms before the first adapted SSB burst occasion.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.12.2-1: General test parameters (NR FR1 PCell)

Table A.7.6.3.12.2-2: General test parameters (NR FR2 SCell)

Table A.7.6.3.12.2-3: SSB specific test parameters (NR FR2 SCell)

## A.7.6.3.12.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T1, UE shall send L1-RSRP report including the results for SSB#0 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-160 for UE supporting power class 3.

From the beginning of T2, UE receives a DCI format 2_9 indicating a change in SSB burst periodicity of the SSB #0 transmission on SCell, after Y ms from receiving the first SSB burst after the time point as defined in TS 38.213 plus 3 ms, UE shall send L1-RSRP report for SSB #0 with the updated periodicity while meeting the accuracy requirements defined in clause 10.1.20.1, where Y is

-640 ms for UE supporting power class 3.

From the beginning of T3, UE receives another DCI format 2_9 indicating a change in SSB burst periodicity of the SSB #0 transmission on SCell, after Z ms from receiving the first SSB burst after the time point as defined in TS 38.213 plus 3 ms, UE shall send L1-RSRP report for SSB #0 with the updated periodicity while meeting the accuracy requirements defined in clause 10.1.20.1, where Z is

-320 ms for UE supporting power class 3.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.13Event Triggered Reporting for the UE initiated beam management

## A.7.6.3.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes the correct reporting of event triggered L1-RSRP measurement for the UE initiated beam management. This test will partly verify the L1-RSRP reporting requirements in clause 9.5.3.4, with the testing configurations for NR cells in table A.7.6.3.13.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Config 1 is used in this test, and it is given by, Config 1: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode.

## A.7.6.3.13.2Test parameters

There is one cell in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.13.2-1 and table A.7.6.3.13.2-2 below.

In CSI resource configuration, UE is indicated to perform L1-RSRP measurement on the resourcesForChannelMeasurement and the resourcesForChannelMeasurement consists of SSB. In the CSI report configuration, UE is configured with event-triggered reporting, with the event 2 and Mode-A. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

During the T1, SSB 1 is not detectable. At the beginning of T2, SSB 1 becomes stronger than the SSB 0 by offset amount and the event entering condition is met.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.7.6.3.13.2-1: General test parameters

Table A.7.6.3.13.2-2: SSB specific test parameters

## A.7.6.3.13.3Test Requirements

In the test, the UE shall send a first PUCCH message using the new UCI type, within 160ms plus 5 slots from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.14CSI-RS based UE-initiated/event-driven beam management of event2

## A.7.6.3.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of event2 UE initiated beam management. This test will partly verify the Event Triggered Reporting for the UE initiated beam management requirements in clause 9.5.3.4, with the testing configurations for NR cells in table A.7.6.3.14.1-1.

Table A.7.6.3.14.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.6.3.14.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.14.2-1 and table A.7.6.3.14.2-2 below.

In CSI measurement and report configurations, CSI-ReportConfig is configured with the higher layer parameter eventType-r19 set to ‘event2, and newBeamResourceSet is configured as NZP-CSI-RS-ResourceSet configured with repetition.

The test consists of two time period T1 and T2. UE is also configured to measure L1-RSRP based on SSB.There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.7.6.3.14.2-1: General test parameters

Table A.7.6.3.14.2-1: CSI-RS specific test parameters

## A.7.6.3.14.3Test Requirements

The UE shall send one Event triggered measurement report, no later than 20 ms plus 5 slots from the beginning of time period T2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.15Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR2 when DRX is not used

## A.7.6.3.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event based on L1-RSRP measurement. This test will partly verify the event triggered reporting for UE initiated beam management in clause 9.13.3.4 configured with event2-r19, modeA-r19 and without eventCountWindow-r19 configuration.

The AoA setup of FR2 cell for this test is Setup 3 as defined in clause A.3.15.

Table A.7.6.3.15.1-1: Applicable NR configurations for inter-cell SSB based Event triggered reporting for UE initiated beam management in FR2

## A.7.6.3.15.2Test parameters

There are two cells in the test, Cell 1 is the serving cell in CA, including a FR1 PCC and FR2 SCC. Cell 2 is a FR2 cell with different PCI from Cell 1. The test parameters for Cell 1 are given in table A.7.6.3.15.2-1. The test parameters for FR2 Cell (Cell 2) are given in table A.7.6.3.15.2-2 and table A.7.6.3.15.2-3.

SSB#0 is transmitted on Cell 1. SSB#1 and SSB#2 are transmitted on FR2 Cell 2. In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on SSB#1 and SSB#2, where SSB#1 is for current beam measurement and SSB#2 is for new beam measurement. The test consists of two successive time periods, with time duration of T1 and T2 respectively. At the beginning of T2, SSB#2 starts transmission and the UE is configured for L1-RSRP measurement on SSB#2 and the RSRP configuration of SSB#2 is better than SSB#1 to trigger the event-2 reporting. The test has higher layer parameter timeRestrictionForChannelMeasurements configured in CSI-ReportConfig and additionalPCIList configured in CSI-SSB-ResourceSet.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD on Cell 1 in FR1 and perform L1-RSRP measurements on the SSB#0in FR2.

Table A.7.6.3.15.2-1: Cell specific test parameters for FR1 PCell

Table A.7.6.3.15.2-2: Cell specific test parameters for FR2 SCell

Table A.7.6.3.15.2-3: SSB specific test parameters for FR2 SCell

## A.7.6.3.15.3Test Requirements

The UE shall send a first PUCCH message using the new UCI type, no later than 160 ms plus 5 slots from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.3.16CSI-RS based L1-RSRP measurement when DRX is not used with SBFD

## A.7.6.3.16.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.7.6.3.16.1-1.

Table A.7.6.3.16.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.6.3.16.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.3.16.2-1 and table A.7.6.3.16.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 1 of a frame and UE provides the report back based on the reporting configuration as defined in table A.7.6.3.16.2-1. In the test, UE is configured to report for SBFD symbols.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.7.6.3.16.2-1: General test parameters

Table A.7.6.3.16.2-2: CSI-RS specific test parameters

## A.7.6.3.16.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8 from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.6.3.16.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

## A.7.6.4CLI measurements

## A.7.6.4.1SRS-RSRP measurement with non-DRX

## A.7.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SRS-RSRP measurement. This test will verify the SRS-RSRP measurement requirements in clause 9.7.2.5 with the testing configurations for NR cells in table A.7.6.4.1.1-1.

Table A.7.6.4.1.1-1: Applicable NR configurations for FR2 SRS-RSRP test

## A.7.6.4.1.2Test Parameters

One cell is deployed in the test, which is FR2 PCell (Cell 1). The test parameters for PCell is given in table A.7.6.4.1.2-1 ~ A.7.6.4.1.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system transmits SRS resource for measurement in the DL slot according to the SRS configuration in table A.7.6.4.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A. 7.6.4.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 2 data symbols before SRS to be transmitted.

Table A.7.6.4.1.2-1: General test parameters for SRS-RSRP event triggered reporting for PCell in FR2

Table A.7.6.4.1.2-2: NR Cell specific test parameters for SA SRS-RSRP event triggered reporting for PCell in FR2

Table A.7.6.4.1.2-3: NR OTA Cell specific test parameters for SA SRS-RSRP event triggered reporting for PCell and neighbour cell UE in FR2

Table A.7.6.4.1.2-4: SRS configuration for measurement reporting

## A.7.6.4.1.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 60 ms from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.4.2CLI-RSSI measurement with non-DRX

## A.7.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of CLI-RSSI measurement. This test will verify the CLI-RSSI measurement requirements in clause 9.7.3.5 with the testing configurations for NR cells in table A.7.6.4.2.1-1.

Table A.7.6.4.2.1-1: Applicable NR configurations for FR2 CLI-RSSI test

## A.7.6.4.2.2Test Parameters

One cell is deployed in the test, which is FR2 PCell (Cell 1). The test parameters for PCell is given in table A.7.6.4.2.2-1 ~ A.7.6.4.2.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI measurement resource and on 2 data symbols before. The CLI-RSSI measurement resource configuration is in table A.7.6.4.2.2-4.

Table A.7.6.4.2.2-1: General test parameters for CLI-RSSI event triggered reporting for PCell in FR2

Table A.7.6.4.2.2-2: NR Cell specific test parameters for CLI-RSSI event triggered reporting for PCell in FR2

Table A.7.6.4.2.2-3: NR OTA Cell specific test parameters for CLI-RSSI event triggered reporting for PCell in FR2

Table A.7.6.4.2.2-4: CLI-RSSI measurement resource configuration for measurement reporting

## A.7.6.4.2.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 5 ms from the beginning of time period T2. The nominal RSSI used to evaluate the requirement shall be based on Io.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.7.6.5NR Measurements with autonomous gaps

## A.7.6.5.1SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2)

## A.7.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an CGI. This test will partly verify the SA inter-frequency NR cell search requirements in clause 8.2.1.2.16 and 9.11

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.5.1.1-1, A.7.6.5.1.1-2, and A.7.6.5.1.1-3.

Measurement gap patterns are configured. During T1 the UE shall report event A3 for cell 2. Within 3 seconds of the event report, the test equipment shall add a measurement reporting configuration using ReportConfigNR which containsa ReportCGI IE with cellForWhichToReportCGI set to the physical Cell ID of cell 2 and including the optional IE useAutonomousGaps-r16

In the measurement control information, it is indicated to the UE to decode the CGI of the neighbour cell using autonomous gaps. The test consists of two time phases, T1 and T2. Time period T2 begins when the last TTI containing the RRC message implying SI reading is sent to the UE.

Supported test configurations are shown in table A.7.6.5.1.1-1.

Table A.7.6.5.1.1-1 SA interfrequency CGI reporting test in autonomous gaps

Table A.7.6.5.1.1-2: General test parameters for SA interfrequency CGI reporting in autonomous gaps

Table A.7.6.5.1.1-3: Cell specific test parameters SA interfrequency CGI reporting in autonomous gaps

## A.7.6.5.1.2Test Requirements

The UE shall report the CGI of cell 2 within 10 + 25*Tsmtc + 6* TRMSI-scheduling +20 ms +2 ms= 652 ms from the start of T2, allow 655 ms.  The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall be scheduled continuously throughout the test, and from the start of T3 until 655 ms the number of interrupted slots shall not exceed the allowed number as defined in clause 8.2.2.2.14.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.6L1-SINR measurement for beam reporting

A.7.6.6.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used

A.7.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.1, with the testing configurations for NR cells in table A.7.6.6.1.1-1.

Table A.7.6.6.1.1-1: Applicable NR configurations for FR2 CSI-RS based L1-SINR test

A.7.6.6.1.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.6.1.2-1 and table A.7.6.6.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. After 160 ms from the beginning of the test, the DCI trigger comes in slot 8 of a frame and UE provides the report back based on the reporting configuration as defined in table A.7.6.6.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.7.6.6.1.2-1: General test parameters

Table A.7.6.6.1.2-2: CSI-RS specific test parameters

A.7.6.6.1.3Test Requirements

After 160 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.28.1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.6.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used

## A.7.6.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.2, with the testing configurations for NR cells in table A.7.6.6.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.6.2.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with SSB based CMR and CSI-IM based IMR

## A.7.6.6.2.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.6.2.2-1 and table A.7.6.6.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-IM resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-IM resources as IMR.

Table A.7.6.6.2.2-1: General test parameters

Table A.7.6.6.2.2-2: SSB specific test parameters

## A.7.6.6.2.3Test Requirements

The UE shall send L1-SINR report every 640 slots. No later than X ms plus 640 slots from the beginning of time period T2, UE shall send L1-SINR report including the results for both SSB#0+CSI-IM#0 and SSB#1+CSI-IM#1 while meeting the accuracy requirements defined in clause 10.1.28.2, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2,3 or 4.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used

## A.7.6.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR cofigured in clause 9.8.4.3, with the testing configurations for NR cells in table A.7.6.6.3.1-1.

Table A.7.6.6.3.1-1: Applicable NR configurations for FR2 L1-SINR test with CMR and dedicated IMR

## A.7.6.6.3.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.6.3.2-1 and table A.7.6.6.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-RS as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources and the associated IMR. UE is also configured to measure L1-SINR based on SSB. After 1440 ms from the beginning of the test, the DCI trigger comes in slot 8 of a frame and UE provides the report back based on the reporting configuration as defined in table A.7.6.6.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-RS as IMR.

Table A.7.6.6.3.2-1: General test parameters

Table A.7.6.6.3.2-2: CSI-RS specific test parameters

## A.7.6.6.3.3Test Requirements

After 1440 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 as CMR + CSI-RS#0 as IMR and CSI-RS#1 as CMR + CSI-RS#1 as IMR while meeting the accuracy requirement in clause 10.1.28.3. The reported L1-SINR value shall consider the Rx antenna gain in the range of [-10 ~ +20] dB when calculated.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.6.4L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD

## A.7.6.6.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement when UE supports sbfd-Aware-r19 and SBFD is configured by the network. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.2, with the testing configurations for NR cells in table A.7.6.6.4.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.7.6.6.4.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with SSB based CMR and CSI-IM based IMR

## A.7.6.6.4.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.6.6.4.2-1 and table A.7.6.6.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-IM resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-IM resources as IMR.

Table A.7.6.6.4.2-1: General test parameters

Table A.7.6.6.4.2-2: SSB specific test parameters

## A.7.6.6.4.3Test Requirements

The UE shall send L1-SINR report every 640 slots. No later than X ms plus 640 slots from the beginning of time period T2, UE shall send L1-SINR report including the results for both SSB#0+CSI-IM#0 and SSB#1+CSI-IM#1 while meeting the accuracy requirements defined in clause 10.1.28.2, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2,3 or 4.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.7CSI-RS based intra-frequency Measurements

## A.7.6.7.1SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement

## A.7.6.7.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency measurement requirements in clause 9.10.2. Supported test configurations are shown in table A.7.6.7.1.1-1.

Table A.7.6.7.1.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.7.1.1-2 ~ 6.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.7.6.7.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.7.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

Table A.7.6.7.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap with DRX

## A.7.6.7.1.2Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

-9.6 s for a UE supporting power class 1,

-5.76 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.8CSI-RS based inter-frequency Measurements

## A.7.6.8.1SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2)

## A.7.6.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for CSI-RS based L3 measurement. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.10.3.5.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.8.1.1-1, A.7.6.8.1.1-2, and A.7.6.8.1.1-3.

In test measurement gap pattern configuration # 13 as defined in table A.7.6.8.1.1-2 is provided for UE.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.8.1.1-1.

Table A.7.6.8.1.1-1: SA event triggered reporting tests for CSI-RS based L3 measurement for FR2-FR2

Table A.7.6.8.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 CSI-RS based L3 measurement

Table A.7.6.8.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 CSI-RS based L3 measurement

## A.7.6.8.1.2Test Requirements

In the test the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10880 for UE supporting power class 1, or

## 6720 for UE supporting other power class

The UE is required to read the SSB index indicated by associatedSSB in the neighbour cell in this test

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.9RSTD measurements

## A.7.6.9.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA

## A.7.6.9.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.7.7.1.1-1. The test parameters are as given in table 7.6.7.1.1-2, table A.7.6.9.1.1-3 and , table A.7.6.9.1.1-4.

Table A.7.6.9.1.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.7.6.9.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

Table A.7.6.9.1.-5: Void

## A.7.6.9.1.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.6.9.2 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA

## A.7.6.9.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when dual positioning frequency layer is configured.

Supported test configurations are shown in table A.7.6.9.2.1-1. The test parameters are as given in table 7.6.7.2.1-2, table A.7.6.9.2.1-3 and table A.7.6.9.2.1-4.

Table A.7.6.9.2.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the 2 RF channels distributed in dual positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.7.6.9.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

Table A.7.6.9.2.1-5: Void

## A.7.6.9.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.6.9.3NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR2 SA

## A.7.6.9.3.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured. In this test PRS is transmitted within the active BWP of the UE.

Supported test configurations are shown in table A.7.6.9.3.1-1. The test parameters are as given in table 7.6.9.3.1-2, table A.7.6.9.3.1-3 and table A.7.6.9.3.1-4.

Table A.7.6.9.3.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layer.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples. NsampleNsampleNsample

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.7.6.9.3.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.3.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.3.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.6.9.3.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.1.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.6.9.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA without measurement gap

## A.7.6.9.4.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the gapless RSTD measurement requirements specified in clause 9.9.2.7 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured. Reporting delay test for gapless PRS measurement is conducted assuming that the PRS has higher priority, i.e., state 1, than all other DL signals/channels and is transmitted within active DL BWP of UE. Two sub-tests are defined, sub-test 1 is for Nsample = 4 and sub-test 2 is for Nsample = 1. For sub-test 2 LMF indicates UE to perform PRS measurement with reduced number of samples  via reducedDL-PRS-ProcessingSamples.NsampleNsample

Supported test configurations are shown in table A.7.6.9.4.1-1. The test parameters are as given in table A.7.6.9.4.1-2, table A.7.6.9.4.1-3, and table A.7.6.9.4.1-4.

Table A.7.6.9.4.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first PRS processing window instance containing the PRS resources.

The UE is configured with PPW before T2.

Table A.7.6.9.4.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.4.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.4.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.6.9.4.2Test Requirements

The RSTD measurement time fulfils the gapless RSTD measurement reporting delay requirements specified in clause 9.9.2.7.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2.7 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.6.9.5NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state with Rx TEG

## A.7.6.9.5.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the Rx TEG based measurement period requirements specified in clause 9.9.2.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.7.6.9.5.1-1. The test parameters are as given in table A7.6.9.5.1-2, table A.7.6.9.5.1-3 and, table A.7.6.9.5.1-4.

Table A.7.6.9.5.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layer.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

The test applies to the UE supporting Rx TEG indicated via NR-UE-TEG-Capability and is requested to provide the Rx TEG in the test via nr-UE-RxTEG-Request-r17 in NR-TDOA-RequestLocationInformation. In the location request measureSameDL-PRS-ResourceWithDifferentRxTEGs-r17 is set to n0. The UE shall perform and optionally report the Rx TEG based RSTD measurements.

The UE is capable of performing Rx TEG based RSTD measurements. UE may or may not be able to receive same DL PRS resource from the same TRP simultaneously from multiple Rx TEGs.

Table A.7.6.9.5.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.5.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.5.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.6.9.5.2Test Requirements

The RSTD measurement time fulfils the Rx TEG based RSTD measurement period requirements specified in clause 9.9.2.5. The UE shall perform and report the Rx TEG based RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.7.6.9.6NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode

## A.7.6.9.6.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement performed by UE by aggregating PRS resources from multiple positioning frequency layers (PFLs) meets the requirements specified in clause 9.9.2.10 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.7.6.9.6.1-1.

Table A.7.6.9.6.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, all cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS resources on two positioning frequency layers during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The UE is capable of performing RSTD measurements by aggregating PRS resources from two PFLs and is configured by the LMF to perform measurements by aggregating the PRS resources from two positioning frequency layers via nr-DL-PRS-JointMeasurementRequestedPFL-List. The NR-DL-TDOA-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first measurement gap instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

The general test parameters are listed in table A.7.6.9.6.1-2, and cell specific test parameters are listed in table A.7.6.9.6.1-3 during T1 and table A.7.6.9.6.1-4 during T2.

Table A.7.6.9.6.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.6.9.6.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.9.6.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.6.9.6.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9.2.10.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2.10 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.2, i.e., between RSTD_000000000 and RSTD_126083073.

## A.7.6.10 PRS-RSRP measurements

## A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer

## A.7.6.10.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.6.10.1.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.10.1.1-2, and table A.7.6.10.1.1-3.

Table A.7.6.10.1.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

Table A.7.6.10.1.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.6.10.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.7.6.10.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.5.The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.6.10.2PRS-RSRP reporting delay test case for dual positioning frequency layer

## A.7.6.10.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9.3.5 for dual positioning frequency layers under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.6.10.2.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the different frequency from the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.10.2.1-2, and table A.7.6.10.2.1-3.

Table A.7.6.10.2.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

Table A.7.6.10.2.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.6.10.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.7.6.10.2.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.5.The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.6.10.3PRS-RSRP reporting delay test case for reduced number of samples

## A.7.6.10.3.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements for reduced number of samples specified in clause 9.9.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.6.10.3.1-1. In this test PRS is transmitted within the active BWP of the UE.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples.NsampleNsample

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.10.3.1-2, and table A.7.6.10.3.1-3.

Table A.7.6.10.3.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

Table A.7.6.10.3.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.6.10.3.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.7.6.10.3.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.6.10.4PRS-RSRP reporting delay test case for single positioning frequency layer outside MG

## A.7.6.10.4.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement outside MG requirements specified in clause 9.9.3.6 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. There are two sub-tests in the test, sub-test 1 is to verify the delay requirements with Nsample=1, and sub-test 2 is to verify the delay requirements with Nsample=4.

Supported test configurations are shown in table A.7.6.10.4.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In sub-test 1, reducedDL-PRS-ProcessingSamples shall be included in the location information request and set to ‘requested’, and lowerRxBeamSweepingThan8-FR2 shall be included.

During T1, a PPW shall be configured for the PCell and be activated via DL MAC CE. The last PDSCH containing the MAC CE shall be transmitted before slot #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first PPW instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are as given in table A.7.6.10.4.1-2, and cell specific test parameters during T2 are listed in table A.7.6.10.4.1-3.

Table A.7.6.10.4.1-1: supported test configurations for PRS RSRP measurement for FR2

Table A.7.6.10.4.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.6.10.4.1-3: Cell-specific test parameters during T2 for PRS RSRP measurement reporting delay

## A.7.6.10.4.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.6, with Nsample=1 for sub-test 1 and Nsample=4 for sub-test 2. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.3.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.6.11UE Rx-Tx time difference measurements

## A.7.6.11.1UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA

## A.7.6.11.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.7.6.11.1.1-1.

Table A.7.6.11.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.1.1-2 and table A.7.6.11.1.1-3 respectively.

Table A.7.6.11.1.1-2: General test parameters

Table A.7.6.11.1.1-3: Cell specific test parameters

Table Table A.7.6.11.1.1-4: Void

## A.7.6.11.1.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.6.11.2UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA

## A.7.6.11.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR2 in standalone scenario when dual positioning frequency layers are cnfigured.

The supported test configurations in listed in table A.7.6.11.2.1-1.

Table A.7.6.11.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on different RF channels in FR2.

transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.2.1-2 and table A.7.6.11.2.1-3 respectively.

Table A.7.6.11.2.1-2: General test parameters

Table A.7.6.11.2.1-3: Cell specific test parameters

Table Table A.7.6.11.1.1-4: Void

## A.7.6.11.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.6.11.3UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with reduced sample number

## A.7.6.11.3.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 with Nsample = 1 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured. In this test PRS is transmitted within the active BWP of the UE. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples.NsampleNsample

The supported test configurations are listed in table A.7.6.11.3.1-1.

Table A.7.6.11.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.3.1-2 and table A.7.6.11.3.1-3 respectively.

Table A.7.6.11.3.1-2: General test parameters

Table A.7.6.11.3.1-3: Cell specific test parameters

## A.7.6.11.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5 with Nsample=1.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.6.11.4UE Rx-Tx time difference measurements without gaps in FR2 SA

## A.7.6.11.4.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.6 in AWGN propagation condition in FR2 in standalone scenario. There are two sub-tests in the test, sub-test 1 is to verify the delay requirements with Nsample=1, and sub-test 2 is to verify the delay requirements with Nsample=4.

The supported test configurations are listed in table A.7.6.11.4.1-1.

Table A.7.6.11.4.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of PRS processing window containing the PRS resources.

The UE is configured with PRS processing window before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.4.1-2 and table A.7.6.11.4.1-3 respectively.

Table A.7.6.11.4.1-2: General test parameters

Table A.7.6.11.4.1-3: Cell specific test parameters

## A.7.6.11.4.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.6.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.6.11.5UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with RxTx TEG

## A.7.6.11.5.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 9.9.4.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured, and when UE is requested to measure a PRS resource with RxTx TEG.

The supported test configurations are listed in table A.7.6.11.5.1-1.

Table A.7.6.11.5.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The test applies to the UE supporting RxTx TEG indicated via NR-UE-TEG-Capability and is requested to provide the RxTx TEG in the test via nr-UE-RxTxTEG-Request-r17 in nr-Multi-RTT-RequestLocationInformation. The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request. In nr-Multi-RTT-RequestLocationInformation, measureSameDL-PRS-ResourceWithDifferentRxTxTEGs-r17 shall be set to ‘n2’.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.5.1-2 and table A.7.6.11.5.1-3 respectively.

Table A.7.6.11.5.1-2: General test parameters

Table A.7.6.11.5.1-3: Cell specific test parameters

## A.7.6.11.5.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.5, with =2 if UE does not support or indicate value ‘n1’ for measureSameDL-PRS-ResourceWithDifferentRxTEGsSimul, and =1 otherwise.kmultiTEGkmultiTEG

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.6.11.6UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA

## A.7.6.11.6.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 9.9.4.9 for UE Rx-Tx measurements with PRS bandwidth aggregation. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR2.

The supported test configurations are listed in table A.7.6.11.6.1-1.

Table A.7.6.11.6.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The general test parameters and cell specific test parameters are as given in table A.7.6.11.6.1-2 and table A.7.6.11.6.1-3 respectively.

Table A.7.6.11.6.1-2: General test parameters

Table A.7.6.11.6.1-3: Cell specific test parameters

## A.7.6.11.6.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.4.9.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.

## A.7.6.12PRS-RSRPP measurements

## A.7.6.12.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_CONNECTED state

## A.7.6.12.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement requirements specified in clause 9.9.6.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.6.12.1.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.12.1.1-2, and table A.7.6.12.1.1-3.

Table A.7.6.12.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.7.6.12.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.7.6.12.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

## A.7.6.12.1.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 9.9.6.5.The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.6.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1.38, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.7.6.12.2PRS-RSRPP reporting delay test case for reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state

## A.7.6.12.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement requirements specified in clause 9.9.6.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.6.12.2.1-1. In this test PRS is transmitted within the active BWP of the UE. UE can support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the LMF indicates the UE to perform positioning measurements with reduced number of samples  via reducedDL-PRS-ProcessingSamples.NsampleNsample

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.12.2.1-2, and table A.7.6.12.2.1-3.

Table A.7.6.12.2.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.7.6.12.2.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.7.6.12.2.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

## A.7.6.12.2.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 9.9.6.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.6.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1.38, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.7.6.12.3PRS-RSRPP reporting delay test case for gapless measurement in FR2

## A.7.6.12.3.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement requirements specified in clause 9.9.6.6 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Reporting delay test for gapless PRS measurement is conducted assuming that the PRS has higher priority, i.e., state 1, than all other DL signals/channels and is transmitted within active DL BWP of UE. Two sub-tests are defined, sub-test 1 is for Nsample = 4 and sub-test 2 is for Nsample = 1. For sub-test 2 LMF indicates UE to perform PRS measurement with reduced number of samples  via reducedDL-PRS-ProcessingSamples.NsampleNsample

The supported test configurations are shown in table A.7.6.12.3.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first PRS processing window instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.6.12.3.1-2, and table A.7.6.12.3.1-3.

Table A.7.6.12.3.1-1: supported test configurations for PRS RSRPP measurement for FR2-FR2

Table A.7.6.12.3.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.7.6.12.3.1-3: Cell-specific test parameters during T2

## A.7.6.12.3.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9.6.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %.

## A.7.6.13UE Rx-Tx time difference measurements for PDC

## A.7.6.13.1UE Rx-Tx time difference measurement for propagation delay compensation using PRS in FR2

## A.7.6.13.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement for RTT-based PDC meets the requirements specified in clause 9.12.4.1in AWGN propagation condition in FR2 in standalone scenario.

The supported test configurations in listed in table A.7.6.13.1.1-1.

Table A.7.6.13.1.1-1: Supported test configurations

The test is considered with one cell (Cell 1) in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. If the test is based on PRS, the Cell 1 mutes PRS transmission during T1 and transmits PRS during T2.

The MeasObjectRxTxDiff-r17 with prs-Ref-r17 , measObject  with measObjectRxTxDiff-17, and NR-DL-PRS-PDC-Info as defined in TS 38.331 shall be provided to the UE during T1.

The last TTI containing the RRC configuration shall be provided to the UE T ms before the start of T2, where T = 10 ms.

The beginning of the time interval T2 shall be aligned with the beginning of the first PRS resources.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.13.1.1-2. The test parameters for PRS are given Table A.7.6.13.1.1-3.

Table A.7.6.13.1.1-2: General test parameters

Table A.7.6.13.1.1-3: Cell specific test parameters

## A.7.6.13.1.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in 9.12.4.1.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

The reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1, for k=5.

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.39.2 for Cell 1.

## A.7.6.13.2UE Rx-Tx time difference measurement for propagation delay compensation using TRS in FR2

## A.7.6.13.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with TRS for RTT-based PDC meets the requirements specified in clause 9.12.4.2 for measurement delay and clause 10.1.39.3 for measurement accuracy in AWGN propagation condition in FR2 in standalone scenario.

The supported test configurations in listed in table A.7.6.13.2.1-1.

Table A.7.6.13.2.1-1: Supported test configurations

The test is considered with one cell (Cell 1) in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 does not have TRS transmission during T1 and transmits TRS during T2.

The MeasObjectRxTxDiff-r17 with csi-RS-Ref-r17, and measObject  with measObjectRxTxDiff-17 as defined in TS 38.331 shall be provided to the UE during T1.

The last TTI containing the RRC configuration shall be provided to the UE T ms before the start of T2, where T = [10] ms is the maximum processing time of the measurement request.

The beginning of the time interval T2 shall be aligned with the beginning of the first TRS resources.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.6.13.2.1-2. The test parameters for PRS are given Table A.7.6.13.2.1-3.

Table A.7.6.13.2.1-2: General test parameters

Table A.7.6.13.2.1-3: Cell specific test parameters

## A.7.6.13.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in 9.12.4.2.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.39.3.

The reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1, for k=5.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %.

## A.7.6.14SA event triggered reporting tests with Pre-MG

## A.7.6.14.1Intra-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MG in FR2

## A.7.6.14.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with autonomous activation/deactivation of Pre-MG. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.7.6.14.1.2Test parameters

Supported test configurations are shown in table A.7.6.14.1.2-1. There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.14.1.2-2, A.7.6.14.1.2-3 and A.7.6.14.1.2-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A4 is used.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

BWP-1 includes bandwidth of the initial DL BWP and SSB.

BWP-2 does not include bandwidth of the initial DL BWP and SSB.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

The TE schedules ontinuous DL data on PCell throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2 and T3, respectively.

During time period T1, BWP-1 is the active BWP. The Pre-MG is expected to be deactivated. UE shall be able to measure neighbor cell without gap.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

During time period T3, BWP-2 is the active BWP. The Pre-MG is expected to be activated. UE shall be able to measure neighbor cell within Pre-MG.

Table A.7.6.14.1.2-1: supported test configurations

Table A.7.6.14.1.2-2: General test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

Table A.7.6.14.1.2-3: NR Cell specific test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

Table A.7.6.14.1.2-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

## A.7.6.14.1.3Test Requirements

During T1, the UE shall be able to receive PDSCH and report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions.

During T2 and T3, the UE shall not report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions, starting from the 1 st complete Pre-MG occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) + 5 ms as defined in clause 8.19.2.

The UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T3, where Y is

-3.2 s for a UE supporting power class 1 and 5,

-1.92 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.14.2Intra-frequency measurement test with SA event triggered reporting tests: with network-controlled activation/deactivation of Pre-MG in FR2

## A.7.6.14.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with network-controlled activation/deactivation of Pre-MG. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.7.6.14.2.2Test parameters

Supported test configurations are shown in table A.7.6.14.2.2-1. There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.14.2.2-2, A.7.6.14.2.2-3 and A.7.6.14.2.2-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

BWP-1 includes bandwidth of the initial DL BWP and SSB with the Pre-MG status set to ‘deactivated’.

BWP-2 does not include bandwidth of the initial DL BWP and SSB with the Pre-MG status set to ‘activated’.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

The TE schedules continuous DL data on PCell throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2 and T3, respectively.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The time period T3 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted j. The UE shall switch its bandwidth part from BWP-2 to BWP-1.

Table A.7.6.14.2.2-1: supported test configurations

Table A.7.6.14.2.2-2: General test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

Table A.7.6.14.2.2-3: NR Cell specific test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

Table A.7.6.14.2.2-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting with network-controlled activation/deactivation of Pre-MG

## A.7.6.14.2.3Test Requirements

During T2, the UE shall not report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions, starting from the 1 st complete Pre-MG occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) + 5 ms as defined in clause 8.19.2.

During T3, the UE shall be able to receive PDSCH and report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots overlapped with the Pre-MG occasions, starting from the 1 st complete Pre-MG occasion after the beginning of PCell’s DL slot (j+TBWPswitchDelay) + 5 ms as defined in clause 8.19.2.

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T3, where X is

-1.6 s for a UE supporting power class 1 and 5,

-0.96 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.15SA event triggered reporting tests with concurrent gaps

## A.7.6.15.1SA event triggered reporting tests For FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

## A.7.6.15.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: NR cell 1 as PCell in FR2 on NR RF channel 1, NR cell 2 as neighbour cell in FR2 on NR RF channel 2, and NR cell 3 as neighbour cell in FR2 on NR RF channel 3. The test parameters and configurations are given in tables A.7.6.15.1.1-1, A.7.6.15.1.1-2, and A.7.6.15.1.1-3.

Two measurement gaps with pattern configuration # 14 as defined in table A.7.6.15.1.1-2 are provided for UE. The measurement object for NR RF channel 2 is associated with MG#1, and measurement object for NR RF channel 3 is associated with MG#2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2 or NR cell 3.

Supported test configurations are shown in table A.7.6.15.1.1-1.

Table A.7.6.15.1.1-1 SA event triggered reporting tests without SSB index reading for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

Table A.7.6.15.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

Table A.7.6.15.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

## A.7.6.15.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report for each neighboring cell, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 10240 for UE supporting power class 1 and 5, or

## 6400 for UE supporting other power class.

The  UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.15.2SA event triggered reporting tests For FR2 with concurrent measurement gaps without SSB time index detection when DRX is not used (PCell in FR2)

## A.7.6.15.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for each neighbour cell. This test will partly verify the SA inter-frequency NR cell search requirements and collision handling between two partially-partial overlapping gaps in clause 9.1.8.

In this test, there are three cells: NR cell 1 as PCell in FR2 on NR RF channel 1, NR cell 2 as neighbour cell in FR2 on NR RF channel 2 and NR cell 3 as another neighbour cell in FR2 on NR RF channel 3.  The test parameters and configurations are given in tables A.7.6.15.2.1-1, A.7.6.15.2.1-2, and A.7.6.15.2.1-3.

Two measurement gaps are configured to UE with measurement gap pattern configuration #13 and #14 respectively. Measurement gap with pattern #13 is associated with inter-frequency measurement on NR cell 2, and measurement gap with pattern #14 is associated with inter-frequency measurement on NR cell 3.  Measurement gap pattern configuration # 13 and #14 as defined in table A.7.6.15.2.1-2  are provided to for UE that does not support per-FR gap and for UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2 and NR cell 3.

Supported test configurations are shown in table A.7.6.15.2.1-1.

Table A.7.6.15.2.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.15.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements without SSB time index detection

Table A.7.6.15.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.15.2.2Test Requirements

For both NR cell 2 and NR cell 3, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 10240 for UE supporting power class 1 and 5, or

## 6400 for UE supporting other power class.

The  UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.15.3SA event triggered reporting tests for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS-based measurement

## A.7.6.15.3.1Test Purpose and Environment

The purpose of this test is to verify that the concurrent gap capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4 and PRS-RSRP measurement delay requirements specified in clause 9.9.3.5.

In this test, there are three cells: NR cell 1 as PCell in FR2 on NR RF channel 1, NR cell 2 as neighbour cell in FR2 on NR RF channel 2, and NR cell 3 as neighbour cell in FR2 on NR RF channel 1.  The test parameters are given in tables A.7.6.15.3.1-1, A.7.6.15.3.1-2 and A.7.6.15.3.1-3.

Two measurement gap patterns (MeasGapId #0 and MeasGapId #1) are configured with the gap pattern ID #0 and #1 as defined in table A.7.6.15.3.1-2. MeasGapId #1 is configured with a higher priority than MeasGapId #0. MeasGapId #0 and MeasGapId #1 are associated with the MOs for RF channel numbers #1 and #2, respectively.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used for carrier 2. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2 and NR cell 3. Cell 1 and cell 3 transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance of MeasGapId #1 containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

Table A.7.6.15.3.1-1: SA event triggered reporting tests for FR2

Table A.7.6.15.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS measurement

Table A.7.6.15.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 concurrent gap with partially-partial overlapping scenario for SSB-based measurements and PRS measurement

## A.7.6.15.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report for cell 2, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 10240 for UE supporting power class 1 and 5, or

## 6400 for UE supporting other power class.

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 3 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9.3.5 starting from the beginning of time interval T2.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

IUE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.16SA event triggered reporting tests with NCSG

## A.7.6.16.1SA event triggered reporting test with per-UE NCSG under non-DRX

## A.7.6.16.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.7.1 and 9.2.7.2, and also verify the scheduling availability during intra-frequency measurement with NCSG in clause 9.2.7.3. Supported test configurations are shown in table A.7.6.16.1.1-1.

The serving frequency should be selected for which UE reports ‘ncsg’.

Table A.7.6.16.1.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.16.1.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

During T2, the UE is continuously scheduled with data on the PCell.

The UE is capable of NCSG and report ‘ncsg’ through NeedForGapNCSG-InfoNR for PCell.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.16.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE NCSG without DRX

Table A.7.6.16.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE NCSG without DRX

Table A.7.6.16.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE NCSG without DRX

Figure A.7.6.16.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.16.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3.2 s for a UE supporting power class 1 and 5,

-1.92 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T2, UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots except for the case where PDSCH or PUCCH is overlapped with the VIL of NCSG pattern.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.16.2SA event triggered reporting tests on inter-frequency measurement with NCSG for FR2 when DRX is not used (PCell in FR2)

## A.7.6.16.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.10. The test will partly verify the interruption requirements on PCell in clause 9.1.9.1.

The serving frequency and the target frequency should be selected such that UE reports ‘ncsg’ for the target frequency given the serving frequency.

In this test, there are two cells: NR cell 1 as PCell in FR2 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.7.6.16.2.1-1, A.7.6.16.2.1-2, and A.7.6.16.2.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Supported test configurations are shown in table A.7.6.16.2.1-1.

Table A.7.6.16.2.1-1 SA event triggered reporting tests with NCSG without SSB index reading for FR2-FR2

Table A.7.6.16.2.1-2: General test parameters for SA inter-frequency event triggered reporting with NCSG for FR2 without SSB time index detection

Table A.7.6.16.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting with NCSG for FR2 without SSB time index detection

## A.7.6.16.2.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1 and 5, or

## 3200 for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall be scheduled on PCell continuously throughout the test. During the time duration T2, the interruption on PCell shall not be more than the values specified for SA in clause 9.1.9.1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

NOTE:For a UE that supports per-FR NCSG, it only needs to pass test case with per-FR NCSG, otherwise, it only needs to pass test case with per-UE NCSG.

## A.7.6.16.3Event triggered reporting test on deactivated SCell measurement via NCSG in FR2 in non-DRX

## A.7.6.16.3.1Test Purpose and Environment

The purpose of this test is to verify that the delay and interruption requirements for deactived SCell measurement stated in clause 9.2.7 and 8.2 respectively, when both PCell and SCell are in FR2.

The supported test configurations are shown in table A.7.6.16.3.1-1 below. The general test parameters are defined in table A.7.6.16.3.1-2. Three cells are deployed in the test, which are one FR2 PCell (Cell 1) on frequency 1 and one FR2 SCell (Cell 2) on frequency 2 and one neighboring cell (Cell 3) on frequency 2. The cell-specific test parameters are given in A.7.6.16.3.1-3 below. OTA related test parameters are shown in table A.7.6.16.3.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of 2 successive time periods, with duration of T1 and T2, respectively.

Before the test starts the UE is connected to PCell (Cell 1) but is not aware of SCell (Cell 2) nor the neighboring cell (Cell 3). The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the deactivated SCC.

NCSG is configured with the NCSG pattern ID #0 as defined in table A.7.6.16.3.1-2.

Table A.7.6.16.3.1-1: Supported test configurations for FR2 deactivated SCell measurement via NCSG

Table A.7.6.16.3.1-2: General test parameters for FR2 deactivated SCell measurement via NCSG

Table A.7.6.16.3.1-3: Cell specific test parameters for FR2 deactivated SCell measurement via NCSG

Table A.7.6.16.3.1-4: OTA related test parameters for FR2 deactivated SCell measurement via NCSG

## A.7.6.16.3.2Test Requirements

UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 12.8 s for UE supporting power class 1 and 5, or

## 7.68 s for UE supporting other power class.

UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

During the T1 and T2, UE be able to report ACK/NACK for all slots with PDCCH/PDSCH on PCell excluding those slots overlapped with

VIL1, ML and VIL2 of NCSG for intra-band FR2 CA

VIL1 and VIL2 of NCSG for inter-band FR2 CA

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.17SA event triggered reporting tests for concurrent measurement gaps with Pre-MG in FR2

## A.7.6.17.1SA event triggered reporting test for FR2 with one pre-configured gap and one measurement gap

## A.7.6.17.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with with one pre-configured gap and one measurement gap for SSB-based measurements. This test will partly verify the SA NR cell search requirements in clause 9.2.5 and 9.3.4, pre-configured gap activation delay in clause 8.19 and measurement gap collision handling in clause 9.1.12.

In this test, there are three cells: NR cell 1 as PCell in FR2 on NR RF channel 1, NR cell 2 as intra-frequency neighbour cell in FR2 on NR RF channel 1, and NR cell 3 as inter-frequency neighbour cell in FR2 on NR RF channel 2.

Two measurement gaps with pattern configuration # 13 and 14 as defined in table A.7.6.17.1.1-2 are provided for UE. The measurement object #1 for NR RF channel 1 is associated with MG#1, and measurement object #2 for NR RF channel 2 is associated with MG#2. MG#1 is a pre-configured measurement gap, and with higher priority than MG#2.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

BWP-1 includes bandwidth of the initial DL BWP and SSB with the Pre-MG status set to ‘deactivated’ (preConfGapStatus of the pre-MG on BWP-1 is set to ‘0’).

BWP-2 does not include bandwidth of the initial DL BWP and SSB with the Pre-MG status set to ‘activated’ (preConfGapStatus of the pre-MG on BWP-2 is set to ‘1’).

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

The TE schedules continuous DL data on PCell throughout the test.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of 2 successive time periods, with durations of T1 and T2, respectively. Before the test starts, the UE shall not have any timing information of NR Cell 2 or NR Cell 3.

During T1, UE active DL BWP is BWP-1, and the pre-configured gap (MG#1) is deactivated. Cell 3 is switched ON from the beginning of T1, and UE is expected to search for Cell 3 in MG#2.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted by i. The UE shall switch its DL active BWP from BWP-1 to BWP-2, and the pre-configured gap shall be activated. Cell 2 is switched ON from the beginning of T2, and UE is expected to search for Cell 2 in MG#1.

Supported test configurations are shown in table A.7.6.17.1.1-1. The general and cell specific test parameters are given in tables A.7.6.17.1.1-2, and A.7.6.17.1.1-3.

Table A.7.6.17.1.1-1 SA event triggered reporting tests without SSB index reading for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

Table A.7.6.17.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

Table A.7.6.17.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements

## A.7.6.17.1.2Test Requirements

For UE supporting dynamicCollision-r18:

During T1, the UE shall report ACK/NACK for PDSCHs scheduled in the slots that are not overlapped with the MG#2 occasions. The UE shall send one Event A3 triggered measurement report for Cell 3, with a measurement reporting delay less than X ms from the beginning of time period T1, where X is

## 5120 for UE supporting power class 1 and 5, or

## 3200 for UE supporting other power class.

X is derived based on the requirements for inter-frequency measurement in clause 9.3.4 and 9.3.5.

For UE not supporting dynamicCollision-r18:

During T1, the UE shall report ACK/NACK at least for PDSCHs scheduled in the slots that are not overlapped with the non-dropped MG#2 occasions. The UE shall send one Event A3 triggered measurement report for Cell 3, with a measurement reporting delay less than X ms from the beginning of time period T1, where X is

## 10240 for UE supporting power class 1 and 5, or

## 6400 for UE supporting other power class.

X is derived based on the requirements for inter-frequency measurement in clause 9.3.4 and 9.3.5.

For both UE supporting FG dynamicCollision-r18 and not supporting dynamicCollision-r18:

During T2, the UE shall report ACK/NACK for PDSCHs scheduled in the slots that are not overlapped with the MG#1 occasions or non-dropped MG#2 occasions after MG#1 is activated, i.e. starting from the 1 st complete MG#1 occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) + 5 ms as defined in clause 8.19.2. The UE shall send one Event A3 triggered measurement report for Cell 2, with a measurement reporting delay less than Y ms from the beginning of time period T2, where Y is

## 6480 for UE supporting power class 1 and 5, or

## 3920 for UE supporting other power class.

Y is derived based on the requirements for intra-frequency measurement in clause 9.2.6 plus 80 ms, considering that the frist MG#1 occasion in T2 may collide with the pre-configured gap activation delay.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.17.2Inter-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MGs in FR2

## A.7.6.17.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with autonomous activation/deactivation of Pre-MGs within FR2 concurrent gaps. This test will partly verify the TDD inter-frequency cell search requirements in clause 9.2.6.and 9.3.4. Also, this test will also jointly verify pre-configured measurement gap activation/deactivation delay in clause 8.19.2.

## A.7.6.17.2.2Test parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) in FR1 on NR RF channel 1 and a neighbour cell (Cell 2) in FR2 on NR RF channel 2. The supported test configurations are shown in table A.7.6.17.2.2-1. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.17.2.2-2, A.7.6.17.2.2-3 and A.7.6.17.2.2-4 below.

Two pre-configured measurement gaps with same pattern (# 13) but different offset as defined in table A.7.6.17.2.2-2 are provided for UE. The measurement object for NR RF channel 1 is associated with MG#1, and measurement object for NR RF channel 2 is associated with MG#2.

In the measurement control information, two measurement object is configured for the frequency of the PCell and neihghbour cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

UE is configured with 2 different UE-specific bandwidth parts for Cell 1 (PCell), BWP-1 and BWP-2, before starting the test.

BWP-1 includes bandwidth of the initial DL BWP and SSBs.

BWP-2 does not include bandwidth of the initial either switched DL BWP and SSBs.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

The TE schedules continuous DL data on PCell throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2 and T3, respectively.

During time period T1, BWP-1 is the active BWP. The Pre-MG#1 is expected to be deactivated and the Pre-MG#2 is expected to be activated. UE shall be able to measure Cell 1 without gap but Cell 2 with the activated Pre-MG#2.

The time period T2 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i.

During time period T3, BWP-2 is the active BWP. Both Pre-MG#1 and Pre-MG#2 expected to be activated. UE shall be able to measure Cell 1 and Cell 2 with the activated Pre-MG#1 and Pre-MG#2 respectively.

Table A.7.6.17.2.2-1: supported test configurations

Table A.7.6.17.2.2-2: General test parameters for intra-frequency event triggered reporting with  autonomous activation/deactivation of Pre-MG

Table A.7.6.17.2.2-3: NR Cell specific test parameters for intra-frequency event triggered reporting with autonomous activation/deactivation of Pre-MG

Table A.7.6.17.2.2-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting with automous activation/deactivation of Pre-MG

## A.7.6.17.2.3Test Requirements

During T1, the UE shall be able to receive PDSCH and report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the Pre-MG#2 occasions.

During T2 and T3, the UE shall be able to receive PDSCH and report corresponding valid ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the Pre-MG#1 or Pre-MG#2 occasions, starting from the 1 st complete Pre-MG#1 occasion after the beginning of PCell’s DL slot (i+TBWPswitchDelay) + 5 ms as defined in clause 8.19.5.

The UE shall send one Event A3 triggered measurement report for measurements on cell 2, with a measurement reporting delay less than Y ms from the beginning of time period T3, where Y is

-5120 ms for a UE supporting power class 1 and 5,

-3200 ms for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.18SA event triggered reporting tests with concurrent gaps and NCSG

## A.7.6.18.1SA event triggered reporting tests For FR2 with concurrent measurement gaps and NCSG without SSB time index detection when DRX is not used (PCell in FR2)

## A.7.6.18.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for each neighbour cell. This test will partly verify the SA inter-frequency NR cell search requirements and collision handling between partially-partial overlapped concurrent gaps and NCSG in clause 9.1.13.

In this test, there are three cells: NR cell 1 as PCell in FR2 on NR RF channel 1, NR cell 2 as neighbour cell in FR2 on NR RF channel 2 and NR cell 3 as another neighbour cell in FR2 on NR RF channel 3.  The test parameters and configurations are given in tables A.7.6.18.1.1-1, A.7.6.18.1.1-2, and A.7.6.18.1.1-3.

During T2, the UE is continuously scheduled with data on the PCell when measuring within NCSG.

One measurement gap and one NCSG are configured to UE with measurement gap pattern #13 and NCSG pattern #14 respectively. Measurement gap with pattern #13 is associated with inter-frequency measurement on NR cell 2, and NCSG with pattern #14 is associated with inter-frequency measurement on NR cell 3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2 and NR cell 3.

Supported test configurations are shown in table A.7.6.18.1.1-1.

Table A.7.6.18.1.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.7.6.18.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 partially overlapped concurrent gap and NCSG for SSB-based measurements without SSB time index detection

Table A.7.6.18.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.7.6.18.1.2Test Requirements

For both NR cell 2 and NR cell 3, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 10240 for UE supporting power class 1 and 5, or

## 6400 for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

During the T1 and T2, UE shall be able to report ACK/NACK for all slots with PDCCH/PDSCH on PCell excluding those slots overlapped with

VIL1 and VIL2 of NCSG

Measurement gap

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.19SA event triggered reporting tests with NeedForGap in FR2

## A.7.6.19.1SA event triggered reporting test for UE indicating NeedforInterruptionInfoNR under non-DRX and no interruption outside configured measurement gaps

## A.7.6.19.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test partly verifies the TDD intra-frequency cell search and measurement requirements in clause 9.2.6.1 and 9.2.6.2. This test also verifies that the UE does not cause interruption outside measurement gap when SMTC occasions overlap with measurement gap occassions. Supported test configurations are shown in table A.7.6.19.1.1-1.

The UE who passes this test can skip the corresponding Rel-15 test cases.

Table A.7.6.19.1.1-1: supported test configurations

There are two cells in the test, a FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.19.1.1-2, A.7.6.19.1.1-3 and A.7.6.19.1.1-4 below. The serving frequency selected for this test case should be one in which the UE reports NeedForGapsInfoNR-r16 = ‘no-gap’ and NeedForInterruptionInfoNR-r18 = ‘no-gap-with-interruption’ for the PCell.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE operates in an active BWP which does not contain cell-defined SSB so that the UE uses configured measurement gaps to measure on the intra-frequency target SSB.

The TE schedules continuous DL data on PCell throughout the test.

Table A.7.6.19.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2

Table A.7.6.19.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2

Table A.7.6.19.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2

Figure A.7.6.19.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.19.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3200 ms for a UE supporting power class 1 and 5,

-1920 ms for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

UE shall report corresponding HARQ-ACK/NACK for those PDSCHs scheduled in the slots that are not overlapped with the measurement gap. UE is not allowed to cause any interruption outside the configured measurement gap occasions.

## A.7.6.19.2SA event triggered reporting test without gap under non-DRX

## A.7.6.19.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.7.6.19.2.1-1.

Table A.7.6.19.2.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.19.2.1-2, A.7.6.19.2.1-3 and A.7.6.19.2.1-4 below. The serving frequency selected for this test case should be one in which the UE reports NeedForGapsInfoNR-r16 = ‘no-gap’ and NeedForInterruptionInfoNR-r18 = ‘no-gap-no-interruption’ for the PCell.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The TE schedules continuous DL data on PCell throughout the test.

Table A.7.6.19.2.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.19.2.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.19.2.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Figure A.7.6.19.2.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.7.6.19.2.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-1.6 s for a UE supporting power class 1 and 5,

-1.08 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

UE shall report corresponding HARQ-ACK/NACK for all PDSCHs scheduled during the test.

## A.7.6.19.3SA event triggered reporting test without gap without interruption under non-DRX

## A.7.6.19.3.1Test Purpose and Environment

The purpose of this test is to verify that if UE reports “no-gap” via interFreq-needForGap-r16 and reports “no-gap-no-interruption” via interFreq-needForInterruption-r18, the UE makes correct reporting of an event. This test will partly verify the inter-frequency without gap cell search requirements in clause 9.3.9. Supported test configurations are shown in table A.7.6.19.3.1-1.

Table A.7.6.19.3.1-1: supported test configurations

There are two cells in the test, NR cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters for the Cell 1 and Cell 2 are given in tables A.7.6.19.3.1-2, A.7.6.19.3.1-3 and A.7.6.19.3.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the neighbour cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.7.6.19.3.1-2: General test parameters for inter-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without interruption

Table A.7.6.19.3.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.19.3.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

## A.7.6.19.3.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4s for a UE supporting power class 1,

-1.44s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

During the T1 and T2, UE shall be able to report ACK/NACK for all slots with PDCCH/PDSCH on PCell excluding those symbles as defined in clause 9.3.9.4.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.20LTM Intra-frequency L1-RSRP measurement

## A.7.6.20.1Intra-frequency SSB based L1-RSRP measurement in FR2

## A.7.6.20.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SSB based intra-frequency L1-RSRP measurement on neighbor cell in FR2. This test will partly verify the L1-RSRP measurement requirements in clause 9.14, with the testing configurations for NR cells in table A.7.6.20.1.1-1.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

Table A.7.6.20.1.1-1: Applicable NR configurations for SSB based Intra-frequency L1-RSRP LTM measurement with activated TCI state test in FR2

## A.7.6.20.1.2Test parameters

There are two cells in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

Measurement period and measurement accuracy is tested by using the parameters in table A.7.6.20.1.2-1 and table A.7.6.20.1.2-2.

There are two tests in the test case, test 1 and test 2:

-In test 1, time offset between cells is within CP length.

-In test 2, time offset between cells is larger than CP length.

If a UE does not support multiCellL1-measRTD-greaterThan-CP-r18, it is only required to pass test 1. Otherwise, it is only required to pass test 2.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs, and report measurement results periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-The UE has performed L3 measurement on Cell 2.

At the beginning of T2, SSB_RP of Cell 2 change to different values from T1. T2 starts at the beginning of a frame with an odd SFN.

Table A.7.6.20.1.2-1: General test parameters for SSB based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

Table A.7.6.20.1.2-2: Cell specific test parameters for SSB based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

Table A.7.6.20.1.2-3: NR OTA Cell specific test parameters for SSB based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

## A.7.6.20.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots in T2. The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 960 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20A. The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.20.2Intra-frequency SSB based L1-RSRP measurement in FR2 with event triggered reporting

## A.7.6.20.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event triggered on neighbor cell in FR2. This test will partly verify the event triggered reporting requirements in clause 9.15.3.4, with the testing configurations for NR cells in table A.7.6.20.1.1-1.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

The UE which passes this test case can skip the test case in A.7.6.20.1.

## A.7.6.20.2.2Test parameters

There are two cells in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in tables A.7.6.20.1.2-1, A.7.6.20.1.2-2 and A.7.6.20.1.2-3, except for the parameters specific for this test case, which are defined in table A.7.6.20.2.2-1.

There are two tests in the test case, test 1 and test 2:

-In test 1, time offset between cells is within CP length.

-In test 2, time offset between cells is larger than CP length.

If a UE does not support multiCellL1-measRTD-greaterThan-CP-r18, it is only required to pass test 1. Otherwise, it is only required to pass test 2.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs. A measurement object is configured for the frequency of the PCell in the measurement control information, and it is indicated to the UE that event-triggered reporting with event LTM3 is used. The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered L3 reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements

-UE is configured with event-triggered L1 reporting with event LTM3 for candidate cell (Cell2)

-The UE has performed L3 measurement on Cell 2.

At the beginning of T2, SSB_RP of Cell 2 change to different values from T1. T2 starts at the beginning of a frame with an odd SFN, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.7.6.20.2.2-1: General test parameters for SSB based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

## A.7.6.20.2.3Test Requirements

The UE shall send one Event LTM3 triggered measurement report less than 1920 ms from the beginning of time period T2.

UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20A. The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.20.3CSI-RS based L1-RSRP intra-frequency measurement for neighbour cell in FR2 without SSB based L1-RSRP measurement

## A.7.6.20.3.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting skippingSSBbasedL1mesurement-R19 makes correct reporting of an event triggered L1-RSRP measurement or periodic L1-RSRP measurement.

This test will partially verify the intra-frequency L1-RSRP measurement requirements in clause 9.14a.Supported test configurations are shown in table A.7.6.20.3.1-1.

Table A.7.6.20.3.1-1: supported test configurations

## A.7.6.20.3.2Test parameters

There are two intra-frequency cells in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2). The cell 1 and cell 2 are on the same frequency.

Measurement period is tested by using the parameters in table A.7.6.20.3.2-1 (General test parameters) and Cell specific test parameters provided in the table A.7.6.20.1.2-2 (Cell specific test parameters for SSB based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2). NR OTA Cell specific test parameters are provided in the table A.7.6.20.3.2-2.

In the test, the time offset between cells shall be within CP length.

In CSI measurement configuration, the UE is configured to perform L1-RSRP measurement on the CSI-RS but the UE shall not be configured to perform L1-RSRP measurements for the SSB specified in the section 9.14.

There are two sub-test cases in this test, Test 1 and Test 2. No gap patterns are configured in the test cases.

-Test 1: Periodic L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is not configured

-Test 2: Event triggered L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is not configured

If a UE supports both periodic reporting (tested using Test 1) and event triggered reporting (tested using Test 2), UE needs to pass only event triggered reporting test (Test 2). Else, UE needs to pass the respective test as its capability reported.

Both the Test 1 and Test 2 consist of two successive time periods with durations T1 and T2, during which the SSBRP of Cell 2 differs between the two periods. At the beginning of T2, SSB_RP of Cell 2 change to different values from T1. T2 starts at the beginning of a frame with an odd SFN.

In Test 1, the UE shall report measurement results periodically. Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has performed SSB based L3 measurement on Cell 2 and transmitted a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-LTM-NZP-CSI-RS-ResourceSet-r19 is provided to the UE to configure periodic L1-RSRP on CSI-RS and the UE is configured with PUCCH format 2 to transmit CSI-RS-based periodic L1-RSRP measurement reports on candidate cell (Cell 2). UE is not configured with SSB based L1-RSRP on the Cell 2.

In Test 2, the UE shall report measurement results only when the event condition is met. Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has performed SSB based L3 measurement on Cell 2 and transmitted a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-LTM-NZP-CSI-RS-ResourceSet-r19 is provided to the UE to configure event triggered L1-RSRP on the CSI-RS. UE is configured with event triggered L1-RSRP measurement reports on candidate cell (Cell 2) using the MAC CE. UE is not configured with SSB based L1-RSRP on the Cell 2.

In Test 2, after the start time of T2, the UE has no available UL data and receives no UL scheduling. Scheduling request resources are configured, and the periodicity of SR resources is 10ms.

Table A.7.6.20.3.2-1: General test parameters for CSI-RS based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

Table A.7.6.20.3.2-2: NR OTA Cell specific test parameters for CSI-RS based intra-frequency L1-RSRP LTM measurement without activated TCI state test in FR2

## A.7.6.20.3.3Test Requirements

In Test 1:

-The UE shall send first CSI-RS L1-RSRP report within 160ms + 320 slots from the beginning of T1.

-From the start of T2, the UE shall report higher RSRP values for cell 2 at least after 160ms + 320 slots from the start of T2.

-The UE shall send CSI-RS L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

In Test 2:

-The UE shall send the first UL transmission to the PCell within 170 ms (160ms + 10ms uncertainty to acquire the SR) from the start of T2 and send CSI-RS L1-RSRP report to the TE based on the grant provided by the TE as a response to the first UL transmission. From the start of T2, and till the first UL transmission is sent, it is assumed that there is no UL data is available at the UE.

-The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 170ms plus the uncertainty acquire the UL grant as a response to first UL transmission (i.e. SR), from the beginning of time period T2.

-The UE shall send CSI-RS L1-RSRP report including results of Cell 2 while meeting the L1-RSRP absolute accuracy requirement in clause 10.1.19D.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.6.20.4Intra-frequency CSI-RS based L1-RSRP measurement in FR2

## A.7.6.20.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of CSI-RS based intra-frequency L1-RSRP measurement on neighbor cell in FR2. This test will partly verify the CSI-RS based L1-RSRP measurement requirements in clause 9.14a, with the testing configurations for NR cells in table A.7.6.20.4.1-1.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

Table A.7.6.20.4.1-1: Applicable NR configurations for CSI-RS based Intra-frequency L1-RSRP LTM measurement test in FR2

A.7.6.20.4.2Test parameters

There are two cells in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

Measurement period and measurement accuracy is tested by using the parameters in table A.7.6.20.4.2-1 and table A.7.6.20.4.2-2. The time offset between cells is within CP length.

There are two tests in the test case, test 1 and test 2:

Test 1: Periodic L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is configured

Test 2: Event triggered L1-RSRP reporting of CSI-RS, when the SSB based L1-RSRP is configured

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on CSI-RS. Test 1 and Test 2 consist of two successive time periods, with time duration of T1 and T2 respectively. No gap patterns are configured in the two test cases.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements.

-The UE has performed L3 measurement on Cell 2.

-UE is configured with CSI-based L1-RSRP measurements, and qcl-InfoPeriodicCSI-RS is configured for all the resources in the resource set and for each resource one RS has QCL-TypeD with SSB for L1-RSRP measurement.

-In test 1, the field ltm-ReportConfigType is configured as periodic-r18,  and UE periodically report CSI-RS L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-In test 2, the field ltm-ReportConfigType is configured as eventTriggered,  and UE supporting LTM event triggered reporting shall report CSI-RS L1-RSRP measurement reports on candidate cell (Cell 2) by event-triggered measurement report by MAC CE.At the beginning of T2, SSB_RP and CSI_RP of Cell 2 change to different values from T1. T2 starts at the beginning of a frame with an odd SFN, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.7.6.20.4.2-1: General test parameters for CSI-RS based intra-frequency L1-RSRP LTM measurement test in FR2

Table A.7.6.20.4.2-2: Cell specific test parameters for CSI-RS based intra-frequency L1-RSRP LTM measurement test in FR2

Table A.7.6.20.4.2-3: NR OTA Cell specific test parameters for CSI-RS based intra-frequency L1-RSRP LTM measurement test in FR2

## A.7.6.20.4.3Test Requirements

In test 1, UE not supporting LTM event triggered reporting shall send L1-RSRP report every 20 slots in T2. The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 20 slots from the beginning of time period T2, UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20A. The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

In test2, UE supporting LTM event triggered reporting shall sent Event LTM3 triggered CSI-RS based L1 RSRP measurement report, with a measurement reporting delay less than 22ms from the beginning of time period T2. The reported CSI-RS L1-RSRP shall meet the accuracy requirements defined in clause 10.1.20A. The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.21LTM Inter-frequency L1-RSRP measurement with measurement gap

## A.7.6.21.1Inter-frequency SSB-based L1-RSRP measurement with measurement gap for LTM in FR2

## A.7.6.21.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of inter-frequency L1-RSRP measurement with MG for LTM. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.5, with the testing configurations in tables A.7.6.21.1.1-1, A.7.6.21.1.2-1, A.7.6.21.1.2-2 and A.7.6.21.1.2-3.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

Table A.7.6.21.1.1-1: Applicable NR configurations for SSB based inter-frequency L1-RSRP measurement with measurement gap for LTM

## A.7.6.21.1.2Test parameters

There are two cells in the test, Cell 1 is the PCell on NR RF channel number 1 and Cell 2 is a neighbor cell NR RF channel number 2. The test parameters for Cell 1 and Cell 2 are given in table A.7.6.21.1.2-2 and table A.7.6.21.1.2-3.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. Measurement gap is configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1.

Table A.7.6.21.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with measurement gap test in FR2

Table A.7.6.21.1.2-1: Cell specific test parameters for SSB based inter-frequency L1-RSRP LTM measurement with measurement gap test in FR2

Table A.7.6.21.1.2-3: SSB specific test parameters for neighbor cell

## A.7.6.21.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots in T2. The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 1280 ms plus 320 slots from the beginning of time period T2. UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20B.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.21.2Inter-frequency SSB-based L1-RSRP measurement with measurement gap in FR2 with event triggered reporting

A.7.6.21.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event with MG for LTM. This test will partly verify the L1-RSRP event triggered reporting requirements in clause 9.15.3.4, with the testing configurations in tables A.7.6.21.1.1-1.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

The UE which passes this test case can skip the test case in A.7.6.21.1.

A.7.6.21.2.2Test parameters

There are two cells in the test, Cell 1 is the PCell on NR RF channel number 1 and Cell 2 is a neighbor cell on NR RF channel number 2. The test parameters for Cell 1 and Cell 2 are given in tables A.7.6.21.1.2-1, A.7.6.21.1.2-2 and A.7.6.21.1.2-3, except for the parameters specific for this test case, which are defined in table A.7.6.21.2.2-1.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. Measurement gap is configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and event-triggered reporting with event LTM3.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.7.6.21.2.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with measurement gap test in FR2

## A.7.6.21.2.3Test Requirements

The UE shall send one Event LTM3 triggered measurement report, with a measurement reporting delay less than 2560 ms from the beginning of time period T2.

UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20B.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.22LTM Inter-frequency L1-RSRP measurement without measurement gap

## A.7.6.22.1Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR2

## A.7.6.22.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting interFreqSSB-L1-MeasWithoutGaps-r18 makes correct reporting of inter-frequency L1-RSRP measurement without gap for LTM. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.6, with the testing configurations in tables A.7.6.22.1.1-1, A.7.6.22.1.2-1, A.7.6.22.1.2-2, A.7.6.22.1.2-3 and A.7.6.22.1.2-4.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

Table A.7.6.22.1.1-1: Applicable NR configurations for SSB based inter-frequency L1-RSRP LTM measurement without gap in FR2

## A.7.6.22.1.2Test parameters

There are two cells in the test, Cell 1 is the PCell on NR RF channel number 1 and Cell 2 is a neighbor cell NR RF channel number 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters for Cell 1 are given in table A.7.6.22.1.2-1. The test parameters for Cell 2 are given in table A.7.6.22.1.2-2 and table A.7.6.22.1.2-3.

There are two tests in the test case, test 1 and test 2:

-In test 1, time offset between cells is within CP length.

-In test 2, time offset between cells is larger than CP length.

UE not capable of multiCellL1-measRTD-greaterThan-CP-r18 is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. No measurement gap is configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an odd SFN.

Table A.7.6.22.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement test in FR2

Table A.7.6.22.1.2-2: Cell specific test parameters for SSB based inter-frequency L1-RSRP LTM measurement test in FR2

Table A.7.6.22.1.2-3: NR OTA Cell specific test parameters for SSB based inter-frequency L1-RSRP LTM measurement without measurement gap in FR2

## A.7.6.22.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots in T2. No later than 960 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20B.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.23Idle Mode CA/DC Measurements

## A.7.6.23.1Test case for Idle mode fast CA/DC eEMR measurement for FR2 without valid reporting

## A.7.6.23.1.1Test Purpose and Environment

The purpose of this test is to verify UE measurement reporting behaviour as specified in clause 4.7 when the UE supports measValidationReportEMR-r18. This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7 when measIdleValidityDuration is configured for the test case when there are no measurement results to report at RRC connection setup.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 1 and NR cell 2 as inter-frequency neighbour cell in FR2 on NR RF channel 2. The test parameters are given in tables A.7.6.23.1.1-1, A.7.6.23.1.1-2, A.7.6.23.1.1-3 and A.7.6.23.1.1-4.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

Before T1, the UE is connected to cell 1 and configured with inter-frequency measurement on cell 2 with periodic reporting. The time when a valid measurement report is received at TE defines the starting point of T1.

During T1, the UE is configured with early measurement reporting for cell 2 in measIdleCarrierListNR-r16. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode. The time when T331 timer expires defines the ending point of T2.

At the beginning of T2, cell 2 becomes detectable however cell reselection shall not be performed. Signal level of cell 2 is set to the value given in table A.7.6.23.1.1-3. The time when T331 timer expires defines the ending point of T2.At the beginning of T3, the signal level of the neighbour cell is set to turned off. The duration of the T3 equals to measIdleValidityDuration.

The time when TE sends the paging message is defined as the starting point of T4. During T4, in this test the UE shall not send measurement report.

Table A.7.6.23.1.1-1: supported test configuration

Table A.7.6.23.1.1-2: General test parameters for Idle mode fast CA/DC eEMR measurement for FR2

Table A.7.6.23.1.1-3: Cell specific test parameters in Idle and Connected mode for Idle mode fast CA/DC eEMR measurement for FR2

Table A.7.6.23.1.1-4: OTA related test parameters for Test case Idle mode fast CA/DC eEMR measurement for FR2

## A.7.6.23.1.2Test Requirements

During the period T2 and T3, the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for cell 2.

The UE shall NOT send early measurement report to the PCell in this test.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.23.2Test case for Idle mode fast CA/DC cell reselection measurement for FR2 without valid reporting

## A.7.6.23.2.1Test Purpose and Environment

The purpose of this test is to verify UE measurement reporting behaviour as specified in clause 4.7 when the UE supports measValidationReportReselectionMeasurements-r18 This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7 when measReselectionValidityDuration-r18 is configured for the test case when there are no measurement results to report at RRC connection setup.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 1 and NR cell 2 as inter-frequency neighbour cell in FR2 on NR RF channel 2. The test parameters are given in tables A.7.6.23.2-1, A.7.6.23.2-2, A.7.6.23.2-3 and A.7.6.23.2-4.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

Before T1, the UE is connected to cell 1 and configured with inter-frequency measurement on cell 2 with periodic reporting. The time when a valid measurement report is received at TE defines the starting point of T1.

During T1, the UE is configured with early measurement reporting for cell 2 in MeasReselectionCarrierListNR-r18. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode.

At the beginning of T2, cell 2 becomes detectable however no cell reselection is being performed. Signal level of cell 2 is set to the level according to Table A.7.6.23.2-3. The duration of T2 is set to fixed value according to the Table A.7.6.23.2-2.

At the beginning of T3, the signal level of the neighbour cell is set to turned off. The duration of the T3 equals to measReselectionValidityDuration-r18.

The time when TE sends the paging message defined as the starting point of T4.

During T4, UE shall not send measurement report.

Table A.7.6.23.2-1: supported test configuration

Table A.7.6.23.2-2: General test parameters for Idle mode fast CA/DC cell reselection measurement for FR2

Table A.7.6.23.2-3: Cell specific test parameters in Idle and Connected mode for Idle mode fast CA/DC cell-reselection measurement for FR2

Table A.7.6.23.2-4: OTA related test parameters for Test case Idle mode fast CA/DC cell-reselection measurement for FR2

## A.7.6.23.2.2Test Requirements

During the period T2 and T3, the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for cell 2.

The UE shall NOT send early measurement report to the PCell in this test.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.23.3 Test case for Idle mode fast CA/DC cell reselection measurement for FR2 with valid reporting

## A.7.6.23.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the required measurements on the serving cell and the configured inter-frequency carrier for idle mode measurement reporting after the UE has entered Idle mode when the UE supports measValidationReportReselectionMeasurements-r18. This test will partly verify the fast CA/DC measurement reporting requirements in clause 4.7  when measReselectionValidityDuration-r18 is configured for the test case when there are measurement results to report at RRC connection setup.

In this test, there are two cells: NR cell 1 as PCell in FR1 on NR RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters are given in tables A.7.6.23.3.1-1, A.7.6.23.3.1-2, A.7.6.23.3.1-3 and A.7.6.23.3.1-4.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During T1, the UE is connected to cell 1 only and shall not have any timing information of cell 2. UE is configured with early measurement reporting for cell 2 in MeasReselectionCarrierListNR-r18. Beam level reporting for early measurements is not configured. The time point when UE receives RRC_Release message from the TE defines as the starting point of T2.

During T2, cell 2 becomes detectable however no cell reselection is being performed. Signal level of cell 2 is set to fixed value according to Table A.7.6.23.3-2. The duration of T2 is set to fixed value according to the Table A.7.6.23.3-2.

The duration of the T3 equals to the configured value measReselectionValidityDuration-r18. During T3, the signal level of cell 2 is set to another value according to the Table A.7.6.23.3-2.

The time when TE sends the paging message defines the starting point of T4.

During T4, UE shall send measurement report within the duration of T4.

Table A.7.6.23.3-1: supported test configuration

Table A.7.6.23.3-2: General test parameters for Idle mode fast CA/DC cell reselection measurement for FR2

Table A.7.6.23.3-3: Cell specific test parameters in Idle and Connected mode for Idle mode fast CA/DC cell-reselection measurement for FR2

Table A.7.6.23.3-4: OTA related test parameters for Test case Idle mode fast CA/DC cell-reselection measurement for FR2

## A.7.6.23.3.2Test Requirements

During the period T2 and T3, the UE shall not perform reselection.

At the start of T4 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report for cell 2.

The UE shall send early measurement report to the PCell with valid measurement results.

After receiving the requested early measurement report, the test equipment verifies the accuracy of measurement reported for Cell 2 meets the requirements in clause 10.1.4B for SS-RSRP and in clause 10.1.8B for SS-RSRQ and test ends. In the test case, the reported measurements are considered valid if they fulfil measurement accuracy requirements according to Cell 2 signal level during T3.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.24RSCPD measurements

## A.7.6.24.1NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state

## A.7.6.24.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD measurement reported together with the RSTD measurement meets the requirements specified in clause 9.9.7 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.7.6.24.1.1-1.

Table A.7.6.24.1.1-1: Supported test configurations for NR DL RSCPD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layer.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. In NR-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

The general test parameters are listed in table A.7.6.24.1.1-2. Cell specific parameters during T1 are listed in table A.7.6.24.1.1-3. Cell specific parameters during T2 are listed in table A.7.6.24.1.1-4.

Table A.7.6.24.1.1-2: General test parameters for RSCPD with RSTD measurement reporting delay

Table A.7.6.24.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.6.24.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.6.24.1.2Test Requirements

The RSCPD reported together with RSTD measurement time fulfils the requirements specified in the clause 9.9.7.

The UE shall perform and report the RSCPD and RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.7 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The reported DL RSCPD measurement shall be within the DL RSCPD reporting range specified in the clause 10.1.43.3 and the reported RSTD measurement shall be within the RSTD reporting range specified in the clause 10.1.23.

## A.7.6.25RSCP measurements

## A.7.6.25.1DL RSCP with UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA

## A.7.6.25.1.1Test purpose and environment

The purpose of the test is to verify that the DL RSCP and UE Rx-Tx time difference measurements meet the requirements specified in clause 9.9.8.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured for both DL RSCP measurement and UE Rx-Tx time difference measurement.

The supported test configurations are listed in table A.7.6.25.1.1-1.

Table A.7.6.25.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-Multi-RTT-ProvideAssistanceData message and NR-Multi-RTT-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE during T1. In NR-Multi-RTT-RequestLocationInformation, the UE is configured to perform DL RSCP measurement via nr-DL-PRS-RSCP-Request. The UE is configured to perform both DL RSCP and UE Rx-Tx time difference measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources to be measured within the configured time window.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are listed in table A.7.6.25.1.1-2 and table A.7.6.25.1.1-3.

Table A.7.6.25.1.1-2: General test parameters

Table A.7.6.25.1.1-3: Cell specific test parameters

## A.7.6.25.1.2Test requirements

The DL RSCP with UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9.8 with Nsample=4 for UE Rx-Tx time difference.

The UE shall perform and report the DL RSCP and UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified DL RSCP with UE Rx-Tx time difference measurement time specified in clause 9.9.8 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%. The reported DL RSCP measurement shall be within the DL RSCP reporting range specified in clause 10.1.44 and the reported UE Rx-Tx measurement shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.

## A.7.6.26Inter-RAT Measurements

## A.7.6.26.1SA event triggered reporting test without gap under non-DRX for UE configured with [MeasuringoneCCperFR2band] in FR2 inter-band CA

## A.7.6.26.1.1Test purpose and Environment

The purpose of this test is to verify that if the UE indicates ‘nogap-noncsg’ via NeedForGapNCSG-InfoEUTRA for the inter-RAT measurement, the UE is configured by the network with [MeasuringoneCCperFR2band], the UE makes correct reporting of an event. This test will partly verify the SA inter-RAT cell search requirements in clause 9.4.8.3 and 9.4.8.4 based on the enhanced CSSFoutside,gap in clause 9.1.5.1 by measuring one serving carrier per FR2 band. Supported test configurations are shown in table A.7.6.26.1.1-1.

Table A.7.6.26.1.1-1: SA event triggered reporting tests without SSB index reading for FR2

In this test, there are three cells: NR cell 1 as PCell in FR2 on RF channel 1, NR cell 2 as SCell in FR2 on RF channel 2, which is within the same band with RF channel 1, and E-UTRA cell 3 as neighbour cell in FR1 on RF channel 3. The SSB of cell 3 is completely within UE’s active BWP BW. The PRBs containing SSB from cell 1 and cell 3 should be different in frequency location within the cell bandwidth. The test parameters for the cell 1 and cell 2 are given in table A.7.6.26.1.1-2, A.7.6.26.1.1-3 and A.7.6.26.1.1-4 below. The test parameters for cell 3 are given in tables A.7.6.26.1.1-5, A.7.6.26.1.1-6 and A.7.6.26.1.1-7.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

In the measurement control information, measurement objects are configured for the frequency of the PCell and SCells respectively, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. At the beginning of T1 the UE receives an RRC message by which the SCells (Cell 2 and Cell 3) becomes configured on NR. UE is also indicated to perform enhanced measurement by measuring one serving CC per band. During time duration T1, the UE shall have no timing information of Cell 2 and Cell 3.

Table A.7.6.26.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.26.1.1-3: Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

Table A.7.6.26.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX

## A.7.6.26.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.7.6.27L1 CLI measurements

## A.7.6.27.1L1-SRS-RSRP measurement with DRX with SBFD

## A.7.6.27.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SRS-RSRP measurement when configured with SBFD in DU operation. This test will verify the L1-SRS-RSRP measurement requirements in clause 9.18.2 with the testing configurations for NR cells in table A.7.6.27.1.1-1.

Table A.7.6.27.1.1-1: Applicable NR configurations for FR1 L1-SRS-RSRP test

## A.7.6.27.1.2Test Parameters

One cell is deployed in the test, which is FR2 PCell (Cell 1). The test parameters for PCell is given in table A.7.6.27.1.2-1 and A.7.6.27.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SRS-RSRP measurement on SRS-RSRP-MeasurementResourceSet configured in a CSI-ResourceConfig and report aperiodically. The higher layer parameter timeRestrictionForChannelMeasurements is configured to UE in the test.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. During the test, the test system transmits SRS resource for measurement in the SBFD slot according to the SRS configuration in table A.7.6.27.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A.7.6.27.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

At 640ms after the beginning of time period T2, the DCI triggering L1-SRS-RSRP reporting is sent to UE and UE provides the report back based on the reporting configuration.

Table A.7.6.27.1.2-1: General test parameters for L1-SRS-RSRP reporting for PCell in FR2

Table A.7.6.27.1.2-2: NR Cell specific test parameters for L1-SRS-RSRP reporting for PCell in FR2

Table A.7.6.27.1.2-3: FR1 test parameters for aggressor UE

Table A.7.6.27.1.2-4: SRS configuration parameters

## A.7.6.27.1.3Test Requirements

Within 7 ms from the beginning of time period T2, the UE shall send L1-SRS-RSRP report.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.6.27.2L1-CLI-RSSI measurement with DRX with SBFD

## A.7.6.27.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-CLI-RSSI measurement with UE configured with two DL subbands in SBFD DUD operation. The RSSI resource CLI-RSSI-MeasResource is configured across two DL subbands. This test will verify the CLI-RSSI measurement requirements in clause 9.18.3 with the testing configurations for NR cells in table A.7.6.27.2.1-1.

Table A.7.6.27.2.1-1: Applicable NR configurations for FR2 L1-CLI-RSSI test

## A.7.6.27.2.2Test Parameters

One cell is deployed in the test, which are FR2 PCell (Cell 1). The test parameters for PCell is given in table A.7.6.27.2.2-1 and A.7.6.27.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-CLI-RSSI measurement on CLI-RSSI-MeasResource and report aperiodically. The test consists of two successive time periods, with time duration of T1 and T2, respectively. The higher layer parameter timeRestrictionForChannelMeasurements is configured to UE in the test. At 5ms after the beginning of time period T2, the DCI triggering L1-CLI-RSSI reporting is sent to UE and UE provides the report back based on the reporting configuration.

There is no measurement gap configured in the test. The L1-CLI-RSSI measurement resource CLI-RSSI-MeasResource configuration is in table A.7.6.27.2.2-3.

Table A.7.6.27.2.2-1: General test parameters for L1-CLI-RSSI reporting for PCell in FR1

Table A.7.6.27.2.2-2: NR Cell specific test parameters for L1-CLI-RSSI reporting for PCell in FR2

Table A.7.6.27.2.2-3: NR OTA Cell specific test parameters for CLI-RSSI event triggered reporting for PCell in FR2

Table A.7.6.27.2.2-4: CLI-RSSI-MeasResource measurement resource configuration for measurement reporting

## A.7.6.27.2.3Test Requirements

Within 7ms from the beginning of time period T2, the UE shall send L1-CLI-RSSI report. The nominal RSSI used to evaluate the requirement shall be based on Io. The UE shall send HARQ ACK/NACK for the corresponding PDSCH scheduled in PCell in all the slots.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.6.28LTM Inter-frequency L1-RSRP event triggered reporting without measurement gap

## A.7.6.28.1Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR2

## A.7.6.28.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting interFreqSSB-L1-MeasWithoutGaps-r18 reports inter-frequency L1-RSRP measurement without gap correctly for LTM, when event triggered L1-RSRP reporting is configured. This test will partly verify the L1-RSRP event triggered reporting requirements in clause 9.15.3.4.

The UE which passes this test case can skip the test case in A.7.6.22.

The testing configurations and parameters are as given in tables A.7.6.22.1.1-1, A.7.6.22.1.2-1, A.7.6.22.1.2-2, A.7.6.22.1.2-3 and A.7.6.22.1.2-4, except for the parameters specific for this test case, which are defined in table A.7.6.28.1.2-1. The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

## A.7.6.28.1.2Test parameters

There are two cells in the test, Cell 1 is the PCell on NR RF channel number 1 and Cell 2 is a neighbor cell NR RF channel number 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters for Cell 1 are given in table A.7.6.22.1.2-1. The test parameters for Cell 2 are given in table A.7.6.22.1.2-2 and table A.7.6.22.1.2-3.

There are two tests in the test case, test 1 and test 2:

-In test 1, time offset between cells is within CP length.

-In test 2, time offset between cells is larger than CP length.

UE not capable of multiCellL1-measRTD-greaterThan-CP-r18 is only required to pass test 1. Otherwise, it is only required to pass test 2.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. No measurement gap is configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and event-triggered L1-RSRP measurement reports on candidate cell (Cell 2) in PUSCH

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1. T2 starts at the beginning of a frame with an odd SFN, and the UE has no available UL data and receives no UL scheduling. SR resources are configured, and the uncertainty time of transmitting SR is 10ms.

Table A.7.6.28.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement test in FR2

## A.7.6.28.1.3Test Requirements

The UE shall send event-triggered L1 report based on Event LTM3 less than 160 ms from the beginning of time period T2.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.29LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation

## A.7.6.29.1Inter-frequency SSB-based L1-RSRP measurement with measurement gap cancellation for LTM in FR2

## A.7.6.29.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of inter-frequency L1-RSRP measurement with MG cancellation for LTM. This test will partly verify the L1-RSRP measurement requirements in clause 9.15.5, with the testing configurations in tables A.7.6.21.1.1-1, A.7.6.21.1.2-1, A.7.6.21.1.2-2 and A.7.6.21.1.2-3.

The AoA setup of FR2 cell for this test is Setup 1 as defined in clause A.3.15.

NOTE:The parameters and configurations of this test follow the tables defined in A.7.6.21.2 as a baseline except for parameters explicitly indicated in Table A.7.6.29.1.2-1.

## A.7.6.29.1.2Test parameters

There are two cells in the test, Cell 1 is the PCell on NR RF channel number 1 and Cell 2 is a neighbour cell NR RF channel number 2. The test parameters for Cell 1 and Cell 2 are given in table A.7.6.21.1.2-1, table A.7.6.21.1.2-2, table A.7.6.21.1.2-3, and table A.7.6.29.1.2-1.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. SSB_RP of Cell 2 in T1 and T2 are different. Measurement gap is configured in the test.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on RF channel 1 (PCC).

-A measurement object is configured for the RF channel 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. Before the start of the T1, event is triggered, and UE has sent a measurement report for the Cell 2 with SSB Index.

-UE is provided with LTM-Candidate-r18 for Cell 2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

At the beginning of T2, SSB_RP of Cell 2 changes to a different value from T1.

The time duration T2 is divided in 2 phases, T2-1 and T2-2. During time duration T2-1, the test equipment randomly selects Lcancel gap occasions to be cancelled via DCI indication where T2-1 and Lcancel are given in Table A.7.6.29.1.2-1. If a measurement gap occasion is determined to be cancelled, the TE sends the DCI indication latest X ms before the start of the measurement gap occasion using DCI format 1-1, where X is 3ms or 5ms as given by the UE capability minimumTimeOffset-r19. During T2-2 there is no cancelled gap occasions. Table A.7.6.29.1.2-1: General test parameters for SSB based inter-frequency L1-RSRP LTM measurement with measurement gap test in FR2 with gap cancellation

The UE is scheduled with DL data on PCell on all the slots overlapping with the cancelled measurement gap occasions.

## A.7.6.29.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots in T2. The UE shall start to report a larger L1-RSRP value of Cell 2 in no later than 2080 ms plus 320 slots from the beginning of time period T2. UE shall send L1-RSRP report including the valid results for Cell 2 while meeting the accuracy requirements defined in clause 10.1.20B.

During T2, the UE shall send valid ACK/NACK for all the scheduled transmissions within cancelled measurement gap occasions.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.6.30DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR2 SA

## A.7.6.30.1Test Purpose and Environment

The purpose of the test is to verify that the DL AI/ML positioning reporting delay meets the requirement specified in clause 9.9E.5 in an environment with TDL-C propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.7.6.30.1-1.

Table A.7.6.30.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layer.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells start transmitting PRS from the beginning of time period T2.

NOTE:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-AIML-ProvideAssistanceData and NR-DL-AIML-RequestLocationInformation as defined in TS 37.355 [34, clause 6.5.13.5], shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE DT before the start of T2, where DT = 50 ms is the maximum processing time of the DL assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.7.6.30.1-2, and cell specific test parameters are listed in table A.7.6.30.1-3.

Table A.7.6.30.1-2: General test parameters for DL AI/ML positioning reporting delay

Table A.7.6.30.1-3: Cell-specific test parameters for DL AI/ML positioning reporting delay during T1

Table A. 7.6.30.1-4: Cell-specific test parameters for DL AI/ML positioning reporting delay during T2

## A.7.6.30.2Test Requirements

The DL AI/ML positioning reporting delay fulfils the requirements specified in clause 9.9E.1 and 9.9E.5.

The UE shall perform and report its inferred position within the time duration specified in section 9.9E.1 and 9.9E.5 starting from the beginning of time interval T2 provided that the PRS resources are transmitted during that time period.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The UE reports its infered location in NR-DL-AIML-LocationInformation as specified in TS 37.355 [34].

## A.7.7Measurement Performance requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause 10 for at least 90 % of the reported cases.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.7.7.1SS-RSRP

## A.7.7.1.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3.1.1 and 10.1.3.1.2 for intra-frequency measurements.

## A.7.7.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.7.7.1.1.2-2 and A.7.7.1.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. The test consists of two time phases T1 and T2.

Table A.7.7.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.7.7.1.1.2-2: SS-RSRP  Intra frequency general test parameters

Table A.7.7.1.1.2-3: SS-RSRP Intra frequency OTA related test parameters

## A.7.7.1.1.3Test Requirements

The SS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.1.1 and relative accuracy requirements in clause 10.1.3.1.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

During T2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

During T1 and T2:

Relative accuracy of Cell 1 during T2 compared with Cell 1 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

Table A.7.7.1.1.3-1: SS-RSRP absolute accuracy test requirement

## A.7.7.1.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.1.1 and 10.1.5.1.2 for intrer-frequency measurements with the testing configurations for NR cells in table A.7.7.1.2.1-1.

Table A.7.7.1.2.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

## A.7.7.1.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 1 and Cell 2 are given in table A.7.7.1.2.2-1 and table A.7.7.1.2.2-2 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.7.7.1.2.2-1 and table A.7.7.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.7.7.1.2.2-1: SS-RSRP inter-frequency test parameters

Table A.7.7.1.2.2-2: SS-RSRP inter frequency OTA related test parameters

## A.7.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirements in clause 10.1.5.1.1 and the relative requirements in clause 10.1.5.1.2.

Test 1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in A.7.7.1.2.3-2.

Test 2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in A.7.7.1.2.3-2.

Table A.7.7.1.2.3-1: SS-RSRP absolute accuracy test requirement

Table A.7.7.1.2.3-2: SS-RSRP relative accuracy test requirement

## A.7.7.1.3SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell

## A.7.7.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.1.1 for inter-frequency measurements with the testing configurations in table A.7.7.1.3.1-1.

Table A.7.7.1.3.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

## A.7.7.1.3.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) in FR1 and Cell 2 in FR2 . The test parameters for the Cell 1 and Cell 2 are given in table A.7.7.1.3.2-1 and table A.7.7.1.3.2-2 below. Absolute accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.7.7.1.3.2-1 and table A.7.7.1.3.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.7.7.1.3.2-1: SS-RSRP inter-frequency test parameters

Table A.7.7.1.3.2-2: SS-RSRP inter-frequency OTA related test parameters

## A.7.7.1.3.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 shall fulfil the Absolute requirement in clause 10.1.5.1.1.

Test 1:

Absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.3.3.

Test 2:

Absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.7.7.1.3.3.

Table A.7.7.1.3.3: SS-RSRP absolute accuracy test requirement

## A.7.7.2SS-RSRQ

## A.7.7.2.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.8.1.1.

## A.7.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.2.1.2-1. . The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.7.7.2.1.2-2 and table A.7.7.2.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.7.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.7.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

Table A.7.7.2.1.2-3: SS-RSRQ Intra frequency OTA related test parameters

## A.7.7.2.1.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ-2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal RSRQ+3.5 dB to Nominal RSRQ-3.5 dB  according to the requirements in clause 10.1.8.1.1.Nominal RSRQ is the value shown in table A.7.7.2.1.2-3.

## A.7.7.2.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.7.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2 for inter-frequency measurement.

## A.7.7.2.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.7.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.7.7.2.2.2-2 and table A.7.7.2.2.2-3.. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A. 7.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.7.7.2.2.2-2: SS-RSRQ Inter frequency general test parameters

Table A.7.7.2.2.2-3: SS-RSRQ Inter frequency OTA related test parameters

## A.7.7.2.2.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ -2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal SS-RSRQ +3.5 dB to Nominal SS-RSRQ -3.5 dB  according to the requirements in clause 10.1.10.1.1.

The SS-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1.10.1.2.

## A.7.7.3SS-SINR

## A.7.7.3.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.13.1.1.

## A.7.7.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.3.1.2-1. . The absolute accuracy of SS-SINR intra-frequency measurement is test by using the parameters in table A.7.7.3.1.2-2 and table A.7.7.3.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table  A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.7.7.3.1.2-2: SS-SINR Intra frequency test parameters

Table A.7.7.3.1.2-3: SS-SINR Intra frequency OTA related test parameters

## A.7.7.3.1.3Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR+3B to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR +3.5 dB to Nominal SS-SINR -3.5 dB  according to the requirements in clause 10.1.10.13.1.

## A.7.7.3.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.7.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.15.1.1 and 10.1.15.1.2 for inter-frequency measurement.

## A.7.7.3.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.7.7.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.7.7.3.2.2-2 and table A.7.7.3.2.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell. The TCI status for Cell 1 is defined in table  A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.7.7.3.2.2-2: SS-SINR Inter frequency general test parameters

Table A.7.7.3.2.2-3: SS-SINR Inter frequency OTA related test parameters

## A.7.7.3.2.3Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR +3 dB to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR +3.5 dB to Nominal SS-SINR -3.5 dB  according to the requirements in clause 10.1.15.1.1.

The SS-SINR relative measurement accuracy shall fulfil the requirements in clause 10.1.15.1.2.

## A.7.7.4L1-RSRP measurement for beam reporting

## A.7.7.4.1SSB based L1-RSRP measurement

## A.7.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.2 and clause 10.1.20.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.7.7.4.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.4.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.7.4.1.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.4.1.2-1 and table A.7.7.4.1.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.7.7.4.1.2-1 and table A.7.7.4.1.2-2.

Here is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.7.7.4.1.2-1: FR2 SSB based L1-RSRP general test parameters

Table A.7.7.4.1.2-2: FR2 SSB based L1-RSRP OTA related test parameters

## A.7.7.4.1.3Test Requirements

After 320 ms from the beginning of the test, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirements in clauses 10.1.20.1. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

For Test 2:

Absolute accuracy of SSB resource reported by UE in L1-RSRP report (SSB0 or SSB1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

Table A.7.7.4.1.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.7.7.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause 10.1.20.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.4.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.7.7.4.2.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.4.2.2-1 and table A.7.7.4.2.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.7.7.4.2.2-1 and table A.7.7.4.2.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.7.7.4.2.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.7.7.4.2.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.7.7.4.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.20.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

For Test 2:

Absolute accuracy of CSI-RS resource reported by UE in L1-RSRP report (CSI-RS0 or CSI-RS1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.7.4.2.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.4.3CSI-RS based L1-RSRP measurement with SBFD DUD

## A.7.7.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits, when UE is configured with 2 DL subbands in SBFD and the CSI-RS BW is each DL subband is 36 RB. This test will verify the requirements in clauses 9.5.3 and clause 10.1.20.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.4.3.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.4.3.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.7.4.3.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.4.3.2-1 and table A.7.7.4.3.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.7.7.4.3.2-1 and table A.7.7.4.3.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.7.7.4.3.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.7.7.4.3.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.7.7.4.3.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.20.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.3.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

For Test 2:

Absolute accuracy of CSI-RS resource reported by UE in L1-RSRP report (CSI-RS0 or CSI-RS1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.3.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.7.4.3.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.4.4CSI-RS based L1-RSRP measurement with SBFD DU

## A.7.7.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits, when UE is configured with 1 DL subband in SBFD and the CSI-RS BW is the DL subband is 32 RB. This test will verify the requirements in clauses 9.5.3 and clause 10.1.20.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.4.4.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.4.4.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.7.4.4.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.4.4.2-1 and table A.7.7.4.4.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.7.7.4.4.2-1 and table A.7.7.4.4.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.7.7.4.4.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.7.7.4.4.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.7.7.4.4.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.20.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.4.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

For Test 2:

Absolute accuracy of CSI-RS resource reported by UE in L1-RSRP report (CSI-RS0 or CSI-RS1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.4.4.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.7.4.4.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.5CLI measurements

## A.7.7.5.1SA SRS-RSRP measurement accuracy with FR2 serving cell

## A.7.7.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the SRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.1.1 with the testing configurations for NR cells in table A.7.7.5.1.1-1.

Table A.7.7.5.1.1-1: Applicable NR configurations for FR2 SRS-RSRP accuracy test

## A.7.7.5.1.2Test parameters

In this set of test cases there is one cell in the test, FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.5.1.2-1 and A.7.7.5.1.2-2 below. The test parameter for the (virtual) neighbor cell UE transmitting SRS are given in table A.7.7.5.1.2-2.

Before the test UE is configured to perform SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in the DL slots according to the SRS configuration in table A.7.7.5.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 2 data symbols before SRS to be transmitted.

Table A.7.7.5.1.2-1: FR2 test parameters for SRS-RSRP accuracy

Table A.7.7.5.1.2-2: SRS-RSRP accuracy OTA related test parameters for PCell and Neighbour cell UE in FR2

Table A.7.7.5.1.2-3: SRS configuration parameters for FR2 SRS-RSRP accuracy

## A.7.7.5.1.3Test Requirements

The SRS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.22.1.1. The following requirements are to be verified:

During T1:

The UE is deemed to meet the requirement if the reported SRS-RSRP is in the range shown in table A.7.7.5.1.3-1.

During T2:

The UE is deemed to meet the requirement if the reported SRS-RSRP is in the range shown in table A.7.7.5.1.3-1.

Table A.7.7.5.1.3-1: SRS-RSRP absolute accuracy test requirement

## A.7.7.5.2SA CLI-RSSI measurement accuracy with FR2 serving cell

## A.7.7.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.2.1 with the testing configurations for NR cells in table A.7.7.5.2.1-1.

Table A.7.7.5.2.1-1: Applicable NR configurations for FR2 CLI-RSSI accuracy test

## A.7.7.5.2.2Test parameters

In this set of test cases there is one cell in the test, FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.5.2.2-1 and A.7.7.5.2.2-2 below.

Before the test UE is configured to perform CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI resource and on 2 data symbol before. The CLI-RSSI measurement resource configuration is in table A.7.7.5.2.2-3.

Table A.7.7.5.2.2-1: FR2 test parameters for CLI-RSSI accuracy

Table A.7.7.5.2.2-2: CLI-RSSI accuracy OTA related test parameters

Table A.7.7.5.2.2-3: CLI-RSSI measurement resource configuration for FR2 CLI-RSSI accuracy

## A.7.7.5.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.22.2.1. The following requirements are to be verified:

During T1:

The UE is deemed to meet the requirement if the reported CLI-RSSI is in the range shown in table A.7.7.5.2.3-1.

During T2:

The UE is deemed to meet the requirement if the reported CLI-RSSI is in the range shown in table A.7.7.5.2.3-1.

Table A.7.7.5.2.3-1: CLI-RSSI absolute accuracy test requirement

## A.7.7.6L1-SINR measurement for beam reporting

A.7.7.6.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

## A.7.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.1 and clause 10.1.28.1 for L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.6.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.6.1.1-1: Applicable NR configurations for FR2 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

## A.7.7.6.1.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.6.1.2-1 and table A.7.7.6.1.2-2 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.7.7.6.1.2-1 and table A.7.7.6.1.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.7.7.6.1.2-1: FR2 CSI-RS based L1-SINR general test parameters

Table A.7.7.6.1.2-2: FR2 CSI-RS based L1-SINR OTA related test parameters

## A.7.7.6.1.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clauses 10.1.28.1. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.7.7.6.1.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the reported differential L1-SINR is in the range shown in table A.7.7.6.1.3-1.

Table A.7.7.6.1.3-1: L1-SINR absolute accuracy test requirement

Table A.5.7.6.1.3-2: L1-SINR relative accuracy test requirement

## A.7.7.6.2L1-SINR measurement with SSB based CMR and dedicated IMR

## A.7.7.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.2 and clause 10.1.28.2 for L1-SINR measurements with SSB based CMR and CSI-IM based IMR, with the testing configurations for NR cells in table A.7.7.6.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.6.2.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with SSB based CMR and CSI-IM based IMR

## A.7.7.6.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.6.2.2-1 and table A.7.7.6.2.2-2 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.7.7.6.2.2-1 and table A.7.7.6.2.2-2.

Here is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-IM resource set with two CSI-IM resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-IM resources as IMR.

Table A.7.7.6.2.2-1: FR2 L1-SINR general test parameters with SSB based CMR and CSI-IM based IMR

Table A.7.7.6.2.2-2: FR2 L1-SINR SSB specific test parameters

## A.7.7.6.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for SSB#0+CSI-IM#0 and SSB#1+CSI-IM#1 of Cell 1 shall fulfil the requirements in clauses 10.1.28.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB#0+CSI-IM#0. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.7.7.6.2.3-1.

Relative accuracy of SSB#0+CSI-IM#0 compared with SSB#1+CSI-IM#1. The UE is deemed to meet the requirement if the reported differential L1-SINR is in the range shown in table A.7.7.6.2.3-2.

Table A.7.7.6.2.3-1: L1-SINR absolute accuracy test requirement

Table A.7.7.6.2.3-2: L1-SINR relative accuracy test requirement

## A.7.7.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR

## A.7.7.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8.4.3 and clause 10.1.28.3 for L1-SINR measurements based on CSI-RS as both CMR and IMR with the testing configurations for NR cell in table A.7.7.6.3.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.6.3.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with CSI-RS based both CMR based IMR

## A.7.7.6.3.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.6.3.2-1 and table A.7.7.6.3.2-2 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.7.7.6.3.2-1 and table A.7.7.6.3.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured two CSI-RS resource sets with two CSI-RS resources for each set. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as both CMR and IMR.

Table A.7.7.6.3.2-1: FR2 L1-SINR measurement test with CSI-RS based both CMR and IMR

Table A.7.7.6.3.2-2: FR2 CSI-RS based L1-SINR measurement OTA related test parameters

## A.7.7.6.3.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for CSI-RS#0 for CMR +CSI-RS#0 for IMR and CSI-RS#1 for CMR +CSI-RS#0 for IMR of Cell 1 shall fulfil the requirements in clause 10.1.28.3. The following requirements are to be verified:

Absolute accuracy of CSI-RS#0 for CMR + CSI-RS#0 for IMR. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.7.7.6.3.3-1.

Relative accuracy of CSI-RS#0 for CMR + CSI-RS#0 for IMR compared with CSI-RS#1 for CMR + CSI-RS#1 for IMR. The UE is deemed to meet the requirement if the reported differential L1-SINR is in the range shown in table A.7.7.6.3.3-2.

Table A.7.7.6.3.3-1: L1-SINR absolute accuracy test requirement

Table A.7.7.6.3.3-2: L1-SINR relative accuracy test requirement

## A.7.7.7CSI-RSRP

## A.7.7.7.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3.2.1 and 10.1.3.2.2 for intra-frequency measurements.

## A.7.7.7.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.7.1.2-1. Both absolute and relative accuracy of CSI-RSRP intra-frequency measurements are tested by using the parameters in table A.7.7.7.1.2-2 and A.7.7.7.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. The test consists of two time phases T1 and T2.

Table A.7.7.7.1.2-1: CSI-RSRP Intra frequency CSI-RSRP supported test configurations

Table A.7.7.7.1.2-2: CSI-RSRP Intra frequency general test parameters

Table A.7.7.7.1.2-3: CSI-RSRP Intra frequency OTA related test parameters

## A.7.7.7.1.3Test Requirements

The CSI-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.2.1 and relative accuracy requirements in clause 10.1.3.2.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.7.7.7.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.2.2-1.

During T2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.7.7.7.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.2.2-1.

During T1 and T2:

Relative accuracy of Cell 1 during T2 compared with Cell 1 during T1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.2.2-1

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.2.2-1.

Table A.7.7.7.1.3-1: CSI-RSRP absolute accuracy test requirement

## A.7.7.7.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.2.1 and 10.1.5.2.2 for inter-frequency measurements with the testing configurations for NR cells in table A.7.7.7.2.1-1.

Table A.7.7.7.2.1-1: Applicable NR configurations for FR2 inter-frequency CSI-RSRP accuracy test

## A.7.7.7.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 1 and Cell 2 are given in table A.7.7.7.2.2-1 and table A.7.7.7.2.2-2 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.7.7.7.2.2-1 and table A.7.7.7.2.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.7.7.7.2.2-1: CSI-RSRP inter-frequency test parameters

Table A.7.7.7.2.2-2: SS-RSRP inter frequency OTA related test parameters

## A.7.7.7.2.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirements in clause 10.1.5.2.1 and the relative requirements in clause 10.1.5.2.2.

Test 1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.7.7.7.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in A.7.7.7.2.3-2.

Test 2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.7.7.7.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in A.7.7.7.2.3-2.

Table A.7.7.7.2.3-1: CSI-RSRP absolute accuracy test requirement

Table A.7.7.7.2.3-2: CSI-RSRP relative accuracy test requirement

## A.7.7.8CSI-RSRQ

## A.7.7.8.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.8.2.1.

## A.7.7.8.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.8.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is tested by using the parameters in table A.7.7.8.1.2-2 and table A.7.7.8.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.7.7.8.1.2-1: CSI-RSRQ Intra frequency CSI-RSRQ supported test configurations

Table A.7.7.8.1.2-2: CSI-RSRQ Intra frequency test parameters

Table A.7.7.8.1.2-3: CSI-RSRQ Intra frequency OTA related test parameters

## A.7.7.8.1.3Test Requirements

The CSI-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal CSI-RSRQ+2.5 dB to Nominal CSI-RSRQ-3.5 dB and the CSI-RSRQ measurement accuracy in test 2 shall be within the range Nominal CSI-RSRQ+3.5 dB to Nominal CSI-RSRQ-4.5 dB according to the requirements in clause 10.1.8.2.1 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test. Nominal RSRQ is the value shown in table A.7.7.8.1.2-3.

## A.7.7.8.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.7.7.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.10.2.1 and 10.1.10.2.2 for inter-frequency measurement.

## A.7.7.8.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.7.7.8.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test parameters in table A.7.7.8.2.2-2 and table A.7.7.8.2.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A. 7.7.8.2.2-1: CSI-RSRQ Inter frequency supported test configurations

Table A.7.7.8.2.2-2: CSI-RSRQ Inter frequency general test parameters

Table A.7.7.8.2.2-3: CSI-RSRQ Inter frequency OTA related test parameters

## A.7.7.8.2.3Test Requirements

The CSI-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal CSI-RSRQ+2.5 dB to Nominal CSI-RSRQ -3.5 dB and the CSI-RSRQ measurement accuracy in test 2 shall be within the range Nominal CSI-RSRQ +3.5 dB to Nominal CSI-RSRQ -4.5 dB according to the requirements in clause 10.1.10.2.1 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test.

The CSI-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1.10.2.2.

## A.7.7.9CSI-SINR

## A.7.7.9.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.7.7.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.13.2.1.

## A.7.7.9.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.9.1.2-1. . The absolute accuracy of CSI-SINR intra-frequency measurement is test by using the parameters in table A.7.7.9.1.2-2 and table A.7.7.9.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.9.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

Table A.7.7.9.1.2-2: CSI-SINR Intra frequency test parameters

Table A.7.7.9.1.2-3: CSI-SINR Intra frequency OTA related test parameters

## A.7.7.9.1.3Test Requirements

The CSI-SINR absolute measurement accuracy in test 1 shall be within the range Nominal CSI-SINR+XdB to Nominal CSI-SINR –X-1 dB and the CSI-SINR measurement accuracy in test 2 shall be within the range Nominal CSI-SINR +YdB to Nominal CSI-SINR –Y-1 dB according to the requirements in clause 10.1.13.2.1 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test. The relative CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.13.2.1.

Editor’s note: The values of X and Y are pending on the accuracy requirement discussion

## A.7.7.9.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.7.7.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.15.2.1 and 10.1.15.2.2 for inter-frequency measurement.

## A.7.7.9.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.7.7.9.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test parameters in table A.7.7.9.2.2-2 and table A.7.7.9.2.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.9.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

Table A.7.7.9.2.2-2: CSI-SINR Inter frequency general test parameters

Table A.7.7.9.2.2-3: CSI-SINR Inter frequency OTA related test parameters

## A.7.7.9.2.3Test Requirements

The CSI-SINR absolute measurement accuracy in test 1 shall be within the range Nominal CSI-SINR +XdB to Nominal CSI-SINR –X-1 dB and the CSI-SINR measurement accuracy in test 2 shall be within the range Nominal CSI-SINR +YdB to Nominal CSI-SINR –Y-1 dB according to the requirements in clause 10.1.15.2.1 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test.

The CSI-SINR relative measurement accuracy shall fulfil the requirements in clause 10.1.15.2.2.

## A.7.7.10RSTD measurements

## A.7.7.10.1RSTD measurement accuracy test case for single positioning frequency layer

## A.7.7.10.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.7.10.1.1-1.

Table A.7.7.10.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

Table A.7.7.10.1.1-2: RSTD accuracy test parameters

Table A.7.7.10.1.1-3: RSTD accuracy OTA related test parameters

## A.7.7.10.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.7.7.10.2RSTD measurement accuracy test case for dual positioning frequency layer

## A.7.7.10.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

The supported test configurations are specified in table A.7.7.10.2.1-1.

Table A.7.7.10.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell on NR RF channel #1 in FR2. Cell 2 is a neighbour cell on a different NR RF channel #2 in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test.

Table A.7.7.10.2.1-2: RSTD accuracy test parameters

Table A.7.7.10.2.1-3: RSTD accuracy OTA related test parameters

## A.7.7.10.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.7.7.10.3RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state

## A.7.7.10.3.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-CONNECTED is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.7.7.10.3.1-1.

Table A.7.7.10.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be longer than the UE measurement period as defined in clause 9.9.2.7.

Table A.7.7.10.3.1-2: RSTD accuracy test parameters

Table A.7.7.10.3.1-3: RSTD accuracy OTA related test parameters

## A.7.7.10.3.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.7.7.10.4RSTD measurement accuracy test case with Rx TEG

## A.7.7.10.4.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement when the measurements of reference cell and neighbor cell are within the same Rx TEG meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.7.10.4.1-1.

Table A.7.7.10.4.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test.

The UE is requested to provide the Rx TEG in the test via nr-UE-RxTEG-Request-r17 in NR-TDOA-RequestLocationInformation.

The test applies to the UE supporting Rx TEG defiend in NR-UE-TEG-Capability and reporting the same Rx TEG for the measurements of reference cell and neighbour cell.

Table A.7.7.10.4.1-2: RSTD accuracy test parameters

Table A.7.7.10.4.1-3: RSTD accuracy OTA related test parameters

## A.7.7.10.4.2Test Requirements

The RSTD measurement for Cell 1 and Cell 2 should both fulfil the absolute accuracy requirements with same Rx TEG for reference cell and neighbour cell defined in clause 10.1.23.2.

## A.7.7.10.5NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode

## A.7.7.10.5.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement performed by UE by aggregating PRS resources from two positioning frequency layers (PFLs) meets the accuracy requirements specified in clause 10.1.23A.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.7.10.5.1-1.

Table A.7.7.10.5.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, all cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The UE is capable of performing RSTD measurements by aggregating PRS resources from two PFLs and is configured by the LMF to perform measurements by aggregating the PRS resources from two PFLs via nr-DL-PRS-JointMeasurementRequestedPFL-List. The NR-DL-TDOA-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test.

The test duration should be larger than the UE measurement period as defined in clause 9.9.2.10.

Table A.7.7.10.5.1-2: RSTD accuracy test parameters for PRS aggregation

Table A.7.7.10.5.1-3: RSTD accuracy OTA related test parameters

## A.7.7.10.5.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23A.2.

## A.7.7.11PRS-RSRP measurements

## A.7.7.11.1SA measurement accuracy with PRS in FR2

## A.7.7.11.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.7.7.11.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.11.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.7.7.11.1.2-2 and A.7.7.11.1.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.11.1.2-1: PRS-RSRP supported test configurations

Table A.7.7.11.1.2-2: PRS-RSRP general test parameters

Table A.7.7.11.1.2-3: PRS-RSRP OTA related test parameters

## A.7.7.11.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1 if the reported PRS-RSRP is in the range shown in table A.7.7.11.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

Table A.7.7.11.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.7.7.11.2SA measurement accuracy with PRS in FR2 with reduced sample number

## A.7.7.11.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with reduced sample number is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.7.7.11.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.11.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.7.7.11.2.2-2 and A.7.7.11.2.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.11.2.2-1: PRS-RSRP supported test configurations

Table A.7.7.11.2.2-2: PRS-RSRP general test parameters

Table A.7.7.11.2.2-3: PRS-RSRP OTA related test parameters

## A.7.7.11.2.3Test Requirements

In the test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1 if the reported PRS-RSRP is in the range shown in table A.7.7.11.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

Table A.7.7.11.2.3-1: PRS-RSRP absolute accuracy test requirement

## A.7.7.12UE Rx-Tx time difference measurements

## A.7.7.12.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA

## A.7.7.12.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.7.12.1.1-1.

Table A.7.7.12.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.7.12.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.7.12.1.2-1.

Table A.7.7.12.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

Table A.7.7.12.1.2-2: Void

## A.7.7.12.1.3Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.7.7.12.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA

## A.7.7.12.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with reduced number of samples is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.7.12.2.1-1.

Table A.7.7.12.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test.

The UE is configured to measure UE Rx-Tx time difference using reduced number of samples via reducedDL-PRS-ProcessingSamples in NR-Multi-RTT-RequestLocationInformation during the test.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.7.12.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.7.12.2.2-1.

Table A.7.7.12.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.7.7.12.2.3Test requirements

The UE Rx-Tx time difference measurement with reduced number of samples fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.7.7.12.3UE Rx-Tx time difference measurement accuracy with RxTx TEG

## A.7.7.12.3.1Test purpose and environment

The purpose of the test is to verify that the relative UE Rx-Tx time difference measurement accuracy when the two measurements are within the same RxTx TEG is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.7.12.3.1-1.

Table A.7.7.12.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test.

The UE is requested to provide the RxTx TEG in the test via nr-UE-RxTxTEG-Request-r17 in NR-Multi-RTT-RequestLocationInformation.

The test applies to the UE supporting RxTx TEG defiend in NR-UE-TEG-Capability and reporting the same RxTx TEG for the two UE Rx-Tx measurements.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The UE Rx-Tx time difference is derived by the difference of the receiving timing and the transmit timing for each cell.

## A.7.7.12.3.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.7.12.3.2-1.

Table A.7.7.12.3.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.7.7.12.3.3Test requirements

The relative accuracy is derived by the difference of the UE Rx-Tx measurements on the two cells.

The UE Rx-Tx time difference measurements for Cell 1 and Cell 2 fulfil the relative UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2.

## A.7.7.12.4UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA

## A.7.7.12.4.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25A. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR2.

The supported test configurations are listed in table A.7.7.12.4.1-1.

Table A.7.7.12.4.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2.. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

The general test parameters and cell specific test parameters are as given in table A.7.7.12.4.1-2 and table A.7.7.12.4.1-3 respectively.

Table A.7.7.12.4.1-2: General test parameters

Table A.7.7.12.4.1-3: Cell specific test parameters

## A.7.7.12.4.2Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25A for both Cell 1 and Cell 2.

## A.7.7.13PRS-RSRPP measurements

## A.7.7.13.1SA measurement accuracy with PRS in FR2

## A.7.7.13.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.

## A.7.7.13.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.13.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.13.1.2-1: PRS-RSRPP supported test configurations

Table A.7.7.13.1.2-2: PRS-RSRPP general test parameters

Table A.7.7.13.1.2-3: PRS-RSRPP OTA related test parameters

## A.7.7.13.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2 if the reported PRS-RSRPP is in the range shown in table A.7.7.13.1.2-1.

Table A.7.7.13.1.3-1: PRS-RSRPP absolute accuracy test requirement

## A.7.7.13.2SA measurement accuracy with reduced PRS samples in FR2

## A.7.7.13.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy with = 1 in FR2 is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.Nsample

The UE under test should support supportedDL-PRS-ProcessingSamples-RRC-CONNECTED, and the TE indicates the UE to perform positioning measurements with reduced number of samples. The PRS bandwidth is contained within the active BWP and the power difference between the serving cell SS-RSRP and neighbour cell PRS-RSRP is within [6] dB, so that = 1 is assumed.Nsample

## A.7.7.13.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.7.13.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.7.13.2.2-1: PRS-RSRPP supported test configurations

Table A.7.7.13.2.2-2: PRS-RSRPP general test parameters

Table A.7.7.13.2.2-3: PRS-RSRPP OTA related test parameters

## A.7.7.13.2.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2 if the reported PRS-RSRPP is in the range shown in table A.7.7.13.2.3-1.

Table A.7.7.13.2.3-1: PRS-RSRPP absolute accuracy test requirement

## A.7.7.14L1-RSRP measurement for group-based beam reporting

## A.7.7.14.1SSB based L1-RSRP measurement

## A.7.7.14.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for group-based beam reporting is within the specified limits. This test will verify the requirements in clauses 9.5.2 and clause 10.1.20.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.7.7.14.1.1-1.

The AoA setup for this test is Setup 5 as defined in clause A.3.15.5.

The UE which passes this test can skip A.7.7.4.1.

Table A.7.7.14.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.7.14.1.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.14.1.2-1 and table A.7.7.14.1.2-2 below. The absolute and relative accuracy of L1-RSRP measurements is tested by using the parameters in table A.7.7.14.1.2-1 and table A.7.7.14.1.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured two CSI resource sets with one SSB resource in each set. UE is configured to perform RLM, BFD measurement based on the SSB resources 0 and UE is configured to perform group-based L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.7.7.14.1.2-1: FR2 SSB based L1-RSRP general test parameters

Table A.7.7.14.1.2-2: FR2 SSB based L1-RSRP OTA related test parameters

## A.7.7.14.1.3Test Requirements

After 320 ms from the beginning of the test, the UE shall send L1-RSRP measurement report with SSB0 and SSB1 as a resource group, where the accuracy of the reported measurement results for SSB0 and SSB1 of Cell 1 shall fulfil the requirements in clauses 10.1.20.1. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB0 and SSB1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.14.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

For Test 2:

Absolute accuracy of SSB resource reported by UE in L1-RSRP report (SSB0 or SSB1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.14.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

Table A.7.7.14.1.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.14.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.7.7.14.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for group-based beam reporting is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause 10.1.20.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.14.2.1-1.

The AoA setup for this test is Setup X1 as defined in clause A.3.15.X1.

Table A.7.7.14.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.7.7.14.2.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.14.2.2-1 and table A.7.7.14.2.2-2 below. The absolute and relative accuracy of L1-RSRP measurements is tested by using the parameters in table A.7.7.14.2.2-1 and table A.7.7.14.2.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured two CSI resource sets with one CSI-RS resource in each set. UE is configured to perform RLM and BFD based on SSB 0 and 1 and UE is configured to perform group-based L1-RSRP measurement based on the CSI resources. CSI-RS resources are not transmitted in the same OFDM symbols as SSB.

Table A.7.7.14.2.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.7.7.14.2.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.7.7.14.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.20.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0 and CSI-RS1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.14.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

For Test 2:

Absolute accuracy of CSI-RS resource reported by UE in L1-RSRP report (CSI-RS0 or CSI-RS1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.14.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.7.7.14.2.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.15LTM L1-RSRP measurement

## A.7.7.15.1SSB based inter-frequency L1-RSRP measurement

## A.7.7.15.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause10.1.20B.1.1] for inter-frequency L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.7.7.15.1.1-1.

Prior to the start of the test,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A4 is used.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-The UE has reported L3 measurement results and performed SSB based L1-RSRP measurement on Cell 2.

Table A.7.7.15.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.7.7.15.1.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.7.15.1.2-1 and table A.7.7.15.1.2-2 below. The absolute accuracy of inter-frequency L1-RSRP measurements are tested by using the parameters in table A.7.7.15.1.2-1 and table A.7.7.15.1.2-2. The inter-frequency L1-RSRP measurements are supported by a measurement gap.

Before the test, UE is configured L1-RSRP measurement on SSB0 of Cell 2.

Table A.7.7.15.1.2-1: FR2 SSB based inter-frequency L1-RSRP general test parameters

Table A.7.7.15.1.2-2: FR2 SSB based inter-frequency L1-RSRP OTA related test parameters

## A.7.7.15.1.3Test Requirements

The L1-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirements in clause 10.1.20B.1.1.

Test 1:

Absolute accuracy of SSB0 in Cell 2. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.15.1.3-1.

Test 2:

Absolute accuracy of SSB0 in Cell 2. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.15.1.3-1.

Table A.7.7.15.1.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.15.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.7.7.15.2.1Test Purpose and Environment

The purpose of this test is to verify that CSI-RS based L1-RSRP measurement accuracy is within the specified requirements in clauses 9.5A.3 and clause 10.1.20A.2 with the testing configurations for NR cells in table A.7.7.15.2.1-1.

Before the test,

-UE is configured to Cell 1 (PCell)

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for Pcell indicating the UE to do periodic reporting

-UE is configured with CSI-RS based L1-RSRP measurement and periodic reporting on candidate cell (Cell 2) in PUCCH format 2.

-The UE has reported L3 measurement results and performance SSB based L1-RSRP measurement on Cell2.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-The UE has reported L3 measurement results and performed SSB based L1-RSRP measurement on Cell 2.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.7.7.15.2.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.7.7.15.2.2Test parameters

In this set of test cases there are 2 cells: NR Cell 1 as Pcell and NR Cell 2 as neighbour cell. All cells are on the same frequency. The absolute and relative accuracy of CSI-RS based L1-RSRP measurements are tested by using the parameters in table A.7.7.15.2.2-1 and table A.7.7.15.2.2-2.

There is no measurement gap configured in the test.

Table A.7.7.15.2.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.7.7.15.2.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.7.7.15.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for Cell 2 shall fulfil the requirements in clause 10.1.20A.2.

For Test 1:

Absolute accuracy of CSI-RS0 for Cell2. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.15.2.3-1.

Absolute accuracy of CSI-RS0 for Cell2. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.7.7.15.2.3-1.

Table A.7.7.15.2.3-1: L1-RSRP absolute accuracy test requirement

## A.7.7.16RSCPD Measurements

## A.7.7.16.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_CONNECTED

## A.7.7.16.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCPD measurement reported with RSTD measurement is within the specified limits. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.7.7.16.1.1-1.

Table A.7.7.16.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP [34] as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC_CONNECTED, shall be provided to the UE before the start of the test.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The test duration should be larger than the UE measurement period as defined in clause 9.9.2.

## A.7.7.16.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.7.7.16.1.2-1 and table A.7.7.16.1.2-2.

Table A.7.7.16.1.2-1: RSCPD accuracy test parameters

Table A.7.7.16.1.2-2: RSCPD accuracy OTA related test parameters

## A.7.7.16.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy specified in clause 10.1.43.2 for Cell 2.

## A.7.7.17RSCP with UE Rx-Tx time difference measurements

## A.7.7.17.1RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA

## A.7.7.17.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of DL RSCP measurement reported with UE Rx-Tx time difference measurement is within the specified limits. This test will verify the requirements in clause 10.1.44.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.7.12.2.1-1.

Table A.7.7.12.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData, NR-Multi-RTT-RequestLocationInformation with nr-DL-PRS-RSCP-Request from LMF via LPP [34] and NR-Multi-RTT-MeasurementCapability as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCP in RRC CONNECTED, shall be provided to the UE before the start of the test.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.7.17.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.7.17.1.2-1.

Table A.7.7.17.1.2-1: RSCP with UE Rx-Tx time difference measurement accuracy test parameters

## A.7.7.17.1.3Test requirements

The RSCP with UE Rx-Tx time difference measurements fulfils the RSCP measurement accuracy requirements specified in clause 10.1.44.2 for both Cell 1 and Cell 2.

## A.7.7.18L1 CLI measurements

## A.7.7.18.1SA L1-SRS-RSRP measurement accuracy with FR2 serving cell with SBFD

## A.7.7.18.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SRS-RSRP measurement accuracy in SBFD operation is within the specified limits. This test will verify the requirements in clauses 10.1.47.1.1 with the testing configurations for NR cells in table A.7.7.18.1.1-1.

Table A.7.7.18.1.1-1: Applicable NR configurations for FR2 L1-SRS-RSRP accuracy test

## A.7.7.18.1.2Test parameters

In this set of test cases there is one cell in the test, FR2 PCell (Cell 1) with SBFD operation. The test parameters for the Cell 1 are given in table A.7.7.18.1.2-1 and A.7.7.18.1.2-2 below. The test parameters for the (virtual) aggressor UE transmitting SRS are given in table A.7.7.18.1.2-2.

Before the test UE is configured to perform L1-SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in the UL subband in SBFD slots according to the SRS configuration in table A.7.7.18.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH on SRS symbol to be transmitted and on 2 data symbols before SRS to be transmitted, and OCNG/Noc is transmitted additionally in PRBs in UL subband.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. At the beginning of T2, the test equipment sends a DCI to trigger UE to report L1-SRS-RSRP.

Table A.7.7.18.1.2-1: FR2 test parameters for L1-SRS-RSRP accuracy

Table A.7.7.18.1.2-2: L1-SRS-RSRP accuracy OTA related test parameters for PCell and aggressor UE in FR2

Table A.7.7.18.1.2-3: SRS configuration parameters for FR2 L1-SRS-RSRP accuracy

## A.7.7.18.1.3Test Requirements

The L1-SRS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.47.1.1 and the rate of correct L1-SRS-RSRP measurement accuracy observed during repeated tests shall be at least 90%. The following requirements are to be verified:

During T1:

The UE is deemed to meet the requirement if the reported L1-SRS-RSRP is in the range shown in table A.7.7.18.1.3-1.

During T2:

The UE is deemed to meet the requirement if the reported L1-SRS-RSRP is in the range shown in table A.7.7.18.1.3-1.

Table A.7.7.18.1.3-1: L1-SRS-RSRP absolute accuracy test requirement

## A.7.7.18.2L1-CLI-RSSI measurement accuracy in FR2 with SBFD

## A.7.7.18.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.47.2.1 with the testing configurations for NR cells in table A.7.7.18.2.1-1.

Table A.7.7.18.2.1-1: Applicable NR configurations for FR2 CLI-RSSI accuracy test

## A.7.7.18.2.2Test parameters

In this set of test cases there is one cell in the test, FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.7.7.18.2.2-1 and A.7.7.18.2.2-2 below.

Before the test UE is configured to perform L1-CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for L1-CLI-RSSI resource. The L1-CLI-RSSI measurement resource configuration is in table A.7.7.18.2.2-3.

The test consists of two successive time periods, with time duration of T1 and T2, respectively. At the beginning of T2, the test equipment sends an DCI to trigger UE to report L1-CLI-RSSI.

Table A.7.7.18.2.2-1: FR2 test parameters for CLI-RSSI accuracy

Table A.7.7.18.2.2-2: CLI-RSSI accuracy OTA related test parameters

Table A.7.7.18.2.2-3: CLI-RSSI measurement resource configuration for FR2 CLI-RSSI accuracy

## A.7.7.18.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.47.2.1. The UE is deemed to meet the requirement if the reported CLI-RSSI is in the range shown in table A.7.7.18.2.3-1.

Table A.7.7.18.2.3-1: L1-CLI-RSSI absolute accuracy test requirement

## A.7.8Measurement procedure in RRC_INACTIVE

## A.7.8.1RSTD measurements

## A.7.8.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

## A.7.8.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6.2.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.7.8.1.1.1-1.

Table A.7.8.1.1.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.7.8.1.1.1-2, and cell specific test parameters are listed in table Table A.7.8.1.1.1-3 and table A.7.8.1.1.1-4.

Table A.7.8.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.8.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.8.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.8.1.1.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.8.1.2NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA

## A.7.8.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive.

The supported test configurations are specified in table A.7.8.1.2.1-1.

Table A.7.8.1.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2. PRS resources from all three cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The nr-DL-TDOA-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to m1.

The general test parameters are listed in table A.7.8.1.2.1-2, and cell specific test parameters are listed in table A.7.8.1.2.1-3 and A.7.8.1.2.1-4.

Table A.7.8.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.8.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.8.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.8.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.7.8.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_INACTIVE state

## A.7.8.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation in RRC_INACTIVE state meets the requirements specified in clause 5.6.2.6 in AWGN propagation condition in FR2 in standalone scenario when two intra-band contiguous positioning frequency layers (PFL) are configured.

The supported test configurations are listed in table A.7.8.1.3.1-1.

Table A.7.8.1.3.1-1: Supported test configurations

There are 6 synchronous cells in the test: Cell 1, Cell 2, Cell 3 Cell 4, Cell 5 and Cell 6. Cell 1 is the PCell on NR RF channel 1 in FR2. Cell 2 and Cell 3 are neighbour cells on the same RF channel as Cell 1. Cell 4, Cell 5 and Cell 6 are the neighbour cells on a different NR RF channel, i.e., RF channel 2, in FR2. Cell 1 and Cell 4, Cell 2 and Cell 5, Cell 3 and Cell 6 are respectively intra-band contiguous and PRS resources are transmitted by the same Tx chain for each combination.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2, Cell 3, Cell 4, Cell 5 and Cell 6. During T2 UE shall be in RRC_INACTIVE state and all 6 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note:The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

In NR-TDOA-ProvideAssistanceData, there are three NR-linkedDL-PRS-ResourceSetID-PRS-AggregationList. The first list indicates aggregation of PRS resource sets from Cell 1 and Cell 4, and the second list indicates aggregation of PRS resource sets from Cell 2 and Cell 5. The third list indicates aggregation of PRS resource sets from Cell 3 and Cell 6. In NR-TDOA-RequestLocationInformation, the IE nr-DL-PRS-JointMeasurementRequestedPFL-List is included and indicates aggregation of PFLs on RF channel 1 and RF channel 2.

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are given in table A.7.8.1.3.1-2, and cell specific test parameters for T1 and T2 are listed in table A.7.8.1.3.1-3 and table A.7.8.1.3.1-4, respectively.

Table A.7.8.1.3.1-2: General test parameters for RSTD measurement with PRS aggregation reporting delay

Table A.7.8.1.3.1-3: Cell-specific test parameters for RSTD measurement with PRS aggregation reporting delay during T1

Table A.7.8.1.3.1-4: Cell-specific test parameters for RSTD measurement with PRS aggregation reporting delay during T2

## A.7.8.1.3.2Test requirements

The RSTD measurement time with PRS aggregation in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.2.6.

The UE shall perform and report the RSTD measurements by aggregating PRS resources from Cell 2 and Cell 5, Cell 3 and Cell 6 respectively with respect to the Cell 1 and Cell 4 from which the transmitted PRS resources are also aggregated, within the time duration specified in clause 5.6.2.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events observed during repeated tests shall be at least 90%, where the reported RSTD measurement with PRS aggregation for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.3.

## A.7.8.1.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s

## A.7.8.1.4.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.2.5 for RSTD measurements in RRC_INACTIVE with eDRX and periodic reporting. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.7.8.1.4.1-1.

Table A.7.8.1.4.1-1: Supported test configurations

There are three cells in the test: Cell 1 (PCell and RSTD reference cell), Cell 2 (neighbor cell) and Cell 3 (neighbor cell). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and released to RRC_INACTIVE state before the start of T2. All cells transmit PRS only during the second time interval of duration T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the start of the first PRS resource instance received after the UE has transitioned to RRC_INACTIVE.

The test concludes after the UE reports the first set of measurements based on the configured reporting periodicity.

The general test parameters and cell specific test parameters are as given in table A.7.8.1.4.1-2 and table A.7.8.1.4.1-3 respectively.

Table A.7.8.1.4.1-2: General test parameters

Table A.7.8.1.4.1-3: Cell specific test parameters

## A.7.8.1.4.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 5.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

A test is considered complete after the UE has reported the first set of measurements based on the configured reporting interval.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3.

## A.7.8.2PRS-RSRP measurements

## A.7.8.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE

## A.7.8.2.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 5.6.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE. Supported test configurations are shown in table A.7.8.2.1.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.2.1.1-2, and table A.7.8.2.1.1-3.

Table A.7.8.2.1.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

Table A.7.8.2.1.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.8.2.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.7.8.2.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6.3.5.The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.8.2.2PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE

## A.7.8.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements specified in clause 5.6.3.5 in an environment with AWGN propagation conditions when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive.

The supported test configurations are specified in table A.7.8.2.2.1-1.

Table A.7.8.2.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2. PRS resources from both cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-AoD assistance data and location information request.

The nr-DL-AoD-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to m1.

The general test parameters are listed in table A.7.8.2.2.1-2, and cell specific test parameters are listed in table A.7.8.2.2.1-3.

Table A.7.8.2.2.1-2: General test parameters

Table A.7.8.2.2.1-3: Cell specific test parameters

## A.7.8.2.2.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.8.2.3PRS-RSRP reporting delay in RRC_INACTIVE with eDRX

## A.7.8.2.3.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 5.6.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE when configured with eDRX. Supported test configurations are shown in table A.7.8.2.3.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34], shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.2.3.1-2 and table A.7.8.2.3.1-3.

Table A.7.8.2.3.1-1: Supported test configurations

Table A.7.8.2.3.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.7.8.2.3.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.7.8.2.3.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6.3.5 with Tavailable_PRS = 0.64s starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is complete after the UE has reported the first set of results based on the configured reporting interval.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.8.3UE Rx-Tx time difference measurements

## A.7.8.3.1UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA

## A.7.8.3.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement in RRC_INACTIVE state meets the requirements specified in clause 5.6.4 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations in listed in table A.7.8.3.1.1-1.

Table A.7.8.3.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.8.3.1.1-2 and table A.7.8.3.1.1-3 respectively.

Table A.7.8.3.1.1-2: General test parameters

Table A.7.8.3.1.1-3: Cell specific test parameters

## A.7.8.3.1.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.4.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time specified in clause 5.6.4 starting from the beginning of time interval T2.

NOTE The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.8.3.2UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR2 SA

## A.7.8.3.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement meets the requirements specified in clause 5.6.4.5 in AWGN propagation condition in FR2 in standalone scenario when single-sample measurements are requested by the LMF. This test is applicable to UEs that support supportedDL-PRS-ProcessingSamples-RRC-Inactive.

The supported test configurations in listed in table A.7.8.3.2.1-1.

Table A.7.8.3.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2. PRS resources from both cells are transmitted within the initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The nr-Multi-RTT-RequestLocationInformation IE should indicate to the UE that single-sample measurements are requested, i.e. requestedDL-PRS-ProcessingSamples-r17 is set to m1.

The UE is configured to transmit SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.7.8.3.2.1-2 and table A.7.8.3.2.1-3 respectively.

Table A.7.8.3.2.1-2: General test parameters

Table A.7.8.3.2.1-3: Cell specific test parameters

## A.7.8.3.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90 %, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.8.3.3UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA

## A.7.8.3.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.4.6 for UE Rx-Tx measurements with PRS bandwidth aggregation. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR2.

The supported test configurations are listed in table A.7.8.3.3.1-1.

Table A.7.8.3.3.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2.. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The general test parameters and cell specific test parameters are as given in table A.7.8.3.3.1-2 and table A.7.8.3.3.1-3, respectively.

Table A.7.8.3.3.1-2: General test parameters

Table A.7.8.3.3.1-3: Cell specific test parameters

## A.7.8.3.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.6.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.8.3.4UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA

## A.7.8.3.4.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.4.5 for UE Rx-Tx measurements in RRC_INACTIVE with eDRX. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform UE Rx-Tx measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations in listed in table A.7.8.3.4.1-1.

Table A.7.8.3.4.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The general test parameters and cell specific test parameters are as given in table A.7.8.3.4.1-2 and table A.7.8.3.4.1-3 respectively.

Table A.7.8.3.4.1-2: General test parameters

Table A.7.8.3.4.1-3: Cell specific test parameters

## A.7.8.3.4.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

A test is complete after the UE has reported the first set of results based on the configured reporting interval.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.3.1.

## A.7.8.4PRS-RSRPP measurements

## A.7.8.4.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_INACTIVE state

## A.7.8.4.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement requirements specified in clause 5.6.5.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.7.8.4.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.4.1.1-2, and table A.7.8.4.1.1-3.

Table A.7.8.4.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.7.8.4.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.7.8.4.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

## A.7.8.4.1.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 5.6.5.5.The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6.5.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1.X, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.7.8.4.2PRS-RSRPP reporting delay test with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state

## A.7.8.4.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement requirements specified in clause 5.6.5.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario for reduced number of samples. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-Inactive is configured by LMF to perform PRS measurement with reduced number of samples. Supported test configurations are shown in table A.7.8.4.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.4.2.1-2, and table A.7.8.4.2.1-3.

Table A.7.8.4.2.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.7.8.4.2.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.7.8.4.2.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

## A.7.8.4.2.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 5.6.5.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6.5.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90 %, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1.38, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.7.8.4.3PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s in FR2

## A.7.8.4.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6.5.5 for PRS-RSRPP measurements in RRC_INACTIVE with eDRX and periodic reporting. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform PRS-RSRPP measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.7.8.4.3.1-1.

Table A.7.8.4.3.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and released to RRC_INACTIVE state before the start of T2. Both cells transmit PRS only during the second time interval of duration T2.

The NR-DL-AoD-ProvideAssistanceData and NR-DL-AoD-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-AoD assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the start of the first PRS resource instance received after the UE has transitioned to RRC_INACTIVE.

The test concludes after the UE reports the first set of measurements based on the configured reporting periodicity.

The general test parameters and cell specific test parameters are as given in table A.7.8.4.3.1-2 and table A.7.8.4.3.1-3, respectively.

Table A.7.8.4.3.1-2: General test parameters

Table A.7.8.4.3.1-3: Cell specific test parameters

## A.7.8.4.3.2Test requirements

The PRS-RSRPP measurement time shall fulfill the requirements specified in clause 5.6.5.5.

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1.38.3.

## A.7.8.5RSCPD Measurements

## A.7.8.5.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

## A.7.8.5.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD reported with RSTD measurement meets the requirements specified in clause 5.6.7.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The test environment is the same as in clause A.7.8.1.1 with the following additional configuration in table A.7.8.5.1.1-1 and description.

In nr-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE also is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s) to be measured within the configured time window.

Table A.7.8.5.1.1-1: Time window configuration

## A.7.8.5.1.2Test Requirements

The DL RSCPD reported with RSTD measurement time fulfils the requirements specified in clause 5.6.7.5.

The UE shall perform and report the DL RSCPD and DL RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3 and the reported RSCPD measurement for each correct event shall be within the RSCPD reporting range specified in clause 10.1.43.3.

## A.7.8.6RSCP Measurements

## A.7.8.6.1DL RSCP with UE Rx-Tx time difference measurements in RRC_INACTIVE for single positioning frequency layer in FR2 SA

## A.7.8.6.1.1Test purpose and environment

The purpose of the test is to verify that the DL RSCP and UE Rx-Tx time difference measurements in RRC_INACTIVE state meet the requirements specified in clause 5.6.8.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured for both DL RSCP measurement and UE Rx-Tx time difference measurement.

The supported test configurations are listed in table A.7.8.6.1.1-1.

Table A.7.8.6.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData message and NR-Multi-RTT-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE during T1. In NR-Multi-RTT-RequestLocationInformation, the UE is configured to perform DL RSCP measurement via nr-DL-PRS-RSCP-Request. The UE is configured to perform both DL RSCP and UE Rx-Tx time difference measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig, but the time window periodicity is not configured. The last slot containing the two messages for the multi-RTTI assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 shall be aligned with the start of the configured time window containing the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are listed in table A.7.8.6.1.1-2 and table A.7.8.6.1.1-3.

Table A.7.8.6.1.1-2: General test parameters

Table A.7.8.6.1.1-3: Cell specific test parameters

## A.7.8.6.1.2Test requirements

The DL RSCP with UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6.8.

The UE shall perform and report the DL RSCP and UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified DL RSCP with UE Rx-Tx time difference measurement time specified in clause 5.6.8 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported DL RSCP measurement for each correct event shall be within the DL RSCP reporting range specified in clause 10.1.44 and the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1.25.

## A.7.9Measurement performance requirements in RRC_INACTIVE

## A.7.9.1RSTD measurements

## A.7.9.1.1RSTD measurement accuracy test case for single positioning frequency layer in FR2 in RRC_INACTIVE state

## A.7.9.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.9.1.1.1-1.

Table A.7.9.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355[34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

Table A.7.9.1.1.1-2: RSTD accuracy test parameters

Table A.7.9.1.1.1-3: RSTD accuracy OTA related test parameters

## A.7.9.1.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.7.9.1.2RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state

## A.7.9.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions. In this test UE that supports supportedDL-PRS-ProcessingSamples-RRC-Inactive is configured by LMF to perform PRS measurement with reduced number of samples.

The supported test configurations are specified in table A.7.9.1.2.1-1.

Table A.7.9.1.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

Table A.7.9.1.2.1-2: RSTD accuracy test parameters

Table A.7.9.1.2.1-3: RSTD accuracy OTA related test parameters

## A.7.9.1.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

A.7.9.1.3RSTD measurement accuracy for PRS aggregation in FR2 in RRC_INACTIVE state

A.7.9.1.3.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation on two PFLs meets the accuracy requirements specified in clause 10.1.23A.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.9.1.3.1-1.

Table A.7.9.1.3.1-1: Supported test configurations

In the test there are four synchronous cells: Cell 1, Cell 2, Cell 3 and Cell 4. Cell 1 is the reference as well as the PCell on NR RF channel #1 in FR2. Cell 2 is a neighbour cell on the same NR RF channel as Cell 1. Cell 3 and Cell 4 are neighbor cells in a different NR RF channel #2 in FR2. Cell 1 and Cell 3 are intra-band contiguous, and PRS resources from Cell 1 and Cell 3 are transmitted by the same Tx chain. Cell 2 and Cell 4 are intra-band contiguous, and PRS resources from Cell 2 and Cell 4 are transmitted by the same Tx chain.

GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. The UE is configured with DRX cycle of 0.64s.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.6.

In NR-TDOA-ProvideAssistanceData, there are two NR-linkedDL-PRS-ResourceSetID-PRS-AggregationList. The first list indicates aggregation of resource sets from Cell 1 and Cell 3, and the second list indicates aggregation of resource sets from Cell 2 and Cell 4. In NR-TDOA-RequestLocationInformation, nr-DL-PRS-JointMeasurementRequestedPFL-List is included and indicates aggregation of PFLs on NR RF channel #1 and NR RF channel #2.

Table A.7.9.1.3.1-2: RSTD accuracy test parameters

Table A.7.9.1.3.1-3: RSTD accuracy OTA related test parameters

A.7.9.1.3.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23A.2.

## A.7.9.2PRS-RSRP measurements

## A.7.9.2.1SA measurement accuracy with PRS in FR2 in RRC_INACTIVE

## A.7.9.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.7.9.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.9.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.7.9.2.1.2-2 and A.7.9.2.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.7.9.2.1.2-1: PRS-RSRP supported test configurations

Table A.7.9.2.1.2-2: PRS-RSRP general test parameters

Table A.7.9.2.1.2-3: PRS-RSRP OTA related test parameters

## A.7.9.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1 if the reported PRS-RSRP is in the range shown in table A.7.9.2.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

Table A.7.9.2.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.7.9.2.2PRS-RSRP measurements with reduced number of sample in RRC_INACTIVE

## A.7.9.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.7.9.2.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.9.2.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.7.9.2.2.2-2 and A.7.9.2.2.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.7.9.2.2.2-1.

Table A.7.9.2.2.2-1: PRS-RSRP supported test configurations

Table A.7.9.2.2.2-2: PRS-RSRP general test parameters

Table A.7.9.2.2.2-3: PRS-RSRP OTA related test parameters

## A.7.9.2.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1 if the reported PRS-RSRP is in the range shown in table A.7.9.2.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

Table A.7.9.2.2.3-1: PRS-RSRP absolute accuracy test requirement

## A.7.9.3UE Rx-Tx time difference measurements

## A.7.9.3.1UE Rx-Tx time difference measurements in RRC_INACTIVE

## A.7.9.3.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario.

The supported test configuration is listed in table A.7.9.3.1.1-1.

Table A.7.9.3.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.9.3.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.9.3.1.2-1.

Table A.7.9.3.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.7.9.3.1.3Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.7.9.3.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA

## A.7.9.3.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with reduced number of samples in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clause 10.1.25.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.9.3.2.1-1.

Table A.7.9.3.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The UE is configured to measure UE Rx-Tx time difference using reduced number of samples via requestedDL-PRS-ProcessingSamples in NR-Multi-RTT-RequestLocationInformation.

UE shall be configured to enter into RRC_INACTIVE state before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.9.3.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.7.9.3.2.2-1.

Table A.7.9.3.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.7.9.3.2.3Test requirements

The UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE state fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25.2 for both Cell 1 and Cell 2.

## A.7.9.3.3UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA in RRC_INACTIVE state

## A.7.9.3.3.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.25A. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform UE Rx-Tx measurements by aggregating two intra-band contiguous positioning frequency layers (PFLs) in FR2.

The supported test configurations are listed in table A.7.9.3.3.1-1.

Table A.7.9.3.3.1-1: Supported test configurations

There are two cells in the test: Cell 1 (PCell) and Cell 2 (neighbor cell). Each cell is associated with a different TRP/DL PRS ID in the NR-DL-PRS-AssistanceData TS 37.355 [34]. Cell 1 transmissions other than DL PRS are allocated in RF channel #1. In addition, both cells/TRPs transmit DL PRS in two intra-band contiguous PFLs in RF channel #1 and RF channel #2. PFL1 is allocated within RF channel #1 and PFL2 is allocated within RF channel #2. Except for the frequency offset between them, both PFLs have identical PRS configuration.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test.

The NR-Multi-RTT-ProvideAssistanceData message provided to the UE must include NR-DL-PRS-AggregationInfo-r18 linking each PRS resource in PFL1 to the corresponding PRS resource in PFL2.

The NR-Multi-RTT-RequestLocationInformation message provided to the UE must request bandwidth aggregated measurements via jointMeasurementsReq and nr-DL-PRS-JointMeasurementRequestedPFL-List.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

The general test parameters and cell specific test parameters are as given in table A.7.9.3.3.1-2 and table A.7.9.3.3.1-3, respectively.

Table A.7.9.3.3.1-2: General test parameters

Table A.7.9.3.3.1-3: Cell specific test parameters

## A.7.9.3.3.2Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1.25A for both Cell 1 and Cell 2.

## A.7.9.4PRS-RSRPP measurements

## A.7.9.4.1SA measurement accuracy in FR2 in RRC INACTIVE

## A.7.9.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1.38.2.

## A.7.9.4.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.9.4.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.7.9.4.1.2-1.

Table A.7.9.4.1.2-1: PRS-RSRPP supported test configurations

Table A.7.9.4.1.2-2: PRS-RSRPP general test parameters

Table A.7.9.4.1.2-3: PRS-RSRPP OTA related test parameters

## A.7.9.4.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2. if the reported PRS-RSRPP is in the range shown in table A.7.9.4.1.3-1.

Table A.7.9.4.1.3-1: PRS-RSRPP absolute accuracy test requirement

## A.7.9.4.2SA measurement accuracy with reduced PRS samples in FR2 in RRC INACTIVE

## A.7.9.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy with = 1 in FR2in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1.38.2. The UE under test should support supportedDL-PRS-ProcessingSamples-RRC-Inactive, and the TE indicates the UE to perform positioning measurements with reduced number of samples. The PRS bandwidth is contained within the initial DL BWP and the power difference between the serving cell SS-RSRP and neighbour cell PRS-RSRP is within 6 dB, so that = 1 is assumed. NsampleNsample

## A.7.9.4.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.9.4.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.7.9.4.2.2-1: PRS-RSRPP supported test configurations

Table A.7.9.4.2.2-2: PRS-RSRPP general test parameters

Table A.7.9.4.2.2-3: PRS-RSRPP OTA related test parameters

## A.7.9.4.2.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2 if the reported PRS-RSRPP is in the range shown in table A.7.9.4.2.3-1.

Table A.7.9.4.2.3-1: PRS-RSRPP absolute accuracy test requirement

## A.7.9.5RSCPD Measurements

## A.7.9.5.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_INACTIVE

## A.7.9.5.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCPD measurement reported with RSTD measurement is within the specified limits. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.7.9.5.1.1-1.

Table A.7.9.5.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC_INACTIVE, shall be provided to the UE before the start of the test.

## A.7.9.5.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.7.9.5.1.2-1.

Table A.7.9.5.1.2-1: RSCPD with UE RSTD measurement accuracy test parameters in RRC_INACTIVE

Table A.7.7. 5.1.2-2: RSTD accuracy OTA related test parameters

## A.7.9.5.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy specified in clause 10.1.43.2 for Cell 2.

## A.7.9.6RSCP Measurements

## A.7.9.6.1RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA

## A.7.9.6.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of DL RSCP measurement reported with UE Rx-Tx time difference measurement in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clause 10.1.44.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.7.9. 6.1.1-1.

Table A.7.9.6.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData , NR-Multi-RTT-RequestLocationInformation with nr-DL-PRS-RSCP-Request from LMF via LPP and NR-Multi-RTT-MeasurementCapability as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCP in RRC INACTIVE, shall be provided to the UE before the start of the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.7.9.6.1.2Test parameters

The test parameters are given in table A.7.9. 6.1.2-1.

Table A.7.9. 6.1.2-1: RSCP with UE Rx-Tx time difference measurement accuracy test parameters

## A.7.9.6.1.3Test requirements

The RSCP measurement reported with UE Rx-Tx time difference measurements fulfils the RSCP measurement accuracy requirements specified in clause 10.1.44.2 for both Cell 1 and Cell 2.

## A.7.10Measurement Procedure in RRC_IDLE

## A.7.10.1RSTD Measurements

## A.7.10.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE

## A.7.10.1.1.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 4.5.2.5 for RSTD measurements in RRC_IDLE without eDRX. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.7.10.1.1.1-1.

Table A.7.10.1.1-1: Supported test configurations

There are three cells in the test: Cell 1 (PCell and RSTD reference cell), Cell 2 (neighbor cell) and Cell 3 (neighbor cell). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and released to RRC_IDLE state before the start of T2. All cells transmit PRS only during the second time interval of duration T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.7.10.1.1.1-2, and cell specific test parameters are listed in table A.7.10.1.1.1-2, table A.7.10.1.1.1-3, and table A.7.10.1.1.1-4.

Table A.7.10.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.7.10.1.1.1-2-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.7.10.1.1.1-2-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.7.10.1.1.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 4.5.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2.

NOTE  1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3.

## A.7.10.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

## A.7.10.1.2.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 4.5.2.5 for RSTD measurements in RRC_IDLE with eDRX and periodic reporting. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.7.10.1.2.1-1.

Table A.7.10.1.2.1-1: Supported test configurations

There are three cells in the test: Cell 1 (PCell and RSTD reference cell), Cell 2 (neighbor cell) and Cell 3 (neighbor cell). All cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and released to RRC_IDLE state before the start of T2. All cells transmit PRS only during the second time interval of duration T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE at least T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the start of the first PRS resource instance received after the UE has transitioned to RRC_IDLE.

The test concludes after the UE reports the first set of measurements based on the configured reporting periodicity.

The general test parameters and cell specific test parameters are as given in table A.7.10.1.2.1-2 and table A.7.10.1.2.1-3, respectively.

Table A.7.10.1.2.1-2: General test parameters

Table A.7.10.1.2.1-3: Cell specific test parameters

## A.7.10.1.2.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 4.5.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

A test is considered complete after the UE has reported first set of measurement based on the configured reporting periodicity.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3.

## A.7.10.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_IDLE state

## A.7.10.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement with PRS aggregation in RRC_IDLE state meets the requirements specified in clause 4.5.2.6 in AWGN propagation condition in FR2 in standalone scenario when two intra-band contiguous positioning frequency layers (PFLs) are configured.

The test environment and configurations reuse the test case for RRC_INACTIVE state defined in clause A.7.8.1.3 except that UE shall be in RRC_IDLE state and all 6 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DLBWP during T2.

## A.7.10.1.3.2Test requirements

The RSTD measurement time with PRS aggregation in RRC_IDLE state fulfils the requirements specified in clause 4.5.2.6.

The UE shall perform and report the RSTD measurements by aggregating PRS resources from Cell 2 and Cell 5, Cell 3 and Cell 6 respectively with respect to the Cell 1 and Cell 4 from which the transmitted PRS resources are also aggregated, within the time duration specified in clause 4.5.2.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events observed during repeated tests shall be at least 90%, where the reported RSTD measurement with PRS aggregation for each correct event shall be within the RSTD reporting range specified in clause 10.1.23A.3.

## A.7.10.2PRS-RSRP Measurements

## A.7.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR2

## A.7.10.2.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 4.5.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_IDLE state. Supported test configurations are shown in table A.7.10.2.1.1-1.

Table A.7.10.2.1.1-1: supported test configurations for PRS RSRP measurement for FR2.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED state, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34], shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_IDLE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.10.2.1.1-2 and table A.7.10.2.1.1-3.

Table A.7.10.2.1.1-2: General test parameters for PRS RSRP measurement reporting delay.

Table A.7.10.2.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay.

## A.7.10.2.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 4.5.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 4.5.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.7.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s

## A.7.10.2.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 4.5.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_IDLE when configured with eDRX.

The supported test configurations in table A.7.8.2.3.1-1 apply for this test.

The test procedure in clause A.7.8.2.3.1 apply for this test, except that during T2, UE is in RRC_IDLE state.

The general test parameters as specified in table A.7.8.2.3.1-2 apply for this test, except those specified in table A.7.10.2.2.1-1.

The cell specific test parameters as specified in table A.7.8.2.3.1-3 apply for this test.

Table A.7.10.2.2.1-1: General test parameters for PRS RSRP measurement reporting delay

## A.7.10.2.2.2Test Requirements

The test requirements in clause A.7.8.2.3.2 apply for this test, except that the time limits are specified in clause 4.5.3.5.

## A.7.10.3RSCPD Measurements

## A.7.10.3.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state

## A.7.10.3.1.1Test Purpose and Environment

The purpose of the test is to verify that the DL RSCPD reported with RSTD measurement meets the requirements specified in clause 5.6.7.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The test environment is the same as in clause A.7.10.1.1 with the following additional configuration in table A.7.10.3.1.1-1 and description.

In nr-DL-TDOA-RequestLocationInformation, the UE is configured to perform DL RSCPD measurement via dl-PRS-RSCPD-Request. The UE also is configured to perform both RSCPD and RSTD measurements within the time window indicated to UE via nr-DL-PRS-MeasurementTimeWindowsConfig.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s) to be measured within the configured time window.

Table A.7.10.3.1.1-1: Time window configuration

## A.7.10.3.1.2Test Requirements

The DL RSCPD reported with RSTD measurement time fulfils the requirements specified in clause 5.6.7.5.

The UE shall perform and report the DL RSCPD and DL RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1.23.3 and the reported RSCPD measurement for each correct event shall be within the RSCPD reporting range specified in clause 10.1.43.3.

## A.7.11Measurement Performance Requirements in RRC_IDLE

## A.7.11.1RSTD Measurements

## A.7.11.1.1NR RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE

## A.7.11.1.1.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement in RRC_IDLE state without eDRX meets the accuracy requirements specified in clause 10.1.23.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.7.11.1.1.1-1.

Table A.7.11.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6.2.5.

The RSTD accuracy test parameters are listed in table A.7.11.1.1.1-2, and the RSTD accuracy OTA related test parameters are listed in table A.7.11.1.1.1-3.

Table A.7.11.1.1.1-2: RSTD accuracy test parameters

Table A.7.11.1.1.1-3: RSTD accuracy OTA related test parameters

## A.7.11.1.1.2Test requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23.2.

## A.7.11.1.2RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

## A.7.11.1.2.1Test purpose and environment

The purpose of this test is to verify that RSTD measurements performed in RRC_IDLE with eDRX and periodic reporting satisfy the measurement accuracy requirements specified in clause 10.1.23.2. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.7.11.1.2.1-1.

Table A.7.11.1.2.1-1: Supported test configurations

There are two synchronous cells in the test: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34], shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.5.2.5.

The general test parameters and cell specific test parameters are as given in table A.7.11.1.2.1-2 and table A.7.11.1.2.1-3 respectively.

Table A.7.11.1.2.1-2: General test parameters

Table A.7.11.1.2.1-3: Cell specific test parameters

## A.7.11.1.2.2Test requirements

The reported RSTD measurements shall fulfill the absolute accuracy requirements specified in clause 10.1.23.2.

## A.7.11.1.3NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_IDLE state

## A.7.11.1.3.1Test purpose and environment

The purpose of the test is to verify that the RSTD measurement results with PRS aggregation in RRC_IDLE state meets the requirements specified in clause 10.1.23A.2 in AWGN propagation condition in FR2 in standalone scenario when two intra-band contiguous positioning frequency layers (PFLs) are configured.

The test environment and configurations reuse the test case for RRC_INACTIVE state defined in clause A.7.9.1.3, except that UE shall be in RRC_IDLE state and all 4 cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP during T2.

## A.7.11.1.3.2Test requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.23A.2.

## A.7.11.2PRS-RSRP measurements

## A.7.11.2.1PRS-RSRP measurement accuracy test case for non-RedCap UE in FR2 in RRC_IDLE state

## A.7.11.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy in RRC_IDLE is within the specified limits. This test will verify the requirements in clauses 10.1.24.2.1 and 10.1.24.2.2.

## A.7.11.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.7.11.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in tables A.7.11.2.1.2-2 and A.7.11.2.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.7.11.2.1.2-1: PRS-RSRP supported test configurations

Table A.7.11.2.1.2-2: PRS-RSRP general test parameters

Table A.7.11.2.1.2-3: PRS-RSRP OTA related test parameters

## A.7.11.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.24.2.1 if the reported PRS-RSRP is in the range shown in table A.7.11.2.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1.24.2.2.

Table A.7.11.2.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.7.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 for case 2 when eDRX cycle > 10.24s

## A.7.11.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE with eDRX meets the accuracy requirements specified in clauses 10.1.24.2.1 and 10.1.24.2.2 in an environment with AWGN propagation conditions.

## A.7.11.2.2.1Test parameters

The supported test configurations in table A.7.9.2.1.2-1 apply for this test.

The test procedure in clause A.7.9.2.1.2 apply for this test, except that UE is in RRC_IDLE state.

The general test parameters as specified in table A.7.9.2.1.2-2 apply for this test, except those additionally specified in table A.7.11.2.2.1-1.

The OTA related test parameters in table A.7.9.2.1.2-3 apply for this test.

Table A.7.11.2.2.1-1: PRS-RSRP test parameters

## A.7.11.2.2.2Test Requirements

The test requirements in clause A.7.9.2.1.3 apply for this test.

## A.7.11.3RSCPD measurements

## A.7.11.3.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_IDLE

## A.7.11.3.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of RSCPD measurement reported with RSTD measurement is within the specified limits. This test will verify the requirements in clause 10.1.43.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.7.11.3.1.1-1.

Table A.7.11.3.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation with dl-PRS-RSCPD-Request from LMF via LPP [34] as defined in TS 37.355 [34], clause 6.5.12, to enable UE to perform and report RSCPD in RRC_IDLE, shall be provided to the UE before the start of the test.

## A.7.11.3.1.2Test parameters

The RSCPD with RSTD accuracy test parameters are given in table A.7.11.3.1.1.2-1.

Table A.7.11.3.1.2-1: RSCPD with UE RSTD measurement accuracy test parameters in RRC_IDLE

Table A.7. 11.3.1.2-1-2: RSTD accuracy OTA related test parameters

## A.7.11.3.1.3Test requirements

The RSCPD reported together with RSTD fulfils RSCPD measurement accuracy specified in clause 10.1.43.2 for Cell 2.
