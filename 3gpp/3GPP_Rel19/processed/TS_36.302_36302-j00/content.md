---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.302_36302-j00/content.md"
---
# TS 36.302 36302-j00

3GPP TS 36.302 V19.0.0 (2025-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

Evolved Universal Terrestrial Radio Access (E-UTRA); Services provided by the physical layer

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords

UTRAN, radio, layer 1

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

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Contents

Foreword4

1Scope5

2References5

3Definitions and abbreviations6

3.1Definitions6

3.2Abbreviations6

4Void8

4.1Void8

4.2Void8

5Services and functions of the physical layer8

5.1General8

5.2Overview of L1 functions8

5.3Void9

6Model of physical layer of the UE9

6.1Uplink model9

6.1.1Uplink Shared Channel9

6.1.2Random-access Channel10

6.2Downlink model11

6.2.1Downlink-Shared Channel11

6.2.2Broadcast Channel12

6.2.3Paging Channel13

6.2.4Multicast Channel14

6.3Sidelink model15

6.3.1Sidelink Broadcast Channel15

6.3.2Sidelink Discovery Channel16

6.3.3Sidelink Shared Channel17

7Void18

8Parallel transmission of simultaneous Physical Channels and SRS18

8.1Uplink19

8.2Downlink20

8.3Sidelink29

9Measurements provided by the physical layer31

9.1Void31

9.2UE Measurements31

9.3E-UTRAN Measurements31

Annex A (informative): Change history32

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

The present document is a technical specification of the services provided by the physical layer of E-UTRA to upper layers.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or non specific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]Void

[2]Void

[3]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[4]Void

[5]Void

[6]Void

[7]Void

[8]3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[9]Void

[10]Void

[11]3GPP TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements".

[12]3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[13]3GPP TS 36.306: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio access capabilities".

[14]3GPP TS 23.303: "Technical Specification Group Services and System Aspects; Proximity-based services (ProSe)".

[15]Void

[16]3GPP TS 23.285: "Technical Specification Group Services and System Aspects; Architecture enhancements for V2X services".

[17]3GPP TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRAN); Overall description; Stage 2".

## 3Definitions and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [3] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [3].

Carrier frequency: center frequency of the cell.

Frequency layer: set of cells with the same carrier frequency.

NB-IoT: NB-IoT allows access to network services via E-UTRA with a channel bandwidth limited to 200 kHz.

Short Processing Time: For 1 ms TTI length, the operation with short processing time in UL data transmission and DL data reception.

Short TTI: TTI length based on a slot or a subslot.

Sidelink: UE to UE interface for sidelink communication, V2X sidelink communication and sidelink discovery. The sidelink corresponds to the PC5 interface as defined in TS 23.303 [14].

Sidelink communication: AS functionality enabling ProSe Direct Communication as defined in TS 23.303 [14], between two or more nearby UEs, using E-UTRA technology but not traversing any network node. In this version, the terminology "sidelink communication" without "V2X" prefix only concerns PS unless explicitly stated otherwise.

Sidelink discovery: AS functionality enabling ProSe Direct Discovery as defined in TS 23.303 [14], using E-UTRA technology but not traversing any network node.

V2X Sidelink communication: AS functionality enabling V2X Communication as defined in TS 23.285 [16], between nearby UEs, using E-UTRA technology but not traversing any network node.

Timing Advance Group: See the definition in TS 36.321 [12].

Transmission using PUR: Allows one uplink data transmission using preconfigured uplink resource from RRC_IDLE mode as specified in TS 36.300 [17]. Transmission using PUR refers to both CP transmission using PUR and UP transmission using PUR.

## 3.2Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [3] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [3].

For the purposes of the present document, the following abbreviations apply:

ACKAcknowledgement

ARQAutomatic Repeat Request

BCCHBroadcast Control Channel

BCHBroadcast Channel

BLBandwidth reduced Low complexity

BLERBlock Error Rate

CGCell Group

CMASCommercial Mobile Alert System

CPCyclic Prefix

C-planeControl Plane

CRCCyclic Redundancy Check

CSIChannel State Information

DCDual Connectivity

DCCHDedicated Control Channel

DLDownlink

DRXDiscontinuous Reception

DTCHDedicated Traffic Channel

DTXDiscontinuous Transmission

eNBE-UTRAN NodeB

eIMTAEnhanced Interference Management and Traffic Adaptation

EPDCCHEnhanced physical downlink control channel

E-UTRAEvolved UTRA

E-UTRANEvolved UTRAN

FDDFrequency Division Duplex

FDMFrequency Division Multiplexing

FSFrame Structure

GERANGSM EDGE Radio Access Network

GSMGlobal System for Mobile communication

HARQHybrid ARQ

LAALicensed-Assisted Access

LTELong Term Evolution

MACMedium Access Control

MBMSMultimedia Broadcast Multicast Service

MBSFNMultimedia Broadcast multicast service Single Frequency Network

MCCHMulticast Control Channel

MCHMulticast Channel

MCSModulation and Coding Scheme

MIMOMultiple Input Multiple Output

MTCHMulticast Traffic Channel

MWUSMTC Wake Up Signal

NACKNegative Acknowledgement

NB-IoTNarrow Band Internet of Things

NPBCHNarrow Band Physical Broadcast Channel

NPDCCHNarrow Band Physical Downlink Control Channel

NPDSCHNarrow Band Physical Downlink Shared Channel

NPRACHNarrow Band Physical Random Access Channel

NPUSCHNarrow Band Physical Uplink Shared Channel

NWUSNarrow Band Wake Up Signal

OFDMOrthogonal Frequency Division Multiplexing

OFDMAOrthogonal Frequency Division Multiple Access

PBCHPhysical broadcast channel

PDCCHPhysical downlink control channel

PDSCHPhysical downlink shared channel

PHYPhysical layer

PMCHPhysical multicast channel

PRACHPhysical random access channel

PRBPhysical Resource Block

ProSeProximity based Services

PSBCHPhysical Sidelink Broadcast CHannel

PSCCHPhysical Sidelink Control Channel

PSCellPrimary SCell

PSDCHPhysical Sidelink Discovery Channel

PSSCHPhysical Sidelink Shared CHannel

PUCCHPhysical uplink control channel

PURPreconfigured Uplink Resource

PUSCHPhysical uplink shared channel

QAMQuadrature Amplitude Modulation

RACHRandom Access Channel

RFRadio Frequency

RRCRadio Resource Control

SAPService Access Point

SBCCHSidelink Broadcast Control CHannel

SC-FDMASingle Carrier – Frequency Division Multiple Access

SCellSecondary Cell

SC-PTMSingle Cell Point to Multipoint

SL-BCHSidelink Broadcast Channel

SL-DCHSidelink Discovery Channel

SL-SCHSidelink Shared Channel

SPDCCHShort PDCCH

SPTShort Processing Time

SPUCCHShort PUCCH

SRSSounding Reference Symbol

STCHSidelink Traffic Channel

TAGTiming Advance Group

TBTransport Block

TDDTime Division Duplex

TTITransmission Time Interval

UEUser Equipment

ULUplink

UMTSUniversal Mobile Telecommunication System

U-planeUser plane

UTRAUniversal Terrestrial Radio Access

UTRANUniversal Terrestrial Radio Access Network

V2XVehicle-to-Everything

## 4Void

## 4.1Void

## 4.2Void

## 5Services and functions of the physical layer

## 5.1General

The physical layer offers data transport services to higher layers.

The access to these services is through the use of transport channels via the MAC sub-layer.

A transport block is defined as the data delivered by MAC layer to the physical layer and vice versa. Transport blocks are delivered once every TTI.

## 5.2Overview of L1 functions

The physical layer offers data transport services to higher layers. The access to these services is through the use of a transport channel via the MAC sub-layer. The physical layer is expected to perform the following functions in order to provide the data transport service:

-Error detection on the transport channel and indication to higher layers

-FEC encoding/decoding of the transport channel

-Hybrid ARQ soft-combining

-Rate matching of the coded transport channel to physical channels

-Mapping of the coded transport channel onto physical channels

-Power weighting of physical channels

-Modulation and demodulation of physical channels

-Frequency and time synchronisation

-Radio characteristics measurements and indication to higher layers

-Multiple Input Multiple Output (MIMO) antenna processing

-Transmit Diversity (TX diversity)

-Beamforming

-RF processing.

L1 functions are modelled for each transport channel in clauses 6.1, 6.2 and 6.3.

## 5.3Void

## 6Model of physical layer of the UE

The E-UTRA physical-layer model captures those characteristics of the E-UTRA physical-layer that are relevant from the point-of-view of higher layers. More specifically, the physical-layer model captures:

-The structure of higher-layer data being passed down to or up from the physical layer;

-The means by which higher layers can configure the physical layer;

-The different indications (error indications, channel-quality indications, etc.) that are provided by the physical layer to higher layers;

-Other (non-transport-channel-based) higher-layer peer-to-peer signalling supported by the physical layer.

## 6.1Uplink model

## 6.1.1Uplink Shared Channel

The physical-layer model for Uplink Shared Channel transmission is described based on the corresponding physical-layer-processing chain, see Figure 6.1.1-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue. It should be noted that, in the cases of PUSCH and NPUSCH, the scheduling decision is fully done at the network side. The uplink transmission control in the UE then configures the uplink physical-layer processing, based on uplink transport-format and resource-assignment information received on the downlink.

-Higher-layer data passed to/from the physical layer

-One transport block of dynamic size delivered to the physical layer once every TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-Physical layer model support of HARQ: in case of Incremental Redundancy, the corresponding Layer 2 Hybrid-ARQ process controls what redundancy version is to be used for the physical layer transmission for each TTI.

-Interleaving

-No control of interleaving by higher layers.

-Data modulation

-Modulation scheme is decided by MAC Scheduler (QPSK, 16QAM, 64QAM, and 256QAM; for BL UEs or UEs in enhanced coverage, supported modulation schemes are QPSK and 16QAM; for NB-IoT, supported modulation schemes are Pi/4-QPSK and Pi/2-BPSK for single-tone allocation, QPSK and 16QAM for multi-tone allocation).

-Mapping to physical resource

-L2-controlled resource assignment.

-Multi-antenna processing

-MAC Scheduler partly configures mapping from assigned resource blocks to the available number of antenna ports.

-Support of L1 control signalling

-Transmission of ACK/NACK and CSI feedback related to DL data transmission

The model of Figure 6.1.1-1 also captures

-Transport via physical layer of Hybrid-ARQ related information associated with the PUSCH, to the peer HARQ process at the transmitter side;

-Transport via physical layer of corresponding HARQ acknowledgements to PUSCH transmitter side (except for NB-IoT UEs).

If a UE is configured with one or more SCells, the physical-layer-processing chain in Figure 6.1.1-1 is repeated for every UL Serving Cell.

Figure 6.1.1-1: Physical-layer model for UL-SCH transmission

## 6.1.2Random-access Channel

The physical-layer model for RACH transmission is characterized by a random access burst that consists of a cyclic prefix, a preamble, and a guard time during which nothing is transmitted.

The random access preambles are generated from Zadoff-Chu sequences with zero correlation zone (ZC-ZCZ), generated from one or several root Zadoff-Chu sequences. For NB-IoT, the random access preambles are generated from single-subcarrier frequency-hopping symbol groups. A symbol group consists of a cyclic prefix followed by five identical symbols, whose value is constant across symbol groups during each NPRACH transmission.

## 6.2Downlink model

## 6.2.1Downlink-Shared Channel

The physical-layer model for Downlink Shared Channel transmission is described based on the corresponding PDSCH or NPDSCH physical-layer-processing chain, see Figure 6.2.1-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue on the figure.

-Higher-layer data passed to/from the physical layer

-N (up to two) transport blocks of dynamic size delivered to the physical layer once every TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-Physical layer model support of HARQ: in case of Incremental Redundancy, the corresponding Layer 2 Hybrid-ARQ process controls what redundancy version is to be used for the physical layer transmission for each TTI.

-Data modulation

-Modulation scheme is decided by MAC Scheduler (QPSK, 16QAM, 64 QAM, 256QAM, and 1024QAM; for BL UEs or UEs in enhanced coverage, supported modulation schemes are QPSK and 16QAM, and 64QAM for CE mode A with no repetitions; for NB-IoT, QPSK and 16QAM are supported).

Multi-antenna processing

-MAC Scheduler partly configures mapping from modulated code words (for each stream) to the available number of antenna ports.

-Mapping to physical resource

-L2-controlled resource assignment.

-Support of L1 control signalling

-Transmission of scheduler related control signals.

-Support for Hybrid-ARQ-related signalling

The model of Figure 6.2.1-1 also captures:

-Transport via physical layer of Hybrid-ARQ related information associated with the PDSCH, to the peer HARQ process at the receiver side;

-Transport via physical layer of corresponding HARQ acknowledgements to PDSCH transmitter side.

If a UE is configured with one or more SCells, the physical-layer-processing chain in Figure 6.2.1-1 is repeated for every DL Serving Cell.

NOTE:The signalling of transport-format and resource-allocation is not captured in the physical-layer model. At the transmitter side, this information can be directly derived from the configuration of the physical layer. The physical layer then transports this information over the radio interface to its peer physical layer, presumably multiplexed in one way or another with the HARQ-related information. On the receiver side, this information is, in contrast to the HARQ-related information, used directly within the physical layer for PDSCH demodulation, decoding etc., without passing through higher layers.

Figure 6.2.1-1: Physical-layer model for DL-SCH transmission

## 6.2.2Broadcast Channel

The physical-layer model for BCH transmission is characterized by a fixed pre-defined transport format. The TTI (repetition rate) of the BCH is 40 ms except for NB-IoT and 640 ms for NB-IoT. The BCH physical-layer model is described based on the corresponding BCH physical-layer-processing chain, see Figure 6.2.2-1:

-Higher-layer data passed to/from the physical layer

-A single (fixed-size) transport block per TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-No BCH Hybrid ARQ, i.e. no higher-layer control of redundancy version.

-Data modulation

-Fixed modulation scheme (QPSK), i.e. no higher-layer control.

-Mapping to physical resource

-Fixed pre-determined transport format and resource allocation, i.e. no higher-layer control.

-Multi-antenna processing

-Fixed pre-determined processing, i.e. no higher-layer control.

-Support for Hybrid-ARQ-related signalling

-No Hybrid ARQ.

Figure 6.2.2-1: Physical-layer model for BCH transmission

NOTE:For NB-IoT, the BCH transport block of 40 bits is truncated to 34 bits by the NodeB when provided to the physical layer for BCH transmission. The BCH transport block of 34 bits is padded to 40 bits when delivered by the UE physical layer to the upper layer.

## 6.2.3Paging Channel

The physical-layer model for PCH transmission is described based on the corresponding PCH physical-layer-processing chain, see Figure 6.2.3-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue on the figure.

-Higher-layer data passed to/from the physical layer

-A single transport block per TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-No PCH Hybrid ARQ, i.e. no higher-layer control of redundancy version.

-Data modulation

-Modulation scheme is decided by MAC Scheduler.

-Mapping to physical resource

-L2 controlled resource assignment;

-Possible support of dynamic transport format and resource allocation.

-Multi-antenna processing

-MAC Scheduler partly configures mapping from assigned resource blocks to the available number of antenna ports.

-Support for Hybrid-ARQ-related signalling

No Hybrid ARQ.

Figure 6.2.3-1: Physical-layer model for PCH transmission

## 6.2.4Multicast Channel

The physical-layer model for MCH transmission is characterized by the support for multi-cell reception at the UE (a.k.a. "MBSFN" transmission). This implies that only semi-static configuration of the MCH transport format and resource assignment is possible. The MCH physical-layer model is described based on the corresponding MCH physical-layer-processing chain, see Figure 6.2.4-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue.

-Higher-layer data passed to/from the physical layer

-One transport block delivered to physical layer once every TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-No MCH Hybrid ARQ, i.e. no higher-layer control of redundancy version.

-Data modulation

-Modulation scheme is configured by RRC layer.

-Mapping to physical resource

-L2 controlled semi–static resource assignment.

-Multi-antenna processing

-MAC Scheduler partly configures mapping from assigned resource blocks (for each stream) to the available number of antenna ports.

-Support for Hybrid-ARQ-related signalling

-No Hybrid ARQ.

Figure 6.2.4-1: Physical-layer model for MCH transmission

## 6.3Sidelink model

## 6.3.1Sidelink Broadcast Channel

The physical-layer model for Sidelink Broadcast Channel transmission is characterized by a fixed pre-defined transport format. The TTI (repetition rate) of the SL-BCH not corresponding to V2X sidelink communication is 40ms whereas the TTI (repetition rate) of the SL-BCH corresponding to V2X sidelink communication is 160 ms, if a UE is configured to transmit on SL-BCH. The SL-BCH physical-layer model is described based on the corresponding SL-BCH physical-layer-processing chain, see Figure 6.3.1-1.

-Higher-layer data passed to/from the physical layer

-A single (fixed-size) transport block per TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-No SL-BCH Hybrid ARQ, i.e. no higher-layer control of redundancy version.

-Data modulation

-Fixed modulation scheme (QPSK), i.e. no higher-layer control.

-Mapping to physical resource

-Fixed pre-determined transport format i.e. no higher-layer control.

-RRC controlled semi-static resource assignment.

-Multi-antenna processing

-Single antenna port is used.

-Support for Hybrid-ARQ-related signalling

-No Hybrid ARQ.

Figure 6.3.1-1: Physical-layer model for SL-BCH transmission

## 6.3.2Sidelink Discovery Channel

The physical-layer model for Sidelink Discovery Channel transmission is characterized by a fixed pre-defined transport format. The SL-DCH physical-layer model is described based on the corresponding SL-DCH physical-layer-processing chain, see Figure 6.3.2-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue. It should be noted that, in case scheduled resource allocation of SL-DCH, the scheduling decision is fully done by network side. The sidelink transmission control in the UE configures the sidelink physical-layer processing, based on sidelink transport-format and resource-assignment information received on the downlink. In case UE autonomous resource selection of SL-DCH, the scheduling decision is done by UE side. The sidelink transmission control in the UE configures the sidelink physical-layer processing, based on pre-defined sidelink transport-format and UE randomly selected resource-assignment.

-Higher-layer data passed to/from the physical layer

-A single (fixed-size) transport block per TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layer.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-Support for soft combining, but no support for ACK/NACK feedback.

-Data modulation

-Fixed modulation scheme (QPSK), i.e. no higher-layer control.

-Mapping to physical resource

-RRC controlled semi-static resource assignment;

-Multi-antenna processing

-Single antenna port is used.

Figure 6.3.2-1: Physical-layer model for SL-DCH transmission

## 6.3.3Sidelink Shared Channel

The physical-layer model for Sidelink Shared Channel transmission is described based on the corresponding SL-SCH physical-layer-processing chain, see Figure 6.3.3-1. Processing steps that are relevant for the physical-layer model, e.g. in the sense that they are configurable by higher layers, are highlighted in blue on the figure. It should be noted that, in case of scheduled resource allocation, the SL-SCH scheduling decision is done by network side. The sidelink transmission control in the UE configures the sidelink physical-layer processing, based on sidelink transport-format and resource-assignment information received on the downlink. In case of UE autonomous resource selection, the SL-SCH scheduling decision is done by UE side, and the MAC scheduler in the UE configures the sidelink physical-layer processing, based on the sidelink transport-format autonomously decided by the UE and autonomously selected resource-assignment.

-Higher-layer data passed to/from the physical layer

-One transport block of dynamic size delivered to the physical layer once every TTI.

-CRC and transport-block-error indication

-Transport-block-error indication delivered to higher layers.

-FEC and rate matching

-Channel coding rate is implicitly given by the combination of transport block size, modulation scheme and resource assignment;

-Support for soft combining, but no support for ACK/NACK feedback.

-Data modulation

-For scheduled resource allocation, modulation scheme is decided by higher layer signaling from eNB.

-For UE autonomous resource selection for sidelink communication, modulation scheme is decided by MAC scheduler (QPSK, 16QAM) in transmitter UE. For UE autonomous resource selection for V2X sidelink communication, modulation scheme is decided by MAC scheduler (QPSK, 16QAM, 64QAM) in transmitter UE.

-For UE autonomous resource selection for V2X sidelink communication, modulation scheme is decided by MAC scheduler in transmitter UE, according to the range defined by higher layer signalling from eNB or preconfiguration if configured.

-Mapping to physical resource

-L2-controlled resource assignment.

-Multi-antenna processing

-Single antenna port is used.

Figure 6.3.3-1: Physical-layer model for SL-SCH transmission

NOTE:For UE autonomous resource selection for V2X sidelink communication, the MAC scheduler in the transmitter UE decides whether to use 64QAM for data modulation based on UE capability, see TS 36.306 [13].

## 7Void

## 8Parallel transmission of simultaneous Physical Channels and SRS

This clause describes the requirements from the UE to send and receive on multiple Physical and Transport Channels and SRS simultaneously depending on the service capabilities and requirements.

## 8.1Uplink

The table 8.1-1 describes the possible combinations of physical channels that can be sent in parallel in the uplink within the same subframe/slot/subslot. For NB-IoT, see Table 8.1-1a.

Table 8.1-1: Uplink

Table 8.1-1a: Uplink for NB-IoT

The table 8.1-2 describes the possible combinations of SRS and physical channels that can be sent in parallel in uplink in the last symbol within the same subframe/slot/subslot by one UE. Table 8.1-2 is not applicable for NB-IoT.

Table 8.1-2: Uplink in combinations with SRS

## 8.2Downlink

The tables describe the possible combinations of physical channels that can be received in parallel in the downlink in the same subframe by one UE. In one subframe, the UE shall be able to receive all TBs according to the indication on PDCCH. Tables 8.2-1, 8.2-1a, 8.2-2 and 8.2-2a are applicable to LTE; Tables 8.2-1b and 8.2-2b are applicable to NB-IoT.

Table 8.2-1: Downlink "Reception Types" except for NB-IoT UEs, BL UEs and UEs in enhanced coverage

Table 8.2-1a: Downlink "Reception Types" for BL UEs and UEs in enhanced coverage

Table 8.2-1b: Downlink "Reception Types" for NB-IoT UEs

The "Reception Type" used in Table 8.2-2 refers to the "Reception Type" in Table 8.2-1.

Table 8.2-2: Downlink "Reception Type" Combinations except for NB-IoT UEs, BL UEs and UEs in enhanced coverage

The "Reception Type" used in Table 8.2-2a refers to the "Reception Type" in Table 8.2-1a.

Table 8.2-2a: Downlink "Reception Type" Combinations for BL UEs and UEs in enhanced coverage

NOTE:Any subset of the combinations specified in table 8.2-2 and 8.2-2a are also supported.

The "reception type" names in Table 8.2-2b refer to the "reception types" from Table 8.2-1b.

Table 8.2-2b: Downlink "Reception Type" Combinations for NB-IoT UEs

## 8.3Sidelink

The table 8.3-1 describes the possible combinations of physical channels that can be sent in parallel from UE perspective in the sidelink within the same subframe. Table 8.3-2 describes the possible combinations of physical channels that can be received in parallel from UE perspective in the sidelink within the same subframe.

Table 8.3-1: Sidelink transmission

Table 8.3-2: Sidelink reception

## 9Measurements provided by the physical layer

## 9.1Void

## 9.2UE Measurements

The list and detailed definition of UE measurements definition is provided in TS 36.214 [11].

## 9.3E-UTRAN Measurements

The list and detailed definition of E-UTRAN measurements definition is provided in TS 36.214 [11].

## Annex A (informative):Change history
