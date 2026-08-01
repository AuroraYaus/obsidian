---
type: spec
aliases:
  - 36.133_36133-j50_sA.1-A.6
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.133_36133-j50_sA.1-A.6/content.md"
---
# TS 36.133 36133-j50_sA.1-A.6

## Annex A (normative):Test Cases

## A.1Purpose of annex

This Annex specifies test specific parameters for some of the functional requirements in sections 4 to 9. The tests provide additional information to how the requirements should be interpreted for the purpose of conformance testing. The tests in this Annex are described such that one functional requirement may be tested in one or several test and one test may verify several requirements. Some requirements may lack a test.

The conformance tests are specified in TS 36.521-3 [23]. Statistical interpretation of the requirements is described in Annex A.2.

## A.2Requirement classification for statistical testing

Requirements in this specification are either expressed as absolute requirements with a single value stating the requirement, or expressed as a success rate. There are no provisions for the statistical variations that will occur when the parameter is tested.

Annex A outlines the tests in more detail and lists the test parameters needed. The test will result in an outcome of a test variable value for the device under test (DUT) inside or outside the test limit. Overall, the probability of a "good" DUT being inside the test limit(s) and the probability of a "bad" DUT being outside the test limit(s) should be as high as possible. For this reason, when selecting the test variable and the test limit(s), the statistical nature of the test is accounted for.

The statistical nature depends on the type of requirement. Some have large statistical variations, while others are not statistical in nature at all. When testing a parameter with a statistical nature, a confidence level is set. This establishes the probability that a DUT passing the test actually meets the requirements and determines how many times a test has to be repeated and what the pass and fail criteria are. Those aspects are not covered by TS 36.133. The details of the tests on how many times to run it and how to establish confidence in the tests are described in TS 36.521-3 [23]. This Annex establishes the variable to be used in the test and whether it can be viewed as statistical in nature or not.

## A.2.1Types of requirements in TS 36.133

## A.2.1.1Time and delay requirements on UE higher layer actions

A very large part of the RRM requirements are delay requirements:

-In E-UTRAN RRC_IDLE state mobility (clause A.4) there is cell re-selection delay.

-In E-UTRAN RRC_CONNECTED state mobility (clauses A.5 and A.8) there is handover delay, cell search delay and measurement reporting delay.

-In RRC Connection Control (clause A.6) there is RRC re-establishment delay.

All have in common that the UE is required to perform an action observable in higher layers (e.g. camp on the correct cell) within a certain time after a specific event (e.g. when a new strong pilot or reference signal appears). The delay time is statistical in nature for several reasons, among others that several of the measurements are performed by the UE in a fading radio environment.

The variations make a strict limit unsuitable for a test. Instead there is a condition set for a correct action by the UE, e.g. that the UE shall camp on the correct cell within X seconds. Then the rate of correct events is observed during repeated tests and a limit is set on the rate of correct events, usually 90% correct events are required. How the limit is applied in the test depends on the confidence required, further detailed are in TS 36.521-3 [23].

## A.2.1.2Measurements of power levels, relative powers and time

A very large number of requirements are on measurements that the UE performs:

-In E-UTRAN RRC_CONNECTED state mobility (clause A.5) there are measurement reports.

-In Measurement Performance Requirements (clause A.9) there are requirements for all type of measurements.

The accuracy requirements on measurements are expressed in this specification as a fixed limit (e.g. +/-X dB), but the measurement error will have a distribution that is not easily confined in fixed limits. Assuming a Gaussian distribution of the error, the limits will have to be set at +/-3.29 if the probability of failing a "good DUT" in a single test is to be kept at 0.1%. It is more reasonable to set the limit tighter and test the DUT by counting the rate of measurements that are within the limits, in a way similar to the requirements on delay.

## A.2.1.3Implementation requirements

A few requirements are strict actions the UE should take or capabilities the UE should have, without any allowance for deviations. These requirements are absolute and should be tested as such. Examples are:

-"Event triggered report rate" in E-UTRAN RRC_CONNECTED state mobility (clauses A.5 and A.8)

-"Correct behaviour at time-out" in RRC connection control (clause A.6)

## A.2.1.4Physical layer timing requirements

There are requirements on Timing and Signaling Characteristics (clauses A.7). There are both absolute and relative limits on timing accuracy depending upon the type of requirement. Examples are:

-Initial Transmit Timing (clause A.7.1) has an absolute limit on timing accuracy.

-Timing Advance (clause A.7.2) has a relative limit on timing accuracy.

## A.3RRM test configurations

## A.3.1Reference Measurement Channels

## A.3.1.1PDSCH

## A.3.1.1.1FDD

Table A.3.1.1.1-1: PDSCH Reference Measurement Channels for FDD

Table A.3.1.1.1-2: PDSCH Reference Measurement Channels for FDD with slot duration TTI

Table A.3.1.1.1-3: PDSCH Reference Measurement Channels for FDD with subslot duration TTI

## A.3.1.1.2TDD

Table A.3.1.1.2-1: PDSCH Reference Measurement Channels for TDD UL/DL configuration1

Table A.3.1.1.2-2: PDSCH Reference Measurement Channels for TDD UL/DL configuration0

Table A.3.1.1.2-3: PDSCH Reference Measurement Channels for TDD slot duration TTI

## A.3.1.1.3FDD for UE category 0

Table A.3.1.1.3-1: PDSCH Reference Measurement Channels for FDD

## A.3.1.1.4HD-FDD for UE category 0

Table A.3.1.1.4-1: PDSCH Reference Measurement Channels for HD-FDD

## A.3.1.1.5TDD for UE category 0

Table A.3.1.1.5-1: PDSCH Reference Measurement Channels for TDD UL/DL configuration1

## A.3.1.1.6Frame Structure 3

Table A.3.1.1.6-1: PDSCH Reference Measurement Channels for FS 3

## A.3.1.2PCFICH/PDCCH/PHICH

## A.3.1.2.1FDD

Table A.3.1.2.1-1: PCFICH/PDCCH/PHICH Reference Channel for FDD

## A.3.1.2.2TDD

Table A.3.1.2.2-1: PCFICH/PDCCH/PHICH Reference Channel for TDD

## A.3.1.2.3HD-FDD for UE category 0

Table A.3.1.2.3-1: PCFICH/PDCCH/PHICH Reference Channel for HD-FDD

## A.3.1.2.4FS 3

Table A.3.1.2.4-1: PCFICH/PDCCH/PHICH Reference Channel for FS 3

## A.3.1.3MPDCCH Reference Channels for Cat-M1 UEs

MPDCCH reference measurement channels in this section can be used in tests for Cat-M2 UEs.

## A.3.1.3.1FDD in CEModeA

Table A.3.1.3.1-1: MPDCCH Reference Channel for Cat-M1 FDD UEs in CEModeA

## A.3.1.3.2HD-FDD in CEModeA

Table A.3.1.3.2-1: MPDCCH Reference Channel for Cat-M1 HD-FDD UEs in CEModeA

## A.3.1.3.3TDD in CEModeA

Table A.3.1.3.3-1: MPDCCH Reference Channel for Cat-M1 TDD UEs in CEModeA

## A.3.1.3.4FDD in CEModeB

Table A.3.1.3.4-1: MPDCCH Reference Channel for Cat-M1 FDD UEs in CEModeB

## A.3.1.3.5HD-FDD in CEModeB

Table A.3.1.3.5-1: MPDCCH Reference Channel for Cat-M1 HD-FDD UEs in CEModeB

## A.3.1.3.6TDD in CEModeB

Table A.3.1.3.6-1: MPDCCH Reference Channel for Cat-M1 TDD UEs in CEModeB

## A.3.1.4PDSCH Reference Channel for Cat-M1 UEs

## A.3.1.4.1FDD in CEModeA

Table A.3.1.4.1-1: PDSCH Reference Channel for Cat-M1 FDD in CEModeA

## A.3.1.4.2HD-FDD in CEModeA

Table A.3.1.4.2-1: PDSCH Reference Channel for Cat-M1 HD-FDD in CEModeA

## A.3.1.4.3TDD in CEModeA

Table A.3.1.4.3-1: PDSCH Reference Channel for Cat-M1 TDD in CEModeA

## A.3.1.4.4FDD in CEModeB

Table A.3.1.4.4-1: PDSCH Reference Channel for Cat-M1 FDD in CEModeB

## A.3.1.4.5HD-FDD in CEModeB

Table A.3.1.4.5-1: PDSCH Reference Channel for Cat-M1 HD-FDD in CEModeB

## A.3.1.4.6TDD in CEModeB

Table A.3.1.4.6-1: PDSCH Reference Channel for Cat-M1 TDD in CEModeB

## A.3.1.5NPDSCH Reference Channel for UE category NB1

## A.3.1.5.1HD-FDD in-band operation

Table A.3.1.5.1-1: NPDSCH Reference Channel for UE category NB1 for in-band operation

## A.3.1.5.2Void

## A.3.1.5.3HD-FDD standalone operation

Table A.3.1.5.3-1: NPDSCH Reference Channel for UE category NB1 for standalone operation

## A.3.1.5.4Void

## A.3.1.5.5HD-FDD guard band operation

Table A.3.1.5.5-1: NPDSCH Reference Channel for UE category NB1 for guard band operation

## A.3.1.5.6Void

## A.3.1.5.7TDD in-band operation

Table A.3.1.5.7-1: NPDSCH Reference Channel for UE category NB1 for in-band operation

## A.3.1.5.8TDD standalone operation

Table A.3.1.5.8-1: NPDSCH Reference Channel for UE category NB1 for standalone operation

## A.3.1.5.9TDD guard band operation

Table A.3.1.5.9-1: NPDSCH Reference Channel for UE category NB1 for guard band operation

## A.3.1.5.10NTN-TDD standalone operation

Table A.3.1.5.10-1: NPDSCH Reference Channel for UE category NB1 for standalone operation

## A.3.1.6NPDCCH Reference Channel for UE category NB1

## A.3.1.6.1In-band operation

Table A.3.1.6.1-1: NPDCCH Reference Channel for UE category NB1 for in-band operation in 10MHz LTE system

Table A.3.1.6.1-2: NPDCCH Reference Channel for UE category NB1 for in-band operation in 5MHz LTE system

## A.3.1.6.2Void

## A.3.1.6.3Standalone operation

Table A.3.1.6.3-1: NPDCCH Reference Channel for UE category NB1 for standalone operation

## A.3.1.6.4Void

## A.3.1.6.5Guard band operation

Table A.3.1.6.5-1: NPDCCH Reference Channel for UE category NB1 for guard band operation in 10MHz LTE system

Table A.3.1.6.5-2: NPDCCH Reference Channel for UE category NB1 for guard band operation in 5MHz LTE system

## A.3.1.6.6Void

## A.3.2OFDMA Channel Noise Generator (OCNG)

## A.3.2.1OCNG Patterns for FDD

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test) and/or allocations used for MBSFN. The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols without and with reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PDSCH reference channel, a constant transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PCFICH/PDCCH/PHICH reference channel which specifies the control region. The number of PDCCH OFDM symbols in the non-MBSFN subframes is the same as specified in the RMC used in the test. The number of PDCCH OFDM symbols in the MBSFN subframe is the maximal allowed according to TS 36.213 [16]. For any aggregation and PHICH allocation, the PDCCH and any unused PHICH groups are padded with resource element groups with a power level given by PDCCH_RA/RB and PHICH_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

For subframes configured as PRS subframes the PDSCH allocation defined in the OCNG pattern does not apply.

For subframes configured as ABS subframes the PDSCH and PMCH allocation defined in the OCNG pattern does not apply.

The system information is scheduled in the allocations reserved for the OCNG patterns, in the subframes not configured for MBSFN. For this purpose the number of the RB-s allocated with PDSCH defined in the OCNG pattern can be reduced as necessary.

## A.3.2.1.1OCNG FDD pattern 1: outer resource blocks allocation in 10 MHz

Table A.3.2.1.1-1: OP.1 FDD: OCNG FDD Pattern 1

## A.3.2.1.2OCNG FDD pattern 2: full bandwidth allocation in 10 MHz

Table A.3.2.1.2-1: OP.2 FDD: OCNG FDD Pattern 2

## A.3.2.1.3OCNG FDD pattern 3: outer resource blocks allocation in 1.4 MHz

Table A.3.2.1.3-1: OP.3 FDD: OCNG FDD Pattern 3

## A.3.2.1.4OCNG FDD pattern 4: full bandwidth allocation in 1.4 MHz

Table A.3.2.1.4-1: OP.4 FDD: OCNG FDD Pattern 4

## A.3.2.1.5OCNG FDD pattern 5: outer resource blocks allocation in 10 MHz (without MBSFN)

Table A.3.2.1.5-1: OP.5 FDD: OCNG FDD Pattern 5

## A.3.2.1.6OCNG FDD pattern 6: full bandwidth allocation in 10 MHz (without MBSFN)

Table A.3.2.1.6-1: OP.6 FDD: OCNG FDD Pattern 6

## A.3.2.1.7OCNG FDD pattern 7: full bandwidth allocation in 1.4 MHz (without MBSFN)

Table A.3.2.1.7-1: OP.7 FDD: OCNG FDD Pattern 7

## A.3.2.1.8OCNG FDD pattern 8: outer resource blocks allocation in 10 MHz for MBSFN ABS

Table A.3.2.1.8-1: OP.8 FDD: OCNG FDD Pattern 8

## A.3.2.1.9OCNG FDD pattern 9: full bandwidth allocation in 10 MHz for MBSFN ABS

Table A.3.2.1.9-1: OP.9 FDD: OCNG FDD Pattern 9

## A.3.2.1.10OCNG FDD pattern 10: outer resource blocks allocation in 10 MHz with user data in every subframe (without MBSFN)

Table A.3.2.1.10-1: OP.10 FDD: OCNG FDD Pattern 10

## A.3.2.1.11OCNG FDD pattern 11: outer resource blocks allocation in 20 MHz

Table A.3.2.1.11-1: OP.11 FDD: OCNG FDD Pattern 11

## A.3.2.1.12OCNG FDD pattern 12: full bandwidth allocation in 20 MHz

Table A.3.2.1.12-1: OP.12 FDD: OCNG FDD Pattern 12

## A.3.2.1.13OCNG FDD pattern 13: outer resource blocks allocation in 20 MHz (without MBSFN)

Table A.3.2.1.13-1: OP.13 FDD: OCNG FDD Pattern 13

## A.3.2.1.14OCNG FDD pattern 14: full bandwidth allocation in 20 MHz (without MBSFN)

Table A.3.2.1.14-1: OP.14 FDD: OCNG FDD Pattern 14

## A.3.2.1.15OCNG FDD pattern 15: outer resource blocks allocation in 5 MHz

Table A.3.2.1.15-1: OP.15 FDD: OCNG FDD Pattern 15

## A.3.2.1.16OCNG FDD pattern 16: full bandwidth allocation in 5 MHz

Table A.3.2.1.16-1: OP.16 FDD: OCNG FDD Pattern 16

## A.3.2.1.17OCNG FDD pattern 17: outer resource blocks allocation in 20 MHz with user data in every subframe (without MBSFN)

Table A.3.2.1.17-1: OP.17 FDD: OCNG FDD Pattern 17

## A.3.2.1.18OCNG FDD pattern 18: outer resource blocks allocation in 5 MHz (without MBSFN)

Table A.3.2.1.18-1: OP.18 FDD: OCNG FDD Pattern 18

## A.3.2.1.19OCNG FDD pattern 19: full bandwidth allocation in 5 MHz (without MBSFN)

Table A.3.2.1.19-1: OP.19 FDD: OCNG FDD Pattern 19

## A.3.2.1.20OCNG FDD pattern 20: outer resource blocks allocation in 5 MHz with user data in every subframe (without MBSFN)

Table A.3.2.1.20-1: OP.20 FDD: OCNG FDD Pattern 20

## A.3.2.1.21OCNG FDD pattern 21: Generic resource blocks allocation (without MBSFN)

Table A.3.2.1.21-1: OP.21 FDD: OCNG FDD Pattern 21

## A.3.2.1.22OCNG FDD pattern 22: Generic resource blocks allocation in 5MHz (without MBSFN)

Table A.3.2.1.22-1: OP.22 FDD: OCNG FDD Pattern 22

## A.3.2.2OCNG Patterns for TDD

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test). The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols without and with reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PDSCH reference channel, a transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PCFICH/PDCCH/PHICH reference channel which specifies the control region. The number of PDCCH OFDM symbols in the non-MBSFN subframes is the same as specified in the RMC used in the test. The number of PDCCH OFDM symbols in the MBSFN subframe is the maximal allowed according to TS 36.213 [16]. For any aggregation and PHICH allocation, the PDCCH and any unused PHICH groups are padded with resource element groups with a power level given by PDCCH_RA/RB and PHICH_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

For subframes configured as PRS subframes the PDSCH allocation defined in the OCNG pattern does not apply.

For subframes configured as ABS subframes the PDSCH and PMCH allocation defined in the OCNG pattern does not apply.

The system information is scheduled in the allocations reserved for the OCNG patterns, in the subframes not configured for MBSFN. For this purpose the number of the RB-s allocated with PDSCH defined in the OCNG pattern can be reduced as necessary.

## A.3.2.2.1OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz

Table A.3.2.2.1-1: OP.1 TDD: OCNG TDD Pattern 1 for 5ms downlink-to-uplink switch-point periodicity

Table A.3.2.2.1-2: OP.1 TDD: OCNG TDD Pattern 1 for special subframe configuration with 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.2OCNG TDD pattern 2: full bandwidth allocation in 10 MHz

Table A.3.2.2.2-1: OP.2 TDD: OCNG TDD Pattern 2 for 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.3OCNG TDD pattern 3: outer resource blocks allocation in 1.4 MHz

Table A.3.2.2.3-1: OP.3 TDD: OCNG TDD Pattern 3 for 5 ms downlink-to-uplink switch-point periodicity

## A.3.2.2.4OCNG TDD pattern 4: full bandwidth allocation in 1.4 MHz

Table A.3.2.2.4-1: OP.4 TDD: OCNG TDD Pattern 4 for 5 ms downlink-to-uplink switch-point periodicity

## A.3.2.2.5OCNG TDD pattern 5: outer resource blocks allocation in 10 MHz for MBSFN ABS

Table A.3.2.2.5-1: OP.5 TDD: OCNG TDD Pattern 5 for 5ms downlink-to-uplink switch-point periodicity

Table A.3.2.2.5-2: OP.5 TDD: OCNG TDD Pattern 5 for special subframe configuration with 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.6OCNG TDD pattern 6: full bandwidth allocation in 10 MHz for MBSFN ABS

Table A.3.2.2.6-1: OP.6 TDD: OCNG TDD Pattern 6 for 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.7OCNG TDD pattern 7: outer resource blocks allocation in 20 MHz

Table A.3.2.2.7-1: OP.7 TDD: OCNG TDD Pattern 7 for 5ms downlink-to-uplink switch-point periodicity

Table A.3.2.2.7-2: OP.7 TDD: OCNG TDD Pattern 7 for special subframe configuration with 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.8OCNG TDD pattern 8: full bandwidth allocation in 20 MHz

Table A.3.2.2.8-1: OP.8 TDD: OCNG TDD Pattern 8 for 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.9OCNG TDD pattern 9: outer resource blocks allocation in 5 MHz

Table A.3.2.2.9-1: OP.9 TDD: OCNG TDD Pattern 9 for 5ms downlink-to-uplink switch-point periodicity

Table A.3.2.2.9-2: OP.9 TDD: OCNG TDD Pattern 9 for special subframe configuration with 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.10OCNG TDD pattern 10: full bandwidth allocation in 5 MHz

Table A.3.2.2.10-1: OP.10 TDD: OCNG TDD Pattern 10 for 5ms downlink-to-uplink switch-point periodicity

## A.3.2.2.11OCNG TDD pattern 11: Generic resource blocks allocation (without MBSFN)

Table A.3.2.2.11-1: OP.11 TDD: OCNG TDD Pattern 11

## A.3.2.3OCNG Patterns for Narrowband IoT

The following Narrowband OCNG patterns (NOCNG) are used for modelling allocations to UEs not under test in a Narrowband IoT cell. Depending on scenario, allocations may be for UEs of category NB1only, or for UEs of category NB1 as well as of other categories. The former is applicable to guard-band and stand-alone deployments of Narrowband IoT, whereas the latter is applicable to in-band deployment. In order to allow different power levels for the LTE cell and the Narrowband IoT cell, a distinction is made between OCNG and NOCNG where the latter is used for category NB1 UEs and the former is used for other UE categories.

OCNG in the LTE cell is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH-to-RS EPRE ratio in OFDM symbols with and without LTE cell-specific reference symbols, respectively. The relative power, which is used for modelling boosting per virtual LTE UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual LTE UE.

Moreover in each test case NOCNG is expressed by parameters NOCNG_RA and NOCNG_RB which together with a relative power level () specifies the <channel>-to-RS EPRE ratio in OFDM symbols with and without Narrowband reference symbols (NB-RS), respectively. The relative power, which is used for modelling boosting per virtual UE category NB1 allocation, is expressed by:

where  denotes the relative power level of the k:th virtual NB-IoT UE, and channel may be either of NPDCCH and NPDSCH.

The parameter settings of OCNG_RA, OCNG_RB, NOCNG_RA, NOCNG_RB and the set of relative power levels are chosen such that when also taking allocations to the UE category NB1 under test into account, as given by a NPDCCH and NPDSCH reference channels, a transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

## A.3.2.3.1Narrowband IoT OCNG FDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell

Table A.3.2.3.1-1: NOP.1 FDD: OCNG FDD Pattern 1

## A.3.2.3.2Narrowband IoT OCNG FDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell

Table A.3.2.3.2-1: NOP.2 FDD: OCNG FDD Pattern 2

## A.3.2.3.3Narrowband IoT OCNG FDD pattern 3: standalone NB-IoT

Table A.3.2.3.3-1: NOP.3 FDD: OCNG FDD Pattern 3

## A.3.2.3.4Narrowband IoT OCNG FDD pattern 4: In-band NB-IoT in 5 MHz EUTRAN cell

Table A.3.2.3.4-1: NOP.4 FDD: OCNG FDD Pattern 4

## A.3.2.3.5Narrowband IoT OCNG FDD pattern 5: guard band NB-IoT in 5 MHz EUTRAN cell

Table A.3.2.3.5-1: NOP.5 FDD: OCNG FDD Pattern 5

## A.3.2.3.6Narrowband IoT OCNG TDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell

Table A.3.2.3.6-1: NOP.1 TDD: OCNG TDD Pattern 1 for uplink-downlink configurations 1 and 2

## A.3.2.3.7Narrowband IoT OCNG TDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell

Table A.3.2.3.7-1: NOP.2 TDD: OCNG TDD Pattern 2 for uplink-downlink configurations 1 and 2

## A.3.2.3.8Narrowband IoT OCNG TDD pattern 3: standalone NB-IoT

Table A.3.2.3.8-1: NOP.3 TDD: OCNG TDD Pattern 3 for uplink-downlink configurations 1 and 2

## A.3.2.3.9Narrowband IoT OCNG FDD pattern 6: In-band NB-IoT in 5 MHz NTN NR cell

Table A.3.2.3.9-1: NOP.6 FDD: OCNG FDD Pattern 6

## A.3.2.3.10Narrowband IoT OCNG NTN TDD pattern 4: standalone NB-IoT

Table A.3.2.3.10-1: NOP.4 TDD: OCNG TDD Pattern 4

## A.3.2.4OCNG Patterns for V2X sidelink

The following V2X sidelink OCNG patterns (VOCNG) are used for modelling allocations to virtual V2X UEs (which are not under test). The OCNG pattern for each subframe specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case VOCNG is expressed by parameters VOCNG_RA and VOCNG_RB which together with a relative power level () specifies the PSSCH EPRE-to-RS EPRE ratios in OFDM symbols without and with reference symbols, respectively. The relative power, which is used for modelling boosting per virtual V2X UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual V2X UE. The parameter settings of VOCNG_RA, VOCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PSSCH reference channel.

Moreover the VOCNG pattern is accompanied by a PSCCH reference channel which specifies the control region. The number of PSCCH OFDM symbols in all subframes is the same as specified in the RMC used in the test.

## A.3.2.4.1V2X sidelink OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz

Table A.3.2.4.1-1: VOP.1 HD: OCNG TDD Pattern 1

## A.3.2.4.2V2X sidelink OCNG TDD pattern 2: outer resource blocks allocation in 10 MHz

Table A.3.2.4.2-1: VOP.2 HD: OCNG TDD Pattern 2

## A.3.3Reference DRX Configurations

Table A.3.3-1: Reference DRX Configurations

## A.3.4ABS Transmission Configurations

## A.3.4.1Non-MBSFN ABS Transmission Configurations

## A.3.4.1.1Non-MBSFN ABS Transmission, 1x2 antenna with PBCH

Table A.3.4.1.1-1: Transmission configuration with non-MBSFN ABS, 1x2 with PBCH

## A.3.4.1.2Non-MBSFN ABS Transmission, 2x2 antenna without PBCH

Table A.3.4.1.2-1: Transmission configuration #1 with non-MBSFN ABS, 2x2 without PBCH

Table A.3.4.1.2-2: Transmission configuration #2 with non-MBSFN ABS, 2x2 without PBCH

## A.3.4.2MBSFN ABS Transmission Configurations

## A.3.4.2.1MBSFN ABS Transmission, 1x2 antenna

Table A.3.4.2.1-1: Transmission configuration with MBSFN ABS, 1x2

## A.3.4.2.2MBSFN ABS Transmission, 2x2 antenna

Table A.3.4.2.2-1: Transmission configuration #1 with MBSFN ABS, 2x2

Table A.3.4.2.2-2: Transmission configuration # 2 with MBSFN ABS, 2x2

## A.3.5Impact of Reference Sensitivity Degradation with Carrier Aggregation on Test Cases

## A.3.5.1Impact of Reference Sensitivity Degradation due to Insertion Loss

For a UE supporting inter-band carrier aggregation configuration with uplink in one E-UTRA band, if there is a relaxation of receiver sensitivity ΔRIB,c>0 dB as defined in TS 36.101 [5], 7.3.1-1A, there is no adjustment of test parameters in the tests specified in TS 36.133 when ΔRIB,c  1 dB.

## A.3.6Carrier Aggregation Test Cases with Different Channel Bandwidth Combinations

## A.3.6.1Introduction

In Annex A carrier aggregation test cases may be defined with different channel bandwidth combinations to verify the same RRM requirement.

If multiple carrier aggregation test cases with different channel bandwidth combinations are defined to verify the same RRM requirement that is channel bandwidth independent, then the UE needs to be tested only with one bandwidth combination out of the bandwidth combination sets supported by that UE.

## A.3.7Test Cases with Different Channel Bandwidths

## A.3.7.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for single carrier operation.

## A.3.7.2Principle of testing

Test cases defined for 5MHz channel bandwidth that reference this clause are applicable to UEs that support only bands within band group FDD_N.

## A.3.8Antenna Configuration

Unless otherwise specified, E-UTRA FDD or E-UTRA TDD cells in all RRM Test cases in AWGN propagation condition are configured with Antenna Configuration 1x2.

## A.3.8.1Antenna connection for 4 Rx capable UEs

## A.3.8.1.1 Introduction

All tests in sections A.4 to A.9 are specified for UEs supporting either category 0 (1RX) or 2RX. In this section, the antenna connection method for applying 2RX tests to UEs supporting 4RX antenna ports is specified. No tests are currently specified in section A.4-A.9 which are applicable only to 4RX antenna ports, so 4RX capable UEs are always tested by reusing tests which were originally specified for 2RX UEs.

## A.3.8.1.2 Principle of testing

## A.3.8.1.2.1 Single carrier tests

For 4RX capable UEs supporting at least one 2RX band, all single carrier tests specified in section A.4 to A.8 shall be tested on any band where 2RX is supported with the antenna connection specified in A.8.3.1.2.3. For single carrier tests specified in section A.9, all tests shall be tested with the antenna connection specified in A.3.8.1.2.3 for bands where 2RX is supported, and the antenna connection specified in A.3.8.1.2.4 for bands where 4RX is supported.

For 4RX capable UEs which do not support any 2RX band, all tests specified in sections A.4 to A.9 shall be tested using the antenna connection specified in section A.3.8.1.2.4. For radio link monitoring tests, the SNR levels are modified according to table A.3.8.1.2.1-1 and table A.3.8.1.2.1-2.

Table A.3.8.1.2.1-1 Modified parameters for RLM out of sync testing with 4 RX antenna connection

Table A.3.8.1.2.1-2 Modified parameters for RLM in sync single carrier testing with 4 RX antenna connection

## A.3.8.1.2.2Carrier aggregation and Dual connectivity tests

All carrier aggregation and dual connectivity tests are performed using the antenna connection in section A.3.8.1.2.3 for the PCell antenna connection if the PCell is on a band where 2RX is supported or the antenna connection in A.3.8.1.2.4 for the PCell antenna connection if the PCell is on a band where 4RX is supported.

All carrier aggregation and dual connectivity tests are performed using the antenna connection in section A.3.8.1.2.3 for the SCell or PSCell antenna connection if an SCell or PSCell is on band where 2RX is supported or the testing procedure in A.3.8.1.2.4 for the SCell or PSCell antenna connection if an SCell or PSCell is on a band where 4RX is supported.

For dual connectivity radio link monitoring tests with the PSCell on a band where 4RX is supported, the PSCell SNR levels are modified according to table A.3.8.1.2.2 -1 and table A.3.8.1.2.2 -2.

Tabke A.3.8.1.2.1-1 Modified parameters for dual connectivity RLM out of sync testing with 4 RX antenna connection

Table A.3.8.1.2.1-1 Modified parameters for RLM out of sync testing with 4 RX antenna connection

## A.3.8.1.2.3Antenna connection for bands where 2RX is supported

For bands where 2RX is supported, it is left to the UE declaration and AP configuration to decide which 2 of the 4 Rx ports are connected with data source from system simulator. The remaning 2 Rx ports shall be connected with zero input. No test parameters or requirements are modified.

## A.3.8.1.2.4Antenna connection for bands where 4RX is supported

For bands where 4RX is supporetd, all 4 Rx are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring theresholds described in sections A.3.8.1.2.1 and A.3.8.1.2.2, no test parameters or requirements are modified.

## A.3.8.2Antenna connection for 8 Rx capable UEs

## A.3.8.2.1Introduction

In this clause, the antenna connection method for applying 2RX tests or 4RX tests to UEs supporting 8RX antenna ports is specified. No tests are currently specified in clause A.4-A.9 which are applicable only to 8RX antenna ports, so 8RX capable UEs are always tested by reusing tests which were originally specified for 2RX UEs or 4Rx UEs.

## A.3.8.2.2Principle of testing

## A.3.8.2.2.1Single carrier tests

For 8RX capable UEs supporting at least one 2RX band, all single carrier tests specified in clause A.4 to A.8 shall be tested on any band where 2RX is supported with the antenna connection specified in A.8.3.2.2.3. For single carrier tests specified in clause A.9, all tests shall be tested with the antenna connection specified in A.3.8.2.2.3 for bands where 2RX is supported, and the antenna connection specified in A.3.8.2.2.5 for bands where 8RX is supported.

For 8RX capable UEs supporting at least one 4RX band but without supporting any 2RX band, all single carrier tests specified in clause A.4 to A.8 shall be tested on any band where 4RX is supported with the antenna connection specified in A.3.8.2.2.4. For single carrier tests specified in clause A.9, all tests shall be tested with the antenna connection specified in A.3.8.2.2.4 for bands where 4RX is supported, and the antenna connection specified in A.3.8.2.2.8 for bands where 8RX is supported. For radio link monitoring tests, the SNR levels are modified according to table A.3.8.1.2.1-1 and table A.3.8.1.2.1-2.

For 8RX capable UEs which do not support any 2RX or 4RX band, all tests specified in clauses A.4 to A.9 shall be tested using the antenna connection specified in clause A.3.8.1.2.5. For radio link monitoring tests, the SNR levels are modified according to table A.3.8.1.2.1-1 and table A.3.8.1.2.1-2.

## A.3.8.2.2.2Carrier aggregation and Dual connectivity tests

All carrier aggregation and dual connectivity tests are performed using the antenna connection in clause A.3.8.2.2.3 for the PCell antenna connection if the PCell is on a band where 2RX is supported or the antenna connection in A.3.8.2.2.4 for the PCell antenna connection if the PCell is on a band where 4RX is supported but without supporting any 2RX band or the antenna connection in A.3.8.2.2.5 for the PCell antenna connection if the PCell is on a band where 8RX is supported.

All carrier aggregation and dual connectivity tests are performed using the antenna connection in clause A.3.8.2.2.3 for the SCell or PSCell antenna connection if an SCell or PSCell is on band where 2RX is supported or the testing procedure in A.3.8.2.2.4 for the SCell or PSCell antenna connection if an SCell or PSCell is on a band where 4RX is supported but without supporting any 2RX band or the testing procedure in A.3.8.2.2.5 for the SCell or PSCell antenna connection if an SCell or PSCell is on a band where 8RX is supported.

For dual connectivity radio link monitoring tests with the PSCell on a band where 8RX is supported, the PSCell SNR levels are modified according to table A.3.8.1.2.2 -1 and table A.3.8.1.2.2 -2.

## A.3.8.2.2.3Antenna connection for bands where 2RX is supported

For bands where 2RX is supported, it is left to the UE declaration and AP configuration to decide which 2 of the 8 Rx ports are connected with data source from system simulator. The remaning 6 Rx ports shall be connected with zero input. No test parameters or requirements are modified.

## A.3.8.2.2.4Antenna connection for bands where 4RX is supported

For bands where 4RX is supporetd, it is left to the UE declaration and AP configuration to decide which 4 of the 8 Rx ports are connected with data source from system simulator. The remaning 4 Rx ports shall be connected with zero input. Except for the modifications to radio link monitoring theresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2, no test parameters or requirements are modified.

## A.3.8.2.2.5Antenna connection for bands where 8RX is supported

For bands where 8RX is supporetd, all 8 Rx are connected with data source from system simulator. The system simulator shall provide independent noise and fading (low correlation) for each antenna port. Except for the modifications to radio link monitoring theresholds described in clauses A.3.8.1.2.1 and A.3.8.1.2.2, no test parameters or requirements are modified.

## A.3.9Carrier Aggregation Test Cases with Different Duplex Modes

## A.3.9.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for carrier aggregation.

## A.3.9.2Principle of testing

In Annex A carrier aggregation test cases may be defined for different duplex modes or combination of duplex modes (E-UTRA FDD, E-UTRA TDD and E-UTRA TDD-FDD) to verify the same RRM requirement.

If multiple carrier aggregation test cases are defined for different duplex modes (E-UTRA FDD or E-UTRA TDD) or for combination of duplex modes (E-UTRA TDD-FDD) to verify the same RRM requirement which is independent of the duplex mode and is identical for different duplex modes or combination of duplex modes, then from UE the performance point of view the test coverage can be considered fulfilled by executing only the corresponding test case(s) with one of the duplex modes supported by the UE.

## A.3.10Carrier Aggregation Test Cases with Different CA Configurations

## A.3.10.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for carrier aggregation.

## A.3.10.2Principle of testing

In Annex A carrier aggregation test cases may be defined for two CCs as well as for more than two CCs to verify the same RRM requirement.

If multiple carrier aggregation test cases are defined for two CCs as well as for more than two CCs to verify the same RRM requirement, then from the UE performance point of view the test coverage can be considered fulfilled by executing only the test cases with the maximum number of CCs supported by the UE.

Editor’s note: whether it is sufficient to test for any one of the band combinations supported by the UE is FFS.

## A.3.11Test Cases for Synchronous and Asynchronous Dual Connectivity

## A.3.11.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for dual connectivity (DC) operation in synchronous and asynchronous scenarios.

## A.3.11.2Principle of Testing

In Annex A test cases may be defined in both synchronous DC and asynchronous DC scenarios to verify the same RRM requirement.

If test cases are defined in both synchronous and asynchronous DC scenarios to verify the same RRM requirement then the UE capable of both synchronous and asynchronous DC operations needs to be tested with one of the tests in either synchronous or asynchronous DC scenarios.

## A.3.12Proximity-based Services

## A.3.12.1Introduction

This clause also defines the principle and the reference configurations that are applicable to test cases verifying RRM core requirements for ProSe Direct Discovery and ProSe Direct Communication.

## A.3.12.2Reference DRX configurations for ProSe tests

Table A.3.12.2-1: Reference DRX Configurations

## A.3.12.3Test Cases with Different Channel Bandwidths

## A.3.12.3.1Introduction

This clause defines a principle which is applicable to test cases verifying ProSe RRM requirements with different channel bandwidths.

## A.3.12.3.2Principle of testing

Some ProSe test cases are defined for different channel bandwidths to verify the same RRM requirement.

If test cases with different channel bandwidth are defined to verify the same RRM requirement then the UE is required to pass the test cases only with one of the channel bandiwdths.

## A.3.12.4Reference resource pool configurations for ProSe Direct Discovery

Table A.3.12.4-1: ProSe Direct Discovery configuration for E-UTRA FDD (Configuration #1)

Table A.3.12.4-2: ProSe Direct Discovery configuration for E-UTRA FDD (Configuration #2)

Table A.3.12.4-3: ProSe Direct Discovery configuration for E-UTRA TDD Config 0 (Configuration #3)

Table A.3.12.4-4: ProSe Direct Discovery configuration for E-UTRA FDD for PS discovery (Configuration #4)

Table A.3.12.4-5: ProSe Direct Discovery configuration for E-UTRA FDD for inter-frequency discovery (Configuration #5)

## A.3.12.5Reference resource pool configurations for ProSe Direct Communication

Table A.3.12.5-1: ProSe Direct Communication configuration for E-UTRA FDD (Configuration #1)

Table A.3.12.5-2: ProSe Direct Communication pre-configuration for E-UTRAN FDD for out-of-network coverage operation (Configuration #2)

## A.3.12.6Reference Measurement Channels for ProSe Direct Discovery

## A.3.12.6.1FDD

Table A.3.12.6-1: PSDCH Reference Measurement Channels for FDD

## A.3.12.7Reference measurement channels for ProSe Direct Communication

## A.3.12.7.1FDD

Table A.3.12.7-1: PSCCH Reference Measurement Channels for FDD

Table A.3.12.7-1: PSSCH Reference Measurement Channels for FDD

## A.3.12.8ProSe Receive Traffic Generator

This clause defines the configuration for active Sidelink UEs used to generate receive traffic in ProSe RRM tests.

## A.3.12.8.1ProSe Direct Communication Receive Traffic Generator for FDD

Table A.3.12.8.1-1: Active Sidelink UE configuration for ProSe Direct Communication

## A.3.12.8.2ProSe Direct Discovery Receive Traffic Generator for FDD

Table A.3.12.8.2-1: Active Sidelink UE configuration for ProSe Direct Discovery

## A.3.13Time Offset between Cells

## A.3.13.1Introduction

In Annex A in some test cases a parameter called, ‘time offset between cells’ is used. The meaning of this parameter is defined in this clause.

## A.3.13.2Definition

Unless explicitly stated otherwise, the time offset between cells for a pair of cells is defined as the difference between radio frame start timings of the pair of cells.

## A.3.14Carrier Aggregation under operation with Frame Structure 3 Test Cases with Different Duplex Modes

## A.3.14.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for carrier aggregation with at least one Scell under operation with Frame Structure 3.

## A.3.14.2Principle of testing

In Annex A, tests for carrier aggregation with at least one Scell under operation with frame structure 3are specified with both an FDD and a TDD Pell to verify the same RRM requirement. If both types of tests are relevant to a UE considering supported CA bands, the test coverage can be considered fulfilled by executing either the tests with FDD PCell or the tests with TDD PCell and the UE is not required to pass both tests.

## A.3.15Dual connectivity test cases with different combination of duplex mode

## A.3.15.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for dual connectivity (DC) operation with different combination of duplex modes.

## A.3.15.2Principle of testing

If multiple dual connectivity test cases are defined for different combination of duplex modes (E-UTRA FDD-FDD, E-UTRA TDD-TDD and E-UTRA TDD-FDD) to verify the same RRM requirement which is independent of the combination of duplex modes and is identical for different combination of duplex modes, then from UE the performance point of view the test coverage can be considered fulfilled by executing only the corresponding test case(s) with one of the combination of duplex modes supported by the UE.

## A.3.16Reference PRACH Configurations

Table A.3.16-1: PRACH configuration parameters

## A.3.17Listen before talk model

## A.3.17.1Introduction

In some RRM test cases for FS3, a listen before talk (LBT) model is specified. The intention of the LBT model is to emulate using test equipment the behaviour of an FS3 eNB which performs channel measurement to check that the channel is clear prior to performing downlink transmission.

## A.3.17.2Definition

Prior to each DMTC window, the test equipment shall determine whether to transmit a discovery reference signal (DRS) during the DMTC window with probability P=0.75. In many cases the test requirement depends on the number of configured discovery signal occasions which are not available during the test, so the test equipment shall track how many DRS are not transmitted during the test period. If the test equipment determines that it shall transmit a DRS, then the timing of the DRS transmission within the DMTC window is randomly selected from the set of possible DRS transmission signal timings, such that there is an equal probability of any valid DRS timing.

For non DRS downlink transmission bursts, if transmission occurred in the previous subframe, transmission is muted for a duration of one subframe. Additionaly, if the start time of the candidate transmission burst is within 8 subframes of the start of the DMTC window, transmission is not performed. Otherwise

The length of the transmission burst in subframes is defined as N. The burst transmission format is determined according to the steps below:

1.Select N randomly from a given set of the number of subframes S1={1,3,5,8} with equal probability as the total length of burst transmission format.

2.A uniform random variable from 0 to 1 is generated. If the random variable is less than P=0.75, a burst of N fully occupied subframes is transmitted. Otherwise, the burst transmission is muted and the muting duration is the same as the number N of subframes for determined burst format.

## A.3.18Reference NPRACH Configurations

Table A.3.18-1, A.3.18-2 and A.3.18.3 define the reference NB-IoT PRACH configurations for a NB-IoT RRM test case where the UE is required to transmit NPRACH during the testing procedure, but the testing purpose of the RRM test case does not include testing NPRACH performance.

Table A.3.18-1: NPRACH.R-1: HD-FDD Reference NPRACH Configuration

Table A.3.18-2: NPRACH.R-2: TDD Reference NPRACH Configuration

Table A.3.18-3: NPRACH.R-3: NTN-TDD Reference NPRACH Configuration

## A.3.19Dual connectivity test cases with different bandwidth combinations

## A.3.19.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for dual connectivity (DC) operation with different bandwidth combinations.

## A.3.19.2Principle of testing

If multiple dual connectivity test cases with different channel bandwidth combinations are defined to verify the same RRM requirement that is channel bandwidth independent, then the UE needs to be tested only with one bandwidth combination out of the bandwidth combination sets supported by that UE.

## A.3.20Category M1 UE Test Cases

## A.3.20.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for Category M1 UE in both CEModeA and CEModeB.

## A.3.20.2Principle of Cat-M1 UE Testing

In Annex A Cat-M1 UE test cases may be defined for both CEModeA and CEModeB to verify the same type of RRM requirement.

If test cases are defined in both CEModeA and CEmodeB in order to verify the same type of RRM requirement then the UE capable of CEModeB needs to be tested for the corresponding test(s) defined in CEModeA and/or in CEModeB according to the applicability rules defined in Table A.3.20.2-1.

The UE which is not capable of CEModeB shall be tested for all CEModeA test cases defined in Annex A.

In test cases defined for CEModeB, test equipment shall transmit PBCH with 5 repetitions as specified in section 6.6.4 of TS 36.211 [16].

Table A.3.20.2-1: Test case applicability rules for category M1 UE in CEModeA and CEModeB

## A.3.20.3Principle of Cat-M1 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps

For the Cat-M1 UE, capable of supporting measurement gaps specified in Table 8.1.2.1-3 and requiring gaps for inter-frequency RSTD measurements, and which can be configured with applicable measurement gaps specified in Table 8.1.2.1-1 or Table 8.1.2.1-3, in order to verify inter-frequency RSTD measurement period with measurement gaps, it is sufficient to verify the RSTD measurement period requirements only under the applicable measurement gaps specified in Table 8.1.2.1-3, for each of the CEModeA and CEModeB.

## A.3.21V2V Sidelink Communication on Dedicated V2V Carrier

## A.3.21.1Introduction

This clause also defines the principle and the reference configurations that are applicable to test cases verifying RRM core requirements for V2V sidelink communication on dedicated V2V carrier.

## A.3.21.2Reference resource pool configurations for V2V Sidelink Communication

Table A.3.21.2-1: Pre-configuration for V2V Sidelink Communication

## A.3.21.3Reference measurement channels for V2V Sidelink Communication

Table A.3.21.3-1: PSCCH Reference Measurement Channels

Table A.3.21.3-2: PSSCH Reference Measurement Channels

## A.3.22Category 1bis UE Test Cases

## A.3.22.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for Category 1bis UE.

## A.3.22.2Principle of Category 1bis UE Testing

In Annex A, tests in table A.3.22.2-1 defined for Category ≥1 UE with 2 Rx antenna are applicable to Category 1bis UE with 1 Rx antenna. Unless otherwise specified, same test configurations are used except for propagation channel change to 1x1 or 2x1 according to number of Tx antennas. For RSRP and RSRQ measurement accuracy test, corresponding measurement accuracy requirement for Category 1bis UE is specified in the table. For band dependent RRM tests defined in section A.9, only subset of bands that are defined for Cat.1bis UE are applicable.

Table A.3.22.2-1: Test cases applicable to category 1bis UE

## A.3.23Category NB2 UE Test Cases

## A.3.23.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for Category NB2 UE in both normal and enhanced coverage.

## A.3.23.2Principle of Category NB2 UE Testing

In Annex A, test cases in table A.3.23.2-1 defined for Category NB1 UE are applicable to Category NB2 UE.

Table A.3.23.2-1: Test cases applicable to Category NB2 UE

## A.3.24V2X sidelink communication

## A.3.24.1Introduction

This clause also defines the principle and the reference configurations that are applicable to test cases verifying RRM core requirements for V2X sidelink communication.

## A.3.24.2Reference resource pool configurations for V2X Sidelink Communication

Table A.3.24.2-1: Pre-configuration for V2X Sidelink Communication (Configuration #1)

Table A.3.24.2-2: V2X sidelink Communication configuration for E-UTRAN (Configuration #2)

## A.3.24.3Reference measurement channels for V2X Sidelink Communication

Table A.3.24.3-1: PSCCH Reference Measurement Channels

Table A.3.24.3-2: PSSCH Reference Measurement Channels

Table A.3.24.3-3: PSSCH Reference Measurement Channels

## A.3.25Category M2 UE Test Cases

## A.3.25.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for Category M2 UE in both CEModeA and CEModeB.

## A.3.25.2Principle of Cat-M2 UE Testing

In Annex A Cat-M2 UE test cases may be defined for both CEModeA and CEModeB to verify the same type of RRM requirement.

If test cases are defined in both CEModeA and CEmodeB in order to verify the same type of RRM requirement then the UE capable of CEModeB needs to be tested for the corresponding test(s) defined in CEModeA and/or in CEModeB according to the applicability rules defined in Table A.3.25.2-1.

The UE which is not capable of CEModeB shall be tested for all CEModeA test cases defined in Annex A.

Table A.3.25.2-1: Test case applicability rules for category M2 UE in CEModeA and CEModeB

## A.3.25.3Principle of Cat-M2 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps

For the Cat-M2 UE configured with 1.4 MHz UE RF bandwidth, capable of supporting measurement gaps specified in Table 8.1.2.1-3 and requiring gaps for inter-frequency RSTD measurements, and which can be configured with applicable measurement gaps specified in Table 8.1.2.1-1 or Table 8.1.2.1-3, in order to verify inter-frequency RSTD measurement period with measurement gaps it is sufficient to verify the requirement only under the applicable measurement gaps specified in Table 8.1.2.1-3, for each of the CEModeA and CEModeB.

For the Cat-M2 UE in CEModeB configured with 5 MHz UE RF bandwidth, capable of supporting measurement gaps specified in Table 8.1.2.1-3 and requiring gaps for inter-frequency RSTD measurements, and which can be configured with applicable measurement gaps specified in Table 8.1.2.1-1 or Table 8.1.2.1-3, in order to verify inter-frequency RSTD measurement period with measurement gaps it is sufficient to verify the requirement only under the applicable measurement gaps specified in Table 8.1.2.1-3.

## A.3.26sTTI and processing time reduction test cases with different sTTI/processing time reduction scheme

## A.3.26.1Introduction

This clause defines a principle which is applicable to RRM performance requirement  test cases with different TTI duration and processing time for a UE configured with ShortTTI-r15 or ShortProcessingTime=TRUE.

## A.3.26.2Principle of testing

If multiple test cases defined for different TTI duration and processing time are applicable to a UE configured with ShortTTI-r15 or ShortProcessingTime=TRUE to verify the timing advance adjustment delay, from the UE performance point of view the test coverage can be considered fulfilled by executing only the test case with the shortest TTI duration and processing time among all the TTI duration and processing time supported by the UE. For a UE capable of ShortTTI-r15 and dl-STTI-Length-r15=subslot configuration and ProcessingTimelineSet-r15=set1, coverage is fulfilled by executing only the test with configured ShortTTI-r15, dl-STTI-Length-r15= subslot, and proc-Timeline-r15= nplus4set1, and for a UE capable of ShortTTI-r15 and dl-STTI-Length-r15=subslot configuration and ProcessingTimelineSet-r15=set2, coverage is fulfilled by executing only the test with configured ShortTTI-r15, dl-STTI-Length-r15= subslot, and proc-Timeline-r15=nplus6set2.

## A.3.27LTE INACTIVE Cell Re-selection Test Cases

## A.3.27.1Introduction

This clause defines a principle which is applicable to test cases verifying RRM requirements for INACTIVE mode cell-reselection under connectivity to 5GC.

## A.3.27.2Principle of INACTIVE cell re-selection Testing

For a UE supporting RRC_INACTIVE state, the requirements in Section 4A are considered fulfilled if the UE passes the cell-reselection test cases defined in Section A.4 for RRC_IDLE state.

## A.3.28Testing related to Satellite access

## A.3.28.1Introduction

In annex A test cases are defined for verifying various type of RRM requirements related to satellite access.

## A.3.28.2Principle of testing GSO and NGSO scenarios

In Annex A, RRM test cases related to satellite access are defined for both GSO and NGSO. The testing principle for these test cases is as follows:

-A UE capable of GSO only is required to pass the test cases with GSO.

-A UE capable of NGSO only is required to pass the test cases with NGSO.

-A UE capable of both GSO and NGSO is required to pass the test cases with NGSO only.

Support of GSO and NGSO scenario is indicated via ntn-ScenarioSupport-r17.

## A.3.28.2Principle of testing different RRM requirements

In Annex A, RRM test cases related to satellite access are defined for all applicable RRM requirements. The testing principle for these test cases is as follows:

-A UE capable of NTN only is required to pass all the test cases defined in clauses A.13 and/or A.14.

-A UE capable of both TN and NTN is required to pass the test cases for NTN specific requirements in Table A.3.28.2-1.

Table A.3.28.2-1: Test cases for NTN specific requirements

## A.3.28.3Principle of testing different ephemeris formats

Satellite access RRM test cases are defined such that satellite ephemeris information is sent to UE in each test case using position and velocity state vectors format.

## A.3.28.4General setup for SIB31/SIB-31-NB

The general parameters for SIB31/SIB31-NB setup is specified in Table A.3.28.4-1.

Table A.3.28.4-1: General setup for SIB31/SIB31-NB

## A.3.28.5Satellite specific parameters configuration

## A.3.28.5.1Satellite specific configuration for serving cell

The general parameters for SIB31 setup for serving satellite are specified in Table A.3.28.5.1-1.

Table A.3.28.5.1-1: SIB31/SIB31-NB parameters setup for Serving satellite

## A.3.28.5.2Satellite specific configuration for neighbour cell

The general parameters for SIB33 setup for neighbor cells in both serving and neighbour satellites are specified in Table A.3.28.5.2-1.

Table A.3.28.5.2-1: SIB33/SIB33-NB parameters setup for neighbour cell

## A.4E-UTRAN RRC_IDLE state

## A.4.2Cell Re-Selection

## A.4.2.1E-UTRAN FDD – FDD Intra frequency case

## A.4.2.1.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.1.1-1 and A.4.2.1.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.1.1-1: General test parameters for FDD intra frequency cell reselection test case

Table A.4.2.1.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case in AWGN

## A.4.2.1.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: TevaluateFDD,intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

TevaluateFDD,intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.2E-UTRAN TDD – TDD Intra frequency case

## A.4.2.2.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency cell reselection requirements specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.2.1-1 and A.4.2.2.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.2.1-1: General test parameters for TDD intra frequency cell re-selection test case

Table A.4.2.2.1-2: Cell specific test parameters for TDD intra frequency cell re-selection test case in AWGN

## A.4.2.2.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,E-UTRAN_ intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.3E-UTRAN FDD – FDD Inter frequency case

## A.4.2.3.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency cell reselection requirements specified in clause 4.2.2.4.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.3.1-1 and A.4.2.3.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.3.1-1: General test parameters for FDD-FDD inter frequency cell re-selection test case

Table A.4.2.3.1-2: Cell specific test parameters for FDD-FDD inter-frequency cell reselection test case in AWGN

## A.4.2.3.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateFDD,inter + TSI , and to lower priority cell can be expressed as: TevaluateFDD,inter + TSI,

Where:

Thigher_priority_searchSee clause 4.2.2

TevaluateFDD,interSee Table 4.2.2.4-1 in clause 4.2.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.4E-UTRAN FDD – TDD Inter frequency case

## A.4.2.4.1Test Purpose and Environment

This test is to verify the requirement for the FDD-TDD inter-frequency cell reselection requirements specified in clause 4.2.2.4.

The test scenario comprises of 1 E-UTRA FDD cell and 1 E-UTRA TDD cell as given in tables A.4.2.4.1-1 and A.4.2.4.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.4.1-1: General test parameters for FDD-TDD inter frequency cell re-selection test case

Table A.4.2.4.1-2: Cell specific test parameters for FDD-TDD inter-frequency cell reselection test case in AWGN

## A.4.2.4.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.5E-UTRAN TDD – FDD Inter frequency case

## A.4.2.5.1Test Purpose and Environment

This test is to verify the requirement for the TDD-FDD inter-frequency cell reselection requirements specified in clause 4.2.2.4.

The test scenario comprises of 1 E-UTRA TDD cell and 1 E-UTRA FDD cell as given in tables A.4.2.5.1-1 and A.4.2.5.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.5.1-1: General test parameters for TDD-FDD inter frequency cell re-selection test case

Table A.4.2.5.1-2: Cell specific test parameters for TDD-FDD inter-frequency cell reselection test case in AWGN

## A.4.2.5.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.6E-UTRAN TDD – TDD: Inter frequency case

## A.4.2.6.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter-frequency cell reselection requirements specified in clause 4.2.2.4.

The test scenario comprises of 2 E-UTRA TDD cells on 2 different carriers as given in tables A.4.2.6.1-1 and A.4.2.6.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.6.1-1: General test parameters for TDD-TDD inter frequency cell reselection test case

Table A.4.2.6.1-2: Cell specific test parameters for TDD-TDD inter-frequency cell reselection test case in AWGN

## A.4.2.6.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.7E-UTRAN FDD – FDD Inter frequency case in the existence of non-allowed CSG cell

## A.4.2.7.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency cell reselection requirements specified in clause 4.2.2.4 when there is the interference from non-allowed CSG cell and the layers have equal priority.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers and 1 non-allowed E-UTRA FDD CSG cell as given in tables A.4.2.7.1-1 and A.4.2.7.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 3 is a non-allowed CSG cell. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.7.1-1: General test parameters for FDD-FDD inter frequency cell re-selection test case with non-allowed CSG cell

Table A.4.2.7.1-2: Cell specific test parameters for FDD-FDD inter frequency cell re-selection test case with non-allowed CSG cell

## A.4.2.7.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

The probability of reselection from Cell 2 to Cell 1 during T3 observed during testing shall be less than 10%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter + TSI,

Where:

Tdetect,EUTRAN_InterSee Table 4.2.2.4-1 in clause 4.2.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell in the test case.

## A.4.2.8E-UTRAN TDD – TDD Inter frequency case in the existence of non-allowed CSG cell

## A.4.2.8.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter-frequency cell reselection requirements specified in clause 4.2.2.4 when there is the interference from non-allowed CSG cell and the layers have equal priority.

The test scenario comprises of 2 E-UTRA TDD cells on 2 different carriers and 1 non-allowed E-UTRA TDD CSG cell as given in tables A.4.2.8.1-1 and A.4.2.8.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 3 is a non-allowed CSG cell. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.8.1-1: General test parameters for TDD-TDD inter frequency cell re-selection test case with non-allowed CSG cell

Table A.4.2.8.1-2: Cell specific test parameters for TDD-TDD inter frequency cell re-selection test case with non-allowed CSG cell

## A.4.2.8.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

The probability of reselection from Cell 2 to Cell 1 during T3 observed during testing shall be less than 10%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter + TSI,

Where:

Tdetect,EUTRAN_InterSee Table 4.2.2.4-1 in clause 4.2.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell in the test case.

## A.4.2.9E-UTRAN FDD – FDD Intra frequency case for 5MHz bandwidth

## A.4.2.9.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.4.2.1.1.

The parameters of this test are the same as defined in Subclause A.4.2.1.1 except that the values of the parameters in the Table A.4.2.9.1-1 will replace the values of the corresponding parameters in A.4.2.1.1-1, and the values of the parameters in the Table A.4.2.9.1-2 will replace the values of the corresponding parameters in A.4.2.1.1-2.

Table A.4.2.9.1-1: General test parameters for FDD intra frequency cell reselection test case for 5MHz bandwidth

Table A.4.2.9.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case in AWGN for 5MHz

## A.4.2.9.2Test Requirements

The test requirements defined in section A.4.2.1.2 shall apply to this test case.

## A.4.2.10E-UTRAN FDD – FDD reselection using an increased number of carriers

## A.4.2.10.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4.

The test scenario comprises of indicating 8 E-UTRA FDD interfrequency cells on 8 different carriers in the neighbour list of cell 1 as given in tables A.4.2.10.1-1 and A.4.2.10.1-2. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3 and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (serving cell), and selects frequencies for cells 2, 3 and 4 which are chosen from the 8 intefrequency layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2, 3 and 4 shall include the frequency of cell 1 in the normal performance group as well as the other frequencies configured to the UE in the test.

Cell 1, 2, 3 and 4 are identified by the UE during time phase T0. Cell 1, cell 2, cell 3 and cell 4 all belong to different tracking areas.  Furthermore, UE has not registered with network for the tracking area containing cell 2, 3 or 4. Cells 1, 2, 3 and 4 all have equal absolute priority.

Table A.4.2.10.1-1: General test parameters for FDD-FDD inter frequency cell re-selection test case

Table A.4.2.10.1-2: Cell specific test parameters for FDD-FDD inter-frequency cell reselection test case in AWGN

## A.4.2.10.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.2.10.2-1.

Table A.4.2.10.2-1 : Reselection delay requirements

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: Kcarrier,normal * Tevaluate,E-UTRAN_Inter, + TSI , and to a reduced performance group cell can be expressed as: 6* Kcarrier,reduced * Tevaluate,E-UTRAN_Inter, + TSI,

This gives a total of 20.48 s for normal performance group reselection and 193.28 s for reduced performance group reselection, allow 20.5 s for normal performance group and 193.3 s for reduced performance group in the test case. At least 90% of reselections to the reduced performance group shall be within the required time, and at least 90% of reselections to the normal performance group shall be within the required time, with a successful reselection counted if it is within the required time regardless of the carrier frequencies involved.

## A.4.2.11E-UTRAN TDD – TDD reselection using an increased number of carriers

## A.4.2.11.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter-frequency cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4.

The test scenario comprises of indicating 8 E-UTRA TDD interfrequency cells on 8 different carriers in the neighbour list of cell 1 as given in tables A.4.2.11.1-1 and A.4.2.11.1-2. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3 and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (serving cell), and selects frequencies for cells 2, 3 and 4 which are chosen from the 8 intefrequency layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2, 3 and 4 shall include the frequency of cell 1 in the normal performance group as well as the other frequencies configured to the UE in the test.

Cell 1, 2, 3 and 4 are identified by the UE during time phase T0. Cell 1, cell 2, cell 3 and cell 4 all belong to different tracking areas.  Furthermore, UE has not registered with network for the tracking area containing cell 2, 3 or 4. Cells 1, 2, 3 and 4 all have equal absolute priority.

Table A.4.2.11.1-1: General test parameters for TDD-TDD inter frequency cell re-selection test case

Table A.4.2.11.1-2: Cell specific test parameters for TDD-TDD inter-frequency cell reselection test case in AWGN

## A.4.2.11.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.2.11.2-1

Table A.4.2.11.2-1 : Reselection delay requirements

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: Kcarrier,normal * Tevaluate,E-UTRAN_Inter, + TSI , and to a reduced performance group cell can be expressed as: 6* Kcarrier,reduced * Tevaluate,E-UTRAN_Inter, + TSI,

This gives a total of 20.48 s for normal performance group reselection and 193.28 s for reduced performance group reselection, allow 20.5 s for normal performance group and 193.3 s for reduced performance group in the test case. At least 90% of reselections to the reduced performance group shall be within the required time, and at least 90% of reselections to the normal performance group shall be within the required time, with a successful reselection counted if it is within the required time regardless of the carrier frequencies involved.

## A.4.2.12E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.12.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.12.1-1 and A.4.2.12.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.12.1-1: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.12.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.12.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.13E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.13.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.4.2.13.1-1 and A.4.2.13.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.13.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.13.1-2: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.13.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.14E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.14.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.14.1-1 and A.4.2.14.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.14.1-1: General test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE

Table A.4.2.14.1-2: Cell specific test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE in AWGN in normal coverage

## A.4.2.14.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,EUTRAN_ intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.15 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.15.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in enhanced coverage specified in clause 4.2.2.11.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.15.1-1 and A.4.2.15.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.15.1-1: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.15.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.15.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 18 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

Tevaluate,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 17.36 s, allow 18 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.16 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.16.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.11.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.4.2.16.1-1 and A.4.2.16.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.16.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.16.1-2: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.16.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 18 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

Tevaluate,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 17.36 s, allow 18 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.17 E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.17.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.11.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.17.1-1 and A.4.2.17.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.17.1-1: General test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE

Table A.4.2.17.1-2: Cell specific test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE in AWGN in enhanced coverage

## A.4.2.17.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 18 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

Tevaluate,EUTRAN_IntraSee Table 4.2.2.11-1 in clause 4.2.2.11

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 17.36 s, allow 18 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.18 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage

## A.4.2.18.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two ecells of different cell ID and one NB-IoT carrier with 2 ncells of different physical cell ID, as given in tables A.4.2.18.1-1, A.4.2.18.1-2 and A.4.2.18.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.18.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.18.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.18.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.18.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 59.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 14.82 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NB-IoT-NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-NC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6.2.2-1 in clause 4.6.2.2

Tevaluate, NB_intra_NB-IoT-NCSee Table 4.6.2.2-1 in clause 4.6.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.19HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage

## A.4.2.19.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.4.

The test scenario comprises of 1 E-UTRA carrier and a total of 4 cells as given in tables A.4.2.19.1-1, A.4.2.19.1-2 and A.4.2.19.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.19.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.19.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.19.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.19.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 21.12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Intra_NB-IoT-EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-EC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

Tevaluate, NB_intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32s is assumed in this test case.

This gives a total of 66.32 s, allow 67 s for the cell re-selection delay to a newly detectable cell and 21.12s, allow 22s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.20E-UTRAN FDD – FDD Intra frequency case for UE Category 1bis

## A.4.2.20.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for UE category 1bis specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.20.1-1 and A.4.2.20.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.20.1-1: General test parameters for FDD intra frequency cell reselection test case

Table A.4.2.20.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case in AWGN

## A.4.2.20.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: TevaluateFDD,intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

TevaluateFDD,intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.21E-UTRAN TDD – TDD Intra frequency case for UE Category 1bis

## A.4.2.21.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency cell reselection requirements for UE category 1bis specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.21.1-1 and A.4.2.21.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.21.1-1: General test parameters for TDD intra frequency cell re-selection test case

Table A.4.2.21.1-2: Cell specific test parameters for TDD intra frequency cell re-selection test case in AWGN

## A.4.2.21.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,E-UTRAN_ intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.22E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

## A.4.2.22.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for UE configured with highSpeedEnhancedMeasFlag specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.22.1-1 and A.4.2.22.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. highSpeedEnhancedMeasFlag is broadcasted to UE. Only Cell 1 is already identified by the UE prior to the start of the test, i.e., Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.22.1-1: General test parameters for E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

Table A.4.2.22.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

## A.4.2.22.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 15 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: TevaluateFDD,intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-3 in clause 4.2.2.3

TevaluateFDD,intraSee Table 4.2.2.3-3 in clause 4.2.2.3

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 14.08 s, allow 15 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.23E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

## A.4.2.23.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency cell reselection requirements for UE configured with highSpeedEnhancedMeasFlag specified specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.23.1-1 and A.4.2.23.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. highSpeedEnhancedMeasFlag is broadcasted to UE. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.23.1-1: General test parameters for E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

Table A.4.2.23.1-2: Cell specific test parameters for E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag

## A.4.2.23.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 15 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-3 in clause 4.2.2.3

Tevaluate,E-UTRAN_ intraSee Table 4.2.2.3-3 in clause 4.2.2.3

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 14.08 s, allow 15 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.24HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage

## A.4.2.24.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.6.

The test scenario comprises of 1 E-UTRA carrier and a total of 3 cells as given in tables A.4.2.24.1-1, A.4.2.24.1-2 and A.4.2.24.1-3. The test consists of four successive time periods, with time duration of T0, T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.24.1-1: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.24.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.24.1-3: eCell 1 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.24.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 21.12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

Tevaluate, NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 66.32 s, allow 67 s for the cell re-selection delay to a newly detectable cell and 21.12 s, allow 22 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.25E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage

## A.4.2.25.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.7.2.1.3.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.25.1-1 and A.4.2.25.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.25.1-1: General test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.25.1-2: Cell specific test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.25.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateFDD,inter + TSI , and to lower priority cell can be expressed as: TevaluateFDD,inter + TSI,

Where:

Thigher_priority_searchSee clause 4.7.2.1.3

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7.2.1.3-1 in clause 4.7.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.26E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage

## A.4.2.26.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.7.2.1.3.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.26.1-1 and A.4.2.26.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.26.1-1: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.26.1-2: Cell specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.26.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateFDD,inter + TSI , and to lower priority cell can be expressed as: TevaluateFDD,inter + TSI,

Where:

Thigher_priority_searchSee clause 4.7.2.1.3

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7.2.1.3-1 in clause 4.7.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.27E-UTRAN TDD – FDD Inter frequency case for Cat-M1 UE in normal coverage

## A.4.2.27.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.7.2.1.3.

The test scenario comprises of 2 E-UTRA TDD cells on 2 different carriers as given in tables A.4.2.27.1-1 and A.4.2.27.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.27.1-1: General test parameters for TDD-TDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.27.1-2: Cell specific test parameters for TDD-TDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.27.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateFDD,inter + TSI , and to lower priority cell can be expressed as: TevaluateFDD,inter + TSI,

Where:

Thigher_priority_searchSee clause 4.7.2.1.3

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7.2.1.3-1 in clause 4.7.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.28E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.28.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter frequency cell reselection requirements for category M1 UE in enhanced coverage specified in clause 4.7.2.2.3.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.28.1-1 and A.4.2.28.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.28.1-1: General test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.28.1-2: Cell specific test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.28.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 337 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter_EC + TSI-EUTRA-M1-EC ,and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Inter_EC + TSI_M1_EC,

Where:

Tdetect,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

Tevaluate,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

TSI-EUTRA-M1-ECMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 336.64 s, allow 337 s for the cell re-selection delay to a newly detectable cell and 16.64 s, allow 17 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.29E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.29.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for category M1 UE in enhanced coverage specified in clause 4.7.2.2.3.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.29.1-1 and A.4.2.29.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.29.1-1: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.29.1-2: Cell specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.29.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 337 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter_EC + TSI-EUTRA-M1-EC ,and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Inter_EC + TSI_M1_EC,

Where:

Tdetect,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

Tevaluate,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

TSI-EUTRA-M1-ECMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 336.64 s, allow 337 s for the cell re-selection delay to a newly detectable cell and 16.64 s, allow 17 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.30E-UTRAN TDD Inter frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.30.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter frequency cell reselection requirements for category M1 UE in enhanced coverage specified in clause 4.7.2.2.3.

The test scenario comprises of 2 E-UTRA TDD cells on 2 different carriers as given in tables A.4.2.30.1-1 and A.4.2.30.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.30.1-1: General test parameters for TDD-TDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.30.1-2: Cell specific test parameters for TDD-TDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.30.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 337 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter_EC + TSI-EUTRA-M1-EC ,and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Inter_EC + TSI_M1_EC,

Where:

Tdetect,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

Tevaluate,EUTRAN_Inter_ECSee Table 4.7.2.2.3-1 in clause 4.7.2.2.3

TSI-EUTRA-M1-ECMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 336.64 s, allow 337 s for the cell re-selection delay to a newly detectable cell and 16.64 s, allow 17 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.31E-UTRAN FDD – FDD Inter frequency case for UE Category 1bis

## A.4.2.31.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency cell reselection requirements for UE category 1bis specified in clause 4.2.2.4.

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.4.2.31.1-1 and A.4.2.31.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.31.1-1: General test parameters for FDD-FDD inter frequency cell re-selection test case for UE Category 1bis

Table A.4.2.31.1-2: Cell specific test parameters for FDD-FDD inter-frequency cell reselection test case in AWGN for UE Category 1bis

## A.4.2.31.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateFDD,inter + TSI , and to lower priority cell can be expressed as: TevaluateFDD,inter + TSI,

Where:

Thigher_priority_searchSee clause 4.2.2

TevaluateFDD,interSee Table 4.2.2.4-1 in clause 4.2.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.32E-UTRAN FDD – TDD Inter frequency case for UE Category 1bis

## A.4.2.32.1Test Purpose and Environment

This test is to verify the requirement for the FDD-TDD inter-frequency cell reselection requirements for UE Category 1bis specified in clause 4.2.2.4.

The test scenario comprises of 1 E-UTRA FDD cell and 1 E-UTRA TDD cell as given in tables A.4.2.32.1-1 and A.4.2.32.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.32.1-1: General test parameters for FDD-TDD inter frequency cell re-selection test case for UE Category 1bis

Table A.4.2.32.1-2: Cell specific test parameters for FDD-TDD inter-frequency cell reselection test case in AWGN for UE Category 1bis

## A.4.2.32.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.33E-UTRAN TDD – FDD Inter frequency case for UE Category 1bis

## A.4.2.33.1Test Purpose and Environment

This test is to verify the requirement for the TDD-FDD inter-frequency cell reselection requirements for UE Category 1bis specified in clause 4.2.2.4.

The test scenario comprises of 1 E-UTRA TDD cell and 1 E-UTRA FDD cell as given in tables A.4.2.33.1-1 and A.4.2.33.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.33.1-1: General test parameters for TDD-FDD inter frequency cell re-selection test case for UE Category 1bis

Table A.4.2.33.1-2: Cell specific test parameters for TDD-FDD inter-frequency cell reselection test case in AWGN for UE Category 1bis

## A.4.2.33.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.34E-UTRAN TDD – TDD: Inter frequency case for UE Category 1bis

## A.4.2.34.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter-frequency cell reselection requirements for UE Category 1bis specified in clause 4.2.2.4.

The test scenario comprises of 2 E-UTRA TDD cells on 2 different carriers as given in tables A.4.2.34.1-1 and A.4.2.34.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.34.1-1: General test parameters for TDD-TDD inter frequency cell reselection test case for UE Category 1bis

Table A.4.2.34.1-2: Cell specific test parameters for TDD-TDD inter-frequency cell reselection test case in AWGN for UE Category 1bis

## A.4.2.34.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,E-UTRAN_inter  + TSI-EUTRA , and to lower priority cell can be expressed as: Tevaluate,E-UTRAN_inter  + TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2

Tevaluate,E-UTRAN_inter See Table 4.2.2.4-1 in clause 4.2.2.4

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.4.2.35E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage

## A.4.2.35.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two ecells of different cell ID and one NB-IoT carrier with 2 ncells of different physical cell ID, as given in tables A.4.2.35.1-1, A.4.2.35.1-2 and A.4.2.35.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.35.1-1: General test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.35.1-2: nCell 1, nCell 2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.35.1-3: eCell 1 and eCell2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.35.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 59.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 14.82 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NB-IoT-NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-NC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6.2.2-1 in clause 4.6.2.2

Tevaluate, NB_intra_NB-IoT-NCSee Table 4.6.2.2-1 in clause 4.6.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.36E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage

## A.4.2.36.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.4.

The test scenario comprises of 1 E-UTRA carrier and a total of 4 cells as given in tables A.4.2.36.1-1, A.4.2.36.1-2 and A.4.2.36.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.36.1-1: General test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.36.1-2: nCell 1, nCell 2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.36.1-3: eCell 1 and eCell2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.36.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 21.12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Intra_NB-IoT-EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-EC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

Tevaluate, NB_intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32s is assumed in this test case.

This gives a total of 66.32 s, allow 67 s for the cell re-selection delay to a newly detectable cell and 21.12s, allow 22s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.37E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage

## A.4.2.37.1Test Purpose and Environment

This test is to verify the requirement for the TDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.6.

The test scenario comprises of 1 E-UTRA carrier and a total of 3 cells as given in tables A.4.2.37.1-1, A.4.2.37.1-2 and A.4.2.37.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.37.1-1: General test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.37.1-2: nCell 1, nCell 2 specific test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.37.1-3: eCell 1 specific test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.37.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 21.12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

Tevaluate, NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 66.32 s, allow 67 s for the cell re-selection delay to a newly detectable cell and 21.12 s, allow 22 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.38HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation

## A.4.2.38.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.1A when UE is configured to monitor WUS according to Table A.4.2.38.1-1 and under the serving cell RRM measurement relaxation according to the subclause 4.6.2.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two eCells of different cell ID and one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.4.2.38.1-1, A.4.2.38.1-2 and A.4.2.38.1-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.4.2.38.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.38.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.38.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.38.2Test Requirements

Before the beginning of T2, UE is under relaxed monitoring where the serving cell measurement is performed every 5.12 s and the infra-frequency measurement for the neighbor cells is relaxed according to subclause 5.2.4.12.0 in TS 36.304 [1].

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than [69.56] s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate, serv_NB-NC + Tdetect,NB_Intra_NB-IoT-NC + TSI.

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6.2.2-1 in clause 4.6.2.2, based on the configured DRX cycle

Tevaluate, serv_NB-NCSee Table 4.6.2.2-1 in clause 4.6.2.2, based on the effective DRX cycle after relaxation; [10.24] s is assumed in this test case.

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of [69.56] s, allow [70] s for the cell re-selection delay to a newly detectable in the test case.

## A.4.2.39E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

## A.4.2.39.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for UE configured with highSpeedEnhMeasFlag2-r16 specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.39.1-1 and A.4.2.39.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. highSpeedEnhMeasFlag2-r16 is broadcasted to UE. Only Cell 1 is already identified by the UE prior to the start of the test, i.e., Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.39.1-1: General test parameters for E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

Table A.4.2.39.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

## A.4.2.39.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 11 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI, and to an already detected cell can be expressed as: TevaluateFDD,intra + TSI,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-3 in clause 4.2.2.3

TevaluateFDD,intraSee Table 4.2.2.3-3 in clause 4.2.2.3

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 14.08 s, allow 15 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.40E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

## A.4.2.40.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency cell reselection requirements for UE configured with highSpeedEnhMeasFlag2-r16 specified specified in clause 4.2.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.40.1-1 and A.4.2.40.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. highSpeedEnhMeasFlag2-r16 is broadcasted to UE. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.40.1-1: General test parameters for E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

Table A.4.2.40.1-2: Cell specific test parameters for E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16

## A.4.2.40.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 11 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-3 in clause 4.2.2.3

Tevaluate,E-UTRAN_ intraSee Table 4.2.2.3-3 in clause 4.2.2.3

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 14.08 s, allow 15 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.41 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX

## A.4.2.41.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two ecells of different cell ID and one NB-IoT carrier with 2 ncells of different physical cell ID, as given in tables A.4.2.41.1-1, A.4.2.41.1-2 and A.4.2.41.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.41.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.41.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.41.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.41.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1 and test 2.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 13.44 s in test 1 and test 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NC + TSI,

Where:

Tdetect,NB_Intra_NCSee Table 4.6.2.2-1 in clause 4.6.2.2

Tevaluate, NB_intra_NCSee Table 4.6.2.2-1 in clause 4.6.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 34.32 s, allow 35 s for the cell re-selection delay to a newly detectable cell and 13.44 s, allow 14s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.42HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX

## A.4.2.42.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.4.

The test scenario comprises of 1 E-UTRA carrier and a total of 4 cells as given in tables A.4.2.42.1-1, A.4.2.42.1-2 and A.4.2.42.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.42.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.42.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.42.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.42.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1.

The cell re-selection delay to a newly detectable cell shall be less than 37.32 s in test 2.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 18.56 s in test 1 and test 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Intra_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_EC + TSI,

Where:

Tdetect,NB_Intra_ECSee Table 4.6.2.4-1 in clause 4.6.2.4

Tevaluate, NB_intra_ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32s is assumed in this test case.

This gives a total of 34.32 s in test 1 and 37.32 s in test 2, allow 35 s and 38 s for the cell re-selection delay to a newly detectable cell in each test respectively and 18.56 s, allow 19 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.43HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX

## A.4.2.43.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.6.

The test scenario comprises of 1 E-UTRA carrier and a total of 3 cells as given in tables A.4.2.43.1-1, A.4.2.43.1-2 and A.4.2.43.1-3. The test consists of four successive time periods, with time duration of T0, T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.43.1-1: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.43.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.43.1-3: eCell 1 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.43.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1.

The cell re-selection delay to a newly detectable cell shall be less than 37.32 s in test 2.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 18.56 s in test 1 and test 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

Tevaluate, NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 34.32 s in test 1 and 37.32 in test 2, allow 35 s and 38 s for the cell re-selection delay to a newly detectable cell in each test respectively and 18.56 s, allow 19 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.44E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX

## A.4.2.44.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two ecells of different cell ID and one NB-IoT carrier with 2 ncells of different physical cell ID, as given in tables A.4.2.44.1-1, A.4.2.44.1-2 and A.4.2.44.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.44.1-1: General test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.44.1-2: nCell 1, nCell 2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.44.1-3: eCell 1 and eCell2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.44.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1 and test 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 13.44 s in test 1 and test 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NC + TSI,

Where:

Tdetect,NB_Intra_NCSee Table 4.6.2.2-1 in clause 4.6.2.2

Tevaluate, NB_intra_NCSee Table 4.6.2.2-1 in clause 4.6.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 34.32 s, allow 35 s for the cell re-selection delay to a newly detectable cell and 13.44 s, allow 14 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.45E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX

## A.4.2.45.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.4.

The test scenario comprises of 1 E-UTRA carrier and a total of 4 cells as given in tables A.4.2.45.1-1, A.4.2.45.1-2 and A.4.2.45.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.45.1-1: General test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.45.1-2: nCell 1, nCell 2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.45.1-3: eCell 1 and eCell2 specific test parameters for TDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.45.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1.

The cell re-selection delay to a newly detectable cell shall be less than 37.32 s in test 2.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 21.12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Intra_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_EC + TSI,

Where:

Tdetect,NB_Intra_ECSee Table 4.6.2.4-1 in clause 4.6.2.4

Tevaluate, NB_intra_ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32s is assumed in this test case.

This gives a total of 34.32 s in test 1 and 37.32 s in test 2, allow 35 s and 38 s for the cell re-selection delay to a newly detectable cell in each test respectively and 18.56 s, allow 19 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.46E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX

## A.4.2.46.1Test Purpose and Environment

This test is to verify the requirement for the TDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.6.

The test scenario comprises of 1 E-UTRA carrier and a total of 3 cells as given in tables A.4.2.46.1-1, A.4.2.46.1-2 and A.4.2.46.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.46.1-1: General test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.46.1-2: nCell 1, nCell 2 specific test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.4.2.46.1-3: eCell 1 specific test parameters for TDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.4.2.46.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34.32 s in test 1.

The cell re-selection delay to a newly detectable cell shall be less than 37.32 s in test 2.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 18.56 s in test 1 and test 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

Tevaluate, NB_Inter_ECSee Table 4.6.2.6-1 in clause 4.6.2.6

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 34.32 s in test 1 and 37.32 s in test 2, allow 35 s and 38 s for the cell re-selection delay to a newly detectable cell in each test respectively and 18.56 s, allow 19 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.47HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation with UE specific DRX

## A.4.2.47.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6.2.1A when UE is configured to monitor WUS according to Table A.4.2.47.1-1 and under the serving cell RRM measurement relaxation according to the subclause 4.6.2.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.6.2.2.

The test scenario comprises of 1 E-UTRA carrier with two eCells of different cell ID and one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.4.2.47.1-1, A.4.2.47.1-2 and A.4.2.47.1-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

Table A.4.2.47.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.47.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.4.2.47.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.4.2.47.2Test Requirements

Before the beginning of T2, UE is under relaxed monitoring where the serving cell measurement is performed every 1.28 s in test 1 and 2.56 s in test 2 and the infra-frequency measurement for the neighbor cells is relaxed according to subclause 5.2.4.12.0 in TS 36.304 [1].

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 36.88 s in test 1.

The cell re-selection delay to a newly detectable cell shall be less than 39.44 s in test 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate, serv_NB-NC + Tdetect,NB_Intra_NB-IoT-NC + TSI.

Where:

Tdetect,NB_Intra_NCSee Table 4.6.2.2-1 in clause 4.6.2.2, based on the configured DRX cycle

Tevaluate, serv_NB-NCSee Table 4.6.2.2-1 in clause 4.6.2.2, based on the effective DRX cycle after relaxation; 2.56 s is assumed in test 1 and 5.12 s is assumed in test 2.

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 36.88 s in test 1 and 39.44 s in test 2, allow 37 s and 40 s for the cell re-selection delay to a newly detectable cell in each test respectively.

## A.4.2.48E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.48.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage based on RSS as specified in clause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.48.1-1 and A.4.2.48.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.48.1-2.

Table A.4.2.48.1-1: General test parameters for FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.48.1-2: Cell specific test parameters for FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.48.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC_RSS + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

Tevaluate,EUTRAN_Intra_NC_RSSSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.49E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.49.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE in normal coverage based on RSS as specified in clause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.4.2.49.1-1 and A.4.2.49.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.49.1-2.

Table A.4.2.49.1-1: General test parameters for HD-FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.49.1-2: Cell specific test parameters for HD-FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.49.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC_RSS + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

Tevaluate,EUTRAN_Intra_NC_RSSSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.50E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.50.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-M1 UE based on RSS as specified in clause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.50.1-1 and A.4.2.50.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.50.1-2.

Table A.4.2.50.1-1: General test parameters for TDD RSS based intra frequency cell re-selection test case for Cat-M1 UE

Table A.4.2.50.1-2: Cell specific test parameters for TDD RSS based intra frequency cell re-selection test case for Cat-M1 UE in AWGN in normal coverage

## A.4.2.50.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra_NC_RSS + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

Tevaluate,EUTRAN_ intra_NC_RSSSee Table 4.7.2.1.2-1 in clause 4.7.2.1.2

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 5.12 s, allow 6 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.51 E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.51.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in enhanced coverage based on RSS as specified in clause 4.7.2.2.2.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.51.1-1 and A.4.2.51.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.51.1-2.

Table A.4.2.51.1-1: General test parameters for FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.51.1-2: Cell specific test parameters for FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.51.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 13 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_EC + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_EC_RSS + TSI,

Where:

Tdetect,EUTRAN_Intra_ECSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

Tevaluate,EUTRAN_Intra_EC_RSSSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 12.8 s, allow 13 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.52 E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.52.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE in enhanced coverage based on RSS as specified in clause 4.7.2.2.2.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.4.2.52.1-1 and A.4.2.52.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.52.1-2.

Table A.4.2.52.1-1: General test parameters for HD-FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.4.2.52.1-2: Cell specific test parameters for HD-FDD RSS based intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.4.2.52.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 13 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_EC + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_EC_RSS + TSI,

Where:

Tdetect,EUTRAN_Intra_ECSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

Tevaluate,EUTRAN_Intra_EC_RSSSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 12.8 s, allow 13 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.53 E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage

## A.4.2.53.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-M1 UE in enhanced coverage based on RSS as specified in clause 4.7.2.2.2.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.53.1-1 and A.4.2.53.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

RSS measurement is enabled in both Cell 1 and Cell2 with rss-MeasConfig and rss-MeasNonNCL in SIB2 set to ‘enabled’. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in SIB4. intraFreqNeighCellList-v1610 is also absent in SIB4. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.4.2.53.1-2.

Table A.4.2.53.1-1: General test parameters for TDD RSS based intra frequency cell re-selection test case for Cat-M1 UE

Table A.4.2.53.1-2: Cell specific test parameters for TDD RSS based intra frequency cell re-selection test case for Cat-M1 UE in AWGN in enhanced coverage

## A.4.2.53.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 13 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_EC + TSI, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_EC_RSS + TSI,

Where:

Tdetect,EUTRAN_Intra_ECSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

Tevaluate,EUTRAN_Intra_EC_RSSSee Table 4.7.2.2.2-1 in clause 4.7.2.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell and 12.8 s, allow 13 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.54E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation

## A.4.2.54.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.2.2.3 when UE is configured to monitor WUS according to Table A.4.2.54.1-1 and under the serving cell RRM measurement relaxation according to the subclause 4.7.2.1.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.4.2.54.1-1 and A.4.2.54.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.54.1-1: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.54.1-2: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.54.2Test Requirements

Before the beginning of T2, UE is under relaxed monitoring where the serving cell measurement is performed every 5.12 s and the infra-frequency measurement for the neighbor cells is relaxed according to subclause 5.2.4.12.0 in TS 36.304 [1].

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 20 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 9 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3 based on the configured DRX cycle

Tevaluate,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3 based on the effective DRX cycle after relaxation; [10.24] s is assumed in this test case.

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 19.2 s, allow 20 s for the cell re-selection delay to a newly detectable cell and 8.96 s, allow 9 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.55E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation

## A.4.2.55.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.3 when UE is configured to monitor WUS according to Table A.4.2.55.1-1 and under the serving cell RRM measurement relaxation according to the subclause 4.7.2.1.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.4.2.55.1-1 and A.4.2.55.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.4.2.55.1-1: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.4.2.55.1-2: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.4.2.55.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 20 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 9 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 19.2 s, allow 20 s for the cell re-selection delay to a newly detectable cell and 8.96 s, allow 9 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.2.56E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage

## A.4.2.56.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.3 when UE is configured to monitor WUS according to Table A.4.2.56.1-1 and under the serving cell RRM measurement relaxation according to the subclause 4.7.2.1.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.4.2.56.1-1 and A.4.2.56.1-2. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.4.2.56.1-1: General test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE

Table A.4.2.56.1-2: Cell specific test parameters for TDD intra frequency cell re-selection test case for Cat-M1 UE in AWGN in normal coverage

## A.4.2.56.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 20 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay shall be less than 9 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate, E-UTRAN_ intra + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_IntraSee Table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate,EUTRAN_ intraSee Table 4.2.2.3-1 in clause 4.2.2.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 19.2 s, allow 20 s for the cell re-selection delay to a newly detectable cell and 8.96 s, allow 9 s for the cell re-selection delay to an already detected cell in the test case.

## A.4.3E-UTRAN to UTRAN Cell Re-Selection

## A.4.3.1E-UTRAN FDD – UTRAN FDD:

## A.4.3.1.1EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of higher priority

## A.4.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRA FDD- UTRA FDD inter-RAT cell reselection requirements specified in clause 4.2.2.5 when the UTRA cell is of higher priority.

The test scenario comprises of one E-UTRA FDD and one UTRA FDD cells as given in tables A.4.3.1.1.1-1, A.4.3.1.1.1-2 and A.4.3.1.1.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. E-UTRA cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than cell 1.

Table A.4.3.1.1.1-1: General test parameters for E-UTRA FDD- higher priority UTRA FDD inter RAT cell re-selection test case

Table A.4.3.1.1.1-2: Cell specific test parameters for cell 1(E-UTRA)

Table A.4.3.1.1.1-3: Cell specific test parameters for cell 2(UTRA)

## A.4.3.1.1.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to higher priority shall be less than 81 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search +TevaluateUTRA_FDD + TSI-UTRA

Where:

Thigher_priority_search See clause 4.2.2; 60s is assumed in this test case

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 80.48 s for higher priority cell search, allow 81 s for higher priority cell reselection in the test case.

## A.4.3.1.2EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority

## A.4.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the EUTRA FDD- UTRA FDD inter-RAT cell reselection requirements specified in clause 4.2.2.5.1 when the UTRA cell is of lower priority.

The test scenario comprises of one UTRA FDD and one E-UTRA FDD cells as given in tables A.4.3.1.2.1-1, A.4.3.1.2.1-2 and A.4.3.1.2.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both E-UTRA cell 1 and UTRA cell 2 are already identified by the UE prior to the start of the test. Cell 2 is of lower priority than cell 1.

Table A.4.3.1.2.1-1: General test parameters for EUTRA FDD- lower priority UTRA FDD inter RAT cell re-selection test case

Table A.4.3.1.2.1-2: Cell specific test parameters for cell 1 (E-UTRA)

Table A.4.3.1.2.1-3: Cell specific test parameters for cell 2 (UTRA)

## A.4.3.1.2.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_FDD + TSI-UTRA

Where:

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for lower priority cell reselection, allow 21 s.

## A.4.3.1.3EUTRA FDD-UTRA FDD cell reselection in fading propagation conditions: UTRA FDD is of lower priority

## A.4.3.1.3.1Test Purpose and Environment

This test is to verify the requirement for the EUTRA FDD- UTRA FDD inter-RAT cell reselection requirements specified in clause 4.2.2.5.1 when the UTRA cell is of lower priority, and to verify  the robustness of the UE measurement filtering in a fading environment.  The E-UTRA cell is in fading propagation conditions and the UTRA cell is in AWGN propagation conditions.

The test scenario comprises of one UTRA FDD and one E-UTRA FDD cells as given in tables A.4.3.1.3.1-1, A.4.3.1.3.1-2 and A.4.3.1.3.1-3. The test consists of four successive time periods, with time duration of T1 T2, T3 and T4 respectively. Both E-UTRA cell 1 and UTRA cell 2 are already identified by the UE prior to the start of the test. Cell 2 is of lower priority than cell 1.

Table A.4.3.1.3.1-1: General test parameters for EUTRA FDD- lower priority UTRA FDD inter RAT cell re-selection test case

Table A.4.3.1.3.1-2: Cell specific test parameters for cell 1 (E-UTRA)

Table A.4.3.1.3.1-3: Cell specific test parameters for cell 2 (UTRA)

## A.4.3.1.3.2Test Requirements

The probability of reselection from cell 1to cell 2 during T2 observed during testing shall be less than 10%

The probability of reselection from cell 2 to cell 1 during T4 observed during testing shall be less than 10%

The cell reselection delay to lower priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message on cell 2. In order to evaluate reselection delay, the system simulator first needs to verify that the UE is camped on cell 1 at the start of T3

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_FDD + TSI-UTRA

Where:

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for lower priority cell reselection, allow 21 s.

## A.4.3.1.4EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority for 5MHz bandwidth

## A.4.3.1.4.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.4.3.1.2.1

The parameters of this test are the same as defined in Subclause A.4.3.1.2.1 except that the values of the parameters in the Table A.4.3.1.4.1-2 will replace the values of the corresponding parameters in A.4.3.1.2.1-2.

This is according to the principle defined in section A.3.7.2.

Table A.4.3.1.4.1-2: Cell specific test parameters for cell 1 (E-UTRA) for 5MHz bandwidth

## A.4.3.1.4.2Test Requirements

The test requirements defined in section A.4.3.1.2.1 shall apply to this test case.

## A.4.3.1.5Idle mode FDD to UTRA FDD interRAT reselection

## A.4.3.1.5.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRA FDD-UTRA FDD inter-RAT cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4.

The test scenario comprises of indicating 8 UTRA FDD interfrequency cells on 6 different carriers in the neighbour list of cell 1 as given in table A.4.3.1.5-1 and cells 2 and 3 as given in table A.4.3.1.5-2. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3 and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (serving cell), and selects frequencies for cells 2 and 3 which are chosen from the 6 inter-RAT layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2 and 3 shall include the frequency of cell 1 in the normal performance group and shall exclude the other frequencies configured to the UE in the test.

Cell 1, 2 and 3 are identified by the UE during time period T0. Cell 1, cell 2 and cell 3 all belong to different tracking areas.  Furthermore, UE has not registered with network for the tracking area containing cell 2 or 3. Cells 2 and 3 all have lower absolute priority than cell 1.

Table A.4.3.1.5-1: General test parameters for E-UTRAN FDD- UTRAN FDD inter frequency cell re-selection test case

Table A.4.3.1.5-2: Cell specific test parameters for E-UTRAN FDD- UTRAN FDD inter-RAT cell reselection test case in AWGN cell 1 (E-UTRAN)

Table A.4.3.1.5-3: Cell specific test parameters for cells 2 and 3 (UTRA)

## A.4.3.1.5.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.3.1.5.2-1

Table A.4.3.1.5.2-1

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: (NUTRA_carrier,normal) * TevaluateUTRA_FDD + TSI-UTRA and to a reduced performance group cell can be expressed as: 6 * NUTRA_carrier,reduced * TevaluateUTRA_FDD + TSI-UTRA.

Where:

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 58.88 s for normal performance group reselection, allow 21 s, and gives a total of 346.88 s for reduced performance group reselection, allow 347 s for reduced performance group in the test case. For reselections back to cell 1 since only one frequency is configured, the requirement is Tevaluate,E-UTRAN + TSI = 20.48 s, allow 21 s.

## A.4.3.2E-UTRAN FDD – UTRAN TDD:

## A.4.3.2.1Test Purpose and Environment

## A.4.3.2.1.1Void

## A.4.3.2.1.21.28Mcps TDD option

This test is to verify the requirement for the E-UTRA FDD to UTRA TDD inter-RAT cell reselection requirements specified in clause 4.2.2.5.2 when the UTRA cell is of lower priority.

This test scenario comprised of 1 E-UTRA FDD serving cell (Cell 1), and 1 UTRA TDD cell (Cell 2) to be re-selected. Test parameters are given in table A.4.3.2.1.2-1, A.4.3.2.1.2-2, and A.4.3.2.1.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Cell 2 is of lower priority than cell 1.

The ranking of the cells shall be made according to the cell reselection criteria specified in TS36.304.

Table A.4.3.2.1.2-1: General test parameters for E-UTRA FDD to UTRA (1.28 Mcps TDD OPTION) Cell Re-selection

Table A.4.3.2.1.2-2: Cell specific test parameters for cell re-selection E-UTRA FDD to UTRA TDD test case (cell 1)

Table A.4.3.2.1.2-3: Cell specific test parameters for cell re-selection E-UTRA FDD to UTRA TDD test case (cell 2)

## A.4.3.2.1.3Void

## A.4.3.2.2Test Requirements

## A.4.3.2.2.11.28Mcps TDD option

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send the SYNCH-UL sequence in the UpPTS for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_TDD + TSI-UTRA

Where:

TevaluateUTRA_TDD19.2s, See table table 4.2.2.5.2-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s, allow 21 s for lower priority cell reselection in the test case.

A.4.3.2.2.2.3Void

## A.4.3.2AE-UTRA FDD to UTRA TDD cell re-selection for IncMon

## A.4.3.2A.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRA FDD to UTRA TDD inter-RAT cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4. UTRA TDD cells are of lower priority than E-UTRA serving cell.

The test scenario comprises of indicating 7 UTRA TDD inter-RAT cells on 7 different carriers in the neighbour list of cell 1 as given in tables A.4.3.2A.1-1, A.4.3.2A.1-2 and A.4.3.2A.1-3. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3, and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (E-UTRA serving cell), and selects frequencies for cells 2 and 3 which are chosen from the 7 inter-RAT layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2 and 3 shall include the frequency of cell 1 in the normal performance group and shall exclude the other UTRA TDD frequencies configured to the UE in the test.

Cell 1, 2 and 3 are identified by the UE during time phase T0. Cell 1, cell 2 and cell 3 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2 or 3.

Table A.4.3.2A.1-1: General test parameters for E-UTRA FDD to UTRA TDD inter-RAT cell re-selection test case

Table A.4.3.2A.1-2: E-UTRA Cell specific test parameters for E-UTRA FDD to UTRA TDD inter-RAT cell reselection test case in AWGN

Table A.4.3.2A.1-3: UTRA TDD Cell specific test parameters for E-UTRA FDD to UTRA TDD inter-RAT cell reselection test case in AWGN

Table A.4.3.2A.1-4:

## A.4.3.2A.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send the SYNCH-UL sequence in the UpPTS on cell 2, 3 for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.3.2A.2-1

Table A.4.3.2A.2-1: Test requirements for E-UTRA FDD to UTRA TDD inter-RAT cell reselection

The rate of correct cell reselections observed during repeated tests shall be at least 90%, with a successful reselection counted if it is within the required time regardless of the carrier frequencies involved. At least 90% of reselections to the reduced performance group shall be within the required time, and at least 90% of reselections to the normal performance group shall be within the required time.

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: NUTRA_carrier_TDD,normal *TevaluateUTRA_TDD + TSI_UTRA, and to a reduced performance group cell can be expressed as: 6 * NUTRA_carrier_TDD,reduced * TevaluateUTRA_TDD + TSI_UTRA,

Where:

TevaluateUTRA_TDD19.2s, See Table 4.2.2.5.2-1

TSI_UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 3 * 19.2 + 1.28 = 58.88 s for normal performance group reselection and 6 * 4 * 19.2 + 1.28 = 462.08s for reduced performance group reselection, allow 58.9s for normal performance group and 462.1s for reduced performance group in the test case.

Since only one E-UTRA frequency is configured and signal level of UTRA cell is lower than threshold of Sprioritysearch, the UE shall select back to cell 1 (E-UTRA cell) within Kcarrier * TevaluateEUTRA + TSI = 19.2 + 1.28 = 20.48s.

## A.4.3.3E-UTRAN TDD – UTRAN FDD:

## A.4.3.3.1Test Purpose and Environment

This test is to verify the requirement for the EUTRA TDD- UTRA FDD inter-RAT cell reselection requirements specified in clause 4.2.2.5.1 when the UTRA cell is of lower priority.

The test scenario comprises of one UTRA FDD and one E-UTRA TDD cells as given in tables A.4.3.3.1-1, A.4.3.3.1-2 and A.4.3.3.1-3. The test consists of two successive time periods, with time duration of T1 andT2 respectively. Both E-UTRA cell 1 and UTRA cell 2 are already identified by the UE prior to the start of the test. Cell 2 is of lower priority than cell 1.

Table A.4.3.3.1-1: General test parameters for EUTRA TDD- lower priority UTRA FDD inter RAT cell re-selection test case

Table A.4.3.3.1-2: Cell specific test parameters for cell 1(E-UTRA)

Table A.4.3.3.1-3: Cell specific test parameters for cell 2 (UTRA)

## A.4.3.3.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_FDD + TSI-UTRA

Where:

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for lower priority cell reselection, allow 21 s.

## A.4.3.3AIdle mode TDD to UTRA FDD interRAT reselection

## A.4.3.3A.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRA TDD-UTRA FDD inter-RAT cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4.

The test scenario comprises of indicating 8 UTRA FDD interfrequency cells on 6 different carriers in the neighbour list of cell 1 as given in table A.4.3.3A.1-2 and table A.4.3.3A.1-3 and cells 2 and 3 as given in table A.4.3.3A.1-4. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3 and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (serving cell), and selects frequencies for cells 2 and 3 which are chosen from the 6 inter-RAT layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2 and 3 shall include the frequency of cell 1 in the normal performance group and shall exclude the other frequencies configured to the UE in the test.

Cell 1, 2 and 3 4 are identified by the UE during time period T0. Cell 1, cell 2 and cell 3 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2 or 3. Cells 1, 2 and 3 4 all have lower absolute priority than cell 1.

Table A.4.3.3A.1-1: General test parameters for E-UTRAN TDD- UTRAN FDD inter frequency cell re-selection test case

Table A.4.3.3A.1-2: General test parameters for EUTRA TDD- UTRA FDD inter RAT cell re-selection test case

Table A.4.3.3A.1-3: Cell specific test parameters for E-UTRAN TDD- UTRAN FDD inter-RAT cell reselection test case in AWGN cell 1 (E-UTRAN)

Table A.4.3.3A.1-4: Cell specific test parameters for cells 2 and 3 (UTRA)

## A.4.3.3A.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.3.1.5-1

Table A.4.3.3A.2-1

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: (NUTRA_carrier,normal) * TevaluateUTRA_FDD + TSI-UTRA and to a reduced performance group cell can be expressed as: 6 * NUTRA_carrier,reduced * TevaluateUTRA_FDD + TSI-UTRA.

Where:

TevaluateUTRA-FDDSee Table 4.2.2.5.1-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 58.88 s for normal performance group reselection, allow 59 s, and gives a total of 346.88 s for reduced performance group reselection, allow 347 s for reduced performance group in the test case. For reselections back to cell 1 since only one frequency is configured, the requirement is Tevaluate,E-UTRAN + TSI = 20.48 s, allow 21 s.

## A.4.3.4E-UTRAN TDD – UTRAN TDD:

## A.4.3.4.1E-UTRA to UTRA TDD cell re-selection: UTRA is of higher priority

## A.4.3.4.1.1Test Purpose and Environment

A.4.3.4.1.1.1Void

A.4.3.4.1.1.21.28 Mcps TDD option

This test is to verify the requirement for the E-UTRA TDD to UTRA TDD inter-RAT cell re-selection requirements specified in clause 4.2.2.5 when the UTRA cell is of higher priority.

This test scenario comprised of 1 E-UTRA TDD serving cell, and 1 UTRA TDD cell to be re-selected. Test parameters are given in table A.4.3.4.1.1.2-1, A.4.3.4.1.1.2-2, and A.4.3.4.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. E-UTRA cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than cell 1.

The ranking of the cells shall be made according to the cell reselection criteria specified in TS36.304.

Table A.4.3.4.1.1.2-1: General test parameters for E-UTRAN to UTRAN (1.28 Mcps TDD OPTION) Cell Re-selection

Table A.4.3.4.1.1.2-2: Cell specific test parameters for cell re-selection E-UTRA TDD to UTRA TDD test case (cell 1)

Table A.4.3.4.1.1.2-3: Cell specific test parameters for cell re-selection E-UTRA TDD to UTRA TDD test case (cell 2)

A.4.3.4.1.1.3Void

## A.4.3.4.1.2Test Requirements

A.4.3.4.1.2.1Void

A.4.3.4.1.2.21.28 Mpcs TDD option

The cell reselection delay to higher priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send the SYNCH-UL sequence in the UpPTS for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to higher priority shall be less than 81 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + TevaluateUTRA_TDD + TSI_UTRA,

Where:

Thigher_priority_search 60s, See clause 4.2.2

TevaluateUTRA_TDD19.2s, See Table 4.2.2.5.2-1

TSI_UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 80.48 s, allow 81 s for higher priority cell reselection in the test case.

A.4.3.4.1.2.3Void

## A.4.3.4.2E-UTRA to UTRA TDD cell re-selection: UTRA is of lower priority

## A.4.3.4.2.1Test Purpose and Environment

A.4.3.4.2.1.1Void

A.4.3.4.2.1.21.28 Mcps TDD option

This test is to verify the requirement for the E-UTRA TDD to UTRA TDD inter-RAT cell re-selection requirements specified in clause 4.2.2.5 when the UTRA cell is of lower priority.

This test scenario comprised of 1 E-UTRA TDD serving cell (Cell 1), and 1 UTRA TDD cell (Cell 2) to be re-selected. Test parameters are given in table A.4.3.4.2.1.2-1, A.4.3.4.2.1.2-2, and A.4.3.4.2.1.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Cell 2 is of lower priority than cell 1.

The ranking of the cells shall be made according to the cell reselection criteria specified in TS36.304.

Table A.4.3.4.2.1.2-1: General test parameters for E-UTRAN to UTRAN (1.28 Mcps TDD OPTION) Cell Re-selection

Table A.4.3.4.2.1.2-2: Cell specific test parameters for cell re-selection E-UTRA TDD to UTRA TDD test case (cell 1)

Table A.4.3.4.2.1.2-3: Cell specific test parameters for cell re-selection E-UTRA TDD to UTRA TDD test case (cell 2)

A.4.3.4.2.1.3Void

## A.4.3.4.2.2Test Requirements

A.4.3.4.2.2.1Void

A.4.3.4.2.2.21.28 Mpcs TDD option

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send the SYNCH-UL sequence in the UpPTS for sending the RRC CONNECTION REQUEST message on cell 2.

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_TDD + TSI_UTRA,

Where:

TevaluateUTRA_TDD19.2s, See Table 4.2.2.5.2-1

TSI_UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s, allow 21 s for lower priority cell reselection in the test case.

A.4.3.4.2.2.3Void

## A.4.3.4.3EUTRA TDD-UTRA TDD cell reselection in fading propagation conditions: UTRA TDD is of lower priority

## A.4.3.4.3.1Test Purpose and Environment

This test is to verify the requirement for the EUTRA TDD- UTRA TDD inter-RAT cell reselection requirements specified in clause 4.2.2.5.2 when the UTRA cell is of lower priority, and to verify the robustness of the UE measurement filtering in a fading environment.  The E-UTRA cell is in fading propagation conditions and the UTRA cell is in AWGN propagation conditions.

The test scenario comprises of one UTRA TDD and one E-UTRA TDD cells as given in tables A.4.3.4.3.1-1, A.4.3.4.3.1-2 and A.4.3.4.3.1-3. The test consists of four successive time periods, with time duration of T1 T2, T3 and T4 respectively. Both E-UTRA cell 1 and UTRA cell 2 are already identified by the UE prior to the start of the test. Cell 2 is of lower priority than cell 1.

Table A.4.3.4.3.1-1: General test parameters for EUTRA TDD- lower priority UTRA TDD inter RAT cell re-selection test case

Table A.4.3.4.3.1-2: Cell specific test parameters for cell 1 (E-UTRA)

Table A.4.3.4.3.1-3: Cell specific test parameters for cell 2 (UTRA)

## A.4.3.4.3.2Test Requirements

The probability of reselection from cell 1 to cell 2 during T2 observed during testing shall be less than 10%

The probability of reselection from cell 2 to cell 1 during T4 observed during testing shall be less than 10%

The cell reselection delay to lower priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send the SYNCH-UL sequene in the UpPTS for sending the RRC CONNECTION REQUEST message on cell 2. In order to evaluate reselection delay, the system simulator first needs to verify that the UE is camped on cell 1 at the start of T3

The cell re-selection delay to lower priority shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateUTRA_TDD + TSI-UTRA

Where:

TevaluateUTRA_TDD19.2s, See Table 4.2.2.5.2-1

TSI-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for lower priority cell reselection, allow 21 s.

## A.4.3.4.4E-UTRA TDD to UTRA TDD cell re-selection for IncMon

## A.4.3.4.4.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRA TDD to UTRA TDD inter-RAT cell reselection requirements for increased UE carrier monitoring specified in clause 4.2.2.4. UTRA TDD cells are of lower priority than E-UTRA serving cell.

The test scenario comprises of indicating 7 UTRA TDD inter-RAT cells on 7 different carriers in the neighbour list of cell 1 as given in tables A.4.3.4.4.1-1, A.4.3.4.4.1-2 and A.4.3.4.4.1-3. Each repetition of the test consists of five successive time periods, with time duration of T0, T1, T2, T3, and T4 respectively. In the initialisation phase and at the start of each repetition of T0, the test equipment provides signals for cell 1 (E-UTRA serving cell), and selects frequencies for cells 2 and 3 which are chosen from the 7 inter-RAT layers which are configured in the UE neighbour cell list as described in general and cell specific parameters. The neighbour lists of cells 2 and 3 shall include the frequency of cell 1 in the normal performance group and shall exclude the other UTRA TDD frequencies configured to the UE in the test.

Cell 1, 2, and 3 are identified by the UE during time phase T0. Cell 1, cell 2, and cell 3 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2 or 3.

Table A.4.3.4.4.1-1: General test parameters for E-UTRA TDD to UTRA TDD inter-RAT cell re-selection test case

Table A.4.3.4.4.1-2: E-UTRA Cell specific test parameters for E-UTRA TDD to UTRA TDD inter-RAT cell reselection test case in AWGN

Table A.4.3.4.4.1-3: UTRA TDD Cell specific test parameters for E-UTRA TDD to UTRA TDD inter-RAT cell reselection test case in AWGN

Table A.4.3.4.4.1-4:

## A.4.3.4.4.2Test Requirements

The cell reselection delay is defined as the time from the beginning of a relevant time period, to the moment when the UE camps on the target cell, and starts to send the SYNCH-UL sequence in the UpPTS on cell 2, 3 for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on the target cell.

The reselection delays shall meet the requirements in table A.4.3.4.4.2-1

Table A.4.3.4.4.2-1: Test requirements for E-UTRA TDD to UTRA TDD inter-RAT cell reselection

The rate of correct cell reselections observed during repeated tests shall be at least 90%, with a successful reselection counted if it is within the required time regardless of the carrier frequencies involved. At least 90% of reselections to the reduced performance group shall be within the required time, and at least 90% of reselections to the normal performance group shall be within the required time.

NOTE:The cell re-selection delay to a normal performance group cell can be expressed as: NUTRA_carrier_TDD,normal *TevaluateUTRA_TDD + TSI_UTRA, and to a reduced performance group cell can be expressed as: 6 * NUTRA_carrier_TDD,reduced * TevaluateUTRA_TDD + TSI_UTRA,

Where:

TevaluateUTRA_TDD19.2s, See Table 4.2.2.5.2-1

TSI_UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 3 * 19.2 + 1.28 = 58.88 s for normal performance group reselection and 6 * 4 * 19.2 + 1.28 = 462.08s for reduced performance group reselection, allow 58.9s for normal performance group and 462.1s for reduced performance group in the test case.

Since only one E-UTRA frequency is configured and signal level of UTRA cell is lower than threshold of Sprioritysearch, the UE shall select back to cell 1 (E-UTRA cell) within Kcarrier * TevaluateEUTRA + TSI = 19.2 + 1.28 = 20.48s, allow 21s.

## A.4.4E-UTRAN to GSM Cell Re-Selection

## A.4.4.1E-UTRAN FDD – GSM:

## A.4.4.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to GSM cell re-selection delay reported in clause 4.2.2.5.

This scenario implies the presence of 1 E-UTRAN serving cell, and 1 GSM cell to be re-selected. The UE is requested to monitor neighbouring cells on 1 E-UTRA carrier and 12 GSM cells. Test parameters are given in Table, A.4.4.1-1, A.4.4.1-2, A.4.4.1-3. E-UTRA FDD cell (Cell 1) and GSM cell (cell 2) shall belong to different Location Areas. The test comprises two successive time periods, T1 and T2. During initialization before the start of the test, the UE is camped on cell 1. By the end of T1, the UE has identified BSIC on the GSM BCCH carrier of cell 2 but the signal levels do not meet the reselection criterion during T1. At the start of T2, the signal levels change such that cell 2 satisfies reselection criterion. The GSM layer is configured at a lower priority than the serving E-UTRA FDD layer.

Table A.4.4.1-1: General test parameters for E-UTRA FDD GSM cell re-selection test case

Table A.4.4.1-2: Cell-specific test parameters for Cell 1 – E-UTRA FDD cell

Table A.4.4.1-3: Cell-specific test parameters for Cell 2 – GSM cell

## A.4.4.1.2Test Requirements

The cell re-selection delay is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send the RR Channel Request message for location update to Cell 2.

The cell re-selection delay shall be less than 26 s + TBCCH, where TBCCH is the maximum time allowed to read BCCH data from GSM cell [8].

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay can be expressed as: 4* TmeasureGSM + TBCCH, where:

TmeasureGSMSee Table 4.2.2.5.3-1 in clause 4.2.2.5.3.

TBCCHMaximum time allowed to read BCCH data from GSM cell [8]. According to [8], the maximum time allowed to read the BCCH data, when being synchronized to a BCCH carrier, is 1.9 s.

This gives a total of 25.6 s + TBCCH, allow 26 s + TBCCH in the test case.

## A.4.4.2E-UTRAN TDD – GSM:

## A.4.4.2.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD to GSM cell re-selection delay reported in clause 4.2.2.5.

This scenario implies the presence of 1 E-UTRAN serving cell, and 1 GSM cell to be re-selected. The UE is requested to monitor neighbouring cells on 1 E-UTRA carrier and 12 GSM cells. Test parameters are given in Table, A.4.4.2-1, A.4.4.2-2, A.4.4.2-3. E-UTRA TDD cell (Cell 1) and GSM cell (cell 2) shall belong to different Location Areas. The test comprises two successive time periods, T1 and T2. During initialization before the start of the test, the UE is camped on cell 1. By the end of T1, the UE has identified BSIC on the GSM BCCH carrier of cell 2 but the signal levels do not meet the reselection criterion during T1. At the start of T2, the signal levels change such that cell 2 satisfies reselection criterion. The GSM layer is configured at a lower priority than the serving E-UTRA TDD layer.

Table A.4.4.2-1: General test parameters for E-UTRA TDD GSM cell re-selection test case

Table A.4.4.2-2: Cell-specific test parameters for Cell 1 – E-UTRA TDD cell

Table A.4.4.2-3: Cell-specific test parameters for Cell 2 – GSM cell

## A.4.4.2.2Test Requirements

The cell re-selection delay is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send the RR Channel Request message for location update to Cell 2.

The cell re-selection delay shall be less than 26 s + TBCCH, where TBCCH is the maximum time allowed to read BCCH data from GSM cell [8].

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay can be expressed as: 4* TmeasureGSM + TBCCH, where:

TmeasureGSMSee Table 4.2.2.5.3-1 in clause 4.2.2.5.3.

TBCCHMaximum time allowed to read BCCH data from GSM cell [8]. According to [8], the maximum time allowed to read the BCCH data, when being synchronized to a BCCH carrier, is 1.9 s.

This gives a total of 25.6 s + TBCCH, allow 26 s + TBCCH in the test case.

## A.4.5E-UTRAN to HRPD Cell Re-Selection

## A.4.5.1E-UTRAN FDD – HRPD

## A.4.5.1.1E-UTRAN FDD – HRPD Cell Reselection: HRPD is of Lower Priority

## A.4.5.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD- HRPD inter-RAT cell reselection requirements specified in clause 4.2.2.5.4 when the HRPD cell is of lower priority.

The test scenario comprises of one HRPD and one E-UTRAN FDD cells as given in tables A.4.5.1.1.1-1, A.4.5.1.1.1-2 and A.4.5.1.1.1-3.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both E-UTRAN FDD cell 1 and HRPD cell 2 are already identified by the UE prior to the start of the test. At T1 the UE is camped on to cell 1. Cell 2 is of lower priority than cell 1. Cell 1 and cell 2 shall belong to different tracking areas.

Table A.4.5.1.1.1-1: General Test Parameters for E-UTRAN FDD - lower priority HRPD Cell Re-selection

Table A.4.5.1.1.1-2: Cell Specific Test Parameters for E-UTRAN FDD (Cell # 1)

Table A.4.5.1.1.1-3: Cell Specific Test Parameters for HRPD (cell # 2)

## A.4.5.1.1.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2 and starts to send access probe preambles on the Access Channel on cell 2.

The cell re-selection delay to the lower priority cell 2 shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateHRPD + TSI-HRPD

Where:

TevaluatHRPDSee Table 4.2.2.5.4-1

TSI-HRPDMaximum repetition period of relevant system information blocks that need to be received by the UE to camp on cell 2; 1704 ms is assumed in this test case.

This gives a total of 20.904 s for the lower priority cell reselection, allow 21 s in the test case.

## A.4.5.2E-UTRAN TDD – HRPD

## A.4.5.2.1E-UTRAN TDD – HRPD Cell Reselection: HRPD is of Lower Priority

## A.4.5.2.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD- HRPD inter-RAT cell reselection requirements specified in clause 4.2.2.5.4 when the HRPD cell is of lower priority.

The test scenario comprises of one HRPD and one E-UTRAN TDD cells as given in tables A.4.5.2.1.1-1, A.4.5.2.1.1-2 and A.4.5.2.1.1-3.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both E-UTRAN TDD cell 1 and HRPD cell 2 are already identified by the UE prior to the start of the test. At T1 the UE is camped on to cell 1. Cell 2 is of lower priority than cell 1. Cell 1 and cell 2 shall belong to different tracking areas.

Table A.4.5.2.1.1-1: General Test Parameters for E-UTRAN TDD - lower priority HRPD Cell Re-selection

Table A.4.5.2.1.1-2: Cell Specific Test Parameters for E-UTRAN TDD (Cell # 1)

Table A.4.5.2.1.1-3: Cell Specific Test Parameters for HRPD (cell # 2)

## A.4.5.2.1.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2 and starts to send access probe preambles on the Access Channel on cell 2.

The cell re-selection delay to the lower priority cell 2 shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: TevaluateHRPD + TSI-HRPD

Where:

TevaluatHRPDSee Table 4.2.2.5.4-1

TSI-HRPDMaximum repetition period of relevant system information blocks that need to be received by the UE to camp on cell 2; 1704 ms is assumed in this test case.

This gives a total of 20.904 s for the lower priority cell reselection, allow 21 s in the test case.

## A.4.6E-UTRAN to cdma2000 1X Cell Re-Selection

## A.4.6.1E-UTRAN FDD – cdma2000 1X

## A.4.6.1.1E-UTRAN FDD – cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority

## A.4.6.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD- cdma2000 1X inter-RAT cell reselection requirements specified in clause 4.2.2.5.5 when the cdma2000 1X cell is of lower priority.

The test scenario comprises of one cdma2000 1X and one E-UTRAN FDD cells as given in tables A.4.6.1.1.1-1, A.4.6.1.1.1-2 and A.4.6.1.1.1-3.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both E-UTRAN FDD cell 1 and cdma2000 1X cell 2 are already identified by the UE prior to the start of the test. At T1 the UE is camped on to cell 1. Cell 2 is of lower priority than cell 1. Cell 1 and cell 2 shall belong to different tracking areas.

Table A.4.6.1.1.1-1: General Test Parameters for E-UTRAN FDD - lower priority cdma2000 1X Cell Re-selection

Table A.4.6.1.1.1-2: Cell Specific Test Parameters for E-UTRAN FDD (Cell # 1)

Table A.4.6.1.1.1-3: Cell Specific Test Parameters for cdma2000 1X (cell # 2)

## A.4.6.1.1.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2 and starts to send access probe preambles on the Access Channel on cell 2.

The cell re-selection delay to the lower priority cell 2 shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: Tevaluatecdma2000 1X + TSI-cdma2000 1X

Where:

Tevaluatcdma2000 1XSee Table 4.2.2.5.5-1

TSI-cdma2000 1XMaximum repetition period of relevant system information blocks that need to be received by the UE to camp on cell 2; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for the lower priority cell reselection, allow 21 s in the test case.

## A.4.6.2E-UTRAN TDD – cdma2000 1X

## A.4.6.2.1E-UTRAN TDD –cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority

## A.4.6.2.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD- cdma2000 1X inter-RAT cell reselection requirements specified in clause 4.2.2.5.5 when the cdma2000 1X cell is of lower priority.

The test scenario comprises of one cdma2000 1X and one E-UTRAN TDD cells as given in tables A.4.6.2.1.1-1, A.4.6.2.1.1-2 and A.4.6.2.1.1-3.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both E-UTRAN TDD cell 1 and cdma2000 1X cell 2 are already identified by the UE prior to the start of the test. At T1 the UE is camped on to cell 1. Cell 2 is of lower priority than cell 1. Cell 1 and cell 2 shall belong to different tracking areas.

Table A.4.6.2.1.1-1: General Test Parameters for E-UTRAN TDD - lower priority cdma2000 1X Cell Re-selection

Table A.4.6.2.1.1-2: Cell Specific Test Parameters for E-UTRAN TDD (Cell # 1)

Table A.4.6.2.1.1-3: Cell Specific Test Parameters for cdma2000 1X (cell # 2)

## A.4.6.2.1.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2 and starts to send access probe preambles on the Access Channel on cell 2.

The cell re-selection delay to the lower priority cell 2 shall be less than 21 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: Tevaluatecdma2000 1X + TSI-cdma2000 1X

Where:

Tevaluatcdma2000 1XSee Table 4.2.2.5.5-1

TSI-cdma2000 1XMaximum repetition period of relevant system information blocks that need to be received by the UE to camp on cell 2; 1280 ms is assumed in this test case.

This gives a total of 20.48 s for the lower priority cell reselection, allow 21 s in the test case.

## A.4.7Idle State Positioning Measurement for UE category NB1

## A.4.7.1HD – FDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage

## A.4.7.1.1Test Purpose and Environment

The purpose of the test is to verify that the intra frequency RSTD measurement period for HD-FDD category NB1 UE meets the delay requirements specified in Clause 4.8.2.

In the test there are three synchronous cells: nCell 1, nCell 2 and nCell 3. nCell 1 is the reference cell. nCell 2 and nCell 3 are the neighbour cells. All cells are on the same RF channel.

The test consists of six consecutive time intervals, with duration of T1, T2, T3, T4, T5, and T6. nCell 1 is active throughout T1, T2, T3, T4, T5, and T6, whilst nCell 2 and nCell 3 are activated only in the beginning of T2. nCell 2 is active until the end of T5, and nCell 3 is active until the end of T4. nCell 1 transmits NPRS in T2 and T4, while nCell 2 transmits NPRS in T3 and T5, and nCell 3 transmits NPRS only in T2 and T4. Note: The information on when NPRS is muted is conveyed to the UE using PRS muting information.

Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1.

At the start of the time duration T1, the OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. The duration of T1 is sufficiently long to deliver the OTDOA assistance data and OTDOA-RequestLocationInformation to the UE and is independent of the delay requirements specified in Clause 4.8.2.

After OTDOA assistance data and OTDOA-RequestLocationInformation have been successfully received, the UE is provided with a RRC connection release command. The RRC connection release command shall be received by the UE in the last TTI of interval T1. The UE shall enter RRC_IDLE state within T seconds after the receipt of the RRC connection release, where T = 10s is the maximum delay for NB-IOT UE to perform RRC connection release as define in TS36.331 [2].

The test parameters are given in Tables A.4.7.1.1-1 A.4.7.1.1-2 and A.4.7.1.1-3.

Table A.4.7.1.1-1: General test parameters

Table A.4.7.1.1-2: Cell-specific test parameters during T1 and T6

Table A.4.7.1.1-3: Cell-specific test parameters from T2 to T5

## A.4.7.1.2Test Requirements

The RSTD measurement time fulfils the requirements specified in Clause 4.8.2.

The UE shall perform and report the RSTD measurements for nCell 2 and nCell 3 with respect to the reference cell in the OTDOA assistance data, nCell 1, within TRSTD _intra_NB-IoT-EC +TRandomAccess_NB-IoT-EC = 67.16 s starting from the beginning of time interval T4, to the moment when the UE starts to send preambles on the PRACH for sending the positioning measurement report message to nCell1.

The RSTD measurement time TRSTD _intra_NB-IoT-EC in the test is derived according to section 4.8.2. This gives the total RSTD measurement time of 11.52s for Cell 2 and Cell 3 with respect to the reference Cell 1

The random access to an already detected cell TRandomAccess_NB-IoT-EC can be expressed as: Tevaluate, NB_intra_NB-IoT-EC + TSI + TPRACH_NB-IoT,

Where:

Tevaluate, NB_intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSI = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

TPRACH_NB-IoT = 1280 ms; it is the additional delay caused by the random access procedure.

This gives TRandomAccess_NB-IoT-EC = 55.64 s for the random access delay to an already detected cell in the test case.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in Clause 9.1.10.3 , i.e., between RSTD_0000 and RSTD_12711.

## A.4.7.2HD – FDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage

## A.4.7.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement period for HD-FDD category NB1 UE meets the delay requirements specified in Clause 4.8.4.

In the test there are three synchronous cells: nCell 1, nCell 2 and nCell 3. nCell 1 is the reference cell. nCell 2 and nCell 3 are the neighbour cells.

The test consists of six consecutive time intervals, with duration of T1, T2, T3, T4, T5, and T6. nCell 1 is active throughout T1, T2, T3, T4, T5, and T6, whilst nCell 2 and nCell 3 are activated only in the beginning of T2. nCell 2 is active until the end of T5, and nCell 3 is active until the end of T4. nCell 1 transmits NPRS in T2 and T4, while nCell 2 transmits NPRS in T3 and T5, and nCell 3 transmits NPRS only in T2 and T4. Note: The information on when NPRS is muted is conveyed to the UE using PRS muting information.

Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

At the start of the time duration T1, the OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. The duration of T1 is sufficiently long to deliver the OTDOA assistance data and OTDOA-RequestLocationInformation to the UE and is independent of the delay requirements specified in Clause 4.8.2.

After OTDOA assistance data and OTDOA-RequestLocationInformation have been successfully received, the UE is provided with a RRC connection release command. The RRC connection release command shall be received by the UE in the last TTI of interval T1. The UE shall enter RRC_IDLE state within T seconds after the receipt of the RRC connection release, where T = 10s is the maximum delay for NB-IOT UE to perform RRC connection release as define in TS36.331 [2].

The test parameters are given in Tables A.4.7.2.1-1 A.4.7.2.1-2 and A.4.7.2.1-3.

Table A.4.7.2.1-1: General test parameters

Table A.4.7.2.1-2: Cell-specific test parameters during T1 and T6

Table A.4.7.2.1-3: Cell-specific test parameters from T2 to T5

## A.4.7.4.2Test Requirements

The RSTD measurement time fulfils the requirements specified in Clause 4.8.4.

The UE shall perform and report the RSTD measurements for nCell 2 and nCell 3 with respect to the reference cell in the OTDOA assistance data, nCell 1, within TRSTD _inter_NB-IoT-EC +TRandomAccess_NB-IoT-EC  = 67.16 s starting from the beginning of time interval T4, to the moment when the UE starts to send preambles on the PRACH for sending the positioning measurement report message to nCell1.

The RSTD measurement time TRSTD _inter_NB-IoT-EC  in the test is derived according to section 4.8.4. This gives the total RSTD measurement time of 11.52 s for Cell 2 and Cell 3 with respect to the reference Cell 1.

The random access to an already detected cell TRandomAccess_NB-IoT-EC  can be expressed as: Tevaluate, NB_inter_NB-IoT-EC + TSI + TPRACH_NB-IoT,

Where:

Tevaluate, NB_inter_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSI = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

TPRACH_NB-IoT = 1280 ms; it is the additional delay caused by the random access procedure.

This gives TRandomAccess_NB-IoT =55.64 s for the random access delay to an already detected cell in the test case.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in Clause 9.1.10.3, i.e., between RSTD_0000 and RSTD_12711.

## A.4.7.3TDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage

## A.4.7.3.1Test Purpose and Environment

The purpose of the test is to verify that the intra frequency RSTD measurement period for TDD category NB1 UE meets the delay requirements specified in Clause 4.8.2.In the test there are three synchronous cells: nCell 1, nCell 2 and nCell 3. nCell 1 is the reference cell. nCell 2 and nCell 3 are the neighbour cells. All cells are on the same RF channel.

The test consists of six consecutive time intervals, with duration of T1, T2, T3, T4, T5, and T6. nCell 1 is active throughout T1, T2, T3, T4, T5, and T6, whilst nCell 2 and nCell 3 are activated only in the beginning of T2. nCell 2 is active until the end of T5, and nCell 3 is active until the end of T4. nCell 1 transmits NPRS in T2 and T4, while nCell 2 transmits NPRS in T3 and T5, and nCell 3 transmits NPRS only in T2 and T4. Note: The information on when NPRS is muted is conveyed to the UE using PRS muting information.

Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1.

At the start of the time duration T1, the OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. The duration of T1 is sufficiently long to deliver the OTDOA assistance data and OTDOA-RequestLocationInformation to the UE and is independent of the delay requirements specified in Clause 4.8.2.

After OTDOA assistance data and OTDOA-RequestLocationInformation have been successfully received, the UE is provided with an RRC connection release command. The RRC connection release command shall be received by the UE in the last TTI of interval T1. The UE shall enter RRC_IDLE state within T seconds after the receipt of the RRC connection release, where T = 10s is the maximum delay for NB-IOT UE to perform RRC connection release as define in TS 36.331 [2].

The test parameters are given in Tables A.4.7.3.1-1 A.4.7.3.1-2 and A.4.7.3.1-3.

Table A.4.7.3.1-1: General test parameters

Table A.4.7.3.1-2: Cell-specific test parameters during T1 and T6

Table A.4.7.3.1-3: Cell-specific test parameters from T2 to T5

## A.4.7.3.2Test Requirements

The RSTD measurement time fulfils the requirements specified in Clause 4.8.2.

The UE shall perform and report the RSTD measurements for nCell 2 and nCell 3 with respect to the reference cell in the OTDOA assistance data, nCell 1, within TRSTD _intra_NB-IoT-EC +TRandomAccess_NB-IoT-EC = 68.44 s starting from the beginning of time interval T4, to the moment when the UE starts to send preambles on the PRACH for sending the positioning measurement report message to nCell 1.

The RSTD measurement time TRSTD _intra_NB-IoT-EC in the test is derived according to section 4.8.2. This gives the total RSTD measurement time of 11.52 s for nCell 2 and nCell 3 with respect to the reference nCell 1.

The random access to an already detected cell TRandomAccess_NB-IoT-EC can be expressed as: Tevaluate, NB_intra_NB-IoT-EC + TSI + TPRACH_NB-IoT,

Where:

Tevaluate, NB_intra_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSI = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT TDD cell.

TPRACH_NB-IoT = 2560 ms; it is the additional delay caused by the random access procedure.

This gives TRandomAccess_NB-IoT-EC = 56.92 s for the random access delay to an already detected cell in the test case.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in Clause 9.1.10.3, i.e., between RSTD_0000 and RSTD_12711.

## A.4.7.4TDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage

## A.4.7.4.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement period for TDD category NB1 UE meets the delay requirements specified in Clause 4.8.4. In the test there are three synchronous cells: nCell 1, nCell 2 and nCell 3. nCell 1 is the reference cell. nCell 2 and nCell 3 are the neighbour cells.

The test consists of six consecutive time intervals, with durations of T1, T2, T3, T4, T5, and T6. nCell 1 is active throughout T1, T2, T3, T4, T5, and T6, whilst nCell 2 and nCell 3 are activated only in the beginning of T2. nCell 2 is active until the end of T5, and nCell 3 is active until the end of T4. nCell 1 transmits NPRS in T2 and T4, while nCell 2 transmits NPRS in T3 and T5, and nCell 3 transmits NPRS only in T2 and T4. Note: The information on when NPRS is muted is conveyed to the UE using PRS muting information.

Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell 1.

At the start of the time duration T1, the OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. The duration of T1 is sufficiently long to deliver the OTDOA assistance data and OTDOA-RequestLocationInformation to the UE and is independent of the delay requirements specified in Clause 4.8.2.

After OTDOA assistance data and OTDOA-RequestLocationInformation have been successfully received, the UE is provided with a RRC connection release command. The RRC connection release command shall be received by the UE in the last TTI of interval T1. The UE shall enter RRC_IDLE state within T seconds after the receipt of the RRC connection release, where T = 10s is the maximum delay for NB-IOT UE to perform RRC connection release as define in TS 36.331 [2].

The test parameters are given in Tables A.4.7.4.1-1 A.4.7.4.1-2 and A.4.7.4.1-3.

Table A.4.7.4.1-1: General test parameters

Table A.4.7.4.1-2: Cell-specific test parameters during T1 and T6

Table A.4.7.4.1-3: Cell-specific test parameters from T2 to T5

## A.4.7.4.2Test Requirements

The RSTD measurement time fulfils the requirements specified in Clause 4.8.4.

The UE shall perform and report the RSTD measurements for nCell 2 and nCell 3 with respect to the reference cell in the OTDOA assistance data, nCell 1, within TRSTD _inter_NB-IoT-EC +TRandomAccess_NB-IoT-EC  = 78.68 s starting from the beginning of time interval T4, to the moment when the UE starts to send preambles on the PRACH for sending the positioning measurement report message to nCell 1.

The RSTD measurement time TRSTD _inter_NB-IoT-EC  in the test is derived according to section 4.8.4. This gives the total RSTD measurement time of 21.76 s for nCell 2 and nCell 3 with respect to the reference nCell 1.

The random access to an already detected cell TRandomAccess_NB-IoT-EC  can be expressed as: Tevaluate, NB_inter_NB-IoT-EC + TSI + TPRACH_NB-IoT,

Where:

Tevaluate, NB_inter_NB-IoT-ECSee Table 4.6.2.4-1 in clause 4.6.2.4

TSI = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT TDD cell.

TPRACH_NB-IoT = 2560 ms; it is the additional delay caused by the random access procedure.

This gives TRandomAccess_NB-IoT =56.92 s for the random access delay to an already detected cell in the test case.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in Clause 9.1.10.3, i.e., between RSTD_0000 and RSTD_12711.

## A.5E-UTRAN RRC CONNECTED Mode Mobility

## A.5.1E-UTRAN Handover

## A.5.1.1E-UTRAN FDD - FDD Intra frequency handover

## A.5.1.1.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements specified in clause 5.1.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.1.1-1 and A.5.1.1.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.1.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover test case

Table A.5.1.1.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover test case

## A.5.1.1.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.1.

This gives a total of 50 ms.

## A.5.1.2E-UTRAN TDD - TDD Intra frequency handover

## A.5.1.2.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover requirements specified in clause 5.2.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.2.1-1 and A.5.1.2.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.2.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

Table A.5.1.2.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

## A.5.1.2.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.1.

This gives a total of 50 ms.

## A.5.1.3E-UTRAN FDD – FDD Inter frequency handover

## A.5.1.3.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency handover requirements specified in clause 5.1.2.1.

The test scenario comprises of two E-UTRA FDD carriers and one cell on each carrier as given in tables A.5.1.3.1-1 and A.5.1.3.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.5.1.3.1-1: General test parameters for E-UTRAN FDD-FDD Inter frequency handover test case

Table A.5.1.3.1-2: Cell specific test parameters for E-UTRAN FDD-FDD Inter frequency handover test case

## A.5.1.3.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.1.

This gives a total of 50 ms.

## A.5.1.4E-UTRAN TDD – TDD Inter frequency handover

## A.5.1.4.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter frequency handover requirements specified in clause 5.2.2.4.

The test scenario comprises of two E-UTRA TDD carriers and one cell on each carrier as given in tables Table A.5.1.4.1-1 and Table A.5.1.4.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

Table A.5.1.4.1-1: General test parameters for E-UTRAN TDD-TDD Inter frequency handover test case

Table A.5.1.4.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Inter frequency handover test case

## A.5.1.4.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.1.

This gives a total of 50 ms.

## A.5.1.5E-UTRAN FDD – FDD Inter frequency handover: unknown target cell

## A.5.1.5.1Test Purpose and Environment

This test is to verify the FDD-FDD inter-frequency handover requirements for the case when the target cell is unknown as specified in clause 5.1.2.1.

The test scenario comprises of two E-UTRA FDD carriers and one cell on each carrier as given in tables A.5.1.5.1-1 and A.5.1.5.1-2. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE is expected to detect and start to transmit the PRACH to Cell 2.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.5.1.5.1-1: General test parameters for the E-UTRAN FDD-FDD Inter frequency handover test case when the target cell is unknown

Table A.5.1.5.1-2: Cell specific test parameters for the E-UTRAN FDD-FDD Inter frequency handover test case when the target cell is unknown

## A.5.1.5.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay= 15 ms, which is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt= 115 ms in the test. See clause 5.1.2.1.2.1.

This gives a total of 130 ms.

## A.5.1.6 E-UTRAN TDD – TDD Inter frequency handover; unknown Target Cell

## A.5.1.6.1Test Purpose and Environment

This test is to verify the TDD-TDD inter-frequency handover requirements for the case when the target cell is unknown as specified in clause 5.2.2.4.

The test scenario comprises of two E-UTRA TDD carriers and one cell on each carrier as given in tables A.5.1.6.1-1 and A.5.1.6.1-2. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.5.1.6.1-1: General test parameters for the E-UTRAN TDD-TDD Inter-Frequency handover test case when the target cell is unknown

Table A.5.1.6.1-2: Cell specific test parameters for the E-UTRAN TDD-TDD Inter frequency handover test case when the target cell is unknown

## A.5.1.6.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay= 15 ms, which is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt= 115 ms in the test. See clause 5.2.2.4.2.1.

This gives a total of 130 ms.

## A.5.1.7E-UTRAN FDD – TDD Inter frequency handover

## A.5.1.7.1Test Purpose and Environment

This test is to verify the requirement for the FDD-TDD inter frequency handover requirements specified in clause 5.2.2.2.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA TDD cell as given in tables Table A.5.1.7.1-1 , Table A.5.1.7.1-2 and Table A.5.1.7.1-3. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

Table A.5.1.7.1-1: General test parameters for E-UTRAN FDD-TDD Inter frequency handover test case

Table A.5.1.7.1-2: Cell specific test parameters for E-UTRAN FDD (cell #1) in E-UTRAN FDD-TDD Inter frequency handover test case

Table A.5.1.7.1-3: Cell specific test parameters for E-UTRAN TDD (cell #2) in E-UTRAN FDD-TDD Inter frequency handover test case

## A.5.1.7.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.1.

This gives a total of 50 ms.

## A.5.1.8E-UTRAN TDD – FDD Inter frequency handover

## A.5.1.8.1Test Purpose and Environment

This test is to verify the requirement for the TDD-FDD inter-frequency handover requirements specified in clause 5.2.2.3.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA FDD cell as given in tables Table A.5.1.8.1-1, Table A.5.1.8.1-2 and Table A.5.1.8.1-3.  PDCCHs indicating new transmissions should be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.5.1.8.1-1: General test parameters for E-UTRAN TDD-FDD Inter frequency handover test case

Table A.5.1.8.1-2: Cell specific test parameters for E-UTRAN TDD (cell #1) in E-UTRAN TDD-FDD Inter frequency handover test case

Table A.5.1.8.1-3: Cell specific test parameters for E-UTRAN FDD (cell #2) in E-UTRAN TDD-FDD Inter frequency handover test case

## A.5.1.8.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.1.

This gives a total of 50 ms.

## A.5.1.9E-UTRAN FDD - FDD Intra frequency handover for 5MHz bandwidth

## A.5.1.9.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.5.1.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.5.1.9.1-1 and A.5.1.9.1-2 will replace the values of corresponding parameters in Tables A.5.1.1.1-1 and A.5.1.1.1-2.

Table A.5.1.9.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover test case, 5MHz

Table A.5.1.9.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover test case, 5MHz

## A.5.1.9.2Test Requirements

The requirements defined in section A.5.1.1.2 shall apply to this test case.

## A.5.1.10E-UTRAN FDD - FDD Intra frequency handover for UE category 0

## A.5.1.10.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements specified in clause 5.1.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.10.1-1 and A.5.1.10.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.10.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover test case

Table A.5.1.10.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover test case

## A.5.1.10.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.1.

This gives a total of 50 ms.

## A.5.1.11E-UTRAN HD - FDD Intra frequency handover for UE category 0

## A.5.1.11.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements specified in clause 5.2.2.5.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.11.1-1 and A.5.1.11.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.11.1-1: General test parameters for E-UTRAN HD-FDD intra frequency handover test case

Table A.5.1.11.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover test case

## A.5.1.11.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.5.2.1.

This gives a total of 50 ms.

## A.5.1.12E-UTRAN TDD - TDD Intra frequency handover for UE category 0

## A.5.1.12.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover requirements specified in clause 5.2.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.12.1-1 and A.5.1.12.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.12.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

Table A.5.1.12.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

## A.5.1.12.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.1.

This gives a total of 50 ms.

## A.5.1.13E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.13.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements specified in clause 5.5.2.1.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.13.1-1 and A.5.1.13.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.13.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.13.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA  test case

## A.5.1.13.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 170 ms.

## A.5.1.14E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.14.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements specified in clause 5.5.2.2.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.14.1-1 and A.5.1.14.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.14.1-1: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.14.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.14.2Test Requirements

The UE shall finish the transmission of all the repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 170 ms.

## A.5.1.15E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.15.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency handover requirements specified in clause 5.5.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.15.1-1 and A.5.1.15.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.15.1-1: General test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.15.1-2: Cell specific test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.15.2Test Requirements

The UE shall finish the transmission of all the repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt =  120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.3.2.

This gives a total of 170 ms.

## A.5.1.16E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.16.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements specified in clause 5.6.2.1.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.16.1-1 and A.5.1.16.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, the UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.16.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.16.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeB test case

## A.5.1.16.2Test Requirements

The UE shall finish transmission of all repetitions of the PRACH to Cell 2 less than 2610ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560ms + 35ms = 2595ms is defined in clause 5.6.2.1.2.

This gives a total of 2610ms.

## A.5.1.17E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.17.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements specified in clause 5.6.2.2.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.17.1-1 and A.5.1.17.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. During T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.17.1-1: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.17.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.17.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 2610 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560ms + 35ms = 2595ms is defined in clause 5.6.2.1.2.

This gives a total of 2610ms.

## A.5.1.18E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.18.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover requirements specified in clause 5.6.2.3.

The test scenario comprises of one E-UTRA TDD carrier and two cells as given in tables A.5.1.18.1-1 and A.5.1.18.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. During T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, the UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.18.1-1: General test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.18.1-2: Cell specific test parameters for E-UTRAN TDD Intra frequency handover test case

## A.5.1.18.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 2610 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560ms + 35ms = 2595ms is defined in clause 5.6.2.1.2.

This gives a total of 2610 ms.

## A.5.1.19E-UTRAN FDD - FDD Intra frequency handover for UE Category 1bis

## A.5.1.19.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements for UE category 1bis specified in clause 5.1.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.19.1-1 and A.5.1.19.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.19.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover test case

Table A.5.1.19.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover test case

## A.5.1.19.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.

This gives a total of 50 ms.

## A.5.1.20E-UTRAN TDD - TDD Intra frequency handover for UE Category 1bis

## A.5.1.20.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover requirements for UE category 1bis specified in clause 5.2.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.20.1-1 and A.5.1.20.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.20.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

Table A.5.1.20.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

## A.5.1.20.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.

This gives a total of 50 ms.

## A.5.1.21E-UTRAN FDD - FDD Intra frequency RACH-less handover

## A.5.1.21.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency RACH-less handover requirements specified in clause 5.1.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.21.1-1 and A.5.1.21.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying RACH-less handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.21.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency RACH-less handover test case

Table A.5.1.21.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency RACH-less handover test case

## A.5.1.21.2Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 45 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 30 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.2.

This gives a total of 45 ms.

## A.5.1.22E-UTRAN TDD - TDD Intra frequency RACH-less handover

## A.5.1.22.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency RACH-less handover requirements specified in clause 5.2.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.22.1-1 and A.5.1.22.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying RACH-less handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.5.1.22.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency RACH-less handover test case

Table A.5.1.22.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency RACH-less handover test case

## A.5.1.22.2Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 45 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 30 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.

This gives a total of 45 ms.

## A.5.1.23E-UTRAN FDD – FDD Inter frequency RACH-less handover

## A.5.1.23.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency RACH-less handover requirements specified in clause 5.1.2.1.

The test scenario comprises of two E-UTRA FDD carriers and one cell on each carrier as given in tables A.5.1.23.1-1 and A.5.1.23.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

A RRC message implying RACH-less handover shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.5.1.23.1-1: General test parameters for E-UTRAN FDD-FDD Inter frequency RACH-less handover test case

Table A.5.1.23.1-2: Cell specific test parameters for E-UTRAN FDD-FDD Inter frequency RACH-less handover test case

## A.5.1.23.2Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 45 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 30 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.

This gives a total of 45 ms.

## A.5.1.24E-UTRAN TDD – TDD Inter frequency RACH-less handover

## A.5.1.24.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter frequency RACH-less handover requirements specified in clause 5.2.2.4.

The test scenario comprises of two E-UTRA TDD carriers and one cell on each carrier as given in tables Table A.5.1.24.1-1 and Table A.5.1.24.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying RACH-less handover to cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1.

Table A.5.1.24.1-1: General test parameters for E-UTRAN TDD-TDD Inter frequency RACH-less handover test case

Table A.5.1.24.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Inter frequency RACH-less handover test case

## A.5.1.24.2Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 45 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 30 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.

This gives a total of 45 ms.

## A.5.1.25E-UTRAN FDD - FDD Intra frequency make-before-break handover

## A.5.1.25.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency make-before-break handover requirements specified in clause 5.1.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.25.1-1 and A.5.1.25.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying make-before-break handover to cell 2. The RRC message implying make-before-break handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying make-before-break handover.

Table A.5.1.25.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency make-before-break handover test case

Table A.5.1.25.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency make-before-break handover test case

## A.5.1.25.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The make-before-break handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.1.2.1.2.3.

This gives a total of 50 ms.

The UE shall be scheduled on Cell 1 continuously throughout the test. From the start of T3 until the UE start to transmit the PRACH, at most 5 of all expected ACK/NACKs can be not transmitted by the UE.

Both the rate of correct handovers and the number of not transmitted ACK/NACKs have to be fulfilled simultaneously.

## A.5.1.26E-UTRAN TDD - TDD Intra frequency make-before-break handover

## A.5.1.26.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency make-before-break handover requirements specified in clause 5.2.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.26.1-1 and A.5.1.26.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send a RRC message implying make-before-break handover to cell 2. The RRC message implying make-before-break handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying make-before-break handover.

Table A.5.1.26.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency make-before-break handover test case

Table A.5.1.26.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency make-before-break handover test case

## A.5.1.26.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct make-before-break handovers observed during repeated tests shall be at least 90%.

NOTE:The make-before-break handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.2.2.4.2.3.

This gives a total of 50 ms.

The UE shall be scheduled on Cell 1 continuously throughout the test. From the start of T3 until the UE start to transmit the PRACH, at most 3 of all expected ACK/NACKs can be not transmitted by the UE.

Both the rate of correct handovers and the number of not transmitted ACK/NACKs have to be fulfilled simultaneously.

## A.5.1.27E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.27.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency handover requirements specified in clause 5.5.2.1.

The test scenario comprises of two E-UTRA FDD carriers and one cell in each carrier as given in tables A.5.1.27.1-1 and A.5.1.27.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.27.1-1: General test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.27.1-2: Cell specific test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.27.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 170 ms.

## A.5.1.28E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.28.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency handover requirements specified in clause 5.5.2.2.

The test scenario comprises of two E-UTRA FDD carriers and one cell in each carrier as given in tables A.5.1.28.1-1 and A.5.1.28.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.28.1-1: General test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.28.1-2: Cell specific test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.28.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 170 ms.

## A.5.1.29E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeA

## A.5.1.29.1Test Purpose and Environment

This test is to verify the requirement for the TDD inter frequency handover requirements specified in clause 5.5.2.3.

The test scenario comprises of two E-UTRA TDD carriers and one cell in each carrier as given in tables A.5.1.29.1-1 and A.5.1.29.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.29.1-1: General test parameters for E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeA test case

Table A.5.1.29.1-2: Cell specific test parameters for E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeA test case

## A.5.1.29.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 170 ms.

## A.5.1.30E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.30.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency handover requirements specified in clause 5.5.3.1.

The test scenario comprises of two E-UTRA FDD carriers and one cell in each carrier as given in tables A.5.1.30.1-1 and A.5.1.30.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.30.1-1: General test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.30.1-2: Cell specific test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB test case

## A.5.1.30.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 2610 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 2610 ms.

## A.5.1.31E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.31.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency handover requirements specified in clause 5.5.3.2.

The test scenario comprises of two E-UTRA FDD carriers and one cell in each carrier as given in tables A.5.1.31.1-1 and A.5.1.31.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.31.1-1: General test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.31.1-2: Cell specific test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB test case

## A.5.1.31.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 2610 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 2610 ms.

## A.5.1.32E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeB

## A.5.1.32.1Test Purpose and Environment

This test is to verify the requirement for the TDD inter frequency handover requirements specified in clause 5.5.3.3.

The test scenario comprises of two E-UTRA TDD carriers and one cell in each carrier as given in tables A.5.1.32.1-1 and A.5.1.32.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

During the test, UE is configured with measurement gap to enable inter-frequency monitoring.

Table A.5.1.32.1-1: General test parameters for E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeB test case

Table A.5.1.32.1-2: Cell specific test parameters for E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeB test case

## A.5.1.32.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 2610 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560 + 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 2610 ms.

## A.5.1.33E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition

## A.5.1.33.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.2.1.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.33.1-1 and A.5.1.33.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.33.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.5.1.33.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.5.1.13.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 50 ms.

## A.5.1.34E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition

## A.5.1.34.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.2.2.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.34.1-1 and A.5.1.34.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.34.1-1: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.5.1.34.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.5.1.34.2Test Requirements

The UE shall finish the transmission of all the repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 50 ms.

## A.5.1.35E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition

## A.5.1.35.1Test Purpose and Environment

This test is to verify the requirement for the TDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.2.3.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.35.1-1 and A.5.1.35.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.35.1-1: General test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.5.1.35.1-2: Cell specific test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.5.1.35.2Test Requirements

The UE shall finish the transmission of all the repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.5.2.1.2.

This gives a total of 50 ms.

## A.5.1.36E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition

## A.5.1.36.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.3.1.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.36.1-1 and A.5.1.36.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, the UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.36.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

Table A.5.1.36.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

## A.5.1.36.2Test Requirements

The UE shall finish transmission of all repetitions of the PRACH to Cell 2 less than 50ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35ms is defined in clause 5.6.2.1.2.

This gives a total of 50ms.

## A.5.1.37E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition

## A.5.1.37.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.3.2.

The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.5.1.37.1-1 and A.5.1.37.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. During T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.37.1-1: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

Table A.5.1.37.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

## A.5.1.37.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35ms is defined in clause 5.6.2.1.2.

This gives a total of 50ms.

## A.5.1.38E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition

## A.5.1.38.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover requirements without SFN acquisition specified in clause 5.5.3.3.

The test scenario comprises of one E-UTRA TDD carrier and two cells as given in tables A.5.1.38.1-1 and A.5.1.38.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

During period T2, the UE should report Event A3, and afterwards E-UTRAN shall send a RRC message to the UE implying handover to Cell 2. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. During T3 is defined as the end of the last TTI containing the RRC message from UE implying handover.

During the test, the UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.5.1.38.1-1: General test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

Table A.5.1.38.1-2: Cell specific test parameters for E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

## A.5.1.38.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35ms is defined in clause 5.6.2.1.2.

This gives a total of 50 ms.

## A.5.1.39E-UTRAN FDD - FDD Intra frequency handover with direct SCell activation

## A.5.1.39.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover with direct SCell activation requirements specified in subclause 7.7.19.

The test scenario comprises of two E-UTRA FDD carriers and 2 cells as given in tables A.5.1.39.1-1 and A.5.1.39.1-2. The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell and SCell1 (cell 2) is in activated state and UE is reporting CQI for both PCell and SCell1.

Time period T2 starts when UE receives a handover command that also activates SCell1 (Cell2). This is done using an RRCConnectionReconfiguration message with parameter sCellState set to activated for the SCell1 (Cell 2). The message is sent from the test equipment to the UE and is received in a subframe # denoted m at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (m + Ndirect).

Time period T3 starts at (m + Ndirect), at which point UE shall be reporting a valid CQI for both PCell and SCell1.

Table A.5.1.39.1-1: General test parameters for E-UTRAN FDD-FDD intra-frequency handover with direct SCell activation test case

Table A.5.1.39.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover with direct SCell activation test case

## A.5.1.39.2Test Requirements

The UE shall be capable to transmit valid CSI report for the directly activated SCell1 no later than in subframe m+Ndirect.

The rate of correct observed SCell1 direct activation delay during repeated tests shall be at least 90%.

NOTE:The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + TIU + T2 + T3 + Tinterupt_window + Ttime_direct, where:

TRRC_Process is the RRC procedure delay = 20 ms which is the RRC procedure delay defined for SCell addition in clause 11.2 of TS 36.331 [2],

Tinterrupt is the interruption time as defined in subclause 5.1.2.1.2,

T2 is the delay for obtaining a valid TA command for the target PCell from the target PCell and the scheduling grant for sending valid CSI report in the target PCell. T2 is up to [13] subframes,

T3 is the delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to 6 subframes,

Tinterupt_window is the interruption window which is 5ms for FDD and

Ttime_direct is the direct SCell activation delay.  If the SCell is known, then Ttime_direct is 20 ms. If the SCell is unknown, then Ttime_direct is 30 ms provided the SCell can be successfully detected on the first attempt.

This gives a total of Ndirect = 65 + TIU + T2 + T3 ms = 65 + 10 + 13 + 6 = 94 ms.

During T3 the UE shall send valid CSI reports for PCell and SCell1 with non-zero CQI index and continue to send CSI reports for PCell and SCell1 (Cell 2) with non-zero CQI index until the end of T3.

All of the above test requirements shall be fulfilled in order for the observed SCell1 direct activation delay to be counted as correct.

## A.5.1.40E-UTRAN TDD - TDD Intra frequency handover with direct SCell activation

## A.5.1.40.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency handover with direct SCell activation requirements specified in subclause 7.7.19.

The test scenario comprises of two E-UTRA TDD carriers and 2 cells as given in tables A.5.1.40.1-1 and A.5.1.40.1-2. The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell and SCell1 (cell 2) is in activated state and UE is reporting CQI for both PCell and SCell1.

Time period T2 starts when UE receives a handover command that also activates SCell1 (Cell2). This is done using an RRCConnectionReconfiguration message with parameter sCellState set to activated for the SCell1 (Cell 2). The message is sent from the test equipment to the UE and is received in a subframe # denoted m at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (m+ Ndirect).

Time period T3 starts at (m+ Ndirect), at which point UE shall be reporting a valid CQI for both PCell and SCell1.

Table A.5.1.40.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

Table A.5.1.40.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency handover test case

## A.5.1.40.2Test Requirements

The UE shall be capable to transmit valid CSI report for the directly activated SCell1 no later than in subframe m+Ndirect.

The rate of correct observed SCell1 direct activation delay during repeated tests shall be at least 90%.

NOTE:The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + TIU + T2 + T3 + Tinterupt_window + Ttime_direct, where:

TRRC_Process is the RRC procedure delay = 20 ms which is the RRC procedure delay defined for SCell addition in clause 11.2 of TS 36.331 [2],

Tinterrupt is the interruption time as defined in subclause 5.1.2.1.2,

T2 is the delay for obtaining a valid TA command for the target PCell from the target PCell and the scheduling grant for sending valid CSI report in the target PCell. T2 is up to [13] subframes,

T3 is the delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to 6 subframes,

Tinterupt_window is the interruption window which is 7 ms for TDD and

Ttime_direct is the direct SCell activation delay.  If the SCell is known, then Ttime_direct is 20 ms. If the SCell is unknown, then Ttime_direct is 30 ms provided the SCell can be successfully detected on the first attempt.

This gives a total of Ndirect = 67 + TIU+ T2 + T3 ms = 67 + 10 + 13 + 6 = 96 ms.

During T3 the UE shall send valid CSI reports for PCell and SCell1 with non-zero CQI index and continue to send CSI reports for PCell and SCell1 (Cell 2) with non-zero CQI index until the end of T3.

All of the above test requirements shall be fulfilled in order for the observed SCell1 direct activation delay to be counted as correct.

## A.5.1.41E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover

## A.5.1.41.1Test Purpose and Environment

This test is to verify the requirement for the FDD – FDD Intra-band Inter-frequency sync DAPS handover specified in clause 5.7.2.1. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA FDD cell on the same band as given in tables Table A.5.1.41.1-1 and Table A.5.1.41.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.41.1-1: General test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover test case

Table A.5.1.41.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover test case

## A.5.1.41.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 5ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 20ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 5ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 5 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 20 ms.

## A.5.1.42E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover

## A.5.1.42.1Test Purpose and Environment

This test is to verify the requirement for the FDD – FDD Intra-band Inter-frequency async DAPS handover specified in clause 5.7.2.1. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA FDD cell on the same band as given in tables Table A.5.1.42.1-1 and Table A.5.1.42.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.42.1-1: General test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover test case

Table A.5.1.42.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover test case

## A.5.1.42.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 6ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 21ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 6ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 6 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 21 ms.

## A.5.1.43E-UTRAN FDD – FDD Inter-band Inter-frequency sync DAPS handover

## A.5.1.43.1Test Purpose and Environment

This test is to verify the requirement for the FDD – FDD Inter-band Inter-frequency sync DAPS handover specified in clause 5.7.2.1. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA FDD cell on the different band as given in tables Table A.5.1.43.1-1 and Table A.5.1.43.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.43.1-1: General test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover test case

Table A.5.1.43.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover test case

## A.5.1.43.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T2. During Dhandover1 the interruption on Cell 1 shall not exceed 1ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 16ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 1ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 1 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 16 ms.

## A.5.1.44E-UTRAN FDD – FDD Inter-band Inter-frequency async DAPS handover

## A.5.1.44.1Test Purpose and Environment

This test is to verify the requirement for the FDD – FDD Inter-band Inter-frequency async DAPS handover specified in clause 5.7.2.1. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA FDD cell on the different band as given in tables Table A.5.1.44.1-1 and Table A.5.1.44.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.44.1-1: General test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover test case

Table A.5.1.44.1-2: Cell specific test parameters for E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover test case

## A.5.1.44.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 2ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 17ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 2ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 2 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 17 ms.

## A.5.1.45E-UTRAN FDD - FDD Intra frequency DAPS handover

## A.5.1.45.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency DAPS handover requirements specified in clause 5.7.2.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.45.1-1 and A.5.1.45.1-2. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

Cell 1 shall send a RRC message implying DAPS handover to cell 2. The RRC message implying target cell add shall be sent to the UE during period T2, after the UE has reported Event A3. The start of time duration T3 is defined as the end of the last TTI containing the RRC message implying DAPS handover.

During period T3, UE shall be able to perform random access to cell 2. DL scheduling and UL feedback to cell 1 shall be avoided during the random access procedure to cell 2. After successful random access procedure to cell 2, UE is scheduled with PDSCH from cell 1 and cell 2 in alternative TTIs where cell 1 and cell 2 belong to the same TAG.

Cell 2 shall send another RRC message implying source cell release. The RRC message implying source cell release shall be sent to the UE during period T3, after the UE has successfully sent PRACH to cell 2. The start of the time duration T4 is defined as the end of the last TTI containing the RRC message implying source cell release.

UE shall stop periodic reporting of CSI to cell 1 during T5.

Table A.5.1.45.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency DAPS handover test case

Table A.5.1.45.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency DAPS handover test case

## A.5.1.45.1Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Dhandover1, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Dhandover1 = 35 and is defined in clause 5.7.2.1.1.

This gives a total of 50 ms.

During Dhandover1, the UE is allowed an interruption of up to Tinterrupt1 on cell 1. Tinterrupt1 is defined in clause 5.7.2.1.2.

After successful RACH to cell 2 and until the start of time period T4, UE shall be able to successfully receive PDSCH alternatively from cell 1 and cell 2. UE is not expected to transmit UL to both cell 1 and cell 2 in the same TTI.

The UE shall release cell 2 less than Dhandover2 from the beginning of time period T4. Dhandover2 is defined in clause 5.7.2.1.2.

During Dhandover2, the UE is allowed an interruption of up to Tinterrupt2 on cell 2. Tinterrupt2 is defined in clause 5.7.2.1.2. UE shall not report CSI to cell 1 during T5.

## A.5.1.46E-UTRAN TDD - TDD Intra frequency DAPS handover

## A.5.1.46.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency DAPS handover requirements specified in clause 5.7.2.4.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.46.1-1 and A.5.1.46.1-2. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

Cell 1 shall send a RRC message implying DAPS handover to cell 2. The RRC message implying target cell add shall be sent to the UE during period T2, after the UE has reported Event A3. The start of time duration T3 is defined as the end of the last TTI containing the RRC message implying DAPS handover.

During period T3, UE shall be able to perform random access to cell 2. DL scheduling and UL feedback to cell 1 shall be avoided during the random access procedure to cell 2. After successful random access procedure to cell 2, UE is scheduled with PDSCH from cell 1 and cell 2 in alternative TTIs where cell 1 and cell 2 belong to the same TAG.

Cell 2 shall send another RRC message implying source cell release. The RRC message implying source cell release shall be sent to the UE during period T3, after the UE has successfully sent PRACH to cell 2. The start of the time duration T4 is defined as the end of the last TTI containing the RRC message implying source cell release.

UE shall stop periodic reporting of CSI to cell 1 during T5.

Table A.5.1.46.1-1: General test parameters for E-UTRAN TDD-TDD Intra frequency DAPS handover test case

Table A.5.1.46.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Intra frequency DAPS handover test case

## A.5.1.46.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Dhandover1, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Dhandover1 = 35 and is defined in clause 5.7.2.1.1.

This gives a total of 50 ms.

During Dhandover1, the UE is allowed an interruption of up to Tinterrupt1 on cell 1. Tinterrupt1 is defined in clause 5.7.2.1.2.

After successful RACH to cell 2 and until the start of time period T4, UE shall be able to successfully receive PDSCH alternatively from cell 1 and cell 2. UE is not expected to transmit UL to both cell 1 and cell 2 in the same TTI.

The UE shall release cell 2 less than Dhandover2 from the beginning of time period T4. Dhandover2 is defined in clause 5.7.2.1.2.

During Dhandover2, the UE is allowed an interruption of up to Tinterrupt2 on cell 2. Tinterrupt2 is defined in clause 5.7.2.1.2. UE shall not report CSI to cell 1 during T5.

## A.5.1.47E-UTRAN FDD - FDD Intra frequency conditional handover

## A.5.1.47.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency conditional handover requirements specified in clause 5.1.2.6.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.5.1.47.1-1 and A.5.1.47.1-2. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.47.1-1: General test parameters for E-UTRAN FDD-FDD intra frequency conditional handover test case

Table A.5.1.47.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency conditional handover test case

## A.5.1.47.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 860 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 800 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.48E-UTRAN TDD - TDD Intra frequency conditional handover

## A.5.1.48.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD intra frequency conditional handover requirements specified in clause 5.1.2.9.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.5.1.48.1-1 and A.5.1.48.1-2. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.48.1-1: General test parameters for E-UTRAN TDD-TDD intra frequency conditional handover test case

Table A.5.1.48.1-2: Cell specific test parameters for E-UTRAN TDD-TDD intra frequency conditional handover test case

## A.5.1.48.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 860 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 800 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.49E-UTRAN FDD - FDD Inter frequency conditional handover

## A.5.1.49.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter-frequency conditional handover requirements specified in clause 5.1.2.6.

The test scenario comprises of two E-UTRA FDD carriers and one cell on each carrier as given in tables A.5.1.49.1-1 and A.5.1. 49.1-2. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.49.1-1: General test parameters for E-UTRAN FDD-FDD Inter frequency conditional handover test case

Table A.5.1.49.1-2: Cell specific test parameters for E-UTRAN FDD-FDD Inter frequency conditional handover test case

## A.5.1.49.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 3900 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 3840 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.50E-UTRAN TDD - TDD Inter frequency conditional handover

## A.5.1.50.1Test Purpose and Environment

This test is to verify the requirement for the TDD-TDD inter-frequency conditional handover requirements specified in clause 5.1.2.9.

The test scenario comprises of two E-UTRA TDD carriers and one cell on each carrier as given in tables A.5.150.1-1 and A.5.1. 50.1-2. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.50.1-1: General test parameters for E-UTRAN TDD-TDD Inter frequency conditional handover test case

Table A.5.1.50.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Inter frequency conditional handover test case

## A.5.1.50.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 3900 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 3840 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.51E-UTRAN FDD - TDD Inter frequency conditional handover

## A.5.1.51.1Test Purpose and Environment

This test is to verify the requirement for the FDD-TDD inter-frequency conditional handover requirements specified in clause 5.1.2.7.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA TDD cell as given in tables A.5.1.51.1-1, A.5.1. x+4.1-2 and A.5.1. 51.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.51.1-1: General test parameters for E-UTRAN FDD-TDD Inter frequency conditional handover test case

Table A.5.1.51.1-2: Cell specific test parameters for E-UTRAN FDD (cell #1) in E-UTRAN FDD-TDD Inter frequency conditional handover test case

Table A.5.1.51.1-3: Cell specific test parameters for E-UTRAN TDD (cell #2) in E-UTRAN FDD-TDD Inter frequency conditional handover test case

## A.5.1.51.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 3900 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 3840 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.52E-UTRAN TDD - FDD Inter frequency conditional handover

## A.5.152.1Test Purpose and Environment

This test is to verify the requirement for the TDD-FDD inter-frequency conditional handover requirements specified in clause 5.1.2.8.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA FDD cell as given in tables A.5.1.52.1-1, A.5.1.52.1-2 and A.5.1.52.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

E-UTRAN shall send an RRC message implying conditional handover to cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.5.1.52.1-1: General test parameters for E-UTRAN TDD-FDD Inter frequency conditional handover test case

Table A.5.1.52.1-2: Cell specific test parameters for E-UTRAN TDD (cell #1) in E-UTRAN TDD-FDD Inter frequency conditional handover test case

Table A.5.1.52.1-3: Cell specific test parameters for E-UTRAN FDD (cell #2) in E-UTRAN TDD-FDD Inter frequency conditional handover test case

## A.5.1.52.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 3900 ms from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 3840 ms in the test; Tmeasure is defined in clause 5.1.2.6.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.1.2.6.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

## A.5.1.53E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover

## A.5.1.53.1Test Purpose and Environment

This test is to verify the requirement for the TDD – TDD Intra-band Inter-frequency sync DAPS handover specified in clause 5.7.2.4. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA TDD cell on the same band as given in tables Table A.5.1.53.1-1 and Table A.5.1.53.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stops to send CSI report to the source cell.

Table A.5.1.53.1-1: General test parameters for E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover test case

Table A.5.1.53.1-2: Cell specific test parameters for E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover test case

## A.5.1.53.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 5ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 20ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 5ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 5 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 20 ms.

## A.5.1.54E-UTRAN TDD – TDD Inter-band Inter-frequency sync DAPS handover

## A.5.1.54.1Test Purpose and Environment

This test is to verify the requirement for the TDD – TDD Inter-band Inter-frequency sync DAPS handover specified in clause 5.7.2.4. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA TDD cell on the different band as given in tables Table A.5.1.54.1-1 and Table A.5.1.54.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stops to send CSI report to the source cell.

Table A.5.1.54.1-1: General test parameters for E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover test case

Table A.5.1.54.1-2: Cell specific test parameters for E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover test case

## A.5.1.54.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T2. During Dhandover1 the interruption on Cell 1 shall not exceed 1ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 16ms ((Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 1ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 1 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 16 ms.

## A.5.1.55E-UTRAN FDD - TDD inter-band inter-frequency synchronous DAPS handover

## A.5.1.55.1Test Purpose and Environment

This test is to verify the requirement for the FDD-TDD inter-band inter-frequency synchronous DAPS handover requirements specified in clause 5.7.2.2.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA TDD cell as given in tables A.5.1.55.1-1, A.5.1.55.1-2 and A.5.1.55.1-3. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

At the start of time duration T1, the UE does not have any timing information of Cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

Starting T2, Cell 2 becomes detectable. During T2, the UE performs cell detection and measurements on Cell 2 and shall send event report to the network. After receiving the event report A3, the test system should send an RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover command is sent to the UE. During T3, UE should be continuously scheduled on Cell 1 and shall perform random access to Cell 2. DL scheduling and UL feedback to Cell 1 should be avoided when UE is required to perform DL reception or UL transmission in Cell 2, except preamble transmission. After successful RACH procedure in Cell 2 is completed, the test system should send an RRC message implying Cell 1 release command.

The start of T4 is the instant when the last TTI containing the RRC message implying Cell 1 release command is sent to the UE. During T4, the UE shall accomplish the release actions within Dhandover2.

Starting T5, the UE shall stop to send CSI report to Cell 1.

Table A.5.1.55.1-1: General test parameters for E-UTRAN FDD-TDD inter-band inter-frequency synchronous DAPS handover test case

Table A.5.1.55.1-2: Cell specific test parameters for E-UTRAN FDD (Cell 1) in E-UTRAN FDD-TDD inter-band inter-frequency synchronous DAPS handover test case

Table A.5.1.55.1-3: Cell specific test parameters for E-UTRAN TDD (Cell 2) in E-UTRAN FDD-TDD inter-band inter-frequency synchronous DAPS handover test case

A.5.1.55.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Dhandover1 = 65 ms from the start of T3 and interruption on Cell 1 during T3 shall not exceed Tinterrupt1 = 1ms.

The UE shall complete to release Cell 1 less than Dhandover2 = 16 ms from the start of T4 and interruption on Cell 2 during T4 shall not exceed Tinterrupt2 = 1ms.

The rate of correct DAPS handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + Tsearch + TIU + 20ms, and Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tsearch = 0 ms in the test as it is assumed as known cell; Tsearch is defined in clause 5.7.2.1.1.

TIU = 30 ms in the test; TCHO_execution is defined in clause 5.7.2.1.1.

Tinterrupt1 = 1 ms in the test; Tinterrupt is defined in clause 5.7.2.1.2.

Tinterrupt2 = 1 ms in the test; Tinterrupt is defined in clause 5.7.2.1.2.

This gives a total of 65 ms for Dhandover1 and 16 ms for Dhandover2.

The UE shall not transmit CSI reports on Cell 1 after T5.

## A.5.1.56E-UTRAN TDD - FDD inter-band inter-frequency synchronous DAPS handover

## A.5.1.56.1Test Purpose and Environment

This test is to verify the requirement for the TDD-FDD inter-band inter-frequency synchronous DAPS handover requirements specified in clause 5.7.2.3.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA FDD cell as given in tables A.5.1.x+1.1-1, A.5.1.x+1.1-2 and A.5.1.x+1.1-3. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

At the start of time duration T1, the UE does not have any timing information of Cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-frequency monitoring.

Starting T2, Cell 2 becomes detectable. During T2, the UE performs cell detection and measurements on Cell 2 and shall send event report to the network. After receiving the event report A3, the test system should send an RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover command is sent to the UE. During T3, UE should be continuously scheduled on Cell 1 and should be able to perform random access to Cell 2. DL scheduling and UL feedback to Cell 1 should be avoided when UE is required to perform DL reception or UL transmission in Cell 2, except preamble transmission. After successful RACH procedure of Cell 2 is completed, the test system should send an RRC message implying Cell 1 release command.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover command is sent to the UE. During T3, UE should be continuously scheduled on Cell 1 and shall perform random access to Cell 2. DL scheduling and UL feedback to Cell 1 should be avoided when UE is required to perform DL reception or UL transmission in Cell 2, except preamble transmission. After successful RACH procedure in Cell 2 is completed, the test system should send an RRC message implying Cell 1 release command.

The start of T4 is the instant when the last TTI containing the RRC message implying Cell 1 release command is sent to the UE. During T4, the UE shall accomplish the release actions within Dhandover2.

Starting T5, the UE should stop to send CSI report to Cell 1.

Table A.5.1.56.1-1: General test parameters for E-UTRAN TDD-FDD inter-band inter-frequency synchronous DAPS handover test case

Table A.5.1.56.1-2: Cell specific test parameters for E-UTRAN TDD (Cell 1) in E-UTRAN TDD-FDD inter-band inter-frequency synchronous DAPS handover test case

Table A.5.1.56.1-3: Cell specific test parameters for E-UTRAN FDD (Cell 2) in E-UTRAN TDD-FDD inter-band inter-frequency synchronous DAPS handover test case

## A.5.1.56.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Dhandover1 = 65 ms from the start of T3 and interruption on Cell 1 during T3 shall not exceed Tinterrupt1 = 1ms.

The UE shall complete to release Cell 1 less than Dhandover2 = 16 ms from the start of T4 and interruption on Cell 2 during T4 shall not exceed Tinterrupt2 = 1ms.

The rate of correct DAPS handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + Tsearch + TIU + 20ms, and Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tsearch = 0 ms in the test as it is assumed as known cell; Tsearch is defined in clause 5.7.2.1.1.

TIU = 30 ms in the test; TCHO_execution is defined in clause 5.7.2.1.1.

Tinterrupt1 = 1 ms in the test; Tinterrupt is defined in clause 5.7.2.1.2.

Tinterrupt2 = 1 ms in the test; Tinterrupt is defined in clause 5.7.2.1.2.

This gives a total of 65 ms for Dhandover1 and 16 ms for Dhandover2.

The UE shall not transmit CSI reports on Cell 1 after T5.

## A.5.1.57E-UTRAN FDD – TDD Inter-band Inter-frequency async DAPS handover

## A.5.1.57.1Test Purpose and Environment

This test is to verify the requirement for the FDD – TDD Inter-band Inter-frequency async DAPS handover specified in clause 5.7.2.2. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA FDD cell and one E-UTRA TDD cell on the different band as given in tables Table A.5.1.57.1-1 and Table A.5.1.57.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.57.1-1: General test parameters for E-UTRAN FDD – TDD Intra-band Inter-frequency async DAPS handover test case

Table A.5.1.57.1-2: Cell specific test parameters for E-UTRAN FDD – TDD Inter-band Inter-frequency async DAPS handover test case

## A.5.1.57.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 2ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 17ms (Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 2ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 2 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 17 ms.

## A.5.1.58E-UTRAN TDD – FDD Inter-band Inter-frequency async DAPS handover

## A.5.1.58.1Test Purpose and Environment

This test is to verify the requirement for the TDD – FDD Inter-band Inter-frequency async DAPS handover specified in clause 5.7.2.3. Both handover delay and interruption length are tested.

The test scenario comprises of one E-UTRA TDD cell and one E-UTRA FDD cell on the different band as given in tables Table A.5.1.58.1-1 and Table A.5.1.58.1-2. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would not enter the DRX state. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be continuously scheduled on Cell 1 and shall be able to perform random access to Cell 2. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop to send CSI report to the source cell.

Table A.5.1.58.1-1: General test parameters for E-UTRAN TDD – FDD Inter-band Inter-frequency async DAPS handover test case

Table A.5.1.58.1-2: Cell specific test parameters for E-UTRAN TDD – FDD Inter-band Inter-frequency async DAPS handover test case

## A.5.1.58.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 50 ms (Dhandover1) from the beginning of time period T3. During Dhandover1 the interruption on Cell 1 shall not exceed 2ms (Tinterrupt1).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover1 can be expressed as: Dhandover1 = TRRC_procedure + TIU + 20 ms.

The UE shall complete to release Cell 1 less than 17ms (Dhandover2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed 2ms (Tinterrupt2).

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt2 = 2 ms in the test; Tinterrupt2 is defined in clause 5.7.2.1.2.

This gives a total of 17 ms.

## A.5.2E-UTRAN Handover to other RATs

## A.5.2.1E-UTRAN FDD – UTRAN FDD Handover

## A.5.2.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to UTRAN FDD handover requirements specified in clause 5.3.1.

The test parameters are given in Tables A.5.2.1.1-1, A.5.2.1.1-2 and A.5.2.1.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.2.1.1-1: General test parameters for E-UTRAN FDD to UTRAN FDD handover test case

Table A.5.2.1.1-2: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 1)

Table A.5.2.1.1-3: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 2)

## A.5.2.1.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 190 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.1.1.1.

Tinterrupt = 140 ms in the test; Tinterrupt is defined in clause 5.3.1.1.2.

This gives a total of 190 ms.

## A.5.2.2E-UTRAN TDD - UTRAN FDD Handover

## A.5.2.2.1Test Purpose and Environment

This test is to verify the E-UTRAN TDD – UTRAN FDD handover requirements specified in clause 5.3.1.

The test scenario comprises of one E-UTRAN TDD cell and one UTRAN FDD cell as given in the tables A.5.2.2.1-1, A5.2.2.1-2 and A.5.2.2.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At start of time duration T1, the UE does not have any timing information of cell 2. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before the start of T2 to enable the monitoring of UTRAN FDD. A neighbouring cell list, including the UTRAN cell (cell2), shall be sent to the UE before T2 starts. During the time T2 cell 2 becomes detectable and the UE is expected to detect and send the measurement report. A RRC message implying handover shall be sent to the UE during T2, after the UE has reported event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.2.2.1-1: General test parameters for E-UTRAN TDD-UTRAN FDD handover

Table A.5.2.2.1-2: Cell specific test parameters for E-UTRAN TDD (cell 1) for handover to UTRAN FDD (cell # 2)

Table A.5.2.2.1-3: Cell specific test parameters for UTRAN FDD (cell # 2) for handover from E-UTRAN TDD cell (cell #1)

## A.5.2.2.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 190 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.1.1.1.1.

Tinterrupt = 140 ms in the test; Tinterrupt is defined in clause 5.3.1.1.2.

This gives a total of 190 ms.

## A.5.2.3 E-UTRAN FDD- GSM Handover

## A.5.2.3.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to GSM cell handover delay specified in clause 5.3.3.

The test parameters are given in Table A.5.2.3.1 -1, A.5.2.3.1 -2 and A.5.2.3.1 -3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event B1 shall be used. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

The RRC message implying handover to cell 2 shall be sent to the UE during period T2, after the UE has reported Event B1. The start of T3 is defined as the end of last E-UTRAN TTI containing the RRC message implying handover.

The requirements are also applicable for a UE not requiring measurement gap, in which case no measurement gap pattern should be sent for the parameters specified in Table A.5.2.3.1-1.

Table A.5.2.3.1 -1: General test parameters for E-UTRAN FDD-GSM handover

Table A. A.5.2.3.1 - 2: Cell Specific Parameters for Handover from E- UTRAN FDD to GSM cell case (cell 1)

Table A.5.2.3.1 - 3: Cell Specific Parameters for Handover from E-UTRAN FDD to GSM cell case (cell 2)

## A.5.2.3.2Test Requirements

The UE shall begin to send access bursts on the new DCCH of the target cell less than 100 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

THandover delay = 90 ms (Table 5.3.3.2.1-1) + Toffset + TUL

Toffset :Equal to 4.65 ms, GSM timing uncertainty between the time from when the UE is ready to transmit until the start of the next timeslot in GSM 26 multiframe structure

TUL:Equal to 4.65 ms, the time the UE has to wait in case the next timeslot is an idle frame or a SACCH frame.

This gives a total of 99.3 ms, allow 100 ms in the test case.

## A.5.2.4E-UTRAN TDD - UTRAN TDD Handover

## A.5.2.4.1Test Purpose and Environment

## A.5.2.4.1.1Void

## A.5.2.4.1.21.28 Mcps TDD option

This test is to verify the requirement for E-UTRAN TDD to UTRAN TDD handover requirements specified in clause 5.3.2.

The test scenario comprises of 1 E-UTRA TDD cell and 1 UTRA TDD cell as given in tables Table A.5.2.4.1.2-1, Table A.5.2.4.1.2-2, and Table A.5.2.4.1.2-3. Gap pattern configuration #0 as defined in table 8.1.2.1-1 is provided.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

E-UTRAN shall send a RRC message implying handover to UE. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The end of the last TTI containing handover message is begin of T3 duration.

Table A.5.2.4.1.2-1: General test parameters for E-UTRA TDD to UTRA(1.28 Mcps TDD OPTION) handover test case

Table A.5.2.4.1.2-2: Cell specific test parameters for E-UTRA TDD to UTRA TDD handover test case (cell 1)

Table A.5.2.4.1.2-3: Cell specific test parameters for cell search E-UTRA to UTRA case (cell 2)

## A.5.2.4.1.3Void

## A.5.2.4.2Test Requirements

## A.5.2.4.2.1Void

## A.5.2.4.2.21.28 Mcps TDD option

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 120 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.2.2.1.

Tinterrupt is defined in clause 5.3.2.2.2. Tinterrupt = 70 ms in the test as following:

Tinterrupt1= Toffset+TUL+30*FSFN+20 ms

Toffset = 10 ms; TUL = 10 ms; and FSFN = 1 for UE decoding SFN.

This gives a total of 120 ms.

## A.5.2.4.2.3Void

## A.5.2.5E-UTRAN FDD – UTRAN TDD Handover

## A.5.2.5.1Test Purpose and Environment

A.5.2.5.1.1Void

A.5.2.5.1.21.28 Mcps TDD option

This test is to verify the requirement for the E-UTRAN FDD to UTRAN TDD handover requirements specified in clause 5.3.2.

The test scenario comprises of two cells, E-UTRA TDD cell1 and UTRA TDD cell2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #1 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring. The test parameters are given in Tables A.5.2.5.1-1, A.5.2.5.1-2 and A.5.2.5.1-3.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.2.5.1.2-1: General test parameters for E-UTRA FDD to UTRA (1.28 Mcps TDD option) handover test case

Table A.5.2.5.1.2-2: Cell specific test parameters for E-UTRAN FDD to UTRAN (1.28 Mcps TDD option) handover test case (cell 1)

Table A.5.2.5.1.2-3: Cell specific test parameters for E-UTRAN FDD to UTRAN (1.28 Mcps TDD option) handover test case (cell 2)

## A.5.2.5.1.3Void

## A.5.2.5.2Test Requirements

## A.5.2.5.2.1Void

## A.5.2.5.2.21.28 Mcps TDD option

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 120 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.2.2.1.

Tinterrupt is defined in clause 5.3.2.2.2. Tinterrupt = 70 ms in the test as following:

Tinterrupt1= Toffset+TUL+30*FSFN+20 ms

Toffset = 10 ms; TUL = 10 ms; and FSFN = 1 for UE decoding SFN.

This gives a total of 120 ms.

## A.5.2.5.2.3Void

## A.5.2.6E-UTRAN TDD - GSM Handover

## A.5.2.6.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to GSM cell handover delay specified in clause 5.3.3.

The test parameters are given in Table A.5.2.6.1-1, A.5.2.6.1-2 and A.5.2.6.1-3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event B1 shall be used. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

The RRC message implying handover to cell 2 shall be sent to the UE during period T2, after the UE has reported Event B1. The start of T3 is defined as the end of last E-UTRAN TTI containing the RRC message implying handover.

The requirements are also applicable for a UE not requiring measurement gap, in which case no measurement gap pattern should be sent for the parameters specified in Table A.5.2.6.1-1.

Table A.5.2.6.1-1: General test parameters for E-UTRAN TDD toGSM neighbours handover test case in AWGN propagation condition

Table A.5.2.6.1-2: Cell Specific Parameters for Handover E- UTRAN TDD to GSM handover test case

Table A.5.2.6.1-3: Cell Specific Parameters for Handover E-UTRAN to GSM cell case (cell 2)

## A.5.2.6.2Test Requirements

The UE shall begin to send access bursts on the new DCCH of the target cell less than 100 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

THandover delay = 90 ms (Table 5.3.3.2.1-1) + Toffset + TUL

Toffset:Equal to 4.65 ms, GSM timing uncertainty between the time from when the UE is ready to transmit until the start of the next timeslot in GSM 26 multiframe structure

TUL:Equal to 4.65 ms, the time the UE has to wait in case the next timeslot is an idle frame or a SACCH frame.

This gives a total of 99.3 ms, allow 100 ms in the test case.

## A.5.2.7E-UTRAN FDD – UTRAN FDD Handover; Unknown Target Cell

## A.5.2.7.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to UTRAN FDD handover requirements for the case when the target cell is unknown as specified in clause 5.3.1.

The test parameters are given in Tables A.5.2.7.1-1, A.5.2.7.1-2 and A.5.2.7.1-3. The test consists of two successive time periods, with time durations of T1, T2. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. No Gap pattern configuration shall be used.

Table A.5.2.7.1-1: General test parameters for E-UTRAN FDD to UTRAN FDD handover test case

Table A.5.2.7.1-2: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 1)

Table A.5.2.7.1-3: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 2)

## A.5.2.7.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 290 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay is 50ms. See clause 5.3.1.1.1.

Tinterrupt is 240ms. See clause 5.3.1.1.2.

This gives a total of 290ms in the test case.

## A.5.2.8E-UTRAN FDD - GSM Handover; Unknown Target Cell

## A.5.2.8.1Test Purpose and Environment

This test is to verify the E-UTRAN FDD to GSM handover requirements for the case when the target GSM cell is unknown as specified in clause 5.3.3.

The test parameters are given in Table A.5.2.8.1-1, A.5.2.8.1-2 and A.5.2.8.1-3 below. The test consists of two successive time periods, with time duration of T1, T2 respectively. At the start of time duration T1, the UE will not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. No Gap pattern configuration shall be used.

Table A.5.2.8.1-1: General test parameters for E-UTRAN FDD to GSM handover test case; unknown target cell

Table A.5.2.8.1 - 2: Cell specific parameters for cell # 1 in E-UTRAN FDD to GSM handover test case; unknown target cell

Table A.5.2.8.1-3: Cell specific parameters for cell # 2 in E-UTRAN FDD to GSM handover test case; unknown target cell

## A.5.2.8.2Test Requirements

The UE shall begin to send access bursts on the new DCCH of the target cell less than 200 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

THandover delay = 190 ms (Table 5.3.3.2.1-1) + Toffset + TUL

Toffset:Equal to 4.65 ms is the GSM timing uncertainty from the time when the UE is ready to transmit until the start of the next timeslot in GSM 26 multiframe structure

TUL:Equal to 4.65 ms is the time the UE has to wait in case the next timeslot is an idle frame or a SACCH frame.

This gives a total of 199.3 ms, allow 200 ms in the test case.

## A.5.2.9E-UTRAN TDD - GSM Handover; Unknown Target Cell

## A.5.2.9.1Test Purpose and Environment

This test is to verify the E-UTRAN TDD to GSM handover requirements for the case when the target GSM cell is unknown as specified in clause 5.3.3.

The test parameters are given in Table A.5.2.9.1 -1, A.5.2.9.1 -2 and A.5.2.9.1 -3 below. The test consists of two successive time periods, with time duration of T1, T2 respectively. At the start of time duration T1, the UE will not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. No Gap pattern configuration shall be used.

Table A.5.2.9.1-1: General test parameters for E-UTRAN TDD to GSM handover test case; unknown target cell

Table A.5.2.9.1 - 2: Cell specific parameters for cell # 1 in E-UTRAN TDD to GSM handover test case; unknown target cell

Table A.5.2.9.1 - 3: Cell specific parameters for cell # 2 in E-UTRAN TDD to GSM handover test case; unknown target cell

## A.5.2.9.2Test Requirements

The UE shall begin to send access bursts on the new DCCH of the target cell less than 200 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

THandover delay = 190 ms (Table 5.3.3.2.1-1) + Toffset + TUL

Toffset:Equal to 4.65 ms is the GSM timing uncertainty from the time when the UE is ready to transmit until the start of the next timeslot in GSM 26 multiframe structure

TUL:Equal to 4.65 ms is the time the UE has to wait in case the next timeslot is an idle frame or a SACCH frame.

This gives a total of 199.3 ms, allow 200 ms in the test case.

## A.5.2.10E-UTRAN TDD to UTRAN TDD handover: unknown target cell

## A.5.2.10.1Test Purpose and Environment

This test is to verify the requirement for E-UTRAN TDD to UTRAN TDD handover requirements specified in clause 5.3.2 when the target UTRAN TDD cell is unknown.

The test scenario comprises of 1 E-UTRAN TDD cell and 1 UTRAN TDD cell as given in tables A.5.2.10.1-1, A.5.2.10.1-2, and A.5.2.10.1-3. No gap pattern is configured in the test case.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. During time duration T1, a RRC message implying handover to UTRA 1.28Mcps TDD cell shall be sent to the UE. The end of the last TTI containing handover message is the beginning of T2 duration.

Table A.5.2.10.1-1: General test parameters for E-UTRAN TDD to unknown UTRAN TDD cell handover test case

Table A.5.2.10.1-2: Cell specific test parameters for E-UTRAN TDD to unknown UTRAN TDD cell handover test case (cell 1)

Table A.5.2.10.1-3: Cell specific test parameters for E-UTRAN TDD to unknown UTRAN TDD cell test case (cell 2)

## A.5.2.10.2Test Requirements

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 280 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.2.2.1.

Tinterrupt is defined in clause 5.3.2.2.2. Tinterrupt = 230 ms in the test as following:

Tinterrupt1= Toffset+TUL+30*FSFN+180 ms

Toffset = 10 ms; TUL = 10 ms; and FSFN = 1 for UE decoding SFN.

This gives a total of 280 ms.

## A.5.2.10AE-UTRAN FDD – UTRAN FDD Multicarrier Handover with two target cells

## A.5.2.10A.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to UTRAN FDD handover requirements specified in clause 5.3.1 in a 2 cell multicarrier configuration. It is applicable to UEs that support DC-HSDPA, DB-DC-HSDPA and which do not support 3C-HSDPA or 4C-HSDPA.

The test parameters are given in Tables A.5.2.10A.1-1, A.5.2.10A.1-2 and A.5.2.10A.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 and cell 3 become detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover to cell 2 and cell 3 shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target Primary Serving HS-DSCH cell and cell 3 as the target Secondary Serving HS-DSCH cell.

Table A.5.2.10A.1-1: General test parameters for E-UTRAN FDD to UTRAN FDD handover test case

Table A.5.2.10A.1-2: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 1)

Table A.5.2.10A.1-3: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD multi carrier handover test case (cell 2 and cell 3)

## A.5.2.10A.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 210 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.1.1.1.

Tinterrupt = 160 ms in the test; Tinterrupt is defined in clause 5.3.1.1.2.

This gives a total of 210 ms.

## A.5.2.10BE-UTRAN TDD – UTRAN FDD Multicarrier Handover with two target cells

## A.5.2.10B.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD to UTRAN FDD handover requirements specified in clause 5.3.1 in a 2 cell multicarrier configuration. It is applicable to UEs that support DC-HSDPA, DB-DC-HSDPA and which do not support 3C-HSDPA or 4C-HSDPA.

The test parameters are given in Tables A.5.2.10B.1-1, A.5.2.10B.1-2 and A.5.2.10B.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 and cell 3 become detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover to cell 2 and cell 3 shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target Primary Serving HS-DSCH cell and cell 3 as the target Secondary Serving HS-DSCH cell.

Table A.5.2.10B.1-1: General test parameters for E-UTRAN TDD to UTRAN FDD handover test case

Table A.5.2.10B.1-2: Cell specific test parameters for E-UTRAN TDD to UTRAN FDD handover test case (cell 1)

Table A.5.2.10B.1-3: Cell specific test parameters for E-UTRAN TDD to UTRAN FDD multi carrier handover test case (cell 2 and cell 3)

## A.5.2.10B.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 210 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.1.1.1.

Tinterrupt = 160 ms in the test; Tinterrupt is defined in clause 5.3.1.1.2.

This gives a total of 210 ms.

## A.5.2.11E-UTRAN FDD – UTRAN FDD Handover for 5MHz Bandwidth

## A.5.2.11.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.5.2.1.1.

The parameters of this test are the same as defined in Subclause A.5.2.1.1 except that the values of the parameters in the Table A.5.2.11.1-1 will replace the values of the corresponding parameters in A.5.2.1.1-1, and the values of the parameters in the Table A.5.2.11.1-2 will replace the values of the corresponding parameters in A.5.2.1.1-2.

Table A.5.2.11.1-1: General test parameters for E-UTRAN FDD to UTRAN FDD handover test case for 5MHz bandwidth

Table A.5.2.11.1-2: Cell specific test parameters for E-UTRAN FDD to UTRAN FDD handover test case (cell 1)

## A.5.2.11.2Test Requirements

The test requirements defined in section A.5.2.1.2 shall apply to this test case.

## A.5.3E-UTRAN Handover to Non-3GPP RATs

## A.5.3.1E-UTRAN FDD – HRPD Handover

## A.5.3.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to HRPD handover requirements specified in clause 5.4.1.

The test parameters are given in Tables A.5.3.1.1-1, A.5.3.1.1-2 and A.5.3.1.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.1.1-1: General test parameters for E-UTRAN FDD to HRPD handover test case

Table A.5.3.1.1-2: Cell specific test parameters for E-UTRAN FDD cell#1 for handover to HRPD cell # 2

Table A.5.3.1.1-3: Cell specific test parameters for HRPD (cell # 2) for handover from E-UTRAN FDD cell (cell #1)

## A.5.3.1.2Test Requirements

The UE shall start transmission of the reverse control channel in HRPD to Cell 2 less than 127 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.4.1.1.1.

Tinterrupt = 76.66 ms in the test; Tinterrupt is defined in clause 5.4.1.1.2.

This gives a total of 126.66 ms, allow 127 ms in the test.

## A.5.3.2E-UTRAN FDD – cdma2000 1X Handover

## A.5.3.2.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to cdma2000 1X handover requirements specified in clause 5.4.2.

The test parameters are given in Tables A.5.3.2.1-1, A.5.3.2.1-2 and A.5.3.2.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.2.1-1: General test parameters for E-UTRAN FDD to cdma2000 1X handover test case

Table A.5.3.2.1-2: Cell specific test parameters for E-UTRAN FDD cell#1 for handover to cdma2000 1X cell # 2

Table A.5.3.2.1-3: Cell specific test parameters for cdma2000 1X (cell # 2) for handover from E-UTRAN FDD cell (cell #1)

## A.5.3.2.2Test Requirements

The UE shall start transmission of the reverse control channel in cdma2000 1X to Cell 2 less than 300 ms from the beginning of time period T3.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 130 ms, which is specified in clause 5.4.2.1.1.

Tinterrupt = 170 ms in the test; Tinterrupt is defined in clause 5.4.2.1.2.

This gives a total of 300 ms.

## A.5.3.3E-UTRAN FDD – HRPD Handover; Unknown Target Cell

## A.5.3.3.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to HRPD handover requirements for the case when the target HRPD cell is unknown as specified in clause 5.4.1.

The test parameters are given in Tables A.5.3.3.1-1, A.5.3.3.1-2 and A.5.3.3.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2.  During time period T1, message containing Information Element systemTimeInfo as defined in clause 6.3.1 of TS 36.331 [2] shall be sent by the System Simulator (SS).  No gap patterns are configured in the test case. No HRPD neighbour cell list shall be provided to the UE.

A RRC message implying handover to the unknown HRPD cell shall be sent to the UE towards the end of the time period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.3.1-1: General test parameters for E-UTRAN FDD to HRPD handover test case; unknown target HRPD cell

Table A.5.3.3.1-2: Cell specific test parameters for E-UTRAN FDD cell#1 for handover to unknown HRPD cell # 2

Table A.5.3.3.1-3: Cell specific test parameters for unknown HRPD (cell # 2) for handover from E-UTRAN FDD cell (cell #1)

## A.5.3.3.2Test Requirements

The UE shall start transmission of the reverse control channel in HRPD to Cell 2 less than 127 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt also includes time to detect HRPD cell; see clause 5.4.1.1.2

This gives a total of 126.66 ms, allow 127 ms in the test case.

## A.5.3.4E-UTRAN FDD – cdma2000 1X Handover; Unknown Target cell

## A.5.3.4.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN FDD to cdma2000 1X handover requirements for the case when the target cdma2000 1X cell is unknown as specified in clause 5.4.2.

The test parameters are given in Tables A.5.3.4.1-1, A.5.3.4.1-2 and A.5.3.4.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. During time period T1, message containing Information Element systemTimeInfo as defined in clause 6.3.1 of TS 36.331 [2] shall be sent by the System Simulator (SS). No gap patterns are configured in the test case. No cdma2000 1X neighbour cell list shall be provided to the UE.

A RRC message implying handover to the unknown cdma2000 1X cell shall be sent to the UE towards the end of the time period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.2.1-1: General test parameters for E-UTRAN FDD to cdma2000 1X handover test case; unknown target cdma2000 1X cell

Table A.5.3.2.1-2: Cell specific test parameters for E-UTRAN FDD cell#1 for handover to unknown cdma2000 1X cell # 2

Table A.5.3.2.1-3: Cell specific test parameters for unknown cdma2000 1X (cell # 2) for handover from E-UTRAN FDD cell (cell #1)

## A.5.3.4.2Test Requirements

The UE shall start transmission of the reverse control channel in cdma2000 1X to Cell 2 less than 300 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt also includes time to detect cdma2000 1X cell; see clause 5.4.2.1.2

This gives a total of 300 ms.

## A.5.3.5E-UTRAN TDD – HRPD Handover

## A.5.3.5.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD to HRPD handover requirements specified in clause 5.4.1.

The test parameters are given in Tables A.5.3.5.1-1, A.5.3.5.1-2 and A.5.3.5.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.5.1-1: General test parameters for E-UTRAN TDD to HRPD handover test case

Table A.5.3.5.1-2: Cell specific test parameters for E-UTRAN TDD cell#1 for handover to HRPD cell # 2

Table A.5.3.5.1-3: Cell specific test parameters for HRPD (cell # 2) for handover from E-UTRAN TDD cell (cell #1)

## A.5.3.5.2Test Requirements

The UE shall start transmission of the reverse control channel in HRPD to Cell 2 less than 127 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.4.1.1.1.

Tinterrupt = 76.66 ms in the test; Tinterrupt is defined in clause 5.4.1.1.2.

This gives a total of 126.66 ms, allow 127 ms in the test.

## A.5.3.6E-UTRAN TDD – cdma2000 1X Handover

## A.5.3.6.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN TDD to cdma2000 1X handover requirements specified in clause 5.4.2.

The test parameters are given in Tables A.5.3.6.1-1, A.5.3.6.1-2 and A.5.3.6.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in Table 8.1.2.1-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain cell 2 as the target cell.

Table A.5.3.6.1-1: General test parameters for E-UTRAN TDD to cdma2000 1X handover test case

Table A.5.3.6.1-2: Cell specific test parameters for E-UTRAN TDD cell#1 for handover to cdma2000 1X cell # 2

Table A.5.3.6.1-3: Cell specific test parameters for cdma2000 1X (cell # 2) for handover from E-UTRAN TDD cell (cell #1)

## A.5.3.6.2Test Requirements

The UE shall start transmission of the reverse control channel in cdma2000 1X to Cell 2 less than 300 ms from the beginning of time period T3.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 130 ms, which is specified in clause 5.4.2.1.1.

Tinterrupt = 170 ms in the test; Tinterrupt is defined in clause 5.4.2.1.2.

This gives a total of 300 ms.

## A.6RRC Connection Control

## A.6.1RRC Re-establishment

## A.6.1.1E-UTRAN FDD Intra-frequency RRC Re-establishment

## A.6.1.1.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.1.1-1 and table A.6.1.1.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.1.1-1: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

Table A.6.1.1.1-2: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

## A.6.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 1

Tsearch = 100 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1445 ms, allow 1.5 s in the test case.

## A.6.1.2E-UTRAN FDD Inter-frequency RRC Re-establishment

## A.6.1.2.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.1.2-1 and table A.6.1.1.2-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.6.1.2.1-1: General test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

Table A.6.1.2.1-2: Cell specific test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

## A.6.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown E-UTRA FDD inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 2

Tsearch = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.6.1.3E-UTRAN TDD Intra-frequency RRC Re-establishment

## A.6.1.3.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.3.1-1 and table A.6.1.3.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.3.1-1: General test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

Table A.6.1.3.1-2: Cell specific test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

## A.6.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA TDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 1

Tsearch = 100 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1445 ms, allow 1.5 s in the test case.

## A.6.1.4E-UTRAN TDD Inter-frequency RRC Re-establishment

## A.6.1.4.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.4.1-1 and table A.6.1.4.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.6.1.4.1-1: General test parameters for E-UTRAN TDD inter-frequency RRC Re-establishment test case

Table A.6.1.4.1-2: Cell specific test parameters for E-UTRAN TDD inter-frequency RRC Re-establishment test case

## A.6.1.4.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown E-UTRA TDD inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 2

Tsearch = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.6.1.5E-UTRAN FDD Intra-frequency RRC Re-establishment for 5MHz bandwidth

## A.6.1.5.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.6.1.1.1.

The parameters of this test are the same as defined in Subclause A.6.1.1.1 except that the values of the parameters in the Table A.6.1.5.1-1 will replace the values of the corresponding parameters in A.6.1.1.1-1, and the values of the parameters in the Table A.6.1.5.1-2 will replace the values of the corresponding parameters in A.6.1.1.1-2.

Table A.6.1.5.1-1: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case for 5MHz bandwidth

Table A.6.1.5.1-2: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case for 5MHz bandwidth

## A.6.1.5.2Test Requirements

The test requirements defined in section A.6.1.1.2 shall apply to this test case.

## A.6.1.6E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for UE category 0

## A.6.1.6.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.6.1-1 and table A.6.1.6.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.6.1-1: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

Table A.6.1.6.1-2: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

## A.6.1.6.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 1

Tsearch = 100 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1445 ms, allow 1.5 s in the test case.

## A.6.1.7E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for UE category 0

## A.6.1.7.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.7.1-1 and table A.6.1.7.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.7.1-1: General test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

Table A.6.1.7.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

## A.6.1.7.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 1

Tsearch = 100 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1445 ms, allow 1.5 s in the test case.

## A.6.1.8E-UTRAN TDD Intra-frequency RRC Re-establishment for UE category 0

## A.6.1.8.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.1.2.

The test parameters are given in table A.6.1.8.1-1 and table A.6.1.8.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.8.1-1: General test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

Table A.6.1.8.1-2: Cell specific test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

## A.6.1.8.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA TDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI + TPRACH

Nfreq = 1

Tsearch = 100 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1445 ms, allow 1.5 s in the test case.

## A.6.1.9E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.9.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.9.1-1 and table A.6.1.9.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.9.1-1: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

Table A.6.1.9.1-2: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

## A.6.1.9.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1345 ms, allow 1.5 s in the test case.

## A.6.1.10E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.10.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.10.1-1 and table A.6.1.10.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.10.1-1: General test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

Table A.6.1.10.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

## A.6.1.10.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1345 ms, allow 1.5 s in the test case.

## A.6.1.11E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.11.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.11.1-1 and table A.6.1.11.1-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.11.1-1: General test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

Table A.6.1.11.1-2: Cell specific test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

## A.6.1.11.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA TDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1345 ms, allow 1.5 s in the test case.

## A.6.1.12E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.12.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.12.1-1 and table A.6.1.12.1-2 below. The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.12.1-1: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

Table A.6.1.12.1-2: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

## A.6.1.12.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T4, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6485 ms, allow 7 s in the test case.

## A.6.1.13E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.13.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.13.1-1 and table A.6.1.13.1-2 below. The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.13.1-1: General test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

Table A.6.1.13.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

## A.6.1.13.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T4, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6465 ms, allow 7 s in the test case.

## A.6.1.14E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.14.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.14.1-1 and table A.6.1.14.1-2 below. The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.14.1-1: General test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

Table A.6.1.14.1-2: Cell specific test parameters for E-UTRAN TDD intra-frequency RRC Re-establishment test case

## A.6.1.14.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA TDD intra frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6465 ms, allow 7s in the test case.

## A.6.1.15HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

## A.6.1.15.1Test Purpose and Environment

The purpose is to verify that the NB-IoT FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5.

The test parameters are given in table A.6.1.15.1-1 and table A.6.1.15.1-2 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.15.1-1: General test parameters for HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

Table A.6.1.15.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

Table A.6.1.15.1-3: eCell 1 and eCell2 specific test parameters for HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

## A.6.1.15.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT FDD intra frequency cell shall be less than 58 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 14800 ms

-TSI_NB-IoT = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

-TPRACH_NB-IoT = 1280 ms; it is the additional delay caused by the random access procedure.

## A.6.1.16HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

## A.6.1.16.1Test Purpose and Environment

The purpose is to verify that the NB-IoT FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5.

The test parameters are given in table A.6.1.16.1-1 and table A.6.1.16.1-2 below. nCell1 and nCell2 are NB-IoT cells on different frequency carriers. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be indicated with the carrier frequency of nCell 2 to ensure that the UE has the context of the carrier frequency of nCell 2.

Table A.6.1.16.1-1: General test parameters for HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

Table A.6.1.16.1-2: nCell 1, nCell 2 specific test parameters for HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

Table A.6.1.16.1-3: eCell 1 specific test parameters for HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

## A.6.1.16.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT FDD inter frequency cell shall be less than 12 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 2

-Tsearch_NB-IoT = 1400 ms

-TSI_NB-IoT = 8320 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

-TPRACH_NB-IoT = 80 ms; it is the additional delay caused by the random access procedure.

## A.6.1.17E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.17.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.17.1-1 and table A.6.1.17.2-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.6.1.17.1-1: General test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

Table A.6.1.17.1-2: Cell specific test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

## A.6.1.17.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 3.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 2

Tsearch = 1000 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 3345 ms, allow 3.5 s in the test case.

## A.6.1.18E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.18.1Test Purpose and Environment

The purpose is to verify that the E-UTRA HD-FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.18.1-1 and table A.6.1.18.2-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.6.1.18.1-1: General test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

Table A.6.1.18.1-2: Cell specific test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

## A.6.1.18.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 3.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 2

Tsearch = 1000 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 3345 ms, allow 3.5 s in the test case.

## A.6.1.19E-UTRAN TDD-TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.6.1.19.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test parameters are given in table A.6.1.19.1-1 and table A.6.1.19.2-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.6.1.19.1-1: General test parameters for E-UTRAN TDD inter-frequency RRC Re-establishment test case

Table A.6.1.19.1-2: Cell specific test parameters for E-UTRAN TDD inter-frequency RRC Re-establishment test case

## A.6.1.19.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 3.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 2

Tsearch = 1000 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 3345 ms, allow 3.5 s in the test case.

## A.6.1.20E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.20.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB, and UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.20.1-1: General test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

Table A.6.1.20.1-2: Cell specific test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

## A.6.1.20.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T4, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 2

Tsearch = 100 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6665 ms, allow 7 s in the test case.

## A.6.1.21E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.21.1Test Purpose and Environment

The purpose is to verify that the E-UTRA HD-FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB, and UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.21.1-1: General test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

Table A.6.1.21.1-2: Cell specific test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

## A.6.1.21.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T4, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 2

Tsearch = 100 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6665 ms, allow 7 s in the test case.

## A.6.1.22E-UTRAN TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB

## A.6.1.22.1Test Purpose and Environment

The purpose is to verify that the E-UTRA TDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7.2.

The test consists of 4 successive time periods, with time duration of T1, T2, T3 and T4 respectively. During T1, both cell 1 and cell 2 are in CEModeB, and UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T3, cell 1, which is the active cell, is deactivated. The time period T4 starts after the occurrence of the radio link failure.

Table A.6.1.22.1-1: General test parameters for E-UTRAN TDD inter-frequency RRC Re-establishment test case

Table A.6.1.22.1-2: Cell specific test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

## A.6.1.22.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T4, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA TDD inter frequency cell shall be less than 7 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeB + TPRACH

Nfreq = 2

Tsearch = 100 ms

TSI-EUTRA-M1-CEModeB = 6400 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN TDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 6665 ms, allow 7 s in the test case.

## A.6.1.23E-UTRAN TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

## A.6.1.23.1Test Purpose and Environment

The purpose is to verify that the NB-IoT TDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5.

The test parameters are given in table A.6.1.23.1-1 and table A.6.1.23.1-2 below. nCell1 and nCell2 are NB-IoT cells on different frequency carriers. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be indicated with the carrier frequency of nCell 2 to ensure that the UE has the context of the carrier frequency of nCell 2.

Table A.6.1.23.1-1: General test parameters for TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

Table A.6.1.23.1-2: nCell 1, nCell 2 specific test parameters for TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

Table A.6.1.23.1-3: eCell 1 specific test parameters for TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage

## A.6.1.23.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT TDD inter frequency cell shall be less than 12 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TRACH_NB-IoT

-NNB-Iot-freq = 2

-Tsearch_NB-IoT = 1400 ms

-TSI_NB-IoT = 8320 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 [2] for the target NB-IoT TDD cell.

-TPRACH_NB-IoT = 80 ms; it is the additional delay caused by the random access procedure.

## A.6.1.24E-UTRAN TDD - TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

## A.6.1.24.1Test Purpose and Environment

The purpose is to verify that the NB-IoT TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5.

The test parameters are given in table A.6.1.24.1-1 and table A.6.1.24.1-2 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.1.24.1-1: General test parameters for TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

Table A.6.1.24.1-2: nCell 1, nCell 2 specific test parameters for TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

Table A.6.1.24.1-3: eCell 1 and eCell2 specific test parameters for TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage

## A.6.1.24.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT TDD intra frequency cell shall be less than 60 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 14800 ms

-TSI_NB-IoT = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT TDD cell.

-TPRACH_NB-IoT = 2560 ms; it is the additional delay caused by the random access procedure.

## A.6.2Random Access

## A.6.2.1E-UTRAN FDD – Contention Based Random Access Test

## A.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.1.1-1 and A.6.2.1.1-2.

Table A.6.2.1.1-1: General test parameters for FDD contention based random access test

Table A.6.2.1.1-2: RACH-Configuration parameters for FDD contention based random access test

## A.6.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.1.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.1.1 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.1.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.1.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3 the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.1.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.1.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.1.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.2E-UTRAN FDD – Non-Contention Based Random Access Test

## A.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.2.1-1 and A.6.2.2.1-2.

Table A.6.2.2.1-1: General test parameters for FDD non-contention based random access test

Table A.6.2.2.1-2: RACH-Configuration parameters for FDD non-contention based random access test

## A.6.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.2.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.2.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.3E-UTRAN TDD – Contention Based Random Access Test

## A.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.3.1-1 and A.6.2.3.1-2.

Table A.6.2.3.1-1: General test parameters for TDD contention based random access test

Table A.6.2.3.1-2: RACH-Configuration parameters for TDD contention based random access test

## A.6.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.3.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.1.1 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.3.2.2No Random Access Response reception

To test the UE behavior specified in Subclause 6.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.3.2.3Receiving a NACK on msg3

To test the UE behavior specified in Subclause 6.2.2.1.3 the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.3.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.3.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.3.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.4E-UTRAN TDD – Non-Contention Based Random Access Test

## A.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.4.1-1 and A.6.2.4.1-2.

Table A.6.2.4.1-1: General test parameters for TDD non-contention based random access test

Table A.6.2.4.1-2: RACH-Configuration parameters for TDD non-contention based random access test

## A.6.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.4.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.4.2.2No Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.5E-UTRAN FDD – Contention Based Random Access Test for 5MHz bandwidth

## A.6.2.5.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.6.2.1.1.

The parameters of this test are the same as defined in Subclause A.6.2.1.1 except that the values of the parameters in the Table A.6.2.5.1-1 will replace the values of the corresponding parameters in A.6.2.1.1-1

Table A.6.2.5.1-1: General test parameters for FDD contention based random access test for 5MHz bandwidth

## A.6.2.5.2Test Requirements

The test requirements defined in section A.6.2.1.2 shall apply to this test case.

## A.6.2.6E-UTRAN FDD – Non-contention Based Random Access Test for 5MHz bandwidth

## A.6.2.6.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.6.2.2.1.

The parameters of this test are the same as defined in Subclause A.6.2.2.1except that the values of the parameters in the Table A.6.2.6.1-1will replace the values of the corresponding parameters in A.6.2.2.1-1

Table A.6.2.6.1-1: General test parameters for FDD non-contention based random access test for 5MHz bandwidth

## A.6.2.6.2Test Requirements

The test requirements defined in section A.6.2.2.2 shall apply to this test case.

## A.6.2.7E-UTRAN FDD – Non-Contention Based Random Access Test For SCell

## A.6.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure, for the SCell, is according to the requirements and that the PRACH power settings and timing, for the SCell, are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell and SCell are different timing advance group. Cell 1 is in the primary Timing Advance Group (pTAG) and Cell 2 is in the secondary Timing Advance Group (sTAG). The purpose of the PCell is to allow the SCell to be configured and to handle the Random Access Response which takes place on PCell. The test parameters are given in tables A.6.2.7.1-1 and A.6.2.7.1-2.

Table A.6.2.7.1-1: General test parameters for FDD non-contention based random access test

Table A.6.2.7.1-2: RACH-Configuration parameters for FDD non-contention based random access test

## A.6.2.7.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.7.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit, on Cell 1, the PCell, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on Cell 2. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.7.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.2.2 the System Simulator shall transmit, on Cell 1, the PCell, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator on Cell 2. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.7.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached

To test the UE behavior specified in Subclause 6.2.2 the System Simulator shall transmit, in response to the first 6 preambles, a Random Access Response not corresponding to the transmitted Random Access Preamble on Cell 1, the PCell. The UE shall stop transmitting preambles after 6 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.8E-UTRAN TDD – Non-Contention Based Random Access Test For SCell

## A.6.2.8.1Test Purpose and Environment

This test is applicable for UE supporting the optional capability of Multiple Timing Advance.

The purpose of this test is to verify that the behavior of the random access procedure, for the SCell, is according to the requirements and that the PRACH power settings and timing, for the SCell, are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell and SCell are different timing advance group. Cell 1 is in the primary Timing Advance Group (pTAG) and Cell 2 is in the secondary Timing Advance Group (sTAG). The purpose of the PCell is to allow the SCell to be configured and to handle the Random Access Response which takes place on PCell. The test parameters are given in tables A.6.2.8.1-1 and A.6.2.8.1-2.

Table A.6.2.8.1-1: General test parameters for TDD non-contention based random access test

Table A.6.2.8.1-2: RACH-Configuration parameters for TDD non-contention based random access test

## A.6.2.8.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.8.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit, on Cell 1, the PCell, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on Cell 2. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.8.2.2No Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2.2.2 the System Simulator shall transmit, on Cell 1, the PCell, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on Cell 2. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.8.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached

To test the UE behavior specified in Subclause 6.2.2 the System Simulator shall transmit, in response to the first 6 preambles, a Random Access Response not corresponding to the transmitted Random Access Preamble on Cell 1, the PCell. The UE shall stop transmitting preambles after 6 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22  dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.93DL/3UL TDD CA Non-Contention Based Random Access Test for 2 SCells

## A.6.2.9.1Test Purpose and Environment

This test is applicable for UE supporting the optional capability of Multiple Timing Advance.

The purpose of this test is to verify that the behavior of the random access procedure, for the two SCells, is according to the requirements and that the PRACH power settings and timing, for the SCell, are within specified limits. This test will verify the requirements in Clause 6.2.2 and Clause 7.1.2 in an AWGN model.

For this test three cells are used. Cell 1 is PCell, Cell 2 is SCell1 and Cell 3 is SCell2. Cell 1 and Cell 2/Cell 3 belong to different timing advance groups. Cell 1 is in the primary Timing Advance Group (pTAG). Cell 2 and Cell3 are in the same secondary Timing Advance Group (sTAG). The purpose of the Cell 1 is to allow Cell 2 and Cell 3 to be configured and to handle the Random Access Response which takes place on Cell 1. The test parameters are given in tables A.6.2.9.1-1 and A.6.2.9.1-2.

Table A.6.2.9.1-1: General test parameters for 3DL/3UL TDD CA non-contention based random access test

Table A.6.2.9.1-2: RACH-Configuration parameters for cell2 and cell3 for 3DL/3UL TDD CA non-contention based random access test

## A.6.2.9.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.9.2.1Random Access Response Reception

A.6.2.9.2.1.1Test Requirements for Cell 2

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit, on cell 1 a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on cell 2. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 2 shall be within the accuracy specified in Subclause 7.1.2.

A.6.2.9.2.1.2Test Requirements for Cell 3

To test the UE behavior specified in Subclause 6.2.2.2.1 the System Simulator shall transmit, on cell 1 a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on cell 3. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-transmit the preamble with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 3 shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.9.2.2No Random Access Response Reception

A.6.2.9.2.2.1Test Requirements for Cell 2

To test the UE behavior specified in Subclause 6.2.2.2.2 the System Simulator shall transmit, on cell 1, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on cell 2. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power on cell 2.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 2 shall be within the accuracy specified in Subclause 7.1.2.

A.6.2.9.2.2.2Test Requirements for Cell 3

To test the UE behavior specified in Subclause 6.2.2.2.2 the System Simulator shall transmit, on cell 1, a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator, on cell 3. The System Simulator shall not respond to the first 4 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power on cell 3.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 3 shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.9.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached

A.6.2.9.2.3.1Test Requirements for Cell 2

To test the UE behavior specified in Subclause 6.2.2 the System Simulator shall transmit, in response to the first 6 preambles, a Random Access Response not corresponding to the transmitted Random Access Preamble on cell 1. The UE shall stop transmitting preambles after 6 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power on cell 2.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 2 shall be within the accuracy specified in Subclause 7.1.2.

A.6.2.9.2.3.2Test Requirements for Cell 3

To test the UE behavior specified in Subclause 6.2.2 the System Simulator shall transmit, in response to the first 6 preambles, a Random Access Response not corresponding to the transmitted Random Access Preamble on cell 1. The UE shall stop transmitting preambles after 6 preambles.

The UE shall re-transmit the preamble with the calculated PRACH transmission power on cell 3.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions on cell 3 shall be within the accuracy specified in Subclause 7.1.2.

## A.6.2.10E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage

## A.6.2.10.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Normal Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.2.2, Clause 6.2.3 and Clause 7.24.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.10.1-1 and A.6.2.10.1-2.

Table A.6.2.10.1-1: General test parameters for FDD contention based random access test

Table A.6.2.10.1-2: RACH-Configuration parameters for FDD contention based random access test

Table A.6.2.10.1-3: PRACH-Configuration parameters for FDD contention based random access test

## A.6.2.10.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.10.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.10.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.10.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.10.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.10.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.10.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.10.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 0.

Note: The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.11E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage

## A.6.2.11.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Normal Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.2.2, Clause 6.2.3 and Clause 7.24.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.11.1-1 and A.6.2.11.1-2.

Table A.6.2.11.1-1: General test parameters for HD-FDD contention based random access test

Table A.6.2.11.1-2: RACH-Configuration parameters for HD-FDD contention based random access test

Table A.6.2.11.1-3: PRACH-Configuration parameters for HD-FDD contention based random access test

## A.6.2.11.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.11.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.11.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.11.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.11.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.11.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.11.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.11.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 0.

Note: The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.12E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage

## A.6.2.12.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Normal Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.2.2, Clause 6.2.3 and Clause 7.24.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.12.1-1 and A.6.2.12.1-2.

Table A.6.2.12.1-1: General test parameters for TDD contention based random access test

Table A.6.2.12.1-2: RACH-Configuration parameters for TDD contention based random access test

Table A.6.2.12.1-3: PRACH-Configuration parameters for TDD contention based random access test

## A.6.2.12.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.12.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.12.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -30 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.12.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.12.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.12.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.12.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.12.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 0.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.13E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage

## A.6.2.13.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Enhanced Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 7.24.2, Clause 6.2.3 and Clause 7.1.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.13.1-1 and A.6.2.13.1-2.

Table A.6.2.13.1-1: General test parameters for FDD contention based random access test

Table A.6.2.13.1-2: RACH-Configuration parameters for FDD contention based random access test

Table A.6.2.13.1-3: PRACH-Configuration parameters for FDD contention based random access test

## A.6.2.13.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.13.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause7.24.2.

## A.6.2.13.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.13.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.13.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.13.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.13.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.13.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 2.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.14E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage

## A.6.2.14.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Enhanced Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.2.2, Clause 6.2.3 and Clause 7.24.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.14.1-1 and A.6.2.14.1-2.

Table A.6.2.14.1-1: General test parameters for HD-FDD contention based random access test

Table A.6.2.14.1-2: RACH-Configuration parameters for HD-FDD contention based random access test

Table A.6.2.14.1-3: PRACH-Configuration parameters for HD-FDD contention based random access test

## A.6.2.14.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.14.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.14.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.14.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.14.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.14.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.14.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.14.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 2.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.15E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage

## A.6.2.15.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Enhanced Coverage is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.2.2, Clause 6.2.3 and Clause 7.24.2 in an AWGN model.

For this test a single cell is used. The test parameters are given in tables A.6.2.15.1-1 and A.6.2.15.1-2.

Table A.6.2.15.1-1: General test parameters for TDD contention based random access test

Table A.6.2.15.1-2: RACH-Configuration parameters for TDD contention based random access test

Table A.6.2.15.1-3: PRACH-Configuration parameters for TDD contention based random access test

## A.6.2.15.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.15.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.15.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.101 [5].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24.2.

## A.6.2.15.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

## A.6.2.15.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.15.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.15.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.15.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 2.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.6.2.16Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage

## A.6.2.16.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Normal Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.16.1-1, A.6.2.16.1-2 and A.6.2.16.1-4.

Table A.6.2.16.1-1: nCell specific test parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

Table A.6.2.16.1-2: eCell specific test parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

Table A.6.2.16.1-3: Void

Table A.6.2.16.1-4: NPRACH-Configuration parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

## A.6.2.16.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.16.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 2 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be -25  dBm with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5F.2 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.16.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 2 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5F.2 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.16.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.16.1-4 is reached.

## A.6.2.16.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.16.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.16.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.16.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 0. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.6.2.17Contention Based Random Access Test for UE category NB1 UEs In-band mode in Enhanced Coverage

## A.6.2.17.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.17.1-1, A.6.2.17.1-2 and A.6.2.17.1-4.

Table A.6.2.17.1-1: nCell specific test parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.17.1-2: eCell specific test parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.17.1-3: Void

Table A.6.2.17.1-4: NPRACH-Configuration parameters for HD-FDD contention based random access test for UE category NB1 In-Band mode in Enhanced Coverage

## A.6.2.17.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.17.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.17.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.17.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.17.1-4 is reached.

## A.6.2.17.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.17.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.17.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.17.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level Sselection requirement is a prerequisite already assumed for testing the other NPRACH requirements.

## A.6.2.18Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage

## A.6.2.18.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.18.1-1, A.6.2.18.1-2 and A.6.2.18.1-3.

Table A.6.2.18.1-1: nCell specific test parameters for HD-FDD contention based random access on non-achor carrier test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.18.1-2: eCell specific test parameters for HD-FDD contention based random access on non-achor carrier test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.18.1-3: NPRACH-Configuration parameters for HD-FDD contention based random access on non-anchor carrier test for UE category NB1 In-Band mode in Enhanced Coverage

## A.6.2.18.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.18.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.18.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.18.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.18.1-3 is reached.

## A.6.2.18.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.18.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.18.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.18.2.7NPRACH Resource Selection

The UE shall select NPRACH resources in non-anchor carrier and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.6.2.19TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage

## A.6.2.19.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Normal Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.19.1-1, A.6.2.19.1-2 and A.6.2.19.1-3.

Table A.6.2.19.1-1: nCell specific test parameters for TDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

Table A.6.2.19.1-2: eCell specific test parameters for TDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

Table A.6.2.19.1-3: NPRACH-Configuration parameters for TDD contention based random access test for UE category NB1 In-Band mode in Normal Coverage

## A.6.2.19.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.19.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 2 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5F.2 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.19.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 2 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5F.2 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.19.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.19.1-3 is reached.

## A.6.2.19.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.19.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.19.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.19.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 0. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.6.2.20TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in enhanced coverage

## A.6.2.20.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.20.1-1, A.6.2.20.1-2 and A.6.2.20.1-3.

Table A.6.2.20.1-1: nCell specific test parameters for TDD contention based random access test for UE category NB1 In-Band mode in Enhanced coverage

Table A.6.2.20.1-2: eCell specific test parameters for TDD contention based random access test for UE category NB1 In-Band mode in Enhanced coverage

Table A.6.2.20.1-3: NPRACH-Configuration parameters for TDD contention based random access test for UE category NB1 In-Band mode in Enhanced coverage

## A.6.2.20.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.20.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 2 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5F.2 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.20.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.20.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.20.1-3 is reached.

## A.6.2.20.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.20.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.20.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.20.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level Sselection requirement is a prerequisite already assumed for testing the other NPRACH requirements.

## A.6.2.21TDD Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage

## A.6.2.21.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6.2, Clause 6.6.3 and Clause 7.20.2 in an AWGN model.

For this test a single NB-IoT cell and a single LTE cell are used. The test parameters are given in tables A.6.2.21.1-1, A.6.2.21.1-2 and A.6.2.21.1-3.

Table A.6.2.21.1-1: nCell specific test parameters for TDD contention based random access on non-anchor test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.21.1-2: eCell specific test parameters for TDD contention based random access on non-anchor test for UE category NB1 In-Band mode in Enhanced Coverage

Table A.6.2.21.1-3: NPRACH-Configuration parameters for TDD contention based random access on non-anchor test for UE category NB1 In-Band mode in Enhanced Coverage

## A.6.2.21.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.6.2.21.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.21.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 and 14 dBm for power class 6 with an accuracy specified in clause 6.3.5F.1.1 of TS 36.101 [5].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20.2.

## A.6.2.21.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.6.2.21.1-3 is reached.

## A.6.2.21.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.6.2.21.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.6.2.21.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.2.21.2.7NPRACH Resource Selection

The UE shall select NPRACH resources in non-anchor carrier and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.6.3RRC Connection Release with Redirection

## A.6.3.1Redirection from E-UTRAN FDD to UTRAN FDD

## A.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct performing the RRC connection release with redirection to the target UTRAN FDD cell. This test will partly verify the RRC connection release with redirection to UTRAN FDD cell requirements in clause 6.3.2.1.

The test parameters are given in Tables A.6.3.1.1-1, A.6.3.1.1-2 and A.6.3.1.1-3 below. The test consists of two successive time periods, with time duration of T1, and T2 respectively. The “RRCConnectionRelease” message containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.6.3.1.1-1: General test parameters for RRC Connection Release with Redirection from E-UTRAN FDD to UTRAN FDD under AWGN propagation conditions

Table A.6.3.1.1-2: Cell specific test parameters for cell #1 E-UTRAN FDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

Table A.6.3.1.1-3: Cell specific test parameters for cell #2 E-UTRAN FDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

## A.6.3.1.2Test Requirements

The UE shall start to transmit random access to Cell 2 less than 650 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRAN FDD observed during repeated tests shall be at least 90%.

NOTE:The Re-establishment delay in this case can be expressed as

Tconnection_release_redirect_UTRA FDD = TRRC_procedure_delay + Tidentify-UTRA FDD + TSI-UTRA FDD + TRA

where

TRRC_procedure_delay = 110 ms

Tidentify-UTRA FDD = 500 ms

TSI-UTRA FDD = the time required for acquiring all the relevant system information of the target UTRA FDD cell. This time depends upon whether the UE is provided with the relevant system information of the target UTRA FDD cell or not by the E-UTRAN before the RRC connection is released. 0 ms is assumed in this test case.

TRA = The additional delay caused by the random access procedure. 40 ms is assumed in this test case.

This gives a total of 650 ms.

## A.6.3.2Redirection from E-UTRAN TDD to UTRAN FDD

## A.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct performing the RRC connection release with redirection to the target UTRAN FDD cell. This test will partly verify the RRC connection release with redirection to UTRAN FDD cell requirements in clause 6.3.2.1.

The test parameters are given in Tables A.6.3.2.1-1, A.6.3.2.1-2 and A.6.3.2.1-3 below. The test consists of two successive time periods, with time duration of T1, and T2 respectively. The “RRCConnectionRelease” message containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of cell 2. Cell 2 is powered up at the beginning of the T2,

Table A.6.3.2.1-1: General test parameters for RRC Connection Release with Redirection from E-UTRAN TDD to UTRAN FDD under AWGN propagation conditions

Table A.6.3.2.1-2: Cell specific test parameters for cell #1 E-UTRAN TDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

Table A.6.3.2.1-3: Cell specific test parameters for cell #2 E-UTRAN TDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

## A.6.3.2.2Test Requirements

The UE shall start to transmit random access to Cell 2 less than 650 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRA FDD observed during repeated tests shall be at least 90%.

NOTE:The Re-establishment delay in this case can be expressed as

Tconnection_release_redirect_UTRA FDD = TRRC_procedure_delay + Tidentify-UTRA FDD + TSI-UTRA FDD + TRA

where

TRRC_procedure_delay = 110 ms

Tidentify-UTRA FDD = 500 ms

TSI-UTRA FDD = the time required for acquiring all the relevant system information of the target UTRA FDD cell. This time depends upon whether the UE is provided with the relevant system information of the target UTRA FDD cell or not by the E-UTRAN before the RRC connection is released. 0 ms is assumed in this test case.

TRA = The additional delay caused by the random access procedure. 40 ms is assumed in this test case.

This gives a total of 650 ms.

## A.6.3.3Redirection from E-UTRAN FDD to GERAN when System Information is provided

## A.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA FDD to the target GERAN cell within Tconnection_release_redirect_GERAN. This test will partly verify the RRC connection release with redirection to GERAN requirements in clause 6.3.2.2.

The test parameters are given in Tables A.6.3.3.1-1, A.6.3.3.1-2 and A.6.3.3.1-3 below. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall contain all the relevant system information of cell 2.

Table A.6.3.3.1-1: General test parameters for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

Table A.6.3.3.1-2: Cell specific test parameters for E-UTRA FDD cell (cell #1) for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

Table A.6.3.3.1-3: Cell specific test parameters for GERAN cell (cell #2) for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

## A.6.3.3.2Test Requirements

The UE shall begin to send access bursts on RACH of the target GERAN cell (cell #2) less than 1120 ms from the beginning of time period T2.

The rate of correct “RRC connection release with redirection to GERAN” observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

Tconnection_release_redirect_ GERAN = TRRC_procedure_delay + Tidentify-GERAN + TSI-GERAN + TRA

TRRC_procedure_delay = 110 ms, which is the time for processing the received message “RRCConnectionRelease.

Tidentify-GERAN = 1000 ms, which is the time for identifying the target GERAN cell.

TSI-GERAN = 0; UE does not have to read the system information of the GERAN cell since all relevant SI is provided to the UE in the “RRCConnectionRelease” message.

TRA = 10 ms, which is about 2 GSM frames (2*4.65 ms) to account for the GSM timing uncertainty.

## A.6.3.4Redirection from E-UTRAN TDD to GERAN when System Information is provided

## A.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA TDD to the target GERAN cell within Tconnection_release_redirect_GERAN. This test will partly verify the RRC connection release with redirection to GERAN requirements in clause 6.3.2.2.

The test parameters are given in Tables A.6.3.4.1-1, A.6.3.4.1-2 and A.6.3.4.1-3 below. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall contain all the relevant system information of cell 2.

Table A.6.3.4.1-1: General test parameters for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

Table A.6.3.4.1-2: Cell specific test parameters for E-UTRA TDD cell (cell #1) for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

Table A.6.3.4.1-3: Cell specific test parameters for GERAN cell (cell #2) for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

## A.6.3.4.2Test Requirements

The UE shall begin to send access bursts on RACH of the target GERAN cell (cell #2) less than 1120 ms from the beginning of time period T2.

The rate of correct “RRC connection release with redirection to GERAN” observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

Tconnection_release_redirect_ GERAN = TRRC_procedure_delay + Tidentify-GERAN + TSI-GERAN + TRA

TRRC_procedure_delay = 110 ms, which is the time for processing the received message “RRCConnectionRelease.

Tidentify-GERAN = 1000 ms, which is the time for identifying the target GERAN cell.

## A.6.3.5E-UTRA TDD RRC connection release redirection to UTRA TDD

## A.6.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA TDD to the target UTRA TDD cell within Tconnection_release_redirect_UTRA TDD. This test will partly verify the RRC connection release with redirection to UTRA TDD requirements in clause 6.3.2.3.

The test parameters are given in table A.6.3.5.1-1, table A.6.3.5.1-2, and table A.6.3.5.1-3. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The “RRCConnectionRelease” message containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall contain all the relevant system information of Cell 2.

Table A.6.3.5.1-1: General test parameters for E-UTRA TDD RRC connection release redirection to UTRA TDD

Table A.6.3.5.1-2: Cell specific test parameters for cell 1 in E-UTRA TDD RRC connection release redirection to UTRA TDD test

Table A.6.3.5.1-3: Cell specific test parameters for cell 2 in E-UTRA TDD RRC connection release redirection to UTRA TDD test

## A.6.3.5.2Test Requirements

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 650 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRA TDD observed during repeated tests shall be at least 90%.

NOTE:The time delay can be expressed as: TRRC_procedure_delay + Tidentify-UTRA TDD + TSI-UTRA TDD + TRA, where:

TRRC_procedure_delay = 110 ms, which is specified in clause 6.3.2.3.

Tidentify-UTRA TDD = 500 ms; which is defined in clause 6.3.2.3.

TSI-UTRA TDD = 0 ms, UE does not have to read the system information of the UTRAN TDD since all relevant SI is provided to the UE in the “RRCConnectionRelease” message.

TRA = 40ms. This is the additional delay caused by the random access procedure

It gives a total delay of 650 ms.

## A.6.3.6E-UTRA FDD RRC connection release redirection to UTRA TDD

## A.6.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA FDD to the target UTRA TDD cell within Tconnection_release_redirect_UTRA TDD. This test will partly verify the RRC connection release with redirection to UTRA TDD requirements in clause 6.3.2.3.

The test parameters are given in table A.6.3.6.1-1, table A.6.3.6.1-2, and table A.6.3.6.1-3. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The “RRCConnectionRelease” message containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall contain all the relevant system information of Cell 2.

Table A.6.3.6.1-1: General test parameters for E-UTRA FDD RRC connection release redirection to UTRA TDD

Table A.6.3.6.1-2: Cell specific test parameters for cell 1 in E-UTRA FDD RRC connection release redirection to UTRA TDD test

Table A.6.3.6.1-3: Cell specific test parameters for cell 2 in E-UTRA FDD RRC connection release redirection to UTRA TDD test

## A. 6.3.6.2Test Requirements

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 650 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRA TDD observed during repeated tests shall be at least 90%.

NOTE:The time delay can be expressed as: TRRC_procedure_delay + Tidentify-UTRA TDD + TSI-UTRA TDD + TRA, where:

TRRC_procedure_delay = 110 ms, which is specified in clause 6.3.2.3.

Tidentify-UTRA TDD = 500 ms; which is defined in clause 6.3.2.3.

TSI-UTRA TDD = 0 ms, UE does not have to read the system information of the UTRAN TDD since all relevant SI is provided to the UE in the “RRCConnectionRelease” message.

TRA = 40ms. This is the additional delay caused by the random access procedure.

This gives a total delay of 650 ms.

## A.6.3.7E-UTRA TDD RRC connection release redirection to UTRA TDD without SI provided

## A.6.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA TDD to the target UTRA TDD cell within Tconnection_release_redirect_UTRA TDD. This test will partly verify the RRC connection release with redirection to UTRA TDD requirements in clause 6.3.2.3.

The test parameters are given in table A.6.3.7.1-1, table A.6.3.7.1-2, and table A.6.3.7.1-3. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The “RRCConnectionRelease” message not containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from Cell 1.

Table A.6.3.7.1-1: General test parameters for E-UTRA TDD RRC connection release redirection to UTRA TDD without SI provided

Table A.6.3.7.1-2: Cell specific test parameters for cell 1 in E-UTRA TDD RRC connection release redirection to UTRA TDD test without SI provided

Table A.6.3.7.1-3: Cell specific test parameters for cell 2 in E-UTRA TDD RRC connection release redirection to UTRA TDD test without SI provided

## A.6.3.7.2Test Requirements

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 1930 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRA TDD observed during repeated tests shall be at least 90%.

NOTE:The time delay can be expressed as: TRRC_procedure_delay + Tidentify-UTRA TDD + TSI-UTRA TDD + TRA, where:

TRRC_procedure_delay = 110 ms, which is specified in clause 6.3.2.3.

Tidentify-UTRA TDD = 500 ms; which is defined in clause 6.3.2.3.

TSI-UTRA TDD:Maximum repetition period of relevant system info blocks that need to be received by the UE during RRC connection release redirection to UTRA TDD cell. 1280 ms is assumed in this test case.

TRA = 40ms, this is the additional delay caused by the random access procedure.

This gives a total delay of 1930 ms.

## A.6.3.8E-UTRA FDD RRC connection release redirection to UTRA TDD without SI provided

## A.6.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA FDD to the target UTRA TDD cell within Tconnection_release_redirect_UTRA TDD. This test will partly verify the RRC connection release with redirection to UTRA TDD requirements in clause 6.3.2.3.

The test parameters are given in table A.6.3.8.1-1, table A.6.3.8.1-2, and table A.6.3.8.1-3. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The “RRCConnectionRelease” message not containing the relevant system information of Cell 2 shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from Cell 1.

Table A.6.3.8.1-1: General test parameters for E-UTRA FDD RRC connection release redirection to UTRA TDD without SI provided

Table A.6.3.8.1-2: Cell specific test parameters for cell 1 in E-UTRA FDD RRC connection release redirection to UTRA TDD test without SI provided

Table A.6.3.8.1-3: Cell specific test parameters for cell 2 in E-UTRA FDD RRC connection release redirection to UTRA TDD test without SI provided

## A.6.3.8.2Test Requirements

The UE shall start to transmit the SYNCH-UL sequence in the UpPTS to Cell 2 less than 1930 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRA TDD observed during repeated tests shall be at least 90%.

NOTE:The time delay can be expressed as: TRRC_procedure_delay + Tidentify-UTRA TDD + TSI-UTRA TDD + TRA, where:

TRRC_procedure_delay = 110 ms, which is specified in clause 6.3.2.3.

Tidentify-UTRA TDD = 500 ms; which is defined in clause 6.3.2.3.

TSI-UTRA TDD:Maximum repetition period of relevant system info blocks that need to be received by the UE during RRC connection release redirection to UTRA TDD cell. 1280 ms is assumed in this test case.

TRA = 40ms, this is the additional delay caused by the random access procedure.

This gives a total delay of 1930 ms.

## A.6.3.9Redirection from E-UTRAN FDD to UTRAN FDD without System Information

## A.6.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct performing the RRC connection release with redirection to the target UTRAN FDD cell. This test will partly verify the RRC connection release with redirection to UTRAN FDD cell requirements in clause 6.3.2.1.

The test parameters are given in Tables A.6.3.9.1-1, A.6.3.9.1-2 and A.6.3.9.1-3 below. The test consists of two successive time periods, with time duration of T1, and T2 respectively. The “RRCConnectionRelease” message not containing any system information of Cell 2 shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.6.3.9.1-1: General test parameters for RRC Connection Release with Redirection from E-UTRAN FDD to UTRAN FDD under AWGN propagation conditions

Table A.6.3.9.1-2: Cell specific test parameters for cell #1 E-UTRAN FDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

Table A.6.3.9.1-3: Cell specific test parameters for cell #2 E-UTRAN FDD to UTRAN FDD RRC release with redirection under AWGN propagation conditions

## A.6.3.9.2Test Requirements

The UE shall start to send random access to the target UTRA FDD cell (Cell 2) less than 1930 ms from the beginning of time period T2.

The rate of correct “RRC connection release with redirection to UTRAN” observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this case can be expressed as

Tconnection_release_redirect_UTRA FDD = TRRC_procedure_delay + Tidentify-UTRA FDD + TSI-UTRA FDD + TRA

where

TRRC_procedure_delay = 110 ms

Tidentify-UTRA FDD = 500 ms

TSI-UTRA FDD = the time required for acquiring all the relevant system information of the target UTRA FDD cell. This time depends upon whether the UE is provided with the relevant system information of the target UTRA FDD cell or not by the E-UTRAN before the RRC connection is released. Since no SI is provided, 1280 ms is assumed in this test case.

TRA = The additional delay caused by the random access procedure. 40 ms is assumed in this test case.

This gives a total of 1930 ms.

## A.6.3.10Redirection from E-UTRAN FDD to GERAN when System Information is not provided

## A.6.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA FDD to the target GERAN cell within Tconnection_release_redirect_GERAN. This test will partly verify the RRC connection release with redirection to GERAN requirements in clause 6.3.2.2.

The test parameters are given in Tables A.6.3.10.1-1, A.6.3.10.1-2 and A.6.3.10.1-3 below. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall not contain any system information of cell 2.

Table A.6.3.10.1-1: General test parameters for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

Table A.6.3.10.1-2: Cell specific test parameters for E-UTRA FDD cell (cell #1) for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

Table A.6.3.10.1-3: Cell specific test parameters for GERAN cell (cell #2) for RRC connection release with redirection from E-UTRAN FDD to GERAN in AWGN

## A.6.3.10.2Test Requirements

The UE shall begin to send access bursts on RACH of the target GERAN cell (cell #2) less than 3020 ms from the beginning of time period T2.

The rate of correct “RRC connection release with redirection to GERAN” observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

Tconnection_release_redirect_ GERAN = TRRC_procedure_delay + Tidentify-GERAN + TSI-GERAN + TRA

TRRC_procedure_delay = 110 ms, which is the time for processing the received message “RRCConnectionRelease.

Tidentify-GERAN = 1000 ms, which is the time for identifying the target GERAN cell.

TSI-GERAN = 1900 ms, which is the maximum time allowed to read BCCH data from the target GERAN cell.

TRA = 10 ms, which is about 2 GSM frames (2*4.65 ms) to account for the GSM timing uncertainty.

## A.6.3.11Redirection from E-UTRAN TDD to GERAN when System Information is not provided

## A.6.3.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRA TDD to the target GERAN cell within Tconnection_release_redirect_GERAN. This test will partly verify the RRC connection release with redirection to GERAN requirements in clause 6.3.2.2.

The test parameters are given in Tables A.6.3.11.1-1, A.6.3.11.1-2 and A.6.3.11.1-3 below. No measurement gaps are configured. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from cell 1. The “RRCConnectionRelease” message shall not contain any system information of cell 2.

Table A.6.3.11.1-1: General test parameters for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

Table A.6.3.11.1-2: Cell specific test parameters for E-UTRA TDD cell (cell #1) for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

Table A.6.3.11.1-3: Cell specific test parameters for GERAN cell (cell #2) for RRC connection release with redirection from E-UTRAN TDD to GERAN in AWGN

## A.6.3.11.2Test Requirements

The UE shall begin to send access bursts on RACH of the target GERAN cell (cell #2) less than 3020 ms from the beginning of time period T2.

The rate of correct “RRC connection release with redirection to GERAN” observed during repeated tests shall be at least 90%.

NOTE:The test requirement in this test case is expressed as:

Tconnection_release_redirect_ GERAN = TRRC_procedure_delay + Tidentify-GERAN + TSI-GERAN + TRA

TRRC_procedure_delay = 110 ms, which is the time for processing the received message “RRCConnectionRelease.

Tidentify-GERAN = 1000 ms, which is the time for identifying the target GERAN cell.

TSI-GERAN = 1900 ms, which is the maximum time allowed to read BCCH data from the target GERAN cell.

TRA = 10 ms, which is about 2 GSM frames (2*4.65 ms) to account for the GSM timing uncertainty.

## A.6.3.12E-UTRAN TDD RRC connection release redirection to UTRAN FDD without SI provided

## A.6.3.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE performs the RRC connection release with redirection from the E-UTRAN TDD to the target UTRAN FDD cell within Tconnection_release_redirect_UTRAN FDD. This test will partly verify the RRC connection release with redirection to UTRAN FDD requirements in clause 6.3.2.1.

The test parameters are given in table A.6.3.12.1-1, table A.6.3.12.1-2, and table A.6.3.12.1-3. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. The “RRCConnectionRelease” message not containing any system information of Cell 2 shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message, “RRCConnectionRelease”, is received by the UE from Cell 1.

Table A.6.3.12.1-1: General test parameters for E-UTRAN TDD RRC connection release redirection to UTRAN FDD without SI provided

Table A.6.3.12.1-2: Cell specific test parameters for cell 1 in E-UTRAN TDD RRC connection release redirection to UTRAN FDD test without SI provided

Table A.6.3.12.1-3: Cell specific test parameters for cell 2 in E-UTRAN TDD RRC connection release redirection to UTRAN FDD test without SI provided

## A.6.3.12.2Test Requirements

The UE shall start to send random access to the target UTRAN FDD cell (Cell 2) less than 1930 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to UTRAN FDD observed during repeated tests shall be at least 90%.

NOTE:The time delay can be expressed as: TRRC_procedure_delay + Tidentify-UTRAN FDD + TSI-UTRAN FDD + TRA, where:

TRRC_procedure_delay = 110 ms, which is specified in clause 6.3.2.1.

Tidentify-UTRAN FDD = 500 ms; which is defined in clause 6.3.2.1.

TSI-UTRAN FDD:Maximum repetition period of relevant system info blocks that need to be received by the UE during RRC connection release redirection to UTRAN FDD cell. 1280 ms is assumed in this test case.

TRA = 40ms, this is the additional delay caused by the random access procedure.

This gives a total delay of 1930 ms.

## A.6.3.13Redirection from E-UTRA to NR FR1 for redcap UE

## A.6.3.13.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from E-UTRA to NR requirements specified in clause 6.3.2.4.

## A.6.3.13.2Test Parameters

Supported test configurations are shown in table A.6.3.13.2-1. The time delay is tested by using the parameters in table A.6.3.13.2-2, and A.6.3.13.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.6.3.13.2-1: Redirection from E-UTRAN to NR test configurations

Table A.6.3.13.2-2: General test parameters for Redirection from E-UTRAN to NR test case

Table A.6.3.13.2-3: Cell specific test parameters for Redirection from E-UTRAN to NR test case (cell 1)

Table A.6.3.13.2-4: Cell specific test parameters for Redirection from E-UTRAN to NR test case (cell 2)

## A.6.3.13.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90%.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms regardless RedCap UE is capable of 2 Rx or only supports 1 Rx antenna.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.
