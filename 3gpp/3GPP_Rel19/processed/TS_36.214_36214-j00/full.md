| 3GPP TS 36.214 V19.0.0 (2025-09) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;Evolved Universal Terrestrial Radio Access (E-UTRA);Physical layer;Measurements (Release 19) |  |
|  |  |
| ![](media/image1.emf) |  |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 5

1 Scope 6

2 References 6

3 Definitions, symbols and abbreviations 7

3.1 Definitions 7

3.2 Symbols 7

3.3 Abbreviations 7

4 Control of UE/E-UTRAN measurements 7

5 Measurement capabilities for E-UTRA 8

5.1 UE measurement capabilities 8

5.1.1 Reference Signal Received Power (RSRP) 9

5.1.2 Void 9

5.1.3 Reference Signal Received Quality (RSRQ) 10

5.1.4 UTRA FDD CPICH RSCP 10

5.1.5 UTRA FDD carrier RSSI 10

5.1.6 UTRA FDD CPICH Ec/No 11

5.1.7 GSM carrier RSSI 11

5.1.8 Void 11

5.1.9 UTRA TDD P-CCPCH RSCP 11

5.1.10 CDMA2000 1x RTT Pilot Strength 11

5.1.11 CDMA2000 HRPD Pilot Strength 11

5.1.12 Reference signal time difference (RSTD) 12

5.1.13 UE GNSS Timing of Cell Frames for UE positioning 12

5.1.14 UE GNSS code measurements 12

5.1.14A UE GNSS carrier phase measurements 12

5.1.15 UE Rx – Tx time difference 13

5.1.16 IEEE 802.11 WLAN RSSI 13

5.1.17 MBSFN Reference Signal Received Power (MBSFN RSRP) 13

5.1.18 MBSFN Reference Signal Received Quality (MBSFN RSRQ) 14

5.1.19 Multicast Channel Block Error Rate (MCH BLER) 14

5.1.20 CSI Reference Signal Received Power (CSI-RSRP) 14

5.1.21 Sidelink Reference Signal Received Power (S-RSRP) 15

5.1.22 Sidelink Discovery Reference Signal Received Power (SD-RSRP) 15

5.1.23 Reference signal-signal to noise and interference ratio (RS-SINR) 16

5.1.24 Received Signal Strength Indicator (RSSI) 16

5.1.25 SFN and subframe timing difference (SSTD) 17

5.1.26 Narrowband Reference Signal Received Power (NRSRP) 17

5.1.27 Narrowband Reference Signal Received Quality (NRSRQ) 18

5.1.28 Sidelink Received Signal Strength Indicator (S-RSSI) 18

5.1.29 PSSCH Reference Signal Received Power (PSSCH-RSRP) 18

5.1.30 Channel busy ratio (CBR) 19

5.1.31 Channel occupancy ratio (CR) 19

5.1.32 NR SS reference signal received power (NR-SS-RSRP) 20

5.1.33 NR SS reference signal received quality (NR-SS-RSRQ) 21

5.1.34 SFN and frame timing difference (SFTD) 22

5.1.35 NR SS signal-to-noise and interference ratio (NR-SS-SINR) 22

5.2 E-UTRAN measurement abilities 22

5.2.1 DL RS TX power 23

5.2.2 Received Interference Power 23

5.2.3 Thermal noise power 23

5.2.4 Timing advance (TADV) 23

5.2.5 eNB Rx – Tx time difference 24

5.2.6 E-UTRAN GNSS Timing of Cell Frames for UE positioning 24

5.2.7 Angle of Arrival (AoA) 24

5.2.8 UL Relative Time of Arrival (TUL-RTOA) 24

Annex A (informative): Change history 25

# Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

## 1 presented to TSG for information;

## 2 presented to TSG for approval;

## 3 or greater indicates TSG approved document under change control.

Y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.

# 1 Scope

The present document contains the description and definition of the measurements done at the UE and network in order to support operation in idle mode and connected mode.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TS 36.201: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description ".

[3] 3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[4] 3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding ".

[5] 3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures ".

[6] 3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[7] 3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification ".

[8] 3GPP2 CS.0005-D v1.0 "Upper Layer (Layer 3) Signaling Standard for CDMA2000 Spread Spectrum Systems Release D".

[9] 3GPP2 CS.0024-A v3.0 "cdma2000 High Rate Packet Data Air Interface Specification"

[10] 3GPP TS 36.104: "Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception ".

[11] 3GPP TS 36.355: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol (LPP)"

[12] 3GPP TS 36.455: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol A (LPPa)"

[13] 3GPP TS 36.459: "Evolved Universal Terrestrial Radio Access (E-UTRA); SLm Application Protocol (SLmAP)"

[14] 3GPP TS 36.111: "Evolved Universal Terrestrial Radio Access (E-UTRA); Location Measurement Unit (LMU) performance specification; Network Based Positioning Systems in E-UTRAN"

[15] IEEE 802.11, Part 11: "Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) specifications, IEEE Std.".

[16] 3GPP TS 36.304: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode ".

[17] 3GPP TS 38.213: "NR; Physical layer procedures for control".

[18] 3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[19] 3GPP TS 37.105: "Active Antenna System (AAS) Base Station (BS) transmission and reception".

[20] 3GPP TS 36.108: "Evolved Universal Terrestrial Radio Access (E-UTRA); Satellite Access Node radio transmission and reception".

# 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR21.905[1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR21.905[1].

## 3.2 Symbols

For the purposes of the present document, the following symbols apply:

Ec/No Received energy per chip divided by the power density in the band

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

1x RTT CDMA2000 1x Radio Transmission Technology

CPICH Common Pilot Channel

E-SMLC Enhanced Serving  Location Centre

E-UTRA Evolved UTRA

E-UTRAN Evolved UTRAN

FDD Frequency Division Duplex

GNSS Global Navigation Satellite System

GSM Global System for  communication

HRPD CDMA2000 High Rate Packet Data

LMU Location Measurement Unit

NTN Non-Terrestrial Network

P-CCPCH Primary Common Control Physical Channel

RIB Radiated Interface Boundary

RSCP Received Signal Code Power

RSRP Reference Signal Received Power

RSRQ Reference Signal Received Quality

RSSI Received Signal Strength Indicator

RSTD Reference Signal Time Difference

SAN Satellite Access Node

SRS Sounding Reference Signal

TAB Transceiver Array Boundary

TDD Time Division Duplex

UTRA Universal Terrestrial Radio Access

UTRAN Universal Terrestrial Radio Access Network

# 4 Control of UE/E-UTRAN measurements

In this clause the general measurement control concept of the higher layers is briefly described to provide an understanding on how L1 measurements are initiated and controlled by higher layers.

With the measurement specifications L1 provides measurement capabilities for the UE and E-UTRAN. These measurements can be classified in different reported measurement types: intra-frequency, inter-frequency, inter-system, traffic volume, quality and UE internal measurements (see the RRC Protocol [7]).

In the L1 measurement definitions, see clause 5, the measurements are categorised as measurements in the UE (the messages for these will be described in the MAC Protocol [6] or RRC Protocol [7] or LPP Protocol [11]) or measurements in the E-UTRAN (the messages for these will be described in the Frame Protocol or LPPa Protocol [12]).

To initiate a specific measurement, the E-UTRAN transmits a 'RRC connection reconfiguration message' to the UE including a measurement ID and type, a command (setup, modify, release), the measurement objects, the measurement quantity, the reporting quantities and the reporting criteria (periodical/event-triggered), see [7] or E-SMLC transmits an 'LPP Request Location Information message' to UE, see [11].

When the reporting criteria are fulfilled the UE shall answer with a 'measurement report message' to the E-UTRAN including the measurement ID and the results or an 'LPP Provide Location Information message' to the E-SMLC, see [11].

For idle mode, the measurement information elements are broadcast in the System Information.

# 5 Measurement capabilities for E-UTRA

In this clause the physical layer measurements reported to higher layers are defined.

## 5.1 UE measurement capabilities

The structure of the table defining a UE measurement quantity is shown below.

| Column field | Comment |
| --- | --- |
| Definition | Contains the definition of the measurement. |
| Applicable for | States in which state(s) it shall be possible to perform this measurement. The following terms are used in the tables:RRC_IDLE;RRC_CONNECTED;Intra-frequency appended to the RRC state: Shall be possible to perform in the corresponding RRC state on an intra-frequency cell;Inter-frequency appended to the RRC state:Shall be possible to perform in the corresponding RRC state on an inter-frequency cellInter-RAT appended to the RRC state:Shall be possible to perform in the corresponding RRC state on an inter-RAT cell. |

### 5.1.1 Reference Signal Received Power (RSRP)

| Definition | Reference signal received power (RSRP), is defined as the linear average over the power contributions (in [W]) of the resource elements that carry cell-specific reference signals within the considered measurement frequency bandwidth.For RSRP determination the cell-specific reference signals R0 according to TS 36.211 [3] shall be used. If the UE can reliably detect that R1 is available, it may use R1 in addition to R0 to determine RSRP.If higher layers indicate measurements based on discovery signals, the UE shall measure RSRP in the subframes in the configured discovery signal occasions. For frame structure 1 and 2, if the UE can reliably detect that cell-specific reference signals are present in other subframes, the UE may use those subframes in addition to determine RSRP.If higher layers indicate measurements based on resynchronization signals (RSS), the UE shall measure RSRP on the resynchronization signal in the subframes in the configured resynchronization signal occasions. The reference point for the RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding RSRP of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

### 5.1.2 Void

### 5.1.3 Reference Signal Received Quality (RSRQ)

| Definition | Reference Signal Received Quality (RSRQ) is defined as the ratio N×RSRP/(E-UTRA carrier RSSI), where N is the number of RB's of the E-UTRA carrier RSSI measurement bandwidth. The measurements in the numerator and denominator shall be made over the same set of resource blocks.E-UTRA Carrier Received Signal Strength Indicator (RSSI), comprises the linear average of the total received power (in [W]) observed only in certain OFDM symbols of measurement subframes, in the measurement bandwidth, over N number of resource blocks by the UE from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc. Unless indicated otherwise by higher layers, RSSI is measured only from OFDM symbols containing reference symbols for antenna port 0 of measurement subframes. If higher layers indicate all OFDM symbols for performing RSRQ measurements, then RSSI is measured from all OFDM symbols of the DL part of measurement subframes. If higher-layers indicate certain subframes for performing RSRQ measurements, then RSSI is measured from all OFDM symbols of the DL part of the indicated subframes.If higher layers indicate measurements based on discovery signals, RSSI is measured from all OFDM symbols of the DL part of the subframes in the configured discovery signal occasions.The reference point for the RSRQ shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding RSRQ of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

### 5.1.4 UTRA FDD CPICH RSCP

| Definition | Received Signal Code Power, the received power on one code measured on the Primary CPICH. The reference point for the RSCP shall be the antenna connector of the UE. If Tx diversity is applied on the Primary CPICH the received code power from each antenna shall be separately measured and summed together in [W] to a total received code power on the Primary CPICH. If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding CPICH RSCP of any of the individual receive antenna branches. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.5 UTRA FDD carrier RSSI

| Definition | The received wide band power, including thermal noise and noise generated in the receiver, within the bandwidth defined by the receiver pulse shaping filter. The reference point for the measurement shall be the antenna connector of the UE. If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding UTRA carrier RSSI of any of the individual receive antenna branches. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

NOTE: This definition does not correspond to a reported measurement. This definition is just an intermediate definition used in the definition of UTRA FDD CPICH Ec/No.

### 5.1.6 UTRA FDD CPICH Ec/No

| Definition | The received energy per chip divided by the power density in the band. If receiver diversity is not in use by the UE, the CPICH Ec/No is identical to CPICH RSCP/UTRA Carrier RSSI. Measurement shall be performed on the Primary CPICH. The reference point for the CPICH Ec/No shall be the antenna connector of the UE. If Tx diversity is applied on the Primary CPICH the received energy per chip (Ec) from each antenna shall be separately measured and summed together in [Ws] to a total received chip energy per chip on the Primary CPICH, before calculating the Ec/No. If receiver diversity is in use by the UE, the measured CPICH Ec/No value shall not be lower than the corresponding CPICH RSCPi/UTRA Carrier RSSIi of receive antenna branch i . |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.7 GSM carrier RSSI

| Definition | Received Signal Strength Indicator, the wide-band received power within the relevant channel bandwidth. Measurement shall be performed on a GSM BCCH carrier. The reference point for the RSSI shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.8 Void

### 5.1.9 UTRA TDD P-CCPCH RSCP

| Definition | Received Signal Code Power, the received power on P-CCPCH of a neighbour UTRA TDD cell. The reference point for the RSCP shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.10 CDMA2000 1x RTT Pilot Strength

| Definition | CDMA2000 1x RTT Pilot Strength measurement is defined in clause 2.6.6.2.2 of [8] |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.11 CDMA2000 HRPD Pilot Strength

| Definition | CDMA2000 HRPD Pilot Strength Measurement is defined in clause 8.7.6.1.2.3 of [9] |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.12 Reference signal time difference (RSTD)

| Definition | The relative timing difference between the neighbour cell j and the reference cell i, defined as TSubframeRxj – TSubframeRxi, where: TSubframeRxj is the time when the UE receives the start of one subframe from cell j TSubframeRxi is the time when the UE receives the corresponding start of one subframe from cell i that is closest in time to the subframe received from cell j. The reference point for the observed subframe time difference shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency RRC_CONNECTED inter-frequencyRRC_IDLE intra-frequency only applicable for NB-IoT UEsRRC_IDLE inter-frequency only applicable for NB-IoT UEs |

### 5.1.13 UE GNSS Timing of Cell Frames for UE positioning

| Definition | The timing between cell j and a GNSS-specific reference time for a given GNSS (e.g., GPS/Galileo/Glonass system time). TUE-GNSS is defined as the time of occurrence of a specified E-UTRAN event according to GNSS time for a given GNSS Id. The specified E-UTRAN event is the beginning of a particular frame (identified through its SFN) in the first detected path (in time) of the cell-specific reference signals of the cell j, where cell j is a cell chosen by the UE. The reference point for TUE-GNSSj shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency |

### 5.1.14 UE GNSS code measurements

| Definition | The GNSS code phase (integer and fractional parts) of the spreading code of the ith GNSS satellite signal. The reference point for the GNSS code phase shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | Void (this measurement is not related to E-UTRAN/UTRAN/GSM signals; its applicability is therefore independent of the UE RRC state) |

### 5.1.14A UE GNSS carrier phase measurements

| Definition | The number of carrier-phase cycles (integer and fractional parts) of the ith GNSS satellite signal, measured since locking onto the signal. Also called Accumulated Delta Range (ADR). The reference point for the GNSS carrier phase shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | Void (this measurement is not related to E-UTRAN/UTRAN/GSM signals; its applicability is therefore independent of the UE RRC state) |

### 5.1.15 UE Rx – Tx time difference

| Definition | The UE Rx – Tx time difference is defined as TUE-RX – TUE-TXWhere:TUE-RX is the UE received timing of downlink radio frame #i from the serving cell, defined by the first detected path in time.TUE-TX is the UE transmit timing of uplink radio frame #i.The reference point for the UE Rx – Tx time difference measurement shall be the UE antenna connector. For a HD-FDD UE, if the UE does not receive any DL transmission in radio frame #i, it shall compensate for the difference in the received timing of radio frame #i and the radio frame in which it did receive a DL transmission used for TUE-RX estimation. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequencyNot applicable for NB-IoT UEs |

### 5.1.16 IEEE 802.11 WLAN RSSI

| Definition | The IEEE 802.11 WLAN RSSI as used in RRC specification [7] refers to RSSI as defined in IEEE 802.11 specification [15], measured from Beacon, DMG Beacon or FILS discovery frames (in passive scanning mode) or from probe response frames (in active scanning mode). |
| --- | --- |
| Applicable for | RRC_CONNECTED inter-RAT, RRC_IDLE inter-RAT |

### 5.1.17 MBSFN Reference Signal Received Power (MBSFN RSRP)

| Definition | MBSFN Reference signal received power (MBSFN RSRP), is defined as the linear average over the power contributions (in [W]) of the resource elements that carry MBSFN reference signals within the considered measurement frequency bandwidth. For MBSFN RSRP determination the MBSFN reference signals R4 according to TS 36.211 [3] shall be used. The reference point for the MBSFN RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding MBSFN RSRP of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine MBSFN RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

NOTE 3: The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

### 5.1.18 MBSFN Reference Signal Received Quality (MBSFN RSRQ)

| Definition | MBSFN Reference Signal Received Quality (RSRQ) is defined as the ratio N× MBSFN RSRP/(MBSFN carrier RSSI), where N is the number of RBs of the MBSFN carrier RSSI measurement bandwidth. The measurements in the numerator and denominator shall be made over the same set of resource blocks. MBSFN Carrier Received Signal Strength Indicator (MBSFN carrier RSSI), comprises the linear average of the total received power (in [W]) observed only in OFDM symbols containing reference symbols for antenna port 4, in the measurement bandwidth, over N number of resource blocks by the UE from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc. The reference point for the MBSFN RSRQ shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding MBSFN RSRQ of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

### 5.1.19 Multicast Channel Block Error Rate (MCH BLER)

| Definition | Multicast channel block error rate (MCH BLER) estimation shall be based on evaluating the CRC of MCH transport blocks. The BLER shall be computed over the measurement period as the ratio between the number of received MCH transport blocks resulting in a CRC error and the total number of received MCH transport blocks of an MCH. The MCH BLER estimation shall only consider MCH transport blocks using the same MCS. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency, RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

### 5.1.20 CSI Reference Signal Received Power (CSI-RSRP)

| Definition | CSI reference signal received power (CSI-RSRP), is defined as the linear average over the power contributions (in [W]) of the resource elements that carry CSI reference signals configured for discovery signal measurements within the considered measurement frequency bandwidth in the subframes in the configured discovery signal occasions. For CSI-RSRP determination CSI reference signals R15 according to TS 36.211 [3] shall be used. The reference point for the CSI-RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding CSI-RSRP of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine CSI-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

### 5.1.21 Sidelink Reference Signal Received Power (S-RSRP)

| Definition | Sidelink Reference Signal Received Power (S-RSRP) is defined as the linear average over the power contributions (in [W]) of the resource elements that carry demodulation reference signals associated with PSBCH, within the central 6 PRBs of the applicable subframes.The reference point for the S-RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding S-RSRP of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine S-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

NOTE 3: For RRC_IDLE intra-frequency, S-RSRP is only applicable to the Any Cell Selection state[16].

### 5.1.22 Sidelink Discovery Reference Signal Received Power (SD-RSRP)

| Definition | Sidelink Discovery Reference Signal Received Power (SD-RSRP) is defined as the linear average over the power contributions (in [W]) of the resource elements that carry demodulation reference signals associated with PSDCH for which CRC has been validated.The reference point for the SD-RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding SD-RSRP of any of the individual diversity branches. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequencyRRC_CONNECTED inter-frequency |

NOTE 1: The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine SD-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

### 5.1.23 Reference signal-signal to noise and interference ratio (RS-SINR)

| Definition | Reference signal-signal to noise and interference ratio (RS-SINR), is defined as the linear average over the power contribution (in [W]) of the resource elements carrying cell-specific reference signals divided by the linear average of the noise and interference power contribution (in [W]) over the resource elements carrying cell-specific reference signals within the same frequency bandwidth. For RS-SINR determination, the cell-specific reference signals R0 according TS 36.211 [3] shall be used. The reference point for the RS-SINR shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding RS-SINR of any of the individual diversity branches. If higher-layer signalling indicates certain subframes for performing RS-SINR measurements, then RS-SINR is measured in the indicated subframes. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

### 5.1.24 Received Signal Strength Indicator (RSSI)

| Definition | E-UTRA Received Signal Strength Indicator (RSSI), comprises the linear average of the total received power (in [W]) observed only in the configured OFDM symbol and in the measurement bandwidth over N number of resource blocks, by the UE from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc. Higher layers indicate the measurement duration and which OFDM symbol(s) should be measured by the UE.The reference point for the RSSI shall be the antenna connector of the UE. If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding RSSI of any of the individual diversity branches |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

### 5.1.25 SFN and subframe timing difference (SSTD)

| Definition | The observed SFN and subframe timing difference (SSTD) between a PCell and a PSCell is defined as consisting of the following three components;- SFN offset = (SFNPCell - SFNPSCell) mod 1024, where SFNPCell is the SFN of a PCell radio frame and SFNPSCell is the SFN of the PSCell radio frame of which the UE receives the start closest in time to the time when it receives the start of the PCell radio frame.- Frame boundary offset = ![](media_svg/image3.svg) [公式≈: √^{(T}FrameBoundaryPCell^{−}^{T}FrameBoundaryPSCell^{)/1000}∃], where TFrameBoundaryPCell is the time when the UE receives the start of a radio frame from the PCell and TFrameBoundaryPSCell is the time when the UE receives the start of the radio frame of PSCell that is closest in time to the radio frame received from the PCell. The unit of (TFrameBoundaryPCell - TFrameBoundaryPSCell) is [µs].- Subframe boundary offset = TSubframePCell - TSubframePSCell, where TSubframePCell is the time when the UE receives the start of a subframe from the PCell and TSubframePSCell is the time when the UE receives the start of the subframe from the PSCell that is closest in time to the subframe received from the PCell.The reference point for the observed SFN and subframe time difference shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_CONNECTED intra-frequency |

### 5.1.26 Narrowband Reference Signal Received Power (NRSRP)

| Definition | Unless indicated otherwise by higher layers, narrowband reference signal received power (NRSRP), is defined as the linear average over the power contributions (in [W]) of the resource elements that carry narrowband specific reference signals within the considered measurement frequency bandwidth. For NRS based NRSRP determination, the narrowband reference signals for the first antenna port (R2000) according to TS 36.211 [3] shall be used. If the UE can reliably detect that a second antenna port (R2001) is available, it may use the second antenna port in addition to the first antenna port to determine NRSRP. If higher layers indicate measurements based on narrow band secondary synchronization signal (NSSS), NRSRP is defined as the linear average over the power contributions (in [W]) of the resource elements that carry NSSS in the NSSS occasions that the UE measures. The NRSRP is adjusted by the NSSS to NRS EPRE ratio as indicated by higher layers [7].For NSSS based NRSRP determination, the UE may take the signalled precoder information applied at the antenna ports into account [7].If higher layers indicate measurements based on narrow band physical broadcast channel (NPBCH) on the serving cell, NRSRP is defined as the linear average over the power contributions (in [W]) of the resource elements that carry NPBCH in the NPBCH occasions that the UE measures. The NRSRP is adjusted by the NPBCH to NRS EPRE ratio as defined in clause 16.2.2 of [5].The reference point for the NRSRP shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency (only applicable for NRS based NRSRP) |

### 5.1.27 Narrowband Reference Signal Received Quality (NRSRQ)

| Definition | Narrowband Reference Signal Received Quality (NRSRQ) is defined as the ratio NRSRP/NRSSI. The measurements in the numerator and denominator shall be made over the same set of resource blocks.Narrowband Received Signal Strength Indicator (NRSSI), comprises the linear average of the total received power (in [W]) observed OFDM symbols of measurement subframes, in the measurement bandwidth by the UE from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc. NRSSI is measured from all OFDM symbols of measurement subframes. The reference point for the NRSRQ shall be the antenna connector of the UE. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency, RRC_IDLE inter-frequency |

### 5.1.28 Sidelink Received Signal Strength Indicator (S-RSSI)

| Definition | Sidelink RSSI (S-RSSI) is defined as the linear average of the total received power (in [W]) per SC-FDMA symbol observed by the UE only in the configured sub-channel in SC-FDMA symbols 1, 2, …, 6 of the first slot and SC-FDMA symbols 0,1,…, 5 of the second slot of a subframe The reference point for the S-RSSI shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding S-RSSI of any of the individual diversity branches |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

### 5.1.29 PSSCH Reference Signal Received Power (PSSCH-RSRP)

| Definition | PSSCH Reference Signal Received Power (PSSCH-RSRP) is defined as the linear average over the power contributions (in [W]) of the resource elements that carry demodulation reference signals associated with PSSCH, within the PRBs indicated by the associated PSCCH.The reference point for the PSSCH-RSRP shall be the antenna connector of the UE.If receiver diversity is in use by the UE, the reported value shall not be lower than the corresponding PSSCH-RSRP of any of the individual diversity branches |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

### 5.1.30 Channel busy ratio (CBR)

| Definition | Channel busy ratio (CBR) measured in subframe n is defined as follows:- For PSSCH, the portion of sub-channels in the resource pool whose S-RSSI measured by the UE exceed a (pre-)configured threshold sensed over subframes [n-100, n-1]; - For PSCCH, in a pool (pre)configured such that PSCCH may be transmitted with its corresponding PSSCH in non-adjacent resource blocks, the portion of the resources of the PSCCH pool whose S-RSSI measured by the UE exceed a (pre-)configured threshold sensed over subframes [n-100, n-1], assuming that the PSCCH pool is composed of resources with a size of two consecutive PRB pairs in the frequency domain. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE: The subframe index is based on physical subframe index

### 5.1.31 Channel occupancy ratio (CR)

| Definition | Channel occupancy ratio (CR) evaluated at subframe n is defined as the total number of sub-channels used for its transmissions in subframes [n-a, n-1] and granted in subframes [n, n+b] divided by the total number of configured sub-channels in the transmission pool over [n-a, n+b]. |
| --- | --- |
| Applicable for | RRC_IDLE intra-frequency,RRC_IDLE inter-frequency,RRC_CONNECTED intra-frequency,RRC_CONNECTED inter-frequency |

NOTE 1: a is a positive integer and b is 0 or a positive integer; a and b are determined by UE implementation with a+b+1 = 1000, a >= 500, and n+b should not exceed the last transmission opportunity of the grant for the current transmission.

NOTE 2: CR is evaluated for each (re)transmission.

NOTE 3: In evaluating CR, the UE shall assume the transmission parameter used at subframe n is reused according to the existing grant(s) in subframes [n+1, n+b] without packet dropping.

NOTE 4: The subframe index is based on physical subframe index.

NOTE 5: CR can be computed per priority level

### 5.1.32 NR SS reference signal received power (NR-SS-RSRP)

| Definition | NR SS reference signal received power (NR-SS-RSRP) is defined as the linear average over the power contributions (in [W]) of the resource elements that carry secondary synchronization signals (SS). The measurement time resource(s) for NR-SS-RSRP are confined within SS/PBCH Block Measurement Time Configuration (SMTC) window duration. For NR-SS-RSRP determination demodulation reference signals for physical broadcast channel (PBCH) in addition to secondary synchronization signals may be used. NR-SS-RSRP using demodulation reference signal for PBCH shall be measured by linear averaging over the power contributions of the resource elements that carry corresponding reference signals taking into account power scaling for the reference signals as defined in TS 38.213 [17]. NR-SS-RSRP shall be measured only among the reference signals corresponding to SS/PBCH blocks with the same SS/PBCH block index and the same physical-layer cell identity. If higher-layers indicate certain SS/PBCH blocks for performing NR-SS-RSRP measurements, then NR-SS-RSRP is measured only from the indicated set of SS/PBCH block(s).For frequency range 1, the reference point for the NR-SS-RSRP shall be the antenna connector of the UE. For frequency range 2, NR-SS-RSRP shall be measured based on the combined signal from antenna elements corresponding to a given receiver branch. For frequency range 1 and 2, if receiver diversity is in use by the UE, the reported NR-SS-RSRP value shall not be lower than the corresponding NR-SS-RSRP of any of the individual receiver branches. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

NOTE 1: The number of resource elements within the measurement period that are used by the UE to determine NR-SS-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2: The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

### 5.1.33 NR SS reference signal received quality (NR-SS-RSRQ)

| Definition | NR Secondary synchronization signal reference signal received quality (NR-SS-RSRQ) is defined as the ratio of N× NR-SS-RSRP / NR carrier RSSI, where N is the number of resource blocks in the NR carrier RSSI measurement bandwidth. The measurements in the numerator and denominator shall be made over the same set of resource blocks.NR carrier Received Signal Strength Indicator (NR carrier RSSI), comprises the linear average of the total received power (in [W]) observed only in certain OFDM symbols of measurement time resource(s), in the measurement bandwidth, over N number of resource blocks from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc. The measurement time resource(s) for NR Carrier RSSI are confined within SS/PBCH Block Measurement Time Configuration (SMTC) window duration.If indicated by higher-layers, for a half-frame with SS/PBCH blocks the NR Carrier RSSI is measured from OFDM symbols of the indicated slots and the OFDM symbol are given by Table 5.1.33-1. Otherwise, if measurement gap is not used, NR Carrier RSSI is measured from OFDM symbols within SMTC window duration and, if measurement gap is used, NR Carrier RSSI is measured from OFDM symbols corresponding to overlapped time span between SMTC window duration and minimum measurement time within the measurement gap.Table 5.1.33-1: NR Carrier RSSI measurement symbolsIf higher-layers indicate certain SS/PBCH blocks for performing NR-SS-RSRQ measurements, then NR-SS-RSRP is measured only from the indicated set of SS/PBCH block(s).For frequency range 1, the reference point for the NR-SS-RSRQ shall be the antenna connector of the UE. For frequency range 2, NR Carrier RSSI shall be measured based on the combined signal from antenna elements corresponding to a given receiver branch, where the combining for NR Carrier RSSI shall be the same as the one used for NR-SS-RSRP measurements. For frequency range 1 and 2, if receiver diversity is in use by the UE, the reported NR-SS-RSRQ value shall not be lower than the corresponding NR-SS-RSRQ of any of the individual receiver branches. |
| --- | --- |
| Applicable for | RRC_IDLE inter-RAT,RRC_CONNECTED inter-RAT |

### 5.1.34 SFN and frame timing difference (SFTD)

| Definition | The observed SFN and frame timing difference (SFTD) between an E-UTRA PCell and an NR PSCell (for EN-DC), or an NR PCell and an E-UTRA PSCell (for NE-DC), or an E-UTRA PCell and an NR neighbouring cell is defined as comprising the following two components:- SFN offset = (SFNPCell - SFNTRGCell) mod 1024, where SFNPCell is the SFN of a PCell radio frame and SFNTRGCell is the SFN of the target-cell radio frame of which the UE receives the start closest in time to the time when it receives the start of the PCell radio frame.- Frame boundary offset = ![](media_svg/image4.svg) [公式≈: √^{(T}FrameBoundaryPCell^{−}^{T}FrameBoundaryTRGCell^{)}^{/}^{5}∃], where TFrameBoundaryPCell is the time when the UE receives the start of a radio frame from the PCell, TFrameBoundaryTRGCell is the time when the UE receives the start of the radio frame, from the target cell, that is closest in time to the radio frame received from the PCell. The unit of (TFrameBoundaryPCell - TFrameBoundaryTRGCell) is Ts. |
| --- | --- |
| Applicable for | RRC_CONNECTED |

NOTE : Refer to TS38.133 [18] for applicability to intra-frequency, inter-frequency or inter-RAT.

### 5.1.35 NR SS signal-to-noise and interference ratio (NR-SS-SINR)

| Definition | NR SS signal-to-noise and interference ratio (NR-SS-SINR), is defined as the linear average over the power contribution (in [W]) of the resource elements carrying secondary synchronisation signals divided by the linear average of the noise and interference power contribution (in [W]) over the resource elements carrying secondary synchronisation signals within the same frequency bandwidth. The measurement time resource(s) for NR-SS-SINR are confined within SS/PBCH Block Measurement Time Configuration (SMTC) window duration.For NR-SS-SINR determination demodulation reference signals for physical broadcast channel (PBCH) in addition to secondary synchronization signals may be used.If higher-layers indicate certain SS/PBCH blocks for performing NR-SS-SINR measurements, then NR-SS-SINR is measured only from the indicated set of SS/PBCH block(s).For frequency range 1, the reference point for the NR-SS-SINR shall be the antenna connector of the UE. For frequency range 2, NR-SS-SINR shall be measured based on the combined signal from antenna elements corresponding to a given receiver branch. For frequency range 1 and 2, if receiver diversity is in use by the UE, the reported NR-SS-SINR value shall not be lower than the corresponding NR-SS-SINR of any of the individual receiver branches. |
| --- | --- |
| Applicable for | RRC_CONNECTED inter-RAT |

## 5.2 E-UTRAN measurement abilities

The structure of the table defining a E-UTRAN measurement quantity is shown below.

| Column field | Comment |
| --- | --- |
| Definition | Contains the definition of the measurement. |

The term "antenna connector" used in this clause to define the reference point for the E-UTRAN measurements refers to the "BS antenna connector" test port A and test port B as described in [10]. The term "antenna connector" refers to Rx or Tx antenna connector as described in the respective measurement definitions.

### 5.2.1 DL RS TX power

| Definition | Downlink reference signal transmit power is determined for a considered cell as the linear average over the power contributions (in [W]) of the resource elements that carry cell-specific reference signals which are transmitted by the eNode B within its operating system bandwidth.For DL RS TX power determination the cell-specific reference signals R0 and if available R1 according TS 36.211 [3] can be used.The reference point for the DL RS TX power measurement shall be the TX antenna connector.For NTN, the reference point for the DL RS TX power measurement shall be- the TAB connectors for SAN type 1-H defined in clause 4.3 in TS 36.108 [20],- the RIB for SAN type 1-O defined in clause 4.3 in TS 36.108 [20]. |
| --- | --- |

### 5.2.2 Received Interference Power

| Definition | The uplink received interference power, including thermal noise, within one physical resource block's bandwidth of ![](media_svg/image5.svg) [公式≈: _{N}_{sc}RB]resource elements as defined in TS 36.211 [3]. The reported value shall contain a set of Received Interference Powers of physical resource blocks ![](media_svg/image6.svg) [公式≈: n_{PRB}=0,...,N^{UL}_{RB}−1] as defined in TS 36.211 [3]. The reference point for the measurement shall be the RX antenna connector. In case of receiver diversity, the reported value shall be linear average of the power in the diversity branches.For NTN, the reference point for the received interference power measurement shall be- the TAB connectors for SAN type 1-H defined in clause 4.3 in TS 36.108 [20],- the RIB for SAN type 1-O defined in clause 4.3 in TS 36.108 [20]. |
| --- | --- |

### 5.2.3 Thermal noise power

| Definition | The uplink thermal noise power within the UL system bandwidth consisting of ![](media_svg/image7.svg) [公式≈: _{N}UL_{RB}] resource blocks as defined in [3]. It is defined as (No x W), where No denotes the white noise power spectral density on the uplink carrier frequency and ![](media_svg/image8.svg) [公式≈: W=N^{UL}_{RB}∪N_{sc}^{RB}∪δf] denotes the UL system bandwidth. The measurement is optionally reported together with the Received Interference Power measurement, it shall be determined over the same time period as the Received Interference Power measurement. The reference point for the measurement shall be the RX antenna connector. In case of receiver diversity, the reported value shall be linear average of the power in the diversity branches.For NTN, the reference point for the thermal noise power measurement shall be- the TAB connectors for SAN type 1-H defined in clause 4.3 in TS 36.108 [20],- the RIB for SAN type 1-O defined in clause 4.3 in TS 36.108 [20]. |
| --- | --- |

### 5.2.4 Timing advance (TADV)

| Definition | Type1:Timing advance (TADV) type 1 is defined as the time difference  TADV = (eNB Rx – Tx time difference) + (UE Rx – Tx time difference),where the eNB Rx – Tx time difference corresponds to the same UE that reports the UE Rx – Tx time difference.Type2:Timing advance (TADV) type 2 is defined as the time difference  TADV = (eNB Rx – Tx time difference),where the eNB Rx – Tx time difference corresponds to a received uplink radio frame containing PRACH from the respective UE or similarly NPRACH from the respective NB-IoT UE.. |
| --- | --- |

### 5.2.5 eNB Rx – Tx time difference

| Definition | The eNB Rx – Tx time difference is defined as T eNB-RX – TeNB-TXWhere:T eNB-RX is the eNB received timing of uplink radio frame #i, defined by the first detected path in time.The reference point for TeNB-RX shall be:- for non-AAS base station [10,TS 36.104]: the Rx antenna connector,- for OTA AAS base station [19,TS 37.105]: the Rx antenna,- for Hybrid AAS base station [19,TS 37.105]: the Rx Transceiver Array Boundary connector.T eNB-TX is the eNB transmit timing of downlink radio frame #i.The reference point for TeNB-TX shall be:- for non-AAS base station [10,TS 36.104]: the Tx antenna connector,- for OTA AAS base station [19,TS 37.105]: the Tx antenna,- for Hybrid AAS base station [19,TS 37.105]: the Tx Transceiver Array Boundary connector. |
| --- | --- |

### 5.2.6 E-UTRAN GNSS Timing of Cell Frames for UE positioning

| Definition | TE-UTRAN-GNSS is defined as the time of the occurrence of a specified LTE event according to a GNSS-specific reference time for a given GNSS (e.g., GPS/Galileo/Glonass system time). The specified LTE event is the beginning of the transmission of a particular frame (identified through its SFN) in the cell. The reference point for TE-UTRAN-GNSS shall be the Tx antenna connector. |
| --- | --- |

### 5.2.7 Angle of Arrival (AoA)

| Definition | AoA defines the estimated angle of a user with respect to a reference direction. The reference direction for this measurement shall be the geographical North, positive in a counter-clockwise direction.The AoA is determined at the eNB antenna for an UL channel corresponding to this UE. |
| --- | --- |

### 5.2.8 UL Relative Time of Arrival (TUL-RTOA)

| Definition | The UL Relative Time of Arrival (TUL-RTOA) is the beginning of subframe i containing SRS received in LMU j, relative to the configurable reference time [13], [14]. The reference point [14] for the UL relative time of arrival shall be the RX antenna connector of the LMU node when LMU has a separate RX antenna or shares RX antenna with eNB and the eNB antenna connector when LMU is integrated in eNB. |
| --- | --- |

###### Annex A (informative):
Change history

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | TSG # | TSG Doc. | CR | Rev | Subject/Comment | Old | New |
| 02/10/06 | - | - | - |  | Draft version created | - | 0.0.0 |
| 11/10/06 | - | - | - |  | Minor editorial updates for RAN1#46bis | 0.0.0 | 0.0.1 |
| 13/10/06 | - | - | - |  | Endorsed skeleton | 0.0.1 | 0.1.0 |
| 27/02/07 | - | - | - |  | Update after TSG RAN WG1 #48 | 0.1.0 | 0.1.1 |
| 05/03/07 | - | - | - |  | RAN1 endorsed version | 0.1.1 | 0.2.0 |
| 03/05/07 | - | - | - |  | Update after TSG RAN WG1#48bis | 0.2.0 | 0.2.1 |
| 08/03/07 | - | - | - |  | RAN WG1#49 endorsed version | 0.2.1 | 0.3.0 |
| 31/05/07 | RAN#36 | RP-070490 | - |  | Presented for information at RAN#36 | 0.3.0 | 1.0.0 |
| 21/06/07 | - | - | - |  | Update after TSG RAN #36 | 1.0.0 | 1.0.1 |
| 25/06/07 | - | - | - |  | TSG RAN WG1#49bis endorsed version | 1.0.1 | 1.1.0 |
| 17/08/07 | - | - | - |  | Update after TSG RAN WG1#48bis | 1.1.0 | 1.1.1 |
| 20/08/07 | - | - | - |  | TSG RAN WG1#50 endorsed version | 1.1.1 | 1.2.0 |
| 10/09/07 | RAN#37 | RP-070732 | - |  | For approval at RAN#37 | 1.2.0 | 2.0.0 |
| 12/09/07 | RAN_37 | RP-070732 | - | - | Approved version | 2.0.0 | 8.0.0 |
| 28/11/07 | RAN_38 | RP-070949 | 0001 | 1 | RRC state correction for LTE UE measurements | 8.0.0 | 8.1.0 |
| 05/03/08 | RAN_39 | RP-080145 | 0003 | 1 | Inclusion of agreements from RAN1#51bis and RAN1#52 | 8.1.0 | 8.2.0 |
| 28/05/08 | RAN_40 | RP-080435 | 0004 | - | Introduction of eNode B Measurement of Received Interference Power | 8.2.0 | 8.3.0 |
| 28/05/08 | RAN_40 | RP-080435 | 0005 | - | Introduction of eNode B Measurement of Thermal Noise Power | 8.2.0 | 8.3.0 |
| 09/09/08 | RAN_41 | RP-080671 | 0006 | - | Modification to the RSRP definition | 8.3.0 | 8.4.0 |
| 09/09/08 | RAN_41 | RP-080671 | 0007 | - | Modification of RSRQ definition and removal of RSSI | 8.3.0 | 8.4.0 |
| 03/12/08 | RAN_42 | RP-080985 | 0008 | - | RSRQ Measurement Definition | 8.4.0 | 8.5.0 |
| 04/03/09 | RAN_43 | RP-090237 | 0009 | - | RSRP and RSRQ Definitions with Receiver Diversity | 8.5.0 | 8.6.0 |
| 15/09/09 | RAN_45 | RP-090888 | 0010 |  | Clarification on reference point of RSRP and RSRQ for EUTRA | 8.6.0 | 8.7.0 |
| 01/12/09 | RAN_46 | RP-091172 | 0011 | 1 | Introduction of LTE positioning | 8.7.0 | 9.0.0 |
| 16/03/10 | RAN_47 | RP-100205 | 0012 | 1 | Modification of RSRQ definition | 9.0.0 | 9.1.0 |
| 01/06/10 | RAN_48 | RP-100590 | 0014 | - | On alignment of RAN1/2 positioning specification | 9.1.0 | 9.2.0 |
| 01/06/10 | RAN_48 | RP-100590 | 0015 | 1 | Clarification of RSTD measurement | 9.1.0 | 9.2.0 |
| 07/12/10 | RAN_50 | - | - | - | Creation of Rel-10 specification | 9.2.0 | 10.0.0 |
| 15/03/11 | RAN_51 | RP-110258 | 0016 | - | RSRQ Measurement with ABS | 10.0.0 | 10.1.0 |
| 04/09/12 | RAN_57 | RP-121273 | 0018 | 4 | UL Relative Time of Arrival | 10.1.0 | 11.0.0 |
| 04/12/12 | RAN_58 | RP-121837 | 0019 | 1 | Correcting inconsistency between inter-RAT UTRA measurements and requirements | 11.0.0 | 11.1.0 |
| 10/09/14 | RAN_65 | RP-141484 | 0022 | 2 | Inclusion of definition of WLAN Beacon RSSI in LTE specifications | 11.1.0 | 12.0.0 |
| 08/12/14 | RAN_66 | RP-142105 | 0020 | 1 | Introduction of MBSFN radio measurement | 12.0.0 | 12.1.0 |
| 08/12/14 | RAN_66 | RP-142106 | 0023 | 3 | Measurement definitions for measurements with discovery signals | 12.0.0 | 12.1.0 |
| 09/03/15 | RAN_67 | RP-150361 | 0021 | 2 | New E-UTRA RSRQ measurement definition | 12.1.0 | 12.2.0 |
| 09/03/15 | RAN_67 | RP-150366 | 0026 | 2 | Inclusion of measurement for ProSe | 12.1.0 | 12.2.0 |
| 07/12/15 | RAN_70 | RP-152125 | 0027 | 1 | eD2D CR for 36.214 | 12.2.0 | 13.0.0 |
| 07/12/15 | RAN_70 | RP-152035 | 0028 | 2 | Introduction of RS-SINR measurement for Multicarrier Load Distribution | 12.2.0 | 13.0.0 |
| 07/12/15 | RAN_70 | RP-152026 | 0029 | 1 | Introduction of LAA | 12.2.0 | 13.0.0 |
| 07/12/15 | RAN_70 | RP-152032 | 0030 | - | Introduction of SSTD for dual connectivity enhancement | 12.2.0 | 13.0.0 |

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2016-03 | RAN#71 | RP-160364 | 0031 | 1 | B | Introduction of WLAN RSSI measurements to support WLAN/LTE Radio Interworking | 13.1.0 |
| 2016-03 | RAN#71 | RP-160360 | 0032 | - | F | Correction on RSSI definition of LAA in 36.214 | 13.1.0 |
| 2016-06 | RAN#72 | RP-161067 | 0033 | 2 | B | Introduction of NB-IoT | 13.2.0 |
| 2016-09 | RAN#73 | RP-161567 | 0035 | - | F | Correction to the WLAN RSSI definition | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 0036 | - | F | Correction on NRS port number mapping | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 0037 | - | F | Correction on NRSRQ applicability | 13.3.0 |
| 2016-09 | RAN#73 | RP-161570 | 0038 | 1 | B | Introduction of V2V support | 14.0.0 |
| 2016-12 | RAN#74 | RP-162360 | 0040 | - | A | Correction on SSTD definition | 14.1.0 |
| 2017-03 | RAN#75 | RP-170622 | 0042 | - | B | Introduction of V2X | 14.2.0 |
| 2017-03 | RAN#75 | RP-170624 | 0043 | - | B | Introduction of NB-IoT enhancements | 14.2.0 |
| 2017-09 | RAN#77 | RP-171651 | 0046 | - | A | Clarification CR for LAA RRM measurements within the DRS transmisison window | 14.3.0 |
| 2017-09 | RAN#77 | RP-171641 | 0044 | - | B | CR on 36.214 for UE carrier phase measurements | 15.0.0 |
| 2018-01 |  |  |  |  |  | MCC to correct missing 5G logo on spec cover sheet | 15.0.1 |
| 2018-03 | RAN#79 | RP-180201 | 0048 | 1 | B | Inter-RAT Measurements of NR | 15.1.0 |
| 2018-03 | RAN#79 | RP-180193 | 0049 | - | A | Revision of UE measurement report definitions considering NB-IoT UEs | 15.1.0 |
| 2018-06 | RAN#80 | RP-181166 | 0050 | 1 | B | Introduction Rel-15 Further NB-IoT enhancements | 15.2.0 |
| 2018-09 | RAN#81 | RP-181798 | 0051 | - | B | Introduction of NR-SS-SINR | 15.3.0 |
| 2018-09 | RAN#81 | RP-181783 | 0052 | - | F | Introduction of NPBCH based NRSRP measurement | 15.3.0 |
| 2019-09 | RAN#85 | RP-191938 | 0053 | - | F | Correction on SFTD measurement in TS 36.214 | 15.4.0 |
| 2019-12 | RAN#86 | RP-192622 | 0054 | - | F | Correction on SFTD measurement in TS 36.214 | 15.5.0 |
| 2019-12 | RAN#86 | RP-192647 | 0055 | - | B | Introduction of RSRP measurement based on RSS | 16.0.0 |
| 2020-06 | RAN#88-e | RP-200701 | 0056 | - | F | Corrections to LTE terrestrial broadcast | 16.1.0 |
| 2021-03 | RAN#91-e | RP-210055 | 0057 | - | F | Corrections to 36.214 for Reference Point for eNB Rx – Tx time difference | 16.2.0 |
| 2022-03 | SA#95-e | - | - | - | - | Update to Rel-17 version (MCC) | 17.0.0 |
| 2024-03 | SA#103 | - | - | - | - | Update to Rel-18 version (MCC) | 18.0.0 |
| 2025-06 | RAN#108 | RP-251568 | 0058 | - | F | CR on E-UTRAN measurement in IoT NTN | 18.1.0 |
| 2025-09 | SA#109 | - | - | - | - | Update to Rel-19 version (MCC) | 19.0.0 |
