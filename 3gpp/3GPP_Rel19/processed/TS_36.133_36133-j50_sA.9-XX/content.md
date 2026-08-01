---
type: spec
aliases:
  - 36.133_36133-j50_sA.9-XX
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.133_36133-j50_sA.9-XX/content.md"
---
# TS 36.133 36133-j50_sA.9-XX

## A.9Measurement Performance Requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in Clause 9 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in Clause 9 for at least 90% of the reported cases.

-Cell 1 is the PCell.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.9.1RSRP

## A.9.1.1FDD Intra frequency case

## A.9.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.1 and 9.1.2.2 for FDD intra frequency measurements.

## A.9.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.1.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.1.2-1: RSRP FDD Intra frequency test parameters

## A.9.1.1.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.2.1 and 9.1.2.2. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.2.7 and 9.1.2.8.

## A.9.1.2TDD Intra frequency case

## A.9.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.1 and 9.1.2.2 for TDD intra frequency measurements.

## A.9.1.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.2.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.2.2-1: RSRP TDD Intra frequency test parameters

## A.9.1.2.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.2.1 and 9.1.2.2. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.2.7 and 9.1.2.8.

## A.9.1.3FDD—FDD Inter frequency case

## A.9.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3.1 and 9.1.3.2 for FDD—FDD inter frequency measurements. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.2.7 and 9.1.2.8.

## A.9.1.3.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.3.2-1 In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.1.3.2-1: RSRP FDD—FDD Inter frequency test parameters

## A.9.1.3.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3.1 and 9.1.3.2. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.3.3 and 9.1.3.4.

## A.9.1.4TDD—TDD Inter frequency case

## A.9.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3.1 and 9.1.3.2 for TDD—TDD inter frequency measurements.

## A.9.1.4.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.4.2-1 for TDD configuration 1 and in Table A.9.1.4.2-2 for TDD configuration 0. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.1.4.2-1: RSRP TDD—TDD Inter frequency test parameters for TDD configuration 1

Table A.9.1.4.2-2: RSRP TDD—TDD Inter frequency test parameters for TDD configuration 0

## A.9.1.4.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3.1 and 9.1.3.2. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.3.3 and 9.1.3.4.

## A.9.1.5FDD—TDD Inter frequency case

## A.9.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3.1 and 9.1.3.2 for FDD—TDD inter frequency measurements.

## A.9.1.5.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.5.2-1 and Table A.9.1.5.2-2.  In all test cases, Cell 1 is the serving cell and Cell 2 the target cell. Cell 1 is FDD cell and Cell 2 is TDD cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.1.5.2-1: RSRP FDD—TDD Inter frequency test parameters (FDD Cell1)

Table A.9.1.5.2-2: RSRP FDD—TDD Inter frequency test parameters (TDD cell2)

## A.9.1.5.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3.1 and 9.1.3.2. The RSRP measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.3.3 and 9.1.3.4.

## A.9.1.6FDD RSRP for E-UTRAN Carrier Aggregation

## A.9.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2. The test will also verify the primary and secondary component carrier relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.6.2Test parameters

In this set of cases cell1 is PCell on the primary component carrier, cell2 is SCell on the secondary component carrier and activated, and cell3 is the neighboring cell on the secondary component carrier.  The test parameters are given in Table A.9.1.6.2-1.

Table A.9.1.6.2-1: RSRP FDD carrier aggregation test parameters

## A.9.1.6.3Test Requirements

In the test, the performance of RSRP measurements is verified from following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.7TDD RSRP for E-UTRAN Carrier Aggregation

The test case in this clause are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the absolute RSRP accuracy on PCell defined in clause 9.1.11.1, the absolute RSRP accuracy on Scell defined in clause 9.1.11.2, the relative RSRP accuracy between SCell and Cell 3 defined in clause 9.1.11.2, and the relative RSRP accuracy between PCell and SCell defined in clause 9.1.11.3.

## A.9.1.7.2Test parameters

In this set of test cases there are three cells on two carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, and Cell 3 is neighbour cell which is also on channel 2. The parameters for the test are listed in Table A.9.1.7.2-1.

Table A.9.1.7.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.7.3Test Requirements

In the test, the performance of RSRP measurements is verified form following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3

## A.9.1.8FDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.3 and 9.1.2.4 for FDD intra-frequency RSRP measurements under time-domain measurement resource restriction with non-MBSFN ABS configured in the aggressor cell.

## A.9.1.8.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.8.2-1 and A.9.1.8.2-2.

In the tests there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 2. Cell 2 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 2 are measured for RSRP relative accuracy. Non-MBSFN ABS pattern is configured for Cell 1 during the test. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.1.8.2-1: General test parameters for E-UTRAN FDD RSRP intra frequency test parameters under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.1.8.2-2: Cell-specific test parameters for E-UTRAN FDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with non-MBSFN ABS

## A.9.1.8.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.3 and 9.1.2.4, respectively.

## A.9.1.9TDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.1.9.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.3 and 9.1.2.4 for TDD intra-frequency RSRP measurements under time-domain measurement resource restriction with non-MBSFN ABS configured in the aggressor cell.

## A.9.1.9.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.9.2-1 and A.9.1.9.2-2.

In the tests there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 2. Cell 2 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 2 are measured for RSRP relative accuracy. Non-MBSFN ABS pattern is configured for Cell 1 during the test. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.1.9.2-1: General test parameters for E-UTRAN TDD RSRP intra frequency test parameters under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.1.9.2-2: Cell-specific test parameters for E-UTRAN TDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with non-MBSFN ABS

## A.9.1.9.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.3 and 9.1.2.4, respectively.

## A.9.1.10FDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS

## A.9.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.3 and 9.1.2.4 for FDD intra-frequency RSRP measurements under time-domain measurement resource restriction with MBSFN ABS configured in the aggressor cell.

## A.9.1.10.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.10.2-1 and A.9.1.10.2-2.

In the tests there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 2. Cell 2 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 2 are measured for RSRP relative accuracy. MBSFN ABS pattern is configured in Cell 1 during the test. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.1.10.2-1: General test parameters for E-UTRAN FDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with MBSFN ABS

Table A.9.1.10.2-2: Cell-specific test parameters for E-UTRAN FDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with MBSFN ABS

## A.9.1.10.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.3 and 9.1.2.4, respectively.

## A.9.1.11TDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS

## A.9.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.3 and 9.1.2.4 for TDD intra-frequency RSRP measurements under time-domain measurement resource restriction with MBSFN ABS configured in the aggressor cell.

## A.9.1.11.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.11.2-1 and A.9.1.11.2-2.

In the tests there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 2. Cell 2 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 2 are measured for RSRP relative accuracy. MBSFN ABS pattern is configured in Cell 1 during the test. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.1.11.2-1: General test parameters for E-UTRAN TDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with MBSFN ABS

Table A.9.1.11.2-2: Cell-specific test parameters for E-UTRAN TDD RSRP intra-frequency test parameters under time-domain measurement resource restriction with MBSFN ABS

## A.9.1.11.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.3 and 9.1.2.4, respectively.

## A.9.1.12FDD RSRP for E-UTRAN Carrier Aggregation for 20MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.12.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.6.1.

## A.9.1.12.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.12.2-1 will replace the values of corresponding parameters in Tables A.9.1.6.2-1.

Table A.9.1.12.2-1: RSRP FDD carrier aggregation test parameters

## A.9.1.12.3Test Requirements

The test requirements defined in section A.9.1.6.3 shall apply to this test case.

## A.9.1.13TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.13.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.7.1.

## A.9.1.13.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.13.2-1 will replace the values of corresponding parameters in Tables A.9.1.7.2-1.

Table A.9.1.13.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.13.3Test Requirements

The test requirements defined in section A.9.1.7.3 shall apply to this test case.

## A.9.1.14FDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.5 and 9.1.2.6 for FDD intra-frequency RSRP measurements under time-domain measurement resource restriction with CRS Assistance Information and non-MBSFN ABS configured in the aggressor cells.

## A.9.1.14.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.14.2-1 and A.9.1.14.2-2.

In the tests there are three synchronous cells, Cell 1, Cell2 and Cell 3, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 3. Cell 2 is the neighbour aggressor cell without CRS colliding to Cell 3. Cell 3 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 3 are measured for RSRP relative accuracy. Non-MBSFN ABS pattern is configured for Cell 1 and Cell 2 during the test.

The UE is configured by higher layers with a time domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells, namely Cell 3 measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2. The information for both measurement pattern and the CRS assistance information shall be provided via RRC to the UE before the measurements start.

Note:It’s up to eNB’s implementation whether the time domain measurement resource restriction pattern for PCell measurements is configured or not.

Table A.9.1.14.2-1: General test parameters for FDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

Table A.9.1.14.2-2: Cell-specific test parameters for FDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.1.14.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.5 and 9.1.2.6, respectively.

## A.9.1.15TDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.1.15.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.5 and 9.1.2.6 for TDD intra-frequency RSRP measurements under time-domain measurement resource restriction with CRS Assistance Information and non-MBSFN ABS configured in the aggressor cells.

## A.9.1.15.2Test parameters

In this set of test cases all cells are on the same carrier frequency as PCell. Both absolute and relative accuracy of RSRP intra-frequency measurements are tested, with test parameters specified in Tables A.9.1.15.2-1 and A.9.1.15.2-2.

In the tests there are three synchronous cells, Cell 1, Cell2 and Cell 3, on the same RF channel. In all test cases, Cell 1 is the serving cell (PCell) and also the aggressor cell to Cell 3. Cell 2 is the neighbour aggressor cell without CRS colliding to Cell 3. Cell 3 is the cell to be measured for RSRP absolute accuracy, whilst both Cell 1 and Cell 3 are measured for RSRP relative accuracy. Non-MBSFN ABS pattern is configured for Cell 1 and Cell 2 during the test.

The UE is configured by higher layers with a time domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells, namely Cell 3 measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2. The information for both measurement pattern and the CRS assistance information shall be provided via RRC to the UE before the measurements start.

Note:It’s up to eNB’s implementation whether the time domain measurement resource restriction pattern for PCell measurements is configured or not.

Table A.9.1.15.2-1: General test parameters for TDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

Table A.9.1.15.2-2: Cell-specific test parameters for TDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.1.15.3Test Requirements

The absolute RSRP measurement accuracy and relative RSRP measurement accuracy shall fulfill the requirements in Sections 9.1.2.5 and 9.1.2.6, respectively.

## A.9.1.16FDD Intra frequency case for 5MHz Bandwidth

## A.9.1.16.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2.1 and 9.1.2.2 for FDD intra frequency measurements.

## A.9.1.16.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.16.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.16.2-1: RSRP FDD Intra frequency test parameters for 5MHz Bandwidth

## A.9.1.16.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.2.1 and 9.1.2.2.

## A.9.1.17FDD—FDD Inter frequency case for 5MHz Bandwidth

## A.9.1.17.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3.1 and 9.1.3.2 for FDD—FDD inter frequency measurements.

## A.9.1.17.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.17.2-1 In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.1.17.2-1: RSRP FDD—FDD Inter frequency test parameters for 5MHz Bandwidth

Table A.9.1.17.2-1: Void

## A.9.1.17.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3.1 and 9.1.3.2.

## A.9.1.18FDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.18.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.6.1.

## A.9.1.18.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.18.2-1 will replace the values of corresponding parameters in Tables A.9.1.6.2-1.

Table A.9.1.18.2-1: RSRP FDD carrier aggregation test parameters

## A.9.1.18.3Test Requirements

The test requirements defined in section A.9.1.6.3 shall apply to this test case.

## A.9.1.19TDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.19.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.7.1.

## A.9.1.19.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.19.2-1 will replace the values of corresponding parameters in Tables A.9.1.7.2-1.

Table A.9.1.19.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.19.3Test Requirements

The test requirements defined in section A.9.1.7.3 shall apply to this test case.

## A.9.1.20FDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.20.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.6.1.

## A.9.1.20.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.20.2-1 will replace the values of corresponding parameters in Tables A.9.1.6.2-1.

Table A.9.1.20.2-1: RSRP FDD carrier aggregation test parameters

## A.9.1.20.3Test Requirements

The test requirements defined in section A.9.1.6.3 shall apply to this test case.

## A.9.1.21TDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.21.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.7.1.

## A.9.1.21.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.21.2-1 will replace the values of corresponding parameters in Tables A.9.1.7.2-1.

Table A.9.1.21.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.21.3Test Requirements

The test requirements defined in section A.9.1.7.3 shall apply to this test case.

## A.9.1.22RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD

## A.9.1.22.1Test Purpose and Environment

The test case is applicable for TDD-FDD carrier aggregation capable UEs which have been configured with a downlink PCell in FDD and a downlink SCell in TDD.

The purpose of this test is to verify that the RSRP absolute and relative measurements accuracy in TDD-FDD carrier aggregation is within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2, the relative RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2 between the SCell and a neighbour cell, and the relative RSRP accuracy requirements of the PCell compared to the SCell defined in Clause 9.1.11.3.

## A.9.1.22.2Test parameters

In this test case, Cell 1 is the PCell on the FDD primary component carrier, Cell 2 is the configured and activated SCell on the TDD secondary component carrier, and Cell 3 is the neighboring cell on the TDD secondary component carrier. The test parameters are given in Table A.9.1.22.2-1.

Table A.9.1.22.2-1: RSRP TDD-FDD carrier aggregation test parameters

## A.9.1.22.3Test Requirements

In the test, the performance of RSRP measurements is verified from following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.23 RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD

## A.9.1.23.1Test Purpose and Environment

The test case is applicable for TDD-FDD carrier aggregation capable UEs which have been configured with a downlink PCell in TDD and a downlink SCell in FDD.

The purpose of this test is to verify that the RSRP absolute and relative measurements accuracy in TDD-FDD carrier aggregation is within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2, the relative RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.11.2 between the SCell and a neighbour cell, and the relative RSRP accuracy requirements of the PCell compared to the SCell defined in Clause 9.1.11.3.

## A.9.1.23.2Test parameters

In this test case, Cell 1 is the PCell on the TDD primary component carrier, Cell 2 is the configured and activated SCell on the FDD secondary component carrier, and Cell 3 is the neighboring cell on the FDD secondary component carrier. The test parameters are given in Table A.9.1.23.2-1.

Table A.9.1.23.2-1: RSRP TDD-FDD carrier aggregation test parameters

## A.9.1.23.3Test Requirements

In the test, the performance of RSRP measurements is verified from following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.24TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz + 10MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.1.24.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.1.7.1.

## A.9.1.24.2Test parameters

The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.1.24.2-1 will replace the values of corresponding parameters in Tables A.9.1.7.2-1.

Table A.9.1.24.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.24.3Test Requirements

The test requirements defined in section A.9.1.7.3 shall apply to this test case.

## A.9.1.25FDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal

## A.9.1.25.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRP absolute and relative measurement accuracies in CRS based discovery signal are within the specified limits. This test will verify the requirements in Sections 9.1.14.2.

## A.9.1.25.2Test parameters

In this test case, all cells are on the same carrier frequency. Both absolute and relative accuracies of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.25.2-1. In this test case, Cell 1 is the PCell and Cell 2 is the target cell. The Cell 2 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.25.2-1: RSRP FDD Intra frequency test parameters

## A.9.1.25.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.2.

## A.9.1.26TDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal

## A.9.1.26.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative measurement accuracies in CRS based discovery signal are within the specified limits. This test will verify the requirements in Sections 9.1.14.2.

## A.9.1.26.2Test parameters

In this test case all cells are on the same carrier frequency. Both absolute and relative accuracies of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.26.2-1. In this test case, Cell 1 is the PCell and Cell 2 is the target cell. The Cell 2 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.26.2-1: RSRP TDD Intra frequency test parameters

## A.9.1.26.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14. 2.

## A.9.1.27FDD—FDD inter-frequency absolute and relative RSRP accuracies in CRS based discovery signal

## A.9.1.27.1Test Purpose and Environment

The purpose of this test is to verify that the CRS RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.2 for FDD—FDD inter frequency measurements.

## A.9.1.27.2Test parameters

In this set of test case the cells are on different carrier frequencies. Both absolute and relative accuracy of CRS RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.27.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap and a DMTC configuation.

Table A.9.1.27.2-1: CRS RSRP FDD—FDD Inter frequency test parameters

## A.9.1.27.3Test Requirements

The CRS RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.2.

## A.9.1.28TDD—TDD inter-frequency absolute and relative  RSRP accuracies in CRS based discovery signal

## A.9.1.28.1Test Purpose and Environment

The purpose of this test is to verify that the CRS RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.2 for TDD—TDD inter frequency measurements.

## A.9.1.28.2Test parameters

In this set of test case the cells are on different carrier frequencies. Both absolute and relative accuracy of CRS RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.28.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap and a DMTC configuation.

Table A.9.1.28.2-1: CRS RSRP TDD—TDD Inter frequency test parameters

## A.9.1.28.3Test Requirements

The CRS RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.2.

## A.9.1.29FDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal

## A.9.1.29.1Test Purpose and Environment

The purpose of this test is to verify that the CSI- RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.3 for FDD intra frequency measurements.

## A.9.1.29.2Test parameters

In this set of test case all cells are on the same carrier frequencies. Both absolute and relative accuracy of CSI- RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.29.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The intra frequency measurements are supported by a DMTC configuration.

Table A.9.1.29.2-1: CSI-RSRP FDD Intra frequency test parameters

## A.9.1.29.3Test Requirements

The CSI- RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.3.

## A.9.1.30TDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal

## A.9.1.30.1Test Purpose and Environment

The purpose of this test is to verify that the CSI- RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.3 for TDD intra frequency measurements.

## A.9.1.30.2Test parameters

In this set of test case all cells are on the same carrier frequencies. Both absolute and relative accuracy of CSI- RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.30.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The intra frequency measurements are supported by a DMTC configuation.

Table A.9.1.30.2-1: CSI-RSRP TDD Intra frequency test parameters

## A.9.1.30.3Test Requirements

The CSI- RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.3.

## A.9.1.31FDD—FDD inter-frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal

## A.9.1.31.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.3 for FDD—FDD inter frequency measurements.

## A.9.1.31.2Test parameters

In this set of test case the cells are on different carrier frequencies. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.31.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap and two DMTC configurations which one is for cell1 and the other is for cell2.

Table A.9.1.31.2-1: CSI-RSRP FDD—FDD Inter frequency test parameters

## A.9.1.31.3Test Requirements

The CSI-RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.3.

## A.9.1.32TDD—TDD inter-frequency absolute and relative  CSI-RSRP accuracies in CSI-RS based discovery signal

## A.9.1.32.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.14.3 for TDD—TDD inter frequency measurements.

## A.9.1.32.2Test parameters

In this set of test case the cells are on different carrier frequencies. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.32.2-1. In this test case, Cell 1 is the PCell and Cell 2 the target cell. The inter frequency measurements are supported by a measurement gap and two DMTC configurations which one is for cell1 and the other is for cell2.

Table A.9.1.32.2-1: CSI-RSRP TDD—TDD Inter frequency test parameters

## A.9.1.32.3Test Requirements

The CSI-RSRP measurement accuracy shall fulfil the requirements in sections 9.1.14.3.

## A.9.1.33FDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal

## A.9.1.33.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRP absolute and relative measurement accuracies in carrier aggregation in CRS based discovery signal are within the specified limits. This test will verify the absolute RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.15.1.2, and the relative RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.15.1.2. The test will also verify the primary and secondary component carrier relative RSRP accuracy requirement defined in Clause 9.1.15.1.3.

## A.9.1.33.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier and activated, and Cell3 is the neighboring cell on the secondary component carrier. The test parameters are given in Table A.9.1.33.2-1. The Cell 3 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.33.2-1: RSRP FDD carrier aggregation test parameters

## A.9.1.33.3Test Requirements

In the test, the performance of RSRP measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 3 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.1.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.1.2

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.15.1.3.

## A.9.1.34TDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal

## A.9.1.34.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRP absolute and relative measurement accuracies in carrier aggregation in CRS based discovery signal are within the specified limits. This test will verify the absolute RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.15.1.2, and the relative RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.15.1.2. The test will also verify the primary and secondary component carrier relative RSRP accuracy requirement defined in Clause 9.1.15.1.3.

## A.9.1.34.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier and activated, and Cell3 is the neighboring cell on the secondary component carrier. The test parameters are given in Table A.9.1.34.2-1. The Cell 3 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.34.2-1: Carrier aggregation RSRP test parameters for TDD

## A.9.1.34.3Test Requirements

In the test, the performance of RSRP measurements is verified form following three perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 3 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.1.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.1.2

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.15.1.3.

## A.9.1.35FDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal

## A.9.1.35.1Test Purpose and Environment

The purpose of this test is to verify that the FDD CSI-RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute CSI-RSRP accuracy requirements of the primary component carrier defined in clause 9.1.15.2.1, the absolute CSI-RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.15.2.2, and the relative CSI-RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.15.2.2. The test will also verify the primary and secondary component carrier relative CSI-RSRP accuracy requirement defined in Clause 9.1.15.2.3.

## A.9.1.35.2Test parameters

In this set of cases cell1 is PCell on the primary component carrier, cell2 is SCell on the secondary component carrier and activated, and cell3 is the neighboring cell on the secondary component carrier.  The test parameters are given in Table A.9.1.35.2-1. This set is supported by two DMTC configurations which one is for cell1 and the other is for cell2 and cell3.

Table A.9.1.35.2-1: CSI-RSRP FDD carrier aggregation test parameters

## A.9.1.35.3Test Requirements

In the test, the performance of CSI-RSRP measurements is verified from following four perspectives:

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.15.2.1.

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.2.2.

-The relative accuracy of intra-frequency CSI-RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.2.2.

-The relative accuracy of inter-frequency CSI-RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.15.2.3.

## A.9.1.36TDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal

## A.9.1.36.1Test Purpose and Environment

The purpose of this test is to verify that the TDD CSI-RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute CSI-RSRP accuracy requirements of the primary component carrier defined in clause 9.1.15.2.1, the absolute CSI-RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.15.2.2, and the relative CSI-RSRP accuracy requirements of the secondary component carrier defined in clause 9.1.15.2.2. The test will also verify the primary and secondary component carrier relative CSI-RSRP accuracy requirement defined in Clause 9.1.15.2.3.

## A.9.1.36.2Test parameters

In this set of cases cell1 is PCell on the primary component carrier, cell2 is SCell on the secondary component carrier and activated, and cell3 is the neighboring cell on the secondary component carrier.  The test parameters are given in Table A.9.1.36.2-1. This set is supported by two DMTC configurations which one is for cell1 and the other is for cell2 and cell3.

Table A.9.1.36.2-1: CSI-RSRP TDD carrier aggregation test parameters

## A.9.1.36.3Test Requirements

In the test, the performance of CSI-RSRP measurements is verified from following four perspectives:

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.15.2.1.

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.2.2.

-The relative accuracy of intra-frequency CSI-RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.15.2.2.

-The relative accuracy of inter-frequency CSI-RSRP measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.15.2.3.

## A.9.1.373 DL PCell in FDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.37.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in FDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.37.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2 and cell 4 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. Cell 3 and cell 5 are neighbouring cells on secondary component carriers SCC1 and SCC2 respectively.  The test parameters are given in Table A.9.1.37.2-1.

Table A.9.1.37.2-1: 3 Downlink PCell in FDD RSRP carrier aggregation test parameters

## A.9.1.37.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 7 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.383 DL PCell in TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.38.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in TDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.38.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2 and cell 4 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. Cell 3 and cell 5 are neighbouring cells on secondary component carriers SCC1 and SCC2 respectively.  The test parameters are given in Table A.9.1.38.2-1.

Table A.9.1.38.2-1: 3 Downlink PCell in TDD RSRP carrier aggregation test parameters

## A.9.1.38.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 7 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.393 DL FDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.39.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.39.2Test parameters

In this set of test cases there are five cells on three carrier frequencies. Cell 1 is PCell on channel 1, and cell 2 and cell 4 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. Cell 3 and cell 5 are neighbouring cells on secondary component carriers SCC1 and SCC2 respectively.  The parameters for the test are listed in Table A.9.1.39.2-1.

Table A.9.1.39.2-1: 3 DL FDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #1, cell #2 and cell #3)

Table A.9.1.39.2-2: 3 DL FDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #4 and cell #5)

## A.9.1.39.3Test Requirements

In the test, the performance of RSRP measurements is verified form following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.403 DL TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.40.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.40.2Test parameters

In this set of test cases there are five cells on three carrier frequencies. Cell 1 is PCell on channel 1, and cell 2 and cell 4 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. Cell 3 and cell 5 are neighbouring cells on secondary component carriers SCC1 and SCC2 respectively.  The parameters for the test are listed in Table A.9.1.40.2-1.

Table A.9.1.40.2-1: 3 DL TDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #1, cell #2 and cell #3)

Table A.9.1.40.2-2: 3 DL TDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #4 and cell #5)

## A.9.1.40.3Test Requirements

In the test, the performance of RSRP measurements is verified form following four perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.41FD-FDD RSRP Intra frequency case for UE category 0

## A.9.1.41.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.13.1 and 9.1.13.2 for FD-FDD intra frequency RSRP measurements for UE category 0.

## A.9.1.41.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.41.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.41.2-1: FD-FDD RSRP Intra frequency test parameters for UE category 0

## A.9.1.41.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.13.1 and 9.1.13.2.

## A.9.1.42HD-FDD RSRP Intra frequency case for UE category 0

## A.9.1.42.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.13.1 and 9.1.13.2 for HD-FDD intra frequency RSRP measurements for UE category 0.

## A.9.1.42.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.42.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.42.2-1: HD-FDD RSRP Intra frequency test parameters for UE category 0

## A.9.1.42.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.13.1 and 9.1.13.2.

## A.9.1.43TDD RSRP Intra frequency case for UE category 0

## A.9.1.43.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.13.1 and 9.1.13.2 for TDD intra frequency RSRP measurements for UE category 0.

## A.9.1.43.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.43.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.43.2-1: TDD RSRP Intra frequency test parameters for UE category 0

## A.9.1.43.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.13.1 and 9.1.13.2.

## A.9.1.444 DL CA PCell in FDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.44.1Test Purpose and Environment

The purpose of this test is to verify that the FDD-TDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in FDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.44.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4 and cell 6 are activated SCells on secondary component carriers SCC1, SCC2 and SCC3 respectively. Cell 3, cell 5 and cell 7 are neighbouring cells on secondary component carriers SCC1, SCC2 and SCC3 respectively.  The test parameters are given in Table A.9.1.44.2-1.

Table A.9.1.44.2-1: 4 Downlink PCell in FDD-TDD RSRP carrier aggregation test parameters

## A.9.1.44.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 10 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.454 DL CA PCell in TDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.45.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in TDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.45.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4 and cell 6 are activated SCells on secondary component carriers SCC1, SCC2 and SCC3 respectively. Cell 3, cell 5 and cell 7 are neighbouring cells on secondary component carriers SCC1, SCC2 and SCC3 respectively.  The test parameters are given in Table A.9.1.45.2-1.

Table A.9.1.45.2-1: 4 Downlink PCell in TDD-FDD RSRP carrier aggregation test parameters

## A.9.1.45.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.464 DL FDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.46.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in FDD-FDD carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.46.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4 and cell 6 are activated SCells on secondary component carriers SCC1, SCC2 and SCC3 respectively. Cell 3, cell 5 and cell 7 are neighbouring cells on secondary component carriers SCC1, SCC2 and SCC3 respectively.  The test parameters are given in Table A.9.1.46.2-1, Table A.9.1.46.2-2 and Table A.9.1.46.2-3.

Table A.9.1.46.2-1: 4 DL FDD RSRP carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.1.46.2-2: 4 DL FDD RSRP carrier aggregation test parameters for cell 4 and cell 5

Table A.9.1.46.2-3: 4 DL FDD RSRP carrier aggregation test parameters for cell 6 and cell 7

## A.9.1.46.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 10 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.474 DL TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.47.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in TDD-TDD carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.47.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4 and cell 6 are activated SCells on secondary component carriers SCC1, SCC2 and SCC3 respectively. Cell 3, cell 5 and cell 7 are neighbouring cells on secondary component carriers SCC1, SCC2 and SCC3 respectively.  The test parameters are given in Table A.9.1.47.2-1, Table A.9.1.47.2-2 and Table A.9.1.47.2-3.

Table A.9.1.47.2-1: 4 DL TDD RSRP carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.1.47.2-2: 4 DL TDD RSRP carrier aggregation test parameters for cell 4 and cell 5

Table A.9.1.47.2-3: 4 DL TDD RSRP carrier aggregation test parameters for cell 6 and cell 7

## A.9.1.47.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 10 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.485 DL FDD-TDD with PCell in FDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.48.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in FDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.48.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell 6 and cell 8 are activated SCells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively. Cell 3, cell 5, cell 7 and cell 9 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively.  The test parameters are given in Table A.9.1.48.2-1, Table A.9.1.48.2-2 and Table A.9.1.48.2-3.

Table A.9.1.48.2-1: 5 Downlink PCell in FDD RSRP carrier aggregation test parameters for cell 1, cell 2, cell 3, cell 4 and cell 5

Table A.9.1.48.2-2: 5 Downlink PCell in FDD RSRP carrier aggregation test parameters for cell 6 and cell 7

Table A.9.1.48.2-3: 5 Downlink PCell in FDD RSRP carrier aggregation test parameters for cell 8 and cell 9

## A.9.1.48.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 13 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.495 DL FDD-TDD with PCell in TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.49.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in TDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.49.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell 6 and cell 8 are activated SCells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively. Cell 3, cell 5, cell 7 and cell 9 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively.  The test parameters are given in Table A.9.1.49.2-1, Table A.9.1.49.2-2 and Table A.9.1.49.2-3.

Table A.9.1.49.2-1: 5 Downlink PCell in TDD RSRP carrier aggregation test parameters for cell 1, cell 2, cell 3, cell 4 and cell 5

Table A.9.1.49.2-2: 5 Downlink PCell in TDD RSRP carrier aggregation test parameters for cell 6 and cell 7

Table A.9.1.49.2-3: 5 Downlink PCell in TDD RSRP carrier aggregation test parameters for cell 8 and cell 9

## A.9.1.49.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 13 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.505 DL FDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.50.1Test Purpose and Environment

The purpose of this test is to verify that the FDD-FDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in FDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.50.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell6 and cell8 are activated SCells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively. Cell 3, cell 5, cell7 and cell9 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively.  The test parameters are given in Table A.9.1.50.2-1.

Table A.9.1.50.2-1: 5 DL FDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #1, cell #2 and cell #3)

Table A.9.1.50.2-2: 5 DL FDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #4 – cell #9)

## A.9.1.50.3Test Requirements

In the test, the performance of RSRP measurements is verified form following perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.515 DL TDD RSRP for E-UTRAN in Carrier Aggregation

## A.9.1.51.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRP absolute and relative accuracy requirements in carrier aggregation with PCell in TDD are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.51.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell6 and cell8 are activated SCells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively. Cell 3, cell 5, cell7 and cell9 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively.  The test parameters are given in Table A.9.1.51.2-1.

Table A.9.1.51.2-1: 5 DL TDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #1, cell #2 and cell #3)

Table A.9.1.51.2-2: 5 DL TDD RSRP test parameters for E-UTRAN Carrier aggregation (cell #4 – cell #9)

## A.9.1.51.3Test Requirements

In the test, the performance of RSRP measurements is verified form following perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.52FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.52.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 and 9.1.21.2 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.52.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.52.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.52.2-1: FD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.52.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.52AFD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA

## A.9.1.52A.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 and 9.1.21.2 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.52A.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.52A.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.52A.2-1: FD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA

## A.9.1.52A.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.53HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.53.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 and 9.1.21.2 for HD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.53.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.53.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.53.2-1: HD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.53.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.53AHD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA

## A.9.1.53A.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 and 9.1.21.2 for HD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.53A.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.53A.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.53A.2-1: HD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA

## A.9.1.53A.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.54TDD RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.54.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 and 9.1.21.2 for TDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.54.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.54.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.54.2-1: TDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.54.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.55FS3 Intra frequency absolute and relative RSRP accuracies with FDD PCell

## A.9.1.55.1Test Purpose and Environment

The purpose of this test is to verify that the FDD intra frequency RSRP absolute and relative measurement accuracies in carrier aggregation with frame structure 3 in the configured DMTC occasion are within the specified limits. This test will verify the absolute RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.19.2, and the relative RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.19.2. The test will also verify the primary and secondary component carrier relative RSRP accuracy requirement defined in Clause 9.1.19.4.

## A.9.1.55.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier with frame structure 3 and activated, and Cell3 is the neighboring cell on the same secondary component carrier of Cell2. The test parameters are given in Table A.9.1.55.2-1. The DMTC configuration for Cell2 and Cell3 is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.55.2-1: Test parameters for FDD RSRP accuracies of Scell with FS3

## A.9.1.55.3Test Requirements

In the test, the performance of RSRP measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 3 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.19.4.

## A.9.1.56FS3 Intra frequency absolute and relative RSRP accuracies with TDD PCell

## A.9.1.56.1Test Purpose and Environment

The purpose of this test is to verify that the TDD intra frequency RSRP absolute and relative measurement accuracies in carrier aggregation with frame structure 3 in the configured DMTC occasion are within the specified limits. This test will verify the absolute RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.19.2, and the relative RSRP accuracy requirement of the secondary component carrier defined in clause 9.1.19.2. The test will also verify the primary and secondary component carrier relative RSRP accuracy requirement defined in Clause 9.1.19.4.

## A.9.1.56.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier with frame structure 3 and activated, and Cell3 is the neighboring cell on the same secondary component carrier of Cell2. The test parameters are given in Table A.9.1.56.2-1. The DMTC configuration for Cell2 and Cell3 is provided to the UE in the measDS-Config before the start of the test.

Table A.9.1.56.2-1: Test parameters for TDD RSRP accuracies of Scell with FS3

## A.9.1.56.3Test Requirements

In the test, the performance of RSRP measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 3 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2

-The relative accuracy of inter-frequency RSRP measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.19.4.

## A.9.1.57FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.57.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 and 9.1.21.4 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.57.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.57.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.57.2-1: FD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.57.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3 and 9.1.21.4.

## A.9.1.57AFD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB

## A.9.1.57A.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 and 9.1.21.4 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.57A.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.57A.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.57A.2-1: FD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB

## A.9.1.57A.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3 and 9.1.21.4.

## A.9.1.58HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.58.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 and 9.1.21.4 for HD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.58.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.58.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.58.2-1: HD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.58.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3 and 9.1.21.4.

## A.9.1.58AHD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB

## A.9.1.58A.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 and 9.1.21.4 for HD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.58A.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.58A.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.58.2-1: HD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB

## A.9.1.58A.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3 and 9.1.21.4.

## A.9.1.59TDD RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.59.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 and 9.1.21.4 for TDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.59.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.59.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.59.2-1: TDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.59.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3 and 9.1.21.4.

## A.9.1.60FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with FDD PCell

## A.9.1.60.1Test Purpose and Environment

The purpose of this test is to verify that CSI- RSRP measurement accuracy is within the specified limits. This test will verify the absolute intra-frequency CSI-RSRP accuracy requirements of the SCells defined in Section 9.1.18.4.4 for intra-frequency measurements under FS3, and the relative intra-frequency CSI-RSRP accuracy requirements between SCells defined in Section 9.1.18.4.5.

## A.9.1.60.2Test parameters

In this set of cases Cell 1 is PCell on the primary component carrier, Cell 2 using FS3 is SCell on the secondary component carrier and activated, and Cell 3 using FS3 is the neighbouring cell on the secondary component carrier. The test parameters are given in Table A.9.1.60.2-1. Intra-frequency measurements are supported by a DMTC configuration.

A.9.1.60.2-1: CSI-RSRP carrier aggregation test parameters with FDD PCell and FS3 SCells

## A.9.1.60.3Test Requirements

In the test, the performance of CSI-RSRP measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.4.

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 3 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.4.

-The relative accuracy of intra-frequency CSI-RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.5.

## A.9.1.61FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with TDD PCell

## A.9.1.61.1Test Purpose and Environment

The purpose of this test is to verify that CSI- RSRP measurement accuracy is within the specified limits. This test will verify the absolute intra-frequency CSI-RSRP accuracy requirements of the SCells defined in Section 9.1.18.4.4 for intra-frequency measurements under FS3, and the relative intra-frequency CSI-RSRP accuracy requirements between SCells defined in Section 9.1.18.4.5.

## A.9.1.61.2Test parameters

In this set of cases Cell 1 is PCell on the primary component carrier, Cell 2 using FS3 is SCell on the secondary component carrier and activated, and Cell 3 using FS3 is the neighboring cell on the secondary component carrier. The test parameters are given in Table A.9.1.61.2-1. The intra-frequency measurements are supported by a DMTC configuration.

A.9.1.61.2-1: CSI-RSRP carrier aggregation test parameters with TDD PCell and FS3 SCells

## A.9.1.61.3Test Requirements

In the test, the performance of CSI-RSRP measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.4.

-The absolute accuracy of intra-frequency CSI-RSRP measurements for Cell 3 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.4.

-The relative accuracy of intra-frequency CSI-RSRP measurements for Cell 3 relative to Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.18.4.5.

## A.9.1.62FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA

## A.9.1.62.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.9 and 9.1.21.10 for FD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.62.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.62.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.62.2-1: FD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.62.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.9 and 9.1.21.10.

## A.9.1.63HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA

## A.9.1.53.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in section 9.1.21.9 and 9.1.21.10 for HD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.53.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.63.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.63.2-1: HD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.63.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1 and 9.1.21.2.

## A.9.1.64TDD RSRP Inter frequency case for Cat-M1 UE in CEModeA

## A.9.1.64.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.9 and 9.1.21.10 for TDD inter frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.64.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.64.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.1.64.2-1: TDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.64.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.9 and 9.1.21.10.

## A.9.1.65FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB

## A.9.1.65.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.11 and 9.1.21.12 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.65.2Test parameters

Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.65.2-1 and A.9.1.65.2-2. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.65.2-1: FD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 10MHz cell BW

Table A.9.1.65.2-2: FD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 5MHz cell BW

## A.9.1.65.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.11 and 9.1.21.12.

## A.9.1.66HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB

## A.9.1.66.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.11 and 9.1.21.12 for HD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.66.2Test parameters

Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.66.2-1 and A.9.1.66.2-2. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.66.2-1: HD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 10Mhz Cell BW

Table A.9.1.66.2-2: HD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 5MHz Cell BW

## A.9.1.66.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.11 and 9.1.21.12.

## A.9.1.67TDD RSRP Inter frequency case for Cat-M1 UE in CEModeB

## A.9.1.67.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.11 and 9.1.21.12 for TDD inter frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.67.2Test parameters

Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.9.1.67.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.9.1.67.2-1: TDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.67.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.11 and 9.1.21.12.

## A.9.1.683 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.1.68.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.1.37, A.9.1.38, A.9.1.39, A.9.1.40, does not need to be tested in the generic duplex-mode test case A.9.1.68.

## A.9.1.68.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2 and cell 4 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. Cell 3 and cell 5 are neighbouring cells on secondary component carriers SCC1 and SCC2 respectively.  The test parameters are given in Table A.9.1.68.2-1.

Table A.9.1.68.2-1: 3 Downlink RSRP carrier aggregation test parameters

## A.9.1.68.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 7 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.694 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.1.69.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.1.44, A.9.1.45, A.9.1.46, A.9.1.47, does not need to be tested in the generic duplex-mode test case A.9.1.69.

## A.9.1.69.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4 and cell 6 are activated SCells on secondary component carriers SCC1, SCC2 and SCC3 respectively. Cell 3, cell 5 and cell 7 are neighbouring cells on secondary component carriers SCC1, SCC2 and SCC3 respectively.  The test parameters are given in Table A.9.1.44.2-1.

Table A.9.1.69.2-1: 4 Downlink RSRP carrier aggregation test parameters

## A.9.1.69.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 10 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.705 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.1.70.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.1.48, A.9.1.49, A.9.1.50, A.9.1.51, does not need to be tested in the generic duplex-mode test case A.9.1.70.

## A.9.1.70.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell 6 and cell 8 are activated SCells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively. Cell 3, cell 5, cell 7 and cell 9 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3 and SCC4 respectively.  The test parameters are given in Table A.9.1.70.2-1, Table A.9.1.70.2-2 and Table A.9.1.70.2-3.

Table A.9.1.70.2-1: 5 Downlink RSRP carrier aggregation test parameters for cell 1, cell 2, cell 3, cell 4 and cell 5

Table A.9.1.70.2-2: 5 Downlink RSRP carrier aggregation test parameters for cell 6 and cell 7

Table A.9.1.70.2-3: 5 Downlink PCell in FDD RSRP carrier aggregation test parameters for cell 8 and cell 9

## A.9.1.70.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 13 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.716 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.1.71.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.71.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell 6, cell 8 and cell 10 are activated SCells on secondary component carriers SCC1, SCC2, SCC3, SCC4 and SCC5 respectively. Cell 3, cell 5, cell 7, cell 9 and cell 11 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3, SCC4 and SCC5 respectively. For testing the requirement related to a given SCell, the presence of at least the respective intra-frequency neigbouring cell (i.e. on the same secondary component carrier) is required. The test parameters are given in Table A.9.1.71.2-1, Table A.9.1.71.2-2 and Table A.9.1.71.2-3.

Table A.9.1.71.2-1: 6 Downlink RSRP carrier aggregation test parameters for cell 1, cell 2, cell 3, cell 4 and cell 5

Table A.9.1.71.2-2: 6 Downlink RSRP carrier aggregation test parameters for cell 6, cell 7, cell 8 and cell 9

Table A.9.1.71.2-3: 6 Downlink RSRP carrier aggregation test parameters for cell 10 and cell 11

## A.9.1.71.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 13 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 10 on SCC5 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 11 relative to Cell 10 on SCC5 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC5 and the primary component carriers for Cell 10 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.727 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.1.72.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP absolute and relative accuracy requirements in carrier aggregation are within the specified limits. This test will verify the absolute RSRP accuracy requirements of the primary component carrier defined in clause 9.1.11.1, the absolute RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2, and the relative RSRP accuracy requirements of the secondary component carriers defined in clause 9.1.11.2. The test will also verify the primary and secondary component carriers’ relative RSRP accuracy requirement defined in Clause 9.1.11.3.

## A.9.1.72.2Test parameters

In this set of test cases cell 1 is PCell on the primary component carrier, and cell 2, cell 4, cell 6, cell 8, cell 10 and cell12 are activated SCells on secondary component carriers SCC1, SCC2, SCC3, SCC4, SCC5 and SCC6 respectively. Cell 3, cell 5, cell 7, cell 9, cell 11 and cell 13 are neighbouring cells on secondary component carriers SCC1, SCC2, SCC3, SCC4, SCC5 and SCC6 respectively. For testing the requirement related to a given SCell, the presence of at least the respective intra-frequency neigbouring cell (i.e. on the same secondary component carrier) is required. The test parameters are given in Table A.9.1.72.2-1, Table A.9.1.72.2-2 and Table A.9.1.72.2-3.

Table A.9.1.72.2-1: 7 Downlink RSRP carrier aggregation test parameters for cell 1, cell 2, cell 3, cell 4 and cell 5

Table A.9.1.72.2-2: 7 Downlink RSRP carrier aggregation test parameters for cell 6, cell 7, cell8 and cell 9

Table A.9.1.72.2-3: 7 Downlink RSRP carrier aggregation test parameters for cell 10, cell 11, cell 12 and cell 13

## A.9.1.72.3Test Requirements

In the test, the performance of RSRP measurements is verified from the following 13 perspectives:

-The absolute accuracy of intra-frequency RSRP measurements for Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 10 on SCC5 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRP measurements for Cell 12 on SCC6 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 3 relative to Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 5 relative to Cell 4 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 7 relative to Cell 6 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 9 relative to Cell 8 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 11 relative to Cell 10 on SCC5 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of intra-frequency RSRP measurements for Cell 13 relative to Cell 12 on SCC6 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRP measurements between SCC1 and the primary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC2 and the primary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC3 and the primary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC4 and the primary component carriers for Cell 8 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC5 and the primary component carriers for Cell 10 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRP measurements between SCC5 and the primary component carriers for Cell 12 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.1.73FDD Intra frequency case for CA Idle Mode Measurements

## A.9.1.73.1Test Purpose and Environment

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.2B.2 for FDD intra frequency measurements.

## A.9.1.73.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Only absolute accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.1.2-1. In all test cases, Cell 1 is the serving cell and Cell 2 the target cell.

Table A.9.1.73.2-1: RSRP FDD Intra frequency test parameters

## A.9.1.73.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.2B.2.

## A.9.1.74FDD—FDD Inter frequency case for CA Idle Mode Measurements for overlapping carrier

## A.9.1.74.1Test Purpose and Environment

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3B.2 for FDD—FDD inter frequency measurements.

## A.9.1.74.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Absolute accuracy of RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.74.2-1. In all test cases, Cell 1 is the serving and Cell 2 the target cell.

Table A.9.1.74.2-1: RSRP FDD—FDD Inter frequency test parameters

## A.9.1.74.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3B.2.

## A.9.1.75FDD—FDD Inter frequency case for CA Idle Mode Measurements for non-overlapping carrier

## A.9.1.75.1Test Purpose and Environment

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.3B.3 for FDD—FDD inter frequency measurements.

## A.9.1.75.2Test parameters

In this set of test cases the cells are on different carrier frequencies. Absolute accuracy of RSRP inter-frequency measurements are tested by using the parameters in Table A.9.1.75.2-1. In all test cases, Cell 1 is the serving and Cell 2 the target cell.

Table A.9.1.75.2-1: RSRP FDD—FDD Inter frequency test parameters

## A.9.1.75.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.3B.3.

## A.9.1.76FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.76.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 for FD-FDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.76.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.76.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.76.2-1.

Table A.9.1.76.2-1: FD-FDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.76.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1.

## A.9.1.77HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.77.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 for HD-FDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.77.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.77.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.77.2-1.

Table A.9.1.77.2-1: HD-FDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.77.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1.

## A.9.1.78TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.9.1.78.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.1 for TDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeA.

## A.9.1.78.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.78.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.78.2-1.

Table A.9.1.78.2-1: TDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

## A.9.1.78.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.1.

## A.9.1.79FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.79.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 for FD-FDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.79.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.79.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.79.2-1.

Table A.9.1.79.2-1: FD-FDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.79.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3.

## A.9.1.80HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.80.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 for HD-FDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.80.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.80.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.80.2-1.

Table A.9.1.80.2-1: HD-FDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.80.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3.

## A.9.1.81TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB

## A.9.1.81.1Test Purpose and Environment

The purpose of this test is to verify that the RSS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21.3 for TDD intra frequency RSS based RSRP measurements for Cat-M1 UE in CEModeB.

## A.9.1.78.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Absolute accuracy of RSS based RSRP intra frequency measurements are tested by using the parameters in Table A.9.1.81.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

RSS measurement is enabled for intra-frequency measurement with MeasRSS-DedicatedConfig setup. RSS are transmitted by Cell 1 and Cell 2 in the same time and frequency resources with rss-ConfigCarrierInfo absent in MeasRSS-DedicatedConfig. Other RSS related parameters for Cell 1 and Cell 2 are defined in Table A.9.1.81.2-1.

Table A.9.1.81.2-1: TDD RSS based RSRP Intra frequency test parameters for Cat-M1 UE in CEModeB

## A.9.1.81.3Test Requirements

The RSS based RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21.3.

## A.9.2RSRQ

## A.9.2.1FDD Intra frequency case

## A.9.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.5.1.

## A.9.2.1.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.1.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.1.2-1: RSRQ FDD Intra frequency test parameters

## A.9.2.1.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in section 9.1.5.1. The RSRQ measurement accuracy for UE Category 1bis shall fulfil the requirements in section 9.1.5.5.

## A.9.2.2TDD Intra frequency case

## A.9.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.5.1.

## A.9.2.2.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.2.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.2.2-1: RSRQ TDD Intra frequency test parameters

## A.9.2.2.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in section 9.1.5.1. The RSRQ measurement accuracy for UE Category 1bis shall fulfil the requirements in section 9.1.5.5.

## A.9.2.3FDD—FDD Inter frequency case

## A.9.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6.1 and 9.1.6.2.

## A.9.2.3.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.3.2-1. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.3.2-1: RSRQ FDD—FDD Inter frequency test parameters

## A.9.2.3.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in sections 9.1.6.1 and 9.1.6.2. The RSRQ measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.6.5 and 9.1.6.6.

## A.9.2.4TDD—TDD Inter frequency case

## A.9.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6.1 and 9.1.6.2.

## A.9.2.4.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.4.2-1 for TDD configuration 1 and in Table A.9.2.4.2-2 for TDD configuration 0. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A 9.2.4.2-1: RSRQ TDD—TDD Inter frequency test parameters for TDD configuration 1

Table A 9.2.4.2-2: RSRQ TDD—TDD Inter frequency test parameters for TDD configuration 0

## A.9.2.4.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in sections 9.1.6.1 and 9.1.6.2. The RSRQ measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.6.5 and 9.1.6.6.

## A.9.2.4AFDD—TDD Inter frequency case

## A.9.2.4A.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6.1 and 9.1.6.2 for FDD—TDD inter frequency measurements.

## A.9.2.4A.2Test parameters

In this set of test cases the two cells are on different carrier frequencies. Both absolute and relative accuracy of RSRQ inter frequency measurements are tested by using the parameters in Table A.9.2.4A.2-1 and Table A.9.2.4A.2-2.  In all test cases, Cell 1 is the PCell and Cell 2 the target cell. Cell 1 is FDD cell and Cell 2 is TDD cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.2.4A.2-1: RSRQ FDD—TDD Inter frequency test parameters (FDD Cell1)

Table A.9.2.4A.2-2: RSRQ FDD—TDD Inter frequency test parameters (TDD cell2)

## A.9.2.4A.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in sections 9.1.6.1 and 9.1.6.2. The RSRQ measurement accuracy for UE Category 1bis shall fulfil the requirements in sections 9.1.6.5 and 9.1.6.6.

## A.9.2.5FDD RSRQ for E-UTRA Carrier Aggregation

## A.9.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.5.2Test parameters

In this test case the PCell and the SCell are on different carrier frequencies. There are three cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carrier are tested by using test parameters specified in Table A.9.2.5.2-1.  In the test, Cell 1 is the PCell, Cell 2 is the SCell on the Secondary Component Carrier (SCC) and Cell 3 is the neighbouring cell on the SCC. The SCC is configured and activated.

Table A.9.2.5.2-1: FDD RSRQ Carrier Aggregation test parameters

## A.9.2.5.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.6TDD RSRQ for E-UTRA Carrier Aggregation

The test case in this clause are applicable to carrier aggregation capable UEs which have been configured with a downlink Scell.

## A.9.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRQ measurement accuracy in carrier aggregation is within the specified limits in a synchronized network environment with AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier defined in Clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier defined in Clause 9.1.11.2, and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers defined in Clause 9.1.11.3.

## A.9.2.6.2Test parameters

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is PCell, Cell 2 is SCell, and Cell 3 is the target cell.  PCell and SCell are in different RF channels. Cell 3 is in the same RF channel as Cell 2. The parameters for the test are listed in Table A.9.2.6.2-1.

Table A.9.2.6.2-1: TDD RSRQ test parameters

## A.9.2.6.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in section 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.7FDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction is within the specified limits. This test will verify the requirements in Clause 9.1.5.2 for FDD intra frequency measurements under time domain measurement resource restriction.

## A.9.2.7.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurements under time domain measurement resource restriction is tested by using the parameters in Table A.9.2.7.2-1 and Table A.9.2.7.2-2 for non-MBSFN ABS with non-colliding CRS. In all test cases, Cell 1 is the serving cell and also the aggressor cell to Cell 2. Cell 2 is the target cell to be measured for RSRQ.

The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.2.7.2-1: General test parameters for E-UTRAN FDD RSRQ intra frequency test parameters under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.2.7.2-2: Cell-specific test parameters for E-UTRAN FDD RSRQ intra frequency test parameters under time domain measurement resource restriction with non-MBSFN ABS

## A.9.2.7.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.5.2.

## A.9.2.8TDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction is within the specified limits. This test will verify the requirements in Clause 9.1.5.2 for TDD intra frequency measurements under time domain measurement resource restriction.

## A.9.2.8.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurements under time domain measurement resource restriction is tested by using the parameters in Table A.9.2.8.2-1 and Table A.9.2.8.2-2 for non-MBSFN ABS with non-colliding CRS. In all test cases, Cell 1 is the serving cell and also the aggressor cell to Cell 2. Cell 2 is the target cell to be measured for RSRQ.

The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.2.8.2-1: General test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time domain measurement resource restriction with non-MBSFN ABS

Table A.9.2.8.2-2: Cell-specific test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time domain measurement resource restriction with non-MBSFN ABS

## A.9.2.8.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.5.2.

## A.9.2.9FDD RSRQ under Time Domain Measurement Resource Restriction with MBSFN ABS

## A.9.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction is within the specified limits under AWGN propagation conditions. This test will verify the absolute FDD RSRQ accuracy under time domain measurement resource restriction specified in Clause 9.1.5.2.

## A.9.2.9.2Test parameters

The test parameters are given in Tables A.9.2.9.2-1 and A.9.2.9.2-2 below. In this test case there are two cells on the same frequency used in this test case. In the test, Cell 1 is the serving cell and also the aggressor cell to Cell 2. Cell 2 is the target cell to be measured for RSRQ.

The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured by higher layers with a time domain measurement restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.2.9.2-1: General test parameters for FDD RSRQ under time domain measurement resource restriction with MBSFN ABS

Table A.9.2.9.2-2: Cell specific test parameters for FDD RSRQ under time domain measurement resource restriction with MBSFN ABS

## A.9.2.9.3Test Requirements

In the test, the RSRQ measurement accuracy under time domain measurement resource restriction shall fulfil the requirements in Clause 9.1.5.2

## A.9.2.10TDD Intra frequency case under time domain measurement resource restriction with MBSFN ABS

## A.9.2.10.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction is within the specified limits. This test will verify the requirements in Clause 9.1.5.2 for TDD intra frequency measurements under time domain measurement resource restriction.

## A.9.2.10.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurements under time domain measurement resource restriction is tested by using the parameters in Table A.9.2.10.2-1 and Table A.9.2.10.2-2 for MBSFN ABS with colliding CRS. In all test cases, Cell 1 is the serving cell and also the aggressor cell to Cell 2. Cell 2 is the target cell to be measured for RSRQ.

The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells and provided with a neighbour cell list associated with the pattern, where the cell list includes Cell 2. The UE is also configured with a time-domain measurement resource restriction pattern for the serving cell measurements. The information for both patterns shall be provided to the UE before the measurements start.

Table A.9.2.10.2-1: General test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time-domain measurement resource restriction with MBSFN ABS

Table A.9.2.10.2-2: Cell-specific test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time domain measurement resource restriction with MBSFN ABS

## A.9.2.10.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in clause 9.1.5.2.

## A.9.2.11FDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth)

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.11.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.5.1.

## A.9.2.11.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.5.2 except that the values of the parameters in the Table A.9.2.11.2-1 will replace the values of the corresponding parameters in A.9.2.5.2-1.

Table A.9.2.11.2-1: FDD RSRQ Carrier Aggregation test parameters

## A.9.2.11.3Test Requirements

The test requirements defined in section A.9.2.5.3 shall apply in this test case.

## A.9.2.12TDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth)

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.12.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.6.1.

## A.9.2.12.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.6.2 except that the values of the parameters in the Table A.9.2.12.2-1 will replace the values of the corresponding parameters in A.9.2.6.2-1.

Table A.9.2.12.2-1: TDD RSRQ Carrier Aggregation test parameters

## A.9.2.12.3Test Requirements

The test requirements defined in section A.9.2.6.3 shall apply in this test case.

## A.9.2.13Void

## A.9.2.13.1Void

## A.9.2.13.2Void

Table A.9.2.13.2-1: Void

## A.9.2.13.3Void

## A.9.2.14Void

## A.9.2.14.1Void

## A.9.2.14.2Void

Table A.9.2.14.2-1: Void

## A.9.2.14.3Void

## A.9.2.15FDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.2.15.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction with CRS assistance information is  within the specified limits. This test will verify the requirements in Clause 9.1.5.3 for FDD intra frequency measurements under time domain measurement resource restriction with CRS assistance information.

## A.9.2.15.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurements under time domain measurement resource restriction with CRS assistance information is tested by using the parameters in Table A.9.2.15.2-1 and Table A.9.2.15.2-2 for non-MBSFN ABS with colliding CRS between Cell1 and Cell3 and non-colliding CRS between Cell1 and Cell2. In all test cases, Cell 1 is the serving/aggressor cell, Cell2 is the neighbour/aggressor cell and Cell3 is the target cell to be measured for RSRQ.

The UE is configured by higher layers via Cell 1 with a time domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on neighbour cells, namely Cell 3 measurements with a neighbour cell list, where the cell list includes Cell 3. The UE is also provided via higher layers with the CRS assistance information of Cell 2. The information for both measurement pattern and the CRS assistance information shall be provided to the UE before the measurements start.

Note:It’s up to eNB’s implementation whether the time domain measurement resource restriction pattern for PCell measurements is configured or not.

Table A.9.2.15.2-1: General test parameters for E-UTRAN FDD RSRQ intra frequency test parameters under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.2.15.2-2: Cell-specific test parameters for E-UTRAN FDD RSRQ intra frequency test parameters under time domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

## A.9.2.15.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.5.3.

## A.9.2.16TDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.2.16.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy under time domain measurement resource restriction with CRS assistance information is  within the specified limits. This test will verify the requirements in Clause 9.1.5.3 for TDD intra frequency measurements under time domain measurement resource restriction with CRS assistance information.

## A.9.2.16.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurements under time domain measurement resource restriction with CRS assistance information is tested by using the parameters in Table A.9.2.16.2-1 and Table A.9.2.16.2-2 for non-MBSFN ABS with colliding CRS between Cell1 and Cell3 and non-colliding CRS between Cell1 and Cell2. In all test cases, Cell 1 is the serving/aggressor cell, Cell2 is the neighbour/aggressor cell and Cell3 is the target cell to be measured for RSRQ.

The UE is configured by higher layers  via Cell1 with a time domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on neighbour cells, namely Cell 3 measurements with a neighbour cell list, where the cell list includes Cell 3. The UE is also provided via higher layers with the CRS assistance information of Cell 2. The information for both measurement pattern and the CRS assistance information shall be provided to the UE before the measurements start.

Note:It’s up to eNB’s implementation whether the time domain measurement resource restriction pattern for PCell measurements is configured or not.

Table A.9.2.16.2-1: General test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.2.16.2-2: Cell-specific test parameters for E-UTRAN TDD RSRQ intra frequency test parameters under time domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

## A.9.2.16.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.5.3.

## A.9.2.17FDD Intra frequency case for 5 MHz bandwidth

## A.9.2.17.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.5.1.

## A.9.2.17.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.17.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.17.2-1: RSRQ FDD Intra frequency test parameters, 5MHz

## A.9.2.17.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.5.1.

## A.9.2.18FDD—FDD Inter frequency case for 5MHz bandwidth

## A.9.2.18.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6.1 and 9.1.6.2.

## A.9.2.18.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.18.2-1. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.18.2-1: RSRQ FDD—FDD Inter frequency test parameters, 5MHz

## A.9.2.18.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Sections 9.1.6.1 and 9.1.6.2.

## A.9.2.19FDD-FDD Inter Frequency WB-RSRQ

## A.9.2.19.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits when the measurement configuration message received by the UE contains widebandRSRQ-Meas parameter in TS 36.331 [2]. In the test the UE shall also be configured with the AllowedMeasBandwidth parameter defined in TS 36.331 [2]. The test shall verify the WB-RSRQ inter frequency absolute accuracy requirements defined in Section 9.1.6.3.

## A.9.2.19.2Test parameters

In this test case the two cells are on two different carrier frequencies and measurement gaps are provided. The WB-RSRQ inter frequency absolute accuracy requirement is tested by using test parameters in Table A.9.2.19.2-1. In the test, Cell 1 is the PCell and Cell 2 the target cell on which the UE shall be ordered to measure WB-RSRQ.

Table A.9.2.19.2-1: WB-RSRQ FDD-FDD Inter frequency test parameters

## A.9.2.19.3Test Requirements

The WB-RSRQ measurement accuracy for cell 2 shall fulfil the requirements in Section 9.1.6.3, compared with WB-RSRQ0. or WB-RSRQ1.

## A.9.2.20TDD—TDD Inter Frequency WB-RSRQ

## A.9.2.20.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits when the measurement configuration message received by the UE contains widebandRSRQ-Meas parameter in TS 36.331 [2]. In the test the UE shall also be configured with the AllowedMeasBandwidth parameter defined in TS 36.331 [2]. The test shall verify the WB-RSRQ inter frequency absolute accuracy requirements defined in Section 9.1.6.3.

## A.9.2.20.2Test parameters

In this test case the two cells are on two different carrier frequencies and measurement gaps are provided. The WB-RSRQ inter frequency absolute accuracy requirement is tested by using test parameters in Table A.9.2.20.2-1. In the test, Cell 1 is the PCell and Cell 2 the target cell on which the UE shall be ordered to measure WB-RSRQ.

Table A.9.2.20.2-1: WB-RSRQ TDD-TDD Inter frequency test parameters

## A.9.2.20.3Test Requirements

The WB-RSRQ measurement accuracy for cell 2 shall fulfil the requirements in Section 9.1.6.3, compared with WB-RSRQ0. or WB-RSRQ1.

## A.9.2.21FDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.21.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.5.1.

## A.9.2.21.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.5.2 except that the values of the parameters in the Table A.9.2.21.2-1 will replace the values of the corresponding parameters in A.9.2.5.2-1.

Table A.9.2.21.2-1: FDD RSRQ Carrier Aggregation test parameters

## A.9.2.21.3Test Requirements

The test requirements defined in section A.9.2.5.3 shall apply in this test case.

## A.9.2.22TDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.22.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.6.1.

## A.9.2.22.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.6.2 except that the values of the parameters in the Table A.9.2.22.2-1 will replace the values of the corresponding parameters in A.9.2.6.2-1.

Table A.9.2.22.2-1: TDD RSRQ Carrier Aggregation test parameters

## A.9.2.22.3Test Requirements

The test requirements defined in section A.9.2.6.3 shall apply in this test case.

## A.9.2.23FDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth)

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.23.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.5.1.

## A.9.2.23.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.5.2 except that the values of the parameters in the Table A.9.2.23.2-1 will replace the values of the corresponding parameters in A.9.2.5.2-1.

Table A.9.2.23.2-1: FDD RSRQ Carrier Aggregation test parameters

## A.9.2.23.3Test Requirements

The test requirements defined in section A.9.2.5.3 shall apply in this test case.

## A.9.2.24TDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth)

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.24.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.6.1.

## A.9.2.24.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.6.2 except that the values of the parameters in the Table A.9.2.24.2-1 will replace the values of the corresponding parameters in A.9.2.6.2-1.

Table A.9.2.24.2-1: TDD RSRQ Carrier Aggregation test parameters

## A.9.2.24.3Test Requirements

The test requirements defined in section A.9.2.6.3 shall apply in this test case.

## A.9.2.25RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD

The test case in this section are applicable to TDD-FDD carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.25.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of  RSRQ measurements for the primary component carrier defined in clause 9.1.11.1, the absolute accuracy of RSRQ measurements for the secondary component carrier defined in clause 9.1.11.2, and also the relative RSRQ accuracy requirement between primary and secondary component carriers defined in clause 9.1.11.3.

## A.9.2.25.2Test parameters

In this test case the PCell is FDD and SCell is TDD. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carrier are tested by using test parameters specified in Table A.9.2.25.2-1.  In the test, Cell 1 is the PCell, Cell 2 is the SCell on the Secondary Component Carrier (SCC). The SCC is configured and activated.

The parameters of this test are given in Table A.9.2.25.2-1.

Table A.9.2.25.2-1: RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD test parameters

## A.9.2.25.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.26RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD

The test case in this section are applicable to TDD-FDD carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.26.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD measurement accuracy in carrier aggregation is within the specified limits. This test will verify the absolute accuracy of RSRQ measurements for the primary component carrier defined in Clause 9.1.11.1, the absolute accuracy of RSRQ measurements for the secondary component carrier defined in Clause 9.1.11.2, and also the relative RSRQ accuracy requirement between primary and secondary component carriers defined in Clause 9.1.11.3.

## A.9.2.26.2Test parameters

In this test case the PCell is TDD and SCell is FDD. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carrier are tested by using test parameters specified in Table A.9.2.26.2-1.  In the test, Cell 1 is the PCell, Cell 2 is the SCell on the Secondary Component Carrier (SCC). The SCC is configured and activated.

The parameters of this test are given in Table A.9.2.26.2-1.

Table A.9.2.26.2-1: RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD test parameters

## A.9.2.26.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in section 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.27TDD RSRQ for E-UTRAN Carrier Aggregation for 20MHz+10MHz

The test case in this section are applicable to carrier aggregation capable UEs which have been configured with a downlink SCell.

## A.9.2.27.1Test Purpose and Environment

The purpose of this test is the same as defined in Subclause A.9.2.6.1.

## A.9.2.27.2Test parameters

The parameters of this test are the same as defined in Subclause A.9.2.6.2 except that the values of the parameters in the Table A.9.2.27.2-1 will replace the values of the corresponding parameters in A.9.2.6.2-1.

Table A.9.2.27.2-1: TDD RSRQ Carrier Aggregation test parameters

## A.9.2.27.3Test Requirements

The test requirements defined in section A.9.2.6.3 shall apply in this test case.

## A.9.2.28FDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal

## A.9.2.28.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.14.4.

## A.9.2.28.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement for Cell 2 is tested by using the parameters in Table A.9.2.28.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. Cell 2 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.28.2-1: RSRQ FDD Intra frequency test parameters

## A.9.2.28.3Test Requirements

The absolute accuracy of RSRQ intra frequency measurement for Cell 2 shall fulfil the requirements in Clause 9.1.14.4.

## A.9.2.29TDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal

## A.9.2.29.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.14.4.

## A.9.2.29.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement for Cell 2 is tested by using the parameters in Table A.9.2.29.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. Cell 2 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.29.2-1: RSRQ TDD Intra frequency test parameters

## A.9.2.29.3Test Requirements

The absolute accuracy of RSRQ intra frequency measurement for Cell 2 shall fulfil the requirements in Clause 9.1.14.4.

## A.9.2.30FDD-FDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal

## A.9.2.30.1Test Purpose and Environment

The purpose of this test is to verify that the absolute and relative accuracy of RSRQ measurement in discovery signal occasions is within the specified limits. This test will verify the requirements in Sections 9.1.14.4.

## A.9.2.30.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.30.2-1. In all tests, Cell 1 is the PCell and Cell 2 the target cell. For measurement of the carrier frequency of Cell 2, DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.30.2-1: RSRQ in discovery signal occasions FDD—FDD Inter frequency test parameters

## A.9.2.30.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Sections 9.1.14.4.

## A.9.2.31TDD-TDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal

## A.9.2.31.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in discovery signal occasions is within the specified limits. This test will verify the requirements in Sections 9.1.14.4.

## A.9.2.31.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.31.2-1 for TDD configuration 1. In all tests, Cell 1 is the PCell and Cell 2 the target cell. DMTC configuration for Cell 2 is provided to UE in the measDS-Config before the start of the test.

Table A 9.2.31.2-1: RSRQ TDD—TDD Inter frequency test parameters for TDD configuration 1

## A.9.2.31.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Sections 9.1.14.4.

## A.9.2.32FDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal

## A.9.2.32.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRQ measurement accuracy for carrier aggregation in CRS based discovery signal is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier specified in clause 9.1.15.1.2, and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.15.1.3.

## A.9.2.32.2Test parameters

In this test case the PCell and the SCell are on different carrier frequencies. There are three cells used in this test case. RSRQ absolute and relative accuracy requirements of the primary and secondary component carrier are tested by using test parameters specified in Table A.9.2.32.2-1.  In the test, Cell 1 is the PCell, Cell 2 is the SCell on the Secondary Component Carrier (SCC) and Cell 3 is the neighbouring cell on the SCC.  Cell 2 on SCC is configured and activated. Cell 3 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.32.2-1: FDD RSRQ Carrier Aggregation Test Parameters

## A.9.2.32.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.15.1.1, 9.1.15.1.2, and 9.1.15.1.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.15.1.2.

-The relative accuracy of inter-frequency RSRQ measurements between Cell 1 on primary component carriers and Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.15.1.3.

## A.9.2.33TDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal

## A.9.2.33.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRQ measurement accuracy for carrier aggregation in CRS based discovery signal is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier specified in clause 9.1.15.1.2, and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.15.1.3.

## A.9.2.33.2Test parameters

In this test case the PCell and the SCell are on different carrier frequencies. There are three cells used in this test case. RSRQ absolute and relative accuracy requirements of the primary and secondary component carrier are tested by using test parameters specified in Table A.9.2.33.2-1.  In the test, Cell 1 is the PCell, Cell 2 is the SCell on the Secondary Component Carrier (SCC) and Cell 3 is the neighbouring cell on the SCC.  Cell 2 on SCC is configured and activated. Cell 3 DMTC configuration is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.33.2-1: TDD RSRQ Carrier Aggregation Test Parameters

## A.9.2.33.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.15.1.1, 9.1.15.1.2, and 9.1.15.1.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.15.1.2.

-The relative accuracy of inter-frequency RSRQ measurements between Cell 1 on primary component carriers and Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.15.1.3.

## A.9.2.34FDD—FDD Inter frequency new RSRQ

## A.9.2.34.1Test Purpose and Environment

The purpose of this test is to verify that the absolute accuracy of RSRQ measurement is within the specified limits when measurement configuration message received by the UE contains measRSRQ-OnAllSymbols-r12 parameter in TS 36.331 [2]. This test will verify the requirements in Sections 9.1.16.

## A.9.2.34.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. The new RSRQ inter frequency absolute accuracy requirement is tested by using test parameters in Table A.9.2.34.2-1. In the test, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.34.2-1: New RSRQ FDD—FDD Inter frequency test parameters

## A.9.2.34.3Test Requirements

The new RSRQ measurement accuracy for cell 2 shall fulfil the requirements in Section 9.1.16, compared with any nominal new RSRQ value in subframe 0, 5 or others.

## A.9.2.35TDD—TDD Inter frequency new RSRQ

## A.9.2.35.1Test Purpose and Environment

The purpose of this test is to verify that the absolute accuracy of RSRQ measurement is within the specified limits when measurement configuration message received by the UE contains measRSRQ-OnAllSymbols-r12 parameter in TS 36.331 [2]. This test will verify the requirements in Sections 9.1.16.

## A.9.2.35.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. The new RSRQ inter frequency absolute accuracy requirement is tested by using test parameters in Table A.9.2.35.2-1. In the test, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.35.2-1: New RSRQ TDD—TDD Inter frequency test parameters

## A.9.2.35.3Test Requirements

The new RSRQ measurement accuracy for cell 2 shall fulfil the requirements in Section 9.1.16, compared with any nominal new RSRQ value in subframe 0, 5, 1, 6 or others.

## A.9.2.36FDD—FDD Inter frequency RSRQ measured on all OFDM symbols

## A.9.2.36.1Test Purpose and Environment

The purpose of this test is to verify that the absolute accuracy of RSRQ measurement is within the specified limits when measurement configuration message received by the UE contains measRSRQ-OnAllSymbols-r12 parameter in TS 36.331 [2]. This test will verify the requirements in Section 9.1.16.

A.9.2.3 is also conducted even if UE is capable of measuring RSRQ on all OFDM symbols.

## A.9.2.36.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ measured on all OFDM symbols inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.36.2-1. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.36.2-1: FDD—FDD Inter frequency test parameters

## A.9.2.36.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Section 9.1.16.

## A.9.2.37TDD—TDD Inter frequency RSRQ measurement on all OFDM symbols

## A.9.2.37.1Test Purpose and Environment

The purpose of this test is to verify that the absolute accuracy of RSRQ measurement is within the specified limits when measurement configuration message received by the UE contains measRSRQ-OnAllSymbols-r12 parameter in TS 36.331 [2]. This test will verify the requirements in Section 9.1.16.

A.9.2.4 is also conducted even if UE is capable of measuring RSRQ on all OFDM symbols..

## A.9.2.37.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RSRQ measured on all OFDM symbols inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.37.2-1. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.37.2-1: TDD-TDD Inter frequency test parameters

## A.9.2.37.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Section 9.1.16.

## A.9.2.383 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with two downlink SCells.

## A.9.2.38.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.38.2Test parameters

In this set of test cases there are three cells on three carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, and Cell 3 is activated SCell on channel 3. The parameters for the test are listed in Table A.9.2.38.2-1.

Table A.9.2.38.2-1: 3 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters (cell #1, cell #2 and cell #3)

## A.9.2.38.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.393 DL PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with two downlink SCells.

## A.9.2.39.1Test Purpose and Environment

The purpose of this test is to verify that the TDD-FDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier defined in Clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier defined in Clause 9.1.11.2, and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers defined in Clause 9.1.11.3.

## A.9.2.39.2Test parameters

In this set of cases cell 1 is PCell on the primary component carrier, and cell 2 and cell 3 are activated SCells on secondary component carriers SCC1 and SCC2 respectively. The test parameters for the test are listed in Table A.9.2.39.2-1.

Table A.9.2.39.2-1: 3 Downlink TDD-FDD RSRQ carrier aggregation test parameters with PCell in TDD (cell #1, cell #2 and cell #3)

## A.9.2.39.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.403 DL FDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.40.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.40.2Test parameters

In this test case the PCell and the SCells are on different carrier frequencies. There are three cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carriers are tested by using test parameters specified in Table A.9.2.40.2-1.  In the test, Cell 1 is the PCell, Cell 2 and Cell 3 are the SCells on secondary component carrier SCC1 and SCC2 respectively. The SCC1 and SCC2 are configured and activated.

Table A.9.2.40.2-1: 3 DL FDD RSRQ carrier aggregation test parameters

## A.9.2.40.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.413 DL TDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.41.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRQ measurement accuracy in carrier aggregation is within the specified limits in a synchronized network environment with AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier defined in Clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers defined in Clause 9.1.11.2, and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers defined in Clause 9.1.11.3.

## A.9.2.41.2Test parameters

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is PCell, Cell 2 and Cell 3 are the SCells on secondary component carrier SCC1 and SCC2 respectively.  PCell and SCells are in different RF channels. The parameters for the test are listed in Table A.9.2.41.2-1.

Table A.9.2.41.2-1: 3 DL TDD RSRQ carrier aggregation test parameters

## A.9.2.41.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in section 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.42FD-FDD RSRQ Intra frequency case for UE category 0

## A.9.2.42.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.13.3 for FD-FDD intra frequency RSRQ measurements for UE category 0.

## A.9.2.42.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.42.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.42.2-1: FD-FDD RSRQ Intra frequency test parameters for UE category 0

## A.9.2.42.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.13.3.

## A.9.2.43HD-FDD RSRQ Intra frequency case for UE category 0

## A.9.2.43.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.13.3 for HD-FDD intra frequency RSRQ measurements for UE category 0.

## A.9.2.43.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.43.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.43.2-1: HD-FDD RSRQ Intra frequency test parameters for UE category 0

## A.9.2.43.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.13.3.

## A.9.2.44TDD RSRQ Intra frequency case for UE category 0

## A.9.2.44.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.13.3 for TDD intra frequency RSRQ measurements for UE category 0.

## A.9.2.44.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.44.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.2.44.2-1: TDD RSRQ Intra frequency test parameters for UE category 0

## A.9.2.44.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in Clause 9.1.13.3.

## A.9.2.454 DL CA PCell in FDD FDD-TDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with three downlink SCells.

## A.9.2.45.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.45.2Test parameters

In this set of test cases there are four cells on four carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, and Cell 4 is activated SCell on channel 4. The parameters for the test are listed in Table A.9.2.45.2-1.

Table A.9.2.45.2-1: 4 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters (cell #1, cell #2, cell #3 and cell #4)

## A.9.2.45.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.464 DL CA PCell in TDD TDD-FDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with three downlink SCells.

## A.9.2.46.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.46.2Test parameters

In this set of test cases there are four cells on four carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, and Cell 4 is activated SCell on channel 4. The parameters for the test are listed in Table A.9.2.45.2-1.

Table A.9.2.46.2-1: 4 DL PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation test parameters (cell #1, cell #2, cell #3 and cell #4)

## A.9.2.46.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.475 DL FDD-TDD with PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with four downlink SCells.

## A.9.2.47.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.47.2Test parameters

In this set of test cases there are five cells on five carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, Cell 4 is activated SCell on channel 4, and Cell 5 is activated SCell on channel 5. The parameters for the test are listed in Table A.9.2.45.2-1.

Table A.9.2.47.2-1: 5 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters (cell #1, cell #2, cell #3, cell #4 and cell#5)

## A.9.2.47.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 5 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.485 DL FDD-TDD with PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation

The test case in this clause is applicable to carrier aggregation capable UEs which have been configured with four downlink SCells.

## A.9.2.48.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.48.2Test parameters

In this set of test cases there are five cells on five carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, Cell 4 is activated SCell on channel 4, and Cell 5 is activated SCell on channel 5. The parameters for the test are listed in Table A.9.2.45.2-1.

Table A.9.2.48.2-1: 5 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters (cell #1, cell #2, cell #3, cell #4 and cell#5)

## A.9.2.48.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 5 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.495 DL FDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.49.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.49.2Test parameters

In this set of test cases the PCell and the SCells are on different carrier frequencies. There are five cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carriers are tested by using test parameters specified in Table A.9.2.49.2-1 and Table A.9.2.49.2-2.  In the test, Cell 1 is the PCell, Cell 2, Cell 3, Cell 4 and Cell 5 are the SCells on secondary component carrier SCC1, SCC2, SCC3 and SCC4 respectively. The SCC1, SCC2, SCC3 and SCC4 are configured and activated.

Table A.9.2.49.2-1: 5 DL FDD RSRQ carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.2.49.2-2: 5 DL FDD RSRQ carrier aggregation test parameters for cell 4 and cell 5

## A.9.2.49.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC3 for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC4 for Cell 5 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.505 DL TDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.50.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.50.2Test parameters

In this set of test cases the PCell and the SCells are on different carrier frequencies. There are five cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carriers are tested by using test parameters specified in Table A.9.2.50.2-1 and Table A.9.2.50.2-2.  In the test, Cell 1 is the PCell, Cell 2, Cell 3, Cell 4 and Cell 5 are the SCells on secondary component carrier SCC1, SCC2, SCC3 and SCC4 respectively. The SCC1, SCC2, SCC3 and SCC4 are configured and activated.

Table A.9.2.50.2-1: 5 DL TDD RSRQ carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.2.50.2-2: 5 DL TDD RSRQ carrier aggregation test parameters for cell 4 and cell 5

## A.9.2.50.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on SCC4 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC3 for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC4 for Cell 5 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.51FS3 Intra frequency absolute and relative RSRQ accuracies with FDD PCell

## A.9.2.51.1Test Purpose and Environment

The purpose of this test is to verify that the FDD intra frequency RSRQ absolute and relative measurement accuracies in carrier aggregation with frame structure 3 in the configured DMTC occasion are within the specified limits. This test will verify the absolute RSRQ accuracy requirement of the secondary component carrier defined in clause 9.1.19.2. The test will also verify the primary and secondary component carrier relative RSRQ accuracy requirement defined in Clause 9.1.19.4.

## A.9.2.51.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier with frame structure 3 and activated, and Cell3 is the neighboring cell on the same secondary component carrier of Cell2. The test parameters are given in Table A.9.2.51.2-1. The DMTC configuration for Cell2 and Cell3 is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.51.2-1: Test parameters for FDD RSRQ accuracies of Scell with FS3

## A.9.2.51.3Test Requirements

In the test, the performance of RSRQ measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency RSRQ measurements for Cell 3 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.19.4.

## A.9.2.52FS3 Intra frequency absolute and relative RSRQ accuracies with TDD PCell

## A.9.2.52.1Test Purpose and Environment

The purpose of this test is to verify that the TDD intra frequency RSRQ absolute and relative measurement accuracies in carrier aggregation with frame structure 3 in the configured DMTC occasion are within the specified limits. This test will verify the absolute RSRQ accuracy requirement of the secondary component carrier defined in clause 9.1.19.2. The test will also verify the primary and secondary component carrier relative RSRQ accuracy requirement defined in Clause 9.1.19.4.

## A.9.2.52.2Test parameters

In this test case, Cell1 is PCell on the primary component carrier, Cell2 is SCell on the secondary component carrier with frame structure 3 and activated, and Cell3 is the neighboring cell on the same secondary component carrier of Cell2. The test parameters are given in Table A.9.2.52.2-1. The DMTC configuration for Cell2 and Cell3 is provided to the UE in the measDS-Config before the start of the test.

Table A.9.2.52.2-1: Test parameters for FDD RSRQ accuracies of Scell with FS3

## A.9.2.52.3Test Requirements

In the test, the performance of RSRQ measurements is verified from following three perspectives:

-The absolute accuracy of intra-frequency RSRQ measurements for Cell 3 on the secondary component carrier with frame structure 3 shall fulfil the requirements defined in clause 9.1.19.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.19.4.

## A.9.2.534DL FDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.53.1Test Purpose and Environment

The purpose of this test is to verify that the FDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.53.2Test parameters

In this set of test cases the PCell and the SCells are on different carrier frequencies. There are five cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carriers are tested by using test parameters specified in Table A.9.2.53.2-1 and Table A.9.2.53.2-2.  In the test, Cell 1 is the PCell, Cell 2, Cell 3 and Cell 4 are the SCells on secondary component carrier SCC1, SCC2 and SCC3 respectively. The SCC1, SCC2 and SCC3 are configured and activated.

Table A.9.2.53.2-1: 4 DL FDD RSRQ carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.2.53.2-2: 4 DL FDD RSRQ carrier aggregation test parameters for cell 4

## A.9.2.53.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC3 for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.544DL TDD RSRQ for E-UTRAN in Carrier Aggregation

## A.9.2.54.1Test Purpose and Environment

The purpose of this test is to verify that the TDD RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.54.2Test parameters

In this set of test cases the PCell and the SCells are on different carrier frequencies. There are five cells used in this test case. Both RSRQ absolute and relative accuracy requirements of the primary and secondary component carriers are tested by using test parameters specified in Table A.9.2.54.2-1 and Table A.9.2.54.2-2.  In the test, Cell 1 is the PCell, Cell 2, Cell 3 and Cell 4 are the SCells on secondary component carrier SCC1, SCC2 and SCC3 respectively. The SCC1, SCC2 and SCC3 are configured and activated.

Table A.9.2.54.2-1: 4 DL TDD RSRQ carrier aggregation test parameters for cell 1, cell 2 and cell 3

Table A.9.2.54.2-2: 4 DL TDD RSRQ carrier aggregation test parameters for cell 4

## A.9.2.54.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements defined in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on SCC1 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on SCC2 shall fulfil the requirements defined in clause 9.1.11.2.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on SCC3 shall fulfil the requirements defined in clause 9.1.11.2.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC1 for Cell 2 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC2 for Cell 3 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary component carrier and SCC3 for Cell 4 relative to Cell 1 shall fulfil the requirements defined in clause 9.1.11.3.

## A.9.2.553 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.2.55.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carrier specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.2.38, A.9.2.39, A.9.2.40, A.9.2.41, does not need to be tested in the generic duplex-mode test case A.9.2.55.

## A.9.2.55.2Test parameters

In this set of test cases there are three cells on three carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, and Cell 3 is activated SCell on channel 3. The parameters for the test are listed in Table A.9.2.55.2-1.

Table A.9.2.55.2-1: 3 DL RSRQ for E-UTRAN in Carrier Aggregation test parameters

## A.9.2.55.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.564 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.2.56.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.2.45, A.9.2.46, A.9.2.53 A.9.2.54, does not need to be tested in the generic duplex-mode test case A.9.2.56.

## A.9.2.56.2Test parameters

In this set of test cases there are four cells on four carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, and Cell 4 is activated SCell on channel 4. The parameters for the test are listed in Table A.9.2.56.2-1.

Table A.9.2.56.2-1: 4 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters

## A.9.2.56.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.575 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.2.57.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

Note on the applicability: the requirement tested in the specific duplex-mode test cases A.9.2.47, A.9.2.48, A.9.2.49 A.9.2.50, does not need to be tested in the generic duplex-mode test case A.9.2.57.

## A.9.2.57.2Test parameters

In this set of test cases there are five cells on five carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, Cell 4 is activated SCell on channel 4, and Cell 5 is activated SCell on channel 5. The parameters for the test are listed in Table A.9.2.57.2-1.

Table A.9.2.57.2-1: 5 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation test parameters

## A.9.2.57.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 5 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.586 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.2.58.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.58.2Test parameters

In this set of test cases there are six cells on six carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, Cell 4 is activated SCell on channel 4, Cell 5 is activated SCell on channel 5 and Cell 6 is activated SCell on channel 6. The parameters for the test are listed in Table A.9.2.58.2-1.

Table A.9.2.58.2-1: 6 DL RSRQ for E-UTRAN in Carrier Aggregation test parameters

## A.9.2.58.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 6 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 5 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.597 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes

## A.9.2.59.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy in carrier aggregation is within the specified limits under AWGN propagation conditions. This test will verify the absolute accuracy of intra-frequency RSRQ measurements for the primary component carrier specified in clause 9.1.11.1, the absolute accuracy of intra-frequency RSRQ measurements for the secondary component carriers specified in clause 9.1.11.2 and also the relative inter-frequency RSRQ accuracy requirement between primary and secondary component carriers specified in clause 9.1.11.3.

## A.9.2.59.2Test parameters

In this set of test cases there are seven cells on seven carrier frequencies. Cell 1 is PCell on channel 1, Cell 2 is activated SCell on channel 2, Cell 3 is activated SCell on channel 3, Cell 4 is activated SCell on channel 4, Cell 5 is activated SCell on channel 5, Cell 6 is activated SCell on channel 6 and Cell 7 is activated SCell on channel 7. The parameters for the test are listed in Table A.9.2.59.2-1.

Table A.9.2.59.2-1: 7 DL RSRQ for E-UTRAN in Carrier Aggregation test parameters

## A.9.2.59.3Test Requirements

In the test, the RSRQ measurement accuracy in carrier aggregation shall fulfil the requirements in clause 9.1.11.1, 9.1.11.2, and 9.1.11.3.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 1 on the primary component carrier shall fulfil the requirements specified in clause 9.1.11.1.

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 2 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 3 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 4 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 5 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 6 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The absolute accuracy of intra-frequency RSRQ measurements of Cell 7 on the secondary component carrier shall fulfil the requirements specified in clause 9.1.11.2

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 2 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 3 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 4 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 5 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 6 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

-The relative accuracy of inter-frequency RSRQ measurements between the primary and secondary component carriers for Cell 7 relative to Cell 1 shall fulfil the requirements specified in clause 9.1.11.3.

## A.9.2.60FDD Intra frequency case for CA Idle Mode Measurements

## A.9.2.60.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.5B.2.

## A.9.2.60.2Test parameters

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

In this test case all cells are on the same carrier frequency. The absolute accuracy of RSRQ intra frequency measurement is tested by using the parameters in Table A.9.2.60.2-1. In all test cases, Cell 1 is the serving and Cell 2 the target cell.

Table A.9.2.60.2-1: RSRQ FDD Intra frequency test parameters

## A.9.2.60.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in section 9.1.5B.2.

## A.9.2.61FDD—FDD Inter frequency case for CA Idle Mode Measurements on overlapping carrier

## A.9.2.61.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6B.2.

## A.9.2.61.2Test parameters

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

In this test case the two cells are on different carrier frequencies. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.61.2-1. In all tests, Cell 1 is the serving cell and Cell 2 the target cell.

Table A.9.2.61.2-1: RSRQ FDD—FDD Inter frequency test parameters

## A.9.2.61.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in sections 9.1.6B.2.

## A.9.2.62FDD—FDD Inter frequency case for CA Idle Mode Measurements on non-overlapping carrier

## A.9.2.62.1Test Purpose and Environment

The purpose of this test is to verify that the RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.6B.3.

## A.9.2.62.2Test parameters

The requirements in this clause are applicable for a UE:

- in state RRC_IDLE

- that is synchronised to the cell that is measured.

The requirements apply for UE supporting ca-IdleModeMeasurements, when configured with measIdleConfig and while T331 timer is running.

In this test case the two cells are on different carrier frequencies. Both RSRQ inter frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.2.62.2-1. In all tests, Cell 1 is the serving cell and Cell 2 the target cell.

Table A.9.2.62.2-1: RSRQ FDD—FDD Inter frequency test parameters

## A.9.2.62.3Test Requirements

The RSRQ measurement accuracy shall fulfil the requirements in sections 9.1.6B.3.

## A.9.3UTRAN FDD CPICH RSCP

## A.9.3.1E-UTRAN FDD

## A.9.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the CPICH RSCP absolute measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.2.1. There are two different test setups with different UTRAN parameters.

## A.9.3.1.2Parameters

The test parameters are given in Tables A.9.3.1.2-1, A.9.3.1.2-2 and A.9.3.1.2-3 below.

Table A.9.3.1.2-1: General test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN FDD

Table A.9.3.1.2-2: E-UTRAN FDD cell specific test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN FDD

Table A.9.3.1.2-3: UTRAN FDD cell specific test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN FDD

## A.9.3.1.3Test Requirements

The CPICH RSCP measurement absolute accuracy shall meet the requirements in Clause 9.2.1.

## A.9.3.2 E-UTRAN TDD

## A.9.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the CPICH RSCP absolute measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.2.1. There are three different test setups with different UTRAN parameters.

## A.9.3.2.2Parameters

The test parameters are given in Tables A.9.3.2.2-1, A.9.3.2.2-2 and A.9.3.2.2-3 below.

Table A.9.3.2.2-1: General test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN TDD

Table A.9.3.2.2-2: E-UTRAN TDD cell specific test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN TDD

Table A.9.3.2.2-3: UTRAN FDD cell specific test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN TDD

## A.9.3.2.3Test Requirements

The CPICH RSCP measurement absolute accuracy shall meet the requirements in Clause 9.2.1.

## A.9.3.3E-UTRAN FDD for 5MHz Bandwidth

## A.9.3.3.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.3.1.1.

## A.9.3.3.2Parameters

The parameters of this test are the same as defined in Subclause A.9.3.1.2 except that the values of the parameters in the Table A.9.3.3.2-1 will replace the values of the corresponding parameters in A.9.3.1.2-1, and the values of E-UTRAN FDD cell specific parameters in the Table A.9.3.3.2-2 shall be adopted, and the values of UTRA FDD cell specific parameters shall be reused as defined in Table A.9.3.1.2-3 of Subclause A.9.3.1.2.

Table A.9.3.3.2-1: General test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN FDD for 5MHz bandwidth

Table A.9.3.3.2-2: E-UTRAN FDD cell specific test parameters for UTRAN FDD CPICH RSCP absolute measurement accuracy test in E-UTRAN FDD for 5MHz bandwidth

## A.9.3.3.3Test Requirements

The test requirements defined in section A.9.3.1.3 shall apply to this test case.

## A.9.4UTRAN FDD CPICH Ec/No

## A.9.4.1E-UTRAN FDD

## A.9.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the CPICH Ec/No absolute measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.2.3. There are three different test setups with different UTRAN parameters.

## A.9.4.1.2Parameters

The test parameters are given in Tables A.9.4.1.2-1, A.9.4.1.2-2 and A.9.4.1.2-3 below.

Table A.9.4.1.2-1: General test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN FDD

Table A.9.4.1.2-2: E-UTRAN FDD cell specific test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN FDD

Table A.9.4.1.2-3: UTRAN FDD cell specific test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN FDD

## A.9.4.1.3Test Requirements

The CPICH Ec/No measurement absolute accuracy shall meet the requirements in Clause 9.2.3.

The effect of assumed thermal noise and noise generated in the receiver (-99 dBm for frequency bands I, IV, VI, X, XI, XIX and XXI; -98 dBm for frequency band IX, -97dBm for frequency bands II, V and VII; -95.5dBm for frequency band XXV and XXVI; and -96dBm for frequency band III) shall be added into the required accuracy. The test requirements for the absolute CPICH_Ec/Io measurement are shown in Table A.9.4.1.3-1.

Table A.9.4.1.3-1: CPICH_Ec/Io absolute accuracy

## A.9.4.2E-UTRAN TDD

## A.9.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the CPICH Ec/No absolute measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.2.3. There are three different test setups with different UTRAN parameters.

## A.9.4.2.2Parameters

The test parameters are given in Tables A.9.4.2.2-1, A.9.4.2.2-2 and A.9.4.2.2-3 below.

Table A.9.4.2.2-1: General test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN TDD

Table A.9.4.2.2-2: E-UTRAN TDD cell specific test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN TDD

Table A.9.4.2.2-3: UTRAN FDD cell specific test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN TDD

## A.9.4.2.3Test Requirements

The CPICH Ec/No measurement absolute accuracy shall meet the requirements in Clause 9.2.3.

The effect of assumed thermal noise and noise generated in the receiver (-99 dBm for frequency bands I, IV, VI, X, XI, XIX and XXI; -98 dBm for frequency band IX, -97dBm for frequency bands II, V and VII; -95.5dBm for frequency band XXV and XXVI; and -96dBm for frequency band III) shall be added into the required accuracy. The test requirements for the absolute CPICH_Ec/Io measurement are shown in Table A.9.4.2.3-1.

Table A.9.4.2.3-1: CPICH_Ec/Io absolute accuracy

## A.9.4.3E-UTRAN FDD for 5MHz Bandwidth

## A.9.4.3.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.4.1.1.

## A.9.4.3.2Parameters

The parameters of this test are the same as defined in Subclause A.9.4.1.2 except that the values of the parameters in the Table A.9.4.3.2-1 will replace the values of the corresponding parameters in A.9.4.1.2-1, and the values of E-UTRAN FDD cell specific parameters in the Table A.9.4.3.2-2 shall be adopted, and the values of UTRA FDD cell specific parameters shall be reused as defined in Table A.9.4.1.2-3 of Subclause A.9.4.1.2.

Table A.9.4.3.2-1: General test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN FDD for 5MHz bandwidth

Table A.9.4.3.2-2: E-UTRAN FDD cell specific test parameters for UTRAN FDD CPICH Ec/No absolute measurement accuracy test in E-UTRAN FDD for 5MHz bandwidth

## A.9.4.3.3Test Requirements

The test requirements defined in section A.9.4.1.3 shall apply to this test case.

## A.9.5UTRAN TDD measurement

## A.9.5.1P-CCPCH RSCP absolute accuracy for E-UTRAN FDD

## A.9.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UTRAN TDD P-CCPCH RSCP measurement absolute accuracy is within the specified limits. This test will verify the requirements in clause 9.3.1 and applies to UE supporting this capability.

Gap pattern configuration with id #1 as specified in Table 8.1.2.1-1 is provided. In the measurement control information it is indicated to the UE that periodic reporting of the UTRA TDD P-CCPCH RSRP measurement is used.

## A.9.5.1.2Test parameters

In this set of test cases there are two cells. Cell 1 is a E-UTRA FDD cell and cell 2 is a UTRA TDD cell. The absolute accuracy of P-CCPCH RSCP measurements are tested by using test parameters in Table A.9.5.1-1, Table A.9.5.1-2, and Table A.9.5.1-3. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.9.5.1-1: General test parameters for UTRA TDD P-CCPCH RSCP measurement absolute accuracy in E-UTRAN FDD

Table A.9.5.1-2: UTRA TDD P-CCPCH RSCP measurement tests parameters (cell 1)

Table A.9.5.1-3: UTRA TDD P-CCPCH RSCP measurement tests parameters (cell 2)

## A.9.5.1.3Test Requirements

The UTRA TDD P-CCPCH RSCP measurement accuracy shall meet the requirements in clause 9.3.1.

## A.9.5.2P-CCPCH RSCP absolute accuracy for E-UTRAN TDD

## A.9.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UTRAN TDD P-CCPCH RSCP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.3.1 and applies to UE supporting this capability.

Gap pattern configuration with id #1 as specified in Table 8.1.2.1-1 is provided. In the measurement control information it is indicated to the UE that periodic reporting of the UTRA TDD P-CCPCH RSRP measurement is used.

## A.9.5.2.2Test parameters

In this set of test cases there are two cells. Cell 1 is a E-UTRA TDD cell and cell 2 is a UTRA TDD cell. The absolute accuracy of P-CCPCH RSCP measurements are tested by using test parameters in Table A.9.5.2-1, Table A.9.5.2-2, and Table A.9.5.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.9.5.2-1: General test parameters for UTRA TDD P-CCPCH RSCP measurement

Table A.9.5.2-2: UTRA TDD P-CCPCH RSCP measurement tests parameters (cell 1)

Table A.9.5.2-3: UTRA TDD P-CCPCH RSCP measurement tests parameters (cell 2)

## A.9.5.2.3Test Requirements

The UTRA TDD P-CCPCH RSCP measurement accuracy shall meet the requirements in clause 9.3.1.

## A.9.6GSM Carrier RSSI

## A.9.6.1E-UTRAN FDD

## A.9.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the GSM Carrier RSSI measurement accuracy is within the specified limits when the active cell is E-UTRAN FDD. This test will verify the requirements in clause 9.4.1. There are 12 different test setups with different signal levels for the GSM cells.

Measurement gaps are configured to measure on the GSM cells. Table A.9.6.1.1-2 defines the cell specific test parameters for the E-UTRAN FDD cell. In the measurement control information it is indicated to the UE that periodic reporting of the GSM RSSI measurement is used. The limits of the GSM test parameters in terms of GSM BCCH received level at the receiver inputs are defined in Table A.9.6.1.1-3.

Table A.9.6.1.1-1: General GSM Carrier RSSI test parameters

Table A.9.6.1.1.-2: E-UTRAN FDD Cell specific test parameters for GSM Carrier RSSI accuracy test in E-UTRAN FDD

Table A.9.6.1.1-3: BCCH signal levels at receiver input in dBm

## A.9.6.1.2Test Requirements

The GSM Carrier RSSI measurement accuracy shall meet the requirements in clause 9.4.1.

## A.9.6.2E-UTRAN TDD

## A.9.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the GSM Carrier RSSI measurement accuracy is within the specified limits when the active cell is E-UTRAN TDD. This test will verify the requirements in clause 9.4.1. There are 12 different test setups with different signal levels for the GSM cells.

Measurement gaps are configured to measure on the GSM cells. Table A.9.6.2.1-2 defines the cell specific test parameters for the E-UTRAN TDD cell. In the measurement control information it is indicated to the UE that periodic reporting of the GSM RSSI measurement is used. The limits of the GSM test parameters in terms of GSM BCCH received level at the receiver inputs are defined in Table A.9.6.2.1-3.

Table A.9.6.2.1-1: General GSM Carrier RSSI test parameters

Table A.9.6.2.1-2: E-UTRAN TDD Cell specific test parameters for GSM Carrier RSSI accuracy test in E-UTRAN TDD

Table A.9.6.2.1-3: BCCH signal levels at receiver input in dBm

## A.9.6.2.2Test Requirements

The GSM Carrier RSSI measurement accuracy shall meet the requirements in clause 9.4.1.

## A.9.7UE Rx – Tx Time Difference

## A.9.7.1E-UTRAN FDD UE Rx – Tx time difference case

## A.9.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN FDD UE Rx – Tx time difference measurement accuracy is within the specified limits in Clause 9.1.9.

There is only one active cell in the test. The tested UE is connected with the PCell, configured to transmit SRS signals periodically, and signaled to report UE Rx – Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE.

## A.9.7.1.2Test parameters

The parameters for this test case are defined in Table A.9.7.1.2-1, and the SRS configuration used is defined in Table A.9.7.1.2-2.

Table A.9.7.1.2-1: FDD UE Rx – Tx time difference test parameters

Table A.9.7.1.2-2: Sounding Reference Symbol Configuration to be used in FDD UE Rx – Tx time difference test

## A.9.7.1.3Test Requirements

The UE Rx – Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.9.1.

## A.9.7.2E-UTRA TDD UE Rx – Tx time difference case

## A.9.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN TDD UE Rx-Tx time difference measurement accuracy is within the specified limits in clause 9.1.9.

There is only one cell in the test. The tested UE is connected with the PCell, configured to transmit SRS signals periodcally, and signaled to report UE Rx – Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx – Tx measurement reported by the UE.

## A.9.7.2.2Test parameters

The parameters for this test case are defined in Table A.9.7.2.2-1, and the SRS configuration used is defined in Table A.9.7.2.2-2.

Table A.9.7.2.2-1: Cell specific test parameters for UE Rx-Tx time difference measurement

Table A.9.7.2.2-2: Sounding Reference Symbol Configuration to be used in TDD UE Rx – Tx time difference test

## A.9.7.2.3Test Requirements

The UE Rx – Tx time difference measurement accuracy shall fulfill the requirements in clause 9.1.9.1.

## A.9.7.3E-UTRAN FDD UE Rx–Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.7.3.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN FDD UE Rx–Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.9.3 when time-domain measurement resource restriction is configured for PCell measurements via higher-layer signalling [2] and non-MBSFN ABS are configured in the interfering cell.

## A.9.7.3.2Test parameters

In this test case, there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. Cell 1 is the PCell on which UE Rx-Tx is measured, and Cell 2 is the interfering cell. Non-MBSFN ABS pattern is configured in Cell 2 during the entire test.

The tested UE is connected to the PCell and configured to transmit SRS signals periodically. The SRS configuration is provided to the UE before the measurement starts. The UE is configured to report UE Rx–Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on PCell. The information for both patterns shall be provided to the UE before the measurement starts.

The general and cell-specific parameters for this test case are defined in Table A.9.7.3.2-1 and Table A.9.7.3.2-2, respectively, and the SRS configuration used is specified in Table A.9.7.3.2-3.

Table A.9.7.3.2-1: General test parameters for FDD UE Rx–Tx time difference measurement under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.7.3.2-2: Cell-specific test parameters for FDD UE Rx–Tx time difference measurement under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.7.3.2-3: Sounding Reference Symbol Configuration to be used in FDD UE Rx–Tx time difference test

## A.9.7.3.3Test Requirements

The UE Rx–Tx time difference measurement accuracy shall fulfill the requirements in Section 9.1.9.3.

## A.9.7.4E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.9.7.4.1Test Purpose and Environment

The purpose of this test is to verify that the TDD UE Rx-Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.9.3 when time-domain measurement resource restriction is configured for PCell measurements via higher-layer signalling [2] and non-MBSFN ABS are configured in the interfering cell.

## A.9.7.4.2Test Parameters

In the test, there are two synchronous cells, Cell 1 and Cell 2, on the same RF channel. Cell 1 is the PCell on which UE Rx-Tx is measured, and Cell 2 is the interfering cell. Non-MBSFN ABS pattern is configured in Cell 2 during the entire test.

The tested UE is connected to the PCell and configured to transmit SRS signals periodically. The SRS configuration is provided to the UE before the measurement starts. The UE is configured to report UE Rx–Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD UE Rx-Tx time difference measurements on PCell. The information for both patterns shall be provided to the UE before the measurement starts.

The general and cell-specific parameters for this test case are defined in Table A.9.7.4.2-1 and Table A.9.7.4.2-2, respectively, and the SRS configuration used is defined in Table A.9.7.4.2-3.

Table A.9.7.4.2-1: General test parameters for E-UTRAN TDD UE Rx-Tx time difference measurement under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.7.4.2-2: Cell-specific test parameters for E-UTRAN TDD UE Rx-Tx time difference measurement under time-domain measurement resource restriction with non-MBSFN ABS

Table A.9.7.4.2-3: Sounding Reference Symbol Configuration to be used in TDD UE Rx–Tx time difference test

## A.9.7.4.3Test Requirements

The UE Rx–Tx time difference measurement accuracy shall fulfill the requirements in Section 9.1.9.3.

## A.9.7.5E-UTRAN FDD UE Rx–Tx time difference under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.7.5.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN FDD UE Rx–Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.9.4 when the UE is provided with a time-domain measurement resource restriction pattern and CRS assistance information, and when non-MBSFN ABS configured in the interfering cells.

## A.9.7.5.2Test parameters

In this test case, there are three synchronous cells, Cell 1, Cell 2 and Cell 3, on the same RF channel. Cell 1 is the PCell on which UE Rx-Tx is measured. Cell 2 and Cell 3 are the interfering cells. A non-MBSFN ABS pattern is configured in each of the Cell 2 and Cell 3 during the entire test.

The tested UE is connected to the PCell and configured to transmit SRS signals periodically. The SRS configuration is provided to the UE before the measurement starts. The UE is configured to report UE Rx–Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN FDD intra-frequency measurements on PCell. The UE is also provided via higher layers with the CRS assistance information for Cell 2. The information for both measurement patterns and the CRS assistance information shall be provided via RRC to the UE before the measurement starts.

The general and cell-specific parameters for this test case are defined in Table A.9.7.5.2-1 and Table A.9.7.5.2-2, respectively, and the SRS configuration used is specified in Table A.9.7.5.2-3.

Table A.9.7.5.2-1: General test parameters for FDD UE Rx–Tx time difference measurement under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.7.5.2-2: Cell-specific test parameters for FDD UE Rx–Tx time difference measurement under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.7.5.2-3: Sounding Reference Symbol Configuration to be used in FDD UE Rx–Tx time difference test

## A.9.7.5.3Test Requirements

The UE Rx–Tx time difference measurement accuracy shall fulfill the requirements in Section 9.1.9.4.

## A.9.7.6E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.9.7.6.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN TDD UE Rx–Tx time difference measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.9.4 when the UE is provided with a time-domain measurement resource restriction pattern and CRS assistance information, and when non-MBSFN ABS configured in the interfering cells.

## A.9.7.6.2Test Parameters

In this test case, there are three synchronous cells, Cell 1, Cell 2 and Cell 3, on the same RF channel. Cell 1 is the PCell on which UE Rx-Tx is measured. Cell 2 and Cell 3 are the interfering cells. A non-MBSFN ABS pattern is configured in each of the Cell 2 and Cell 3 during the entire test.

The tested UE is connected to the PCell and configured to transmit SRS signals periodically. The SRS configuration is provided to the UE before the measurement starts. The UE is configured to report UE Rx–Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE. The UE is configured by higher layers via Cell 1 with a time-domain measurement resource restriction pattern for performing E-UTRAN TDD intra-frequency measurements on PCell. The UE is also provided via higher layers with the CRS assistance information for Cell 2. The information for both measurement patterns and the CRS assistance information shall be provided via RRC to the UE before the measurement starts.

The general and cell-specific parameters for this test case are defined in Table A.9.7.6.2-1 and Table A.9.7.6.2-2, respectively, and the SRS configuration used is specified in Table A.9.7.6.2-3.

Table A.9.7.6.2-1: General test parameters for E-UTRAN TDD UE Rx-Tx time difference measurement under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.7.6.2-2: Cell-specific test parameters for E-UTRAN TDD UE Rx-Tx time difference measurement under time-domain measurement resource restriction with CRS assistance information and non-MBSFN ABS

Table A.9.7.6.2-3: Sounding Reference Symbol Configuration to be used in TDD UE Rx–Tx time difference test

## A.9.7.6.3Test Requirements

The UE Rx–Tx time difference measurement accuracy shall fulfill the requirements in Section 9.1.9.4.

## A.9.7.7E-UTRAN FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA

## A.9.7.7.1Test Purpose and Environment

The purpose of this test is to verify that Cat-M1 and Cat-M2 UE can meet the E-UTRAN FDD UE Rx-Tx time difference measurement accuracy requirements. Requirements for Cat-M1 UE is specified in Clause 9.1.21.21 and requirements for Cat-M2 UE is specified in Clause 9.1.25.25.

There is only one active cell in the test. The tested UE is connected with the PCell, configured to transmit SRS signals periodically, and signaled to report UE Rx-Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE.

## A.9.7.7.2Test parameters

The parameters for this test case are defined in Table A.9.7.7.2-1, and the SRS configuration used is defined in Table A.9.7.7.2-2.

Table A.9.7.7.2-1: FDD UE Rx-Tx time difference test parameters for Cat-M1/M2 UE in CEModeA

Table A.9.7.7.2-2: Sounding Reference Symbol Configuration to be used in FDD UE Rx-Tx time difference test for Cat-M1/M2 UE in CEModeA

## A.9.7.7.3Test Requirements

For Cat-M1 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.21.21.

For Cat-M2 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.25.25.

## A.9.7.8E-UTRAN HD-FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA

## A.9.7.8.1Test Purpose and Environment

The purpose of this test is to verify that Cat-M1 and Cat-M2 UE can meet the E-UTRAN HD-FDD UE Rx-Tx time difference measurement accuracy requirements. Requirements for Cat-M1 UE is specified in Clause 9.1.21.21 and requirements for Cat-M2 UE is specified in Clause 9.1.25.25.

There is only one active cell in the test. The tested UE is connected with the PCell, configured to transmit SRS signals periodically, and signaled to report UE Rx-Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE.

## A.9.7.8.2Test parameters

The parameters for this test case are defined in Table A.9.7.8.2-1, and the SRS configuration used is defined in Table A.9.7.8.2-2.

Table A.9.7.8.2-1: HD-FDD UE Rx-Tx time difference test parameters for Cat-M1/M2 UE in CEModeA

Table A.9.7.8.2-2: Sounding Reference Symbol Configuration to be used in HD-FDD UE Rx-Tx time difference test for Cat-M1/M2 UE in CEModeA

## A.9.7.8.3Test Requirements

For Cat-M1 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.21.21.

For Cat-M2 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.25.25.

## A.9.7.9E-UTRAN TDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA

## A.9.7.9.1Test Purpose and Environment

The purpose of this test is to verify that Cat-M1 and Cat-M2 UE can meet the E-UTRAN TDD UE Rx-Tx time difference measurement accuracy requirements. Requirements for Cat-M1 UE is specified in Clause 9.1.21.21 and requirements for Cat-M2 UE is specified in Clause 9.1.25.25.

There is only one active cell in the test. The tested UE is connected with the PCell, configured to transmit SRS signals periodically, and signaled to report UE Rx-Tx time difference measurement. The test equipment measures the transmit timing of the UE using the transmitted SRS, and measures the receive timing using the downlink CRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE.

## A.9.7.9.2Test parameters

The parameters for this test case are defined in Table A.9.7.9.2-1, and the SRS configuration used is defined in Table A.9.7.9.2-2.

Table A.9.7.9.2-1: TDD UE Rx-Tx time difference test parameters for Cat-M1/M2 UE in CEModeA

Table A.9.7.9.2-2: Sounding Reference Symbol Configuration to be used in TDD UE Rx-Tx time difference test for Cat-M1/M2 UE in CEModeA

## A.9.7.9.3Test Requirements

For Cat-M1 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.21.21.

For Cat-M2 UE, the UE Rx-Tx time difference measurement accuracy shall fulfill the requirements in Clause 9.1.25.25.

## A.9.8RSTD

## A.9.8.1E-UTRAN FDD RSTD intra frequency case

## A.9.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSTD intra-frequency measurement accuracy is within the specified limits in clause 9.1.10.1 in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.1.1-1 and A.9.8.1.1-2 during this time.

The test parameters are given in Table A.9.8.1.1-1 and Table A.9.8.1.1-2.

Table A.9.8.1.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

Table A.9.8.1.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

## A.9.8.1.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.1.

## A.9.8.1.2ATest Requirements for UE Category 1bis

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.5. The test parameters given in Table A.9.8.1.1-1 and Table A.9.8.1.1-2 shall be applied with the exceptions given in Table A.9.8.1.2A-1.

Table A.9.8.1.2A-1: Specific test parameters for UE Category for 1Bis intra frequency RSTD Tests for E-UTRAN FDD

## A.9.8.2E-UTRAN TDD RSTD intra frequency case

## A.9.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSTD intra-frequency measurement accuracy is within the specified limits in clause 9.1.10.1 in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.2.1-1 and A.9.8.2.1-2 during this time.

The test parameters are given in Table A.9.8.2.1-1 and Table A.9.8.2.1-2.

Table A.9.8.2.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

Table A.9.8.2.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

## A.9.8.2.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.1.

## A.9.8.2.2ATest Requirements for UE Category 1bis

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.5. The test parameters given in Table A.9.8.2.1-1 and Table A.9.8.2.1-2 shall be applied with the exceptions given in Table A.9.8.2.2A-1.

Table A.9.8.2.2A-1: Specific test parameters for UE Category for 1Bis intra frequency RSTD Tests for E-UTRAN TDD

## A.9.8.3E-UTRAN FDD-FDD RSTD inter frequency case

## A.9.8.3.1Test Purpose and Environment

The purpose of these tests is to verify that the RSTD inter-frequency measurement accuracy is within the specified limits in clause 9.1.10.2 in AWGN channels.

There are two synchronous cells on different carrier frequencies in the test. In all test cases, Cell 1 is the reference cell as well as the PCell and Cell 2 the neighbor cell. The inter frequency measurements on Cell 2 are supported by measurement gaps. PCIs of the two cells are selected randomly.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.3.1-1 and Table A.9.8.3.1-2 for each of the two cells during this time.

The test parameters are given in Table A.9.8.3.1-1 and Table A.9.8.3.1-2.

Table A.9.8.3.1-1: General Test Parameters for inter frequency RSTD Tests for E-UTRAN FDD

Table A.9.8.3.1-2: Cell Specific Test Parameters for inter frequency RSTD Tests for E-UTRAN FDD

## A.9.8.3.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.2.

## A.9.8.3.2ATest Requirements for UE Category 1bis

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.6. The test parameters given in Table A.9.8.3.1-1 and Table A.9.8.3.1-2 shall be applied with the exceptions given in Table A.9.8.3.2A-1.

Table A.9.8.3.2A-1: Specific test parameters for UE Category for 1Bis inter frequency RSTD Tests for E-UTRAN FDD-FDD

## A.9.8.4E-UTRAN TDD-TDD RSTD inter frequency case

## A.9.8.4.1Test Purpose and Environment

The purpose of this test is to verify that the RSTD inter-frequency measurement accuracy is within the specified limits in clause 9.1.10.2 in AWGN channels.

There are two synchronous cells on different carrier frequencies in the test. In all test cases, Cell 1 is the reference cell as well as the PCell and Cell 2 is the neighbour cell. The inter frequency measurements on Cell 2 are supported by a measurement gap. PCIs of the two cells are selected randomly.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.4.1-1 and Table A.9.8.4.1-2 for each of the two cells during this time.

The test parameters are given in Table A.9.8.4.1-1 and Table A.9.8.4.1-2.

Table A.9.8.4.1-1: General Test Parameters for inter frequency RSTD Tests for E-UTRAN TDD

Table A.9.8.4.1-2: Cell Specific Test Parameters for inter frequency RSTD Tests for E-UTRAN TDD

## A.9.8.4.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.2.

## A.9.8.4.2ATest Requirements for UE Category 1bis

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.10.6. The test parameters given in Table A.9.8.4.1-1 and Table A.9.8.4.1-2 shall be applied with the exceptions given in Table A.9.8.4.2A-1.

Table A.9.8.4.2A-1: Specific test parameters for UE Category for 1Bis inter frequency RSTD Tests for E-UTRAN TDD-TDD

## A.9.8.5E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation

## A.9.8.5.1Test Purpose and Environment

The purpose of these tests is to verify that the E-UTRAN FDD RSTD measurement accuracy in carrier aggregation is within the specified limits in clause 9.1.12.

There are three synchronous cells on two different carrier frequencies in the test. Cell 1 is the PCell on primary component carrier F1 (RF channel number 1), Cell 2 is the SCell and reference cell on sceondary component carrier F2 (RF channel number 2), and Cell 3 is the neighbor cell on F2.

Cell2 and Cell3 are included in the OTDOA assistance data, whilst Cell1 is not included in the OTDOA assistance data. The RSTD measurements are performed between Cell 2 and Cell 3 to verify that when both the reference cell and neighbouring cell belong to the secondary component carrier the RSTD measurement accuracy can meet the intra-frequency RSTD accuracy requirements defined in clause 9.1.10.1.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap is not configured in the test because of UE carrier aggregation capability.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.5.1-1 and Table A.9.8.5.1-2 for each of the three cells during this time.

The test parameters are given in Table A.9.8.5.1-1 and Table A.9.8.5.1-2.

Table A.9.8.5.1-1: General Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation

Table A.9.8.5.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation

## A.9.8.5.2Test Requirements

The measurement accuracy of RSTD between Cell2 and Cell3 shall fulfill the requirements in clause 9.1.12.

## A.9.8.6E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation

## A.9.8.6.1Test Purpose and Environment

The purpose of these tests is to verify that the E-UTRAN TDD RSTD measurement accuracy in carrier aggregation is within the specified limits in clause 9.1.12.

There are three synchronous cells on two different carrier frequencies in the test. Cell 1 is the PCell on primary component carrier F1 (RF channel number 1), Cell 2 is the SCell and reference cell on sceondary component carrier F2 (RF channel number 2), and Cell 3 is the neighbor cell on F2.

Cell2 and Cell3 are included in the OTDOA assistance data, whilst Cell1 is not included in the OTDOA assistance data. The RSTD measurements are performed between Cell 2 and Cell 3 to verify that when both the reference cell and neighbouring cell belong to the secondary component carrier the RSTD measurement accuracy can meet the intra-frequency RSTD accuracy requirements defined in clause 9.1.10.1.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap is not configured in the test because of UE carrier aggregation capability.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.6.1-1 and Table A.9.8.6.1-2 for each of the three cells during this time.

The test parameters are given in Table A.9.8.6.1-1 and Table A.9.8.6.1-2.

Table A.9.8.6.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation

Table A.9.8.6.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation

## A.9.8.6.2Test Requirements

The measurement accuracy of RSTD between Cell2 and Cell3 shall fulfill the requirements in clause 9.1.12.

## A.9.8.7E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth

## A.9.8.7.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.5.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.7.1-1 and A.9.8.7.1-2 will replace the values of corresponding parameters in Tables A.9.8.5.1-1 and A.9.8.5.1-2.

Table A.9.8.7.1-1: General Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 20MHz bandwidth

Table A.9.8.7.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 20MHz bandwidth

## A.9.8.7.2Test Requirements

The test requirements defined in section A.9.8.5.2 shall apply to this test case.

## A.9.8.8E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth

## A.9.8.8.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.6.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.8.1-1 and A.9.8.8.1-2 will replace the values of corresponding parameters in Tables A.9.8.6.1-1 and A.9.8.6.1-2.

Table A.9.8.8.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 20MHz bandwidth

Table A.9.8.8.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 20MHz bandwidth

## A.9.8.8.2Test Requirements

The test requirements defined in section A.9.8.6.2 shall apply to this test case.

## A.9.8.9E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz

## A.9.8.9.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.5.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.9.1-1 and A.9.8.9.1-2 will replace the values of corresponding parameters in Tables A.9.8.5.1-1 and A.9.8.5.1-2.

Table A.9.8.9.1-1: General Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 10MHz+5MHz

Table A.9.8.9.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 10MHz+5MHz

## A.9.8.9.2Test Requirements

The test requirements defined in section A.9.8.5.2 shall apply to this test case.

## A.9.8.10E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz

## A.9.8.10.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.6.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.10.1-1 and A.9.8.10.1-2 will replace the values of corresponding parameters in Tables A.9.8.6.1-1 and A.9.8.6.1-2.

Table A.9.8.10.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 10MHz+5MHz

Table A.9.8.10.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 10MHz+5MHz

## A.9.8.10.2Test Requirements

The test requirements defined in section A.9.8.6.2 shall apply to this test case.

## A.9.8.11E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 5 + 5MHz bandwidth

## A.9.8.11.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.5.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.11.1-1 and A.9.8.11.1-2 will replace the values of corresponding parameters in Tables A.9.8.5.1-1 and A.9.8.5.1-2.

Table A.9.8.11.1-1: General Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 5+5MHz bandwidth

Table A.9.8.11.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation for 5+5MHz bandwidth

## A.9.8.11.2Test Requirements

The test requirements defined in section A.9.8.5.2 shall apply to this test case.

## A.9.8.12E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 5+5MHz bandwidth

## A.9.8.12.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.6.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.12.1-1 and A.9.8.12.1-2 will replace the values of corresponding parameters in Tables A.9.8.6.1-1 and A.9.8.6.1-2.

Table A.9.8.12.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 5+5MHz bandwidth

Table A.9.8.12.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 5+5MHz bandwidth

## A.9.8.12.2Test Requirements

The test requirements defined in section A.9.8.6.2 shall apply to this test case.

## A.9.8.13E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz+10MHz

## A.9.8.13.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.9.8.6.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.9.8.13.1-1 and A.9.8.13.1-2 will replace the values of corresponding parameters in Tables A.9.8.6.1-1 and A.9.8.6.1-2.

Table A.9.8.13.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 20MHz+10MHz

Table A.9.8.13.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation for 20MHz+10MHz

## A.9.8.13.2Test Requirements

The test requirements defined in section A.9.8.6.2 shall apply to this test case.

## A.9.8.14E-UTRAN FDD RSTD Measurement Accuracy in 3DL Carrier Aggregation

## A.9.8.14.1Test Purpose and Environment

The purpose of these tests is to verify that the E-UTRAN FDD RSTD measurement accuracy in carrier aggregation is within the specified limits in clause 9.1.12.

There are four synchronous cells on three different carrier frequencies in the test. Cell 1 is the PCell on primary component carrier F1 (RF channel number 1), Cell 2 is an SCell on secondary component carrier F2 (RF channel number 2), Cell 3 is an SCell and reference cell on secondary component carrier F3 (RF channel number 3), and Cell 4 is the neighbor cell on F3.

Cell 1, Cell2, Cell3, and Cell 4 are included in the OTDOA assistance data. The RSTD measurements are performed

-between Cell 4 and Cell 3 to verify the accuracy of RSTD measurement when the reference cell and neighbouring cell belong to the same secondary component carrier can meet the intra-frequency RSTD accuracy requirements defined in clause 9.1.10.1.

-between Cell 1 and Cell 3 to verify the accuracy of RSTD measurement between the PCell and an SCell can meet the inter-frequency RSTD accuracy requirements defined in clause 9.1.10.2.

-between Cell 2 and Cell 3 to verify the accuracy of RSTD measurement between two SCells can meet the inter-frequency RSTD accuracy requirements defined in clause 9.1.10.2.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap is not configured in the test because of UE carrier aggregation capability.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.14.1-1 and Table A.9.8.14.1-2 for each of the three cells during this time.

The test parameters are given in Table A.9.8.14.1-1 and Table A.9.8.14.1-2.

Table A.9.8.14.1-1: General Test Parameters for RSTD Tests for E-UTRAN FDD for 3DL Carrier Aggregation

Table A.9.8.14.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN FDD for Carrier Aggregation

## A.9.8.14.2Test Requirements

The measurement accuracy of RSTD between Cell1 and Cell3 shall fulfill the requirements in clause 9.1.12.2

The measurement accuracy of RSTD between Cell2 and Cell3 shall fulfill the requirements in clause 9.1.12.2

The measurement accuracy of RSTD between Cell4 and Cell3 shall fulfill the requirements in clause 9.1.12.1.

## A.9.8.15E-UTRAN TDD RSTD Measurement Accuracy in 3DL Carrier Aggregation

## A.9.8.15.1Test Purpose and Environment

The purpose of these tests is to verify that the E-UTRAN TDD RSTD measurement accuracy in carrier aggregation is within the specified limits in clause 9.1.12.

There are four synchronous cells on three different carrier frequencies in the test. Cell 1 is the PCell on primary component carrier F1 (RF channel number 1), Cell 2 is an SCell on secondary component carrier F2 (RF channel number 2), Cell 3 is an SCell and reference cell on secondary component carrier F3 (RF channel number 3), and Cell 4 is the neighbor cell on F3.

Cell 1, Cell2, Cell3, and Cell 4 are included in the OTDOA assistance data. The RSTD measurements are performed

-between Cell 4 and Cell 3 to verify the accuracy of RSTD measurement when the reference cell and neighbouring cell belong to the same secondary component carrier can meet the intra-frequency RSTD accuracy requirements defined in clause 9.1.10.1.

-between Cell 1 and Cell 3 to verify the accuracy of RSTD measurement between the PCell and an SCell can meet the inter-frequency RSTD accuracy requirements defined in clause 9.1.10.2.

-between Cell 2 and Cell 3 to verify the accuracy of RSTD measurement between two SCells can meet the inter-frequency RSTD accuracy requirements defined in clause 9.1.10.2.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap is not configured in the test because of UE carrier aggregation capability.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Table A.9.8.15.1-1 and Table A.9.8.15.1-2 for each of the three cells during this time.

The test parameters are given in Table A.9.8.15.1-1 and Table A.9.8.15.1-2.

Table A.9.8.15.1-1: General Test Parameters for RSTD Tests for E-UTRAN TDD for 3DL Carrier Aggregation

Table A.9.8.15.1-2: Cell Specific Test Parameters for RSTD Tests for E-UTRAN TDD for Carrier Aggregation

## A.9.8.15.2Test Requirements

The measurement accuracy of RSTD between Cell1 and Cell3 shall fulfill the requirements in clause 9.1.12.2

The measurement accuracy of RSTD between Cell2 and Cell3 shall fulfill the requirements in clause 9.1.12.2

The measurement accuracy of RSTD between Cell4 and Cell3 shall fulfill the requirements in clause 9.1.12.1.

## A.9.8.16HD – FDD Intra frequency case for UE Category NB1 inband mode in normal coverage

## A.9.8.16.1Test Purpose and Environment

The purpose of the tests is to verify that the intra frequency RSTD measurement for HD-FDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.10. Test 1 is applicable for UE supporting NPRS Type 1 and Test 2 is applicable for UE supporting NPRS Type 2.

In the tests there are three synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell12 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355, shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.16.1-1, A.9.8.16.1-2 and A.9.8.16.1-3.

Table A.9.8.16.1-1: General test parameters

Table A.9.8.16.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.16.1-3: eCell 1 and eCell 2 specific test parameters

## A.9.8.16.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.10.

## A.9.8.17HD – FDD Inter frequency case for UE Category NB1 inband mode in normal coverage

## A.9.8.17.1Test Purpose and Environment

The purpose of the tests is to verify that the intra frequency RSTD measurement for HD-FDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.11. Test 1 is applicable for UE supporting NPRS Type 1 and Test 2 is applicable for UE supporting NPRS Type 2.

In the tests there are three synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell2 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355, shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.17.1-1, A.9.8.17.1-2 and A.9.8.17.1-3.

Table A.9.8.17.1-1: General test parameters

Table A.9.8.17.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.17.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.17.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.11.

## A.9.8.18HD – FDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage

## A.9.8.18.1Test Purpose and Environment

The purpose of the tests is to verify that the intra frequency RSTD measurement for HD-FDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.12. Test 1 is applicable for UE supporting NPRS Type 1 and Test 2 is applicable for UE supporting NPRS Type 2.

In the tests there are three synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell2 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355, shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.18.1-1, A.9.8.18.1-2 and A.9.8.18.1-3.

Table A.9.8.18.1-1: General test parameters

Table A.9.8.18.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.18.1-3: eCell 1 and eCell 2 specific test parameters

## A.9.8.18.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.12.

## A.9.8.19HD – FDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage

## A.9.8.19.1Test Purpose and Environment

The purpose of the tests is to verify that the intra frequency RSTD measurement for HD-FDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.13. Test 1 is applicable for UE supporting NPRS Type 1 and Test 2 is applicable for UE supporting NPRS Type 2.

In the tests there are three synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell2 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355, shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.19.1-1, A.9.8.19.1-2 and A.9.8.19.1-3.

Table A.9.8.19.1-1: General test parameters

Table A.9.8.19.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.19.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.19.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.13.

## A.9.8.20E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode A

## A.9.8.20.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE ModeA that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.20 and 9.1.25.4, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.20.1-1 and A.9.8.20.1-2 during this time.

The test parameters are given in Table A.9.8.20.1-1 and Table A.9.8.20.1-2.

Table A.9.8.20.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

Table A.9.8.20.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

## A.9.8.20.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.20.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.4.

## A.9.8.21E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CEModeA

## A.9.8.21.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CEModeA that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.20 and 9.1.25.4, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.21.1-1 and A.9.8.21.1-2 during this time.

The test parameters are given in Table A.9.8.21.1-1 and Table A.9.8.21.1-2.

Table A.9.8.21.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN HD-FDD

Table A.9.8.21.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN HD-FDD

## A.9.8.21.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.20.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.4.

## A.9.8.22E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode A

## A.9.8.22.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode A that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.20 and 9.1.25.4, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.22.1-1 and A.9.8.22.1-2 during this time.

The test parameters are given in Table A.9.8.22.1-1 and Table A.9.8.22.1-2.

Table A.9.8.22.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

Table A.9.8.22.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

## A.9.8.22.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.20.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.4.

## A.9.8.23E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode B

## A.9.8.23.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.21 and 9.1.25.5, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.23.1-1 and A.9.8.23.1-2 during this time.

The test parameters are given in Table A.9.8.23.1-1 and Table A.9.8.23.1-2.

Table A.9.8.23.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

Table A.9.8.23.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN FDD

## A.9.8.23.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.21.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.5.

## A.9.8.24E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CE Mode B

## A.9.8.24.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.21 and 9.1.25.5, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.24.1-1 and A.9.8.24.1-2 during this time.

The test parameters are given in Table A.9.8.24.1-1 and Table A.9.8.24.1-2.

Table A.9.8.24.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN HD-FDD

Table A.9.8.24.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN HD-FDD

## A.9.8.24.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.21.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.5.

## A.9.8.25E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode B

## A.9.8.25.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD intra-frequency measurement accuracy is within the specified limits in sections 9.1.21.21 and 9.1.25.5, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell on the same frequency. Tests 1 and 2 are applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Tests 3 and 4 are applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data.

A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.25.1-1 and A.9.8.25.1-2 during this time.

The test parameters are given in Table A.9.8.25.1-1 and Table A.9.8.25.1-2.

Table A.9.8.25.1-1: General Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

Table A.9.8.25.1-2: Cell Specific Test Parameters for intra frequency RSTD Tests for E-UTRAN TDD

## A.9.8.25.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.21.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.5.

## A.9.8.26E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode A

## A.9.8.26.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE ModeA that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.17 and 9.1.25.1, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on FDD RF channel 1 and Cell 2 is on FDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.26.1-1 and A.9.8.26.1-2 during this time.

The test parameters are given in Table A.9.8.26.1-1 and Table A.9.8.26.1-2.

Table A.9.8.26.1-1: General Test Parameters for E-UTRAN FDD-FDD inter-frequency RSTD Tests

Table A.9.8.26.1-2: Cell Specific Test Parameters for E-UTRAN FDD-FDD inter-frequency RSTD Tests

## A.9.8.26.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.17.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.1.

## A.9.8.27E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode A

## A.9.8.27.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE ModeA that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.17 and 9.1.25.1, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on FDD RF channel 1 and Cell 2 is on FDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.27.1-1 and A.9.8.27.1-2 during this time.

The test parameters are given in Table A.9.8.27.1-1 and Table A.9.8.27.1-2.

Table A.9.8.27.1-1: General Test Parameters for E-UTRAN HD-FDD inter-frequency RSTD Tests

Table A.9.8.27.1-2: Cell Specific Test Parameters for E-UTRAN HD-FDD inter-frequency RSTD Tests

## A.9.8.27.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.17.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.1.

## A.9.8.28E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode A

## A.9.8.28.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE ModeA that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.17 and 9.1.25.1, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on TDD RF channel 1 and Cell 2 is on TDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.28.1-1 and A.9.8.28.1-2 during this time.

The test parameters are given in Table A.9.8.28.1-1 and Table A.9.8.28.1-2.

Table A.9.8.28.1-1: General Test Parameters for E-UTRAN TDD inter-frequency RSTD Tests

Table A.9.8.28.1-2: Cell Specific Test Parameters for E-UTRAN TDD inter-frequency RSTD Tests

## A.9.8.28.2Test Requirements

For Cat-M1 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.17.

For Cat-M2 UE in CE Mode A, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.1.

## A.9.8.29E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode B

## A.9.8.29.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.18 and 9.1.25.2, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on FDD RF channel 1 and Cell 2 is on FDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.29.1-1 and A.9.8.29.1-2 during this time.

The test parameters are given in Table A.9.8.29.1-1 and Table A.9.8.29.1-2.

Table A.9.8.29.1-1: General Test Parameters for E-UTRAN FDD-FDD inter-frequency RSTD Tests

Table A.9.8.29.1-2: Cell Specific Test Parameters for E-UTRAN FDD-FDD inter-frequency RSTD Tests

## A.9.8.29.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.18.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.2.

## A.9.8.30E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode B

## A.9.8.30.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.18 and 9.1.25.2, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on FDD RF channel 1 and Cell 2 is on FDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.30.1-1 and A.9.8.30.1-2 during this time.

The test parameters are given in Table A.9.8.30.1-1 and Table A.9.8.30.1-2.

Table A.9.8.30.1-1: General Test Parameters for E-UTRAN HD-FDD inter-frequency RSTD Tests

Table A.9.8.30.1-2: Cell Specific Test Parameters for E-UTRAN HD-FDD inter-frequency RSTD Tests

## A.9.8.30.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.18.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.2.

## A.9.8.31E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode B

## A.9.8.31.1Test Purpose and Environment

The purpose of the test is to verify for Cat-M1 and Cat-M2 UE in CE Mode B that the RSTD inter-frequency measurement accuracy is within the specified limits in sections 9.1.21.18 and 9.1.25.2, respectively, in AWGN channels.

In the test, there are two synchronous cells, Cell 1 as the reference cell and Cell 2 as the neighbour cell. Cell 1 is on TDD RF channel 1 and Cell 2 is on TDD RF channel 2.

The UE requires measurement gaps to perform inter-frequency measurements. Gap pattern configuration # 0 as defined in Table 8.1.2.1-1 is provided and configured not to overlap with PRS subframes of Cell 1. Test 1 is applicable for Cat-M1 and Cat-M2 supporting 1.4 MHz UE RF bandwidth, while Test 2 is applicable for Cat-M2 supporting 5 MHz UE RF bandwidth.

The OTDOA assistance data as defined in TS 36.355, Clause 6.5.1, shall be provided to the UE before the measurement period. The last TTI containing the OTDOA assistance data shall be provided to the UE T ms before the start of measurement period, where T = 150 ms is the maximum processing time of the OTDOA assistance data. The measurement gap configuration is known and configured in the UE before the measurements start.

There is no PDSCH allocated in the subframe transmitting PRS. A time span of  is provided for the measurement period, and PRS are configured according to  in Tables A.9.8.31.1-1 and A.9.8.31.1-2 during this time.

The test parameters are given in Table A.9.8.31.1-1 and Table A.9.8.31.1-2.

Table A.9.8.31.1-1: General Test Parameters for E-UTRAN TDD inter-frequency RSTD Tests

Table A.9.8.31.1-2: Cell Specific Test Parameters for E-UTRAN TDD inter-frequency RSTD Tests

## A.9.8.31.2Test Requirements

For Cat-M1 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.21.18.

For Cat-M2 UE in CE Mode B, the RSTD measurement accuracy shall fulfill the requirements in clause 9.1.25.2.

## A.9.8.32TDD Intra frequency case for UE Category NB1 inband mode in normal coverage

## A.9.8.32.1Test Purpose and Environment

The purpose of the test is to verify that the intra frequency RSTD measurement for TDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.10.

In the test there are four synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell12 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.32.1-1, A.9.8.32.1-2 and A.9.8.32.1-3.

Table A.9.8.32.1-1: General test parameters

Table A.9.8.32.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.32.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.32.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.10.

## A.9.8.33TDD Inter frequency case for UE Category NB1 inband mode in normal coverage

## A.9.8.33.1Test Purpose and Environment

The purpose of the test is to verify that the inter frequency RSTD measurement for TDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.11.

In the test there are four synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell2 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.33.1-1, A.9.8.33.1-2 and A.9.8.33.1-3.

Table A.9.8.33.1-1: General test parameters

Table A.9.8.33.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.33.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.33.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.11.

## A.9.8.34TDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage

## A.9.8.34.1Test Purpose and Environment

The purpose of the test is to verify that the intra frequency RSTD measurement for TDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.12.

In the test there are four synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell12 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.34.1-1, A.9.8.34.1-2 and A.9.8.34.1-3.

Table A.9.8.34.1-1: General test parameters

Table A.9.8.34.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.34.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.34.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.12.

## A.9.8.35TDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage

## A.9.8.35.1Test Purpose and Environment

The purpose of the test is to verify that the inter frequency RSTD measurement for TDD category NB1 UE meets the accuracy requirements specified in Clause 9.1.22.13.

In the test there are four synchronous cells: nCell 1, nCell 2, eCell1 and eCell 2. nCell 1 is the reference as well as the PCell. nCell 2, eCell1 and eCell12 are the neighbour cells.

The OTDOA assistance data and OTDOA-RequestLocationInformation as defined in TS 36.355 [24], shall be provided to the UE. After the receipt of the OTDOA assistance data and OTDOA-RequestLocationInformation has been successfully acknowledged, the UE is provided with a RRC connection release command. The UE is expected to enter RRC_IDLE before the measurement period.

The test parameters are given in Tables A.9.8.35.1-1, A.9.8.35.1-2 and A.9.8.35.1-3.

Table A.9.8.35.1-1: General test parameters

Table A.9.8.35.1-2: nCell1 and nCell2 specific test parameters

Table A.9.8.35.1-3: eCell 1 and eCell2 specific test parameters

## A.9.8.35.2Test Requirements

The RSTD measurement accuracy shall fulfill the requirements in clause 9.1.22.13.

## A.9.9RSRP and RSRQ on the serving cell

## A.9.9.1FDD Intra frequency serving cell case

## A.9.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP/ RSRQ absolute measurement accuracy is within the specified limits. This test will verify the requirements in Clause 9.1.2.1 and 9.1. 5.1 for FDD intra frequency measurements.

## A.9.9.1.2Test parameters

In this set of test case there is only the serving cell. Absolute accuracy of RSRP/ RSRQ intra frequency measurements for the serving cell is tested by using the parameters in Table A.9.9.1.2-1. In the test case, Cell 1 is the serving cell.

Table A.9.9.1.2-1: RSRP FDD Intra frequency test parameters

## A.9.9.1.3Test Requirements

The absolute RSRP and RSRQ measurement accuracy shall fulfil the requirements in clause 9.1.2.1 and 9.1.5.1 respectively.

## A.9.9.2TDD Intra frequency serving cell case

## A.9.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP/ RSRQ absolute measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.2.1 and 9.1.5.1 for TDD intra frequency measurements.

## A.9.9.2.2Test parameters

In this set of test case there is only the serving cell. Absolute accuracy of RSRP/ RSRQ intra frequency measurements for the serving cell is tested by using the parameters in Table A.9.9.2.2-1. In the test case, Cell 1 is the serving cell.

Table A.9.9.2.2-1: RSRP TDD Intra frequency test parameters

## A.9.9.2.3Test Requirements

The absolute RSRP and RSRQ measurement accuracy shall fulfil the requirements in section 9.1.2.1 and 9.1.5.1 respectively.

## A.9.10SSTD

## A.9.10.1EUTRAN FDD-FDD SSTD accuracy in asynchronous DC

## A.9.10.1.1Test Purpose and Environment

The purpose of this test is to verify that the SSTD measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.20 for FDD SSTD measurements.

## A.9.10.1.2Test parameters

The test parameters are given in Tables A.9.10.1.2-1 and A.9.10.1.2-2. In this test there are 2 cells.  Cell 1 is the PCell and cell 2 is the PScell. Cell 1 and cell 2 are on different frequencies. The SSTD time difference between PCell and PSCell reported by the UE is compared to the actual SSTD. The SSTD time difference between PCell and PSCell shall be set by the test equipment to one of the time differences in table A.9.10.1.2-3.

Table A.9.10.1.2-1: EUTRAN FDD-FDD SSTD accuracy in asynchronous DC

Table A.9.10.1.2-2: EUTRAN FDD-FDD SSTD accuracy in asynchronous DC

Table A.9.10.1.2-3: EUTRAN FDD-FDD SSTD accuracy in asynchronous DC timing offsets

## A.9.10.1.3Test Requirements

The SSTD reported by the UE consists of 3 elements,  SFN offset between MeNB and SeNB (ΔX), frame boundary offset between MeNB and SeNB (ΔY)  and subframe boundary offset between MeNB and SeNB (ΔZ).

The reported ΔX, ΔY and ΔZ shall meet the accuracy requirements in section 9.1.20.

## A.9.10.2Void

## A.9.10.3Void

## A.9.10.4Void

## A.9.11 RSSI

## A.9.11.1FS3 average RSSI accuracy case (PCell using FDD)

## A.9.11.1.1Test Purpose and Environment

The purpose of this test is to verify that the average RSSI measurement accuracy is within the specified limits. This test will partially verify the requirements in Section 9.1.18.5.2.

## A.9.11.1.2Test parameters

In all test cases, Cell 1 is the PCell and Cell 2 the FS3 Scell. RSSI is measured on channel number 2.

Table A.9.11.1.2-1: Average RSSI test parameters

Table A.9.11.1.2-2: Average RSSI RMTC and DMTC parameters

## A.9.11.1.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 9.1.18.5.2. The nominal RSSI used to evaluate the requirement shall be based on Io in subframes corresponding to RSSI measurement time configuration (RMTC).

## A.9.11.2FS3 average RSSI accuracy case (PCell using TDD)

## A.9.11.2.1Test Purpose and Environment

The purpose of this test is to verify that the average RSSI measurement accuracy is within the specified limits. This test will partially verify the requirements in Section 9.1.18.5.2.

## A.9.11.2.2Test parameters

In all test cases, Cell 1 is the PCell and Cell 2 the FS3 Scell. RSSI is measured on channel number 2.

Table A.9.11.2.2-1: Average RSSI test parameters

Table A.9.11.2.2-2: Average RSSI RMTC and DMTC parameters

A.9.11.2.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 9.1.18.5.2. The nominal RSSI used to evaluate the requirement shall be based on Io in subframes corresponding to RSSI measurement time configuration (RMTC).

## A.9.12Channel occupancy

## A.9.12.1FS3 channel occupancy test (PCell using FDD)

## A.9.12.1.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy is within the specified limits. This test will partially verify the requirements in Section 9.1.18.6.1.

## A.9.12.1.2Test parameters

In all test cases, Cell 1 is the PCell and Cell 2 the FS3 Scell. Channel occupancy is measured on channel number 2.

Table A.9.12.1.2-1: Channel occupancy test parameters

Table A.9.12.1.2-2: Channel occupancy RMTC and DMTC parameters

## A.9.12.1.3Test Requirements

The nominal reported channelOccupancy shall be 33. At least 90% of channel occupancy reports made by the UE shall indicate this value.

## A.9.12.2FS3 channel occupancy test (PCell using TDD)

## A.9.12.2.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy is within the specified limits. This test will partially verify the requirements in Section 9.1.18.6.1.

## A.9.12.2.2Test parameters

In all test cases, Cell 1 is the PCell and Cell 2 the FS3 Scell. Channel occupancy is measured on channel number 2.

Table A.9.12.2.2-1: Channel occupancy test parameters

Table A.9.12.2.2-2: Channel occupancy RMTC and DMTC parameters

## A.9.12.2.3Test Requirements

The nominal reported channelOccupancy in this test is 33. At least 90% of channel occupancy reports made by the UE shall indicate this value.

## A.9.13RS-SINR

## A.9.13.1FDD Intra-Frequency Case

## A.9.13.1.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.17.2.1.

## A.9.13.1.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RS-SINR intra-frequency measurement is tested by using the parameters in Table A.9.13.1.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.13.1.2-1: RS-SINR FDD intra-frequency test parameters

## A.9.13.1.3Test Requirements

The RS-SINR measurement accuracy for Cell 2 shall fulfil the requirements in Section 9.1.17.2.1.

## A.9.13.2TDD Intra-Frequency Case

## A.9.13.2.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Section 9.1.17.2.1.

## A.9.13.2.2Test parameters

In this test case all cells are on the same carrier frequency. The absolute accuracy of RS-SINR intra-frequency measurement is tested by using the parameters in Table A.9.13.2.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.13.2.2-1: RS-SINR TDD intra-frequency test parameters

## A.9.13.2.3Test Requirements

The RS-SINR measurement accuracy for Cell 2 shall fulfil the requirements in Section 9.1.17.2.1.

## A.9.13.3FDD—FDD Inter frequency case

## A.9.13.3.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.17.3.

## A.9.13.3.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RS-SINR inter-frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.13.3.2-1 and Table A.9.13.3.2-2. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.13.3.2-1: RS-SINR FDD—FDD Inter frequency test parameters (Cell 1)

Table A.9.13.3.2-2: RS-SINR FDD—FDD Inter frequency test parameters (Cell 2)

## A.9.13.3.3Test Requirements

The RS-SINR measurement accuracy shall fulfil the requirements in Sections 9.1.17.3.

## A.9.13.4TDD—TDD Inter frequency case

## A.9.13.4.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.17.3.

## A.9.13.4.2Test parameters

In this test case the two cells are on different carrier frequencies and measurement gaps are provided. Both RS-SINR inter-frequency absolute and relative accuracy requirements are tested by using test parameters in Table A.9.13.4.2-1 and Table A.9.13.4.2-2 for TDD configuration 1 and in Table A.9.13.4.2-3 and Table A.9.13.4.2-4 for TDD configuration 0. In all tests, Cell 1 is the PCell and Cell 2 the target cell.

Table A.9.13.4.2-1: RS-SINR TDD—TDD Inter frequency test parameters for TDD configuration 1 (Cell 1)

Table A.9.13.4.2-2: RS-SINR TDD—TDD Inter frequency test parameters for TDD configuration 1 (Cell 2)

Table A.9.13.4.2-3: RS-SINR TDD—TDD Inter frequency test parameters for TDD configuration 0 (Cell 1)

Table A.9.13.4.2-4: RS-SINR TDD—TDD Inter frequency test parameters for TDD configuration 0 (Cell 2)

## A.9.13.4.3Test Requirements

The RS-SINR measurement accuracy shall fulfil the requirements in Sections 9.1.17.3.

## A.9.13.5FDD—TDD Inter frequency case

## A.9.13.5.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.17.3.

## A.9.13.5.2Test parameters

In this set of test cases the two cells are on different carrier frequencies. Both absolute and relative accuracy of RS-SINR inter frequency measurements are tested by using the parameters in Table A.9.13.5.2-1. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell. Cell 1 is FDD cell and Cell 2 is TDD cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.13.5.2-1: RS-SINR FDD—TDD Inter frequency test parameters (FDD Cell1)

Table A.9.13.5.2-2: RS-SINR FDD—TDD Inter frequency test parameters (TDD cell2)

## A.9.13.5.3Test Requirements

The RS-SINR measurement accuracy shall fulfil the requirements in Sections 9.1.17.3.

## A.9.13.6TDD—FDD Inter frequency case

## A.9.13.6.1Test Purpose and Environment

The purpose of this test is to verify that the RS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.17.3.

## A.9.13.6.2Test parameters

In this set of test cases the two cells are on different carrier frequencies. Both absolute and relative accuracy of RS-SINR inter frequency measurements are tested by using the parameters in Table A.9.13.6.2-1. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell. Cell 1 is TDD cell and Cell 2 is FDD cell. The inter frequency measurements are supported by a measurement gap.

Table A.9.13.6.2-1: RS-SINR TDD—FDD Inter frequency test parameters (TDD cell1)

Table A.9.13.6.2-2: RS-SINR TDD—FDD Inter frequency test parameters (FDD Cell2)

## A.9.13.6.3Test Requirements

The RS-SINR measurement accuracy shall fulfil the requirements in Sections 9.1.17.3.

## A.9.14Channel quality reporting accuracy

## A.9.14.1E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage

## A.9.14.1.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

## A.9.14.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.1.2-1 and A.9.14.1.2-2.

Table A.9.14.1.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

Table A.9.14.1.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

## A.9.14.1.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

## A.9.14.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage

## A.9.14.2.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

## A.9.14.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.2.2-1 and A.9.14.2.2-2.

Table A.9.14.2.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.9.14.2.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

## A.9.14.2.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

## A.9.14.3E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage

## A.9.14.3.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy on non-anchor carrier is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

## A.9.14.3.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy on non-anchor carrier is tested by using the parameters in Tables A.9.14.3.2-1 and A.9.14.3.2-2.

Table A.9.14.3.2-1: General Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

Table A.9.14.3.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

## A.9.14.3.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

## A.9.14.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage

## A.9.14.4.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy on non-anchor carrier is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

## A.9.14.4.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy on non-anchor carrier is tested by using the parameters in Tables A.9.14.4.2-1 and A.9.14.4.2-2.

Table A.9.14.4.2-1: General Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.9.14.4.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

## A.9.14.4.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

A.9.14.5E-UTRAN HD-FDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under normal coverage

A.9.14.5.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

A.9.14.5.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The tests consist of two successive time periods of length T1 and T2, respectively, at different SNR levels. The start of T2 coincides with the start of the channel quality measurement period specified in section 8.14.4. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.5.2-1 and A.9.14.5.2-2.

Table A.9.14.5.2-1: General Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

Table A.9.14.5.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under normal coverage

A.9.14.5.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

A.9.14.6E-UTRAN HD-FDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under enhanced coverage

A.9.14.6.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.22.16.

A.9.14.6.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The tests consist of two successive time periods of length T1 and T2, respectively, at different SNR levels. The start of T2 coincides with the start of the channel quality measurement period specified in section 8.14.4. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.6.2-1 and A.9.14.6.2-2.

Table A.9.14.6.2-1: General Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.9.14.6.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

A.9.14.6.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22.16.

A.9.14.7E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A

A.9.14.7.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.7.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.7.2-1 and A.9.14.7.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.7.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode A

Table A.9.14.7.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode A

A.9.14.7.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.8E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A

A.9.14.8.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.8.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.8.2-1 and A.9.14.8.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.8.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode A

Table A.9.14.8.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode A

A.9.14.8.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.9E-UTRAN TDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A

A.9.14.9.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.9.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.9.2-1 and A.9.14.9.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.9.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE in CE Mode A

Table A.9.14.9.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE in CE Mode A

A.9.14.9.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.10E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B

A.9.14.10.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.10.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.10.2-1 and A.9.14.10.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.10.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode B

Table A.9.14.10.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode B

A.9.14.10.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

A.9.14.11E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B

A.9.14.11.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.11.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.11.2-1 and A.9.14.11.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.11.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode B

Table A.9.14.11.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode B

A.9.14.11.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

A.9.14.12E-UTRAN TDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B

A.9.14.12.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.12.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.12.2-1 and A.9.14.12.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.12.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE in CE Mode B

Table A.9.14.12.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE in CE Mode B

A.9.14.12.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

A.9.14.13E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 under normal coverage

A.9.14.13.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.13.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.13.2-1 and A.9.14.13.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3. The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.13.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE under normal coverage

Table A.9.14.13.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE under normal coverage

A.9.14.13.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.14E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 under normal coverage

A.9.14.14.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.14.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.14.2-1 and A.9.14.14.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3. The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.14.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE under normal coverage

Table A.9.14.14.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE under normal coverage

A.9.14.14.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.15E-UTRAN TDD Downlink channel quality reporting accuracy for UE Category M1 under normal coverage

A.9.14.15.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.23.

A.9.14.15.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.15.2-1 and A.9.14.15.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3. The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.15.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE under normal coverage

Table A.9.14.15.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE under normal coverage

A.9.14.15.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.23.

A.9.14.16E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 under enhanced coverage

A.9.14.16.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.16.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.16.2-1 and A.9.14.16.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3. The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.16.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE under enhanced coverage

Table A.9.14.16.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE under enhanced coverage

A.9.14.16.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

A.9.14.17E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 under enhanced coverage

A.9.14.17.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.17.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.17.2-1 and A.9.14.17.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3. The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.17.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE under enhanced coverage

Table A.9.14.17.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE under enhanced coverage

A.9.14.17.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

A.9.14.18E-UTRAN TDD Downlink channel quality reporting accuracy for UE Category M1 under enhanced coverage

A.9.14.18.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in idle mode is within the specified limits. This test will verify the requirements in Section 9.1.21.24.

A.9.14.18.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.9.14.18.2-1 and A.9.14.18.2-2. There are two time periods T1 and T2 with different SNR levels. The start of T2 coincides with the start of the channel quality measurement period defined in clause 4.7.3.  The UE transmits the downlink channel quality report (“Msg3 DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.9.14.18.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE under enhanced coverage

Table A.9.14.18.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN TDD Category M1 UE under enhanced coverage

A.9.14.18.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21.24.

## A.10Proximity-based Services in Any Cell Selection State

## A.10.1E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test

## A.10.1.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for ProSe Direct Communication transmissions in Any Cell Selection state defined in clause 11.2.

For this test, the UE is triggered by the test loop function or the upper layers to transmit for ProSe Direct Communication.

The test parameters are given in Table A.10.1.1-1 below. There is no serving cell and one active SyncRef UE in this test. The test system shall emulate the SyncRef UE to transmit SLSS and MIB-SL every synchronization period.

The test system will configure the ProSe UE to transmit SLSS in each period (40ms) by configuring syncTxThreshOoC as +infinity in the pre-configured parameters. The ProSe UE is expected to synchronize to the SyncRef UE and transmit its own SLSS and SL-MIB in accordance to the procedure specified in clause 5.10.7.3 of TS 36.331.

The transmit timing is verified using the transmission timing of SLSS transmissions.

Table A.10.1.1-1: Test parameters for ProSe Transmission Timig Accuracy test for E-UTRAN FDD

## A.10.1.2Test Requirements

For parameters specified in Tables A.10.1.1-1, the timing accuracy for ProSe Direct Communication transmissions shall be within the limits defined in clause 11.2.2. The timing accuracy is verified using SLSS transmissions.

Prior to start of test, test system is required to ensure that the ProSe UE is synchornized to the SyncRef UE 1 and is transmitting SLSS + MIB-SL as derived from the SLSS + MIB-SL of SyncRef UE 1  as per clause 5.10.7.3 of TS 36.331. For the test configuration, the SLSSID used by the ProSe UE shall be 30 with inCoverage IE in MIB-SL set as FALSE.

The following sequence of events shall be used to verify that the requirements are met.

For 5MHz or 10MHz channel bandwith, the test sequence shall be carried out in Any Cell Selection state.

a) After the ProSe UE is synchronized to SyncRef UE 1, the test system shall verify that the ProSe UE SLSS transmission timing offset is within ± 24×TS with respect to the first detected path (in time) of the corresponding frame of SyncRef UE 1.

b) The test system adjusts the transmit timing of SyncRef UE 1 by +24TS compared to that in (a). The test system shall wait for at least one SLSS period (40ms) before verifying the requirement again in (c).

c) The test system shall verify that the UE SLSS transmissiontiming offset stays within ± 24×TS with respect to the first detected path (in time) of the corresponding frame of SyncRef UE 1.

## A.10.2E-UTRAN FDD – Initiation/Cease of SLSS Transmission with ProSe Direct Communication

## A.10.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the evaluation time allowed to initiate and cease SLSS transmissions in Any Cell Selection state defined in clause 11.3.

For this test, the UE is triggered by the test loop function or the upper layers to transmit for ProSe Direct Communication.

The test parameters are given in Table A. X.2.1-1 and Table A.10.2.1-2 below. There are no active cells in this test. There is one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit SLSS and MIB-SL every synchronization period.

Prior to start of test, test system is required to ensure that the ProSe UE is synchornized to the SyncRef UE 1 and is transmitting SLSS + MIB-SL as derived from the SLSS + MIB-SL of SyncRef UE 1  as per clause 5.10.7.3 of TS 36.331. For the test configuration, the SLSSID used by the ProSe UE shall be 30 with inCoverage IE in MIB-SL set as FALSE.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the S-RSRP of SyncRef UE 1 is above syncTxThreshOOC and the UE is not expected to be transmitting SLSS. During T2, the S-RSRP of SyncRef UE 1 is lowered below syncTxThreshOOC and the UE is expected to initiate SLSS transmissions. During T3, the S-RSRP of SyncRef UE 1 is increased back to be above syncTxThreshOOC and the UE is expected to cease SLSS transmissions.

Table A.10.2.1-1: Test parameters for initiation/cease of SLSS transmissions test for E-UTRAN FDD

Table A.10.2.1-2: SyncRef UE specific test parameters for initiation/cease of SLSS transmissions test for E-UTRAN FDD

## A.10.2.2Test Requirements

The SLSS transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the SLSS transmission.

The SLSS transmission initiation delay shall be less than 0.84 s.

The SLSS transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the SLSS transmission.

The SLSS transmission cease delay shall be less than 0.84 s.

The rate of correct initiation/cease delay of SLSS transmissions observed during repeated tests shall be at least 90%.

NOTE:The initiation/cease delay of SLSS transmissions can be expressed as: Tevaluate,SLSS + SLSS period,

Where:

Tevaluate,SLSS is the evaluation time for initiate/cease of SLSS, and is 0.8 sec (clause 11.3.2) for the parameters in this test;

SLSS periodis set as 40ms in this test.

## A.10.3E-UTRAN FDD – SyncRef UE Selection / Reselection Test

## A.10.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection in Any Cell Selection state defined in clause 11.5.

For this test, the UE is triggered by the test loop function or the upper layers to transmit for ProSe Direct Communication.

The test parameters are given in Table A. X.3.1-1 and Table A.10.3.1-2 below. There are no active cells in this test. There are two active SyncRef UEs (SyncRef UE 1 and SyncRef UE 2) in this test. The test system shall emulate SyncRef UE 1 and SyncRef UE 2 to transmit SLSS and MIB-SL every SLSS period (40ms).

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the ProSe UE for its SLSS+MIB-SL transmissions. When the ProSe UE is not synchronized to any SyncRef UE, then the ProSe UE shall use the SLSS ID pre-configured in the ProSe UE. When the ProSe UE is synchronized to a SyncRef UE, the ProSe UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.10.7.3 of TS 36.331.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, both SyncRef UE 1 and SyncRef UE 2 are powered off and the ProSe UE is expected to transmit SLSS as an independent synchronization source. During T1, SyncRef UE 1 is powered ON and the ProSe UE will select SyncRef UE 1 as the synchronization source. During T2, a higher priority SyncRef UE 2 is additionally powered ON and the ProSe UE will reselect to the higher priority SyncRef UE 2 as the synchronization source.

Table A.10.3.1-1: Test parameters for SyncRef UE selection/reselection test for E-UTRAN FDD

Table A.10.3.1-2: SyncRef UE specific test parameters for SyncRef UE selection/reselection test for E-UTRAN FDD

## A.10.3.2Test Requirements

SyncRef UE selection delay is defined as the time from the beginning of T2 to the time UE is synchronized to SyncRef UE 1 and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 168+59 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T2.

The SyncRef UE selection delay shall be less than 20.84sec.

SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2, and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed o 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE reselection delay shall be less than 20.84sec.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90%.

The test system will verify that the ProSe UE does not drop or delay more than 2% of its SLSS transmissions during the duration of T1, T2, and T3.

The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 20sec (as specified in sub-clause 11.5.2.2)

-Tevaluate,SLSS = 0.8 (as specified in sub-clause 11.3.2)

-SLSS period = 40ms

This gives a total of 20.84 seconds.

## A.10.4E-UTRAN FDD – Cell Identification on downlink frequency associated with ProSe frequency (when UE is transmitting for ProSe)

## A.10.4.1Test Purpose and Environment

The purpose of this test is to verify cell identification delay requirement for a newly detectable cell on the downink frequency associated with the pre-configured ProSe carrier frequency in Any Cell Selection state. This test will verify the requirements in clause 11.4 when the UE is transmitting for ProSe.

For this test, the UE is triggered by the test loop function or the upper layers to transmit for ProSe Direct Communication.

The test parameters are given in Table A. 10.4.1-1, Table A. 10.4.1-2, and Table A.10.4.1-3 below. There is one active cell (Cell 1) and active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit SLSS and MIB-SL every SLSS period (40ms).

The test consists of two successive time periods, with time duration of T1 and T2 respectively. During T1, the cell is powered OFF and the ProSe UE is synchronized to SyncRef UE 1. During T2, the cell is powered ON and the ProSe UE will detect the cell and attempt to camp on the cell.

Prior to start of test, test system is required to ensure that the ProSe UE is synchornized to the SyncRef UE 1 and is transmitting SLSS + MIB-SL as derived from the SLSS + MIB-SL of SyncRef UE 1  as per clause 5.10.7.3 of TS 36.331. For the test configuration, the SLSSID used by the ProSe UE shall be 30 with inCoverage IE in MIB-SL set as FALSE.

Table A.10.4.1-1: Test parameters for cell identification test on on downlink frequency associated with ProSe frequency for E-UTRAN FDD (when UE is transmitting for ProSe)

Table A.10.4.1-2: Cell specific test parameters for cell identification test on on downlink frequency associated with ProSe frequency for E-UTRAN FDD (when UE is transmitting for ProSe)

Table A.10.4.1-3: SyncRef UE specific test parameters for cell identification test on on downlink frequency associated with ProSe frequency for E-UTRAN FDD

## A.10.4.2Test Requirements

The cell selection delay to a newly detectable cell on the downlink associated with the preconfigured ProSe carrier is defined as the time from the beginning of T2 to the time UE camps on the cell and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST.

The cell selection delay to a newly detectable cell on the downlink associated with the preconfigured ProSe carrier shall be less than 7.68 s.

The cell selection delay can be expressed as Tbasic_identify_OoC_ProSe Tx_ON + TSI, where

-Tbasic_identify_OoC_ProSe Tx_ON = 6.4sec as specified in sub-clause 11.4.2.2

-TSI = Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case

This gives a total of 7.68 sec.

## A.11V2V Sidelink Communication for V2V Operation on Dedicated V2V Carrier

## A.11.1V2V UE Transmission Timing Accuracy Test

## A.11.1.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for V2V sidelink transmissions specified in clause 12.2.

For this test, the UE is triggered by the test loop function to transmit for V2V sidelink Communication.

Table A.11.1.1-1 defines test parameters for UE transmit timing accuracy tests for V2V. There is one GNSS based synchronization source during the test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.6.1.

The transmit timing accuracy is verified by the UE transmitting PSSCH and PSCCH.

UE is not expected to receive any configuration related to V2V sidelink communication from the serving cell.

The test parameters of pre-configuration for V2V sidelink communication is defined in Table A.3.21.2-1.

Table A.11.1.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for V2V

## A.11.1.2Test requirements

For parameters specified in Tables A.11.1.1-1, the timing accuracy for V2V sidelink transmission shall be within the limits defined in clause 12.2.1. The timing accuracy is verified by using PSSCH and PSCCH transmissions.

The following sequence of events shall be used to verify that the requirements are met:

-After the UE is synchronized to the GNSS synchronization source, the test system shall verify that the UE PSSCH and PSCCH transmission timing offset is within ± 12×TS with respect to the GNSS reference time.

## A.11.2Interruptions due to V2V sidelink communication

## A.11.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements as defined in clause 12.3, related to interruptions due to V2V sidelink communication under the following additional conditions:

-the UE is pre-configured with parameters for enabling the UE to acquire timing synchronization

-the UE has dedicated transmitter chain and dedicated receiver chain for the V2V operation.

This test is applicable for V2V sidelink communication capable UEs that performs independent concurrent E-UTRAN operation in an E-UTRA band and stand-alone V2V sidelink operation in Band 47. If UE supports multiple bands, the UE needs to be tested only with the band with highest frequency.

In the test, the UE under test is configured with PCell on a serving frequency in the E-UTRA band, and is pre-configured with V2V sidelink communication resources for a non-serving frequency in Band 47. The test consists of one active serving cell (cell 1) on the serving RF channel 1, and there is no active cell on RF channel 2. There is no other UE in the test.

UE is not expected to receive any configuration related to V2V sidelink communication from the serving cell. Prior to the start of the test, UE is already synchronized to a GNSS source for V2V sidelink communication. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.6.1.

At the beginning of the test, UE is triggered by the test loop function or the upper layers to receive and transmit V2V sidelink communication. The UE is continuously scheduled with PDSCH traffic on PCell downlink in RF channel 1 for a duration of 1s. The UE is then triggered by the test loop function or the upper layers to stop receiving and transmitting V2V sidelink communication before the end of the test.

The test parameters are given in Table A.11.2.1-1, Table A.11.2.1-2, and Table A.11.2.1-3 below.

Table A.11.2.1-1: Test parameters for interruptions due to V2V sidelink communication

Table A.11.2.1-2: Sidelink communication configuration for interruptions due to V2V

Table A.11.2.1-3: Cell specific test parameters for interruptions due to V2V sidelink communication

## A.11.2.2Test Requirements

The test system shall verify that no interruption is caused to the ACK/NACKs on the serving cell on RF channel 1 during the test.

## A.12

## A.12.1V2X UE Transmission Timing Accuracy Test

## A.12.1.1V2X UE Transmission Timing Accuracy Test for eNB as Timing Reference

## A.12.1.1.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for V2X sidelink transmissions specified in clause 13.2.2, when the downlink timing of the serving cell (RRC_IDLE) or PCell (RRC_CONNECTED) on a non-V2X sidelink carrier is used as timing reference. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X sidelink communication.

Table A.12.1.1.1-1 and A.12.1.1.1-2 define test parameters for UE transmit timing accuracy tests for V2X sidelink Communication. There is one active cell (PCell) in this test. The transmit timing accuracy is verified by using the transmission timing of PSSCH transmissions.

Table A.12.1.1.1-1: V2XSidelink Test Parameters for V2X UE Transmit Timing Accuracy Test for eNB as Timing Reference

Table A.12.1.1.1-2: Cell Test parameters for V2X UE Transmit Timing Accuracy Test for eNB as Timing Reference

## A.12.1.1.2Test requirements

For parameters specified in Tables A.12.1.1.1-1 and A.12.1.1.1-2, the timing accuracy for V2X sidelink transmission shall be within the limits defined in clause 13.2.2. The timing accuracy is verified by using PSSCH transmissions.

## A.12.1.2V2X UE Transmission Timing Accuracy Test for SyncRef UE as Timing Reference

## A.12.1.2.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for V2X sidelink transmissions specified in clause 13.2.3, when SyncRef UE is used as timing reference. For this test, the UE is triggered by the test loop function to transmit for V2X sidelink communication.

Table A.12.1.2.1-1 defines test parameters for UE transmit timing accuracy tests for V2X sidelink Communication. There is one active SyncRef UE in this test without either serving cell and or GNSS signals. Before the test starts, the UE has been synchronized to the SyncRef UE. The transmit timing accuracy is verified by using the transmission timing of PSSCH transmissions.

Table A.12.1.2.1-1: Test parameters for V2X UE Transmit Timing Accuracy Test for SyncRef UE as Timing Reference

## A.12.1.2.2Test Requirements

For parameters specified in Tables A.12.1.2.1-1, the timing accuracy for V2X sidelink transmission shall be within the limits defined in clause 13.2.3. The timing accuracy is verified by using PSSCH transmissions.

## A.12.2Initiation/Cease of SLSS Transmission with V2X Sidelink Communication

## A.12.2.1Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for eNB as Timing Reference

## A.12.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the V2X UE meets the requirements related to the maximum evaluation time allowed to initiate and cease SLSS transmissions defined in clause 13.3.1.1, when the downlink timing of the serving cell (RRC_IDLE) or PCell (RRC_CONNECTED) on a non-V2X sidelink carrier is used as timing reference. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X sidelink Communication.

The test parameters are given in Table A.12.2.1.1-1 and Table A.12.2.1.1-2 below. There is one active cell in this test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the RSRP of the PCell is above syncTxThreshIC and the UE is not expected to be transmitting SLSS. During T2, the RSRP of the PCell is lowered below syncTxThreshIC and the UE is expected to initiate SLSS transmissions. During T3, the RSRP of the PCell is increased back to be above syncTxThreshIC and the UE is expected to cease SLSS transmissions.

Table A.12.2.1.1-1: Test Parameters for Initiation/Cease of SLSS Transmissions Test for eNB as Timing Reference

Table A.12.2.1.1-2: Cell Test Parameters for Initiation/Cease of SLSS Transmissions Test for eNB as Timing Reference

## A.12.2.1.2Test Requirements

The SLSS transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the SLSS transmission.

The SLSS transmission initiation delay shall be less than 0.56 s.

The SLSS transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the SLSS transmission.

The SLSS transmission cease delay shall be less than 0.56 s.

The rate of correct initiation/cease delay of SLSS transmissions observed during repeated tests shall be at least 90%.

NOTE:The initiation/cease delay of SLSS transmissions can be expressed as: Tevaluate,SLSS + SLSS period,

Where:

Tevaluate,SLSS is the evaluation time for initiate/cease of SLSS, and is 0.4 sec (clause 13.3.1.1) for the parameters in this test;

SLSS periodis set as 160ms in this test.

## A.12.2.2Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for SyncRef UE as Timing Reference

## A.12.2.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the evaluation time allowed to initiate and cease SLSS transmissions defined in clause 13.3.1.3, when SyncRef UE is used as timing reference. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X sidelink Communication.

The test parameters are given in Table A.12.2.2.1-1 and Table A.12.2.2.1-2 below. There are neither active cells and nor GNSS signals in this test. There is one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit SLSS and MIB-SL every synchronization period.

Prior to start of test, test system is required to ensure that the V2X UE is synchornized to the SyncRef UE 1 and is transmitting SLSS + MIB-SL as derived from the SLSS + MIB-SL of SyncRef UE 1 as per clause 5.10.7.3 of TS 36.331. For the test configuration, the SLSSID used by the V2X UE shall be 30 with inCoverage IE in MIB-SL set as FALSE. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the S-RSRP of SyncRef UE 1 is above syncTxThreshOOC and the UE is not expected to be transmitting SLSS. During T2, the S-RSRP of SyncRef UE 1 is lowered below syncTxThreshOOC and the UE is expected to initiate SLSS transmissions. During T3, the S-RSRP of SyncRef UE 1 is increased back to be above syncTxThreshOOC and the UE is expected to cease SLSS transmissions.

Table A.12.2.2.1-1: Test Parameters for Initiation/Cease of SLSS Transmissions Test for SyncRef UE as Timing Reference

Table A.12.2.2.1-2: SyncRef UE Specific Test Parameters for Initiation/Cease of SLSS Transmissions Test for SyncRef UE as Timing Reference

## A.12.2.2.2Test Requirements

The SLSS transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the SLSS transmission.

The SLSS transmission initiation delay shall be less than 0.8 s.

The SLSS transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the SLSS transmission.

The SLSS transmission cease delay shall be less than 0.8 s.

The rate of correct initiation/cease delay of SLSS transmissions observed during repeated tests shall be at least 90%.

NOTE:The initiation/cease delay of SLSS transmissions can be expressed as: Tevaluate,SLSS + SLSS period,

Where:

Tevaluate,SLSS is the evaluation time for initiate/cease of SLSS, and is 0.64 sec (clause 13.3.1.3) for the parameters in this test;

SLSS periodis set as 160ms in this test.

## A.12.3V2X Synchronization Reference Selection/Reselection Tests

## A.12.3.1V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

## A.12.3.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 13.4, when GNSS is configured as the highest priority. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in Table A.12.3.1.1-1and A.12.3.1.1-2 below. There are no GNSS signals in this test. There are one active cell (PCell) and two active SyncRef UEs (SyncRef UE 1 and SyncRef UE 2) in this test. The test system shall emulate SyncRef UE 1 and SyncRef UE 2 to transmit SLSS and MIB-SL every SLSS period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its SLSS+MIB-SL transmissions. When the V2X UE is not synchronized to any SyncRef UE, then the V2X UE shall use the SLSS ID pre-configured in the V2X UE. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.10.7.3 of TS 36.331.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, both SyncRef UE 1 and SyncRef UE 2 are powered off and the V2X UE will select PCell as synchronization source. During T2, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as the synchronization source. During T3, a higher priority SyncRef UE 2 is additionally powered ON and the V2X UE will reselect to the higher priority SyncRef UE 2 as the synchronization source.

Table A.12.3.1.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

Table A.12.3.1.1-2: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

Table A.12.3.1.1-3: Cell Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

## A.12.3.1.2Test Requirements

1) During T2, SyncRef UE selection delay is defined as the time from the beginning of T2 to the time UE is synchronized to SyncRef UE 1 and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 168 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T2.

The SyncRef UE selection delay shall be less than 8.8sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 8sec (as specified in sub-clause 13.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 13.3.1.3)

-SLSS period = 160ms

This gives a total of 8.8seconds.

2) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2, and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will still be 0 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE reselection delay shall be less than 2.4sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 1.6sec (as specified in sub-clause 13.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 13.3.1.3)

-SLSS period = 160ms

This gives a total of 2.4seconds.

The test system will verify that the V2X UE does not drop or delay more than 6% of its V2X data and SLSS transmissions during the duration of T2, and does not drop or delay more than 30% of its SLSS transmissions during the duration of T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90%.

## A.12.3.2V2X Synchronization Reference Selection/Reselection Tests for eNB configured as the highest priority

## A.12.3.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 13.4, when eNB is configured as the highest priority. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in Table A.12.3.2.1-1and A.12.3.2.1-2 below. There are no active cells and GNSS is reliable during the whole test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.6.1. There are two active SyncRef UEs (SyncRef UE 1 and SyncRef UE 2) in this test. The test system shall emulate SyncRef UE 1 and SyncRef UE 2 to transmit SLSS and MIB-SL every SLSS period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its SLSS+MIB-SL transmissions. When the V2X UE is not synchronized to any SyncRef UE, then the V2X UE shall use the SLSS ID pre-configured in the V2X UE. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.10.7.3 of TS 36.331.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, both SyncRef UE 1 and SyncRef UE 2 are powered off and the V2X UE will select GNSS as synchronization source. During T2, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as the synchronization source. During T3, a higher priority SyncRef UE 2 is additionally powered ON and the V2X UE will reselect to the higher priority SyncRef UE 2 as the synchronization source.

Table A.12.3.2.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for eNB configured as the highest priority

Table A.12.3.2.1-2: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for eNB configured as the highest priority

## A.12.3.1.2Test Requirements

1) During T2, SyncRef UE selection delay is defined as the time from the beginning of T2 to the time UE is synchronized to SyncRef UE 1 and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 168+59 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T2.

The SyncRef UE selection delay shall be less than 8.8sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 8sec (as specified in sub-clause 11.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 13.3.1.3)

-SLSS period = 160ms

This gives a total of 8.8 seconds.

2) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2, and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed o 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE reselection delay shall be less than 8.8sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 8sec (as specified in sub-clause 11.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 13.3.1.3)

-SLSS period = 160ms

This gives a total of 8.8 seconds.

The test system will verify that the V2X UE does not drop or delay more than 6% of its V2X data and SLSS transmissions during the duration of T2 and T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90%.

## A.12.4Congestion Control Measurement Test for V2X UE

## A.12.4.1Test Purpose and Environment

The purpose of this test is to verify that the V2X UE makes correct reporting of an event. This test will verify the congestion control measurement requirements in section 13.6.

The test parameters are given in Table A.12.4.1-1 and A.12.4.1-2 below. In the measurement control information it is indicated to the V2X UE that event-triggered reporting with Event V1 is used. There are 4 active sidelink UEs in this test. The test system shall emulate the active sidelink UE to transmit PSCCH/PSSCH every 100ms. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During T1, all of active sidelink UEs are powered off. During T2, all of active sidelink UEs are powered on and transmit PSCCH/PSSCH every 100ms.

Table A.12.4.1-1: General test parameters for Congestion Control Measurement Test for V2X UE

Table A.12.4.1-2: Active sidelink UE specific test parameters for Congestion Control Measurement Test for V2X UE

## A.12.4.2Test Requirements

The UE shall not send event V1 triggered measurement reports during T1 and shall send event V1 triggered measurement reports during T2.

The rate of correct events observed during repeated tests shall be at least 98%.

## A.12.5Interruptions due to V2X Sidelink Communication

## A.12.5.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to V2X sidelink communication defined in clause 13.7.1 under the following additional conditions:

-The UE is out of coverage on the V2X sidelink carrier and is associated with a serving cell on a non-V2X sidelink carrier

This test is applicable for V2X sidelink communication capable UEs that support concurrent inter-band E-UTRAN and V2X sidelink operation.

For this test, the UE is triggered by the test loop function or the upper layers to monitor V2X sidelink communication.

The test parameters are given in Table A.12.5.1-1, Table A.12.5.1-2, and Table A.12.5.1-3. The test consists of one active cell (PCell) on the serving RF channel 1, and there are no active cells on RF channel 2. On RF channel 2, the test consists of 8 active Sidelink UEs in this test transmitting V2X sidelink communication.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the V2X sidelink communication transmission from other active Sidelink UEs on the V2X sidelink communication resoruces.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE during T2, and the UE is expected to transmit SidelinkUEInformation indicating v2x-CommRxInterestedFreqList during T2. On reception of SidelinkUEInformation, the test system shall send RRC reconfiguration message to the UE and wait for the UE to repond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformation for up to 2 second, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during V2X sidelink communication (no missed ACK/NACKs are allowed).

Table A.12.5.1-1: Test Parameters for Interruptions due to V2X Sidelink Communication

Table A.12.5.1-2: Slidelink Communication Configuration for Interruptions due to V2X Sidelink Communication

Table A.12.5.1-3: Cell specific test parameters for interruptions due to V2X slidelink communication

## A.12.5.2Test Requirements

The UE shall be continuously scheduled on PCell on RF channel 1 during T3. During T3, 100% of all expected ACK/NACKs shall be transmitted by the V2X UE.

## A.12.6V2X UE Autonomous Resource Selection/Reselection Measurement Test

## A.12.6.1V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements

## A.12.6.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 4 defined in clause 13.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in Table A.12.6.1.1-1and A.12.6.1.1-2 below. There are 20 active V2X sidelink UEs in this test. Both the UE under test and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.6.1. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH every 20ms. At the beginning of whole test, the test equipment shall send one message with a SL-SCH MAC PDU as specified in Clause 6.1.6 in TS 36.321, in order to make sure that the UE under test needs continuously transmit PSCCH/PSSCH.

The test consists of two duration T1 and T2. During T1, the signal from Test Equipement are configured such that the measured PSSCH-RSRP is above the measurement threshold, and the resource occupied by the active V2X sidelink UEs is expected to be excluded in the resource selection procedure. During T2, the signal from Test Equipement are configured such that the measured PSSCH-RSRP is below the measurement threshold, and the resource occupied by the active V2X sidelink UEs is expected to included in the resource selection procedure.

Table A.12.6.1.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements

Table A.12.6.1.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements

## A.12.6.1.2Test Requirements

The test time T1 and T2 should be long enough. The rate of PSSCH transmissions on the resources on subchannel #1 or #3 shall be less than 10% during T1. The rate of PSSCH transmissions on the resources on subchannel #1 or #3 shall be more than 90% during T2.

## A.12.6.2V2X UE Autonomous Resource Selection/Reselection Tests for S-RSSI measurements

## A.12.6.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 4 defined in clause 13.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in Table A.12.6.2.1-1and A.12.6.2.1-2 below. There are 20 active V2X sidelink UEs in this test. Both the UE under test and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.6.1. The test system shall emulate the active sidelink UE to transmit PSCCH/PSSCH every 20ms. At the beginning of whole test, the test equipment shall send one message with a SL-SCH MAC PDU as specified in Clause 6.1.6 in TS 36.321, in order to make sure that the UE under test needs continuely transmit PSCCH/PSSCH.

Table A.12.6.2.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for S-RSSI measurements

Table A.12.6.2.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for S-RSSI measurements

## A.12.6.1.2Test Requirements

The test shall be run for a long enough amount of time. The rate of PSSCH transmissions on the resources on subchannel #1 shall be more than 80%.

## A.12.7V2X Synchronization Reference Selection/Reselection Tests for V2X Carrier Aggregation

## A.12.7.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 13.10, when GNSS is configured as the highest priority.

The test parameters are given in Table A.12.7.1-1and A.12.7.1-2 below. GNSS is configured as the highest priority, and there are no GNSS signals in this test. There are one active cell (PCell) and one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit SLSS and MIB-SL every SLSS period. SyncRef UE1 is operating on a PC5-based V2X channel (RF channel 1), and no active SyncRef UE is operating on another PC5-based V2X channel (RF channel 2). PCell is operating on an E-UTRAN channel (RF channel 3).

For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X sidelink communication both on RF channel 1 and on RF channel 2. RF channel 1 and on RF channel 2 are both included in syncFreqList.

The test system can verify the selection/reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its SLSS+MIB-SL transmissions. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the selected SyncRef UE as defined in clause 5.10.7.3 of TS 36.331 [2].

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. PCell is only powered on during T1. SyncRef UE 1 is only powered on during T3.

During T1, the V2X UE will select PCell as synchronization source. During T3, the V2X UE will select SyncRef UE 1 as the synchronization source and select RF channel 1 as synchronization carrier.

Table A.12.7.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests

Table A.12.7.1-2: SyncRef UE 1 Test Parameters for V2X Synchronization Reference Selection/Reselection Tests

Table A.12.7.1-3: Cell Test Parameters for V2X Synchronization Reference Selection/Reselection Tests

## A.12.7.2Test Requirements

1) During T3, SyncRef UE selection delay is defined as the time from the beginning of T3 to the time UE is synchronized to SyncRef UE 1 and changes its SLSS transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 168 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE selection delay shall be less than 17.44sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + SLSS period

Where

-Tdetect,SyncRef UE = 16sec (as specified in subclause 13.10)

-Tevaluate,SLSS = 1.28sec (as specified in subclause 13.10)

-SLSS period = 160ms

This gives a total of 17.44 seconds.

The test system will verify that the V2X UE does not drop or delay more than 6% of its V2X data and SLSS transmissions during the duration of T3, and does not drop or delay more than 30% of its SLSS transmissions during the duration of T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90%.

## A.12.8Interruptions due to V2X Carrier Aggregation

## A.12.8.1Interruptions on a FDD PCell

## A.12.8.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to V2X carrier aggregation defined in clause 13.7.3, under the following additional conditions:

-The UE is out of coverage on the V2X sidelink carriers and is associated with the PCell on a non-V2X sidelink carrier

For this test, the UE is triggered by the test loop function or the upper layers to monitor and transmit V2X sidelink communication. There are three carriers, including two V2X sidelink carriers (CC2 and CC3) and one E-UTRAN carrier (CC1). Before the test starts the UE is connected to PCell on CC1. The UE uses PCell as synchronization reference for V2X sidelik communication and shall be continuously scheduled in the PCell throughout the whole test.

The test consists of two consecutive time periods, with time duration of T1 and T2, respectively.

At the beginning of T1, the UE receives an RRCConnectionReconfiguration message by which the UE is configured only to monitor and transmit V2X sidelik communication on CC2.

An RRCConnectionReconfiguration message including sl-V2X-ConfigDedicated, by which the UE is configured to monitor and transmit V2X sidelik communication on CC2 and CC3, is sent by the test equipment in subframe #n. The point in time at which the sl-V2X-ConfigDedicated message for adding CC3 for V2X sidelik communication is received at the UE antenna connector defines the start of time period T2.

During T2, the test system will count the missed ACK/NACKs during T2 to verify the allowed interruptions due to V2X CC addition/release.

The test parameters are given in Table A.12.8.1.1-1, Table A.12.8.1.1-2, and Table A.12.8.1.1-3.

Table A.12.8.1.1-1: Test Parameters for Interruptions due to V2X Carrier Aggregation

Table A.12.8.1.1-2: Slidelink Communication Configuration for Interruptions due to V2X Carrier Aggregation

Table A.12.8.1.1-3: Cell Specific Test Parameters for Interruptions due to V2X Carrier Aggregation

## A.12.8.1.2Test Requirements

During T2, an interruption on PCell shall occur no earlier than in subframe (n+5) and no later than in subframe (n + 22), and the total number of missed ACK/NACKs is no more than 4. The ACK/NACK missing shall occur no earlier than in subframe (n+5) and no later than in subframe (n +26).

All of the above test requirements shall be fulfilled in order for the observed CC3 addition delay and PCell interruptions to be counted as correct. The rate of correct observed CC3 addition delay and PCell interruptions during repeated tests shall be at least 90%.

## A.12.8.2Interruptions on a TDD PCell

## A.12.8.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to V2X carrier aggregation defined in clause 13.7.3, under the following additional conditions:

-The UE is out of coverage on the V2X sidelink carriers and is associated with the PCell on a non-V2X sidelink carrier

For this test, the UE is triggered by the test loop function or the upper layers to monitor and transmit V2X sidelink communication. There are three carriers, including two V2X sidelink carriers (CC2 and CC3) and one E-UTRAN carrier (CC1). Before the test starts the UE is connected to PCell on CC1. The UE uses PCell as synchronization reference for V2X sidelik communication and shall be continuously scheduled in the PCell throughout the whole test.

The test consists of two consecutive time periods, with time duration of T1 and T2, respectively.

At the beginning of T1, the UE receives an RRCConnectionReconfiguration message by which the UE is configured only to monitor and transmit V2X sidelik communication on CC2.

An RRCConnectionReconfiguration message including sl-V2X-ConfigDedicated, by which the UE is configured to monitor and transmit V2X sidelik communication on CC2 and CC3, is sent by the test equipment in subframe #n. The point in time at which the sl-V2X-ConfigDedicated message for adding CC3 for V2X sidelik communication is received at the UE antenna connector defines the start of time period T2.

During T2, the test system will count the missed ACK/NACKs during T2 to verify the allowed interruptions due to V2X CC addition/release.

The test parameters are given in Table A.12.8.2.1-1, Table A.12.8.2.1-2, and Table A.12.8.2.1-3.

Table A.12.8.2.1-1: Test Parameters for Interruptions due to V2X Carrier Aggregation

Table A.12.8.2.1-2: Slidelink Communication Configuration for Interruptions due to V2X Carrier Aggregation

Table A.12.8.2.1-3: Cell Specific Test Parameters for Interruptions due to V2X Carrier Aggregation

## A.12.8.2.2Test Requirements

During T2, an interruption on PCell shall occur no earlier than in subframe (n+5) and no later than in subframe (n + 22), and the total number of missed ACK/NACKs is no more than 2. The ACK/NACK missing shall occur no earlier than in subframe (n+5) and no later than in subframe (n +29).

All of the above test requirements shall be fulfilled in order for the observed CC3 addition delay and PCell interruptions to be counted as correct. The rate of correct observed CC3 addition delay and PCell interruptions during repeated tests shall be at least 90%.

## A.13E-UTRAN Standalone Tests for UE Category NB for Satellite Access

## A.13.1RRC_IDLE state for satellite access

## A.13.1.1Cell re-selection for satellite access

## A.13.1.1.1HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage

## A.13.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD and TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.2 for HD-FDD and 4.6B.2.2 for TDD. The TDD requirements are applicable for UEs that support IoT NTN TDD Mode as described in clause 7.10.6 of [31].

The test scenario comprises of one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.13.1.1.1.1-1, A.13.1.1.1.1-2 and A.13.1.1.1.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.1.1.1.1-1: Supported test configurations

Table A.13.1.1.1.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.13.1.1.1.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.13.1.1.1.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

For configuration 1 and 2: 59.32 s.

For configuration 3: 13.53 s

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than:

For configuration 1 and 2: 14.82 s.

For configuration 3: 10.97 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NB-IoT-NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-NC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2 and Table 4.6B.2.2-1 in clause 4.6B.2.2.

Tevaluate, NB_intra_NB-IoT-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2 and Table 4.6B.2.2-1 in clause 4.6B.2.2.

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case for HD-FDD and 8.41s for TDD.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15s for the cell re-selection delay to an already detected cell in the HD-FDD test case.

This gives a total of 13.53 s, allow 14 s for the cell re-selection delay to a newly detectable cell and 10.97 s, allow 11s for the cell re-selection delay to an already detected cell in the TDD test case.

## A.13.1.1.2HD – FDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with serving cell RRM measurement relaxation

## A.13.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.1A when UE is configured to monitor WUS according to Table A.13.1.1.2.1-2 and under the serving cell RRM measurement relaxation according to the subclause 4.6A.2.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.6A.2.2.

The test scenario comprises of one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.13.1.1.2.1-1, A.13.1.1.2.1-2 and A.13.1.1.2.1-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.1.1.2.1-1: Supported test configurations

Table A.13.1.1.2.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.13.1.1.2.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

A.13.1.1.2.2Test Requirements

Before the beginning of T2, UE is under relaxed monitoring where the serving cell measurement is performed every 5.12 s and the infra-frequency measurement for the neighbor cells is relaxed according to subclause 5.2.4.12.0 in TS 36.304 [1].

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 69.56 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate, serv_NB-NC + Tdetect,NB_Intra_NB-IoT-NC + TSI.

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2, based on the configured DRX cycle

Tevaluate, serv_NB-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2, based on the effective DRX cycle after relaxation; 10.24 s is assumed in this test case.

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 69.56 s, allow 70 s for the cell re-selection delay to a newly detectable in the test case.

## A.13.1.1.3HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with UE specific DRX

## A.13.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD and TDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.2 for HD-FDD and 4.6B.2.2 for TDD. The TDD requirements are applicable for UEs that support IoT NTN TDD Mode as described in clause 7.10.6 of [31].

The test scenario comprises of one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.13.1.1.3.1-1, A.13.1.1.3.1-2 and A.13.1.1.3.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2. In Test 1, UE supports the UE specific DRX cycle of 0.32 s and the UE shall be configured with DRX cycle of 0.32 s prior to the start of the test. In Test 2, UE supports the UE specific DRX cycle of 0.64 s and the UE shall be configured with DRX cycle of 0.64 s prior to the start of the test.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.1.1.3.1-1: Supported test configurations

Table A.13.1.1.3.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.13.1.1.3.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.13.1.1.3.2Test Requirements

In each test, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable in test 1 and test 2 cell shall be less than:

For test configuration 1 and 2: 34.32 s ;

For test configuration 3: 13.53 s.

In each test, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected in test 1 and test 2 cell shall be less than:

For test configuration 1 and 2:  13.44 s.

For test configuration 3: 10.97 s

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NC + TSI,

Where:

Tdetect,NB_Intra_NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2 and Table 4.6B.2.2-1 in clause 4.6B.2.2

Tevaluate, NB_intra_NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2 and Table 4.6B.2.2-1 in clause 4.6B.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case for HD-FDD and 8.41 s for TDD.

This gives a total of 34.32 s, allow 35 s for the cell re-selection delay to a newly detectable cell and 13.44 s, allow 14s for the cell re-selection delay to an already detected cell in the HD-FDD test case.

This gives a total of 13.53 s, allow 14 s for the cell re-selection delay to a newly detectable cell and 10.97 s, allow 11s for the cell re-selection delay to an already detected cell in the TDD test case.

## A.13.1.1.4HD – FDD and TDD Inter frequency case for UE Category NB1 Standalone mode in normal coverage

## A.13.1.1.4.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD and TDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.5 for HD-FDD and 4.6B.2.2 for TDD. The TDD requirements are applicable for UEs that support IoT NTN TDD Mode as described in clause 7.10.6 of [31].

The test scenario comprises of 2 cells as given in tables A.13.1.1.4.1-1, A.13.1.1.4.1-2 and A.13.1.1.4.1-3. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.13.1.1.4.1-1: Supported test configurations

Table A.13.1.1.4.1-2: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in normal coverage

Table A.13.1.1.4.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in normal coverage

## A.13.1.1.4.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

For configuration 1 and 2: 59.32 s.

For configuration 3:  13.53 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than:

For configuration 1 and 2: 14.82 s.

For configuration 3: 10.97 s

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6A.2.5-1 in clause 4.6A.2.5 and Table 4.6B.2.5-1 in clause 4.6B.2.5.

Tevaluate, NB_Inter_ECSee Table 4.6A.2.5-1 in clause 4.6A.2.5 and Table 4.6B.2.5-1 in clause 4.6B.2.5.

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case for HD-FDD and 8.41s for TDD.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15 s for the cell re-selection delay to an already detected cell in the HD-FDD test case.

This gives a total of 13.53 s, allow 14 s for the cell re-selection delay to a newly detectable cell and 10.97 s, allow 11s for the cell re-selection delay to an already detected cell in the TDD test case.

## A.13.1.1.5HD – FDD Intra frequency case for UE Category NB1 Standalone mode in enhanced coverage, location-based cell reselection for NGSO

## A.13.1.1.5.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.4.

The test scenario comprises of one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.13.1.1.5.1-1, A.13.1.1.5.1-2 and A.13.1.1.5.1-3. The test consists of 3 successive time periods, with time duration of T0, T1, and T2 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

At 4s after the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SIB31 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.13.1.1.5.1-1: Supported test configurations

Table A.13.1.1.5.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.13.1.1.5.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.13.1.1.5.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from 4s after the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NB-IoT-NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-NC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6A.2.4-1 in clause 4.6A.2.4

Tevaluate, NB_intra_NB-IoT-NCSee Table 4.6A.2.4-1 in clause 4.6A.2.4

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of (66.32+4) s, allow 71 s after T2, for the cell re-selection delay to a newly detectable cell.

## A.13.1.1.6HD – FDD Inter frequency case for UE Category NB1 Standalone mode in enhanced coverage, time-based cell reselection for NGSO

## A.13.1.1.6.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.6.

The test scenario comprises of 2 cells as given in tables A.13.1.1.6.1-1, A.13.1.1.6.1-2 and A.13.1.1.6.1-3. The test consists of 3 successive time periods, with time duration of T0, T1, and T2 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

t-Service broadcasted in SystemInformationBlockType3-NB of Cell 1 is set to the time point that is 67s after start of T2.

Table A.13.1.1.6.1-1: Supported test configurations

Table A.13.1.1.6.1-2: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

Table A.13.1.1.6.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-NB1 UE in enhanced coverage

## A.13.1.1.6.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 66.32 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6A.2.6-1 in clause 4.6A.2.6

Tevaluate, NB_Inter_ECSee Table 4.6A.2.6-1 in clause 4.6A.2.6

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 66.32 s, allow 67 s for the cell re-selection delay to a newly detectable cell.

## A.13.1.1.7HD – FDD Intra frequency case for UE Category NB1 in in-band mode in NTN NR in normal coverage

## A.13.1.1.7.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.2.

The test scenario comprises of one NB-IoT carrier with 2 nCells of different physical cell ID, as given in tables A.13.1.1.7.1-1, A.13.1.1.7.1-2 and A.13.1.1.7.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.1.1.7.1-1: Supported test configurations

Table A.13.1.1.7.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in in-band mode in NTN NR under normal coverage

Table A.13.1.1.7.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in in-band mode in NTN NR under normal coverage

Table A.13.1.1.7.1-4: nrCell 1, nrCell 2 specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-NB1 UE in in-band mode in NTN NR under normal coverage

## A.13.1.1.7.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 59.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 14.82 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NB_Intra_NB-IoT-NC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_intra_NB-IoT-NC + TSI,

Where:

Tdetect,NB_Intra_NB-IoT-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2

Tevaluate, NB_intra_NB-IoT-NCSee Table 4.6A.2.2-1 in clause 4.6A.2.2

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15s for the cell re-selection delay to an already detected cell in the test case.

## A.13.1.1.8HD – FDD Inter-frequency case for UE Category NB1 in-band mode in NTN NR in normal coverage

## A.13.1.1.8.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter-frequency cell reselection requirements for Cat-NB1 UE specified in clause 4.6A.2.5.

The test scenario comprises of 2 cells as given in tables A.13.1.1.8.1-1, A.13.1.1.8.1-2 and A.13.1.1.8.1-3. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. Only nCell1 is already identified by the UE prior to the start of the test, i.e. nCell 2 is not identified. nCell 1 and nCell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing nCell 2.

Table A.13.1.1.8.1-1: Supported test configurations

Table A.13.1.1.8.1-2: General test parameters for HD-FDD inter-frequency cell reselection test case for Cat-NB1 UE in in-band in NTN NR under normal coverage

Table A.13.1.1.8.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD inter-frequency cell reselection test case for Cat-NB1 UE in in-band mode in NTN NR under normal coverage

Table A.13.1.1.8.1-4: nrCell 1, nrCell 2 specific test parameters for HD-FDD inter-frequency cell reselection test case for Cat-NB1 UE in in-band mode in NTN NR under normal coverage

## A.13.1.1.8.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on nCell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 2.

The cell re-selection delay to a newly detectable cell shall be less than 59.32 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on nCell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on nCell 1.

The cell re-selection delay to an already detected cell shall be less than 14.82 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as:  Tdetect,NB_Inter_EC + TSI, and to an already detected cell can be expressed as: Tevaluate, NB_Inter_EC + TSI,

Where:

Tdetect,NB_Inter_ECSee Table 4.6A.2.5-1 in clause 4.6A.2.5

Tevaluate, NB_Inter_ECSee Table 4.6A.2.5-1 in clause 4.6A.2.5

TSIMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 8.32 s is assumed in this test case.

This gives a total of 59.32 s, allow 60 s for the cell re-selection delay to a newly detectable cell and 14.82 s, allow 15 s for the cell re-selection delay to an already detected cell in the test case.

## A.13.2Void

## A.13.3RRC connection mobility control for satellite access

## A.13.3.1RRC re-establishment for satellite access

## A.13.3.1.1HD-FDD and TDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under normal coverage

## A.13.3.1.1.1Test Purpose and Environment

The purpose is to verify that the NB-IoT HD-FDD and TDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5A.

The test parameters are given in table A.13.3.1.1.1-1 and table A.13.3.1.1.1-2 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.3.1.1.1-1: Supported test configurations

Table A.13.3.1.1.1-2: General test parameters for HD-FDD and TDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under normal coverage

Table A.13.3.1.1.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD and TDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under normal coverage

## A.13.3.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT HD-FDD and TDD intra frequency cell shall be less than 10.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 1400 ms

-TSI_NB-IoT = 8320 ms and 8410 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT cell in HD-FDD and TDD respectively.

-TPRACH_NB-IoT = 80 ms; it is the additional delay caused by the random access procedure in HD-FDD and 360ms in TDD.

## A.13.3.1.2HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

## A.13.3.1.2.1Test Purpose and Environment

The purpose is to verify that the NB-IoT FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5A.

The test parameters are given in table A.13.3.1.2.1-1 and table A.13.3.1.2.1-2 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.3.1.2.1-1: Supported test configurations

Table A.13.3.1.2.1-2: General test parameters for HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

Table A.13.3.1.2.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

## A.13.3.1.2.2Test Requirements

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

## A.13.3.1.3HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

## A.13.3.1.3.1Test Purpose and Environment

The purpose is to verify that the NB-IoT HD-FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements for Cat-NB1 UE in clause 6.5A.

The test parameters are given in table A.13.3.1.3.1-1, table A.13.3.1.3.1-2 and table A.13.3.1.3.1-3 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the different frequency carrier. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be indicated with the carrier frequency of nCell 2 to ensure that the UE has the context of the carrier frequency of nCell 2.

Table A.13.3.1.3.1-1: Supported test configurations

Table A.13.3.1.3.1-2: General test parameters for HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

Table A.13.3.1.3.1-3: nCell 1, nCell 2 specific test parameters for HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage

## A.13.3.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NB-IoT HD-FDD inter frequency cell shall be less than 58 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 14800 ms

-TSI_NB-IoT = 41560 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.TPRACH_NB-IoT = 1280 ms; it is the additional delay caused by the random access procedure.

## A.13.3.2Random Access for Satellite Access

This clause provides the list of Random Access test cases for category NB1 UEs when connecting to a NTN cell using satellite access. The list of supported test configurations is provided in Table A.13.3.2-1.

Table A.13.3.2-1: Supported test configurations

## A.13.3.2.1Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage

## A.13.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Normal Coverage is according to the requirements when connected to a NTN NB-IoT cell, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6A.2, Clause 6.6A.3 and Clause 7.20A.2 in an AWGN model.

For this test a single NB-IoT cell is used. The test parameters are given in tables A.13.3.2.1.1-1, A.13.3.2.1.1-2 and A.13.3.2.1.1-3. The UE shall perform timing pre-compensation before the initial NPRACH transmission using AT command-based test approach.

Table A.13.3.2.1.1-1: nCell specific test parameters for HD-FDD and TDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

Table A.13.3.2.1.1-2: NTN specific test parameters for HD-FDD and TDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

Table A.13.3.2.1.1-3: NPRACH-Configuration parameters for HD-FDD and TDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

## A.13.3.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.13.3.2.1.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6A.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 2 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6A.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3B.4 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A.2.

A.13.3.2.1.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6A.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 2 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window. The RA response window shall be started at the point in time indicated by clause 5.1.4 in TS 36.321[17].

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6A.2. The power of the first preamble shall be [-25] dBm with an accuracy specified in clause 6.3B.4 of TS 36.102 [60].The relative power applied to additional preambles shall have an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A.2.

A.13.3.2.1.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6A.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.13.3.2.1.1-3 is reached.

A.13.3.2.1.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.13.3.2.1.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.13.3.2.1.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6A.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.13.3.2.1.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 0. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.13.3.2.2Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in Enhanced Coverage

## A.13.3.2.2.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced Coverage is according to the requirements when connected to a NTN NB-IoT cell, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6A.2, Clause 6.6A.3 and Clause 7.20A.2 in an AWGN model.

For this test a single NB-IoT cell is used. The test parameters are given in tables A.13.3.2.1.1-1, A.13.3.2.1.1-2 and A.13.3.2.1.1-3. The UE shall perform timing pre-compensation before the initial NPRACH transmission using AT command-based test approach.

Table A.13.3.2.2.1-1: nCell specific test parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Enhanced Coverage

Table A.13.3.2.2.1-2: NTN specific test parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Enhanced Coverage

Table A.13.3.2.2.1-4: NPRACH-Configuration parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Enhanced Coverage

## A.13.3.2.2.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.13.3.2.2.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6A.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6A.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 with an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A.2.

A.13.3.2.2.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6A.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window. The RA response window shall be started at the point in time indicated by clause 5.1.4 in TS 36.321[17].

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2A.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 with an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A.2.

A.13.3.2.2.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6A.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.13.3.2.2.1-4 is reached.

A.13.3.2.2.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.13.3.2.2.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.13.3.2.2.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6A.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.13.3.2.2.2.7NPRACH Resource Selection

The UE shall select NPRACH resources and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level Sselection requirement is a prerequisite already assumed for testing the other NPRACH requirements.

## A.13.3.2.3Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs Standalone mode in Enhanced Coverage

## A.13.3.2.3.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Enhanced Coverage is according to the requirements, whether the NPRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6A.2, Clause 6.6A.3 and Clause 7.20A2 in an AWGN model.

For this test a single NB-IoT cell is used. The test parameters are given in tables A.13.3.2.3.1-1, A.13.3.2.3.1-2 and A.13.3.2.3.1-3.

Table A.13.3.2.3.1-1: nCell specific test parameters for HD-FDD contention based random access on non-achor carrier test for UE category NB1 Standalone mode in Enhanced Coverage

Table A.13.3.2.1.3-2: NTN specific test parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

Table A.13.3.2.3.1-3: NPRACH-Configuration parameters for HD-FDD contention based random access on non-anchor carrier test for UE category NB1 Standalone mode in Enhanced Coverage

## A.13.3.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.13.3.2.3.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.6A.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6A.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 with an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A2.

A.13.3.2.3.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.6A.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window. The RA response window shall be started at the point in time indicated by clause 5.1.4 in TS 36.321[17].

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.6A.2. The power of the first preamble shall be 23 dBm for power class 3, 20 dBm for power class 5 with an accuracy specified in clause 6.3B.4 of TS 36.102 [60].

The transmit timing of all NPRACH transmissions shall be within the accuracy specified in Subclause 7.20A2.

A.13.3.2.3.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.6A.2.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of re-transmissions defined by maxNumPreambleAttemptCE in the table A.13.3.2.3.1-3 is reached.

A.13.3.2.3.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.13.3.2.3.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.6A.2.4, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.13.3.2.3.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.6A.2.5, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated NPRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.13.3.2.3.2.7NPRACH Resource Selection

The UE shall select NPRACH resources in non-anchor carrier and transmits or re- transmits NPRACH preambles using the NPRACH resources and NPRACH configuration corresponding to the coverage enhancement level 1. The rate of correct coverage enhancement level selection during repeated tests shall be at least 90%.

Note:Correct coverage enhancement level selection is a prerequisite for testing the other NPRACH requirements.

## A.13.3.2.4Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage for CB-Msg3-EDT procedure

## A.13.3.2.4.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a category NB1 UE in Normal Coverage is according to the requirements when connected to a NTN NB-IoT cell, whether the CB-Msg3 power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the NRSRP measurement and the configured criterion in NRSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.6A.4, 7.20A in an AWGN model.

For this test a single NB-IoT cell is used. The test parameters are given in tables A.13.3.2.4.1-1, A.13.3.2.4.1-2 and A.13.3.2.4.1-3. The UE shall perform timing pre-compensation before the initial CB-Msg3 transmission using AT command-based test approach.

Table A.13.3.2.4.1-1: nCell specific test parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

Table A.13.3.2.4.1-2: NTN specific test parameters for HD-FDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

Table A.13.3.2.4.1-3: NPUSCH Configuration parameters for CB-Msg3 for HD-FDD contention based random access test for UE category NB1 Standalone mode in Normal Coverage

## A.13.3.2.4.2Test Requirements

A.13.3.2.4.2.1Transmitting CB-Msg3

To test the UE behavior specified in subclause 6.6A.4.1, the UE shall calculate the transmission power for the initial CB-Msg3 transmission and [the subsequent CB-Msg3 replica transmissions] according to the formula defined in TS 36.213.

The transmit timing of all CB-Msg3 transmissions shall be within the accuracy specified in Subclause 7.20A.

A.13.3.2.4.2.2receiving a CB-Msg4 over CB-RNTI

To test the UE behavior specified in Subclause 6.6A.4.2.

The System Simulator shall transmit CB-Msg4 that include the backoff indicator field.

The UE shall set the backoff time, according to the CB-Msg3-EDT backoff parameters as described in TS 36.321.

A.13.3.2.4.2.3Reception of an Incorrect CB-Msg4 over CB-RNTI

To test the UE behavior specified in Subclause 6.6A.4.3.

The System Simulator shall send a message addressed to the CB-RNTI with a UE Contention Resolution Identity MAC control element that not matches the CCCH SDU transmitted in the uplink message.

The UE shall re-attempt a CB-Msg3 transmission when the backoff expires in the next CB-Msg3 window with the calculated PUSCH transmission power, until the maximum number of re-transmissions defined by cb-Msg3-MaxAttemptNum-NB-19 in the table A.13.3.2.4.1-3 is reached.

A.13.3.2.4.2.4Reception of a Correct CB-Msg4 over CB-RNTI

To test the UE behavior specified in Subclause 6.6A.4.2.

The System Simulator shall send a message addressed to the CB-RNTI with a UE Contention Resolution Identity MAC control element that matches the CCCH SDU transmitted in the uplink message.

The System Simulator shall allocate and indicate HARQ-ACK resources to the UE.

The UE shall send HARQ-ACK if the Contention Resolution is successful.

## A.13.4Timing and signalling characteristics for satellite access

## A.13.4.1UE transmit timing for satellite access

## A.13.4.1.1E-UTRAN HD-FDD and TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under normal coverage for Satellite Access

## A.13.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under normal coverage is capable of following the frame timing change of the connected eNodeB and that the UE initial transmits timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.20A.

For this test a single NB-IoT cell is used. Test parameters are given in Table A.13.4.1.1.1-1, Table A.13.4.1.1.1-2 and A.13.4.1.1.1-3. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.13.4.1.1.1-1: Supported test configurations

Table A.13.4.1.1.1-2: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage for Satellite AccessAccess

Table A.13.4.1.1.1-3: Cell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage for Satellite Access

## A.13.4.1.1.2Test Requirements

For parameters specified in Tables A.13.4.1.1.1-1, A.13.4.1.1.1-2 and A.13.4.1.1.1-3. the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.20A.2.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED:

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤ ×TS   ± (97×TS – TGNSS_margin)) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.(NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

is calculated based on the generated UL channel with time varying Doppler and delay shifts.NTA, UE-specific

b) Using the value of n measured in a), the test system adjusts the downlink transmit timing for the cell:

-if n < 0, by +(144 – |n|)TS compared to that in (a).

-if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c) Immediately after (b), the test system sends NPDCCH including uplink grant for NPUSCH transmission and immediately after receiving NPUSCH the test system repeatedly sends NPDCCH including uplink grant for NPUSCH transmission until the UE transmit timing offset is within ×TS   ± (97×TS – TGNSS_margin)  with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. The test system shall verify that the difference in timing between the first NPUSCH transmission in step c) and the NPUSCH transmission in step a) shall be not greater than the maximum amount of the magnitude of the timing change in one adjustment requirement in clause 7.20.2. Using the first NPUSCH transmission in step c) and subsequent NPUSCH transmissions. The test system shall verify that the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.20A.2 until the UE transmit timing offset is within ×TS   ± (97×TS – TGNSS_margin)  with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.(NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)(NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)

d) The test system the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within ×TS   ± (97×TS– TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1.NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific

## A.13.4.1.2E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage for Satellite Access

## A.13.4.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under enhanced coverage is capable of following the frame timing change of the connected eNode B, that the UE initial transmit timing accuracy is within the specified limits and that the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission. This test will verify the requirements in clause 7.20A.

For this test a single NB-IoT cell is used. Test parameters are given in Table A.13.4.1.2.1-1 and Table A.13.4.1.2.1-2, Table A.13.4.1.2.1-3 and Table A.13.4.1.2.1-4. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.13.4.1.2.1-1: Supported test configurations

Table A.13.4.1.2.1-2: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage for Satellite Access

Table A.13.4.1.2.1-3: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage for Satellite Access

Table A.13.4.1.2.1-4: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 for E-UTRAN HD-FDD Category NB1 UE Standalone mode under enhanced coverage for Satellite Access

## A.13.4.1.2.2Test Requirements

For parameters specified in Tables A.13.4.1.2.1-1, Tables A.13.4.1.2.1-2, Tables A.13.4.1.2.1-3 and Tables A.13.4.1.2.1-4, the initial transmit timing accuracy shall be within the limits defined in clause 7.20A.2 and the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 2048 ms (Tests 2):

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤×TS   ± (97×TS – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.(NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

is calculated based on the generated UL channel with time varying Doppler and delay shifts.NTA, UE-specific

b) The test system sends NPDCCH including uplink grant for NPUSCH transmission. After 16ms from the initial NPUSCH transmission, the test system adjusts the downlink transmit timing for the cell, using the value of n measured in a),

- if n < 0, by +(144 – |n|)TS compared to that in (a).

- if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c)For test 2, the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within (×TS   ± (97×TS– TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1. The UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)

## A.13.4.1.3E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage with segment transmission in NGSO for Satellite Access

## A.13.4.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE, which is not supporting the capability of ntn-SegmentedPrecompensationGaps-r17, under enhanced coverage is capable of following the frame timing change of the connected eNode B, that the UE initial transmit timing accuracy is within the specified limits and that the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission or at the start of a transmission segment boundary. This test will verify the requirements in clause 7.20A.

For this test a single NB-IoT cell is used. Test parameters are given in Table A.13.4.1.3.1-1 and Table A.13.4.1.3.1-2. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.13.4.1.3.1-1: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage for Satellite Access

Table A.13.4.1.3.1-2: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage for Satellite Access

## A.13.4.1.3.2Test Requirements

For parameters specified in Tables A.13.4.1.3.1-1, and Tables A.13.4.1.3.1-2, the initial transmit timing accuracy shall be within the limits defined in clause 7.20A.2 and the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission or at the start of a transmission segment boundary.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1):

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) of the first transmission in each segment and verify that it is within Te (nTs ≤(×TS   ± (97×TS – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.NTA_Ref+NTAoffset+NTA,common+NTA, UE-specific)

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

is calculated based on the generated UL channel with time varying Doppler and delay shifts.NTA, UE-specific

b) The test system sends NPDCCH including uplink grant for NPUSCH transmission. After 16ms from the initial NPUSCH transmission, the test system adjusts the downlink transmit timing for the cell, using the value of n measured in a),

- if n < 0, by +(144 – |n|)TS compared to that in (a).

- if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

## A.13.4.2UE timing advance for satellite access

## A.13.4.2.1HD-FDD and TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Normal Coverage for Satellite Access

## A.13.4.2.1.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN Timing Advance adjustment accuracy requirements for UE category NB1 in normal coverage, defined in clause 7.22A.2.2, in an AWGN model.

The test parameters are given in tables A.13.4.2.1.1-1 A.13.4.2.1.1-2 and A.13.4.2.1.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and the UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 16.1.2 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.13.4.2.1.1-3. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the NPUSCH sent from the UE.

As specified in Clause 7.22A.2.1, the UE adjusts its uplink timing at sub-frame n+12+ k-Offset-r17+1 for a timing advance command received in sub-frame n, where sub-frame n refers to the last subframe in the repetition period in which the MAC control element containing timing advance command was received and k-Offset-r17 is specified in [2]. In addition, the UE shall not apply a TA command during an uplink repetition period. The timing advance adjustment accuracy is verified via the uplink transmission of NPUSCH carrying ACK/NACK response to the NPDSCH carrying TA command. k0 in ACK/NACK resource filed in DCI is set as 13.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.13.4.2.1.1-1: Supported test configurations

Table A.13.4.2.1.1-2: General Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Normal Coverage for Satellite Access

Table A.13.4.2.1.1-3: Cell specific Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Normal Coverage for Satellite Access

## A.13.4.2.1.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at subframe n+12+ k-Offset-r17+1, where subframe n is the last subframe in the repetition period of NPDSCH in which the timing advance command is received by the UE.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.22A.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.13.4.2.2HD-FDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhance Coverage for Satellite Access

## A.13.4.2.2.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN Timing Advance adjustment accuracy requirements for UE category NB1 in enhanced coverage, defined in clause 7.22A.2.2, in an AWGN model.

The test parameters are given in tables A.13.4.2.2.1-1, A.13.4.2.2.1-2and A.13.4.2.2.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and the UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 16.1.2 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.13.4.2.2.1-3. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the NPUSCH sent from the UE.

As specified in Clause 7.22A.2.1, the UE adjusts its uplink timing at sub-frame n+12+ k-Offset-r17+1 for a timing advance command received in sub-frame n, where sub-frame n refers to the last subframe in the repetition period in which the MAC control element containing timing advance command was received and k-Offset-r17 is specified in [2]. In addition, the UE shall not apply a TA command during an uplink repetition period. The timing advance adjustment accuracy is verified via the uplink transmission of NPUSCH carrying ACK/NACK response to the NPDSCH carrying TA command. k0 in ACK/NACK resource filed in DCI is set as 13.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.13.4.2.2.1-1: Supported test configurations

Table A.13.4.2.2.1-2: General Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage for Satellite Access

Table A.13.4.2.2.1-3: Cell specific Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage for Satellite Access

## A.13.4.2.2.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at subframe n+12+ k-Offset-r17+1, where subframe n is the last subframe in the repetition period of NPDSCH in which the timing advance command is received by the UE.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.22A.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.13.4.3Radio Link Monitoring for satellite access

## A.13.4.3.1HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage

## A.13.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD and TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23A for HD-FDD and in clause 7.23B for TDD.

The test parameters are given in Tables A.13.4.3.1.1-1, A.13.4.3.1.1-2, A.13.4.3.1.1-3, A.13.4.3.1.1-4 and A.13.4.3.1.1-5. nCell 1 is the active NB-IoT SAN PCell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during the period from (B+dT/2) to the end of T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF before the end of T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.1.1-1: Supported test configurations

Table A.13.4.3.1.1-2: General test parameters for HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.1.1-3: nCell specific test parameters for HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.1.1-4: DRX-Configuration for HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.1.1-5: TimeAlignmentTimer -Configuration for NB-IoT HD-FDD and TDD out-of-sync testing for UE category NB1 Standalone mode in normal coverage

Figure A.13.4.3.1.1-1: SNR variation for out-of-sync testing in DRX for NB-IoT HD-FDD and TDD out-of-sync testing for UE category NB1 Standalone mode in normal coverage

## A.13.4.3.1.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.2HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

## A.13.4.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23A.

The test parameters are given in Tables A.13.4.3.2.1-1, A.13.4.3.2.1-2, A.13.4.3.2.1-3, A.13.4.3.2.1-4 and A.13.4.3.2.1-5. nCell 1 is the active NB-IoT SAN PCell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during the period from (B+dT/2) to the end of T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF before the end of T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.2.1-1: Supported test configurations

Table A.13.4.3.2.1-2: General test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.2.1-3: nCell specific test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.2.1-4: DRX-Configuration for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.2.1-5: TimeAlignmentTimer -Configuration for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

Figure A.13.4.3.2.1-1: SNR variation for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage

## A.13.4.3.2.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4.

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.3HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Enhanced Coverage

## A.13.4.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23A.

The test parameters are given in Tables A.13.4.3.3.1-1, A.13.4.3.3.1-2, A.13.4.3.3.1-3, A.13.4.3.3.1-4 and A.13.4.3.3.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps.  Figure A.13.4.3.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR1.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [3]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.3.1-1: Supported test configurations

Table A.13.4.3.3.1-2: General test parameters for HD-FDD in-sync test with DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.3.1-3: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test with DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.3.1-4: DRX-Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.3.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 Standalone mode in enhanced coverage

Figure A.13.4.3.3.1-1: SNR variation for in-sync testing with DRX

## A.13.4.3.3.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.4HD-FDD and TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Normal Coverage

## A.13.4.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD and TDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23A for HD-FDD and in clause 7.23B for TDD.

The test parameters are given in Tables A.13.4.3.4.1-1, A.13.4.3.4.1-2, A.13.4.3.4.1-3, A.13.4.3.4.1-4 and A.13.4.3.4.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 are as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR1.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [2]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.4.1-1: Supported test configurations

Table A.13.4.3.4.1-2: General test parameters for HD-FDD and TDD in-sync test with DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.4.1-3: nCell 1 specific test parameters for HD-FDD and TDD in-sync radio link monitoring test with DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.4.1-4: DRX-Configuration for E-UTRAN HD-FDD and TDD in-sync tests with DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.4.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD and TDD in-sync tests with DRX for UE category NB1 Standalone mode in normal coverage

Figure A.13.4.3.4.1-1: SNR variation for in-sync testing with DRX

## A.13.4.3.4.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.5HD-FDD and TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage

## A.13.4.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD and TDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23A for HD-FDD and in clause 7.23B for TDD.

The test parameters are given in Tables A.13.4.3.5.1-1, A.13.4.3.5.1-2, A.13.4.3.5.1-3, and A.13.4.3.5.1-4. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.5.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR1.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.5.1-1: Supported test configurations

Table A.13.4.3.5.1-2: General test parameters for HD-FDD and TDD in-sync test without DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.5.1-3: nCell 1 specific test parameters for HD-FDD and TDD in-sync radio link monitoring test without DRX for UE category NB1 Standalone mode in normal coverage

Table A.13.4.3.5.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD and TDD in-sync tests without DRX for UE category NB1 Standalone mode in normal coverage

Figure A.13.4.3.5.1-1: SNR variation for in-sync testing without DRX

## A.13.4.3.5.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.6HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage

## A.13.4.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23A.

The test parameters are given in Tables A.13.4.3.6.1-1, A.13.4.3.6.1-2, A.13.4.3.6.1-3, and A.13.4.3.6.1-4. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.6.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR1.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.6.1-1: Supported test configurations

Table A.13.4.3.6.1-2: General test parameters for HD-FDD in-sync test without DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.6.1-3: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test without DRX for UE category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.6.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests without DRX for UE category NB1 Standalone mode in enhanced coverage

Figure A.13.4.3.6.1-1: SNR variation for in-sync testing without DRX

## A.13.4.3.6.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.7HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage

## A.13.4.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD and TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23A for HD-FDD and 7.23B for TDD.

The test parameters are given in Tables A.13.4.3.7.1-1, Tables A.13.4.3.7.1-2 and A.13.4.3.7.1-3. nCell1 is the active NB-IoT SAN PCell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.7.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during the period from (B+dT/2) to the end of T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF before the end of T3.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.7.1-1: Supported test configurations

Table A.13.4.3.7.1-2: General test parameters for HD-FDD and TDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Standalone mode in normal coverage

Table A.13.4.3.7.1-3: nCell1 specific test parameters for HD-FDD and TDD sRadio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Standalone mode in normal coverage

Figure A.13.4.3.7.1-1: SNR variation for out-of-sync testing

## A.13.4.3.7.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.13.4.3.8HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage

## A.13.4.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23A.

The test parameters are given in Tables A.13.4.3.8.1-1, A.13.4.3.8.1-2 and A.13.4.3.8.1-3 below. nCell1 is the active NB-IoT SAN PCell, in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.8.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure.

-Before the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 with duration dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH.

Note:The UE is expected to decode NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 with duration dT

-During T3, the SNR is kept at SNR3.

Note:The UE is expected to detect OOS and declare RLF during the period from (B+dT/2) to the end of T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with duration dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct the UL transmission during T4 since the UE is expected to declare RLF before the end of T3.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.8.1-1: Supported test configurations

Table A.13.4.3.8.1-2: General test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Standalone mode in enhanced coverage

Table A.13.4.3.8.1-3: nCell1 specific test parameters for  HD-FDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Standalone mode in enhanced coverage

Figure A.13.4.3.8.1-1: SNR variation for out-of-sync testing

## A.13.4.3.8.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behave correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

In the following section, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

## A.13.4.3.9HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 in-band mode in NTN NR in Enhanced Coverage

## A.13.4.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT SAN PCell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23A.

The test parameters are given in Tables A.13.4.3.9.1-1, A.13.4.3.9.1-2 and A.13.4.3.9.1-3 below. nCell1 is the active NB-IoT SAN PCell, in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.13.4.3.8.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure.

-Before the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 with duration dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH.

Note:The UE is expected to decode NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 with duration dT

-During T3, the SNR is kept at SNR3.

Note:The UE is expected to detect OOS and declare RLF during the period from (B+dT/2) to the end of T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with duration dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct the UL transmission during T4 since the UE is expected to declare RLF before the end of T3.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.4.3.9.1-1: Supported test configurations

Table A.13.4.3.9.1-2: General test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 in-band mode in NTN NR in enhanced coverage

Table A.13.4.3.9.1-3: nCell1 specific test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 in-band mode in NTN NR in enhanced coverage

Table A.13.4.3.9.1-3: nrCell 1 specific test parameters for HD-FDD out-of-sync radio link monitoring test without DRX for UE category NB1 in-band mode in NTN NR in enhanced coverage

Figure A.13.4.3.9.1-1: SNR variation for out-of-sync testing

## A.13.4.3.9.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behave correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

In the following section, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

## A.13.5UE measurement procedures in RRC_CONNECTED state for UE category NB1 for satellite access

## A.13.5.1HD-FDD and TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

## A.13.5.1.1Test Purpose and Environment

The purpose is to verify that the NB-IoT intra-frequency neighbour cell measurement requirement in clause 8.14A.6.3 and 8.14B.6.3 is met.

The test parameters are given in table A.13.5.1.1-1, table A.13.5.1.1-2 and table A.13.5.1.1-3 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively.

Table A.13.5.1.1-1: Supported test configurations

Table A.13.5.1.1-2: General test parameters for HD-FDD and TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

Table A.13.5.1.1-3: General test parameters for HD-FDD and TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage

A.13.5.1.2Test Requirements

UE shall trigger RLF during T4 and complete neighbour cell measurement before end of T4. UE shall start to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2 before the end of T5 to fulfil the RRC re-establishment delay to a known NB-IoT FDD intra frequency cell.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 0 ms

-TSI_NB-IoT = 8320 and 8410 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD and TDD cell, respectively.

-TPRACH_NB-IoT = 80 and 360 ms; it is the additional delay caused by the random access procedure for the target NB-IoT FDD and TDD cell, respectively.

## A.13.5.2HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

## A.13.5.2.1Test Purpose and Environment

The purpose is to verify that the NB-IoT inter-frequency neighbour cell measurement requirement in clause 8.14A.6.3 and 8.14B.6.3 is met.

The test parameters are given in table A.13.5.2.1-1, table A.13.5.2.1-2, table A.13.5.2.1-3 and table A.13.5.2.1-4 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the different frequency carriers. The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively.

Table A.13.5.2.1-1: Supported test configurations

Table A.13.5.2.1-2: General test parameters for HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

Table A.13.5.2.1-3: General test parameters for HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

Table A.13.5.2.1-4: DRX-Configuration for HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

A.13.5.2.2 Test Requirements

UE shall trigger RLF during T4 and complete neighbour cell measurement before end of T4. UE shall start to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2 before the end of T5 to fulfil the RRC re-establishment delay to a known NB-IoT FDD inter frequency cell.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 0 ms

-TSI_NB-IoT = 8320 and 8410 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD and TDD cell, respectively.

-TPRACH_NB-IoT = 80 and 360 ms; it is the additional delay caused by the random access procedure for the target NB-IoT FDD and TDD cell, respectively.

## A.13.5.3HD-FDD and TDD Intra-frequency location-based neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

## A.13.5.3.1Test Purpose and Environment

The purpose is to verify that the NB-IoT intra-frequency neighbour cell measurement requirement in clause 8.14A.6.3 and 8.14B.6.3 is met.

The test parameters are given in table A.13.5.3.1-1, table A.13.5.3.1-2 and table A.13.5.3.1-3 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 4 successive time periods, with time duration of T1, T2, T3, T4 respectively.

At the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SystemInformationBlockType31-NB of nCell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.13.5.3.1-1: Supported test configurations

Table A.13.5.3.1-2: General test parameters for HD-FDD and TDD Intra-frequency location-based neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access

Table A.13.5.3.1-3: General test parameters for HD-FDD and TDD location-based Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage

## A.13.5.3.2Test Requirements

UE shall trigger RLF during T3 and complete neighbour cell measurement before end of T3. UE shall start to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2 before the end of T4 to fulfil the RRC re-establishment delay to a known NB-IoT FDD intra frequency cell.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 0 ms

-TSI_NB-IoT = 8320 and 8410 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD and TDD cell, respectively.

-TPRACH_NB-IoT = 80 and 360 ms; it is the additional delay caused by the random access procedure for the target NB-IoT FDD and TDD cell, respectively.

## A.13.5.4HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access

## A.13.5.4.1Test Purpose and Environment

The purpose is to verify that the NB-IoT intra-frequency neighbour cell measurement requirement in clause 8.14A.6.3 is met.

The test parameters are given in table A.13.5.4.1-1, table A.13.5.4.1-2 and table A.13.5.4.1-3 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the same frequency carrier. The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively.

Table A.13.5.4.1-1: Supported test configurations

Table A.13.5.4.1-2: General test parameters for HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access

Table A.13.5.4.1-3: General test parameters for HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode in NTN NR under normal coverage

Table A.13.5.4.1-4: nrCell 1 and nrCell2 specific test parameters for HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in In-Band mode in NTN NR under normal coverage

## A.13.5.4.2Test Requirements

UE shall trigger RLF during T4 and complete neighbour cell measurement before end of T4. UE shall start to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2 before the end of T5 to fulfil the RRC re-establishment delay to a known NB-IoT FDD intra frequency cell.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 0 ms

-TSI_NB-IoT = 8320 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

-TPRACH_NB-IoT = 80 ms; it is the additional delay caused by the random access procedure.

## A.13.5.5HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access

## A.13.5.5.1Test Purpose and Environment

The purpose is to verify that the NB-IoT inter-frequency neighbour cell measurement requirement in clause 8.14A.6.3 is met.

The test parameters are given in table A.13.5.5.1-1, table A.13.5.5.1-2, table A.13.5.5.1-3, table A.13.5.5.1-4 and table A.13.5.5.1-5 below. nCell1 and nCell2 are NB-IoT cells with different physical cell ID on the different frequency carriers. The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively.

Table A.13.5.5.1-1: Supported test configurations

Table A.13.5.5.1-2: General test parameters for HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access

Table A.13.5.5.1-3: General test parameters for HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode under in NTN NR normal coverage for Satellite Access

Table A.13.5.5.1-4: nrCell 1 and nrCell2 specific test parameters for HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage

Table A.13.5.5.1-5: DRX-Configuration for HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access

## A.13.5.5.2Test Requirements

UE shall trigger RLF during T4 and complete neighbour cell measurement before end of T4. UE shall start to send NPRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2 before the end of T5 to fulfil the RRC re-establishment delay to a known NB-IoT FDD inter frequency cell.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE-re-establish_delay_NB-IoT.

Where:

-TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The NPRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

-TUE-re-establish_delay_NB-IoT = 100 ms + NNB-Iot-freq*Tsearch_NB-IoT + TSI_NB-IoT + TPRACH_NB-IoT

-NNB-Iot-freq = 1

-Tsearch_NB-IoT = 0 ms

-TSI_NB-IoT = 8320 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target NB-IoT FDD cell.

-TPRACH_NB-IoT = 80 ms; it is the additional delay caused by the random access procedure.

## A.13.6Measurement performance requirements for UE for satellite access

## A.13.6.1Void

## A.13.6.2Channel quality reporting accuracy for satellite access

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.13.6.2.1: Supported test configurations

## A.13.6.2.1E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage

## A.13.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for HD-FDD and the requirements in section 9.1.22B.8 for TDD NB-IoT SAN PCell

## A.13.6.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.13.6.2.1.2-1 and A.13.6.2.1.2-2.

Table A.13.6.2.1.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

Table A.13.6.2.1.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

## A.13.6.2.1.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8 for HD-FDD and in section 9.1.22B.8 for TDD.

## A.13.6.2.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage

## A.13.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for NB-IoT SAN PCell.

## A.13.6.2.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.13.6.2.2.2-1 and A.13.6.2.2.2-2.

Table A.13.6.2.2.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.13.6.2.2.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

## A.13.6.2.2.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8.

## A.13.6.2.3E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage

## A.13.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy on non-anchor carrier is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for HD-FDD and the requirements in section 9.1.22B.8 for TDD NB-IoT SAN PCell.

## A.13.6.2.3.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy on non-anchor carrier is tested by using the parameters in Tables A.13.6.2.3.2-1 and A.13.6.2.3.2-2.

Table A.13.6.2.3.2-1: General Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

Table A.13.6.2.3.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

## A.13.6.2.3.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8 for HD-FDD and in section 9.1.22B.8 for TDD.

## A.13.6.2.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage

## A.13.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy on non-anchor carrier is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for NB-IoT SAN PCell.

## A.13.6.2.4.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MSG3-based downlink channel quality reporting accuracy on non-anchor carrier is tested by using the parameters in Tables A.13.6.2.4.2-1 and A.13.6.2.4.2-2.

Table A.13.6.2.4.2-1: General Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.13.6.2.4.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test on non-anchor carrier for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

## A.13.6.2.4.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8.

## A.13.6.2.5E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under normal coverage

A.13.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for HD_FDD and in section 9.1.22B.8 for TDD NB-IoT SAN PCell.

## A.13.6.2.5.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The tests consist of two successive time periods of length T1 and T2, respectively, at different SNR levels. The start of T2 coincides with the start of the channel quality measurement period specified in section 8.14.4. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.13.6.2.5.2-1 and A.13.6.2.5.2-2.

Table A.13.6.2.5.2-1: General Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

Table A.13.6.2.5.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD and TDD Category NB1 UE in Standalone mode under normal coverage

## A.13.6.2.5.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8 for HD-FDD and in section 9.1.22B.8 for TDD.

## A.13.6.2.6E-UTRAN HD-FDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under enhanced coverage

## A.13.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in Section 9.1.22A.8 for NB-IoT SAN PCell.

## A.13.6.2.6.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The tests consist of two successive time periods of length T1 and T2, respectively, at different SNR levels. The start of T2 coincides with the start of the channel quality measurement period specified in section 8.14.4. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.13.6.2.6.2-1 and A.13.6.2.6.2-2.

Table A.13.6.2.6.2-1: General Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

Table A.13.6.2.6.2-2: nCell specific Test Parameters for Downlink channel quality reporting accuracy test in RRC_CONNECTED for E-UTRAN HD-FDD Category NB1 UE in Standalone mode under enhanced coverage

## A.13.6.2.6.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.22A.8.

## A.14E-UTRAN Standalone Tests for UE Category M1 for Satellite Access

## A.14.1RRC_IDLE state for satellite access

## A.14.1.1Cell re-selection for satellite access

## A.14.1.1.1E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage

## A.14.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.7A.2.1.2.

The supported test configurations are provided in Table A.14.1.1.1.1-1.

Table A.14.1.1.1.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.14.1.1.1.1-2 and A.14.1.1.1.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.1.1-2: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.1.1-3: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.1.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7A.2.1.2-1 in clause 4.7A.2.1

Tevaluate,EUTRAN_Intra_NC See Table 4.7A.2.1.2-1 in clause 4.7A.2.1

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; [1280] ms is assumed in this test case. This include the time to acquire satellite assistance information (ephemeris, common delay, etc) conveyed in NB-SystemInformation-31, when the test is performed for configuration 1 (GSO) and no satellite assistance information is conveyed for the target cell by the current serving cell.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.14.1.1.2E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage

## A.14.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.7A.2.1.2.

The supported test configurations are provided in Table A.14.1.1.2.1-1.

Table A.14.1.1.1.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.14.1.1.2.1-2 and A.14.1.1.2.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.2.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.2.1-3: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.2.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7A.2.1.2-1 in clause 4.7A.2.1

Tevaluate,EUTRAN_Intra_NC See Table 4.7A.2.1.2-1 in clause 4.7A.2.1

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; [1280] ms is assumed in this test case. This include the time to acquire satellite assistance information (ephemeris, common delay, etc) conveyed in NB-SystemInformation-31, when the test is performed for configuration 1 (GSO) and no satellite assistance information is conveyed for the target cell by the current serving cell.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s, allow 8 s for the cell re-selection delay to an already detected cell in the test case.

## A.14.1.1.3E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation

## A.14.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage specified in clause 4.2.2.3 when UE is configured to monitor WUS according to Table A.14.1.1.3.1-2 and under the serving cell RRM measurement relaxation according to the subclause 4.7A.2.1.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.7A.2.1.2.

The supported test configurations are provided in Table A.14.1.1.1.1-1.

Table A.14.1.1.1.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.14.1.1.3.1-2 and A.14.1.1.3.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.3.1-2: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.3.1-3: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.3.2Test Requirements

Before the beginning of T2, UE is under relaxed monitoring where the serving cell measurement is performed every 5.12 s and the infra-frequency measurement for the neighbor cells is relaxed according to subclause 5.2.4.12.0 in TS 36.304 [1].

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than [TBD] s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than [TBD] s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7A.2.1.2-1 in clause 4.7A.2.1 based on the configured DRX cycle

Tevaluate,EUTRAN_Intra_NC See Table 4.7A.2.1.2-1 in clause 4.7A.2.1 based on the effective DRX cycle after relaxation; [TBD] s is assumed in this test case.

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; [1280] ms is assumed in this test case. This include the time to acquire satellite assistance information (ephemeris, common delay, etc) conveyed in NB-SystemInformation-31, when the test is performed for configuration 1 (GSO) and no satellite assistance information is conveyed for the target cell by the current serving cell.

This gives a total of [TBD] s, allow [TBD] s for the cell re-selection delay to a newly detectable cell and [TBD] s, allow [TBD] s for the cell re-selection delay to an already detected cell in the test case.

## A.14.1.1.4E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation

## A.14.1.1.4.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE specified in clause 4.2.2.3 when UE is configured to monitor WUS according to Table A.14.1.1.4.1-2 and under the serving cell RRM measurement relaxation according to the subclause 4.7.2.1.1A and under the intra-frequency neighbor cell measurement relaxation according to the subclause 4.7.2.1.2.

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.14.1.1.4.1-2 and A.14.1.1.4.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.4.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.4.1-3: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.4.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than [TBD] s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than [TBD] s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC, and to an already detected cell can be expressed as: Tevaluate,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC,

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7A.2.1.2-1 in clause 4.7A.2.1 based on the configured DRX cycle

Tevaluate,EUTRAN_Intra_NC See Table 4.7A.2.1.2-1 in clause 4.7A.2.1 based on the effective DRX cycle after relaxation; [TBD] s is assumed in this test case.

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; [1280] ms is assumed in this test case. This include the time to acquire satellite assistance information (ephemeris, common delay, etc) conveyed in NB-SystemInformation-31, when the test is performed for configuration 1 (GSO) and no satellite assistance information is conveyed for the target cell by the current serving cell.

This gives a total of [TBD] s, allow [TBD] s for the cell re-selection delay to a newly detectable cell and [TBD] s, allow [TBD] s for the cell re-selection delay to an already detected cell in the test case.

## A.14.1.1.5E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage

## A.14.1.1.5.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter frequency cell reselection requirements for category M1 UE in normal coverage for satellite access specified in clause 4.7A.2.1.3.

The supported test configurations are provided in Table A.14.1.1.5.1-1.

Table A.14.1.1.5.1-1: Supported test configurations

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.14.1.1.5.1-2 and A.14.1.1.5.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.14.1.1.5.1-2: General test parameters for FDD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.5.1-3: Cell specific test parameters for FDD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.5.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN_Inter_NC + TSI-EUTRA-M1-NC , and to lower priority cell can be expressed as: Tevaluate, E-UTRAN_Inter_NC + TSI-EUTRA-M1-NC,

Where:

Thigher_priority_searchSee clause 4.7A.2.1.3

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7A.2.1.3-1 in clause 4.7A.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.14.1.1.6E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage

## A.14.1.1.6.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for category M1 UE in normal coverage for satellite access specified in clause 4.7A.2.1.3.

The supported test configurations are provided in Table A.14.1.1.6.1-1.

Table A.14.1.1.6.1-1: Supported test configurations

The test scenario comprises of 2 E-UTRA carriers and 2 cells as given in tables A.14.1.1.6.1-2 and A.14.1.1.6.1-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.14.1.1.6.1-2: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.6.1-3: Cell specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.6.2Test Requirements

The cell reselection delay to higher priority is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to higher priority shall be less than 68 s.

The cell reselection delay to lower priority is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 1.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN_Inter_NC + TSI-EUTRA-M1-NC , and to lower priority cell can be expressed as: Tevaluate, E-UTRAN_Inter_NC + TSI-EUTRA-M1-NC,

Where:

Thigher_priority_searchSee clause 4.7A.2.1.3

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7A.2.1.3-1 in clause 4.7A.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 67.68 s for higher priority cell search and 7.68 s for lower priority cell search, allow 68 s for higher priority cell and 8 s for lower priority cell in the test case.

## A.14.1.1.7E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage, time-based triggering

## A.14.1.1.7.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency cell reselection requirements for category M1 UE in normal coverage for satellite access specified in clause 4.7A.2.1.2.

The supported test configurations are provided in Table A.14.1.1.7.1-1.

Table A.14.1.1.7.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.14.1.1.7.1-2 and A.14.1.1.7.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

T-Service broadcasted in SIB3 of Cell 1 is set to the time point that is 36s after start of T2.

Table A.14.1.1.7.1-2: General test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.7.1-3: Cell specific test parameters for FDD intra frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.7.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_NC + TSI-EUTRA-M1-NC.

Where:

Tdetect,EUTRAN_Intra_NCSee Table 4.7A.2.1.2-1 in clause 4.7A.2.1.2

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB3 is scheduled with 20ms period, SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell in the test case.

## A.14.1.1.8 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage, time-based triggering

## A.14.1.1.8.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency cell reselection requirements for Cat-M1 UE in enhanced coverage for satellite access specified in clause 4.7A.2.2.2.

The supported test configurations are provided in Table A.14.1.1.8.1-1.

Table A.14.1.1.8.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA carrier and 2 cells as given in tables A.14.1.1.8.1-2 and A.14.1.1.8.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

T-Service broadcasted in SIB3 of Cell 1 is set to the time point that is 36s after start of T2.

TableA.14.1.1.8.1-2: General test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.14.1.1.8.1-3: Cell specific test parameters for HD-FDD intra frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.14.1.1.8.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 338 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Intra_EC + TSI-EUTRA-M1-EC.

Where:

Tdetect,EUTRAN_Intra_ECSee Table 4.7A.2.2.2-1 in clause 4.7A.2.2.2.

TSI-EUTRA-M1-ECMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case provided that SIB3 is scheduled with 20ms period, SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 337.36 s, allow 338 s for the cell re-selection delay to a newly detectable cell in the test case.

## A.14.1.1.9E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage, location-based triggering

## A.14.1.1.9.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD inter frequency cell reselection requirements for category M1 UE in enhanced coverage for satellite access specified in clause 4.7A.2.2.3.

The supported test configurations are provided in Table A.14.1.1.9.1-1.

Table A.14.1.1.9.1-1: Supported test configurations

The test scenario comprises of 2 E-UTRA FDD cells on 2 different carriers as given in tables A.14.1.1.9.1-2 and A.14.1.1.9.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test, i.e. Cell 2 is not identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

At 4s after the start of T2, the UE location is changed such that the distance to the referencelocation broadcasted in SIB31 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.1.9.1-2: General test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

Table A.14.1.1.9.1-3: Cell specific test parameters for FD-FDD inter frequency cell reselection test case for Cat-M1 UE in enhanced coverage

## A.14.1.1.9.2Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 337 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,EUTRAN_Inter_EC + TSI-EUTRA-M1-EC.

Where:

Tdetect,EUTRAN_Inter_ECSee Table 4.7A.2.2.3-1 in clause 4.7A.2.2.3

TSI-EUTRA-M1-ECMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 6400 ms is assumed in this test case provided that SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 336.64 s, allow 337 s for the cell re-selection delay to a newly detectable cell in the test case.

## A.14.1.1.10E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage, location-based triggering

## A.14.1.1.10.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency cell reselection requirements for category M1 UE in normal coverage for satellite access specified in clause 4.7A.2.1.3.

The supported test configurations are provided in Table A.14.1.1.10.1-1.

Table A.14.1.1.10.1-1: Supported test configurations

The test scenario comprises of 2 E-UTRA carriers and 2 cells as given in tables Table A.14.1.1.10.1-2 and A.14.1.1.10.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of lower priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

At 4s after the start of T2, the UE location is changed such that the distance to the referencelocation broadcasted in SIB31 of Cell 2 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.1.10.1-2: General test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

Table A.14.1.1.10.1-3: Cell specific test parameters for HD-FDD inter frequency cell reselection test case for Cat-M1 UE in normal coverage

## A.14.1.1.10.2Test Requirements

The cell reselection delay to lower priority is defined as the time from the beginning of time period T2, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to lower priority shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to lower priority cell can be expressed as: Tevaluate, E-UTRAN_Inter_NC + TSI-EUTRA-M1-NC.

Where:

Tevaluate, E-UTRAN_Inter_NCSee Table 4.7A.2.1.3-1 in clause 4.7A.2.1.3

TSI-EUTRA-M1-NCMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB31 and SIB33 are scheduled with 80 ms period.

This gives a total of 7.68 s for lower priority cell search, allow 8 s for lower priority cell in the test case.

## A.14.2RRC_CONNECTED state mobility for satellite access

## A.14.2.1E-UTRAN handover for satellite access

## A.14.2.1.1E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition

## A.14.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency handover requirements without SFN acquisition for Satellite Access as specified in clause 5.5A.2.1.

The test configurations are given in Table A.14.2.1.1.1-1. The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.1.1-2 and A.14.2.1.1.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.14.2.1.1.1-1: Supported test configurations

Table A.14.2.1.1.1-2: General test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.1.1-3: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.1.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 50 ms.

## A.14.2.1.2E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition

## A.14.2.1.2.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements without SFN acquisition for Satellite Access specified in clause 5.5A.2.2.

The test configurations are given in Table A.14.2.1.1.2-1. The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.14.2.1.1.2-2 and A.14.2.1.1.2-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. The field sameSFN-Indication and mib-RepetitionStatus are included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.14.2.1.1.2-1: Supported test configurations

Table A. 14.2.1.1.2-2: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.1.1-3: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.2.2Test Requirements

The UE shall finish the transmission of all the repetitions of the PRACH to Cell 2 less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 50 ms.

## A.14.2.1.3E-UTRAN FDD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.3.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD intra frequency conditional handover requirements with SFN acquisition for Satellite Access as specified in clause 5.5.2.1.

The test configurations are given in Table A.14.2.1.3.1-1. The test scenario comprises of one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.3.1-2 and A.14.2.1.3.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying conditional handover to Cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. The field sameSFN-Indication and mib-RepetitionStatus are not included in the handover command. At the start of T2, cell 2 becomes detectable and meets the handover condition.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.14.2.1.3.1-2: General test parameters for E-UTRAN FDD-FDD intra frequency conditional handover for Cat-M1 UEs in CEModeA test case

Table A.14.2.1.3.1-3: Cell specific test parameters for E-UTRAN FDD-FDD intra frequency conditional handover for Cat-M1 UEs in CEModeA test case

## A.14.2.1.3.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 965 ms from the start of T2 and interruption during T2 shall not exceed 155ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 800 ms in the test; Tmeasure is defined in clause 5.5A.2.3.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.5A.2.3.3.

Tinterrupt = 155 ms in the test; Tinterrupt is defined in clause 5.5A.2.3.4.

## A.14.2.1.4E-UTRAN HD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.4.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency conditional handover requirements with SFN acquisition for Satellite Access as specified in clause 5.5.2.2.

The test configurations are given in Table A.14.2.1.4.1-1. The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.14.2.1.4.1-2 and A.14.2.1.4.1-3. The The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

E-UTRAN shall send a RRC message implying conditional handover to Cell 2. The RRC message implying conditional handover shall be sent to the UE during period T1, at a time earlier than TRRC before the beginning of T2. The field sameSFN-Indication and mib-RepetitionStatus are not included in the handover command. At the start of T2, cell 2 becomes detectable and meets the handover condition.

During the test, UE is configured with measurement gap for cell search, because the narrowband of the PDSCH Reference Measurement Channel does not overlap with the centre 6 PRBs of the carrier bandwidth.

Table A.14.2.1.4.1-2: General test parameters for E-UTRAN HD-FDD intra frequency conditional handover for Cat-M1 UEs in CEModeA test case

Table A.14.2.1.4.1-3: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA test case

## A.14.2.1.4.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 965 ms from the start of T2 and interruption during T2 shall not exceed 155ms.

The rate of correct conditional handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = 800 ms in the test; Tmeasure is defined in clause 5.5A.2.3.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.5A.2.3.3.

Tinterrupt = 155 ms in the test; Tinterrupt is defined in clause 5.5A.2.3.4.

## A.14.2.1.5E-UTRAN FDD Intra frequency handover for Cat-M1 UEs in CEModeA

## A.14.2.1.5.1Test Purpose and Environment

This test is to verify the requirement for the FDD intra frequency handover requirements.

The test configurations are given in Table A.14.2.1.5.1-1. The test scenario comprises one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.5.1-2 and A.14.2.1.5.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.5.1-1: Supported test configurations

Table A.14.2.1.5.1-2: General test parameters for E-UTRAN FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.5.1-3: Cell specific test parameters for E-UTRAN FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.5.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 170 ms.

## 14.2.1.6E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA

## A.14.2.1.6.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements.

The test configurations are given in Table A.14.2.1.6.1-1. The test scenario comprises one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.6.1-2 and A.14.2.1.6.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.6.1-1: Supported test configurations

Table A.14.2.1.6.1-2: General test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.6.1-3: Cell specific test parameters for E-UTRAN HD-FDD intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.6.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 170 ms.

## A.14.2.1.7E-UTRAN FD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA

## A.14.2.1.7.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency handover requirements.

The test configurations are given in Table A.14.2.1.7.1-1. The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.7.1-2 and A.14.2.1.7.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. . The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.7.1-1: Supported test configurations

Table A.14.2.1.7.1-2: General test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.7.1-3: Cell specific test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.7.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 170 ms.

## A.14.2.1.8E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA

## A.14.2.1.8.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency handover requirements. The test configurations are given in Table A.14.2.1.8.1-1.

The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.8.1-2 and A.14.2.1.8.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.8.1-1: Supported test configurations

Table A.14.2.1.8.1-2: General test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.8.1-3: Cell specific test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.8.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 120+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 170 ms.

## A.14.2.1.9E-UTRAN FDD Inter frequency handover for Cat-M1 UEs in CEModeB

## A.14.2.1.9.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency handover requirements.

The test configurations are given in Table A.14.2.1.9.1-1. The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.9.1-2 and A.14.2.1.9.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. . The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.9.1-1: Supported test configurations

Table A.14.2.1.9.1-2: General test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

Table A.14.2.1.9.1-3: Cell specific test parameters for E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

## A.14.2.1.9.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 2610 ms.

## A.14.2.1.10E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeB

## A.14.2.1.10.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency handover requirements. The test configurations are given in Table A.14.2.1.10.1-1.

The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.10.1-2 and A.14.2.1.10.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

Starting T2, cell 2 becomes detectable and the UE is expected to detect and send a measurement report. E-UTRAN shall send a RRC message implying handover to Cell 2 during period T2, after the UE has reported Event A3. The field sameSFN-Indication is not included in the handover command. T3 is defined as the end of the last TTI containing the RRC message implying handover.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.10.1-1: Supported test configurations

Table A.14.2.1.10.1-2: General test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

Table A.14.2.1.10.1-3: Cell specific test parameters for E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition test case

## A.14.2.1.10.2Test Requirements

The UE shall finish the transmission of all repetitions of the PRACH to Cell 2 less than 170 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tinterrupt = 2560+35 ms in the test; Tinterrupt is defined in clause 5.5A.2.1.2.

This gives a total of 2610 ms.

## A.14.2.1.11E-UTRAN FDD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.11.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency conditional handover requirements.

The test configurations are given in Table A.14.2.1.11.1-1. The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.11.1-2 and A.14.2.1.11.1-3 The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

E-UTRAN shall send a RRC message implying conditional handover to Cell 2 during period T1 at a time earlier than TRRC before the beginning of T2. The field sameSFN-Indication is not included in the handover command. At the start of T2, cell 2 becomes detectable and meets the handover condition.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.11.1-1: Supported test configurations

Table A.14.2.1.11.1-2: General test parameters for E-UTRAN FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.11.1-3: Cell specific test parameters for E-UTRAN FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.12.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = [860 ms] from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = [800] ms in the test; Tmeasure is defined in clause 5.5A.2.3.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.5A.2.3.3.

## A.14.2.1.12E-UTRAN HD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.12.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency conditional handover requirements. The test configurations are given in Table A.14.2.1.12.1-1.

The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.12.1-2 and A.14.2.1.12.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

E-UTRAN shall send a RRC message implying conditional handover to Cell 2 during period T1 at a time earlier than TRRC before the beginning of T2. The field sameSFN-Indication is not included in the handover command. At the start of T2, cell 2 becomes detectable and meets the handover condition.

During the test, UE is configured with measurement gap to enable inter-frequency measurement.

Table A.14.2.1.12.1-1: Supported test configurations

Table A.14.2.1.12.1-2: General test parameters for E-UTRAN HD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.12.1-3: Cell specific test parameters for E-UTRAN HD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.12.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = [860 ms] from the start of T2 and interruption during T2 shall not exceed 50ms.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The conditional handover delay can be expressed as: TRRC + TDelayUncertainty + Tmeasure + TCHO_execution + Tinterrupt, where:

TRRC = 15 ms and is specified in clause 11.2 in TS 36.331 [2].

Tmeasure = [800] ms in the test; Tmeasure is defined in clause 5.5A.2.3.2 without TDelayUncertainty.

TCHO_execution = 10 ms in the test; TCHO_execution is defined in clause 5.5A.2.3.3.

Tinterrupt = 50 ms in the test; Tinterrupt is defined in clause 5.1.2.6.4.

5.5A.2.3A.14.2.1.13E-UTRAN FDD Intra frequency time based condition handover for Cat-M1 UEs in CEModeA

A.14.2.1.13.1Test Purpose and Environment

This test is to verify the requirement for the FDD intra frequency handover requirements.

The test configurations are given in Table A.14.2.1.13.1-1. The test scenario comprises one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.13.1-2 and A.14.2.1.13.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying time-based handover to cell 2 with Event CondEvent T1 and CondEvent A3 shall be sent to UE, at a time earlier than TRRC (15ms) before the beginning of T2. Starting T2, cell 2 becomes detectable and offset better than cell 1. Time period T3 starts at 1500ms after beginning of T2, and time condition event t1-Threshold-r17 is fulfilled at beginning of T3.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.13.1-1: Supported test configurations

Table A.14.2.1.13.1-2: General test parameters for E-UTRAN FDD intra frequency time based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.13.1-3: Cell specific test parameters for E-UTRAN FDD intra frequency time based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

A.14.2.1.13.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than beginning of T3 and less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is defined in clause 5.5A.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

TRRC = 15, which is the RRC procedure delay as specified in clause 11.2 in TS 36.331 [2] and included in T1.

TEvent_DU = 0, with CondEvent A3 met at beginning of T2;

Tmeasure = max(1440, 1500) ms, where 1440ms is the cell identification time, and Tmeasure is included in T2;

Tinterrupt = 40ms with Tsearch = 0;

TCHO_execution = 10ms.

This gives a total of 50 ms from beginning of T3.

14.2.1.14E-UTRAN HD-FDD Intra frequency location based condition handover for Cat-M1 UEs in CEModeA

A.14.2.1.14.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD intra frequency handover requirements.

The test configurations are given in Table A.14.2.1.14.1-1. The test scenario comprises one E-UTRA FDD carrier and two cells as given in tables A.14.2.1.14.1-2 and A.14.2.1.14.1-3. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying location-based handover to cell 2 with Event CondEvent D1 and CondEvent A3 shall be sent to UE, at a time earlier than TRRC (15ms) before the beginning of T2. Starting T2, cell 2 becomes detectable and offset better than cell 1. Time period T3 starts at 1500ms after beginning of T2, and location condition condEventD1-r17 is fulfilled at beginning of T3.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.14.1-1: Supported test configurations

Table A.14.2.1.14.1-2: General test parameters for E-UTRAN HD-FDD intra frequency location based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.14.1-3: Cell specific test parameters for E-UTRAN HD-FDD intra frequency location based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

A.14.2.1.14.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than beginning of T3 and less than 50 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is defined in clause 5.5A.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

TRRC = 15, which is the RRC procedure delay as specified in clause 11.2 in TS 36.331 [2] and included in T1.

TEvent_DU = 0, with CondEvent A3 met at beginning of T2;

Tmeasure = max(1440, 1500) ms, where 1440ms is the cell identification time, and Tmeasure is included in T2;

Tinterrupt = 40ms with Tsearch = 0;

TCHO_execution = 10ms.

This gives a total of 50 ms from beginning of T3.

## A.14.2.1.15E-UTRAN FDD-FDD Inter frequency location based conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.15.1Test Purpose and Environment

This test is to verify the requirement for the FDD inter frequency conditional handover requirements.

The test configurations are given in Table A.14.2.1.15.1-1. The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.15.1-2 and A.14.2.1.15.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying location-based handover to cell 2 with Event CondEvent D1 and without CondEvent A3 shall be sent to UE, at a time earlier than TRRC (15ms) before the beginning of T2. Starting T2, cell 2 becomes detectable and offset better than cell 1 and location condition event condEventD1-r17 is fulfilled.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.15.1-1: Supported test configurations

Table A.14.2.1.15.1-2: General test parameters for E-UTRAN FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.15.1-3: Cell specific test parameters for E-UTRAN FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.16.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 no later than 1490 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is defined in clause 5.5A.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

TRRC = 15, which is the RRC procedure delay as specified in clause 11.2 in TS 36.331 [2] and included in T1

TEvent_DU = 0, with condEventD1-r17 met at beginning of T2;

Tinterrupt = 1480ms with Tsearch = 1440ms;

TCHO_execution = 10ms.

This gives a total of 1490 ms from beginning of T3.

## A.14.2.1.16E-UTRAN HD-FDD Inter frequency time based conditional handover for Cat-M1 UEs in CEModeA

## A.14.2.1.16.1Test Purpose and Environment

This test is to verify the requirement for the HD-FDD inter frequency conditional handover requirements. The test configurations are given in Table A.14.2.1.16.1-1.

The test scenario comprises of two E-UTRA FDD carrier and one cell in each carrier as given in tables A.14.2.1.16.1-2 and A.14.2.1.16.1-3. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE shall have had the opportunity to acquire satellite assistance information for Cell 2, provided by Cell 1 in SystemInformationBlockType33.

During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying location-based handover to cell 2 with Event CondEvent T1 and without CondEvent A3 shall be sent to UE, at a time earlier than TRRC (15ms) before the beginning of T2. Starting T2, cell 2 becomes detectable and offset better than cell 1 and location condition event t1-Threshold-r17 is fulfilled.

During the test, UE is configured with measurement gap for cell search.

Table A.14.2.1.16.1-1: Supported test configurations

Table A.14.2.1.16.1-2: General test parameters for E-UTRAN HD-FDD Inter frequency time based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

Table A.14.2.1.16.1-3: Cell specific test parameters for E-UTRAN HD-FDD Inter frequency time based conditional handover for Cat-M1 UEs in CEModeA without SFN acquisition test case

## A.14.2.1.16.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 no later than 1490 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

NOTE:The handover delay is defined in clause 5.5A.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

TRRC = 15, which is the RRC procedure delay as specified in clause 11.2 in TS 36.331 [2] and included in T1

TEvent_DU = 0, with CondEvent T1 met at beginning of T2;

Tinterrupt = 1480ms with Tsearch = 1440ms;

TCHO_execution = 10ms.

This gives a total of 1490 ms from beginning of T3.

## A.14.3RRC connection mobility control for satellite access

## A.14.3.1RRC re-establishment for satellite access

## A.14.3.1.1E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access

## A.14.3.1.1.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7A.2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.3.1.1.1-1: Supported test configurations

The test parameters are given in table A.14.3.1.1.1-2 and table A.14.3.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.14.3.1.1.1-2: General test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

Table A.14.3.1.1.1-3: Cell specific test parameters for E-UTRAN FDD intra-frequency RRC Re-establishment test case

## A.14.3.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 1

Ksatellite,i =1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1345 ms, allow 1.5 s in the test case.

## A.14.3.1.2E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA

## A.14.3.1.2.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD intra-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7A.2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.6.2.1-1: Supported test configurations

The test parameters are given in table A.14.3.1.2.1-2 and table A.14.3.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.14.3.1.2.1-2: General test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

Table A.14.3.1.2.1-3: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency RRC Re-establishment test case

## A.14.3.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD intra frequency cell shall be less than 1.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay = 50 ms + Nfreq* Tsearch + TSI-EUTRA-M1-CEModeA + TPRACH

Nfreq = 1

Ksatellite,i =1

Tsearch = 0 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1345 ms, allow 1.5 s in the test case.

## A.14.3.1.3E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access

## A.14.3.1.3.1Test Purpose and Environment

The purpose is to verify that the E-UTRA FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7A.2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

The test parameters are given in table A.14.3.1.3-1 and table A.14.3.1.3-2 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.14.3.1.3.1-1: Supported test configurations

Table A.14.3.1.3.1-2: General test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

Table A.14.3.1.3.1-3: Cell specific test parameters for E-UTRAN FDD inter-frequency RRC Re-establishment test case

## A.14.3.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 3.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+i=1NfreqKsatellite,i*Tsearch+TSI_EUTRA-M1-CEModeA+TPRACH

Nfreq = 2

Ksatellite,i =1

Tsearch = 1000 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 3345 ms, allow 3.5 s in the test case.

## A.14.3.1.4E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access

## A.14.3.1.4.1Test Purpose and Environment

The purpose is to verify that the E-UTRA HD-FDD inter-frequency RRC re-establishment delay is within the specified limits. These tests will verify the requirements in clause 6.7A.2.

The UE shall be provided with the valid information about the SAN serving cells before the test.

The test parameters are given in tables A.14.3.1.4-1, A.14.3.1.4-2 and A.14.3.1.4-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. During T1, the UE shall be indicated with the carrier frequency of Cell 2 to ensure that the UE has the context of the carrier frequency of Cell 2. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of radio link failure. At the start of time period T3, cell 2, which is the neighbour cell, is activated.

Table A.14.3.1.4.1-1: Supported test configurations

Table A.14.3.1.4.1-2: General test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

Table A.14.3.1.4.1-3: Cell specific test parameters for E-UTRAN HD-FDD inter-frequency RRC Re-establishment test case

## A.14.3.1.4.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCConnectionReestablishmentRequest message to cell 2.

The RRC re-establishment delay to a known E-UTRA FDD inter frequency cell shall be less than 3.5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90%.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+i=1NfreqKsatellite,i*Tsearch+TSI_EUTRA-M1-CEModeA+TPRACH

Nfreq = 2

Ksatellite,i =1

Tsearch = 1000 ms

TSI-EUTRA-M1-CEModeA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRAN FDD cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 3345 ms, allow 3.5 s in the test case.

## A.14.3.2Random access for satellite access

## A.14.3.2.1E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access

## A.14.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Normal Coverage for satellite access is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.2.2, Clause 6.2.3A and Clause 7.24A.2 in an AWGN model.

The UE shall be provided with the valid information about the SAN serving cells before the test.

For this test a single cell is used. The test parameters are given in tables A.14.3.2.1.1-1 to A.14.3.2.1.1-4.

Table A.14.3.2.1.1-1: Supported test configurations

Table A.14.3.2.1.1-2: General test parameters for FDD contention based random access test

Table A.14.3.2.1.1-3: RACH-Configuration parameters for FDD contention based random access test

Table A.14.3.2.1.1-4: PRACH-Configuration parameters for FDD contention based random access test

## A.14.3.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.3.2.1.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.1.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.1.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

A.14.3.2.1.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.3.2.1.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.3.2.1.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.14.3.2.1.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 0.

Note: The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.14.3.2.2E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access

## A.14.3.2.2.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Normal Coverage for satellite access is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2].  This test will verify the requirements in Clause 6.2.2, Clause 6.2.3A and Clause 7.24A.2 in an AWGN model.

The UE shall be provided with the valid information about the SAN serving cells before the test.

For this test a single cell is used. The test parameters are given in tables A.14.3.2.2.1-1 to A.14.3.2.2.1-4.

Table A.14.3.2.2.1-1: Supported test configurations

Table A.14.3.2.2.1-2: General test parameters for HD-FDD contention based random access test

Table A.14.3.2.2.1-3: RACH-Configuration parameters for HD-FDD contention based random access test

Table A.14.3.2.2.1-4: PRACH-Configuration parameters for HD-FDD contention based random access test

## A.14.3.2.2.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.3.2.2.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.2.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -25 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.2.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

A.14.3.2.2.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.3.2.2.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.3.2.2.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.14.3.2.2.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 0.

Note: The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.14.3.2.3E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access

## A.14.3.2.3.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Enhanced Coverage for satellite access is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 7.24A.2, Clause 6.2.3A and Clause 7.1.2 in an AWGN model.

The UE shall be provided with the valid information about the SAN serving cells before the test.

For this test a single cell is used. The test parameters are given in tables A.14.3.2.3.1-1 to A.14.3.2.3.1-4.

Table A.14.3.2.3-1: Supported test configurations

Table A.14.3.2.3.1-2: General test parameters for FDD contention based random access test

Table A.14.3.2.3.1-3: RACH-Configuration parameters for FDD contention based random access test

Table A.14.3.2.3.1-4: PRACH-Configuration parameters for FDD contention based random access test

## A.14.3.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.3.2.3.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause7.24A.2.

A.14.3.2.3.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.3.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

A.14.3.2.3.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.3.2.3.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.3.2.3.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.14.3.2.3.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 2.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.14.3.2.4E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access

## A.14.3.2.4.1Test Purpose and Environment

The purpose of this test is to verify whether the behavior of the random access procedure of a Cat-M1 UE in Enhanced Coverage for satellite access is according to the requirements, whether the PRACH power settings and timing are within specified limits, and whether the UE determines properly the enhanced coverage level based on the RSRP measurement and the configured criterion in RSRP-ThresholdsPrach [2]. This test will verify the requirements in Clause 6.2.2, Clause 6.2.3A and Clause 7.24A.2 in an AWGN model.

The UE shall be provided with the valid information about the SAN serving cells before the test.

For this test a single cell is used. The test parameters are given in tables A.14.3.2.4.1-1 to A.14.3.2.4.1-4.

Table A.14.3.2.4-1: Supported test configurations

Table A.14.3.2.4.1-2: General test parameters for HD-FDD contention based random access test

Table A.14.3.2.4.1-3: RACH-Configuration parameters for HD-FDD contention based random access test

Table A.14.3.2.4.1-4: PRACH-Configuration parameters for HD-FDD contention based random access test

## A.14.3.2.4.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.3.2.4.2.1Random Access Response Reception

To test the UE behavior specified in Subclause 6.2.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts (the preamble may be transmitted multiple times in each attempt) have been received by the System Simulator. In response to the first 4 preamble transmission attempts, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.4.2.2No Random Access Response Reception

To test the UE behavior specified in subclause 6.2.2.1.2, the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preamble transmission attempts have been received by the System Simulator. The System Simulator shall not respond to the first 4 preamble transmission attempts.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Subclause 6.2.2. The power of the first preamble shall be -27 dBm with an accuracy specified in clause 6.3.5.1.1 of TS 36.102 [60]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.5.2.1 of TS 36.102 [60].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Subclause 7.24A.2.

A.14.3.2.4.2.3Receiving a NACK on msg3

To test the UE behavior specified in subclause 6.2.2.1.3, the System Simulator shall NACK all UE msg3 following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of a NACK on msg3 until the maximum number of HARQ re-transmissions is reached.

A.14.3.2.4.2.4Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.3.2.4.2.5Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Subclause 6.2.2.1.5, the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.3.2.4.2.6Contention Resolution Timer expiry

To test the UE behavior specified in Subclause 6.2.2.1.6, the System Simulator shall not send a response to a msg3.

The UE shall re-select a preamble and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

A.14.3.2.4.2.7PRACH Resource Selection

The UE shall select PRACH resources and transmits or re- transmits PRACH preambles using the PRACH resources and PRACH configuration corresponding to the coverage enhancement level 2.

Note:The PRACH Resource Selection requirement is already assumed for testing the other PRACH requirements.

## A.14.4Timing and signalling characteristics for satellite access

## A.14.4.1UE transmit timing for satellite access

The transmit timing test cases provided in this clause for Cat-M1 UEs using satellite access, the supported test configurations are provided in Table A.14.4.1-1.

Table A.14.4.1.1.-1: Supported test configurations

## A.14.4.1.1E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA

## A.14.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24A.2.

For this test a single cell is used. Table A.14.4.1.1.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.14.4.1.1.1-2.

Table A.14.4.1.1.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeA

Table A.14.4.1.1.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeA

Table A.14.4.1.1.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M1 UE under CEModeA

## A.14.4.1.1.2Test Requirements

For parameters specified in Tables A.14.4.1.1.1-1 and A.14.4.1.1.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24A.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within ± (Te_NTN_M1 – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1, whereNTA+NTA,adjcommon+NTA,adjUE×Ts

is provided by the network via higher layer parameters as described in TS 36.213[3]NTA-offset

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3].  is calculated based on the generated UL channel with time varying Doppler and delay shiftsNTA,adjUENTA,adjUE

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3]NTA,adjUE

Te_NTN_M1 is given by the values in Table 7.24A.2-1

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

NOTE: For this test case, the value of  is assumed to be zero.NTA-offset

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a). If the test configuration is for NGSO the system adjustment shall be made on top of any timing adjustment of the DL path made by the test equipment related to to the serving-satellite-ephemeris and common delay higher-layer parameters.

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24A.2 until the UE transmit timing offset is within ± Te_NTN_M1 – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.NTA+NTA,adjcommon+NTA,adjUE×(Ts

d) The test system shall verify that the UE transmit timing offset stays within ± (Te_NTN_M1 – TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA,adjcommon+NTA,adjUE×Ts

## A.14.4.1.2E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA

## A.14.4.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24A.2.

For this test a single cell is used. Table A.14.4.1.2.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.14.4.1.2.1-2.

Table A.14.4.1.2.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

Table A.14.4.1.2.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

Table A.14.4.1.2.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

## A.14.4.1.2.2Test Requirements

For parameters specified in Tables A.14.4.1.2.1-1 and A.14.4.1.2.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24A.2.

The following sequence of events shall be used to verify that the requirements are met.

For the [10MHz] channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

1.After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1, whereNTA+NTA,adjcommon+NTA,adjUE×Ts

is provided by the network via higher layer parameters as described in TS 36.213[3]NTA-offset

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3].  in test requirements is calculated based on the generated UL channel with time varying Doppler and delay shiftsNTA,adjUENTA,adjUE

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3]NTA,adjUE

Te_NTN_M1 is given by the values in Table 7.24A.2-1

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

NOTE: For this test case, the value of  is assumed to be zero.NTA-offset

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a). If the test configuration is for NGSO the system adjustment shall be made on top of any timing adjustment of the DL path made by the test equipment related to to the serving-satellite-ephemeris and common delay higher-layer parameters.

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24A.2 until the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.NTA+NTA,adjcommon+NTA,adjUE×Ts

d) The test system shall verify that the UE transmit timing offset stays within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA,adjcommon+NTA,adjUE×Ts

## A.14.4.1.3E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB

## A.14.4.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24A.2.

As specified in Clause 7.24A.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions.  By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.14.4.1.3.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.14.4.1.3.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeB

Table A.14.4.1.3.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M1 UE under CEModeB

## A.14.4.1.3.2Test Requirements

For parameters specified in Tables A.14.4.1.3.1-1 and A.14.4.1.3.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24A.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

1.After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1, whereNTA+NTA,adjcommon+NTA,adjUE×Ts

is provided by the network via higher layer parameters as described in TS 36.213[3]NTA-offset

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3].  in test requirements is calculated based on the generated UL channel with time varying Doppler and delay shiftsNTA,adjUENTA,adjUE

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3]NTA,adjUE

Te_NTN_M1 is given by the values in Table 7.24A.2-1

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

NOTE: For this test case, the value of  is assumed to be zero.NTA-offset

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a). If the test configuration is for NGSO the system adjustment shall be made on top of any timing adjustment of the DL path made by the test equipment related to to the serving-satellite-ephemeris and common delay higher-layer parameters.

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24A.2 until the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3. NTA+NTA,adjcommon+NTA,adjUE×Ts

d) The test system shall verify that the UE transmit timing offset stays within ± (Te_NTN_M1 – TGNSS_margin)  with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA,adjcommon+NTA,adjUE×Ts

## A.14.4.1.4E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB

## A.14.4.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24A.2.

As specified in Clause 7.24A.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions. By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.14.4.1.4.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.14.4.1.4.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeB

Table A.14.4.1.4.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M1 UE under CEModeB

## A.14.4.1.4.2Test Requirements

For parameters specified in Tables A.14.4.1.4.1-1 and A.14.4.1.4.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24A.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

1.After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1, whereNTA+NTA,adjcommon+NTA,adjUE×Ts

is provided by the network via higher layer parameters as described in TS 36.213[3]NTA-offset

, value is derived from the higher-layer parameters nta-Common, nta-CommonDrift, and nta-CommonDriftVariation, as described in TS 36.213[3]NTA,adjcommon

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3].  in test requirements is calculated based on the generated UL channel with time varying Doppler and delay shiftsNTA,adjUENTA,adjUE

Te_NTN_M1 is given by the values in Table 7.24A.2-1

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

NOTE: For this test case, the value of  is assumed to be zero.NTA-offset

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a). If the test configuration is for NGSO the system adjustment shall be made on top of any timing adjustment of the DL path made by the test equipment related to to the serving-satellite-ephemeris and common delay higher-layer parameters.

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24A.2 until the UE transmit timing offset is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3. NTA+NTA,adjcommon+NTA,adjUE×Ts

d) The test system shall verify that the UE transmit timing offset stays within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA,adjcommon+NTA,adjUE×Ts

## A.14.4.1.5E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB with segment transmission in NGSO for Satellite Access

## A.14.4.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE, which is not supporting the capability of ntn-SegmentedPrecompensationGaps-r17, in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24A.2.

As specified in Clause 7.24A.2 the UE adjusts its uplink timing at the start of a transmission segment boundary or at the end of of repetition period when configured with repetitions. By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.14.4.1.5.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.14.4.1.5.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeB

## A.14.4.1.5.2Test Requirements

For parameters specified in Tables A.14.4.1.5.1-1, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24A.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period or at the start of a transmission segment boundary.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1):

a.After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset of the first transmission in each segment is within ± (Te_NTN_M1 – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1, whereNTA+NTA,adjcommon+NTA,adjUE×Ts

is provided by the network via higher layer parameters as described in TS 36.213[3]NTA-offset

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3].  in test requirements is calculated based on the generated UL channel with time varying Doppler and delay shiftsNTA,adjUENTA,adjUE

, value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters TS 36.213[3]NTA,adjUE

Te_NTN_M1 is given by the values in Table 7.24A.2-1

TGNSS_margin counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usuage of AT commands in the test. TGNSS_margin = 5.12TS

NOTE: For this test case, the value of  is assumed to be zero.NTA-offset

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1) compared to that in (a). If the test configuration is for NGSO the system adjustment shall be made on top of any timing adjustment of the DL path made by the test equipment related to to the serving-satellite-ephemeris and common delay higher-layer parameters.

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24A.2 until the UE transmit timing offset of the first transmission in each segment is within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. NTA+NTA,adjcommon+NTA,adjUE×Ts

d) The test system shall verify that the UE transmit timing offset of the first transmission in each segment stays within ± (Te_NTN_M1  – TGNSS_margin) with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. NTA+NTA,adjcommon+NTA,adjUE×Ts

## A.14.4.2UE timing advance for satellite access

This clause provides the UE timing advance test cases for Cat-M1 UEs using satellite access, the supported test configurations are provided in Table A.14.4.2-1.

Table A.14.4.2-1: Supported test configurations

## A.14.4.2.1E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA

## A.14.4.2.1.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeA, defined in clause 7.28A.2.2, in an AWGN model.

The test parameters are given in tables A.14.4.2.1.1-1, A.14.4.2.1.1-2, and A.14.4.2.1.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.4.2.1.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the Satellite Access Node serving cell before and during the test via SI messages configured as provided in Table A.14.4.2.1.1-4. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established. The reference timing advance used by the UE is equal to:  .NTA-offset+NTA,adjcommon+NTA,adjUE×Ts

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.4.2.1.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.28A.2.1, the UE adjusts its uplink timing at sub-frame n+6+Koffset for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.14.4.2.1.1-1: General Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.1.1-2: Cell specific Test Parameters for E-UTRAN FDD UE Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.1.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD UE Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.1.1-4: NTN specific test for E-UTRAN FDD UE Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

## A.14.4.2.1.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 + Koffset sub frames after the reception of the timing advance command. The applied timing advance shall be additional to any variation on the timing advance components caused by the satellite ephemeris and common delay information.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.28A.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.14.4.2.2E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA

## A.14.4.2.2.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN HD-FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeA, defined in clause 7.28A.2.2, in an AWGN model.

The test parameters are given in tables A.14.4.2.2.1-1, A.14.4.2.2.1-2, and A.14.4.2.2.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.4.2.2.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the Satellite Access Node serving cell before and during the test via SI messages configured as provided in Table A.14.4.2.2.1-4. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established. The reference timing advance used by the UE is equal to:  .NTA-offset+NTA,adjcommon+NTA,adjUE×Ts

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.4.2.2.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.28A.2.1, the UE adjusts its uplink timing at sub-frame n+6+Koffset for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.14.4.2.2.1-1: General Test Parameters for E-UTRAN HD-FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.2.1-2: Cell specific Test Parameters for E-UTRAN HD-FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.2.1-3: Sounding Reference Symbol Configuration for E-UTRAN HD-FDD Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

Table A.14.4.2.2.1-4: NTN specific test parameters for E-UTRAN HD-FDD Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

## A.14.4.2.2.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6+ Koffset sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.28A.2.2. The applied timing advance shall be additional to any variation on the timing advance components caused by the satellite ephemeris and common delay information.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.14.4.2.3E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.14.4.2.3.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeB, defined in clause 7.28A.2.2, in an AWGN model.

The test parameters are given in tables A.14.4.2.3.1-1and A.14.4.2.3.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and PUSCH are sent from the UE and received by the test equipment. By measuring the reception of the PUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the Satellite Access Node serving cell before and during the test via SI messages configured as provided in Table A.14.4.2.3.1-3. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established. The reference timing advance used by the UE is equal to:  .NTA-offset+NTA,adjcommon+NTA,adjUE×Ts

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.4.2.3.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using PUSCH sent from the UE.

As specified in Clause 7.28A.2.1, the UE adjusts its uplink timing at sub-frame n+6+Koffset for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via PUSCH sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.14.4.2.3.1-1: General Test Parameters for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.14.4.2.3.1-2: Cell specific Test Parameters for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.14.4.2.3.1-3: NTN specific test for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.14.4.2.3.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 subframes after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.28A.2.2. The applied timing advance shall be additional to any variation on the timing advance components caused by the satellite ephemeris and common delay information.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

When a repetition period is configured on the uplink, the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition segment period for which R>1. The repetition segment period is given by the higher layer parameter Tx-Duration as specified in TS 36.331.

## A.14.4.2.4E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.14.4.2.4.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN HD-FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeB, defined in clause 7.28A.2.2, in an AWGN model.

The test parameters are given in tables A.14.4.2.4.1-1and A.14.4.2.4.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and PUSCH are sent from the UE and received by the test equipment. By measuring the reception of the PUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the Satellite Access Node serving cell before and during the test via SI messages configured as provided in Table A.14.4.2.4.1-3. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established. The reference timing advance used by the UE is equal to:  .NTA-offset+NTA,adjcommon+NTA,adjUE×Ts

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.4.2.4.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using PUSCH sent from the UE.

As specified in Clause 7.28A.2.1, the UE adjusts its uplink timing at sub-frame n+6+Koffset for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via PUSCH sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.14.4.2.4.1-1: General Test Parameters for E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.14.4.2.4.1-2: Cell specific Test Parameters for E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.14.4.2.3.3-3: NTN specific test for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.14.4.2.4.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 + Koffset sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.28A.2.2. The applied timing advance shall be additional to any variation on the timing advance components caused by the satellite ephemeris and common delay information.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

When a repetition period is configured on the uplink, the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition segment period for which R>1. The repetition segment period is given by the higher layer parameter Tx-Duration as specified in TS 36.331.

## A.14.4.3Radio Link Monitoring for satellite access

## A.14.4.3.1E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access

## A.14.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19A.

The test parameters are given in Tables A.14.4.3.1.1-1, A.14.4.3.1.1-2 and A.14.4.3.1.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.3.1.1-2 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.3.1.1-1: Supported test configurations

Table A.14.4.3.1.1-2: General test parameters for E-UTRAN FD-FDD out-of-sync testing for UE Cat-M1 in CEMode A

Table A.14.4.3.1.1-3: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.14.4.3.1.1-1: SNR variation for out-of-sync testing

## A.14.4.3.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.2E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access

## A.14.4.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19A.

The test parameters are given in Tables A.14.4.3.2.1-1, A.14.4.3.2.1-2 and A.14.4.3.2.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.3.2.1-2 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.3.2.1-1: Supported test configurations

Table A.14.4.3.2.1-1: General test parameters for E-UTRAN FD-FDD in-sync testing for UE Cat-M1 in CEMode A

Table A.14.4.3.2.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.14.4.3.2.1-1: SNR variation for in-sync testing

## A.14.4.3.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (720 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.3E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access

## A.14.4.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19A.

The test parameters are given in Tables A.14.4.3.3.1-1, A.14.4.3.3.1-2 and A.14.4.3.3.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.3.3.1-2 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 20 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.3.3.1-1: Supported test configurations

Table A.14.4.3.3.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync testing for UE Cat-M1 in CEMode A

Table A.14.4.3.3.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.14.4.3.3.1-1: SNR variation for out-of-sync testing

## A.14.4.3.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.4E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access

## A.14.4.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19A.

The test parameters are given in Tables A.14.4.3.4.1-1, A.14.4.3.4.1-2 and A.14.4.3.4.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.3.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 20 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.3.4.1-1: Supported test configurations

Table A.14.4.3.4.1-1: General test parameters for E-UTRAN HD-FDD in-sync testing for UE Cat-M1 in CEMode A

Table A.14.4.3.4.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.14.4.3.4.1-1: SNR variation for in-sync testing

## A.14.4.3.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (740 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.5E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A

## A.14.4.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category M1 UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell served by satellite access node (SAN) when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19A.

The test configurations are given in Table A.14.4.3.5.1-1, the test parameters are given in Tables A.14.4.3.5.1-2, A.14.4.3.5.1-3, A.14.4.3.5.1-4 and A.14.4.3.5.1-5. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.3.5.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about each cell served by SAN in the test before the test.

Table A.14.4.3.5.1-1: Supported test configurations

Table A.14.4.3.5.1-2: General test parameters for E-UTRAN FD-FDD out-of-sync tests in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.5.1-3: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.5.1-4: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.14.4.3.5.1-5: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.14.4.3.5.1-1: SNR variation for out-of-sync testing in DRX

## A.14.4.3.5.2 Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.6E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A

## A.14.4.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category M1 UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell served by satellite access node (SAN) when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19A.

The test configurations are given in Table A.14.4.3.6.1-1, the test parameters are given in Tables A.14.4.3.6.1-2, A.14.4.3.6.1-3, A.14.4.3.6.1-4 and A.14.4.3.6.1-5. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.3.6.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about each cell served by SAN in the test before the test.

Table A.14.4.3.6.1-1: Supported test configurations

Table A.14.4.3.6.1-2: General test parameters for E-UTRAN FD-FDD in-sync test in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.6.1-3: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.6.1-4: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.14.4.3.6.1-5: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.14.4.3.6.1-1: SNR variation for in-sync testing in DRX

## A.14.4.3.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.7E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A

## A.14.4.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category M1 UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell served by satellite access node (SAN) when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.19A.

The test configurations are given in Table A.14.4.3.7.1-1, the test parameters are given in Tables A.14.4.3.7.1-2, A.14.4.3.7.1-3, A.14.4.3.7.1-4 and A.14.4.3.7.1-5. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.3.7.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 20 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

During the test, the test system shall emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in TBD. The UE shall be provided with the valid information about each cell served by SAN in the test before the test.

Table A.14.4.3.7.1-1: Supported test configurations

Table A.14.4.3.7.1-2: General test parameters for E-UTRAN HD-FDD out-of-sync tests in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.7.1-3: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.7.1-4: DRX-Configuration for E-UTRAN HD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.14.4.3.7.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.14.4.3.7.1-1: SNR variation for out-of-sync testing in DRX

A.14.4.3.7.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6520 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.4.3.8E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A

## A.14.4.3.8.1 Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category M1 UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell served by satellite access node (SAN) when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.19A.

The test configurations are given in Table A.14.4.3.8.1-1, the test parameters are given in Tables A.14.4.3.8.1-2, A.14.4.3.8.1-3, A.14.4.3.8.1-4 and A.14.4.3.8.1-5. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.3.8.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 20 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

The UE shall be provided with the valid information about each cell served by SAN in the test before the test.

Table A.14.4.3.8.1-1: Supported test configurations

Table A.14.4.3.8.1-2: General test parameters for E-UTRAN HD-FDD in-sync test in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.8.1-3: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category M1 configured in CEMode A

Table A.14.4.3.8.1-4: DRX-Configuration for E-UTRAN HD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.14.4.3.8.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.14.4.3.8.1-1: SNR variation for in-sync testing in DRX

## A.14.4.3.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1140 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.14.5UE measurement procedures in RRC_CONNECTED state for satellite access

The reference channels in this clause assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.14.5.1 Intra-frequency measurements for satellite access

## A.14.5.1.1E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

## A.14.5.1.1.1Test Purpose and Environment

The supported test configurations are provided in Table A.14.5.1.1.1-3. The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements for Cat-M1 UE in clause 8.13A.2.1.1.1.

The test parameters are given in Table A.14.5.1.1.1-1 and A.14.5.1.1.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

Table A.14.5.1.1.1-1: General test parameters for E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.1.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.1.1-3: Supported test configurations

## A.14.5.1.1.2Test Requirements

For test configuration 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2.88s from the beginning of time period T2.

For test configuration 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 5.76s from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.2E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX

## A.14.5.1.2.1Test Purpose and Environment

The supported test configurations are provided in Table A.14.5.1.2.1-5. The purpose of the two tests is to verify that the Cat-M1 UE makes correct reporting of an event in DRX. The tests will partly verify the FDD intra-frequency cell search in DRX requirements in clause 8.13A.2.1.1.2.

The test parameters are given in Tables A.14.5.1.2.1-1, A.14.5.1.2.1-2, A.14.5.1.2.1-3 and A.14.5.1.2.1-4. In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

In Test 1 UE needs to be provided at least once every 500ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore UE is allocated with PUSCH resource at every DRX cycle.

In Test 2 the uplink time alignment is not maintained and UE needs to use RACH to obtain UL allocation for measurement reporting.

Table A.14.5.1.2.1-1: General test parameters for E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE when DRX is used

Table A.14.5.1.2.1-2: Cell specific test parameters for E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE when DRX is used

Table A.14.5.1.2.1-3: DRX-Configuration for E-UTRAN FDD-FDD intra-frequency event triggered reporting in DRX under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.2.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD-FDD intra-frequency event triggered reporting in DRX under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.2.1-5: Supported test configurations

## A.14.5.1.2.2Test Requirements

In Test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1.44 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE send the measurement report on PUSCH.

In Test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 25600 ms from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE starts to send preambles on the PRACH for scheduling request (SR) to obtain allocation to send the measurement report on PUSCH.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE 1:The actual overall delays measured in the test may be up to one DRX cycle higher than the measurement reporting delays above because UE is allowed to delay the initiation of the measurement reporting procedure to the next until the Active Time.

NOTE 2:In order to calculate the rate of correct events the system simulator shall verify that it has received correct Event A3 measurement report.

## A.14.5.1.3E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

## A.14.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the HD-FDD intra-frequency cell search requirements in clause 8.13A.2.1.2.1.

The supported test configurations are provided in Table A.14.5.1.3.1-3. The test parameters are given in Table A.14.5.1.3.1-1 and A.14.5.1.3.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

Table A.14.5.1.3.1-1: General test parameters for E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.3.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.3.1-3: Supported test configurations

## A.14.5.1.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2.88s from the beginning of time period T2.

The UE shall not send event triggered measurement reports as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the tests may be up to 2×TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.4E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX

## A.14.5.1.4.1Test Purpose and Environment

The purpose of the two tests is to verify that the Cat-M1 UE makes correct reporting of an event in DRX. The tests will partly verify the HD-FDD intra-frequency cell search in DRX requirements in clause 8.13A.2.1.2.2.

The supported test configurations are provided in Table A.14.5.1.4.1-5. The test parameters are given in Tables A.14.5.1.4.1-1, A.14.5.1.4.1-2, A.14.5.1.4.1-3 and A.14.5.1.4.1-4. In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2.

In Test 1 UE needs to be provided at least once every 500ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore UE is allocated with PUSCH resource at every DRX cycle.

In Test 2 the uplink time alignment is not maintained and UE needs to use RACH to obtain UL allocation for measurement reporting.

Table A.14.5.1.4.1-1: General test parameters for E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA when DRX is used

Table A.14.5.1.4.1-2: Cell specific test parameters for E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA when DRX is used

Table A.14.5.1.4.1-3: DRX-Configuration for E-UTRAN HD-FDD intra-frequency event triggered reporting in DRX under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA

Table A.14.5.1.4.1-5: Supported test configurations

Table A.14.5.1.4.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD intra-frequency event triggered reporting in DRX under AWGNn conditions in synchronous cells for Cat-M1 UE in CEModeA

## A.14.5.1.4.2Test Requirements

In Test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1.44 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE send the measurement report on PUSCH.

In Test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 32 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE starts to send preambles on the PRACH for scheduling request (SR) to obtain allocation to send the measurement report on PUSCH.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE 1:The actual overall delays measured in the test may be up to one DRX cycle higher than the measurement reporting delays above because UE is allowed to delay the initiation of the measurement reporting procedure to the next until the Active Time.

NOTE 2:In order to calculate the rate of correct events the system simulator shall verify that it has received correct Event A3 measurement report.

## A.14.5.1.5E-UTRAN FD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

## A.14.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements for Cat-M1 UE in clause 8.13A.2.1.1.1.

The test parameters are given in Table A.14.5.1.5.1-1 and A.14.5.1.5.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with EventD1 is used. Parameters referenceLocation1, referenceLocation2, distanceThreshFromReference1, distanceThreshFromReference2 are configured in eventD1. The test consists of two successive time periods, with time duration of T1, and T2 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. And the UE location shall be set such that the distance between UE and the reference location referenceLocation1 is shorter than distanceThreshFromReference1 and distance between UE and a reference location referenceLocation2 is larger than configured threshold distanceThreshFromReference2.

At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1. The position of the UE shall also be updated in the test environment such that the distance between UE and a reference location referenceLocation1 becomes larger than configured threshold distanceThreshFromReference1 and distance between UE and a reference location referenceLocation2 becomes shorter than configured threshold distanceThreshFromReference2. This shall result in reporting of eventA1.

Table A.14.5.1.5.1-1: General test parameters for E-UTRAN FD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

Table A.14.5.1.5.1-2: Cell specific test parameters for E-UTRAN FD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

## A.14.5.1.5.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 2.88s from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.6 E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

## A.14.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the HD-FDD intra-frequency cell search requirements in clause 8.13A.2.1.2.1.

The test parameters are given in Table A.14.5.1.6.1-1 and A.14.5.1.6.1-2 below In the measurement control information it is indicated to the UE that event-triggered reporting with EventD1 is used. Parameters referenceLocation1, referenceLocation2, distanceThreshFromReference1, distanceThreshFromReference2 are configured in eventD1. The test consists of two successive time periods, with time duration of T1, and T2 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. And the UE location shall be set such that the distance between UE and the reference location referenceLocation1 is shorter than distanceThreshFromReference1 and distance between UE and a reference location referenceLocation2 is larger than configured threshold distanceThreshFromReference2.

At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1. The position of the UE shall also be updated in the test environment such that the distance between UE and a reference location referenceLocation1 becomes larger than configured threshold distanceThreshFromReference1 and distance between UE and a reference location referenceLocation2 becomes shorter than configured threshold distanceThreshFromReference2. This shall result in reporting of eventA1.

.

Table A.14.5.1.6.1-1: General test parameters for E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

Table A.14.5.1.6.1-2: Cell specific test parameters for E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering

## A.14.5.1.6.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 2.88s from the beginning of time period T2.

The UE shall not send event triggered measurement reports as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the tests may be up to 2×TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.7E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting when t-serviceStartNeigh is configured. This test will partly verify the FDD intra-frequency cell search requirements for Cat-M1 UE in clause 8.13A.2.1.1.1.

The test parameters are given in Table A.14.5.1.7.1-1 and A.14.5.1.7.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with EventA3 is used. The test consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. The assistance information provided for cell 2 indicates that t-serviceStartNeigh happens at the beginning of time T4.

At the beginning of T2 the transmission power of cell 2, configured in a different satellite, is increased to the same level as for cell 1. As the UE has not reached t-serviceStartNeigh for this frequency layer, UE shall skip the measurement gaps in this interval and no report is made.

At the beginning of T3 the transmission power of cell 2 is turned down, such that it become an unknown cell for the UE after 5 seconds.

At the beginning of T4, the transmission power of cell 2 increased to the same level as for cell 1. This shall result in reporting of event A3.

Table A.14.5.1.7.1-1: General test parameters for E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

Table A.14.5.1.7.1-2: Cell specific test parameters for E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.1.7.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 6.4s from the beginning of time period T4.

NOTE: The delay time is calculated as (3.2 * Kintra_M1 *  Ksatellite_intra_i  ) seconds, according to 8.13A.2.1, with Ksatellite_intra_i =2).

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2 Inter-frequency measurements for satellite access

## A.14.5.2.1E-UTRAN FD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting when t-serviceStartNeigh is configured. This test will partly verify the FDD inter-frequency cell search requirements for Cat-M1 UE in clause 8.13A.2.1.1.1.

The test parameters are given in Table A.14.5.2.1.1-1 and A.14.5.2.1.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with EventA3 is used. The test consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. The assistance information provided for cell 2 indicates that t-serviceStartNeigh happens at the beginning of time T4.

At the beginning of T2 the transmission power of cell 2, configured in a different satellite, is increased to the same level as for cell 1. As the UE has not reached t-serviceStartNeigh for this frequency layer, UE shall skip the measurement gaps in this interval and no report is made.

At the beginning of T3 the transmission power of cell 2 is turned down, such that it become an unknown cell for the UE after 5 seconds.

At the beginning of T4, the transmission power of cell 2 increased to the same level as for cell 1. This shall result in reporting of event A3.

Table A.14.5.2.1.1-1: General test parameters for E-UTRAN FD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

Table A.14.5.2.1.1-2: Cell specific test parameters for E-UTRAN FD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.2.1.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 3.2s from the beginning of time period T4.

NOTE: The delay time is calculated as (3.2 * Kinter_M1 *  Ksatellite_inter_i  ) seconds, according to 8.13A.2.2, with Ksatellite_inter_i =1).

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.2E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the HD-FDD inter-frequency cell search requirements in clause 8.13A.2.1.2.1.

The test parameters are given in Table A.14.5.2.2.1-1 and A.14.5.2.2.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with EventA3 is used. The test consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. The assistance information provided for cell 2 indicates that t-serviceStartNeigh happens at the beginning of time T4.

At the beginning of T2 the transmission power of cell 2, configured in a different satellite, is increased to the same level as for cell 1. As the UE has not reached t-serviceStartNeigh for this frequency layer, UE shall skip the measurement gaps in this interval and no report is made.

At the beginning of T3 the transmission power of cell 2 is turned down, such that it become an unknown cell for the UE after 5 seconds.

At the beginning of T4, the transmission power of cell 2 increased to the same level as for cell 1. This shall result in reporting of event A3.

.

Table A.14.5.2.2.1-1: General test parameters for E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

Table A.14.5.2.2.1-2: E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering

## A.14.5.2.2.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 3.2s from the beginning of time period T4.

NOTE: The delay time is calculated as (3.2 * Kinter_M1 *  Ksatellite_inter_i  ) seconds, according to 8.13A.2.2, with Ksatellite_inter_i =1).

The UE shall not send event triggered measurement reports as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the tests may be up to 2×TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.3E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeB when DRX is used with time-based triggering

## A.14.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the HD-FDD inter-frequency cell search requirements in clause 8.13A.2.1.2.1.

The test parameters are given in Table A.14.5.2.3.1-1 and A.14.5.2.3.1-2 below. In the measurement control information it is indicated to the UE that event-triggered reporting with EventA3 is used. The test consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively.

During time duration T1, the UE shall not have any timing information of cell 2. The assistance information provided for cell 2 indicates that t-serviceStartNeigh happens at the beginning of time T4.

At the beginning of T2 the transmission power of cell 2, configured in a different satellite, is increased to the same level as for cell 1. As the UE has not reached t-serviceStartNeigh for this frequency layer, UE shall skip the measurement gaps in this interval and no report is made.

At the beginning of T3 the transmission power of cell 2 is turned down, such that it become an unknown cell for the UE after 5 seconds.

At the beginning of T4, the transmission power of cell 2 increased to the same level as for cell 1. This shall result in reporting of event A3.

.

Table A.14.5.2.3.1-1: General test parameters for E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeB when DRX is used with time-based triggering

Table A.14.5.2.3.1-2: Cell specific test parameters for E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeB when DRX is used with time-based triggering

## A.14.5.2.3.2Test Requirements

The UE shall send one Event D1 triggered measurement report, with a measurement reporting delay less than 14.5s from the beginning of time period T4.

NOTE: The delay time is calculated as (22.6 * Kinter_M1 *  Ksatellite_inter_i  ) cycles, according to 8.13A.3.2, with Ksatellite_inter_i =1).

The UE shall not send event triggered measurement reports as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the tests may be up to 2×TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.4E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA

## A.14.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event with discontinuous MPDCCH monitoring. This test will partly verify the FDD-FDD inter-frequency cell search requirements in clause 8.13A.2.2.1. The supported test configurations are provided in Table A.14.5.2.4.1-1.

Table A.14.5.2.4.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.4.1-2 and A.14.5.2.4.1-3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

Table A.14.5.2.4.1-2: General test parameters

Table A.14.5.2.4.1-3: Cell specific test parameters

## A.14.5.2.4.2Test Requirement

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 3.2 s from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.5E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA when DRX is used

## A.14.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event for inter-frequency. This test will partly verify the FDD-FDD inter-frequency cell search requirements in clause 8.13A.2.2.1. The supported test configurations are provided in Table A.14.5.2.5.1-1.

Table A.14.5.2.5.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.5.1-2, A.14.5.2.5.1-3 and A.14.5.2.5.1-4 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

In Test 1 UE needs to be provided at least once every 500ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

In Test 2 the uplink time aligment is not maintained and UE needs to use RACH to obtain UL allocation for measurement reporting.

Table A.14.5.2.5.1-2: General test parameters

Table A.14.5.2.5.1-3: Cell specific test parameters

Table A.14.5.2.5.1-4: DRX-Configuration

Table A.14.5.2.5.1-4: TimeAlignmentTimer -Configuration

## A.14.5.2.5.2Test Requirement

In Test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6.4 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE send the measurement report on PUSCH.

In Test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 51.2 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE starts to send preambles on the PRACH for scheduling request (SR) to obtain allocation to send the measurement report on PUSCH.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE 1:The actual overall delays measured in the test may be up to one DRX cycle higher than the measurement reporting delays above because UE is allowed to delay the initiation of the measurement reporting procedure to the next until the Active Time.

NOTE 2:In order to calculate the rate of correct events the system simulator shall verify that it has received correct Event A3 measurement report.

## A.14.5.2.6E-UTRAN HD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA

## A.14.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event with discontinuous MPDCCH monitoring. This test will partly verify the HD-FDD inter-frequency cell search requirements in clause 8.13A.2.2.2. The supported test configurations are provided in Table A.14.5.2.6.1-1.

Table A.14.5.2.6.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.6.1-2 and A.14.5.2.6.1-3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

Table A.14.5.2.6.1-2: General test parameters

Table A.14.5.2.6.1-3: Cell specific test parameters

## A.14.5.2.6.2Test Requirement

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 3.2 s from the beginning of time period T2. During the test, downlink traffic is continuously scheduled.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.7E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA in DRX

## A.14.5.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event. This test will partly verify the HD-FDD inter-frequency cell search requirements in clause 8.13A.2.2.2. The supported test configurations are provided in Table A.14.5.2.7.1-1.

Table A.14.5.2.7.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.7.1-2, A.14.5.2.7.1-3, A.14.5.2.7.1-4 and A.14.5.2.6.1-5 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

In Test 1 UE needs to be provided at least once every 500ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

In Test 2 the uplink time aligment is not maintained and UE needs to use RACH to obtain UL allocation for measurement reporting.

Table A.14.5.2.7.1-2: General test parameters

Table A.14.5.2.7.1-3: Cell specific test parameters

Table A.14.5.2.7.1-4: DRX-Configuration

Table A.14.5.2.7.1-5: TimeAlignmentTimer -Configuration

## A.14.5.2.7.2Test Requirement

In Test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6.4 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE send the measurement report on PUSCH.

In Test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 51.2 s from the beginning of time period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE starts to send preambles on the PRACH for scheduling request (SR) to obtain allocation to send the measurement report on PUSCH.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE 1:The actual overall delays measured in the test may be up to one DRX cycle higher than the measurement reporting delays above because UE is allowed to delay the initiation of the measurement reporting procedure to the next until the Active Time.

NOTE 2:In order to calculate the r

## A.14.5.2.8E-UTRAN FDD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB

## A.14.5.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event with discontinuous MPDCCH monitoring. This test will partly verify the FDD-FDD inter-frequency cell search requirements in clause 8.13A.3.2.1. The supported test configurations are provided in Table A.14.5.2.8.1-1.

Table A.14.5.2.8.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.8.1-2 and A.14.5.2.8.1-3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

Table A.14.5.2.8.1-2: General test parameters

Table A.14.5.2.8.1-3: Cell specific test parameters

## A.14.5.2.8.2Test Requirement

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than [819.2] s from the beginning of time period T2 which is derived from section 8.13.3.5.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to pusch-maxNumRepetitionCEmodeB x TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH, where pusch-maxNumRepetitionCEmodeB [2] is the maximum number of PUSCH repetitions configured

## A.14.5.2.9E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB

## A.14.5.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE makes correct reporting of an event with discontinuous MPDCCH monitoring. This test will partly verify the HD-FDD inter-frequency cell search requirements in clause 8.13A.3.2.2. The supported test configurations are provided in Table A.14.5.2.9.1-1.

Table A.14.5.2.9.1-1: Supported test configurations

The test parameters are given in Table A.14.5.2.9.1-2 and A.14.5.2.9.1-3 below. In the measurement control information it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 2. At the beginning of T2 the transmission power of cell 2 is increased to the same level as for cell 1, and due to usage of an offset this shall result in reporting of Event A3.

During the test, downlink traffic is continuously scheduled. MPDCCH is not collided with gap.

Table A.14.5.2.9.1-2: General test parameters

Table A.14.5.2.9.1-3: Cell specific test parameters

## A.14.5.2.9.2Test Requirement

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 819.2 s from the beginning of time period T2 which is derived from section 8.13.3.5.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to pusch-maxNumRepetitionCEmodeB x TTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH, where pusch-maxNumRepetitionCEmodeB [2] is the maximum number of PUSCH repetitions configured

reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.6Measurement performance requirements for UE for satellite access

## A.14.6.1RSRP for satellite access

## A.14.6.1.1FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.14.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21A.1 and 9.1.21A.2 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.14.6.1.1.2Test parameters

The supported test configurations are provided in Table A.14.6.1.1.2-2.  In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.14.6.1.1.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.14.6.1.1.2-1: FD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

Table A.14.6.1.1.2-2: Supported test configurations

## A.14.6.1.1.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.1 and 9.1.21A.2.

## A.14.6.1.2HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA

## A.14.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21A.1 and 9.1.21A.2 for HD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.14.6.1.2.2Test parameters

The supported test configurations are provided in Table A.14.6.1.2.2-2.  In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP intra frequency measurements are tested by using the parameters in Table A.14.6.1.2.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.14.6.1.2.2-1: HD-FDD RSRP Intra frequency test parameters for Cat-M1 UE in CEModeA

Table A.14.6.1.2.2-2: Supported test configurations

## A.14.6.1.2.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.1 and 9.1.21A.2.

## A.14.6.1.3FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA

## A.14.6.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21A.9 and 9.1.21A.10 for FD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.14.6.1.3.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.14.6.1.3.2-1 and Table A.14.6.1.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.14.6.1.3.2-1: Supported test configurations

Table A.14.6.1.3.2-2: FD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeA

## A.14.6.1.3.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.9 and 9.1.21A.10.

## A.14.6.1.4HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA

## A.14.6.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in section 9.1.21A.9 and 9.1.21A.10 for HD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeA.

## A.14.6.1.4.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.14.6.1.4.2-1. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.14.6.1.4.2-1: HD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeA

## A.14.6.1.4.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.9 and 9.1.21A.10.

## A.14.6.1.5FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB

## A.14.6.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21A.11 and 9.1.21A.12 for FD-FDD intra frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.14.6.1.5.2Test parameters

Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.14.6.1.5.2-1 and A.14.6.1.5.2-2. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.14.6.1.5.2-1: FD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 1.4 MHz cell BW

## A.14.6.1.5.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.11 and 9.1.21A.12.

## A.14.6.1.6HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB

## A.14.6.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the RSRP measurement accuracy is within the specified limits. This test will verify the requirements in Sections 9.1.21A.11 and 9.1.21A.12 for HD-FDD inter frequency RSRP measurements for Cat-M1 UE in CEModeB.

## A.14.6.1.6.2Test parameters

Both absolute and relative accuracy of RSRP inter frequency measurements are tested by using the parameters in Table A.14.6.1.6.2-1 and A.14.6.1.6.2-2. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. All the tests contain MPDCCH for UL grant for reporting RSRP.

Table A.14.6.1.6.2-1: HD-FDD RSRP Inter frequency test parameters for Cat-M1 UE in CEModeB for 1.4 Mhz Cell BW

## A.14.6.1.6.3Test Requirements

The RSRP measurement accuracy shall fulfil the requirements in sections 9.1.21A.11 and 9.1.21A.12.

## A.14.6.2Channel quality reporting accuracy for satellite access

## A.14.6.2.1E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access

## A.14.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in section 9.1.21A.18.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.6.2.1.1-1: Supported test configurations

## A.14.6.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.14.6.2.1.2-1 and A.14.6.2.1.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.14.6.2.1.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode A

Table A.14.6.2.1.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode A

## A.14.6.2.1.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21A.18.

## A.14.6.2.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access

## A.14.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in section 9.1.21A.18.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.6.2.2.1-1: Supported test configurations

## A.14.6.2.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.14.6.2.2.2-1 and A.14.6.2.2.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.14.6.2.2.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode A

Table A.14.6.2.2.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode A

## A.14.6.2.2.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21A.18.

A.14.6.2.3E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B for Satellite access

A.14.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in section 9.1.21A.19.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.6.2.3.1-1: Supported test configurations

## A.14.6.2.3.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.14.6.2.3.2-1 and A.14.6.2.3.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.14.6.2.3.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode B

Table A.14.6.2.3.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN FD-FDD Category M1 UE in CE Mode B

## A.14.6.2.3.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21A.19.

## A.14.6.2.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B for Satellite access

## A.14.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the downlink channel quality reporting accuracy in connected mode is within the specified limits. This test will verify the requirements in section 9.1.21A.19.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.6.2.4.1-1: Supported test configurations

## A.14.6.2.4.2Test parameters

In this set of test cases all cells are on the same carrier frequency. The MAC CE-based downlink channel quality reporting accuracy is tested by using the parameters in Tables A.14.6.2.4.2-1 and A.14.6.2.4.2-2. There are two time periods T1 and T2 with different SNR levels. At the start of T2 the active cell should trigger a downlink channel quality report (“Regular DCQR”) as described in clause 5.25 of TS 36.321. Upon receiving the DCQR from the UE, the active cell should re-configure MPDCCH according to the signaled aggregation and repetition levels.

Table A.14.6.2.4.2-1: General Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode B

Table A.14.6.2.4.2-2: Cell specific Test Parameters for Downlink channel quality reporting accuracy test for E-UTRAN HD-FDD Category M1 UE in CE Mode B

## A.14.6.2.4.3Test Requirements

The downlink channel quality reporting accuracy shall fulfil the requirements in section 9.1.21A.19.

## Annex B (normative):Conditions for RRM requirements applicability for operating bands

## B.1Conditions for E-UTRAN RRC_IDLE state mobility

## B.1.1Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection

This clause defines the E-UTRAN intra-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.1-1.

Table B.1.1-1: Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection

## B.1.2Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection

This clause defines the E-UTRAN inter-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection defined in Table B.1.1-1 also apply for inter-frequency E-UTRAN cells in this section.

## B.1.3Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M1

This clause defines the E-UTRAN intra-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.1.3 is defined in Section 3.1.

The conditions for normal coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.3-1 and for E-UTRAN HD-FDD are defined are defined in Table B.1.3-2.

The conditions for enhanced coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.3-3 and for E-UTRAN HD-FDD are defined are defined in Table B.1.3-4.

Table B.1.3-1: E-UTRAN intra-frequency measurements for FDD and TDD for normal coverage

Table B.1.3-2: E-UTRAN intra-frequency measurements for HD-FDD for normal coverage

Table B.1.3-3: E-UTRAN intra-frequency measurements for FDD and TDD for enhanced coverage

Table B.1.3-4: E-UTRAN intra-frequency measurements for HD-FDD for enhanced coverage

## B.1.4Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB1

This clause defines the NB-IoT intra-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.1.4 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection are defined in Table B.1.4-1 and B.1.4-3.

The conditions for measurements of intra-frequency NB-IoT cells in enhanced coverage for cell re-selection are defined in Table B.1.4-2 and B.1.4-4.

Table B.1.4-1: NB-IoT intra-frequency measurements for HD-FDD in normal coverage

Table B.1.4-2: NB-IoT intra-frequency measurements for HD-FDD in enhanced coverage

Table B.1.4-3: NB-IoT intra-frequency measurements for TDD in normal coverage

Table B.1.4-4: NB-IoT intra-frequency measurements for TDD in enhanced coverage

## B.1.5Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB1

This clause defines the NB-IoT inter-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.1.5 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection defined in Table B.1.4-1 and B.1.4-3 also apply for inter-frequency NB-IoT cells in normal coverage in this section.

The conditions for measurements of intra-frequency NB-IoT cells in enhanced coverage for cell re-selection defined in Table B.1.4-2 and B.1.4-4 also apply for inter-frequency NB-IoT cells in enhanced coverage in this section.

## B.1.6Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category 1bis

This clause defines the E-UTRAN intra-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.6-1.

Table B.1.6-1: Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection

## B.1.7Conditions for measurements of E-UTRAN cells for cell re-selection for UE Category M2

## B.1.7.1Conditions for measurements of intra-frequence E-UTRAN cells for cell selection

This clause defines the E-UTRAN intra-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M2 applicability of the conditions in Appendix B.1.7 is defined in Section 3.1.

The conditions for CE mode A measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.7.1-1 and for E-UTRAN HD-FDD are defined are defined in Table B.1.7.1-2.

The conditions for CE mode B measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.7.1-3 and for E-UTRAN HD-FDD are defined are defined in Table B.1.7.1-4.

Table B.1.7.1-1: E-UTRAN intra-frequency measurements for FDD and TDD for normal coverage

Table B.1.7.1-2: E-UTRAN intra-frequency measurements for HD-FDD for normal coverage

Table B.1.7.1-3: E-UTRAN intra-frequency measurements for FDD and TDD for enhanced coverage

Table B.1.7.1-4: E-UTRAN intra-frequency measurements for HD-FDD for enhanced coverage

## B.1.7.2Condition for measurements of inter-frequence E-UTRAN cells for cell selection

This clause defines the E-UTRAN inter-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M2 applicability of the conditions in Appendix B.1.7 is defined in Section 3.1.

The conditions for CE mode A measurements of FDD and TDD inter-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.7.2-1 and for E-UTRAN HD-FDD are defined are defined in Table B.1.7.2-2.

The conditions for CE mode B measurements of FDD and TDD inter-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.7.2-3 and for E-UTRAN HD-FDD are defined are defined in Table B.1.7.2-4.

Table B.1.7.2-1: E-UTRAN inter-frequency measurements for FDD and TDD for normal coverage

Table B.1.7.2-2: E-UTRAN inter-frequency measurements for HD-FDD for normal coverage

Table B.1.7.2-3: E-UTRAN inter-frequency measurements for FDD and TDD for enhanced coverage

Table B.1.7.2-4: E-UTRAN inter-frequency measurements for HD-FDD for enhanced coverage

## B.1.8Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M1

This clause defines the E-UTRAN inter-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.1.3 is defined in Section 3.1.

The conditions for normal coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection defined in Table B.1.3-1 and for E-UTRAN HD-FDD defined in Table B.1.3-2 also apply for E-UTRAN FDD, TDD and HD-FDD inter-frequency E-UTRAN cells for cell reselection.

The conditions for enhanced coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection defined in Table B.1.3-3 and for E-UTRAN HD-FDD defined in Table B.1.3-4 also apply for E-UTRAN FDD, TDD, and HD-FDD inter-frequency E-UTRAN cells for re-selection.

## B.1.9Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access

This clause defines the E-UTRAN intra-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for UE category M1 for a corresponding operating band for satellite access. The band groups for category M1 for satellite access are defined in Section 3.5.1A. The UE category M1 applicability of the conditions in Appendix B.1.9 is defined in Section 3.6.

The conditions for normal coverage measurements of FDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.9-1 and for E-UTRAN HD-FDD are defined in Table B.1.9-2.

The conditions for enhanced coverage measurements of FDD intra-frequency E-UTRAN cells for cell re-selection are defined in Table B.1.9-3 and for E-UTRAN HD-FDD are defined in Table B.1.9-4.

Table B.1.9-1: E-UTRAN intra-frequency measurements for FDD for normal coverage for satellite access

Table B.1.9-2: E-UTRAN intra-frequency measurements for HD-FDD for normal coverage for satellite access

Table B.1.9-3: E-UTRAN intra-frequency measurements for FDD for enhanced coverage for satellite access

Table B.1.9-4: E-UTRAN intra-frequency measurements for HD-FDD for enhanced coverage for satellite access

## B.1.10Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB1 and NB2 for satellite access

This clause defines the NB-IoT intra-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band for satellite access. The band groups for UE category NB1 and NB2 for satellite access are defined in Section 3.5.1A. The UE category NB1 and NB2 applicability of the conditions in Appendix B.1.10 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection are defined in Table B.1.10-1.

The conditions for measurements of intra-frequency NB-IoT cells in enhanced coverage for cell re-selection are defined in Table B.1.10-2.

Table B.1.10-1: NB-IoT intra-frequency measurements for HD-FDD and TDD in normal coverage for satellite access

Table B.1.10-2: NB-IoT intra-frequency measurements for HD-FDD in enhanced coverage for satellite access

## B.1.11Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB1 for satellite access

This clause defines the NB-IoT inter-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.1.11 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection defined in Table B.1.10-1 also apply for inter-frequency NB-IoT cells in normal coverage in this section.

The conditions for measurements of intra-frequency NB-IoT cells in enhanced coverage for cell re-selection defined in Table B.1.10-2 also apply for inter-frequency NB-IoT cells in enhanced coverage in this section.

## B.1.12Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access

This clause defines the E-UTRAN inter-frequency RSRP, RSRP Ês/Iot, SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.1.12 is defined in Section 3.1.

The conditions for normal coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection defined in Table B.1.9-1 and for E-UTRAN HD-FDD defined in Table B.1.9-2 also apply for E-UTRAN FDD, TDD and HD-FDD inter-frequency E-UTRAN cells for cell reselection.

The conditions for enhanced coverage measurements of FDD and TDD intra-frequency E-UTRAN cells for cell re-selection defined in Table B.1.9-3 and for E-UTRAN HD-FDD defined in Table B.1.9-4 also apply for E-UTRAN FDD, TDD, and HD-FDD inter-frequency E-UTRAN cells for re-selection.

## B.2Conditions for UE Measurements Procedures in RRC_CONNECTED State

## B.2.1Conditions for E-UTRAN intra-frequency measurements

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for intra-frequency E-UTRAN measurements are defined in Table B.2.1-1.

Table B.2.1-1: E-UTRAN intra-frequency measurements

## B.2.2Conditions for E-UTRAN intra-frequency measurements with autonomous gaps

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for intra-frequency E-UTRAN measurements with autonomous gap are as in Table B.2.1-1.

Table B.2.2-1: Void

## B.2.3Conditions for E-UTRAN inter-frequency measurements

This clause defines the E-UTRAN inter-frequency SCH_RP, SCH Ês/Iot, RSRP and RSRP Ês/Iot applicable for a corresponding operating band.

The conditions for inter-frequency E-UTRAN measurements with autonomous gap are defined in Table B.2.3-1.

Table B.2.3-1: E-UTRAN inter-frequency measurements

## B.2.4Conditions for E-UTRAN inter-frequency measurements with autonomous gaps

This clause defines the E-UTRAN inter-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for inter-frequency E-UTRAN measurements with autonomous gap are defined in Table B.2.4-1.

Table B.2.4-1: E-UTRAN inter-frequency measurements with autonomous gaps

## B.2.5Conditions for E-UTRAN OTDOA intra-frequency RSTD Measurements

This clause defines the E-UTRAN intra-frequency PRP1,2 applicable for a corresponding operating band

The conditions for E-UTRAN OTDOA intra-frequency RSTD measurements  are defined in Table B.2.5-1

Table B.2.5-1: E-UTRAN OTDOA intra-frequency RSTD measurements

## B.2.6Conditions for E-UTRAN OTDOA inter-frequency RSTD Measurements

This clause defines the E-UTRAN inter-frequency PRP1,2 applicable for a corresponding operating band.

The conditions for E-UTRAN OTDOA inter-frequency RSTD measurements  are defined in Table B.2.5-1.

## B.2.7Conditions for Measurements of the secondary component carrier with deactivated SCell

This clause defines the SCH_RP and SCH Ês/Iot for measurements in the secondary component carrier applicable for a corresponding operating band.

The conditions for measurements of the secondary component carrier with deactivated SCell are defined in Table B.2.7-1.

Table B.2.7-1: Measurements of the secondary component carrier with deactivated SCell

## B.2.8Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for intra-frequency E-UTRAN measurements under time domain measurement resource restriction are defined in Table B.2.8-1.

Table B.2.8-1: E-UTRAN intra-frequency measurements under time domain measurement resource restriction

## B.2.9Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction with CRS Assistance Information

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for intra-frequency E-UTRAN measurements under time domain measurement resource restriction with CRS assistance information are defined in Table B.2.9-1.

Table B.2.9-1: E-UTRAN intra-frequency measurements under time domain measurement resource restriction with CRS assistance information

## B.2.10Conditions for E-UTRAN intra-frequency discovery signal measurements

## B.2.10.1Conditions for E-UTRAN intra-frequency CRS-based measurements

This clause defines the E-UTRAN intra-frequency SCH_RP, SCH Ês/Iot in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements

The conditions for E-UTRAN intra-frequency CRS based discovery signal measurements are as in Table B.2.1-1.

## B.2.10.2Conditions for E-UTRAN intra-frequency CSI-RS based measurements

This clause defines the E-UTRAN intra-frequency SCH_RP, SCH Ês/Iot, CSI-RSRP, and CSI-RS Ês/Iot in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for E-UTRAN intra-frequency CRI-RS based discovery signal measurements in discovery signal occasions are specified in Table B.2.10.2-1.

Table B.2.10.2-1: E-UTRAN intra-frequency discovery signal measurements

## B.2.11Conditions for E-UTRAN inter-frequency discovery signal measurements

## B.2.11.1Conditions for E-UTRAN inter-frequency CRS-based measurements

This clause defines the E-UTRAN inter-frequency SCH_RP, SCH Ês/Iot, RSRP, and Ês/Iot in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements.

The conditions for E-UTRAN inter-frequency CRS-based discovery signal measurements in discovery signal occasions are specified in Table B.2.11.1-1.

Table B.2.11.1-1: E-UTRAN inter-frequency discovery signal measurements

## B.2.11.2Conditions for E-UTRAN inter-frequency CSI-RS based measurements

This clause defines the E-UTRAN inter-frequency SCH_RP, SCH Ês/Iot, CSI-RSRP, and CSI-RS Ês/Iot in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for E-UTRAN inter-frequency CRS-based discovery signal measurements in discovery signal occasions are specified in Table B.2.11.2-1.

Table B.2.11.2-1: E-UTRAN inter-frequency discovery signal measurements

## B.2.12Conditions for E-UTRAN intra-frequency discovery signal measurements under operation with frame structure 3

This section defines the E-UTRAN intra-frequency SCH_RP in discovery signal occasions [16], applicable for a corresponding operating band for discovery signal measurements under frame structure type 3.

The conditions for E-UTRAN intra-frequency discovery signal measurements are defined in Table B.2.12-1.

Table B.2.12-1: E-UTRAN intra-frequency measurements under operation with frame structure 3

## B.2.13Conditions for E-UTRAN inter-frequency discovery signal measurements under operation with frame structure 3

## B.2.13.1Conditions for E-UTRAN inter-frequency CRS-based measurements

This section defines the E-UTRAN inter-frequency SCH_RP in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements under frame structure 3.

The conditions for E-UTRAN inter-frequency CRS-based discovery signal measurements in discovery signal occasions are specified in Table B.2.13.1-1.

Table B.2.13.1-1: E-UTRAN inter-frequency discovery signal measurements

## B.2.13.2Conditions for E-UTRAN inter-frequency CSI-RS based measurements

This section defines the E-UTRAN inter-frequency SCH_RP in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for E-UTRAN inter-frequency CSI-RS based discovery signal measurements in discovery signal occasions under frame structure 3 are specified in Table B.2.13.2-1.

Table B.2.13.2-1: E-UTRAN inter-frequency discovery signal measurements

## B.2.14Conditions for E-UTRAN intra-frequency measurements by UE Category M1

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.2.14 is defined in Section 3.1.

The conditions for CE mode A intra-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.14-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.14-2.

The conditions for CE mode B for intra-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.14-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.14-4.

Table B.2.14-1: E-UTRAN intra-frequency measurements for FDD and TDD for CE mode A

Table B.2.14-2: E-UTRAN intra-frequency measurements for HD-FDD for CEModeA

Table B.2.14-3: E-UTRAN intra-frequency measurements for FDD and TDD for CEModeB

Table B.2.14-4: E-UTRAN intra-frequency measurements for HD-FDD for CE mode B

## B.2.15Conditions for NB-IoT intra-frequency measurements by UE Category NB1

This clause defines the NB-IoT intra-frequency NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.15 is defined in Section 3.6.

The conditions for intra-frequency measurements in normal coverage are defined in Table B.2.15-1 and B.2.15-3.

The conditions for intra-frequency measurements in denhanced coverage are defined in Table B.2.15-2 and B.2.15-4.

Table B.2.15-1: NB-IoT intra-frequency measurements for HD-FDD in normal coverrage

Table B.2.15-2: NB-IoT intra-frequency measurements for HD-FDD in enhanced coverrage

Table B.2.15-3: NB-IoT intra-frequency measurements for TDD in normal coverrage

Table B.2.15-4: NB-IoT intra-frequency measurements for TDD in enhanced coverrage

## B.2.16Conditions for NB-IoT intra-frequency RSTD measurements by UE Category NB1

This clause defines the NB-IoT intra-frequency PRP1,2 applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.16 is defined in Section 3.1.

The conditions for intra-frequency RSTD measurements in normal coverage are defined in Table B.2.16-1 and B.2.16-3.

The conditions for intra-frequency RSTD measurements in enhanced coverage are defined in Table B.2.16-2 and B.2.16-4.

Table B.2.16-1: NB-IoT intra-frequency RSTD measurements for HD-FDD in normal coverrage

Table B.2.16-2: NB-IoT intra-frequency RSTD measurements for HD-FDD in enhanced coverrage

Table B.2.16-3: NB-IoT intra-frequency RSTD measurements for TDD in normal coverrage

Table B.2.16-4: NB-IoT intra-frequency RSTD measurements for TDD in enhanced coverrage

## B.2.17Conditions for NB-IoT inter-frequency RSTD measurements by UE Category NB1

This clause defines the NB-IoT inter-frequency PRP1,2 applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.17 is defined in Section 3.1.

The conditions for intra-frequency RSTD measurements in normal coverage are defined in Table B.2.17-1 and B.2.17-3.

The conditions for intra-frequency RSTD measurements in enhanced coverage are defined in Table B.2.17-2 and B.2.17-4.

Table B.2.17-1: NB-IoT inter-frequency RSTD measurements for HD-FDD in normal coverrage

Table B.2.17-2: NB-IoT inter-frequency RSTD measurements for HD-FDD in enhanced coverrage

Table B.2.17-3: NB-IoT inter-frequency RSTD measurements for TDD in normal coverrage

Table B.2.17-4: NB-IoT inter-frequency RSTD measurements for TDD in enhanced coverrage

## B.2.18Conditions for E-UTRAN inter-frequency measurements by UE Category M1

This clause defines the E-UTRAN inter-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.2.18 is defined in Section 3.1.

The conditions for CE mode A inter-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.18-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.18-2.

The conditions for CE mode B for inter-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.18-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.18-4.

Table B.2.18-1: E-UTRAN inter-frequency measurements for FDD and TDD for CEModeA

Table B.2.18-2: E-UTRAN inter-frequency measurements for HD-FDD for CEModeA

Table B.2.18-3: E-UTRAN inter-frequency measurements for FDD and TDD for CEModeB

Table B.2.18-4: E-UTRAN inter-frequency measurements for HD-FDD for CEModeB

## B.2.19Conditions for E-UTRAN measurements by UE Category M2

## B.2.19.1Conditions for E-UTRAN intra-frequency measurements

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for intra-frequency measurements are defined in sub-section B.2.14.

## B.2.19.2Conditions for E-UTRAN inter-frequency measurements

This clause defines the E-UTRAN inter-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for inter-frequency measurements are defined in sub-section B.2.18.

## B.2.20Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M1

This clause defines the E-UTRAN inter-frequency PRP1,2 applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.2.20 is defined in Section 3.1.

The conditions for CE mode A inter-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.20-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.20-2.

The conditions for CE mode B for inter-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.20-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.20-4.

Table B.2.20-1: E-UTRAN inter-frequency measurements for FDD and TDD for CE mode A

Table B.2.20-2: E-UTRAN inter-frequency measurements for HD-FDD for CE mode A

Table B.2.20-3: E-UTRAN inter-frequency measurements for FDD and TDD for CE mode B

Table B.2.20-4: E-UTRAN inter-frequency measurements for HD-FDD for CE mode B

## B.2.21Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M2

This section defines the inter-frequency PRP applicable for a corresponding operating band for Cat-M2.

The conditions for inter-frequency RSTD measurements are defined in sub-section B.2.20.

## B.2.22Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M1

This clause defines the E-UTRAN intra-frequency PRP1,2 applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.2.22 is defined in Section 3.1.

The conditions for CE mode A intra-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.22-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.22-2.

The conditions for CE mode B for intra-frequency E-UTRAN FDD and TDD measurements are defined in Table B.2.22-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.22-4.

Table B.2.22-1: E-UTRAN intra-frequency measurements for FDD and TDD for CE mode A

Table B.2.22-2: E-UTRAN intra-frequency measurements for HD-FDD for CE mode A

Table B.2.22-3: E-UTRAN intra-frequency measurements for FDD and TDD for CE mode B

Table B.2.22-4: E-UTRAN intra-frequency measurements for HD-FDD for CE mode B

## B.2.23Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M2

This section defines the intra-frequency PRP applicable for a corresponding operating band for Cat-M2.

The conditions for intra-frequency RSTD measurements are defined in sub-section B.2.22.

## B.2.24Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1

This clause defines the NB-IoT intra-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.24 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage are defined in Table B.2.24-1 and B.2.24-2.

Table B.2.24-1: NB-IoT intra-frequency measurements for HD-FDD in normal coverage

Table B.2.24-2: NB-IoT intra-frequency measurements for TDD in normal coverage

## B.2.25Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1

This clause defines the NB-IoT inter-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.25 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection defined in Table B.2.24-1 and B.2.24-2 also apply for inter-frequency NB-IoT cells in normal coverage in this section.

## B.2.26Conditions for E-UTRAN intra-frequency measurements by UE Category M1 for satellite access

This clause defines the E-UTRAN intra-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band for UE category M1 for satellite access. The band groups for category M1 for satellite access are defined in Section 3.5.1A. The UE category M1 applicability of the conditions in Appendix B.2.26 is defined in Section 3.6.

The conditions for CE mode A intra-frequency E-UTRAN FDD measurements are defined in Table B.2.26-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.26-2.

The conditions for CE mode B for intra-frequency E-UTRAN FDD measurements are defined in Table B.2.26-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.26-4.

Table B.2.26-1: E-UTRAN intra-frequency measurements for FDD for CE mode A for satellite access

Table B.2.26-2: E-UTRAN intra-frequency measurements for HD-FDD for CE ModeA for satellite access

Table B.2.26-3: E-UTRAN intra-frequency measurements for FDD for CE ModeB for satellite access

Table B.2.26-4: E-UTRAN intra-frequency measurements for HD-FDD for CE mode B for satellite access

## B.2.27Conditions for NB-IoT intra-frequency measurements by UE Category NB1 and NB2 for satellite access

This clause defines the NB-IoT intra-frequency NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band for satellite access. The band groups for UE category NB1 and NB2 for satellite access are defined in Section 3.5.1A. The UE category NB1 and NB2 applicability of the conditions in Appendix B.2.27 is defined in Section 3.6.

The conditions for intra-frequency measurements in normal coverage are defined in Table B.2.27-1 and B.2.27-3.

The conditions for intra-frequency measurements in denhanced coverage are defined in Table B.2.25-2 and B.2.27-4.

Table B.2.27-1: NB-IoT intra-frequency measurements for HD-FDD and TDD in normal coverage for satellite access

Table B.2.27-2: NB-IoT intra-frequency measurements for HD-FDD in enhanced coverage for satellite access

## B.2.28Conditions for E-UTRAN inter-frequency measurements by UE Category M1 for satellite access

This clause defines the E-UTRAN inter-frequency SCH_RP and SCH Ês/Iot applicable for a corresponding operating band. The UE category M1 applicability of the conditions in Appendix B.2.28 is defined in Section 3.1.

The conditions for CE mode A inter-frequency E-UTRAN FDD measurements are defined in Table B.2.28-1 and for E-UTRAN HD-FDD measurements are defined in Table B.2.28-2.

The conditions for CE mode B for inter-frequency E-UTRAN FDD measurements are defined in Table B.2.28-3 and for E-UTRAN HD-FDD measurements are defined in Table B.2.28-4.

Table B.2.28-1: E-UTRAN inter-frequency measurements for FDD for CEModeA for satellite access

Table B.2.28-2: E-UTRAN inter-frequency measurements for HD-FDD for CEModeA for satellite access

Table B.2.28-3: E-UTRAN inter-frequency measurements for FDD for CEModeB for satellite access

Table B.2.28-4: E-UTRAN inter-frequency measurements for HD-FDD for CEModeB for satellite access

## B.2.29Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access

This clause defines the NB-IoT intra-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.29 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage are defined in Table B.2.29-1 and B.2.29-2.

Table B.2.29-1: NB-IoT intra-frequency measurements for HD-FDD and TDD in normal coverage

## B.2.30Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access

This clause defines the NB-IoT inter-frequency NRSRP, NRSRP Ês/Iot, NSCH_RP and NSCH Ês/Iot applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.2.30 is defined in Section 3.6.

The conditions for measurements of intra-frequency NB-IoT cells in normal coverage for cell re-selection defined in Table B.2.29-1 and B.2.29-2 also apply for inter-frequency NB-IoT cells in normal coverage in this section.

## B.3Conditions for measurements performance requirements for UE

## B.3.1Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements

This clause defines the E-UTRAN intra-frequency RSRP applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRP and RSRQ accuracy requirements are defined in Table B.3.1-1.

Table B.3.1-1: Intra-frequency absolute RSRP and RSRQ Accuracy Requirements

## B.3.2Void

## B.3.3Conditions for inter-frequency RSRP and RSRQ Accuracy Requirements

This clause defines the E-UTRAN inter-frequency RSRP applicable for a corresponding operating band.

The conditions for inter-frequency absolute RSRP and RSRQ accuracy requirements are defined in Table B.3.1-1.

## B.3.4Conditions for inter-frequency relative RSRP and RSRQ Accuracy Requirements

This clause defines the E-UTRAN inter-frequency RSRP1,2 applicable for a corresponding operating band.

The conditions for inter-frequency relative RSRP and RSRQ accuracy requirements are defined in Table B.3.8-1.

## B.3.5Conditions for UE Rx – Tx time difference

This clause defines the E-UTRAN RSRP applicable for a corresponding operating band.

The conditions for UE Rx-Tx time difference are defined in Table B.3.1-1.

## B.3.6Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements

This sections defines the E-UTRAN intra-frequency PRP  applicable for a corresponding operating band.

The conditions for intra-frequency RSTD measurements  are defined in Table B.2.5-1.

## B.3.7Conditions for inter-frequency RSTD measurements

This sections defines the E-UTRAN inter-frequency PRP  applicable for a corresponding operating band.

The conditions for inter-frequency RSTD measurements  are defined in Table B.2.5-1.

## B.3.8Conditions for Intra-Frequency Relative RSRP Accuracy Requirements

This clause defines the E-UTRAN intra-frequency RSRP1,2 applicable for a corresponding operating band.

The conditions for intra-frequency relative RSRP accuracy requirements are specified in Table B.3.8-1.

Table B.3.8-1: Intra-frequency relative RSRP accuracy requirements

## B.3.9Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction

This clause defines the E-UTRAN intra-frequency RSRP applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRP and RSRQ accuracy requirements under time domain measurement resource restriction are as specified in Table B.3.1-1.

## B.3.10Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction

This clause defines the E-UTRAN intra-frequency RSRP1,2 applicable for a corresponding operating band.

The conditions for intra-frequency relative RSRP accuracy requirements under time domain measurement resource restriction are defined in Table B.3.8-1.

## B.3.11Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information

This clause defines the E-UTRAN intra-frequency RSRP applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRP and RSRQ accuracy requirements under time domain measurement resource restriction with CRS assistance information are as specified in Table B.3.1-1.

## B.3.12Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information

This clause defines the E-UTRAN intra-frequency RSRP1,2 applicable for a corresponding operating band.

The conditions for intra-frequency relative RSRP accuracy requirements under time domain measurement resource restriction with CRS assistance information are as specified in Table B.3.8-1.

## B.3.13Conditions for UE Rx–Tx Time Difference Measurement under Time Domain Measurement Resource Restriction with CRS Assistance Information

This clause defines the E-UTRAN RSRP applicable for a corresponding operating band.

The conditions for UE Rx-Tx time difference measurements, when time domain measurement resource restriction pattern and CRS assistance information are provided, are as defined in Table B.3.1-1.

## B.3.14Conditions for Intra-Frequency Absolute Discovery Signal Measurement Accuracy Requirements

## B.3.14.1Conditions for Intra-frequency CRS-based measurements

This clause defines the intra-frequency RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements.

The conditions for intra-frequency absolute RSRP and RSRQ accuracy requirements for CRS-based discovery signal measurements in discovery signal occasions are as in Table B.3.1-1

## B.3.14.2Conditions for Intra-frequency CSI-RS-based measurements

This clause defines the intra-frequency CSI-RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for intra-frequency absolute CSI-RSRP accuracy requirements for CSI-RS-based discovery signal measurements in discovery signal occasions are specified in Table B.3.14.2-1

Table B.3.14.2-1: Intra-frequency Absolute CSI-RSRP Accuracy Requirements

## B.3.15Conditions for Intra-Frequency Relative Discovery Signal Measurement Accuracy Requirements

## B.3.15.1Conditions for Intra-frequency CRS-based measurements

This clause defines the intra-frequency RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements.

The conditions for intra-frequency relative RSRP accuracy requirements for CRS-based discovery signal measurements in discovery signal occasions are as in Table B.3.8-1

## B.3.15.2Conditions for Intra-frequency CSI-RS-based measurements

This clause defines the intra-frequency CSI-RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for intra-frequency relative CSI-RSRP accuracy requirements for CSI-RS-based discovery signal measurements in discovery signal occasions are specified in Table B.3.15.2-1

Table B.3.15.2-1: Intra-frequency Relative CSI-RSRP Accuracy Requirements

## B.3.16Conditions for Inter-Frequency Absolute Discovery Signal Measurement Accuracy Requirements

## B.3.16.1Conditions for Inter-frequency CRS-based measurements

This clause defines the inter-frequency RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements.

The conditions for inter-frequency absolute RSRP and RSRQ accuracy requirements for CRS-based discovery signal measurements in discovery signal occasions are as in Table B.3.1-1

## B.3.16.2Conditions for Inter-frequency CSI-RS-based measurements

This clause defines the inter-frequency CSI-RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for inter-frequency absolute CSI-RSRP accuracy requirements for CSI-RS-based discovery signal measurements in discovery signal occasions are as in Table B.3.14.2-1.

## B.3.17Conditions for Inter-Frequency Relative Discovery Signal Measurement Accuracy Requirements

## B.3.17.1Conditions for Inter-frequency CRS-based measurements

This clause defines the inter-frequency RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CRS based discovery signal measurements.

The conditions for inter-frequency relative RSRP and RSRQ accuracy requirements for CRS-based discovery signal measurements in discovery signal occasions are as in Table B.3.8-1

## B.3.17.2Conditions for Inter-frequency CSI-RS-based measurements

This clause defines the inter-frequency CSI-RSRP in discovery signal occasions [16], applicable for a corresponding operating band for CSI-RS based discovery signal measurements.

The conditions for inter-frequency relative CSI-RSRP accuracy requirements for CSI-RS-based discovery signal measurements in discovery signal occasions are as in Table B.3.15.2-1.

## B.3.18Conditions for Intra-frequency Absolute RS-SINR Accuracy Requirements

This clause defines the E-UTRAN intra-frequency RSRP applicable for a corresponding operating band.

The conditions for intra-frequency absolute RS-SINR accuracy requirements are the same as defined in Table B.3.1-1.

## B.3.19Conditions for Inter-frequency Absolute RS-SINR Accuracy Requirements

This clause defines the E-UTRAN inter-frequency RSRP applicable for a corresponding operating band.

The conditions for inter-frequency absolute RS-SINR accuracy requirements are the same as defined in Table B.3.1-1.

## B.3.20Conditions for Inter-frequency Relative RS-SINR Accuracy Requirements

This clause defines the E-UTRAN inter-frequency RSRP1,2 applicable for a corresponding operating band.

The conditions for inter-frequency relative RS-SINR accuracy requirements are the same as defined in Table B.3.8-1.

## B.3.21Conditions for Intra-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 3

## B.3.21.1Conditions for RSRP measurements

This clause defines the intra-frequency absolute RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRP accuracy requirements are defined in Table B.3.21.1-1.

Table B.3.21.1-1: Intra-frequency absolute RSRP requirements

## B.3.21.2Conditions for RSRQ measurements

This clause defines the intra-frequency absolute RSRQ during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRQ accuracy requirements are the same as defined in Table B.3.21.1-1.

## B.3.21.3Conditions for CSI-RSRP measurements

This clause defines the intra-frequency absolute CSI-RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for intra-frequency absolute RSRP accuracy requirements are defined in Table B.3.21.3-1.

Table B.3.21.3-1: Intra-frequency absolute CSI-RSRP requirements

## B.3.22Conditions for Intra-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 3

## B.3.22.1Conditions for RSRP measurements

This clause defines the intra-frequency relative RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for intra-frequency relative RSRP accuracy requirements are as defined in Table B.3.22.1-1.

Table B.3.22.1-1: Intra-frequency relative RSRP requirements

## B.3.22.2Void

## B.3.22.3Conditions for CSI-RSRP measurements

This clause defines the intra-frequency relative CSI-RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for intra-frequency relative CSI-RSRP accuracy requirements are as defined in Table B.3.22.3-1.

Table B.3.22.3-1: Intra-frequency relative CSI-RSRP requirements

## B.3.23Conditions for Inter-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 3

## B.3.23.1Conditions for RSRP measurements

This clause defines the inter-frequency absolute RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency absolute RSRP accuracy requirements are the same as defined in Table B.3.21.1-1.

## B.3.23.2Conditions for RSRQ measurements

This clause defines the inter-frequency absolute RSRQ during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency absolute RSRQ accuracy requirements are the same as defined in Table B.3.21.1-1.

## B.3.23.3Conditions for CSI-RSRP measurements

This clause defines the inter-frequency absolute CSI-RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency absolute CSI-RSRP accuracy requirements are the same as defined in Table B.3.21.3-1.

## B.3.24Conditions for Inter-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 3

## B.3.24.1Conditions for RSRP measurements

This clause defines the inter-frequency relative RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency relative RSRP accuracy requirements are the same as defined in Table B.3.22.1-1.

## B.3.24.2Conditions for RSRQ measurements

This clause defines the inter-frequency relative RSRQ during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency relative RSRP accuracy requirements are the same as defined in Table B.3.22.1-1.

## B.3.24.3Conditions for CSI-RSRP measurements

This clause defines the inter-frequency relative CSI-RSRP during the configured DMTC occasion [2] under operation with frame structure 3 [16], applicable for a corresponding operating band.

The conditions for inter-frequency relative CSI-RSRP accuracy requirements are the same as defined in Table B.3.22.3-1.

## B.3.25Conditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1

This clause defines the NB-IoT intra-frequency NRSRP applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.3.25 is defined in Section 3.6.

The conditions for intra-frequency absolute NRSRP and NRSRQ accuracy requirements are defined in Table B.3.25-1.

Table B.3.25-1: NB-IoT intra-frequency absolute NRSRP and NRSRQ Accuracy Requirements

## B.3.25AConditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1 for satellite access

This clause defines the NB-IoT intra-frequency NRSRP applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.3.25A is defined in Section 3.6.

The conditions for intra-frequency absolute NRSRP and NRSRQ accuracy requirements are defined in Table B.3.25A-1.

Table B.3.25A-1: NB-IoT intra-frequency absolute NRSRP and NRSRQ Accuracy Requirements

## B.3.26Conditions for NB-IoT inter-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1

This clause defines the NB-IoT inter-frequency NRSRP applicable for a corresponding operating band. The UE category NB1 applicability of the conditions in Appendix B.3.26 is defined in Section 3.6.

The conditions for inter-frequency absolute NRSRP and NRSRQ accuracy requirements are defined in Table B.3.25-1.

## B.3.27Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements for Category 0

This clause defines the E-UTRAN intra-frequency RSRP applicable for a corresponding operating band. The UE category 0 applicability of the conditions in Appendix B.3.27 is defined in Section 3.1.

The conditions for intra-frequency absolute RSRP and RSRQ accuracy requirements are defined in Table B.3.27-1.

Table B.3.27-1: Intra-frequency absolute RSRP and RSRQ Accuracy Requirements

## B.3.28Conditions for Intra-Frequency Relative RSRP Accuracy Requirements for Category 0

This clause defines the E-UTRAN intra-frequency RSRP1,2 applicable for a corresponding operating band. The UE category 0 applicability of the conditions in Appendix B.3.28 is defined in Section 3.1.

The conditions for intra-frequency relative RSRP accuracy requirements are specified in Table B.3.28-1.

Table B.3.28-1: Intra-frequency relative RSRP accuracy requirements

## B.3.29Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for NB1

This sections defines the intra-frequency PRP applicable for a corresponding operating band for NB1.

The conditions for intra-frequency RSTD measurements are defined in Table B.2.16-1 and Table B.2.16-2

## B.3.30Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for NB1

This sections defines the inter-frequency PRP applicable for a corresponding operating band for NB1.

The conditions for inter-frequency RSTD measurements are defined in Table B.2.17-1 and Table B.2.17-2.

## B.3.31Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M1

This sections defines the inter-frequency PRP applicable for a corresponding operating band for Cat-M1.

The conditions for inter-frequency RSTD measurements are defined in sub-section B.2.20.

## B.3.32Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M2

This sections defines the inter-frequency PRP applicable for a corresponding operating band for Cat-M2.

The conditions for inter-frequency RSTD measurements are defined in sub-section B.2.21.

## B.3.33Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M1

This section defines the intra-frequency PRP applicable for a corresponding operating band for Cat-M1.

The conditions for intra-frequency RSTD measurements are defined in sub-section B.2.22.

## B.3.34Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M2

This section defines the intra-frequency PRP applicable for a corresponding operating band for Cat-M2.

The conditions for intra-frequency RSTD measurements are defined in sub-section B.2.23.

## B.4RRM Requirements Exceptions

## B.4.1General

## B.4.2Receiver sensitivity relaxation for UE supporting CA

For a UE supporting inter-band carrier aggregation configuration with uplink in one E-UTRA band, if there is a relaxation of receiver sensitivity ΔRIB,c>0 dB as defined in TS 36.101 [5], Table 7.3.1-1A, the relevant side conditions specifying received power levels (E-UTRA RSRP, SCH_RP, PRP, CSI-RSRP, and Io) shall be increased by the amount Δ=ΔRIB,c defined for each of the downlink E-UTRA bands.

NOTE:This side condition adjustment applies only for a UE supporting a single inter-band LTE CA band combination. For a UE supporting additional inter-band LTE CA band combinations, the ΔRIB,c for all bands supported by the UE, need to be studied [5].

## B.4.3Receiver sensitivity relaxation for UE configured with CA

## B.4.3.1Inter-band carrier aggregation

In this section, requirements exceptions are described for the UE configured with inter-band carrier aggregation with one uplink active in low operating band.

A relevant side condition (e.g., E-UTRA RSRP, SCH_RP, PRP, CSI-RSRP, and Io) in a requirement shall be increased by the amount Δ=L2-L1, where L1 is the reference sensitivity level specified in 36.101, Table 7.3.1-1, and L2 is the reference sensitivity level specified in 36.101, Table 7.3.1A-0a, when the following conditions are fulfilled,

-both downlink component carriers on different bands are configured with CA and active,

-the single uplink is active in the low operating band,

-the exception requirements specified in TS36.101, Table 7.3.1A-0a, apply.

If the relaxation Δ specified in this section applies, then the relaxation specified in Section B.4.2 should not be applied.

## B.4.3.2Intra-band non-contiguous carrier aggregation

For a UE configured with intra-band non-contiguous carrier aggregation configuration with uplink in one E-UTRA band, if there is a relaxation of receiver sensitivity ΔRIBNC>0 as defined in TS 36.101 [5], Table 7.3.1A-3, the relevant side conditions specifying received power levels (E-UTRA RSRP, SCH_RP, PRP, CSI-RSRP, and Io) shall be increased by the amount Δ=ΔRIBNC defined for the downlink SCC, when the following conditions are fulfilled,

-both downlink component carriers are configured with CA and active,

-one uplink carrier is active,

-the exception requirements specified in TS36.101, Table 7.3.1A-3, apply.

If the relaxation Δ specified in this section applies, then the relaxation specified in Section B.4.2 should not be applied.

## B.4.3.3Inter-band carrier aggregation with operating bands without uplink band

In this section, requirements are described for the UE configured with inter-band carrier aggregation involving one operating band without uplink band.

There is no relaxation in relevant side condition (e.g., E-UTRA RSRP, SCH_RP, PRP, CSI-RSRP, and Io) in a requirement, i.e., Δ=0, when the following conditions are fulfilled,

-both downlink component carriers on different bands are configured with CA and active,

-the single uplink is active in the high operating band,

-conditions specified in TS36.101, Table 7.3.1A-0d, apply.

If Δ specified in this section applies, then no other additional relaxation to REFSENS shall be applied.

## B.5Conditions for Measurement Performance Requirements for ProSe UE

## B.5.1Conditions for S-RSRP Accuracy Requirements

This clause defines the S-RSRP applicable for a corresponding operating band.

The conditions for absolute S-RSRP accuracy requirements are defined in Table B.5.1-1.

Table B.5.1-1: Absolute S-RSRP Requirements

## B.5.2Conditions for Relative S-RSRP Accuracy Requirements

This clause defines the S-RSRP1,2 applicable for a corresponding operating band.

The conditions for relative S-RSRP accuracy requirements are specified in Table B.5.2-1.

Table B.5.2-1: Relative S-RSRP accuracy requirements

## B.5.3Conditions for Selection/Reselection to Intra-frequency SyncRef UE

This clause defines the ProSe SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for selection/reselection to intra-frequency SyncRef UE are defined in Table B.5.3-1.

Table B.5.3-1: ProSe synchronization measurements

## B.5.4Conditions for SD-RSRP Accuracy Requirements

This clause defines the intra-frequency SD-RSRP applicable for a corresponding operating band.

The conditions for intra-frequency absolute SD-RSRP accuracy requirements are defined in Table B.5.4-1.

Table B.5.4-1: Absolute SD-RSRP Requirements

## B.5.5Conditions for Relative SD-RSRP Accuracy Requirements

This clause defines the intra-frequency SD-RSRP applicable for a corresponding operating band.

The conditions for intra-frequency relative S-RSRP accuracy requirements are specified in Table B.5.5-1.

Table B.5.5-1: Relative S-RSRP accuracy requirements

## B.6Conditions for V2X

## B.6.1Test parameters for GNSS signals

This clause defines the reference signal power levels of generated salellites for a corresponding GNSS, which will be used in V2V and V2X test cases.

Table B.6.1-1: GNSS Referenece Signal Power Parameters

## B.6.2Conditions for Absolute S-RSRP Accuracy Requirements

This clause defines the S-RSRP applicable for a corresponding operating band.

The conditions for absolute S-RSRP accuracy requirements are defined in Table B.6.2-1.

Table B.6.2-1: Absolute S-RSRP Requirements

## B.6.3Conditions for Relative S-RSRP Accuracy Requirements

This clause defines the S-RSRP1,2 applicable for a corresponding operating band.

The conditions for relative S-RSRP accuracy requirements are specified in Table B.6.3-1.

Table B.6.3-1: Relative S-RSRP accuracy requirements

## B.6.4Conditions for Selection/Reselection to Intra-frequency SyncRef UE

This clause defines the V2X SCH_RP and SCH Ês/Iot applicable for a corresponding operating band.

The conditions for selection/reselection to intra-frequency SyncRef UE are defined in Table B.6.4-1.

Table B.6.4-1: V2X synchronization measurements

## B.6.5Conditions for Absolute PSSCH-RSRP Accuracy Requirements

This clause defines the PSSCH-RSRP applicable for a corresponding operating band.

The conditions for absolute PSSCH-RSRP accuracy requirements are defined in Table B.6.5-1.

Table B.6.5-1: Absolute PSSCH-RSRP Requirements

## B.7Conditions for sTTI and 1ms-TTI with 3 Subframe HARQ Processing

## B.7.1Conditions for Maximum Timing Difference Between Uplink and Downlink Carriers in Carrier Aggregation

This clause defines the condition on the maximum timing difference between the earliest uplink carrier and the latest downlink carrier in carrier aggregation when a UE is configured with at least one serving cell that is configured with dl-STTI-Length-r15 or ShortProcessingTime =TRUE.

The timing difference between the earliest uplink carrier and the latest downlink carrier among all the serving cells configured to the UE is no larger than

when any of the serving cells is configured with dl-STTI-Length-r15=subslot and proc-Timeline-r15=nplus4set1,

when any of the serving cells is configured with dl-STTI-Length-r15 =subslot and proc-Timeline-r15=nplus6set2,

when any of the serving cells is configured with ShortProcessingTime =TRUE,

when any of the serving cells is configured with dl-STTI-Length-r15=slot,

when any of the serving cells is configured with dl-STTI-Length-r15=subslot and proc-Timeline-r15=nplus6set1,

when any of the serving cells is configured with dl-STTI-Length-r15=subslot and proc-Timeline-r15=nplus8set2.

The values of the parameters for i=1,… ,6 are as specified in Table B.7.2-1.

Table B.7.2-1: Maximum Subframe Timing Boundary Difference Between Earliest Uplink Carrier and Latest Downlink Carrier

## B.8High level test procedure for SAN RRM tests

The following high level steps are conducted for test cases for SAN defined in clauses A.13 and A.14.

-A set of ephemeris information are pre-defined for each satellite corresponding to respective epoch times in TS 36.508.

- The same ephemeris information will be maintained during the test (constant ephemerisInfo in all SBI31 updates), i.e. SAN RRM test cases are defined with fixed constant Delay and Doppler shift from Satellite access node to UE unless otherwise stated.

-    The range from which the constant Delay is selected is as follows:

-For GSO an altitude of 35,786km is considered.The range of the one-way delay between UE and satellite is from 119.375ms to 128.79ms.

-For NGSO an altitude of 600km and 1200km on a circular orbit are considered. The range of the one-way delay between UE and satellite is from 2ms (lowest value for LEO orbit 600km) to 6.67ms (highest for LEO orbit 1200 km).

-UE location is determined for the test. During the test, the test system shall provide the UE location to the DUT using AT commands.

- The ephemeris and the UE location should be designed such that elevation angle relative to the UE position shall not be smaller than 30 deg during entire test time.

-Test equipment adjusts the time and frequency of transmission according to the pre-defined and UE location.

## Annex C (informative):Change history:
