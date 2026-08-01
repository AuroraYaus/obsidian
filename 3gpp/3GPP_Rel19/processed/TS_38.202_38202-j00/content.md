---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.202_38202-j00/content.md"
---
# TS 38.202 38202-j00

3GPP TS 38.202 V19.0.0 (2025-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Services provided by the physical layer

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP..The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords

3GPP, New Radio, Layer 1

3GPP

Postal address

3GPP support office address

## 650 Route des Lucioles - Sophia Antipolis

Valbonne - FRANCE

Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

http://www.3gpp.org

Copyright Notification

No part may be reproduced except as authorized by written permission.The copyright and the foregoing restriction extend to reproduction in all media.

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersLTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Contents

Foreword4

1Scope5

2References5

3Definitions of terms, symbols and abbreviations5

3.1Terms5

3.2Symbols5

3.3Abbreviations5

4Services and functions of the physical layer6

4.1General6

4.2Overview of L1 functions6

5Model of physical layer of the UE6

5.1Uplink model7

5.1.1Uplink shared channel7

5.1.2Random access channel7

5.2Downlink model8

5.2.1Downlink shared channel8

5.2.2Broadcast channel8

5.2.3Paging channel9

5.3Sidelink model10

5.3.1Sidelink shared channel10

5.3.2Broadcast channel11

6Simultaneous transmission and reception of physical channels and physical signals12

6.1Uplink12

6.2Downlink13

6.3Sidelink15

7Measurements provided by the physical layer17

7.1UE measurements17

Annex A (informative):Change history18

## Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

xthe first digit:

1presented to TSG for information;

2presented to TSG for approval;

3or greater indicates TSG approved document under change control.

ythe second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

zthe third digit is incremented when editorial only changes have been incorporated in the document.

## 1Scope

The present document is a technical specification of the services provided by the physical layer of 5G-NR to upper layers.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications"

[2]3GPP TS 38.201: "NR; Physical Layer – General Description"

[3]3GPP TS 38.211: "NR; Physical channels and modulation"

[4]3GPP TS 38.212: "NR; Multiplexing and channel coding"

[5]3GPP TS 38.213: "NR; Physical layer procedures for control"

[6]3GPP TS 38.214: "NR; Physical layer procedures for data"

[7]3GPP TS 38.215: "NR; Physical layer measurements"

[8]3GPP TS 38.306: "NR; User Equipment (UE) radio access capabilities"

## 3Definitions of terms, symbols and abbreviations

## 3.1Terms

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

For the purposes of the present document, the following abbreviations apply:

ARQAutomatic Repeat Request

BCHBroadcast Channel

CACarrier Aggregation

CRCCyclic Redundancy Check

DCDual Connectivity

DLDownlink

FECForward Error Correction

GFGrant-Free

MACMedium Access Control

MIMOMultiple Input Multiple Output

PBCHPhysical Broadcast Channel

PCHPaging Channel

PDCCHPhysical Downlink Control Channel

PDSCHPhysical Downlink Shared Channel

PRACHPhysical Random Access Channel

PUCCHPhysical Uplink Control Channel

PUSCHPhysical Uplink Shared Channel

RACHRandom Access Channel

RFRadio Frequency

RNTIRadio Network Temporary Identifier

SCHShared Channel

SISystem Information

SPSSemi-Persistent Scheduling

SRSSounding Reference Signal

TPCTransmit Power Control

ULUplink

## 4Services and functions of the physical layer

## 4.1General

The physical layer offers data transport services to higher layers.

The access to these services is through the use of transport channels via the MAC sub-layer.

A transport block is defined as the data delivered by MAC layer to the physical layer and vice versa.

## 4.2Overview of L1 functions

As mentioned in [2, TS 38.201], the physical layer is expected to perform the following functions to provide the data transport service:

-Error detection on the transport channel and indication to higher layers;

-FEC encoding/decoding of the transport channel;

-Hybrid ARQ soft-combining;

-Rate matching of the coded transport channel to physical channels;

-Mapping of the coded transport channel onto physical channels;

-Power weighting of physical channels;

-Modulation and demodulation of physical channels;

-Frequency and time synchronisation;

-Radio characteristics measurements and indication to higher layers;

-Multiple Input Multiple Output (MIMO) antenna processing;

-RF processing.

L1 functions are modelled for each transport channel in clause 5.

## 5Model of physical layer of the UE

The 5G-NR physical-layer model captures those characteristics of the 5G-NR physical-layer that are relevant from the point-of-view of higher layers. More specifically, the physical-layer model captures:

-The structure of higher-layer data being passed down to or up from the physical layer;

-The means by which higher layers can configure the physical layer;

-The different indications (error indications, channel-quality indications, etc.) that are provided by the physical layer to higher layers.

## 5.1Uplink model

## 5.1.1Uplink shared channel

The physical-layer model for Uplink Shared Channel transmission is described based on the corresponding PUSCH physical-layer-processing chain, see Figure 5.1.1-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue.

-Higher-layer data passed to/from the physical layer

-CRC and transport-block-error indication

-FEC and rate matching

-Data modulation

-Mapping to physical resource

-Multi-antenna processing

-Support of L1 control and Hybrid-ARQ-related signalling

Figure 5.1.1-1: Physical-layer model for UL-SCH transmission

## 5.1.2Random access channel

The physical-layer model for RACH transmission is characterized by a PRACH preamble format that consists of a cyclic prefix, a preamble, and a guard time during which nothing is transmitted.

## 5.2Downlink model

## 5.2.1Downlink shared channel

The physical-layer model for Downlink Shared Channel transmission is described based on the corresponding PDSCH physical-layer-processing chain, see Figure 5.2.1-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue.

-Higher-layer data passed to/from the physical layer;

-CRC and transport-block-error indication;

-FEC and rate matching;

-Data modulation;

-Mapping to physical resource;

-Multi-antenna processing;

-Support of L1 control and Hybrid-ARQ-related signalling.

Figure 5.2.1-1: Physical-layer model for DL-SCH transmission

## 5.2.2Broadcast channel

The physical-layer model for BCH transmission is characterized by a fixed pre-defined transport format. There is one transport block for the BCH every 80ms. The BCH physical-layer model is described based on the corresponding PBCH physical-layer-processing chain, see Figure 5.2.2-1:

-Higher-layer data passed to/from the physical layer;

-CRC and transport-block-error indication;

-FEC and rate matching;

-Data modulation;

-Mapping to physical resource;

-Multi-antenna processing.

Figure 5.2.2-1: Physical-layer model for BCH transmission

## 5.2.3Paging channel

The physical-layer model for PCH transmission is described based on the corresponding physical-layer-processing chain, see Figure 5.2.3-1. The PCH is carried on PDSCH. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue.

-Higher-layer data passed to/from the physical layer;

-CRC and transport-block-error indication;

-FEC and rate matching;

-Data modulation;

-Mapping to physical resource;

-Multi-antenna processing.

Figure 5.2.3-1: Physical-layer model for PCH transmission

## 5.3Sidelink model

## 5.3.1Sidelink shared channel

The physical-layer model for Sidelink Shared Channel transmission is described based on the corresponding SL-SCH physical-layer-processing chain, see Figure 5.3.1-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue.

-Higher-layer data passed to/from the physical layer;

-CRC and transport-block-error indication;

-FEC and rate matching;

-Data modulation;

-Mapping to physical resource;

-Multi-antenna processing;

-Support of L1 control and Hybrid-ARQ-related signalling.

Figure 5.3.1-1: Physical-layer model for SL-SCH transmission

## 5.3.2Broadcast channel

The physical-layer model for Sidelink Broadcast Channel transmission is characterized by a fixed pre-defined transport format. There is one transport block for every slot in which the UE transmits SL-BCH, if the UE is configured to transmit on SL-BCH. The SL-BCH physical-layer model is described based on the corresponding SL-BCH physical-layer-processing chain, see Figure 5.3.2-1:

-Higher-layer data passed to/from the physical layer;

-CRC and transport-block-error indication;

-FEC and rate matching;

-Data modulation;

-Mapping to physical resource;

-Multi-antenna processing.

Figure 5.3.2-1: Physical-layer model for SL-BCH transmission

## 6Simultaneous transmission and reception of physical channels and physical signals

This clause describes the requirements from the UE to send and receive multiple physical channels and physical signals simultaneously depending on the capabilities and service requirements. The following notation is used between both the uplink and downlink clauses below.

-p is the number of uplink carriers configured for the UE on which physical channels can be transmitted

-p' is the number of uplink carriers configured for the UE on which SRS can be transmitted

-q is the number of downlink carriers configured for the UE

-j is the number of cell groups configured for the UE.

-k is the number of PUCCH groups configured for the UE.

## 6.1Uplink

The tables 6.1-1 and 6.1-2 describe the possible combinations of physical channels and SRS that can be sent in simultaneously in the uplink by one UE. Table 6.1-1 introduces notation for a "Transmission Type" which represents a physical channel or sounding reference signal, and any associated transport channel. Table 6.1-2 describes the combinations of these "Transmission Types" which are supported by the UE depending on capabilities [8, TS 38.306], and enumerates how many of each can be transmitted simultaneously.

Table 6.1-1: Uplink "Transmission Types"

Table 6.1-2: Uplink "Transmission Type" combinations

## 6.2Downlink

The tables 6.2-1, 6.2-2 describe the possible combinations of physical channels that can be received simultaneously in the downlink by one UE. Table 6.2-1 introduces notation for a "Reception Type" which represents a physical channel and any associated transport channel. Table 6.2-2 describes the combinations of these "Reception Types" which are supported by the UE depending on capabilities [8, TS 38.306], and enumerates how many of each can be received simultaneously. The UE shall be able to receive all TBs according to the indication on PDCCH. Any subset of the combinations specified in table 6.2-2 is also supported.

Table 6.2-1: Downlink "Reception Types"

Table 6.2-2: Downlink "Reception Type" combinations

## 6.3Sidelink

The tables 6.3-1 and 6.3-2 describe the possible combinations of physical channels that can be sent simultaneously in the sidelink by a UE. Table 6.3-1 introduces notation for a sidelink "Transmission Type" which represents a physical channel, and any associated transport channel. Table 6.3-2 describes the combinations of these "Transmission Types" which are supported by the UE depending on capabilities [8, TS 38.306], and enumerates how many of each can be transmitted simultaneously.

Table 6.3-1: Sidelink "Transmission Types"

Table 6.3-2: Sidelink "Transmission Type" combinations

The tables 6.3-3 and 6.3-4 describe the possible combinations of physical channels that can be received simultaneously in the sidelink by a UE. Table 6.3-3 introduces notation for a sidelink "Reception Type" which represents a physical channel, and any associated transport channel. Table 6.3-4 describes the combinations of these "Reception Types" which are supported by the UE depending on capabilities [8, TS 38.306], and enumerates how many of each can be received simultaneously.

Table 6.3-3: Sidelink "Reception Types"

Table 6.3-4: Sidelink "Reception Type" combinations

## 7Measurements provided by the physical layer

## 7.1UE measurements

The list and detailed definition of UE measurements is provided in [7, TS 38.215].

## Annex A (informative):Change history
