| 3GPP TS 36.201 V19.0.0 (2025-09) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;Evolved Universal Terrestrial Radio Access (E-UTRA);LTE physical layer; General description(Release 19) |  |
|  |  |
| ![](media/image1.emf) | ![](media/image2.emf) |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttps://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 4

1 Scope 6

2 References 6

3 Definitions of terms, symbols and abbreviations 6

3.1 Terms 6

3.2 Symbols 6

3.3 Abbreviations 7

4 General description of LTE Layer 1 8

4.1 Relation to other layers 8

4.1.1 General protocol architecture 8

4.1.2 Service provided to higher layers 8

4.2 General description of Layer 1 9

4.2.1 Multiple access 9

4.2.2 Physical channels and modulation 10

4.2.3 Channel coding and interleaving 11

4.2.4 Physical layer procedures 11

4.2.5 Physical layer measurements 11

5 Document structure of LTE physical layer specification 12

5.1 Overview 12

5.2 TS 36.201: Physical layer – General description 12

5.3 TS 36.211: Physical channels and modulation 12

5.4 TS 36.212: Multiplexing and channel coding 13

5.5 TS 36.213: Physical layer procedures 13

5.6 TS 36.214: Physical layer – Measurements 13

5.7 TS 36.216: Physical layer for relaying operation 14

Annex A (informative): Preferred mathematical notations 15

Annex B (informative): Change history 16

# Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

## 1 presented to TSG for information;

## 2 presented to TSG for approval;

## 3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.

In the present document, modal verbs have the following meanings:

shall indicates a mandatory requirement to do something

shall not indicates an interdiction (prohibition) to do something

The constructions "shall" and "shall not" are confined to the context of normative provisions, and do not appear in Technical Reports.

The constructions "must" and "must not" are not used as substitutes for "shall" and "shall not". Their use is avoided insofar as possible, and they are not used in a normative context except in a direct citation from an external, referenced, non-3GPP document, or so as to maintain continuity of style when extending or modifying the provisions of such a referenced document.

should indicates a recommendation to do something

should not indicates a recommendation not to do something

may indicates permission to do something

need not indicates permission not to do something

The construction "may not" is ambiguous and is not used in normative elements. The unambiguous constructions "might not" or "shall not" are used instead, depending upon the meaning intended.

can indicates that something is possible

cannot indicates that something is impossible

The constructions "can" and "cannot" are not substitutes for "may" and "need not".

will indicates that something is certain or expected to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

will not indicates that something is certain or expected not to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

might indicates a likelihood that something will happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

might not indicates a likelihood that something will not happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

In addition:

is (or any other verb in the indicative mood) indicates a statement of fact

is not (or any other negative verb in the indicative mood) indicates a statement of fact

The constructions "is" and "is not" do not indicate requirements.

# 1 Scope

The present document describes a general description of the physical layer of the E-UTRA radio interface. The present document also describes the document structure of the 3GPP physical layer specifications, i.e. TS 36.200 series. The TS 36.200 series specifies the Uu and Un points for the 3G LTE mobile system, and defines the minimum level of specifications required for basic connections in terms of mutual connectivity and compatibility.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies.  In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[3] 3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[4] 3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[5] 3GPP TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer – Measurements".

[6] 3GPP TS 36.216: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer for relaying operation".

# 3 Definitions of terms, symbols and abbreviations

## 3.1 Terms

For the purposes of the present document, the terms given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

Definition format (Normal)

<defined term>: <definition>.

example: text used to clarify abstract rules by applying them literally.

## 3.2 Symbols

For the purposes of the present document, the following symbols apply:

Symbol format (EW)

<symbol> <Explanation>

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905[1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

BPSK Binary Phase Shift Keying

CoMP Coordinated Multi-Point

CP Cyclic Prefix

CQI Channel Quality Indicator

CRC Cyclic Redundancy Check

CSI Channel State Information

eNode-B Evolved Node B

EPDCCH Enhanced Physical Downlink Control Channel

E-UTRA Evolved Universal Terrestrial Radio Access

FDD Frequency Division Duplex

HARQ Hybrid Automatic Repeat Request

LAA Licensed-Assisted Access

LTE Long Term Evolution

MAC Medium Access Control

MBMS Multimedia Broadcast and Multicast Service

MBSFN Multicast/Broadcast over Single Frequency Network

MIMO Multiple Input Multiple Output

MPDCCH MTC Physical Downlink Control Channel

MTC Machine Type Communications

NPBCH Narrowband Physical Broadcast Channel

NPDCCH Narrowband Physical Downlink Control Channel

NPDSCH Narrowband Physical Downlink Shared Channel

NPRACH Narrowband Physical Random Access Channel

NPUSCH Narrowband Physical Uplink Shared Channel

OFDM Orthogonal Frequency Division Multiplexing

PBCH Physical Broadcast Channel

PCFICH Physical Control Format Indicator Channel

PDSCH Physical Downlink Shared Channel

PDCCH Physical Downlink Control Channel

PHICH Physical Hybrid ARQ Indicator Channel

PMCH Physical Multicast Channel

PRACH Physical Random Access Channel

ProSe Proximity Services

PSBCH Physical Sidelink Broadcast Channel

PSCCH Physical Sidelink Control Channel

PSDCH Physical Sidelink Discovery Channel

PSSCH Physical Sidelink Shared Channel

PUCCH Physical Uplink Control Channel

PUSCH Physical Uplink Shared Channel

QAM Quadrature Amplitude Modulation

QPP Quadratic Permutation Polynomial

QPSK Quadrature Phase Shift Keying

RLC Radio Link Control

RN Relay Node

R-PDCCH Relay Physical Downlink Control Channel

RRC Radio Resource Control

RSSI Received Signal Strength Indicator

RSRP Reference Signal Received Power

RSRQ Reference Signal Received Quality

SAP Service Access Point

SC-FDMA Single-Carrier Frequency Division Multiple Access

SPDCCH Short Physical Downlink Control Channel

SPUCCH Short Physical Uplink Control Channel

TDD Time Division Duplex

TX Diversity Transmit Diversity

UE User Equipment

V2X Vehicle-to-Everything

# 4 General description of LTE Layer 1

## 4.1 Relation to other layers

### 4.1.1 General protocol architecture

The radio interface described in this specification covers the interface between the User Equipment (UE) and the network, and sidelink transmissions between UEs. The radio interface is composed of the Layer 1, 2 and 3. The TS 36.200 series describes the Layer 1 (Physical Layer) specifications. Layers 2 and 3 are described in the 36.300 series.

Figure 1: Radio interface protocol architecture around the physical layer

Figure 1 shows the E-UTRA radio interface protocol architecture around the physical layer (Layer 1). The physical layer interfaces the Medium Access Control (MAC) sub-layer of Layer 2 and the Radio Resource Control (RRC) Layer of Layer 3. The circles between different layer/sub-layers indicate Service Access Points (SAPs). The physical layer offers a transport channel to MAC. The transport channel is characterized by how the information is transferred over the radio interface. MAC offers different logical channels to the Radio Link Control (RLC) sub-layer of Layer 2. A logical channel is characterized by the type of information transferred.

### 4.1.2 Service provided to higher layers

The physical layer offers data transport services to higher layers. The access to these services is through the use of a transport channel via the MAC sub-layer. The physical layer is expected to perform the following functions in order to provide the data transport service:

- Error detection on the transport channel and indication to higher layers

- FEC encoding/decoding of the transport channel

- Hybrid ARQ soft-combining

- Rate matching of the coded transport channel to physical channels

- Mapping of the coded transport channel onto physical channels

- Power weighting of physical channels

- Modulation and demodulation of physical channels

- Frequency and time synchronisation

- Radio characteristics measurements and indication to higher layers

- Multiple Input Multiple Output (MIMO) antenna processing

- Transmit Diversity (TX diversity)

- Beamforming

- RF processing. (Note: RF processing aspects are specified in the TS 36.100 series)

## 4.2 General description of Layer 1

### 4.2.1 Multiple access

The multiple access scheme for the LTE physical layer is based on Orthogonal Frequency Division Multiplexing (OFDM) with a cyclic prefix (CP) in the downlink, and on Single-Carrier Frequency Division Multiple Access (SC-FDMA) with a cyclic prefix in the uplink and sidelink. To support transmission in paired and unpaired spectrum, two duplex modes are supported: Frequency Division Duplex (FDD), supporting full duplex and half duplex operation, and Time Division Duplex (TDD).

The Layer 1 is defined in a bandwidth agnostic way based on resource blocks, allowing the LTE Layer 1 to adapt to various spectrum allocations. A resource block spans either 12 sub-carriers with a sub-carrier bandwidth of 15kHz or 24 sub-carriers with a sub-carrier bandwidth of 7.5kHz or 72 sub-carriers with a sub-carrier bandwidth of 2.5kHz, each over a slot duration of 0.5ms, or 144 sub-carriers with a sub-carrier bandwidth of 1.25kHz over a slot duration of 1ms, or 486 sub-carriers with a sub-carrier bandwidth of approximately 0.37kHz over a slot duration of 3ms. Narrowband operation is also defined, whereby certain UEs may operate using a maximum transmission and reception bandwidth of 6 contiguous resource blocks within the total system bandwidth; for narrowband operation, sub-resource-block operation may also be used in the uplink, using 2, 3 or 6 sub-carriers.

For Narrowband Internet of Things (NB-IoT) operation, a UE operates in the downlink using 12 sub-carriers with a sub-carrier bandwidth of 15kHz, and in the uplink using a single sub-carrier with a sub-carrier bandwidth of either 3.75kHz or 15kHz or alternatively 3, 6 or 12 sub-carriers with a sub-carrier bandwidth of 15kHz.

The radio frame structure type 1 is only applicable to FDD (for both full duplex and half duplex operation) and, for sub-carrier bandwidths other than 1.25kHz and approximately 0.37kHz, has a duration of 10ms and consists of 20 slots with a slot duration of 0.5ms. Two adjacent slots form one sub-frame of length 1ms, except when the sub-carrier bandwidth is 1.25kHz or approximately 0.37kHz, in which cases one slot forms one sub-frame or has a time duration of 3ms, respectively. When the sub-carrier bandwidth is 15kHz, a slot can be further subdivided into three subslots of length 2 or 3 OFDM or SC-FDMA symbols for reduced latency operation.

The radio frame structure type 2 is only applicable to TDD and consists of two half-frames with a duration of 5ms each and containing each either 10 slots of length 0.5ms, or 8 slots of length 0.5ms and three special fields (DwPTS, GP and UpPTS) which have configurable individual lengths and a total length of 1ms. A subframe consists of two adjacent slots, except for subframes which consist of DwPTS, GP and UpPTS, namely subframe 1 and, in some configurations, subframe 6. Both 5ms and 10ms downlink-to-uplink switch-point periodicity are supported. Further details on the LTE frame structure are specified in [2]. Adaptation of the uplink-downlink subframe configuration via Layer 1 signalling is supported.

The radio frame structure type 3 is only applicable to LAA secondary cell operation. It has a duration of 10ms and consists of 20 slots with a slot duration of 0.5ms. Two adjacent slots form one subframe of length 1ms. Any subframe may be available for downlink or uplink transmission. For downlink transmission, the eNB shall perform the channel access procedures as specified in [4] prior to transmitting. A downlink or uplink transmission may start at the subframe boundary or later, and may end at the subframe boundary or earlier. For uplink transmission, the UE shall perform the channel access procedures as specified in [4] prior to transmitting.

To support a Multimedia Broadcast and Multicast Service (MBMS), LTE offers the possibility to transmit Multicast/Broadcast over a Single Frequency Network (MBSFN), where a time-synchronized common waveform is transmitted from multiple cells for a given duration. MBSFN transmission enables highly efficient MBMS, allowing for over-the-air combining of multi-cell transmissions in the UE, where the cyclic prefix is utilized to cover the difference in the propagation delays, which makes the MBSFN transmission appear to the UE as a transmission from a single large cell. Transmission on a dedicated carrier for MBSFN is supported, as well as transmission of MBSFN on a mixed carrier with both MBMS transmissions and point-to-point transmissions using time division multiplexing. In addition to the 15kHz sub-carrier bandwidth, the sub-carrier bandwidth of 7.5kHz with a longer CP, the sub-carrier bandwidth of 2.5kHz with a long CP (100µs), the sub-carrier bandwidth of 1.25kHz with a very long CP (200µs), and the sub-carrier bandwidth of approximately 0.37kHz with a very long CP (300µs) are all supported on both dedicated and mixed MBSFN carriers. Transmission of PDSCH also in MBSFN subframes that are not used for MCH is supported on mixed MBSFN carriers.

Transmission with multiple input and multiple output antennas (MIMO) are supported with configurations in the downlink with up to 32 transmit antenna ports and eight receive antennas, which allow for multi-layer downlink transmissions with up to eight streams and beamforming in both horizontal and vertical dimensions. Multi-layer uplink transmissions with up to four streams are supported with configurations in the uplink with up to four transmit antenna ports and four receive antennas. Multi-user MIMO, i.e. allocation of different streams to different users is supported in both UL and DL.

Coordinated Multi-Point (CoMP) transmission and reception are supported, including the possibility to configure a UE with multiple Channel State Information (CSI) feedback processes.

Aggregation of multiple cells is supported in the uplink and downlink with up to 32 serving cells, where each serving cell can use a transmission bandwidth of up to 110 resource blocks and can operate with either frame structure type 1 or frame structure type 2. Dual connectivity to groups of serving cells that belong to two different eNode-Bs is also supported.

Sidelink transmissions are defined for ProSe Direct Discovery and ProSe Direct Communication between UEs. The sidelink transmissions use the same frame structure as uplink and downlink when the UEs are in network coverage; however, the sidelink transmissions are restricted to a sub-set of the uplink resources. V2X communication between UEs is supported via sidelink transmissions or via the eNB.

### 4.2.2 Physical channels and modulation

The physical channels defined in the downlink are:

- the Physical Downlink Shared Channel (PDSCH),

- the Physical Multicast Channel (PMCH),

- the Physical Downlink Control Channel (PDCCH),

- the Enhanced Physical Downlink Control Channel (EPDCCH),

- the MTC Physical Downlink Control Channel (MPDCCH),

- the Relay Physical Downlink Control Channel (R-PDCCH),

- the Short Physical Downlink Control Channel (SPDCCH),

- the Physical Broadcast Channel (PBCH),

- the Physical Control Format Indicator Channel (PCFICH),

- the Physical Hybrid ARQ Indicator Channel (PHICH),

- the Narrowband Physical Broadcast Channel (NPBCH),

- the Narrowband Physical Downlink Control Channel (NPDCCH),

- and the Narrowband Physical Downlink Shared Channel (NPDSCH).

The physical channels defined in the uplink are:

- the Physical Random Access Channel (PRACH),

- the Physical Uplink Shared Channel (PUSCH),

- the Physical Uplink Control Channel (PUCCH),

- the Short Physical Uplink Control Channel (SPUCCH),

- the Narrowband Physical Random Access Channel (NPRACH),

- and the Narrowband Physical Uplink Shared Channel (NPUSCH).

The physical channels defined in the sidelink are:

- the Physical Sidelink Broadcast Channel (PSBCH),

- the Physical Sidelink Control Channel (PSCCH),

- the Physical Sidelink Discovery Channel (PSDCH),

- and the Physical Sidelink Shared Channel (PSSCH).

In addition, signals are defined as reference signals, primary and secondary synchronization signals, resynchronization signals, wake-up signals, and discovery signals.

The modulation schemes supported are:

- in the uplink, depending on the type of operation, π/2 BPSK, π/4 QPSK, QPSK, 16QAM, 64QAM and 256QAM,

- in the downlink, QPSK, 16QAM, 64QAM, 256QAM and 1024QAM,

- in the sidelink, QPSK, 16QAM and 64QAM.

### 4.2.3 Channel coding and interleaving

The channel coding scheme for transport blocks in LTE is Turbo Coding with a coding rate of R=1/3, two 8-state constituent encoders and a contention-free quadratic permutation polynomial (QPP) turbo code internal interleaver (except for downlink transport blocks in NB-IoT operation). Trellis termination is used for the turbo coding. Before the turbo coding, transport blocks are segmented into byte aligned segments with a maximum information block size of 6144 bits. Error detection is supported by the use of 24 bit CRC. Further channel coding schemes for BCH, control information and downlink transport blocks in NB-IoT operation are specified in [3].

### 4.2.4 Physical layer procedures

There are several Physical layer procedures involved with LTE operation. Such procedures covered by the physical layer are;

- Cell search,

- Power control,

- Uplink synchronisation and Uplink timing control,

- Random access related procedures,

- HARQ related procedures,

- Relay related procedures,

- Sidelink related procedures,

- Channel Access procedures.

Through the control of physical layer resources in the frequency domain as well as in the time and power domains, implicit support of interference coordination is provided in LTE.

### 4.2.5 Physical layer measurements

Radio characteristics are measured by the UE and the eNode-B and reported to higher layers in the network. These include, e.g. measurements for intra- and inter-frequency handover, inter RAT handover, timing measurements and measurements for RRM and in support for positioning.

Measurements for inter-RAT handover are defined in support of handover to GSM, UTRA FDD, UTRA TDD, NR, CDMA2000 1x RTT, CDMA2000 HRPD and IEEE 802.11.

# 5 Document structure of LTE physical layer specification

## 5.1 Overview

The physical layer specification consists of a general document (TS 36.201), and five documents (TSs 36.211, 36.212, 36.213, 36.214 and 36.216). The relation between the physical layer specifications in the context of the higher layers is shown in Figure 2; TS 36.216 is the physical layer specification for transmissions between an eNode-B and an RN.













![](media/image4.emf)

Figure 2: Relation between Physical Layer specifications

## 5.2 TS 36.201: Physical layer – General description

The scope is to describe:

- The contents of the Layer 1 documents (TS 36.200 series);

- Where to find information;

- A general description of LTE Layer 1.

## 5.3 TS 36.211: Physical channels and modulation

The scope of this specification is to establish the characteristics of the Layer-1 physical channels, generation of physical layer signals and modulation, and to specify:

- Definition of the uplink, downlink and sidelink physical channels;

- The structure of the physical channels, frame format, physical resource elements, etc.;

- Modulation mapping (BPSK, QPSK, etc);

- Physical shared channel in uplink, downlink and sidelink;

- Reference signals in uplink, downlink and sidelink;

- Random access channel;

- Primary and secondary synchronization signals;

- Resynchronization signal;

- Primary and secondary sidelink synchronization signals;

- Wake-up signals;

- OFDM signal generation in downlink;

- SC-FDMA signal generation in uplink and sidelink;

- Scrambling, modulation and up conversion;

- Uplink-downlink and sidelink timing relations;

- Layer mapping and precoding in downlink, uplink and sidelink.

## 5.4 TS 36.212: Multiplexing and channel coding

The scope of this specification is to describe the transport channel and control channel data processing, including multiplexing, channel coding and interleaving, and to specify:

- Channel coding schemes;

- Coding of Layer 1 / Layer 2 control information;

- Interleaving;

- Rate matching.

## 5.5 TS 36.213: Physical layer procedures

The scope of this specification is to establish the characteristics of the physical layer procedures, and to specify:

- Synchronisation procedures, including cell search procedure and timing synchronisation;

- Power control procedure;

- Random access procedure;

- Physical downlink shared channel related procedures, including CSI feedback reporting;

- Physical uplink shared channel related procedures, including UE sounding and HARQ ACK/NACK detection;

- Physical shared control channel procedures, including assignment of shared control channels;

- Physical multicast channel related procedures;

- Sidelink related procedures;

- Channel access procedures.

## 5.6 TS 36.214: Physical layer – Measurements

The scope of this specification is to establish the characteristics of the physical layer measurements, and to specify:

- Measurements to be performed by Layer 1 in UE and E-UTRAN;

- Reporting of measurement results to higher layers and the network;

- Handover measurements, idle-mode measurements, etc.

## 5.7 TS 36.216: Physical layer for relaying operation

The scope of this specification is to establish the characteristics of eNB - RN transmissions, and to specify relay-specific advancements in relation to:

- Physical Channels and Modulation;

- Multiplexing and channel coding;

- Relay Node procedures.

###### Annex A (informative):
Preferred mathematical notations

The following table contains the preferred mathematical notations used in L1 documentation.

| item | notation |
| --- | --- |
| multiply product | cross sign, e.g.  ab |
| matrix product | dot sign, e.g. ab |
| scalar product (product of a matrix by a scalar) | dot sign, scalar should precede matrix e.g. |
| matrix dimensioning | number of rows  number of column, e.g.:RC |
| Kronecker product | ab |
| bracketing of sets (all elements of same type, not ordered elements) | curly brackets {}, e.g. {a1, a2, …,ap}, or |
| bracketing of lists (all elements not necessary of same type, ordered elements) | round brackets (), e.g. (A, u, x) |
| bracketing of sequences (all elements of same type, ordered elements) | angle brackets, e.g. <a1, a2, …,ap> or |
| bracketing of function argument | round brackets, e.g. f(x) |
| bracketing of array index | square brackets, e.g. a[x] |
| bracketing of matrix or vector | square brackets [], e.g. , , or |
| Separation of indexes | use a comma : e.g. Ni,j |
| use of italic for symbols | a symbol should be either in italic or in normal font, but mixing up should be avoided. |
| bracketing of arithmetic expression to force precedence of operations | round brackets : e.g. |
| necessity of bracketing arithmetic expressions | When only + and  bracketing is not necessary. When the mod operator is used explicit bracketing of mod operands and possibly result should be done. |
| number type | in a context of non negative integer numbers, some notes should stress when a number is signed, or possibly fractional. |
| binary xor and and | respectively use + or . If no "mod 2" is explicitly in the expression some text should stress that the operation is modulo 2. |
| matrix or vector transpose | vT |
| 11 matrices | implicitly cast to its unique element. |
| vector dot product | uTv for column vectors, and uvT for line vectors |
| complex conjugate | v* |
| matrix or vector Hermitian transpose | vH |
| real part and imaginary part of complex numbers. | Re(x) and Im(x) |
| Modulo operation (including negative value)![](media_svg/image12.svg) [公式: r↵amodN] | Let ![](media_svg/image13.svg) [公式: q] be the integer quotient of ![](media_svg/image14.svg) [公式: a] and ![](media_svg/image15.svg) [公式: N],![](media_svg/image16.svg) [公式: Z]is integer, ![](media_svg/image17.svg) [公式: r]is remainder then ![](media_svg/image18.svg) [公式≈: ^{√}^{⌡}_{⌠}_{⌡}_{∞}_{0}^{q}a^{⎰}_{≥}=_{r}^{Z}N_{<}≠_{N}q+r], where![](media_svg/image19.svg) [公式: q=_{√}a/N_{∃}] for all ![](media_svg/image14.svg) [公式: a]and ![](media_svg/image20.svg) [公式: N](Note that ![](media_svg/image21.svg) [公式: √^{…}∃] is floor operation to round the elements of ![](media_svg/image22.svg) [公式: …] to the nearest integers towards minus infinity) |

###### Annex B (informative):
Change history

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2006-10 | - | - | - |  |  | Draft version created | 0.0.1 |
| 2006-10 | - | - | - |  |  | Endorsed by RAN1 | 0.1.0 |
| 2006-11 | - | - | - |  |  | Editors version at RAN1#47 | 0.1.1 |
| 2006-11 | - | - | - |  |  | Revised editors version at RAN1#47 | 0.1.2 |
| 2007-02 | - | - | - |  |  | Editors version at RAN1#48 | 0.2.1 |
| 2007-02 | - | - | - |  |  | Endorsed by RAN1#48 | 0.3.0 |
| 2007-02 | - | - | - |  |  | Editors version after RAN1#48 | 0.3.1 |
| 2007-02 | - | - | - |  |  | Editors version after RAN1#48 | 0.3.2 |
| 2007-03 | RAN#35 | RP-070168 | - |  |  | For information at RAN#35 | 1.0.0 |
| 2007-05 | - | - | - |  |  | Editors version at RAN1#49 | 1.0.1 |
| 2007-05 | - | - | - |  |  | Editors version at RAN1#49 | 1.0.2 |
| 2007-05 | - | - | - |  |  | Endorsed by RAN1#49 | 1.1.0 |
| 2007-05 | - | - | - |  |  | Editors version after RAN1#49 | 1.1.1 |
| 2007-06 | - | - | - |  |  | Endorsed by RAN1#49bis | 1.2.0 |
| 2007-09 | - | - | - |  |  | Editors version after RAN1#50 | 1.2.1 |
| 2007-09 | - | - | - |  |  | Editors version after RAN1#50 | 1.2.2 |
| 2007-09 | RAN#37 | RP-070728 | - |  |  | For approval at RAN#37 | 2.0.0 |
| 2007-09 | RAN#37 | RP-070728 |  |  |  | Approved version | 8.0.0 |
| 2007-11 | RAN#38 | RP-070949 | 0001 | 1 |  | Alignment of 36.201 with other LTE L1 specifications | 8.1.0 |
| 2008-12 | RAN#42 | RP-080981 | 0002 | - |  | Clarification of modular operation | 8.2.0 |
| 2009-03 | RAN#43 | RP-090233 | 0003 | - |  | Removing inverse modulo operation | 8.3.0 |
| 2009-12 | RAN#46 | RP-091177 | 0004 | 1 |  | Editorial corrections to 36.201 | 9.0.0 |
| 2010-03 | RAN#47 | RP-100210 | 0005 | 1 |  | Introduction of LTE MBMS | 9.1.0 |
| 2010-12 | RAN#50 | RP-101320 | 0006 | - |  | Introduction of Rel-10 LTE-Advanced features in 36.201 | 10.0.0 |
| 2012-09 | SP#57 | - | - | - |  | Update to Rel-11 version (MCC) | 11.0.0 |
| 2012-12 | RAN#58 | RP-121846 | 0007 | - |  | Introduction of Rel-11 features | 11.1.0 |
| 2014-09 | SP#65 | - | - | - |  | Update to Rel-12 version (MCC) | 12.0.0 |
| 2014-12 | RAN#66 | RP-142104 | 0008 | 3 |  | Introduction of TDD-FDD CA, Small-Cell Enhancements, Dual Connectivity, eIMTA, WLAN/3GPP interworking | 12.1.0 |
| 2015-03 | RAN#67 | RP-150366 | 0009 | 2 |  | Introduction of ProSe | 12.2.0 |
| 2015-12 | RAN#70 | RP-152027 | 0012 | - |  | Introduction of Rel-13 eCA | 13.0.0 |
| 2015-12 | RAN#70 | RP-152025 | 0013 | - |  | Introduction of EB/FD-MIMO | 13.0.0 |
| 2015-12 | RAN#70 | RP-152026 | 0010 | 3 |  | Introduction of LAA | 13.0.0 |
| 2016-03 | RAN#71 | RP-160361 | 0011 | 1 | B | Introduction of LC/EC MTC | 13.1.0 |
| 2016-06 | RAN#72 | RP-161067 | 0014 | 1 | B | Introduction of NB-IoT | 13.2.0 |
| 2016-09 | RAN#73 | RP-161571 | 0015 | - | B | Introduction of eLAA | 14.0.0 |
| 2016-09 | RAN#73 | RP-161570 | 0016 | 1 | B | Introduction of V2V | 14.0.0 |
| 2017-03 | RAN#75 | RP-170605 | 0017 | - | B | Introduction of Uplink Capacity Enhancements for LTE | 14.1.0 |
| 2017-03 | RAN#75 | RP-170607 | 0018 | - | B | Introduction of eFD-MIMO | 14.1.0 |
| 2017-03 | RAN#75 | RP-170608 | 0019 | - | B | Introduction of eMBMS enhancements for LTE | 14.1.0 |
| 2017-03 | RAN#75 | RP-170613 | 0020 | - | F | Corrections for V2V | 14.1.0 |
| 2017-03 | RAN#75 | RP-170610 | 0022 | - | A | Correction for NB-IoT channel coding | 14.1.0 |
| 2018-03 | RAN#79 | RP-180197 | 0023 | - | B | Introduction of shortened processing time and shortened TTI into TS36.201 | 15.0.0 |
| 2018-06 | RAN#80 | RP-181180 | 0024 | 1 | B | Introduction of Enhancements to LTE operation in unlicensed spectrum into 36.201 | 15.1.0 |
| 2018-06 | RAN#80 | RP-181173 | 0025 | 1 | B | Introduction of Downlink 1024QAM into 36.201 | 15.1.0 |
| 2018-06 | RAN#80 | RP-181176 | 0026 | - | B | Introduction of V2X Phase 2 enhancements into 36.201 | 15.1.0 |
| 2018-12 | RAN#82 | RP-182524 | 0027 | - | F | Introduction of Even Further Enhanced MTC for LTE into 36.201 | 15.2.0 |
| 2018-12 | RAN#82 | RP-182519 | 0028 | - | F | Introduction of NB-IoT TDD into 36.201 | 15.2.0 |
| 2020-03 | RAN#87-e | RP-200181 | 0029 | - | F | Correction to measurements for inter-RAT handover | 15.3.0 |
| 2020-03 | RAN#87-e | RP-200178 | 0030 | - | F | Inclusion of NWUS, MWUS, and RSS in TS 36.201 | 15.3.0 |
| 2020-06 | RAN#88-e | RP-200701 | 0031 | 1 | B | Corrections to LTE-based 5G terrestrial broadcast | 16.0.0 |
| 2022-03 | SA#95-e | - | - | - | - | Update to Rel-17 version (MCC) | 17.0.0 |
| 2024-03 | SA#103 | - | - | - | - | Update to Rel-18 version (MCC) | 18.0.0 |
| 2025-09 | SA#109 | - | - | - | - | Update to Rel-19 version (MCC) | 19.0.0 |
