---
type: spec
aliases:
  - 38.133_38133-j50_sA.4-A.406
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.4-A.406/content.md"
---
# TS 38.133 38133-j50_sA.4-A.406

## A.4EN-DC tests with all NR cells in FR1

## A.4.1Void

## A.4.2Void

## A.4.3RRC_CONNECTED state mobility

## A.4.3.1Void

## A.4.3.2RRC Connection Mobility Control

## A.4.3.2.1Void

## A.4.3.2.2Random Access

## A.4.3.2.2.14-step RA type contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Supported test parameters are shown in table A.4.3.2.2.1.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.4.3.2.2.1.1-2.

Table A.4.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR1 for PSCell in EN-DC

Table A.4.3.2.2.1.1-2: General test parameters for contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via the dedicated signalling in the downlink.

A.4.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4, the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission..

A.4.3.2.2.1.2.5Void

A.4.3.2.2.1.2.6Void

A.4.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.4.3.2.2.24-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Supported test parameters are shown in table A.4.3.2.2.2.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.4.3.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.4.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR1 for PSCell in EN-DC

Table A.4.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.2.2Test Requirements

Non-contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.4.3.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2.. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.4.3.2.2.32-step RA type contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behaviour of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Supported test parameters are shown in table A.4.3.2.2.3.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.4.3.2.2.3.1-2.

Table A.4.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR1 for PSCell in EN-DC

Table A.4.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.4.3.2.2.3.2.1MsgA Transmission

To test the UE behaviour specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first MsgA preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.3.2.2MsgB Reception

To test the UE behaviour specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB with fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first MsgA preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB with fallbackRAR containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first MsgA preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.4.3.2.2.42-step RA type non-contention based random access test in FR1 for PSCell in EN-DC

A.4.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Supported test parameters are shown in table A.4.3.2.2.4.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.4.3.2.2.4.1-2.

Table A.4.3.2.2.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR1 for PSCell in EN-DC

Table A.4.3.2.2.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR1 for PSCell in EN-DC

A.4.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.4.3.2.2.4.2.1MsgA Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.4.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 5 MsgA transmissions have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power if Random Access Responses Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.4.3.2.2.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3 dB lower than first MsgA PRACH power for test configuration 1 & 2 and same as first MsgA PRACH power for test configuration 3 & 4 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.4.3.2.3Void

## A.4.3.3Handover with PSCell from EN-DC to EN-DC with known target PSCell in FR1

## A.4.3.3.1Test Purpose and Environment

This test is to verify the requirements for E-UTRA intra frequency handover with NR FR1 PSCell change specified in clause 5.8 in E-UTRA RRM specification [15] for the case when the target PSCell is known by the UE. Supported test configurations are shown in table A.4.3.3.1-1.

The general test parameters are given in table A.4.3.3.1-2. E-UTRA cells and NR cells specific test parameters are given in table A.4.3.3.1-3 and A.4.3.3.1-4. In the test there are four cells: Cell 1 and Cell 2 are PCell and target PCell on E-UTRA carrier, Cell 3 and Cell 4 are PSCell and target PSCell on NR FR1 carrier. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) and Cell 3 (NR PSCell) with EN-DC mode. At the start of time duration T1, the UE has not any timing information of cell 2 and cell 4. During T1, the UE is configured in the measurement control information that event-triggered reporting with Event A3 for neighbour cells on E-UTRA carrier and NR carrier.

The Cell 2 and Cell 4 becomes known to the UE, and E-UTRA PCell (Cell 1) shall send an RRC message implying handover with PSCell to cell 2 and cell4 during T2. The RRC message implying handover with PSCell shall be sent to the UE after the UE has reported Event A3 for SpCells. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover with PSCell.

Table A.4.3.3.1-1: Handover with PSCell from EN-DC to EN-DC test configurations in FR1

Table A.4.3.3.1-2: General test parameters for Handover with PSCell from EN-DC to EN-DC

Table A.4.3.3.1-3: E-UTRAN cell specific test parameters for Handover with PSCell from EN-DC to EN-DC

Table A.4.3.3.1-4: NR cell specific test parameters for Handover with PSCell from EN-DC to EN-DC

## A.4.3.3.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 60 ms from the beginning of time period T3.

The UE shall transmit the PRACH preamble to Cell 4 less than 87 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90%.

The rate of correct PSCell addition observed during repeated tests shall be at least 90%.

NOTE: The handover requirements for handover with PSCell for EN-DC is defined in clause 5.8 in [15] as:

DHOwithPSCel_PSCell = TRRC_delay + Tsearch + TIU + Tprocessing

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tsearch = 0 ms for known cell.

TIU = 15 ms in the test configuration.

Tprocessing = 25 ms for source Cell and target Cell are in the same FR.

This gives a total of 60 ms for handover delay.

NOTE: The PSCell change delay for handover with PSCell for EN-DC is defined in clause 5.8 in TS 36.133 [15] as:

DHOwithPSCel_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + TPCell_DU + 2 ms

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tprocessing = 25 ms for source Cell and target Cell are in the same FR.

Tsearch = 0 ms for known cell.

T∆ = 20 ms for fine time tracking and acquiring full timing information of the target cell. 1 SMTC period.

TPSCell_ DU = 20 ms based on PSCell addition test in TS 38.133 A.4.5.7.

TPCell_ DU = 0 ms, no clolliding with PCell RACH.

This gives a total of 87 ms for handover delay.

## A.4.4Timing

## A.4.4.1UE transmit timing

## A.4.4.1.1NR UE Transmit Timing Test for FR1

## A.4.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2. Supported test configurations are shown in table 4.4.1.1.1-1.

Table A.4.4.1.1.1-1: Supported test configurations for FR1 PSCell

The test consists of E-UTRA PCell and NR PSCell. The configuration for E-UTRA is given in clause A.3.7.2.1. Table A.4.4.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.4.4.1.1.1-3.

Table A.4.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.4.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

## A.4.4.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.1-1 and setup NR PSCell according to parameters given in table A.4.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset)×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.4.4.1.1.2-1

Table A.4.4.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.4.4.1.2NR UE Transmit Timing Test for two TRPs in FR1

## A.4.4.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timings change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for both TRPs. The test is configured with two TRPs in NR PSCell. This test will verify the requirements in clause 7.1.2. Supported test configurations are shown in table A.4.4.1.2.1-1.

Table A.4.4.1.2.1-1: Supported test configurations for FR1 PSCell

The test consists of E-UTRA PCell and NR PSCell. For NR PSCell, two TRPs are configured. The configuration for E-UTRA is given in A.3.7.2.1. Table A.4.4.1.2.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.4.4.1.2.1-3.

For UE not supporting the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test1 and Test3.

For UE supports the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test2 and Test4.

Table A.4.4.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.4.4.1.2.1-3: SRS Configuration for Timing Accuracy Test

## A.4.4.1.2.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.1-1 and setup NR PSCell according to parameters given in table A.4.4.1.2.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset)×Tc ± Te of the first detected path of DL SSB of TRP#1 and TRP#2.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.4.4.1.2.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.4.4.1.2.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB for TRP#1. For TRP#2, the test system shall verify there is no adjustment.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of TRP#1.

## A.4.4.1.3NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI

## A.4.4.1.3.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timings change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for UE not configured PL offset and is configured with 2 TAGs for

single-DCI multi-TRP operation. The test is configured with two TRPs in NR PSCell. This test will verify the requirements in clause 7.1.2. Supported test configurations are shown in table A.4.4.1.3.1-1.

Table A.4.4.1.3.1-1: Supported test configurations for FR1 PSCell

The test consists of E-UTRA PCell and NR PSCell. For NR PSCell, two TRPs are configured. The configuration for E-UTRA is given in A.3.7.2.1. Table A.4.4.1.3.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.4.4.1.3.1-3.

Table A.4.4.1.3.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.4.4.1.3.1-3: SRS Configuration for Timing Accuracy Test

## A.4.4.1.3.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.1-1 and setup NR PSCell according to parameters given in table A.4.4.1.3.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset)×Tc ± Te of the first detected corresponding path of DL SSB (index 0) for each TAG and detected another path of DL SSB (index 1).

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.4.4.1.3.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.4.4.1.3.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of corresponding DL SSB (TRP#1) of each TAG used by the UE to determine downlink timing is received from the reference cell at UE antenna. For TRP#2, the test system shall verify there is adjusted as well. Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of corresponding DL SSB of TRP#1 for each TAG. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.4.4.2UE timer accuracy

## A.4.4.3Timing advance

## A.4.4.3.1EN-DC FR1 timing advance adjustment accuracy

## A.4.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.4.4.3.1.2Test Parameters

Supported test configurations are shown in table A.4.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in tables A.4.4.3.1.2-2, A.4.4.3.1.2-3 and A.4.4.3.1.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and cell 2 is the PSCell is in the secondary Timing Advance Group (sTAG). Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.4.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for PSCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.4.4.3.1.2-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.4.4.3.1.2-1: Timing advance supported test configurations

Table A.4.4.3.1.2-2: General test parameters for timing advance

Table A.4.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.4.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.4.4.3.1.3Test Requirements

The UE shall apply the signalled Timing Advance value for PSCell in sTAG to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy for PSCell in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.4.4.3.2EN-DC FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs

## A.4.4.3.2.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3 for asymmetric DL sTRP/UL mTRP deployment with two TAs when PL-offset is configured joint/UL TCI state(s).

## A.4.4.3.2.2Test Parameters

Supported test configurations are shown in table A.4.4.3.2.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in tables A.4.4.3.2.2-2, A.4.4.3.2.2-3 and A.4.4.3.2.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and cell 2 is the PSCell is in the secondary Timing Advance Group (sTAG). The NR PSCell is configured with two TRPs (TRP1 and TRP2) in the test. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for two TRP are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.4.4.3.2.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for two TRP in the PSCell.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for each of the TAGs, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, 16 respectively for TRP1 and TRP2, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for TRP1 and TRP2 used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for both TRP, with Timing Advance Command value specified in table A.4.4.3.2.2-2. This value shall result in changes of the timing advance for TRP1 and TRP2 used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE for both TRPs.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.4.4.3.2.2-1: Timing advance supported test configurations

Table A.4.4.3.2.2-2: General test parameters for timing advance

Table A.4.4.3.2.2-3: Cell specific test parameters for timing advance

Table A.4.4.3.2.2-4: Sounding Reference Symbol Configuration for timing advance

## A.4.4.3.2.3Test Requirements

The UE shall apply the signalled Timing Advance value for TRP1 and TRP2  to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy for TRP1 and TRP2 shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90%.

## A.4.5Signaling characteristics

## A.4.5.1Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means uplink signal.

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means no uplink signal.

## A.4.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode

## A.4.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.1.1-1. The test parameters are given in tables A.4.5.1.1.1-2, A.4.5.1.1.1-3, and A.4.5.1.1.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.1.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.4.5.1.1.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

Table A.4.5.1.1.1-3: Cell specific test parameters for FR1 (Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.4.5.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.4.5.1.1.1-1: SNR variation for out-of-sync testing

## A.4.5.1.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 seconds after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.2Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode

## A.4.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.2.1-1. The test parameters are given in tables A.4.5.1.2.1-2, and A.4.5.1.2.1-3 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.1.2.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.4.5.1.2.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.4.5.1.2.1-3: Cell specific test parameters for FR1 (Cell 2) for in-sync radio link monitoring tests in non-DRX mode

Table A.4.5.1.2.1-4: Void

Figure A.4.5.1.2.1-1: SNR variation for in-sync testing

## A.4.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 seconds after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.3Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode

## A.4.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.3.1-1. The test parameters are given in tables A.4.5.1.3.1-2 and A.4.5.1.3.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.3.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.1.3.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.3.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.4.5.1.3.1-3: Cell specific test parameters for FR1 (Cell 2) for out-of-sync radio link monitoring tests in DRX mode

Table A.4.5.1.3.1-4: Void

Table A.4.5.1.3.1-5: Void

Figure A.4.5.1.3.1-1: SNR variation for out-of-sync testing

## A.4.5.1.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 seconds after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.4Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode

## A.4.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.4.1-1. The test parameters are given in tables A.4.5.1.4.1-2, and A.4.5.1.4.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.1.4.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.1.4.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.4.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.4.5.1.4.1-3: Cell specific test parameters for FR1 (Cell 2) for in-sync radio link monitoring tests in DRX mode

Table A.4.5.1.4.1-4: Void

Table A.4.5.1.4.1-5: Void

Figure A.4.5.1.4.1-1: SNR variation for in-sync testing

## A.4.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 seconds after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.5EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode

## A.4.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR1 PSCell CSI-RS out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.4.5.1.5.1-1, A.4.5.1.5.1-2, A.4.5.1.5.1-3, and A.4.5.1.5.1-3A below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.5.1-1 shows the variation of the downlink SNR in the E-UTRAN PCell and the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms). In the test, SSB0 is configured as the BFD-RS.

Table A.4.5.1.5.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.5.1-2: General test parameters for FR1 PSCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.4.5.1.5.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.4.5.1.5.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.4.5.1.5.1-4: Void

Figure A.4.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

## A.4.5.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 (PSCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

The UE shall stop transmitting uplink signal in Cell 2 (PSCell) no later than time point C (D1 after the start of the time duration T3) on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.6EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode

## A.4.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR1 PSCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.4.5.1.6.1-1, A.4.5.1.6.1-2, and A.4.5.1.6.1-3 below. There are two cells, cell 1which is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.1.6.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

Table A.4.5.1.6.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.6.1-2: General test parameters for FR1 PSCell for CSI-RS in-sync testing in non-DRX mode

Table A.4.5.1.6.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.4.5.1.6.1-3A: Void

Table A.4.5.1.6.1-4: Void

Figure A.4.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

## A.4.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.7EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode

## A.4.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR1 PSCell CSI-RS out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.4.5.1.7.1-1, A.4.5.1.7.1-2, and A.4.5.1.7.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.7.1-1 shows the variation of the downlink SNR in the E-UTRAN PCell and the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

Table A.4.5.1.7.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.7.1-2: General test parameters for FR1 PSCell for CSI-RS out-of-sync testing in DRX mode

Table A.4.5.1.7.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Table A.4.5.1.7.1-3A: Void

Table A.4.5.1.7.1-4: Void

Table A.4.5.1.7.1-5: Void

Table A.4.5.1.7.1-6: Void

Figure A.4.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

## A.4.5.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 (PSCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

The UE shall stop transmitting uplink signal in Cell 2 (PSCell) no later than time point C (D1 after the start of the time duration T3) on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.8EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode

## A.4.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used. This test will partly verify the FR1 PSCell CSI-RS in-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.4.5.1.8.1-1, A.4.5.1.8.1-2, A.4.5.1.8.1-3 and A.4.5.1.8.1-3A below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the NR PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.1.8.1-1 shows the variation of the downlink SNR in the PSCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity defined in CSI-RS configuration. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms). In the test, SSB0 is configured as the BFD-RS.

Table A.4.5.1.8.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.8.1-2: General test parameters for FR1 PSCell for CSI-RS in-sync testing in DRX mode

Table A.4.5.1.8.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in DRX mode

Table A.4.5.1.8.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in DRX mode

Table A.4.5.1.8.1-4: Void

Table A.4.5.1.8.1-5: Void

Table A.4.5.1.8.1-6: Void

Figure A.4.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.4.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PSCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion

## A.4.5.1.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements specified in clause 8.1.2.4 for UE fulfilling good serving cell quality criterion and low mobility criterion, if configured.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.9.1-1. The test parameters are given in tables A.4.5.1.9.1-2 and A.4.5.1.9.1-3. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.9.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.1.9.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.1.9.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.4.5.1.91-3: Cell specific test parameters for FR1 (Cell 2) for out-of-sync radio link monitoring tests in DRX mode

Figure A.4.5.1.9.1-1: SNR variation for out-of-sync testing

A.4.5.1.9.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 seconds after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.1.10EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP

## A.4.5.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PSCell when no DRX is used and when CD-SSB is outside active BWP. This test will partly verify the FR1 PSCell CSI-RS out-of-sync radio link monitoring requirements in clause 8.1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in clause A.4.5.1.5.

The test environment is the same as in clause A.4.5.1.5 with following exceptions in Table A.4.5.1.5.1-2.

The value of parameter “DL dedicated BWP configuration” is DLBWP.1.2. The value of parameter “UL dedicated BWP configuration” is ULBWP.1.2.

NOTE: The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as for A.4.5.1.5.2.

## A.4.5.1.11Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP

## A.4.5.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell when CD-SSB is outside active BWP. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1.

The test environment is the same as in clause A.4.5.1.1 with following exceptions in Table A.4.5.1.1.1-2.

## A.4.5.1.11.2Test Requirements

The test requirements are the same as in clause A.4.5.1.1.2.

## A.4.5.1.12EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

## A.4.5.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell for UE supporting FG 53-3. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.4.5.1.12.1-1. The test parameters are given in tables A.4.5.1.12.1-2, A.4.5.1.12.1-3, and A.4.5.1.12.1-4 below. There are two cells, Cell 1 is the E-UTRAN PCell, and Cell 2 is the PSCell, in the test. The E-UTRAN PCell setting refers to table A.3.7.2.1-1. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.4.5.1.12-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.4.5.1.12.1-1: Supported test configurations for FR1 PSCell for UE supporting NCD-SSB based measurement outside active BWP

Table A.4.5.1.12.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

Table A.4.5.1.12.1-3: Cell specific test parameters for FR1 (Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

Table A.4.5.1.12.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.4.5.1.12-1: SNR variation for out-of-sync testing

## A.4.5.1.12.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal in Cell 2 no later than time point C (D1 seconds after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2Interruption

## A.4.5.2.1E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

## A.4.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that when LTE PCell is in DRX and NR PSCell is in non-DRX, NR PSCell interruptions due to transitions from active to non-active and from non-active to active during LTE PCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in TS 38.133 clause 8. 2.1.2.1. Supported test configurations are shown in table A.4.5.2.1.1-1.

The general test parameters and NR cell specific test parameters are given in Tables A.4.5.2.1.1-2 and A.4.5.2.1.1-3. The E-UTRAN PCell DRX configuration parameters are given in Table A.4.5.2.1.1-2 below. And the E-UTRAN cell specific test parameters can refer to Table A.3.7.2.1-1. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is LTE PCell and Cell 2 is NR FR1 PSCell. The test consists of one time period, with duration of T1. During T1, NR PSCell is continuously scheduled in DL while LTE PCell is not scheduled and has DRX configured. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. Prior to start of T1 the DRX inactivity timer for the LTE PCell has already expired. During T1 the UE shall be continuously scheduled on NR PSCell while not scheduled on LTE PCell. CORESET indicating a new transmission on PSCell shall be sent continuously during the entire time duration to ensure UE would not enter DRX state on PSCell.

Table A.4.5.2.1.1-1: Interruption at transitions between active and non-active during DRX supported test configurations

Table A.4.5.2.1.1-2: General test parameters for E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

Table A.4.5.2.1.1-3: NR cell specific test parameters for E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC

Table A.4.5.2.1.1-4: Void

## A.4.5.2.1.2Test Requirements

The UE shall be continuously scheduled in NR PSCell during the entire length of T1. UE shall not be scheduled in LTE PCell during T1. During the time duration T1 the UE shall transmit at least 99% of ACK/NACK on NR PSCell.

Interruption on NR PSCell shall not exceed X slots as defined in Table A.4.5.2.1.2-1.

Table A.4.5.2.1.2-1: Interruption length X at transition between active and non-active during DRX

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.2E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

## A.4.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that when LTE PCell is in DRX and NR PSCell is in non-DRX, NR PSCell interruptions due to transitions from active to non-active and from non-active to active during LTE PCell DRX the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for NR PSCell in EN-DC specified in TS 38.133 clause 8.2.1.2.1. Supported test configurations are shown in table A.4.5.2.2.1-1.

The general test parameters and NR cell specific test parameters are given in Tables A.4.5.2.2.1-2 and A.4.5.2.2.1-3. The E-UTRAN PCell DRX configuration parameters are given in Table A.4.5.2.2.1-2 below. And the E-UTRAN cell specific test parameters can refer to Table A.3.7.2.1-1. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is LTE PCell and Cell 2 is NR FR1 PSCell. The test consists of one time period, with duration of T1. During T1, NR PSCell is continuously scheduled in DL while LTE PCell is not scheduled and has DRX configured. Prior to the start of the time duration T1, Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. Prior to start of T1 the DRX inactivity timer for the LTE PCell has already expired. During T1 the UE shall be continuously scheduled on NR PSCell while not scheduled on LTE PCell. PDCCH indicating a new transmission on PSCell shall be sent continuously during the entire time duration to ensure UE would not enter DRX state on PSCell.

Table A.4.5.2.2.1-1: Interruption at transitions between active and non-active during DRX supported test configurations

Table A.4.5.2.2.1-2: General test parameters for E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.4.5.2.2.1-3: NR cell specific test parameters for E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC

Table A.4.5.2.2.1-4: Void

## A.4.5.2.2.2Test Requirements

The UE shall be continuously scheduled in NR PSCell during the entire length of T1. UE shall not be scheduled in LTE PCell during T1. During the time duration T1 the UE shall transmit at least 99% of ACK/NACK on NR PSCell.

Interruption on NR PSCell shall not exceed X slots as defined in Table A.4.5.2.2.2-1.

Table A.4.5.2.2.2-1: Interruption length X at transition between active and non-active during DRX

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.3E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC

## A.4.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify E-UTRAN PCell and NR PSCell interruptions during the measurement on the deactivated NR SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for E-UTRAN PCell and NR PSCell in EN-DC specified in TS 38.133 clause 8.2.1.2. Supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.2.3.1-1. Supported test configurations for NR SCell are shown in table A.4.5.2.3.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in Tables A.4.5.2.3.1-2, A.4.5.2.3.1-3 and A.4.5.2.3.1-4 below. And the E-UTRAN cell specific test parameters can refer to Table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is LTE PCell, Cell 2 and Cell 3 is NR PSCell and NR deactivated SCell. Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During T1, LTE PCell and NR PSCell are continuously scheduled in DL

Table A.4.5.2.3.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations for LTE PCell and NR PSCell

Table A.4.5.2.3.1-1A: Interruptions during measurements on deactivated NR SCC supported test configurations for NR SCell

Table A.4.5.2.3.1-2: General test parameters for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in synchronous EN-DC

Table A.4.5.2.3.1-3: NR cell specific test parameters for NR PSCell for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in synchronous EN-DC

Table A.4.5.2.3.1-4: NR cell specific test parameters for NR SCell for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in synchronous EN-DC

## A.4.5.2.3.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5% of ACK/NACK on NR PSCell.

If the NR PSCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PSCell immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.4.5.2.3.2-1.

If the NR PSCell is in the same band as the deactivated SCell, the UE is only allowed to cause an interruption on PSCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PSCell shall not exceed the value defined in Table A.4.5.2.3.2-2.

Table A.4.5.2.3.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.4.5.2.3.2-2: Interruption duration if the NR PSCell is in the same band as the deactivated SCell

For synchronous inter-band EN-DC, the UE is only allowed to cause interruptions on E-UTRA PCell immediately before and immediately after an SMTC. Each interruption on E-UTRA PCell shall not exceed 1 subframe.

For synchronous intra-band EN-DC, the UE is only allowed to cause an interruption on E-UTRA PCell no earlier than 1 subframe before an SMTC and no later than 1 subframe after the SMTC. The interruption on E-UTRA PCell shall not exceed SMTC duration + 2 subframes.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.4E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

## A.4.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify E-UTRAN PCell and NR PSCell interruptions during the measurement on the deactivated NR SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for E-UTRAN PCell and NR PSCell in EN-DC specified in TS 38.133 clause 8.2.1.2.5. Supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.2.4.1-1. Supported test configurations for NR SCell are shown in table A.4.5.2.4.1-1. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in Tables A.4.5.2.4.1-2, A.4.5.2.4.1-3 and A.4.5.2.4.1-4 below. And the E-UTRAN cell specific test parameters can refer to Table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is LTE PCell, Cell 2 and Cell 3 is NR PSCell and NR deactivated SCell. Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.4.5.2.4.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations for LTE PCell and NR PSCell

Table A.4.5.2.4.1-1A: Interruptions during measurements on deactivated NR SCC supported test configurations for NR SCell

Table A.4.5.2.4.1-2: General test parameters for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

Table A.4.5.2.4.1-3: NR cell specific test parameters for NR PSCell for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

Table A.4.5.2.4.1-4: NR cell specific test parameters for NR SCell for E-UTRAN – NR interruptions during measurements on deactivated NR SCC in asynchronous EN-DC

## A.4.5.2.4.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5% of ACK/NACK on NR PSCell.

If the NR PSCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PSCell immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in table A.4.5.2.4.2-1.

If the NR PSCell is in the same band as the deactivated SCell, the UE is only allowed to cause an interruption on PSCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PSCell shall not exceed the value defined in Table A.4.5.2.4.2-2.

Table A.4.5.2.4.2-1: Interruption duration if the NR PSCell is not in the same band as the deactivated SCell

Table A.4.5.2.4.2-2: Interruption duration if the NR PSCell is in the same band as the deactivated SCell

For asynchronous inter-band EN-DC, the UE is only allowed to cause interruptions on E-UTRA PCell immediately before and immediately after an SMTC. Each interruption on E-UTRA PCell shall not exceed 2 subframe.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.5E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC

## A.4.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify E-UTRAN PCell and NR PSCell interruptions during the measurement on the deactivated E-UTRAN SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for E-UTRAN PCell and NR PSCell in EN-DC specified in TS 38.133 clause 8.2.1.2.5. Supported test configurations are shown in table A.4.5.2.5.1-1.

The general test parameters and NR cell specific test parameters are given in table A.4.5.2.5.1-2 and A.4.5.2.5.1-3 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 and Cell 3 is E-UTRAN PCell and E-UTRAN deactivated SCell, Cell 2 is NR FR1 PSCell. Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated E-UTRAN SCells is received at the UE antenna connector. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.4.5.2.5.1-1: Interruptions during measurements on deactivated E-UTRAN SCC supported test configurations

Table A.4.5.2.5.1-2: General test parameters for E-UTRAN – NR interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC

Table A.4.5.2.5.1-3: NR cell specific test parameters for E-UTRAN – NR interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC

## A.4.5.2.5.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5% of ACK/NACK on NR PSCell. The UE is only allowed to cause interruptions immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed X defined in Table A.4.5.2.5.2-1 if the NR PSCell is not in the same band as the E-UTRAN deactivated SCell or Y in Table A.4.5.2.5.2-1 if the NR PSCell is in the same band as the E-UTRAN deactivated SCell.

Table A.4.5.2.5.2-1: Interruption length X and Y at measurements on deactivated E-UTRA SCC

Each interruption on E-UTRAN PCell shall not exceed 1 subframe if the PCell is not in the same band as the deactivated SCell, or 5 subframes if the PCell is in the same band as the deactivated SCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.6E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC

## A.4.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify E-UTRAN PCell and NR PSCell interruptions during the measurement on the deactivated NR SCC, the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for E-UTRAN PCell and NR PSCell in EN-DC specified in TS 38.133 clause 8.2.1.2.5. Supported test configurations are shown in table A.4.5.2.6.1-1.

The general test parameters and NR cell specific test parameters are given in table A.4.5.2.6.1-1 and A.4.5.2.6.1-2 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 and Cell 3 is E-UTRAN PCell and E-UTRAN deactivated SCell, Cell 2 is NR FR1 PSCell. Cell 1 shall be configured as LTE PCell and Cell 2 shall be configured as NR PSCell. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

T antenna connector. During T1, LTE PCell and NR PSCell are continuously scheduled in DL.

Table A.4.5.2.6.1-1: Interruptions during measurements on deactivated E-UTRAN SCC supported test configurations

Table A.4.5.2.6.1-2: General test parameters for E-UTRAN – NR interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC

Table A.4.5.2.6.1-3: NR cell specific test parameters for E-UTRAN – NR interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC

## A.4.5.2.6.2Test Requirements

The UE shall be continuously scheduled in LTE PCell and NR PSCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5% of ACK/NACK on E-UTRAN PCell and NR PSCell. The UE is only allowed to cause interruptions immediately before and immediately after an SMTC. Each interruption on NR PSCell shall not exceed the value defined in Table A.4.5.2.6.2-1 and Table A.4.5.2.6.2-2.

Table A.4.5.2.6.2-1: Interruption duration if the NR PSCell is not in the same band as the E-UTRAN deactivated SCell

Table A.4.5.2.6.2-2: Interruption duration if the NR PSCell is in the same band as the E-UTRAN deactivated SCell

Each interruption on E-UTRAN PCell shall not exceed 1 subframe if the PCell is not in the same band as the deactivated SCell, or 5 subframes if the PCell is in the same band as the deactivated SCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.7Void

## A.4.5.2.8E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC

## A.4.5.2.8.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS, the UE can perform carrier based switching to one carrier not configured for PUCCH/PUSCH transmission from a CC with PUCCH/PUSCH transmission. The test will verify the UE missed ACK/NACK does not exceed the interruption requirements on E-UTRAN PCell and NR PSCell in clause 8.2.1.2.12. Supported test configurations are shown in table A.4.5.2.8.1-1.

The general test parameters and NR cell specific test parameters are given in Table A.4.5.2.8.1-2 and A 4.5.2.8.1-3 below. And the E-UTRAN cell specific test parameters can refer to Table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is E-UTRAN PCell, Cell 2 is NR PSCell in FR1 with PUCCH/PUSCH transmission, and Cell 3 is an activated NR SCell in FR1 which operates in downlink without PUCCH/PUSCH transmission. The UE is configured with the SRS carrier based switching between PSCell and SCell.

The test consists of two successive time periods, with duration of T1 and T2, respectively. Throughout the test the UE shall be continuously scheduled on PCell and PSCell. Immediately at the beginning of T2, a PDCCH with TPC-SRS-RNTI is sent to the UE to initiate NR SRS switching.

Table A.4.5.2.8.1-1: Interruptions at SRS carrier switching supported test configurations in FR1

Table A.4.5.2.8.1-2: General test parameters for E-UTRAN – NR FR1 interruptions at SRS carrier based switching in asynchronous EN-DC

Table A.4.5.2.8.1-3: NR Cell specific test parameters for E-UTRAN – NR FR1 interruptions at SRS carrier based switching in asynchronous EN-DC

Table A.4.5.2.8.1-4:  Void

## A.4.5.2.8.2Test Requirements

During the time duration T2, the missed ACK/NACK interruption on NR PSCell during the switching from NR PSCell to NR SCell shall not exceed the value as defined in table A.4.5.2.8.2-1 dependent on the applied SRS carrier switching time.

Table A4.5.2.8.2-1: Interruption length on NR active serving cells at NR SRS carrier switching (slot)

During the time duration T2, the missed ACK/NACK interruption on E-UTRAN PCell during the switching from NR PSCell to NR SCell shall not exceed the value as defined in table A.4.5.2.8.2-2 dependent on the applied SRS carrier switching time.

Table A4.5.2.8.2-2: Interruption length on E-UTRAN active serving cells at NR SRS carrier switching

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.9E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching

## A.4.5.2.9.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS on a PUSCH-less carrier of SCell, the UE can perform carrier based switching to one PUSCH-less SCCs from a CC with PUSCH. The test will verify the UE missed ACK/NACK does not exceed the interruption requirements on active serving cell in SCG in clause 8.2.1.2.13. Supported test configurations are shown in table A.4.5.2.9.1-1.

In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is E-UTRAN PCell on the primary component carrier. Cell 3 is E-UTRAN SCell on the TDD secondary component carrier which operates in downlink without PUCCH/PUSCH. Cell 2 is NR FR1 PSCell. The UE is configured with the SRS switching between E-UTRAN PCell and E-UTRAN SCell. The general test parameters, NR cell specific test parameters and E-UTRA SRS configurations are given in table A.4.5.2.9.1-2, A.4.5.2.9.1-3 and table A.4.5.2.9.1-4 below. And the E-UTRAN cell specific test parameters (for Cell 1 and Cell 3) can refer to table A.3.7.2.1-1. The test consists of two successive time periods, with duration of T1 and T2, respectively. During T1 LTE PCell and NR PSCell are continuously scheduled in DL. Immediately at the beginning of T2, the UE is triggered for SRS switching by DCI 2_3 scheduling. After T2, the UE is expected to transmit aperiodic SRS on a special slot in the configured TDD UL/DL configuration, as scheduled by DCI 2_3.

Table A.4.5.2.9.1-1: E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching supported test configurations

Table A.4.5.2.9.1-2: General test parameters for E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching

Table A.4.5.2.9.1-3: NR cell specific test parameters for E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching

Table A.4.5.2.9.1-4: Sounding Reference Symbol Configuration for E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching

## A.4.5.2.9.2Test Requirements

The UE shall be continuously scheduled in NR PSCell throughout the test and during the time duration T2. Each missed ACK/NACK interruption on NR PSCell shall not exceed X defined in Table A.4.5.2.9.2-1.

Table A.4.5.2.9.2-1: Interruption length X (slot) E-UTRAN – NR at E-UTRA SRS carrier based switching

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.10E-UTRAN – NR FR1 interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell

## A.4.5.2.10.1Test Purpose and Environment

The purpose of this test is to verify E-UTRAN PCell interruptions due to RRM measurements and RLM/BFD measurements on the deactivated NR PSCell, and the UE missed ACK/NACK does not exceed the limits. This test will verify the missed ACK/NACK rate for E-UTRAN PCell in EN-DC according to the requirements specified in TS 36.133 [15] clause 7.32.2.20 for RRM measurements, and BFD measurements. Supported test configurations are shown in table A.4.5.2.10.1-1.

The general test parameters and NR cell specific test parameters are given in Tables A.4.5.2.10.1-2 and A.4.5.2.10.1-3 below. And the E-UTRAN cell specific test parameters can be referred to in Table A.3.7.2.1-1. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is E-UTRAN PCell, and Cell 2 is deactivated NR FR1 PSCell. The test consists of one single period, T1.

Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2. At the start of T1, the RRC message including measCyclePSCell or allowInterruptions is received at the UE antenna connector and Cell 2 is deactivated. During T1, Cell 1 continuously schedules data in DL and the UE is configured with RRM and bfd-and-RLM measurements on the deactivated Cell 2. It is assumed that Cell 1 and Cell 2 are synchronized with a timing difference not larger than 3 ms between the two cells.

Table A.4.5.2.10.1-1: Interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell supported test configurations

Table A.4.5.2.10.1-2: General test parameters for E-UTRAN – NR interruptions due to measurements on deactivated PSCell in synchronous EN-DC

Table A.4.5.2.10.1-3: NR cell specific test parameters for E-UTRAN – NR interruptions due to measurements on deactivated PSCell in synchronous EN-DC

## A.4.5.2.10.2Test Requirements

The UE shall be continuously scheduled in Cell 1 during the entire length of T1 and the UE is configured with RRM and RLM/BFD measurements on the deactivated Cell 2. During the time duration T1 the UE shall transmit at least 98.5% of ACK/NACK on E-UTRAN PCell.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.11E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC

## A.4.5.2.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE can perform SRS antenna port switching when the UE is configured with the higher layer parameter usage in SRS-ResourceSet set as 'antennaSwitching'. The test will verify the interruption requirements on E-UTRAN PCell and NR PSCell at SRS antenna switching in synchronous EN-DC as specified in table 8.2.1.2.18-1 of clause 8.2.1.2.18. Supported test configurations for LTE PCell, NR PSCell and NR SCell are shown in table A.4.5.2.11.1-1. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in table A.4.5.2.11.1-2 and A 4.5.2.11.1-3 below. The dedicated SRS configuration for antenna port switching with 1 SRS symbol in a slot is given in table A 4.5.2.11.1-4 and Table A 4.5.2.11.1-5. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is E-UTRAN PCell, Cell 2 is NR PSCell in FR1 and Cell 3 is an activated NR SCell in FR1. The UE is configured with SRS antenna port switching on NR PSCell.

The test consists of two successive time periods, with duration of T1 and T2, respectively. Throughout the test the UE shall be continuously scheduled on PCell and SCell. Immediately at the beginning of T2, a PDCCH with TPC-SRS-RNTI is sent to the UE to initiate NR SRS switching.

Table A.4.5.2.11.1-1: Interruptions at SRS antenna port switching supported test configurations in FR1 for LTE PCell and NR PSCell

Table A.4.5.2.11.1-1A: Void

Table A.4.5.2.11.1-1A: Interruptions at SRS antenna port switching supported test configurations for NR SCell

Table A.4.5.2.11.1-2: General test parameters for E-UTRAN – NR FR1 interruptions at SRS antenna port switching in synchronous EN-DC

Table A.4.5.2.11.1-3: NR Cell specific test parameters for E-UTRAN – NR FR1 interruptions at SRS antenna port switching in synchronous EN-DC

Table A.4.5.2.11.1-4: SRSConf.1 Dedicated SRS Configuration for antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC

Table A.4.5.2.11.1-5: SRSConf.2 Dedicated SRS Configuration for antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC

## A.4.5.2.11.2Test Requirements

In the test, the interruption is verified by monitoring ACK/NACK sent in E-UTRAN PCell and NR SCell during the SRS antenna switching on NR PSCell.

During the time duration T2, the DL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PSCell shall not exceed 1 slot if SCell is indicated in txSwitchImpactToRx, and the UL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PSCell shall not exceed 1 slot if SCell is indicated in txSwitchWithAnotherBand. Otherwise, the NR SCell shall not be interrupted.

During the time duration T2, the DL interruption on E-UTRAN PCell during the SRS antenna switching in each SRS transmission slot on NR PSCell shall not exceed 1 subframe if PCell is indicated in txSwitchImpactToRx, and the UL interruption on E-UTRAN PCell during the SRS antenna switching in each SRS transmission slot on NR PSCell shall not exceed 1 subframe if SCell is indicated in txSwitchWithAnotherBand. Otherwise, the EUTRAN PCell shall not be interrupted.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.2.12E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching in asynchronous EN-DC

## A.4.5.2.12.1Test Purpose and Environment

The purpose of this test is to verify the interruption during NR SRS antenna port switching on E-UTRAN PCell and NR SCell in TS 36.133 [15] clause 7.32.2.18 and clause 8.2.1.2.18. Supported test configurations for LTE PCell, NR PSCell and NR SCell are shown in table A.4.5.2.12.1-1. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in table A.4.5.2.12.1-2, A.4.5.2.12.1-3 and A.4.5.2.12.1-4 below. And the E-UTRAN cell specific test parameters can refer to table A.3.7.2.1-1. In the test there are three cells: Cell 1, Cell 2 and Cell 3. Cell 1 is E-UTRAN PCell, Cell 2 is NR PSCell in FR1, Cell 3 NR SCell in FR1. The UE is configured with the SRS antenna port switching on Cell 2.

The test consists of two time period, with duration of T1 and T2. Prior to the start of the time duration T1, the UE is connected to Cell 1, Cell 2 and Cell 3. LTE PCell and NR PSCell are continuously scheduled in DL during T1 and T2. UE receives RRC message to trigger periodic SRS for antenna switching and it ready for SRS antenna switching before T2.

Table A.4.5.2.12.1-1: Interruptions at SRS antenna port switching supported test configurations in FR1 for LTE PCell and NR PSCell

Table A.4.5.2.12.1-1A: Void

Table A.4.5.2.12.1-1A: Interruptions at SRS antenna port switching supported test configurations for NR SCell

Table A.4.5.2.12.1-2: General test parameters for E-UTRAN – NR FR1 interruptions at SRS antenna port switching in asynchronous EN-DC

Table A.4.5.2.12.1-3: NR Cell specific test parameters for E-UTRAN – NR FR1 interruptions at SRS antenna port switching in asynchronous EN-DC for NR PSCell

Table A.4.5.2.12.1-4: NR Cell specific test parameters for E-UTRAN – NR FR1 interruptions at SRS antenna port switching in asynchronous EN-DC for NR SCell

Table A.4.5.2.12.1-5: SRSConf.1 Dedicated SRS Configuration for antenna port switching

Table A.4.5.2.12.1-6: SRSConf.2 Dedicated SRS Configuration for antenna port switching

A.4.5.2.12.2Test Requirements

The UE shall be scheduled on Cell 1 and Cell 3 continuously throughout the test. During the time duration T2, the interruption on Cell 1 shall not be more than the values specified in clause 7.32.2.18 in TS 36.133 [15] for each SRS transmission slot, and the interruption on Cell 3 shall not be more than the values specified in clause 8.2.1.2.18 for each SRS transmission slot

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.3SCell Activation and Deactivation Delay

## A.4.5.3.1SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle

## A.4.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.3.1.1-1 below. Supported test configurations for NR SCell are shown in table A.4.5.3.1.1-1A below. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently. The test parameters are given in Tables A.4.5.3.1.1-2 and cell-specific parameters in table A.4.5.3.1.1-3 and A.4.5.3.1.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. The UE now starts monitoring the SCell. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3. The starting point of any PSCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3. The starting point of any E-UTRA PCell interruption due to the deactivation shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n.n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe lengthn1n2

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.4.5.3.1.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for LTE PCell and NR PSCell

Table A.4.5.3.1.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.4.5.3.1.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.1.1-3: Cell specific test parameters for NR PSCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.1.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.4.5.3.1.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PCell in slot (m+k).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstSSB+ 5 ms, as defined in clause 8.3.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruptionm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruption

During T3 the starting point of interruption of PSCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3 and the starting point of interruption of E-UTRA PCell during SCell deactivation shall not happen outside the subframe  to subframe .n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe length

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.4.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90%.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.4.5.3.2SCell Activation and deactivation of known SCell in FR1 for 640 ms SCell measurement cycle

## A.4.5.3.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.4.5.3.1.1. The supported test configurations are the same as defined in clause A.4.5.3.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.4.5.3.2.1-1 will replace the values of corresponding parameters in tables A.4.5.3.1.1-2.

Table A.4.5.3.2.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

## A.4.5.3.2.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + Trs + 5 ms.

## A.4.5.3.3SCell Activation and deactivation of unknown SCell in FR1

## A.4.5.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is unknown by the UE at the time of activation.

The supported test configurations are defined in clause A.4.5.3.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.4.5.3.3.1-1 will replace the values of corresponding parameters in tables A.4.5.3.1.1-2. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. The UE shall be able to report valid CSI for the activated SCell at latest in slot   as defined in clause 8.3 provided the SCell can be successfully detected on the first attempt. The UE shall start reporting CSI after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell at latest in slot  as defined in clause 8.3. The starting point of any PSCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3. The starting point of any E-UTRA PCell interruption due to the deactivation shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n.n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe lengthn1n2

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.4.5.3.3.1-1: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.4.5.3.3.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5 ms as defined in clause 8.3.

## A.4.5.3.4SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command

## A.4.5.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the multiple SCell activation and deactivation times are within the requirements stated in clause 8.3.7 and 8.3.8, when the two configured deactivated SCells in FR1 are unknown by the UE at the time of activation.

The supported test configurations are the same as defined in clause A.4.5.3.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in table A.4.5.3.4.1-1 will replace the values of corresponding parameters in table A.4.5.3.1.1-2. The cell specific test parameter values in table A.4.5.3.4.1-2 will replace the values of corresponding parameters in table A.4.5.3.1.1-3.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are four carriers, E-UTRA has one cell, and NR has three cells. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) and Cell 4(SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCells (Cell 3 and Cell 4) become configured on NR. During T1 the SCells (Cell 3 and Cell 4) are powered off and UE is not aware of SCells.

A MAC message for activation of SCells(Cell 3 and Cell 4) is sent by the test equipment 100ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCells is received at the UE antenna connector defines the start of time period T2. Immediately at beginning of T2 the transmission power of cell 3 and cell 4 are increased to same level as for cell 2. The UE shall be able to report valid CSI for the activated SCells (Cell 3 and Cell 4) at latest in slot   respectively as defined in clause 8.3.7 provided the SCells can be successfully detected on the first attempt. The UE shall start reporting CSI for cell 3 and cell 4 after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation for cell 3 and cell 4 has been completed, respectively. Any PSCell interruption due to activation of SCells shall occur in the slot  to slot, as defined in clause 8.3, where  is the interruption length given in section 8.2. Any E-UTRA PCell interruption due to activation of SCells shall occur in the subframe  to subframe, where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and   is the interruption length given in TS 36.133 [15] clause 7.32.m+THARQ+Tactivation_time_multiple_scells+TCSI_ReportingNR slot lengthm+1+THARQNR slot length m+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruption m1+1+THARQEUTRA slot length m2+1+THARQ+3ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

Time period T3 starts when a MAC message for deactivation of the SCells (Cell 3 and Cell 4), sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCells at latest in slot   as defined in clause 8.3. The starting point of any PSCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3. The starting point of any E-UTRA PCell interruption due to the deactivation shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n.n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe lengthn1n2

The test equipment verifies the activation time for Cell 3 by counting the slots from the time when the SCell activation command is sent until CSI report of activated Cell 3 with other than CQI index 0 is received.

The test equipment verifies the activation time for Cell 4 by counting the slots from the time when the SCell activation command is sent until CSI report of activated Cell 4 with other than CQI index 0 is received.

The test equipment verifies the deactivation time for Cell 3 by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for Cell 3 is discontinued.

The test equipment verifies the deactivation time for Cell 4by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for Cell 4 is discontinued.

Table A.4.5.3.4.1-1: General test parameters for unknown FR1 SCell activation case with 2 deactivated SCells, 160 ms SCell measurement cycle

Table A. 4.5.3.4.1-2: Cell specific test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.4.5.3.4.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case for both Cell 3 and Cell 4, except the followings:

-For Cell 3 activation delay, Tactivation_time will be replaced with the value = TFirstSSB_MAX_multiple_scells + TSMTC_MAX_multiple_scells+Trs +5 ms as defined in clause 8.3.7.Tactivation_time_multiple_scells

-For Cell 4 activation delay, Tactivation_time will be replaced with the value = TFirstSSB_MAX_multiple_scells + TSMTC_MAX_multiple_scells+2*Trs +5 ms as defined in clause 8.3.7.Tactivation_time_multiple_scells

## A.4.5.3.5Direct SCell activation at SCell addition of known SCell in FR1

## A.4.5.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the direct SCell activation time is within the requirements stated in clause 8.3.4, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.3.5.1-1 below. The supported test configurations for NR SCell are shown in table A.4.5.3.5.1-1A below. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.4.5.3.5.1-2 and cell-specific parameters in A.4.5.3.5.1-3 and A.4.5.3.5.1-4 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the measurement on Cell 3 is configured. The UE now starts measuring the Cell 3. During T1, Cell 3 should be detected and measured by the UE such that it meets the condition for known cell defined in clause 8.3.4 for direct SCell activation. At the end of T1, the test equipment sends an RRC message for direct SCell activation of the Cell 3.

The point in time at which the RRC message for direct SCell activation is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3.4. The UE shall start reporting CSI in PSCell in slot (m+k+TRRC_process) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3.4, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+NdirectNR slot lengthm+1m+1+TRRC_Process+T1+TXNR slot length+NinterruptionNinterruptionm1+1m2+1+TRRC_Process+T1+TXNR slot length+Ninterruptionm1m2Ninterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the direct SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.4.5.3.5.1-1: known FR1 direct SCell activation supported test configurations for LTE PCell and NR PSCell

Table A.4.5.3.5.1-1A: known FR1 direct SCell activation supported test configurations for NR SCell

Table A.4.5.3.5.1-2: General test parameters for known FR1 direct SCell activation

Table A.4.5.3.5.1-3: Cell specific test parameters for NR PSCell for known FR1 direct SCell activation

Table A.4.5.3.5.1-4: Cell specific test parameters for NR SCell for known FR1 direct SCell activation

## A.4.5.3.5.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k+TRRC_process). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k+TRRC_process) was interrupted is checked by monitoring ACK/NACK sent in PCell in slot (m+k+TRRC_process).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot . Ndirect = TRRC_Process + T1 + Tactivation_time + TCSI_Reporting - 3 ms, where TRRC_Process = 20 ms and other components are defined in clause 8.3.4.m+NdirectNR slot length

During T2 interruption of PSCell during direct SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.4.m+1m+1+TRRC_Process+T1+TXNR slot length+Ninterruptionm1+1 m2+1+TRRC_Process+T1+TXNR slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.8.

All of the above test requirements shall be fulfilled in order for the observed direct SCell activation delay to be counted as correct. The rate of correct observed direct SCell activation delay during repeated tests shall be at least 90%.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3.4 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+TRRC_Process+T1+TXNR slot length

## A.4.5.3.6Fast SCell Activation of known SCell in FR1 for 160 ms SCell measurement cycle

## A.4.5.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the fast SCell activation times are within the requirements stated in clause 8.3.16, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.4.5.3.6.1-1 below. The test parameters are given in tables A.4.5.3.6.1-2 and cell-specific parameters in A.4.5.3.6.1-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. The UE now starts monitoring the SCell. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.4.5.3.6.1-1: fast known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.4.5.3.6.1-2: General test parameters for fast known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.6-3: Cell specific test parameters for fast known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.4.5.3.6.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PCell in slot (m+k).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstATRS + 5 ms, as defined in clause 8.3.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruptionm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.19.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90%.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.4.5.3.7Fast SCell Activation of known SCell in FR1 for 640 ms SCell measurement cycle

## A.4.5.3.7.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.4.5.3.6.1. The supported test configurations are the same as defined in clause A.4.5.3.6.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.4.5.3.7.1-1 will replace the values of corresponding parameters in tables A.4.5.3.6.1-2. The listed parameter values in tables A.4.5.3.7.1-2 will replace the values of corresponding parameters in tables A.4.5.3.6.1-3.

Table A.4.5.3.7.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

Table A.4.5.3.7-2: Cell specific test parameters for known FR1 Scell activation case, 640 ms Scell measurement cycle

## A.4.5.3.7.2Test Requirements

The test requirements defined in clause A.4.5.3.6.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstATRS + Tgap + TATRS+ 5 ms.

## A.4.5.3.8SCell Activation and deactivation of unknown SCell in FR1 for UE capable of short measurement interval

## A.4.5.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is unknown by the UE at the time of activation and when UE supports shortMeasInterval-r18 capability.

The supported test configurations are defined in clause A.4.5.3.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in Tables A.4.5.3.8.1-1 will replace the values of corresponding parameters in Tables A.4.5.3.1.1-2. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell, and NR has two cells. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. The UE shall be able to report valid CSI for the activated SCell at latest in slot   as defined in clause 8.3 provided the SCell can be successfully detected on the first attempt. The UE shall start reporting CSI after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell at latest in slot  as defined in clause 8.3. The starting point of any PSCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3. The starting point of any E-UTRA PCell interruption due to the deactivation shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n.n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 msNR slot lengthn1+1+THARQEUTRA subframe lengthn2+1+THARQ+3 msEUTRA subframe lengthn1n2

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.4.5.3.8.1-1: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.4.5.3.8.2Test Requirements

The test requirements defined in clause A.4.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value below as defined in clause 8.3.2 when UE supports shortMeasInterval-r18 capability:

Tactivation_time = 3 ms + TFirstSSB_MAX, enhanced + TSMTC_MAX, enhanced + Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP ,report + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay), for which TFirstSSB_MAX, enhanced = TSMTC_MAX, enhanced = Trs, enhanced =20 ms; TL1-RSRP, enhanced_measure = 60 ms and TL1-RSRP, report=5 ms.

## A.4.5.3.9SCell Activation of unknown SCell with valid L3 measurement results in FR1 for 160 ms SCell measurement cycle

## A.4.5.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation time are within the requirements stated in clause 8.3.17, when the SCell in FR1 is unknown by the UE at the time of activation, but UE has valid L3 measurement results of the SCell.

The supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.3.9.1-1 below. Supported test configurations for NR SCell are shown in table A.4.5.3.9.1-1A below. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently. The test parameters are given in Tables A.4.5.3.9.1-2 and cell-specific parameters in A.4.5.3.9.1-3 and A.4.5.3.9.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, E-UTRA has one cell, and NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell.

The test consists of three sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n. TE continuously schedules the downlink data to UE on PCell and PSCell. TE shall schedule DCI format 0_1 at slot n + . In Sub-test 2, TE shall schedule DCI format 0_1 at slot n + , where M is defined in 8.3.17 and k2 = 1. In Sub-test 3, UE shall tranmsit scheduling request on the first SR resource by 7ms+ THARQ + TSR_Periodicity to obtain the UL grant for L3 report transmission.THARQ+7msNR slot lengthTHARQ+3ms+M-k2NR slot length

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. The UE now starts monitoring the SCell. T1 is sufficiently long enough so that UE is able to complete the L3 detection and measurements on the SCell to be activated. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. UE is expected to report L3 measurement result at the first PUSCH scheduled by TE.

The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3. TE shall also indicate the TCI based on L3 report of the UE. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. m+THARQ+Tactivation_time+TCSI_ReportingNR slot length

During T2, any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment. T3 shall be long enough to ensure UE completes the SCell de-activation.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.4.5.3.9.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for LTE PCell and NR PSCell

Table A.4.5.3.9.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.4.5.3.9.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.9.1-3: Cell specific test parameters for NR PSCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.9.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.4.5.3.9.1-5: Scheduling request parameters

## A.4.5.3.9.2Test Requirements

During T2, the UE shall send the first CSI report for SCell in the first available uplink resource after slot (). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption. m+1+THARQ+3 msNR slot length

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

For Sub-test 1, Tactivation_time = 7 ms + k2/SCS + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17, where k2/SCS is 1 ms for config 1,2 and 0.5 ms for config 3.

For Sub-test 2, Tactivation_time = 3 ms + M + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17.

For Sub-test 3, [Tactivation_time = 7ms + Tuncertainity_ULgrant + max (THARQ + Tuncertainty_MAC + 5ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17. Where, Tuncertainity_ULgrant is uncertainty in acquiring UL grant after sending scheduling request].

During T2, interruption of PSCell during SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruptionm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.4.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90%.

NOTE:During T2, if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.4.5.3.10SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation command in non-DRX

## A.4.5.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the multiple SCell activation times are within the requirements stated in clause 8.3.18 when the two configured deactivated SCells in FR1 are unknown by the UE at the time of activation.

The supported test configurations for LTE PCell, NR PSCell and NR SCell are the same as defined in clause A.4.5.3.9.1. The test parameters are the same except those described in the following clause. The listed parameter values in table A.4.5.3.10.1-1 will replace the values of corresponding parameters in table A.4.5.3.9.1-2. The cell specific test parameter values in table A.4.5.3.10.1-2 will replace the values of corresponding parameters in table A.4.5.3.9.1-3.

The test consists of two successive time periods, with duration of T1 and T2, respectively. There are four carriers, E-UTRA has one cell, and NR has three cells. Cell 1 and Cell 2 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRAN and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) and Cell 4 (SCell) on NR. The UE is monitoring the PCell and PSCell. TE continuously schedules the downlink data to UE on PCell and PSCell throughout the whole test.

The test consists of two sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n.

At the beginning of T1 the UE receives an RRC message by which the Cell 3 and Cell 4 becomes configured on radio channel 3 and 4 respectively. During T1 the SCells (Cell 3 and Cell 4) are powered off and UE is not aware of SCells. The UE starts monitoring the SCC1(Cell 3 CC) and SCC2 (Cell 4 CC). The test equipment sends a MAC message for activation of the Cell 3 and Cell 4 simultaneously.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2.

In sub test 1,TE shall transmit DCI 0-1 on PCell to schedule the PUSCH at slot , and the UE shall be able to transmit L3 measurement report of SCells at slot , where k2 = 1. n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+k2 NR slot length

In sub test 2, TE shall transmit DCI 0-1 on PCell to schedule the PUSCH at slot , where M is defined in clause 8.3.17 and k2 = 1, and the UE shall be able to transmit L3 measurement report of SCells at slot . For sub test 2, TE will send TCI activation command after receiving L3 measurement report of the SCell.n+THARQ+3ms+M-k2 NR slot lengthn+THARQ+3ms+M NR slot length

The UE shall be able to report valid CSI for the activated SCells (Cell 3 and Cell 4) at latest in slot   respectively as defined in clause 8.3.18 provided the SCells can be successfully detected on the first attempt. n+THARQ+Tactivation_time_multiple_scells+TCSI_ReportingNR slot length

The UE shall start reporting CSI for cell 3 and cell 4 after at least one CSI-RS transmission occasion for channel measurement and reporting after slot   and shall report CQI index 0 (out-of-range) until the SCell activation for cell 3 and cell 4 has been completed, respectively. Any PSCell interruption due to activation of SCells shall occur in the slot  to slot, as defined in clause 8.3.18, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCells shall occur in the subframe  to subframe, where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot n, and  is the interruption length given in TS 36.133 [15] clause 7.32.n+THARQ+3msNR slot lengthn+1+THARQNR slot length n+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruption n1+1+THARQEUTRA slot length n2+1+THARQ+3ms+TXEUTRA slot length+Ninterruptionn1n2Ninterruption

The test equipment verifies the activation time for Cell 3 by counting the slots from the time when the SCell activation command is sent until CSI report of activated Cell 3 with other than CQI index 0 is received.

The test equipment verifies the activation time for Cell 4 by counting the slots from the time when the SCell activation command is sent until CSI report of activated Cell 4 with other than CQI index 0 is received.

Table A.4.5.3.10.1-1: General test parameters for multiple unknown FR1 SCell activation case with 2 deactivated SCells, 160 ms SCell measurement cycle

Table A.4.5.3.10.1-2: Cell specific test parameters for NR SCell for multiple unknown FR1 SCell activation case, 160ms SCell measurement cycle

## A.4.5.3.10.2Test Requirements

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where as defined in clause 8.3.18, in sub test 1,    Tactivation_time_multiple_scells = 7 ms  + + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay), where = 1 ms for SCS of PSCell =15 kHz, and 0.5 ms for SCS of PSCell = 30 kHz,n+THARQ+Tactivation_time_multiple_scells+TCSI_ReportingNR slot lengthk2NR slot lengthk2NR slot length

In sub test 2, Tactivation_time_multiple_scells = 3 ms + M  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay).

## A.4.5.3.11TRS-based SCell Activation of SSB-less SCell in FR1 collocated inter-band

## A.4.5.3.11.1Test Purpose and Environment

The purpose of this test is to verify that the TRS based SCell activation times are within the requirements stated in clause 8.3.2, when the SCell is an SSB-less SCell on a FR1 band different from the reference cell (i.e., PSCell) and provided with periodic CSI-RS for tracking instead of SSB. The SCell and PSCell are collocated.

The supported test configurations are shown in table A.4.5.3.11.1-1 below. The test parameters are given in tables A.4.5.3.11.1-2 and cell-specific parameters in A.4.5.3.11.1-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three carriers, E-UTRA has one cell; NR has two cells, where each NR cell has one carrier and these two carriers are collocated and on different FR1 bands. SSB is not transmitted on the SCell hence the UE is not provided with SSB configuration (absoluteFrequencySSB) in the SCell (FrequencyInfoDL) nor SMTC configuration. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR, but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on NR. The test equipment sends a MAC message for activation of the SCell and triggering the periodic CSI-RS for TRS-based SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3.2. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. m+THARQ+Tactivation_time+TCSI_ReportingNR slot length

Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2. Any E-UTRA PCell interruption due to activation of SCell shall occur in the subframe  to subframe , where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m, and  is the interruption length given in TS 36.133 [15] clause 7.32.   m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruptionm1m2Ninterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.4.5.3.11.1-1: TRS-based SCell activation of SSB-less SCell in FRI inter-band supported test configurations

Table A.4.5.3.11.1-2: General test parameters for TRS-based SCell activation of SSB-less SCell in FR1 inter-band

Table A.4.5.3.11-3: Cell specific test parameters for TRS-based SCell activation of SSB-less SCell in FR1 inter-band

## A.4.5.3.11.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PSCell in slot (m+k).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , where Tactivation_time = m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-Tfirst_TRS + TTRS + 5 ms, when the EPRE difference(ΔEPRE) is equal to 12 dB

-Tfirst_TRS + 2*TTRS +5 ms, when the EPRE difference(ΔEPRE) is equal to 30 dB

as defined in clause 8.3.2.

During T2 interruption of PSCell during SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruptionm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.3.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90%.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.4.5.3.12Inter-band SSB-less Scell activation using A-TRS

## A.4.5.3.12.1Test Purpose and Environment

The purpose of this test is to verify the SSB less SCell activation delay is within the requirements stated in clause 8.3.2.

The supported test configurations are shown in table A.4.5.3.12.1-1 below. The test parameters are given in tables A.4.5.3.12.1-2 and cell-specific parameters in A.4.5.3.12.1-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three carriers, E-UTRA has one cell, NR has two cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on E-UTRA and Cell 2 (PSCell) on NR but is not aware of Cell 3 (SCell) on NR. The UE is monitoring the PCell and PSCell. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes added. The configuration for the SCell (Cell 3) is not provided with SSB configuration (absoluteFrequencySSB) in the SCell FrequencyInfoDL nor SMTC configuration for the SCell and PSCell (Cell 2) is indicated as reference cell by higherlayer parameter referenceCell-r18. Cell 3 is configured with aperiodic-TRS as shown in table A.4.5.3.12.1-3. The RS(s) of the Cell 3 is QCL-TypeA with TRS(s) of the Cell 3, and the TRS(s) of the Cell 3 is QCL-TypeC with SSB(s) of Cell 2.

The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation. The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2.

The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in between slot  to slot as defined in clause 8.3. Any E-UTRA PCell interruption due to activation of SCell shall occur in between subframe  to subframe   where  and  are the index of the first and last subframe of E-UTRA PCell which overlaps with slot m. m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+Tfirst_ATRSNR slot length+Ninterruptionm1+1+THARQEUTRA slot lengthm2+1+THARQ+3 ms+Tfirst_ATRSEUTRA slot length+Ninterruptionm1m2

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of Scell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the Scell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.4.5.3.12.1-1: Inter-band SSB less SCell SCell activation in FR1 supported test configurations

Table A.4.5.3.12.1-2: General test parameters for Inter-band SSB less SCell SCell activation in FR1

Table A.4.5.3.12-3: Cell specific test parameters for Inter-band SSB less SCell activation in FR1

## A.4.5.3.12.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PSCell in slot (m+k).

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = Tfirst_ATRS + Tgap + TATRS + 5 ms, as defined in clause 8.3.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PSCell during SCell activation shall not happen outside the slot  to  , and interruption of E-UTRA PCell during SCell activation shall not happen outside the subframe  to subframe, as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruptionm1+1+THARQEUTRA slot length m2+1+THARQ+3 ms+TXEUTRA slot length+Ninterruption

The interruption of PSCell shall not be more than the values specified for EN-DC in clause 8.2.1.2.19.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90%.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.4.5.4UE UL carrier RRC reconfiguration Delay

## A.4.5.4.1UE UL carrier RRC reconfiguration Delay

Table A.4.5.4.1-1 - Table A.4.5.4.1-4 : Void

## A.4.5.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that when the UE receives an RRC message implying NR UL or Supplementary UL carrier configuration, the UE shall be ready to start transmission on the newly configured carrier within the time limits specified in clause 8.4.2 and 8.4.3 for configuring and deconfiguring, respectively.

There are three cells: E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and FR1 SCell (Cell 3). For SCell, both NR uplink and supplementary uplink are broadcast by ServingCellConfigCommonSIB. The test parameters for PSCell and SCell are given in Table A. 4.5.4.1.1-1, Table A. 4.5.4.1.1-2, Table A. 4.5.4.1.1-3 and Table A. 4.5.4.1.1-4 below.  The test parameters and applicability for E-UTRAN PCell are defined in clause A.3.7.2.  The test consists of two separate tests. The test consists of three time periods, with duration of T1, T2 and T3 respectively. During time duration T1, NR uplink of cell 3 is configured to UE. At the start of T2, a supplementary uplink of Cell 3 is configured to UE through RRCReconfiguration, then UE shall start transmission on the supplementary uplink. At the start of T3, the supplementary uplink is released through RRCReconfiguration.

Table A.4.5.4.1.1-1: Supported test configurations

Table A.4.5.4.1.1-2: General test parameters for EN-DC UE UL carrier RRC reconfiguration Delay

Table A.4.5.4.1.1-3: NR Cell specific test parameters for EN-DC UE UL carrier RRC reconfiguration Delay on PSCell (Cell 2)

Table A.4.5.4.1.1-4: NR Cell specific test parameters for EN-DC UE UL carrier RRC reconfiguration Delay on SCell (Cell 3)

## A.4.5.4.1.2Test Requirements

The UE shall be ready to start transmission on the supplementary uplink carrier on SCell within 20 ms from the start of T2.

The UE shall stop the transmission on the supplementary uplink carrier on SCell within 20 ms from the start of T3.

All of the above test requirements shall be fulfilled in order for the observed UE UL carrier configuration delay and UE UL carrier release delay to be counted as correct. The rate of correct observed UE UL carrier configuration delay and UE UL carrier release delay during repeated tests shall be at least 90%.

## A.4.5.5Beam Failure Detection and Link recovery procedures

## A.4.5.5.1EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode

## A.4.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.4.5.5.1.1-1, A.4.5.5.1.1-2, and A.4.5.5.1.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.1.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.4.5.5.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms) in test 1.

Table A.4.5.5.1.1-1: Supported test configurations for FR1 PCell

Table A.4.5.5.1.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.1.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.1.1-4: Void

Figure A.4.5.5.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.1.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.4.5.5.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.2EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode

## A.4.5.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.4.5.5.2.1-1, A.4.5.5.2.1-2, and A.4.5.5.2.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.2.1-1 shows the variation of the downlink SNR of the PSCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.4.5.5.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.5.2.1-1: Supported test configurations for FR1 PCell

Table A.4.5.5.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.4.5.5.2.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.4.5.5.2.1-4: Void

Table A.4.5.5.2.1-5: Void

Figure A.4.5.5.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.4.5.5.2.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.4.5.5.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.3EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.4.5.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.4.5.5.3.1-1, A.4.5.5.3.1-2, and A.4.5.5.3.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.3.1-1 shows the variation of the downlink SNR of the PSCell and the SNR of the CSI-RS in set q0 in the active PSCell to emulate CSI-RS based beam failure. Figure A.4.5.5.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled.

Table A.4.5.5.3.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.5.3.1-2: General test parameters for FR1 PSCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.3.1-3: Cell specific test parameters for FR1 PSCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.3.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.3.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.4.5.5.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.4EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode

## A.4.5.5.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.4.5.5.4.1-1, A.4.5.5.4.1-2, and A.4.5.5.4.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell, in the test.  The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.4.1-1 shows the variation of the downlink SNR of the PSCell and the SNR of the CSI-RS in set q0 in the active PSCell to emulate CSI-RS based beam failure. Figure A.4.5.5.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.5.4.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.5.4.1-2: General test parameters for FR1 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.4.5.5.4.1-3: Cell specific test parameters for FR1 PSCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.4.5.5.4.1-4: Void

Table A.4.5.5.4.1-5: Void

Table A.4.5.5.4.1-6: Void

Figure A.4.5.5.4.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.4.5.5.4.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

## A.4.5.5.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.5EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode

## A.4.5.5.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving SCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.4.5.5.5.1-1, A.4.5.5.5.1-2, and A.4.5.5.5.1-3 below. There are three cells, cell 1 is the E-UTRAN PCell, cell 2 is the PSCell and cell 3 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.5.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.4.5.5.5.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1, cell 2 and Cell 3. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.4.5.5.5.1-1: Supported test configurations for FR1 PCell and SCell

Table A.4.5.5.5.1-2: General test parameters for FR1 SCell for beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.5.1-3: Cell specific test parameters for FR1 PSCell and SCell for beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.5.1-1: SNR variation for beam failure detection and link recovery testing for SCell in non-DRX mode

Figure A.4.5.5.5.1-2: L1-RSRP level variation for beam failure detection and link recovery testing for SCell in non-DRX mode

## A.4.5.5.5.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing  a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.6EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode

## A.4.5.5.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS based beam failure in the set q0 configured for a serving SCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.4.5.5.6.1-1, A.4.5.5.6.1-2, and A.4.5.5.6.1-3below. There are three cells, cell 1 is the E-UTRAN PCell, cell 2 is the PSCell and cell 3 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.6.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.4.5.5.6.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1, cell 2 and cell 3. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in SCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.4.5.5.6.1-1: Supported test configurations for FR1 PCell and SCell

Table A.4.5.5.6.1-2: General test parameters for FR1 SCell for beam failure detection and link recovery testing in DRX mode

Table A.4.5.5.6.1-3: Cell specific test parameters for FR1 SCell for beam failure detection and link recovery testing in DRX mode

Figure A.4.5.5.6.1-1: SNR variation for beam failure detection and LR testing for SCell in DRX mode

Figure A.4.5.5.6.1-2: L1-RSRP level variation for beam failure detection and link recovery testing for SCell in DRX mode

## A.4.5.5.6.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing  a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.7EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode

## A.4.5.5.7.1Test Purpose and Environment

The test scenario is EN-DC and NR configured in the test contains two TRPs (i.e., TRP0 and TRP1). Each TRP is configured with different SSB for beam failure detection and candidate beam detection. SSB is configured as BFD-RS and CBD-RS.

The purpose of this test is to verify that the UE properly detects the TRP specific SSB-based beam failure in the set (q0,0) for TRP0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set (q1,0). The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell with schedulingRequestID-BFR-r17 configured, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.4.5.5.7.1-1, A.4.5.5.7.1-2, and A.4.5.5.7.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the active PSCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.7.1-1 shows the variation of the downlink SNR of the PSCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.4.5.5.7.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms) in test 1.

Table A.4.5.5.7.1-1: Supported test configurations for FR1 PCell

Table A.4.5.5.7.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.7.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.7.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.7.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.4.5.5.7.2Test Requirements

Test requirements are applied to TRP specific report respectively on (q0,0), (q1,0) for TRP 0 and (q0,1), (q1,1)  for TRP 1 respectively as Figure A.4.5.5.7.1-1.

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1,0.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1,0. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1,0 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.5.8EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode

## A.4.5.5.8.1Test Purpose and Environment

The test scenario is EN-DC and a NR SCell configured in the test contains two TRPs (i.e., TRP0 and TRP1). Each TRP is configured with different CSI-RS and SSB for beam failure detection and candidate beam detection. CSI-RS is configured as BFD-RS and SSB is configured as CBD-RS.

The purpose of this test is to verify that the UE properly detects the CSI-RS-based beam failure on the TRP using the respective configured BFD set  for TRP0. After the BFD is detected for the TRP, the test further verifies whether the UE performs the correct SSB-based link recovery based on the configured beam candidate set  for TRP0. In the test two TRPs (TRP0 and TRP1) are provided with schedulingRequestID-BFR-r17. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.18.q0,0q1,0

Supported test configuration are provided in table A.4.5.5.8.1-1, general test parameters for FR1 SCell is provided in table A.4.5.5.8.1-2, and Cell specific test parameter are provided in table A.4.5.5.8.1-3. There are three cells in the test, cell 1 is the E-UTRAN PCell, cell 2 is the NR PSCell and cell 3 is the NR SCell. CSI report for SCell (cell 3) are transmitted on PSCell (cell 2).

The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.4.5.5.8.1-1 shows the SNR of the CSI-RS in set q0,0 in the TRP0 to emulate beam failure. Figure A.4.5.5.8.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q10 and q11 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1, cell 2 and Cell 3. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.4.5.5.8.1-1: Supported test configurations for FR1 PCell and SCell

Table A.4.5.5.8.1-2: General test parameters for FR1 SCell for beam failure detection and link recovery testing in non-DRX mode

Table A.4.5.5.8.1-3: Cell specific test parameters for FR1 PSCell and SCell for beam failure detection and link recovery testing in non-DRX mode

Figure A.4.5.5.8.1-1: SNR variation for beam failure detection and link recovery testing for TRP0 in non-DRX mode

Figure A.4.5.5.8.1-2: L1-RSRP level variation for beam failure detection and link recovery testing for TRP 0 in non-DRX mode

## A.4.5.5.8.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 2.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 2 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 2.

During T3 the UE shall detect beam failure on TRP0 and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1,0.

For TRP0, no later than time point F occurring no later than D1 = 60 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1,0. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1,0 earlier than time point B.

Test is concluded once the test equipment has received the BFR MAC CE from the UE. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.6Active BWP switch

## A.4.5.6.1DCI-based and Timer-based Active BWP Switch

## A.4.5.6.1.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.4.5.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in TS 38.133 clause 8.6, and interruption requirement for E-UTRA victim cell defined in TS 36.133 [15] clause 7.32.2.7. Supported test configurations are shown in table A.4.5.6.1.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.4.5.6.1.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.4.5.6.1.1.1-3 below.

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

Time period T1 starts when a DCI format 1_1 command for PSCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6.2 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after DL slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after DL slot (i+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on PSCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6.2 and starts to report valid ACK/NACK for the PSCell at latest at the beginning of the DL slot right after DL slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after DL slot (j+TBWPswitchDelay).

The starting time of PCell(Cell 1) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PSCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of PSCell, respectively.

Table A.4.5.6.1.1.1-1: DL BWP switch supported test configurations

Table A.4.5.6.1.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.1.1.1-3.: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

A.4.5.6.1.1.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

Depending on UE capability bwp-SwitchingDelay TS 38.331 [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in Table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

During T1, the start time of PCell interruption during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start time of PCell interruption of during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in TS 36.133 [15] clause 7.32.2.7.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.4.5.6.1.2E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC

A.4.5.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6.2, and interruption requirements for NR victim cell defined in clause 8.2.1.2.7 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations for LTE PCell and NR PSCell are shown in Table A.4.5.6.1.2.1-1. Supported test configurations for NR SCell are shown in table A.4.5.6.1.2.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The test scenario comprises of one E-UTRA PCell (Cell 1), one PSCell (Cell 2) and one SCell (Cell 3) as given in table A.4.5.6.1.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of PSCell and SCell are specified in table A.4.5.6.1.2.1-3 and table A.4.5.6.1.2.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on E-UTRA PCell (Cell 1) and PSCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 3 and the time duration of T2.

Before the test starts,

-UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 3 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0 in Cell 2 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PSCell.

-UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6.2 and starts to report valid ACK/NACK for the SCell on PSCell no later than on the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

E-UTRA PCell(Cell 1) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

PSCell(Cell 2) interruption due to BWP switch on SCell shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on SCell(Cell 3).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of SCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PSCell no later than on the first UL slot that occurs after the beginning of the slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

E-UTRA PCell (Cell 1) interruption due to BWP switch of SCell shall occur within the BWP switch delay.

PSCell (Cell 2) interruption due to BWP switch of SCell shall occur within the BWP switch delay.The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PCell and NR PSCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during BWP switch of SCell, respectively.

Table A.4.5.6.1.2.1-1: DL BWP switch supported test configurations for LTE PCell and NR PSCell

Table A.4.5.6.1.2.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.4.5.6.1.2.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.1.2.1-3: NR Cell specific test parameters for NR PSCell for DL BWP switch in synchronous EN-DC

Table A.4.5.6.1.2.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in synchronous EN-DC

A.4.5.6.1.2.2Test Requirements

During T1, the UE shall start to send the ACK for SCell on PSCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for SCell on PSCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

During T1, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 7.32.2.7 of TS 36.133 [15].

During T1, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PSCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.6.2.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.4.5.6.2RRC-based Active BWP Switch

A.4.5.6.2.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.4.5.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.4.5.6.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2) as given in table A.4.5.6.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell are specified in table A.4.5.6.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PSCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

If the RRCReconfiguration is embedded in E-UTRA RRC message, time period T1 starts when a E-UTRA RRC message RRCConnectionReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side from PCell in PSCell’s slot # denoted i. Otherwise, i.e., if the RRCReconfiguration is not embedded in E-UTRA RRC message, time period T1 starts when the RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in from PSCell in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC) as defined in clause 8.6.3 and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC).

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurations sent till the time when RRC Reconfiguration Complete message is received.

Table A.4.5.6.2.1.1-1: DL BWP switch supported test configurations

Table A.4.5.6.2.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.2.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

A.4.5.6.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell in the beginning of the DL slot right after  slot (i+ TRRCprocessingDelay+TBWPswitchDelayRRC ).

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.6.3Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs

## A.4.5.6.3.1Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs

A.4.5.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify the requirement of DL BWP switch delay on multiple CCs in TS 38.133 clause 8.6.2A.1, and interruption requirement for E-UTRA victim cell defined in TS 36.133 [15] clause 7.32.2.7. Supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.6.3.1.1-1. Supported test configurations for NR SCell are shown in table A.4.5.6.3.1.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.4.5.6.3.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and NR SCell are specified in table A.4.5.6.3.1.1-3 and table A.4.5.6.3.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) and SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration T2 when BWPs are switching on Cell 2 and Cell 3.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3.

-UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell, BWP-1 and BWP-2, before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell

-UE is configured with a bwp-InactivityTimer timer value for PSCell and SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PSCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall switch its PSCell bandwidth part from BWP-1 to BWP-2. On the same slot on Cell 3 test equipment shall send a DCI format 1_1 command for SCell DL BWP switch. The UE shall switch its SCell bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on PSCell and SCell at the beginning of the DL slot right after DL slot (i+ TMultipleBWPswitchDelay) as defined in clause 8.6.2A.1 and starts to report valid ACK/NACK for the PSCell and SCell no later than at the beginning of the DL slot right after DL slot (i+ TMultipleBWPswitchDelay+k1). The UE shall be continuously scheduled on both PCell’s and SCell’s BWP-2 starting from the beginning of the DL slot right after DL slot (i+ TMultipleBWPswitchDelay).

The starting time of PCell(Cell 1) interruption due to BWP switch on PSCell and SCell shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on PSCell(Cell 2) and SCell(Cell 3).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the bwp-InactivityTimer timer expires on PSCell. bwp-InactivityTimer timer on SCell shall also expire on slot #j. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1 on both PSCell and SCell. The UE shall be able to receive PDSCH on both PSCell and SCell at the beginning of the DL slot right after  DL slot (j+ TMultipleBWPswitchDelay) as defined in clause 8.6.2B.1 and starts to report valid ACK/NACK for the PSCell and SCell  at latest at the beginning of the DL slot right after DL slot (j+ TMultipleBWPswitchDelay +k1). The UE shall be continuously scheduled on both PSCell’s and SCell’s BWP-1 starting from the beginning of the DL slot right after DL slot (j+ TMultipleBWPswitchDelay).

The starting time of PCell(Cell 1) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PSCell and SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of PSCell and SCell.

Table A.4.5.6.3.1.1-1: DL BWP switch supported test configurations for LTE PCell and NR PSCell

Table A.4.5.6.3.1.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.4.5.6.3.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.3.1.1-3: NR Cell specific test parameters for NR PSCell for DL BWP switch in synchronous EN-DC

Table A.4.5.6.3.1.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in synchronous EN-DC

A.4.5.6.3.1.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell and SCell from the first UL slot that occurs after the beginning of DL slot (i+ TMultipleBWPswitchDelay +k1).

During T3, the UE shall start to send the ACK for PSCell and SCell from the first UL slot that occurs after the beginning of DL slot (j+ TMultipleBWPswitchDelay +k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

Depending on UE capability, UE shall finish BWP switch within the time duration TMultipleBWPswitchDelay defined in clause 8.6.2A.1.

All of the above test requirements shall be fulfilled in order for the observed PSCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

During T1, the start time of PCell interruption during PSCell and SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start time of PCell interruption of during PSCell and SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in TS 36.133 [15] clause 7.32.2.7.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+ TMultipleBWPswitchDelay +k1), (j+ TMultipleBWPswitchDelay +k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.4.5.6.4Simultaneous RRC-based Active BWP Switch on multiple CCs

## A.4.5.6.4.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs

## A.4.5.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify the DL dormant BWP switch delay requirement defined in clause 8.6.3A.1, and interruption requirements for NR victim cell defined in clause 8.2.1.2.15 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations for LTE PCell and NR PSCell are shown in Table A.4.5.6.4.1.1-1. Supported test configurations for NR SCell are shown in Table A.4.5.6.4.1.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.4.5.6.4.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.4.5.6.4.1.1-3 and table A.4.5.6.4.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), PSCell (Cell 2) on radio channel 2 (PSCC) and SCell (Cell 3) on radio channel 3 (SCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for PSCell (Cell 2) and SCell (Cell 3)

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell (Cell 2) and SCell (Cell 3).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when the RRCReconfiguration with updated bandwidth part configuration for both PSCell(Cell 2) and SCell(Cell 3), sent from the test equipment to the UE, is completely received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part configuration on PSCell(Cell 2) and SCell(Cell 3).

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+) as defined in clause 8.6.3A.1 and be ready for the reception of uplink grant for the PSCell(Cell 2) and SCell(Cell 3) no later than at the beginning of the DL slot right after slot (i+). The UE shall be continuously scheduled on PSCell’s BWP-1 and SCell’s BWP-1 starting from the beginning of the DL slot right after slot (i +).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

TRRCprocessingDelay , TBWPswitchDelayRRC, are defined in clause 8.6.3A.1 .DRRC

The test equipment verifies the DL BWP switch time in PSCell (Cell 2) and SCell (Cell 3) by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration sent till the time when RRC Reconfiguration Complete message is received.

Table A.4.5.6.4.1.1-1: DL BWP switch supported test configurations for LTE PCell and NR PSCell

Table A.4.5.6.4.1.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.4.5.6.4.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.4.1.1-3: NR Cell specific test parameters for NR PSCell for DL BWP switch in synchronous EN-DC

Table A.4.5.6.4.1.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in synchronous EN-DC

## A.4.5.6.4.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell and SCell in the beginning of the DL slot right after  slot (i+) .TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

All of the above test requirements shall be fulfilled in order for the observed PSCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.6.4.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time

## A.4.5.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify the delay requirement of BWP switching from dormancy to non-dormancy and from non-dormancy to dormancy on SCell defined in clause 8.6.2, and interruption requirements for NR victim cell defined in clause 8.2.1.2.15 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.6.4.2.1-1. Supported test configurations for NR SCells are shown in table A.4.5.6.4.2.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCells are chosen independently. Test configurations for two NR SCells are chosen independently.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and two NR SCells (Cell 3, and Cell 4) as given in table A.4.5.6.4.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCells are specified in table A.4.5.6.4.2.1-3, table A.4.5.6.4.2.1-4 and table A.4.5.6.4.2.1-5 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and PSCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 3, and Cell 4) to ensure that the UE would have ACK/NACK sending except for the time duration when SCell (Cell 2) performs the dormancy switching and stays in the dormant BWP.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC),, Cell 3 (SCell) on radio channel 3 (SCC) and Cell 4 (SCell) on radio channel 4 (SCC).

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0, in Cell 2 before starting the test. BWP-0 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 2 UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2 in Cell 3 and Cell 4 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PSCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in all SCells.

-UE is indicated in dormantBWP -Id that the dormant BWP is BWP-2 in all SCells.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for enterning dormant BWP in SCell, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. Upon reception of the PDCCH indicating entering dormant BWP in PCell, UE shall switch the DL BWP-1 to DL BWP-2 in all SCells, i.e., switching from non-dormant BWP to dormant BWP.

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The starting time of PSCell (Cell 2) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on all SCells.

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

During T3,

Time period T3 starts when a DCI format 1_1 command for leaving dormant BWP in SCells, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted j. Upon reception of the PDCCH indicating leaving dormant BWP in PSCell, UE shall switch the DL BWP-2 to DL BWP-1 in SCells, i.e., switching from dormant BWP to non-dormant BWP.

The UE shall be able to receive PDSCH on all SCells no later than the first DL slot that occurs after the beginning of PSCell’s DL slot (j+ TmutipledormantBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK on all SCells no later than the first UL slot that occurs after the beginning of slot (j+N) as defined in clause 10.3 in TS 38.213.

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The starting time of PSCell (Cell 2) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The test equipment verifies that potential interruption to E-UTRA PCell and NR PSCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during dormant BWP switch of SCells, respectively.

Table A.4.5.6.4.2.1-1: Dormant BWP switch supported test configurations for LTE PCell and NR PSCell

Table A.4.5.6.4.2.1-1A: Dormant BWP switch supported test configurations for NR SCells

Table A.4.5.6.4.2.1-2: General test parameters for Dormant BWP switch in synchronous EN-DC

Table A.4.5.6.4.2.1-3: NR Cell specific test parameters for NR PSCell for Dormant BWP switch in synchronous EN-DC

Table A.4.5.6.4.2.1-4: NR Cell specific test parameters for NR SCell (Cell 3) for Dormant BWP switch in synchronous EN-DC

Table A.4.5.6.4.2.1-5: NR Cell specific test parameters for NR SCell (Cell 4) for Dormant BWP switch in synchronous EN-DC

## A.4.5.6.4.2.2Test Requirements

During T1, the UE shall be able to to send the ACK/NACK for all SCells before UE PDCCH indicating entering dormant BWP is received in PSCell’s slot # denoted.

During T3, the UE shall start to send the ACK/NACK for all SCells from the first UL slot that occurs after the beginning of DL slot (j+N).

Where, N is the timing that UE provide HARQ-ACK information in response to a detection of a DCI format 1_1 indicating SCell dormancy as specified in [3].

All of the above test requirements shall be fulfilled in order for the observed SCell dormant BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

During T1, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T1, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 7.32.2.7 of TS 36.133 [15].

The interruption of PSCell shall not be longer than the interruption duration specified for dormant BWP switch in clause 8.6.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ N), (j+ N), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.4.5.6.5SCell dormancy switch

## A.4.5.6.5.1E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time

A.4.5.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement on multiple CCs for RRC-based BWP switch defined in clause 8.6.3A.1. Supported test configurations for LTE PCell and NR PSCell are shown in table A.4.5.6.5.1.1-1. Supported test configurations for NR SCell are shown in table A.4.5.6.5.1.1-1A. Test configuration for LTE PCell and NR PSCell and test configuration for NR SCell are chosen independently.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell(Cell 3) as given in table A.4.5.6.5.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and NR SCell are specified in table A.4.5.6.5.1.1-3 and table A.4.5.6.5.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and PSCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration when the SCell is in dormancy during T2.

The UE is configured to monitor PDCCH for DCI format 2_6 at ps-Offset before the start of onDuration. Two tests are specified, where a UE that only supports triggering within the first three OFDM symbols of a slot shall undergo Test1 only, and a UE that supports triggering also in remaining OFDM symbols of a slot shall undergo both Test1 and Test2. In the tested scenario, ps-Offset is selected to correspond to the dormancy switching time specified in clause 8.6.2A.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-1 in Cell 3 before starting the test.

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 3 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB. BWP-1 is configured in OutsideActiveTimeConfig as firstOutsideActiveTimeBWP. BWP-2 is configured as dormantBWP.

-UE is configured with RRM measurement on SCC.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

-UE is configured to monitor DCI format 2_6, and to be active during onDuration even when no DCI format 2_6 is detected (ps-WakeUp).

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

Time period T1 starts when a DCI format 2_6 command for SCell switch from non-dormany to dormancy, sent from the test equipment to the UE, is received at the UE side at ps-Offset before onDuration. The UE shall switch its SCell bandwidth part from BWP-1 to BWP-2 into dormancy. During T1, test equipement verifies that:

The UE shall be able to receive CSI-RS on SCell BWP-2 at the beginning of the DL slot right after SCell’s DL slot (i+TdormantBWPswitchDelay) as defined in clause 8.6. TE shall observe the periodic reporting of CQI for SCell starting from slot (i+TdormantBWPswitchDelay).

PCell (Cell 1) interruption due to dormancy switch on SCell shall occur within the dormancy switch delay.

PSCell (Cell 2) interruption due to dormancy switch on SCell shall occur within the dormancy switch delay.

Time period T2 starts when T1 is completed. During T2, the test equipment continues to schedule the UE continuously in PCell and PSCell. The UE shall carry out CSI and RRM measurements on the dormant SCells. The UE shall report ACK/NACK in PCell and PSCell in response to scheduled PDSCH, with the maximum loss of transmitted ACK/NACKs fulfilling the requirement in clause 8.2.1.2.15. The test equipment verifies that the loss of ACK/NACKs is no larger than 1.5%.

Time period T3 starts when T2 is completed. During T3, the test equipment does not schedule the UE, by which the inactivity timer expires and the UE stops monitoring PDCCH except for signalling using DCI format 2_6 at wake-up signalling occasions.

Time period T4 starts when the UE at ps-Offset before onDuration detects a DCI format 2_6 carrying dormancy indication that indicates that SCell 1 and SCell2 are to be switched from dormancy to non-dormancy. During T4, the test equipment schedules the UE with new data indication in PCell, PSCell and SCell during onDuration. The test equipment verifies that:

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+TdormantBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell at latest at the beginning of the DL slot right after slot (j+TdormantBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+TdormantBWPswitchDelay).

PCell (Cell 1) interruption due to dormancy switch on SCell shall occur within the dormancy switch delay.

PSCell (Cell 2) interruption due to dormancy switch on SCell shall occur within the dormancy switch delay.

Table A.4.5.6.5.1.1-1: DL BWP switch supported test configurations for LTE PCell and NR PSCell

Table A.4.5.6.5.1.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.4.5.6.5.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.4.5.6.5.1.1-3: NR Cell specific test parameters for NR PSCell for DL BWP switch in synchronous EN-DC

Table A.4.5.6.5.1.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in synchronous EN-DC

A.4.5.6.5.1.2Test Requirements

During T1, any interruption on PCell and PSCell due to dormancy switching of SCell shall be within the requirement specified in in clause 8.2.1.2.15.1 for NR victim cell, and clause 7.32.2.14.1 of 36.133 [15] for E-UTRA victim cell. Starting from onDuration in time period T1, the UE shall transmit ACK/NACK in response to scheduling in PCell and PSCell. There shall be no loss of ACK/NACK.

During time period T2, the UE shall transmit ACK/NACKs in response to scheduling in PCell and the rate of missed ACK/NACKs shall be no more than 1.5%.

During T1, any interruption on PCell and PSCell due to dormancy switching of SCell shall be within the requirement specified in in clause 8.2.1.2.15.1 for NR victim cell, and clause 7.32.2.14.1 of 36.133 [15] for E-UTRA victim cell. Starting from onDuration in time period T4, the UE shall transmit ACK/NACK in response to scheduling in PCell, SCell 1 and SCell2. There shall be no loss of ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.6.5.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time

## A.4.5.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify the delay requirement of BWP switching from dormancy to non-dormancy and from non-dormancy to dormancy on SCell defined in clause 8.6.2, and interruption requirements for NR victim cell defined in clause 8.2.1.2.15 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations are shown in table A.4.5.6.5.2.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and two NR SCells (Cell 3, and Cell 4) as given in table A.4.5.6.5.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCells are specified in table A.4.5.6.5.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and PSCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 3, and Cell 4) to ensure that the UE would have ACK/NACK sending except for the time duration when SCell (Cell2) performs the dormancy switching and stays in the dormant BWP.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC), Cell 3 (SCell) on radio channel 3 (SCC) and Cell 4 (SCell) on radio channel 4 (SCC).

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0, in Cell 2 before starting the test. BWP-0 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 2 UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2 in Cell 3 and Cell 4 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PSCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in all SCells.

-UE is indicated in dormantBWP -Id that the dormant BWP is BWP-2 in all SCells.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for enterning dormant BWP in SCell, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. Upon reception of the PDCCH indicating entering dormant BWP in PCell, UE shall switch the DL BWP-1 to DL BWP-2 in all SCells, i.e., switching from non-dormant BWP to dormant BWP.

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The starting time of PSCell (Cell 2) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on all SCells.

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

During T3,

Time period T3 starts when a DCI format 1_1 command for leaving dormant BWP in SCells, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted j. Upon reception of the PDCCH indicating leaving dormant BWP in PSCell, UE shall switch the DL BWP-2 to DL BWP-1 in SCells, i.e., switching from dormant BWP to non-dormant BWP.

The UE shall be able to receive PDSCH on all SCells no later than the first DL slot that occurs after the beginning of PSCell’s DL slot (j+ TmutipledormantBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK on all SCells no later than the first UL slot that occurs after the beginning of slot (j+N) as defined in clause 10.3 in TS 38.213 [3].

The UE shall be able to receive PDSCH and report valid ACK/NACK on the PCell and PSCell all the time except interruption.

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The starting time of PSCell (Cell 2) interruption due to dormancy switching on SCells shall occur within the dormant BWP switch delay.

The test equipment verifies that potential interruption to E-UTRA PCell and NR PSCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during dormant BWP switch of SCells, respectively.

Table A.4.5.6.5.2.1-1: Dormant BWP switch supported test configurations

Table A.4.5.6.5.2.1-2: General test parameters for Dormant BWP switch in synchronous EN-DC

Table A.4.5.6.5.2.1-3: NR Cell specific test parameters for Dormant BWP switch in synchronous EN-DC

## A.4.5.6.5.2.2Test Requirements

During T1, the UE shall be able to to send the ACK/NACK for all SCells before UE PDCCH indicating entering dormant BWP is received in PSCell’s slot # denoted.

During T3, the UE shall start to send the ACK/NACK for all SCells from the first UL slot that occurs after the beginning of DL slot (j+N).

Where, N is the timing that UE provide HARQ-ACK information in response to a detection of a DCI format 1_1 indicating SCell dormancy as specified in [3].

All of the above test requirements shall be fulfilled in order for the observed SCell dormant BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

During T1, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T1, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PSCell during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 7.32.2.7 of TS 36.133 [15].

The interruption of PSCell shall not be longer than the interruption duration specified for dormant BWP switch in clause 8.6.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ N), (j+ N), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.4.5.7PSCell addition and release delay

## A.4.5.7.1Addition and Release Delay of known NR PSCell

## A.4.5.7.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delays under EN-DC are within the requirements stated in clause 7.31.2 TS 36.133 [15] for the case when the PSCell is known by the UE at the time of addition.

Supported test configurations are shown in table A.4.5.7.1.1-1. The test parameters for the E-UTRA cell are given in Table A.3.7.2.1-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in Tables A.4.5.7.1.1-2 and cell-specific parameters in table A.4.5.7.1.1-3 below. The test consists of six successive time periods with duration of T1, T2, T3, T4, T5 and T6 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell1 is known to the UE.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event B1 is configured for neighbour cell (Cell2). Before the start of T2 the UE is configured with the measurement gaps (gap pattern Id # 0). The Cell2 becomes known to the UE during T2. Therefore, during T2 the UE shall report Event B1. The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2.

The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The point in time at which the RRC message to add PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

The test system shall observe the periodic reporting of CSI for PSCell during T5. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T5.

The test system shall send an RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell2) shall be sent to the UE during period T5, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell2) is received at the UE antenna connector defines the start of period T6.

Table A.4.5.7.1.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.7.1.1-2: General Test Parameters for PSCell Addition and Release

Table A.4.5.7.1.1-3: Cell Specific Parameters for PSCell Addition and Release

## A.4.5.7.1.2Test Requirements

The UE shall transmit the PRACH to PSCell no later than 82 msNote1 from the start of T4.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T5.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T5

The UE shall stop sending CSI reports for PSCell no later than 20 ms from the start of T6.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90%.

Note1:The PSCell addition delay can be expressed as follows as specified in clause 7.31.2 TS 36.133 [15]:

Tconfig_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 20 ms

Tsearch = 0

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.4.5.8DL Interruptions at switching between two uplink carriers

## A.4.5.8.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.1.2.14. The test case is applicable for an uplink band pair of an inter-band EN-DC configuration when the capability uplinkTxSwitchingPeriod is present.

There are two cells: E-UTRAN FDD PCell (Cell 1), FR1 PSCell (Cell 2). The test parameters for PSCell are given in Table A.4.5.8.1-1, Table A.4.5.8.1-2 and Table A.4.5.8.1-3 below.

Aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on following symbol on the 1 st special slot of every radio frame on NR TDD carrier (Cell 2):

symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

otherwise,

symbol#5 if UE capability uplinkTxSwitchingPeriod is 140 us or

symbol #8 if UE capability uplinkTxSwitchingPeriod is 35 us.

The test parameters and applicability for E-UTRAN FDD PCell are defined in clause A.3.7.2. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE. This test verifies that the UE correctly report the L1-RSRP reporting.

Table A.4.5.8.1-1: Supported test configurations

Table A. 4.5.8.1-2: General test parameters for DL Interruptions at switching between two uplink carriers in EN-DC

Table A. 4.5.8.1-3: NR Cell specific test parameters for DL Interruptions at switching between two uplink carriers in EN-DC (Cell 2)

Table A.4.5.8.1-4: SRS Configuration for DL Interruptions at switching between two uplink carriers

## A.4.5.8.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.1.2.14.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.9UE specific CBW change

## A.4.5.9.1UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC

## A.4.5.9.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13.1. Supported test configurations are shown in table A.4.5.9.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2) as given in table A.4.5.9.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell are specified in table A.4.5.9.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PSCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

-UE is indicated in SCS-SpecificCarrier that the active CBW is CBW-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when the RRCReconfiguration with updated CBW configuration, sent from the test equipment to the UE, is completely received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its CBW with the updated CBW of final condition (CBW-2).

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+ ) as defined in clause 8.13.1 and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+ ). The UE shall be continuously scheduled on PSCell’s BWP-1 of CBW-2 starting from the beginning of the DL slot right after slot (i+ ).TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthTRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthTRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

TRRCprocessingDelay and TCBWchangeDelayRRC are defined in clause 8.13.1.

The test equipment verifies the UE specific CBW change time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated CBW configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.4.5.9.1.1-1: UE specific CBW change supported test configurations

Table A.4.5.9.1.1-2: General test parameters for UE specific CBW change in synchronous EN-DC

A.4.5.9.1.1-3: NR Cell specific test parameters for UE specific CBW change in synchronous EN-DC

## A.4.5.9.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell in the beginning of the DL slot right after slot (i+ ).TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

All of the above test requirements shall be fulfilled in order for the observed PSCell UE specific CBW change delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.5.10PSCell activation and deactivation delay

## A.4.5.10.1PSCell activation and deactivation delay

## A.4.5.10.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell activation and deactivation delay under EN-DC are within the requirements stated in clause 7.38 in TS 36.133 [15] for the case when UE configured with one deactivated SCG and when PScell in one SCG is being activated where the PSCell is known by the UE at the time of activation.

Supported test configurations are shown in table A.4.5.10.1.1-1. The test parameters for the E-UTRA cell are given in Table A.3.7.2.2-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in Tables A.4.5.10.1.1-2, cell-specific parameters in table A.4.5.10.1.1-3 below. The test consists of four successive time periods with duration of T1, T2, T3 and T4. There are two carriers each with one cell. The UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) and PSCell (Cell2) is in deactivated state. During T1, both Cell1 and Cell2 are known to UE and UE performs measurement on deactivated PCell. Before the test starts the UE is configured RLM and BFD on deactivated PSCell. During T1, UE performs RLM and BFD on the deactivated PSCell and TCI state is known.

The test system shall send a RRC message to the UE to activate PSCell (Cell 2) on radio channel 2, where no any PSCell parameter is modified in the RRC message. The RRC message (to activate PSCell) also includes a request for the UE to transmit scheduling request on PUCCH for the PSCell after the PSCell has been successfully activated. The RRC message to activate PSCell shall be sent to the UE during period T1. The point in time at which the RRC message to activate PSCell (Cell2) is received at the UE antenna connector defines the start of period T2.

The test system shall observe the periodic reporting of CSI for PSCell during T3. The point in time at which the UE has sent scheduling request on PUCCH for PSCell (Cell 2) defines the start of period T3.

The test system shall send a RRC message to the UE to deactivate PSCell (Cell 2) on radio channel 2. The RRC message to deactivate PSCell (Cell2) shall be sent to the UE during period T3, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to deactivate PSCell (Cell2) is received at the UE antenna connector defines the start of period T4.

Table A.4.5.10.1.1-1: Supported test configurations for FR1 PSCell

Table A.4.5.10.1.1-2: General Test Parameters for PSCell activation and deactivation

Table A.4.5.10.1.1-3: Cell Specific Parameters for PSCell activation and deactivation

## A.4.5.10.1.2Test Requirements

The UE performs RACH-less based PSCell activation. UE shall transmit the SR on PUCCH for PSCell at latest 67 msNote1 into T2.

The UE shall send at least one PUSCH on PSCell during T3.

The UE shall stop transmit PUSCH for PSCell in at latest 20 ms into T4.

All the above test requirements shall be fulfilled for the observed PSCell activation delay and PSCell deactivation delay to be counted as correct. The rate of correct observed PSCell activation delay and PSCell deactivation delay during repeated tests shall be at least 90%.

Note1:The PSCell activation delay can be expressed as follows as specified in clause 7.38 in TS 36.133 [15]:

Tactivation_time = TRRC_delay + Tprocessing + Tsearch + T∆ + TIU + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 5 ms

Tsearch = 0 ms

T∆ = 20 ms

TIU= max 20 ms

## A.4.5.11Conditional PSCell addition and release delay (FR1 EN-DC)

## A.4.5.11.1Conditional PSCell Addition and Release Delay

## A.4.5.11.1.1Test purpose and environment

The purpose of this test is to verify that the NR conditional PSCell addition and release delay under EN-DC is within the requirements stated in clause 8.9A.2.

## A.4.5.11.1.2Test Parameters

Supported test configurations are shown in table A.4.5.11.1.2-1. The test parameters for the E-UTRA cell are given in Table A.4.5.11.1.2-2. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in Tables A.4.5.11.1.2-2 and cell-specific parameters in table A.4.5.11.1.2-3 below. The test consists of four successive time periods with duration of T1, T2, T3 and T4 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell1 is known to the UE.

At the start of time duration T1, the UE does not have any timing information of Cell 2. The network shall configure a condition and the target PSCell configuration implying addition to cell 2 during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, cell 2 becomes detectable and meets the addition condition. UE shall be able to measure and detect that the condition is fulfilled during time Tmeasure. After which it will transmit the PRACH preamble. Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send an RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell.

Table A.4.5.11.1.2-1: Supported test configurations for FR1 PSCell

Table A.4.5.11.1.2-2: General Test Parameters for Conditional PSCell Addition and Release

Table A.4.5.11.1.2-3: Cell Specific Parameters for Conditional PSCell Addition and Release

## A.4.5.11.1.3Test Requirements

TRRC_delay + TEvent_DU occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 1040 ms+10 ms +62ms=1112 ms from the start of T2.

The UE shall transmit at least one periodic CSI report for PSCell during T3.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T4.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90%.

## A.4.6Measurement procedure

## A.4.6.1Intra-frequency Measurements

## A.4.6.1.1EN-DC event triggered reporting tests without gap under non-DRX

## A.4.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.4.6.1.1.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.1.2-1, A.4.6.1.1.2-2, A.4.6.1.1.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

Table A.4.6.1.1.2-1: Supported test configurations

Table A.4.6.1.1.2-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1

Table A.4.6.1.1.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1

## A.4.6.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.2EN-DC event triggered reporting tests without gap under DRX

## A.4.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.4.6.1.2.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.2.2-1, A.4.6.1.2.2-2, and A.4.6.1.2.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

UE needs to be provided 500 ms with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.1.2.2-1: Supported test configurations

Table A.4.6.1.2.2-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX

Table A.4.6.1.2.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX

## A.4.6.1.2.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.3EN-DC event triggered reporting tests with per-UE gaps under non-DRX

## A.4.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.4.6.1.3.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell.The test parameters for PSCell are given in Table A.4.6.1.3.2-1 and A.4.6.1.3.2-2 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.4.6.1.3.2-1: Supported test configurations

Table A.4.6.1.3.2-2: General test parameters for EN-DC intra-frequency event triggered reporting with per-UE gaps for PSCell in FR1

Table A.4.6.1.3.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting with per-UE gaps for PSCell in FR1

## A.4.6.1.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.4EN-DC event triggered reporting tests with per-UE gaps under DRX

## A.4.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.4.6.1.4.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.4.2-1, A.4.6.1.4.2-2, and A.4.6.1.4.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.1.4.2-1: Supported test configurations

Table A.4.6.1.4.2-2: General test parameters for EN-DC intra-frequency event triggered reporting with per-UE gaps for PSCell in FR1 with DRX

Table A.4.6.1.4.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting with per-UE gaps for PSCell in FR1 with DRX

## A.4.6.1.4.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.5EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading

## A.4.6.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.4.6.1.5.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell.The test parameters for FDD PSCell are given in Table A.4.6.1.5.2-2 and A.4.6.1.5.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

Table A.4.6.1.5.2-1: Supported test configurations

Table A.4.6.1.5.2-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for FDD PSCell in FR1 with SSB index reading

Table A.4.6.1.5.1-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for FDD PSCell in FR1 with SSB index reading

## A.4.6.1.5.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.6EN-DC event triggered reporting tests with SSB index reading with per-UE gaps

## A.4.6.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2.6.2 and 9.2.6.3.

## A.4.6.1.6.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.6.2-1 A.4.6.1.6.2-2 and A.4.6.1.6.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.4.6.1.6.2-1: Supported test configurations

Table A.4.6.1.6.2-2: General test parameters for EN-DC intra-frequency event triggered reporting with gap for PSCell in FR1 with SSB index reading

Table A.4.6.1.6.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting with gap for PSCell in FR1 with SSB index reading

## A.4.6.1.6.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.7EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16

## A.4.6.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for UE configured with highSpeedMeasFlag-r16. This test will partly verify the intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.4.6.1.7.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.7.2-1, A.4.6.1.7.2-2, and A.4.6.1.7.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.1.7.2-1: Supported test configurations

Table A.4.6.1.7.2-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX for UE configured with highSpeedMeasFlag-r16

Table A.4.6.1.7.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX for UE configured with highSpeedMeasFlag-r16

## A.4.6.1.7.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 5120 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.8EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17

## A.4.6.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC intra-frequency NR measurement requirements in clause 9.2.5.

In this test, there are four cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1, NR cell 3 as deactivated SCell in FR1 on NR RF channel 2, and NR cell 4 as neighbour cell on the same frequency as cell 3.  The test parameters and configurations are given in Tables A.4.6.1.8.1-1, A.4.6.1.8.1-1A, A.4.6.1.8.1-2, and A.4.6.1.8.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.1.8.1-1.

Table A.4.6.1.8.1-1: Supported PCell and PSCell configurations in EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17

Table 4.6.1.8. 1-1A: Supported SCell test configurations in EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17

Table A.4.6.1.8.1-2: General test parameters for EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17

Table A.4.6.1.8.1-3: Cell specific test parameters for EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17

## A.4.6.1.8.2Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.9EN-DC event triggered reporting tests without gap under non-DRX with NCD-SSB

## A.4.6.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements when NCD-SSB is configured in clause 9.2.5.1 and 9.2.5.2.

## A.4.6.1.9.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.1.9.2-1, A.4.6.1.9.2-2, and A.4.6.1.9.2-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. The CD-SSB is configured outside active DL BWP and NCD-SSB is configured fully within active DL BWP of FR1 PSCell. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

Table A.4.6.1.9.2-1: Supported test configurations

Table A.4.6.1.9.2-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1

Table A.4.6.1.9.2-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1

## A.4.6.1.9.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.1.10EN-DC event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP

## A.4.6.110.1Test purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of an event when CD-SSB is outside active BWP. This test will partly verify the intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

The test environment is the same as in clause A.4.6.1.1 with following exceptions in Table A.4.6.1.1.2-3.

## A.4.6.1.10.2Test Requirements

The test requirements are the same as in clause A.4.6.1.1.3.

## A.4.6.2Inter-frequency Measurements

## A.4.6.2.1EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used

## A.4.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.4.6.2.1.1-1, A.4.6.2.1.1-2, and A.4.6.2.1.1-3.

Measurement gap pattern configuration is defined in table A.4.6.2.1.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.2.1.1-1.

Table A.4.6.2.1.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.4.6.2.1.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.4.6.2.1.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.4.6.2.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.2.2EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used

## A.4.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.4.6.2.2.1-1, A.4.6.2.2.1-2, and A.4.6.2.2.1-3.

Measurement gap pattern configuration is defined in table A.4.6.2.2.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.2.2.1-1.

UE needs to be provided with new Timing Advance Command MAC control at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.2.2.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.4.6.2.2.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.4.6.2.2.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.4.6.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 3 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement In test 1 and 2, UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.2.3Void

## A.4.6.2.4Void

## A.4.6.2.5EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used

## A.4.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.4.6.2.5.1-1, A.4.6.2.5.1-2, and A.4.6.2.5.1-3.

Measurement gap pattern configuration is defined in table A.4.6.2.5.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.2.5.1-1.

Table A.4.6.2.5.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.4.6.2.5.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.4.6.2.5.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.4.6.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.2.6EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used

## A.4.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.4.6.2.6.1-1, A.4.6.2.6.1-2, and A.4.6.2.6.1-3.

Measurement gap pattern configuration is defined in table A.4.6.2.6.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.2.6.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.2.6.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.4.6.2.6.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.4.6.2.6.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.4.6.2.6.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 1 and 2, UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.2.7Void

## A.4.6.2.8Void

## A.4.6.2.9EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17

## A.4.6.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event for UE configured with highSpeedMeasInterFreq-r17. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2. The test parameters and configurations are given in tables A.4.6.2.9.1-1, A.4.6.2.9.1-2, and A.4.6.2.9.1-3.

Measurement gap pattern configuration is defined in table A.4.6.2.9.1-2 In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.2.9.1-1.

UE needs to be provided with new Timing Advance Command MAC control at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.4.6.2.9.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1 for UE configured with highSpeedMeasInterFreq-r17

Table A.4.6.2.9.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection for UE configured with highSpeedMeasInterFreq-r17

Table A.4.6.2.9.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection for UE configured with highSpeedMeasInterFreq-r17

## A.4.6.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.2.10EN-DC: event triggered reporting tests under non-DRX in FR1 for UE supporting threeCarrierMeasWithoutGap-r19

## A.4.6.2.10.1Test purpose and Environment

The purpose of this test is to partly verify the inter-frequency cell search requirements in clause 9.1.5.1 and 9.3.9 for UE supports interFrequencyMeas-Nogap-r16 and/or NeedForGapsInfoNR-r16 and threeCarrierMeasWithoutGap-r19 makes correct reporting of an event.

The UE is only required to pass one of the three tests in A.4.6.2.10 for FR1 EN-DC, A.6.6.2.17 for FR1 CA, A.7.6.2.25 for FR1 and FR2 CA.

## A.4.6.2.10.2Test parameters

In this test, LTE cell 1 as PCell in FR1 on LTE RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 2, NR cell 3 as SCell in FR1 on NR RF channel 3. NR cell 4 as neighbour cell in FR1 on NR RF channel 4 which is in the same band as NR Cell 3.  The SSB of Cell 4 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 3 and Cell 4 should be different in frequency location within the cell bandwidth.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 4.

Table A.4.6.2.10.2-1: Supported test configurations

Table A.4.6.2.10.2-2: General test parameters for inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.4.6.2.10.2-3: Cell specific test parameters for inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.4.6.2.10.3Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of time period T2

UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.3Void

## A.4.6.4L1-RSRP measurement for beam reporting

## A.4.6.4.1SSB based L1-RSRP measurement when DRX is not used

## A.4.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.4.6.4.1.1-1.

Table A.4.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.4.6.4.1.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.1.2-1 and Table A.4.6.4.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.4.6.4.1.2-1: General test parameters

Table A.4.6.4.1.2-2: SSB specific test parameters

## A.4.6.4.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.4.2SSB based L1-RSRP measurement when DRX is used

## A.4.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.4.6.4.2.1-1.

Table A.4.6.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.4.6.4.2.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.2.2-1 and Table A.4.6.4.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.4.6.4.2.2-1: General test parameters

Table A.4.6.4.2.2-2: SSB specific test parameters

## A.4.6.4.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.4.3CSI-RS based L1-RSRP measurement when DRX is not used

## A.4.6.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.4.6.4.3.1-1.

Table A.4.6.4.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.4.6.4.3.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.3.2-1 and Table A.4.6.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2,4,5 and 8 for Config 3,6) of a frame and UE provides the report back based on the reporting configuration as defined in table A.4.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.4.6.4.3.2-1: General test parameters

Table A.4.6.4.3.2-2: CSI-RS specific test parameters

## A.4.6.4.3.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.20.1.1 and relative accuracy requirement in clause 10.1.20.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.4.4CSI-RS based L1-RSRP measurement when DRX is used

## A.4.6.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.4.6.4.4.1-1.

Table A.4.6.4.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.4.6.4.4.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.4.2-1 and Table A.4.6.4.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2,4,5 and 8 for Config 3,6) of a frame and UE provides the report back based on the reporting configuration as defined in table A.4.6.4.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.4.6.4.4.2-1: General test parameters

Table A.4.6.4.4.2-2: CSI-RS specific test parameters

## A.4.6.4.4.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting absolute accuracy requirement in clause 10.1.20.1.1 and relative accuracy requirement in clause 10.1.20.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.4.5SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r16

## A.4.6.4.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when UE is configured with highSpeedMeasFlag-r16. This test will partly verify the L1-RSRP measurement requirements for UE configured with highSpeedMeasFlag-r16 in clause 9.5.4.1, with the testing configurations for NR cells in table A.4.6.4.5.1-1.

Table A.4.6.4.5.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.4.6.4.5.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.5.2-1 and Table A.4.6.4.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.4.6.4.5.2-1: General test parameters for UE configured with highSpeedMeasFlag-r16

Table A.4.6.4.5.2-2: SSB specific test parameters for UE configured with highSpeedMeasFlag-r16

## A.4.6.4.5.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.4.6CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.4.6.4.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells in table A.4.6.4.3.1-1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in clause A.4.6.4.3.

The test environment is the same as in clause A.4.6.4.3.2 with following exceptions in Table Table A.4.6.4.3.2-1.

The value of parameter “Dedicated BWP configuration” is DLBWP.1.2 and ULBWP.1.2.

Note: The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in clause A.4.6.4.3.3.

## A.4.6.4.7SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP

## A.4.6.4.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 makes correct reporting of L1-RSRP measurement when CD-SSB is outside active BWP. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.4.6.4.1.1-1.

The test environment is the same as in clause A.4.6.4.1 with following exceptions in Table A.4.6.4.1.2-1.

## A.4.6.4.7.2Test Requirements

The test requirements are the same as in clause A.4.6.4.1.3.

## A.4.6.4.8SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used

## A.4.6.4.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells in table A.4.6.4.8.1-1.

Table A.4.6.4.8.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.4.6.4.8.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.4.8.2-1 and Table A.4.6.4.8.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. During time duration T1, the UE shall not have any timing information of NR cell 2.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.4.6.4.8.2-1: General test parameters

Table A.4.6.4.8.2-2: SSB specific test parameters

## A.4.6.4.8.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than [620ms] plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.5CLI measurements

## A.4.6.5.1SRS-RSRP measurement with non-DRX

## A.4.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of SRS-RSRP measurement. This test will verify the SRS-RSRP measurement requirements in clause 9.7.2.5 with the testing configurations for NR cells in table A.4.6.5.1.1-1.

Table A.4.6.5.1.1-1: Applicable NR configurations for FR1 SRS-RSRP test

## A.4.6.5.1.2Test Parameters

Two cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters for PSCell is given in Table A.4.6.5.1.2-1 and A.4.6.5.1.2-2 below and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system transmits SRS resource for measurement in the DL slot according to the SRS configuration in table A.4.6.5.1.2-4 and the test parameters for the (virtual) neighbour cell UE in table A.4.6.5.1.2-3. During the test, the test system does not transmit PDCCH/PDSCH/OCNG on SRS symbol to be transmitted and on 1 data symbol before SRS to be transmitted.

Table A.4.6.5.1.2-1: General test parameters for SRS-RSRP event triggered reporting for PSCell in FR1

Table A.4.6.5.1.2-2: NR Cell specific test parameters for SRS-RSRP event triggered reporting for PSCell in FR1

Table A.4.6.5.1.2-3: NR Cell specific test parameters for SRS-RSRP event triggered reporting for neighbour cell UE

Table A.4.6.5.1.2-4: SRS configuration for measurement reporting

## A.4.6.5.1.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 60 ms from the beginning of time period T2.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.5.2CLI-RSSI measurement with non-DRX

## A.4.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of CLI-RSSI measurement. This test will verify the CLI-RSSI measurement requirements in clause 9.7.3.5 with the testing configurations for NR cells in table A.4.6.5.2.1-1.

Table A.4.6.5.2.1-1: Applicable NR configurations for FR1 CLI-RSSI test

## A.4.6.5.2.2Test Parameters

Two cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters for PSCell is given in Table A.4.6.5.2.2-1 and A.4.6.5.2.2-2 below and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event I1 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively.

During the test, the test system does not transmit PDCCH/PDSCH/OCNG on symbols for CLI-RSSI measurement resource and on 1 data symbol before. The CLI-RSSI measurement resource configuration is in table A.4.6.5.2.2-3.

Table A.4.6.5.2.2-1: General test parameters for CLI-RSSI event triggered reporting for PSCell in FR1

Table A.4.6.5.2.2-2: NR Cell specific test parameters for CLI-RSSI event triggered reporting for PSCell in FR1

Table A.4.6.5.2.2-3: CLI-RSSI measurement resource configuration for measurement reporting

## A.4.6.5.2.3Test Requirements

The UE shall send one Event I1 triggered measurement report, with a measurement reporting delay less than 20 ms from the beginning of time period T2. The nominal RSSI used to evaluate the requirement shall be based on Io.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.4.6.6Measurements with autonomous gaps

A.4.6.6.1EN-DC intra-frequency CGI identification of NR FR1 cell with autonomous gaps in synchronous EN-DC

A.4.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements for intra-frequency identification of a new CGI of NR FR1 cell with autonomous gaps in clause 9.11 for EN-DC.

The test scenario comprises of one E-UTRA carrier and one NR FR1 carrier. Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1) on E-UTRA RF channel 1, NR FR1 PSCell (Cell 2) and NR FR1 neighbour cell (Cell 3) on NR RF channel 1. The supported test configurations are shown in table A.4.6.6.1.1-1 below. The test parameters for NR Cells are given in Tables A.4.6.6.1.2-2 and A.4.6.6.1.2-3 below. The test parameters and applicability for the E-UTRAN PCell are defined in clause A.3.7.2.1. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 3. Starting T2, Cell 3 becomes detectable and the UE is expected to detect and send a measurement report.

An RRC message implying SI reading shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI which cellForWhichToReportCGI set to the physical cell identity of Cell 3. The start of T3 is the instant when the last TTI containing the RRC message implying SI reading of the neighbour cell (Cell 3) using autonomous gap is sent to the UE.

Table A.4.6.6.1.1-1: intra-frequency CGI identification of NR FR1 cell with autonomous gaps in synchronous EN-DC

Table A.4.6.6.1.1-2: General test parameters for intra-frequency CGI identification of NR FR1 cell with autonomous gaps in synchronous EN-DC

Table A.4.6.6.1.1-3: Cell specific test parameters for intra-frequency CGI identification of NR FR1 cell with autonomous gaps in synchronous EN-DC

## A.4.6.6.1.2Test Requirements

The UE shall transmit a measurement report containing the cell global identifier of Cell 3 within 260 ms from the start of T3.

Test requirement = RRC Procedure delay + Tidentify_CGI_NR + TTI insertion uncertainty

= 15 + 240 + 2

= 257 ms, allow 260 ms.

The UE shall be scheduled continuously throughout the test, and from the start of T3 until 260 ms the number of interrupted slots shall not exceed the allowed number specified in clause 8.2.1.2.16.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.7L1-SINR measurement for beam reporting

A.4.6.7.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR when DRX is not used

A.4.6.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement based on CSI-RS CMR without dedicated IMR. This test will partly verify the L1-SINR measurement requirements in clause 9.8.4.1, with the testing configurations for NR cells in table A.4.6.7.1.1-1.

Table A.4.6.7.1.1-1: Applicable NR configurations for FR1 CSI-RS based L1-SINR test

A.4.6.7.1.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.7.1.2-1 and Table A.4.6.7.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2,4,5 and 8 for Config 3,6) of a frame and UE provides the report back based on the reporting configuration as defined in table A.4.6.7.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.4.6.7.1.2-1: General test parameters

Table A.4.6.7.1.2-2: CSI-RS specific test parameters

A.4.6.7.1.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.27.1.1 and relative accuracy requirement in clause 10.1.27.1.2.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.7.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used

## A.4.6.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with SSB based CMR and CSI-IM based IMR in clause 9.8.4.2, with the testing configurations for NR cells in table A.4.6.7.2.1-1.

Table A.4.6.7.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-IM based IMR

## A.4.6.7.2.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.7.2.2-1 and Table A.4.6.7.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-IM resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-IM resources as IMR.

Table A.4.6.7.2.2-1: General test parameters

Table A.4.6.7.2.2-2: SSB specific test parameters

## A.4.6.7.2.3Test Requirements

The UE shall send L1-SINR report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-SINR report including results of both SSB#0+CSI-IM#0 and SSB#1+CSI-IM#1 while meeting the accuracy requirement in clause 10.1.27.2. The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.7.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used

## A.4.6.7.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR cofigured in clause 9.8.4.3, with the testing configurations for NR cells in table A.4.6.7.3.1-1.

Table A. A.4.6.7.3.1-1: Applicable NR configurations for FR1 L1-SINR test with CMR and dedicated IMR

## A.4.6.7.3.2Test parameters

There are two cells in the test, E-UTRAN PCell (Cell 1) and FR1 PSCell (Cell 2). The test parameters and applicability for Cell 1 are defined in clause A.3.7.2. The test parameters for the Cell 2 are given in Table A.4.6.7.3.2-1 and Table A.4.6.7.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-RS as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources and the associated IMR. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2,4,5 and 8 for Config 3,6) of a frame and UE provides the report back based on the reporting configuration as defined in table A.4.6.7.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-RS as IMR.

Table A.4.6.7.3.2-1: General test parameters

Table A.4.6.7.3.2-2: CSI-RS specific test parameters

## A.4.6.7.3.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-SINR report at slot 26 from the reception of DCI triggering the L1-SINR measurement. The L1-SINR report shall include the results for both CSI-RS#0 as CMR + CSI-RS#0 as IMR and CSI-RS#1 as CMR + CSI-RS#1 as IMR while meeting the accuracy requirement in clause 10.1.27.3.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.8CSI-RS based intra-frequency Measurement

## A.4.6.8.1EN-DC event triggered reporting tests without gap under DRX

## A.4.6.8.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the CSI-RS based L3 intra-frequency requirements in clause 9.10.2.

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test parameters for PSCell are given in Table A.4.6.8.1.1-1, A.4.6.8.1.1-2, and A.4.6.8.1.1-3 below and the test parameters and applicability for the E-UTRAN cell are defined in clause A.3.7.2. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used for the CSI-RS based L3 intra-frequency measurements. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of cell 3.

UE is allocated with PUSCH resource at every DRX cycle.

NOTE:TAT= infinite based on the DRX configuration used in test.

Table A.4.6.8.1.1-1: Supported test configurations

Table A.4.6.8.1.1-2: General test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX

Table A.4.6.8.1.1-3: NR Cell specific test parameters for EN-DC intra-frequency event triggered reporting without gap for PSCell in FR1 with DRX

## A.4.6.8.1.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE is not required to read the SSB index indicated by associatedSSB in the neighbour cell in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.4.6.9CSI-RS based inter-frequency Measurement

## A.4.6.9.1EN-DC event triggered reporting tests for FR1 cell when non-DRX is used

## A.4.6.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell measurement requirements in clause 9.10.3.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.4.6.9.1.1-1, A.4.6.9.1.1-2, and A.4.6.9.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in Table A.4.6.9.1.1-2 is provided for a UE that does not support per-FR gap and in test 2 measurement gap pattern configuration #4 as defined in Table A.4.6.2.2.1-2 is provided for UE that support per-FR gap. If a UE supports per-FR gap and gap pattern configuration #4, it is only required to pass test 2. Otherwise, it is only required to pass test 1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.4.6.9.1.1-1.

Table A.4.6.9.1.1-1: EN-DC event triggered reporting tests with SSB index reading for FR1-FR1

Table A.4.6.9.1.1-2: General test parameters for EN-DC inter-frequency event triggered reporting

Table A.4.6.9.1.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting

## A.4.6.9.1.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

In test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 2000 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90%.

The UE is required to read the SSB index indicated by associatedSSB in the neighbour cell in this test.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.
