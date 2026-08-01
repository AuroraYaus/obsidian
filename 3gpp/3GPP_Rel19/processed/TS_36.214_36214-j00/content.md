---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.214_36214-j00/content.md"
---
# TS 36.214 36214-j00

Contents

Foreword5

1Scope6

2References6

3Definitions, symbols and abbreviations7

3.1Definitions7

3.2Symbols7

3.3Abbreviations7

4Control of UE/E-UTRAN measurements7

5Measurement capabilities for E-UTRA8

5.1UE measurement capabilities8

5.1.1Reference Signal Received Power (RSRP)9

5.1.2Void9

5.1.3Reference Signal Received Quality (RSRQ)10

5.1.4UTRA FDD CPICH RSCP10

5.1.5UTRA FDD carrier RSSI10

5.1.6UTRA FDD CPICH Ec/No11

5.1.7GSM carrier RSSI11

5.1.8Void11

5.1.9UTRA TDD P-CCPCH RSCP11

5.1.10CDMA2000 1x RTT Pilot Strength11

5.1.11CDMA2000 HRPD Pilot Strength11

5.1.12Reference signal time difference (RSTD)12

5.1.13UE GNSS Timing of Cell Frames for UE positioning12

5.1.14UE GNSS code measurements12

5.1.14AUE GNSS carrier phase measurements12

5.1.15UE Rx – Tx time difference13

5.1.16IEEE 802.11 WLAN RSSI13

5.1.17MBSFN Reference Signal Received Power (MBSFN RSRP)13

5.1.18MBSFN Reference Signal Received Quality (MBSFN RSRQ)14

5.1.19Multicast Channel Block Error Rate (MCH BLER)14

5.1.20CSI Reference Signal Received Power (CSI-RSRP)14

5.1.21Sidelink Reference Signal Received Power (S-RSRP)15

5.1.22Sidelink Discovery Reference Signal Received Power (SD-RSRP)15

5.1.23Reference signal-signal to noise and interference ratio (RS-SINR)16

5.1.24Received Signal Strength Indicator (RSSI)16

5.1.25SFN and subframe timing difference (SSTD)17

5.1.26Narrowband Reference Signal Received Power (NRSRP)17

5.1.27Narrowband Reference Signal Received Quality (NRSRQ)18

5.1.28Sidelink Received Signal Strength Indicator (S-RSSI)18

5.1.29PSSCH Reference Signal Received Power (PSSCH-RSRP)18

5.1.30Channel busy ratio (CBR)19

5.1.31Channel occupancy ratio (CR)19

5.1.32NR SS reference signal received power (NR-SS-RSRP)20

5.1.33NR SS reference signal received quality (NR-SS-RSRQ)21

5.1.34SFN and frame timing difference (SFTD)22

5.1.35NR SS signal-to-noise and interference ratio (NR-SS-SINR)22

5.2E-UTRAN measurement abilities22

5.2.1DL RS TX power23

5.2.2Received Interference Power23

5.2.3Thermal noise power23

5.2.4Timing advance (TADV)23

5.2.5eNB Rx – Tx time difference24

5.2.6E-UTRAN GNSS Timing of Cell Frames for UE positioning24

5.2.7Angle of Arrival (AoA)24

5.2.8UL Relative Time of Arrival (TUL-RTOA)24

Annex A (informative):Change history25

## Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

xthe first digit:

1presented to TSG for information;

2presented to TSG for approval;

3or greater indicates TSG approved document under change control.

Ythe second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

zthe third digit is incremented when editorial only changes have been incorporated in the document.

## 1Scope

The present document contains the description and definition of the measurements done at the UE and network in order to support operation in idle mode and connected mode.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 36.201: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description ".

[3]3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[4]3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding ".

[5]3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures ".

[6]3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[7]3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification ".

[8]3GPP2 CS.0005-D v1.0 "Upper Layer (Layer 3) Signaling Standard for CDMA2000 Spread Spectrum Systems Release D".

[9]3GPP2 CS.0024-A v3.0 "cdma2000 High Rate Packet Data Air Interface Specification"

[10]3GPP TS 36.104: "Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception ".

[11]3GPP TS 36.355: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol (LPP)"

[12]3GPP TS 36.455: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol A (LPPa)"

[13]3GPP TS 36.459: "Evolved Universal Terrestrial Radio Access (E-UTRA); SLm Application Protocol (SLmAP)"

[14]3GPP TS 36.111: "Evolved Universal Terrestrial Radio Access (E-UTRA); Location Measurement Unit (LMU) performance specification; Network Based Positioning Systems in E-UTRAN"

[15]IEEE 802.11, Part 11: "Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) specifications, IEEE Std.".

[16]3GPP TS 36.304: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode ".

[17]3GPP TS 38.213: "NR; Physical layer procedures for control".

[18]3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[19]3GPP TS 37.105: "Active Antenna System (AAS) Base Station (BS) transmission and reception".

[20]3GPP TS 36.108: "Evolved Universal Terrestrial Radio Access (E-UTRA); Satellite Access Node radio transmission and reception".

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

Ec/NoReceived energy per chip divided by the power density in the band

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

1x RTTCDMA2000 1x Radio Transmission Technology

CPICHCommon Pilot Channel

E-SMLCEnhanced Serving Mobile Location Centre

E-UTRAEvolved UTRA

E-UTRANEvolved UTRAN

FDDFrequency Division Duplex

GNSSGlobal Navigation Satellite System

GSMGlobal System for Mobile communication

HRPDCDMA2000 High Rate Packet Data

LMULocation Measurement Unit

NTNNon-Terrestrial Network

P-CCPCHPrimary Common Control Physical Channel

RIBRadiated Interface Boundary

RSCPReceived Signal Code Power

RSRPReference Signal Received Power

RSRQReference Signal Received Quality

RSSIReceived Signal Strength Indicator

RSTDReference Signal Time Difference

SANSatellite Access Node

SRSSounding Reference Signal

TABTransceiver Array Boundary

TDDTime Division Duplex

UTRAUniversal Terrestrial Radio Access

UTRANUniversal Terrestrial Radio Access Network

## 4Control of UE/E-UTRAN measurements

In this clause the general measurement control concept of the higher layers is briefly described to provide an understanding on how L1 measurements are initiated and controlled by higher layers.

With the measurement specifications L1 provides measurement capabilities for the UE and E-UTRAN. These measurements can be classified in different reported measurement types: intra-frequency, inter-frequency, inter-system, traffic volume, quality and UE internal measurements (see the RRC Protocol [7]).

In the L1 measurement definitions, see clause 5, the measurements are categorised as measurements in the UE (the messages for these will be described in the MAC Protocol [6] or RRC Protocol [7] or LPP Protocol [11]) or measurements in the E-UTRAN (the messages for these will be described in the Frame Protocol or LPPa Protocol [12]).

To initiate a specific measurement, the E-UTRAN transmits a 'RRC connection reconfiguration message' to the UE including a measurement ID and type, a command (setup, modify, release), the measurement objects, the measurement quantity, the reporting quantities and the reporting criteria (periodical/event-triggered), see [7] or E-SMLC transmits an 'LPP Request Location Information message' to UE, see [11].

When the reporting criteria are fulfilled the UE shall answer with a 'measurement report message' to the E-UTRAN including the measurement ID and the results or an 'LPP Provide Location Information message' to the E-SMLC, see [11].

For idle mode, the measurement information elements are broadcast in the System Information.

## 5Measurement capabilities for E-UTRA

In this clause the physical layer measurements reported to higher layers are defined.

## 5.1UE measurement capabilities

The structure of the table defining a UE measurement quantity is shown below.

## 5.1.1Reference Signal Received Power (RSRP)

NOTE 1:The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

## 5.1.2Void

## 5.1.3Reference Signal Received Quality (RSRQ)

## 5.1.4UTRA FDD CPICH RSCP

## 5.1.5UTRA FDD carrier RSSI

NOTE:This definition does not correspond to a reported measurement. This definition is just an intermediate definition used in the definition of UTRA FDD CPICH Ec/No.

## 5.1.6UTRA FDD CPICH Ec/No

## 5.1.7GSM carrier RSSI

## 5.1.8Void

## 5.1.9UTRA TDD P-CCPCH RSCP

## 5.1.10CDMA2000 1x RTT Pilot Strength

## 5.1.11CDMA2000 HRPD Pilot Strength

## 5.1.12Reference signal time difference (RSTD)

## 5.1.13UE GNSS Timing of Cell Frames for UE positioning

## 5.1.14UE GNSS code measurements

## 5.1.14AUE GNSS carrier phase measurements

## 5.1.15UE Rx – Tx time difference

## 5.1.16IEEE 802.11 WLAN RSSI

## 5.1.17MBSFN Reference Signal Received Power (MBSFN RSRP)

NOTE 1:The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine MBSFN RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

NOTE 3:The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

## 5.1.18MBSFN Reference Signal Received Quality (MBSFN RSRQ)

NOTE 1:The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

## 5.1.19Multicast Channel Block Error Rate (MCH BLER)

NOTE 1:The measurement is made only in subframes (or slots in case of 0.37 kHz subcarrier spacing) and on carriers where the UE is decoding PMCH.

## 5.1.20CSI Reference Signal Received Power (CSI-RSRP)

NOTE 1:The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine CSI-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

## 5.1.21Sidelink Reference Signal Received Power (S-RSRP)

NOTE 1:The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine S-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

NOTE 3:For RRC_IDLE intra-frequency, S-RSRP is only applicable to the Any Cell Selection state[16].

## 5.1.22Sidelink Discovery Reference Signal Received Power (SD-RSRP)

NOTE 1:The number of resource elements within the considered measurement frequency bandwidth and within the measurement period that are used by the UE to determine SD-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

## 5.1.23Reference signal-signal to noise and interference ratio (RS-SINR)

## 5.1.24Received Signal Strength Indicator (RSSI)

## 5.1.25SFN and subframe timing difference (SSTD)

## 5.1.26Narrowband Reference Signal Received Power (NRSRP)

## 5.1.27Narrowband Reference Signal Received Quality (NRSRQ)

## 5.1.28Sidelink Received Signal Strength Indicator (S-RSSI)

## 5.1.29PSSCH Reference Signal Received Power (PSSCH-RSRP)

NOTE:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

## 5.1.30Channel busy ratio (CBR)

NOTE:The subframe index is based on physical subframe index

## 5.1.31Channel occupancy ratio (CR)

NOTE 1:a is a positive integer and b is 0 or a positive integer; a and b are determined by UE implementation with a+b+1 = 1000, a >= 500, and n+b should not exceed the last transmission opportunity of the grant for the current transmission.

NOTE 2:CR is evaluated for each (re)transmission.

NOTE 3:In evaluating CR, the UE shall assume the transmission parameter used at subframe n is reused according to the existing grant(s) in subframes [n+1, n+b] without packet dropping.

NOTE 4:The subframe index is based on physical subframe index.

NOTE 5:CR can be computed per priority level

## 5.1.32NR SS reference signal received power (NR-SS-RSRP)

NOTE 1:The number of resource elements within the measurement period that are used by the UE to determine NR-SS-RSRP is left up to the UE implementation with the limitation that corresponding measurement accuracy requirements have to be fulfilled.

NOTE 2:The power per resource element is determined from the energy received during the useful part of the symbol, excluding the CP.

## 5.1.33NR SS reference signal received quality (NR-SS-RSRQ)

## 5.1.34SFN and frame timing difference (SFTD)

NOTE :Refer to TS38.133 [18] for applicability to intra-frequency, inter-frequency or inter-RAT.

## 5.1.35NR SS signal-to-noise and interference ratio (NR-SS-SINR)

## 5.2E-UTRAN measurement abilities

The structure of the table defining a E-UTRAN measurement quantity is shown below.

The term "antenna connector" used in this clause to define the reference point for the E-UTRAN measurements refers to the "BS antenna connector" test port A and test port B as described in [10]. The term "antenna connector" refers to Rx or Tx antenna connector as described in the respective measurement definitions.

## 5.2.1DL RS TX power

## 5.2.2Received Interference Power

## 5.2.3Thermal noise power

## 5.2.4Timing advance (TADV)

## 5.2.5eNB Rx – Tx time difference

## 5.2.6E-UTRAN GNSS Timing of Cell Frames for UE positioning

## 5.2.7Angle of Arrival (AoA)

## 5.2.8UL Relative Time of Arrival (TUL-RTOA)

## Annex A (informative):Change history
