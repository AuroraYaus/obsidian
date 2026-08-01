# TS 36.201 36201-j00

Contents

Foreword4

1Scope6

2References6

3Definitions of terms, symbols and abbreviations6

3.1Terms6

3.2Symbols6

3.3Abbreviations7

4General description of LTE Layer 18

4.1Relation to other layers8

4.1.1General protocol architecture8

4.1.2Service provided to higher layers8

4.2General description of Layer 19

4.2.1Multiple access9

4.2.2Physical channels and modulation10

4.2.3Channel coding and interleaving11

4.2.4Physical layer procedures11

4.2.5Physical layer measurements11

5Document structure of LTE physical layer specification12

5.1Overview12

5.2TS 36.201: Physical layer – General description12

5.3TS 36.211: Physical channels and modulation12

5.4TS 36.212: Multiplexing and channel coding13

5.5TS 36.213: Physical layer procedures13

5.6TS 36.214: Physical layer – Measurements13

5.7TS 36.216: Physical layer for relaying operation14

Annex A (informative):Preferred mathematical notations15

Annex B (informative):Change history16

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

In the present document, modal verbs have the following meanings:

shallindicates a mandatory requirement to do something

shall notindicates an interdiction (prohibition) to do something

The constructions "shall" and "shall not" are confined to the context of normative provisions, and do not appear in Technical Reports.

The constructions "must" and "must not" are not used as substitutes for "shall" and "shall not". Their use is avoided insofar as possible, and they are not used in a normative context except in a direct citation from an external, referenced, non-3GPP document, or so as to maintain continuity of style when extending or modifying the provisions of such a referenced document.

shouldindicates a recommendation to do something

should notindicates a recommendation not to do something

mayindicates permission to do something

need notindicates permission not to do something

The construction "may not" is ambiguous and is not used in normative elements. The unambiguous constructions "might not" or "shall not" are used instead, depending upon the meaning intended.

canindicates that something is possible

cannotindicates that something is impossible

The constructions "can" and "cannot" are not substitutes for "may" and "need not".

willindicates that something is certain or expected to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

will notindicates that something is certain or expected not to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

mightindicates a likelihood that something will happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

might notindicates a likelihood that something will not happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

In addition:

is(or any other verb in the indicative mood) indicates a statement of fact

is not(or any other negative verb in the indicative mood) indicates a statement of fact

The constructions "is" and "is not" do not indicate requirements.

## 1Scope

The present document describes a general description of the physical layer of the E-UTRA radio interface. The present document also describes the document structure of the 3GPP physical layer specifications, i.e. TS 36.200 series. The TS 36.200 series specifies the Uu and Un points for the 3G LTE mobile system, and defines the minimum level of specifications required for basic connections in terms of mutual connectivity and compatibility.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies.  In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[3]3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[4]3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[5]3GPP TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer – Measurements".

[6]3GPP TS 36.216: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer for relaying operation".

## 3Definitions of terms, symbols and abbreviations

## 3.1Terms

For the purposes of the present document, the terms given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

Definition format (Normal)

<defined term>: <definition>.

example: text used to clarify abstract rules by applying them literally.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

Symbol format (EW)

<symbol><Explanation>

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

BPSKBinary Phase Shift Keying

CoMPCoordinated Multi-Point

CPCyclic Prefix

CQIChannel Quality Indicator

CRCCyclic Redundancy Check

CSIChannel State Information

eNode-BEvolved Node B

EPDCCHEnhanced Physical Downlink Control Channel

E-UTRAEvolved Universal Terrestrial Radio Access

FDDFrequency Division Duplex

HARQHybrid Automatic Repeat Request

LAALicensed-Assisted Access

LTELong Term Evolution

MACMedium Access Control

MBMSMultimedia Broadcast and Multicast Service

MBSFNMulticast/Broadcast over Single Frequency Network

MIMOMultiple Input Multiple Output

MPDCCHMTC Physical Downlink Control Channel

MTCMachine Type Communications

NPBCHNarrowband Physical Broadcast Channel

NPDCCHNarrowband Physical Downlink Control Channel

NPDSCHNarrowband Physical Downlink Shared Channel

NPRACHNarrowband Physical Random Access Channel

NPUSCHNarrowband Physical Uplink Shared Channel

OFDMOrthogonal Frequency Division Multiplexing

PBCHPhysical Broadcast Channel

PCFICHPhysical Control Format Indicator Channel

PDSCHPhysical Downlink Shared Channel

PDCCHPhysical Downlink Control Channel

PHICHPhysical Hybrid ARQ Indicator Channel

PMCHPhysical Multicast Channel

PRACHPhysical Random Access Channel

ProSeProximity Services

PSBCHPhysical Sidelink Broadcast Channel

PSCCHPhysical Sidelink Control Channel

PSDCHPhysical Sidelink Discovery Channel

PSSCHPhysical Sidelink Shared Channel

PUCCHPhysical Uplink Control Channel

PUSCHPhysical Uplink Shared Channel

QAMQuadrature Amplitude Modulation

QPPQuadratic Permutation Polynomial

QPSKQuadrature Phase Shift Keying

RLCRadio Link Control

RNRelay Node

R-PDCCHRelay Physical Downlink Control Channel

RRCRadio Resource Control

RSSIReceived Signal Strength Indicator

RSRPReference Signal Received Power

RSRQReference Signal Received Quality

SAPService Access Point

SC-FDMASingle-Carrier Frequency Division Multiple Access

SPDCCHShort Physical Downlink Control Channel

SPUCCHShort Physical Uplink Control Channel

TDDTime Division Duplex

TX DiversityTransmit Diversity

UEUser Equipment

V2XVehicle-to-Everything

## 4General description of LTE Layer 1

## 4.1Relation to other layers

## 4.1.1General protocol architecture

The radio interface described in this specification covers the interface between the User Equipment (UE) and the network, and sidelink transmissions between UEs. The radio interface is composed of the Layer 1, 2 and 3. The TS 36.200 series describes the Layer 1 (Physical Layer) specifications. Layers 2 and 3 are described in the 36.300 series.

Figure 1: Radio interface protocol architecture around the physical layer

Figure 1 shows the E-UTRA radio interface protocol architecture around the physical layer (Layer 1). The physical layer interfaces the Medium Access Control (MAC) sub-layer of Layer 2 and the Radio Resource Control (RRC) Layer of Layer 3. The circles between different layer/sub-layers indicate Service Access Points (SAPs). The physical layer offers a transport channel to MAC. The transport channel is characterized by how the information is transferred over the radio interface. MAC offers different logical channels to the Radio Link Control (RLC) sub-layer of Layer 2. A logical channel is characterized by the type of information transferred.

## 4.1.2Service provided to higher layers

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

-RF processing. (Note: RF processing aspects are specified in the TS 36.100 series)

## 4.2General description of Layer 1

## 4.2.1Multiple access

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

## 4.2.2Physical channels and modulation

The physical channels defined in the downlink are:

-the Physical Downlink Shared Channel (PDSCH),

-the Physical Multicast Channel (PMCH),

-the Physical Downlink Control Channel (PDCCH),

-the Enhanced Physical Downlink Control Channel (EPDCCH),

-the MTC Physical Downlink Control Channel (MPDCCH),

-the Relay Physical Downlink Control Channel (R-PDCCH),

-the Short Physical Downlink Control Channel (SPDCCH),

-the Physical Broadcast Channel (PBCH),

-the Physical Control Format Indicator Channel (PCFICH),

-the Physical Hybrid ARQ Indicator Channel (PHICH),

-the Narrowband Physical Broadcast Channel (NPBCH),

-the Narrowband Physical Downlink Control Channel (NPDCCH),

-and the Narrowband Physical Downlink Shared Channel (NPDSCH).

The physical channels defined in the uplink are:

-the Physical Random Access Channel (PRACH),

-the Physical Uplink Shared Channel (PUSCH),

-the Physical Uplink Control Channel (PUCCH),

-the Short Physical Uplink Control Channel (SPUCCH),

-the Narrowband Physical Random Access Channel (NPRACH),

-and the Narrowband Physical Uplink Shared Channel (NPUSCH).

The physical channels defined in the sidelink are:

-the Physical Sidelink Broadcast Channel (PSBCH),

-the Physical Sidelink Control Channel (PSCCH),

-the Physical Sidelink Discovery Channel (PSDCH),

-and the Physical Sidelink Shared Channel (PSSCH).

In addition, signals are defined as reference signals, primary and secondary synchronization signals, resynchronization signals, wake-up signals, and discovery signals.

The modulation schemes supported are:

-in the uplink, depending on the type of operation, π/2 BPSK, π/4 QPSK, QPSK, 16QAM, 64QAM and 256QAM,

-in the downlink, QPSK, 16QAM, 64QAM, 256QAM and 1024QAM,

-in the sidelink, QPSK, 16QAM and 64QAM.

## 4.2.3Channel coding and interleaving

The channel coding scheme for transport blocks in LTE is Turbo Coding with a coding rate of R=1/3, two 8-state constituent encoders and a contention-free quadratic permutation polynomial (QPP) turbo code internal interleaver (except for downlink transport blocks in NB-IoT operation). Trellis termination is used for the turbo coding. Before the turbo coding, transport blocks are segmented into byte aligned segments with a maximum information block size of 6144 bits. Error detection is supported by the use of 24 bit CRC. Further channel coding schemes for BCH, control information and downlink transport blocks in NB-IoT operation are specified in [3].

## 4.2.4Physical layer procedures

There are several Physical layer procedures involved with LTE operation. Such procedures covered by the physical layer are;

-Cell search,

-Power control,

-Uplink synchronisation and Uplink timing control,

-Random access related procedures,

-HARQ related procedures,

-Relay related procedures,

-Sidelink related procedures,

-Channel Access procedures.

Through the control of physical layer resources in the frequency domain as well as in the time and power domains, implicit support of interference coordination is provided in LTE.

## 4.2.5Physical layer measurements

Radio characteristics are measured by the UE and the eNode-B and reported to higher layers in the network. These include, e.g. measurements for intra- and inter-frequency handover, inter RAT handover, timing measurements and measurements for RRM and in support for positioning.

Measurements for inter-RAT handover are defined in support of handover to GSM, UTRA FDD, UTRA TDD, NR, CDMA2000 1x RTT, CDMA2000 HRPD and IEEE 802.11.

## 5Document structure of LTE physical layer specification

## 5.1Overview

The physical layer specification consists of a general document (TS 36.201), and five documents (TSs 36.211, 36.212, 36.213, 36.214 and 36.216). The relation between the physical layer specifications in the context of the higher layers is shown in Figure 2; TS 36.216 is the physical layer specification for transmissions between an eNode-B and an RN.

Figure 2: Relation between Physical Layer specifications

## 5.2TS 36.201: Physical layer – General description

The scope is to describe:

-The contents of the Layer 1 documents (TS 36.200 series);

-Where to find information;

-A general description of LTE Layer 1.

## 5.3TS 36.211: Physical channels and modulation

The scope of this specification is to establish the characteristics of the Layer-1 physical channels, generation of physical layer signals and modulation, and to specify:

-Definition of the uplink, downlink and sidelink physical channels;

-The structure of the physical channels, frame format, physical resource elements, etc.;

-Modulation mapping (BPSK, QPSK, etc);

-Physical shared channel in uplink, downlink and sidelink;

-Reference signals in uplink, downlink and sidelink;

-Random access channel;

-Primary and secondary synchronization signals;

-Resynchronization signal;

-Primary and secondary sidelink synchronization signals;

-Wake-up signals;

-OFDM signal generation in downlink;

-SC-FDMA signal generation in uplink and sidelink;

-Scrambling, modulation and up conversion;

-Uplink-downlink and sidelink timing relations;

-Layer mapping and precoding in downlink, uplink and sidelink.

## 5.4TS 36.212: Multiplexing and channel coding

The scope of this specification is to describe the transport channel and control channel data processing, including multiplexing, channel coding and interleaving, and to specify:

-Channel coding schemes;

-Coding of Layer 1 / Layer 2 control information;

-Interleaving;

-Rate matching.

## 5.5TS 36.213: Physical layer procedures

The scope of this specification is to establish the characteristics of the physical layer procedures, and to specify:

-Synchronisation procedures, including cell search procedure and timing synchronisation;

-Power control procedure;

-Random access procedure;

-Physical downlink shared channel related procedures, including CSI feedback reporting;

-Physical uplink shared channel related procedures, including UE sounding and HARQ ACK/NACK detection;

-Physical shared control channel procedures, including assignment of shared control channels;

-Physical multicast channel related procedures;

-Sidelink related procedures;

-Channel access procedures.

## 5.6TS 36.214: Physical layer – Measurements

The scope of this specification is to establish the characteristics of the physical layer measurements, and to specify:

-Measurements to be performed by Layer 1 in UE and E-UTRAN;

-Reporting of measurement results to higher layers and the network;

-Handover measurements, idle-mode measurements, etc.

## 5.7TS 36.216: Physical layer for relaying operation

The scope of this specification is to establish the characteristics of eNB - RN transmissions, and to specify relay-specific advancements in relation to:

-Physical Channels and Modulation;

-Multiplexing and channel coding;

-Relay Node procedures.

## Annex A (informative):Preferred mathematical notations

The following table contains the preferred mathematical notations used in L1 documentation.

## Annex B (informative):Change history
