---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.201_38201-j00/content.md"
---
# TS 38.201 38201-j00

3GPP TS 38.201 V19.0.0 (2025-06)3GPP TS 38.201 V19.0.0 (2025-06)Technical SpecificationTechnical Specification3rd Generation Partnership Project;Technical Specification Group Radio Access Network;NR;Physical layer; General description(Release 19)3rd Generation Partnership Project;Technical Specification Group Radio Access Network;NR;Physical layer; General description(Release 19)The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP..The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP..The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords3GPP, New Radio, Layer 1Keywords3GPP, New Radio, Layer 1

3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org

Copyright NotificationNo part may be reproduced except as authorized by written permission.The copyright and the foregoing restriction extend to reproduction in all media.© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersLTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM AssociationCopyright NotificationNo part may be reproduced except as authorized by written permission.The copyright and the foregoing restriction extend to reproduction in all media.© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersLTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association

Contents

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

The present document provides a general description of the physical layer of NR radio interface. The present document also describes the document structure of the 3GPP physical layer specifications, i.e. TS 38.200 series.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications"

[2]3GPP TS 38.202: "NR; Services provided by the physical layer"

[3]3GPP TS 38.211: "NR; Physical channels and modulation"

[4]3GPP TS 38.212: "NR; Multiplexing and channel coding"

[5]3GPP TS 38.213: "NR; Physical layer procedures for control"

[6]3GPP TS 38.214: "NR; Physical layer procedures for data"

[7]3GPP TS 38.215: "NR; Physical layer measurements"

[8]3GPP TS 38.291: "NR; Ambient IoT Physical layer"

## 3Definitions of terms, symbols and abbreviations

## 3.1Terms

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

Definition format

<defined term>: <definition>.

example: text used to clarify abstract rules by applying them literally.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

Symbol format

<symbol><Explanation>

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

BPSKBinary Phase Shift Keying

CPCyclic Prefix

DFT-s-OFDMDiscrete Fourier Transform-spread-Orthogonal Frequency Division Multiplexing

DUDistributed Unit

E-UTRAEvolved Universal Terrestrial Radio Access

FDDFrequency Division Duplex

FECForward Error Correction

HARQHybrid Automatic Repeat Request

IABIntegrated Access and Backhaul

LDPCLow Density Parity Check

MACMedium Access Control

MIMOMultiple Input Multiple Output

MTMobile Termination

NCRNetwork-Controlled Repeater

OFDMOrthogonal Frequency Division Multiplexing

PBCHPhysical Broadcast Channel

PDCCHPhysical Downlink Control Channel

PDSCHPhysical Downlink Shared Channel

PRACHPhysical Random Access Channel

PSBCHPhysical Sidelink Broadcast Channel

PSCCHPhysical Sidelink Control Channel

PSFCHPhysical Sidelink Feedback Channel

PSSCHPhysical Sidelink Shared Channel

PUCCHPhysical Uplink Control Channel

PUSCHPhysical Uplink Shared Channel

QAMQuadrature Amplitude Modulation

QPSKQuadrature Phase Shift Keying

RLCRadio Link Control

RRCRadio Resource Control

SAPService Access Point

SRSSounding Reference Signal

TDDTime Division Duplex

UEUser Equipment

## 4General description of layer 1

## 4.1Relation to other layers

## 4.1.1General protocol architecture

The radio interface described in this specification covers the interface between the User Equipment (UE) and gNB, between gNBs, between IAB-node DU and IAB-node MT/UE, between gNB and NCR-MT, and between UEs. The radio interface is composed of the Layer 1, 2 and 3. The TS 38.200 series describes the Layer 1 (Physical Layer) specifications. Layers 2 and 3 are described in the 38.300 series.

Figure 1: Radio interface protocol architecture around the physical layer

Figure 1 shows the NR radio interface protocol architecture around the physical layer (Layer 1). The physical layer interfaces the Medium Access Control (MAC) sub-layer of Layer 2 and the Radio Resource Control (RRC) Layer of Layer 3. The circles between different layer/sub-layers indicate Service Access Points (SAPs). The physical layer offers a transport channel to MAC. The transport channel is characterized by how the information is transferred over the radio interface. MAC offers different logical channels to the Radio Link Control (RLC) sub-layer of Layer 2. A logical channel is characterized by the type of information transferred.

## 4.1.1AProtocol architecture for Ambient IoT

The radio interface described in this specification also covers the interface between device and reader. For the radio interface protocol architecture between device and reader, the physical layer interfaces the MAC sub-layer of Layer 2, and there is no RRC Layer of Layer 3. The physical layer offers two transport channels to MAC, one is for reader to device (R2D) and the other is for device to reader (D2R). Details are specified in [38.291, 38.391].

## 4.1.2Service provided to higher layers

The physical layer offers data transport services to higher layers. The access to these services is through the use of a transport channel via the MAC sub-layer. Details are specified in [2].

## 4.2General description of layer 1

## 4.2.1Multiple access

The multiple access scheme for the NR physical layer is based on Orthogonal Frequency Division Multiplexing (OFDM) with a cyclic prefix (CP). For uplink, Discrete Fourier Transform-spread-OFDM (DFT-s-OFDM) with a CP is also supported. To support transmission in paired and unpaired spectrum, both Frequency Division Duplex (FDD) and Time Division Duplex (TDD) are enabled.

The Layer 1 is defined in a bandwidth agnostic way based on resource blocks, allowing the NR Layer 1 to adapt to various spectrum allocations. A resource block spans 12 sub-carriers with a given sub-carrier spacing.

The radio frame has a duration of 10ms and consists of 10 sub-frames with a sub-frame duration of 1ms. A sub-frame is formed by one or multiple adjacent slots, each having 14 adjacent symbols. Further details on the frame structure are specified in [2].

## 4.2.2Physical channels and modulation

The physical channels defined in the downlink are:

-the Physical Downlink Shared Channel (PDSCH),

-the Physical Downlink Control Channel (PDCCH),

-the Physical Broadcast Channel (PBCH),

The physical channels defined in the uplink are:

-the Physical Random Access Channel (PRACH),

-the Physical Uplink Shared Channel (PUSCH),

-and the Physical Uplink Control Channel (PUCCH).

The physical channels defined in the sidelink are:

-the Physical Sidelink Broadcast Channel (PSBCH),

-the Physical Sidelink Control Channel (PSCCH),

-the Physical Sidelink Feedback Channel (PSFCH),

-and the Physical Sidelink Shared Channel (PSSCH).

In addition, signals are defined as reference signals, primary and secondary synchronization signals, wake-up signal and low-power synchronization signal.

The modulation schemes supported are

-in the downlink, QPSK, 16QAM, 64QAM, 256QAM, and 1024QAM,

-in the uplink, QPSK, 16QAM, 64QAM and 256QAM for OFDM with a CP and π/2-BPSK, QPSK, 16QAM, 64QAM and 256QAM for DFT-s-OFDM with a CP.

## 4.2.3Channel coding

The channel coding scheme for transport blocks is quasi-cyclic LDPC codes with 2 base graphs and 8 sets of parity check matrices for each base graph, respectively. One base graph is used for code blocks larger than certain sizes or with initial transmission code rate higher than thresholds; otherwise, the other base graph is used. Before the LDPC coding, for large transport blocks, the transport block is segmented into multiple code blocks with equal size. The channel coding scheme for PBCH and control information is Polar coding based on nested sequences. Puncturing, shortening and repetition are used for rate matching. Further details of channel coding schemes are specified in [4].

## 4.2.4Physical layer procedures

There are several Physical layer procedures involved. Such procedures covered by the physical layer are;

-Cell search

-Power control

-Uplink synchronisation and Uplink timing control

-Random access related procedures

-HARQ related procedures

-Beam management and CSI related procedures

-Sidelink related procedures

-Channel access procedures

Through the control of physical layer resources in the frequency domain as well as in the time and power domains, implicit support of interference coordination is provided in NR.

## 4.2.5Physical layer measurements

Radio characteristics are measured by the UE and the network and reported to higher layers. These include, e.g. measurements for intra- and inter-frequency handover, inter RAT handover, timing measurements, and measurements for RRM.

Measurements for inter-RAT handover are defined in support of handover to E-UTRA.

## 4.2.6Physical layer of Ambient IoT

The physical channel defined for R2D is:

-the Physical Reader-to-Device Channel (PRDCH).

The physical channel defined for D2R is:

-the Physical Device-to-Reader Channel (PDRCH).

In addition, signals are defined as R2D timing acquisition signal (R-TAS), R2D postamble signal and D2R amble signal.

The modulation schemes supported are

-for R2D, line encoding with OOK modulation;

-for D2R, modulation of OOK or BPSK, resulting in small frequency shift.

The channel coding scheme for D2R is tail biting convolutional code.

Physical layer procedures for Ambient IoT are:

-PDRCH and D2R amble signal transmission;

-R-TAS reception;

-PRDCH reception;

-Monitoring of R2D.

## 5Document structure of physical layer specification

## 5.1Overview

The physical layer specification consists of a general document (TS 38.201), and seven documents (TS 38.202, 38.211 through 38.215, and 37.213). The relation between the physical layer specifications in the context of the higher layers is shown in Figure 2.

Figure 2: Relation between Physical Layer specifications

## 5.2TS 38.201: Physical layer; General description

The scope is to describe:

-The contents of the Layer 1 documents (TS 38.200 series);

-Where to find information;

## 5.3TS 38.202: Physical layer services provided by the physical layer

The scope is to describe services provided by the physical layer, and to specify:

-Services and functions of the physical layer;

-Model of physical layer of the UE;

-Parallel transmission of simultaneous physical channels and SRS;

-Measurements provided by the physical layer.

## 5.4TS 38.211: Physical channels and modulation

The scope is to establish the characteristics of the Layer-1 physical channels, generation of physical layer signals and modulation, and to specify:

-Definition of the uplink, downlink and sidelink physical channels;

-Frame structure and physical resources;

-Modulation mapping (BPSK, QPSK, etc);

-OFDM signal generation;

-Scrambling, modulation and upconversion;

-Layer mapping and precoding;

-Physical shared channel in uplink, downlink and sidelink;

-Reference signal in uplink, downlink and sidelink;

-Physical random access channel;

-Primary and secondary synchronization signals;

-Wake-up signal and low-power synchronization signal.

## 5.5TS 38.212: Multiplexing and channel coding

The scope is to describe the transport channel and control channel data processing, including multiplexing, channel coding and interleaving, and to specify:

-Channel coding schemes;

-Rate matching;

-Uplink transport channels and control information;

-Downlink transport channels and control information;

-Sidelink transport channels and control information.

## 5.6TS 38.213: Physical layer procedures for control

The scope is to establish the characteristics of the physical layer procedures for control, and to specify:

-Synchronization procedures;

-Uplink power control;

-Random access procedure;

-UE procedure for reporting control information;

-UE procedure for receiving control information.

## 5.7TS 38.214: Physical layer procedures for data

The scope is to establish the characteristics of the physical layer procedures for data, and to specify:

-Power control;

-Physical downlink shared channel related procedures;

-Physical uplink shared channel related procedure;

-Physical sidelink shared channel related procedure.

## 5.8TS 38.215: Physical layer measurements

The scope is to establish the characteristics of the physical layer measurements, and to specify:

-Control of UE/NG-RAN measurements;

-Measurement capabilities for NR.

## 5.9TS 37.213: Physical layer procedures for shared spectrum channel access

The scope is to establish the characteristics of the physical layer procedures for shared spectrum channel, and to specify:

-Downlink channel access procedures;

-Uplink channel access procedures;

-Sidelink channel access procedures.

## 5.10TS 38.291: Ambient IoT Physical layer

The scope is to establish the characteristics of the physical layer of Ambient IoT, and to specify:

-Time and frequency domain structures;

-Physical channels and signals generation;

-Physical layer procedures.

## Annex A (informative):Preferred mathematical notations

The following table contains the preferred mathematical notations used in L1 documentation.

## Annex B (informative):Change history
