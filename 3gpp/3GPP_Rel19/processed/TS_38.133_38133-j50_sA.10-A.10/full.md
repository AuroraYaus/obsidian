# A.10 EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1

Editor’s note: Test cases for EN-DC with NR PSCell under CCA and SCell under CCA are also included here.

## A.10.1 RRC_CONNECTED state mobility

### A.10.1.1 RRC connection mobility control

#### A.10.1.1.1 Random Access

##### A.10.1.1.1.1 4-step RA type contention-based random access for NR PSCell with CCA

###### A.10.1.1.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.1.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.1.1-2.

Table A.10.1.1.1.1.1-1: Supported test configurations for contention based random access test in FR1 for PSCell with CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.10.1.1.1.1.1-2: General test parameters for contention based random access test in FR1 for PSCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1,2 |  | SSB.1 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1,2 |  | SSB.2 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1,2 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1,2 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1,2 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1,2 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1,2 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image4.svg) [公式≈: ^{P}CMAX,f,c]) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  |  |  | FR1 PRACH configuration 1 under CCA | As defined in A.3.8A.2. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75/0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.10.1.1.1.1.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

###### A.10.1.1.1.1.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2A.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.10.1.1.1.1.2:

- The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

- In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.1.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.1.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2A.2.1.4, the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

###### A.10.1.1.1.1.2.5  Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2A.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.10.1.1.1.2 4-step RA type non-contention based random access for NR PSCell with CCA

###### A.10.1.1.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.2.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.2.1-2.

Table A.10.1.1.1.2.1-1: Supported test configurations for non-contention based random access test in FR1 for PSCell with CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.10.1.1.1.2.1-2: General test parameters for non-contention based random access test in FR1 for PSCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1,2 |  | SSB.1 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1,2 |  | SSB.2 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1,2 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1,2 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1,2 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1,2 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1,2 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image4.svg) [公式≈: ^{P}CMAX,f,c]) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  |  |  | FR1 PRACH configuration 2 under CCA | As defined in A.3.8A.2. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75/0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.10.1.1.1.2.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

###### A.10.1.1.1.2.2.1 SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.10.1.1.1.2.2:

- The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

- In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1[18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.2.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.2.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

##### A.10.1.1.1.3 2-step RA type contention-based random access for NR PSCell with CCA

###### A.10.1.1.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the behaviour of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7A.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.3.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.3.1-2.

Table A.10.1.1.1.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR1 for PSCell with CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.10.1.1.1.3.1-2: General test parameters for 2-step RA type contention based random access test in FR1 for PSCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1,2 |  | SSB.1 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1,2 |  | SSB.2 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1,2 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1,2 |  | TDD |  |
| TDD Configuration |  |  |  | Config 3,4 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1,2 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP Note 2 |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP Note 2 |  |  | dBm/ SCS | -115 |  |
| Io |  |  |  | Config 1,2 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image4.svg) [公式≈: ^{P}CMAX,f,c]) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| MsgA Configuration |  |  |  |  |  | FR1 MsgA configuration 1 under CCA | As defined in A.3.20A.2. |
| msgA-RSRP-ThresholdSSB |  |  |  |  | dBm | RSRP_51 | The actual value of the threshold is -105 dBm, as defined in TS 38.331 [2]. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75/0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.10.1.1.1.3.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

###### A.10.1.1.1.3.2.1 MsgA Transmission

To test the UE behaviour specified in clause 6.2.2A.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB, if the UL CCA is successful.

below are relevant for all cases of MsgA transmissions described within the clause A.10.1.1.1.3.2:

- The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

- The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure. In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.3.2.2 MsgB Reception

To test the UE behaviour specified in clause 6.2.2A.3.1.2 the System Simulator shall transmit a MsgB with fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble .

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.3.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.3 the System Simulator shall transmit a MsgB with fallbackRAR containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

##### A.10.1.1.1.4 2-step RA type non-contention based random access for NR PSCell with CCA

###### A.10.1.1.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test two cells are used, with the configuration of Cell 1 (E-UTRA PCell) specified in clause A.3.7.2.1 and Cell 2 configured as PSCell in FR1. Cell 1 is on a licensed band and cell 2 is subjected to CCA. Supported test parameters are shown in table A.10.1.1.1.4.1-1. UE capable of EN-DC with PSCell in FR1 needs to be tested by using the parameters in table A.10.1.1.1.4.1-2.

Table A.10.1.1.1.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR1 for PSCell with CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.10.1.1.1.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR1 for PSCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1,2 |  | SSB.1 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1,2 |  | SSB.2 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1,2 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1,2 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1,2 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1,2 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1,2 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1,2 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1,2 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (PCMAX,f,c) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| MsgA Configuration |  |  |  |  |  | FR1 MsgA configuration 2 under CCA | As defined in A.3.20A.2. |
| msgA-RSRP-ThresholdSSB |  |  |  |  | dBm | RSRP_51 | The actual value of the threshold is -105 dBm, as defined in TS 38.331 [2]. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75/0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.10.1.1.1.4.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

###### A.10.1.1.1.4.2.1 MsgA Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.10.1.1.1.4.2:

- The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

- The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all MsgA transmission shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1[18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.4.2.2 MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 5 MsgA transmissions have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power if Random Access Responses Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.10.1.1.1.4.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

#### A.10.1.2 Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA

##### A.10.1.2.1 Test Purpose and Environment

This test is to verify the requirement for E-UTRA handover with NR PSCell change, where NR PSCell is on carrier with CCA.  The requirements for EN-DC HO with PSCell change on CCA are specified in clause 5.9 in E-UTRA RRM specification [15] for the case when the target PSCell is on carrier with CCA. Supported test configurations are shown in table A.10.1.2.1-1.

Table A.10.1.2.1-1 gives general test configurations for Handover with PSCell from EN-DC to EN-DC, table A.10.1.2.1-2 provides general test parameters for Handover from E-UTRA to E-UTRA cell in EN-DC to EN-DC, table A.10.1.2.1-3 provides E-UTRAN cell specific test parameters for Handover with PSCell from EN-DC to EN-DC, table A.10.1.2.1-4 provides general test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA, table A.10.1.2.1-5 provides cell specific test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA.

In the test there are four cells: Cell 1 and Cell 2 are PCell and target PCell on E-UTRA carrier, Cell 3 and Cell 4 are PSCell and target PSCell on NR CCA carrier. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) and Cell 3 (NR PSCell) with EN-DC mode.

At the start of time duration T1, the UE do not have any information of cell 2 and cell 4. AT the end of T1, UE is configured with neighbour cell measurements on the Cell 3 and Cell 4 for Event A3 conditional measurement report.

During T2, UE acquires the timing information of Cell 3 and Cell 4 and performs L3-RSRP measurements on the configured neighbour cells. UE sends measurement report to the Cell 1 to indicate the event triggering condition A3 is satisfied for the configured for neighbour cells.  By end of T2, E-UTRA PCell (Cell 1) shall send a RRC message implying handover with PSCell change.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover with PSCell. UE shall complete PRACH transmission to PCell and PSCell by end of T3.

Table A.10.1.2.1-1: General test configurations for Handover with PSCell from EN-DC to EN-DC with CCA on NR Cell

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE:  The UE is only required to be tested in one of the supported test configurations depending on the UE capability |  |

Table A.10.1.2.1-2: General test parameters for Handover from E-UTRA to E-UTRA cell in EN-DC to EN-DC

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | One is E-UTRA RF channel and one is NR RF channel |
| Initial conditions | Active PCell |  | Cell 1 | On E-UTRA RF channel number 1. |
|  | E-UTRA Neighbouring cell |  | Cell 2 | On E-UTRA RF channel number 1. |
| Final conditions | Active PCell |  | Cell 2 |  |
| CP length |  |  | Normal | Applicable to Cell 1, Cell 2, Cell 3 and Cell 4. |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| DRX |  |  | OFF | Continuous monitoring of primary cell |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between same RAT cells |  | µs | 3 | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 | Tinterrupt is defined in clause 6.1B.1.2 |

Table A.10.1.2.1-3: E-UTRAN cell specific test parameters for Handover with PSCell from EN-DC to EN-DC

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Duplex mode |  | FDD or TDD |  |  | FDD or TDD |  |  |
| TDD special subframe configurationNote1 |  | 6 |  |  | 6 |  |  |
| TDD uplink-downlink configurationNote1 |  | 1 |  |  | 1 |  |  |
| BWchannel |  | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |  | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |  | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |  | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |  |
| OCNG Patterns defined in A.3.2.1 (FDD) and in A.3.2.2(TDD) Note2 |  | 5 MHz: OP.20 FDD10 MHz:  OP.1 FDD20 MHz: OP.17 FDD5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  | OP.18 FDDOP.2 FDDOP.14 FDDOP.10 TDDOP.2 TDDOP.8 TDD | 5 MHz: OP.18 FDD10 MHz: OP.2 FDD20 MHz: OP.14 FDD5 MHz: OP.10 TDD10 MHz: OP.2 TDD20 MHz: OP.8 TDD |  | OP.20 FDDOP.1 FDDOP.17 FDDOP.9 TDDOP.1 TDDOP.7 TDD |
| PRACH configuration |  | - |  |  | 4, As specified in table 5.7.1-2 in TS 36.211 |  |  |
| PBCH_RA | dB | 0 |  |  | 0 |  |  |
| PBCH_RB | dB |  |  |  |  |  |  |
| PSS_RA | dB |  |  |  |  |  |  |
| SSS_RA | dB |  |  |  |  |  |  |
| PCFICH_RB | dB |  |  |  |  |  |  |
| PHICH_RA | dB |  |  |  |  |  |  |
| PHICH_RB | dB |  |  |  |  |  |  |
| PDCCH_RA | dB |  |  |  |  |  |  |
| PDCCH_RB | dB |  |  |  |  |  |  |
| PDSCH_RA | dB |  |  |  |  |  |  |
| PDSCH_RB | dB |  |  |  |  |  |  |
| OCNG_RANote3 | dB |  |  |  |  |  |  |
| OCNG_RBNote3 | dB |  |  |  |  |  |  |
| NocNote4 | dBm/15 kHz | -98 |  |  |  |  |  |
| Ês/Noc | dB | 8 | 8 | 8 | -infinite | 11 | 11 |
| Ês/Iot | dB | 8 | -3.3 | -3.3 | -infinite | 2.36 | 2.36 |
| RSRP Note5 | dBm/15 kHz | -90 | -90 | -90 | -infinite | -87 | -87 |
| SCH_RP Note5 | dBm/15 kHz | -90 | -90 | -90 | -infinite | -87 | -87 |
| Io Note5 | dBm/Ch BW | -61.58 | -57.23+10log(NPRB,c /50) |  | N/A | -57.23+10log(NPRB,c /50) |  |
| Propagation Condition |  | AWGN |  |  |  |  |  |
| Antenna Configuration |  | 1x2 |  |  |  |  |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211.NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Es/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

Table A.10.1.2.1-4: General test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 3 | On the carrier under CCA |
|  | Neighbouring cell |  | Cell 4 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 4 | On the carrier under CCA |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.20.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.20.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | ≥ Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.10.1.2.1-5: Cell specific test parameters for PSCell change from FR1 carrier under CCA to FR1 carrier under CCA

| Parameter |  |  | Unit | Cell 3 |  |  | Cell 4 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| NR RF Channel Number |  |  |  | 1 |  |  | 1 |  |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  |  | PCCA_DL=0.9375 |  |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 0.75 |  |  | 0.75 |  |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 0.87 |  |  | 0.87 |  |  |
| TDD configuration |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |  |  |  |  |
| BWchannel |  | Config 1, 2 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW |  | Config 1, 2 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference |  | Config 1, 2 |  | SR.1.1 CCA |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 CCA |  |  |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1, 2 |  | CCR.1.1 CCA |  |  |  |  |  |
| TRS configuration |  | Config 1, 2 |  | TRS.1.1 TDD |  |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |  |  |
| DBT window configuration |  | Config 1, 2 |  | DBT.1 |  |  |  |  |  |
| SSB configuration for semi-static channel accessNote 4, 6 |  | Config 1, 2 |  | SSB.1 CCA |  |  |  |  |  |
| SSB configuration for dynamic channel accessNote 5, 6 |  | Config 1, 2 |  | SSB.2 CCA |  |  |  |  |  |
| ssb-PositionQCL |  | Config 1, 2 |  | [1] |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 30 kHz |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1, 2 | kHz | 30 kHz |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 |  | dBm/SCS | -95 |  |  |  |  |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -3.3 | -Infinity | 2.36 | 2.36 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | 8 | -Infinity | 11 | 11 |
| SSB_RP | Config 1, 2 |  | dBm/SCS | -87 | -87 | -87 | -Infinity | -84 | -84 |
| IoNote3 | Config 1, 2 |  | dBm/38.16 MHz | -55.31 | -50.96 | -50.96 | -55.31 | -50.96 | -50.96 |
| Propagation condition |  |  | - | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |  |

##### A.10.1.2.2 Test Requirements

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


## A.10.2 Timing

### A.10.2.1 UE transmit timing

#### A.10.2.1.1 UE Transmit Timing Test with PSCell under DL CCA

##### A.10.2.1.1.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb when PSCell is subject to DL CCA and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2. Supported test configurations are shown in table 10.2.1.1.1-1.

Table A.10.2.1.1.1-1: Supported test configurations for UE transmit timing test

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

The test consists of E-UTRA PCell and NR PSCell, which is subject to DL CCA. The configuration for E-UTRA is given in A.3.7.2.1. Table A.10.2.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.10.2.1.1.1-3.

Table A.10.2.1.1.1-2: Cell Specific Test Parameters for UE Transmit Timing test

| Parameter |  | Unit | Config | Test1 | Test2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  |  | 1,2 | Freq1 | Freq1 |
| TDD configuration |  |  | 1,2 | TDDConf.1.1 CCA |  |
| BWchannel |  | MHz | 1,2 | 40: NPRB,c = 106 |  |
| Initial BWP Configuration |  |  | 1,2 | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP Configuration |  |  | 1,2 | DLBWP.1.1ULBWP.1.1 |  |
| DRX Cycle |  | ms | 1,2 | N/A | DRX.8Note5 |
| DL CCA model |  |  | 1,2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1,2 | As specified in clause A.3.26.2.2 |  |
| PDSCH Reference |  |  | 1,2 | SR.1.1 CCA |  |
| CORESET Reference |  |  | 1,2 | CR.1.1 CCA |  |
| OCNG Patterns |  |  | 1,2 | OCNG pattern 1 |  |
| SSB configuration | Semi- static channel acces |  | 1,2 | SSB.1 CCA |  |
|  | Dymamic channel acces |  | 1,2 | SSB.2 CCA |  |
| SMTC configuration |  |  | 1,2 | SMTC.1 FR1 |  |
| TRS configuration |  |  | 1,2 | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  |  | 1,2 | 0.9375 | 0.9375 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  |  | 1,2 | 0.75 | 0.75 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  |  | 1,2 | 0.75 | 0.75 |
| UL CCA probability (PCCA_UL) |  |  | 1,2 | 1 | 1 |
| EPRE ratio of PSS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 1,2 | 0 | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/30 kHz | 1,2 | -95 | -95 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | 1,2 | 3 | 3 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | 1,2 | 3 | 3 |
| SS-RSRPNote3 |  | dBm/30 kHz | 1,2 | -92 | -92 |
| IoNote3 |  | dBm/38.1 MHz | 1,2 | -59.2 | -59.2 |
| Propagation condition |  |  | 1,2 | AWGN |  |
| SRS Config |  |  | 1,2 | SRSConf.1Note6 | SRSConf.2Note6 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.10.2.1.1.1-3.NOTE 7: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 8: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.10.2.1.1.1-3: SRS Configuration for UE transmit timing

|  | Field | SRSConf.1 | SRSConf.2 | Comments |
| --- | --- | --- | --- | --- |
| SRS-ResourceSet | srs-ResourceSetId | 0 | 0 |  |
|  | srs-ResourceIdList | 0 | 0 |  |
|  | resourceType | Periodic | Periodic |  |
|  | Usage | Codebook | Codebook |  |
| SRS-Resource | SRS-ResourceId | 0 | 0 |  |
|  | nrofSRS-Ports | Port1 | Port1 |  |
|  | transmissionComb | n2 | n2 |  |
|  | combOffset-n2 | 0 | 0 |  |
|  | cyclicShift-n2 | 0 | 0 |  |
|  | resourceMapping startPosition | 0 | 0 |  |
|  | resourceMapping nrofSymbols | n1 | n1 |  |
|  | resourceMappingrepetitionFactor | n1 | n1 |  |
|  | freqDomainPosition | 0 | 0 |  |
|  | freqDomainShift | 0 | 0 |  |
|  | freqHopping c-SRS | 14 for test configuration 1,225 for test configuration 3 | 25 | Matches NPRB,c |
|  | freqHopping b-SRS | 0 | 0 |  |
|  | freqHopping b-hop | 0 | 0 |  |
|  | groupOrSequenceHopping | Neither | Neither |  |
|  | resourceType | Periodic | Periodic |  |
|  | periodicityAndOffset-p | sl1, 0 | sl640, 0 | Offset to align with DRx periodicity |
|  | sequenceId | 0 | 0 | Any 10 bit number |

##### A.10.2.1.1.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Set up E-UTRA PCell according to parameters given in table A.3.7.2.1-1 and setup NR PSCell according to parameters given in table A.10.2.1.1.1-1.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset)×Tc ± Te of the first detected path of DL SSB.

a. The NTA offset value (in Tc units) is 25600

b. The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3) The test system shall adjust the timing of the DL path by values given in table A.10.2.1.1.2-1

Table A.10.2.1.1.2-1: Adjustment Value for DL Timing

| SCS of SSB signals (kHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 30 | +32*64Tc | +16*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.

5) The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

### A.10.2.2 UE timing advance

#### A.10.2.2.1 UE Timing Advance Adjustment Accuracy with PSCell under DL CCA

##### A.10.2.2.1.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

##### A.10.2.2.1.2 Test Parameters

Supported test configurations are shown in table A.10.2.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.10.2.2.1.2-2, A.10.2.2.1.2-3 and A.10.2.2.1.2-4. The configuration of Cell 1 (LTE PCell) is specified in clause A.3.7.2.1.

In all test cases, two cells are used. Cell 1 is the PCell in the primary Timing Advance Group (pTAG) and cell 2 is the PSCell which is subject to DL CCA is in the secondary Timing Advance Group (sTAG). Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for sTAG are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.10.2.2.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for PSCell in sTAG.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element for sTAG, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for sTAG used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value specified in table A.10.2.2.1.2-2. This value shall result in changes of the timing advance for sTAG used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321, shall be configured so that it does not expire in the duration of the test.

Table A.10.2.2.1.2-1: Supported test configurations for timing advance test

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: The UE supporting EN-DC only on NR band(s) with shared spectrum access is required to be tested |  |

Table A.10.2.2.1.2-2: General test parameters for timing advance test

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF channel number |  | Cell 1: 1Cell 2: 2 | 1 for E-UTRAN PCell2 for NR PSCell |
| Initial DL BWP |  | DLBWP.0.1 | As specified in table A.3.9.2.1-1 |
| Dedicated DL BWP |  | DLBWP.1.1 | As specified in table A.3.9.2.2-1 |
| Initial UL BWP |  | ULBWP.0.1 | As specified in table A.3.9.3.1-1 |
| Dedicated UL BWP |  | ULBWP.1.1 | As specified in table A.3.9.3.2-1 |
| Timing Advance Command (TA) value during T1 |  | 31 | NTA_new = NTA_old  for the purpose of establishing a reference value from which the timing advance adjustment accuracy can be measured during T2 |
| Timing Advance Command (TA) value during T2 |  | 39 | For 30 kHz SCS NTA_new = NTA_old  + 4096*Tc (based on equation in clause 4.2 of TS 38.213 [3]) |
| T1 | s | 5 |  |
| T2 | s | 5 |  |

Table A.10.2.2.1.2-3: Cell specific test parameters for timing advance test

| Parameter |  |  |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 |
| TDD configuration |  |  | Config 1,2 |  | TDDConf.1.1 CCA |  |
| BWchannel |  |  | Config 1,2 | MHz | 40: NPRB,c = 106 |  |
| BWP BW |  |  | Config 1,2 | MHz | 40: NPRB,c = 106 |  |
| DRX Cycle |  |  | Config 1,2 | ms | Not Applicable |  |
| DL CCA model |  |  | Config 1,2 |  | As specified in clauseA.3.26.2.1 |  |
| UL CCA model |  |  | Config 1,2 |  | As specified in clause A.3.26.2.2 |  |
| PDSCH Reference |  |  | Config 1,2 |  | SR.1.1 CCA |  |
| CORESET Reference |  |  | Config 1,2 |  | CR.1.1 CCA |  |
| TRS configuration |  |  | Config 1,2 |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  | Config 1,2 |  | OCNG pattern 1 |  |
| SSB Configuration |  | Semi- static channel acces | Config 1,2 |  | SSB.1 CCA |  |
|  |  | Dymamic channel acces | Config 1,2 |  | SSB.2 CCA |  |
| SMTC configuration |  |  | Config 1,2 |  | SMTC.1 FR1 |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  |  | Config 1,2 |  | 1 |  |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  |  | Config 1,2 |  | 1 |  |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  |  | Config 1,2 |  | 1 |  |
| UL CCA probability PCCA |  |  | Config 1,2 |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  | dB | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 |  |  | dBm/30 kHz | -95 |  |
|  | Config 3,6 |  |  |  | -95 |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | 3 |  |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | 3 |  |
| IoNote3 | Config 1,2 |  |  | dBm/38.16 MHz | -62.58 |  |
| Propagation condition |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 5: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |

Table A.10.2.2.1.2-4: Sounding Reference Symbol Configuration for timing advance test

| Field |  | Value | Comment |
| --- | --- | --- | --- |
| c-SRS | Config 1,2 | 24 | Frequency hopping is disabled |
| b-SRS |  | 0 |  |
| b-hop |  | 0 |  |
| freqDomainPosition |  | 0 | Frequency domain position of SRS |
| freqDomainShift |  | 0 |  |
| groupOrSequenceHopping |  | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset |  | sl5=4 for SCS 30 kHz | Once every 5 slots |
| pathlossReferenceRS |  | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage |  | Codebook | Codebook based UL transmission |
| startPosition |  | 0 | resourceMapping setting: SRS on last symbol of slot, and 1symbols for SRS without repetition. |
| nrofSymbols |  | n1 |  |
| repetitionFactor |  | n1 |  |
| combOffset-n2 |  | 0 | transmissionComb setting |
| cyclicShift-n2 |  | 0 |  |
| nrofSRS-Ports |  | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |  |

##### A.10.2.2.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value for PSCell in sTAG to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy for PSCell in sTAG shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.10.3 Signalling characteristics

### A.10.3.1 Radio link monitoring

#### A.10.3.1.1 Introduction

In the test cases specified in clause A.10.3.1, any uplink signal transmitted by the UE is used for detecting the in-/out-of-sync state of the UE. In terms of measurement, the uplink signal is verified based on the UE output power:

- UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means uplink signal

- UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-3 [20]) means no uplink signal.

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

#### A.10.3.1.2 Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode

##### A.10.3.1.2.1 Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.10.3.1.2.1-1. The test parameters are given in tables A.10.3.1.2.1-2, A.10.3.1.2.1-3, and A.10.3.1.2.1-4 below. There are two cells in the test: Cell 1 is the E-UTRAN PCell, and Cell 2 is the FR1 PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

The test consists of three successive time periods, with time duration of T1, T2 and T3, respectively. Figure A.10.3.1.2.1-1 shows the variation of the downlink SNR in the active Cell 2 to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in the test.

Table A.10.3.1.2.1-1: Supported test configurations.

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.3.1.2.1-2: General test parameters for PSCell out-of-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active E-UTRA PCell |  |  |  | Cell 1 |
| E-UTRA RF Channel Number |  |  |  | 1 |
| Active PSCell |  |  |  | Cell 2 |
| RF Channel Number |  |  |  | 2 |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |
| Duplex mode |  | Config 1,2 |  | TDD |
| BWchannel |  | Config 1,2 | MHz | 40: NPRB,c = 106 |
| DL initial BWP configuration |  | Config 1,2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1,2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1,2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1,2 |  | ULBWP.1.1 |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |
| CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 CCA |
| SSB configuration for semi-static channel accessNote 4, 6 |  | Config 1,2 |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote 5, 6 |  | Config 1,2 |  | SSB.2 CCA |
| DBT window configuration |  | Config 1,2 |  | DBT.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 |  | 30 kHz |
| PRACH Configuration |  | Config 1,2 |  | FR1 PRACH configuration 1 under CCA |
| SSB index assigned as RLM RS |  |  |  | 0 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX |  |  |  | OFF |
| Gap pattern ID |  |  |  | gp0 |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 0 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS configuration for CSI reporting |  | Config 1,2 |  | CSI-RS.2.1 TDD |
| CSI-RS for tracking |  | Config 1,2 |  | TRS.1.2 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 1.04 |
| T3 |  |  | s | 1.04 |
| D1 |  |  | s | 1 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 3: E-UTRAN is in non-DRX mode under test.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.10.3.1.2.1-3: Cell-specific test parameters for PSCell out-of-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| DL CCA probability PCCA_DL |  | Note 6,8 |  | PCCA_DL=0.9375 |  |  |
|  |  | Note 7,8 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| UL CCA probability PCCA_UL |  |  |  | 1 |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |
| SNRNote 3,4 on RLM-RS | Config 1,2 |  | dB | 1 | [-7] | -15 |
| SNR on other channels and signals | Config 1,2 |  | dB | 1 |  |  |
| ![](media_svg/image7.svg) [公式≈: ^{N}oc] | Config 1,2 |  | dBm/SCS | -95 |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during muted slots or during DBT windows.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT windows.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3, respectively, in figure A.10.3.1.2.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2 RX on at least one band. For testing of a UE which supports 4 RX on all bands, the SNR during T3 is A.3.6.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

Table A.10.3.1.2.1-4: Measurement gap configuration for PSCell out-of-sync testing in non-DRX mode.

| Field | Test 1 |  |
| --- | --- | --- |
|  | Value |  |
| gapOffset | 0 |  |
| NOTE 1: E-UTRAN PCell and PSCell are SFN-synchronous and frame boundary aligned.NOTE 2: Ensure that RLM RS is partially overlapped with measurement gap. |  |  |

Figure A.10.3.1.2.1-1: SNR variation for out-of-sync testing.

##### A.10.3.1.2.2 Test requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

- During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

- The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode

##### A.10.3.1.3.1 Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PSCell. This test will partly verify the FR1 PSCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.10.3.1.3.1-1. The test parameters are given in tables A.10.3.1.3.1-2, and A.10.3.1.3.1-3 below. There are two cells in the test: Cell 1 is the E-UTRAN PCell, and Cell 2 is the FR1 PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model.

Table A.10.3.1.3.1-1: Supported test configurations.

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.3.1.3.1-2: General test parameters for PSCell in-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active E-UTRA PCell |  |  |  | Cell 1 |
| E-UTRA RF Channel Number |  |  |  | 1 |
| Active PSCell |  |  |  | Cell 2 |
| RF Channel Number |  |  |  | 2 |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |
| Duplex mode |  | Config 1,2 |  | TDD |
| BWchannel |  | Config 1,2 | MHz | 40: NPRB,c = 106 |
| DL initial BWP configuration |  | Config 1,2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1,2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1,2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1,2 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |
| CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 CCA |
| SSB configuration for semi-static channel accessNote 3, 5 |  | Config 1,2 |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote 4,5 |  | Config 1,2 |  | SSB.2 CCA |
| DBT window configuration |  | Config 1,2 |  | DBT.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 |  | 30 kHz |
| PRACH Configuration |  | Config 1,2 |  | FR1 PRACH configuration 1 under CCA |
| SSB index assigned as RLM RS |  |  |  | 0 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |
| In sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX |  |  |  | OFF |
| Gap pattern ID |  |  |  | N/A |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 2000 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1,2 |  |  | CSI-RS.2.1 TDD |
| CSI-RS for tracking | Config 1,2 |  |  | TRS.1.2 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.2 |
| T3 |  |  | s | 0.52 |
| T4 |  |  | s | 0.2 |
| T5 |  |  | s | 2.04 |
| D1 |  |  | s | 2 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 3:     For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 4:     For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 5:     For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.10.3.1.3.1-3: Cell-specific test parameters for PSCell in-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA_DL |  | Note 6,8 |  | PCCA_DL=0.9375 |  |  |  |  |
|  |  | Note 7,8 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |
| UL CCA probability PCCA_UL |  |  |  | 1 |  |  |  |  |
| LCCA_DL |  |  |  | 7 |  |  |  |  |
| WCCA_DL |  |  | ms | TEvaluate_in_SSB,CCANOTE 9 |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 4 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR on RLM-RS | Config 1,2 |  | dB | 1 | -7 | -15 | -4.5 | 1 |
| SNR on other channels and signals | Config 1,2 |  | dB | 1 |  |  |  |  |
| ![](media_svg/image7.svg) [公式≈: ^{N}oc] | Config 1,2 |  | dBm/SCS | -95 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during muted slots or during DBT windows.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT windows.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.10.3.1.2.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4 RX on all bands, the SNR during T3 and T4 is modified as specified in clause A.3.6.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only.NOTE 9:  As defined in table 8.1A.2.2-1. |  |  |  |  |  |  |  |  |

Figure A.10.3.1.2.1-1: SNR variation for in-sync testing.

##### A.10.3.1.3.2 Test requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.10.3.1.4 Void

##### A.10.3.1.4.1 Void

##### A.10.3.1.4.2 Void

#### A.10.3.1.5 Void

##### A.10.3.1.5.1 Void

##### A.10.3.1.5.2 Void

### A.10.3.2 Void

### A.10.3.3 SCell activation and deactivation delay

#### A.10.3.3.1 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle

##### A.10.3.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.10.3.3.1.1-1.

The test parameters are given in table A.10.3.3.1.1-2 and cell-specific parameters for NR cells are provided in table A.10.3.3.1.1-3 below. Cell-specific parameters for EUTRA PCell are provided in clause A.3.7.2.1.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in E-UTRA, Cell 2 (PSCell) on radio channel 2 (PSCC) in NR, and Cell 3 (SCell) on radio channel 3 (SCC) in NR. Before the test starts the UE is connected to Cell 1 and Cell 2, but is not aware of Cell 3, as the UE is only monitoring PCC and PSCC. The UE shall be continuously scheduled in the PCell and PSCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 3) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PSCell for the activated SCell at latest in slot m +  (THARQ+ Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, as defined in clause 8.3A.2. The UE shall start reporting CSI in PSCell in first available uplink resource for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting following slot m+ $\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption shall fall within the time window specified in clause 8.3A.2.

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$. Any PSCell interruption shall fall within the time window specified in clause 8.3A.3.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.10.3.3.1.1-1: Supported test configurations for SCell Activation and Deactivation of known NR SCell with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

| Configuration | Description |
| --- | --- |
| 1 | PCC: LTE FDD duplex mode;With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode;With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | PCC: LTE TDD duplex mode;With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode;With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.3.3.1.1-2: General test parameters for known SCell activation case with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2,3 | Three radio channels (1, 2, 3) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on E-UTRAN RF channel number 1. |
| Active PSCell |  | Cell 2 | Primary secondary cell on NR RF channel number 2. |
| Configured deactivated SCell |  | Cell 3 | Configured deactivated secondary cell on NR RF channel number 3 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| CQI/PMI periodicity and offset configuration index |  | 0 | CQI reporting for SCell every second subframe |
| SCell measurement cycle (measCycleSCell) | ms | 160 |  |
| Cell 3 timing offset to Cell 2 | s | 0 |  |
| Time alignment error between Cell 3 and Cell 2 | s | TAE as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 7 | During this time PCell and PSCell shall be known and the SCell configured and detected. |
| T2 | s | 1 | During this time the UE shall activate the SCell. |
| T3 | s | 1 | During this time the UE shall deactivate the SCell. |
| THARQ | ms | k1 $\times  $ NR slot length | k1 is a number of slots and is indicated by the PDSCH-to-HARQ-timing-indicator field in the DCI format, if present, or provided by dl-DataToUL-ACK, the value of k should be the minimum value defined in TS 38.213 [3] depends on UE’s capability |
| TCSI_Reporting | ms | $ 10+5\cdot  2^{µ_{DL}}$ | The delay (in ms) including uncertainty in acquiring the first available downlink CSI reference resource, UE processing time for CSI reporting (clause 5.2.2.5 in TS 38.214) and uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2]$µ_{DL}$ is the subcarrier spacing configuration for DL |

Table A.10.3.3.1.1-3: Cell specific test parameters for known SCell activation case with NR PSCell and SCell under CCA, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 2 |  |  | Cell 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Duplex mode | Config 1,2 |  | TDD |  |  | TDD |  |  |
| TDD configuration | Config 1,2 |  | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| BWchannel | Config 1,2 | MHz | 40: NPRB,c = 106 |  |  | 40: NPRB,c = 106 |  |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  | As specified in clause A.3.26.2.2 |  |  |
| DL CCA probability for semi-static channel accessNote5,7 | PCCA_DL |  | 0.9375 |  |  | 0.9375 |  |  |
| DL CCA probability for dynamic channel accessNote6,7 | PCCA_DL_1 |  | 0.75 |  |  | 0.75 |  |  |
|  | PCCA_DL_2 |  | 0.75 |  |  | 0.75 |  |  |
| UL CCA probability for semi-static channel access | PCCA_UL |  | 0.87 |  |  | 0.87 |  |  |
| UL CCA probability for dynamic channel access | PCCA_UL |  | 0.75 |  |  | 0.75 |  |  |
| LCCA_DL Note 8 |  |  | 2 |  |  | 2 |  |  |
| WCCA_DL Note 8 |  |  | Tactivation_time_withCCA |  |  | Tactivation_time_withCCA |  |  |
| Initial downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Initial uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Dedicated downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Dedicated uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| TCI state |  |  | TCI.State.0 |  |  | TCI.State.0 |  |  |
| TRS Configuration | Config 1,2 |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel | Config 1,2 |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| Dedicated CORESET parameters | Config 1,2 |  | CCR.1.3 CCA |  |  | CCR.1.3 CCA |  |  |
| RMSI CORESET parameters | Config 1,2 |  | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| OCNG Patterns Note1 |  |  | OP.1 |  |  | OP.1 |  |  |
| SSB Configuration for semi-static channel accessNote5,7 | Config 1,2 |  | SSB.1 CCA |  |  | SSB.1 CCA |  |  |
| SSB Configuration for dynamic channel accessNote6,7 | Config 1,2 |  | SSB.2 CCA |  |  | SSB.2 CCA |  |  |
| SMTC configuration |  |  | SMTC.1 |  |  | SMTC.1 |  |  |
| DBT window configuration |  |  | DBT.1 |  |  | DBT.1 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote1 |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote1 |  |  |  |  |  |  |  |  |
| Noc Note2 | Config 1,2 | dBm/15 kHz | -104 |  |  | -104 |  |  |
| Noc Note2 | Config 1,2 | dBm/SCS | -101 |  |  | -101 |  |  |
| Ês/Iot |  | dB | 17 |  |  | 17 |  |  |
| Ês/Noc |  | dB | 17 |  |  | 17 |  |  |
| SS-RSRP Note3 | Config 1,2 | dBm/SCS | -84 |  |  | -84 |  |  |
| IoNote3 | Config 1,2 | dBm/38.16 MHz | -52.87 |  |  | -52.87 |  |  |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that resources in the cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols in slots with downlink transmission bursts. OCNG is not transmitted during muted slots or during DBT windows.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.NOTE 8: As specified in clause 8.3A for L1,max, L2,1,max, L2,2,max, L3,1,max, and L3,2,max |  |  |  |  |  |  |  |  |

##### A.10.3.3.1.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PSCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB.

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle

##### A.10.3.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.10.3.3.1.1-1 above.

The test parameters are same as in table A.10.3.3.1.1-2 above, except for parameters listed below in table A.10.3.3.2.1-1. The cell-specific parameters are same as in table A.10.3.3.1.1-3 above.

The test execution is the same as described in clause A.10.3.3.1 above.

Table A.10.3.3.2.1-1: General test parameters for known NR SCell activation with NR PSCell and SCell under CCA, 640 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| SCell measurement cycle (measCycleSCell) | ms | 640 |  |

##### A.10.3.3.2.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PSCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB_MAX + L2,1* TSMTC_MAX.

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.10.3.3.3 SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA

##### A.10.3.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for NR SCell, with NR PSCell and NR SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.10.3.3.1.1-1 above.

The test parameters are same as in table A.10.3.3.1.1-2 above, except for parameters listed below in table A.10.3.3.3.1-1. The cell-specific parameters are same as in table A.10.3.3.1.1-3 above.

The test execution is the same as described in clause A.10.3.3.1 above.

Table A.10.3.3.3.1-1: General test parameters for unknown NR SCell activation with NR PSCell and SCell under CCA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| T1 | s | 0.1 | During this time period PCell and PSCell shall be known and the SCell configured, but not detected. |

##### A.10.3.3.3.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+ Tactivation_time_withCCA + TCSI_reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PSCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB_MAX + L3,1* TSMTC_MAX.

During T3, interruption on PSCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PSCell shall not be more than specified for EN-DC in clause 8.2.1.2.4.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

### A.10.3.4 Beam failure detection and link recovery procedures

#### A.10.3.4.1 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode

##### A.10.3.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.10.3.4.1.1-1, A.10.3.4.1.1-2, and A.10.3.4.1.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.4.1.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.10.3.4.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA model. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.10.3.4.1.1-1: Supported test configurations for FR1 PSCell with CCA

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE:  The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.3.4.1.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |  |
| Active E-UTRA PCell |  |  |  |  | Cell 1 |  |
| E-UTRA RF Channel Number |  |  |  |  | 1 |  |
| Active PSCell |  |  |  |  | Cell 2 |  |
| RF Channel Number |  |  |  |  | 2 |  |
| DL CCA model |  |  |  |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  |  | As specified in A.3.26.2.2 |  |
| Duplex mode |  |  | Config 1, 2 |  | TDD |  |
| BWchannel |  |  | Config 1, 2 | MHz | 40: NRB,c = 106 |  |
| DL initial BWP configuration |  |  | Config 1, 2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  |  | Config 1, 2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  |  | Config 1, 2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  |  | Config 1, 2 |  | ULBWP.1.1 |  |
| TDD configuration |  |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |
| CORESET Reference Channel |  |  | Config 1, 2 |  | CR.1.1 CCA |  |
| SSB Configuration |  |  | Config 1, 2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |  |
| DBT Window Configuration |  |  | Config 1, 2 |  | DBT.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1, 2 |  | 30 KHz |  |
| PRACH Configuration |  |  | Config 1, 2 |  | Table A.3.8.2.2-1 |  |
| SSB Index assigned as BFD RS (q0) |  |  |  |  | 0 |  |
| SSB Index assigned as CBD RS (q1) |  |  |  |  | 1 |  |
| OCNG parameters |  |  |  |  | OP.1 |  |
| CP length |  |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x2 Low |  |
| Beam failure |  | DCI format |  |  | 1-0 |  |
| detection transmission parameters |  | Number of Control OFDM symbols |  |  | 2 |  |
|  |  | Aggregation level |  | CCE | 8 |  |
|  |  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |
|  |  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |
|  |  | DMRS precoder granularity |  |  | REG bundle size |  |
|  |  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  |  | OFF |  |
| Gap pattern ID |  |  |  |  | gp0 |  |
| gapOffset |  |  |  |  | 0 |  |
| rlmInSyncOutOfSyncThreshold |  |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1, 2 |  |  | dBm/SCS kHz | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  |  |  |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | Config 1, 2 |  |  | CSI-RS.2.1 TDD |  |
| CSI-RS for tracking |  | Config 1, 2 |  |  | TRS.1.2 TDD |  |
| SSB Index assigned as RLM RS |  |  |  |  | 0,1 |  |
| T310 timer |  |  |  | ms | 1000 |  |
| N310 |  |  |  |  | 2 |  |
| T1 |  |  |  | s | 0.2 | During this time the the UE shall be fully synchronized to cell 1 |
| T2 |  |  |  | s | 0.93 |  |
| T3 |  |  |  | s | 0.52 |  |
| T4 |  |  |  | s | 0 |  |
| T5 |  |  |  | s | 0.45 |  |
| D1 |  |  |  | s | 0.41 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 3: E-UTRAN is in non-DRX mode under test. |  |  |  |  |  |  |

Table A.10.3.4.1.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA,DL | Note 10, 12 |  |  | 1.0 | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
|  | Note 11, 12 |  |  | 1.0/1.0 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA,UL |  |  |  | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| LCCA_DL |  |  |  | N/A | 7 |  |  |  |
| WCCA_DL |  |  | ms | N/A | TEvaluate_CBD_SSB_CCA Note 13 |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 |  | Config 1, 2 | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 |  | Config 1, 2 | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 |  | Config 1, 2 | dBm/SCS kHz | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image7.svg) [公式≈: ^{N}oc] |  | Config 1, 2 | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT window.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6A.NOTE 10: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 11: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 12: For UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only.NOTE 13:  As defined in table 8.5A.5.2-1. |  |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.10.3.4.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.10.3.4.1.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 410 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.10.3.4.2 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode

##### A.10.3.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving PSCell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the PSCell, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.10.3.4.2.1-1, A.10.3.4.2.1-2, and A.4.5.5.2.1-3 below. There are two cells, cell 1 is the E-UTRAN PCell, and cell 2 is the PSCell which operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.10.3.4.2.1-1 shows the variation of the downlink SNR of the PCell and the SNR of the SSB in set q0 in the active PSCell to emulate SSB based beam failure. Figure A.10.3.4.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA model. In the test, DRX configuration is enabled in PSCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.10.3.4.2.1-1: Supported test configurations for FR1 PSCell with CCA

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.3.4.2.1-2: General test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |  |
| Active E-UTRA PCell |  |  |  |  | Cell 1 |  |
| E-UTRA RF Channel Number |  |  |  |  | 1 |  |
| Active PSCell |  |  |  |  | Cell 2 |  |
| RF Channel Number |  |  |  |  | 2 |  |
| DL CCA model |  |  |  |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  |  | As specified in A.3.26.2.2 |  |
| Duplex mode |  |  | Config 1, 2 |  | TDD |  |
| BWchannel |  |  | Config 1, 2 | MHz | 40: NRB,c = 106 |  |
| DL initial BWP configuration |  |  | Config 1, 2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  |  | Config 1, 2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  |  | Config 1, 2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  |  | Config 1, 2 |  | ULBWP.1.1 |  |
| TDD configuration |  |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |
| CORESET Reference Channel |  |  | Config 1, 2 |  | CR.1.1 CCA |  |
| SSB Configuration |  |  | Config 1, 2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |  |
| DBT Window Configuration |  |  | Config 1, 2 |  | DBT.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1, 2 |  | 30 KHz |  |
| PRACH Configuration |  |  | Config 1, 2 |  | Table A.3.8.2.2-1 |  |
| SSB Index assigned as BFD RS (q0) |  |  |  |  | 0 |  |
| SSB Index assigned as CBD RS (q1) |  |  |  |  | 1 |  |
| OCNG parameters |  |  |  |  | OP.1 |  |
| CP length |  |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x2 Low |  |
| Beam failure |  | DCI format |  |  | 1-0 |  |
| detection transmission parameters |  | Number of Control OFDM symbols |  |  | 2 |  |
|  |  | Aggregation level |  | CCE | 8 |  |
|  |  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |
|  |  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |
|  |  | DMRS precoder granularity |  |  | REG bundle size |  |
|  |  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  |  | DRX.7 | A.3.3.7 |
| Gap pattern ID |  |  |  |  | N.A. |  |
| rlmInSyncOutOfSyncThreshold |  |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1, 2 |  |  | dBm/SCS kHz | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  |  |  |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | Config 1, 2 |  |  | CSI-RS.2.1 TDD |  |
| CSI-RS for tracking |  | Config 1, 2 |  |  | TRS.1.2 TDD |  |
| SSB Index assigned as RLM RS |  |  |  |  | 0,1 |  |
| T310 timer |  |  |  | ms | 1000 |  |
| N310 |  |  |  |  | 2 |  |
| T1 |  |  |  | s | 1 | During this time the the UE shall be fully synchronized to cell 1 |
| T2 |  |  |  | s | 9.01 |  |
| T3 |  |  |  | s | 5.16 |  |
| T4 |  |  |  | s | 0 |  |
| T5 |  |  |  | s | 3.89 |  |
| D1 |  |  |  | s | 3.85 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 3: E-UTRAN is in non-DRX mode under test. |  |  |  |  |  |  |

Table A.10.3.4.2.1-3: Cell specific test parameters for FR1 PSCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA,DL | Note 10, 12 |  |  | 1.0 | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
|  | Note 11, 12 |  |  | 1.0/1.0 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA,UL |  |  |  | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 |  | Config 1, 2 | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 |  | Config 1, 2 | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 |  | Config 1, 2 | dBm/SCS kHz | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image7.svg) [公式≈: ^{N}oc] |  | Config 1, 2 | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT window.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6A.NOTE 10: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 11: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 12: For UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.10.3.4.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in DRX mode

##### A.10.3.4.2.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 3850 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

### A.10.3.5 Active BWP switching

#### A.10.3.5.1 UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC

A.10.3.5.1.1 Test Purpose and Environment

The purpose of this test is to verify the UL BWP switch delay requirement defined in clause 8.6.4.

The supported test configurations are shown in table A.10.3.5.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in A.10.3.5.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.10.3.5.1.1-2. SRS configuration used in the test is specified in table A.10.3.5.1.1-4.

The UE shall be configured with PRACH configuration on UL BWP on which the UE shall switch after the consistent UL LBT failure detection.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2.

- UE is configured with 2 different UE-specific downlink and uplink bandwidth parts on Cell 2: DL BWP-1, DL BWP-2, UL BWP-1 and UL BWP-2 before starting the test. DL BWP-1 and DL BWP-2 always include bandwidth of the initial DL BWP and SSB. UL BWP-1 and UL BWP-2 always include bandwidth of the SRS.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is DL BWP-1.

- UE is indicated in firstActiveUplinkBWP-Id that the active UL BWP is UL BWP-1.

- UE is configured with LBT-FailureRecoveryConfig parameters for Cell 2.

The cell has constant signal levels throughout the test. The test consists of 2 successive time periods, with durations of T1 and T2, respectively.

During T1,

- Time period T1 starts when the UE has received the SRS configuration for periodic SRS transmission on active UL BWP-1.

- The UE shall perform UL CCA before SRS transmission.

- The parameter UL CCA probability PCCA is set to 0 during T1. This requires the test system to set energy level above the detection level during portion of the UL slot where the UE performs UL CCA. This in turn forces the UE to fail the UL CCA. The UE consistently fails UL CCA during T1 and is therefore unable to transmit SRS.

During T2,

- T2 starts when the UE detects consistent UL LBT failures i.e. when total number of UL LBT failures in Cell 2 on active UL BWP-1 exceeds lbt-FailureInstanceMaxCount during lbt-FailureDetectionTimer.

- The UE upon detected consistent UL LBT failure starts the LBT recovery mechanism, which requires the UE to switch to active UL BWP-2 in Cell 2 and to send PRACH in the active UL BWP-2.

- Staring from T2, the UE shall be able to send PRACH in the active UL BWP-2 within the delay specified in clause 8.6.4.

Table A.10.3.5.1.1-1: Supported test configurations for UL BWP switch test in EN-DC

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.10.3.5.1.1-2: General test parameters for UL BWP switch in EN-DC

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | 1 | One E-UTRA radio channel is used for this test |
| NR RF Channel Number |  | 2 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| Active PSCell |  | Cell 2 | PSCell on RF channel number 2. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| lbt-FailureDetectionTimer [2] | ms | 80 | Parameter configured by IE: LBT-FailureRecoveryConfig [1] |
| lbt-FailureInstanceMaxCount [2] |  | 4 | Parameter configured by IE: LBT-FailureRecoveryConfig [1] |
| T1 | s | 0.1 | During T1 consistent LBT failure is detected on active UL BWP-1 |
| T2 | s | 0.1 | During T2 UE sends PRACH on active UL BWP-2 |

Table A.10.3.5.1.1-3: NR Cell specific test parameters for UL BWP switch test in EN-DC

| Parameter |  |  | Unit | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| TDD configuration |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1, 2 |  | 40 MHz: NPRB,c = 106 |  |
| DL CCA model |  | Config 1, 2 |  | As specified in clause A.3.20.2.1 |  |
| UL CCA model |  | Config 1, 2 |  | As specified in clause A.3.20.2.2 |  |
| Active BWP ID |  | Config 1, 2 |  | 1, 2 |  |
| Initial DL BWP Configuration |  | Config 1, 2 |  | DLBWP.0.2 Note 4 |  |
| Active DL BWP-1 Configuration |  | Config 1, 2 |  | DLBWP.1.1 Note 4 |  |
| Active DL BWP-2 Configuration |  | Config 1, 2 |  | DLBWP.1.3 Note 4 |  |
| Initial UL BWP Configuration |  | Config 1, 2 |  | ULBWP.0.2 Note 4 |  |
| Active UL BWP-1 Configuration |  | Config 1, 2 |  | ULBWP.1.1 Note 4 |  |
| Active UL BWP-2 Configuration |  | Config 1, 2 |  | ULBWP.1.3 Note 4 |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 CCA |  |
| RMSI CORESET parameters |  | Config 1, 2 |  | CR.1.1 CCA |  |
| Dedicated CORESET parameters |  | Config 1, 2 |  | CCR.1.1 CCA |  |
| OCNG Patterns |  | Config 1, 2 |  | OP.1 |  |
| SSB Configuration | Semi- static channel acces | Config 1, 2 |  | SSB.1 CCA |  |
|  | Dymamic channel acces | Config 1, 2 |  | SSB.2 CCA |  |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 FR1 |  |
| Correlation Matrix and Antenna Configuration |  | Config 1, 2 |  | 1x2 Low |  |
| TRS Configuration |  | Config 1, 2 |  | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1, 2 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  | Config 1, 2 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  | Config 1, 2 |  | 1 | 1 |
| UL CCA probability (PCCA_UL) |  | Config 1, 2 |  | 0 | 1 |
| PRACH configuration |  | Config 1, 2 |  | N/A | Configuration #1 in table A.3.8.2.1-1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| NocNote 2 |  | Config 1, 2 | dBm/SCS | -101 |  |
| SS-RSRP Note 3 |  | Config 1, 2 | dBm/SCS | -84 |  |
| Ês/Iot |  | Config 1, 2 | dB | 17 |  |
| Ês/Noc |  | Config 1, 2 | dB | 17 |  |
| IoNote3 |  | Config 1, 2 | dBm/38.16 MHz | -52.86 |  |
| Propagation Condition |  |  |  | AWGN |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3].NOTE 5: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.20.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.10.3.5.1.1-4: Sounding Reference Symbol Configuration for UL BWP Switch Test in EN-DC

| Field | Value | Comment |
| --- | --- | --- |
| c-SRS | 24 | Frequency hopping is disabled |
| b-SRS | 0 |  |
| b-hop | 0 |  |
| freqDomainPosition | 0 | Frequency domain position of SRS |
| freqDomainShift | 0 |  |
| groupOrSequenceHopping | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset | sl5=4 for SCS 30 kHz | Once every 5 slots |
| pathlossReferenceRS | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage | Codebook | Codebook based UL transmission |
| startPosition | 0 | resourceMapping setting: SRS on last symbol of slot, and 1symbols for SRS without repetition. |
| nrofSymbols | n1 |  |
| repetitionFactor | n1 |  |
| combOffset-n2 | 0 | transmissionComb setting |
| cyclicShift-n2 | 0 |  |
| nrofSRS-Ports | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |

##### A.10.3.5.1.2 Test Requirements

The UE capable of bwp-SwitchingDelay type1 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 2 (PSCell) less than 21.5 ms from the beginning of time period T1.

The UE capable of bwp-SwitchingDelay type2 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 2 (PSCell) less than 23 ms from the beginning of time period T1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The above delay is calculated as follows:’

The active UL BWP switch delay from UL BWP-1 to UL BWP-2 can be expressed as:

TBWPswitchDelay*Tslot +1*Tslot + (1+ L3)*TSSB,RO + 10 ms

Where:

- TBWPswitchDelay = 1 ms (2 slots) and 2.5 ms (5 slots) for bwp-SwitchingDelay [2] type1 and type2 UE capabilities according to clause 8.6.4.

- Tslot = It is the slot length. It is 0.5 ms for 30 kHz.

- L3 = It is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3= 0 during T2 since PCCA = 1.

- TSSB,RO = 10 ms according to FR1 PRACH configuration 1.

This gives a total of 21.5 ms and 23 ms for type1 and type2 UE respectively.

#### A.10.3.5.2 DCI-based and Timer-based Active BWP Switch

##### A.10.3.5.2.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.10.3.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in TS38.133 clause 8.6, and interruption requirement for E-UTRA victim cell defined in TS36.133 clause 7.32.2.7. Supported test configurations are shown in table A.10.3.5.2.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), and one NR PSCell (Cell 2) as given in table A.10.3.5.2.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell is specified in table A.10.3.5.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (PSCell) on radio channel 2 (PSCC).

- UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell.

- UE is configured with a bwp-InactivityTimer timer value for PSCell.

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

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: A UE which fulfils the requirements in test case A.10.3.5.2.2 can skip the test cases in A.10.3.5.2.1.NOTE 3: The UE supporting EN-DC with only NR band(s) with shared spectrum access is required to be test. |  |

Table A.10.3.5.2.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | 1 | One E-UTRA radio channel is used for this test |
| NR RF Channel Number |  | 2 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| Active PSCell |  | Cell 2 | PSCell on RF channel number 2. |
| CP length |  | Normal |  |
| DRX |  | OFF | For both PCell and PSCell |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clause A.3.26.2.2 |  |
| bwp-InactivityTimer | ms | 200 |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 | Individual offset for cells on PCC. |
| Cell-individual offset for cells on RF channel number 2 | dB | 0 | Individual offset for cells on PSCC. |
| Cell 2 timing offset to Cell 1 | s | 3 | Synchronous EN-DC |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.10.3.5.2.1.1-3.: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

| Parameter |  |  | Unit | Cell 2 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1,2 |  | TDD |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |
| BWchannel |  | Config 1,2 |  | 40 MHz: NPRB,c = 106 |
| Active BWP ID |  |  |  | 1, 2 |
| Initial DL BWP Configuration |  | Config 1,2 |  | DLBWP.0.2 Note 4 |
| Active DL BWP-1 Configuration |  | Config 1,2 |  | DLBWP.1.1 Note 4 |
| Active DL BWP-2 Configuration |  | Config 1,2 |  | DLBWP.1.3 Note 4 |
| Initial UL BWP Configuration |  | Config 1,2 |  | ULBWP.0.2 Note 4 |
| Active UL BWP-1 Configuration |  | Config 1,2 |  | ULBWP.1.1 Note 4 |
| Active UL BWP-2 Configuration |  | Config 1,2 |  | ULBWP.1.3 Note 4 |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 CCA |
| RMSI CORESET parameters |  | Config 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET parameters |  | Config 1,2 |  | CCR.1.1 CCA |
| OCNG Patterns |  | Config 1,2 |  | OP.1 |
| SSB Configuration | Semi- static channel acces | Config 1,2 |  | SSB.1 CCA |
|  | Dymamic channel acces | Config 1,2 |  | SSB.2 CCA |
| SMTC Configuration |  | Config 1,2 |  | SMTC.1 |
| TRS Configuration |  | Config 1,2 |  | TRS.1.2 TDD |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1,2 |  | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  | Config 1,2 |  | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  | Config 1,2 |  | 1 |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1,2 |  | 1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 Low |
| EPRE ratio of PSS to SSS |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| NocNote 2 |  | Config 1,2 | dBm/SCS | -101 |
| SS-RSRP Note 3 |  | Config 1,2 | dBm/SCS | -84 |
| Ês/Iot |  | Config 1,2 | dB | 17 |
| Ês/Noc |  | Config 1,2 | dB | 17 |
| IoNote3 |  | Config 1,2 | dBm/38.16 MHz | -59 |
| Propagation Condition |  |  |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3].NOTE 5: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |

A.10.3.5.2.1.2 Test Requirements

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

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

##### A.10.3.5.2.2 E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC

A.10.3.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirements for NR victim cell defined in clause 8.2.1.2.7 and interruption requirement for E-UTRA victim cell defined in clause 7.32.2.7 of TS 36.133 [15]. Supported test configurations are shown in table A.10.3.5.2.2.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1), one NR PSCell (Cell 2) and one NR SCell (Cell 3) as given in table A.10.3.5.2.2.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell and SCell are specified in table A.10.3.5.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and SCell (Cell 3) to ensure that the UE will have ACK/NACK sending.

PDCCHs indicating new transmissions shall be sent continuously on PSCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (PSCell) on radio channel 2 (PSCC) and Cell 3 (SCell) on radio channel 3 (SCC).

- UE is configured with 2 different UE-specific downlink bandwidth parts for PSCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

- UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for SCell, BWP-0 in Cell 3 before starting the test.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PSCell.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in SCell.

- UE is configured with a bwp-InactivityTimer timer value for PSCell.

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

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: A UE which fulfils the requirements in test case A.10.3.5.2.2 can skip the test cases in A.10.3.5.2.1.NOTE 3: NR configuration is the same for PSCell and SCells.NOTE 4: The UE supporting EN-DC with only NR band(s) with shared spectrum access is required to be tested. |  |

Table A.10.3.5.2.2.1-2: General test parameters for DL BWP switch in synchronous EN-DC

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | 1 | One E-UTRA radio channel is used for this test |
| NR RF Channel Number |  | 2, 3 | Two NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| Active PSCell |  | Cell 2 | PSCell on RF channel number 2. |
| Active SCell |  | Cell 3 | SCell on RF channel number 3. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clause A.3.26.2.2 |  |
| Cell-individual offset for cells on RF channel number 2 | dB | 0 | Individual offset for cells on PSCC. |
| Cell-individual offset for cells on RF channel number 3 | dB | 0 | Individual offset for cells on SCC. |
| Cell 2 timing offset to Cell 1 | s | 3 | Synchronous EN-DC |
| Cell 3 timing offset to Cell 2 | s | 3 | Synchronous cells |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.10.3.5.2.2.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

| Parameter |  |  | Unit | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |  |
| Duplex mode |  | Config 1,2 |  | TDD |  |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1,2 |  | 40 MHz: NPRB,c = 106 |  |
| Active BWP ID |  |  |  | 1, 2 | 0 |
| Initial BWP Configuration |  | Config 1,2 |  | DLBWP.0.2 | DLBWP.0.2 |
| Active BWP-0 Configuration |  | Config 1,2 |  | NA | DLBWP.0.2 |
| Active BWP-1 Configuration |  | Config 1,2 |  | DLBWP.1.3 | NA |
| Active BWP-2 Configuration |  | Config 1,2 |  | DLBWP.1.1 | NA |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 CCA |  |
| RMSI CORESET parameters |  | Config 1,2 |  | CR.1.1 CCA |  |
| Dedicated CORESET parameters |  | Config 1,2 |  | CCR.1.1 CCA |  |
| OCNG Patterns |  | Config 1,2 |  | OP.1 |  |
| SSB Configuration | Semi- static channel acces | Config 1,2 |  | SSB.1 CCA |  |
|  | Dymamic channel acces | Config 1,2 |  | SSB.2 CCA |  |
| SMTC Configuration |  | Config 1,2 |  | SMTC.1 |  |
| TRS Configuration |  | Config 1,2 |  | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1,2 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  | Config 1,2 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  | Config 1,2 |  | 1 | 1 |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1,2 |  | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 |  |
| Propagation Condition |  |  |  | AWGN |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| NocNote 2 |  | Config 1,2 | dBm/SCS kHz | -101 | -101 |
| SS-RSRP Note 3 |  | Config 1,2 | dBm/SCS kHz | -84 | -84 |
| Ês/Iot |  | Config 1,2 | dB | 17 | 17 |
| Ês/Noc |  | Config 1,2 | dB | 17 | 17 |
| IoNote3 |  | Config 1,2 | dBm/38.16 MHz | -59 | -59 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3].NOTE 5: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

A.10.3.5.2.2.2 Test Requirements

During T1, the UE shall start to send the ACK for PSCell in the DL slot right after slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK for PSCell in the DL slot right after slot (j+TBWPswitchDelay+k11).

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of PCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 7.32.2.7 of TS 36.133 [15].

During T1, the start of the interruption of SCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

During T3, the start of the interruption of SCell during PSCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of SCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.6.2.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK in the DL slot right after slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

Editor’s note: FFS value of k1 for type 1 and type 2 UE.

#### A.10.3.5.3 RRC-based Active BWP Switch

##### A.10.3.5.3.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC

A.10.3.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.10.3.5.3.1.1-1.

The test scenario comprises of one E-UTRA PCell (Cell 1) and one NR PSCell (Cell 2) as given in table A.10.3.5.3.1.1-2. Cell-specific parameters of E-UTRA PCell are specified in table A.3.7.2.1-1 and Cell-specific parameters of NR PSCell are specified in table A.10.3.5.3.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) and to Cell 2 (PSCell) on radio channel 2 (PSCC).

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PSCell).

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PSCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH at the beginning of the DL slot right after PSCell’s DL slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC) as defined in clause 8.6.3 and be ready for the reception of uplink grant for the PSCell no later than at the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC). The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the beginning of the DL slot right after slot (i+TRRCprocessingDelay+TBWPswitchDelayRRC).

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.10.3.5.3.1.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD, With CCA: NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2:  The UE supporting EN-DC with only NR band(s) with shared spectrum access is required to be tested. |  |

Table A.10.3.5.3.1.1-2: General test parameters for DL BWP switch in synchronous EN-DC

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | 1 | One E-UTRA radio channel is used for this test |
| NR RF Channel Number |  | 2 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| Active PSCell |  | Cell 2 | PSCell on RF channel number 2. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clause A.3.26.2.2 |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 | Individual offset for cells on PCC. |
| Cell-individual offset for cells on RF channel number 2 | dB | 0 | Individual offset for cells on PSCC. |
| Cell 2 timing offset to Cell 1 | s | 3 | Synchronous EN-DC |
| T1 | s | 0.2 |  |

Table A.10.3.5.3.1.1-3: NR Cell specific test parameters for DL BWP switch in synchronous EN-DC

| Parameter |  |  |  | Unit | Cell 2 |
| --- | --- | --- | --- | --- | --- |
| Frequency Range |  |  |  |  | FR1 |
| Duplex mode |  |  | Config 1,2 |  | TDD |
| TDD configuration |  |  | Config 1,2 |  | TDDConf.1.1 CCA |
| BWchannel |  |  | Config 1,2 |  | 40 MHz: NPRB,c = 106 |
| Active DL BWP ID |  |  |  |  | 1, 2 |
| Initial DL BWP Configuration |  |  | Config 1,2 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  |  | Config 1,2 |  | ULBWP.0.2 |
| Initial Condition |  | Active DL BWP-1 Configuration | Config 1,2 |  | DLBWP.1.3 |
| Final Condition |  | Active DL BWP-1 Configuration | Config 1,2 |  | DLBWP.1.1 |
| Initial UL BWP Configuration |  |  | Config 1,2 |  | ULBWP.0.2 |
| Active UL BWP-1 Configuration |  |  | Config 1,2 |  | ULBWP.1.3 |
| Active UL BWP-2 Configuration |  |  | Config 1,2 |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  |  | Config 1,2 |  | SR.1.1 CCA |
| RMSI CORESET parameters |  |  | Config 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET parameters |  |  | Config 1,2 |  | CCR.1.1 CCA |
| OCNG Patterns |  |  | Config 1,2 |  | OP.1 |
| SSB Configuration | Semi- static channel acces |  | Config 1,2 |  | SSB.1 CCA |
|  | Dymamic channel acces |  | Config 1,2 |  | SSB.2 CCA |
| SMTC Configuration |  |  | Config 1,2 |  | SMTC.1 |
| TRS Configuration |  |  | Config 1,2 |  | TRS.1.2 TDD |
| DL CCA probability for semi-static channel access (PCCA_DL) |  |  | Config 1,2 |  | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  |  | Config 1,2 |  | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  |  | Config 1,2 |  | 1 |
| DL CCA probability for semi-static channel access (PCCA_DL) |  |  | Config 1,2 |  | 1 |
| Antenna Configuration |  |  |  |  | 1x2 |
| Propagation Condition |  |  |  |  | AWGN |
| EPRE ratio of PSS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| NocNote 2 |  |  | Config 1,2 | dBm/SCS kHz | -101 |
| SS-RSRP Note 3 |  |  | Config 1,2 | dBm/SCS  kHz | -84 |
| Ês/Iot |  |  | Config 1,2 | dB | 17 |
| Ês/Noc |  |  | Config 1,2 | dB | 17 |
| IoNote3 |  |  | Config 1,2 | dBm/38.16 MHz | -59 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3].NOTE 5: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

A.10.3.5.3.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PSCell in the beginning of the DL slot right after  slot (i+ TRRCprocessingDelay+TBWPswitchDelayRRC ).

All of the above test requirements shall be fulfilled in order for the observed PSCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.10.3.6 PSCell addition and release delay

#### A.10.3.6.1 Addition and Release Delay of known NR PSCell on the carrier under CCA

##### A.10.3.6.1.1 Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delays on the carrier under CCA under EN-DC are within the requirements stated in clause 7.31A.2 [15] for the case when the PSCell is known by the UE at the time of addition.

Supported test configurations are shown in A.10.3.6.1.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.1-1. The E-UTRA cell once set up is not changed across time.

The test parameters for NR cell are given in tables A.10.3.6.1.1-2 and cell-specific parameters in A.10.3.6.1.1-3 below. The test consists of five successive time periods with duration of T1, T2, T3, T4 and T5 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (E-UTRA PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event B1 is configured for neighbour cell (Cell 2). Before the start of T2 the UE is configured with the measurement gaps (gap pattern Id # 0). The Cell 2 becomes known to the UE during T2. Therefore, during T2 the UE shall report Event B1. The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2.

The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The point in time at which the RRC message to add PSCell (Cell 2) is received at the UE antenna connector defines the start of period T4.

The test system shall observe the periodic reporting of CSI for PSCell during T5. The point in time at which the UE has sent PRACH to the PSCell (Cell 2) defines the start of period T5.

The test system shall send a RRC message to the UE to release PSCell (Cell 2) on radio channel 2. The RRC message to release PSCell (Cell 2) shall be sent to the UE during period T5, after the UE has sent at least one CQI report with non-zero CQI index for PSCell (Cell 2). The point in time at which the RRC message to release PSCell (Cell 2) is received at the UE antenna connector defines the start of period T6.

Table A.10.3.6.1.1-1: Supported test configurations for FR1 PSCell

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD, NR SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.3.6.1.1-2: General Test Parameters for PSCell Addition and Release

| Parameter |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| RF Channel Number |  |  |  | 1, 2 | Two radio channels are used for this test. One for E-UTRA cell and second for NR Cell on the carrier under CCA |
| Initial | Active PCell |  |  | Cell 1 | PCell on RF channel number 1. |
|  | Neighbour cell |  |  | Cell 2 | Neighbour cell on RF channel number 2. |
| Final | Active PCell |  |  | Cell 1 | PCell on RF channel number 1. |
| Condition | Neighbour Cell |  |  | Cell 2 | PSCell released on RF channel number 2. |
| B1 | Hysteresis |  | dB | 0 | Hysteresis for evaluation of event B1. |
|  | Threshold RSRP |  | dBm | -93 | Actual RSRP threshold for event B1. Needs to take absolute accuracy tolerance in clause 9.1.11.1 into account plus margin. |
|  | Time to Trigger |  | s | 0 |  |
| DRX |  |  |  | OFF | Continuous monitoring of primary cell |
| DL CCA model |  | Dynamic channel accessNote 1, 3 |  |  | As specified in clause A.3.20.2.1 |
|  |  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model |  | Dynamic channel access Note 1, 3 |  |  | As specified in clause A.3.20.2.2 |
|  |  | Semi-static channel access Note 2,3 |  |  |  |
| Measurement gap pattern Id |  |  |  | 0 | Gaps are configured before T2 and released before T3. |
| PRACH configuration on Cell 2 |  |  |  | FR1 PRACH configuration 2 | Captured in A.3.8.2.1 |
| CQI/PMI periodicity and offset configuration index on Cell 2 |  |  |  | 2 ms | CQI reporting for PSCell every uplink subframe |
| Cell-individual offset for cells on RF channel number 1 |  |  | dB | 0 | Individual offset for cells on primary component carrier. |
| Cell-individual offset for cells on RF channel number 2 |  |  | dB | 0 | Individual offset for cells on carrier frequency of Cell 2. |
| T304 |  |  | ms | 500 |  |
| LCCA_DL |  |  |  | 5 |  |
| T1 |  |  | s | 1 | During this time the PCell shall be known and Cell 2 shall be unknown. |
| T2 |  |  | s | ≥ Tidentify_irat_cca_without_index | Tidentify_irat_cca_without_index is defined in clause 8.1.2.4.21A and 8.1.2.4.22A in TS 36.133During this time the UE shall identify neighbour cell (Cell 2) and report event B1. |
| T3 |  |  | s | 3 | During this time the test system transmit the RRC messages to release measurement gap and add the PSCell |
| T4 |  |  | s | ≥ Tconfig_PSCell_withCCA | During this time the UE adds the PSCell. Tconfig_PSCell_withCCA  is defined in clause 7.31A.2 |
| T5 |  |  | s | 0.5 | During this time the UE sends CSI reports for PSCell. |
| T6 |  |  | s | 0.5 | During this time the UE releases the PSCell. |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under            dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.3.6.1.1-3: Cell Specific Parameters for PSCell Addition and Release

| Parameter | Unit | Config | Test |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| PCCA_DL for dynamic channel access Note 5,7 | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |
| PCCA_DL for semi-static channel access Note 6,7 | - | PCCA_DL=0.9375 | PCCA_DL=0.9375 |  |  |  |  |
| PCCA_UL for dynamic channel access Note 5,7 | - | 1 | 1 |  |  |  |  |
| PCCA_UL for semi-static channel access Note 6,7 | - | 1 | 1 |  |  |  |  |
| E-UTRA RF Channel Number |  | 1,2 | 1 |  |  |  |  |
| NR RF Channel Number |  | 1,2 | 2 |  |  |  |  |
| TDD configuration |  | 1,2 | TDDConf.1.1 CCA |  |  |  |  |
| BWchannel |  | 1,2 | 40: NPRB,c = 106 |  |  |  |  |
| Initial BWP Configuration |  | 1,2 | DLBWP.0.1ULBWP.0.1 |  |  |  |  |
| Dedicated BWP Configuration |  | 1,2 | DLBWP.1.1ULBWP.1.1 |  |  |  |  |
| PDSCH Reference |  | 1,2 | SR1.1 CCA |  |  |  |  |
| RMSI CORESET Reference |  | 1,2 | CR1.1 CCA |  |  |  |  |
| Dedicated CORESET Reference |  | 1,2 | CCR1.1 CCA |  |  |  |  |
| OCNG Patterns |  | 1,2 | OP.1 |  |  |  |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |  |  |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |  |  |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |  |  |  |
| SMTC configuration |  | 1,2 | SMTC.1 |  |  |  |  |
| TRS Configuration |  | 1,2 | TRS.1.2 TDD |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | dB | 1,2 | 0 |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1,2 | N/A | -85 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1,2 | N/A | -82 |  |  |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | 1,2 | -infinity | 0 |  |  |  |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | 1,2 | -infinity | 0 |  |  |  |
| SS-RSRPNote3 | dBm/SCS | 1,2 | -infinity | -82 |  |  |  |
| IoNote3 | dBm/38.1 MHz | 1,2 | N/A | -51 |  |  |  |
| Propagation condition |  | 1,2 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during muted slots or during DBT windows.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

##### A.10.3.6.1.2 Test Requirements

The UE shall transmit the PRACH to PSCell at latest Tconfig_PSCell_withCCA Note1 into T4.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T5.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T5

The UE shall stop sending CSI reports for PSCell in at latest 20 ms into T6.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

NOTE 1: The PSCell addition delay can be expressed as follows as specified in clause 7.31A.2 [15]:

Tconfig_PSCell_withCCA = TRRC_delay + Tprocessing + Tsearch_withCCA + T∆_withCCA + TPSCell_ DU_withCCA + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 20 ms

Tsearch_withCCA = 0

T∆_withCCA = (1+ L2)*20 ms

TPSCell_ DU_withCCA = 20 ms.

L2 is the number of SMTC occasions not available at the UE for fine time tracking and acquiring full timing information, where L2  LCCA_DL.

### A.10.3.7 Void

## A.10.4 Measurement procedure

### A.10.4.1 Intra-frequency measurements

#### A.10.4.1.1 Event-triggered reporting tests on PSCC without gaps under non-DRX

##### A.10.4.1.1.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

##### A.10.4.1.1.2 Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and two cells on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model: PSCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.10.4.1.1.2-1 and A.10.4.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

Table A.10.4.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.10.4.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

| Parameter | Unit | Test Configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 |  |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2 | NR cell 3 | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 5 |  |

Table A.10.4.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 2 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 12 |  | 12 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_intra_cca |  | TPSS/SSS_sync_intra_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.1.1.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.1.2 Void

#### A.10.4.1.3 Void

#### A.10.4.1.4 Event-triggered reporting tests on PSCC with per-UE gaps under DRX

##### A.10.4.1.4.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

##### A.10.4.1.4.2 Test parameters

Three cells are deployed in the test, which are E-UTRAN PCell (Cell 1) and two cells on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model: PSCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.10.4.1.4.2-1, A.10.4.1.4.2-2 and A.10.4.1.4.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PSCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

There are two BWPs configured in Cell 2, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 2. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.10.4.1.4.2-2: General test parameters for intra-frequency event triggered reporting with per-UE gaps

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 |  |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2 | NR cell 3 | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |
| Measurement gap type |  | Config 1,2 | Per-UE gaps |  |
| Measurement gap repitition periodicity | ms | Config 1,2 | 40 |  |
| Measurement gap length | ms | Config 1,2 | 6 |  |
| Measurement gap offset | ms | Config 1,2 | 39 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | DRX.1 |  |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 5 |  |

Table A.10.4.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 2 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 12 |  | 12 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_intra_cca |  | TPSS/SSS_sync_intra_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.1.4.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.1.5 Void

#### A.10.4.1.6 Void

#### A.10.4.1.7 Void

#### A.10.4.1.8 Void

#### A.10.4.1.9 Void

#### A.10.4.1.10 Void

#### A.10.4.1.11 Void

#### A.10.4.1.12 Void

### A.10.4.2 Inter-frequency measurements

#### A.10.4.2.1 Void

#### A.10.4.2.2 Void

#### A.10.4.2.3 EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used

##### A.10.4.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.3.1-1, A.10.4.2.3.1-2, and A.10.4.2.3.1-3.

In this test measurement gap pattern configuration # 0 as defined in table A.10.4.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.3.1-1.

Table A.10.4.2.3.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE TDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.3.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 with CCA is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR cell 3 | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 1.7 |  |

Table A.10.4.2.3.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 12 |  | 12 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.2.3.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.4 EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used

##### A.10.4.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.    The test parameters and configurations are given in tables A.10.4.2.4.1-1, A.10.4.2.4.1-2, and A.10.4.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.4.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.4.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE TDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.4.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter | Unit | Test | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 |  | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) |  | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 with CCA is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |  |
| A3-Offset | dB | Config 1,2 | -6 |  |  |
| Hysteresis | dB | Config 1,2 | 0 |  |  |
| CP length |  | Config 1,2 | Normal |  |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |  |
| Filter coefficient |  | Config 1,2 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s |  | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s |  | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |  |
| T2 | s | Config 1,2 | 2.5 | 17 |  |

Table A.10.4.2.4.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 5 |  | 5 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT windowNOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

Table A.10.4.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1&3 | Test2&4 | Comment |
| --- | --- | --- | --- |
|  | Value | Value |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.10.4.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.10.4.2.4.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.5 EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used

##### A.10.4.2.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.    The test parameters and configurations are given in tables A.10.4.2.5.1-1, A.10.4.2.5.1-2, and A.10.4.2.5.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.10.4.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.5.1-1.

Table A.10.4.2.5.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE TDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.5.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter | Unit | Test Configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 with CCA is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR cell 3 | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 2 |  |

Table A.10.4.2.5.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 5 |  | 5 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.2.5.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.6 EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used

##### A.10.4.2.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2. The test parameters and configurations are given in tables A.10.4.2.6.1-1, A.10.4.2.6.1-2, and A.10.4.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.6.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.6.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE TDDNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.6.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter | Unit | Test | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  | configuration | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 |  | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cell |  | Config 1,2 | LTE Cell 1 (PCell) and NR cell 2 with CCA (PScell) |  | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 with CCA is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |  |
| A3-Offset | dB | Config 1,2 | -6 |  |  |
| Hysteresis | dB | Config 1,2 | 0 |  |  |
| CP length |  | Config 1,2 | Normal |  |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |  |
| Filter coefficient |  | Config 1,2 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between PCell and PSCell |  | Config 1,2 | 3 s |  | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 s |  | Synchronous cells. |
| T1 | s | Config 1,2 | 5 |  |  |
| T2 | s | Config 1,2 | 3 | 20 |  |

Table A.10.4.2.6.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,2 | TDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  |
| TDD configuration |  |  | Config 1,2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| Initial DL BWP |  |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference |  |  | Config 1,2 | SR.1.1 CCA |  | - |  |
| CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 CCA |  | - |  |
| SSB parameters | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 CCA |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  | Config 1,2 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration |  |  | Config 1,2 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  | Config 1,2 | 2 |  | 2 |  |
| WCCA_DL |  | ms | Config 1,2 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/38.16 MHz | Config 1,2 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

Table A.10.4.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1Value | Test2Value | Comment |
| --- | --- | --- | --- |
|  |  |  |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.10.4.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.10.4.2.6.2 Test Requirements

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

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.7 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used

##### A.10.4.2.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.7.1-1, A.10.4.2.7.1-2, and A.10.4.2.7.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.2.7.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.7.1-1.

Table A.10.4.2.7.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | E-UTRAN cell: LTE FDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 5 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 6 | E-UTRAN cell: LTE TDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.7.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter | Unit | Test | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  | configuration | Test 1 |  |
| E-UTRA RF Channel Number |  | Config 1,2,3,4,5,6 | 1 | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2,3,4,5,6 | 1, 2 | Two FR1 NR carrier frequencies are used. NR RF channel 1 is with CCA. |
| Active cell |  | Config 1,2,3,4,5,6 | LTE Cell 1 (PCell) and NR cell 2 (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3,4,5,6 | NR cell 3 | NR cell 3 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2,3,4,5,6 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4,5,6 | 9 |  |
| A3-Offset | dB | Config 1,2,3,4,5,6 | -6 |  |
| Hysteresis | dB | Config 1,2,3,4,5,6 | 0 |  |
| CP length |  | Config 1,2,3,4,5,6 | Normal |  |
| TimeToTrigger | s | Config 1,2,3,4,5,6 | 0 |  |
| Filter coefficient |  | Config 1,2,3,4,5,6 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3,4,5,6 | OFF | DRX is not used |
| Time offset between PCell and PSCell |  | Config 1,2,3,4,5,6 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4,5,6 | 3 ms | Asynchronous cells.The timing of Cell 3 is 3 ms later than the timing of Cell 2. |
|  |  | Config 1,2,3,4,5,6 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2,3,4,5,6 | 5 |  |
| T2 | s | Config 1,2,3,4,5,6 | 1.7 |  |

Table A.10.4.2.7.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2,3,4,5,6 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,4 | TDD |  | FDD |  |
|  |  |  | Config 2,3,5,6 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| TDD configuration |  |  | Config 1,4 | TDDConf.1.1 CCA |  | NA |  |
|  |  |  | Config 2,5 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  | Config 3,6 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| Initial DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2,3,4,5,6 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2,3,4,5,6 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,4 | SR.1.1 CCA |  | SR.1.1 FDD |  |
|  |  |  | Config 2,5 | SR.1.1 CCA |  | SR.1.1 TDD |  |
|  |  |  | Config 3,6 | SR.1.1 CCA |  | SR.2.1 TDD |  |
| CORESET Reference Channel |  |  | Config 1,4 | CR.1.1 CCA |  | CR.1.1 FDD |  |
|  |  |  | Config 2,5 | CR.1.1 CCA |  | CR.1.1 TDD |  |
|  |  |  | Config 3,6 | CR.1.1 CCA |  | CR.2.1 TDD |  |
| SSB | Semi-static channel access Note 5,7 |  | Config 1,4 | SSB.1 CCA |  | SSB.1 FR1 |  |
| parameters |  |  | Config 2,5 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,4 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 2,5 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  | Config 1,2,3,4,5,6 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration |  |  | Config 1,4 | SMTC.2 |  | SMTC.5 |  |
| defined in A.3.11 |  |  | Config 2,3,5,6 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2,4,5 | 30 |  | 15 |  |
| subcarrier spacing |  |  | Config 3,6 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_DL=0.9375 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | Not applicable |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
| LCCA_DL |  |  | Config 1,2,3,4,5,6 | 12 |  | 12 |  |
| WCCA_DL |  | ms | Config 1,2,3,4,5,6 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2,3,4,5,6 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2,3,4,5,6 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2,4,5 | -98 |  | -95 |  |
|  |  |  | Config 3,6 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2,4,5 | -94 | -94 | -Infinity | -88 |
|  |  |  | Config 3,6 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | NR Config 1,2,4,5 | -64.59 | -64.59 | -63.94 | -56.15 |
|  |  | dBm/38.16 MHz | NR Config 3,6 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2,3,4,5,6 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.2.7.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.8 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used

##### A.10.4.2.8.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.8.1-1, A.10.4.2.8.1-2, and A.10.4.2.8.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.8.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.8.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.8.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | E-UTRAN cell: LTE FDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 5 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mod |
| 6 | E-UTRAN cell: LTE TDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.8.1-2: General test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter | Unit | Test | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  | configuration | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | Config 1,2,3,4,5,6 | 1 |  | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2,3,4,5,6 | 1, 2 |  | Two FR1 NR carrier frequencies are used. NR RF channel 1 is with CCA. |
| Active cell |  | Config 1,2,3,4,5,6 | LTE Cell 1 (PCell) and NR cell 2 (PScell) |  | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3,4,5,6 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2,3,4,5,6 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4,5,6 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3,4,5,6 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3,4,5,6 | 0 |  |  |
| CP length |  | Config 1,2,3,4,5,6 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3,4,5,6 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3,4,5,6 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3,4,5,6 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between PCell and PSCell |  | Config 1,2,3,4,5,6 | 3 s |  | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4,5,6 | 3 ms |  | Asynchronous cells.The timing of Cell 3 is 3 ms later than the timing of Cell 2. |
|  |  | Config 1,2,3,4,5,6 | 3 s |  | Synchronous cells. |
| T1 | s | Config 1,2,3,4,5,6 | 5 |  |  |
| T2 | s | Config 1,2,3,4,5,6 | 2.5 | 17 |  |

Table A.10.4.2.8.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting without SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2,3,4,5,6 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,4 | TDD |  | FDD |  |
|  |  |  | Config 2,3,5,6 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| TDD configuration |  |  | Config 1,4 | TDDConf.1.1 CCA |  | NA |  |
|  |  |  | Config 2,5 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  | Config 3,6 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| Initial DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2,3,4,5,6 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2,3,4,5,6 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,4 | SR.1.1 CCA |  | SR.1.1 FDD |  |
|  |  |  | Config 2,5 | SR.1.1 CCA |  | SR.1.1 TDD |  |
|  |  |  | Config 3,6 | SR.1.1 CCA |  | SR.2.1 TDD |  |
| CORESET Reference Channel |  |  | Config 1,4 | CR.1.1 CCA |  | CR.1.1 FDD |  |
|  |  |  | Config 2,5 | CR.1.1 CCA |  | CR.1.1 TDD |  |
|  |  |  | Config 3,6 | CR.1.1 CCA |  | CR.2.1 TDD |  |
| SSB | Semi-static channel access Note 5,7Semi-static channel access Note 5,7 |  | Config 1,4 | SSB.1 CCA |  | SSB.1 FR1 |  |
| parameters |  |  | Config 2,5 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,4 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 2,5 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  | Config 1,2,3,4,5,6 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration |  |  | Config 1,4 | SMTC.2 |  | SMTC.5 |  |
| defined in A.3.11 |  |  | Config 2,3,5,6 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2,4,5 | 30 |  | 15 |  |
| subcarrier spacing |  |  | Config 3,6 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_DL=0.9375 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | Not applicable |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
| LCCA_DL |  |  | Config 1,2,3,4,5,6 | 5 |  | 5 |  |
| WCCA_DL |  | ms | Config 1,2,3,4,5,6 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2,3,4,5,6 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2,3,4,5,6 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2,4,5 | -98 |  | -95 |  |
|  |  |  | Config 3,6 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2,4,5 | -94 | -94 | -Infinity | -88 |
|  |  |  | Config 3,6 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | NR Config 1,2,4,5 | -64.59 | -64.59 | -63.94 | -56.15 |
|  |  | dBm/38.16 MHz | NR Config 3,6 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2,3,4,5,6 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

Table A.10.4.2.8.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test 1Value | Test 2Value | Comment |
| --- | --- | --- | --- |
|  |  |  |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.10.4.2.8.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.10.4.2.8.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.9 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used

##### A.10.4.2.9.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.9.1-1, A.10.4.2.9.1-2, and A.10.4.2.9.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.2.9.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.9.1-1.

Table A.10.4.2.9.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | E-UTRAN cell: LTE FDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 5 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mod |
| 6 | E-UTRAN cell: LTE TDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.9.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter | Unit | Test | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  | configuration |  |  |
| E-UTRA RF Channel Number |  | Config 1,2,3,4,5,6 | 1 | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2,3,4,5,6 | 1, 2 | Two FR1 NR carrier frequencies are used. NR RF channel 1 is with CCA. |
| Active cell |  | Config 1,2,3,4,5,6 | LTE Cell 1 (PCell) and NR cell 2 (PScell) | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3,4,5,6 | NR cell 3 | NR cell 3 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2,3,4,5,6 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4,5,6 | 9 |  |
| A3-Offset | dB | Config 1,2,3,4,5,6 | -6 |  |
| Hysteresis | dB | Config 1,2,3,4,5,6 | 0 |  |
| CP length |  | Config 1,2,3,4,5,6 | Normal |  |
| TimeToTrigger | s | Config 1,2,3,4,5,6 | 0 |  |
| Filter coefficient |  | Config 1,2,3,4,5,6 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3,4,5,6 | OFF | DRX is not used |
| Time offset between PCell and PSCell |  | Config 1,2,3,4,5,6 | 3 s | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4,5,6 | 3 ms | Asynchronous cells.The timing of Cell 3 is 3 ms later than the timing of Cell 2. |
|  |  | Config 1,2,3,4,5,6 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2,3,4,5,6 | 5 |  |
| T2 | s | Config 1,2,3,4,5,6 | 2 |  |

Table A.10.4.2.9.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2,3,4,5,6 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,4 | TDD |  | FDD |  |
|  |  |  | Config 2,3,5,6 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| TDD configuration |  |  | Config 1,4 | TDDConf.1.1 CCA |  | NA |  |
|  |  |  | Config 2,5 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  | Config 3,6 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| Initial DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2,3,4,5,6 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2,3,4,5,6 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,4 | SR.1.1 CCA |  | SR.1.1 FDD |  |
|  |  |  | Config 2,5 | SR.1.1 CCA |  | SR.1.1 TDD |  |
|  |  |  | Config 3,6 | SR.1.1 CCA |  | SR.2.1 TDD |  |
| CORESET Reference Channel |  |  | Config 1,4 | CR.1.1 CCA |  | CR.1.1 FDD |  |
|  |  |  | Config 2,5 | CR.1.1 CCA |  | CR.1.1 TDD |  |
|  |  |  | Config 3,6 | CR.1.1 CCA |  | CR.2.1 TDD |  |
| SSB | Semi-static channel access Note 5,7 |  | Config 1,4 | SSB.1 CCA |  | SSB.1 FR1 |  |
| parameters |  |  | Config 2,5 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,4 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 2,5 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  | Config 1,2,3,4,5,6 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration |  |  | Config 1,4 | SMTC.2 |  | SMTC.5 |  |
| defined in A.3.11 |  |  | Config 2,3,5,6 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2,4,5 | 30 |  | 15 |  |
| subcarrier spacing |  |  | Config 3,6 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_DL=0.9375 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | Not applicable |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
| LCCA_DL |  |  | Config 1,2,3,4,5,6 | 5 |  | 5 |  |
| WCCA_DL |  | ms | Config 1,2,3,4,5,6 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2,3,4,5,6 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2,3,4,5,6 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2,4,5 | -98 |  | -95 |  |
|  |  |  | Config 3,6 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2,4,5 | -94 | -94 | -Infinity | -88 |
|  |  |  | Config 3,6 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | NR Config 1,2,4,5 | -64.59 | -64.59 | -63.94 | -56.15 |
|  |  | dBm/38.16 MHz | NR Config 3,6 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2,3,4,5,6 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

##### A.10.4.2.9.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.2.10 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used

##### A.10.4.2.10.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the EN-DC inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters and configurations are given in tables A.10.4.2.10.1-1, A.10.4.2.10.1-2, and A.10.4.2.10.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.10.4.2.10.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

The configuration of LTE cell 1 is defined in table A.3.7.2.1-1. Supported test configurations are shown in table A.10.4.2.10.1-1.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.10.4.2.10.1-1: EN-DC event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | E-UTRAN cell: LTE FDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | E-UTRAN cell: LTE FDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 5 | E-UTRAN cell: LTE TDDNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mod |
| 6 | E-UTRAN cell: LTE TDDNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1:  The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.4.2.10.1-2: General test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter | Unit | Test | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  | configuration | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | Config 1,2,3,4,5,6 | 1 |  | One E-UTRAN carrier frequency is used. |
| NR RF Channel Number |  | Config 1,2,3,4,5,6 | 1, 2 |  | Two FR1 NR carrier frequencies are used. NR RF channel 1 is with CCA. |
| Active cell |  | Config 1,2,3,4,5,6 | LTE Cell 1 (PCell) and NR cell 2 (PScell) |  | LTE Cell 1 is on E-UTRA RF channel number 1.NR Cell 2 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3,4,5,6 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2,3,4,5,6 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2,3,4,5,6 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4,5,6 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3,4,5,6 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3,4,5,6 | 0 |  |  |
| CP length |  | Config 1,2,3,4,5,6 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3,4,5,6 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3,4,5,6 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3,4,5,6 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between PCell and PSCell |  | Config 1,2,3,4,5,6 | 3 s |  | Synchronous EN-DC |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4,5,6 | 3 ms |  | Asynchronous cells.The timing of Cell 3 is 3 ms later than the timing of Cell 2. |
|  |  | Config 1,2,3,4,5,6 | 3 s |  | Synchronous cells. |
| T1 | s | Config 1,2,3,4,5,6 | 5 |  |  |
| T2 | s | Config 1,2,3,4,5,6 | 3 | 20 |  |

Table A.10.4.2.10.1-3: Cell specific test parameters for EN-DC inter-frequency event triggered reporting with SSB time index detection

| Parameter |  | Unit | Test | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | configuration | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2,3,4,5,6 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1,4 | TDD |  | FDD |  |
|  |  |  | Config 2,3,5,6 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  | MHz | Config 1,2,4,5 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  | Config 3,6 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| TDD configuration |  |  | Config 1,4 | TDDConf.1.1 CCA |  | NA |  |
|  |  |  | Config 2,5 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  | Config 3,6 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| Initial DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.0.1 |  | NA |  |
| Initial UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.0.1 |  | NA |  |
| Dedicated DL BWP |  |  | Config 1,2,3,4,5,6 | DLBWP.1.1 |  | NA |  |
| Dedicated UL BWP |  |  | Config 1,2,3,4,5,6 | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2,3,4,5,6 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2,3,4,5,6 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,4 | SR.1.1 CCA |  | SR.1.1 FDD |  |
|  |  |  | Config 2,5 | SR.1.1 CCA |  | SR.1.1 TDD |  |
|  |  |  | Config 3,6 | SR.1.1 CCA |  | SR.2.1 TDD |  |
| CORESET Reference Channel |  |  | Config 1,4 | CR.1.1 CCA |  | CR.1.1 FDD |  |
|  |  |  | Config 2,5 | CR.1.1 CCA |  | CR.1.1 TDD |  |
|  |  |  | Config 3,6 | CR.1.1 CCA |  | CR.2.1 TDD |  |
| SSB | Semi-static channel access Note 5,7Semi-static channel access Note 5,7 |  | Config 1,4 | SSB.1 CCA |  | SSB.1 FR1 |  |
| parameters |  |  | Config 2,5 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,4 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 2,5 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  | Config 3,6 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  | Config 1,2,3,4,5,6 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration |  |  | Config 1,4 | SMTC.2 |  | SMTC.5 |  |
| defined in A.3.11 |  |  | Config 2,3,5,6 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH |  | kHz | Config 1,2,4,5 | 30 |  | 15 |  |
| subcarrier spacing |  |  | Config 3,6 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_DL=0.9375 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | Not applicable |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 5,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
|  | Dynamic channel access Note 6,7 |  | Config 1,2,3,4,5,6 | PCCA_UL=1 |  | Not applicable |  |
| LCCA_DL |  |  | Config 1,2,3,4,5,6 | 2 |  | 2 |  |
| WCCA_DL |  | ms | Config 1,2,3,4,5,6 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1,2,3,4,5,6 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2,3,4,5,6 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2,4,5 | -98 |  | -95 |  |
|  |  |  | Config 3,6 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2,4,5 | -94 | -94 | -Infinity | -88 |
|  |  |  | Config 3,6 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2,3,4,5,6 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | NR Config 1,2,4,5 | -64.59 | -64.59 | -63.94 | -56.15 |
|  |  | dBm/38.16 MHz | NR Config 3,6 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  | Config 1,2,3,4,5,6 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |

Table A.10.4.2.10.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test 1Value | Test 2Value | Comment |
| --- | --- | --- | --- |
|  |  |  |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.10.4.2.10.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.10.4.2.10.2 Test Requirements

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

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.10.4.3 L1-RSRP measurements for beam reporting

#### A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not used

##### A.10.4.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | LTE FDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.10.4.3.1.2 Test parameters

There are two cells in the test, E-UTRAN Pcell (Cell 1) and FR1 PSCell (Cell 2) which operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.4.3.1.2-1 and table A.10.4.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB GSCN | 1,2 |  | freq1 |
| DL CCA model | 1,2 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1,2 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1,2 |  | TDD |
| TDD Configuration | 1,2 |  | TDDConf.1.1 CCA |
| BWchannel | 1,2 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1,2 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1,2 |  | CCR.1.1 CCA |
| SSB configuration | 1,2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1,2 |  | OP.1 |
| Initial BWP Configuration | 1,2 |  | DLBWP.0.1 ULBWP.0.1 |
| Dedicated BWP configuration | 1,2 |  | DLBWP.1.1 ULBWP.1.1 |
| DBT Window Configuration | 1,2 |  | DBT.1 |
| TRS Configuration | 1,2 |  | TRS.1.2 TDD |
| DRX configuration | 1,2 |  | Off |
| reportConfigType | 1,2 |  | periodic |
| reportQuantity | 1,2 |  | ssb-Index-RSRP |
| Number of reported RS | 1,2 |  | 2 |
| L1-RSRP reporting period | 1,2 | slot | 80 |
| T1 | 1,2 | s | 5 |
| T2 | 1,2 | s | 1 |
| EPRE ratio of PSS to SSS |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | 1,2 | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1,2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.10.4.3.1.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1,2 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1,2 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1,2 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1,2 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1,2 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1,2 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1,2 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1,2 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1,2 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS Res when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.10.4.3.1.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.3.2 SSB based L1-RSRP measurement on PSCC when DRX is used

##### A.10.4.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | LTE FDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.10.4.3.2.2 Test parameters

There are two cells in the test, E-UTRAN Pcell (Cell 1) and FR1 PSCell (Cell 2) which operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.4.3.2.2-1 and table A.10.4.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB GSCN | 1,2 |  | freq1 |
| DL CCA model | 1,2 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1,2 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1,2 |  | TDD |
| TDD Configuration | 1,2 |  | TDDConf.1.1 CCA |
| BWchannel | 1,2 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1,2 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1,2 |  | CCR.1.1 CCA |
| SSB configuration | 1,2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1,2 |  | OP.1 |
| Initial BWP Configuration | 1,2 |  | DLBWP.0.1 ULBWP.0.1 |
| Dedicated BWP configuration | 1,2 |  | DLBWP.1.1 ULBWP.1.1 |
| DBT Window Configuration | 1,2 |  | DBT.1 |
| TRS Configuration | 1,2 |  | TRS.1.2 TDD |
| DRX configuration | 1,2 |  | DRX.3 |
| reportConfigType | 1,2 |  | periodic |
| reportQuantity | 1,2 |  | ssb-Index-RSRP |
| Number of reported RS | 1,2 |  | 2 |
| L1-RSRP reporting period | 1,2 | slot | 80 |
| T1 | 1,2 | s | 5 |
| T2 | 1,2 | s | 1 |
| EPRE ratio of PSS to SSS |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | 1,2 | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1,2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.10.4.3.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1,2 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1,2 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1,2 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1,2 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1,2 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1,2 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1,2 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1,2 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1,2 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.10.4.3.2.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.3.3 SSB based L1-RSRP measurement on SCC when DRX is not used

##### A.10.4.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.1.1-1.

Table A.10.4.3.3.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | LTE FDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.10.4.3.3.2 Test parameters

There are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2), and FR1 SCell (Cell 3). Cell 2 and Cell 3 operate on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 and Cell 3 are given in table A.10.4.3.3.2-1 and table A.10.4.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Active PScell | 1,2 |  | Cell 2 |
| Active Scell | 1,2 |  | Cell 3 |
| RF Channel Number | 1,2 |  | 1: Cell 22: Cell 3 |
| DL CCA model | 1,2 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1,2 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1,2 |  | TDD |
| TDD Configuration | 1,2 |  | TDDConf.1.1 CCA |
| BWchannel | 1,2 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1,2 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1,2 |  | CCR.1.1 CCA |
| SSB configuration | 1,2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1,2 |  | OP.1 |
| Initial BWP Configuration | 1,2 |  | DLBWP.0.1 ULBWP.0.1 |
| Dedicated BWP configuration | 1,2 |  | DLBWP.1.1 ULBWP.1.1 |
| DBT Window Configuration | 1,2 |  | DBT.1 |
| TRS Configuration | 1,2 |  | TRS.1.2 TDD |
| DRX configuration | 1,2 |  | Off |
| reportConfigType | 1,2 |  | periodic |
| reportQuantity | 1,2 |  | ssb-Index-RSRP |
| Number of reported RS | 1,2 |  | 2 |
| L1-RSRP reporting period | 1,2 | slot | 80 |
| T1 | 1,2 | s | 5 |
| T2 | 1,2 | s | 1 |
| EPRE ratio of PSS to SSS |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | 1,2 | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1,2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.10.4.3.3.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1, 2 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1, 2 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1, 2 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1, 2 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1, 2 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1, 2 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1, 2 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.10.4.3.3.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 3.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.3.4 SSB based L1-RSRP measurement on SCC when DRX is used

##### A.10.4.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.10.4.3.4.1-1.

Table A.10.4.3.4.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | LTE FDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.10.4.3.4.2 Test parameters

There are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2), and FR1 SCell (Cell 3). Cell 2 and Cell 3 operate on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 and Cell 3 are given in table A.10.4.3.4.2-1 and table A.10.4.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.10.4.3.4.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Active PScell | 1,2 |  | Cell 2 |
| Active Scell | 1,2 |  | Cell 3 |
| RF Channel Number | 1,2 |  | 1: Cell 22: Cell 3 |
| DL CCA model | 1,2 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1,2 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1,2 |  | TDD |
| TDD Configuration | 1,2 |  | TDDConf.1.1 CCA |
| BWchannel | 1,2 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1,2 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1,2 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1,2 |  | CCR.1.1 CCA |
| SSB configuration | 1,2 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1,2 |  | OP.1 |
| Initial BWP Configuration | 1,2 |  | DLBWP.0.1 ULBWP.0.1 |
| Dedicated BWP configuration | 1,2 |  | DLBWP.1.1 ULBWP.1.1 |
| DBT Window Configuration | 1,2 |  | DBT.1 |
| TRS Configuration | 1,2 |  | TRS.1.2 TDD |
| DRX configuration | 1,2 |  | DRX.3 |
| reportConfigType | 1,2 |  | periodic |
| reportQuantity | 1,2 |  | ssb-Index-RSRP |
| Number of reported RS | 1,2 |  | 2 |
| L1-RSRP reporting period | 1,2 | slot | 80 |
| T1 | 1,2 | s | 5 |
| T2 | 1,2 | s | 1 |
| EPRE ratio of PSS to SSS |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | 1,2 | dB | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1,2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.10.4.3.4.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1, 2 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1, 2 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1, 2 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1, 2 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1, 2 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1, 2 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1, 2 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.10.4.3.4.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 3.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.10.4.4 E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA

#### A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

##### A.10.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements under CCA and clause 8.1.2.4.22A of TS 36.133[15] for E-UTRAN TDD-NR measurements under CCA.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.1.1-1, A.10.4.4.1.1-2, A.10.4.4.1.1-3 and A.10.4.4.1.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.10.4.4.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.4.4.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| E-UTRA RF Channel Number |  |  | 1, 2 | 1 | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  |  | 1, 2 | 1,2 | Two FR1 NR carrier frequency under CCA is used. |
| DL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |
| UL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |
| LCCA_DL |  |  | 1, 2 | 12 |  |
| WCCA_DL |  | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |
| Active cell |  |  | 1, 2 | E-UTRA cell 1 (PCell) and NR cell 2 with CCA (PSCell) | E-UTRA cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  |  | 1, 2 | NR cell 3 | NR cell 3 is on NR RF channel number 2. |
| Gap Pattern Id |  |  | 1, 2 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  |  | 1, 2 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 |  | dBm | 1, 2 | Note 1 | E-UTRA RSRP/RSRQ/SINR threshold for E-UTRA RSRP measurement on cell 1 for event B2 [16] |
| b2-Threshold2NR |  | dBm | 1, 2 | Note 2 | SS-RSRP/ SS-RSRQ/ SS-SINR threshold measurement on cell 3 for event B2 [16] |
| Hysteresis |  | dB | 1, 2 | 0 |  |
| CP length |  |  | 1, 2 | Normal |  |
| TimeToTrigger |  | s | 1, 2 | 0 |  |
| Filter coefficient |  |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  |  | 1, 2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  |  | 1, 2 | 3s | Synchronous cells. |
| T1 |  | s | 1, 2 | 5 |  |
| T2 |  | s | 1, 2 | ≥Tidentify_irat_cca_without_index | Tidentify_irat_cca_without_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.10.4.4.1.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.10.4.4.1.1-4NOTE 3: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 4: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.4.4.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.10.4.4.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 2 |  | 3 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 6,8 |  | 1, 2 | 1 |  | 1 |  |
| PCCA_UL for semi-static channel access Note 7,8 |  | 1, 2 | 1 |  | 1 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | NA |  | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot]Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -58.49 | -58.49 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

##### A.10.4.4.1.2 Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index. Tidentify_irat_cca_without_index is defined in defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.4.2 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

##### A.10.4.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.2.1-1, A.10.4.4.2.1-2, A.10.4.4.2.1-3 and A.10.4.4.2.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.10.4.4.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.4.4.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  |  | 1, 2 | 1 |  | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  |  | 1, 2 | 1,2 |  | Two FR1 NR carrier frequency under CCA is used. |
| Active cell |  |  | 1, 2 | E-UTRA cell 1 (PCell) and NR cell 2 with CCA (PSCell) |  | E-UTRA cell 1 is on E-UTRA RF channel number 1. |
| DL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.1 |  |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |  |
| UL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.2 |  |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |  |
| LCCA_DL |  |  | 1, 2 | 12 | 5 |  |
| WCCA_DL |  | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |  |
| Neighbour cell |  |  | 1, 2 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2. |
| Gap Pattern Id |  |  | 1, 2 | 0 |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  |  | 1, 2 | 39 |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 |  | dBm | 1, 2 | Note 1 |  | E-UTRA RSRP threshold for measurement on cell 1 for event B2 [16] |
| b2-Threshold2NR |  | dBm | 1, 2 | Note 2 |  | SS-RSRP threshold measurement on cell 3 for event B2 [16] |
| Hysteresis |  | dB | 1, 2 | 0 |  |  |
| CP length |  |  | 1, 2 | Normal |  |  |
| TimeToTrigger |  | s | 1, 2 | 0 |  |  |
| Filter coefficient |  |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  |  | 1, 2 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  |  | 1, 2 | 3s |  | Synchronous cells. |
| T1 |  | s | 1, 2 | 5 |  |  |
| T2 |  | s | 1, 2 | ≥Tidentify_irat_cca_without_index |  | Tidentify_irat_cca_without_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.10.4.4.1.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.10.4.4.1.1-4NOTE 3: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 4: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

Table A.10.4.4.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.10.4.4.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 2 |  | 3 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 6,8 |  | 1, 2 | 1 |  | 1 |  |
| PCCA_UL for semi-static channel access Note 7,8 |  | 1, 2 | 1 |  | 1 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | NA |  | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot]Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -58.49 | -58.49 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8:  For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

##### A.10.4.4.2.2 Test Requirements

In test, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.4.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

##### A.10.4.4.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.3.1-1, A.10.4.4.3.1-2, A.10.4.4.3.1-3 and A.10.4.4.3.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In test 1 measurement gap pattern configuration # 0 as defined in table A.10.4.4.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.3.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.4.4.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| E-UTRA RF Channel Number |  |  | 1, 2 | 1 | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  |  | 1, 2 | 1,2 | Two FR1 NR carrier frequency under CCA is used. |
| DL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |
| UL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |
| LCCA_DL |  |  | 1, 2 | 12 |  |
| WCCA_DL |  | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |
| Active cell |  |  | 1, 2 | E-UTRA cell 1 (PCell) and NR cell 2 with CCA (PSCell) | E-UTRA cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  |  | 1, 2 | NR cell 3 | NR cell 3 is on NR RF channel number 2. |
| Gap Pattern Id |  |  | 1, 2 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  |  | 1, 2 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 |  | dBm | 1, 2 | Note 1 | E-UTRA RSRP threshold for measurement on cell 1 for event B2 [16] |
| b2-Threshold2NR |  | dBm | 1, 2 | Note 2 | SS-RSRP threshold measurement on cell 3 for event B2 [16] |
| Hysteresis |  | dB | 1, 2 | 0 |  |
| CP length |  |  | 1, 2 | Normal |  |
| TimeToTrigger |  | s | 1, 2 | 0 |  |
| Filter coefficient |  |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  |  | 1, 2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  |  | 1, 2 | 3s | Synchronous cells. |
| T1 |  | s | 1, 2 | 5 |  |
| T2 |  | s | 1, 2 | ≥ Tidentify_irat_cca_with_index | Tidentify_irat_cca_with_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.10.4.4.3.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.10.4.4.3.1-4NOTE 3: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 4: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.4.4.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.10.4.4.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 2 |  | 3 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 6,8 |  | 1, 2 | 1 |  | 1 |  |
| PCCA_UL for semi-static channel access Note 7,8 |  | 1, 2 | 1 |  | 1 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | NA |  | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot]Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -58.49 | -58.49 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

##### A.10.4.4.3.2 Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.10.4.4.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

##### A.10.4.4.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are three cells: LTE cell 1 as PCell on E-UTRA RF channel 1, NR cell 2 as PSCell in FR1 with CCA on NR RF channel 1 and NR cell 3 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.10.4.4.4.1-1, A.10.4.4.4.1-2, A.10.4.4.4.1-3 and A.10.4.4.4.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.10.4.4.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 3.

Table A.10.4.4.4.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.10.4.4.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter |  | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  |  | 1, 2 | 1 |  | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  |  | 1, 2 | 1,2 |  | Two FR1 NR carrier frequency under CCA is used. |
| DL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.1 |  |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |  |
| UL CCA model | Dynamic channel accessNote 3, 5 |  |  | As specified in clause A.3.26.2.2 |  |  |
|  | Semi-static channel access Note 4, 5 |  |  |  |  |  |
| LCCA_DL |  |  | 1, 2 | 12 |  | 5 |
| WCCA_DL |  | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |  |
| Active cell |  |  | 1, 2 | E-UTRA cell 1 (PCell) and NR cell 2 with CCA (PSCell) |  | E-UTRA cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  |  | 1, 2 | NR cell 3 |  | NR cell 3 is on NR RF channel number 2. |
| Gap Pattern Id |  |  | 1, 2 | 0 |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  |  | 1, 2 | 39 |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 |  | dBm | 1, 2 | Note 1 |  | E-UTRA RSRP/RSRQ/SINR threshold for E-UTRA RSRP measurement on cell 1 for event B2 [16] |
| b2-Threshold2NR |  | dBm | 1, 2 | Note 2 |  | SS-RSRP/ SS-RSRQ/ SS-SINR threshold measurement on cell 3 for event B2 [16] |
| Hysteresis |  | dB | 1, 2 | 0 |  |  |
| CP length |  |  | 1, 2 | Normal |  |  |
| TimeToTrigger |  | s | 1, 2 | 0 |  |  |
| Filter coefficient |  |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  |  | 1, 2 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  |  | 1, 2 | 3s |  | Synchronous cells. |
| T1 |  | s | 1, 2 | 5 |  |  |
| T2 |  | s | 1, 2 | ≥Tidentify_irat_cca_with_index |  | Tidentify_irat_cca_with_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.10.4.4.4.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.10.4.4.4.1-4NOTE 3: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 4: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

Table A.10.4.4.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.10.4.4.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 2 |  | 3 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 6,8 |  | 1, 2 | 1 |  | 1 |  |
| PCCA_UL for semi-static channel access Note 7,8 |  | 1, 2 | 1 |  | 1 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | NA |  | -98 |  |
|  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot]Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 4 | 4 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -58.49 | -58.49 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows. |  |  |  |  |  |  |

##### A.10.4.4.4.2 Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.10.5 Measurement performance

### A.10.5.1 SS-RSRP

#### A.10.5.1.1 Intra-frequency measurement accuracy on a CCA serving cell

##### A.10.5.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.36.1.1 and 10.1.36.1.2 when the serving cell is subject to CCA.

##### A.10.5.1.1.2 Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. Supported test configurations are shown in table A.10.5.1.1.1-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.10.5.1.1.1-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell, and Cell 3 is the target cell.

Table A.10.5.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations for each supported band |  |

Table A.10.5.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| Physical cell ID |  |  |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  |  |  |
| Duplex mode |  | Config 1, 2 |  | TDD |  |  |  |
| TDD configuration |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1, 2 | MHz | 40: NPRB,c = 106 |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  | Config 1, 2 |  | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Control Channel RMC |  | Config 1, 2 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |  |  |  |
| PCCA_DL for dynamic channel access Note 7,8 |  | Config 1, 2 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 | PCCA_DL_1=0.75PCCA_DL_2=0.75 | PCCA_DL_1=0.75PCCA_DL_2=0.75 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |
| PCCA_DL for semi-static channel access Note 6.8 |  | Config 1, 2 |  | PCCA_DL=0.9375 | PCCA_DL=0.9375 | PCCA_DL=0.9375 | PCCA_DL=0.9375 |
| PCCA_UL |  | Config 1, 2 |  | 1 | 1 | 1 | 1 |
| SSB configuration | Semi-static channel access | Config 1, 2 |  | SSB.1 CCA  (As defined in A.3.10A ) | SSB.1 CCA  (As defined in A.3.10A ) | SSB.1 CCA  (As defined in A.3.10A ) | SSB.1 CCA  (As defined in A.3.10A ) |
|  | Dynamic channel access |  |  | SSB.2 CCA  (As defined in A.3.10A ) | SSB.2 CCA  (As defined in A.3.10A ) | SSB.2 CCA  (As defined in A.3.10A ) | SSB.2 CCA  (As defined in A.3.10A ) |
| Time offset with Cell 2 |  | Config 1, 2 | s | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2 |  | SMTC.1 |  |  |  |
| DBT Window Configuration |  | Config 1, 2 |  | As defined in A.3.28.1 |  |  |  |
| DL CCA model |  | Config 1, 2 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1, 2 |  | As specified in clause A.3.26.2.2 |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 30 kHz |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | NR_CCA_FR1_I | dBm/15KhZ | -94 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -109.5 |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | NR_CCA_FR1_I | dBm/SCS | -91 |  | -107.0 |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -106.5 |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 2.46 | -5.97 | -2.01 | -3.54 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 1 | 1 | 0 |
| SS-RSRPNote3 | Config 1, 2 | NR_CCA_FR1_I | dBm/SCS | -85 | -90 | -106.00 | -107.00 |
|  |  | NR_CCA_FR1_J |  |  |  | -105.50 | -106.50 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| IoNote3 | Config 1, 2 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.99 |  | -70.82 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -70.32 |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

##### A.10.5.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for cell 2 and cell 3 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.36.1.1 and 10.1.36.1.2.

#### A.10.5.1.2 Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

##### A.10.5.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.37.1.1 and 10.1.37.1.2 for inter-frequency measurements with the testing configurations in table A.10.5.1.2.1-1.

Table A.10.5.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations on each supported band |  |

##### A.10.5.1.2.2 Test parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7A.2.1. The test parameters for the Cell 2 and Cell 3 are given in table A.10.5.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.10.5.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.10.5.1.2.2-1: SS-RSRP inter-frequency test parameters

| Parameter |  | Config | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| SSB ARFCN |  | 1, 2 |  | freq1 | freq2 | freq1 | freq2 |
| BWchannel |  | 1, 2 | MHz | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| Gap pattern ID |  |  |  | 0 |  | 0 |  |
| Duplex mode |  | 1, 2 |  | TDD |  | TDD |  |
| TDD configuration |  | 1, 2 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| PDSCH Reference measurement channel |  | 1, 2 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | 1, 2 |  | CR.1.1 CCA | - | CR.1.1 CCA | - |
| Dedicated CORESET Reference Channel |  | 1, 2 |  | CCR.1.1 CCA | - | CCR.1.1 CCA | - |
| SSB configuration | Semi-static channel access | 1, 2 |  | SSB.1 CCA  (As defined in A.3.10A ) |  | SSB.1 CCA  (As defined in A.3.10A ) |  |
|  | Dynamic channel access |  |  | SSB.2 CCA  (As defined in A.3.10A ) |  | SSB.2 CCA  (As defined in A.3.10A ) |  |
| OCNG Patterns |  | 1, 2 |  | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| Initial BWP Configuration |  | 1, 2 |  | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP configuration |  | 1, 2 |  | DLBWP.1.1ULBWP.1.1 |  | DLBWP.1.1ULBWP.1.1 |  |
| Time offset with Cell 2 |  | 1, 2 | s | - | 3 | - | 3 |
| SMTC configuration |  | 1, 2 |  | SMTC.1 |  | SMTC.1 |  |
| DBT Window Configuration |  | 1, 2 |  | DBT.1(As defined in A.3.28.1) |  | DBT.1(As defined in A.3.28.1) |  |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | 1, 2 | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |
| Note2 | NR_CCA_FR1_I | 1, 2 | dBm/15 kHz | -94.65 |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for Cell 3 +8 dB) | -111 |
|  | NR_CCA_FR1_J |  |  |  |  |  | -110.5 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| Note2 | NR_CCA_FR1_I | 1, 2 | dBm/SSB SCS | -91.65 |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for C 3 +8 dB) | -109.00 |
|  | NR_CCA_FR1_J |  |  |  |  |  | -108.50 |
|  |  | 1, 2 | dB | 10 | 10 | 13 | -3 |
| SS-RSRPNote3 | NR_CCA_FR1_I | 1, 2 | dBm/SCS | -81.65 |  | (RSRP for Cell 3 +24 dB) | -111.00 |
|  | NR_CCA_FR1_J |  |  |  |  |  | -110.50 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| IoNote3 | R_CCA_FR1_I | 1, 2 | dBm/38.16 MHz | -50.19 |  | (Io for Channel 3 +19.45 dB) | -75.19 |
|  | NR_CCA_FR1_J |  |  |  |  |  | -74.69 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  | 1, 2 | dB | 10 | 10 | 13 | -3 |
| Propagation condition |  | 1, 2 | - | AWGN |  | AWGN |  |
| Antenna configuration |  |  |  | 1x2 |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. NOTE 5: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.10.5.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil the Absolute requirement in clause 10.1.4.1.1 and Relative requirement in clause 10.1.37.1.1 and 10.1.37.1.2.

### A.10.5.2 SS-RSRQ

#### A.10.5.2.1 Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

##### A.10.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

##### A.10.5.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.10.5.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.10.5.2.1.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell and Cell 3 is the target cell.

Table A.10.5.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

Table A.10.5.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  |  | Unit | Test 1 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| SSB ARFCN |  |  |  |  | freq1 |  |  |  |
| Duplex mode |  | Config 1, 2 |  |  | TDD |  |  |  |
| TDD configuration |  | Config 1, 2 |  |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1, 2 |  | MHz | 40: NPRB,c = 106 |  |  |  |
| BWP configuration |  | Initial DL BWP |  |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle |  |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Control Channel RMC |  | Config 1, 2 |  |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS configuration |  | Config 1, 2 |  |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  |  | OP. 1 |  |  |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |  |  |
| Time offset with Cell 2 |  | Config 1, 2 |  | s | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2 |  |  | SMTC.1 |  |  |  |
| SSB configuration |  | Semi-static channel access | Config 1, 2 |  | SSB.1 CCA  (As defined in A.3.10A ) |  |  |  |
|  |  | Dynamic channel access |  |  | SSB.2 CCA  (As defined in A.3.10A ) |  |  |  |
| PDSCH/PDCCH |  | Config 1, 2 |  | kHz | 30 kHz |  |  |  |
| subcarrier spacing |  |  |  |  |  |  |  |  |
| DBT Window Configuration |  | Config 1, 2 |  |  | DBT.1(As defined in A.3.28.1) |  |  |  |
| DL CCA model |  | Config 1, 2 |  |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1, 2 |  |  | As specified in clause A.3.26.2.2 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config1, 2 | NR_CCA_FR1_I |  | Bm/15 kHz | -91 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  | -109.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | NR_CCA_FR1_I |  | dBm/SC S | -88 |  | -107 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  | -106.5 |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | -1.76 |  | -5.46 | -5.46 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | 3 | 3 | -4 | -4 |
| SS-RSRPNote3 | Config 1, 2 | NR_CCA_FR1_I |  | dBm/SCS | -85 | -85 | -111 | -111 |
|  |  | NR_CCA_FR1_J |  |  |  |  | -110.5 | -110.5 |
| SS-RSRQ Note3 |  | NR_CCA_FR1_I |  | dB | -14.77 | -14.77 | -17.34 | -17.34 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| IoNote3 | Config 1, 2 | NR_CCA_FR1_I |  | dBm/38.16 MHz | -50 |  |  | -73.4 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -72.9 |
| Propagation condition |  |  |  | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.10.5.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

#### A.10.5.2.2 Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell

##### A.10.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limitsThis test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2 for inter-frequency measurements with the testing configurations in table A.10.5.2.2.2-1.

##### A.10.5.2.2.2 Test Parameters

In this set of test cases there are three cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on a different frequency than the PSCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 2 and Cell 3 are given in table A.4.7.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.10.5.2.2.2-2. The inter-frequency measurements are supported by a measurement gap.

Table A.10.5.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

Table A.10.5.2.2.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |
| Duplex mode |  | Config 1, 2 |  | TDD |  |  |  |
| TDD configuration |  | Config 1, 2 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1, 2 |  | 40: NRB,c = 106 |  |  |  |
| BWP BW |  | Config 1, 2 | MHz | 40: NRB,c = 106 |  |  |  |
| Gap pattern ID |  |  |  | 0 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS configuration |  | Config 1, 2 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |
| Time offset with Cell 2 |  | Config 1, 2 | s | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2 |  | SMTC.1 |  |  |  |
| SSB configuration | Semi-static channel access | Config 1, 2 |  | SSB.1 CCA (As defined in A.3.10A) |  |  |  |
|  | Dynamic channel access |  |  | SSB.2 CCA (As defined in A.3.10A) |  |  |  |
| DBT Window Configuration |  | Config 1, 2 |  | DBT.1(As defined in A.3.28.1) |  |  |  |
| DL CCA model |  | Config 1, 2 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1, 2 |  | As specified in clause A.3.26.2.2 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 30 kHz |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | NR_CCA_FR1_I | dBm/15kHz | -86.27 | -86.27 | -112 | -112 |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 | -111.5 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | NR_CCA_FR1_I | dBm/SCS | -83.27 | -83.27 | -109 | -109 |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 | -108.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 | -1.75 | 3 | -1.75 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 | -1.75 | 3 | -1.75 |
| SS-RSRPNote3 | Config 1, 2 | NR_CCA_FR1_I | dBm/SCS | -85.02 | -85.02 | -106 | -110.75 |
|  |  | NR_CCA_FR1_J |  |  |  | -105.5 | -110.25 |
| SS-RSRQ Note3 |  | NR_CCA_FR1_I | dB | -14.77 | -14.77 | -12.56 | -14.76 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
| IoNote3 | Config 1, 2 | NR_CCA_FR1_I | dBm/38.16MHz | -50 | -50 | -73.19 | -75.23 |
|  |  | NR_CCA_FR1_J |  |  |  | -72.69 | -74.73 |
| Propagation condition |  |  |  | AWGN | AWGN | AWGN | AWGN |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in Section 3.5.2.Note 6:      For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.10.5.2.2.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

### A.10.5.3 SS-SINR

#### A.10.5.3.1 Intra-frequency measurement accuracy on PSCC

##### A.10.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.

##### A.10.5.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.10.5.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.10.5.3.1.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell with CCA and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 2 and 3.

Table A.10.5.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.5.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |
| DL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.2 |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1,2 |  | TDD |  |  |  |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |
| TRS Configuration |  | Config 1,2 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 CCA |  | SR1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| Time offset with Cell 2 |  | Config 1,2 | s | - | 3 | - | 3 |
| DBT Window Configuration |  | Config 1,2 |  | DBT.1 |  |  |  |
| SSB configuration |  | Config 1,2 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -93 |  | -112 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | NR_CCA_FR1_I | dBm/SCS | -90 |  | -109 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 | -4 |
| SS-RSRPNote3 | Config 1,2 | NR_CCA_FR1_I | dBm/SCS | -85.46 | -87.34 | -113 | -113 |
|  |  | NR_CCA_FR1_J |  |  |  | -112.5 | -112.5 |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | 0 | -3.19 | -5.46 | -5.46 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
| IoNote3 | Config 1,2 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.41 |  | -75.41 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -74.91 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.10.5.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

#### A.10.5.3.2 Inter-frequency measurement accuracy on PSCC

##### A.10.5.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.32.1.1 and 10.1.32.1.2 for inter-frequency measurement.

##### A.10.5.3.2.2 Test Parameters

In this test case the two NR cells (i.e., Cell 2 and Cell 3) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.10.5.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.10.5.3.2.2-2. In all test cases, Cell 2 is the PSCell with CCA and Cell 3 is target cell with CCA. Cell 1 is the E-UTRA cell of which specific test parameters for this test case are specified in table A.3.7A.2.1-1. Three sub-tests (Test 1, Test 2 and Test 3) are provided different Noc on Cells 2 and 3.

Table A.10.5.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.5.3.2.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 | Cell 2 | Cell 3 |  |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 | freq1 | freq2 |  |
| DL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.1 |  |  |  |  |  |  |
| UL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.2 |  |  |  |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - | 1.0 |  | - |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - | 0.9375 |  | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - | 0.75 |  | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - | 0.75 |  | - |
| Duplex mode |  | Config 1,2 |  | TDD |  |  |  |  |  |  |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |  |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |  |  |  |
| Gap pattern ID |  |  |  | 0 | - | 0 | - | 0 | - |  |
| TRS configuration |  | Config 1,2 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 CCA |  | SR.1.1 CCA |  | SR.1.1 CCA |  |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 CCA |  | CR.1.1 CCA |  | CR.1.1 CCA |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |  |  |
| Time offset with Cell 2 |  | Config 1,2 | s | - | 3 | - | 3 | - |  | 3 |
| DBT Window configuration |  | Config 1,2 |  | DBT.1 |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |  |  |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 30 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -88 |  | -108.5 |  | -115.5 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -116 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | NR_CCA_FR1_I | dBm/SCS | -85 |  | -105.5 |  | -112.5 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -113 |  |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |  |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |  |
| SS-RSRPNote3 | Config 1,2 | NR_CCA_FR1_I |  | -86.75 |  | -85.5 |  | -116.5 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -116 |  |  |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | -1.75 |  | 20 |  | -4.0 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |  |  |
| IoNote3 | Config 1,2 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.73 |  | -54.41 |  | -80 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -79.5 |  |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurationNOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |  |

##### A.10.5.3.2.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

#### A.10.5.3.3 Intra-frequency measurement accuracy on SCC

##### A.10.5.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.

##### A.10.5.3.3.2 Test Parameters

In this test case, Cell 2 (PSCell) is on frequency 1 while Cell 3 (SCell) and Cell 4 (target cell) which are intra-frequency neighbors, are on frequency 2. Supported test configuration are shown in table A.10.5.3.3.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.10.5.3.3.2-2. The configuration of cell 1 (E-UTRA PCell) is specified in clause A.3.7A.2.1. In all test cases, Cell 2 is the PSCell with CCA, Cell 3 is the SCell with CCA, and Cell 4 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 2, 3 and 4.

Table A.10.5.3.3.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | LTE FDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDNR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.10.5.3.3.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 / Cell 3 | Cell 4 | Cell 2 / Cell 3 |  | Cell 4 |
| SSB ARFCN |  |  |  | freq1 for Cell 2freq2 for Cell 3 | freq2 | freq1 for Cell 2freq2 for Cell 3 |  | freq2 |
| DL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.1 |  |  |  |  |
| UL CCA model |  | Config 1,2 |  | As specified in clause A.3.26.2.2 |  |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |  |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |  |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |  |
| Duplex mode |  | Config 1,2 |  | TDD |  |  |  |  |
| TDD configuration |  | Config 1,2 |  | TDDConf.1.1 CCA |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |  |
| TRS Configuration |  | Config 1,2 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 CCA |  | SR1.1 CCA |  |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |
| Time offset with Cell 2 |  | Config 1,2 | s | 3 (for Cell 3) | 3 | 3 (for Cell 3) |  | 3 |
| DBT Window Configuration |  | Config 1,2 |  | DBT.1 |  |  |  |  |
| SSB configuration |  | Config 1,2 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 30 |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -93 |  | -112 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | NR_CCA_FR1_I | dBm/SCS | -90 |  | -109 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |  |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 |  | -5.46 |
| ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 |  | -4 |
| SS-RSRPNote3 | Config 1,2 | NR_CCA_FR1_I | dBm/SCS | -85.46 | -87.34 | -113 |  | -113 |
|  |  | NR_CCA_FR1_J |  |  |  | -112.5 |  | -112.5 |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | 0 | -3.19 | -5.46 |  | -5.46 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |
| IoNote3 | Config 1,2 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.41 |  | -75.41 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -74.91 |  |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurationNOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.10.5.3.3.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

### A.10.5.4 L1-RSRP measurement for beam reporting with CCA serving cell

#### A.10.5.4.1 SSB based L1-RSRP measurement

##### A.10.5.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.10.5.4.1.1-1.

Table A.10.5.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | LTE FDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to pass in one of the supported test configurations |  |

##### A.10.5.4.1.2 Test parameters

In this set of test cases there are two cells in the test, E-UTRAN PCell (Cell 1), FR1 PSCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 2. The test parameters and applicability for Cell 1 are defined in A.3.7A.2. The test parameters for the Cell 2 are given in table A.10.5.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.10.5.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.10.5.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB GSCN |  | 1,2 |  | freq1 | freq1 |
| DL CCA model |  | 1,2 |  | As specifieed in A.3.26.2.1 | As specifieed in A.3.26.2.1 |
| UL CCA model |  | 1,2 |  | As specified in A.3.26.2.2 | As specified in A.3.26.2.2 |
| Duplex mode |  | 1,2 |  | TDD | TDD |
| TDD Configuration |  | 1,2 |  | TDDConf.1.1 CCA | TDDConf.1.1 CCA |
| BWchannel |  | 1,2 | MHz | 40: NPRB,c = 106 | 40: NPRB,c = 106 |
| Duplex mode |  | 1,2 |  | TDD | TDD |
| TDD configuration |  | 1,2 |  | TDDConf.1.1 CCA | TDDConf.1.1 CCA |
| PDSCH Reference measurement channel |  | 1,2 |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  | 1,2 |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  | 1,2 |  | CCR.1.1 CCA | CCR.1.1 CCA |
| SSB configuration for Semi-static channel access |  | 1,2 |  | SSB.3 CCA | SSB.3 CCA |
| SSB configuration for Dynamic channel access |  | 1,2 |  | SSB.4 CCA | SSB.4 CCA |
| OCNG Patterns |  | 1,2 |  | OP.1 | OP.1 |
| TRS configuration |  | 1,2 |  | TRS.1.2 TDD | TRS.1.2 TDD |
| Initial BWP Configuration |  | 1,2 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration |  | 1,2 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration |  | 1,2 |  | DBT.1 | DBT.1 |
| reportConfigType |  | 1,2 |  | periodic | periodic |
| reportQuantity |  | 1,2 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS |  | 1,2 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1,2 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1,2 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  | 1,2 |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_TDD_FR1_I | 1,2 | dBm/15 kHz | -94.65 | -113 |
| Note2 | NR_TDD_FR1_I | 1,2 | dBm/SCS | -91.65 | -110 |
|  |  | 1,2 | dB | 10 | -3 |
| SS-RSRPNote3 | NR_TDD_FR1_I | 1,2 | dBm/SCS | -81.65 | -113 |
| IoNote3 | NR_TDD_FR1_I | 1,2 | dBm/38.16 MHz | -50.19 | -77.19 |
|  |  | 1,2 | dB | 10 | -3 |
| Propagation condition |  | 1,2 |  | AWGN | AWGN |
| Antenna configuration |  | 1,2 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The test configuration excludes support for band n51 and it is not required to run this test on band n51 in this release of the specification |  |  |  |  |  |

##### A.10.5.4.1.3 Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.33.1.

### A.10.5.5 RSSI

#### A.10.5.5.1  RSSI measurement accuracy on PSCC with CCA

##### A.10.5.5.1.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

##### A.10.5.5.1.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, and Cell 2 is PSCell operating on a carrier frequency under CCA. RSSI is measured on channel number 1. Supported test configurations are shown in table A.10.5.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.10.5.5.1.2-2 and A.10.5.5.1.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.1.2-1: RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.5.1.2-2: RSSI test parameters

| Parameter |  | Configurations | Unit | Test 1 |
| --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  |  | MHz | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA |
| PCCA_DL |  |  |  | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |
| Channel access bandwidth |  |  | MHz | 20 |
| DRX Cycle configuration |  |  | ms | Not Applicable |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -58.96 |
| Propagation condition |  |  | - | AWGN |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.10.5.5.1.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.5.1.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

#### A.10.5.5.2 RSSI measurement accuracy on SCC with CCA

##### A.10.5.5.2.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

##### A.10.5.5.2.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, Cell 3 is SCell on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.10.5.5.2.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.10.5.5.2.2-2 and A.10.5.5.2.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.2.2-1: RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.5.2.2-2: RSSI test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.5.5.2.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.5.2.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

#### A.10.5.5.3  Inter-frequency RSSI measurement accuracy on a carrier with CCA

##### A.10.5.5.3.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

##### A.10.5.5.3.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, and Cell 3 is the neighbour with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.10.5.5.3.2-1. The accuracy of RSSI inter-frequency measurements is tested by using the parameters in A.10.5.5.3.2-2 and A.10.5.5.3.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.5.3.2-1: RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.5.3.2-2: RSSI test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 TDD | NA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 TDD | NA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 TDD | NA |
| OCNG Patterns |  |  |  | OP.1 | NA |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | NA |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.5.5.3.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.5.3.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

### A.10.5.6 Channel occupancy

#### A.10.5.6.1  Channel occupancy measurement accuracy on PSCC with CCA

##### A.10.5.6.1.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

##### A.10.5.6.1.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, and Cell 2 is PSCell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 1. Supported test configurations are shown in table A.10.5.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.10.5.6.1.2-2 and A.10.5.6.1.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.1.2-1: CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.6.1.2-2: CO test parameters

| Parameter |  | Configurations | Unit | Test 1 |
| --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  |  | MHz | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA |
| PCCA_DL |  |  |  | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |
| Channel access bandwidth |  |  | MHz | 20 |
| DRX Cycle configuration |  |  | ms | Not Applicable |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -58.96 |
| Propagation condition |  |  | - | AWGN |
| channelOccupancyThreshold |  |  | dBm | -83 |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.10.5.6.1.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.6.1.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

#### A.10.5.6.2  Channel occupancy measurement accuracy on SCC with CCA

##### A.10.5.6.2.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

##### A.10.5.6.2.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, Cell 3 is SCell on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.10.5.6.2.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.10.5.6.2.2-2 and A.10.5.6.2.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.2.2-1: CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.6.2.2-2: CO test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.5.6.2.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.6.2.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

#### A.10.5.6.3  Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

##### A.10.5.6.3.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

##### A.10.5.6.3.2 Test parameters

In all test cases, Cell 1 is E-UTRAN PCell on a licensed band, Cell 2 is PSCell operating on a carrier frequency under CCA, and Cell 3 is the neighbour with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.10.5.6.3.2-1. The accuracy of channel occupancy inter-frequency measurements is tested by using the parameters in A.10.5.6.3.2-2 and A.10.5.6.3.2-3. The E-UTRAN PCell setting refers to Table A.3.7.2.1-1.

Table A.10.5.6.3.2-1: CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| 2 | LTE TDD; NR: TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations above. |  |

Table A.10.5.5.3.2-2: CO test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image14.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 TDD | NA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 TDD | NA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 TDD | NA |
| OCNG Patterns |  |  |  | OP.1 | NA |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | NA |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.10.5.6.3.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.10.5.6.3.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.
