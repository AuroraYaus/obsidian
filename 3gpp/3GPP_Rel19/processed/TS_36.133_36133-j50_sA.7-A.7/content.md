---
type: spec
aliases:
  - 36.133_36133-j50_sA.7-A.7
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.133_36133-j50_sA.7-A.7/content.md"
---
# TS 36.133 36133-j50_sA.7-A.7

## A.7Timing and Signalling Characteristics

## A.7.1UE Transmit Timing

## A.7.1.1E-UTRAN FDD – UE Transmit Timing Accuracy Tests

## A.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

For this test a single cell is used. Table A.7.1.1.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.1.1-2.

Table A.7.1.1.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD

Table A.7.1.1.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN FDD

Table A.7.1.1.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 4 for E-UTRAN FDD

## A.7.1.1.2Test Requirements

For parameters specified in Tables A.7.1.1.1-1 and A.7.1.1.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 4, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 4) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offset is within NTA×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 4.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 4 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

For the 1.4MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for non-DRX (Test 3):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +128TS (approximately +4µs) compared to that in (a).

c) The test system shall verify that the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offset is within NTA×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 24×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1.

## A.7.1.2E-UTRAN TDD - UE Transmit Timing Accuracy Tests

## A.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

For this test a single cell is used. Table A.7.1.2.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.2.1-2.

Table A.7.1.2.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD

Table A.7.1.2.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN TDD

Table A.7.1.2.1-3: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 4 for E-UTRAN TDD

## A.7.1.2.2Test Requirements

For parameters specified in Tables A.7.1.2.1-1 and A.7.1.2.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 4, respectively):

a)After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b)The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 4) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offset is within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for test 2 and test 4.

d) The test system shall verify that the UE transmit timing offset stays within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. For test 2 and test 4 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

For the 1.4MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for non-DRX (Test 3):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within (NTA +624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +128TS (approximately +4µs) compared to that in (a).

c) The test system shall verify that the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offset is within (NTA +624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

d) The test system shall verify that the UE transmit timing offset stays within (NTA +624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

## A.7.1.3E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell

## A.7.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. Both PCell and SCell are in the primary Timing Advance Group (pTAG). Table A.7.1.3.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.3.1-2.

Table A.7.1.3.1-1: General test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD

Table A.7.1.3.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN FDD

Table A.7.1.3.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD

## A.7.1.3.2Test Requirements

For parameters specified in Tables A.7.1.3.1-1, and A.7.1.3.1-2 the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test 1) and DRX with a cycle length of 80 ms or a cycle length of 640 mss(Test 2 and 3, respectively):

a)After the SCell (Cell 2) is activated, the test system shall verify that the UE transmit timing offsets of both PCell and SCell are within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of PCell (Cell 1).

b)The test system adjusts the downlink transmit timing for the PCell (Cell 1) by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c)The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offsets of both PCell and SCell are within NTA×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of PCell (Cell 1). Skip this step for Test 2 and Test 3.

d)The test system shall verify that the UE transmit timing offsets of both PCell and SCell stay within NTA×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of PCell (Cell 1). For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.4E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell

## A.7.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. Both PCell and SCell are in the primary Timing Advance Group (pTAG). Table A.7.1.4.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.4.1-2.

Table A.7.1.4.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD

Table A.7.1.4.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN TDD

Table A.7.1.4.1-3: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN TDD

## A.7.1.4.2Test Requirements

For parameters specified in Tables A.7.1.4.1-1 and A.7.1.4.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test 1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Test 2 and 3, respectively):

a)After the SCell (Cell 2) is activated, the test system shall verify that the UE transmit timing offsets of both PCell and SCell are within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of PCell (Cell 1).

b)The test system adjusts the downlink transmit timing for the PCell (Cell 1) by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.1.2 until the UE transmit timing offsets of both PCell and SCell are within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of PCell (Cell 1). Skip this step for test 2 and test 3.

d) The test system shall verify that the UE transmit timing offsets of both PCell and SCell stay within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of PCell (Cell 1). For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.4AE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell for 20 MHz + 10 MHz

## A.7.1.4A.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.1.4.1.

The parameters of this test are the same as defined in Subclause A.7.1.4.1 except that the values of the parameters in the Table A.7.1.4A.1-1 will replace the values of the corresponding parameters in A.7.1.4.1-1. Parameters used for the sounding reference symbol configuration and DRX configuration are unchanged from table A.7.1.4.1-2 and table A.7.1.4.1-3.

Table A.7.1.4A.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD for 20 MHz +10 MHz

## A.7.1.4A.2Test Requirements

The test requirements defined in section A.7.1.4.2 shall apply to this test case.

## A.7.1.5E-UTRAN FDD – UE Transmit Timing Accuracy Tests for 5MHz Bandwidth

## A.7.1.5.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.1.1.1.

The parameters of this test are the same as defined in Subclause A.7.1.1.1 except that the values of the parameters in Test 1 in the Table A.7.1.5.1-1 will replace the values of the corresponding parameters in A.7.1.1.1-1. Only Test 1 is defined for the 5MHz bandwidth.

Table A.7.1.5.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD for 5MHz bandwidth

## A.7.1.5.2Test Requirements

The test requirements defined in section A.7.1.1.2 shall apply to this test case.

## A.7.1.6E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell in sTAG

## A.7.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for SCell in sTAG. This test will verify the requirements in clause 7.1.2.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell is in the Primary Timing Advance Group (pTAG) and Scell is in the secondary Timing Advance Group (sTAG). Table A.7.1.6.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing for Scell in sTAG is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.6.1-2.

Table A.7.1.6.1-1: General test Parameters for UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN FDD

Table A.7.1.6.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN FDD

Table A.7.1.6.1-3: drx-Configuration to be used in Test 2 of UE Transmit Timing Accuracy for SCell in sTAG for E-UTRAN FDD

## A.7.1.6.2Test Requirements

For parameters specified in Tables A.7.1.6.1-1, and A.7.1.6.1-2 the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate for Scell in sTAG shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

For Test1 and Test2, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX and DRX with a cycle length of 80 ms:

a)After the SCell (Cell 2) is activated, the test system shall verify that the UE transmit timing offsets for SCell in sTAG are within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated Scell.

b)The test system adjusts the downlink transmit timing for the activated Scell (Cell 2) by +64TS (approximately +2µs) compared to that in (a).

c)The test system shall verify that for Test 1 the adjustment step size and the adjustment rate for Scell in sTAG shall be according to the requirements in clause 7.1.2 until the UE transmit timing offsets of SCell within NTA×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell (Cell 2). Skip this step for Test 2.

d)The test system shall verify that the UE transmit timing offsets of the SCell in sTAG stay within NTA×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of the activated SCell (Cell 2).

## A.7.1.7E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG

## A.7.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for SCell in sTAG. This test will verify the requirements in clause 7.1.2.

For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell is in the Primary Timing Advance Group (pTAG) and Scell is in the secondary Timing Advance Group (sTAG). Table A.7.1.7.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing for Scell in sTAG is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.7.1-2.

Table A.7.1.7.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN TDD

Table A.7.1.7.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN TDD

Table A.7.1.7.1-3: DRX Configuration to be used in Test 2 of UE Transmit Timing Accuracy for SCell in sTAG for E-UTRAN TDD

## A.7.1.7.2Test Requirements

For parameters specified in Tables A.7.1.7.1-1 and A.7.1.7.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate for Scell in sTAG shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

For Test 1 and Test 2, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX and DRX with a cycle length of 80 ms:

a)After the SCell (Cell 2) is activated, the test system shall verify that the UE transmit timing offsets for Scell in sTAG are within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell (Cell 2).

b)The test system adjusts the downlink transmit timing for the activated Scell (Cell 2) by +64TS (approximately +2µs) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate for Scell in sTAG shall be according to the requirements in clause 7.1.2 until the UE transmit timing offsets of SCell are within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell(Cell 2). Skip this step for test 2.

d) The test system shall verify that the UE transmit timing offsets of the SCell in sTAG stay within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated Scell (Cell 2).

## A.7.1.7AE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +20MHz

## A.7.1.7A.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.1.7. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.7.1.7B.1.1-1 will replace the values of corresponding parameters in Tables A.7.1.7.1-1.

Table A.7.1.7A.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN TDD with 20MHz +20MHz bandwidth

## A.7.1.7A.2Test Requirements

The test requirements defined in section A.7.1.7.2 shall apply to these test cases.

## A.7.1.7BE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +10MHz

## A.7.1.7B.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.1.7. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.7.1.7B.1-1 will replace the values of corresponding parameters in Tables A.7.1.7.1-1.

Table A.7.1.7B.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for Scell in sTAG for E-UTRAN TDD with 20MHz +10MHz bandwidth

## A.7.1.7B.2Test Requirements

The test requirements defined in section A.7.1.7.2 shall apply to these test cases.

## A.7.1.8Void

## A.7.1.8.1Void

Table A.7.1.8.1-1: Void

## A.7.1.8.2Void

## A.7.1.9Void

## A.7.1.9.1Void

Table A.7.1.9.1-1: Void

## A.7.1.9.2Void

## A.7.1.10E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA

## A.7.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

For this test a single cell is used. Table A.7.1.10.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.10.1-2.

Table A.7.1.10.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeA

Table A.7.1.10.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeA

Table A.7.1.10.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M1 UE under CEModeA

## A.7.1.10.2Test Requirements

For parameters specified in Tables A.7.1.10.1-1 and A.7.1.10.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 4, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within NTA×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 24×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.11E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA

## A.7.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

For this test a single cell is used. Table A.7.1.11.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.11.1-2.

Table A.7.1.11.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

Table A.7.1.11.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

Table A.7.1.11.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M1 UE under CEModeA

## A.7.1.11.2Test Requirements

For parameters specified in Tables A.7.1.11.1-1 and A.7.1.11.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 4, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within NTA×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 24×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.12E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA

## A.7.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

For this test a single cell is used. Table A.7.1.12.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.12.1-2.

Table A.7.1.12.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M1 UE under CEModeA

Table A.7.1.12.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M1 UE under CEModeA

Table A.7.1.12.1-3: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN TDD Cat-M1 UE under CEModeA

## A.7.1.12.2Test Requirements

For parameters specified in Tables A.7.1.12.1-1 and A.7.1.12.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 4, respectively):

a)After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within (NTA + 624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b)The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within (NTA + 624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for test 2 and test 3.

d) The test system shall verify that the UE transmit timing offset stays within (NTA + 624)×TS  ± 24×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.133DL/3UL TDD CA UE Transmit Timing Accuracy Tests for 2 SCells

## A.7.1.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for SCell in sTAG. This test will verify the requirements in clause 7.1.2.

For this test three cells are used. Cell 1 is PCell, Cell 2 is SCell1 and Cell 3 is SCell2. PCell is in the Primary Timing Advance Group (pTAG) and SCell1 and SCell2 are in the secondary Timing Advance Group (sTAG). Table A.7.1.13.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing for SCell1 and SCell2 in sTAG is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.13.1-2.

Table A.7.1.13.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for SCell1 and SCell2 in sTAG for 3DL/3UL TDD CAE-UTRAN TDD

Table A.7.1.13.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for SCell1 and SCell2 in sTAG for 3DL/3UL TDD CA

Table A.7.1.13.1-3: DRX Configuration to be used in Test 2 of UE Transmit Timing Accuracy for SCell1 and SCell2 in sTAG for  3DL/3UL TDD CA

## A.7.1.13.2Test Requirements

For parameters specified in Tables A.7.1.13.1-1, 7.1.8.1-2 and A.7.1.13.1-3, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate for Scell1 and SCell2 in sTAG shall be within the limits defined in clause 7.1.2.

The following sequence of events shall be used to verify that the requirements are met.

For Test 1 and Test 2, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX and DRX with a cycle length of 80 ms:

a)After the SCell1 (Cell 2) and SCell2 (Cell3) are activated, the test system shall verify that the UE transmit timing offsets for SCell1 and SCell2 in sTAG are within (NTA + 624) ×TS ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell1 (Cell 2) or SCell2 (Cell3).

b)The test system adjusts the downlink transmit timing for the activated SCell1 (Cell 2) and SCell2 (Cell3) by +64TS (approximately +2µs) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate for SCell1 and SCell2 in sTAG shall be according to the requirements in clause 7.1.2 until the UE transmit timing offsets of SCell1 and SCell2 are within (NTA + 624) ×TS ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell1 (Cell 2) or SCell2 (Cell3). Skip this step for test 2.

d) The test system shall verify that the UE transmit timing offsets of the SCell1 and SCell2 in sTAG stay within (NTA + 624) ×TS ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of the activated SCell1 (Cell 2) or SCell2 (Cell3).

## A.7.1.14E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB

## A.7.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

As specified in Clause 7.24.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions.  By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.14.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.14.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M1 UE under CEModeB

Table A.7.1.14.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M1 UE under CEModeB

## A.7.1.14.2Test Requirements

For parameters specified in Tables A.7.1.14.1-1 and A.7.1.14.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within NTA×TS  ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 48×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.15E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB

## A.7.1.15.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

As specified in Clause 7.24.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions. By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.15.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.15.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M1 UE under CEModeB

Table A.7.1.15.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M1 UE under CEModeB

## A.7.1.15.2Test Requirements

For parameters specified in Tables A.7.1.15.1-1 and A.7.1.15.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within NTA×TS  ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 48×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.16E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB

## A.7.1.16.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M1 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.24.2.

As specified in Clause 7.24.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions.  By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.16.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.16.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M1 UE under CEModeB

Table A.7.1.16.1-2: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN TDD Cat-M1 UE under CEModeB

## A.7.1.16.2Test Requirements

For parameters specified in Tables A.7.1.16.1-1 and A.7.1.16.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.24.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.24.2 until the UE transmit timing offset is within NTA×TS  ± 48×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 48×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.17E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage

## A.7.1.17.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under normal coverage is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.20.

For this test a single NB-IoT cell and a single LTE cell are used. Test parameters are given in Table A.7.1.17.1-1, Table A.7.1.17.1-2, and Table A.7.1.17.1-3. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.7.1.17.1-1: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under normal coverage

Table A.7.1.17.1-2: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under normal coverage

Table A.7.1.17.1-3: eCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under normal coverage

## A.7.1.17.2Test Requirements

For parameters specified in Tables A.7.1.17.1-1, A.7.1.17.1-2, and A.7.1.17.1-3, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.20.2.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED:

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤ NTA×TS   ± 80×TS) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.

b) Using the value of n measured in a), the test system adjusts the downlink transmit timing for the cell:

-if n < 0, by +(144 – |n|)TS compared to that in (a).

-if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c) Immediately after (b), the test system sends NPDCCH including uplink grant for NPUSCH transmission and immediately after receiving NPUSCH the test system repeatedly sends NPDCCH including uplink grant for NPUSCH transmission until the UE transmit timing offset is within NTA×TS  ± 80×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. The test system shall verify that the difference in timing between the first NPUSCH transmission in step c) and the NPUSCH transmission in step a) shall be not greater than the maximum amount of the magnitude of the timing change in one adjustment requirement in clause 7.20.2. Using the first NPUSCH transmission in step c) and subsequent NPUSCH transmissions. The test system shall verify that the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.20.2 until the UE transmit timing offset is within NTA×TS  ± 80×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

d) The test system the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within NTA×TS  ± 80×TS with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1.

## A.7.1.18E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage

## A.7.1.18.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under enhanced coverage is capable of following the frame timing change of the connected eNode B, that the UE initial transmit timing accuracy is within the specified limits and that the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission. This test will verify the requirements in clause 7.20.

For this test a single NB-IoT cell and a single LTE cell are used. Test parameters are given in Table A.7.1.18.1-1, Table A.7.1.18.1-2, Table A.7.1.18.1-3, and Table A.7.1.18.1-4. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.7.1.18.1-1: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.18.1-2: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.18.1-3: eCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.18.1-4: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 for E-UTRAN HD-FDD Category NB1 UE In-band mode under enhanced coverage

## A.7.1.18.2Test Requirements

For parameters specified in Tables A.7.1.18.1-1, Tables A.7.1.18.1-2, Tables A.7.1.18.1-3 and Tables A.7.1.18.1-4, the initial transmit timing accuracy shall be within the limits defined in clause 7.20.2 and the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 2048 ms (Tests 2):

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤NTA×TS   ± 80×TS) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.

b) The test system sends NPDCCH including uplink grant for NPUSCH transmission. After 16ms from the initial NPUSCH transmission, the test system adjusts the downlink transmit timing for the cell, using the value of n measured in a),

- if n < 0, by +(144 – |n|)TS compared to that in (a).

- if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c)For test 2, the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within NTA×TS  ± 80×TS with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1. The UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.19E-UTRAN FDD - UE Transmit Timing Accuracy Test for RACH-less Handover

## A.7.1.19.1Test Purpose and Environment

This test is to verify the requirement for the UE initial transmit timing after RACH-less handover specified in clause 7.1.

The test scenario comprises of 1 E-UTRA FDD carrier and 2 cells as given in tables A.7.1.19.1-1 and A.7.1.19.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

A RRC message implying RACH-less handover with targetTa = ta0 shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1. T3 is defined as the end of the last TTI containing the RRC message implying handover.

The transmit timing is verified by the PUSCH transmited by the UE

Table A.7.1.19.1-1: General test parameters for E-UTRAN FDD - UE Transmit Timing Accuracy Test for RACH-less Handover

Table A.7.1.19.1-2: Cell specific test parameters for E-UTRAN FDD - UE Transmit Timing Accuracy Test for RACH-less Handover

## A.7.1.19.2Test Requirements

When first PUSCH is transmitted to cell2, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 2.

## A.7.1.20E-UTRAN TDD - UE Transmit Timing Accuracy Test for RACH-less Handover

## A.7.1.20.1Test Purpose and Environment

This test is to verify the requirement for the UE initial transmit timing after RACH-less handover specified in clause 7.1.

The test scenario comprises of 1 E-UTRA TDD carrier and 2 cells as given in tables A.7.1.20.1-1 and A.7.1.20.1-2. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

A RRC message implying RACH-less handover with targetTa = ta0 shall be sent to the UE during period T2, after the UE has reported Event A3, and the PUSCH transmission in the cell2 is configured in the RRC message from cell1. T3 is defined as the end of the last TTI containing the RRC message implying handover.

The transmit timing is verified by the PUSCH transmited by the UE

Table A.7.1.20.1-1: General test parameters for E-UTRAN TDD - UE Transmit Timing Accuracy Test for RACH-less Handover

Table A.7.1.20.1-2: Cell specific test parameters for E-UTRAN TDD - UE Transmit Timing Accuracy Test for RACH-less Handover

## A.7.1.20.2Test Requirements

When first PUSCH is transmitted to cell2, the test system shall verify that the UE transmit timing offset is within (NTA + 624)×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 2.

## A.7.1.21E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA

## A.7.1.21.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M2 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

For this test a single cell is used. Table A.7.1.21.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.21.1-2.

Table A.7.1.21.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M2 UE under CEModeA

Table A.7.1.21.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M2 UE under CEModeA

Table A.7.1.21.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M2 UE under CEModeA

## A.7.1.21.2Test Requirements

For parameters specified in Tables A.7.1.21.1-1 and A.7.1.21.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within NTA×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.22E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA

## A.7.1.22.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M2 UE in CEModeA is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

For this test a single cell is used. Table A.7.1.22.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.22.1-2.

Table A.7.1.22.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M2 UE under CEModeA

Table A.7.1.22.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M2 UE under CEModeA

Table A.7.1.22.1-3: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M2 UE under CEModeA

## A.7.1.22.2Test Requirements

For parameters specified in Tables A.7.1.22.1-1 and A.7.1.22.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within NTA×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.23E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA

## A.7.1.23.1Test Purpose and Environment

The purpose of this test is to verify that the UE is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

For this test a single cell is used. Table A.7.1.23.1-1 defines the strength of the transmitted signals and the propagation condition. The transmit timing is verified by the UE transmitting SRS using the configuration defined in Table A.7.1.23.1-2.

Table A.7.1.23.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M2 UE under CEModeA

Table A.7.1.23.1-2: Sounding Reference Symbol Configuration to be used in UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M2 UE under CEModeA

Table A.7.1.23.1-3: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN TDD Cat-M2 UE under CEModeA

## A.7.1.23.2Test Requirements

For parameters specified in Tables A.7.1.23.1-1 and A.7.1.23.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a)After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b)The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for test 2 and test 3.

d) The test system shall verify that the UE transmit timing offset stays within (NTA + 624)×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.24E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB

## A.7.1.24.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M2 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

As specified in Clause 7.26.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions.  By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.24.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.24.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN FDD Cat-M2 UE under CEModeB

Table A.7.1.24.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN FDD Cat-M2 UE under CEModeB

## A.7.1.24.2Test Requirements

For parameters specified in Tables A.7.1.24.1-1 and A.7.1.24.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within NTA×TS  ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 40×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.25E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB

## A.7.1.25.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M2 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

As specified in Clause 7.26.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions. By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.25.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.25.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN HD-FDD Cat-M2 UE under CEModeB

Table A.7.1.25.1-2: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN HD-FDD Cat-M2 UE under CEModeB

## A.7.1.25.2Test Requirements

For parameters specified in Tables A.7.1.25.1-1 and A.7.1.25.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within NTA×TS  ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 40×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.26E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB

## A.7.1.26.1Test Purpose and Environment

The purpose of this test is to verify that the Cat-M2 UE in CEModeB is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.26.2.

As specified in Clause 7.26.2 the UE adjusts its uplink timing at the end of of repetition period when configured with repetitions.  By measuring the reception of the PUSCH, the transmit timing accuracy can be measured and the requirements can be verified. For this test a single cell is used. Table A.7.1.26.1-1 defines the strength of the transmitted signals and the propagation condition.

Table A.7.1.26.1-1: Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Cat-M2 UE under CEModeB

Table A.7.1.26.1-2: DRX Configuration to be used in UE Transmit Timing Accuracy Test 2 and Test 3 for E-UTRAN TDD Cat-M2 UE under CEModeB

## A.7.1.26.2Test Requirements

For parameters specified in Tables A.7.1.26.1-1 and A.7.1.26.1-2, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.26.2. The UE shall not adjust the the transmission timing autonomously during an ongoing repetition period. Adjustments can only be done at the end of a last subframe in a repetition period.

The following sequence of events shall be used to verify that the requirements are met.

For the 10MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 80 ms or a cycle length of 640 ms (Tests 2 and 3, respectively):

a) After a connection is set up with the cell, the test system shall verify that the UE transmit timing offset is within NTA×TS   ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +64TS (for Test 1 and Test 2) or +32TS (for Test 3) compared to that in (a).

c) The test system shall verify that for Test 1 the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.26.2 until the UE transmit timing offset is within NTA×TS  ± 40×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. Skip this step for Test 2 and Test 3.

d) The test system shall verify that the UE transmit timing offset stays within NTA×TS  ± 40×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1. For test 2 and test 3 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.1.27E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage

## A.7.1.27.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under normal coverage is capable of following the frame timing change of the connected eNode B and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.20.

For this test a single NB-IoT cell and a single LTE cell are used. Test parameters are given in Table A.7.1.27.1-1, Table A.7.1.27.1-2, and Table A.7.1.27.1-3. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.7.1.27.1-1: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under normal coverage

Table A.7.1.27.1-2: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under normal coverage

Table A.7.1.27.1-3: eCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under normal coverage

## A.7.1.27.2Test Requirements

For parameters specified in Tables A.7.1.27.1-1, A.7.1.27.1-2, and A.7.1.27.1-3, the initial transmit timing accuracy, the maximum amount of timing change in one adjustment, the minimum and the maximum adjustment rate shall be within the limits defined in clause 7.20.2.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED:

a) After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤ NTA×TS   ± 80×TS) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.

b) Using the value of n measured in a), the test system adjusts the downlink transmit timing for the cell:

-if n < 0, by +(144 – |n|)TS compared to that in (a).

-if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c) Immediately after (b), the test system sends NPDCCH including uplink grant for NPUSCH transmission and immediately after receiving NPUSCH the test system repeatedly sends NPDCCH including uplink grant for NPUSCH transmission until the UE transmit timing offset is within NTA×TS  ± 80×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1. The test system shall verify that the difference in timing between the first NPUSCH transmission in step c) and the NPUSCH transmission in step a) shall be not greater than the maximum amount of the magnitude of the timing change in one adjustment requirement in clause 7.20.2. Using the first NPUSCH transmission in step c) and subsequent NPUSCH transmissions. The test system shall verify that the adjustment step size and the adjustment rate shall be according to the requirements in clause 7.20.2 until the UE transmit timing offset is within NTA×TS  ± 80×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

d) The test system the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within NTA×TS  ± 80×TS with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1.

## A.7.1.28E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage

## A.7.1.28.1Test Purpose and Environment

The purpose of this test is to verify that the Category NB1 UE under enhanced coverage is capable of following the frame timing change of the connected eNode B, that the UE initial transmit timing accuracy is within the specified limits and that the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission. This test will verify the requirements in clause 7.20.

For this test a single NB-IoT cell and a single LTE cell are used. Test parameters are given in Table A.7.1.28.1-1, Table A.7.1.28.1-2, Table A.7.1.28.1-3, and Table A.7.1.28.1-4. The transmit timing is verified by the UE transmitting NPUSCH.

Table A.7.1.28.1-1: General Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.28.1-2: nCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.28.1-3: eCell specific Test Parameters for UE Transmit Timing Accuracy Tests for E-UTRAN TDD Category NB1 UE in In-Band mode under enhanced coverage

Table A.7.1.28.1-4: drx-Configuration to be used in UE Transmit Timing Accuracy Test 2 for E-UTRAN TDD Category NB1 UE In-band mode under enhanced coverage

## A.7.1.28.2Test Requirements

For parameters specified in Tables A.7.1.28.1-1, Tables A.7.1.28.1-2, Tables A.7.1.28.1-3 and Tables A.7.1.28.1-4, the initial transmit timing accuracy shall be within the limits defined in clause 7.20.2 and the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period other than at initial transmission.

The following sequence of events shall be used to verify that the requirements are met.

The test sequence shall be carried out in RRC_CONNECTED for both non-DRX (for Test1) and DRX with a cycle length of 2048 ms (Tests 2):

a)After a connection is set up with the cell, the test system sends NPDCCH including uplink grant for NPUSCH transmission and the test system shall measure the UE transmit timing offset (nTs) and verify that it is within Te (nTs ≤NTA×TS   ± 80×TS) with respect to the first detected path (in time) of the corresponding downlink frame of NB-IoT cell 1.

b)The test system sends NPDCCH including uplink grant for NPUSCH transmission. After 16ms from the initial NPUSCH transmission, the test system adjusts the downlink transmit timing for the cell, using the value of n measured in a),

-if n < 0, by +(144 – |n|)TS compared to that in (a).

-if n ≥ 0, by -(144 – |n|)TS compared to that in (a).

The timing adjustment is performed monotonically in multiple steps of |∆T| ≤ 9×TS per 256 ms (∆T is to be defined in the test procedure) until the above required total timing change is achieved, during which no grant is transmitted for the UE.

c)For test 2, the test system sends NPDCCH including uplink grant for NPUSCH transmission and shall verify that the UE transmit timing offset stays within NTA×TS  ± 80×TS with respect to the first detected path  (in time) of the corresponding downlink frame of NB-IoT cell 1. The UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.2UE Timing Advance

## A.7.2.1E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test

## A.7.2.1.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.1.1-1, A.7.2.1.1-2, and A.7.2.1.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.1.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.1.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.1.1-1: General Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test

Table A.7.2.1.1-2: Cell specific Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test

Table A.7.2.1.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD Transmit Timing Accuracy Test

## A.7.2.1.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.2E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test

## A.7.2.2.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN TDD Timing Advance adjustment accuracy requirements, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.2.1-1, A.7.2.2.1-2, and A.7.2.2.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.2.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.1.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.2.1-1: General Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test

Table A.7.2.2.1-2: Cell specific Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test

Table A.7.2.2.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD Transmit Timing Accuracy Test

## A.7.2.2.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.3E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for 5MHz

## A.7.2.3.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.2.1.1.

The parameters of this test are the same as defined in Subclause A.7.2.1.1 except that the values of the parameters in the Table A.7.2.3.1-1 will replace the values of the corresponding parameters in A.7.2.1.1-1, table A.7.2.3.1-2 will replace the values of the corresponding parameters in A.7.2.1.1-2. Parameters used for the sounding reference symbol configuration are unchanged from table A.7.2.1.1-3.

Table A.7.2.3.1-1: General Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for 5MHz bandwidth

Table A.7.2.3.1-2: Cell specific Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for 5MHz bandwidth

## A.7.2.3.2Test Requirements

The test requirements defined in section A.7.2.1.2 shall apply to this test case.

## A.7.2.4E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for SCell in sTAG

## A.7.2.4.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.4.1-1, A.7.2.4.1-2, and A.7.2.4.1-3. For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell is in the primary Timing Advance Group (pTAG) and SCell is in the secondary Timing Advance Group (sTAG). The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.4.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for SCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.7.2.4.1-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.4.1-1: General Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for SCell in sTAG

Table A.7.2.4.1-2: Cell specific Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for SCell in sTAG

Table A.7.2.4.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD Transmit Timing Accuracy Test for SCell in sTAG

## A.7.2.4.2Test Requirements

The UE shall apply the signalled Timing Advance value for SCell in sTAG to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy for SCell in STAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.5E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG

## A.7.2.5.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN TDD Timing Advance adjustment accuracy requirements, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.5.1-1, A.7.2.5.1-2, and A.7.2.5.1-3. For this test two cells are used. Cell 1 is PCell and Cell 2 is SCell. PCell is in the primary Timing Advance Group (pTAG) and SCell is in the secondary Timing Advance Group (sTAG). The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.5.1-3, are sent from the UE and received by the test equipment, but only for SCell. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for SCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.7.2.5.1-2. This value shall result in changes of the timing advance on SCell used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.5.1-1: General Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG

Table A.7.2.5.1-2: Cell specific Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG

Table A.7.2.5.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD Transmit Timing Accuracy Test for SCell in sTAG

## A.7.2.5.2Test Requirements

The UE shall apply the signalled Timing Advance value for SCell in sTAG to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy for SCell in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.5AE-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +20 MHz

## A.7.2.5A.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.2.5.1.

The parameters of this test are the same as defined in Subclause A.7.2.5.1 except that the values of the parameters in the Table A.7.2.5A.1-1 will replace the values of the corresponding parameters in A.7.2.5.1-1, table A.7.2.5A.1-2 will replace the values of the corresponding parameters in A.7.2.5.1-2. Parameters used for the sounding reference symbol configuration are unchanged from table A.7.2.5.1-3.

Table A.7.2.5A.1-1: General Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG for 20 MHz +20 MHz

Table A.7.2.5A.1-2: Cell specific Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG for 20 MHz +20 MHz

## A.7.2.5A.2Test Requirements

The test requirements defined in section A.7.2.5.2 shall apply to this test case.

## A.7.2.5BE-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +10 MHz

## A.7.2.5B.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.2.5.1.

The parameters of this test are the same as defined in Subclause A.7.2.5.1 except that the values of the parameters in the Table A.7.2.5B.1-1 will replace the values of the corresponding parameters in A.7.2.5.1-1, table A.7.2.5B.1-2 will replace the values of the corresponding parameters in A.7.2.5.1-2. Parameters used for the sounding reference symbol configuration are unchanged from table A.7.2.5.1-3.

Table A.7.2.5B.1-1: General Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG for 20 MHz +10 MHz

Table A.7.2.5B.1-2: Cell specific Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for SCell in sTAG for 20 MHz +10 MHz

## A.7.2.5B.2Test Requirements

The test requirements defined in section A.7.2.5.2 shall apply to this test case.

## A.7.2.6E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.6.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeA, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.6.1-1, A.7.2.6.1-2, and A.7.2.6.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.1.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.6.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.6.1-1: General Test Parameters for E-UTRAN FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.6.1-2: Cell specific Test Parameters for E-UTRAN FDD UE Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.6.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD UE Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.6.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.7E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.7.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN HD-FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeA, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.7.1-1, A.7.2.7.1-2, and A.7.2.7.1-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.7.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.7.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.7.1-1: General Test Parameters for E-UTRAN HD-FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.7.1-2: Cell specific Test Parameters for E-UTRAN HD-FDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.7.1-3: Sounding Reference Symbol Configuration for E-UTRAN HD-FDD Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.7.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.8E-UTRAN TDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.8.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN TDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeA, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.8.1-1, A.7.2.8.1-2, and A.7.2.8-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.8.1-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.8.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.8.1-1: General Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.8.1-2: Cell specific Test Parameters for E-UTRAN TDD Timing Advance Accuracy Test for Cat-M1 UE in CEModeA

Table A.7.2.8.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD Transmit Timing Accuracy Test for Cat-M1 UE in CEModeA

## A.7.2.8.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

A.7.2.9HD-FDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhance Coverage

A.7.2.9.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN Timing Advance adjustment accuracy requirements for UE category NB1 in enhanced coverage, defined in clause 7.22.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.9.1-1 and A.7.2.9.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and the UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 16.1.2 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.9.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the NPUSCH sent from the UE.

As specified in Clause 7.22.2.1, the UE adjusts its uplink timing at sub-frame n+12 for a timing advance command received in sub-frame n, where sub-frame n refers to the last subframe in the repetition period in which the MAC control element containing timing advance command was received. In addition, the UE shall not apply a TA command during an uplink repetition period. The timing advance adjustment accuracy is verified via the uplink transmission of NPUSCH carrying ACK/NACK response to the NPDSCH carrying TA command. k0 in ACK/NACK resource filed in DCI is set as 13.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.9.1-1: General Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage

Table A.7.2.9.1-2: Cell specific Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage

## A.7.2.9.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at subframe n+12, where subframe n is the last subframe in the repetition period of NPDSCH in which the timing advance command is received by the UE.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.22.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.10E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.10.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeB, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.10.1-1and A.7.2.10.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and PUSCH are sent from the UE and received by the test equipment. By measuring the reception of the PUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.10.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using PUSCH sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via PUSCH sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.10.1-1: General Test Parameters for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.7.2.10.1-2: Cell specific Test Parameters for E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.10.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 subframes after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

When a repetition period is configured on the uplink, the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period for which R>1.

## A.7.2.11E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.11.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN HD-FDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeB, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.11.1-1and A.7.2.11.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and PUSCH are sent from the UE and received by the test equipment. By measuring the reception of the PUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.11.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using PUSCH sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via PUSCH sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.11.1-1: General Test Parameters for E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.7.2.11.1-2: Cell specific Test Parameters for E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.11.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

When a repetition period is configured on the uplink, the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period for which R>1.

## A.7.2.12E-UTRAN TDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.12.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN TDD Timing Advance adjustment accuracy requirements for Cat-M1 UE configured with CEModeB, defined in clause 7.3.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.12.1-1and A.7.2.12.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and PUSCH are sent from the UE and received by the test equipment. By measuring the reception of the PUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321. The Timing Advance Command value shall be set to 31, which according to Clause 4.2.3 in TS 36.213 results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.12.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using PUSCH sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at sub-frame n+6 for a timing advance command received in sub-frame n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via PUSCH sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.12.1-1: General Test Parameters for E-UTRAN TDD UE Timing Advance Adjustment Accuracy Test in CEModeB

Table A.7.2.12.1-2: Cell specific Test Parameters for E-UTRAN TDD UE Timing Advance Adjustment Accuracy Test in CEModeB

## A.7.2.12.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 6 sub frames after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

When a repetition period is configured on the uplink, the UE shall not adjust the uplink transmission timing autonomously during an ongoing repetition period for which R>1.

## A.7.2.13E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

## A.7.2.13.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN FDD Timing Advance adjustment delay requirements when ShortTTI-r15 is configured or ShortProcessingTime=TRUE, defined in clause 7.3.2.2, in an AWGN model.

The test consists of 4 tests.The test parameters are given in tables A.7.2.13.1-1, A.7.2.13.1-2, and A.7.2.13.1-3. In each test, timing advance command is sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.13.1-3, is sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment delay can be measured.The test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.13.1-2.

In test 1, when ShortTTI-r15 is not configured and ShortProcessingTime=TRUE , the UE adjusts its uplink timing at sub-frame n+5 for a timing advance command received in sub-frame n. In test 2, when dl-STTI-Length-r15=slot, the UE adjusts its uplink timing at the first subframe boundary following n+8 slot for a timing advance command received in slot n. In test 3, when dl-STTI-Length-r15=subslot and proc-Timeline-r15= nplus4set1, the UE adjusts its uplink timing at the first subframe boundary following n+16 subslot for a timing advance command received in subslot n. In test 4, when dl-STTI-Length-r15=subslot and proc-Timeline-r15= nplus6set1 or

proc-Timeline-r15= nplus6set2, the UE adjusts its uplink timing at the first subframe boundary following n+18 subslot for a timing advance command received in subslot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.13.1-1: General Test Parameters for E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

Table A.7.2.13.1-2: Cell specific Test Parameters E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE (test1, test 2, test 3 and test 4)

Table A.7.2.13.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

## A.7.2.13.2Test Requirements

In test 1, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 5 sub frames after the reception of the timing advance command in sub-frame n.

In test 2, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. at the first subframe boundary following 8 slots after the reception of the timing advance command in slot n.

In test 3, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. at the first subframe boundary following 16 subslots after the reception of the timing advance command in subslot n.

In test 4, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. at the first subframe boundary following 18 subslots after the reception of the timing advance command in subslot n.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.14E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

## A.7.2.14.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN TDD Timing Advance adjustment delay requirements when ShortTTI-r15 is configured or ShortProcessingTime=TRUE, defined in clause 7.3.2.2, in an AWGN model.

The test consists of 2 tests.The test parameters are given in tables A.7.2.14.1-1, A.7.2.14.1-2, and A.7.2.14.1-3. In each test, timing advance command is sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.2.14.1-3, is sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment delay can be measured.The test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.14.1-2.

In test 1, when ShortTTI-r15 is not configured and ShortProcessingTime=TRUE , the UE adjusts its uplink timing at sub-frame n+5 for a timing advance command received in sub-frame n. In test 2, when dl-STTI-Length-r15=slot, the UE adjusts its uplink timing at the first subframe boundary following n+8 slot for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321, shall be configured so that it does not expire in the duration of the test.

Table A.7.2.14.1-1: General Test Parameters for E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

Table A.7.2.14.1-2: Cell specific Test Parameters E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE (test1 and test 2)

Table A.7.2.14.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE

## A.7.2.14.2Test Requirements

In test 1, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. 5 sub frames after the reception of the timing advance command in sub-frame n.

In test 2, the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. at the first subframe boundary following 8 slots after the reception of the timing advance command in slot n.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.2.15E-UTRAN TDD – TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage

## A.7.2.15.1Test Purpose and Environment

The purpose of the test is to verify E-UTRAN Timing Advance adjustment accuracy requirements for UE category NB1 in enhanced coverage, defined in clause 7.22.2.2, in an AWGN model.

The test parameters are given in tables A.7.2.15.1-1 and A.7.2.15.1-2. The test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and the UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in Clause 6.1.3.5 in TS 36.321 [17]. The Timing Advance Command value shall be set to 31, which according to Clause 16.1.2 in TS 36.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.2.15.1-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the NPUSCH sent from the UE.

As specified in Clause 7.22.2.1, the UE adjusts its uplink timing at sub-frame n+12 for a timing advance command received in sub-frame n, where sub-frame n refers to the last subframe in the repetition period in which the MAC control element containing timing advance command was received. In addition, the UE shall not apply a TA command during an uplink repetition period. The timing advance adjustment accuracy is verified via the uplink transmission of NPUSCH carrying ACK/NACK response to the NPDSCH carrying TA command. k0 in ACK/NACK resource filed in DCI is set as 13 or larger to to refer to the first UL subframe after n+12.

The UE Time Alignment Timer, described in Clause 5.2 in TS 36.321 [17], shall be configured so that it does not expire in the duration of the test.

Table A.7.2.15.1-1: General Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage

Table A.7.2.15.1-2: Cell specific Test Parameters for E-UTRAN Timing Advance Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage

## A.7.2.15.2Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at subframe n+12, where subframe n is the last subframe in the repetition period of NPDSCH in which the timing advance command is received by the UE.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.22.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.7.3Radio Link Monitoring

In the following section, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 36.101 [5]) means uplink signal

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 36.101 [5]) means no uplink signal.

## A.7.3.1E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync

## A.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.1.1-1, A.7.3.1.1-2 and A.7.3.1.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Table A.7.3.1.1-1: General test parameters for E-UTRAN FDD out-of-sync testing

Table A.7.3.1.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for out-of-sync radio link monitoring tests # 1 and # 2

Table A.7.3.1.1-3: Cell specific test parameters for E-UTRAN FDD (cell # 1) for out-of-sync radio link monitoring tests # 3 and # 4

Figure A.7.3.1.1-1 SNR variation for out-of-sync testing

## A.7.3.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.2E-UTRAN FDD Radio Link Monitoring Test for In-sync

## A.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.2.1-1 and A.7.3.2.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Table A.7.3.2.1-1: General test parameters for E-UTRAN FDD in-sync testing

Table A.7.3.2.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for in-sync radio link monitoring tests # 1 and # 2

Figure A.7.3.2.1-1 SNR variation for in-sync testing

## A.7.3.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.3E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync

## A.7.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.3.1-1, A.7.3.3.1-2 and A.7.3.3.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Table A.7.3.3.1-1: General test parameters for E-UTRAN TDD out-of-sync testing

Table A.7.3.3.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests # 1 and # 2

Table A.7.3.3.1-3: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests # 3 and # 4

Figure A.7.3.3.1-1. SNR variation for out-of-sync testing

## A.7.3.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.4E-UTRAN TDD Radio Link Monitoring Test for In-sync

## A.7.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.4.1-1 and A.7.3.4.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Table A.7.3.4.1-1: General test parameters for E-UTRAN TDD in-sync testing

Table A.7.3.4.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring tests # 1 and # 2

Figure A.7.3.4.1-1. SNR variation for in-sync testing

## A.7.3.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink subframes configured for CQI transmission according to the configured CQI mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.5E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync in DRX

## A.7.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.5.1-1, A.7.3.5.1-2, A.7.3.5.1-3 and A.7.3.5.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.5.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.5.1-1: General test parameters for E-UTRAN FDD out-of-sync tests in DRX

Table A.7.3.5.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for out-of-sync radio link monitoring tests # 1 and # 2 in DRX

Table A.7.3.5.1-3: DRX-Configuration for E-UTRAN FDD out-of-sync tests

Table A.7.3.5.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing

Figure A.7.3.5.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.5.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

In test 1 and test 2 during the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

In test 1 the UE shall stop transmitting uplink signal no later than time point C (duration D1 = 900 ms after the start of time duration T3).

In test 2 the UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.6E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX

## A.7.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.6.1-1, A.7.3.6.1-2, A.7.3.6.1-3 and A.7.3.6.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.6.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.6.1-1: General test parameters for E-UTRAN FDD in-sync test in DRX

Table A.7.3.6.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for in-sync radio link monitoring test # 1 in DRX

Table A.7.3.6.1-3: DRX-Configuration for E-UTRAN FDD out-of-sync tests

Table A.7.3.6.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing

Figure A.7.3.6.1-1 SNR variation for in-sync testing in DRX

## A.7.3.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.7E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX

## A.7.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.7.1-1, A.7.3.7.1-2, A.7.3.7.1-3 and A.7.3.7.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.7.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.7.1-1: General test parameters for E-UTRAN TDD out-of-sync tests in DRX

Table A.7.3.7.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests # 1 and # 2 in DRX

Table A.7.3.7.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests

Table A.7.3.7.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing

Figure A.7.3.7.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.7.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

In test 1 and test 2 during the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe according to the configured CQI reporting mode (PUCCH 1-0).

In test 1 the UE shall stop transmitting uplink signal no later than time point C (D1 = 900 ms after the start of time duration T3).

In test 2 the UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.8E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX

## A.7.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.8.1-1, A.7.3.8.1-2, A.7.3.8.1-3 and A.7.3.8.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.8.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.8.1-1: General test parameters for E-UTRAN TDD in-sync test in DRX

Table A.7.3.8.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring test # 1 in DRX

Table A.7.3.8.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests

Table A.7.3.8.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing

Figure A.7.3.8.1-1 SNR variation for in-sync testing in DRX

## A.7.3.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.9 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction and Non-MBSFN ABS

A.7.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.9.1-1 and A.7.3.9.1-2 below. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.9.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in the aggressor Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.9.1-1: General test parameters for E-UTRAN FDD out-of-sync testing under time domain measurement resource restriction with non-MBSFN ABS

Table A.7.3.9.1-2: Cell specific test parameters for E-UTRAN FDD for out-of-sync radio link monitoring under time domain measurement resource restriction with non-MBSFN ABS

Figure A.7.3.9.1-1 SNR variation for out-of-sync testing

## A.7.3.9.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.10E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with Non-MBSFN ABS

## A.7.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.10.1-1 and A.7.3.10.1-2 below. There are two cells, cell 1 is the serving cell and cell 2 is the neigbhor aggressor cell. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.10.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Non-MBSFN ABS pattern is configured in Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.10.1-1: General test parameters for E-UTRAN TDD out-of-sync testing under time domain measurement resource restriction with non-MBSFN ABS

Table A.7.3.10.1-2: Cell specific test parameters for E-UTRAN TDD for out-of-sync radio link monitoring under time domain measurement resource restriction with non-MBSFN ABS

Figure A.7.3.10.1-1 SNR variation in active cell for out-of-sync testing under time domain measurement resource restriction with non-MBSFN ABS

A.7.3.10.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.11E-UTRAN FDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS

## A.7.3.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.11.1-1 and A.7.3.11.1-2 below. There are two cells in the test: Cell 1 is the Active cell and Cell 2 is the Neighbor cell. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.11.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.11.1-1: General test parameters for E-UTRAN FDD in-sync testing under time domain measurement resource restriction

Table A.7.3.11.1-2: Cell specific test parameters for E-UTRAN FDD for in-sync radio link monitoring under time domain measurement resource restriction

Figure A.7.3.11.1-1 SNR variation in the active cell for in-sync testing under time domain measurement resource restriction

## A.7.3.11.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.12E-UTRAN TDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS

## A.7.3.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.12.1-1 and A.7.3.12.1-2 below. There are two cells in the test: Cell 1 is the Active cell and Cell 2 is the Neighbor cell. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.12.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Non-MBSFN ABS pattern is configured in the aggressor Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.12.1-1: General test parameters for E-UTRAN TDD in-sync testing under time domain measurement resource restriction

Table A.7.3.12.1-2: Cell specific test parameters for E-UTRAN TDD for in-sync radio link monitoring under time domain measurement resource restriction

Figure A.7.3.12.1-1 SNR variation in active cell for in-sync testing under time domain measurement resource restriction

## A.7.3.12.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink subframes configured for CQI transmission according to the configured CQI mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.13 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS

## A.7.3.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.13.1-1 and A.7.3.13.1-2 below. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.13.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

MBSFN ABS pattern is configured in the aggressor Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.13.1-1: General test parameters for E-UTRAN FDD out-of-sync testing under time domain measurement resource restriction with MBSFN ABS

Table A.7.3.13.1-2: Cell specific test parameters for E-UTRAN FDD for out-of-sync radio link monitoring under time domain measurement resource restriction with MBSFN ABS

Figure A.7.3.13.1-1 SNR variation for out-of-sync testing

## A.7.3.13.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.14 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS

## A.7.3.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.14.1-1 and A.7.3.14.1-2 below. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.14.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

MBSFN ABS pattern is configured in the aggressor Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.14.1-1: General test parameters for E-UTRAN TDD out-of-sync testing under time domain measurement resource restriction with MBSFN ABS

Table A.7.3.14.1-2: Cell specific test parameters for E-UTRAN TDD for out-of-sync radio link monitoring under time domain measurement resource restriction with MBSFN ABS

Figure A.7.3.14.1-1 SNR variation for out-of-sync testing

## A.7.3.14.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.15E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS

## A.7.3.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.15.1-1 and A.7.3.15.1-2 below. There are two cells, cell 1 is the serving cell and cell 2 is the neighbour aggressor cell. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.15.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

MBSFN ABS pattern is configured in Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.15.1-1: General test parameters for E-UTRAN FDD in-sync testing under time domain measurement resource restriction with MBSFN ABS

Table A.7.3.15.1-2: Cell specific test parameters for E-UTRAN FDD for in-sync radio link monitoring under time domain measurement resource restriction with MBSFN ABS

Figure A.7.3.15.1-1 SNR variation in the active cell for in-sync testing under time domain measurement resource restriction with MBSFN ABS

## A.7.3.15.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.16E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS

## A.7.3.16.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction when CRS assistance information is not provided. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.16.1-1 and A.7.3.16.1-2 below. There are two cells, cell 1 is the serving cell and cell 2 is the neighbour aggressor cell. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.15.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

MBSFN ABS pattern is configured in Cell 2 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing serving cell measurements. The patterns shall be configured prior to the start of T1.

Table A.7.3.16.1-1: General test parameters for E-UTRAN TDD in-sync testing under time domain measurement resource restriction with MBSFN ABS

Table A.7.3.16.1-2: Cell specific test parameters for E-UTRAN TDD for in-sync radio link monitoring under time domain measurement resource restriction with MBSFN ABS

Figure A.7.3.16.1-1 SNR variation in the active cell for in-sync testing under time domain measurement resource restriction with MBSFN ABS

## A.7.3.16.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.17E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.7.3.17.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell under time domain measurement resource restriction with CRS assistance information. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.17.1-1 and A.7.3.17.1-2 below. There are three active cells in the test: Cell 1 is the PCell cell and Cell 2 and 3 are the neighbour cells. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.17.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing Pcell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2 and T3 in this test. The non-MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.17.1-1: General test parameters for E-UTRAN FDD out-of-sync testing under time domain measurement resource restriction with CRS Assistance Information and Non-MBSFN ABS

Table A.7.3.17.1-2: Cell specific test parameters for E-UTRAN FDD for out-of-sync radio link monitoring under time domain measurement resource restriction with CRS Assistance Information and Non-MBSFN ABS

Figure A.7.3.17.1-1 SNR variation for out-of-sync testing

## A.7.3.17.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.18E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS

## A.7.3.18.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the serving cell under time domain measurement resource restriction with CRS assistance information. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.18.1-1 and A.7.3.18.1-2 below. There are three active cells in the test: Cell 1 is the PCell cell and Cell 2 and 3 are the neighbour cells. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.18.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing Pcell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2 and T3 in this test. The non-MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.18.1-1: General test parameters for E-UTRAN TDD out-of-sync testing under time domain measurement resource restriction with CRS Assistance Information and Non-MBSFN ABS

Table A.7.3.18.1-2: Cell specific test parameters for E-UTRAN TDD for out-of-sync radio link monitoring under time domain measurement resource restriction with CRS Assistance Information and Non-MBSFN ABS

Figure A.7.3.18.1-1 SNR variation for out-of-sync testing

## A.7.3.18.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.19E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS

## A.7.3.19.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell under time domain measurement resource restriction with CRS assistance information. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in section 7.6.

The test parameters are given in Tables A.7.3.19.1-1 and A.7.3.19.1-2 below. There are three active cells in the test: Cell 1 is the PCell cell and Cell 2 and 3 are the neighbour cells. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.19.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing PCell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2, T3, T4 and T5 in this test. The Non-MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.19.1-1: General test parameters for E-UTRAN FDD in-sync radio link monitoring test

Table A.7.3.19.1-2: Cell specific test parameters for E-UTRAN FDD in-sync radio link monitoring test

Figure A.7.3.19.1-1 SNR variation for in-sync testing

## A.7.3.19.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.20E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS

## A.7.3.20.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell under time domain measurement resource restriction with CRS assistance information. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in section 7.6.

The test parameters are given in Tables A.7.3.20.1-1 and A.7.3.20.1-2 below. There are three active cells in the test: Cell 1 is the PCell and Cell 2 and 3 are the Neighbor cells. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.20.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Non-MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing PCell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2, T3, T4 and T5 in this test. The Non-MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.20.1-1: General test parameters for E-UTRAN TDD in-sync radio link monitoring test

Table A.7.3.20.1-2: Cell specific test parameters for E-UTRAN TDD in-sync radio link monitoring test

Figure A.7.3.20.1-1 SNR variation for in-sync testing

## A.7.3.20.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.21E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS

## A.7.3.21.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell under time domain measurement resource restriction with CRS assistance information and MBSFN ABS. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in section 7.6.

The test parameters are given in Tables A.7.3.21.1-1 and A.7.3.21.1-2 below. There are three active cells in the test: Cell 1 is the PCell cell and Cell 2 and 3 are the neighbour cells. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.21.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing PCell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2, T3, T4 and T5 in this test. The MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.21.1-1: General test parameters for E-UTRAN FDD in-sync radio link monitoring test

Table A.7.3.21.1-2: Cell specific test parameters for E-UTRAN FDD in-sync radio link monitoring test

Figure A.7.3.21.1-1 SNR variation for in-sync testing

## A.7.3.21.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.22E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS

## A.7.3.22.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell under time domain measurement resource restriction with CRS assistance information. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in section 7.6.

The test parameters are given in Tables A.7.3.22.1-1 and A.7.3.22.1-2 below. There are three active cells in the test: Cell 1 is the PCell and Cell 2 and 3 are the Neighbor cells. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.22.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

MBSFN ABS pattern is configured in both Cell 2 and Cell 3 in this test. The UE is configured by higher layers with a time domain measurement restriction pattern for performing PCell measurements. The UE is also provided via higher layers with the CRS assistance information for Cell 2 and Cell 3, which shall be valid during T1, T2, T3, T4 and T5 in this test. The MBSFN ABS pattern, the time domain measurement resource restriction pattern and the CRS assistance information shall be configured prior to the start of T1.

Table A.7.3.22.1-1: General test parameters for E-UTRAN TDD in-sync radio link monitoring test

Table A.7.3.22.1-2: Cell specific test parameters for E-UTRAN TDD in-sync radio link monitoring test

Figure A.7.3.22.1-1 SNR variation for in-sync testing

## A.7.3.22.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.23E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync for 5MHz Bandwidth

## A.7.3.23.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in subclause A.7.3.1. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.7.3.23.1-1 and A.7.3.23.1-2 will replace the values of corresponding parameters in Test 4 in Tables A.7.3.1.1-1 and A.7.3.1.1-2. Only Test 4 is defined for the 5MHz bandwidth.

Table A.7.3.23.1-1: General test parameters for E-UTRAN FDD out-of-sync testing under 5MHz Bandwidth

Table A.7.3.23.1-2: Cell specific test parameters for E-UTRAN FDD for out-of-sync radio link monitoring test #4 under 5MHz Bandwidth

## A.7.3.23.2Test Requirements

The requirements defined in section A.7.3.1.2 shall apply to this test case.

## A.7.3.24E-UTRAN FDD Radio Link Monitoring Test for In-sync for 5MHz Bandwidth

## A.7.3.24.1Test Purpose and Environment

The purpose of this test case is the same as for the Test 2 defined in subclause A.7.3.2. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.7.3.24.1-1 and A.7.3.24.1-2 will replace the values of corresponding parameters in Tables A.7.3.2.1-1 and A.7.3.2.1-2.

Table A.7.3.24.1-1: General test parameters for E-UTRAN FDD in-sync testing

Table A.7.3.24.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for in-sync radio link monitoring test

## A.7.3.24.2Test Requirements

The requirements defined in section A.7.3.2.2 shall apply to this test case.

## A.7.3.25E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX for 5MHz Bandwidth

## A.7.3.25.1Test Purpose and Environment

The purpose of this test case is the same as for the Test 2 defined in subclause A.7.3.6. The test parameters are the same except those described in the following section. The listed parameter values in Tables A.7.3.25.1-1 and A.7.3.25.1-2 will replace the values of corresponding parameters in Tables A.7.3.6.1-1 and A.7.3.6.1-2.

Table A.7.3.25.1-1: General test parameters for E-UTRAN FDD in-sync testing

Table A.7.3.25.1-2: Cell specific test parameters for E-UTRAN FDD (cell # 1) for in-sync radio link monitoring test

## A.7.3.25.2Test Requirements

The requirements defined in section A.7.3.6.2 shall apply to this test case.

## A.7.3.26E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 0

## A.7.3.26.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.26.1-1, A.7.3.26.1-2 and A.7.3.26.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.26.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Table A.7.3.26.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync testing for UE Category 0

Table A.7.3.26.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests for UE Category 0

Figure A.7.3.26.1-1: SNR variation for out-of-sync testing

## A.7.3.26.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.27E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync for UE Category 0

## A.7.3.27.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.27.1-1 and A.7.3.27.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.27.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms.

Table A.7.3.27.1-1: General test parameters for E-UTRAN FD-FDD in-sync testing for UE Category 0

Table A.7.3.27.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring test for UE Category 0

Figure A.7.3.27.1-1: SNR variation for in-sync testing

## A.7.3.27.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.28E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0

## A.7.3.28.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.28.1-1, A.7.3.28.1-2, A.7.3.28.1-3 and A.7.3.28.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.28.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.28.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync tests in DRX for UE category 0

Table A.7.3.28.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category 0

Table A.7.3.28.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category 0

Table A.7.3.28.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category 0

Figure A.7.3.28.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.28.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.29E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 0

## A.7.3.29.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.29.1-1, A.7.3.29.1-2, A.7.3.29.1-3 and A.7.3.29.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.29.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.29.1-1: General test parameters for E-UTRAN FD-FDD in-sync test in DRX for UE category 0

Table A.7.3.29.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category 0

Table A.7.3.29.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category 0

Table A.7.3.29.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category 0

Figure A.7.3.29.1-1: SNR variation for in-sync testing in DRX

## A.7.3.29.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.30E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 0

## A.7.3.30.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.30.1-1, A.7.3.30.1-2 and A.7.3.30.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.30.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 10 ms.

Table A.7.3.30.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync testing for UE Category 0

Table A.7.3.30.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring for UE Category 0

Figure A.7.3.30.1-1: SNR variation for out-of-sync testing

## A.7.3.30.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.31E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync for UE Category 0

## A.7.3.31.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.31.1-1 and A.7.3.31.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.31.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 10 ms.

Table A.7.3.31.1-1: General test parameters for E-UTRAN HD-FDD in-sync testing

Table A.7.3.31.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring test for UE category 0

Figure A.7.3.31.1-1: SNR variation for in-sync testing

## A.7.3.31.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.32E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0

## A.7.3.32.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.32.1-1, A.7.3.32.1-2, A.7.3.32.1-3 and A.7.3.32.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.32.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 5ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.Table A.7.3.32.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync tests in DRX for UE category 0

Table A.7.3.32.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category 0

Table A.7.3.32.1-3: DRX-Configuration for E-UTRAN HD-FDD out-of-sync test for UE category 0

Table A.7.3.32.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category 0

Figure A.7.3.32.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.32.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.33E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 0

## A.7.3.33.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.33.1-1, A.7.3.33.1-2, A.7.3.33.1-3 and A.7.3.33.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.33.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.33.1-1: General test parameters for E-UTRAN HD-FDD in-sync test in DRX for UE category 0

Table A.7.3.33.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category 0

Table A.7.3.33.1-3: DRX-Configuration for E-UTRAN HD-FDD out-of-sync test for UE category 0

Table A.7.3.33.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category 0

Figure A.7.3.33.1-1: SNR variation for in-sync testing in DRX

## A.7.3.33.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.34E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for UE Category 0

## A.7.3.34.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.34.1-1, A.7.3.34.1-2 and A.7.3.34.1-3 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.34.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Table A.7.3.34.1-1: General test parameters for E-UTRAN TDD out-of-sync testing for UE Category 0

Table A.7.3.34.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring for UE Category 0

Figure A.7.3.34.1-1: SNR variation for out-of-sync testing

## A.7.3.34.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (240 ms after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.35E-UTRAN TDD Radio Link Monitoring Test for In-sync for UE category 0

## A.7.3.35.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.35.1-1 and A.7.3.35.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.35.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

Table A.7.3.35.1-1: General test parameters for E-UTRAN TDD in-sync testing

Table A.7.3.35.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring test

Figure A.7.3.35.1-1: SNR variation for in-sync testing

## A.7.3.35.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (420 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.36E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0

## A.7.3.36.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.36.1-1, A.7.3.36.1-2, A.7.3.36.1-3 and A.7.3.36.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.36.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.36.1-1: General test parameters for E-UTRAN TDD out-of-sync test in DRX for UE category 0

Table A.7.3.36.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring test in DRX for UE category 0

Table A.7.3.36.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync test for UE category 0

Table A.7.3.36.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for UE category 0

Figure A.7.3.36.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.36.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.37E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE category 0

## A.7.3.37.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category 0 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.11.

The test parameters are given in Tables A.7.3.37.1-1, A.7.3.37.1-2, A.7.3.37.1-3 and A.7.3.37.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.37.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.37.1-1: General test parameters for E-UTRAN TDD in-sync test in DRX for UE category 0

Table A.7.3.37.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category 0

Table A.7.3.37.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync test for UE category 0

Table A.7.3.37.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for UE category 0

Figure A.7.3.37.1-1: SNR variation for in-sync testing in DRX

## A.7.3.37.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.38E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC

## A.7.3.38.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.38.1-1, A.7.3.38.1-2, A.7.3.38.1-3, and A.7.3.38.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of three successive time periods with time duration of T1, T2 and T3 respectively. Figure A.7.3.38.1-1 shows the variation of the downlink SNR in the PCell and PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.38.1-1: General test parameters for E-UTRAN FDD out-of-sync tests in DRX in synchronous dual connectivity

Table A.7.3.38.1-2: Cell specific test parameters for E-UTRAN FDD out-of-sync radio link monitoring in DRX in synchronous dual connectivity

Table A.7.3.38.1-3: DRX-Configuration for E-UTRAN FDD out-of-sync tests in synchronous dual connectivity

Table A.7.3.38.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing in synchronous dual connectivity

Figure A.7.3.38.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.38.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CQI transmission on Cell1.

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe on Cell2.

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 900 ms after the start of time duration T3) on PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.39E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in asynchronous DC

## A.7.3.39.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in asynchronous dual connectivity. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in section 7.6.

The test parameters are given in Tables A.7.3.39.1-1, A.7.3.39.1-2, A.7.3.39.1-3 and A.7.3.39.1-4. There are two cells in the test. Cell 1 is PCell in MCG and cell 2 is PSCell in SCG. Before the test starts the UE is connected to cell 1 on radio channel 1 and to cell 2 on radio channel 2. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. The downlink SNR in cell 1 keeps constant in the test. Figure A.7.3.39.1-1 shows the variation of the downlink SNR in the cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2 in asynchronous dual connectivity. For both cells, the UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.39.1-1: General test parameters for E-UTRAN FDD out-of-sync in DRX

Table A.7.3.39.1-2: Cell specific test parameters for E-UTRAN FDD for out-of-sync radio link monitoring in DRX

Table A.7.3.39.1-3: DRX-Configuration for E-UTRAN FDD out-of-sync tests

Table A.7.3.39.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing

Figure A.7.3.39.1-1 SNR variation for out-of-sync test in DRX

## A.7.3.39.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

In the test, during time durations T1, T2 and T3, the UE shall transmit uplink signal on cell 1 at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

In the test, during the period from time point A to time point B the UE shall transmit uplink signal on cell 2 at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

In the test, the UE shall stop transmitting uplink signal on cell 2 no later than time point C (duration D1 = 900 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.40E-UTRAN TDD-TDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC

## A.7.3.40.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.40.1-1, A.7.3.40.1-2, A.7.3.40.1-3, and A.7.3.40.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of three successive time periods with time duration of T1, T2 and T3 respectively. Figure A.7.3.40.1-1 shows the variation of the downlink SNR in the PCell and PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.40.1-1: General test parameters for E-UTRAN TDD out-of-sync tests in DRX in synchronous dual connectivity

Table A.7.3.40.1-2: Cell specific test parameters for E-UTRAN TDD out-of-sync radio link monitoring in DRX in synchronous dual connectivity

Table A.7.3.40.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests in synchronous dual connectivity

Table A.7.3.26.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing in synchronous dual connectivity

Figure A.7.3.40.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.40.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CQI transmission on Cell1.

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe on Cell2.

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 900 ms after the start of time duration T3) on PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.41E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

## A.7.3.41.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in dual connectivity. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.41.1-1, A.7.3.41.1-2, A.7.3.41.1-3 and A.7.3.41.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.41.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration for PCell and PSCell is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.41.1-1: General test parameters for E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.41.1-2: Cell specific test parameters for E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.41.1-3: DRX-Configuration for E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.41.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Figure A.7.3.41.1-1 SNR variation of cell 2 (PSCell) for in-sync testing in DRX

## A.7.3.41.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0) on PCell and PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.42E-UTRAN FDD-FDD DC Radio Link Monitoring Test for In-sync in DRX in asynchronous DC

## A.7.3.42.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in asynchronous dual connectivity. This test will partly verify the E-UTRAN FDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.42.1-1, A.7.3.42.1-2, A.7.3.42.1-3 and A.7.3.42.1-4. There are two cells in the test. Cell 1 is PCell in MCG and cell 2 is PSCell in SCG. Before the test starts the UE is connected to cell 1 on radio channel 1 and to cell 2 on radio channel 2. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. The downlink SNR in cell 1 keeps constant in the test. Figure A.7.3.42.1-1 shows the variation of the downlink SNR in cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2 in asynchronous dual connectivity. For both cell 1 and cell 2, the UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.42.1-1: General test parameters for E-UTRAN FDD in-sync test in DRX

Table A.7.3.42.1-2: Cell specific test parameters for E-UTRAN FDD for in-sync radio link monitoring in DRX

Table A.7.3.42.1-3: DRX-Configuration for E-UTRAN FDD out-of-sync tests

Table A.7.3.42.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD out-of-sync testing

Figure A.7.3.42.1-1 Cell 2 SNR variation for in-sync testing in DRX

## A.7.3.42.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal on cell 2 at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.43E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

## A.7.3.43.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in dual connectivity. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.43.1-1, A.7.3.43.1-2, A.7.3.43.1-3 and A.7.3.43.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.43.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms. In the test, DRX configuration for PCell and PSCell is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.43.1-1: General test parameters for E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.43.1-2: Cell specific test parameters for E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.43.1-3: DRX-Configuration for E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Table A.7.3.43.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity

Figure A.7.3.43.1-1 SNR variation of cell 2 (PSCell) for in-sync testing in DRX

## A.7.3.43.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0) on PCell and PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.44E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in FDD

## A.7.3.44.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.44.1-1, A.7.3.44.1-2, A.7.3.44.1-3, and A.7.3.44.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of three successive time periods with time duration of T1, T2 and T3 respectively. Figure A.7.3.44.1-1 shows the variation of the downlink SNR in the PCell and PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2ms on cell 1 and 1ms on cell 2, respectively. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.44.1-1: General test parameters for E-UTRAN TDD-FDD DC out-of-sync tests in DRX in synchronous dual connectivity with PCell in FDD

Table A.7.3.44.1-2: Cell specific test parameters for E-UTRAN TDD-FDD DC out-of-sync radio link monitoring in DRX in synchronous dual connectivity with PCell in FDD

Table A.7.3.44.1-3: DRX-Configuration for E-UTRAN TDD-FDD DC out-of-sync tests in synchronous dual connectivity with PCell in FDD

Table A.7.3.44.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD-FDD DC out-of-sync testing in synchronous dual connectivity with PCell in FDD

Figure A.7.3.44.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.44.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CQI transmission on Cell1.

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe on Cell2.

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 900 ms after the start of time duration T3) on PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.45E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in TDD

## A.7.3.45.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.45.1-1, A.7.3.45.1-2, A.7.3.45.1-3, and A.7.3.45.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of three successive time periods with time duration of T1, T2 and T3 respectively. Figure A.7.3.45.1-1 shows the variation of the downlink SNR in the PCell and PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1ms on cell 1 and 2ms on cell 2, respectively. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.45.1-1: General test parameters for E-UTRAN TDD-FDD DC out-of-sync tests in DRX in synchronous dual connectivity with PCell in TDD

Table A.7.3.45.1-2: Cell specific test parameters for E-UTRAN TDD-FDD DC out-of-sync radio link monitoring in DRX in synchronous dual connectivity with PCell in TDD

Table A.7.3.45.1-3: DRX-Configuration for E-UTRAN TDD-FDD DC out-of-sync tests in synchronous dual connectivity with PCell in TDD

Table A.7.3.45.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD-FDD CA out-of-sync testing in synchronous dual connectivity with PCell in TDD

Figure A.7.3.45.1-1 SNR variation for out-of-sync testing in DRX

## A.7.3.45.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CQI transmission on Cell1.

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the uplink subframe on Cell2.

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 900 ms after the start of time duration T3) on PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.46E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD

## A.7.3.46.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in dual connectivity. This test will partly verify the E-UTRAN FDD and TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.46.1-1, A.7.3.46.1-2, A.7.3.46.1-3 and A.7.3.46.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.46.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms on PCell and 1ms on PSCell. In the test, DRX configuration for PCell and PSCell is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.46.1-1: General test parameters for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD

Table A.7.3.46.1-2: Cell specific test parameters for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD

Table A.7.3.46.1-3: DRX-Configuration for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD

Table A.7.3.46.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD

Figure A.7.3.46.1-1 SNR variation of cell 2 (PSCell) for in-sync testing in DRX

## A.7.3.46.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0) on PCell and PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.47E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD

## A.7.3.47.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used in dual connectivity. This test will partly verify the E-UTRAN FDD and TDD radio link monitoring requirements in clause 7.6.

The test parameters are given in Tables A.7.3.47.1-1, A.7.3.47.1-2, A.7.3.47.1-3 and A.7.3.47.1-4. There are two cells, cell 1 is PCell and cell 2 is PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.47.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1ms on PCell and 2ms on PSCell. In the test, DRX configuration for PCell and PSCell is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.47.1-1: General test parameters for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD

Table A.7.3.47.1-2: Cell specific test parameters for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD

Table A.7.3.47.1-3: DRX-Configuration for E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD

Table A.7.3.47.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD

Figure A.7.3.47.1-1 SNR variation of cell 2 (PSCell) for in-sync testing in DRX

## A.7.3.47.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0) on PCell and PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.48E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A

## A.7.3.48.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.48.1-1 and A.7.3.48.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.48.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.48.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.48.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.48.1-1: SNR variation for out-of-sync testing

## A.7.3.48.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.49E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A

## A.7.3.49.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.49.1-1 and A.7.3.49.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.49.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.49.1-1: General test parameters for E-UTRAN FD-FDD in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.49.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.49.1-1: SNR variation for in-sync testing

## A.7.3.49.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (720 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.50E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A

## A.7.3.50.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category M1 UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.50.1-1, A.7.3.50.1-2, A.7.3.50.1-3 and A.7.3.50.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.50.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.50.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.50.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.50.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.50.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.50.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.50.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.51E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A

## A.7.3.51.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD category M1 UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.51.1-1, A.7.3.51.1-2, A.7.3.51.1-3 and A.7.3.51.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.51.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.51.1-1: General test parameters for E-UTRAN FD-FDD in-sync test in DRX for UE category M1 configured in CEMode A

Table A.7.3.51.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category M1 configured in CEMode A

Table A.7.3.51.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.51.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.51.1-1: SNR variation for in-sync testing in DRX

## A.7.3.51.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.52E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A

## A.7.3.52.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.52.1-1 and A.7.3.52.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.52.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 20 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.52.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.52.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.52.1-1: SNR variation for out-of-sync testing

## A.7.3.52.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.53E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A

## A.7.3.53.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.53.1-1 and A.7.3.53.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.53.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 20 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.53.1-1: General test parameters for E-UTRAN HD-FDD in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.53.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.53.1-1: SNR variation for in-sync testing

## A.7.3.53.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (740 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.54E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A

## A.7.3.54.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category M1 UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.54.1-1, A.7.3.54.1-2, A.7.3.54.1-3 and A.7.3.54.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.54.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 20 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.54.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.54.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.54.1-3: DRX-Configuration for E-UTRAN HD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.54.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.54.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.54.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6520 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.55E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A

## A.7.3.55.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category M1 UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN HD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.55.1-1, A.7.3.55.1-2, A.7.3.55.1-3 and A.7.3.55.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.55.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 20 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.55.1-1: General test parameters for E-UTRAN HD-FDD in-sync test in DRX for UE category M1 configured in CEMode A

Table A.7.3.55.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category M1 configured in CEMode A

Table A.7.3.55.1-3: DRX-Configuration for E-UTRAN HD-FDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.55.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.55.1-1: SNR variation for in-sync testing in DRX

## A.7.3.55.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1140 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.56E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A

## A.7.3.56.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN TDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.56.1-1 and A.7.3.56.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.56.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.56.1-1: General test parameters for E-UTRAN TDD out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.56.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.56.1-1: SNR variation for out-of-sync testing

## A.7.3.56.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.57E-UTRAN TDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A

## A.7.3.57.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN TDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.57.1-1 and A.7.3.57.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.57.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 1 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.57.1-1: General test parameters for E-UTRAN TDD in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.57.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.57.1-1: SNR variation for in-sync testing

## A.7.3.57.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (720 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.58E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A

## A.7.3.58.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category M1 UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.58.1-1, A.7.3.58.1-2, A.7.3.58.1-3 and A.7.3.58.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.58.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 4. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.58.1-1: General test parameters for E-UTRAN TDD out-of-sync tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.58.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for UE category M1 configured in CEMode A

Table A.7.3.58.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.58.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.58.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.58.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.59E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A

## A.7.3.59.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category M1 UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.59.1-1, A.7.3.59.1-2, A.7.3.59.1-3 and A.7.3.59.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.59.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.59.1-1: General test parameters for E-UTRAN TDD in-sync test in DRX for UE category M1 configured in CEMode A

Table A.7.3.59.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring test in DRX for UE category M1 configured in CEMode A

Table A.7.3.59.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests for UE category M1 configured in CEMode A

Table A.7.3.59.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for UE category M1 configured in CEMode A

Figure A.7.3.59.1-1: SNR variation for in-sync testing in DRX

## A.7.3.59.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.60HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

## A.7.3.60.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.60.1-1, A.7.3.60.1-2, A.7.3.60.1-2A, A.7.3.60.1-3 and A.7.3.60.1-4. nCell 1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.60.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.60.1-1: General test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.60.1-2: nCell specific test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.60.1-2A: eCell 1 specific test parameters for HD-FDD Out-of-sync radio link monitoring test in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.60.1-3: DRX-Configuration for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.60.1-4: TimeAlignmentTimer -Configuration for NB-IoT HD-FDD out-of-sync testing for UE category NB1 In-band mode in normal coverage

Figure A.7.3.60.1-1: SNR variation for out-of-sync testing in DRX for NB-IoT HD-FDD out-of-sync testing for UE category NB1 In-band mode in normal coverage

## A.7.3.60.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.61HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

## A.7.3.61.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.61.1-1, A.7.3.61.1-2, A.7.3.61.1-2A, A.7.3.61.1-3 and A.7.3.61.1-4. nCell 1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.61.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.61.1-1: General test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.61.1-2: nCell specific test parameters for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.61.1-2A: eCell 1 specific test parameters for HD-FDD Out-of-sync radio link monitoring test in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.61.1-3: DRX-Configuration for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.61.1-4: TimeAlignmentTimer -Configuration for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Figure A.7.3.61.1-1: SNR variation for HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

## A.7.3.61.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4.

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.62HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage

## A.7.3.62.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.62.1-1, A.7.3.62.1-2, A.7.3.62.1-3, A.7.3.62.1-4 and A.7.3.62.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps.  Figure A.7.3.62.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [3]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.62.1-1: General test parameters for HD-FDD in-sync test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.62.1-2: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.62.1-3: eCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.62.1-4: DRX-Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.62.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 In-Band mode in enhanced coverage

Figure A.7.3.62.1-1: SNR variation for in-sync testing with DRX

## A.7.3.62.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.63HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage

## A.7.3.63.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.63.1-1, A.7.3.63.1-2, A.7.3.63.1-3, A.7.3.63.1-4 and A.7.3.63.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.63.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 are as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [2]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.63.1-1: General test parameters for HD-FDD in-sync test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.63.1-2: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.63.1-3: eCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.63.1-4: DRX-Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.63.1-5: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests with DRX for UE category NB1 In-Band mode in normal coverage

Figure A.7.3.63.1-1: SNR variation for in-sync testing with DRX

## A.7.3.63.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.64HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage

## A.7.3.64.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.64.1-1, A.7.3.64.1-2, A.7.3.64.1-3, A.7.3.64.1-4 and A.7.3.64.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.64.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.64.1-1: General test parameters for HD-FDD in-sync test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.64.1-2: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.64.1-3: eCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.64.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests without DRX for UE category NB1 In-Band mode in normal coverage

Figure A.7.3.64.1-1: SNR variation for in-sync testing without DRX

## A.7.3.64.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.65HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage

## A.7.3.65.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.65.1-1, A.7.3.65.1-2, A.7.3.65.1-3, A.7.3.65.1-4 and A.7.3.65.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.65.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in designated uplink subframes to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. During the period from time point A to time point D, the UE shall not be provisioned with any UL grant.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.65.1-1: General test parameters for HD-FDD in-sync test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.65.1-2: nCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.65.1-3: eCell 1 specific test parameters for HD-FDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.65.1-4: TimeAlignmentTimer -Configuration for E-UTRAN HD-FDD in-sync tests without DRX for UE category NB1 In-Band mode in enhanced coverage

Figure A.7.3.65.1-1: SNR variation for in-sync testing without DRX

## A.7.3.65.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.66HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage

## A.7.3.66.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.66.1-1 and A.7.3.66.1-2. nCell1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.66.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

Table A.7.3.66.1-1: General test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Standalone mode in normal coverage

Table A.7.3.66.1-2: nCell1 specific test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Standalone mode in normal coverage

Figure A.7.3.66.1-1: SNR variation for out-of-sync testing

## A.7.3.66.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.67HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage

## A.7.3.67.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT HD-FDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.67.1-1 and A.7.3.67.1-2 below. nCell1 is the active NB-IoT cell, in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.67.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure.

-Before the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 with duration dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH.

Note:The UE is expected to decode NPDCCH and complete the UL transmission during T2 according to the UL grant. The UE shall not be provisioned with any more UL grants until the start of time period T4.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 with duration dT

-During T3, the SNR is kept at SNR3.

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with duration dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct the UL transmission during T4 since the UE is expected to declare RLF during T3.

Table A.7.3.67.1-1: General test parameters for HD-FDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Guard band mode in enhanced coverage

Table A.7.3.67.1-2: nCell1 specific test parameters for  HD-FDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Guard band mode in enhanced coverage

Table A.7.3.67.1-3: eCell 1 specific test parameters for HD-FDD out-of-sync radio link monitoring test without DRX for UE category NB1 Guard band mode in enhanced coverage

Figure A.7.3.67.1-1: SNR variation for out-of-sync testing

## A.7.3.67.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behave correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.68E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A

## A.7.3.68.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.68.1-1 and A.7.3.68.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.68.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.68.1-1: General test parameters for E-UTRAN FD-FDD early out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.68.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.68.1-1: SNR variation for early out-of-sync testing

## A.7.3.68.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.2.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.69E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A

## A.7.3.69.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.69.1-1 and A.7.3.69.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.69.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.69.1-1: General test parameters for E-UTRAN HD-FDD early out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.69.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.69.1-1: SNR variation for early out-of-sync testing

## A.7.3.69.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.3.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.70E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A

## A.7.3.70.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.70.1-1 and A.7.3.70.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.70.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.70.1-1: General test parameters for E-UTRAN TDD early out-of-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.70.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.70.1-1: SNR variation for early out-of-sync testing

## A.7.3.70.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.2.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.71E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA

## A.7.3.71.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.71.1-1 and A.7.3.71.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.71.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.71.1-1: General test parameters for E-UTRAN FD-FDD early in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.71.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.71.1-1: SNR variation for early in-sync testing

## A.7.3.71.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.2.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.72E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA

## A.7.3.72.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.72.1-1 and A.7.3.72.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.72.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.72.1-1: General test parameters for E-UTRAN HD-FDD early in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.72.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.72.1-1: SNR variation for early in-sync testing

## A.7.3.72.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.2.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.73E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA

## A.7.3.73.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.73.1-1 and A.7.3.73.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.73.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.73.1-1: General test parameters for E-UTRAN TDD early in-sync testing for UE Cat-M1 in CEMode A

Table A.7.3.73.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEMode A

Figure A.7.3.73.1-1: SNR variation for early in-sync testing

## A.7.3.73.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.2.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.74E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A

## A.7.3.74.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD non-BL CE UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for non-BL CE UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.74.1-1 and A.7.3.74.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.74.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.74.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync testing for non-BL CE UE in CEMode A

Table A.7.3.74.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests for non-BL CE UE in CEMode A

Figure A.7.3.74.1-1: SNR variation for out-of-sync testing

## A.7.3.74.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.75E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A

## A.7.3.75.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD non-BL CE UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for non-BL CE UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.75.1-1 and A.7.3.75.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.75.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.75.1-1: General test parameters for E-UTRAN FD-FDD in-sync testing for non-BL CE UE in CEMode A

Table A.7.3.75.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring tests for non-BL CE UE in CEMode A

Figure A.7.3.75.1-1: SNR variation for in-sync testing

## A.7.3.75.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (720 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.76E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A

## A.7.3.76.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD non-BL CE UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.76.1-1, A.7.3.76.1-2, A.7.3.76.1-3 and A.7.3.76.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.76.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.76.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync tests in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.76.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.76.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for non-BL CE UE configured in CEMode A

Table A.7.3.76.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for non-BL CE UE configured in CEMode A

Figure A.7.3.76.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.76.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.77E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A

## A.7.3.77.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD non-BL CE UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN FD-FDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.77.1-1, A.7.3.77.1-2, A.7.3.77.1-3 and A.7.3.77.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.77.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 2 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.77.1-1: General test parameters for E-UTRAN FD-FDD in-sync test in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.77.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for in-sync radio link monitoring test in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.77.1-3: DRX-Configuration for E-UTRAN FD-FDD out-of-sync tests for non-BL CE UE configured in CEMode A

Table A.7.3.77.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FD-FDD out-of-sync testing for non-BL CE UE configured in CEMode A

Figure A.7.3.77.1-1: SNR variation for in-sync testing in DRX

## A.7.3.77.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.78E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A

## A.7.3.78.1Test Purpose and Environment

The purpose of this test is to verify that the TDD non-BL CE UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN TDD radio link monitoring requirements for non-BL CE UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.78.1-1 and A.7.3.78.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.78.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.78.1-1: General test parameters for E-UTRAN TDD out-of-sync testing for non-BL CE UE in CEMode A

Table A.7.3.78.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests for non-BL CE CE in CEMode A

Figure A.7.3.78.1-1: SNR variation for out-of-sync testing

## A.7.3.78.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.79E-UTRAN TDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A

## A.7.3.79.1Test Purpose and Environment

The purpose of this test is to verify that the TDD non-BL CE UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA. This test will partly verify the E-UTRAN TDD radio link monitoring requirements for non-BL CE UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.79.1-1 and A.7.3.79.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.79.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 1 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.79.1-1: General test parameters for E-UTRAN TDD in-sync testing for non-BL CE UE in CEMode A

Table A.7.3.79.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring tests for non-BL CE UE in CEMode A

Figure A.7.3.79.1-1: SNR variation for in-sync testing

## A.7.3.79.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (720 ms after the start of time duration T5) the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.80E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A

## A.7.3.80.1Test Purpose and Environment

The purpose of this test is to verify that the TDD non-BL CE UE configured in CEMode A properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.80.1-1, A.7.3.80.1-2, A.7.3.80.1-3 and A.7.3.80.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.80.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.80.1-1: General test parameters for E-UTRAN TDD out-of-sync tests in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.80.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.80.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests for non-BL CE UE configured in CEMode A

Table A.7.3.80.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for non-BL CE UE configured in CEMode A

Figure A.7.3.80.1-1: SNR variation for out-of-sync testing in DRX

## A.7.3.80.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (duration D1 = 6500 ms after the start of time duration T3.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.81E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A

## A.7.3.81.1Test Purpose and Environment

The purpose of this test is to verify that the TDD non-BL CE UE configured in CEMode A properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the E-UTRAN TDD radio link monitoring requirements in clause 7.19.

The test parameters are given in Tables A.7.3.81.1-1, A.7.3.81.1-2, A.7.3.81.1-3 and A.7.3.81.1-4. There is one cell (cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.3.81.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms without repetition. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode MPDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

In the test, the RRC parameter numberPRB-Pairs is set to 4 and the RRC parameter mPDCCH-NumRepetition is set 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.81.1-1: General test parameters for E-UTRAN TDD in-sync test in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.81.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for in-sync radio link monitoring test in DRX for non-BL CE UE configured in CEMode A

Table A.7.3.81.1-3: DRX-Configuration for E-UTRAN TDD out-of-sync tests for non-BL CE UE configured in CEMode A

Table A.7.3.81.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD out-of-sync testing for non-BL CE UE configured in CEMode A

Figure A.7.3.81.1-1: SNR variation for in-sync testing in DRX

## A.7.3.81.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (1120 ms after the start of time duration T5) the UE shall transmit uplink signal at least once every DRX cycle, in the On-duration part of the cycle in the subframe according to the configured CQI reporting mode (PUCCH 1-0).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.82E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.82.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.82.1-1 and A.7.3.82.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.82.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.82.1-1: General test parameters for E-UTRAN FD-FDD early out-of-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.82.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.82.1-1: SNR variation for early out-of-sync testing

## A.7.3.82.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.83E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.83.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.83.1-1 and A.7.3.83.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.83.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.83.1-1: General test parameters for E-UTRAN FD-FDD early in-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.83.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.83.1-1: SNR variation for early in-sync testing

## A.7.3.83.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.84E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.84.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.84.1-1 and A.7.3.84.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.84.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.84.1-1: General test parameters for E-UTRAN HD-FDD early out-of-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.84.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.84.1-1: SNR variation for early out-of-sync testing

## A.7.3.84.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.85E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.85.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.85.1-1 and A.7.3.85.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.85.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.85.1-1: General test parameters for E-UTRAN HD-FDD early in-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.85.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.85.1-1: SNR variation for early in-sync testing

## A.7.3.85.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.86E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.86.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.86.1-1 and A.7.3.86.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.86.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.86.1-1: General test parameters for E-UTRAN TDD early out-of-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.86.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.86.1-1: SNR variation for early out-of-sync testing

## A.7.3.86.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.87E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB

## A.7.3.87.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects an early in sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.87.1-1 and A.7.3.87.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.87.1-1 shows the variation of the downlink SNR in the active cell to emulate early in-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.87.1-1: General test parameters for E-UTRAN TDD early in-sync testing for UE Cat-M1 in CEModeB

Table A.7.3.87.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for early in-sync radio link monitoring tests for Cat-M1 in CEModeB

Figure A.7.3.87.1-1: SNR variation for early in-sync testing

## A.7.3.87.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qin_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold Q E2_in_CatM1. When the estimated quality becomes better than the threshold starting from time point E, Layer 1 of the UE shall trigger event E2 and send a report to the higher layers within Qin_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.88TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

## A.7.3.88.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.88.1-1, A.7.3.88.1-2, A.7.3.88.1-2A, A.7.3.88.1-3 and A.7.3.88.1-4. nCell 1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.88.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.88.1-1: General test parameters for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.88.1-2: nCell specific test parameters for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.88.1-2A: eCell 1 specific test parameters for TDD Out-of-sync radio link monitoring test in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.88.1-3: DRX-Configuration for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage

Table A.7.3.88.1-4: TimeAlignmentTimer -Configuration for NB-IoT TDD out-of-sync testing for UE category NB1 In-band mode in normal coverage

Figure A.7.3.88.1-1: SNR variation for out-of-sync testing in DRX for NB-IoT TDD out-of-sync testing for UE category NB1 In-band mode in normal coverage

## A.7.3.88.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.89TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

## A.7.3.89.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.89.1-1, A.7.3.89.1-2, A.7.3.89.1-2A, A.7.3.89.1-3 and A.7.3.89.1-4. nCell 1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.89.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode the NPDCCH and complete the UL transmission when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.3.89.1-1: General test parameters for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.89.1-2: nCell specific test parameters for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.89.1-2A: eCell 1 specific test parameters for TDD Out-of-sync radio link monitoring test in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.89.1-3: DRX-Configuration for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Table A.7.3.89.1-4: TimeAlignmentTimer -Configuration for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

Figure A.7.3.89.1-1: SNR variation for TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage

## A.7.3.89.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4.

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.90TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage

## A.7.3.90.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell when DRX is used. This test will partly verify the TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.90.1-1, A.7.3.90.1-2, A.7.3.90.1-3, A.7.3.90.1-4 and A.7.3.90.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.90.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 are as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [2]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.90.1-1: General test parameters for TDD in-sync test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.90.1-2: nCell 1 specific test parameters for TDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.90.1-3: eCell 1 specific test parameters for TDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.90.1-4: DRX-Configuration for E-UTRAN TDD in-sync tests with DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.90.1-5: TimeAlignmentTimer -Configuration for E-UTRAN TDD in-sync tests with DRX for UE category NB1 In-Band mode in normal coverage

Figure A.7.3.90.1-1: SNR variation for in-sync testing with DRX

## A.7.3.90.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.91TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage

## A.7.3.91.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell when DRX is used. This test will partly verify the TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.91.1-1, A.7.3.91.1-2, A.7.3.91.1-3, A.7.3.91.1-4 and A.7.3.91.1-5. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps.  Figure A.7.3.91.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2 and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. NPDCCH repetition level is determined by RRC parameter npdcch-NumRepetitions [3]. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.91.1-1: General test parameters for TDD in-sync test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.91.1-2: nCell 1 specific test parameters for TDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.91.1-3: eCell 1 specific test parameters for TDD in-sync radio link monitoring test with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.91.1-4: DRX-Configuration for E-UTRAN TDD in-sync tests with DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.91.1-5: TimeAlignmentTimer -Configuration for E-UTRAN TDD in-sync tests with DRX for UE category NB1 In-Band mode in enhanced coverage

Figure A.7.3.91.1-1: SNR variation for in-sync testing with DRX

## A.7.3.91.2Test Requirements

The UE behaviour in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.92TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage

## A.7.3.92.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE configured in normal coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.92.1-1, A.7.3.92.1-2, A.7.3.92.1-3 and A.7.3.92.1-4. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.92.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.92.1-1: General test parameters for TDD in-sync test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.92.1-2: nCell 1 specific test parameters for TDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.92.1-3: eCell 1 specific test parameters for TDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in normal coverage

Table A.7.3.92.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD in-sync tests without DRX for UE category NB1 In-Band mode in normal coverage

Figure A.7.3.92.1-1: SNR variation for in-sync testing without DRX

## A.7.3.92.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.93TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage

## A.7.3.93.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE configured in enhanced coverage properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.93.1-1, A.7.3.93.1-2, A.7.3.93.1-3 and A.7.3.93.1-4. nCell 1 is the active cell in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.93.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states.

Prior to the start of the time duration T1, the UE shall be fully be synchronized to nCell 1. The UE is scheduled in every uplink subframe to transmit NPUSCH, which is received by the test equipment. By measuring the reception of the NPUSCH, detection of out of sync and in sync requirements can be measured. In the test, DRX configuration is disabled, i.e. UE tries to decode NPDCCH and to send NPUSCH during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The test setup in each test during time durations T1, T2, dT and T3 shall be as follows:

-During the period from time point A to time point B, the SNR is decreasing linearly from SNR1 to SNR2.

-During the period from time point C to time point D, the SNR is increasing linearly from SNR2 to SNR3.

-During the period T3, the test system shall send the UE a grant to transmit in uplink. UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission.

-Thereafter UE switches back to downlink.

In each run of the test, the test equipment selects NPDCCH repetition level, and sends the RRC configuration to the UE. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.93.1-1: General test parameters for TDD in-sync test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.93.1-2: nCell 1 specific test parameters for TDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.93.1-3: eCell 1 specific test parameters for TDD in-sync radio link monitoring test without DRX for UE category NB1 In-Band mode in enhanced coverage

Table A.7.3.93.1-4: TimeAlignmentTimer -Configuration for E-UTRAN TDD in-sync tests without DRX for UE category NB1 In-Band mode in enhanced coverage

Figure A.7.3.93.1-1: SNR variation for in-sync testing without DRX

## A.7.3.93.2Test Requirements

The UE behavior in each test shall be as follows:

During the period T3, the UE under test is expected to decode the uplink grant and switch to uplink and complete the uplink transmission. This is considered a correct event.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.94TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage

## A.7.3.94.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.94.1-1 and A.7.3.94.1-2. nCell1 is the active NB-IoT cell in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.94.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure:

-Prior to the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 within dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH

Note:The UE is expected to decode the NPDCCH and complete the UL transmission during T2 according to the UL grant.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 within dT

-During T3, the SNR is kept as SNR3

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct any UL transmission during T4, since the UE is expected to declare RLF during T3.

Table A.7.3.94.1-1: General test parameters for TDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Standalone mode in normal coverage

Table A.7.3.94.1-2: nCell1 specific test parameters for TDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Standalone mode in normal coverage

Figure A.7.3.94.1-1: SNR variation for out-of-sync testing

## A.7.3.94.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behaves correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.95TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage

## A.7.3.95.1Test Purpose and Environment

The purpose of this test is to verify that the TDD category NB1 UE properly detects the out of sync for the purpose of monitoring downlink radio link quality of the NB-IoT Cell. This test will partly verify the NB-IoT TDD radio link monitoring requirements in clause 7.23.

The test parameters are given in Tables A.7.3.95.1-1 and A.7.3.95.1-2 below. nCell1 is the active NB-IoT cell, in the test. The test consists of four successive time periods with time duration of T1, T2, T3 and T4 respectively, excluding the transition time duration dT, where the SNR increases or decreases gradually in small steps. Figure A.7.3.95.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync state with the following testing procedure.

-Before the start of the time duration T1, the UE shall be fully synchronized to nCell1

-Starting at point A, the SNR is decreased in small steps from SNR1 to SNR2 with duration dT

-At the start of the time duration T2, the UE is provided with a UL grant with NPDCCH.

Note:The UE is expected to decode NPDCCH and complete the UL transmission during T2 according to the UL grant.

-Starting at point B, the SNR is decreased in small steps from SNR2 to SNR3 with duration dT

-During T3, the SNR is kept at SNR3.

Note:The UE is expected to detect OOS and declare RLF during T3.

-Starting at point C, the SNR is increased in small steps from SNR3 to SNR1 with duration dT

-At the start of the time period T4, the UE will be provided with another UL grant with NPDCCH

Note:The UE is not expected to decode the UL grant and conduct the UL transmission during T4 since the UE is expected to declare RLF during T3.

Table A.7.3.95.1-1: General test parameters for TDD Radio Link Monitoring Test for out-of-sync tests without DRX for UE Category NB1 Guard band mode in enhanced coverage

Table A.7.3.95.1-2: nCell1 specific test parameters for TDD Radio Link Monitoring Test for out-of-sync without DRX for UE Category NB1 Guard band mode in enhanced coverage

Table A.7.3.95.1-3: eCell 1 specific test parameters for TDD out-of-sync radio link monitoring test without DRX for UE category NB1 Guard band mode in enhanced coverage

Figure A.7.3.95.1-1: SNR variation for out-of-sync testing

## A.7.3.95.2Test Requirements

The UE behaviors in each test shall be as follows:

-The UE shall complete the NPUSCH transmission during T2 according to the received UL grant;

-The UE shall not conduct any NPUSCH transmission during T4

A correct event is defined as UE behave correctly in all above steps. The correct events observed during repeated tests shall be at least 90%.

## A.7.3.96E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement

## A.7.3.96.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.96.1-1 and A.7.3.96.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.96.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 2 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.96.1-1: General test parameters for E-UTRAN FD-FDD out-of-sync testing for UE Cat-M1 in CEMode A for MPDCCH performance improvement

Table A.7.3.96.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A for MPDCCH performance improvement

## A.7.3.97E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement

## A.7.3.97.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.97.1-1 and A.7.3.97.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.97.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode without repetition with a reporting periodicity of 20 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.97.1-1: General test parameters for E-UTRAN HD-FDD out-of-sync testing for UE Cat-M1 in CEMode A for MPDCCH performance improvement

Table A.7.3.97.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A for MPDCCH performance improvement

Figure A.7.3.97.1-1: SNR variation for out-of-sync testing

## A.7.3.97.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.98E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement

## A.7.3.98.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell in CEModeA configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN TDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.98.1-1 and A.7.3.98.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.98.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CQI reporting in PUCCH 1-0 mode with a reporting periodicity of 1 ms.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 8. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.98.1-1: General test parameters for E-UTRAN TDD out-of-sync testing for UE Cat-M1 in CEMode A for MPDCCH performance improvement

Table A.7.3.98.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for out-of-sync radio link monitoring tests for Cat-M1 in CEMode A for MPDCCH performance improvement

Figure A.7.3.98.1-1: SNR variation for out-of-sync testing

## A.7.3.98.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all subframes configured for CQI transmission according to the configured CQI reporting mode (PUCCH 1-0).

The UE shall stop transmitting uplink signal no later than time point C (440 ms after the start of time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.99E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement

## A.7.3.99.1Test Purpose and Environment

The purpose of this test is to verify that the FD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.99.1-1 and A.7.3.99.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.99.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.99.1-1: General test parameters for E-UTRAN FD-FDD early out-of-sync testing for UE Cat-M1 in CEModeB for MPDCCH performance improvement

Table A.7.3.82.1-2: Cell specific test parameters for E-UTRAN FD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB for MPDCCH performance improvement

Figure A.7.3.99.1-1: SNR variation for early out-of-sync testing

## A.7.3.99.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.100E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement

## A.7.3.100.1Test Purpose and Environment

The purpose of this test is to verify that the HD-FDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.100.1-1 and A.7.3.100.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.100.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.100.1-1: General test parameters for E-UTRAN HD-FDD early out-of-sync testing for UE Cat-M1 in CEModeB for MPDCCH performance improvement

Table A.7.3.100.1-2: Cell specific test parameters for E-UTRAN HD-FDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB for MPDCCH performance improvement

Figure A.7.3.100.1-1: SNR variation for early out-of-sync testing

## A.7.3.100.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.3.101E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement

## A.7.3.101.1Test Purpose and Environment

The purpose of this test is to verify that the TDD Cat-M1 UE properly detects an early out of sync event and makes correct reporting of it for the purpose of monitoring the downlink radio link quality of the PCell in CEModeB configured with mpdcch-crs-connnected-config. This test will partly verify the E-UTRAN FDD radio link monitoring requirements for Cat-M1 UE defined in clause 7.19.

The test parameters are given in Tables A.7.3.101.1-1 and A.7.3.101.1-2 below. There is one cell (cell 1), which is the active cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.3.101.1-1 shows the variation of the downlink SNR in the active cell to emulate early out-of-sync and early in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1.

In the test, the RRC parameter numberPRB-Pairs is set to 6 and the RRC parameter mPDCCH-NumRepetition is set to 128. In addition, the UE is configured with rlm-ReportConfig. UE shall successfully complete the RRC reconfiguration accordingly prior to the start of time duration T1.

Table A.7.3.101.1-1: General test parameters for E-UTRAN TDD early out-of-sync testing for UE Cat-M1 in CEModeB for MPDCCH performance improvement

Table A.7.3.101.1-2: Cell specific test parameters for E-UTRAN TDD (cell # 1) for early out-of-sync radio link monitoring tests for Cat-M1 in CEModeB for MPDCCH performance improvement

Figure A.7.3.101.1-1: SNR variation for early out-of-sync testing

## A.7.3.101.2Test Requirements

The UE shall compare the downlink radio link quality of the PCell over the last Qout_CatM1 evaluation, which is defined in 7.19.4.1, with the threshold QE1_out_CatM. When the estimated quality becomes worse than the threshold starting from time point B, Layer 1 of the UE shall trigger event E1 and send a report to the higher layers within Qout_CatM1 evaluation period.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4Interruption for Dual Connectivity

## A.7.4.1E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that when PCell is in non-DRX and PSCell is in DRX, PCell interruptions due to transitions from active to non-active and from non-active to active during PSCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for FDD PCell in dual connectivity requirements in clause 7.12.2.

The test parameters are given in Table A.7.4.1.1-1, A.7.4.1.1-2 and A.7.4.1.1-3 below. In the test there are two cells: Cell1 and Cell2. Cell1 is PCell and Cell2 is PSCell. PCell is continuously scheduled in DL while PSCell is not scheduled and has DRX configured. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell1 and Cell2. Cell1 shall be configured as PCell and Cell2 shall be configured as PSCell. Prior to start of T1 the DRX inactivity timer for the PSCell have already expired. During T1 the UE shall be continuously scheduled on PCell while not scheduled on PSCell.

Table A.7.4.1.1-1: General test parameters for E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.1.1-2: Cell specific test parameters for E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.1.1-3: DRX-Configuration for E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.1.2Test Requirements

The UE shall be continuously scheduled in PCell during the entire length of T1. UE shall not be scheduled in PSCell during T1. During the time duration T1 the UE shall transmit at leat 99% of ACK/NACK on PCell.

The UE shall not miss transmitting two consequtive ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.2E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.2.1Test Purpose and Environment

The purpose of this test is to verify that when PCell is in non-DRX and PSCell is in DRX, PCell interruptions due to transitions from active to non-active and from non-active to active during PSCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for TDD PCell in dual connectivity requirements in clause 7.12.2.

The test parameters are given in Table A.7.4.2.1-1, A.7.4.2.1-2 and A.7.4.2.1-3 below. In the test there are two cells: Cell1 and Cell2. Cell1 is PCell and Cell2 is PSCell. PCell is continuously scheduled in DL while PSCell is not scheduled and has DRX configured. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell1 and Cell2. Cell1 shall be configured as PCell and Cell2 shall be configured as PSCell. Prior to start of T1 the DRX inactivity timer for the PSCell have already expired. During T1 the UE shall be continuously scheduled on PCell while not scheduled on PSCell.

Table A.7.4.2.1-1: General test parameters for E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.2.1-2: Cell specific test parameters for E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.2.1-3: DRX-Configuration for E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.2.2Test Requirements

The UE shall be continuously scheduled in PCell during the entire length of T1. UE shall not be scheduled in PSCell during T1. During the time duration T1 the UE shall transmit at leat 99% of ACK/NACK on PCell.

The UE shall not miss transmitting two consequtive ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.3E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity

## A.7.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE fulfils the requirement on interruptions on PCell at transitions between active and non-active during DRX in TS36.133 section 7.12.2.

The test parameters are given in Table A.7.4.3.1-1, Table A.7.4.3.1-2and Table A.7.4.3.1-3 below. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell on the FDD primary component (RF channel 1). Cell 2 is PSCell on the FDD secondary component (RF channel 2). The test consists of 1 time period, with time duration of T1. PDCCH indicating a new transmission on PCell shall be sent continuously during the whole time duration to ensure UE would not enter DRX state on PCell. PSCell is in DRX state with 320ms DRX cycle.

Table A.7.4.3.1-1: General test parameters for E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity

Table A.7.4.3.1-2: Cell specific test parameters for E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity

Table A.7.4.3.1-3: DRX-Configuration for E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity

Table A.7.4.3.1-4: TimeAlignmentTimer -Configuration for E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity

## A.7.4.3.2Test Requirements

The UE shall be scheduled on PCell continuously during the whole time duration T1. During time durations T1, at least 99% of all expected ACK/NACKs shall be transmitted on PCell by the UE.

Each interruption shall not exceed 1 subframe.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.4E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.4.1Test Purpose and Environment

The purpose of this test is to verify that when PCell is in non-DRX and PSCell is in DRX, PCell interruptions due to transitions from active to non-active and from non-active to active during PSCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for FDD PCell in dual connectivity requirements in clause 7.12.2.

The test parameters are given in Table A.7.4.4.1-1, A.7.4.4.1-2 and A.7.4.4.1-3 below. In the test there are two cells: Cell1 and Cell2. Cell1 is PCell and Cell2 is PSCell. PCell is continuously scheduled in DL while PSCell is not scheduled and has DRX configured. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell1 and Cell2. Cell1 shall be configured as PCell and Cell2 shall be configured as PSCell. Prior to start of T1 the DRX inactivity timer for the PSCell have already expired. During T1 the UE shall be continuously scheduled on PCell while not scheduled on PSCell.

Table A.7.4.4.1-1: General test parameters for E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.4.1-2: Cell specific test parameters for E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.4.1-3: DRX-Configuration for E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.4.2Test Requirements

The UE shall be continuously scheduled in PCell during the entire length of T1. UE shall not be scheduled in PSCell during T1. During the time duration T1 the UE shall transmit at leat 99% of ACK/NACK on PCell.

The UE shall not miss transmitting two consequtive ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.5E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.5.1Test Purpose and Environment

The purpose of this test is to verify that when PCell is in non-DRX and PSCell is in DRX, PCell interruptions due to transitions from active to non-active and from non-active to active during PSCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for TDD PCell in dual connectivity requirements in clause 7.12.2.

The test parameters are given in Table A.7.4.5.1-1, A.7.4.5.1-2 and A.7.4.5.1-3 below. In the test there are two cells: Cell1 and Cell2. Cell1 is PCell and Cell2 is PSCell. PCell is continuously scheduled in DL while PSCell is not scheduled and has DRX configured. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell1 and Cell2. Cell1 shall be configured as PCell and Cell2 shall be configured as PSCell. Prior to start of T1 the DRX inactivity timer for the PSCell have already expired. During T1 the UE shall be continuously scheduled on PCell while not scheduled on PSCell.

Table A.7.4.5.1-1: General test parameters for E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.5.1-2: Cell specific test parameters for E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

Table A.7.4.5.1-3: DRX-Configuration for E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC

## A.7.4.5.2Test Requirements

The UE shall be continuously scheduled in PCell during the entire length of T1. UE shall not be scheduled in PSCell during T1. During the time duration T1 the UE shall transmit at leat 99% of ACK/NACK on PCell.

The UE shall not miss transmitting two consequtive ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.6E-UTRAN FDD-TDD DC interruption at SRS carrier based switching

## A.7.4.6.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will will verify the interruption requirements on PCC in clause 7.12.2.7.

In the test there are three cells: cell1, cell2 and cell3. Cell1 and cell2 are PCell and PSCell on the FDD primary component carriers, Cell3 is activated SCell on the TDD secondary component carrier which operats in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 the UE shall be continuously scheduled on PCell and PSCell. Immediately at the beginning of T2, a PDCCH with SRS-TPC-RNTI is sent to the UE to initiate SRS switching.

Table A.7.4.6.1-1: General test parameters for E-UTRAN FDD-TDD DC interruption at SRS carrier based switching

Table A.7.4.6.1-2: Cell specific test parameters for E-UTRAN FDD-TDD DC interruption at SRS carrier based switching

Table A.7.4.6.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD-TDD DC interruption at SRS carrier based switching

## A.7.4.6.2Test Requirements

The UE shall be continuously scheduled in PCell throughout the test and during the time duration T2, at most 6 ACK/NACK loss on PCell shall be detected.

The UE shall be continuously scheduled in PSCell throughout the test and during the time duration T2, at most 6 ACK/NACK loss on PSCell shall be detected.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.4.7E-UTRAN TDD-TDD DC interruption at SRS carrier based switching

## A.7.4.7.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will will verify the interruption requirements on PCC in clause 7.12.2.7.

In the test there are two cells: cell1, cell2 and cell3. Cell1 and cell2 are PCell and PSCell respectively on the TDD primary component carriers, Cell3 is activated SCell on the TDD secondary component carrier which operats in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 the UE shall be continuously scheduled on PCell and PSCell. Immediately at the beginning of T2, a PDCCH with SRS-TPC-RNTI is sent to the UE to initiate SRS switching.

Table A.7.4.7.1-1: General test parameters for E-UTRAN TDD-TDD DC interruption at SRS carrier based switching

Table A.7.4.7.1-2: Cell specific test parameters for E-UTRAN TDD-TDD DC interruption at SRS carrier based switching

Table A.7.4.7.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD-TDD DC interruption at SRS carrier based switching

## A.7.4.7.2Test Requirements

The UE shall be continuously scheduled in PCell throughout the test and during the time duration T2, at most 4 ACK/NACK loss on PCell shall be detected.

The UE shall be continuously scheduled in PSCell throughout the test and during the time duration T2, at most 4 ACK/NACK loss on PSCell shall be detected.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.5Proximity-based Services

## A.7.5.1E-UTRAN FDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test

## A.7.5.1.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for ProSe Direct Discovery transmissions when PCell downlink timing is used as a reference with. This test will verify the requirements in clause 7.16.2.1.1.1 ProSe Direct Discovery transmissions. In the test the UE under test is configured for ProSe operation only on PCell and also the UE is configured only for PCell for WAN.

For this test, the UE is triggered by the test loop function or the upper layers to announce ProSe Direct Discovery.

The test parameters are given in Table A.7.5.1.1-1 below. There is one active cell (PCell) in this test. The transmit timing is verified using the transmission timing of PSDCH.

Table A.7.5.1.1-1: Test parameters for ProSe Transmission Timing Accuracy test for E-UTRAN FDD

## A.7.5.1.2Test Requirements

For parameters specified in Tables A.7.5.1.1-1, the timing accuracy for ProSe Direct Discvoery transmissions shall be within the limits defined in clause 7.16.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 5MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED DRX with a cycle length of 320ms:

a) After a connection is set up with the cell, the test system shall verify that the ProSe UE transmit timing offset is within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +32TS (approximately +1µs) compared to that in (a). The test system shall wait for at least one discovery period (320ms) before verifying the requirement again in (c).

c) The test system shall verify that the UE transmit timing offset stays within ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1.

## A.7.5.2E-UTRAN TDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test

## A.7.5.2.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for ProSe Direct Discovery transmissions when PCell downlink timing is used as a reference with. This test will verify the requirements in clause 7.16.2.1.1.1 for ProSe Direct Discovery transmissions. In the test the UE under test is configured for ProSe operation only on PCell and also the UE is configured only for PCell for WAN.

For this test, the UE is triggered by the test loop function or the upper layers to announce ProSe Direct Discovery.

The test parameters are given in Table A.7.5.2.1-1 below. There is one active cell (PCell) in this test. The transmit timing is verified using the transmission timing of PSDCH.

Table A.7.5.2.1-1: Test parameters for ProSe Transmission Timing Accuracy test for E-UTRAN TDD

## A.7.5.1.2Test Requirements

For parameters specified in Tables A.7.5.2.1-1, the timing accuracy for ProSe Direct Discvoery transmissions shall be within the limits defined in clause 7.16.2.

The following sequence of events shall be used to verify that the requirements are met.

For the 5MHz channel bandwidth, the test sequence shall be carried out in RRC_CONNECTED DRX with a cycle length of 320ms:

a) After a connection is set up with the cell, the test system shall verify that the ProSe UE transmit timing offset is within 624×TS  ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +32TS (approximately +1µs) compared to that in (a). The test system shall wait for at least one discovery period (320ms) before verifying the requirement again in (c).

c) The test system shall verify that the UE transmit timing offset stays within 624×TS  ± 12×TS with respect to the first detected path  (in time) of the corresponding downlink frame of cell 1.

## A.7.5.3E-UTRAN FDD - Interruptions due to ProSe Direct Discovery

## A.7.5.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the allowed PCell interruptions due to ProSe Direct Discovery defined in clause 7.16.3.1 and clause 7.16.3.3. In the test the UE under test is configured for ProSe operation only on PCell and also the UE is configured only for PCell for WAN.

For this test, the UE is triggered by the test loop function or the upper layers to monitor ProSe Direct Discovery.

The test parameters are given in Table A.7.5.3.1-1 and Table A.7.5.3.1-2 below. There is one active cell (PCell) in this test and 24 active Sidelink transmissions in this test (with 12 active Sidelink UEs per configured discovery subframe). Two tests (Test 1 and Test 2) are defined to verify interruptions due to synchronous (Test 1) and asynchronous (Test 2) ProSe Direct Discovery.

The tests consist of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the ProSe Direct Discovery announcements from other active Sidelink UEs on the ProSe Direct Discvoery resources.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE during T2, and the UE is expected to transmit SidelinkUEInformation indicating discRxInterest during T2. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformation for up to [2] sec, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during ProSe Direct Discovery.

Table A.7.5.3.1-1: Test parameters for interruption due to ProSe Direct Discovery tests

Table A.7.5.3.1-2: ProSe Direct Discovery configuration for interruption due to ProSe Direct Discovery tests

Table A.7.5.3.1-3: Cell specific test parameters for interruption due to ProSe Direct Discovery tests

## A.7.5.3.2Test Requirements

The UE shall be scheduled on PCell continuously during T3.

In Test 1, at least 98.75% of all expected ACK/NACKs during T3 shall be transmitted by the ProSe UE. The missed ACK/NACKs can occur only on subframe ‘n’, if either n±1 subframe is a discovery subframe, or if n-3, or n-5 is a discovery subframe.

NOTE:For the test configuration in Table A.7.5.3.1-1 and Table A.7.5.3.1-2, the specific subframes where missed ACK/NACKs are allowed are when (subframe mod 320) = 159, 163, 162, 166, corresponding to allowed interruptions on subframe 159 and 162.

In Test 2, at least 97.5% of all expected ACK/NACKs during T3 shall be transmitted by the ProSe UE. The missed ACK/NACK can occur only on subframe ‘n’, if either n±5 subframe is a discovery or SLSS subframe, or if n+1, or n-9 is a discovery or SLSS subframe.

NOTE:For the test configuration in Table A.7.5.3.1-1 and Table A.7.5.3.1-2, the specific subframes where missed ACK/NACKs are allowed are when (subframe mod 320) = 135, 139, 145, 149, 155, 159, 166, 170, corresponding to allowed interruptions on subframes 135, 145, 155 and 166.

## A.7.5.4E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test

## A.7.5.4.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for ProSe Direct Communication transmissions when PCell downlink timing is used as a reference with. This test will verify the requirements in clause 7.16.2.1.1.1 for ProSe Direct Communication transmissions. In the test the UE under test is configured for ProSe operation only on PCell and also the UE is configured only for PCell for WAN.

For this test, the UE is triggered by the test loop function or the upper layers to transmit for ProSe Direct Communication.

The test parameters are given in Table A.7.5.4.1-1 below. There is one active cell (PCell) in this test. The test system will configure the ProSe UE to transmit SLSS in each period (40ms) by configuring networkControlledSyncTx as ON via dedicated RRC signaling. The transmit timing is verified using the transmission timing of SLSS transmissions.

Table A.7.5.4.1-1: Test parameters for ProSe Transmission Timig Accuracy test for E-UTRAN FDD

## A.7.5.4.2Test Requirements

For parameters specified in Tables A.7.5.4.1-1, the timing accuracy for ProSe Direct Communication transmissions shall be within the limits defined in clause 7.16.2. The timing accuracy is verified using SLSS transmissions.

The following sequence of events shall be used to verify that the requirements are met.

For 5MHz or 10MHz channel bandwith, the test sequence shall be carried out in RRC_CONNECTED DRX with a cycle length of 320ms:

a) After a connection is set up with the cell, the test system shall verify that the ProSe UE SLSS transmission timing offset is within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

b) The test system adjusts the downlink transmit timing for the cell by +32TS (approximately +1µs) compared to that in (a). The test system shall wait for at least one SLSS period (40ms) before verifying the requirement again in (c).

c) The test system shall verify that the UE SLSS transmissiontiming offset stays within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 1.

## A.7.5.5E-UTRAN FDD - Interruptions due to ProSe Direct Communication

## A.7.5.5.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to PCell interruptions due to ProSe Direct Communication defined in clause 7.16.3. In the test the UE under test is configured for ProSe operation only on PCell and also the UE is configured only for PCell for WAN.

For this test, the UE is triggered by the test loop function or the upper layers to monitor ProSe Direct Communication.

The test parameters are given in Table A.7.5.5.1-1, Table A.7.5.5.1-2 and Table A.7.5.5.1-3 below. There is one active cell (PCell) in this test and 12 (5MHz) or 16 (10 MHz) active Sidelink UEs in this test transmitting ProSe Direct Communication.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the ProSe Direct Communication transmission from other active Sidelink UEs on the ProSe Direct Communication resoruces.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE during T2, and the UE is expected to transmit SidelinkUEInformation indicating commRxInterestedFreq during T2. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to repond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformation for up to [2] sec, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during ProSe Direct Communication (no missed ACK/NACKs are allowed).

Table A.7.5.5.1-1: Test parameters for interruption due to ProSe Direct Communication tests

Table A.7.5.5.1-2: ProSe Direct Communication specific configuration for interruption due to ProSe Direct Communication tests

Table A.7.5.5.1-2: Cell specific test parameters for interruption due to ProSe Direct Communication tests

## A.7.5.5.2Test Requirements

The UE shall be scheduled on PCell continuously during T3. During T3, 100% of all expected ACK/NACKs shall be transmitted by the ProSe UE.

## A.7.5.6E-UTRAN FDD - Interruptions due to ProSe Direct Discovery with discovery period less than 320ms

## A.7.5.6.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the allowed PCell interruptions due to ProSe Direct Discovery defined in clause 7.16.3.3 when the discovery period less than 320ms. In the test the UE under test is configured only with PCell with the ProSe operation on uplink carrier of the PCell.

This test is applicable to ProSe Direct Discovery capable UEs that support discovery periods of less than 320ms.

For this test, the UE is triggered by the test loop function or the upper layers to monitor ProSe Direct Discovery.

The test parameters are given in Table A.7.5.6.1-1, Table A.7.5.6.1-2, and Table A.7.5.6.1-3 below. There is one active cell (PCell) in this test and 24 active Sidelink transmissions in this test (with 12 active Sidelink UEs per configured discovery subframe).

The tests consist of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the ProSe Direct Discovery announcements from other active Sidelink UEs on the ProSe Direct Discovery resources.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE during T2, and the UE is expected to transmit SidelinkUEInformation indicating discRxInterest during T2. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformation for up to [2] sec, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during ProSe Direct Discovery.

Table A.7.5.6.1-1: Test parameters for interruption due to ProSe Direct Discovery test with discovery period less than 320ms for E-UTRAN FDD

Table A.7.5.6.1-2: ProSe Direct Discovery configuration for interruption test due to ProSe Direct Discovery with discovery period less than 320ms for E-UTRAN FDD

Table A.7.5.6.1-3: Cell specific test parameters for interruption due to ProSe Direct Discovery test with discovery period less than 320ms for E-UTRAN FDD

## A.7.5.6.2Test Requirements

The UE shall be scheduled on PCell continuously during T3.

The test system shall verify that at least 98.75% of all expected ACK/NACKs during T3 shall be transmitted by the ProSe UE. The missed ACK/NACKs can occur only on subframe ‘n’, if either n±1 subframe is a discovery subframe, or if n-3, or n-5 is a discovery subframe.

NOTE:For the test configuration in Table A.7.5.6.1-1 and Table A.7.5.6.1-2, the specific subframes where missed ACK/NACKs are allowed are when (subframe mod 40) = 19, 23, 22, 26, corresponding to allowed interruptions on subframe (subframe mod 40) = 19 and 22.

## A.7.5.7E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery

## A.7.5.7.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the allowed PCell interruptions due to ProSe Direct Discovery defined in clause 7.16.3.1 and clause 7.16.3.3. In the test the UE under test is configured with PCell and one SCell, with ProSe operation configured on the PCell.

A UE that meets the requirements of this clause is not required to be tested for the requirements of clause 7.5.3.

For this test, the UE is triggered by the test loop function or the upper layers to monitor ProSe Direct Discovery.

The test parameters are given in Table A.7.5.7.1-1, Table A.7.5.7.1-2, and Table A.7.5.7.1-3 below. There are two configured component carriers: PCC and SCC, and two active cells: Cell 1 and Cell2. Cell1 is the PCell on PCC, and Cell 2 is the SCell on SCC.  Sidelink operation is configured on the PCC UL. There are 24 active Sidelink transmissions in this test (with 12 active Sidelink UEs per configured discovery subframe). Two tests (Test 1 and Test 2) are defined to verify interruptions due to synchronous (Test 1) and asynchronous (Test 2) ProSe Direct Discovery.

The tests consist of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the ProSe Direct Discovery announcements from other active Sidelink UEs on the ProSe Direct Discovery resources.

During T2, the test system establishes a RRC connection with the UE. The test system shall configure the UE with the SCC. No PDSCH traffic is scheduled for UE during T2, and the UE is expected to transmit SidelinkUEInformation indicating discRxInterest during T2. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformation for up to [2] sec, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on both PCell and SCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during ProSe Direct Discovery.

Table A.7.5.7.1-1: Test parameters for interruption due to ProSe Direct Discovery tests

Table A.7.5.7.1-2: ProSe Direct Discovery configuration for interruption due to ProSe Direct Discovery tests

Table A.7.5.7.1-3: Cell specific test parameters for interruption due to ProSe Direct Discovery tests

## A.7.5.7.2Test Requirements

The UE shall be scheduled on PCell and SCell downlink continuously during T3.

In Test 1, at least 98.75% of all expected ACK/NACKs during T3 shall be transmitted by the ProSe UE. The missed ACK/NACKs can occur only on subframe ‘n’, if either n±1 subframe is a discovery subframe, or if n-3, or n-5 is a discovery subframe.

NOTE:For the test configuration in Table A.7.5.12.1-1 and Table A.7.5.12.1-2, the specific subframes where missed ACK/NACKs are allowed are when (subframe mod 320) = 159, 163, 162, 166, corresponding to allowed interruptions on subframe 159 and 162.

In Test 2, at least 97.5% of all expected ACK/NACKs during T3 shall be transmitted by the ProSe UE. The missed ACK/NACK can occur only on subframe ‘n’, if either n±5 subframe is a discovery or SLSS subframe, or if n+1, or n-9 is a discovery or SLSS subframe.

NOTE:For the test configuration in Table A.7.5.7.1-1 and Table A.7.5.7.1-2, the specific subframes where missed ACK/NACKs are allowed are when (subframe mod 320) = 135, 139, 145, 149, 155, 159, 166, 170, corresponding to allowed interruptions on subframes 135, 145, 155 and 166.

## A.7.5.8E-UTRAN FDD-FDD - Cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency

## A.7.5.8.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to cell reselection and timing accuracy for ProSe Direct Discovery transmissions on a non-serving frequency defined in clauses 7.16.4 and 7.16.2.1.2, respectively. In the test the UE under test is configured with PCell on a serving frequency, and the PCell provides the ProSe Direct Discovery resources for a non-serving frequency.

This test is applicable for ProSe Direct Discovery capable UEs that support concurrent inter-band E-UTRAN and E-UTRAN ProSe operation, and indicates the support of inter-frequency discovery transmission using discInterFreqTx.

For this test, the UE is triggered by the test loop function or the upper layers to announce ProSe Direct Discovery.

The test parameters are given in Table A.7.5.8.1-1, Table A.7.5.8.1-2, and Table A.7.5.8.1-3 below. The test consists of one active serving cell (cell 1) on the serving RF channel 1, and two active non-serving cells (cell 2 and cell3) on the non-serving discovery RF channel 2.

The tests consist of three successive time periods, with time duration of T1, T2 and T3 respectively.

The serving cell (cell 1 on RF channel 1) is active during the entire test duration (T1, T2, T3) without any changes to cell 1 RSRP. Prior to start of the test, the test system shall verify that the UE is transmitting ProSe Direct Discovery transmissions on the non-serving RF channel 2.

During T1, only one non-serving cell (cell 2 on RF channel 2) is active. The UE is expected to be following the timing of cell 2 for its discovery transmissions on RF channel 2. During T2, cell 3 on the non-serving RF channel 2 is also turned ON and is configured to be better ranked than cell 2. The UE is expected to reselect to cell 3 for discovery transmit timing. During T3, RSRP of cell 2 is increased so that it becomes better ranked than cell 3. The UE is supposed to reselect back to cell 2 and follow its timing for discovery transmissions.

Table A.7.5.8.1-1: Test parameters for cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.8.1-2: ProSe Direct Discovery configuration for cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.8.1-3: Cell specific test parameters for cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

## A.7.5.8.2Test Requirements

During T1, the test system shall verify that the transmit timing offset of discovery transmission on RF channel 2 is within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 2.

During T2, the UE is expected to reselect to cell 3 for discovery timing synchronization after cell reselection delay to a newly detectable cell from start of T2. After the period of cell reselection delay to a newly detectable cell from the start of T2, the test system shall verify that the transmit timing offset of discovery transmission on RF channel 2 are within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 3.

The cell reselection delay to a newly detectable cell for discovery transmission on non-serving carrier shall be 10.56s.

NOTE:The cell reselection delay to a newly detectable cell for discovery transmission on non-serving carrier can be expressed as (Tdetect,EUTRAN_ProSe_Intra + 1 discovery period).

During T3, the UE is expected to reselect back to cell 2 for discovery timing synchronization after cell reselection delay to an already detected cell from start of T3. After the period of cell reselection delay to a newly detectable cell from the start of T3, the test system shall verify that the transmit timing offset of discovery transmission on RF channel 2 are within ± 12×TS with respect to the first detected path (in time) of the corresponding downlink frame of cell 2.

The cell reselection delay to an already detected cell for discovery transmission on non-serving carrier shall be 5.44s.

NOTE:The cell reselection delay to an already detected cell for discovery transmission on non-serving carrier can be expressed as (Tevaluate, E-UTRAN_ProSe_Intra + 1 discovery period).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.5.9E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery reception on non-serving frequency

## A.7.5.9.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to ProSe Direct Discovery reception on a non-serving frequency as defined in clause 7.16.3.3 and 7.16.3.4. In the test the UE under test is configured with PCell on a serving frequency, and the PCell provides the ProSe Direct Discovery resources for a non-serving frequency.

This test is applicable for ProSe Direct Discovery capable UEs that support concurrent inter-band E-UTRAN and E-UTRAN ProSe operation.

For this test, the UE is triggered by the test loop function or the upper layers to monitor ProSe Direct Discovery.

The test parameters are given in Table A.7.5.9.1-1, Table A.7.5.9.1-2, and Table A.7.5.9.1-3 below. The test consists of one active serving cell (cell 1) on the serving RF channel 1, and one active non-serving cells (cell 2) on the non-serving discovery RF channel 2. There are 96 active Sidelink transmissions in this test (with 12 active Sidelink UEs per configured discovery subframe) on RF channel 2.

After the test system establishes a RRC connection with the UE, the UE is expected to transmit SidelinkUEInformation indicating discRxInterest. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before start of the test. Further, depending on UE implementation, the UE may request for discovery reception gaps (using discRxGapReq) for the ProSe Direct Discovery reception operation on the non-serving frequency. If gaps are requested, the test system shall configure the gaps as requested and modify the PDSCH scheduling on cell 1 for this UE such that the UE is not scheduled on the DL on the subframes configured as reception gaps.

The test shall start after the completion of the RRC reconfiguration is complete following the SidelinkUEInformation message transmission from the UE. The test system shall then continuously schedule the UE on DL of cell 1 (apart from any subframes that are configured as discovery gaps).

Table A.7.5.9.1-1: Test parameters for interruptions due to ProSe Direct Discovery reception on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.9.1-2: ProSe Direct Discovery configuration for interruptions due to ProSe Direct Discovery reception on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.9.1-3: Cell specific test parameters for interruptions due to ProSe Direct Discovery reception on non-serving frequency test for E-UTRAN FDD-FDD

## A.7.5.9.2Test Requirements

The test system shall verity the allowed interruptions for ProSe Direct Discovery reception on non-serving frequency, and depends on the discovery gap configuration for the UE.

If no discovery gaps are configured, the test system shall verify that the total number of missed ACK/NACKs on the serving cell are less than 0.5%.

If discovery gaps are configured as requested by the UE, then test system shall verify that the missed ACK/NACKs, if any, correspond to locations as specified in subclause 7.16.3.4:

-Missed ACK/NACKs is allowed on a subframe n, if subframe n is configured as downlink reception gap (using discRxGapConfig) and either the subframe immediately preceding or immediately following that subframe is not configured as reception gap, and

-One additional missed ACK/NACK per discovery period is allowed on a subframe m, such that the subframe m is configured as reception gap.

## A.7.5.10E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery transmission on non-serving frequency

## A.7.5.10.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to ProSe Direct Discovery reception on a non-serving frequency as defined in clause 7.16.3.3 and 7.16.3.4. In the test the UE under test is configured with PCell on a serving frequency, and the PCell provides the ProSe Direct Discovery resources for a non-serving frequency.

This test is applicable for ProSe Direct Discovery capable UEs that support concurrent inter-band E-UTRAN and E-UTRAN ProSe operation, and indicates the support of inter-frequency discovery transmission using discInterFreqTx.

For this test, the UE is triggered by the test loop function or the upper layers to announce ProSe Direct Discovery.

The test parameters are given in Table A.7.5.10.1-1, Table A.7.5.10.1-2, and Table A.7.5.10.1-3 below. The test consists of one active serving cell (cell 1) on the serving RF channel 1, and one active non-serving cells (cell 2) on the non-serving discovery RF channel 2.

After the test system establishes a RRC connection with the UE, the UE is expected to transmit SidelinkUEInformation. On reception of SidelinkUEInformation, the test system shall RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before start of the test. Further, depending on UE implementation, the UE may request for discovery transmission and/or reception gaps (using discTxGapReq and/or discRxGapReq) for the ProSe Direct Discovery transmission operation on the non-serving frequency. If transmission gap is requested, the test system shall configure the transmission gap as requested. The test system shall not configure any reception gap for the UE for the purpose of this test.

The test shall start after the completion of the RRC reconfiguration is complete following the SidelinkUEInformation message transmission from the UE. The test system shall then continuously schedule the UE on DL of cell 1.

Table A.7.5.10.1-1: Test parameters for interruptions due to ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.10.1-2: ProSe Direct Discovery configuration for interruptions due to ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.10.1-3: Cell specific test parameters for interruptions due to ProSe Direct Discovery transmission on non-serving frequency test for E-UTRAN FDD-FDD

## A.7.5.10.2Test Requirements

The test system shall verity the allowed interruptions for ProSe Direct Discovery trannsmission on non-serving frequency.

If no discovery transmission gaps are configured, the test system shall verify that the total number of missed ACK/NACKs on the serving cell are less than 0.5%.

If discovery transmission gaps are configured as requested by the UE,  the test system shall verify that the number of missed ACK/NACKs are less than or equal to 5 missed ACK/NACKs during a discovery period (configured as 320ms in this test). Corresponding to discovery transmission on s subframe n (with respect to PCell) on the non-serving carrier, the missed ACK/NACKs are allowed only on subframes (n-1), n, (n+1), (n+3), (n+5).

## A.7.5.11E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Communication on non-serving frequency

## A.7.5.11.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to ProSe Direct Communication on a non-serving frequency as defined in clause 7.16.3.5. In the test the UE under test is configured with PCell on a serving frequency, and is pre-configured with ProSe Direct Communication resources for a non-serving frequency.

This test is applicable for ProSe Direct Communication capable UEs that support concurrent inter-band E-UTRAN and E-UTRAN ProSe operation.

For this test, the UE is triggered by the test loop function or the upper layers to receive ProSe Direct Communication.

The test parameters are given in Table A.7.5.11.1-1, Table A.7.5.11.1-2, Table A.7.5.11.1-3 and Table A.7.5.11.1-4 below. The test consists of one active serving cell (cell 1) on the serving RF channel 1, and there are no active cells on RF channel 2. On RF channel 2, the test consists of one active SyncRef UE (SyncRef UE 1) transmitting synchronization signals and channels, and 12 (5MHz) or 16 (10 MHz) active Sidelink UEs in this test transmitting ProSe Direct Communication.

The serving cell (cell 1) on RF channel 1 is not broadcasting SIB18, and the UE is expected to use its preconfigured parameters for ProSe Direct Communication operation on RF channel 2.

The UE is continuously scheduled with PDSCH traffic on PCell downlink in RF channel 1.

Table A.7.5.11.1-1: Test parameters for interruptions due to ProSe Direct Communication on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.11.1-2: ProSe Direct Communication configuration for interruptions due to ProSe Direct Communication on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.11.1-3: SyncRef UE specific test parameters for interruptions due to ProSe Direct Communication on non-serving frequency test for E-UTRAN FDD-FDD

Table A.7.5.11.1-4: Cell specific test parameters for interruptions due to ProSe Direct Communication on non-serving frequency test for E-UTRAN FDD-FDD

## A.7.5.11.2Test Requirements

The test system shall verify that the total number of missed ACK/NACKs on the serving cell on RF channel 1 are less than 0.5%.

## A.7.5.12E-UTRAN FDD - Selection / Reselection of ProSe relay UE

## A.7.5.12.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to selection / reselection of ProSe relay UE defined in clauses 7.16.5. In the test the UE under test is configured with PCell and is configured with ProSe Direct Discovery and ProSe Direct Communication resources as required for remote UE operation.

This test is applicable to UEs capable of ProSe Direct Discovery and ProSe Direct Communication, and further support the optional feature of sidelink remote UE operation.

The test parameters are given in Table A.7.5.12.1-1, Table A.7.5.12.1-2, Table A.7.5.12.1-3, Table A.7.5.12.1-4, and Table A.7.5.12.1-5 below. The test consists of one active serving cell (cell 1), and two active Sidelink relay UEs (Sidelink Relay UE 1, Sidelink Relay UE 2). The Sidelink relay UEs are configured to be transmitting relay discovery messages every discovery period.

The test system shall ensure that the remote UE under test has transmitted SidelinkUEInformation message and has been configured with the ProSe Direct Discovery resources for relay operation prior to the start of the test.

The tests consist of five successive time periods, with time duration of T1, T2, T3, and T4 respectively.

During T1, RSRP of cell 1 is kept higher than threshHigh (within remoteUE-Config), and the remote UE is not required to perform relay UE selection.

During T2, RSRP of cell 1 is configured to be lower than threshHigh. The UE is expected to start looking for relay UE and request the serving cell for ProSe Direct Communication resources for communicating with a candidate Sidelink Relay UE. The test system shall ensure that the UE under test transmits the SidelinkUEInformation message (requesting the ProSe Direct Communication resources) and has been configured the resource pool prior to end of T2 duration. During T2, the SD-RSRP of Sidelink Relay UE 1 and Sidelink Relay UE 2 is configured to be lower than the detection threshold and no relay UE will be available for the remote UE under test.

During T3, the SD-RSRP of Sidelink Relay UE 1 is raised above the detection threshold and the UE is expected to perform relay selection to Sidelink Relay 1. The test system can determine that the remote UE has selected a relay by monitoring the configured ProSe Direct Communication resource for the direct communication setup message to the relay UE.

During T4, the UE is expected to complete the direct communication setup with the relay UE. Note that the RSRP of the serving cell (cell 1) and the SD-RSRP of sidelink relay UEs is kept unchanged during T3. The period T3 ends when Sidelink Relay UE1 sends the direct communication accept message back to the remote UE.

During T5, SD-RSRP of Sidelink Relay UEs are modified such that the remote UE is expected to reselect to Sidelink Relay UE2.

Table A.7.5.12.1-1: Test parameters for selection / reselection of ProSe relay UE test for E-UTRAN FDD

Table A.7.5.12.1-2: ProSe Direct Discovery configuration for selection / reselection of ProSe relay UE test for E-UTRAN FDD

Table A.7.5.12.1-3: ProSe Direct Communication configuration for selection / reselection of ProSe relay UE test for E-UTRAN FDD

Table A.7.5.12.1-4: Sidelink Relay UE specific test parameters for selection / reselection of ProSe relay UE test for E-UTRAN FDD

Table A.7.5.12.1-5: Cell specific test parameters for interruptions due to ProSe Direct Communication on non-serving frequency test for E-UTRAN FDD-FDD

## A.7.5.12.2Test Requirements

Sidelink relay UE selection delay is defined as the time from the beginning of time period T3 to the moment when the UE selects the Sidelink Relay UE1 and transmits the PC5-SP direct communication setup message using ProSe Direct Communications.

The test system shall verify that the sidelink relay UE selection delay is less than 680ms.

NOTE:The sidelink relay UE selection delay can be expressed as (Tevaluate, ProSe_Relay_intra + 1 sc-period).

Sidelink relay UE reselection time is defined as the time from the beginning of time period T5 to the moment when the UE reselects to Sidelink relay UE2 and transmits the direct communication setup message using ProSe Direct Communications.

The test system shall verify that the sidelink relay UE reselection delay is less than 800ms.

NOTE:The sidelink relay UE reselection delay can be expressed as (Tmeasure,ProSe_Relay_Intra + Tevaluate, ProSe_Relay_intra + 1 sc-period).

## A.7.6Interruption for carrier aggregation

## A.7.6.1E-UTRAN FDD-TDD CA interruption at SRS carrier based switching

## A.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit periodic SRS, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will will verify the interruption requirements on PCC in clause 7.8.2.13

In the test there are two cells: cell1 and cell2. Cell1 is PCell on the FDD primary component carrier, Cell2 is activated SCell on the TDD secondary component carrier which operats in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 the UE shall be continuously scheduled on PCell. Immediately at the beginning of T2, a PDCCH with SRS-TPC-RNTI is sent to the UE to initiate SRS switching.

Table A.7.6.1.1-1: General test parameters for E-UTRAN FDD-TDD CA interruption at SRS carrier based switching

Table A.7.6.1.1-2: Cell specific test parameters for E-UTRAN FDD-TDD CA interruption at SRS carrier based switching

Table A.7.6.1.1-3: Sounding Reference Symbol Configuration for E-UTRAN FDD-TDD CA interruption at SRS carrier based switching

## A.7.6.1.2Test Requirements

The UE shall be continuously scheduled in PCell throughout the test and during the time duration T2, at most 6 ACK/NACK loss on PCell shall be detected.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.7.6.2E-UTRAN TDD-TDD CA interruption at SRS carrier based switching

## A.7.6.2.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit periodic SRS, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will will verify the interruption requirements on PCC in clause 7.8.2.13

In the test there are two cells: cell1 and cell2. Cell1 is PCell on the TDD primary component carrier, Cell2 is activated SCell on the TDD secondary component carrier which operats in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 the UE shall be continuously scheduled on PCell. Immediately at the beginning of T2, a PDCCH with SRS-TPC-RNTI is sent to the UE to initiate SRS switching.

Table A.7.6.2.1-1: General test parameters for E-UTRAN TDD-TDD CA interruption at SRS carrier based switching

Table A.7.6.2.1-2: Cell specific test parameters for E-UTRAN TDD-TDD CA interruption at SRS carrier based switching

Table A.7.6.2.1-3: Sounding Reference Symbol Configuration for E-UTRAN TDD-TDD CA interruption at SRS carrier based switching

## A.7.6.2.2Test Requirements

The UE shall be continuously scheduled in PCell throughout the test and during the time duration T2, at most 4 ACK/NACK loss on PCell shall be detected.

The rate of correct events observed during repeated tests shall be at least 90%.
