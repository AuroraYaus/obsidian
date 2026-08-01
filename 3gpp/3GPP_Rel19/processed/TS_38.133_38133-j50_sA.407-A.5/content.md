---
type: spec
aliases:
  - 38.133_38133-j50_sA.407-A.5
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.407-A.5/content.md"
---
# TS 38.133 38133-j50_sA.407-A.5

## A.4.7Measurement Performance requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause 10 for at least 90 % of the reported cases.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.4.7.1SS-RSRP

## A.4.7.1.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.1.1 and 10.1.2.1.2 for intra-frequency measurements.

## A.4.7.1.1.2Test parameters

In this set of test cases all NR cells are on the same carrier frequency. Supported test configurations are shown in table A.4.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.4.7.1.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1 In all test cases, Cell 2 is the PSCell, and Cell 3 is the target cell.

Table A.4.7.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.4.7.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.4.7.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.2.1.2.

## A.4.7.1.2EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.1.1 and 10.1.4.1.2 for inter-frequency measurements with the testing configurations in table A.4.7.1.2.1-1.

Table A.4.7.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.4.7.1.2.2Test parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.4.7.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.4.7.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.4.7.1.2.2-1: SS-RSRP inter-frequency test parameters

## A.4.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the Absolute requirement in clause 10.1.4.1.1 and Relative requirement in clause 10.1.4.1.2.

## A.4.7.1.3Void

## A.4.7.2SS-RSRQ

## A.4.7.2.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.1.1.

## A.4.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.4.7.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.4.7.2.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.4.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.4.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.4.7.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.1.1.

## A.4.7.2.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2 for inter frequency measurement.

## A.4.7.2.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.4.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.4.7.2.2.2-2. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.4.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.4.7.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.4.7.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

## A.4.7.3SS-SINR

## A.4.7.3.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.1.1.

## A.4.7.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.4.7.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.4.7.3.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.4.7.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.4.7.3.1.2-2: SS-SINR Intra frequency test parameters

## A.4.7.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.1.1.

## A.4.7.3.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.14.1.1 and 10.1.14.1.2 for interfrequency measurement.

## A.4.7.3.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.4.7.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.4.7.3.2.2-2. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell of which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.4.7.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.4.7.3.2.2-2: SS-SINR Inter frequency test parameters

## A.4.7.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.1.1 and 10.1.14.1.2.

## A.4.7.4L1-RSRP measurement for beam reporting

## A.4.7.4.1SSB based L1-RSRP measurement

## A.4.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.2 and clause 10.1.19.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.4.7.4.1.1-1.

Table A.4.7.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.4.7.4.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.4.7.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.4.7.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.4.7.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1.19.1.

## A.4.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.4.7.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause 10.1.19.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.4.7.4.2.1-1.

Table A.4.7.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.4.7.4.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.4.7.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.4.7.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.4.7.4.2.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 2 shall fulfil the requirements in clauses 10.1.19.2.

## A.4.7.5SFTD accuracy

## A.4.7.5.1SFTD accuracy

## A.4.7.5.1.1Test Purpose and Environment

The purpose of this set of tests is to verify that the SFTD measurement accuracy is within the specified limits. This test will verify the requirements as specified in clause 9.1.27 in TS 36.133 [15] for EN-DC SFTD measurements.

## A.4.7.5.1.2Test Parameters

Supported test configurations are shown in table A.4.7.5.1.2-1. In this set of test cases there are two cells on different carriers. Cell 1 is E-UTRAN PCell and Cell 2 is NR FR1 PSCell. The test parameters of Cell 1 are given in clause A.3.7.2.1. The test parameters of Cell 2 are given in table A.4.7.5.1.2-2. The SFTD between PCell and PSCell shall be set by the test equipment to one of the time differences in table A.4.7.5.1.2-3.

Table A.4.7.5.1.2-1: Supported test configurations for SFTD accuracy

Table A.4.7.5.1.2-2: Test parameters for SFTD accuracy

Table A.4.7.5.1.2-3: Timing offsets for SFTD accuracy test

## A.4.7.5.1.3Test Requirements

The SFTD reported by the UE consists of 2 elements, SFN offset and frame boundary offset between PCell and PSCell. The reported SFTD accuracy shall fulfil the requirement in clause 9.1.27 in TS 36.133 [15].

## A.4.7.5.2Void

## A.4.7.5.3Void

## A.4.7.6CLI measurements

## A.4.7.6.1EN-DC SRS-RSRP measurement accuracy with FR1 serving cell

## A.4.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the SRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.1.1 with the testing configurations for NR cells in table A.4.7.6.1.1-1.

Table A.4.7.6.1.1-1: Applicable NR configurations for FR1 SRS-RSRP accuracy test

## A.4.7.6.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.6.1.2-1 below. The test parameter for the (virtual) neighbor cell UE transmitting SRS are given in table A.4.7.6.1.2-2.

Before the test UE is configured to perform SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in the DL slots according to the SRS configuration in table A.4.7.6.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

Table A.4.7.6.1.2-1: FR1 test parameters for SRS-RSRP accuracy for PSCell

Table A.4.7.6.1.2-2: FR1 test parameters for SRS-RSRP accuracy for neighbour cell UE

Table A.4.7.6.1.2-3: SRS configuration parameters for FR1 SRS-RSRP accuracy

## A.4.7.6.1.3Test Requirements

The SRS-RSRP measurement accuracy shall fulfil the requirements in clauses 10.1.22.1.1.

## A.4.7.6.2EN-DC CLI-RSSI measurement accuracy with FR1 serving cell

## A.4.7.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.2.1 with the testing configurations for NR cells in table A.4.7.6.2.1-1.

Table A.4.7.6.2.1-1: Applicable NR configurations for FR1 CLI-RSSI accuracy test

## A.4.7.6.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.6.2.2-1 below.

Before the test UE is configured to perform CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI resource and on 1 data symbol before. The CLI-RSSI measurement resource configuration is in table A.4.7.6.2.2-2.

Table A.4.7.6.2.2-1: FR1 test parameters for CLI-RSSI accuracy

Table A.4.7.6.2.2-2: CLI-RSSI measurement resource configuration for FR1 CLI-RSSI accuracy

## A.4.7.6.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the requirements in clauses 10.1.22.2.1.

## A.4.7.7L1-SINR measurement for beam reporting

A.4.7.7.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

A.4.7.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.1 and clause 10.1.27.1 for FR1 L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.4.7.7.1.1-1, which configures the measurement resources for the CSI-RS based CMR and no dedicated IMR.

Table A.4.7.7.1.1-1: Applicable NR configurations for FR1 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

A.4.7.7.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.7.1.2-1 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.4.7.7.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.4.7.7.1.2-1: FR1 CSI-RS based L1-SINR test parameters

A.4.7.7.1.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 2 shall fulfil the requirements in clauses 10.1.27.1.

## A.4.7.7.2L1-SINR measurement with SSB based CMR and dedicated IMR

## A.4.7.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.2 and clause 10.1.27.2  for L1-SINR measurements with SSB based CMR and CSI-IM based IMR, with the testing configurations for NR cells in table A.4.7.7.2.1-1.

Table A.4.7.7.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-IM based IMR

## A.4.7.7.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.7.2.2-1 below. The absolute accuracy of L1-SINR measurements are tested by using the parameters in table A.4.7.7.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-IM resource set with two CSI-IM resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-IM resources as IMR.

Table A.4.7.7.2.2-1: FR1 L1-SINR measurement test parameters with SSB based CMR and CSI-IM based IMR

## A.4.7.7.2.3Test Requirements

The L1-SINR measurement accuracy for SSB#0+CSI-IM#0 and SSB#1+CSI-IM#1 of Cell 2 shall fulfil the requirements in clauses 10.1.27.2.

## A.4.7.7.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR

## A.4.7.7.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8.4.3 and clause 10.1.27.3 for L1-SINR measurements based on CSI-RS as both CMR and IMR with the testing configurations for NR cells in table A.4.7.7.3.1-1.

Table A.4.7.7.3.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with CSI-RS based both CMR based IMR

## A.4.7.7.3.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.7.3.2-1 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.4.7.7.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured two CSI-RS resource sets with two CSI-RS resources for each set. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as both CMR and IMR.

Table A.4.7.7.3.2-1: FR1 L1-SINR measurement test with CSI-RS based both CMR and IMR

## A.4.7.7.3.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0+CSI-RS#2 and CSI-RS#1+CSI-RS#3 of Cell 2 shall fulfil the requirements in clauses 10.1.27.3.

## A.4.7.8CSI-RSRP

## A.4.7.8.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.3.1 and 10.1.2.3.2 for intra-frequency CSI-RS based L3 measurements.

## A.4.7.8.1.2Test parameters

In this set of test cases all NR cells are on the same carrier frequency. Supported test configurations are shown in table A.4.7.8.1.2-1. Both absolute and relative accuracy of CSI-RSRP intra-frequency measurements are tested by using the parameters in table A.4.7.8.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.4.7.8.1.2-1: CSI-RSRP Intra frequency CSI-RSRP supported test configurations

Table A.4.7.8.1.2-2: CSI-RSRP Intra frequency test parameters

## A.4.7.8.1.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfill absolute requirement in clause 10.1.2.3.1 and relative requirement in clause 10.1.2.3.2.

## A.4.7.8.2EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.3.1 and 10.1.4.3.2 for inter-frequency measurements with the testing configurations in table A.4.7.8.2.1-1.

Table A.4.7.8.2.1-1: Applicable NR configurations for FR1 inter-frequency CSI-RSRP accuracy test

## A.4.7.8.2.2Test parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.4.7.8.2.2-1 below. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in table A.4.7.8.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.4.7.8.2.2-1: CSI-RSRP inter-frequency test parameters

## A.4.7.8.2.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the Absolute requirement in clause 10.1.4.2.1 and Relative requirement in clause 10.1.4.2.2.

## A.4.7.9CSI-RSRQ

## A.4.7.9.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.

## A.4.7.9.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.4.7.9.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is test by using the parameters in table A.4.7.9.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.4.7.9.1.2-1: CSI-RSRQ Intra frequency CSI-RSRQ supported test configurations

Table A.4.7.9.1.2-2: CSI-RSRQ Intra frequency test parameters

## A.4.7.9.1.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.

## A.4.7.9.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2 for inter frequency measurement.

## A.4.7.9.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.4.7.9.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test parameters in table A.4.7.9.2.2-2. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.4.7.9.2.2-1: CSI-RSRQ Inter frequency CSI-RSRQ supported test configurations

Table A.4.7.9.2.2-2: CSI-RSRQ Inter frequency test parameters

## A.4.7.9.2.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.

## A.4.7.10CSI-SINR

## A.4.7.10.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.10.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.

## A.4.7.10.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.4.7.10.1.2-1. The absolute accuracy of CSI-SINR intra-frequency measurement is tested by using the parameters in table A.4.7.10.1.2-2. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell. CSI-RS for mobility configured for Cell 2 is associated to the SSB of Cell 2, and CSI-RS for mobility configured for Cell 3 is associated to the SSB of Cell 3.

Table A.4.7.10.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

Table A.4.7.10.1.2-2: CSI-SINR Intra frequency test parameters

## A.4.7.10.1.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.

## A.4.7.10.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.4.7.10.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.14.2.1 and 10.1.14.2.2 for inter-frequency measurement.

## A.4.7.10.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.4.7.10.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test parameters in table A.4.7.10.2.2-2. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell of which specific test parameters for this test case are specified in table A.3.7.2.1-1. CSI-RS for mobility configured for Cell 2 is associated to the SSB of Cell 2, and CSI-RS for mobility configured for Cell 3 is associated to the SSB of Cell 3.

Table A.4.7.10.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

Table A.4.7.10.2.2-2: CSI-SINR Inter frequency test parameters

## A.4.7.10.2.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.2.1 and 10.1.14.2.2.

## A.4.7.11TDCP amplitude measurement accuracy

## A.4.7.11.1TDCP amplitude measurement accuracy in EN-DC

## A.4.7.11.1.1Test Purpose and Environment

The purpose of this test is to verify that the TRS based TDCP amplitude measurement accuracy is within the specified limits in the test requirements clause. The configurations for the test are specified in table A.4.7.11.1.1-1.

The test consists of two tests, Test 1 and Test 2. Each test further consists of two subtests Test 1A, 1B and Test 2A, 2B.

Test 1A: 10 Hz doppler + 15 kHz SCS FDD + 20 dB SNR

Test 1B: 300 Hz doppler + 15 kHz SCS FDD + 10 dB SNR

Test 2A: 10 Hz doppler + 30 kHz SCS TDD + 20 dB SNR

Test 2B: 300 Hz doppler + 30 kHz SCS TDD + 10 dB SNR

Relevant parameters for each test are provided in the table A.4.7.11.1.2-1. UE needs to pass Test 1A, 1B, 2A, 2B.

Table A.4.7.11.1.1-1: Applicable NR configurations for FR1 TRS based TDCP test

## A.4.7.11.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in table A.4.7.11.1.2-1. Ampliutude of TDCP is tested by using the parameters in table A.4.7.11.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured with 1 TRS set with the TRS resources in the set are configured in adjacent slot. UE is configured to perform L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.4.7.11.1.2-1: FR1 TRS based TDCP test parameters

## A.4.7.11.1.3Test Requirements

For Test 1A, the reported TDCP index shall be smaller than or equal to 6 for the 80 % of the times over repeated tests.

For Test 1B: the reported TDCP index shall be smaller than or equal to 5 for the 80 % of the times over repeated tests.

For Test 2A: the reported TDCP index shall be larger than 8 for the 80% of the times over repeated tests.

For Test 2B: the reported TDCP index shall be larger than 6 for the 80 % of the times over repeated tests.

## A.4.8Void

## A.4ANE-DC test with all NR cells in FR1

## A.4A.1Signaling characteristics

## A.4A.1.1E-UTRAN PSCell addition

## A.4A.1.1.1Test purpose and environment

The purpose of this test is to verify that the LTE PSCell addition/release delay and interruption under NE-DC are within the requirements stated in clause 8.8 and clause 8.2.3.2.3 for the case when the PSCell is known by the UE at the time of addition.

Supported test configurations are shown in table A.4A.1.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.1-1.

The test parameters for NR cell are given in Tables A.4A.1.1.1-2 and cell-specific parameters in table A.4A.1.1.1-3 below. The test consists of six successive time periods with duration of T1, T2, T3, T4, T5 and T6 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (E-UTRAN PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell1 is known to the UE.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event B1 is configured for neighbour cell (Cell2). Before the start of T2 the UE is configured with the measurement gaps (gap pattern Id # 0). The Cell2 becomes known to the UE during T2. Therefore, during T2 the UE shall report Event B1. The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2.

The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The point in time at which the RRC message to add PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

The test system shall observe the periodic reporting of CSI for PSCell during T5. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T5.

The test system shall send an RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell2) shall be sent to the UE during period T5, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell2) is received at the UE antenna connector defines the start of period T6.

Table A.4A.1.1.1-1: Applicable E-UTRA and NR configurations for NE-DC PSCell addition and Release test

Table A.4A.1.1.1-2: General Test Parameters for PSCell Addition and Release

Table A.4A.1.1.1-3: NR Cell Specific Parameters for PSCell Addition and Release

Table A.4A.1.1.1-4: E-UTRAN cell specific test parameters for PSCell Addition and Release tests

## A.4A.1.1.2Test Requirements

The UE shall transmit the PRACH to PSCell at latest 120 msNote1 into T4.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T5.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T5

The UE shall stop sending CSI reports for PSCell in at latest 20 ms into T6.

Interruption on PCell during PSCell addition and release shall not exceed the values specified for NE-DC in clause 8.2.3.2.3.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

Note1:The PSCell addition delay can be expressed as follows as specified in clause 8.8 TS 36.133 [15]:

Tconfig_EUTRAN-PSCell = 20 ms + Tactivation_time + 50 ms + TPCell_ DU + TE-UTRAN-PSCell_ DU

Where:

Tactivation_time = 20 ms

TPSCell_ DU = 0 ms

TE-UTRAN-PSCell_ DU = 30 ms

## A.4A.1.2Active BWP switch

## A.4A.1.2.1E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC

## A.4A.1.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in TS 38.133 clause 8.6, and interruption requirement for E-UTRA victim cell defined in TS 36.133 [15] clause 7.36.2.6. Supported test configurations are shown in table A.4A.1.2.1.1-1.

The test scenario comprises of one NR PCell (Cell 1), and one E-UTRA PSCell (Cell 2) as given in table A.4A.1.2.1.1-2. Cell-specific parameters of NR PCell is specified in table A.4A.1.2.1.1-3. below, and cell-specific parameters of E-UTRA PSCell are specified in table A.3.7.2.1-1.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 1 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for PCell, BWP-1 and BWP-2, in Cell 1 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

-UE is configured with a bwp-InactivityTimer timer value for PCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PCell no later than at the beginning of the DL slot right after DL slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-2 starting from the beginning of the DL slot right after DL slot (i+TBWPswitchDelay).

The starting time of PSCell(Cell 2) interruption due to BWP switch on PCell shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on PCell (Cell 1).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PCell at latest at the beginning of the DL slot right after DL slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-1 starting from the beginning of the DL slot right after DL slot (j+TBWPswitchDelay).

The starting time of PSCell (Cell 2) interruption due to BWP switch of PCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PSCell is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during BWP switch of PCell, respectively.

Table A.4A.1.2.1.1-1: DL BWP switch supported test configurations

Table A.4A.1.2.1.1-2: General test parameters for DL BWP switch in synchronous NE-DC

Table A.4A.1.2.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous NE-DC

## A.4A.1.2.1.2Test Requirements

During T1, the UE shall start to send the ACK for PCell in the DL slot right after DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PCell in the DL slot right after DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start time of PSCell interruption during PCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start time of PSCell interruption of during PCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PSCell shall not be longer than the interruption duration specified for active BWP switch in TS 36.133 [15] Clause 7.36.2.6.

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.4A.1.3Intra-frequency handover with E-UTRAN PSCell

## A.4A.1.3.1Test purpose and environment

The purpose of this test is to verify that the intra-frequency handover with PSCell addition/change delay and interruption under NE-DC are within the requirements stated in clause 6.1.5.3 for the case when the PCell and PSCell are known by the UE.

Supported test configurations are shown in table A.4A.1.3.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.1-1.

The test parameters for NR cells are given in Tables A.4A.1.3.1-2 and cell-specific parameters in table A.4A.1.3.1-3 below. The test consists of three time periods with duration of T1, T2 and T3 respectively. There are two carriers and two cells on each carrier. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) and Cell 2 (E-UTRAN PSCell) on radio channel 2. During T1 only Cell1 and Cell 2 are known to the UE.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for NR neighbour cell (Cell 3), and event-triggered reporting with Event A3 is configured for neighbour cell (Cell4). The Cell3 and Cell4 become known to the UE during T2. Therefore, during T2 the UE shall report Event A3 for the PCC frequency layer and Event A3 for the PSCC frequency layer.

The test system shall send a RRC message to the UE implying handover with PSCell, with targe PCell as Cell 3 and target PSCell as Cell 4 at the end of T2 duration. The point in time at which the RRC message implying handover with PSCell is received at the UE antenna connector defines the start of period T3. UE shall complete PRACH transmission to PCell and PSCell by end of T3.

Table A.4A.1.3.1-1: Applicable E-UTRA and NR configurations for NE-DC Handover with PSCell test

Table A.4A.1.3.1-2: General Test Parameters for Intra-frequency handover with PSCell

Table A.4A.1.3.1-3: NR Cell Specific Parameters for Intra-frequency handover with PSCell

Table A.4A.1.3.1-4: E-UTRAN cell specific test parameters for Intra-frequency handover with PSCell

## A.4A.1.3.2Test Requirements

The UE shall transmit the PRACH to PCell at latest DHOwithPSCell_PCell = 83 ms into T3.

The UE shall transmit the PRACH to PSCell at latest DHOwithPSCell_PSCell = 121 ms into T3.

The PCell handover delay, DHOwithPSCell_PCell, is equals the applicable RRC procedure delay (16 ms) defined in clause 12 in TS 38.331 [2] plus the PCell interruption time (Tinterrupt = 67 ms) define in clause 6.1.5.3.2.

PSCell addition/change delay, DHOwithPSCell_PSCell is defined in clause 6.1.5.3.3 as below.

DHOwithPSCel_PSCell = Tconfig_EUTRAN-PSCell + Tprocessing_margin

Tconfig_EUTRAN-PSCell = TRRC_delay + Tactivation_time + 50 ms + TE-UTRAN-PSCell_ DU

Where:

Tprocessing_margin = 5 ms

TRRC_delay = 16 ms

Tactivation_time = 20 ms

TE-UTRAN-PSCell_DU = 30 ms

All the above test requirements shall be fulfilled in order for the observed handover with PSCell delay to be counted as correct. The rate of correct observed handover with PSCell delay during repeated tests shall be at least 90 %.

## A.4A.1.4Handover with PSCell from NE-DC to NE-DC with unknown target PSCell

## A.4A.1.4.1Test Purpose and Environment

This test is to verify the requirement for the requirements of HO with PSCell requirements specified in clause 6.1.5.3. HO from NR FR1 to NR FR1 and E-UTRAN PSCell change are tested independently in the same test, with different end points.

## A.4A.1.4.2Test Parameters

Supported test configurations are shown in table A.4A.1.4.2-1. Both handover delay and interruption length are tested by using the parameters in tables A.4A.1.4.2-2, and A.4A.1.4.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, UE is connected to Cell 1 (NR PCell) and Cell 3 (LTE PSCell 1). The UE may not have any timing information of Cell 2 at the start of T1. Starting of T1, Cell 2 becomes detectable and known to UE for entire T1 duration.

Cell 4 is turned on at the end of T1. At the start of T2, UE do not have timing information of Cell 4 (LTE PSCell 2).

During T2, UE reports Event A3 to TE and TE shall send an RRC message implying handover from Cell 1 to Cell 2 and PSCell change from Cell 3 to Cell 4 in the same RRC message implying handover with PSCell change during T2.

Start of T3 is defined as the end of the last TTI containing the RRC message implying handover with PSCell change. UE shall complete PRACH transmission to PCell and PSCell by end of T3.

Table A.4A.1.4.2-1: NE-DC test configurations for NE-DC to NE-DC HO with PSCell

Table A.4A.1.4.2-2: General test parameters NE-DC to NE-DC HO with PSCell

Table A.4A.1.4.2-3: Cell specific test parameters for NR for NE-DC to NE-DC HO with PSCell test

Table A.4A.1.4.2-4: E-UTRAN cell specific test parameters for EUTRA PSCell addition/change

## A.4A.1.4.3Test Requirements

## A.4A.1.4.3.1Test Requirements for NR HO

The UE shall start to transmit the PRACH to Cell 2 less than 83 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 16 ms and is specified in clause 12 in TS 38.331 [2], RRC reconfiguration (LTE/NR SCG

establishment/ modification/ release).

Tinterrupt = 67 ms in the test. Tinterrupt is defined in clause 6.1.5.3.2.

This gives a total of 83 ms.

## A.4A.1.4.3.2Test Requirements for LTE PSCell Change

The UE shall transmit the PRACH to PSCell at latest 131 msNote1 into T3.

There cannot be any interruptions on PCell during PSCell change.

All the above test requirements shall be fulfilled in order for the observed PSCell change delay to be counted as correct. The rate of correct observed PSCell change delay during repeated tests shall be at least 90 %.

Note1:The PSCell change delay can be expressed as follows as specified in clause 6.1.5.3.3 of TS 38.133 is

DHOwithPSCel_PSCell = Tconfig_EUTRAN-PSCell + 5 ms,

Tconfig_EUTRAN-PSCell  =TRRC_delay + Tactivation_time + 50 ms + TE-UTRAN-PSCell_ DU,

Tactivation_time is the PSCell activation delay. If the PSCell is known, then Tactivation_time is 20 ms. If the PSCell is unknown, then Tactivation_time is 30 ms provided the PSCell can be successfully detected on the first attempt.

TE-UTRAN-PSCell_DU is the delay uncertainty in acquiring the first available PRACH occasion in the E-UTRAN PSCell. TE-UTRAN-PSCell_DU is up to 30 ms.

Where:

TRRC_delay = 16 ms

Tactivation_time = 30 ms

TE-UTRAN-PSCell_DU = 30 ms

## A.4A.2Measurement performance

## A.4A.2.1SFTD accuracy

## A.4A.2.1.1SFTD accuracy

## A.4A.2.1.1.1Test Purpose

The purpose of this set of tests is to verify that the SFTD measurement accuracy is within the specified limits. This test will verify the requirements as specified in clause 10.21.1.1 for NE-DC SFTD measurements.

## A.4A.2.1.1.2Test Environment

Supported test configurations are shown in table A.4A.2.1.1.2-1. In this set of test cases there are two cells on different carriers. Cell 1 is NR FR1 PCell and Cell 2 is E-UTRAN target cell. The test parameters of Cell 1 are given in clause A.4A.2.1.1.2-2. The test parameters of Cell 2 are given in table A.3.7.2.1. The SFTD between PCell and target cell shall be set by the test equipment to one of the time differences in table A.4A.2.1.1.2-3.

Table A.4A.2.1.1.2-1: Supported test configurations for SFTD accuracy

Table A.4A.2.1.1.2-2: Test parameters for SFTD accuracy (Cell 1)

Table A.4A.2.1.1.2-3: Timing offsets for SFTD accuracy test

## A.4A.2.1.1.3Test Requirements

The SFTD reported by the UE consists of 2 elements, SFN offset and frame boundary offset between PCell and E-UTRAN target cell. The reported SFTD accuracy shall fulfil the requirement in clause 10.1.21.1.

## A.5EN-DC tests with one or more NR cells in FR2

## A.5.1Void

## A.5.2Void

## A.5.3RRC_CONNECTED state mobility

## A.5.3.1Void

## A.5.3.2RRC Connection Mobility Control

## A.5.3.2.1Void

## A.5.3.2.2Random Access

## A.5.3.2.2.14-step RA type c ontention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell or SCell in FR2. Supported test parameters are shown in table A.5.3.2.2.1.1-1. UE capable of EN-DC with PSCell or SCell in FR2 needs to be tested by using the parameters in table A.5.3.2.2.1.1-2 and table A.5.3.2.2.1.1-3.

Table A.5.3.2.2.1.1-1: Supported test configurations for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.1.1-2: General test parameters for contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.1.1-3: OTA-related test parameters for contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.5.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.5.3.2.2.1.2.5Void

A.5.3.2.2.1.2.6Void

A.5.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.5.3.2.2.24-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell or SCell in FR2. Supported test parameters are shown in table A.5.3.2.2.2.1-1. UE capable of EN-DC withPSCell or SCell in FR2 needs to be tested by using the parameters in table A.5.3.2.2.2.1-2 and table A.5.3.2.2.2.1-3 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.5.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.2.1-3: OTA-related test parameters for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.5.3.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.5.3.2.2.32-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell or SCell in FR2. Supported test parameters are shown in table A.5.3.2.2.3.1-1. UE capable of EN-DC with PSCell or SCell in FR2 needs to be tested by using the parameters in table A.5.3.2.2.3.1-2 and table A.5.3.2.2.3.1-3.

Table A.5.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.3.1-3: OTA-related test parameters for 2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.5.3.2.2.3.2.1MsgA Transmission

To test the UE behaviour specified in clause 6.2.2.3.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first MsgA preamble transmission shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA PRACH and MsgA PUSCH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.3.2.2MsgB Reception

To test the UE behaviour specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB with successRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgBs contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first MsgA preamble transmission shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.3.2.3No MsgB Reception

To test the UE behaviour specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB with successRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the RA Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble transmission shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA PRACH and MsgA PUSCH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.5.3.2.2.42-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell or SCell in FR2. Supported test parameters are shown in table A.5.3.2.2.4.1-1. UE capable of EN-DC with PSCell or SCell in FR2 needs to be tested by using the parameters in table A.5.3.2.2.4.1-2 and table A.5.3.2.2.4.1-3 for SSB-based non-contention based random access test.

Table A.5.3.2.2.4.1-1: Supported test configurations for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.4.1-2: General test parameters for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

Table A.5.3.2.2.4.1-3: OTA-related test parameters for non-contention based random access test in FR2 for PSCell/SCell in EN-DC

A.5.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.5.3.2.2.4.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.4.2.3MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR MAC subPDU.

The UE shall fallback to the 4-step RA type by transmitting the msg3 containing the payload of MsgA PUSCH and monitoring contention resolution as described in clause 8.2A in TS 38.213 [3].

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1.2.

A.5.3.2.2.4.2.4No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.5.3.2.3Void

## A.5.3.3Handover with PSCell with known FR2 target PSCell

## A.5.3.3.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell change delays in handover with PSCell from EN-DC to EN-DC are within the requirements stated in clause 5.8 of TS 36.133 [15] for the case when the source PSCell is in FR1 and the target PSCell in FR2 is known by the UE at the time of handover with PSCell.

Supported test configurations are shown in A.5.3.3.1-1. The test parameters for the E-UTRA cells are given in table A.3.7.2.2-1. The E-UTRA Cell 1 will handover to E-UTRA Cell 2 in this test case. The test parameters for NR cells are given in tables A.5.3.3.1-2, cell-specific parameters in A.5.3.3.1-3 and OTA parameters in A.5.3.3.1-4 below. The test consists of three successive time periods with duration of T1, T2 and T3. There are four carriers each with one cell. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on E-UTRA and Cell 4 (SCell) on NR. The UE is monitoring the PCell and PSCell.

The test system shall send a RRC message to the UE to handover with PSCell (target PCell Cell 2, target PSCell Cell 4). The RRC message (to handover with PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The RRC message to handover with PSCell shall be sent to the UE during period T1. The point in time at which the RRC message to handover with PSCell (Cell2, Cell 4) is received at the UE antenna connector defines the start of period T2.

The test system shall observe the periodic reporting of CSI for the target PSCell during T3. The point in time at which the UE has sent PRACH to the target PSCell (Cell 4) defines the start of period T3.

Table A.5.3.3.1-1: Supported test configurations for Handover with PSCell

Table A.5.3.3.1-2: General Test Parameters for Handover with PSCell

Table A.5.3.3.1-3: Cell specific test parameters for Handover with PSCell

Table A.5.3.3.1-4: OTA related test parameters for Handover with PSCell

## A.5.3.3.2Test Requirements

The UE shall transmit the PRACH to PSCell at latest 107 msNote1 into T2.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T3.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T3

All the above test requirements shall be fulfilled for the observed PSCell change delay to be counted as correct. The rate of correct observed PSCell change delay during repeated tests shall be at least 90 %.

Note1:The PSCell change delay can be expressed as follows as specified in clause 5.8.1.2 of TS 36.133 [15]:

DHOwithPSCel_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + TPCell_DU + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 45 ms

Tsearch = 0 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

TPCell_ DU = 0 ms

## A.5.3.3.3Void

## A.5.3.3.4Void

## A.5.3.3.5Void

## A.5.3.3.6Void

## A.5.4Timing

## A.5.4.1UE transmit timing

## A.5.4.1.1NR UE Transmit Timing Test for FR2

## A.5.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table 5.4.1.1.1-1.

Table A.5.4.1.1.1-1: Supported test configurations for FR2 PSCell

The test consists of E-UTRA PCell and NR PSCell. The configuration for E-UTRA is given in A.3.7.2.1. Tables A.5.4.1.1.1-2 and A.5.4.1.1.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.5.4.1.1.1-3.

Table A.5.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.5.4.1.1.1-2A: OTA related test parameters

Table A.5.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

Table A.5.4.1.1.1-4: Void

## A.5.4.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.2-1 and setup NR PSCell according to parameters given in table A.5.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.5.4.1.1.2-1

Table A.5.4.1.1.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

## A.5.4.1.2NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18

## A.5.4.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits, for UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18 and is configured with 2 TAGs for multi-DCI multi-TRP operation. UE is also configured with dl-OrJointTCI-StateList or ul-TCI-State-List. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.5.4.1.2.1-1.

Table A.5.4.1.2.1-1: Supported test configurations for FR2 PSCell

The test consists of E-UTRA PCell and NR PSCell. The configuration for E-UTRA is given in A.3.7.2.1. Tables A.5.4.1.2.1-2 and A.5.4.1.2.1-2A define the parameters to be configured and strength of the transmitted signals. The NR PSCell is configured with two TRPs in the test. Each TRP is associated with a CORESET, with coresetPoolIndex-r16 is set to 0 for the first TRP and set to 1 for the second TRP. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.5.4.1.2.1-3.

For UE not support the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test1 and Test3.

For UE supports the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test2 and Test4.

Table A.5.4.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.5.4.1.2.1-2A: OTA related test parameters

Table A.5.4.1.2.1-3: SRS Configuration for Timing Accuracy Test

Table A.5.4.1.2.1-4: Void

## A.5.4.1.2.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.2-1 and setup NR PSCell according to parameters given in table A.5.4.1.2.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB for each TAG.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.5.4.1.2.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.5.4.1.2.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For TRP#2, the test system shall verify there is no adjustment. Skip this step for Test 3 and Test 4 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 3 and Test 4 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

## A.5.4.1.3NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI

## A.5.4.1.3.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits, for UE for UE not configured PL offset and is configured with 2 TAGs for single-DCI multi-TRP operation. UE is also configured with dl-OrJointTCI-StateList. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.5.4.1.3.1-1.

Table A.5.4.1.3.1-1: Supported test configurations for FR2 PSCell

The test consists of E-UTRA PCell and NR PSCell. The configuration for E-UTRA is given in A.3.7.2.1. Tables A.5.4.1.3.1-2 and A.5.4.1.3.1-2A define the parameters to be configured and strength of the transmitted signals. The NR PSCell is configured with two TRPs in the test. Each TRP is associated with a CORESET, with coresetPoolIndex-r16 is set to 0 for the first TRP and set to 1 for the second TRP. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.5.4.1.3.1-3.

Table A.5.4.1.3.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.5.4.1.3.1-2A: OTA related test parameters

Table A.5.4.1.3.1-3: SRS Configuration for Timing Accuracy Test

## A.5.4.1.3.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.2-1 and setup NR PSCell according to parameters given in table A.5.4.1.3.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected corresponding path of DL SSB (TRP#1) for each TAG and detected another path of DL SSB (TRP#2).

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.5.4.1.3.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.5.4.1.3.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of corresponding DL SSB (TRP#1) of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For TRP#2, the test system shall verify there is adjusted as well. Skip this step for Test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

## A.5.4.2UE timer accuracy

## A.5.4.3Timing advance

## A.5.4.3.1EN-DC FR2 timing advance adjustment accuracy

## A.5.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.5.4.3.1.2Test Parameters

Supported test configurations are shown in table A.5.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in tables A.5.4.3.1.2-2, A.5.4.3.1.2-3, A.5.4.3.1.2-3A and A.5.4.3.1.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and Cell 2 is the PSCell is in the secondary Timing Advance Group (sTAG). Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.5.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for PSCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.5.4.3.1.2-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321, shall be configured so that it does not expire in the duration of the test.

Table A.5.4.3.1.2-1: Timing advance supported test configurations

Table A.5.4.3.1.2-2: General test parameters for timing advance

Table A.5.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.5.4.3.1.2-3A: OTA related test parameters

Table A.5.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.5.4.3.1.3Test Requirements

The UE shall apply the signalled Timing Advance value for PSCell in sTAG to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11.

The Timing Advance adjustment accuracy for PSCell in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.5.4.3.2EN-DC FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs

## A.5.4.3.2.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3 for asymmetric DL sTRP/UL mTRP deployment with two TAs when PL-offset is configured joint/UL TCI state(s).

## A.5.4.3.2.2Test Parameters

Supported test configurations are shown in table A.5.4.3.2.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in tables A.5.4.3.2.2-2, A.5.4.3.2.2-3, A.5.4.3.2.2-3A and A.5.4.3.2.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and Cell 2 is the PSCell is in the secondary Timing Advance Group (sTAG). The NR PSCell is configured with two TRPs in the test. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.5.4.3.2.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for PSCell in sTAG.

During time period T1, the test equipment shall send message with a Timing Advance Command MAC Control Element for sTAG for each of the TAGs, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.5.4.3.2.2-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE for both TAGs.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321, shall be configured so that it does not expire in the duration of the test.

Table A.5.4.3.2.2-1: Timing advance supported test configurations

Table A.5.4.3.2.2-2: General test parameters for timing advance

Table A.5.4.3.2.2-3: Cell specific test parameters for timing advance

Table A.5.4.3.2.2-3A: OTA related test parameters

Table A.5.4.3.2.2-4: Sounding Reference Symbol Configuration for timing advance

## A.5.4.3.2.3Test Requirements

For TRP1 the UE shall apply the signalled Timing Advance value for PSCell in sTAG to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11. For TRP2 there shall be no change in the uplink timing.

The Timing Advance adjustment accuracy for PSCell TAGs in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.5.5Signaling characteristics

## A.5.5.1Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

Editor NOTE: The metric for the detection of the UE UL transmitted signal by the TE is FFS.

## A.5.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode

## A.5.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.1.1-1. The test parameters are given in tables A.5.5.1.1.1-2, A.5.5.1.1.1-3, and A. 5.5.1.1.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.5.5.1.1.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.5.5.1.1.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.1.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.5.5.1.1.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.5.5.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.5.5.1.1.1-1: SNR variation for out-of-sync testing

Figure A.5.5.1.1.1-2: Time multiplexed downlink transmissions

## A.5.5.1.1.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.2Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode

## A.5.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.2.1-1. The test parameters are given in tables A.5.5.1.2.1-2, and A.5.5.1.2.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.5.5.1.2.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.5.5.1.2.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.2.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

Table A.5.5.1.2.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for in-sync radio link monitoring tests in non-DRX mode

Table A.5.5.1.2.1-4: Void

Figure A.5.5.1.2.1-1: SNR variation for in-sync testing

Figure A.5.5.1.2.1-2: Time multiplexed downlink transmissions

## A.5.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode

## A.5.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.3.1-1. The test parameters are given in tables A.5.5.1.3.1-2, and A.5.5.1.3.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.1.3.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.3.1-2: General test parameters for FR2 out-of-sync testing in DRX mode

Table A.5.5.1.3.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for out-of-sync radio link monitoring tests in DRX mode

Table A.5.5.1.3.1-4: Void

Table A.5.5.1.3.1-5: Void

Figure A.5.5.1.3.1-1: SNR variation for out-of-sync testing

## A.5.5.1.3.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.4Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode

## A.5.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.4.1-1. The test parameters are given in tables A.5.5.1.4.1-2, and A.5.5.1.4.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.1.4.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.4.1-2: General test parameters for FR2 in-sync testing in DRX mode

Table A.5.5.1.4.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for in-sync radio link monitoring test in DRX mode

Table A.5.5.1.4.1-4: Void

Table A.5.5.1.4.1-5: Void

Figure A.5.5.1.4.1-1: SNR variation for in-sync testing.

## A.5.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.5EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode

A.5.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR2 TDD PSCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.5.5.1.5.1-1, A.5.5.1.5.1-2, A.5.5.1.5.1-3 and A.5.5.1.5.1-3A below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.5.1-1 shows the variation of the downlink SNR in the E-UTRAN PCell and the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms). In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.5.5.1.5.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.5.1-2: General test parameters for FR2 PSCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.5.5.1.5.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.5.5.1.5.1-3A: Measurement gap configuration for FR2 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.5.5.1.5.1-4: Void

Figure A.5.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

A.5.5.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 (PSCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

The UE shall stop transmitting uplink signal in Cell 2 (PSCell) no later than time point C (D1 after the start of the time duration T3) on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.6EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode

A.5.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR2 TDD PSCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.5.5.1.6.1-1, A.5.5.1.6.1-2, and A.5.5.1.6.1-3 below. There are two cells, cell 1which is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.1.6.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5ms. In the test, DRX configuration is not enabled. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.5.5.1.6.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.6.1-2: General test parameters for FR2 PSCell for CSI-RS in-sync testing in non-DRX mode

Table A.5.5.1.6.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.5.5.1.6.1-3A: Void

Table A.5.5.1.6.1-4: Void

Figure A.5.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

A.5.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.7EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode

A.5.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when DRX is used. This test will partly verify the FR2 TDD PSCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.5.5.1.7.1-1, A.5.5.1.7.1-2, and A.5.5.1.7.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.7.1-1 shows the variation of the downlink SNR in the E-UTRAN PCell and the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.5.5.1.7.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.7.1-2: General test parameters for FR2 PSCell for CSI-RS out-of-sync testing in DRX mode

Table A.5.5.1.7.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in DRX mode

Table A.5.5.1.7.1-3A: Void

Table A.5.5.1.7.1-4: Void

Table A.5.5.1.7.1-5: Void

Table A.5.5.1.7.1-6: Void

Figure A.5.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

A.5.5.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 (PSCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

The UE shall stop transmitting uplink signal in Cell 2 (PSCell) no later than time point C (D1 after the start of the time duration T3) on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.8EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode

A.5.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when DRX is used. This test will partly verify the FR2 TDD PSCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.5.5.1.8.1-1, A.5.5.1.8.1-2, A.5.5.1.8.1-3 and A.5.5.1.8.1-3A below. There are two cells, Cell 1which is the E-UTRAN PCell, and Cell 2 is the NR PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.1.8.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms). In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.5.5.1.8.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.8.1-2: General test parameters for FR2 PSCell for CSI-RS in-sync testing in non-DRX mode

Table A.5.5.1.8.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in DRX mode

Table A.5.5.1.8.1-3A: Measurement gap configuration for FR2 CSI-RS in-sync radio link monitoring in DRX mode

Table A.5.5.1.8.1-4: Void

Table A.5.5.1.8.1-5: Void

Table A.5.5.1.8.1-6: Void

Figure A.5.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.5.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.9EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR2

## A.5.5.1.9.1Test Purpose and Environment

The purpose is to verify that the NR UE correctly follows the RLM scheduling restrictions requirements defined in clause 8.1.7. This test verifies that the UE correctly receive the PDCCH scheduled on the symbols right before the RLM SSB symbols without overlap so that it sends ACK/NACK correctly. The test case is only applicable to UE which supports pdcch-MonitoringAnyOccasions or pdcch-MonitoringAnyOccasionsWithSpanGap.

Two cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and NR FR2 PSCell (Cell 2). The test parameters for NR PSCell are given in table A.5.5.1.9.1-1, table A.5.5.1.9.1-2 and table A.5.5.1.9.1-3 below and the parameters and applicability for the E-UTRAN cell are defined in A.3.7.2. The UE is required during time period T1 to transmit ACK/NACK correctly upon scheduling of PDSCH.

Table A.5.5.1.9.1-1: Supported test configurations

Table A.5.5.1.9.1-2: General test parameters for RLM scheduling restriction test case in FR2

Table A.5.5.1.9.1-3: Cell specific test parameters for RLM scheduling restriction test case in FR2

Figure A.5.5.1.9.1-1: Time multiplexed downlink transmissions

## A.5.5.1.9.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.1.7.3.

The UE shall be continuously scheduled by PDCCH on the symbols right before each SSB which is not covered by SMTC during the entire length of T1. The UE shall transmit ACK/NACK for every scheduled PDCCH during the time duration T1.

## A.5.5.1.10Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion

## A.5.5.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.2.4 for UE fulfilling good serving cell quality criterion.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.10.1-1. The test parameters are given in tables A.5.5.1.10.1-2, and A.5.5.1.10.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.10.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.1.10.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.10.1-2: General test parameters for FR2 out-of-sync testing for UE fulfilling relaxed measurement criterion

Table A.5.5.1.10.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for out-of-sync radio link monitoring tests for UE fulfilling relaxed measurement criterion

Figure A.5.5.1.10.1-1: SNR variation for out-of-sync testing

## A.5.5.1.10.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.11Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx

## A.5.5.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.11.1-1. The test parameters are given in tables A.5.5.1.11.1-2, and A.5.5.1.11.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.11.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.5.5.1.11.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2 and configured with groupBasedBeamReporting-r17. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.5.5.1.11.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.1.11.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.5.5.1.11.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode

Figure A.5.5.1.11.1-1: SNR variation for out-of-sync testing

Figure A.5.5.1.11.1-2: Time multiplexed downlink transmissions

## A.5.5.1.11.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.1.12EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP

## A.5.5.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used and when CD-SSB is outside active BWP. This test will partly verify the FR2 TDD PSCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in A.5.5.1.5.

The test environment is the same as in A.5.5.1.5.

NOTE: The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in A.5.5.1.5.2.

## A.5.5.1.13Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP

## A.5.5.1.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when CD-SSB is outside active BWP. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

The test environment is the same as in A.5.5.1.1 with following exceptions in table A.5.5.1.1.1-2.

## A.5.5.1.13.2Test Requirements

The test requirements are the same as in A.5.5.1.1.2.

## A.5.5.1.14EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

## A.5.5.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell for UE supporting FG 53-3. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.5.5.1.14.1-1. The test parameters are given in tables A.5.5.1.14.1-2, A.5.5.1.14.1-3, and A. 5.5.1.x.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.5.5.1.14.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.5.5.1.14.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.5.5.1.14.1-1: Supported test configurations for FR2 PSCell for UE supporting NCD-SSB based measurement outside active BWP

Table A.5.5.1.14.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.5.5.1.14.1-3: OTA related cell specific test parameters for FR2 (Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.5.5.1.14.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.5.5.1.14.1-1: SNR variation for out-of-sync testing

Figure A.5.5.1.14.1-2: Time multiplexed downlink transmissions

## A.5.5.1.14.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2Interruption

## A.5.5.2.1E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

## A.5.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that when E-UTRA PCell is in DRX and NR PSCell is in non-DRX, NR PSCell interruptions due to transitions from active to non-active and from non-active to active during LTE PCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.1.1-1.

The general test parameters are given in table A.5.5.2.1.1-2, and NR cell specific test parameters are given in table A.5.5.2.1.1-3 and A.5.5.2.1.1-4. The E-UTRAN PCell DRX configuration parameters are given in table A.5.5.2.1.1-5 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.2-1. In the test there are two cells: Cell 1 and Cell2. Cell 1 is LTE PCell on  and Cell2 is NR FR2 PSCell. The test consists of one time period, with duration of T1. During T1, NR PSCell is continuously scheduled in DL while LTE PCell is not scheduled and has DRX configured. Prior to the start of the time duration T1, Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. Prior to start of T1 the DRX inactivity timer for the LTE PCell has already expired. During T1 the UE shall be continuously scheduled on NR PSCell while not scheduled on LTE PCell. PDCCH indicating a new transmission on PSCell shall be sent continuously during the entire time duration to ensure UE would not enter DRX state on PSCell.

Table A.5.5.2.1.1-1: Interruption at transitions between active and non-active during DRX supported test configurations

Table A.5.5.2.1.1-2: General test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

Table A.5.5.2.1.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

Table A.5.5.2.1.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

Table A.5.5.2.1.1-5: Void

## A.5.5.2.1.2Test Requirements

The UE shall be continuously scheduled in NR PSCell during the entire length of T1. UE shall not be scheduled in LTE PCell during T1. During the time duration T1 the UE shall transmit at least 99 % of ACK/NACK on NR PSCell.

Interruption on NR PSCell shall not exceed 0.625 ms (5 slots) as defined in clause 8. 2.1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.2E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

## A.5.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that when LTE PCell is in DRX and NR PSCell is in non-DRX, NR PSCell interruptions due to transitions from active to non-active and from non-active to active during LTE PCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.2.1-1.

The general test parameters are given in table A.5.5.2.2.1-2, and NR cell specific test parameters are given in table A.5.5.2.2.1-3 and A.5.5.2.2.1-4. The E-UTRAN PCell DRX configuration parameters are given in table A.5.5.2.2.1-5 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.2-1. In the test there are two cells: Cell 1 and Cell2. Cell 1 is LTE PCell and Cell2 is NR PSCell. The test consists of one time period, with duration of T1. During T1, NR PSCell is continuously scheduled in DL while LTE PCell is not scheduled and has DRX configured. Prior to the start of the time duration T1, Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. Prior to start of T1 the DRX inactivity timer for the LTE PCell has already expired. During T1 the UE shall be continuously scheduled on NR PSCell while not scheduled on LTE PCell. PDCCH indicating a new transmission on PSCell shall be sent continuously during the entire time duration to ensure UE would not enter DRX state on PSCell.

Table A.5.5.2.2.1-1: Interruption at transitions between active and non-active during DRX supported test configurations

Table A.5.5.2.2.1-2: General test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.2.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.2.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.2.1-5: Void

## A.5.5.2.2.2Test Requirements

The UE shall be continuously scheduled in NR PSCell during the entire length of T1. UE shall not be scheduled in LTE PCell during T1. During the time duration T1 the UE shall transmit at least 99 % of ACK/NACK on NR PSCell.

Interruption on NR PSCell shall not exceed 0.625 ms (5 slots) as defined in clause 8. 2.1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.3E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC

## A.5.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that for NR PSCell interruptions during the measurement on the deactivated NR SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for and NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.3.1-1.

The general test parameters are given in table A.5.5.2.3.1-2, and NR cell specific test parameters are given in table A.5.5.2.3.1-3 and A.5.5.2.3.1-4 below. The E-UTRAN cell specific test parameters can be found in table A.3.7.2.1-2. In the test there are three cells: Cell 1, Cell2 and Cell3. Cell 1 is LTE PCell, Cell2 and Cell 3 are NR FR2 PSCell and NR FR2 deactivated SCell, respectively. Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell2. The point in time at which the RRC message including measCycleSCell for the deactivated NR SCells is received by the UE, defines the start of time period T1. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.5.5.2.3.1-1: Interruption during measurements on deactivated NR SCC supported test configurations

Table A.5.5.2.3.1-2: General test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC

Table A.5.5.2.3.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC

Table A.5.5.2.3.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC

## A.5.5.2.3.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on NR PSCell.

If the NR PSCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PSCell immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.3.2-1.

If the NR PSCell is in the same band as the deactivated SCell, the UE is only allowed to cause an interruption on PSCell no earlier than 4 slot before an SMTC and no later than 4 slot after the SMTC. the interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.3.2-2.

Table A.5.5.2.3.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.5.5.2.3.2-2: Interruption duration if the NR PSCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.4E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

## A.5.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that for NR PSCell interruptions during the measurement on the deactivated NR SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.4.1-1.

The general test parameters are given in table A.5.5.2.4.1-2, and NR cell specific test parameters are given in table A.5.5.2.4.1-3 and A.5.5.2.4.1-4 below. The E-UTRAN cell specific test parameters can be found in table A.3.7.2.1-2. In the test there are three cells: Cell 1, Cell2 and Cell3. Cell 1 is LTE PCell, Cell2 and Cell 3 are NR FR2 PSCell and NR FR2 deactivated SCell, respectively. Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell2. The point in time at which the RRC message including measCycleSCell for the deactivated NR SCells is received by the UE, defines the start of time period T1. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.5.5.2.4.1-1: Interruption during measurements on deactivated NR SCC supported test configurations

Table A.5.5.2.4.1-2: General test parameters for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

Table A.5.5.2.4.1-3: NR cell specific test parameters for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

Table A.5.5.2.4.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

## A.5.5.2.4.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on NR PSCell.

If the NR PSCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PSCell immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.4.2-1.

If the NR PSCell is in the same band as the deactivated SCell, the UE is only allowed to cause an interruption on PSCell no earlier than 4 slot before an SMTC and no later than 4 slot after the SMTC. the interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.4.2-2.

Table A.5.5.2.4.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.5.5.2.4.2-2: Interruption duration if the NR PSCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.5E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC

## A.5.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that for NR PSCell interruptions during the measurement on the deactivated E-UTRAN SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.5.1-1.

The general test parameters are given in table A.5.5.2.5.1-2, and NR cell specific test parameters are given in table A.5.5.2.5.1-3 and A.5.5.2.5.1-4 below. The E-UTRAN cell specific test parameters can be found in table A.3.7.2.1-2. In the test there are three cells: Cell 1, Cell2 and Cell3. Cell 1 and Cell3 are LTE PCell and LTE deactivated SCell, respectively, and Cell2 is NR FR2 PSCell. Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell2. The point in time at which the RRC message including measCycleSCell or allowInterruptions for the deactivated E-UTRA SCell is received by the UE, defines the start of time period T1. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.5.5.2.5.1-1: Interruption during measurements on deactivated E-UTRAN SCC supported test configurations

Table A.5.5.2.5.1-2: General test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC

Table A.5.5.2.5.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E_UTRAN SCC in synchronous EN-DC

Table A.5.5.2.5.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E_UTRAN SCC in synchronous EN-DC

## A.5.5.2.5.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on NR PSCell. The UE is only allowed to cause interruptions immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.5.2-1.

Table A.5.5.2.5.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.5.5.2.5.2-2: Void

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.6E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC

## A.5.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that for NR PSCell interruptions during the measurement on the deactivated E-UTRAN SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in clause 8. 2.1.2. Supported test configurations are shown in table A.5.5.2.6.1-1.

The general test parameters are given in table A.5.5.2.6.1-2, and NR cell specific test parameters are given in table A.5.5.2.6.1-3 and A.5.5.2.6.1-4 below. The E-UTRAN cell specific test parameters can be found in table A.3.7.2.1-2. In the test there are three cells: Cell 1, Cell2 and Cell3. Cell 1 and Cell3 are LTE PCell and LTE deactivated SCell, respectively, and Cell2 is NR FR2 PSCell. Cell 1 shall be configured as LTE PCell and Cell2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell2. The point in time at which the RRC message including measCycleSCell or allowInterruptions for the deactivated E-UTRA SCell is received by the UE, defines the start of time period T1. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.5.5.2.6.1-1: Interruption during measurements on deactivated E-UTRAN SCC supported test configurations

Table A.5.5.2.6.1-2: General test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E_UTRAN SCC in asynchronous EN-DC

Table A.5.5.2.6.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E_UTRAN SCC in asynchronous EN-DC

Table A.5.5.2.6.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated E_UTRAN SCC in asynchronous EN-DC

## A.5.5.2.6.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on NR PSCell. The UE is only allowed to cause interruptions immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.5.5.2.6.2-1.

Table A.5.5.2.6.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.5.5.2.6.2-2: Void

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.7E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching

## A.5.5.2.7.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS on a PUSCH-less carrier of SCell, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will verify the interruption requirements on active serving cell in SCG in clause 8.2.1.2.13. Supported test configurations are shown in table A.5.5.2.7.1-1.

In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is E-UTRAN PCell on the primary component carrier. Cell3 is E-UTRAN SCell on the TDD secondary component carrier which operates in downlink without PUCCH/PUSCH. Cell2 is NR FR2 PSCell. The UE is configured with the SRS switching between E-UTRAN PCell and E-UTRAN SCell. The general test parameters and NR cell specific test parameters are given in table A.5.5.2.7.1-2, A.5.5.2.7.1-3. And the E-UTRAN cell specific test parameters (for Cell 1 and Cell 3) can refer to table A.3.7.2.2-1. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 LTE PCell and NR PSCell are continuously scheduled in DL. Immediately at the beginning of T2, the UE is triggered for SRS switching by DCI 2_3 scheduling. After T2, the UE is expected to transmit aperiodic SRS on a special slot in the configured TDD UL/DL configuration, as scheduled by DCI 2_3.

Table A.5.5.2.7.1-1: E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching supported test configurations

Table A.5.5.2.7.1-2: General test parameters for E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching

Table A.5.5.2.7.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching

Table A.5.5.2.7.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.7.1-5: Sounding Reference Symbol Configuration for E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching

## A.5.5.2.7.2Test Requirements

The UE shall be continuously scheduled in NR FR2 PSCell throughout the test. During T2 two interruption time periods are allowed on Cell2 and Cell 1, each interruption due to SRS carrier based switching on Cell2 shall not exceed X defined in table A.5.5.2.7.2-1.

Table A.5.5.2.7.2-1: Interruption length X (slot) E-UTRAN – NR at E-UTRA SRS carrier based switching

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching

## A.5.5.2.8.1 Test Purpose and Environment

The purpose of the test is to verify interruptions at NR SRS carrier based switching requirements defined in TS 38.133 [2] clause 8.2.1.2.12 and TS 36.133 [15] clause 7.32.2.13. The general test parameters are given in table A.5.5.2.8.1-2, and NR cell specific test parameters are given in table A.5.5.2.8.1-3. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.2-1.

In the test there are three cells: Cell 1, Cell2 and Cell3. Cell 1 is LTE PCell, Cell2 is NR FR2 PSCell and Cell3 is NR FR2 SCell. Cell3 is not configured with PUCCH/PUSCH transmission. The test consists of two time periods, with duration of T1 and T2, respectively. During T1 and T2, Cell 1, Cell2 and Cell3 are continuously scheduled in DL. Prior to the start of the time duration T1, Cell 1 shall be configured as LTE PCell, Cell2 shall be configured as NR PSCell and Cell3 shall be configured as NR SCell.

At the beginning of T2, the UE is triggered for SRS switching by DCI 2_3 scheduling. After T2, the UE is expected to transmit aperiodic SRS on a special slot in the configured TDD UL/DL configuration, as scheduled by DCI 2_3. TE shall trigger aperiodic SRS transmission on Cell3.

Table A.5.5.2.8.1-1: Interruption at transitions between active and non-active during DRX supported test configurations

Table A.5.5.2.8.1-2: General test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.8.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.5.5.2.8.1-3A: OTA related test parameters

Table A.5.5.2.8.1-4: Void

## A.5.5.2.8.3Test Requirements

In T2 UE shall transmit SRS on Cell3 as requested. During T2 interruption on Cell2 due to SRS carrier based switching from Cell2 to Cell3 shall not exceed the requirements defined in TS 38.133 [2] clause 8.2.1.2.12.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.2.9E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell

## A.5.5.2.9.1Test Purpose and Environment

The purpose of this test is to verify that for E-UTRAN PCell interruptions during the measurement on the deactivated NR PSCell, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for LTE PCell in EN-DC specified in TS 36.133 [15] clause 7.32.2.20. Supported test configurations are shown in table A.5.5.2.9.1-1.

The general test parameters are given in table A.5.5.2.9.1-2, and NR cell specific test parameters are given in table A.5.5.2.9.1-3 and A.5.5.2.9.1-4 below. The E-UTRAN cell specific test parameters can be found in table A.3.7.2.1-2. In the test there are two cells: Cell 1 and Cell2. Cell 1 is LTE PCell, Cell2 is NR FR2 deactivated PSCell, respectively. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell2. The point in time at which the RRC message including measCyclePSCell for the deactivated NR PSCell and NR PSCell deactivation command is received by the UE, defines the start of time period T1. During T1, LTE PCell is continuously scheduled in DL. UE is configured with RRM and bfd-and-RLM measurements on the deactivated Cell2.

Table A.5.5.2.9.1-1: Interruption during measurements on deactivated NR PSCell supported test configurations

Table A.5.5.2.9.1-2: General test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell

Table A.5.5.2.9.1-3: NR cell specific test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell

Table A.5.5.2.9.1-4: NR cell specific OTA related test parameters for E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell

## A.5.5.2.9.2Test Requirements

The UE shall be continuously scheduled in Cell 1 during the entire length of T1 and the UE is configured with RRM and RLM/BFD measurements on the deactivated Cell2. During the time duration T1 the UE shall transmit at least 99 % of ACK/NACK on E-UTRAN PCell. The UE is only allowed to cause interruptions immediately before and immediately after an SMTC. Each interruption shall not exceed 1 subframe for synchronous inter-band EN-DC.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.3SCell Activation and Deactivation Delay

## A.5.5.3.1SCell Activation and deactivation of SCell in FR2 intra-band

## A.5.5.3.1.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.4.5.3.1.1 except the SCell is in FR2 intra-band.

The supported test configurations are shown in table A.5.5.3.1.1-1 below. The general and cell specific test parameters are the same except those described in the following clause. The listed parameter values in tables A.5.5.3.1.1-2 and A.5.5.3.1.1-3 will replace the values of corresponding parameters in tables A.4.5.3.1.1-2 and A.4.5.3.1.1-3. In this case, OTA related test parameters are shown in table A.5.5.3.1.1-4 below.

In this test it is assumed that the UE is receiving RRC messages pertaining to the SCell in SCG via signaling on SRB3.

Table A.5.5.3.1.1-1: Supported test configurations for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.1.1-2: General test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.1.1-3: Cell specific test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.1.1-4: OTA related test parameters for FR2 SCell activation case with FR2 PSCell

## A.5.5.3.1.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case, with the following exceptions:

-Placement of interruptions is only verified in NR PSCell.

## A.5.5.3.2SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle

## A.5.5.3.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.4.5.3.1.1, except PSCell is in FR2.

The supported test configurations are shown in table A.5.5.3.2.1-1 below. The general test parameters are the same in tables A.4.5.3.1.1-2. The cell specific test parameters are given in tables A.5.5.3.2.1-2. In this case, OTA related test parameters are the same as in table A.5.5.3.2.1-3.

Table A.5.5.3.2.1-1: Supported test configurations for FR1 SCell activation case with PSCell is FR2

Table A.5.5.3.2.1-2: Cell specific test parameters for FR1 SCell activation case with FR2 PSCell

Table A.5.5.3.2.1-3: OTA related test parameters for FR1 SCell activation case with FR2 PSCell

## A.5.5.3.2.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case.

## A.5.5.3.3Void

## A.5.5.3.4Void

## A.5.5.3.5SCell Activation and deactivation of SCell in FR2

## A.5.5.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell is in FR2.

The supported test configurations are shown in table A.5.5.3.5.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The listed parameter values in tables A.5.5.3.5.1-2 will replace the values of corresponding parameters in tables A.4.5.3.3.1-2. The listed parameter values in tables A.5.5.3.5.1-3 will replace the values of corresponding parameters in tables A.4.5.3.3.1-3. In this case, OTA related test parameters are shown in table A.5.5.3.5.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell (Cell 1), NR has two cells, PSCell (Cell 2) in FR1 and SCell (Cell 3) in FR2. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.5.5.3.5.1-1: FR2 SCell activation in non-DRX test configurations with FR1 PSCell

Table A.5.5.3.5.1-2: General test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.5.1-3: Cell specific test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.5.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PSCell

## A.5.5.3.5.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PSCell in the slot.

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

## 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP 1000 ms.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

- THARQ is defined in table A.5.5.3.1.1-2

- Tactivation_time = 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1030 ms

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot   to , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3, where TX =20 ms, and  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot lengthm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot lengthm1m2

During T3 the starting point of interruption of PSCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3 and the starting point of interruption of E-UTRA PCell during SCell deactivation shall not happen outside the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe lengthn1n2

The interruption of PSCell due to activation of SCell 1 and SCell2 shall not be more than the values specified for EN-DC in clause 8.2.1.2.10.

The interruption of PCell due to activation of SCell 1 and SCell2 shall not be more than the values specified for EN-DC in clause 7.32.2.5 of TS 36.133 [15].

## A.5.5.3.6Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR2

## A.5.5.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the multiple SCell activation and deactivation delay and interruption are within the requirements stated in clause 8.3, when the two SCells to be activated are in FR2 and one SCell is known and the other SCell is unknown by the UE at the time of activation.

The supported test configurations are shown in table A.5.5.3.6.1-1 below. The general test parameters are given in table A.5.5.3.6.1-2 and cell-specific test parameters in table A.5.5.3.6.1-3 below. OTA related test parameters are shown in table A.5.5.3.6.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are four carriers, one E-UTRA cell, and three NR cells. Before the test starts the UE is connected to Cell 1 (PCell) on the E-UTRA carrier and Cell 2 (PSCell) on the NR carrier in FR1, but is not aware of Cell 3 (SCell 1) or Cell 4 (SCell2) on the NR carriers both in FR2. Cell 1, Cell 2 and Cell 3 have constant signal levels throughout the test. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the Cell 3 (SCell 1) and Cell 4 (SCell2) are configured on NR. The test equipment sends a single MAC message for activation of both SCells within 3 s for UE power class 2/3/4 or 4 s for UE power class 1 after RRM reports is sent for SCell 1.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. In the same MAC PDU, the test equipment activates the TCI state of RMC CORESET. In slot #m, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell 1 and SCell2.

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.5.5.3.6.1-1: Supported test configurations

Table A.5.5.3.6.1-2: General test parameters

Table A. 5.5.3.6.1-3: Cell specific test parameters

Table A.5.5.3.6.1-4: OTA related test parameters

## A.5.5.3.6.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PSCell in the slot.

During T2 the UE shall start sending CSI reports for SCell 1 and SCell2 with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

- THARQ is defined in table A.5.5.3.Y.1-2

- Tactivation_time = 5 ms + TFineTiming = 25 ms,

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.5.5.3.7Direct SCell activation at SCell addition of known SCell in FR2

## A.5.5.3.7.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.4.5.3.5 except the SCell is in FR2 intra-band.

The supported test configurations are shown in table A.5.5.3.7.1-1 below. The general and cell specific test parameters are the same except those described in the following clause. The listed parameter values in tables A.5.5.3.7.1-2 and A.5.5.3.7.1-3 will replace the values of corresponding parameters in tables A.4.5.3.5.1-2 and A.4.5.3.5.1-3. In this case, OTA related test parameters are shown in table A.5.5.3.7.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, each with one cell. Cell 1 operates in either FDD or TDD duplex mode according to test configuration. Cell 2 and Cell 3 operate in TDD duplex mode. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and Cell 2 (PSCell) on radio channel 2 (PSCC), but is not aware of Cell 3 (SCell 1) on radio channel 3 (SCC). The UE is only monitoring the PCC/PSCC. The UE shall be continuously scheduled in the PCell/PSCell throughout the whole test.

At the beginning of T1, the UE is configured to measure radio channel 3 and starts detecting the Cell 3 (SCell) on radio channel 3 (SCC). During T1 Cell 3 is detected and measured and measurement report is sent by the UE to the test equipment.

Time period T2 starts when test equipment sends the RRCConnectionReconfiguration message for the activation of the SCell within time period specified in clause 8.3.2 for known cell definition to ensure the configured SCell is known.The NR shall be use an RRCConnectionReconfigurationComplete message with parameter sCellState set to activatedfor the SCell (Cell 3), which causes the SCell to become configured and activated on radio channel 3 (SCC). The message is sent from the test equipment to the UE and is received in a subframe # denoted m at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (m+ Ndirect).

Time period T3 starts at (m+ Ndirect), at which point UE shall be reporting a valid CQI for PCell/PSCell and SCell.

During T3, the UE shall be continuously scheduled in the SCell.

The test equipment verifies the activation time by counting the subframes from the time when the direct SCell activation is sent and until a CSI report with other than CQI index 0 is received.

The test equipment verifies the CSI report from the direct activated SCell after the activation procedure is completed contains CQI index other than 0.

Table A.5.5.3.7.1-1: Supported test configurations for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.7.1-2: General test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.7.1-3: Cell specific test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.7.1-4: OTA related test parameters for FR2 SCell activation case with FR2 PSCell

## A.5.5.3.7.2Test Requirements

The UE shall accomplish the activation of the SCell no later than subframe m+Ndirect as defined in clause 8.3.4.

Time period T3 starts at (m+ Ndirect), at which point UE shall be reporting a valid CQI for both PSCell and SCell.

During T3 the UE shall send CSI reports for SCell with non-zero CQI index and continue to send CSI reports for SCell 1 with non-zero CQI index until the end of T3. All of the above test requirements shall be fulfilled in order for the observed SCell 1 direct activation delay to be counted as correct. The rate of correct observed SCell 1 direct activation delay during repeated tests shall be at least 90 %.

## A.5.5.3.8Fast SCell Activation of SCell in FR2 intra-band

## A.5.5.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the fast SCell activation and deactivation times are within the requirements stated in clause 8.3.16, when the SCell in FR2 is known by the UE at the time of activation.

The supported test configurations are shown in table A.5.5.3.8-1 below. The test parameters are given in tables A.5.5.3.8-2 and cell-specific parameters in A.5.5.3.8-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test. In this case, OTA related test parameters are shown in table A.5.5.3.8.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. The UE now starts monitoring the SCell. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m (where m mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3.16. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.5.5.3.8.1-1: Supported test configurations for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.8.1-2: General test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.8.1-3: Cell specific test parameters for FR2 SCell activation case with FR2 PSCell

Table A.5.5.3.8.1-4: OTA related test parameters for FR2 SCell activation case with FR2 PSCell

## A.5.5.3.8.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PCell in slot (m+k).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstATRS+ 5 ms, as defined in clause 8.3.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot  to  .m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.4.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.5.5.3.9PUCCH SCell Activation and deactivation of known SCell in FR2

## A.5.5.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3, when the PUCCH SCell is in FR2.

The supported test configurations are shown in table A.5.5.3.9.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The listed parameter values in tables A.5.5.3.9.1-2 will replace the values of corresponding parameters in tables A.4.5.3.3.1-2. The listed parameter values in tables A.5.5.3.9.1-3 will replace the values of corresponding parameters in tables A.4.5.3.3.1-3. In this case, OTA related test parameters are shown in table A.5.5.3.9.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell (Cell 1), and NR has two cells, PSCell (Cell 2) in FR1 and PUCCH SCell (Cell 3) in FR2. Cell 1 and Cell 2 have constant signal levels throughout the test. Cell 1, Cell2 and Cell 3 are in primary Timing Advance Group (pTAG). UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment for sTAG.

Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (PUCCH SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 3) becomes configured on NR. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector provided that the HARQ ACK of the MAC message is received by TE, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI on for the activated PUCCH SCell on PUCCH SCell at latest in slot, as defined in clause 8.3. n+THARQ+Tactivation_time+ X + TCSI_ReportingNR slot length

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UEin a slot # denoted m, is received at the UE antenna connector provided that the HARQ ACK of the MAC message is received by TE. The UE shall carry out deactivation of the PUCCH SCell in a slot , as defined in clause 8.3.m+THARQ+3msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the PUCCH SCell deactivation command is sent until CSI reporting for PUCCH SCell is discontinued.

Table A.5.5.3.9.1-1: FR2 SCell activation in non-DRX test configurations with FR1 PSCell

Table A.5.5.3.9.1-2: General test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.9.1-3: Cell specific test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.9.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PSCell

## A.5.5.3.9.2Test Requirements

During T2 the UE shall start sending CSI reports for PUCCH SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstSSB+ 5 ms, as defined in clause 8.3. n+THARQ+Tactivation_time+ X + TCSI_ReportingNR slot length

During T3 the UE shall stop sending CSI reports for PUCCH SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

All of the above test requirements shall be fulfilled in order for the observed PUCCH SCell activation delay and PUCCH SCell deactivation delay to be counted as correct. The rate of correct observed PUCCH SCell activation delay and PUCCH SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in slot  then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.n+THARQ+Tactivation_time+ X + TCSI_ReportingNR slot length

## A.5.5.3.10PUCCH SCell Activation and deactivation of unknown SCell in FR2

## A.5.5.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3, when the PUCCH SCell is in FR2.

The supported test configurations are shown in table A.5.5.3.10.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The listed parameter values in tables A.5.5.3.10.1-2 will replace the values of corresponding parameters in tables A.4.5.3.3.1-2. The listed parameter values in tables A.5.5.3.10.1-3 will replace the values of corresponding parameters in tables A.4.5.3.3.1-3. In this case, OTA related test parameters are shown in table A.5.5.3.10.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell (Cell 1), and NR has two cells, PSCell (Cell 2) in FR1 and PUCCH SCell (Cell 3) in FR2. Cell 1 and Cell 2 have constant signal levels throughout the test.

Cell 1, Cell2 are in primary Timing Advance Group (pTAG), and Cell3 is in secondary Timing Advance Group (sTAG). The TimeAlignmentTimer of sTAG expires before receiving the activation command.

Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (PUCCH SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 3) becomes configured on NR.

The point in time at which the MAC message is received at the UE antenna connector provided that the HARQ ACK of the MAC message is received by TE, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI on for the activated PUCCH SCell on PUCCH SCell at latest in slot, as defined in clause 8.3. n+THARQ+Tdelay_PUCCH_SCellNR slot length

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UEin a slot # denoted m, is received at the UE antenna connector provided that the HARQ ACK of the MAC message is received by TE. The UE shall carry out deactivation of the PUCCH SCell in a slot , as defined in clause 8.3.m+THARQ+3msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the PUCCH SCell deactivation command is sent until CSI reporting for PUCCH SCell is discontinued.

Table A.5.5.3.10.1-1: FR2 SCell activation in non-DRX test configurations with FR1 PSCell

Table A.5.5.3.10.1-2: General test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.10.1-3: Cell specific test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.10.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PSCell

## A.5.5.3.10.2Test Requirements

During T2 the UE shall start sending CSI reports for PUCCH SCell with non-zero CQI index at latest in a slot , as defined in clause 8.3. n+THARQ+Tdelay_PUCCH_SCellNR slot length

During T3 the UE shall stop sending CSI reports for PUCCH SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

All of the above test requirements shall be fulfilled in order for the observed PUCCH SCell activation delay and PUCCH SCell deactivation delay to be counted as correct. The rate of correct observed PUCCH SCell activation delay and PUCCH SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in slot  then the UE shall use the next available uplink resource for reporting the corresponding valid CSI. n+THARQ+Tdelay_PUCCH_SCellNR slot length

## A.5.5.3.11Multiple SCell activation and deactivation of one known PUCCH SCell and one unknown SCell in FR2

## A.5.5.3.11.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell with multiple SCell activation and deactivation delay requirement defined in clause 8.3, and interruption requirement defined in clause 8.2, when one known PUCCH SCell and one unknown SCell to be activated are in FR2.

The supported test configurations are shown in table A.5.5.3.11.1-1 below. The general test parameters are given in table A.5.5.3.11.1-2 and cell-specific test parameters in table A.5.5.3.11.1-3 below. OTA related test parameters are shown in table A.5.5.3.11.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are four carriers, one E-UTRA cell, and three NR cells. Before the test starts the UE is connected to Cell 1 (PCell) on the E-UTRA carrier and Cell 2 (PSCell) on the NR carrier in FR2, but is not aware of Cell 3 (PUCCH SCell) or Cell 4 (SCell) on the NR carriers both in FR2. Cell 2 and Cell 4 are in the primary PUCCH group, and Cell 3 is in the secondary PUCCH group. In addition, Cell 2 and Cell 4 are in primary Timing Advance Group (pTAG), and Cell 3 is in the secondary Timing Advance Group (sTAG). Cell 1, Cell 2 and Cell 3 have constant signal levels throughout the test. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

There are two sub tests in this section.

-For Test 1 (valid TA case), UE is provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment for sTAG.

-For Test 2 (invalid TA case), TimeAlignmentTimer of sTAG expires before UE receives the activation command

At the beginning of T1 the UE receives an RRC message by which the Cell 3 (PUCCH SCell) and Cell 4 (SCell) are configured on NR. The test equipment sends a single MAC message for activation of both Cell 3 and Cell 4 within 3 s for UE power class 2/3/4 or 4 s for UE power class 1 after RRM reports is sent for Cell 3.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. In the same MAC PDU, the test equipment activates the TCI state of RMC CORESET. In slot #m, the test equipment also sends an RRC message to configure the CSI-RS resources for both Cell 3 and Cell 4.

During T2, the UE shall be able to report valid CSI on PUCCH SCell for the activated PUCCH SCell at latest in

-slot m+ Tactivate_total_PUCCH_SCell as defined in clause 8.3.13.

During T2, the UE shall be able to report valid CSI on PCell for the activated SCell at latest in

-slot m+ Tactivate_total_other_SCell. as defined in clause 8.3.13.

Any PCell and PSCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.m+1+THARQNR slot lengthm+1+Tactivate_total_PUCCH_SCell+NinterruptionNinterruption

Any PCell and PSCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.m+1+THARQNR slot lengthm+1+Tactivate_total_other_SCell+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of both Cell 3 and Cell 4, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the PUCCH SCell in a slot , as defined in clause 8.3, and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.5.5.3.11.1-1: Supported test configurations

Table A.5.5.3.11.1-2: General test parameters

Table A.5.5.3.11.1-3: Cell specific test parameters

Table A.5.5.3.11.1-4: OTA related test parameters

## A.5.5.3.11.2Test Requirements

During T2 the UE shall start sending CSI reports for Cell 3 with non-zero CQI index in the configured slots for CSI reporting no later than slot m+ Tactivate_total_PUCCH_SCell , as defined in clause 8.3.

During T2 the UE shall start sending CSI reports for Cell 4 with non-zero CQI index in the configured slots for CSI reporting no later than slot m+ Tactivate_total_other_SCell , as defined in clause 8.3.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell and PSCell during PUCCH SCell activation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+Tactivate_total_PUCCH_SCell+Ninterruption

During T2 interruption of PCell and PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+Tactivate_total_other_SCell+Ninterruption

During T3 the starting point of interruption of PCell and PSCell during the deactivation of PUCCH SCell and SCell shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the summation of interruption length due to PUCCH SCell activation/ deactivation and interruption length due to SCell activation/ deactivation, the values of interruption length are specified for EN-DC in clause 8.2.

All of the above test requirements shall be fulfilled in order for the observed SCells activation delay to be counted as correct. The rate of correct observed SCells activation delay and SCells deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI for PUCCH SCell in a slot m+ Tactivate_total_PUCCH_SCell as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI for SCell in a slot m+ Tactivate_total_other_SCell as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

## A.5.5.3.12SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in non-DRX

## A.5.5.3.12.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell and DL SCell activation and deactivation times are within the requirements stated in clause 8.3.13, when the PUCCH SCell in FR2 and DL SCell in FR2 is unknown to the UE at the time of activation.

The supported test configurations are shown in table A.5.5.3.12.1-1 below. The test parameters are given in tables A.5.5.3.12.1-2 and cell-specific parameters in A.5.5.3.12.1-3 below. OTA related test parameters are shown in table A.5.5.3.12.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are four carriers, each with one cell. Before the test starts the UE is connected to Cell 1(PCell) on the E-UTRA carrier and Cell 2 (PSCell) on the NR carrier in FR2, but is not aware of Cell3 (PUCCH SCell) and Cell4(DL SCell2) on the NR carriers both in FR2. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test. SCC of Cell 3 and SCC of Cell 4 are on a same band.

At the beginning of T1 the UE receives an RRC message by which the Cell 3 and Cell 4 becomes configured on NR. The test equipment sends a single MAC message for activation of both SCells.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. In the same MAC PDU, the test equipment activates the TCI state of RMC CORESET. In slot #m, the test equipment also sends an RRC message to configure the CSI-RS resources for Cell 3 and Cell 4.

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.5.5.3.12.1-1: Supported test configurations

Table A.5.5.3.12.1-2: General test parameters

Table A.5.5.3.12.1-3: Cell specific test parameters

Table A.5.5.3.12.1-4: OTA related test parameters

## A.5.5.3.12.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PSCell in the slot.

During T2 the UE shall start sending CSI reports for SCell 1 with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length

THARQ is defined in table A.5.5.3.12.1-2

Tdelay_multiple_SCells_PUCCH_SCell  is defined in section 8.13.13.1. In this test case, both valid TA and invalid TA cases shall be tested.

Test for case when UE has valid TA: the TimeAlignmentTimer [2] associated with the TAG containing the PUCCH SCell is running, and Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), 3*Ttarget_PL-RS) + TCSI_reporting_after.

Test for case when UE do not have valid TA: Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3), 3*Ttarget_PL-RS) + TCSI_reporting_after

Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in section 8.3.7

TCSI_Reporting = 10 ms

NR slot length is 0.125 ms.

During T2 the UE shall start sending CSI reports for SCell2 with non-zero CQI index in the configured slots for CSI reporting no later than slot where m+THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

THARQ is defined in table A.5.5.3.12.1-2

Tdelay_multiple_SCells_other_SCell   = Tactivation_time_multiple_scells +TCSI_Reporting.

- Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in section 8.3.7

TCSI_Reporting = 10 ms

NR slot length is 0.125 ms.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.14.n+THARQ+3 msNR slot length

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot ,  as defined in clause 8.3.13 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length

## A.5.5.3.13SCell Activation and deactivation of unknown SCell in FR2 for UE in DRX, capable of small beam sweeping factors and/or short measurement interval

## A.5.5.3.13.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell is unknown in FR2 by the UE at the time of activation. The test will also verify that the SSB-based L1-RSRP measurement accuracy is within the specified limits as stated in clause 10.1.20.1.

The supported test configurations are shown in table A.5.5.3.13.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The general test parameters are given in table A.5.5.3.13.1-2 and cell-specific test parameters in table A.5.5.3.13.1-3 below. In this case, OTA related test parameters are shown in table A.5.5.3.13.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell (Cell 1), NR has two cells, PSCell (Cell 2) in FR1 and SCell (Cell 3) in FR2. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled within on-duration based on DRX configuration in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received. In this test the allowed time for SCell activation depends on the UE reported capabilities regarding small beam sweeping factors (i.e. X1/X2 as indicated in beamSweepingFactorReduction-r18) and short measurement intervals (shortMeasInterval-r18).

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

The test equipment verifies the absolute accuracy of SSB-based L1-RSRP measurements during T2 by using the parameters in table A.5.5.3.13.1-3 and table A.5.5.3.13.1-4.

Table A.5.5.3.13.1-1: Supported test configurations for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.13.1-2: General test parameters for FR2 SCell activation case with FR1 PSCell

Table A.5.5.3.13.1-3: Cell specific test parameters for FR2 SCell activation case with FR1 active PSCell

Table A.5.5.3.13.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PSCell

## A.5.5.3.13.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PSCell in the slot.

For UE capable of beamSweepingFactorReduction-r18 and shortMeasInterval-r18 capabilities:

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

-3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report as defined in clause 8.3.2.

-For this test case, TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced = TSSB=20 ms; TL1-RSRP, enhanced_measure= (X2/8)*480 ms and TL1-RSRP,reprt=5 ms, which allows TL1-RSRP = 968 ms if X1 and X2 use the default value. Value of TL1-RSRP for various X1/X2 capabilities is obtained from table A.5.5.3.13.1-5.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivation_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.4.5.3.1.1-2

-Tactivation_time = 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max{(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)} which allows 1000 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted from table A.5.5.3.13.1-5).

TL1-RSRP, enhanced_measure is

-SSB based L1-RSRP measurement delay TL1-RSRP_Measurement_Period_SSB ms based on applicability as defined in clause 9.5 assuming M=1 and TReport=0; N is equal to the value reported by the UE in reduceForSSB-L1-RSRP-Meas i.e. X2. Otherwise, if reduceForSSB-L1-RSRP-Meas is absent, N= 8.

-CSI-RS based L1-RSRP measurement delay TL1-RSRP_Measurement_Period_CSI-RS ms based on applicability as defined in clause 9.5 assuming M=1 and TReport=0.

In case UE has signalled X1/X2 to be lower than 8 the following values are allowed for TL1-RSRP:

Table A.5.5.3.13.2-1: TL1-RSRP for different X1/X2 capabilities (ms)

For UE capable of beamSweepingFactorReduction-r18 but not shortMeasInterval-r18 capabilities, and the cell specific test parameters are described in table A.5.5.3.13.1-3 except that SMTC value is SMTC.1:

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

-3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report as defined in clause 8.3.2.

-For this test case, considering DRX,  TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced =20 ms; from table 9.5.4.1-2 TL1-RSRP, enhanced_measure= (X2/8)*11520 ms and TL1-RSRP,report=5 ms, which allows TL1-RSRP = 12008 ms if X1 and X2 are absent. Value of TL1-RSRP for various X1/X2 capabilities is obtained from table A.5.5.3.13.1-6 assuming DRX cycle = 320 ms.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivation_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.4.5.3.1.1-2

-Tactivation_time = 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max{(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)} which allows 12040 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted from table A.5.5.3.13.1-6).

Table A.5.5.3.13.1-6: TL1-RSRP for different X1/X2 capabilities with 320 ms DRX cycle (ms)

For UE capable of shortMeasInterval-r18 but not beamSweepingFactorReduction-r18 capabilities, the general test parameters are described in table A.5.5.3.13.1-2 except that the default value for X1=X2=8 is chosen.

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

-3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report as defined in clause 8.3.2.

-For this test case, even with DRX, the UE treats the case as non-DRX, thus TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced = TSSB=20 ms; TL1-RSRP, measure= 480 ms and TL1-RSRP,report=5 ms, which allows TL1-RSRP = 968 ms.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivation_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.4.5.3.1.1-2

-Tactivation_time = 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, measure + TL1-RSRP, report + max{(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)} which allows 1000 ms.

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 3 shall fulfil the accuracy requirements in clauses 10.1.20.1 provided the side condition is -2 dB as defined in clause 8.3.2.

During T3 the UE shall stop sending CSI reports for the SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

## A.5.5.3.14PUCCH SCell activation and deactivation with FR1 PSCell based on L3 reporting after SCell activation command

## A.5.5.3.14.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3.12 for UE capable of l3-MeasUnknownSCellActivation-r18.

The supported test configurations are shown in table A.5.5.3.14.1-1 below. The test parameters are given in tables A.5.5.3.14.1-2 and cell-specific parameters in A.5.5.3.14.1-3 and A.5.5.3.14.1-4 below. The test consists of Three successive time periods, with duration of T1, T2 and T3 respectively. There are two NR carriers and one E-UTRA carrier, each with one cell. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. Before the test starts the UE is connected to Cell 1 and Cell 2 but is not aware of Cell3, and UE is configured with MeasObjectNR on carriers of Cell2 and Cell3. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 3) becomes configured on radio channel 3, and one measID is associated with reportOnActivation. The UE now starts monitoring the Cell3. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI for the activated PUCCH SCell at latest in slotn+ , as defined in clause 8.3.12.  THARQ+Tdelay_PUCCH_SCellNR slot length

There are two sub-tests in the test. In sub-test 1, TE shall transmit DCI 0-1 to PSCell at slot , and the UE shall be able to send L3 measurements report of the SCell at slot , where k2 =1. In sub-test 2, TE shall transmit DCI 0-1 to PSCell at slot , where k2=1 and M is defined in 8.3.12. The UE shall be able to send L3 measurements report of the SCell at.n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+k2 NR slot lengthn+THARQ+7 ms+M-k2 NR slot length+THARQ+7 ms+M NR slot length

Any PSCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.14and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.14.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.5.5.3.14.1-1: Supported test configurations for FR2 SCell activation case

Table A. A.5.5.3.14.1-2: General test parameters for FR2 SCell activation case

Table A.5.5.3.14.1-3: Cell specific test parameters for FR2 SCell activation case: Cell2

Table A.5.5.3.14.1-4: Cell specific test parameters for FR2 SCell activation case: Cell3

Table A.5.5.3.14.1-4: OTA related test parameters for FR2 SCell with FR1 PCell

## A.5.5.3.14.2Test Requirements

By end of T2 the UE shall finish the DL activation for the PUCCH SCell. Assuming the periodic CSI reporting is used and assuming periodic CSI activation and TCI state is sent along with SCell activation MAC CE, UE shall finish the DL activation by slot n+  as defined in clause 8.3.12.THARQ+Tactivation_timeNR slot length

During T2 the UE shall start sending PRACH preamble to TE and shall obtain the TA command from TE and shall be ready to send valid CSI report to the TE. CSI report shall be transmitted within  Tactivation_time + Max((TFirst_available_CSI + TCSI_processing), (T1+T2+T3)) + TCSI_reporting_after from the transmission of HARQ feedback of SCell activation command as specified in the 8.3.12.

In sub-test 1, Tactivation_time = 7 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

In sub-test 2, Tactivation_time = 7 ms + M+ max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PSCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption of PSCell due to activation of SCell shall not be more than the values specified for SA in clause 8.2.2.2.7.

## A.5.5.3.15SCell Activation of unknown SCell in FR2 in non-DRX for 160 ms SCell measurement cycle with the L3 reporting during activation

## A.5.5.3.15.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3.17, when the SCell in FR2 is unknown by the UE at the time of activation. In this test, UE shall perform two sub-tests where two different UL resource locations are configured.

The supported test configurations are shown in table A.5.5.3.15.1-1 below. The test parameters are given in tables A.5.5.3.15.1-2 and cell-specific parameters in A.5.5.3.15.1-3 and A.5.5.3.15.1-5 below. OTA related test parameters are shown in table A.5.5.3.15.1-4. The test consists of three successive time periods, with duration of T1, T2, and T3, respectively. There are three carriers and each with one cell. E-UTRA has one cell (Cell 1), NR has two cells, PSCell (Cell 2) in FR1 and SCell (Cell 3) in FR2. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR but is not aware of Cell 3 (SCell) on NR. The UE is only monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on radio channel 3. In the measurement control information for Cell 3, it is indicated to the UE that event-triggered reporting with Event A2 and reportOnActivation is used. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3. n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

In sub-test1, TE shall transmit DCI 0-1 to PSCell at slot .  The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 1.In sub-test2, TE shall transmit DCI 0-1 to PSCell at slot , The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 2. TE will send TCI activation command after receiving L3 measurement report of the SCell. n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+0.125 ms NR slot lengthn+THARQ+3 ms+M-0.125 ms NR slot lengthn+THARQ+7 ms+ M NR slot length

The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.5.5.3.15.1-1: Supported test configurations for FR2 SCell activation case

Table A.5.5.3.15.1-2: General test parameters for FR2 SCell activation case

Table A.5.5.3.15.1-3: Cell specific test parameters for FR2 SCell activation case: Cell 3

Table A.5.5.3.15.1-4: OTA related test parameters for FR2 SCell activation case

Table A.5.5.3.15.1-5: Cell specific test parameters for FR2 SCell activation case: Cell 2

## A.5.5.3.15.2Test Requirements

During T2, the UE shall be able to send a valid L3-RSRP report for the SCell in the configured slots for CSI reporting at slot  for sub-test 1. For sub-test2, the UE shall be able to send a valid L3-RSRP for the SCell at slot  . The UE is not required to send L3-RSRP report after slot , where M is defined in 8.3.17.n+THARQ+7ms+0.125msNR slot lengthn+THARQ+7ms+MNR slot lengthn+THARQ+3ms+MNR slot length

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ and TCSI_Reporting are defined in table A.7.5.3.16.1-2.

-In this case, TSSB=TSMTC = 20 ms and TL1-RSRP,report = 5 ms.

-For sub-test1, Tactivation_time = 7 ms + 0.125 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay).

- For sub-test2, Tactivation_time = 3 ms + M  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay)

-NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.5.5.4Void

## A.5.5.5Beam Failure Detection and Link recovery procedures

## A.5.5.5.1EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode

## A.5.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.1.1-1, A.5.5.5.1.1-2, A.5.5.5.1.1-3 and A.5.5.5.1.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.1.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.5.5.5.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.5.5.5.1.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.1.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.1.1-3: Cell specific test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.1.1-4: Void

Figure A.5.5.5.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.5.5.5.1.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.5.5.5.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 960+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.2EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode

## A.5.5.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.2.1-1, A.5.5.5.2.1-2, A.5.5.5.2.1-3, A.5.5.5.2.1-4 and A.5.5.5.2.1-5 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.2.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.5.5.5.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCSell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.5.2.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.2.1-2: General test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.2.1-3: Cell specific test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.2.1-4: Void

Table A.5.5.5.2.1-5: Void

Figure A.5.5.5.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.5.5.5.2.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.5.5.5.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 560+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.3EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.5.5.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.3.1-1, A.5.5.5.3.1-2, and A.5.5.5.3.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.3.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the CSI-RS in set q0 in the active PSCell to emulate CSI-RS based beam failure. Figure A.5.5.5.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled.

Table A.5.5.5.3.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.3.1-2: General test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.3.1-3: Cell specific test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.3.1-4: Void

Table A.5.5.5.3.1-5: Void

Figure A.5.5.5.3.1-1: SNR variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

Figure A.5.5.5.3.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.5.5.5.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.4EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode

## A.5.5.5.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.4.1-1, A.5.5.5.4.1-2, A.5.5.5.4.1-3, and A.5.5.5.4.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.4.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the CSI-RS in set q0 in the active PSCell to emulate CSI-RS based beam failure. Figure A.5.5.5.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.5.4.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.4.1-2: General test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.4.1-3: Cell specific test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.4.1-4: Void

Table A.5.5.5.4.1-5: Void

Table A.5.5.5.4.1-6: Void

Figure A.5.5.5.4.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.5.5.5.4.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

## A.5.5.5.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.5EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode

## A.5.5.5.5.1Test Purpose and Environment

The purpose is to test scheduling availability restrictions when the UE is performing beam failure detection or when the UE is performing L1-RSRP measurement for candidate beam detection, when no DRX is used. This test will verify the scheduling availability restriction requirements for SSB based beam failure detection and link recovery for an FR2 serving cell in clause 8.5.7 and 8.5.8.

The test parameters are given in tables A.5.5.5.5.1-1, A.5.5.5.5.1-2 and A.5.5.5.5.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.5.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB index 0 in the active PSCell to emulate SSB based beam failure. Figure A.5.5.5.5.1-2 shows the variation of the downlink L1-RSRP of the SSB index 1 used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. This test will focus on the scheduling availability during beam failure detection and candidate beam detection. In the test, DRX configuration is not enabled. Test is to test the scheduling availability restriction of UE performing beam failure detection and candidate beam detection when SSB RS configured for Beam failure detection and candidate beam detection. During the test the UE is scheduled to transmit continuously in UL.

Table A.5.5.5.5.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.5.1-2: General test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.5.1-3: Cell specific test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.5.5.5.5.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.5.5.5.5.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.5.5.5.5.2Test Requirements

The UE behaviour during time duration T3 follows the requirements defined in clause 8.5.7.3:

-The UE is not expected to transmit PUCCH/PUSCH/SRS or receive PDCCH/PDSCH/CSI-RS for tracking/CSI-RS for CQI on BFD-RS symbols to be measured for beam failure detection.

The UE behaviour during time durations T4 and T5 follows the requirements defined in clause 8.5.8.3:

-The UE is not expected to transmit PUCCH/PUSCH or receive PDCCH/PDSCH on reference symbols to be measured for candidate beam detection.

## A.5.5.5.6EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.5.5.5.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for an active SCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell with schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 SCell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.6.1-1, A.5.5.5.6.1-2 and A.5.5.5.6.1-3. There are three cells, Cell 1 is the E-UTRAN PCell, Cell 2 is the PSCell, and Cell 3 is the SCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.6.1-1 shows the variation of the downlink SNR of the active SCell and the SNR of the CSI-RS in set q0 in the active SCell to emulate CSI-RS based beam failure. Figure A.5.5.5.6.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1, Cell 2, and Cell 3. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.5.5.5.6.1-1: Supported test configurations for FR2 PSCell and SCell

Table A.5.5.5.6.1-2: General test parameters for FR2 SCell for beam failure detection and link recovery testing in non-DRX mode

Table A.5.5.5.6.1-3: Cell specific test parameters for FR2 SCell for beam failure detection and link recovery testing in non-DRX mode

Figure A.5.5.5.6.1-1: SNR variation for CSI-RS based beam failure detection and link recovery testing for SCell in non-DRX mode

Figure A.5.5.5.6.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing for SCell in non-DRX mode

## A.5.5.5.6.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 in A.5.5.5.6.1 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initial link recovery. During T4 and T5 the UE measures and evaluates beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.7EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode

## A.5.5.5.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for an active SCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell with schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 SCell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.7.1-1, A.5.5.5.7.1-2 and A.5.5.5.7.1-3. There are three cells, Cell 1 is the E-UTRAN PCell, Cell 2 is the PSCell, and Cell 3 is the SCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.7.1-1 shows the variation of the downlink SNR of the active SCell and the SNR of the CSI-RS in set q0 in the active SCell to emulate CSI-RS based beam failure. Figure A.5.5.5.7.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1, Cell 2, and Cell 3. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.5.7.1-1: Supported test configurations for FR2 PSCell and SCell

Table A.5.5.5.7.1-2: General test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.7.1-3: Cell specific test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Figure A.5.5.5.7.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing for SCell in DRX mode

Figure A.5.5.5.7.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing for SCell in DRX mode

## A.5.5.5.7.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 in A.5.5.5.7.1 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initial link recovery. During T4 and T5 the UE measures and evaluates beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.8EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode

## A.5.5.5.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the TRP specific CSI-RS-based beam failure in the set (q0,0), (q0,1) configured for a serving PSCell and a cell with PCID different from the serving cell, and that the UE performs correct CSI-RS-based link recovery based on beam candidate set  (q1,0) and (q1,1). The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell with schedulingRequestID-BFR-r17 configured, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.5.5.5.8.1-1, A.5.5.5.8.1-2, A.5.5.5.8.1-3, and A.5.5.5.8.1-4 below. There are three cells, Cell 1 is the E-UTRAN PCell, Cell 2 is the PSCell and Cell 3 is the cell with different PCID in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.8.1-1 shows the variation of the downlink SNR of the PSCell and the SNR of the CSI-RS in set q0 in the active PSCell to emulate CSI-RS based beam failure. Figure A.5.5.5.8.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.5.8.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.8.1-2: General test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.8.1-3: Cell specific test parameters for FR2 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.5.5.5.8.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.5.5.5.8.2Test Requirements

Test requirements are applied to TRP specific report respectively on (q0,0), (q0,1) for cell-2 and (q1,0), (q1,1)  for cell-3 repectively as Figure A.5.5.5.8.1-1.

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1,0. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1,0 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.5.9Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion

## A.5.5.5.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.2.4 for UE fulfilling good serving cell quality criterion, if configured. goodServingCellEvaluationBFD [2] criterion is configured according to the parameters listed in table A.5.5.5.9.1-2.

The test parameters are given in tables A.5.5.5.9.1-1, A.5.5.5.9.1-2 and A.5.5.5.9.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.5.5.5.9.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSBs in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.5.5.5.9.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.5.5.5.9.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.5.9.1-2: General test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.5.5.5.9.1-3: Cell specific test parameters for FR2 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.5.5.5.9.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in DRX mode for UE fulfilling relaxed measurement criterion

## A.5.5.5.9.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 560+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.6Active BWP switch

## A.5.5.6.1DCI-based and Timer-based Active BWP Switch

## A.5.5.6.1.1E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC

## A.5.5.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6. Supported test configurations are shown in table A.5.5.6.1.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.6.1.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.5.5.6.1.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.6.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell.

-UE is configured with a bwp-InactivityTimer timer value for PSCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PSCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE should switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PSCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the slot wherein bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell at latest at the beginning of the DL slot right after slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time in PSCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

Table A.5.5.6.1.1.1-1: DL BWP switch supported test configurations

Table A.5.5.6.1.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.1.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.1.1.1-4: OTA related test parameters for DL BWP switch in synchronous EN-DC

## A.5.5.6.1.1.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+Y1), (j+Y2), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.5.5.6.1.2E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC

A.5.5.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6.2, and interruption requirements for NR victim cell defined in clause 8.2.1.2.7. Supported test configurations are shown in table A.5.5.6.1.2.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.5.5.6.1.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.5.5.6.1.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) and SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 3 and the time duration of T2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 3 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0 in Cell 2 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PSCell.

-UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after slot (i+TBWPswitchDelay).

PCell(Cell 1) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

PSCell(Cell 2) interruption due to BWP switch on SCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PSCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after the slot wherein bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after SCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PSCell at latest at the beginning of the DL slot right after slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+TBWPswitchDelay).

PCell(Cell 1) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

PSCell(Cell 2) interruption due to BWP switch of SCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to NR PSCell is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during BWP switch of SCell.

Table A.5.5.6.1.2.1-1: DL BWP switch supported test configurations

Table A.5.5.6.1.2.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.1.2.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.1.2.1-4: OTA related test parameters for DL BWP switch in synchronous EN-DC

A.5.5.6.1.2.2Test Requirements

During T1, the UE shall start to send the ACK for SCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for SCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in TS 36.133 [15] clause 7.32.2.7.

During T1, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PSCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.6.2.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.5.5.6.2RRC-based Active BWP Switch

## A.5.5.6.2.1E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC

A.5.5.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.5.5.6.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one PSCell (Cell 2) as given in table A.5.5.6.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of PSCell are specified in table A.5.5.6.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on E-UTRA PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2.

Before the test starts,

-UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 2 (PSCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

If the RRCReconfiguration is embedded in E-UTRA RRC message, time period T1 starts when a E-UTRA RRC message RRCConnectionReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side from PCell in PSCell’s slot # denoted i. Otherwise, i.e., if the RRCReconfiguration is not embedded in E-UTRA RRC message, time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in from PSCell in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to completely receive PDSCH on PSCell from the first DL slot occurs right after the beginningof PSCell’s DL slot  as defined in clause 8.6.3 and starts to report valid ACK/NACK for the PSCell from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PSCell’s BWP-1 starting the first DL slot that occurs right after the beginning of DL slot .i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when a vaild ACK/NACK is received.

Table A.5.5.6.2.1.1-1: DL BWP switch supported test configurations

Table A.5.5.6.2.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.2.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.2.1.1-4: OTA related test parameters for BWP switching test case

A.5.5.6.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell from the first DL slot that occurs right after the beginning of DL slot  and starts to report valid ACK/NACK for the PSCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs

## A.5.5.6.3.1E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC

A.5.5.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch on multiple CCs delay requirement defined in clause 8.6. Supported test configurations are shown in table A.5.5.6.3.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.5.5.6.3.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and NR SCell is specified in table A.5.5.6.3.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.6.3.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) and SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and Cell 3 and the time duration of T2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell and SCell, BWP-1 and BWP-2, in Cell 2 and Cell 3 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell and SCell.

-UE is configured with a bwp-InactivityTimer timer value for PSCell and SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PSCell DL BWP switch and a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE simultaneously, are received at the UE side in PSCell and SCell slot # denoted i. The UE should switch its bandwidth part from BWP-1 to BWP-2 in PSCell and SCell.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TMultipleBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after slot (i+TMultipleBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after slot (i+TMultipleBWPswitchDelay).

The UE shall be able to receive PDSCH at the beginning of the DL slot right after SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after slot (i+TMultipleBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after slot (i+TMultipleBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PSCell (Cell 2) and SCell (Cell 3).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the slot wherein bwp-InactivityTimer timer expires in PSCell and SCell. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1 in both PSCell and SCell.

The UE shall be able to receive PDSCH on PSCell at the beginning of the DL slot right after PSCell’s DL slot (j+ TMultipleBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell at latest at the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay +k1). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay).

The UE shall be able to receive PDSCH on SCell at the beginning of the DL slot right after SCell’s DL slot (j+ TMultipleBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell at latest at the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay +k1). The UE shall be continuously scheduled on SCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay).

The test equipment verifies the DL BWP switch time in PSCell and SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

Table A.5.5.6.3.1.1-1: DL BWP switch supported test configurations

Table A.5.5.6.3.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.3.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.3.1.1-4: OTA related test parameters for DL BWP switch in synchronous EN-DC

A.5.5.6.3.1.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell and SCell from the first UL slot that occurs after the beginning of DL slot (i+TMultipleBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell and SCell from the first UL slot that occurs after the beginning of DL slot (j+TMultipleBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay and bwp-SwitchingMultiCCs-r16 [2], UE shall finish BWP switch within the time duration TMultipleBWPswitchDelay defined in TS 38.133 caluse 8.6.2A and 8.6.2B

All of the above test requirements shall be fulfilled in order for the observed PSCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+Y1), (j+Y2), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.5.5.6.4SCell dormancy switch

## A.5.5.6.4.1E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time

## A.5.5.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify

1) the interruption due to RRM and CSI measurement during SCell dormancy on spCell is within the limits 1) the interruption due to RRM and CSI measurement during SCell dormancy on spCell is within the limits specified in clause 8.2.1.2.15.2 and 8.2.1.2.15.3 for NR victim cell, and

2) the SCell dormancy switch delay is within the requirement defined in clause 8.6.2, and the SCell dormancy switch interruption is within the limits defined in clause 8.2.1.2.15.1 for NR victim cell.

Supported test configurations are shown in table A.5.5.6.4.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.5.5.6.4.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.5.5.6.4.1.1-3 below.

The tests consist of three consecutive time periods T1, T2, and T3, respectively. All cells have constant signal levels throughout the test. The UE is continuously scheduled in PCell and PSCell throughout the test

Before the test starts,

-UE is connected to Cell 1 (PCell), Cell 2 (PSCell) and Cell 3 (SCell).

-UE is configured with a single UE-specific downlink bandwidth part, BWP-0, for Cell 2. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is configured with one non-dormant and one dormant UE-specific downlink bandwidth part, BWP-0 and BWP-1, respectively, for Cell 3. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 3 is BWP-0.

-UE is indicated that firstOutsideActiveTimeBWP-Id that the active DL BWP after when switching from dormant BWP in Cell 3 is BWP-0

T1 starts at the point in time at which the UE receives a DCI with dormancy indication on PDCCH in PSCell at the antenna connector, in a slot # denoted m, pertaining to dormancy indication for switching SCell from non-dormancy to dormancy. The UE shall complete switching of the SCells to dormancy by the end of slot m + ceil(TBWPswitchDelay/NR slot length) + 1 in Test1, and slot m + ceil(TBWPswitchDelay/NR slot length) + 2 in Test2, as specified in clause 8.6.2. Any PSCell interruptions due to the switching between non-dormant and dormant BWPs shall fulfill requirements in clause 8.2.1.2.15.1 for NR victim cell. The test equipment verifies that interruptions due to switching from non-dormancy to dormancy are within the requirements by analysing HARQ feedback transmitted in PSCell for PSCell.

During T2, the UE is carrying out CSI and RRM measurements on dormant SCell. Any interruptions due to CSI and RRM measurements shall fulfill requirements in clause 8.2.1.2.15.2 and 8.2.1.2.15.3 for NR victim cell. The test equipment verifies that the interruptions are within the allowed percentages by counting ACK/NACKs in PSCell. At the end of T2, the test equipment transmits a DCI with dormancy indication on PDCCH in PSCell carrying a dormany indication for switching SCell from dormancy to non-dormancy.

T3 starts at the point in time at which the UE receives a DCI with dormancy indication on PDCCH in PSCell at the antenna connector, in a slot # denoted n, pertaining to dormancy indication for switching SCell from dormancy to non-dormancy. The UE shall complete switching of the SCell to non-dormancy by the end of slot n + ceil(TBWPswitchDelay/NR slot length) + 1 in Test1, and slot n + ceil(TBWPswitchDelay/NR slot length) + 2 in Test2, as specified in clause 8.6.2. Any PSCell interruptions due to the switching between non-dormant and dormant BWPs shall fulfill requirements in clause 8.2.1.2.15.1 for NR victim cell. The test equipment verifies that interruptions due to switching from dormancy to non-dormancy are within the requirements by analysing HARQ feedback transmitted in PSCell for PSCell. PDCCHs indicating new transmissions shall be sent continuously on SCell from the slot right after n + ceil(TBWPswitchDelay/NR slot length) + 1 in Test1, and slot n + ceil(TBWPswitchDelay/NR slot length) + 2 in Test2. The test equipment verifies the SCell dormancy switch delay by counting the slots from slot n till an ACK/NACK for SCell is received.

There are two subtests in this test. In Subtest 1 the DCI format 1_1 command for SCell dormancy switch is transmitted within the first 3 OFDM symbols in a slot, and in Subtest 2 the DCI format 1_1 command for SCell dormancy switch is transmitted after the first 3 OFDM symbols in a slot. A UE that only supports triggering during within the first three OFDM symbols of a slot shall only undergo Test1, whereas a UE that supports triggering also in remaining OFDM symbols of a slot shall undergo Test1 and Test2.

Table A.5.5.6.4.1.1-1: Dormancy switch supported test configurations

Table A.5.5.6.4.1.1-2: General test parameters for Dormancy switch in synchronous EN-DC

Table A.5.5.6.4.1.1-3: NR Cell specific test parameters for Dormancy switch in synchronous EN-DC

Table A.5.5.6.4.1.1-4: OTA related test parameters for Dormancy switch in synchronous EN-DC

## A.5.5.6.4.1.2Test Requirements

During T1, any interruption on PSCell due to dormancy switching of SCell shall be within the requirement specified in in clause 8.2.1.2.15.1 for NR victim cell.

During T2, interruptions on PSCell due to CSI and RRM measurements on dormant SCell shall be within the interruption rate requirements specified in 8.2.1.2.15.1 for NR victim cell.

During T3, any interruption on PSCell due to dormancy switching of SCell shall be within the requirement specified in in clause 8.2.1.2.15.1 for NR victim cell. Monitoring of PDCCH for SCell in PSCell shall be resumed within the dormancy switching time specified in clause 8.6.2A.

For an event to be considered to be correct, all requirements above have to be fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.6.4.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time

## A.5.5.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify the NR SCell dormant BWP switch delay requirement defined in clause 8.6.2A.1, interruption requirements due to the NR SCell dormant BWP switch defined in clause 8.2.1.2.15.1 for NR victim cells and in clause 7.32.2.14.1 of TS 36.133 [15] for E-UTRA victim cell, respectively, and interruption requirements due to CSI and RRM measurements on the NR dormant SCells defined in clauses 8.2.1.2.15.2 and 8.2.1.2.15.3 for NR victim cells and in clause 7.32.2.14.2 of TS 36.133 [15] for E-UTRA victim cell, respectively. Supported test configurations are shown in table A.5.5.6.4.2.1-1.

The general test parameters are given in table A.5.5.6.4.2.1-2, and NR cell specific test parameters are given in table A.5.5.6.4.2.1-3 and table A.5.5.6.4.2.1-4 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR FR1 PSCell (Cell 2), and three NR FR2 SCells (Cell 3-5) as given in table A.5.5.6.4.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.5.5.6.4.2.1-3 and table A.5.5.6.4.2.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1), PSCell (Cell 2), and SCell (Cell 5) to ensure that the UE will have ACK/NACK sending except the time before T1 and during T3. PDCCHs indicating new transmissions shall be sent continuously on SCells (Cell 3,4) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on the cells and the time duration of when active BWP of the cell is dormant.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC), and Cell 3-5 (SCells) on radio channels 3-5 (SCCs), respectively.

-UE is configured with 2 different UE-specific downlink BWPs for Cell 3 and Cell 4, BWP-1 and BWP-2. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB. Here, BWP-2 on Cell 3 and Cell 4 is configured as dormant BWP.

-UE is configured with 1 UE-specific downlink BWP the same as initial BWP for Cell 3 and Cell 4.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in Cell 3 and Cell 4.

-UE is configured with DRX.

-UE is configured to monitor PDCCH for DCI format 2_6 from Cell 2 at ps-Offset before the start of onDuration. ps-Offset is selected to correspond to the dormancy switching time specified in clause 8.6.2A.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, T3, and T4, respectively.

During T1,

Time period T1 starts when a DCI format 2_6 command for Cell 3 and Cell 4 DL BWP switch to BWP-2, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2. The UE shall be continuously scheduled on the cell starting from the beginning of the DL slot right after slot (i+ TMultipleBWPswitchDelay+X).

The UE shall be able to receive PDSCH at the beginning of the DL slot right after SCell(Cell 5)’s DL slot (i+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2. The UE shall be continuously scheduled on the cell starting from the beginning of the DL slot right after slot (i+ TMultipleBWPswitchDelay+X).

PCell(Cell 1) interruption due to dormant BWP switch on PSCell shall occur within the dormant BWP switch delay.

SCell(Cell 5) interruption due to dormant BWP switch on SCell(Cell 5) shall occur within the dormant BWP switch delay.

During T2,

Time period T2 starts when dormant BWP switch latency requirement test is completed. The test equipement shall schedule PDSCH every slot.

The UE shall be able to report ACK/NACK corresponding to the scheduled PDSCH to PSCell except for the allowed times as defined in clauses 8.2.1.2.15.2 and 8.2.1.2.15.3.

The UE shall be able to report ACK/NACK corresponding to the scheduled PDSCH to PCell except for the allowed times as defined in clause 7.32.2.14.2 of TS 36.133 [15].

During T3,

Time period T3 starts when interruption due to SSB based RRM measurement and CSI measurement requirements test is completed. Test equipment shall not transmit PDCCH, hence, the UE doesn’t monitor PDCCH except DCI format 2_6 based PDCCH.

During T4,

Time period T4 starts when a DCI format 2_6 command for Cell 3 and Cell 4 DL BWP switch to BWP-1, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted j. The UE shall switch its bandwidth part from BWP-2 to BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2. The UE shall be continuously scheduled on the cell starting from the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay+X).

The UE shall be able to receive PDSCH at the beginning of the DL slot right after all SCell’s (Cell 3,4,5) DL slot (j+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2. The UE shall be continuously scheduled on the cells starting from the beginning of the DL slot right after slot (j+ TMultipleBWPswitchDelay+X).

PCell(Cell 1) interruption due to dormant BWP switch on PSCell shall occur within the dormant BWP switch delay.

SCell(Cell 5) interruption due to dormant BWP switch on SCell(Cell 5) shall occur within the dormant BWP switch delay.

Table A.5.5.6.4.2.1-1: Supported test configurations for EN-DC DCI 2_6 based Domant BWP Switch on Multiple NR FR2 SCells

Table A.5.5.6.4.2.1-2: General test parameters for EN-DC DCI 2_6 based Domant BWP Switch on Multiple NR FR2 SCells

Table A.5.5.6.4.2.1-3: Cell specific test parameters for EN-DC DCI 2_6 based Domant BWP Switch on Multiple NR FR2 SCells

Table A.5.5.6.4.2.1-4: OTA related test parameters for EN-DC DCI 2_6 based Domant BWP Switch on Multiple NR FR2 SCells

## A.5.5.6.4.2.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of PSCell’s DL slot (i+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2.

During T2, the UE shall transmit at least 98.5 % of ACK/NACK on NR PCell.

During T4, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of PSCell’s DL slot (j+ TMultipleBWPswitchDelay+X) as defined in clause 8.6.2A.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start of the interruption of PCell and SCell (Cell 5) during dormant BWP switch on SCells (Cell 3,4) shall not happen outside the dormant BWP switch delay.

During T1, the start of the interruption of PCell and SCells (Cell 3,4,5) during dormant BWP switch on SCells (Cell 3,4) shall not happen outside the dormant BWP switch delay.

## A.5.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs

## A.5.5.6.5.1E-UTRAN – NR PSCell FR2  and NR SCell FR2 DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC

A.5.5.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for simultaneous RRC-based BWP switch on multiple CCs defined in clause 8.6.3A. Supported test configurations are shown in table A.5.5.6.5.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2)  and one NR SCell (Cell 3) as given in table A.5.5.6.5.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and NR SCell are specified in table A.5.5.6.5.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), to Cell 2 (PSCell) on radio channel 2 (PSCC) and to Cell 3 (SCell) on radio channel 3.

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 2 (PSCell) and Cell 3 (SCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 2 (PSCell) and Cell 3 (SCell).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration in Cell 2 and Cell3, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition in Cell 2 and Cell 3.

The UE shall be able to completely receive PDSCH on Cell 2 and Cell 3 at the beginning of the DL slot right after PSCell’s DL slot (i+) as defined in clause 8.6.3A and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+). The UE shall be continuously scheduled on Cell 2’s BWP-1and Cell 3’s BWP-1 starting from the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

TRRCprocessingDelay , TBWPswitchDelayRRC and DRRC are defined in clause 8.6.3A.

The test equipment verifies the DL BWP switch time in Cell 2 and Cell 3 by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when RRC Reconfiguration Complete message is received.

Table A.5.5.6.5.1.1-1: DL BWP switch supported test configurations

Table A.5.5.6.5.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.5.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

Table A.5.5.6.5.1.1-4: OTA related test parameters for BWP switching test case

A.5.5.6.5.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell and SCell in the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

All of the above test requirements shall be fulfilled in order for the observed PSCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.7PSCell addition and release delay

## A.5.5.7.1Addition and Release Delay of NR PSCell

## A.5.5.7.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delays under EN-DC are within the requirements stated in clause 7.31.2 of TS 36.133 [15] for the case when the PSCell is unknown by the UE at the time of addition.

Supported test configurations are shown in A.5.5.7.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.2-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in tables A.5.5.7.1.1-2, cell-specific parameters in A.5.5.7.1.1-3 and OTA parameters in A.5.5.7.1.1-4   below. The test consists of four successive time periods with duration of T1, T2, T3 and T4. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

The test system shall send a RRC message to the UE to add PSCell (Cell 2) on radio channel 2. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The RRC message to add PSCell shall be sent to the UE during period T1. The point in time at which the RRC message to add PSCell (Cell2) is received at the UE antenna connector defines the start of period T2.

The test system shall observe the periodic reporting of CSI for PSCell during T3. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T3.

The test system shall send a RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell2) shall be sent to the UE during period T3, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

Table A.5.5.7.1.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.7.1.1-2: General Test Parameters for PSCell Addition and Release

Table A.5.5.7.1.1-3: Cell Specific Parameters for PSCell Addition and Release

Table A.5.5.7.1.1-4: OTA related test parameters

## A.5.5.7.1.2Test Requirements

The UE shall transmit the PRACH to PSCell at latest 582 msNote1 into T2.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T3.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T3

The UE shall stop sending CSI reports for PSCell in at latest 20 ms into T4.

All the above test requirements shall be fulfilled for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

NOTE 1:The PSCell addition delay can be expressed as follows as specified in clause 7.31.2 of TS 36.133 [15]:

Tconfig_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 40 ms

Tsearch = 8*3*20 = 480 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.5.5.8Active TCI state switch delay

## A.5.5.8.1MAC-CE based active TCI state switch

## A.5.5.8.1.1E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state

## A.5.5.8.1.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3. Supported test configurations are shown in table A.5.5.8.1.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.8.1.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.5.5.8.1.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.8.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 2 different TCI states for PSCell, PDCCH TCI state 0 (QCL’d to SSB0) and TCIstate 1 (QCL’d to SSB1), in Cell 2 before starting the test.

-UE is indicated in TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. Figure A.5.5.8.1.1.1-1 and Figure A.5.5.8.1.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PSCell on TCI state 0 till slot n+ THARQ +. The test equipment also verifies the TCI state switch time in PSCell by scheduling the UE on TCI state 1 after slot n+ THARQ + + (Tfirst-SSB + TSSB-proc)/NR slot length .3Nslotsubframe,µ3Nslotsubframe,µ

Table A.5.5.8.1.1.1-1: Supported test configurations

Table A.5.5.8.1.1.1-2: General test parameters for TCI state switch

Table A.5.5.8.1.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.5.5.8.1.1.1-4: OTA related test parameters for TCI state switch

Figure A.5.5.8.1.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.5.5.8.1.1.1-2: Time multiplexed downlink transmissions during T2

## A.5.5.8.1.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on TCI state 0 till slot n+ THARQ + 3Nslotsubframe,µ

-be able to start receiving on TCI state 1 after slot n+ THARQ + + Tfirst-SSB/NR slot length5Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.8.2RRC based active TCI state switch

## A.5.5.8.2.1E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state

## A.5.5.8.2.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3Supported test configurations are shown in table A.5.5.8.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.8.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.5.5.8.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.8.2.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 1 TCI state for PSCell, PDCCH-TCI-state0 (QCL’d to SSB0)

-UE is indicated in TCI state0 as the active TCI state

The test consists of two time periods, T1 and T2. Figure A.5.5.8.2.1.1-1 and Figure A.5.5.8.2.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI-state1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a RRC command indicating a switch to TCI-state1.

The test equipment verifies the TCI state switch time in PSCell by scheduling the UE on TCI state 1 after slot n+ (TRRC_processing  + Tfirst-SSB )/NR slot length + .2Nslotsubframe,µ

Table A.5.5.8.2.1.1-1: Supported test configurations

Table A.5.5.8.2.1.1-2: General test parameters for TCI state switch

Table A.5.5.8.2.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.5.5.8.2.1.1-4: OTA related test parameters for TCI state switch

Figure A.5.5.8.2.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.5.5.8.2.1.1-2: Time multiplexed downlink transmissions during T2

## A.5.5.8.2.1.2Test Requirements

During T2, UE shall send L1-RSRP report with both SSB0 and SSB1.

After receiving RRC command in slot n, UE shall be able to start receiving on TCI state 1 after slot n+ (TRRC_processing  + Tfirst-SSB)/NR slot length + .2Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.9Uplink spatial relation switch delay

## A.5.5.9.1MAC-CE based uplink spatial relation switch

## A.5.5.9.1.1E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation

## A.5.5.9.1.1.1Test Purpose and Environment

The purpose of this test is to verify the uplink spatial relation switch delay requirement defined in clause 8.12.3 by a UE capable of beam correspondence without the need for UL beam sweeping. Supported test configurations are shown in table A.5.5.9.1.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.9.1.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.5.5.9.1.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.9.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have continuous ACK/NACK sending by PUCCH.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 2 different spatial relations for PSCell, PUCCH spatial relation 0 (QCL’d to SSB0) and spatial relation 1 (QCL’d to SSB1), in Cell 2 before starting the test.

-UE is indicated in spatial relation 0 as the active PUCCH spatial relation

The test consists of two time periods, T1 and T2. During T1 only SSB to which PUCCH spatial relation 0 QCLed is transmitted. At the beginning of T2, the SSB corresponding to spatial relation 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to transmit PUCCH with spatial relation 1.

The test equipment verifies that UE can be scheduled on PSCell on spatial relation 0 till n + THARQ/NR slot length + . The test equipment also verifies the spatial relation switch time in PSCell by scheduling the UE on spatial relation 1 from slot n + THARQ/NR slot length +  + 1 and onwards.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.5.5.9.1.1.1-1: Supported test configurations

Table A.5.5.9.1.1.1-2: General test parameters for spatial relation switch

Table A.5.5.9.1.1.1-3: NR Cell specific test parameters for spatial relation switch

Table A.5.5.9.1.1.1-4: OTA related test parameters for uplink spatial relation switch

## A.5.5.9.1.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to transmit PUCCH on spatial relation 0 till n + THARQ/NR slot length + ; 3Nslotsubframe,µ

-be able to start transmitting PUCCH on spatial relation 1 from slot n + THARQ/NR slot length +  + 1.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.9.2RRC based spatial relation switch

## A.5.5.9.2.1E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS

## A.5.5.9.2.1.1Test Purpose and Environment

The purpose of this test is to verify the RRC based spatial relation switch delay requirement defined in clause 8.12.5 by a UE capable of beam correspondence without the need for UL beam sweeping. Supported test configurations are shown in table A.5.5.9.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.9.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.5.5.9.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.9.2.1.1-4.

Periodic SRS is transmitted on NR PSCell (Cell2), and the SRS configuration is SRSConf.1 given in table A.5.4.1.1.1-3.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is configured with 1 SRS-SpatialRelation0 associated with SSB0.

-UE is indicated SRS-SpatialRelation0 as the active SRS spatial relation.

The test consists of two time periods, T1 and T2. During T1 only SSB0 to which SRS-SpatialRelation0 associated is transmitted. UE shall transmit periodic SRS with SRS-SpatialRelation0 of PSCell. At the beginning of T2, the SSB1 corresponding to SRS-SpatialRelation1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a RRC command indicating a switch to transmit periodic SRS with target SRS-SpatialRelation1. The test equipment verifies that UE shall be able to transmit periodic SRS with target spatial relation (SRS-SpatialRelation1) on PSCell in the slot n + TRRC_processing/NR slot length + 1.

Table A.5.5.9.2.1.1-1: Supported test configurations

Table A.5.5.9.2.1.1-2: General test parameters for spatial relation switch associated with a known DL-RS

Table A.5.5.9.2.1.1-3: NR Cell specific test parameters for spatial relation switch associated with a known DL-RS

Table A.5.5.9.2.1.1-4: OTA related test parameters for spatial relation switch associated with a known DL-RS

## A.5.5.9.2.1.2Test Requirements

During T2, UE shall send L1-RSRP report with SSB1 to which SRS-SpatialRelation1 is associated.

After receiving RRC command in slot n, UE shall be able to transmit target periodic SRS with SRS-SpatialRelation1 on PSCell in the slot n + TRRC_processing/NR slot length + 1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.10UE specific CBW change

## A.5.5.10.1UE specific CBW change on FR2 NR PSCell

## A.5.5.10.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13. Supported test configurations are shown in table A.5.5.10.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2) as given in table A.5.5.10.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell are specified in table A.5.5.10.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 2 (PSCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

-UE is indicated in SCS-SpecificCarrier that the active CBW is CBW-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration which reconfigure the UE specific CBW parameter, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated UE specific CBW of final condition.

The UE shall be able to completely receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+) as defined in clause 8.13 and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+). The UE shall be continuously scheduled on PSCell’s BWP-1 on CBW-2 starting from the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthTRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthTRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

TRRCprocessingDelay and TCBWchangeDelayRRC are defined in clause 8.13.

The test equipment verifies the UE specific CBW change switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated UE specific CBW configuration is sent till the time when RRC Reconfiguration Complete message is received.

Table A.5.5.10.1.1-1: UE specific CBW change supported test configurations

Table A.5.5.10.1.1-2: General test parameters for UE specific CBW change in synchronous EN-DC

Table A.5.5.10.1.1-3: NR Cell specific test parameters for UE specific CBW change in synchronous EN-DC

Table A.5.5.10.1.1-4: OTA related test parameters for UE specific CBW change test case

## A.5.5.10.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell in the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

All of the above test requirements shall be fulfilled in order for the observed PSCell UE specific CBW change switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.11Unified TCI state switch delay

## A.5.5.11.1MAC-CE based active joint TCI state switch

## A.5.5.11.1.1E-UTRAN – NR PSCell FR2 active joint TCI state switch for a known TCI state

## A.5.5.11.1.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based joint TCI state switch delay requirement defined in clause 8.15.3 and 8.16.3 by a UE capable of beam correspondence without the need for UL beam sweeping. Supported test configuration is shown in table A.5.5.11.1.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.11.1.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.2-1 and cell-specific parameters of NR PSCell is specified in table A.5.5.11.1.1.2-1 below. The OTA related test parameters for FR2 are shown in table A.5.5.11.1.1.2-2.

PDCCHs indicating new transmissions shall be sent continuously on PSCell to ensure that the UE would have ACK/NACK sending.

Table A.5.5.11.1.1.1-1: Supported test configurations

Table A.5.5.11.1.1.1-2: General test parameters for TCI state switch

## A.5.5.11.1.1.2Test parameters

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to joint.

-UE is configured with 2 different DLorJoint States for PSCell, Joint TCI state 0 (QCL’d to SSB0) and Joint TCI state 1 (QCL’d to SSB1) before starting the test,

-UE is indicated in Joint TCI state 0 as the active joint TCI state.

The test consists of two time periods, T1 and T2. Figure A.5.5.11.3.1.1-1 and Figure A.5.5.11.3.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB0 to which Joint TCI state 0 is QCL’d is transmitted. At the beginning of T2, the SSB1 corresponding to Joint TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to Joint TCI state 1.The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The test equipment verifies that UE shall be able to receive and transmit with Joint TCI state 0 until slot n+ THARQ +, and shall be able to receive and transmit with Joint TCI state 1 from slot n+ THARQ + + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.5.5.11.1.1.2-1: NR Cell specific test parameters for TCI state switch

Table A.5.5.11.1.1.2-2: OTA related test parameters for TCI state switch

## A.5.5.11.1.1.3Test Requirements

The test verifies that UE can be scheduled by PSCell on Joint TCI state 0 and Joint TCI state 1.

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to receive and transmit with Joint TCI state 0 until  slot n+ THARQ + 3Nslotsubframe,µ

-be able to start receiving and transmitting with Joint TCI state 1 after slot n+ THARQ + + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.11.2MAC-CE based active uplink TCI state switch

## A.5.5.11.2.1E-UTRAN – NR PSCell FR2 active uplink TCI state switch for a known TCI state

## A.5.5.11.2.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based uplink TCI state switch delay requirement defined in clause 8.16.3 by a UE capable of beam correspondence without the need for UL beam sweeping. Supported test configurations are shown in table A.5.5.11.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.5.5.11.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.2-1 and cell-specific parameters of NR PSCell is specified in table A.5.5.11.2.1.2-1 below. The OTA related test parameters for FR2 is shown in table A.5.5.11.2.1.2-2.

Table A.5.5.11.2.1.1-1: Supported test configurations

Table A.5.5.11.2.1.1-2: General test parameters for spatial relation switch

## A.5.5.11.2.1.2Test parameters

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC);

-PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have continuous ACK/NACK sending by PUCCH;

-UE is provided with TCI-UL-State-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to separate;

-UE is configured with 2 different uplink TCI states for PSCell, uplink TCI state 0 (associated with SSB0) and uplink TCI state 1 (associated with SSB1), by using RRC signalling ul-TCI-StateList-r17 in IE BWP-UplinkDedicated, in Cell 2 before starting the test;

-UE is indicated uplink TCI state 0 as the active uplink TCI state.

The test consists of two time periods, T1 and T2. During T1 only SSB#0 with which uplink TCI state 0 is associated is transmitted. At the beginning of T2, the SSB#1 corresponding to uplink TCI state 1 starts transmitting. After the beginning of T2, in slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB#0 and SSB#1, UE receives a MAC-CE command indicating a switch to transmit PUCCH with uplink TCI state 1. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

Index of CSI-RS#1 is configured for UE as PUSCH-PathlossReferenceRS-Id-r17 which is indicated in TCI-UL-State-r17 of uplink TCI state 1. CSI-RS#1 is QCLed typeD with SSB#1. UE does not maintain CSI-RS#1 as pathloss RS before the uplink TCI state switching.

Table A.5.5.11.2.1.2-1: NR Cell specific test parameters for uplink TCI state switch

Table A.5.5.11.2.1.2-2: OTA related test parameters for uplink spatial relation switch

## A.5.5.11.2.1.3Test Requirements

The test verifies that UE can be scheduled by PSCell on uplink TCI state 0 and uplink TCI state 1. The test also verifies the active uplink TCI state switch time in PSCell meeting the requirement defined in 8.16.3. Specifically,

During T2, UE shall send L1-RSRP report with results for SSB#0 and SSB#1 before sending MAC-CE command.

After receiving MAC-CE command in slot n in T2, UE shall:

-be able to continue to transmit PUCCH on uplink TCI state 0 till slot n + THARQ + ; 3Nslotsubframe,µ

-be able to start transmitting PUCCH on uplink TCI state 1 from slot n + THARQ +  + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length and onwards.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.11.3MAC-CE based active downlink TCI state switch

## A.5.5.11.3.1E-UTRAN – NR PSCell FR2 downlink TCI state switch to cell with additional PCI for a known TCI state

## A.5.5.11.3.1.1Test Purpose and Environment

The purpose of this test is to verify the active DL TCI state switch delay requirement for unified TCI defined in clause 8.15.3. Supported test configurations are shown in table A.5.5.X.3.1.1-1.

Table A.5.5.11.3.1.1-1: Supported test configurations

## A.5.5.11.3.1.2Test Parameters

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2), and one NR cell with additional PCI different from from serving cell (Cell 3) configured for intercell L1-RSRP measurement and report as given in table A.5.5.11.3.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and cell with additional PCI are specified in table A.5.5.11.3.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.5.5.11.3.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) and cell with additional PCI (Cell 3) to ensure that the UE would have ACK/NACK transmission.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC), Cell 3 (Cell with additional PCI) in radio channel 3.

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to seperate;

-UE is configured with L1-RSRP measurements on cell with additional PCI (Cell 3)

-UE is configured with 2 different TCI states for PSCell, PDCCH TCI state 0 (QCL’d to TRS resource set 1, TCI state of which is QCLed to SSB0 of Cell2) and TCI state 1 (QCL’d to TRS resource set 3, TCI state of which is QCLed to SSB1 of Cell3), in Cell 2 before starting the test.

-UE is indicated in TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. Figure A.5.5.11.3.1.1-1 and Figure A.5.5.11.3.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 of Cell 2 and SSB1 of Cell 3, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PSCell on TCI state 0 till slot n+ THARQ +3. The test equipment also verifies the TCI state switch time in to cell with additional PCI by scheduling the UE on TCI state 1 after slot n+ THARQ +3 + (Tfirst-SSB + TSSB-proc) /NR slot length .Nslotsubframe,µNslotsubframe,µ

Table A.5.5.11.3.1.1-2: General test parameters for TCI state switch

Table A.5.5.11.3.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.5.5.11.3.1.1-4: OTA related test parameters for TCI state switch

Figure A.5.5.11.3.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.5.5.11.3.1.1-2: Time multiplexed downlink transmissions during T2

## A.5.5.11.3.1.3Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on DL TCI state 0 till slot n+ THARQ +3Nslotsubframe,µ

-be able to start receiving on DL TCI state 1 after slot n+ THARQ +(5 ms + Tfirst-SSB) / NR slot length

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.5.12PSCell activation and deactivation delay

## A.5.5.12.1PSCell activation and deactivation delay

## A.5.5.12.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell activation and deactivation delay under EN-DC are within the requirements stated in clause 7.38 in TS 36.133 [15] for the case when UE configured with one deactivated SCG and when PScell in one SCG is being activated where the PSCell is known by the UE at the time of activation.

Supported test configurations are shown in A.5.5.12.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.2-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in tables A.5.5.12.1.1-2, cell-specific parameters in A.5.5.12.1.1-3 and OTA parameters in A.5.5.12.1.1-4 below. The test consists of four successive time periods with duration of T1, T2, T3 and T4. There are two carriers each with one cell. The UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) and PSCell (Cell2) is in deactivated state. During T1, both Cell 1 and Cell2 are known to UE and UE performs measurement on deactivated PCell. Before the test starts the UE is configured RLM and BFD on deactivated PSCell. During T1, UE performs RLM and BFD on the deactivated PSCell and TCI state is known.

The test system shall send a RRC message to the UE to activate PSCell (Cell 2) on radio channel 2, where no any PSCell parameter is modified in the RRC message. The RRC message (to activate PSCell) also includes a request for the UE to transmit scheduling request on PUCCH for the PSCell after the PSCell has been successfully activated. The RRC message to activate PSCell shall be sent to the UE during period T1. The point in time at which the RRC message to activate PSCell (Cell2) is received at the UE antenna connector defines the start of period T2.

The test system shall observe the periodic reporting of CSI for PSCell during T3. The point in time at which the UE has sent scheduling request on PUCCH for PSCell (Cell 2) defines the start of period T3.

The test system shall send a RRC message to the UE to deactivate PSCell (Cell 2) on radio channel 2. The RRC message to deactivate PSCell (Cell2) shall be sent to the UE during period T3, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to deativate PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

Table A.5.5.12.1.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.12.1.1-2: General Test Parameters for PSCell activation and deactivation

Table A.5.5.12.1.1-3: Cell Specific Parameters for PSCell activation and deactivation

Table A.5.5.12.1.1-4: OTA related test parameters

## A.5.5.12.1.2Test Requirements

The UE performs RACH-less based PSCell activation. UE shall transmit the SR on PUCCH for PSCell at latest 65 msNote1 into T2.

The UE shall send at least one PUSCH on PSCell during T3.

The UE shall stop transmit PUSCH for PSCell in at latest 20 ms into T4.

All the above test requirements shall be fulfilled for the observed PSCell activation delay and PSCell deactivation delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

Note1:The PSCell addition delay can be expressed as follows as specified in clause 7.38 in TS 36.133 [15]:

Tactivation_time = TRRC_delay + Tprocessing + Tsearch + T∆ + TIU + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 5 ms

Tsearch = 0 ms

T∆ = 20 ms

TIU= max 20 ms

## A.5.5.13Conditional PSCell addition and release delay

## A.5.5.13.1Addition and Release Delay of NR PSCell

## A.5.5.13.1.1Test purpose and environment

The purpose of this test is to verify that the conditional NR PSCell addition and release delays under EN-DC are within the requirements stated in clause 8.9A.2.

Supported test configurations are shown in A.5.5.13.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.2-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in tables A.5.5.13.1.1-2, cell-specific parameters in A.5.5.13.1.1-3 and OTA parameters in A.5.5.13.1.1-4 below. The test consists of four successive time periods with duration of T1, T2, T3 and T4. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC.

During T1 only Cell 1 is known to the UE. NR shall configure a condition implying PSCell addition (Cell 2) during T1, at a time earlier than TRRC_delay before the beginning of T2.

Starting T2, Cell 2 becomes detectable. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T3. The test system shall observe the periodic reporting of CSI for PSCell during T3.

The test system shall send a RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell2) shall be sent to the UE during period T3, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

Table A.5.5.13.1.1-1: Supported test configurations for FR2 PSCell

Table A.5.5.13.1.1-2: General Test Parameters for Conditional PSCell Addition and Release

Table A.5.5.13.1.1-3: Cell Specific Parameters for Conditional PSCell Addition and Release

Table A.5.5.13.1.1-4: OTA related test parameters

## A.5.5.13.1.2Test Requirements

TRRC_delay + TEvent_DU occurs during T1 as the PSCell addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall transmit the PRACH to PSCell (Cell 2) less than Tconfig_PSCell_Addition_Conditional Note1 into T2.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T3.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T3

The UE shall stop sending CSI reports for PSCell in at latest 20 ms into T4.

All the above test requirements shall be fulfilled for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

Note1:The PSCell addition delay during T2 can be expressed as follows:

Tconfig_PSCell_Addition_Conditional = Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms

Where:

Tmeasure = 6720 ms for power class 1 or 4160 for power class 2/3/4

TUE_preparation = 10 ms

Tprocessing = 40 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.5.6Measurement procedure

## A.5.6.1Intra-frequency Measurements

## A.5.6.1.1EN-DC event triggered reporting test without gap under non-DRX

## A.5.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.5.6.1.1.1-1.

Table A.5.6.1.1.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.1.1.1-2, A.5.6.1.1.1-3 and A.5.6.1.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.5.6.1.1.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Figure A.5.6.1.1.1-1: Time multiplexed downlink transmissions (Config 1,2 example)

## A.5.6.1.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.1.2EN-DC event triggered reporting test without gap under DRX

## A.5.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.5.6.1.2.1-1.

Table A.5.6.1.2.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.1.2.1-2 ~ table A.5.6.1.2.1-6 below.

In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.1.2.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap with DRX

Table A.5.6.1.2.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap with DRX

Table A.5.6.1.2.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap with DRX

## A.5.6.1.2.2Test Requirements

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

## A.5.6.1.3EN-DC event triggered reporting test with per-UE gaps under non-DRX

## A.5.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3. Supported test configurations are shown in table A.5.6.1.3.1-1.

Table A.5.6.1.3.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.1.3.1-2 ~ 4 below.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.5.6.1.3.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps without DRX

Table A.5.6.1.3.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps without DRX

Table A.5.6.1.3.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps without DRX

Figure A.5.6.1.3.1-1: Time multiplexed downlink transmissions (Config 1,2 example)

## A.5.6.1.3.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3.2 s for a UE supporting power class 1,

-1.92 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.1.4EN-DC event triggered reporting test with per-UE gaps under DRX

## A.5.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3. Supported test configurations are shown in table A.5.6.1.4.1-1.

Table A.5.6.1.4.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.1.4.1-2 ~ 6.

During the test, Cell 2 and Cell 3 are transmitted from the direction determined according to A3.8.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.1.4.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps with DRX

Table A.5.6.1.4.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps with DRX

Table A.5.6.1.4.1-4: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 with per-UE gaps with DRX

Table A.5.6.1.4.1-5: Void

Table A.5.6.1.4.1-6: Void

## A.5.6.1.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X  from the beginning of time period T2, where X is

-4.8s for a UE supporting power class 1,

-2.88s for a UE supporting power class 2, 3 and 4

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X from the beginning of time period T2, where X is

-51.20 s for a UE supporting power class 1,

-30.72 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.1.5EN-DC event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP

## A.5.6.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of an event when CD-SSB is outside active BWP. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.5.6.1.1.1-1.

The test environment is the same as in A.5.6.1.1 with following exceptions in table A.5.6.1.1.1-3.

## A.5.6.1.5.2Test Requirements

The test requirements are the same as in A.5.6.1.1.2.

## A.5.6.1.6EN-DC event triggered reporting test without gap under non-DRX

## A.5.6.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2. Supported test configurations are shown in table A.5.6.1.6.1-1.

Table A.5.6.1.6.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.1.6.1-2, A.5.6.1.6.1-3 and A.5.6.1.6.1-4 below.

The CD-SSB is configured outside active DL BWP and NCD-SSB is configured fully within active DL BWP of FR2 PSCell. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.5.6.1.6.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.6.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.6.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Figure A.5.6.1.1.1-1: Time multiplexed downlink transmissions (Config 1,2 example)

## A.5.6.1.6.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X from the beginning of time period T2, where X is

-9.6s for a UE supporting power class 1,

-5.76s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.1.7EN-DC event triggered reporting test without gap under non-DRX for UE configured with cssf-Config

## A.5.6.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2 based on the enhanced CSSFoutside,gap by measuring one serving carrier per FR2 band. Supported test configurations are shown in table A.5.6.1.7.1-1.

Table A.5.6.1.7.1-1: supported test configurations

There are four cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2), FR2 SCell (Cell 3) and a FR2 neighbour cell (Cell 4) on the same frequency as the PSCell. All the FR2 cells are on the same FR2 band. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2, Cell 3 and Cell 4 are given in table A.5.6.1.7.1-2, A.5.6.1.7.1-3 and A.5.6.1.7.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PSCell and the frequency of the SCells respectively, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. At the beginning of T1 the UE receives an RRC message by which the PSCell and SCells (Cell 2 and Cell 3) becomes configured on NR. UE is also indicated to perform enhanced measurement by measuring one serving CC per FR2 band. During time duration T1, the UE shall not have any timing information of Cell 4.

Table A.5.6.1.7.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.7.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Table A.5.6.1.7.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with TDD PSCell in FR2 without gap without DRX

Figure A.5.6.1.7.1-1: Time multiplexed downlink transmissions (Config 1,2 example)

## A.5.6.1.7.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1,

-1.44 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2Inter-frequency Measurements

## A.5.6.2.1EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used

## A.5.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.1.1-1, A.5.6.2.1.1-2, and A.5.6.2.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in Table A.5.6.2.1.1-2 is provided for UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #13 as defined in Table A.5.6.2.1.1-2 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.2.1.1-1.

Table A.5.6.2.1.1-1 EN-DC event triggered reporting tests without SSB index reading for FR2-FR2

Table A.5.6.2.1.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.5.6.2.1.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.5.6.2.1.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.2 EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used

## A.5.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.2.1-1, A.5.6.2.2.1-2, and A.5.6.2.2.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.5.6.2.2.1-2 is provided for UE that does not support per-FR gap and in test 3&4 measurement gap pattern configuration #13 as defined in table A.5.6.2.2.1-2 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.2.2.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.2.2.1-1 EN-DC event triggered reporting tests without SSB index reading for FR2-FR2

Table A.5.6.2.2.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.5.6.2.2.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.5.6.2.2.2Test Requirements

In test 1 with per-UE gap and in test 3 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.3 EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used

## A.5.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.3.1-1, A.5.6.2.3.1-2, and A.5.6.2.3.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.5.6.2.3.1-1 is provided for UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #13 as defined in table A.5.6.2.3.1-1 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.2.3.1-1.

Table A.5.6.2.3.1-1 EN-DC event triggered reporting tests with SSB index reading for FR2-FR2

Table A.5.6.2.3.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.5.6.2.3.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.5.6.2.3.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.4EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used

## A.5.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.4.1-1, A.5.6.2.4.1-2, and A.5.6.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.5.6.2.4.1-2 is provided for UE that does not support per-FR gap and in test 3&4 measurement gap pattern configuration #13 as defined in table A.5.6.2.4.1-2 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.2.4.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.2.4.1-1: EN-DC event triggered reporting tests with SSB index reading for FR2-FR2

Table A.5.6.2.4.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.5.6.2.4.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.5.6.2.4.2Test Requirements

In test 1 with per-UE gap and in test 3 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.5EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used

## A.5.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR1 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.5.1-1, A.5.6.2.5.1-2, and A.5.6.2.5.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.5.6.2.5.1-2 is provided for a UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #13 as defined in table A.5.6.2.5.1-2 is provided for UE that support per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.5.6.2.5.1-1.

Table A.5.6.2.5.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR2

Table A.5.6.2.5.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.5.6.2.5.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.5.6.2.5.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.6EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used

## A.5.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR1 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.6.1-1, A.5.6.2.6.1-2, and A.5.6.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.5.6.2.6.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 measurement gap pattern configuration #13 as defined in table A.5.6.2.6.1-2 is provided for UE that support per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.5.6.2.6.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.2.6.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR2

Table A.5.6.2.6.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.5.6.2.6.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.5.6.2.6.2Test Requirements

In test 1 with per-UE gap and in test 3 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.7EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used

## A.5.6.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR1 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.7.1-1, A.5.6.2.7.1-2, and A.5.6.2.7.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.5.6.2.7.1-2 is provided for a UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #13 as defined in table A.5.6.2.7.1-2 is provided for UE that support per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.5.6.2.7.1-1.

Table A.5.6.2.7.1-1: EN-DC event triggered reporting tests with SSB index reading for FR1-FR2

Table A.5.6.2.7.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.5.6.2.7.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.5.6.2.7.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.8EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used

## A.5.6.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR1 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.2.8.1-1, A.5.6.2.8.1-2, and A.5.6.2.8.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.5.6.2.8.1-2 is provided for a UE that does not support per-FR gap and in test 3&4 measurement gap pattern configuration #13 as defined in table A.5.6.2.8.1-2 is provided for UE that support per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test 3&4. Otherwise it is only required to pass test 1&2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A4 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.5.6.2.8.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.2.8.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR2

Table A.5.6.2.8.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.5.6.2.8.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.5.6.2.8.2Test Requirements

In test 1 with per-UE gap and in test 3 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 2 with per-UE gap and in test 4 with per-FR gap, the UE shall send one Event A4 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1, 2, 3 and 4 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.2.9EN-DC event triggered reporting tests without gap under non-DRX in FR for UE supporting [FR1 only EN-DC 3-searcher capability]

## A.5.6.2.9.1Test purpose and Environment

The purpose of this test is to partly verify the intra-frequency cell search requirements in clause 9.1.5.1, clauses 9.2.5.1 and 9.2.5.2 for UE supporting [FR1 only EN-DC 3-searcher capability] makes correct reporting of an event.

## A.5.6.2.9.2Test parameters

In this test, LTE cell 1 as PCell in FR1 on LTE RF channel 1, NR cell 1 as PSCell in FR1 on NR RF channel 2, NR cell 2 as SCell in FR1 on NR RF channel 3 and NR cell 3 as SCell in FR1 on NR RF channel 4, where NR RF channel 2, NR RF channel 3 and NR RF channel 4 are in different bands, furthermore, NR cell 4 as neighbour cell in FR1 on NR RF channel 2 same as NR cell 2.

In the measurement control information, SCells with only SSB based L3 measurement are configured, and a measurement object is configured for the frequency of the neigbor cell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 4.

Supported test configurations of tess are shown in table A.5.6.2.9.2-1.

Table A.5.6.2.9.2-1: Supported test configurations

The test parameters of tests are shown in table A.5.6.2.9.2-2 and A.5.6.2.9.2-3 below.

Table A.5.6.2.9.2-2: General test parameters for intra-frequency event triggered reporting for FR2 without SSB time index detection

Table A.5.6.2.9.2-3: Cell specific test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection, for test case 2

## A.5.6.2.9.3Test Requirements

In this test , the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 1600 for UE supporting power class 1, or

## 960 for UE supporting other power class.

In this test, UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.3L1-RSRP measurement for beam reporting

## A.5.6.3.1SSB based L1-RSRP measurement when DRX is not used

## A.5.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.5.6.3.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.5.6.3.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.5.6.3.1.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.3.1.2-1 and table A.5.6.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.5.6.3.1.2-1: General test parameters

Table A.5.6.3.1.2-2: SSB specific test parameters

## A.5.6.3.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-1680 for UE supporting power class 1

-1200 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.6.3.2SSB based L1-RSRP measurement when DRX is used

## A.5.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.5.6.3.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.5.6.3.2.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.5.6.3.2.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.3.2.2-1 and table A.5.6.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.5.6.3.2.2-1: General test parameters

Table A.5.6.3.2.2-2: SSB specific test parameters

## A.5.6.3.2.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used

## A.5.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.5.6.3.3.1-1.

Table A.5.6.3.3.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.5.6.3.3.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.3.3.2-1 and table A.5.6.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.5.6.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.5.6.3.3.2-1: General test parameters

Table A.5.6.3.3.2-2: CSI-RS specific test parameters

## A.5.6.3.3.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.6.3.3.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.5.6.3.3.3-1: L1-RSRP absolute accuracy test requirement

## A.5.6.3.4CSI-RS based L1-RSRP measurement when DRX is used

## A.5.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.5.6.3.4.1-1.

Table A.5.6.3.4.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.5.6.3.4.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.3.4.2-1 and table A.5.6.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 1440 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.5.6.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.5.6.3.4.2-1: General test parameters

Table A.5.6.3.4.2-1: CSI-RS specific test parameters

## A.5.6.3.4.3Test Requirements

After 1440 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range from -10 to +20 dB which is referred to Table B.2.1.5.1-1 when calculated.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.6.3.4.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.5.6.3.4.3-1: L1-RSRP absolute accuracy test requirement

## A.5.6.3.5CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP

## A.5.6.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.5.6.3.3.1-1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in A.5.6.3.3.

The test environment is the same as in A.5.6.3.3 with following exceptions in table A.5.6.3.3.2-1.

The value of parameter “Dedicated BWP configuration” is DLBWP.1.2 and ULBWP.1.2.

NOTE:The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in A.5.6.3.3.3.

## A.5.6.3.6SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.5.6.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.5.6.3.1.1-1.

The test environment is the same as in A.5.6.3.1 with following exceptions in table A.5.6.3.1.2-1.

## A.5.6.3.6.2Test Requirements

The test requirements are the same as in A.5.6.3.1.3.

## A.5.6.3.7SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used

## A.5.6.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.5.6.3.7.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.5.6.3.7.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.5.6.3.7.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.3.7.2-1 and table A.5.6.3.7.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. During time duration T1, the UE shall not have any timing information of NR Cell 2.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.5.6.3.7.2-1: General test parameters

Table A.5.6.3.7.2-2: SSB specific test parameters

## A.5.6.3.7.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-[3360] for UE supporting power class 1

-[2080] for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.5.6.4CLI measurements

## A.5.6.4.1SRS-RSRP measurement with DRX

## A.5.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SRS-RSRP measurement. This test will verify the SRS-RSRP measurement requirements in clause 9.7.2.5 with the testing configurations for NR cells in table A.5.6.4.1.1-1.

Table A.5.6.4.1.1-1: Applicable NR configurations for FR2 SRS-RSRP test

## A.5.6.4.1.2Test Parameters

Two cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and FR2 PSCell (Cell 2). The test parameters for PSCell is given in table A.5.6.4.1.2-1 ~ A.5.6.4.1.2-3 below and applicability for the E-UTRAN cell are defined in A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system transmits SRS resource for measurement in the DL slot according to the SRS configuration in table A.5.6.4.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A.5.6.4.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 2 data symbols before SRS to be transmitted.

Table A.5.6.4.1.2-1: General test parameters for SRS-RSRP event triggered reporting for PSCell in FR2

Table A.5.6.4.1.2-2: NR Cell specific test parameters for SRS-RSRP event triggered reporting for PSCell in FR2

Table A.5.6.4.1.2-3: NR OTA Cell specific test parameters for SRS-RSRP event triggered reporting for PSCell and Neighbour cell UE in FR2

Table A.5.6.4.1.2-4: SRS configuration for measurement reporting

## A.5.6.4.1.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 100 ms from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.4.2CLI-RSSI measurement with DRX

## A.5.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of CLI-RSSI measurement. This test will verify the CLI-RSSI measurement requirements in clause 9.7.3.5 with the testing configurations for NR cells in table A.5.6.4.2.1-1.

Table A.5.6.4.2.1-1: Applicable NR configurations for FR2 CLI-RSSI test

## A.5.6.4.2.2Test Parameters

Two cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and FR2 PSCell (Cell 2). The test parameters for PSCell is given in table A.5.6.4.2.2-1 ~ A.5.6.4.2.2-3 below and applicability for the E-UTRAN cell are defined in A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI measurement resource and on 2 data symbols before. The CLI-RSSI measurement resource configuration is in table A.5.6.4.2.2-4.

Table A.5.6.4.2.2-1: General test parameters for CLI-RSSI event triggered reporting for PSCell in FR2

Table A.5.6.4.2.2-2: NR Cell specific test parameters for CLI-RSSI event triggered reporting for PSCell in FR2

Table A.5.6.4.2.2-3: NR OTA Cell specific test parameters for CLI-RSSI event triggered reporting for PSCell in FR2

Table A.5.6.4.2.2-4: CLI-RSSI measurement resource configuration for measurement reporting

## A.5.6.4.2.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 20 ms from the beginning of time period T2. The nominal RSSI used to evaluate the requirement shall be based on Io.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.5Measurements with autonomous gaps

## A.5.6.5.1 EN-DC inter-frequency CGI identification of NR neighbor cell in FR2

## A.5.6.5.1.1Test Purpose and Environment

This test is to verify the requirement for identification of a new CGI of NR cell with autonomous gaps in clause 9.11.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.5.6.5.1.1-1, A.5.6.5.1.1-2, and A.5.6.5.1.1-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 3 Starting T2, Cell 3 becomes detectable and the UE is expected to detect and send a measurement report with SSB index. In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. Gap pattern configuration with id #0 is configured before T2 begins to enable inter-frequency monitoring.

A RRC message implying SI reading with autonomous gap shall be sent to the UE during period T2, within 3 s after the UE has reported Event A3. The RRC message shall create a measurement report configuration with reportCGI and useAutonomousGaps-r16 setup. The start of T3 is the instant when the last TTI containing the RRC message implying SI reading is sent to the UE. Measurement gaps shall be deconfigured before the start of T3.

PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would have ACK/NACK sending during identifying a new CGI of NR cell.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.5.1.1-1.

Table A.5.6.5.1.1-1 Supported test configurations for EN-DC inter-frequency CGI identification of NR neighbor cell in FR2

Table A.5.6.5.1.1-2: General test parameters for EN-DC inter-frequency CGI identification of NR neighbor cell in FR2

Table A.5.6.5.1.1-3: Cell specific test parameters for EN-DC inter-frequency CGI identification of NR neighbor cell in FR2

Table A.5.6.5.1.1-4: OTA cell specific test parameters for EN-DC inter-frequency CGI identification of NR neighbor cell in FR2

## A.5.6.5.1.2Test Requirements

The UE shall transmit a measurement report containing the cell global identifier of Cell 3 within 660 milliseconds from the start of T3.

Test requirement = RRC Procedure delay + Tidentify_CGI + additional margin for FR2 + TTI insertion uncertainty

= 15 + (25*20 + 6*20) + 20 + 2 ms from the start of T3

= 657 ms, allow 660 ms.

The UE shall be scheduled continuously throughout the test, and from the start of T3 until 660 ms the number of interrupted slots shall not exceed the allowed number as defined in clause 8.2.1.2.16.

The maximum number of interrupted slots allowed is 25*48 + 6*49 = 1494.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.6L1-SINR measurement for beam reporting

A.5.6.6.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used

A.5.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.1, with the testing configurations for NR cells in table A.5.6.6.1.1-1.

Table A.5.6.6.1.1-1: Applicable NR configurations for FR2 CSI-RS based L1-SINR test

A.5.6.6.1.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.6.1.2-1 and table A.5.6.6.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1- SINR on aperiodic CSI-RS resources. After 480 ms from the beginning of the test, the DCI trigger comes in slot 8 of a frame and UE provides the report back based on the reporting configuration as defined in table A.5.6.6.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.5.6.6.1.2-1: General test parameters

Table A.5.6.6.1.2-2: CSI-RS specific test parameters

A.5.6.6.1.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.28.1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.6.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used

## A.5.6.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.2, with the testing configurations for NR cells in table A.5.6.6.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.5.6.6.2.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.5.6.6.2.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.6.2.2-1 and table A.5.6.6.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.5.6.6.2.2-1: General test parameters

Table A.5.6.6.2.2-2: SSB specific test parameters

Table A.5.6.6.2.2-3: CSI-RS specific test parameters

## A.5.6.6.2.3Test Requirements

The UE shall send L1-SINR report every 640 slots. No later than X ms plus 640 slots from the beginning of time period T2, UE shall send L1-SINR report including the results for both SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.28.2, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2, 3 or 4.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used

## A.5.6.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR cofigured in clause 9.8.4.3, with the testing configurations for NR cells in table A.5.6.6.3.1-1.

Table A.5.6.6.3.1-1: Applicable NR configurations for FR2 L1-SINR test with CMR and dedicated IMR

## A.5.6.6.3.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR2 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.6.6.3.2-1 and table A.5.6.6.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-IM as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources and the associated IMR. UE is also configured to measure L1-SINR based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 8 of a frame and UE provides the report back based on the reporting configuration as defined in table A.5.6.6.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-IM as IMR.

Table A.5.6.6.3.2-1: General test parameters

Table A.5.6.6.3.2-2: CSI-RS specific test parameters

## A.5.6.6.3.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 as CMR + CSI-IM#0 as IMR and CSI-RS#1 as CMR + CSI-IM#1 as IMR while meeting the accuracy requirements defined in clause 10.1.28.3. The reported L1-SINR value shall consider the Rx antenna gain in the range from -10 to +20 dB which is referred to Table B.2.1.5.1-1 when calculated.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.7CSI-RS based Intra-frequency Measurements

## A.5.6.7.1EN-DC event triggered reporting test without gap under non-DRX

## A.5.6.7.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification requirements in clause 9.10.2. Supported test configurations are shown in table A.5.6.7.1.1-1.

Table A.5.6.7.1.1-1: supported test configurations

There are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.6.7.1.1-2, A.5.6.7.1.1-3 and A.5.6.7.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.5.6.7.1.1-2: General test parameters for intra-frequency event triggered reporting for EN-DC with PSCell in FR2 without gap without DRX

Table A.5.6.7.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with PSCell in FR2 without gap without DRX

Table A.5.6.7.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for EN-DC with PSCell in FR2 without gap without DRX

## A.5.6.7.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3.2 s for a UE supporting power class 1,

-2.4 s for a UE supporting power class 2, 3 and 4

The UE is not required to read the neighbour cell SSB index in this test in order to detect associated SSB for the CSI-RS resource of Cell 3.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.6.8CSI-RS based Inter-frequency Measurements

## A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when DRX is used

## A.5.6.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.10.3.

In this test, there are three cells: LTE Cell 1 as PCell on E-UTRA RF channel 1, NR Cell 2 as PSCell in FR2 on NR RF channel 1 and NR Cell 3 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.5.6.8.1.1-1, A.5.6.8.1.1-2, and A.5.6.8.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.5.6.8.1.1-2 is provided for UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #13 as defined in table A. 5.6.5.1.1-2 is provided for UE that supports per-FR gap. If a UE supports per-FR gap and gap pattern configuration #13, it is only required to pass test2. Otherwise it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

The configuration of LTE Cell 1 is defined in table A.3.7.2.2-1. Supported test configurations are shown in table A.5.6.8.1.1-1.

Table A.5.6.8.1.1-1 EN-DC event triggered reporting tests for FR2-FR2

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.5.6.8.1.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection with DRX

Table A.5.6.8.1.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.5.6.8.1.2Test Requirements

In test 1 with per-UE gap and in test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 20160 ms for UE supporting power class 1, or

## 12480 ms for UE supporting other power class.

The UE is required to read the neighbour cell SSB index in this test in order to detect associated SSB for the CSI-RS resource of Cell 3.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.5.7Measurement Performance requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause 10 for at least 90 % of the reported cases.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.5.7.1SS-RSRP

## A.5.7.1.1EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.5.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3.1.1 and 10.1.3.1.2 for intra-frequency measurements.

## A.5.7.1.1.2Test parameters

In this set of test cases, all NR cells are on the same carrier frequency. Supported test configurations are shown in table A.5.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.5.7.1.1.2-2 and A.5.7.1.1.2-3. The E-UTRA PCell is configured as specified in clause A.3.7.2.2. In all test cases, Cell 1 is the PCell, Cell 2 is the PSCell and Cell 3 is the target cell. The test consists of two time phases T1 and T2.

Table A.5.7.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.5.7.1.1.2-2: SS-RSRP Intra frequency general test parameters

Table A.5.7.1.1.2-3: SS-RSRP Intra frequency OTA related test parameters

## A.5.7.1.1.3Test Requirements

The SS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.1.1 and relative accuracy requirements in clause 10.1.3.1.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.1.3-1.

Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

During T2:

Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.1.3-1.

Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

During T1 and T2:

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1

Relative accuracy of Cell 3 during T2 compared with Cell 3 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3.1.2-1.

Table A.5.7.1.1.3-1: SS-RSRP absolute accuracy test requirement

## A.5.7.1.2EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.5.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.1.1 and 10.1.5.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.5.7.1.2.1-1.

Table A.5.7.1.2.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

## A.5.7.1.2.2Test parameters

In this set of test cases, there are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.7.1.2.2-1 and table A.5.7.1.2.2-2 below. Both absolute and relative accuracy of RSRP intrer-frequency measurements are tested by using the parameters in table A.5.7.1.2.2-1 and table A.5.7.1.2.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.5.7.1.2.2-1: SS-RSRP inter-frequency test parameters

Table A.5.7.1.2.2-2: SS-RSRP inter frequency OTA related test parameters

## A.5.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the absolute requirements in clause 10.1.5.1.1 and the relative requirements in clause 10.1.5.1.2.

Test 1:

Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.2.3-1.

Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in A.5.7.1.2.3-2.

Test 2:

Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.2.3-1.

Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in A.5.7.1.2.3-2.

Table A.5.7.1.2.3-1: SS-RSRP absolute accuracy test requirement

Table A.5.7.1.2.3-2: SS-RSRP relative accuracy test requirement

## A.5.7.1.3EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell

## A.5.7.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.1.1 for inter-frequency measurements with the testing configurations in table A.5.7.1.3.1-1.

Table A.5.7.1.3.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

## A.5.7.1.3.2Test parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.7.1.3.2-1 and table A.5.7.1.3.2-2 below. Absolute accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.5.7.1.3.2-1 and table A.5.7.1.3.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.5.7.1.3.2-1: SS-RSRP inter-frequency test parameters

Table A.5.7.1.3.2-2: SS-RSRP inter-frequency OTA related test parameters

## A.5.7.1.3.3Test Requirements

The SS-RSRP measurement accuracy for Cell 3 shall fulfil the Absolute requirement in clause 10.1.5.1.1.

Test 1:

Absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.3.3.

Test 2:

Absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.5.7.1.3.3.

Table A.5.7.1.3.3: SS-RSRP absolute accuracy test requirement

## A.5.7.2SS-RSRQ

## A.5.7.2.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.8.1.1.

## A.5.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.5.7.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.5.7.2.1.2-2 and table A.5.7.2.1.2-3. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.5.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.5.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

Table A.5.7.2.1.2-3: SS-RSRQ Intra frequency OTA related test parameters

## A.5.7.2.1.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ -2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal SS-RSRQ +3.5 dB to Nominal SS-RSRQ -3.5 dB  according to the requirements in clause 10.1.8.1.1. Nominal SS-RSRQ is the value shown in table A.5.7.2.1.2-3.

## A.5.7.2.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2 for inter-frequency measurement.

## A.5.7.2.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.5.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test setup in table A.5.7.2.2.2-2 and table A.5.7.2.2.2-3. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.5.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.5.7.2.2.2-2: SS-RSRQ Inter frequency general test parameters

Table A.5.7.2.2.2-3: SS-RSRQ Inter frequency OTA related test parameters

## A.5.7.2.2.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SSRQ-2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal SS-RSRQ+3.5 dB to Nominal SS-RSRQ-3.5 dB  according to the requirements in clause 10.1.10.1.1.

The SS-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1.10.1.2.

## A.5.7.3SS-SINR

## A.5.7.3.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.13.1.1.

## A.5.7.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.5.7.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is test by using the parameters in table A.5.7.3.1.2-2 and table A.5.7.3.1.2-3. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.5.7.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.5.7.3.1.2-2: SS-SINR Intra frequency test parameters

Table A.5.7.3.1.2-3: SS-SINR Intra frequency OTA related test parameters

## A.5.7.3.1.3Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR+3B to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR +3.5 dB to Nominal SS-SINR -3.5 dB  according to the requirements in clause 10.1.10.13.1. Nominal SS-SINR is the value shown in table A.5.7.3.1.2-3.

## A.5.7.3.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.15.1.1 and 10.1.15.1.2 for inter-frequency measurement.

## A.5.7.3.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.5.7.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test setup in table A.5.7.3.2.2-2 and table A.5.7.3.2.2-3. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.5.7.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.5.7.3.2.2-2: SS-SINR Inter frequency general test parameters

Table A.5.7.3.2.2-3: SS-SINR Inter frequency OTA related test parameters

## A.5.7.3.2.3Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR+3 dB to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR+3.5 dB to Nominal SS-SINR -3.5 dB  according to the requirements in clause 10.1.15.1.1. Nominal SS-SINR is the value shown in table A.5.7.2.2.2-3

The SS-SINR relative measurement accuracy shall fulfil the requirements in clause 10.1.15.1.2.

## A.5.7.4L1-RSRP measurement for beam reporting

## A.5.7.4.1SSB based L1-RSRP measurement

## A.5.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.2 and clause 10.1.20.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.5.7.4.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.5.7.4.1.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.5.7.4.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.4.1.2-1 and table A.5.7.4.1.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.5.7.4.1.2-1 and table A.5.7.4.1.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.5.7.4.1.2-1: FR2 SSB based L1-RSRP general test parameters

Table A.5.7.4.1.2-2: FR2 SSB based L1-RSRP OTA related test parameters

## A.5.7.4.1.3Test Requirements

After 320 ms from the beginning of the test, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.20.1. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.7.4.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

For Test 2:

Absolute accuracy of SSB resource reported by UE in L1-RSRP report (SSB0 or SSB1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.7.4.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.1.2-1.

Table A.5.7.4.1.3-1: L1-RSRP absolute accuracy test requirement

## A.5.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.5.7.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause 10.1.20.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.5.7.4.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.5.7.4.2.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.5.7.4.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.4.2.2-1 and table A.5.7.4.2.2-2 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.5.7.4.2.2-1 and table A.5.7.4.2.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.5.7.4.2.2-1: FR2 CSI-RS based L1-RSRP general test parameters

Table A.5.7.4.2.2-2: FR2 CSI-RS based L1-RSRP OTA related test parameters

## A.5.7.4.2.3Test Requirements

After 320 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 2 shall fulfil the requirements in clauses 10.1.20.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.7.4.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

For Test 2:

Absolute accuracy of CSI-RS resource reported by UE in L1-RSRP report (CSI-RS0 or CSI-RS1). The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.5.7.4.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.5.7.4.2.3-1: L1-RSRP absolute accuracy test requirement

## A.5.7.5CLI measurements

## A.5.7.5.1EN-DC SRS-RSRP measurement accuracy with FR2 serving cell

## A.5.7.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the SRS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.1.1 with the testing configurations for NR cells in table A.5.7.5.1.1-1.

Table A.5.7.5.1.1-1: Applicable NR configurations for FR2 SRS-RSRP accuracy test

## A.5.7.5.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.5.1.2-1 and A.5.7.5.1.2-2 below. The test parameter for the (virtual) neighbor cell UE transmitting SRS are given in table A.5.7.5.1.2-2.

Before the test UE is configured to perform SRS-RSRP measurement. During the test, the test system transmits SRS resources for measurement in the DL slots according to the SRS configuration in table A.5.7.5.1.2-3. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 2 data symbols before SRS to be transmitted.

Table A.5.7.5.1.2-1: FR2 test parameters for SRS-RSRP accuracy

Table A.5.7.5.1.2-2: SRS-RSRP accuracy OTA related test parameters for PSCell and Neighbour cell UE in FR2

Table A.5.7.5.1.2-3: SRS configuration parameters for FR2 SRS-RSRP accuracy

## A.5.7.5.1.3Test Requirements

The SRS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.22.1.1. The following requirements are to be verified:

During Test 1:

The UE is deemed to meet the requirement if the reported SRS-RSRP is in the range shown in table A.5.7.5.1.3-1.

During Test 2:

The UE is deemed to meet the requirement if the reported SRS-RSRP is in the range shown in table A.5.7.5.1.3-1.

Table A.5.7.5.1.3-1: SRS-RSRP absolute accuracy test requirement

## A.5.7.5.2EN-DC CLI-RSSI measurement accuracy with FR2 serving cell

## A.5.7.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the CLI-RSSI measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.22.2.1 with the testing configurations for NR cells in table A.5.7.5.2.1-1.

Table A.5.7.5.2.1-1: Applicable NR configurations for FR2 CLI-RSSI accuracy test

## A.5.7.5.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.5.2.2-1 and A.5.7.5.2.2-2 below.

Before the test UE is configured to perform CLI-RSSI measurement. There is no measurement gap configured in the test. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI resource and on 2 data symbol before. The CLI-RSSI measurement resource configuration is in table A.5.7.5.2.2-3.

Table A.5.7.5.2.2-1: FR2 test parameters for CLI-RSSI accuracy

Table A.5.7.5.2.2-2: CLI-RSSI accuracy OTA related test parameters

Table A.5.7.5.2.2-3: CLI-RSSI measurement resource configuration for FR2 CLI-RSSI accuracy

## A.5.7.5.2.3Test Requirements

The CLI-RSSI measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.22.2.1. The following requirements are to be verified:

During Test 1:

The UE is deemed to meet the requirement if the reported CLI-RSSI is in the range shown in table A.5.7.5.2.3-1.

During Test 2:

The UE is deemed to meet the requirement if the reported CLI-RSSI is in the range shown in table A.5.7.5.2.3-1.

Table A.5.7.5.2.3-1: CLI-RSSI absolute accuracy test requirement

## A.5.7.6L1-SINR measurement for beam reporting

A.5.7.6.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

A.5.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.1 and clause 10.1.28.1 for FR2 L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.5.7.6.1.1-1, which configures the measurement resources for the CSI-RS based CMR and no dedicated IMR.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.5.7.6.1.1-1: Applicable NR configurations for FR2 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

A.5.7.6.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.6.1.2-1 and table A.5.7.6.1.2-2 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.5.7.6.1.2-1 and table A.5.7.6.1.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.5.7.6.1.2-1: FR2 CSI-RS based L1-SINR general test parameters

Table A.5.7.6.1.2-2: FR2 CSI-RS based L1-SINR OTA related test parameters

A.5.7.6.1.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 2 shall fulfil the requirements in clauses 10.1.28.1. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.5.7.6.1.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the reported differential L1-SINR meets is in the range shown in table A.5.7.6.1.3-2.

Table A.5.7.6.1.3-1: L1-SINR absolute accuracy test requirement

Table A.5.7.6.1.3-2: L1-SINR relative accuracy test requirement

## A.5.7.6.2L1-SINR measurement with SSB based CMR and dedicated IMR

## A.5.7.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.8.4.2 and clause 10.1.28.2 for L1-SINR measurements with SSB based CMR and dedicated CSI-RS based IMR, with the testing configurations for NR cells in table A.5.7.6.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.5.7.6.2.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.5.7.6.2.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.6.2.2-1 and table A.5.7.6.2.2-2 below. The absolute accuracy of L1-SINR measurements are tested by using the parameters in table A.5.7.6.2.2-1 and table A.5.7.6.2.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-RS resource set with two CSI-RS resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.5.7.6.2.2-1: FR2 L1-SINR measurement test parameters with SSB based CMR and CSI-RS based IMR

Table A.5.7.6.2.2-2: FR2 SSB specific test parameters

Table A.5.7.6.2.2-3: FR2 CSI-RS specific test parameters

## A.5.7.6.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 of Cell 2 shall fulfil the requirements in clauses 10.1.28.2. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB#0+CSI-RS#0. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.5.7.6.2.3-1.

Relative accuracy of SSB#0+CSI-RS#0 compared with SSB#1+CSI-RS#1. The UE is deemed to meet the requirement if the reported differential L1-SINR is in the range shown in table A.5.7.6.2.3-2.

Table A.5.7.6.2.3-1: L1-SINR absolute accuracy test requirement

Table A.5.7.6.2.3-2: L1-SINR relative accuracy test requirement

## A.5.7.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR

## A.5.7.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8.4.3 and clause 10.1.28.3 for L1-SINR measurements based on CSI-RS as CMR and CSI-IM as IMR with the testing configurations for NR cells in table A.5.7.6.3.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

Table A.5.7.6.3.1-1: Applicable NR configurations for FR2 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

## A.5.7.6.3.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 are given in table A.5.7.6.3.2-1 and A.5.7.6.3.2-2 below. The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.5.7.6.3.2-1 and A.5.7.6.3.2-2.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources and one CSI-IM resource set with two CSI-IM resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as CMR and CSI-IM as IMR.

Table A.5.7.6.3.2-1: FR2 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

Table A.5.7.6.3.2-2: FR2 CSI-RS based L1-SINR measurement OTA related test parameters

## A.5.7.6.3.3Test Requirements

After 640 ms from the beginning of the test, the L1-SINR measurement accuracy for CSI-RS#0+CSI-IM#0 and CSI-RS#1+CSI-IM#1 of Cell 2 shall fulfil the requirements in clauses 10.1.28.3. The following requirements are to be verified:

Absolute accuracy of CSI-RS#0+CSI-IM#0. The UE is deemed to meet the requirement if the reported L1-SINR is in the range shown in table A.5.7.6.3.3-1.

Relative accuracy of CSI-RS#0+CSI-IM#0 compared with CSI-RS#1+CSI-IM#1. The UE is deemed to meet the requirement if the reported differential L1-SINR is in the range shown in table A.5.7.6.3.3-2.

Table A.5.7.6.3.3-1: L1-SINR absolute accuracy test requirement

Table A.5.7.6.3.3-2: L1-SINR relative accuracy test requirement

## A.5.7.7CSI-RSRP

## A.5.7.7.1EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.5.7.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3.1.1 and 10.1.3.1.2 for intra-frequency measurements.

## A.5.7.7.1.2Test parameters

In this set of test cases, all NR cells are on the same carrier frequency. Supported test configurations are shown in table A.5.7.7.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.5.7.7.1.2-2 and A.5.7.7.1.2-3. The E-UTRA PCell is configured as specified in clause A.3.7.2.2. In all test cases, Cell 1 is the PCell, Cell 2 is the PSCell and Cell 3 is the target cell. The test consists of two time phases T1 and T2.

Table A.5.7.7.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.5.7.7.1.2-2: CSI-RSRP Intra frequency general test parameters

Table A.5.7.7.1.2-3: CSI-RSRP Intra frequency OTA related test parameters

## A.5.7.7.1.3Test Requirements

The CSI-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.1.1 and relative accuracy requirements in clause 10.1.3.1.2. The following requirements are to be verified:

During T1:

-Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.5.7.6.1.3-1.

-Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.1.2-1.

During T2:

-Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.5.7.6.1.3-1.

-Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.1.2-1.

During T1 and T2:

-Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported CSI-RSRP meets the requirements in table 10.1.3.1.2-1

-Relative accuracy of Cell 3 during T2 compared with Cell 3 during T1. The UE is deemed to meet the requirement if the difference in reported CSI -RSRP meets the requirements in table 10.1.3.1.2-1.

Table A.5.7.7.1.3-1: CSI-RSRP absolute accuracy test requirement

## A.5.7.7.2EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.5.7.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RS based RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.5.3.1 and 10.1.5.3.2 for inter-frequency measurements with the testing configurations for NR cells in table A.5.7.7.2.1-1.

Table A.5.7.7.2.1-1: Applicable NR configurations for FR2 inter-frequency CSI-RSRP accuracy test

## A.5.7.7.2.2Test parameters

In this set of test cases, there are three cells in the test, E-UTRAN PCell (Cell 1), FR2 PSCell (Cell 2) and a FR2 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.5.7.7.2.2-1 and table A.5.7.7.2.2-2 below. Both absolute and relative accuracy of RSRP intrer-frequency measurements are tested by using the parameters in table A.5.7.7.2.2-1 and table A.5.7.7.2.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.5.7.7.2.2-1: CSI-RSRP inter-frequency general test parameters

Table A.5.7.7.2.2-2: CSI-RSRP inter-frequency OTA related test parameters

## A.5.7.7.2.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the absolute requirements in clause 10.1.5.3.1 and the relative requirements in clause 10.1.5.3.2.

Test 1:

-Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported CSI-RSRP is in the range shown in table A.5.7.7.2.3-1.

-Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported CSI -RSRP meets the requirements in table A.5.7.7.2.3-2.

Test 2:

-Absolute accuracy of Cell 2 and absolute accuracy of Cell 3. The UE is deemed to meet the requirement if the reported CSI -RSRP is in the range shown in table A.5.7.7.2.3-1.

-Relative accuracy of Cell 3 compared with Cell 2. The UE is deemed to meet the requirement if the difference in reported CSI -RSRP meets the requirements in table A.5.7.7.2.3-2.

Table A.5.7.7.2.3-1: CSI-RSRP absolute accuracy test requirement

Table A.5.7.7.2.3-2: CSI-RSRP relative accuracy test requirement

## A.5.7.8CSI-RSRQ

## A.5.7.8.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell

## A.5.7.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.8 for inter-frequency measurement.

## A.5.7.8.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.5.7.8.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is test by using the parameters in table A.5.7.8.1.2-2. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1.

Table A.5.7.8.1.2-1: CSI-RSRQ Intra frequency CSI-RSRQ supported test configurations

Table A.5.7.8.1.2-2: CSI-RSRQ Intra frequency test parameters

Table A.5.7.8.1.2-3: CSI-RSRQ Intra frequency OTA related test parameters

## A.5.7.8.1.3Test Requirements

The CSI-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal CSI-RSRQ +2.5 dB to Nominal CSI-RSRQ –3.5 dB and the CSI-RSRQ measurement accuracy in test 2 shall be within the range Nominal CSI-RSRQ +3.5 dB to Nominal CSI-RSRQ –4.5 dB  according to the requirements in clause 10.1.8 with an additional -1 dB margin reflecting the possible impact of UE self-noise in the test. Nominal CSI-RSRQ is the value shown in table A.5.7.8.1.2-3.

## A.5.7.8.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.10 for inter-frequency measurement.

## A.5.7.8.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.5.7.8.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test setup in table A.5.7.8.2.2-2 and table A.5.7.8.2.2-3. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.5.7.8.2.2-1: CSI-RSRQ Inter frequency CSI-RSRQ supported test configurations

Table A.5.7.8.2.2-2: CSI-RSRQ Inter frequency general test parameters

Table A.5.7.8.2.2-3: CSI-RSRQ Inter frequency OTA related test parameters

## A.5.7.8.2.3Test Requirements

The CSI-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal CSI-RSRQ +2.5 dB to Nominal CSI-RSRQ -3.5 dB and the CSI-RSRQ measurement accuracy in test 2 shall be within the range Nominal CSI-RSRQ +3.5 dB to Nominal CSI-RSRQ -4.5 dB  according to the requirements in clause 10.1.10 with an additional -1 dB margin reflecting the possible impact of UE self-noise in the test.

The CSI-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1.10.

## A.5.7.9CSI-SINR

## A.5.7.9.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.13.2.1.

## A.5.7.9.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.5.7.9.1.2-1. The absolute accuracy of CSI-SINR intra-frequency measurement is test by using the parameters in table A.5.7.9.1.2-2 and table A.5.7.9.1.2-3. The configuration of Cell 1 (E-UTRA PCell) is specified in clause A.3.7.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.5.7.9.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

Table A.5.7.9.1.2-2: CSI-SINR Intra frequency test parameters

Table A.5.7.9.1.2-3: CSI-SINR Intra frequency OTA related test parameters

## A.5.7.9.1.3Test Requirements

The CSI-SINR absolute measurement accuracy in test 1 shall be within the range Nominal CSI-SINR+3 dB to Nominal CSI-SINR -4 dB and the CSI-SINR measurement accuracy in test 2 shall be within the range Nominal CSI-SINR +3.5 dB to Nominal CSI-SINR -4.5 dB  according to the requirements in clause 10.13.2 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test. Nominal CSI-SINR is the value shown in table A.5.7.9.1.2-3.

## A.5.7.9.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.5.7.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.15.2.1 and 10.1.15.2.2 for inter-frequency measurement.

## A.5.7.9.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.5.7.9.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test setup in table A.5.7.9.2.2-2 and table A.5.7.9.2.2-3. In all test cases, Cell 2 is the PSCell and Cell 3 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.5.7.9.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

Table A.5.7.9.2.2-2: CSI-SINR Inter frequency general test parameters

Table A.5.7.9.2.2-3: CSI-SINR Inter frequency OTA related test parameters

## A.5.7.9.2.3Test Requirements

The CSI-SINR absolute measurement accuracy in test 1 shall be within the range Nominal CSI-SINR+3 dB to Nominal CSI-SINR -4 dB and the CSI-SINR measurement accuracy in test 2 shall be within the range Nominal CSI-SINR+3.5 dB to Nominal CSI-SINR -4.5 dB according to the requirements in clause 10.1.15.2.1 with an additional -1 dB margin reflecting the possible impact of UE self noise in the test. Nominal CSI-SINR is the value shown in table A.5.7.2.2.2-3

The CSI-SINR relative measurement accuracy shall fulfil the requirements in clause 10.1.15.2.2.

## A.5.8Void
