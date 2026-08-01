---
type: spec
aliases:
  - 38.133_38133-j50_sA.1-A.3
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.1-A.3/content.md"
---
# TS 38.133 38133-j50_sA.1-A.3

## Annex A (normative):Test Cases

## A.1Purpose of annex

The purpose of annex A is to define test cases and the relevant configurations for verifying various types of RRM requirements with NR cells, including SA NR, EN-DC, and NE-DC deployments as well as standalone E-UTRA deployments.

## A.2Requirement classification for statistical testing

Requirements in this specification are either expressed as absolute requirements with a single value stating the requirement or expressed as a success rate. There are no provisions for the statistical variations that will occur when the parameter is tested.

Annex A outlines the tests in more detail and lists the test parameters needed. The test will result in an outcome of a test variable value for the device under test (DUT) inside or outside the test limit. Overall, the probability of a "good" DUT being inside the test limit(s) and the probability of a "bad" DUT being outside the test limit(s) should be as high as possible. For this reason, when selecting the test variable and the test limit(s), the statistical nature of the test is accounted for.

The statistical nature depends on the type of requirement. Some have large statistical variations, while others are not statistical in nature at all. When testing a parameter with a statistical nature, a confidence level is set. This establishes the probability that a DUT passing the test actually meets the requirements and determines how many times a test has to be repeated and what the pass and fail criteria are. Those aspects are not covered by TS 38.133. The details of the tests on how many times to run it and how to establish confidence in the tests are described in TS 38.533 [5]. This annex establishes the variable to be used in the test and whether it can be viewed as statistical in nature or not.

## A.2.1Types of requirements in TS 38.133

## A.2.1.1Time and delay requirements on UE higher layer actions

A very large part of the RRM requirements are delay requirements:

-In RRC_IDLE state mobility (clause A.6.1 and A.7.1) there is cell re-selection delay.

-In RRC_CONNECTED state mobility (clauses A.4.3, A.4.6, A.5.3, A.5.6, A.6.3, A.6.6, A.7.3 and A.7.6) there is handover delay, cell search delay and measurement reporting delay.

-In RRC Connection Control (clauses A.4.3.2, A.5.3.2, A.6.3.2 and A.7.3.2) there is RRC re-establishment delay.

All have in common that the UE is required to perform an action observable in higher layers (e.g. camp on the correct cell) within a certain time after a specific event (e.g. when a new strong pilot or reference signal appears). The delay time is statistical in nature for several reasons, among others that several of the measurements are performed by the UE in a fading radio environment.

The variations make a strict limit unsuitable for a test. Instead there is a condition set for a correct action by the UE, e.g. that the UE shall camp on the correct cell within X seconds. Then the rate of correct events is observed during repeated tests and a limit is set on the rate of correct events, usually 90% correct events are required. How the limit is applied in the test depends on the confidence required, further detailed are in TS 38.533 [5].

## A.2.1.2Measurements of power levels, relative powers and time

A very large number of requirements are on measurements that the UE performs:

-In RRC_CONNECTED state mobility (clauses A.4.3, A.5.3, A.6.3 and A.7.3) there are measurement reports.

-In Measurement Performance Requirements (clauses A.4.7, A.5.7, A.6.7 and A.7.7) there are requirements for all type of measurements.

The accuracy requirements on measurements are expressed in this specification as a fixed limit (e.g. +/-X dB), but the measurement error will have a distribution that is not easily confined in fixed limits. Assuming a Gaussian distribution of the error, the limits will have to be set at +/-3.29 if the probability of failing a "good DUT" in a single test is to be kept at 0.1%. It is more reasonable to set the limit tighter and test the DUT by counting the rate of measurements that are within the limits, in a way similar to the requirements on delay.

## A.2.1.3Implementation requirements

A few requirements are strict actions the UE should take or capabilities the UE should have, without any allowance for deviations. These requirements are absolute and should be tested as such. Examples are:

-"Event triggered report rate" in RRC_CONNECTED state mobility (clauses A.4.3, A.4.6, A.5.3, A.5.6, A.6.3, A.6.6, A.7.3 and A.7.6),

-"Correct behaviour at time-out" in RRC connection control (clauses A.4.3.2, A.5.3.2, A.6.3.2 and A.7.3.2).

## A.2.1.4Physical layer timing requirements

There are requirements on Timing (clauses A.4.4, A.5.4, A.6.4 and A.7.4). There are both absolute and relative limits on timing accuracy depending upon the type of requirement. Examples are:

-Initial Transmit Timing (clauses A.4.4.1, A.5.4.1, A.6.4.1 and A.7.4.1) has an absolute limit on timing accuracy.

-Timing Advance (clauses A.4.4.2, A.5.4.2, A.6.4.2 and A.7.4.2) has a relative limit on timing accuracy.

## A.2.1.5Requirements under CCA

A few requirements include CCA failures in DL and or UL. Considering that the CCA model is of statistical nature, requirements that include CCA failures are always considered of statistical nature.

## A.3RRM test configurations

## A.3.1Reference measurement channels

## A.3.1.1PDSCH

## A.3.1.1.1FDD

Table A.3.1.1.1-1: PDSCH Reference Measurement Channels for SCS=15 kHz

## A.3.1.1.2TDD

For tests with VSAT UEs using FR1 numerology in FDD operation, the TDD tables below may be used.

Table A.3.1.1.2-1: PDSCH Reference Measurement Channels for SCS=15 kHz

Table A.3.1.1.2-2: PDSCH Reference Measurement Channels for SCS=30 kHz

Table A.3.1.1.2-3: PDSCH Reference Measurement Channels for SCS=120 kHz

## A.3.1.2CORESET for RMSI scheduling

## A.3.1.2.1FDD

Table A.3.1.2.1-1: RMSI CORESET Reference Channel for FDD with SCS=15KHz

## A.3.1.2.2TDD

For tests with VSAT UEs using FR1 numerology in FDD operation, the TDD tables below may be used.

Table A.3.1.2.2-1: RMSI CORESET Reference Channel for TDD with SCS=15kHz

Table A.3.1.2.2-2: RMSI CORESET Reference Channel for TDD with SCS=30kHz

Table A.3.1.2.2-3: RMSI CORESET Reference Channel for TDD with SCS=120kHz

## A.3.1.3CORESET for RMC scheduling

## A.3.1.3.1FDD

Table A.3.1.3.1-1: Control Channel RMC for FDD with SCS=15kHz

Table A.3.1.3.1-2: Control Channel RMC for FDD with SCS=120kHz

Table A.3.1.3.1-3: Control Channel RMC for FDD with SCS=15kHz

## A.3.1.3.2TDD

For tests with VSAT UEs using FR1 numerology in FDD operation, the TDD tables below may be used.

Table A.3.1.3.2-1: Control Channel RMC for TDD with SCS=15kHz

Table A.3.1.3.2-2: Control Channel RMC for TDD with SCS=30kHz

Table A.3.1.3.2-3: Control Channel RMC for TDD with SCS=120kHz

Table A.3.1.3.2-4: Control Channel RMC for TDD with SCS=15kHz

Table A.3.1.3.2-5: Control Channel RMC for TDD with SCS=30kHz

## A.3.1.4TDD UL/DL configuration

Table A.3.1.4-1: TDD UL/DL configuration for SCS=15 kHz

Table A.3.1.4-2: TDD UL/DL configuration for SCS=30 kHz

Table A.3.1.4-3: TDD UL/DL configuration for SCS=120 kHz

Table A.3.1.4-4: TDD UL/DL configuration of SBFD for SCS=30 kHz

## A.3.1AReference measurement channels under CCA

## A.3.1A.1PDSCH

## A.3.1A.1.1TDD

Table A.3.1A.1.1-1: PDSCH Reference Measurement Channels for SCS=30 kHz

## A.3.1A.2CORESET for RMSI scheduling

## A.3.1A.2.1TDD

Table A.3.1A.2.1-1: RMSI CORESET Reference Channel for SCS=30KHz

## A.3.1A.3CORESET for RMC scheduling

## A.3.1A.3.1TDD

Table A.3.1A.3.1-1: Control Channel RMC with SCS=30KHz

## A.3.1A.4TDD UL/DL configuration

Table A.3.1A.4-1: TDD UL/DL configuration for SCS=30 kHz

## A.3.1A.5RMC burst transmission model

RMC not conveying RMSI is scheduled during the RMC burst. The length of the transmission burst in slots is defined as N. The burst transmission format is determined according to the steps below:

1.Select N randomly from a given set of the number of slots S1 = {1,3,5} with equal probability as the total length of RMC burst transmission format.

2.A uniform random variable from 0 to 1 is generated. If the random variable is less than PCCA_DL, a burst of N fully occupied slots is transmitted. Otherwise, the RMC burst transmission is muted and the muting duration is the same as the number N of slots for determined burst format.

RMC burst transmission is scheduled outside discovery burst transmission window. If transmission occurred in the previous slot, transmission is muted for a duration of one slot. Additionally, if the start time of the candidate RMC burst transmission is within 5 slots of the start of the discovery burst transmission window, RMC transmission is not performed.A.3.2OFDMA channel noise generator (OCNG).

## A.3.2.1Generic OFDMA Channel Noise Generator (OCNG)

The OCNG pattern is used in a test for modelling allocations of unused resources in the channel bandwidth to virtual UEs (which are not under test). The OCNG pattern comprises PDCCH and PDSCH transmissions to the virtual UEs. For the cells operating under CCA, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during the slots for which CCA attempt is unsuccessful or during DBT windows.

## A.3.2.1.1OCNG pattern 1: Generic OCNG pattern for all unused REs

Table A.3.2.1.1-1: OP.1: Generic OCNG pattern for all unused REs

## A.3.2.1.2OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup

Table A.3.2.1.2-2: OP.2: Generic OCNG pattern for all unused REs for 2AoA setup

## A.3.2.1.3OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET

Table A.3.2.1.3-1: OP.3: Generic OCNG pattern for unused REs in the same BW as CORESET

## A.3.2.1.4OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s)

Table A.3.2.1.4-1: OP.4: Generic OCNG pattern for all unused REs outside SSB slot(s)

A.3.2.1.5OCNG pattern 5: Generic OCNG pattern for unused REs in the same bandwidth as CORESET for 2AoA setup

Table A.3.2.1.5-1: OP.5: Generic OCNG pattern for unused REs in the same BW as CORESET for 2AoA setup

## A.3.2.2Void

## A.3.3Reference DRX configurations

## A.3.3.1DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms

Table A.3.3.1-1: DRX.1: DRX cycle = 40 ms and time alignment timer (TAT) = 500 ms

## A.3.3.2DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms

Table A.3.3.2-1: DRX.2: DRX cycle = 640 ms and time alignment timer (TAT) = 500 ms

## A.3.3.3DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity

Table A.3.3.3-1: DRX.3: DRX cycle = 40 ms and time alignment timer (TAT) = Infinity

## A.3.3.4DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity

Table A.3.3.4-1: DRX.4: DRX cycle = 160 ms and time alignment timer (TAT) = Infinity

## A.3.3.5DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity

Table A.3.3.5-1: DRX.5: DRX cycle = 320 ms and time alignment timer (TAT) = Infinity

## A.3.3.6DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms

Table A.3.3.6-1: DRX.6: DRX cycle = 320 ms and time alignment timer (TAT) = 500 ms

## A.3.3.7DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity

Table A.3.3.7-1: DRX.7: DRX cycle = 640 ms and time alignment timer (TAT) = Infinity

## A.3.3.8DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity

Table A.3.3.8-1: DRX.8: DRX cycle = 320 ms and time alignment timer (TAT) = Infinity

## A.3.3.9DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms

Table A.3.3.9-1: DRX.9: DRX cycle = 40 ms and time alignment timer (TAT) = 500 ms

## A.3.3.10DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms

Table A.3.3.10-1: DRX.10: DRX cycle = 640 ms and time alignment timer (TAT) = 500 ms

## A.3.3.11DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity

Table A.3.3.11-1: DRX.11: DRX cycle = 20 ms and time alignment timer (TAT) = Infinity

## A.3.3.12DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity

Table A.3.3.12-1: DRX.12: DRX cycle = 640 ms and time alignment timer (TAT) = Infinity

## A.3.3.13DRX Configuration X1: DRX cycle = 80 ms and TAT = Infinity

Table A.3.3.13-1: DRX.X1: DRX cycle = 80 ms and time alignment timer (TAT) = Infinity

## A.3.3.14DRX Configuration 14: DRX cycle = 160 ms and TAT = Infinity

Table A.3.3.13-1: DRX.14: DRX cycle = 160 ms and time alignment timer (TAT) = Infinity

## A.3.4Test Cases with Different Channel Bandwidths

## A.3.4.1Test Cases with Different E-UTRA Channel Bandwidths

## A.3.4.1.1Introduction

In annex A test cases involving E-UTRA cell(s) may be defined with different E-UTRA channel bandwidths to verify the same type of RRM requirement.

## A.3.4.1.2Principle of testing

If multiple test cases involving E-UTRA cell(s) are defined with different E-UTRA channel bandwidths to verify the same type of RRM requirement that is E-UTRA channel bandwidth independent, then the UE needs to be tested with only one channel bandwidth in each E-UTRA cell and with the same bandwidth in all the E-UTRA cells used in the test case.

## A.3.5Test Cases for Synchronous and Asynchronous DC Operations

## A.3.5.1EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations

## A.3.5.1.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for EN-DC operation in synchronous and asynchronous scenarios.

In annex A test cases may be defined in both synchronous EN-DC and asynchronous EN-DC scenarios to verify the same type of RRM requirement.

## A.3.5.1.2Principle of Testing

If EN-DC test cases are defined in both synchronous and asynchronous EN-DC scenarios to verify the same type of RRM requirement then the UE capable of both synchronous and asynchronous EN-DC operations needs to be tested with one of the tests in either synchronous or asynchronous EN-DC scenarios.

## A.3.6Antenna configurations

## A.3.6.1Antenna configurations for FR1

Unless otherwise specified, NR FDD or NR TDD cells in all RRM Test cases in AWGN propagation condition are configured with Antenna Configuration 1x2.

## A.3.6.1.1Antenna connection for 4 Rx capable UEs

## A.3.6.1.1.1Introduction

All tests in clause A.4 and A.6 are specified for UEs supporting 2RX. In this clause, the antenna connection method for applying 2RX tests to UEs supporting 4RX antenna ports is specified. No tests are currently specified in clause A.4 or A.6 which are applicable only to 4RX antenna ports, so 4RX capable UEs are always tested by reusing tests which were originally specified for 2RX UEs.

## A.3.6.1.1.2Principle of testing

A.3.6.1.1.2.1Single carrier tests

For 4RX capable UEs supporting at least one band where 2RX is supported and 4RX is not supported, the, all single carrier tests specified in clause A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 2RX is supported and 4RX is not supported with the antenna connection specified in clause A.3.6.1.1.2.4. For single carrier tests specified in clause A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.1.2.4 for bands where 2RX is supported and 4RX is not supported, and the antenna connection specified in clause A.3.6.1.1.2.5 for bands where 4RX is supported.

For 4RX capable UEs which do not support any band where 2RX is supported and 4RX is not supported, all tests specified in clauses A.4 and A.6 shall be tested using the antenna connection specified in clause A.3.6.1.1.2.5. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

Table A.3.6.1.1.2.1-1: Modified parameters for RLM out of sync testing with 4 RX antenna connection

Table A.3.6.1.1.2.1-2: Modified parameters for RLM in sync single carrier testing with 4 RX antenna connection

Table A.3.6.1.1.2.1-3: Modified parameters for Beam Failure Detection and Link Recovery testing with 4 RX antenna connection

A.3.6.1.1.2.2Carrier aggregation tests

All carrier aggregation tests are performed using the antenna connection in clause A.3.6.1.1.2.4 for the PCell antenna connection if the PCell is on a band where 2RX is supported and 4RX is not supported, or using the antenna connection in clause A.3.6.1.1.2.5 for the PCell antenna connection if the PCell is on a band where 4RX is supported.

All carrier aggregation tests are performed using the antenna connection in clause A.3.6.1.1.2.4 for the SCell antenna connection if an SCell is on band where 2RX is supported and 4RX is not supported, or using the antenna connection in clause A.3.6.1.1.2.5 for the SCell antenna connection if an SCell is on a band where 4RX is supported.

A.3.6.1.1.2.3EN-DC tests

All EN-DC tests are performed using the antenna connection in clause A.3.6.1.1.2.6 for the PCell antenna connection if the PCell is on a band where 2RX is supported and 4RX is not supported, or using the antenna connection in clause A.3.6.1.1.2.7 for the PCell antenna connection if the PCell is on a band where 4RX is supported.

All EN-DC tests are performed using the antenna connection in clause A.3.6.1.1.2.4 for the PSCell or SCell antenna connection if an SCell is on band where 2RX is supported and 4RX is not supported, or using antenna connection in clause A.3.6.1.1.2.5 for the SCell antenna connection if an SCell or PSCell is on a band where 4RX is supported.

A.3.6.1.1.2.4Antenna connection for bands where 2RX is supported

For bands where 2RX is supported and 4RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 2 of the 4 Rx ports are connected with data source from system simulator. The remaining 2 RX ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6.1.1.2.5Antenna connection for bands where 4RX is supported

For bands where 4RX is supported, all 4 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds and beam failure detection thresholds described in clauses A.3.6.1.1.2.1, no test parameters or requirements are modified.

A.3.6.1.1.2.6EN-DC LTE Antenna connection for bands where 2RX is supported

For E-UTRAN bands where 2RX is supported and 4RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 2 of the 4 Rx ports are connected with data source from system simulator. The remaining 2 RX ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6.1.1.2.7EN-DC LTE Antenna connection for bands where 4RX is supported

For bands E-UTRAN where 4RX is supported, all 4 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2 of TS 36.133 [15], no test parameters or requirements are modified.

## A.3.6.1.2Antenna connection for 8 Rx capable UEs

## A.3.6.1.2.1Introduction

All tests in clause A.4 and A.6 are specified for UEs supporting 2RX. In this clause, the antenna connection method for applying 2RX tests or 4RX tests to UEs supporting 8RX antenna ports is specified. No tests are currently specified in clause A.4 or A.6 which are applicable only to 8RX antenna ports, so 8RX capable UEs are always tested by reusing tests which were originally specified for 2RX UEs or 4Rx UEs.

## A.3.6.1.2.2Principle of testing

A.3.6.1.2.2.1Single carrier tests

For 8RX capable UEs supporting at least one band where 2RX is supported and either 4RX, 6RX or 8RX is not supported, all single carrier tests specified in clauses A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 2RX is supported and 8RX is not supported with the antenna connection specified in clause A.3.6.1.2.2.4. For single carrier tests specified in clauses A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.2.2.4 for bands where 2RX is supported and 8RX is not supported, and the antenna connection specified in clause A.3.6.1.2.2.6 for bands where 8RX is supported.

For 8RX capable UEs supporting at least one band where 4RX is supported and either 6RX or 8RX is not supported but without supporting any band where only 2RX is supported, all single carrier tests specified in clauses A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 4RX is supported and 8RX is not supported with the antenna connection specified in clause A.3.6.1.2.2.5. For single carrier tests specified in clauses A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.2.2.5 for bands where 4RX is supported and 8RX is not supported, and the antenna connection specified in clause A.3.6.1.2.2.6 for bands where 8RX is supported. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

For 8RX capable UEs supporting at least one band where 6RX is supported and 8RX is not supported but without supporting any band where only 2RX or only 4RX is supported, all single carrier tests specified in clauses A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 6RX is supported and 8RX is not supported with the antenna connection specified in clause A.3.6.1.2.2.5A. For single carrier tests specified in clauses A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.2.2.5A for bands where 6RX is supported and 8RX is not supported, and the antenna connection specified in clause A.3.6.1.2.2.6 for bands where 8RX is supported. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

For 8RX capable UEs which do not support any band where 8RX is not supported, all tests specified in clauses A.4 and A.6 shall be tested using the antenna connection specified in clause A.3.6.1.2.2.6. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

A.3.6.1.2.2.2Carrier aggregation tests

All carrier aggregation tests are performed using the antenna connection in clause A.3.6.1.2.2.4 for the PCell antenna connection if the PCell is on a band where 2RX is supported and either 4RX or 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.5 for the PCell antenna connection if the PCell is on a band where 4RX is supported and 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.6 for the PCell antenna connection if the PCell is on a band where 8RX is supported.

All carrier aggregation tests are performed using the antenna connection in clause A.3.6.1.2.2.4 for the SCell antenna connection if an SCell is on band where 2RX is supported and either 4RX or 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.5 for the SCell antenna connection if an SCell is on a band where 4RX is supported and 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.6 for the SCell antenna connection if an SCell is on a band where 8RX is supported.

A.3.6.1.2.2.3EN-DC tests

All EN-DC tests are performed using the antenna connection in clause A.3.6.1.2.2.7 for the PCell antenna connection if the PCell is on a band where 2RX is supported and either 4RX or 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.8 for the PCell antenna connection if the PCell is on a band where 4RX is supported and 8RX is not supported, or using the antenna connection in clause A.3.6.1.2.2.9 for the PCell antenna connection if the PCell is on a band where 8RX is supported.

All EN-DC tests are performed using the antenna connection in clause A.3.6.1.2.2.4 for the PSCell or SCell antenna connection if an SCell or PSCell is on band where 2RX is supported and either 4RX or 8RX is not supported, or using antenna connection in clause A.3.6.1.2.2.5 for the PSCell or SCell antenna connection if an SCell or PSCell is on a band where 4RX is supported and 8RX is not supported, or using antenna connection in clause A.3.6.1.2.2.6 for the PSCell or SCell antenna connection if an SCell or PSCell is on a band where 8RX is supported.

A.3.6.1.2.2.4Antenna connection for bands where 2RX is supported

For bands where 2RX is supported and either 4RX, 6RX or 8RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 2 of the 8 Rx ports are connected with data source from system simulator. The remaining 6 RX ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6.1.2.2.5Antenna connection for bands where 4RX is supported

For bands where 4RX is supported and either 6RX or 8RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 4 of the 8 Rx ports are connected with data source from system simulator. The remaining 4 RX ports shall be connected with zero input. Except for the modifications to radio link monitoring thresholds and beam failure detection thresholds described in clause A.3.6.1.1.2.1, no test parameters or requirements are modified.

A.3.6.1.2.2.5AAntenna connection for bands where 6RX is supported

For bands where 6RX is supported and 8RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 6 of the 8 Rx ports are connected with data source from system simulator. The remaining 2 RX ports shall be connected with zero input. Except for the modifications to radio link monitoring thresholds and beam failure detection thresholds described in clause A.3.6.1.1.2.1, no test parameters or requirements are modified.

A.3.6.1.2.2.6Antenna connection for bands where 8RX is supported

For bands where 8RX is supported, all 8 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clause A.3.6.1.1.2.1, no test parameters or requirements are modified.

A.3.6.1.2.2.7EN-DC LTE Antenna connection for bands where 2RX is supported

For E-UTRAN bands where 2RX is supported and 4RX or 8RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 2 of the 8 Rx ports are connected with data source from system simulator. The remaining 6 RX ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6.1.2.2.8EN-DC LTE Antenna connection for bands where 4RX is supported

For bands E-UTRAN where 4RX is supported and 8RX is not supported, it is left to the UE declaration and antenna port configuration to decide which 4 of the 8 Rx ports are connected with data source from system simulator. The remaining 4 RX ports shall be connected with zero input. Except for the modifications to radio link monitoring thresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2 of TS 36.133 [15], no test parameters or requirements are modified.

A.3.6.1.2.2.9EN-DC LTE Antenna connection for bands where 8RX is supported

For bands E-UTRAN where 8RX is supported, all 8 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2 of TS 36.133 [15], no test parameters or requirements are modified.

## A.3.6.1.3Antenna connection for 6 Rx capable UEs

## A.3.6.1.3.1Introduction

All tests in clause A.4 and A.6 are specified for UEs supporting 2RX. In this clause, the antenna connection method for applying 2RX tests or 4RX tests to UEs supporting 6Rx antenna ports is specified. No tests are currently specified in clause A.4 or A.6 which are applicable only to 6Rx antenna ports, so 6Rx capable UEs are always tested by reusing tests which were originally specified for 2RX UEs or 4Rx UEs.

## A.3.6.1.3.2Principle of testing

A.3.6.1.3.2.1Single carrier tests

For 6Rx capable UEs supporting at least one band where 2RX is supported and either 4RX or 6Rx is not supported, all single carrier tests specified in clauses A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 2RX is supported and 6Rx is not supported with the antenna connection specified in clause A.3.6.1.3.2.2. For single carrier tests specified in clauses A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.3.2.2 for bands where 2RX is supported and 6Rx is not supported, and the antenna connection specified in clause A.3.6.1.3.2.4 for bands where 6Rx is supported.

For 6Rx capable UEs supporting at least one band where 4RX is supported and 6Rx is not supported but without supporting any band where only 2RX is supported, all single carrier tests specified in clauses A.4 and A.6 except those in clauses A.4.7 and A.6.7 shall be tested on any band where 4RX is supported and 6Rx is not supported with the antenna connection specified in clause A.3.6.1.3.2.3. For single carrier tests specified in clauses A.4.7 or A.6.7, all tests shall be tested with the antenna connection specified in clause A.3.6.1.3.2.3 for bands where 4RX is supported and 6Rx is not supported, and the antenna connection specified in clause A.3.6.1.3.2.4 for bands where 6Rx is supported. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

For 6Rx capable UEs which do not support any band where 6Rx is not supported, all tests specified in clauses A.4 and A.6 shall be tested using the antenna connection specified in clause A.3.6.1.3.2.4. For radio link monitoring tests, the SNR levels are modified according to table A.3.6.1.1.2.1-1 and table A.3.6.1.1.2.1-2. For beam failure detection and link recovery tests, the SNR levels are modified according to table A.3.6.1.1.2.1-3.

A.3.6.1.3.2.2Antenna connection for bands where 2RX is supported

For bands where 2RX is supported and either 4RX or 6Rx is not supported, it is left to the UE declaration and antenna port configuration to decide which 2 of the 6 Rx ports are connected with data source from system simulator. The remaining 6 RX ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6.1.3.2.3Antenna connection for bands where 4RX is supported

For bands where 4RX is supported and 6Rx is not supported, it is left to the UE declaration and antenna port configuration to decide which 4 of the 6 Rx ports are connected with data source from system simulator. The remaining 4 RX ports shall be connected with zero input. Except for the modifications to radio link monitoring thresholds and beam failure detection thresholds described in clause A.3.6.1.1.2.1, no test parameters or requirements are modified.

A.3.6.1.3.2.4Antenna connection for bands where 6Rx is supported

For bands where 6Rx is supported, all 6 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clause A.3.6.1.1.2.1, no test parameters or requirements are modified.

## A.3.6.2Antenna configurations for FR2

Unless otherwise specified, the default Downlink Antenna Configuration for NR FR2 cells is 1x2.

In case of Downlink Antenna Configuration 2x2 for NR FR2 cells, unless otherwise specified, the downlink signal is transmitted over the two polarizations (V and H) of the dual polarized antenna of the test equipment.

In both cases, the downlink signal is received assuming 2 UE baseband receivers. As the UE is tested following the Blackbox Approach with regard to the UE Rx antennas, the exact UE Rx antenna configuration is not relevant for the test configuration and has no impact on the test implementation.

## A.3.6AAntenna configurations with unlicensed bands

## A.3.6A.1Antenna configurations for FR1

Unless otherwise specified, NR unlicensed cells in all RRM Test cases in AWGN propagation condition are configured with Antenna Configuration 1x2.

## A.3.6A.1.1Antenna connection for 4 Rx capable UEs

## A.3.6A.1.1.1Introduction

All tests in clause A.13, A.10, A.11, and A.12 are specified for UEs supporting 2RX. In this clause, the antenna connection method for applying 2RX tests to UEs supporting 4RX antenna ports is specified. No tests are currently specified in clause A.13, A.10, A.11 or A.12 which are applicable only to 4RX antenna ports, so 4RX capable UEs are always tested by reusing tests which were originally specified for 2RX UEs.

## A.3.6A.1.1.2Principle of testing

A.3.6A.1.1.2.1Single carrier tests

For 4RX capable UEs supporting at least one 2RX band, the, all single carrier tests specified in clause A.13. A.10, A.11 and A.12 except those in clauses A.13.4, A.10.5, A.11.6 and A.12.5 shall be tested on any band where 2RX is supported with the antenna connection specified in clause A.3.6A.1.1.2.4. For single carrier tests specified in clauses A.13.4, A.10.5, A.11.6 or A.12.5, all tests shall be tested with the antenna connection specified in clause A.3.6A.1.1.2.4 for bands where 2RX is supported, and the antenna connection specified in clause A.3.6A.1.1.2.5 for bands where 4RX is supported.

For 4RX capable UEs which do not support any 2RX band, all tests specified in clauses A.13, A.10, A.11 and A.12 shall be tested using the antenna connection specified in clause A.3.6A.1.1.2.5. For radio link monitoring tests, the SNR levels are modified according to table A.3.6A.1.1.2.1-1 and table A.3.6A.1.1.2.1-2.

Table A.3.6A.1.1.2.1-1: Modified parameters for RLM out of sync testing with 4 RX antenna connection

Table A.3.6A.1.1.2.1-2: Modified parameters for RLM in sync single carrier testing with 4 RX antenna connection

Table A.3.6A.1.1.2.1-3: Modified parameters for Beam Failure Detection and Link Recovery testing with 4 RX antenna connection

A.3.6A.1.1.2.2Carrier aggregation tests

All carrier aggregation tests are performed using the antenna connection in clause A.3.6A.1.1.2.4 for the PCell antenna connection if the PCell is on a band where 2RX is supported or the antenna connection in clause A.3.6A.1.1.2.5 for the PCell antenna connection if the PCell is on a band where 4RX is supported.

All carrier aggregation tests are performed using the antenna connection in clause A.3.6A.1.1.2.4 for the SCell antenna connection if an SCell is on band where 2RX is supported or the testing procedure in clause A.3.6A.1.1.2.5 for the SCell antenna connection if an SCell is on a band where 4RX is supported.

A.3.6A.1.1.2.3EN-DC tests

All carrier aggregation tests are performed using the antenna connection in clause A.3.6A.1.1.2.6 for the PCell antenna connection if the PCell is on a band where 2RX is supported or the antenna connection in clause A.3.6A.1.1.2.7 for the PCell antenna connection if the PCell is on a band where 4RX is supported.

All carrier aggregation tests are performed using the antenna connection in clause A.3.6A.1.1.2.4 for the PSCell or SCell antenna connection if an SCell is on band where 2RX is supported or the testing procedure in clause A.3.6A.1.1.2.5 for the SCell antenna connection if an SCell or PSCell is on a band where 4RX is supported.

A.3.6A.1.1.2.4Antenna connection for bands where 2RX is supported

For bands where 2RX is supported, it is left to the UE declaration and AP configuration to decide which 2 of the 4 Rx ports are connected with data source from system simulator. The remaining 2 Rx ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6A.1.1.2.5Antenna connection for bands where 4RX is supported

For bands where 4RX is supported, all 4 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clauses A.3.6A.1.1.2.1 and A.3.6A.1.1.2.2, no test parameters or requirements are modified.

A.3.6A.1.1.2.6EN-DC LTE Antenna connection for bands where 2RX is supported

For bands where LTE 2RX is supported, it is left to the UE declaration and AP configuration to decide which 2 of the 4 Rx ports are connected with data source from system simulator. The remaining 2 Rx ports shall be connected with zero input. No test parameters or requirements are modified.

A.3.6A.1.1.2.7EN-DC LTE Antenna connection for bands where 4RX is supported

For bands where LTE 4RX is supported, all 4 RX antennas are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring thresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2 of TS 36.133 [15], no test parameters or requirements are modified.

## A.3.7EN-DC test setup

## A.3.7.1Introduction

## A.3.7.2E-UTRAN Serving Cell Parameters

## A.3.7.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1

table A.3.7.2.1-1 defines cell specific test parameters for E-UTRAN cell which can be used in EN-DC test cases or in any test case comprising at least one E-UTRA serving cell with all NR cells in FR1. Unless otherwise stated within the test, all measurements in annex A.4 and A.5 are performed only on the NR carrier. The E-UTRA serving cell shall configured to not interfere with NR operation and the E-UTRA serving cell signal power shall not be critical to the test purpose.

Table A.3.7.2.1-1: E-UTRAN cell specific test parameters for tests with all NR cells in FR1

## A.3.7.2.2E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2

table A.3.7.2.2-1 defines cell specific test parameters for E-UTRAN cell which can be used in EN-DC test cases or in any test case comprising at least one E-UTRA serving cell with one or more NR cells in FR2.

Table A.3.7.2.2-1: E-UTRAN cell specific test parameters for tests with one or more NR cells in FR2

## A.3.7ANR FR1-FR2 test setup

Some Test cases in clause A.7 have NR cells in both FR1 and FR2. Unless otherwise stated within the test, the NR FR1 Cell signal is required only to provide a link to the UE under test. The Test System shall provide a stable and noise-free NR FR1 signal without need of precise propagation modelling, path loss and polarization control. Further details of the NR FR1 signal configuration are not defined as part of the cell specific test parameters, since the NR FR1 link is not under performance verification and shall not affect the test result unless otherwise specifically stated in the test case.

## A.3.7BEN-DC test setup with unlicensed bands

## A.3.7B.1Introduction

## A.3.7B.2E-UTRAN Serving Cell Parameters

## A.3.7B.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR1

table A.3.7A.2.1-1 defines cell specific test parameters for E-UTRAN cell which can be used in EN-DC test cases or in any test case comprising at least one E-UTRA serving cell with all NR cells under CCA in FR1. Unless otherwise stated within the test, all measurements in annex A.4 and A.5 are performed only on the unlicensed NR carrier. The E-UTRA serving cell shall configured to not interfere with NR operation and the E-UTRA serving cell signal power shall not be critical to the test purpose.

Table A.3.7B.2.1-1: E-UTRAN cell specific test parameters for tests with all NR cells user CCA in FR1

## A.3.7CLTE-FR1/FR2 test setup

Some Test cases in clause A.5 have LTE and FR2 NR cells. Unless otherwise stated within the test, the LTE Cell signal is required only to provide a link to the UE under test. The Test System shall provide a stable and noise-free LTE signal without need of precise propagation modelling, path loss and polarization control. Further details of the LTE signal configuration are not defined as part of the cell specific test parameters, since the LTE link is not under performance verification and shall not affect the test result unless otherwise specifically stated in the test case.

## A.3.7DNE-DC test setup

## A.3.7D.1Introduction

## A.3.7D.2E-UTRAN Serving Cell Parameters

## A.3.7D.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1

The parameters are same as specified in clause A.3.7.2.1.

## A.3.7D.2.2E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2

The parameters are same as specified in clause A.3.7.2.2.

## A.3.8PRACH configurations

## A.3.8.1Introduction

This clause provides the typical PRACH configurations used for RRM test cases defined in annex A. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.8.2PRACH configurations in FR1

## A.3.8.2.1FR1 PRACH configuration 1

FR1 PRACH configuration 1 in this clause provides the typical PRACH configuration for SSB-based contention based random access in FR1.

Table A.3.8.2.1-1: Parameters for FR1 PRACH configuration 1

## A.3.8.2.2FR1 PRACH configuration 2

FR1 PRACH configuration 2 in this clause provides the typical PRACH configuration for SSB based non-contention based random access in FR1.

Table A.3.8.2.2-1: Parameters for FR1 PRACH configuration 2

## A.3.8.2.3FR1 PRACH configuration 3

FR1 PRACH configuration 3 in this clause provides the typical PRACH configuration for CSI-RS based non-contention based random access in FR1.

Table A.3.8.2.3-1: Parameters for FR1 PRACH configuration 3

## A.3.8.2.4FR1 PRACH configuration 4

FR1 PRACH configuration 4 in this clause provides the PRACH configuration for CSI-RS based non-contention based random access in FR1 to convey BFR.

Table A.3.8.2.4-1: Parameters for FR1 PRACH configuration 4

## A.3.8.2.5FR1 PRACH configuration 5

FR1 PRACH configuration 5 in this clause provides the typical PRACH configuration for LTM early UL synchronization on candidate cell in FR1.

Table A.3.8.2.5-1: Parameters for FR1 PRACH configuration 5

## A.3.8.2.6FR1 PRACH configuration 6

FR1 PRACH configuration 6 in this clause provides the typical PRACH configuration for SSB-based contention free random access in FR1.

Table A.3.8.2.6-1: Parameters for FR1 PRACH configuration 6

## A.3.8.3PRACH configurations in FR2

## A.3.8.3.1FR2 PRACH configuration 1

FR2 PRACH configuration 1 in this clause provides the typical PRACH configuration for SSB-based contention based random access in FR2.

Table A.3.8.3.1-1: Parameters for FR2 PRACH configuration 1

## A.3.8.3.2FR2 PRACH configuration 2

FR2 PRACH configuration 2 in this clause provides the typical PRACH configuration for SSB based non-contention based random access in FR2.

Table A.3.8.3.2-1: Parameters for FR2 PRACH configuration 2

## A.3.8.3.3FR2 PRACH configuration 3

FR2 PRACH configuration 3 in this clause provides the typical PRACH configuration for CSI-RS based non-contention based random access in FR2.

## A.3.8.3.4FR2 PRACH configuration 4

FR2 PRACH configuration 4 in this clause provides the PRACH configuration for CSI-RS based non-contention based random access in FR2 to convey BFR.

Table A.3.8.3.4-1: Parameters for FR2 PRACH configuration 4

## A.3.8.3.5FR2 PRACH configuration 5

FR2 PRACH configuration 5 in this clause provides the typical PRACH configuration for LTM early UL synchronization on candidate cell in FR2.

Table A.3.8.3.5-1: Parameters for FR2 PRACH configuration 5

## A.3.8.3.6FR2 PRACH configuration 6

FR2 PRACH configuration 6 in this clause provides the typical PRACH configuration for SSB-based contention free random access in FR2.

Table A.3.8.3.6-1: Parameters for FR2 PRACH configuration 6

## A.3.8APRACH configurations under CCA

## A.3.8A.1Introduction

This clause provides the typical PRACH configurations used for RRM test cases defined in annex A. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.8A.2PRACH configurations in FR1

## A.3.8A.2.1FR1 PRACH configuration 1 under CCA

FR1 PRACH configuration 1 under CCA in this clause provides the typical PRACH configuration for SSB-based contention based random access in FR1.

Table A.3.8A.2.1-1: Parameters for FR1 PRACH configuration 1 under CCA

## A.3.8A.2.2FR1 PRACH configuration 2 under CCA

FR1 PRACH configuration 2 under CCA in this clause provides the typical PRACH configuration for SSB based non-contention based random access in FR1.

Table A.3.8A.2.2-1: Parameters for FR1 PRACH configuration 2 under CCA

## A.3.9BWP configurations

## A.3.9.1Introduction

This clause provides the typical BWP configurations used for RRM test cases defined in annex A. For downlink BWP, both initial BWP and dedicated BWP configurations are specified in clause A.3.9.2 and for uplink BWP, both initial BWP and dedicated BWP configurations are specified in clause A.3.9.3. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.9.2Downlink BWP configurations

## A.3.9.2.1Initial BWP

Table A.3.9.2.1-1: Downlink BWP patterns for initial BWP configuration

## A.3.9.2.2Dedicated BWP

Table A.3.9.2.2-1: Downlink BWP patterns for dedicated BWP configuration

## A.3.9.3Uplink BWP configurations

## A.3.9.3.1Initial BWP

Table A.3.9.3.1-1: Uplink BWP patterns for initial BWP configuration

## A.3.9.3.2Dedicated BWP

Table A.3.9.3.2-1: Uplink BWP patterns for dedicated BWP configuration

## A.3.9ABWP configurations for RedCap

## A.3.9A.1Introduction

This clause provides the typical BWP configurations used for RedCap RRM test cases defined in annex A. For downlink BWP, RedCap dedicated BWP configurations are specified in clause A.3.9A.2 and for uplink BWP, RedCap dedicated BWP configurations are specified in clause A.3.9A.3. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.9A.2Downlink BWP configurations

## A.3.9A.2.1Dedicated BWP

Table A.3.9A.2.2-1: Downlink BWP patterns for RedCap dedicated BWP configuration

## A.3.9A.3Uplink BWP configurations

## A.3.9A.3.1Dedicated BWP

Table A.3.9A.3.1-1: Uplink BWP patterns for RedCap dedicated BWP configuration

## A.3.10SSB Configurations

## A.3.10.1SSB Configurations for FR1

## A.3.10.1.1SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.1-1: SSB.1 FR1: SSB Pattern 1 for SSB SCS=15 kHz in 10 MHz channel

A.3.10.1.2SSB pattern 2 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.2-1: SSB.2 FR1: SSB Pattern 2 for SSB SCS=30 kHz in 40 MHz channel

A.3.10.1.3SSB pattern 3 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.3-1: SSB.3 FR1: SSB Pattern 3 for SSB SCS=15 kHz in 10 MHz channel

A.3.10.1.4SSB pattern 4 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.4-1: SSB.4 FR1: SSB Pattern 4 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.5SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz

Table A.3.10.1.5-1: SSB.5 FR1: SSB Pattern 5 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.6SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40 MHz

Table A.3.10.1.6-1: SSB.6 FR1: SSB Pattern 6 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.7SSB pattern 7 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.7-1: SSB.7 FR1: SSB Pattern 7 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.8SSB pattern 8 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.8-1: SSB.8 FR1: SSB Pattern 8 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.9SSB pattern 9 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.9-1: SSB.9 FR1: SSB Pattern 9 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.10SSB pattern 10 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.10-1: SSB.10 FR1: SSB Pattern 10 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.11SSB pattern 11 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.11-1: SSB.11 FR1: SSB Pattern 11 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.12SSB pattern 12 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.12-1: SSB.12 FR1: SSB Pattern 12 for SSB SCS=30 kHz in 20 MHz channel

## A.3.10.1.13SSB pattern 13 in FR1: SSB allocation for SSB SCS=15 kHz in 3 MHz

Table A.3.10.1.13-1: SSB.13 FR1: SSB Pattern 1 for SSB SCS=15 kHz in 3 MHz channel

## A.3.10.1.14SSB pattern 14 in FR1: SSB allocation for SSB SCS=15 kHz with 160 ms periodicity in 10MHz

Table A.3.10.1.14-1: SSB.14 FR1: SSB Pattern 14 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.15SSB pattern 15 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.15-1: SSB.15 FR1: SSB Pattern 15 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.16SSB pattern 16 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.16-1: SSB.16 FR1: SSB Pattern 16 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.17SSB pattern 17 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.17-1: SSB.17 FR1: SSB Pattern 17 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.18SSB pattern 18 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.18-1: SSB.18 FR1: SSB Pattern 18 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.19SSB pattern 19 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.19-1: SSB.10 FR1: SSB Pattern 19 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.20SSB pattern 20 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.20-1: SSB.20 FR1: SSB Pattern 20 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.21SSB pattern 21 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.21-1: SSB.21 FR1: SSB Pattern 21 for SSB SCS=15 kHz in 10 MHz channel

A.3.10.1.22SSB pattern 22 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.22-1: SSB.22 FR1: SSB Pattern 22 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10.1.23SSB pattern 23 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10.1.23-1: SSB.23 FR1: SSB Pattern 23 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10.1.24SSB pattern 24 in FR1: SSB allocation for SSB SCS=30 kHz in 100 MHz

Table A.3.10.1.24-1: SSB.24 FR1: SSB Pattern 24 for SSB SCS=30 kHz in 100 MHz channel

## A.3.10.2SSB Configurations for FR2

## A.3.10.2.1SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.1-1: SSB.1 FR2: SSB Pattern 1 for SSB SCS = 120 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.2SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.2-1: SSB.2 FR2: SSB Pattern 2 for SSB SCS = 240 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.3SSB pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.3-1: SSB.3 FR2: SSB Pattern 3 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.4SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.4-1: SSB.4 FR2: SSB Pattern 4 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.5SSB pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.5-1: SSB.5 FR2: SSB Pattern 5 for SSB SCS = 120 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.6SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.6-1: SSB.6 FR2: SSB Pattern 6 for SSB SCS = 240 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.7SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.7-1: SSB.7 FR2: SSB Pattern 7 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.8SSB pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.8-1: SSB.8 FR2: SSB Pattern 8 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.9SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.9-1: SSB.9 FR2: SSB Pattern 9 for SSB SCS = 120 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.10SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.10-1: SSB.10 FR2: SSB Pattern 10 for SSB SCS = 240 kHz in 100 MHz channel with 2 SSBs per SS-burst

A.3.10.2.11SSB pattern 11 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz

Table A.3.10.2.11-1: SSB.11 FR2: SSB Pattern 11 for SSB SCS = 480 kHz in 400 MHz channel with 2 SSBs per SS-burst

A.3.10.2.12SSB pattern 12 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz

Table A.3.10.2.12-1: SSB.12 FR2: SSB Pattern 12 for SSB SCS = 960 kHz in 400 MHz channel with 2 SSBs per SS-burst

A.3.10.2.13SSB pattern 13 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz

Table A.3.10.2.13-1: SSB.13 FR2: SSB Pattern 13 for SSB SCS = 480 kHz in 400 MHz channel with 1 SSB per SS-burst

A.3.10.2.14SSB pattern 14 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz

Table A.3.10.2.14-1: SSB.14 FR2: SSB Pattern 14 for SSB SCS = 960 kHz in 400 MHz channel with 1 SSB per SS-burst

A.3.10.2.15SSB pattern 15 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz

Table A.3.10.2.15-1: SSB.15 FR2: SSB Pattern 15 for SSB SCS = 480 kHz in 400 MHz channel with 2 SSBs per SS-burst

A.3.10.2.16SSB pattern 16 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz

Table A.3.10.2.16-1: SSB.16 FR2: SSB Pattern 16 for SSB SCS = 960 kHz in 400 MHz channel with 2 SSBs per SS-burst

A.3.10.2.17SSB pattern 17 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz

Table A.3.10.2.17-1: SSB.17 FR2: SSB Pattern 17 for SSB SCS = 480 kHz in 400 MHz channel with 1 SSB per SS-burst

A.3.10.2.18SSB pattern 18 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz

Table A.3.10.2.18-1: SSB.18 FR2: SSB Pattern 18 for SSB SCS = 960 kHz in 400 MHz channel with 1 SSB per SS-burst

## A.3.10.2.19SSB pattern 19 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10B.2.2-1: SSB.19 FR2: SSB Pattern 17 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.20SSB pattern 20 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.20-1: SSB.20 FR2: SSB Pattern 18 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.21SSB pattern 21 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.21-1: SSB.21 FR2: SSB Pattern 19 for SSB SCS = 120 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.22SSB pattern 22 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.22-1: SSB.22 FR2: SSB Pattern 20 for SSB SCS = 240 kHz in 100 MHz channel with 2 SSBs per SS-burst

## A.3.10.2.23SSB pattern 23 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.23-1: SSB.23 FR2: SSB Pattern 21 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.24SSB pattern 24 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.24-1: SSB.24 FR2: SSB Pattern 22 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.25SSB pattern 25 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.25-1: SSB.25 FR2: SSB Pattern 17 for SSB SCS = 120 kHz in 100 MHz channel with 3 SSBs per SS-burst

## A.3.10.2.26SSB pattern 26 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.26-1: SSB.26 FR2: SSB Pattern 26 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.27SSB pattern 27 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.27-1: SSB. 27 FR2: SSB Pattern 27 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.28SSB pattern 28 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.28-1: SSB.28 FR2: SSB Pattern 28 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.29SSB pattern 29 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.29-1: SSB.29 FR2: SSB Pattern 29 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.30SSB pattern 30 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10.2.30-1: SSB.30 FR2: SSB Pattern 30 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.31SSB pattern 31 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.31-1: SSB.31 FR2: SSB Pattern 31 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.32SSB pattern 32 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.32-1: SSB.32 FR2: SSB Pattern 32 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.33SSB pattern 33 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10.2.33-1: SSB.33 FR2: SSB Pattern 33 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10.2.34SSB pattern 34 in FR2: SSB allocation for SSB SCS=120 kHz in 200 MHz

Table A.3.10.2.34-1: SSB.34 FR2: SSB Pattern 34 for SSB SCS = 120 kHz in 200 MHz channel with 2 SSBs per SS-burst

## A.3.10ASSB Configurations under CCA

## A.3.10A.1SSB Configurations under CCA for FR1

## A.3.10A.1.1SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10A.1.1-1: SSB.1 CCA: SSB Pattern 1 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10A.1.2SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10A.1.2-1: SSB.2 CCA: SSB Pattern 2 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10A.1.3SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.3-1: SSB.3 CCA: SSB Pattern 3 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10A.1.4SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz

Table A.3.10.1.4-1: SSB.4 CCA: SSB Pattern 4 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10BSSB Configurations for RedCap

## A.3.10B.1SSB Configurations for FR1

## A.3.10B.1.1SSB pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz

Table A.3.10B.1.1-1: SSB.1 RedCap FR1: SSB Pattern 1 for SSB SCS=30 kHz in 20 MHz channel

## A.3.10B.1.2SSB pattern 2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz

Table A.3.10B.1.2-1: SSB.2 RedCap FR1: SSB Pattern 2 for SSB SCS=30 kHz in 20 MHz channel

## A.3.10B.1.3SSB pattern 3 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz

Table A.3.10B.1.3-1: SSB.3 RedCap FR1: SSB Pattern 3 for SSB SCS=30 kHz in 20 MHz channel

## A.3.10B.1.4SSB pattern 4 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10B.1.4-1: SSB.4 RedCap FR1: SSB Pattern 4 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10B.1.5SSB pattern 5 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz

Table A.3.10B.1.5-1: SSB.5 RedCap FR1: SSB Pattern 5 for SSB SCS=30 kHz in 20 MHz channel

## A.3.10B.1.6SSB pattern 6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz

Table A.3.10B.1.6-1: SSB.6 RedCap FR1: SSB Pattern 6 for SSB SCS=15 kHz in 10 MHz channel

## A.3.10B.1.7SSB pattern 7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz

Table A.3.10B.1.7-1: SSB.7 RedCap FR1: SSB Pattern 7 for SSB SCS=30 kHz in 40 MHz channel

## A.3.10B.2SSB Configurations for FR2

## A.3.10B.2.1SSB pattern 1 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10B.2.1-1: SSB.1 RedCap FR2: SSB Pattern 1 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10B.2.2SSB pattern 2 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10B.2.2-1: SSB.2 RedCap FR2: SSB Pattern 2 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10B.2.3SSB pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz

Table A.3.10B.2.3-1: SSB.3 RedCap FR2: SSB Pattern 3 for SSB SCS = 120 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10B.2.4SSB pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10B.2.4-1: SSB.4 RedCap FR2: SSB Pattern 4 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.10B.2.5SSB pattern 5 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz

Table A.3.10B.2.5-1: SSB.5 RedCap FR2: SSB Pattern 5 for SSB SCS = 240 kHz in 100 MHz channel with 1 SSB per SS-burst

## A.3.11SMTC Configurations

## A.3.11.1SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms

Table A.3.11.1-1: SMTC.1: SMTC Pattern 1 for SMTC period = 20 ms and duration = 1 ms

## A.3.11.2SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms

Table A.3.11.2-1: SMTC.2: SMTC Pattern 2 for SMTC period = 20 ms and duration = 5 ms

## A.3.11.3SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms

Table A.3.11.3-1: SMTC.3: SMTC Pattern 3 for SMTC period = 160 ms and duration = 1 ms

## A.3.11.4SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms

Table A.3.11.4-1: SMTC.4: SMTC Pattern 4 for SMTC period = 20 ms and duration = 1 ms

## A.3.11.5SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms

Table A.3.11.5-1: SMTC.5: SMTC Pattern 5 for SMTC period = 20 ms and duration = 5 ms

## A.3.11.6SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms

Table A.3.11.6-1: SMTC.6: SMTC Pattern 6 for SMTC period = 20 ms and duration = 5 ms

## A.3.11.7SMTC pattern 7: SMTC period = 20 ms with SMTC duration = 5 ms

Table A.3.11.7-1: SMTC.7: SMTC Pattern 7 for SMTC period = 20 ms and duration = 5 ms

## A.3.11.8SMTC pattern 8: SMTC period = 10 ms with SMTC duration = 1 ms

Table A.3.11.8-1: SMTC.8: SMTC Pattern 8 for SMTC period = 10 ms and duration = 1 ms

## A.3.11.9SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms

Table A.3.11.9-1: SMTC.9: SMTC Pattern 6 for SMTC period = 20 ms and duration = 1 ms

## A.3.11.10SMTC pattern 10: SMTC period = 80 ms with SMTC duration = 1 ms

Table A.3.11.10-1: SMTC.10: SMTC Pattern 10 for SMTC period = 80 ms and duration = 1 ms

## A.3.11.11SMTC pattern 11: SMTC period = 80 ms with SMTC duration = 5 ms

Table A.3.11.11-1: SMTC.11: SMTC Pattern 11 for SMTC period = 80 ms and duration = 5 ms

## A.3.11.12SMTC pattern 12: SMTC period = 20 ms with SMTC duration = 5 ms

Table A.3.11.12-1: SMTC.12: SMTC Pattern 12 for SMTC period = 20 ms and duration = 4 ms

## A.3.11.13SMTC pattern 13: SMTC period = 160 ms with SMTC duration = 1 ms

Table A.3.11.13-1: SMTC.13: SMTC Pattern 13 for SMTC period = 160 ms and duration = 1 ms

## A.3.11.14SMTC pattern 14: SMTC period = 20 ms with SMTC duration = 1 ms

Table A.3.11.14-1: SMTC.14: SMTC Pattern 14 for SMTC period = 20 ms and duration = 1 ms

## A.3.11ASMTC Configurations for RedCap

## A.3.11A.0Introduction

The SMTC configuration for RedCap can also be used in test case for non-RedCap.

## A.3.11A.1SMTC pattern 1 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms

Table A.3.11A.1-1: SMTC.1 RedCap: SMTC Pattern 1 for SMTC period = 40 ms and duration = 1 ms

## A.3.11A.2SMTC pattern 2 for RedCap: SMTC period = 80 ms with SMTC duration = 1 ms

Table A.3.11A.2-1: SMTC.2 RedCap: SMTC Pattern 2 for SMTC period = 80 ms and duration = 1 ms

## A.3.11A.3SMTC pattern 3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms

Table A.3.11A.3-1: SMTC.3 RedCap: SMTC Pattern 3 for SMTC period = 40 ms and duration = 1 ms

## A.3.11A.4SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms

Table A.3.11A.4-1: SMTC.4 RedCap: SMTC Pattern 4 for SMTC period = 80 ms and duration = 5 ms

## A.3.12Test Cases with Different CC Configurations

## A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations

## A.3.12.1.1Introduction

In annex A EN-DC test cases may be defined for two component carriers (CCs) as well as for more than two CCs to verify the same RRM requirement.

## A.3.12.1.2Principle of testing

If multiple EN-DC test cases are defined for two CCs as well as for more than two CCs to verify the same type of RRM requirement, which depends on the number of CCs, then from the UE performance point of view the test coverage can be considered fulfilled by executing only the EN-DC test cases with the maximum number of CCs in EN-DC supported by the UE. Otherwise, if the same type of RRM requirement is independent of the number of CCs then from the UE performance point of view the test coverage can be considered fulfilled by executing only the EN-DC test cases with two CCs in EN-DC supported by the UE.

NOTE: The maximum number of CCs that can be used in FR2 tests in EN-DC would depend on the test equipment capability.

## A.3.12.2Carrier Aggregation Test Cases with Different CA Configurations

## A.3.12.2.1Introduction

In annex A carrier aggregation test cases may be defined for two CCs as well as for more than two CCs to verify the same RRM requirement.

## A.3.12.2.2Principle of testing

If multiple carrier aggregation test cases are defined for two CCs as well as for more than two CCs to verify the same RRM requirement, which depends on the number of CCs, then from the UE performance point of view the test coverage can be considered fulfilled by executing only the CA test cases with the maximum number of CCs in CA supported by the UE. Otherwise if the same type of RRM requirement is independent of the number of CCs then from the UE performance point of view the test coverage can be considered fulfilled by executing only the CA test cases with at least two CCs in CA supported by the UE.

NOTE: The maximum number of CCs that can be used in FR2 tests in CA would depend on the test equipment capability.

## A.3.13Test Cases in SA and EN-DC Operations

## A.3.13.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements in standalone (SA) or EN-DC operations.

In annex A test cases may be defined in SA and EN-DC operations to verify the same RRM requirement.

## A.3.13.2Principle of Testing

If test cases are defined in both SA and EN-DC operations to verify the same RRM requirement then the UE capable of both SA and EN-DC operations needs to verify that RRM requirement by performing test case(s) in either SA operation or in EN-DC operation.

If test cases are defined in both SA and EN-DC operations to verify at least one common RRM requirement then the UE capable of both SA and EN-DC operations needs to verify RRM requirements by performing test case(s) in either SA operation or in EN-DC operation provided that the performed test case(s):

-verifies the largest number of RRM requirements and

-verifies at least all RRM requirements covered in the test case(s), which is not performed.

A.3.13AVoid

A.3.13A.1Void

A.3.13A.2Void

Table A.3.13A.2-1: Void

A.3.13A.3Void

Table A.3.13A.3-1: Void

A.3.13A.4Void

Table A.3.13A.4-1: Void

A.3.13A.5Void

Table A.3.13A.5-1: Void

## A.3.13BTest Cases for EN-DC and NE-DC Operations

## A.3.13B.1Active BWP switch Test Cases for EN-DC and NE-DC Operations

## A.3.13B.1.1Introduction

This clause defines a principle which is applicable to test cases verifying active BWP switch requirements for EN-DC operation and NE-DC operations.

In annex A test cases are defined for both EN-DC and NE-DC operations to verify the same type of RRM requirement.

## A.3.13B.1.2Principle of Testing

UE capable of both EN-DC and NE-DC operations needs to be tested with one of the tests in either EN-DC or NE-DC operations.

## A.3.13B.2SFTD accuracy Test Cases for EN-DC and NE-DC Operations

## A.3.13B.2.1Introduction

This clause defines a principle which is applicable to test cases verifying SFTD accuracy requirements for EN-DC operation and NE-DC operations.

In annex A test cases are defined for both EN-DC and NE-DC operations to verify the same type of RRM requirement.

## A.3.13B.2.2Principle of Testing

UE capable of both EN-DC and NE-DC operations needs to be tested with one of the tests in either EN-DC or NE-DC operations.

## A.3.14CSI-RS configurations

## A.3.14.1FDD

Table A.3.14.1-1: CSI-RS Reference Measurement Channels for SCS=15 kHz

Table A.3.14.1-2: CSI-RS Reference Measurement Channels for SCS=120 kHz

## A.3.14.2TDD

Table A.3.14.2-1: CSI-RS Reference Measurement Channels for SCS=15 kHz

Table A.3.14.2-1A: CSI-RS Reference Measurement Channels for SCS=15 kHz

Table A.3.14.2-2: CSI-RS Reference Measurement Channels for SCS=30 kHz

Table A.3.14.2-2A: CSI-RS Reference Measurement Channels for SCS=30 kHz

Table A.3.14.2-3: CSI-RS Reference Measurement Channels for SCS=120 kHz

Table A.3.14.2-3A: CSI-RS Reference Measurement Channels for SCS=120 kHz

## A.3.15Angle of Arrival (AoA) for FR2 RRM test cases

This clause specifies the AoA setups for FR2 RRM test cases in clause A.5 and A.7. The applicable AoA setup is defined in each test case in clause A.5 and A.7.

## A.3.15.1Setup 1: Single AoA in Rx beam peak direction

There is only one active probe in the test. The DL signals, and noise if applicable, transmitted from the probe, are aligned to the UE Rx beam peak direction (as defined in TS 38.101-2 [19]).

## A.3.15.2Setup 2: Single AoA in non Rx beam peak direction

## A.3.15.2.1Setup 2a: Single AoA in non Rx beam peak direction without change in direction

There is only one active probe in the test. The DL signals, and noise if applicable, transmitted from the probe, align to a direction (AoA) which is from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class. The direction (AoA) of the signals shall not be changed between test iterations.

## A.3.15.2.2Setup 2b: Single AoA in non Rx beam peak direction with change in direction

There is only one active probe in the test. The DL signals, and noise if applicable, transmitted from the probe, align to a direction (AoA) which is from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class. For UE power class 3, the direction (AoA) of the signals shall be changed for each test iteration.

## A.3.15.3Setup 3: 2 AoAs

There are 2 active probes in the test. The DL signals, and noise if applicable, transmitted from the two active probes, align to directions (AoAs) which are from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class. The relative angular offset between the directions (AoAs) of the 2 active probes, shall be changed for each test iteration. The applicable set of relative angular offsets between the 2 active probes is given in table 3.15.3-1 for each UE power class.

Table A.3.15.3-1: Set of relative angular offsets between active probes for each power class

## A.3.15.4Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak

## A.3.15.4.1Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction

There are 2 active probes in the test. The DL signals, and noise if applicable, are transmitted from the two active probes. One probe is aligned to the UE Rx beam peak direction as defined in TS 38.101-2 [19]. The second is aligned to a direction (AoA) which is from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class. The direction (AoA) of the non Rx beam peak signal shall not be changed between test iterations.

## A.3.15.4.2Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction

There are 2 active probes in the test. The DL signals, and noise if applicable, are transmitted from the two active probes. One probe is aligned to the UE Rx beam peak direction as defined in TS 38.101-2 [19]. The second is aligned to a direction (AoA) which is from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class.

For UE power class 3, the relative angular offset between the directions (AoAs) of the 2 active probes shall be changed for each test iteration, within the probe alignment described above. The applicable set of relative angular offsets between the 2 active probes is given in table 3.15.3-1 for each UE power class.

## A.3.15.4.3Setup 4c: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak for power class 6 UE supporting simultaneous reception from multiple directions

There are 2 active probes in the test. The DL signals, and noise if applicable, are transmitted from the two active probes. One probe is aligned to the UE Rx beam peak direction as defined in TS 38.101-2 [19]. The second is aligned to a direction (AoA) which is from the set of directions corresponding to the 2AoA spherical coverage requirement for simultaneous reception from multiple directions as defined in clause 7.3K.6 of TS 38.101-2 [19] for power class 6.

For power class 6 supporting simultaneous reception from multiple directions, the angular separation between the directions (AoAs) of the 2 active probes is 150°, and the direction (AoA) of the non Rx beam peak signal shall not be changed between test iterations.

## A.3.15.5Setup 5: 2 AoAs for simultaneous reception with QCL Type-D

There are 2 active probes in the test. The DL signals, and noise if applicable, are transmitted from the two active probes.  The 2 AoAs (AoA1 and AoA2) for simultaneous reception with different QCL-typeD are from the set of AoA pairs, denoted by (AoA1, AoA2) that can support 2 AoA reception for UE declared AoA angular separation and declared orientation in the positioner of the test system according to the spherical coverage requirement for simultaneous reception from multiple directions as defined in clause 7.3K.3 of TS 38.101-2 [19] for UE power class 3 supporting simultaneous reception from multiple directions. The angular separation between the directions (AoA1 and AoA2) of the 2 active probes is declared from table 7.3K.3-1 in clause 7.3K.3 of TS 38.101-2 [19] and shall not be changed for each test iteration.

AoA1 needs to satisfy the spherical coverage requirement in table 7.3.4.3-1 of TS 38.101-2 [19].

NOTE: The chosen AoA pair (AoA1, AoA2) is up to RAN5.

## A.3.15.6Setup 6: 3 AoAs for simultaneous reception with different QCL Type-D

There are 3 active probes in the test and the DL signals and noise are transmitted from the three active probes.

Out of the three AoAs, one AoA (AoA1) is aligned to a direction which is from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for UE power class 3 and other 2 AoAs (AoA2 and AoA3) are from the set of AoA pairs, denoted by (AoA2, AoA3) that can support 2 AoA reception for UE declared AoA angular separation and declared orientation in the positioner of the test system according to the spherical coverage requirement for simultaneous reception from multiple directions as defined in clause 7.3K.3 of TS 38.101-2 [19] for power class 3 supporting simultaneous reception from multiple directions. The UE positioning shall be such that the UE passes both spherical coverage requirements.

The angular offset between the directions of the AoA pair (AoA2, AoA3) is declared from table 7.3K.3-1 in clause 7.3K.3 of TS 38.101-2 [19] and shall not be changed for each test iteration.

NOTE: The chosen AoA pair (AoA2, AoA3) is up to RAN5.

## A.3.15.7Setup 7: 3 AoAs

There are 3 active probes in the test. The DL signals, and noise if applicable, transmitted from the three active probes, align to directions (AoAs) which are from the set of directions corresponding to the EIS spherical coverage percentile of the DUT as defined in clause 7.3.4 of TS 38.101-2 [19] for each UE power class. The relative angular offset between the directions (AoAs) of the 3 active probes, shall be changed for each test iteration. Any combinations of two relative angular offsets between 2 active probes specified in table A.3.15.3-1, is considered as a valid applicable relative angular offsets between 3 active probes for the respective power class.

## A.3.15.8Setup 8: 4 AoAs

There are 4 active probes in the test, placed in single plane (xz plane). The DL signals, and noise if applicable, are transmitted from the four active probes. The relative angular offset between the directions (AoAs) of the 4 active probes is 30, 60 and 60 degrees between neighboring probes.

Note: The deployment of this 4 AoAs setup is assumed to be done using the Indirect Far Field (IFF) FR2 method.

## A.3.15CAngle of Arrival (AoA) for FR2-NTN RRM test cases

This clause specifies the AoA setups for FR2-NTN RRM test cases in clause A.14. The applicable AoA setup is defined in each test case in clause A.14.

## A.3.15C.1Setup 1: Single AoA

There is only one active probe in the test. The DL signals, and noise if applicable, transmitted from the probe, are aligned with the satellite epherimis information used in the test case and within the declared minimum elevation angle supported for receiving.

## A.3.15C.2Setup 2: 2 AoAs

There are 2 active probes in the test. The DL signals, and noise if applicable, are transmitted from the two active probes. One probe is aligned with the first satellite epherimis information used in the test case. The second probe is aligned with the second satellite epherimis information used in the test case. Both AoAs are within the declared minimum elevation angle supported for receiving and the relative angular offset between the two AoAs is 30°. The directions (AoAs) of the signals shall not be changed between test iterations.

## A.3.16TCI State Configuration

## A.3.16.1Introduction

This clause provides the configurations for TCI states towards either SSB or CSI-RS. The TCI states defined in this clause are configured in each test when applicable to indicate that certain DL signals are QCL’ed with the referenceSignal configured in the TCI states.

## A.3.16.2TCI states

Table A.3.16.2-1: TCI States

Table A.3.16.2-2: Void

## A.3.16AUnified TCI State Configuration

## A.3.16A.1Introduction

This clause provides the configurations for unified TCI states towards either SSB or CSI-RS. The DLorJoint TCI states defined in this clause are configured in each test when applicable to indicate that certain DL (and UL, if joint DL/UL operation is configured) signals are QCL’ed with the referenceSignal configured in the TCI states. The UL TCI states defined in this clause are configured in each test when applicable to indicate that certain UL signals are QCL’ed with the referenceSignal configured in the TCI states.

## A.3.16A.2DLorJoint TCI states

Table A.3.16A.2-1: DLorJoint TCI States

Table A.3.16A.2-2: DLorJoint TCI States for mTRP FR1

## A.3.16A.3UL TCI states

Table A.3.16A.3-1: UL TCI States

## A.3.16BLTM Candidate TCI State Configuration

## A.3.16B.1Introduction

This clause provides the configurations for TCI states of LTM candidate cell(s) towards either SSB or TRS. The LTM candidate DLorJoint TCI states defined in this clause are configured in each test when applicable to indicate that certain DL (and UL, if joint DL/UL operation is configured) signals are QCL’ed with the referenceSignal configured in the TCI states. The UL TCI states defined in this clause are configured in each test when applicable to indicate that certain UL signals are QCL’ed with the referenceSignal configured in the TCI states.

## A.3.16B.2LTM candidate DLorJoint TCI states

Table A.3.16B.2-1: LTM candidate DLorJoint TCI States

## A.3.16B.3LTM candidate UL TCI states

Table A.3.16B.3-1: LTM candidate UL TCI States

## A.3.17Configurations of CSI-RS for tracking

## A.3.17.1Configuration of CSI-RS for tracking for FR1

## A.3.17.1.1FDD

Table A.3.17.1.1-1: CSI-RS for tracking for SCS=15 kHz

Table A.3.17.1.1-2: CSI-RS for tracking for SCS=30 kHz

Table A.3.17.1.1-3: Aperiodic CSI-RS for tracking for SCS=15 kHz

Table A.3.17.1.1-4: Aperiodic CSI-RS for tracking for SCS=30 kHz

Table A.3.17.1.1-5: CSI-RS for tracking for SCS=15 kHz Set 1

Table A.3.17.1.1-6: CSI-RS for tracking for SCS=15 kHz Set 2

Table A.3.17.1.1-7: CSI-RS for tracking for SCS=15 kHz

## A.3.17.1.2TDD

Table A.3.17.1.2-1: CSI-RS for tracking for SCS=15 kHz

Table A.3.17.1.2-2: CSI-RS for tracking for SCS=30 kHz

Table A.3.17.1.2-3: Aperiodic CSI-RS for tracking for SCS=15 kHz

Table A.3.17.1.2-4: Aperiodic CSI-RS for tracking for SCS=30 kHz

Table A.3.17.1.2-5: CSI-RS for tracking for SCS=15 kHz Set 1

Table A.3.17.1.2-6: CSI-RS for tracking for SCS=15 kHz Set 2

Table A.3.17.1.2-7: CSI-RS for tracking for SCS=30 kHz Set 1

Table A.3.17.1.2-8: CSI-RS for tracking for SCS=30 kHz Set 2

Table A.3.17.1.2-9: CSI-RS for tracking for SCS=30 kHz

## A.3.17.2Configuration of CSI-RS for tracking for FR2

## A.3.17.2.1TDD

Table A.3.17.2.1-1: CSI-RS for tracking for SCS=120 kHz Set 1

Table A.3.17.2.1-2: CSI-RS for tracking for SCS=120 kHz Set 2

Table A.3.17.2.1-3: Aperiodic CSI-RS for tracking for SCS=120 kHz Set 1

Table A.3.17.2.1-4: CSI-RS for tracking for SCS=120 kHz Set 3

Table A.3.17.2.1-5: CSI-RS for tracking for SCS=120 kHz Set 4

Table A.3.17.2.1-6: CSI-RS for tracking for SCS=120 kHz Set 5

## A.3.17.2.2FDD

Table A.3.17.2.2-1: CSI-RS for tracking for SCS=120 kHz Set 1

## A.3.18Additional definitions related to OTA testing for FR2 RRM test cases

## A.3.18.1Introduction

FR2 RRM test cases are performed over the air (OTA). This clause provides additional definitions and clarifications on the OTA measurements and metrics defined or refered in the test cases.

## A.3.18.2PRACH Power Measurement

PRACH power is measured as EIRP(Link=Link angle, Meas=Link angle) as defined in clause 3.1 of TS 38.101-2 [19].

## A.3.19Test applicability for DAPS handover

## A.3.19.1Introduction

In annex A test cases for DAPS handover may be defined with cells in on same or different carrier frequency to verify intra-frequency, intra-band inter-frequency and inter-band inter-frequency DAPS handover RRM requirements, respectively.

## A.3.19.2Principle of testing

To verify intra-frequency DAPS handover requirements

-The UE capable of intra-frequency asynchronous DAPS handover on any band needs to be tested only in asynchronous scenario.

-The UE not capable of intra-frequency asynchronous DAPS handover on any band but capable of synchronous DAPS handover on some band needs to be tested only in synchronous scenario.

To verify intra-band inter-frequency DAPS handover requirements

-The UE capable of intra-band inter-frequency asynchronous DAPS handover on any band needs to be tested only in asynchronous scenario.

-The UE not capable of intra-band inter-frequency asynchronous DAPS handover on any band but capable of intra-band inter-frequency synchronous DAPS handover on some band needs to be tested only in synchronous scenario.

To verify inter-band inter-frequency DAPS handover requirements

-The UE capable of inter-band inter-frequency asynchronous DAPS handover on any band combination needs to be tested only in asynchronous scenario.

-The UE not capable of inter-band inter-frequency asynchronous DAPS handover on any band combination but capable of inter-band inter-frequency synchronous DAPS handover on some band combination needs to be tested only in synchronous scenario.

## A.3.20MsgA configurations

## A.3.20.1Introduction

This clause provides the typical PRACH and PUSCH configurations for MsgA used for RRM test cases defined in annex A. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.20.2MsgA configurations in FR1

## A.3.20.2.1FR1 MsgA configuration 1

FR1 MsgA configuration 1 in this clause provides the typical MsgA configuration for SSB-based contention based random access for 2-step RA type in FR1.

Table A.3.20.2.1-1: Parameters for FR1 MsgA configuration 1

## A.3.20.2.2FR1 MsgA configuration 2

FR1 PRACH configuration 2 in this clause provides the typical MsgA configuration for SSB based non-contention based random access for 2-step RA type in FR1.

Table A.3.20.2.2-1: Parameters for FR1 MsgA configuration 2

## A.3.20.3MsgA configurations in FR2

## A.3.20.3.1FR2 MsgA configuration 1

FR2 MsgA configuration 1 in this clause provides the typical MsgA configuration for SSB-based contention based random access for 2-step RA type in FR2.

Table A.3.20.3.1-1: Parameters for FR2 MsgA configuration 1

## A.3.20.3.2FR2 MsgA configuration 2

FR2 MsgA configuration 2 in this clause provides the typical MsgA configuration for SSB based non-contention based random access for 2-step RA type in FR2.

Table A.3.20.3.2-1: Parameters for FR2 MsgA configuration 2

## A.3.20AMsgA configurations under CCA

## A.3.20A.1Introduction

This clause provides the typical PRACH and PUSCH configurations for MsgA used for RRM test cases defined in annex A. To note that for other parameters not listed in this clause, either it can be derived from the set up of each test or it is subjected to RAN5 specifications.

## A.3.20A.2MsgA configurations in FR1

## A.3.20A.2.1FR1 MsgA configuration 1 under CCA

FR1 MsgA configuration 1 under CCA in this clause provides the typical MsgA configuration for SSB-based contention based random access for 2-step RA type in FR1.

Table A.3.20A.2.1-1: Parameters for FR1 MsgA configuration 1 under CCA

## A.3.20A.2.2FR1 MsgA configuration 2 under CCA

FR1 PRACH configuration 2 under CCA in this clause provides the typical MsgA configuration for SSB based non-contention based random access for 2-step RA type in FR1.

Table A.3.20A.2.2-1: Parameters for FR1 MsgA configuration 2 under CCA

## A.3.21V2X sidelink communication

## A.3.21.1Introduction

This clause also defines the principle and the reference configurations that are applicable to test cases verifying RRM core requirements for V2X sidelink communication.

## A.3.21.2Reference resource pool configurations for V2X Sidelink Communication

Table A.3.21.2-1: V2X sidelink SL-BWP configuration for NR

Table A.3.21.2-2: V2X sidelink resource pool configuration for NR

Table A.3.21.2-3: V2X sidelink UE autonomous resource selection configuration for NR

## A.3.21.3Reference measurement channels for V2X Sidelink Communication

Table A.3.21.3-1: PSCCH Reference Measurement Channels

Table A.3.21.3-2: PSSCH Reference Measurement Channels

## A.3.21.4Reference SL-DRX configurations

## A.3.21.4.1SL-DRX Configuration 1: SL-DRX cycle = 40 ms

Table A.3.21.4.1-1: SL-DRX.1: SL-DRX cycle = 40 ms

## A.3.21.4.2SL-DRX Configuration 2: SL-DRX cycle = 320 ms

Table A.3.21.4.2-1: SL-DRX.2: SL-DRX cycle = 320 ms

## A.3.21.4.3SL-DRX Configuration 3: SL-DRX cycle = 640 ms

Table A.3.21.4.3-1: SL-DRX.3: SL-DRX cycle = 640 ms

## A.3.21ANR Sidelink Measurements for Positioning

## A.3.21A.1Introduction

This clause defines the principles and the reference configurations that are applicable to test cases verifying RRM requirements for NR sidelink measurements for positioning.

## A.3.21A.2NR SL-PRS configurations

## A.3.21A.2.1NR SL-PRS configurations for FR1

Table A.3.21A.2.1-1: SL PRS.1 FR1: SL-PRS configuration

## A.3.22CSI-IM configurations

## A.3.22.1FDD

Table A.3.22.1-1: CSI-IM Reference Measurement Channels for SCS=15 kHz

## A.3.22.2TDD

Table A.3.22.2-1: CSI-IM Reference Measurement Channels for SCS=15 kHz

Table A.3.22.2-2: CSI-IM Reference Measurement Channels for SCS=30 kHz

Table A.3.22.2-3: CSI-RS Reference Measurement Channels for SCS=120 kHz

## A.3.23Spatial Relation Configuration

## A.3.23.1Introduction

This clause provides the configurations for spatial relation towards either SSB or CSI-RS. The spatial relation defined in this clause are configured in each test when applicable to indicate spatial setting for certain UL signals with the referenceSignal configured in the spatial relation.

## A.3.23.2Spatial Relation

Table A.3.23.2-1: PUCCH Spatial Relation

Table A.3.23.2-2: SRS Spatial Relation

## A.3.24SRS configuration

Table A.3.24-1: Sounding Reference Symbol Configuration for SCS=15 kHz

Table A.3.24-2: Sounding Reference Symbol Configuration for SCS=30 kHz

Table A.3.24-3: Sounding Reference Symbol Configuration for SCS=120 kHz

## A.3.25Channel bandwidth (CBW) configurations

## A.3.25.1DL UE specific CBW

Table A.3.25.1-1: DL CBW patterns for UE specific CBW configuration

## A.3.25.2UL UE specific CBW

Table A.3.25.2-1: UL CBW patterns for UE specific CBW configuration

## A.3.26CCA model

## A.3.26.1Introduction

The CCA model is used in some RRM test cases with at least one cell on a carrier frequency with CCA. The intention with the CCA model is to emulate in the test equipment the behaviour of a gNB or UE which performs channel measurement to check that the channel is clear prior to performing one or more downlink, uplink or sidelink transmissions.

## A.3.26.2CCA model for operation on a carrier frequency with CCA in FR1

## A.3.26.2.1DL CCA model

The same DL CCA model is applicable regardless of whether DRX cycle is used or not with the following differences:

-The counter, lCCA, is used to monitor the number of unavailable DBT samples withing an evaluation window, WCCA_DL. DBT samples outside of the evaluation window WCCA_DL are discarded.

If DRX cycle is not used then prior to each DBT window, the test equipment shall determine whether the DL CCA attempt is successful (i.e., the corresponding signals have to be transmitted), based on probability PCCA_DL of successful DL CCA configured in the corresponding test case. If DRX cycle is not used, then the DL CCA model shall increment the counter lCCA for every unavailable DBT sample due to DL CCA failure.

-If DRX cycle is used, then the DL CCA model shall increment the counter, lCCA, once per DRX cycle for a DRX cycle if the first DBT sample in that DRX cycle is unavailable due to DL CCA failure. DL CCA failures in a DRX cycle are determined as follows:

-The test system in the first DBT window of each DRX cycle determines whether the DL CCA attempt is successful or not using the principle as follows:

-If the DL CCA is successful then the test system shall transmit in all DBT windows within that DRX cycle.

-If the DL CCA is not successful then the test system shall not transmit in any of the DBT windows within that DRX cycle. In this case lCCA is increased by 1.

-The parameters, LCCA_DL, LCCA_UL, WCCA_DL and WCCA_UL can be used as in non-DRX tests.

If the CCA attempt is successful for a transmission, then the test equipment shall transmit also other remaining transmissions, according to the configuration, within the same DBT window.

If the CCA attempt is not successful for a transmission within the DBT window, the test equipment shall determine whether the CCA attempt is successful for the next configured transmission, based on probability PCCA_DL.

The probability can be different in different time intervals Ti during a test case. One probability value (per cell) applies at any time point during a test; one or more probability values can be configured in the entire test, one value PCCA_DL per time interval Ti where i≥1, and the multiple time intervals (when i>1) do not overlap (e.g., PCCA_DL=1.0 in T1 and PCCA_DL=0.75 in T2).

For semi-static channel access configuration, a single value PCCA_DL is used to configure the probability of CCA success in different time intervals Ti during a test realization. An additional limit LCCA_DL is used to determine the maximum number of unavailable DBT samples within an evaluation window WCCA_DL. If the number of unavailable DBT samples on the last WCCA_DL DBT samples is larger or equal to LCCA_DL, the CCA attempt is considered successful for transmission.

For dynamic channel access configuration, the parameters PCCA_DL_1 and PCCA_DL_2 are used to configure the probability of CCA success on the first and second SSB candidate positions, respectively, in different time intervals Ti during a test realization. An additional limit LCCA_DL is used to determine the maximum number of unavailable DBT samples within an evaluation window WCCA_DL. If the number of unavailable DBT samples on the last WCCA_DL DBT samples is larger or equal to LCCA_DL, the CCA attempt is considered successful for transmission.

For semi-static channel access configuration or for dynamic channel access configuration where one candidate SSB position is modelled, prior to each discovery burst transmission window within a time interval Ti of the test, the test equipment shall:

1Generate a uniform random variable p1 from the range [0, 1] for the first candidate position.

## 2 Transmit the discovery burst based on p1 in the first candidate position. If p1 ≤ PCCA_DL, the discovery burst is transmitted at the first candidate SSB location; else if lCCA is larger than or equal to LCCA_DL, the discovery burst is transmitted at the first candidate SSB location, otherwise the discovery burst is muted. If DRX cycle is used, then the decision whether the discover burst is muted or not is repeated for the rest of the DRX cycle.

For dynamic channel access configuration where two candidate SSB positions are modelled, prior to each discovery burst transmission window within a time interval Ti of the test, the test equipment shall:

## 1 Generate a uniform random variable p1 from the range [0, 1] for the first candidate position.

## 2 Transmit the discovery burst based on p1 in the first candidate position: if p1 ≤ PCCA_DL1, the discovery burst is transmitted at first candidate SSB location, else the test equipment shall:

a Generate a uniform random variable p2 from the range [0, 1] for the second candidate SSB position.

b Transmit the discovery burst based on p2 in the second candidate position.  If p2 ≤ PCCA_DL2, the discovery burst is transmitted at the second candidate SSB location; else if lCCA is larger than or equal to LCCA_DL, the discovery burst is transmitted at the second candidate SSB location, otherwise the discovery burst is muted. If DRX cycle is used, then the decision whether the discover burst is muted or not is repeated for the rest of the DRX cycle.

The above steps are repeated for each discovery burst transmission window in each time interval Ti of the test. The limit LCCA_DL and window WCCA_DL is a configuration parameter for each test case.

In many test cases, the requirement under a test depends on the number of configured SSB transmissions which are not available during the test due to CCA failure, so the test equipment shall track how many such signal occasions are not transmitted in DL during the test period.

## A.3.26.2.2UL CCA model

For UL CCA, the modelling approach is based on probability PCCA_UL of successful CCA. Probability PCCA_UL is configured in the corresponding test case, based on a set SCCA_UL of possible values including 75 % and 87% as typical values for dynamic and semi-static channel access configurations, 0% to model consistent UL CCA failures, and 100% to model no UL CCA failures.

Consistent UL CCA failures are modelled by configuring a low value for PCCA_UL, e.g., PCCA_UL = 0%.

In the same time interval Ti during the same test case, PCCA_UL can be different from PCCA_DL.

The probability can be different in different time intervals Ti during a test case. One probability value applies at any time point during a test; one or more probability values can be configured in the entire test, one value PCCA_UL per time interval Ti where i ≥ 1, and the multiple time intervals (when i > 1) do not overlap (e.g., PCCA_UL = 1.0 in T1 and PCCA_UL = 0.75 in T2).

TCCA µs prior to each UL transmission burst in the test, the test equipment (TE) shall generate a uniform random variable p from the range [0, 1]. If p>PCCA_UL, the TE transmits an OCNG noise pattern with an energy level X per LBT measurement BW, within the UE BW scheduled/configured for the UL transmission for at-least TCCA µs. Where TCCA µs is energy detection time for accessing the uplink channel as defined in section 5.1.1 of TS 37.106 [36]. Where:

-X is 9 dB above the energy detection threshold defined in section 5.1.1 of TS 37.106 [36].

-TCCA is the channel sensing period depending on CCA category for the next UL transmission.

The TE shall count the number of UL CCA failures, and no further UL CCA failures are modelled if the number of failures exceeds the limit LCCA_UL within a window WCCA_UL. For each UL CCA failure generated by the model, the TE shall monitor the corresponding UL resource for the desired UL signal, and based on when and/or whether the TE received the desired UL signal, it deems the test case to pass or fail.

In many cases, the requirement under a test depends on the number of configured signal occasions which are not available during the test, so the test equipment shall track how many such signal occasions are not transmitted in UL during the test period.

## A.3.26.3CCA model for operation on a carrier frequency with CCA in FR2-2

## A.3.26.3.1DL CCA model

For DL CCA, the modelling approach is based on probability PCCA_DL of successful CCA.

If the CCA attempt is successful for a transmission, then the test equipment shall transmit also other remaining transmissions, according to the configuration, within the same DBT window.

If the CCA attempt is not successful for a transmission within the DBT window, the test equipment shall determine whether the CCA attempt is successful for the next configured transmission, based on probability PCCA_DL.

To decide whether the CCA attempt for one SSB/SMTC occasion within one SSB/SMTC occasion group, where one SSB/SMTC occasion group consists of 12 consecutive SSB/SMTC occasions is successful or not, TE shall:

## 1 - Generate a uniform random variable p from the range [0, 1].

## 2 - If p > PCCA_DL,

-TE picks one SSB/SMTC occasion out of a group of 12 consecutive SSB/SMTC occasions based on a fixed pattern, where one SSB/SMTC occasion is equivalent to one SSB burst Set.

-TE models CCA failure in this SSB/SMTC occasion. Note that other 11 SSB/SMTC occasions shall be transmitted by the TE.

-Whole SSB/SMTC occasion group is considered as unavailable to the UE.

## 2 - If p ≤ PCCA_DL,

-TE transmit 12 consecutive SSB/SMTC occasions.

-Whole SSB/SMTC occasion group is considered as available to the UE.

In many test cases, the requirement under a test depends on the number of configured SSB transmissions which are not available during the test due to CCA failure, so the test equipment shall track how many such signal occasions are not transmitted in DL during the test period.

## A.3.26.3.2UL CCA model

For UL CCA, the modelling approach is based on probability PCCA_UL of successful CCA. Probability PCCA_UL is configured in the corresponding test case.

Consistent UL CCA failures are modelled by configuring a low value for PCCA_UL, e.g., PCCA_UL = 0%.

In the same time interval Ti during the same test case, PCCA_UL can be different from PCCA_DL.

The probability can be different in different time intervals Ti during a test case. One probability value applies at any time point during a test; one or more probability values can be configured in the entire test, one value PCCA_UL per time interval Ti where i ≥ 1, and the multiple time intervals (when i > 1) do not overlap (e.g., PCCA_UL = 1.0 in T1 and PCCA_UL = 0.75 in T2).

TCCA µs prior to each UL transmission burst in the test, the test equipment (TE) shall generate a uniform random variable p from the range [0, 1]. If p>PCCA_UL, the TE transmits an OCNG noise pattern with an energy level X within the UE BW scheduled/configured for the UL transmission for at-least TCCA µs. Where TCCA µs is energy detection time for accessing the uplink channel as defined in section 5.1.1 of TS 37.106 [36]. Where:

-X is 3 dB above the energy detection threshold defined in section 5.1.1 of TS 37.106 [36].

-TCCA is the channel sensing period depending on CCA category for the next UL transmission.

In many cases, the requirement under a test depends on the number of configured signal occasions which are not available during the test, so the test equipment shall track how many such signal occasions are not transmitted in UL during the test period.

## A.3.26.4CCA model for operation on a sidelink carrier frequency with CCA

## A.3.26.4.1CCA model for SyncRef UE

For the SyncRef UE transmitting S-SSB in sidelink carrier frequency with CCA, the modelling approach is based on probability PCCA_SL_SyncRefUE of successful CCA.

If the CCA attempt is successful for a S-SSB transmission, then the test equipment shall transmit S-SSB on S-SSB transmission occasion, according to the configuration.

If the CCA attempt is not successful for a S-SSB transmission, the test equipment shall determine whether the CCA attempt is successful for the next S-SSB occasion, based on probability PCCA_SL_SyncRefUE.

A counter, denoted by lCCA, tracks the number of unavailable S-SSB periods. In the SL CCA model, the counter lCCA is incremented when CCA failures led to an unavailable S-SSB period.

The probability can be different in different time intervals Ti during a test case. One probability value applies at any time point during a test; one or more probability values can be configured in the entire test, one value PCCA_SL_SyncRefUE per time interval Ti where i ≥ 1, and the multiple time intervals (when i > 1) do not overlap (e.g., PCCA_SL_SyncRefUE = 1.0 in T1 and PCCA_SL_ SyncRefUE = 0.75 in T2).

The parameters P CCA_SL_SyncRefUE_1 and PCCA_SL_SyncRefUE_2 are used to configure the probability of CCA success on the first and second S-SSB candidate occasions, respectively, in different time intervals Ti during a test realization. An additional limit LCCA_SL determines the maximum number of unavailable S-SSB periods. If lCCA ≥LCCA_SL, the CCA attempt is considered successful for S-SSB transmissions.

Two candidate SSB occasions are modelled within each S-SSB period. To decide whether the CCA attempt for the two S-SSB occasions within each of S-SSB period is successful, TE shall:

## 1 - Generate a uniform random variable p1 from the range [0, 1] for the first candidate S-SSB occasion.

## 2 - Transmit the S-SSB based on p1 in the first candidate occasion:

-if p1 ≤ PCCA_SL_SyncRefUE_1, the S-SSB is transmitted in first candidate SSB occasion and this S-SSB period is considered as available to the DUT,

-else TE shall generate a uniform random variable p2 from the range [0, 1] for the second candidate SSB occasion

-If p2 ≤ PCCA_SL_SyncRefUE_2 or if lCCA ≥ LCCA_SL, the S-SSB is transmitted in the second candidate SSB occasion;

-else this S-SSB period is muted.

The above steps are repeated for each S-SSB periods in each time interval Ti of the test. The limit LCCA_SL is a configuration parameter for each test case.

In many test cases, the requirement under a test depends on the counter lCCA, so the test equipment shall track how many such S-SSB periods are not transmitted by TE during the test period.

## A.3.27Void

## A.3.27.1Void

## A.3.27.2Void

## A.3.27.3Void

## A.3.27.4Void

## A.3.27.5Void

## A.3.28Discovery Burst Transmission Window configuration under CCA

## A.3.28.1DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms

Table A.3.28.1-1: DBT.1: DBT Window Pattern 1 for DBT Window period = 20 ms and duration = 1 ms

## A.3.29Testing principles for UE capable of only NR bands with shared spectrum access

## A.3.29.1Introduction

In annex A test cases are defined involving one or more NR cells operating on NR band(s) with shared spectrum channel access. The NR bands with shared spectrum channel access are defined in clause 5.2 of TS 38-101-1 [18].

## A.3.29.2Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access

In annex A, test cases in table A.3.29.2-1 are defined for UE capable of EN-DC with only NR band(s) with shared spectrum access and are not required for UE supporting also other NR band(s) (i.e. band with no shared spectrum access). The EN-DC configurations are defined in clause of 5.5B of TS 38.101-3 [20].

Table A.3.29.2-1: Test cases applicable to UE supporting EN-DC with only NR bands with shared spectrum access

## A.3.29.3Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access

In annex A, test cases in table A.3.29.3-1 are defined for UE capable of NR SA operation with only NR band(s) with shared spectrum access and are not required for UE supporting also other NR band(s) (i.e. band with no shared spectrum access).

Table A.3.29.3-1: Test cases applicable to UE supporting SA operation with only NR bands with shared spectrum access

## A.3.30CSI-RS configurations for RRM

## A.3.30.1FDD

Table A.3.30.1-1: CSI-RS RRM Reference Measurement Channels for SCS=15 kHz

## A.3.30.2TDD

Table A.3.30.2-1: CSI-RS RRM Reference Measurement Channels for SCS=15 kHz

Table A.3.30.2-2: CSI-RS RRM Reference Measurement Channels for SCS=30 kHz

Table A.3.30.2-3: CSI-RS RRM Reference Measurement Channels for SCS=120 kHz

## A.3.31PRS Configurations

## A.3.31.1PRS Configurations for FR1

## A.3.31.1.1PRS pattern 1 in FR1: SCS=15 kHz

Table A.3.31.1.1-1: PRS.1 FR1: PRS Pattern 1 for SCS=15 kHz

## A.3.31.1.2PRS pattern 2 in FR1: SCS=30 kHz

Table A.3.31.1.2-1: PRS.2 FR1: PRS Pattern 2 for SCS=30 kHz

## A.3.31.2PRS Configurations for FR2

## A.3.31.2.1PRS pattern 1 in FR2: SCS=120 kHz

Table A.3.31.2.1-1: PRS.1 FR2: PRS Pattern 1 for SCS=120 kHz

## A.3.32NR sidelink discovery

## A.3.32.1Introduction

This clause also defines the principle and the reference configurations that are applicable to test cases verifying RRM core requirements for NR sidelink discovery.

## A.3.32.2Reference resource pool configurations for NR Sidelink Discovery

Table A.3.32.2-1: SL-BWP configuration for NR sidelink discovery

## A.3.32.3Principle of Testing

The UE capable of both V2X sidelink communication and NR sidelink discovery does not have to pass the test for interruption at NR sidelink discovery configuration defined in clause 9.1.6.1, if this UE has already passed the test case for interruption due to V2X sidelink communication defined in clause 9.1.6.1.

## A.3.33PRS Processing Window (PPW) configurations

Table A.3.33-1: Reference PPW configuration

## A.3.34Testing principles for test cases related to PRS measurements

## A.3.34.1Introduction

In annex A test cases are defined for verifying various type of PRS measurement and accuracy requirements.

## A.3.34.2Test cases in RRC_INACTIVE state

In annex A, PRS measurement test cases are defined with 4 samples and with reduced number of samples in RRC_INACTIVE state. The testing principle for these test cases is as follows:

-A UE capable of supportedDL-PRS-ProcessingSamples-RRC-Inactive [34] is only required to pass the test cases with reduced number of samples.

-A UE not capable of supportedDL-PRS-ProcessingSamples-RRC-Inactive [34] is required to pass the test cases with 4 samples.

In Annex A, PRS measurement delay test cases are defined for both PRS-RSRP and PRS-RSRPP measurements in RRC_INACTIVE state when UE is configured with DRX cycle and eDRX cycle > 10.24s for positioning measurements. The testing principle for these test cases is as follows:

-A UE capable of both PRS-RSRP and PRS-RSRPP measurements is required to pass either PRS-RSRP measurement delay test or PRS-RSRPP measurement delay test.

In Annex A, PRS measurement delay test cases are defined for both RSTD and UE Rx-Tx time difference measurements in RRC_INACTIVE state when UE is configured with DRX cycle and eDRX cycle > 10.24s for positioning measurements. The testing principle for these test cases is as follows:

-A UE capable of both RSTD and UE Rx-Tx time difference measurements is required to pass either RSTD measurement delay test or UE Rx-Tx time difference measurement delay test.

## A.3.34.3Test cases for PRS measurements with gaps in RRC_CONNECTED state

In annex A, PRS measurement test cases are defined with 4 samples and with reduced number of samples with measurement gaps in RRC_CONNECTED state. The testing principle for these test cases is as follows:

-A UE capable of supportedDL-PRS-ProcessingSamples [34] is only required to pass the test cases with reduced number of samples.

-A UE not capable of supportedDL-PRS-ProcessingSamples [34] is required to pass the test cases with 4 samples.

In annex A, PRS measurement delay test cases are defined for both PRS-RSRP and PRS-RSRPP measurements with measurement gaps in RRC_CONNECTED state. The testing principle for these test cases is as follows:

-A UE capable of both PRS-RSRP and PRS-RSRPP measurements is required to pass either PRS-RSRP measurement delay test or PRS-RSRPP measurement delay test.

## A.3.34.4Test cases for PRS measurements without gaps in RRC_CONNECTED state

In annex A, PRS measurement test cases are defined with 4 samples and with reduced number of samples without measurement gaps in RRC_CONNECTED state. The testing principle for these test cases is as follows:

-A UE capable of supportedDL-PRS-ProcessingSamples [34] is only required to pass the test cases with reduced number of samples.

-A UE not capable of supportedDL-PRS-ProcessingSamples [34] is required to pass the test case with 4 samples.

In annex A, PRS measurement delay test cases are defined for both PRS-RSRP and PRS-RSRPP measurements without measurement gaps in RRC_CONNECTED state. The testing principle for these test cases is as follows:

-A UE capable of both PRS-RSRP and PRS-RSRPP measurements is required to pass either PRS-RSRP measurement delay test or PRS-RSRPP measurement delay test.

In annex A, PRS measurement delay test cases are defined for both RSTD and UE Rx-Tx time difference measurements without measurement gaps in RRC_CONNECTED state. The testing principle for these test cases is as follows:

-A UE capable of both RSTD and UE Rx-Tx time difference measurements is required to pass either RSTD measurement delay test or UE Rx-Tx time difference measurement delay test.

## A.3.34.5Testing principles for positioning measurements by aggregating PRS resources from multiple PFLs

In annex A, test cases for measurement delay requirement and accuracy requirement for positioning measurements by aggregating PRS resources from multiple PLFs are defined. While verifying the UE capability to meet the requirements defined for the positioning measurements by aggregating PRS resources from multiple PFLs, a UE capable of both RSTD and UE Rx-Tx time difference measurements by aggregating PRS resources from multiple PFLs is required to pass either PRS aggregation based RSTD measurement delay test or PRS aggregation-based UE Rx-Tx time difference measurement delay test.

## A.3.34.6Testing principles for carrier phase measurement for positioning

In annex A, test cases for measurement delay requirement and accuracy requirement for carrier phase measurement reported together with legacy positioning measurement are defined.

While verifying the UE capability to meet the requirements defined for the carrier phase measurement reported together with the legacy positioning measurement, a UE capable of both RSCPD with RSTD and RSCP with UE Rx-Tx time difference measurements is required to pass either RSCPD with RSTD measurement delay test or RSCP with UE Rx-Tx time difference measurement delay test.

When a UE is tested for DL RSCPD with RSTD measurement, then the UE shall pass tests for RSTD measurement and RSCPD measurement.

When a UE is tested for DL RSCP with UE Rx-Tx measurement, then the UE shall pass tests for UE Rx-Tx measurement and DL RSCP measurement.

## A.3.34.7Test cases in RRC_IDLE state

For the measurements supported by the UE in both RRC_IDLE and RRC_INACTIVE modes, UE shall pass the test cases for RRC_IDLE mode and does not need to be tested for the same measurement in RRC_INACTIVE mode.

## A.3.35Testing principle for RedCap UE

## A.3.35.1Introduction

This clause defines testing principles which are applicable to test cases verifying RRM requirements for RedCap UE and test cases verifying PRS measurement requirements for RedCap UE.

## A.3.35.2Principle of testing for FR1

For RedCap and eRedCap UEs supporting 1 Rx branch, all single carrier tests specified in clause A.16 and A.18 except for tests defined for 2 Rx and/or FR2 shall be tested on any band.

For RedCap and eRedCap UEs supporting 2Rx branches, all single carrier tests specified in clause A.16 and A.18 except for tests defined for 1 Rx and/or FR2 shall be tested on any band.

## A.3.35.3Principle of testing for FR2

For RedCap UEs, all single carrier tests specified in clause A.17 and A.18 except for tests defined for FR1 shall be tested on any band.

## A.3.35.4Principle of testing for PRS measurement

In annex A, test cases for measurement delay requirement and accuracy requirement for PRS measurement for RedCap UE are defined. The following testing principles are applied while verifying the RedCap UE capability to meet the PRS measurement requirements.

-A UE capable of both PRS-RSRP and PRS-RSRPP measurements is required to pass either PRS-RSRP measurement delay test or PRS-RSRPP measurement delay test.

-A UE capable of both RSTD and UE Rx-Tx time difference measurements is required to pass either RSTD measurement delay test or UE Rx-Tx time difference measurement delay test.

-A UE capable of performing PRS measurement with RX FH is only required to pass the measurement delay test cases for PRS measurement with RX FH.

-For the measurements supported by the UE in both RRC_IDLE and RRC_INACTIVE modes, UE shall pass the test cases for RRC_IDLE mode and does not need to be tested for the same measurement in RRC_INACTIVE mode.

-A UE that indicates  via processingPRS-SymbolsDurationN3-r18 which leads to  to be equal to 0 is not required to pass corresponding test cases. N3iNhop,i,j

## A.3.36Testing related to Satellite access

## A.3.36.1Introduction

In annex A test cases are defined for verifying various type of RRM requirements related to satellite access.

## A.3.36.2Principle of testing GSO and NGSO scenarios

In annex A, RRM test cases related to satellite access are defined for both GSO and NGSO. The testing principle for these test cases is as follows:

-A UE capable of GSO only is required to pass the test cases with GSO.

-A UE capable of NGSO only is required to pass the test cases with NGSO.

-A UE capable of both GSO and NGSO is required to pass the test cases with NGSO only.

Support of GSO and NGSO scenario is indicated via ntn-ScenarioSupport-r17.

The tests with the satellite-motion based varying Doppler and delay shift NTN channel model for FR1-NTN bands is NOT applicable for VSAT UE.

For UE and onwards under the satellite-motion based varying Doppler and delay shift NTN channel model for FR1-NTN bands, supporting NGSO, the following test applicability rules apply:

-The UE shall pass test “A.14.3.1.1 NR UE Transmit Timing Test for FR1” based on Config ID#3 defined for Rel-19 satellite-motion based varying Doppler and delay shift NTN channel model.

-For the rest test cases where the satellite-motion based varying Doppler and delay shift NTN channel model can be applied, i.e. A.14.1.1, A.14.2.1.1 and A.14.5.3.1,

-The UE shall pass the test cases based on either Config ID#2 with the existing static NGSO channel, or the Config ID#3 defined for the satellite-motion based varying Doppler and delay shift NTN channel model.

-For other test cases where the satellite-motion based varying Doppler and delay shift NTN channel model cannot be applied, the UE shall pass the existing test cases.

## A.3.36.3Principle of testing different RRM requirements

In annex A, RRM test cases related to satellite access are defined for all applicable RRM requirements. The testing principle for these test cases is as follows:

-A UE capable of NTN only is required to pass all the test cases defined in clause A.14.

-A UE capable of both TN and NTN is required to pass the test cases for NTN specific requirements in table A.3.36.3-1.

Table A.3.36.3-1: Test cases for NTN specific requirements

For UEs that declare capabilities to support channel bandwidth of 3 MHz (clause 4.2.7.2 in TS 38.306 [14]), the UE shall also pass the following test cases indicated in Table A.3.36.3-2.

Table A.3.36.3-2: Test cases for NTN UEs supporting operation with 3 MHz channel bandwith

## A.3.36.4Principle of testing different ephemeris formats

Satellite access RRM test cases are defined such that satellite ephemeris information is sent to UE in each test case, according to tables A.3.36.34-1 and A.3.36.34-2.

Table A.3.36.4-1: Test cases configuring EphemerisInfo as PositionVelocity

Table A.3.36.4-2: Test cases configuring EphemerisInfo as Orbital

## A.3.36.5General setup for SIB19

The general parameters for SIB19 setup is specified in table A.3.36.5-1.

Table A.3.36.5-1: Test cases for NTN specific requirements

## A.3.36.6Satellite specific parameters configuration

## A.3.36.6.1Satellite specific configuration for serving cell

Table A.3.36.6.1-1: Satellite specific configuration pattern 1 for serving cell in GSO scenario

Table A.3.36.6.1-2: Satellite specific configuration pattern 2 for serving cell in NGSO scenario

## A.3.36.6.2Satellite specific configuration for neighbour cell

Table A.3.36.6.2-1: Satellite specific configuration pattern 1 for neighbour cell in GSO scenario

.

Table A.3.36.6.2-2: Satellite specific configuration pattern 2 for neighbour cell in NGSO scenario

## A.3.37Reference Cell DTX configurations

## A.3.37.1Cell DTX Configuration 1: Cell DTX cycle = 160 ms and TAT = Infinity

Table A.3.37.1-1: DTX.1: Cell DTX cycle = 160 ms and time alignment timer (TAT) = Infinity

## A.3.38DL-PRS Measurement Time Window configurations

Table A.3.38-1: Reference configuration for DL-PRS Measurement Time Window

## A.3.39Testing related to RedCap UE with Satellite Access

## A.3.39.1Introduction

In annex A test cases are defined for verifying various type of RRM requirements for RedCap UE with Satellite Access.

## A.3.39.2Principle of testing 1Rx and 2Rx (e)RedCap UE in FR1

For RedCap UEs supporting 1 Rx branch, all single carrier tests specified in clause A.20 except for tests defined for 2 Rx shall be tested on any band.

For RedCap UEs supporting 2 Rx branches, all single carrier tests specified in clause A.20 except for tests defined for 1Rx shall be tested on any band.

## A.3.39.3Principle of testing GSO and NGSO scenarios

In annex A, RRM test cases related to RedCap UE with Satellite Access are defined for both GSO and NGSO. The testing principle for these test cases is as follows:

-A UE capable of GSO only is required to pass the test cases with GSO.

-A UE capable of NGSO only is required to pass the test cases with NGSO.

-A UE capable of both GSO and NGSO is required to pass the test cases with NGSO only.

Support of GSO and NGSO scenario is indicated via ntn-ScenarioSupport-r17.

## A.3.39.4Principle of testing different RRM requirements

In annex A, RRM test cases related to RedCap UE with Satellite Access are defined for all applicable RRM requirements. The testing principle for these test cases is as follows:

-A RedCap UE capable of NTN only is required to pass all the test cases defined in clause A.20.

-A RedCap UE capable of both TN and NTN is required to pass the test cases for RedCap UE with NTN specific requirements in table A.3.39.4-1.

Table A.3.39.4-1: Test cases for RedCap UE with NTN specific requirements

## A.3.39.5Principle of testing HD-FDD RedCap UE

In annex A, RRM test cases related to RedCap UE with Satellite Access are defined for FD-FDD and HD-FDD. The testing principle for these test cases is as follows:

-A RedCap UE capable of both FDD and HD-FDD operation only is required to pass the test cases with one of both.

## A.3.39.6Principle of testing different ephemeris formats

RRM test cases for RedCap UE with Satellite Access are defined such that satellite ephemeris information is sent to RedCap UE in each test case, according to Tables A.3.39.6-1 and A.3.39.6-2.

Table A.3.39.6-1: Test cases configuring EphemerisInfo as PositionVelocity

Table A.3.39.6-2: Test cases configuring EphemerisInfo as Orbital

## A.3.39.7General setup for SIB19

The general parameters for SIB19 setup is specified in table A.3.39.7-1 for RedCap UE with NTN.

Table A.3.39.7-1: Test cases for specific requirements for RedCap UE with NTN

## A.3.39.8Satellite specific parameters configuration

## A.3.39.8.1Satellite specific configuration for serving cell

Table A.3.39.8.1-1: Satellite specific configuration pattern 1 for serving cell in GSO scenario

Table A.3.39.8.1-2: Satellite specific configuration pattern 2 for serving cell in NGSO scenario

## A.3.39.8.2Satellite specific configuration for neighbour cell

Table A.3.39.8.2-1: Satellite specific configuration pattern 1 for neighbour cell in GSO scenario

.

Table A.3.39.8.2-2: Satellite specific configuration pattern 2 for neighbour cell in NGSO scenario

## A.3.40Testing principles for eEMR based fast SCell activation

## A.3.40.1Introduction

In annex A test cases are defined for verifying eEMR (enhanced early measurement reporting) based fast SCell activation requirements specified in clause 8.3.

## A.3.40.2Principle of testing

For UE supporting eEMR-based Direct SCell activation at SCell addition or eEMR-based PUCCH SCell activation, eEMR-based fast SCell activation for normal SCell activation can be skipped.

For UE supporting both eEMR-based Direct SCell activation at SCell addition and eEMR-based PUCCH SCell activation, eEMR-based PUCCH SCell activation can be skipped.

For UE which can pass R19 test cases for fast SCell activation based on R18 early measurement report, corresponding R18 test cases with valid report can be skipped.

## A.3.41Test configurations related to SBFD

## A.3.41.1SBFD configurations for FR1

## A.3.41.1.0Introduction

This clause provides typical SBFD configurations used for SBFD RRM test cases defined in annex A. Both the time domain and frequency domain configurations for SBFD are provided for FR1.

The applicable TDD DL/UL configurations for SBFD RRM test cases are defined in Clause A.3.1.4. Based on the applicable TDD DL/UL configurations for SBFD, the time domain configuration of SBFD slots/symbols is set as ‘DXXXU’, where ‘X’ denotes the SBFD slot with all ‘D’ and ‘S’ symbols in the slots configured as SBFD symbol.

For the frequency domain configuration of SBFD subbands, DU and DUD cases are allowed. For the case of DU, 80MHz is in D subband, and 20MHz is in U subband. For the case of DUD, 40MHz is in the 1st D subband, 20MHz is in U subband, and 40MHz is in the 2nd D subband.

## A.3.41.1.1SBFD.1 FR1

Table A.3.41.1.1-1: SBFD.1 FR1

## A.3.41.1.2SBFD.2 FR1

Table A.3.41.1.2-1: SBFD.2 FR1

## A.3.41.2SBFD configurations for FR2

## A.3.41.2.0Introduction

This clause provides typical SBFD configurations used for SBFD RRM test cases defined in annex A. Both the time domain and frequency domain configurations for SBFD are provided for FR2.

The applicable TDD DL/UL configurations for SBFD RRM test cases are defined in Clause A.3.1.4. Based on the applicable TDD DL/UL configurations for SBFD, the time domain configuration of SBFD slots/symbols is set as ‘DXXXU’, where ‘X’ denotes the SBFD slot with all ‘D’ and ‘S’ symbols in the slots configured as SBFD symbol.

## A.3.41.2.1SBFD.1 FR2

Table A.3.41.2.1-1: SBFD.1 FR2

## A.3.41.2.2SBFD.2 FR2

Table A.3.41.2.2-1: SBFD.2 FR2

## A.3.41.3Principle of testing L1-RSRP and L1-SINR measurements

In annex A, test cases are defined for L1-RSRP measurement with SBFD in clasue A.6.6.4.15 for FR1 and A.7.6.3.16 for FR2, and test cases are defined for L1-SINR measurement with SBFD in clasue A.6.6.8.5 for FR1 and A.7.6.6.4 for FR2, respectively. The testing principle for these test cases is as follows:

-A UE capable of L1-SINR measurement is only required to pass the test cases defined in clasue A.6.6.8.5 for FR1 and A.7.6.6.4 for FR2.

## A.3.41.4Collision configurations between CSI-RS and UL scheduling for SBFD

It is possible that the UL scheduling collides with the CSI-RS. In the test a single collision between UL scheduling and CSI-RS happens and the collision is randomly determined by the TE.

## A.3.41.5Configurations of DL RMC for SBFD

In the test, the PDSCH RMC is not transmitted in UL subband of SBFD symbols, unless otherwise stated in the test case. In the test, the CORESET RMC is not transmitted in UL subband of SBFD symbols, unless otherwise stated in the test case.

## A.3.41.6Configurations of OCNG for SBFD

In the test, the OCNG shall not be assumed in UL subband of SBFD symbols, unless otherwise stated in the test case.

## A.3.41.7Configuration of Noc for SBFD

In the test, the interference from other cells and noise sources shall not be assumed in UL subband of SBFD symbols, unless otherwise stated in the test case.

## A.3.42LP-SS configurations

## A.3.42.1LP-SS Configuration 1: M=1

Table A.3.42.1-1: LP-SS.1: LP-SS with M=1

## A.3.42.2LP-SS Configuration 2: M=4

Table A.3.42.2-1: LP-SS.2: LP-SS with M=4

## A.3.43Test conditions for AI/ML

## A.3.43.1Channel models for AI/ML based Beam Management FR2

Following simplified channel is used as specifically referred in the test case:

Table A.3.43.1-1: Simplified channel model parameters for UMi CDL-C at 28 GHz

The above channel model results from a simplification process of a more comprehensive CDL channel. For informative purposes only, this process has been summarized below:

1.Baseline channel model table is taken from the channel realization described in TR 38.827 [45].

2.The clusters that have the same AoAs are merged, by keeping the delay for the first tap, and combining the power of the three taps with the same AoD/AoAs.

3.After step 2, the weak clusters falling outside the UE’s spherical coverage (i.e. < -10dB) are removed to reduce the number of clusters, under the assumption that they have a limited impact on the beam management.

4.The intra-cluster elevation angle spread (i.e. CZSA) is flattened to fit the probe layout placed in a single plane. The ZoA is modified to the result of the weighted average of the ZoA for the remaining clusters after step 3.

5.The mid-point of the total angular spread of the clusters after step 4 is aligned so it falls inside the total spread of the probes, and then the AoAs in the channel model parameter table are modified to align with the closest probe location. Here, every cluster will be aligned with one probe location.
