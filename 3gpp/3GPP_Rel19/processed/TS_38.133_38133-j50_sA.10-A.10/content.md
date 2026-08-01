---
type: spec
aliases:
  - 38.133_38133-j50_sA.10-A.10
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.10-A.10/content.md"
---
# TS 38.133 38133-j50_sA.10-A.10

## A.10EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1

Editor’s note: Test cases for EN-DC with NR PSCell under CCA and SCell under CCA are also included here.

## A.10.1RRC_CONNECTED state mobility

## A.10.1.1RRC connection mobility control

## A.10.1.1.1Random Access

## A.10.1.1.1.14-step RA type contention-based random access for NR PSCell with CCA

## A.10.1.1.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.1.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.1.1-2.

Table A.10.1.1.1.1.1-1: Supported test configurations for contention based random access test in FR1 for PSCell with CCA

Table A.10.1.1.1.1.1-2: General test parameters for contention based random access test in FR1 for PSCell with CCA

## A.10.1.1.1.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.10.1.1.1.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2A.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.10.1.1.1.1.2:

-The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

-In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2A.2.1.4, the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

## A.10.1.1.1.1.2.5Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2A.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.10.1.1.1.24-step RA type non-contention based random access for NR PSCell with CCA

## A.10.1.1.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.2.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.2.1-2.

Table A.10.1.1.1.2.1-1: Supported test configurations for non-contention based random access test in FR1 for PSCell with CCA

Table A.10.1.1.1.2.1-2: General test parameters for non-contention based random access test in FR1 for PSCell with CCA

## A.10.1.1.1.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

## A.10.1.1.1.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.10.1.1.1.2.2:

-The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

-In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.2.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.2.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.32-step RA type contention-based random access for NR PSCell with CCA

## A.10.1.1.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the behaviour of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.3.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.3.1-2.

Table A.10.1.1.1.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR1 for PSCell with CCA

Table A.10.1.1.1.3.1-2: General test parameters for 2-step RA type contention based random access test in FR1 for PSCell with CCA

## A.10.1.1.1.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.10.1.1.1.3.2.1MsgA Transmission

To test the UE behaviour specified in clause 6.2.2A.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB, if the UL CCA is successful.

below are relevant for all cases of MsgA transmissions described within the clause A.10.1.1.1.3.2:

-The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

-The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure. In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.3.2.2MsgB Reception

To test the UE behaviour specified in clause 6.2.2A.3.1.2 the System Simulator shall transmit a MsgB with fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble .

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.3 the System Simulator shall transmit a MsgB with fallbackRAR containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.42-step RA type non-contention based random access for NR PSCell with CCA

## A.10.1.1.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.4.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.4.1-2.

Table A.10.1.1.1.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR1 for PSCell with CCA

Table A.10.1.1.1.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR1 for PSCell with CCA

## A.10.1.1.1.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

## A.10.1.1.1.4.2.1MsgA Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.10.1.1.1.4.2:

-The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

-The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be   dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.4.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 5 MsgA transmissions have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power if Random Access Responses Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be   dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.1.1.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be   dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.10.1.2Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA

## A.10.1.2.1Test Purpose and Environment

This test is to verify the requirement for E-UTRA handover with NR PSCell change, where NR PSCell is on carrier with CCA.  The requirements for EN-DC HO with PSCell change on CCA are specified in clause 5.9 in E-UTRA RRM specification [15] for the case when the target PSCell is on carrier with CCA. Supported test configurations are shown in table A.10.1.2.1-1.

Table A.10.1.2.1-1 gives general test configurations for Handover with PSCell from EN-DC to EN-DC, table A.10.1.2.1-2 provides general test parameters for Handover from E-UTRA to E-UTRA cell in EN-DC to EN-DC, table A.10.1.2.1-3 provides E-UTRAN cell specific test parameters for Handover with PSCell from EN-DC to EN-DC, table A.10.1.2.1-4 provides general test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA, table A.10.1.2.1-5 provides cell specific test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA.

In the test there are four cells: Cell 1 and Cell 2 are PCell and target PCell on E-UTRA carrier, Cell 3 and Cell 4 are PSCell and target PSCell on NR CCA carrier. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) and Cell 3 (NR PSCell) with EN-DC mode.

At the start of time duration T1, the UE do not have any information of cell 2 and cell 4. AT the end of T1, UE is configured with neighbour cell measurements on the Cell 3 and Cell 4 for Event A3 conditional measurement report.

During T2, UE acquires the timing information of Cell 3 and Cell 4 and performs L3-RSRP measurements on the configured neighbour cells. UE sends measurement report to the Cell 1 to indicate the event triggering condition A3 is satisfied for the configured for neighbour cells.  By end of T2, E-UTRA PCell (Cell 1) shall send a RRC message implying handover with PSCell change.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover with PSCell. UE shall complete PRACH transmission to PCell and PSCell by end of T3.

Table A.10.1.2.1-1: General test configurations for Handover with PSCell from EN-DC to EN-DC with CCA on NR Cell

Table A.10.1.2.1-2: General test parameters for Handover from E-UTRA to E-UTRA cell in EN-DC to EN-DC

Table A.10.1.2.1-3: E-UTRAN cell specific test parameters for Handover with PSCell from EN-DC to EN-DC

Table A.10.1.2.1-4: General test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA

Table A.10.1.2.1-5: Cell specific test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA

## A.10.1.2.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 60 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover requirements for handover with PSCell for EN-DC is defined in clause 5.9 in [15] as:

DHOwithPSCel_PCell = TRRC_delay + Tsearch + TIU + Tprocessing

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tsearch = 0 ms for known cell.

TIU = 15 ms in the test configuration.

Tprocessing = 25 ms for source Cell and target Cell are in the same FR.

This gives a total of 60 ms for handover delay.

The UE shall transmit the PRACH preamble to Cell 4 less than DHOwithPSCell_PSCell from the beginning of time period T3.

NOTE: The PSCell change delay for handover with PSCell for EN-DC is defined in clause 5.8 in [15] as:

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TIU_PSCell + 2 ms

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tprocessing = 25 ms for source Cell and target Cell are in the same FR.

Tsearch = 0 ms for known cell.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3) *10 + 10 ms

L2 is the number of SMTC occasions not available at the UE during the time tracking period where L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2, L3 and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2]. Test equipment should make sure that LCCA_DL and LCCA_UL are not exceeded during a test by monitoring the number of CCA failures and preventing additional CCA failures from happening after LCCA_DL or LCCA_UL is reached.

The rate of correct PSCell addition observed during repeated tests shall be at least 90 %.

## A.10.2Timing

## A.10.2.1UE transmit timing

## A.10.2.1.1UE Transmit Timing Test with PSCell under DL CCA

## A.10.2.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb when PSCell is subject to DL CCA and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2. Supported test configurations are shown in table 10.2.1.1.1-1.

Table A.10.2.1.1.1-1: Supported test configurations for UE transmit timing test

The test consists of E-UTRA PCell and NR PSCell, which is subject to DL CCA. The configuration for E-UTRA is given in A.3.7.2.1. Table A.10.2.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.10.2.1.1.1-3.

Table A.10.2.1.1.1-2: Cell Specific Test Parameters for UE Transmit Timing test

Table A.10.2.1.1.1-3: SRS Configuration for UE transmit timing

## A.10.2.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up E-UTRA PCell according to parameters given in table A.3.7.2.1-1 and setup NR PSCell according to parameters given in table A.10.2.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset)×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.10.2.1.1.2-1

Table A.10.2.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.10.2.2UE timing advance

## A.10.2.2.1UE Timing Advance Adjustment Accuracy with PSCell under DL CCA

## A.10.2.2.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.10.2.2.1.2Test Parameters

Supported test configurations are shown in table A.10.2.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.10.2.2.1.2-2, A.10.2.2.1.2-3 and A.10.2.2.1.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and cell 2 is the PSCell which is subject to DL CCA is in the secondary Timing Advance Group (sTAG). Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.10.2.2.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for PSCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.10.2.2.1.2-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321, shall be configured so that it does not expire in the duration of the test.

Table A.10.2.2.1.2-1: Supported test configurations for timing advance test

Table A.10.2.2.1.2-2: General test parameters for timing advance test

Table A.10.2.2.1.2-3: Cell specific test parameters for timing advance test

Table A.10.2.2.1.2-4: Sounding Reference Symbol Configuration for timing advance test

## A.10.2.2.1.3Test Requirements

The UE shall apply the signalled Timing Advance value for PSCell in sTAG to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy for PSCell in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.10.3Signalling characteristics

## A.10.3.1Radio link monitoring

## A.10.3.1.1Introduction

In the test cases specified in clause A.10.3.1, any uplink signal transmitted by the UE is used for detecting the in-/out-of-sync state of the UE. In terms of measurement, the uplink signal is verified based on the UE output power:

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means uplink signal

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means no uplink signal.

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

## A.10.3.1.2Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode

## A.10.3.1.2.1Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.10.3.1.2.1-1. The test parameters are given in tables A.10.3.1.2.1-2, A.10.3.1.2.1-3, and A.10.3.1.2.1-4 below. There are two cells in the test: Cell 1 is the E-UTRAN PCell, and Cell 2 is the FR1 PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

The test consists of three successive time periods, with time duration of T1, T2 and T3, respectively. Figure A.10.3.1.2.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in the test.

Table A.10.3.1.2.1-1: Supported test configurations.

Table A.10.3.1.2.1-2: General test parameters for PSCell out-of-sync testing in non-DRX mode.

Table A.10.3.1.2.1-3: Cell-specific test parameters for PSCell out-of-sync testing in non-DRX mode.

Table A.10.3.1.2.1-4: Measurement gap configuration for PSCell out-of-sync testing in non-DRX mode.

Figure A.10.3.1.2.1-1: SNR variation for out-of-sync testing.

## A.10.3.1.2.2Test requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

-During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

-The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.10.3.1.3Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode

## A.10.3.1.3.1Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.10.3.1.3.1-1. The test parameters are given in tables A.10.3.1.3.1-2, and A.10.3.1.3.1-3 below. There are two cells in the test: Cell 1 is the E-UTRAN PCell, and Cell 2 is the FR1 PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model.

Table A.10.3.1.3.1-1: Supported test configurations.

Table A.10.3.1.3.1-2: General test parameters for PSCell in-sync testing in non-DRX mode.

Table A.10.3.1.3.1-3: Cell-specific test parameters for PSCell in-sync testing in non-DRX mode.

Figure A.10.3.1.2.1-1: SNR variation for in-sync testing.

## A.10.3.1.3.2Test requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.10.3.1.4Void

## A.10.3.1.4.1Void

## A.10.3.1.4.2Void

## A.10.3.1.5Void

## A.10.3.1.5.1Void

## A.10.3.1.5.2Void

## A.10.3.2Void

## A.10.3.3SCell activation and deactivation delay

## A.10.3.3.1SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle

## A.10.3.3.1.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.10.3.3.1.1-1.

The test parameters are given in table A.10.3.3.1.1-2 and cell-specific parameters for NR cells are provided in table A.10.3.3.1.1-3 below. Cell-specific parameters for EUTRA PCell are provided in clause A.3.7.2.1.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in E-UTRA, Cell 2 (PSCell) on radio channel 2 (PSCC) in NR, and Cell 3 (SCell) on radio channel 3 (SCC) in NR. Before the test starts the UE is connected to Cell 1 and Cell 2, but is not aware of Cell 3, as the UE is only monitoring PCC and PSCC. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PSCell for the activated SCell at latest in slot m +  (THARQ+ Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, as defined in clause 8.3A.2. The UE shall start reporting CSI in PSCell in first available uplink resource for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting following slot m+  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption shall fall within the time window specified in clause 8.3A.2. THARQ+3 msNR slot length

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot . Any PSCell interruption shall fall within the time window specified in clause 8.3A.3.n+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.10.3.3.1.1-1: Supported test configurations for SCell Activation and Deactivation of known NR SCell with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

Table A.10.3.3.1.1-2: General test parameters for known SCell activation case with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

Table A.10.3.3.1.1-3: Cell specific test parameters for known SCell activation case with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

## A.10.3.3.1.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PSCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle

## A.10.3.3.2.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.10.3.3.1.1-1 above.

The test parameters are same as in table A.10.3.3.1.1-2 above, except for parameters listed below in table A.10.3.3.2.1-1. The cell-specific parameters are same as in table A.10.3.3.1.1-3 above.

The test execution is the same as described in clause A.10.3.3.1 above.

Table A.10.3.3.2.1-1: General test parameters for known NR SCell activation with NR PSCell and SCell under CCA, 640 ms SCell measurement cycle

## A.10.3.3.2.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PSCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB_MAX + L2,1* TSMTC_MAX.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.10.3.3.3SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA

## A.10.3.3.3.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.10.3.3.1.1-1 above.

The test parameters are same as in table A.10.3.3.1.1-2 above, except for parameters listed below in table A.10.3.3.3.1-1. The cell-specific parameters are same as in table A.10.3.3.1.1-3 above.

The test execution is the same as described in clause A.10.3.3.1 above.

Table A.10.3.3.3.1-1: General test parameters for unknown NR SCell activation with NR PSCell and SCell under CCA

## A.10.3.3.3.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PSCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB_MAX + L3,1* TSMTC_MAX.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.10.3.4Beam failure detection and link recovery procedures

## A.10.3.4.1EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode

## A.10.3.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.10.3.4.1.1-1, A.10.3.4.1.1-2, and A.10.3.4.1.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.4.1.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.10.3.4.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA model. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.10.3.4.1.1-1: Supported test configurations for FR1 PSCell with CCA

Table A.10.3.4.1.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.10.3.4.1.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.10.3.4.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.10.3.4.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 410 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.10.3.4.2EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode

## A.10.3.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.10.3.4.2.1-1, A.10.3.4.2.1-2, and A.4.5.5.2.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.4.2.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.10.3.4.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA model. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.10.3.4.2.1-1: Supported test configurations for FR1 PSCell with CCA

Table A.10.3.4.2.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.10.3.4.2.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.10.3.4.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.10.3.4.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 3850 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.10.3.5Active BWP switching

## A.10.3.5.1UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC

A.10.3.5.1.1Test Purpose and Environment

The purpose of this test is to verify the UL BWP switch delay requirement defined in clause 8.6.4.

The supported test configurations are shown in table A.10.3.5.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in A.10.3.5.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.10.3.5.1.1-2. SRS configuration used in the test is specified in table A.10.3.5.1.1-4.

The UE shall be configured with PRACH configuration on UL BWP on which the UE shall switch after the consistent UL LBT failure detection.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2.

-UE is configured with 2 different UE-specific downlink and uplink bandwidth parts on Cell 2: DL BWP-1, DL BWP-2, UL BWP-1 and UL BWP-2 before starting the test. DL BWP-1 and DL BWP-2 always include bandwidth of the initial DL BWP and SSB. UL BWP-1 and UL BWP-2 always include bandwidth of the SRS.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is DL BWP-1.

-UE is indicated in firstActiveUplinkBWP-Id that the active UL BWP is UL BWP-1.

-UE is configured with LBT-FailureRecoveryConfig parameters for Cell 2.

The cell has constant signal levels throughout the test. The test consists of 2 successive time periods, with durations of T1 and T2, respectively.

During T1,

-Time period T1 starts when the UE has received the SRS configuration for periodic SRS transmission on active UL BWP-1.

-The UE shall perform UL CCA before SRS transmission.

-The parameter UL CCA probability PCCA is set to 0 during T1. This requires the test system to set energy level above the detection level during portion of the UL slot where the UE performs UL CCA. This in turn forces the UE to fail the UL CCA. The UE consistently fails UL CCA during T1 and is therefore unable to transmit SRS.

During T2,

-T2 starts when the UE detects consistent UL LBT failures i.e. when total number of UL LBT failures in Cell 2 on active UL BWP-1 exceeds lbt-FailureInstanceMaxCount during lbt-FailureDetectionTimer.

-The UE upon detected consistent UL LBT failure starts the LBT recovery mechanism, which requires the UE to switch to active UL BWP-2 in Cell 2 and to send PRACH in the active UL BWP-2.

-Staring from T2, the UE shall be able to send PRACH in the active UL BWP-2 within the delay specified in clause 8.6.4.

Table A.10.3.5.1.1-1: Supported test configurations for UL BWP switch test in EN-DC

Table A.10.3.5.1.1-2: General test parameters for UL BWP switch in EN-DC

Table A.10.3.5.1.1-3: NR Cell specific test parameters for UL BWP switch test in EN-DC

Table A.10.3.5.1.1-4: Sounding Reference Symbol Configuration for UL BWP Switch Test in EN-DC

## A.10.3.5.1.2Test Requirements

The UE capable of bwp-SwitchingDelay type1 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 2 (PSCell) less than 21.5 ms from the beginning of time period T1.

The UE capable of bwp-SwitchingDelay type2 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 2 (PSCell) less than 23 ms from the beginning of time period T1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The above delay is calculated as follows:’

The active UL BWP switch delay from UL BWP-1 to UL BWP-2 can be expressed as:

TBWPswitchDelay*Tslot +1*Tslot + (1+ L3)*TSSB,RO + 10 ms

Where:

-TBWPswitchDelay = 1 ms (2 slots) and 2.5 ms (5 slots) for bwp-SwitchingDelay [2] type1 and type2 UE capabilities according to clause 8.6.4.

-Tslot = It is the slot length. It is 0.5 ms for 30 kHz.

-L3 = It is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3= 0 during T2 since PCCA = 1.

-TSSB,RO = 10 ms according to FR1 PRACH configuration 1.

This gives a total of 21.5 ms and 23 ms for type1 and type2 UE respectively.

## A.10.3.5.2DCI-based and Timer-based Active BWP Switch

## A.10.3.5.2.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.10.3.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in TS38.133 clause 8.6, and interruption requirement for E-UTRA victim cell defined in TS36.133 clause 7.32.2.7. Supported test configurations are shown in table A.10.3.5.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.10.3.5.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.10.3.5.2.1.1-3 below.

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

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after DL slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after DL slot (i+TBWPswitchDelay).

The starting time of PCell(Cell 1) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PSCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell at latest at the beginning of the DL slot right after DL slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after DL slot (j+TBWPswitchDelay).

The starting time of PCell(Cell 1) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PSCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of PSCell, respectively.

Table A.10.3.5.2.1.1-1: DL BWP switch supported test configurations

Table A.10.3.5.2.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.10.3.5.2.1.1-3.: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

A.10.3.5.2.1.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell in the DL slot right after DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell in the DL slot right after DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start time of PCell interruption during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start time of PCell interruption of during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in TS36.133 clause 7.32.2.7.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.10.3.5.2.2E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC

A.10.3.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirements for NR victim cell defined in clause 8.2.1.2.7 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations are shown in table A.10.3.5.2.2.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.10.3.5.2.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.10.3.5.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and SCell (Cell 3) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for SCell, BWP-0 in Cell 3 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in SCell.

-UE is configured with a bwp-InactivityTimer timer value for PSCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PSCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell no later than at the beginning of the DL slot right after slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-2 starting from the beginning of the DL slot right after slot (i+TBWPswitchDelay).

PCell(Cell 1) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

SCell(Cell 3) interruption due to BWP switch on PSCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PSCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the beginning slot of the DL subframe immediately after the slot wherein bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PSCell at latest at the beginning of the DL slot right after slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (j+TBWPswitchDelay).

PCell(Cell 1) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

SCell(Cell 3) interruption due to BWP switch of PSCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PSCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

The test equipment verifies that potential interruption to E-UTRA PCell and NR SCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell and SCell during BWP switch of PSCell, respectively.

Table A.10.3.5.2.2.1-1: DL BWP switch supported test configurations

Table A.10.3.5.2.2.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.10.3.5.2.2.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

A.10.3.5.2.2.2Test Requirements

During T1, the UE shall start to send the ACK for PSCell in the DL slot right after slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell in the DL slot right after slot (j+TBWPswitchDelay+k11).

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 7.32.2.7 of TS 36.133 [15].

During T1, the start of the interruption of SCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of SCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of SCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.6.2.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

Editor’s note: FFS value of k1 for type 1 and type 2 UE.

## A.10.3.5.3RRC-based Active BWP Switch

## A.10.3.5.3.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.10.3.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.10.3.5.3.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2) as given in table A.10.3.5.3.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell are specified in table A.10.3.5.3.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PSCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC) as defined in clause 8.6.3 and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC).

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.10.3.5.3.1.1-1: DL BWP switch supported test configurations

Table A.10.3.5.3.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

Table A.10.3.5.3.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

A.10.3.5.3.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell in the beginning of the DL slot right after  slot (i+ TRRCprocessingDelay+TBWPswitchDelayRRC ).

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.10.3.6PSCell addition and release delay

## A.10.3.6.1Addition and Release Delay of known NR PSCell on the carrier under CCA

## A.10.3.6.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delays on the carrier under CCA under EN-DC are within the requirements stated in clause 7.31A.2 [15] for the case when the PSCell is known by the UE at the time of addition.

Supported test configurations are shown in A.10.3.6.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.1-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in tables A.10.3.6.1.1-2 and cell-specific parameters in A.10.3.6.1.1-3 below. The test consists of five successive time periods with duration of T1, T2, T3, T4 and T5 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event B1 is configured for neighbour cell (Cell 2). Before the start of T2 the UE is configured with the measurement gaps (gap pattern Id # 0). The Cell 2 becomes known to the UE during T2. Therefore, during T2 the UE shall report Event B1. The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2.

The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The point in time at which the RRC message to add PSCell (Cell 2) is received at the UE antenna connector defines the start of period T4.

The test system shall observe the periodic reporting of CSI for PSCell during T5. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T5.

The test system shall send a RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell 2) shall be sent to the UE during period T5, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell 2) is received at the UE antenna connector defines the start of period T6.

Table A.10.3.6.1.1-1: Supported test configurations for FR1 PSCell

Table A.10.3.6.1.1-2: General Test Parameters for PSCell Addition and Release

Table A.10.3.6.1.1-3: Cell Specific Parameters for PSCell Addition and Release

## A.10.3.6.1.2Test Requirements

The UE shall transmit the PRACH to PSCell at latest Tconfig_PSCell_withCCA Note1 into T4.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T5.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T5

The UE shall stop sending CSI reports for PSCell in at latest 20 ms into T6.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

NOTE 1:The PSCell addition delay can be expressed as follows as specified in clause 7.31A.2 [15]:

Tconfig_PSCell_withCCA = TRRC_delay + Tprocessing + Tsearch_withCCA + T∆_withCCA + TPSCell_ DU_withCCA + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 20 ms

Tsearch_withCCA = 0

T∆_withCCA = (1+ L2)*20 ms

TPSCell_ DU_withCCA = 20 ms.

L2 is the number of SMTC occasions not available at the UE for fine time tracking and acquiring full timing information, where L2  LCCA_DL.

## A.10.3.7Void

## A.10.4Measurement procedure

## A.10.4.1Intra-frequency measurements

## A.10.4.1.1Event-triggered reporting tests on PSCC without gaps under non-DRX

## A.10.4.1.1.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

## A.10.4.1.1.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and two cells on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model: PSCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.10.4.1.1.2-1 and A.10.4.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.10.4.1.1.2-1: Supported test configurations

Table A.10.4.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

Table A.10.4.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.10.4.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.1.2Void

## A.10.4.1.3Void

## A.10.4.1.4Event-triggered reporting tests on PSCC with per-UE gaps under DRX

## A.10.4.1.4.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

## A.10.4.1.4.2Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and two cells on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model: PSCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.10.4.1.4.2-1, A.10.4.1.4.2-2 and A.10.4.1.4.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.1.4.2-1: Supported test configurations

Table A.10.4.1.4.2-2: General test parameters for intra-frequency event triggered reporting with per-UE gaps

Table A.10.4.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.10.4.1.4.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.1.5Void

## A.10.4.1.6Void

## A.10.4.1.7Void

## A.10.4.1.8Void

## A.10.4.1.9Void

## A.10.4.1.10Void

## A.10.4.1.11Void

## A.10.4.1.12Void

## A.10.4.2Inter-frequency measurements

## A.10.4.2.1Void

## A.10.4.2.2Void

## A.10.4.2.3EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used

## A.10.4.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.3.1-1, A.10.4.2.3.1-2, and A.10.4.2.3.1-3.

In this test measurement gap pattern configuration # 0 as defined in table A.10.4.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.3.1-1.

Table A.10.4.2.3.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.3.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.3.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.4EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used

## A.10.4.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.    The test parameters and configurations are given in tables A.10.4.2.4.1-1, A.10.4.2.4.1-2, and A.10.4.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.4.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.4.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.4.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.4.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.5EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used

## A.10.4.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.    The test parameters and configurations are given in tables A.10.4.2.5.1-1, A.10.4.2.5.1-2, and A.10.4.2.5.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.10.4.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.5.1-1.

Table A.10.4.2.5.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.5.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.5.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.10.4.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.6EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used

## A.10.4.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2. The test parameters and configurations are given in tables A.10.4.2.6.1-1, A.10.4.2.6.1-2, and A.10.4.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.6.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.6.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.6.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.6.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.6.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.7EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used

## A.10.4.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.7.1-1, A.10.4.2.7.1-2, and A.10.4.2.7.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.2.7.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.7.1-1.

Table A.10.4.2.7.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.7.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.7.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.7.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.8EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used

## A.10.4.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.8.1-1, A.10.4.2.8.1-2, and A.10.4.2.8.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.8.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.8.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.8.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.8.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.8.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.8.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.8.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.8.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.9EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used

## A.10.4.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.9.1-1, A.10.4.2.9.1-2, and A.10.4.2.9.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.2.9.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.9.1-1.

Table A.10.4.2.9.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.9.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.9.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

## A.10.4.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.2.10EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used

## A.10.4.2.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.10.1-1, A.10.4.2.10.1-2, and A.10.4.2.10.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.10.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.10.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.10.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

Table A.10.4.2.10.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.10.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

Table A.10.4.2.10.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.10.4.2.10.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.10.4.2.10.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.3L1-RSRP measurements for beam reporting

## A.10.4.3.1SSB based L1-RSRP measurement on PSCC when DRX is not used

## A.10.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.10.4.3.1.2Test parameters

There are two cells in the test, E-UTRAN Pcell (Cell 1) and FR1 PSCell (Cell 2) which operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.4.3.1.2-1 and table A.10.4.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.1.2-1: General test parameters

Table A.10.4.3.1.2-2: SSB specific test parameters

## A.10.4.3.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.3.2SSB based L1-RSRP measurement on PSCC when DRX is used

## A.10.4.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.10.4.3.2.2Test parameters

There are two cells in the test, E-UTRAN Pcell (Cell 1) and FR1 PSCell (Cell 2) which operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.4.3.2.2-1 and table A.10.4.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.2.2-1: General test parameters

Table A.10.4.3.2.2-2: SSB specific test parameters

## A.10.4.3.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.3.3SSB based L1-RSRP measurement on SCC when DRX is not used

## A.10.4.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.3.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.10.4.3.3.2Test parameters

There are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2), and FR1 SCell (Cell 3). Cell 2 and Cell 3 operate on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 and Cell 3 are given in table A.10.4.3.3.2-1 and table A.10.4.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.3.2-1: General test parameters

Table A.10.4.3.3.2-2: SSB specific test parameters

## A.10.4.3.3.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 3.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.3.4SSB based L1-RSRP measurement on SCC when DRX is used

## A.10.4.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.4.1-1.

Table A.10.4.3.4.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.10.4.3.4.2Test parameters

There are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2), and FR1 SCell (Cell 3). Cell 2 and Cell 3 operate on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 and Cell 3 are given in table A.10.4.3.4.2-1 and table A.10.4.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.4.2-1: General test parameters

Table A.10.4.3.4.2-2: SSB specific test parameters

## A.10.4.3.4.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 3.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.4E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA

## A.10.4.4.1E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.10.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements under CCA and clause 8.1.2.4.22A of TS 36.133 [15] for E-UTRAN TDD-NR measurements under CCA.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.1.1-1, A.10.4.4.1.1-2, A.10.4.4.1.1-3 and A.10.4.4.1.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.10.4.4.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.10.4.4.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.10.4.4.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.10.4.4.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.10.4.4.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index. Tidentify_irat_cca_without_index is defined in defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.4.2E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.10.4.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.2.1-1, A.10.4.4.2.1-2, A.10.4.4.2.1-3 and A.10.4.4.2.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.10.4.4.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.10.4.4.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.10.4.4.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.10.4.4.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.10.4.4.2.2Test Requirements

In test, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.4.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.10.4.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.3.1-1, A.10.4.4.3.1-2, A.10.4.4.3.1-3 and A.10.4.4.3.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.4.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.3.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

Table A.10.4.4.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

Table A.10.4.4.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

Table A.10.4.4.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

## A.10.4.4.3.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.4.4.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.10.4.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.4.1-1, A.10.4.4.4.1-2, A.10.4.4.4.1-3 and A.10.4.4.4.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.10.4.4.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.4.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

Table A.10.4.4.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

Table A.10.4.4.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

Table A.10.4.4.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

## A.10.4.4.4.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.5Measurement performance

## A.10.5.1SS-RSRP

## A.10.5.1.1Intra-frequency measurement accuracy on a CCA serving cell

## A.10.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.36.1.1 and 10.1.36.1.2 when the serving cell is subject to CCA.

## A.10.5.1.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. Supported test configurations are shown in table A.10.5.1.1.1-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.10.5.1.1.1-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell, and Cell 3 is the target cell.

Table A.10.5.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.10.5.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.10.5.1.1.3Test Requirements

The SS-RSRP measurement accuracy for cell 2 and cell 3 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.36.1.1 and 10.1.36.1.2.

## A.10.5.1.2Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

## A.10.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.37.1.1 and 10.1.37.1.2 for inter-frequency measurements with the testing configurations in table A.10.5.1.2.1-1.

Table A.10.5.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.10.5.1.2.2Test parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7A.2.1. The test parameters for the Cell 2 and Cell 3 are given in table A.10.5.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.10.5.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.10.5.1.2.2-1: SS-RSRP inter-frequency test parameters

## A.10.5.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the Absolute requirement in clause 10.1.4.1.1 and Relative requirement in clause 10.1.37.1.1 and 10.1.37.1.2.

## A.10.5.2SS-RSRQ

## A.10.5.2.1Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

## A.10.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

## A.10.5.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.10.5.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.10.5.2.1.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.10.5.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.10.5.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.10.5.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

## A.10.5.2.2Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

## A.10.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limitsThis test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2 for inter-frequency measurements with the testing configurations in table A.10.5.2.2.2-1.

## A.10.5.2.2.2Test Parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.4.7.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.10.5.2.2.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.10.5.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.10.5.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.10.5.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

## A.10.5.3SS-SINR

## A.10.5.3.1Intra-frequency measurement accuracy on PSCC

## A.10.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.

## A.10.5.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.10.5.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.10.5.3.1.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell with CCA and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 2 and 3.

Table A.10.5.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.10.5.3.1.2-2: SS-SINR Intra frequency test parameters

## A.10.5.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

## A.10.5.3.2Inter-frequency measurement accuracy on PSCC

## A.10.5.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.32.1.1 and 10.1.32.1.2 for inter-frequency measurement.

## A.10.5.3.2.2Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.10.5.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.10.5.3.2.2-2. In all test cases, Cell 2 is the PSCell with CCA and Cell 3 is target cell with CCA. Cell 1 is the E-UTRA cell of which specific test parameters for this test case are specified in table A.3.7A.2.1-1. Three sub-tests (Test 1, Test 2 and Test 3) are provided different Noc on Cells 2 and 3.

Table A.10.5.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.10.5.3.2.2-2: SS-SINR Inter frequency test parameters

## A.10.5.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

## A.10.5.3.3Intra-frequency measurement accuracy on SCC

## A.10.5.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.

## A.10.5.3.3.2Test Parameters

In this test case, Cell 2 (PSCell) is on frequency 1 while Cell 3 (SCell) and Cell 4 (target cell) which are intra-frequency neighbors, are on frequency 2. Supported test configuration are shown in table A.10.5.3.3.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.10.5.3.3.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell with CCA, Cell 3 is the SCell with CCA, and Cell 4 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 2, 3 and 4.

Table A.10.5.3.3.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.10.5.3.3.2-2: SS-SINR Intra frequency test parameters

## A.10.5.3.3.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

## A.10.5.4L1-RSRP measurement for beam reporting with CCA serving cell

## A.10.5.4.1SSB based L1-RSRP measurement

## A.10.5.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.10.5.4.1.1-1.

Table A.10.5.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.10.5.4.1.2Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 2. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.5.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.10.5.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.10.5.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.10.5.4.1.3Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.33.1.

## A.10.5.5RSSI

## A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA

## A.10.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

## A.10.5.5.1.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, and Cell 2 is PSCell operating on a carrier frequency under CCA. RSSI is measured on channel number 1. Supported test configurations are shown in table A.10.5.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.10.5.5.1.2-2 and A.10.5.5.1.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.1.2-1: RSSI supported test configurations

Table A.10.5.5.1.2-2: RSSI test parameters

Table A.10.5.5.1.2-3: RSSI RMTC parameters

## A.10.5.5.1.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.10.5.5.2RSSI measurement accuracy on SCC with CCA

## A.10.5.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

## A.10.5.5.2.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, Cell 3 is SCell on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.10.5.5.2.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.10.5.5.2.2-2 and A.10.5.5.2.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.2.2-1: RSSI supported test configurations

Table A.10.5.5.2.2-2: RSSI test parameters

Table A.10.5.5.2.2-3: RSSI RMTC parameters

## A.10.5.5.2.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.10.5.5.3 Inter-frequency RSSI measurement accuracy on a carrier with CCA

## A.10.5.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

## A.10.5.5.3.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, and Cell 3 is the neighbour with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.10.5.5.3.2-1. The accuracy of RSSI inter-frequency measurements is tested by using the parameters in A.10.5.5.3.2-2 and A.10.5.5.3.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.3.2-1: RSSI supported test configurations

Table A.10.5.5.3.2-2: RSSI test parameters

Table A.10.5.5.3.2-3: RSSI RMTC parameters

## A.10.5.5.3.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.10.5.6Channel occupancy

## A.10.5.6.1 Channel occupancy measurement accuracy on PSCC with CCA

## A.10.5.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

## A.10.5.6.1.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, and Cell 2 is PSCell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 1. Supported test configurations are shown in table A.10.5.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.10.5.6.1.2-2 and A.10.5.6.1.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.1.2-1: CO supported test configurations

Table A.10.5.6.1.2-2: CO test parameters

Table A.10.5.6.1.2-3: CO RMTC parameters

## A.10.5.6.1.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.10.5.6.2 Channel occupancy measurement accuracy on SCC with CCA

## A.10.5.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

## A.10.5.6.2.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, Cell 3 is SCell on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.10.5.6.2.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.10.5.6.2.2-2 and A.10.5.6.2.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.2.2-1: CO supported test configurations

Table A.10.5.6.2.2-2: CO test parameters

Table A.10.5.6.2.2-3: CO RMTC parameters

## A.10.5.6.2.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

## A.10.5.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

## A.10.5.6.3.2Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, and Cell 3 is the neighbour with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.10.5.6.3.2-1. The accuracy of channel occupancy inter-frequency measurements is tested by using the parameters in A.10.5.6.3.2-2 and A.10.5.6.3.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.3.2-1: CO supported test configurations

Table A.10.5.5.3.2-2: CO test parameters

Table A.10.5.6.3.2-3: CO RMTC parameters

## A.10.5.6.3.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.
