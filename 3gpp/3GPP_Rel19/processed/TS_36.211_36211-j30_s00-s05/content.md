# TS 36.211 36211-j30_s00-s05

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

The present document describes the physical channels for evolved UTRA.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]TS 36.201: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE physical layer; General description".

[3]TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[4]TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[5]TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements".

[6]TS 36.104: "Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception".

[7]TS 36.101: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception".

[8]TS 36.321, "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[9]TS 36.331, "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC) Protocol specification"

[10]TS 36.304, "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode"

[11]TS 37.213: "Physical layer procedures for shared spectrum channel access"

[12]TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2"

## 3Symbols and abbreviations

## 3.1Symbols

For the purposes of the present document, the following symbols apply:

Resource element with frequency-domain index  and time-domain index

Value of resource element  [for antenna port]

Matrix for supporting cyclic delay diversity

Density of random access opportunities per radio frame

Carrier frequency

PRACH resource frequency index within the considered time-domain location

PRACH frequency hopping offset, expressed as a number of resource blocks

Start symbol in slot 0 for NPDCCH

Start symbol in slot 0 for NPDSCH

Bandwidth for PSBCH transmission, expressed as a number of subcarriers

Bandwidth for PSBCH transmission, expressed as a number of resource blocks

Bandwidth for PSCCH transmission, expressed as a number of subcarriers

Bandwidth for PSCCH transmission, expressed as a number of resource blocks

Bandwidth for PSDCH transmission, expressed as a number of subcarriers

Bandwidth for PSDCH transmission, expressed as a number of resource blocks

Scheduled bandwidth for PSSCH transmission, expressed as a number of subcarriers

Scheduled bandwidth for PSSCH transmission, expressed as a number of resource blocks

Scheduled bandwidth for uplink transmission, expressed as a number of subcarriers

Scheduled bandwidth for uplink transmission, expressed as a number of resource blocks

Scheduled number of repetitions of a NPUSCH transmission

Scheduled number of repetitions of a NPDSCH transmission

Scheduled bandwidth for uplink NPUSCH transmission, expressed as a number of subcarriers

Number of repetitions of identical slots for NPUSCH

Number of coded bits to transmit on a physical channel [for codeword ]

Number of modulation symbols to transmit on a physical channel [for codeword ]

Number of modulation symbols to transmit per layer for a physical channel

Number of modulation symbols to transmit per antenna port for a physical channel

Number of consecutive subcarriers in an UL resource unit for PUSCH sub-PRB allocation

Number of slots in an UL resource unit for PUSCH sub-PRB allocation

Number of SC-FDMA symbols in an uplink slot for PUSCH sub-PRB allocation

Number of subcarriers in the frequency domain for PUSCH sub-PRB allocation

Number of reference signal sequences available for the UL resource unit size for PUSCH sub-PRB allocationMseqRU

Number of scheduled UL resource units for PUSCH sub-PRB allocationMRU

A constant equal to 2048 for , 4096 for  and 8192 for

Downlink cyclic prefix length for OFDM symbol  in a slot

Cyclic shift value used for random access preamble generation

Number of cyclic shifts used for PUCCH formats 1/1a/1b in a resource block with a mix of formats 1/1a/1b and 2/2a/2b

Bandwidth available for use by PUCCH formats 2/2a/2b, expressed in multiples of

The offset used for PUSCH frequency hopping, expressed in number of resource blocks (set by higher layers)

Physical layer cell identity

Narrowband physical layer cell identity

MBSFN area identity

Physical layer sidelink synchronization identity

Positioning reference signal identity

Downlink bandwidth configuration, expressed in multiples of

Smallest downlink bandwidth configuration, expressed in multiples of

Largest downlink bandwidth configuration, expressed in multiples of

Uplink bandwidth configuration, expressed in multiples of

Smallest uplink bandwidth configuration, expressed in multiples of

Largest uplink bandwidth configuration, expressed in multiples of

Sidelink bandwidth configuration, expressed in multiples of

Duration of RSS measured in subframesNRSS

Number of scheduled subframes for NPDSCH transmission

Number of symbols for NPSS in a subframe

Number of symbols for NSSS in a subframe

Number of consecutive subcarriers in an UL resource unit for NB-IoT

Number of reference signal sequences available for the UL resource unit size

Number of scheduled UL resource units for NB-IoT

Total number of uplink narrowbands

Total number of uplink widebands

Number of subcarriers in the frequency domain for NB-IoT

Number of consecutive absolute subframes over which the scrambling sequence stays the same

Total number of absolute subframes a PUSCH with repetition spans expressed as a number of absolute subframes

Number of repetitions of a PUSCH transmission

Number of consecutive absolute subframes over which PUCCH or PUSCH stays at the same narrowband before hopping to another narrowband, expressed as a number of absolute subframes

Narrowband offset between one narrowband and the next narrowband a PUSCH hops to, expressed as a number of uplink narrowbands

Total number of absolute subframes a PUCCH with repetition spans, expressed as a number of absolute subframes

Number of repetitions of a PUCCH transmission

Number of PRACH repetitions per preamble transmission attempt

Number of subframes allowed for preamble transmission within a 1024-frame interval

PRACH starting subframe periodicity

Number of NPRACH repetitions per preamble transmission attempt

NPRACH resource periodicity

Frequency location of the first sub-carrier allocated to NPRACH

Number of sub-carriers allocated to NPRACH

Number of starting sub-carriers allocated for UE initiated random access

NPRACH starting subframe

Fraction for starting subcarrier index for UE support for multi-tone msg3 transmission

Periodicity for NPDSCH/NPDCCH gaps

Duration for NPDSCH/NPDCCH gaps

Threshold for applying NPDSCH/NPDCCH gaps

Total number of downlink narrowbands

Total number of downlink widebands

Total number of absolute subframes a PDSCH with repetition spans, expressed as a number of absolute subframes

Number of repetitions of a PDSCH transmission

Number of consecutive absolute subframes over which MPDCCH or PDSCH stays at the same narrowband before hopping to another narrowband, expressed as a number of absolute subframes

Number of narrowbands over which MPDCCH or PDSCH frequency hops

Narrowband offset between one narrowband and the next narrowband an MPDCCH or PDSCH hops to, expressed as a number of downlink narrowbands

Number of times a PDSCH carrying SIB1-BR is transmitted over 8 radio frames

Total number of absolute subframes a MPDCCH with repetition spans, expressed as a number of absolute subframes

Number of repetitions of a MPDCCH transmission

Total number of absolute subframes a MPDCCH search space with maximum repetition level spans, expressed as a number of absolute subframes

Maximum repetition level of a MPDCCH search space

Number of ECCEs in a subframe for one MPDCCH

Number of OFDM symbols in a downlink slot

Number of SC-FDMA symbols in an uplink slot

Number of symbols in a guard period for narrowband or wideband retuning

Number of consecutive slots in an UL resource unit for NB-IoT

Number of SC-FDMA symbols in a sidelink slot

Resource block size in the frequency domain, expressed as a number of subcarriers

Number of sub-bands for PUSCH frequency-hopping with predefined hopping pattern

Size of each sub-band for PUSCH frequency-hopping with predefined hopping pattern, expressed as a number of resource blocks

Size of narrow-band random-access resource in number of subcarriers

Number of downlink to uplink switch points within the radio frame

Number of reference symbols per slot for PUCCH

Number of reference symbols per subslot or per slot for SPUCCH

Timing offset between uplink and downlink radio frames at the UE, expressed in units of

Fixed timing advance offset, expressed in units of

Timing offset between sidelink and timing reference frames at the UE, expressed in units of

Resource index for PUCCH formats 1/1a/1b

Resource index for PUCCH formats 2/2a/2b

Resource index for PUCCH format 3

Number of PDCCHs present in a subframe

Physical resource block number

First physical resource block occupied by PRACH resource considered

First physical resource block available for PRACH

Lowest PRB number of RSSnPRB,RSS

Subcarrier occupied by NPRACH resource considered

Virtual resource block number

Radio network temporary identifier

Sidelink group destination identity

System frame number

Slot number within a radio frame

Absolute subframe number

Index for subframes allowed for preamble transmission

Starting frame offset of RSS in each RSS periodORSS

Number of antenna ports used for transmission of a channel

Antenna port number

Period of RSS measured in framesPRSS

Codeword number

Index for PRACH versions with same preamble format and PRACH density

QmModulation order: 1 for π/2-BPSK, 2 for QPSK, 4 for 16QAM, 6 for 64QAM and 8 for 256QAM transmissions

Time-continuous baseband signal for antenna port  and SC-FDMA/OFDM symbol  in a slot

Radio frame indicator index of PRACH opportunity

Half frame index of PRACH opportunity within the radio frame

Uplink subframe number for start of PRACH opportunity within the half frame

Radio frame duration

Basic time unit

Slot duration

Precoding matrix for downlink spatial multiplexing

Amplitude scaling for PRACH

Amplitude scaling for NPRACH

Amplitude scaling for PUCCH

Amplitude scaling for PUSCH

Amplitude scaling for NPUSCH

Amplitude scaling for SPUCCH

Amplitude scaling for sounding reference symbols

Subcarrier spacing

Subcarrier spacing for the random access preamble

Number of transmission layers

## 3.2Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

CCEControl Channel Element

CDDCyclic Delay Diversity

CRSCell-specific Reference Signal

CSIChannel-State Information

DCIDownlink Control Information

DM-RSDemodulation Reference Signal

ECCEEnhanced Control Channel Element

EPDCCHEnhanced Physical Downlink Control CHannel

EREGEnhanced Resource-Element Group

MPDCCHMTC Physical Downlink Control Channel

MWUSMTC Wake-Up Signal

NCCENarrowband Control Channel Element

NPBCHNarrowband Physical Broadcast CHannel

NPDCCHNarrowband Physical Downlink Control CHannel

NPDSCHNarrowband Physical Downlink Shared CHannel

NPRACHNarrowband Physical Random Access CHannel

NPUSCHNarrowband Physical Uplink Shared CHannel

NPRSNarrowband Positioning Reference Signal

NPSSNarrowband Primary Synchronization Signal

NSSSNarrowband Secondary Synchronization Signal

NRSNarrowband Reference Signal PBCHPhysical Broadcast CHannel

NTNNon-Terrestrial Networks

PCFICHPhysical Control Format Indicator CHannel

PDCCHPhysical Downlink Control CHannel

PDSCHPhysical Downlink Shared CHannel

PHICHPhysical Hybrid-ARQ Indicator CHannel

PMCHPhysical Multicast CHannel

PRACHPhysical Random Access CHannel

PRBPhysical Resource Block

PRGPrecoding Resource Block Group

PRSPositioning Reference Signal

PSBCHPhysical Sidelink Broadcast CHannel

PSCCHPhysical Sidelink Control CHannel

PSDCHPhysical Sidelink Discovery CHannel

PSSCHPhysical Sidelink Shared CHannel

PUCCHPhysical Uplink Control CHannel

PUSCHPhysical Uplink Shared CHannel

REGResource-Element Group

RSSResynchronization Signal

SCCEShort Control Channel Element

SCGSecondary Cell Group

SPDCCHShort Physical Downlink Control CHannel

SPUCCHShort Physical Uplink Control CHannel

SREGShort Resource-Element Group

SRSSounding Reference Signal

VRBVirtual Resource Block

## 4Frame structure

Throughout this specification, unless otherwise noted, the size of various fields in the time domain is expressed as a number of time units  seconds.

Downlink, uplink and sidelink transmissions are organized into radio frames with  duration. Three radio frame structures are supported:

-Type 1, applicable to FDD and IoT NTN TDD only,

-Type 2, applicable to TDD only,

-Type 3, applicable to LAA secondary cell operation only.

NOTE: LAA secondary cell operation only applies to frame structure type 3.

Transmissions in multiple cells can be aggregated where up to 31 secondary cells can be used in addition to the primary cell. Unless otherwise noted, the description in this specification applies to each of the up to 32 serving cells. In case of multi-cell aggregation, different frame structures can be used in the different serving cells.

## 4.1Frame structure type 1 for FDD

Frame structure type 1 is applicable to both full duplex and half duplex FDD only. Each radio frame is  long and consists of 10 subframes of length , numbered from 0 to 9. Subframe  in frame  has an absolute subframe number  where  is the system frame number.

For subframes using , , or , subframe  is defined as two slots,  and , of length  each.Δf=2.5 kHz

For subframes using , subframe  is defined as one slot, , of length .

For transmissions using , a slot has a length of 92160. There are 13 slots, numbered in increasing order from 0 to 12, in a 40 ms period starting at  with slot 0 starting at  in the 40 ms period. Δf=182944Ts≈0.37 kHzTs=3 msnf mod 4=030720Ts

For subframes using , the subframe can further be divided into six subslots according to Table 4.1-1. Downlink subslot pattern 1 is applied if the number of symbols used for PDCCH is equal to 1 or 3 and downlink subslot pattern 2 is applied if the number of symbols used for PDCCH is equal to 2. For system bandwidths , subslot transmission is not supported in case 4 symbols used for PDCCH.

For FDD, 10 subframes, 20 slots, or up to 60 subslots are available for downlink transmission and 10 subframes, 20 slots, or up to 60 subslots are available for uplink transmissions in each 10 ms interval. Uplink and downlink transmissions are separated in the frequency domain. In half-duplex FDD operation, the UE cannot transmit and receive at the same time while there are no such restrictions in full-duplex FDD.

Figure 4.1-1: Frame structure type 1 (assuming ).Δfϵ2.5, 7.5, 15 kHz

Table 4.1-1: SC-FDMA/OFDM symbols in different subslots of subframe i

## 4.2Frame structure type 2

Frame structure type 2 is applicable to TDD only. Each radio frame of length  consists of two half-frames of length each. Each half-frame consists of five subframes of length. Each subframe is defined as two slots, and, of length  each. Subframe  in frame  has an absolute subframe number  where  is the system frame number.

The uplink-downlink configuration in a cell may vary between frames and controls in which subframes uplink or downlink transmissions may take place in the current frame. The uplink-downlink configuration in the current frame is obtained according to Clause 13 in [4].

The supported uplink-downlink configurations are listed in Table 4.2-2 where, for each subframe in a radio frame, "D" denotes a downlink subframe reserved for downlink transmissions, "U" denotes an uplink subframe reserved for uplink transmissions and "S" denotes a special subframe with the three fields DwPTS, GP and UpPTS. The length of DwPTS and UpPTS is given by Table 4.2-1 subject to the total length of DwPTS, GP and UpPTS being equal to where X is the number of additional SC-FDMA symbols in UpPTS provided by the higher layer parameter srs-UpPtsAdd if configured otherwise X is equal to 0. The UE is not expected to be configured with 2 additional UpPTS SC-FDMA symbols for special subframe configurations {3, 4, 7, 8} for normal cyclic prefix in downlink and special subframe configurations {2, 3, 5, 6} for extended cyclic prefix in downlink and 4 additional UpPTS SC-FDMA symbols for special subframe configurations {1, 2, 3, 4, 6, 7, 8} for normal cyclic prefix in downlink and special subframe configurations {1, 2, 3, 5, 6} for extended cyclic prefix in downlink.

Uplink-downlink configurations with both 5 ms and 10 ms downlink-to-uplink switch-point periodicity are supported.

-In case of 5 ms downlink-to-uplink switch-point periodicity, the special subframe exists in both half-frames.

-In case of 10 ms downlink-to-uplink switch-point periodicity, the special subframe exists in the first half-frame only.

Subframes 0 and 5 and DwPTS are always reserved for downlink transmission. For special subframe configurations 1, 2, 3, 4, 6, 7 and 8, DwPTS is split into two parts, of which the first part is a slot and the second part is of X-symbol duration within the second slot. Downlink subframes, downlink slots in the downlink subframe and DwPTS, and the X–symbol duration in the second slot of DwPTS are available for downlink transmission. The X-symbol transmission opportunity is only available for special subframe configuration 3,4 and 8.

UpPTS and the subframe immediately following the special subframe are always reserved for uplink transmission. Uplink subframes, uplink slots and UpPTS with special subframe configuration 10 are available for uplink transmission. Note that UpPTS with special subframe configuration 10 are not available for SPUCCH transmission.

In case multiple cells are aggregated, the UE may assume that the guard period of the special subframe in the cells using frame structure type 2 have an overlap of at least .

In case multiple cells with different uplink-downlink configurations in the current radio frame are aggregated and the UE is not capable of simultaneous reception and transmission in the aggregated cells, the following constraints apply:

-if the subframe in the primary cell is a downlink subframe, the UE shall not transmit any signal or channel on a secondary cell in the same subframe

-if the subframe in the primary cell is an uplink subframe, the UE is not expected to receive any downlink transmissions on a secondary cell in the same subframe

-if the subframe in the primary cell is a special subframe and the same subframe in a secondary cell is a downlink subframe, the UE is not expected to receive PDSCH/EPDCCH/PMCH/PRS transmissions in the secondary cell in the same subframe, and the UE is not expected to receive any other signals on the secondary cell in OFDM symbols that overlaps with the guard period or UpPTS in the primary cell.

For frame structure type 2, the higher-layer parameters for symbol-level resource reservation for BL/CE UEs (symbolBitmap1 and symbolBitmap2) do not apply to special subframes.

Figure 4.2-1: Frame structure type 2 (for 5 ms switch-point periodicity)

Table 4.2-1: Configuration of special subframe (lengths of DwPTS/GP/UpPTS)

Table 4.2-2: Uplink-downlink configurations

## 4.3Frame structure type 3

Frame structure type 3 is applicable to LAA secondary cell operation with normal cyclic prefix only. Each radio frame is  long and consists of 20 slots of length, numbered from 0 to 19. A subframe is defined as two consecutive slots where subframe  consists of slots and.

The 10 subframes within a radio frame are available for downlink or uplink transmissions. Downlink transmissions occupy one or more consecutive subframes, starting anywhere within a subframe and ending with the last subframe either fully occupied or following one of the DwPTS durations in Table 4.2-1. Uplink transmisisons occupy one or more consecutive subframes.

## 4.4Frame structure type 1 for IoT NTN TDD

Frame structure type 1 is applicable to IoT NTN TDD in band 249. Each radio frame is  long and consists of 10 subframes of length , numbered from 0 to 9. Subframe  in frame  has an absolute subframe number  where  is the system frame number.Tf=307200Ts=10 ms30720Ts=1 msinfnsfabs=10nf+inf

The frame structure for IoT NTN TDD, at the uplink time synchronization reference point defined in clause 16.1.2 of TS 36.213 [4] consists of  consecutive downlink subframes, followed by 50 consecutive guard period subframes, followed by  consecutive uplink subframes, followed by 24 consecutive guard period subframes in each 90 ms interval.D=8U=8

-The UE shall not assume any signal or channel being transmitted in subframes other than downlink subframes 3, 4, 5, 6, 7, 8, 9, and 0 across two consecutive radio frames.

-The UE shall not transmit any signal or channel on a subframe other than the 8 consecutive uplink subframes.

## 5Uplink

## 5.1Overview

The smallest resource unit for uplink transmissions is denoted a resource element and is defined in clause 5.2.2.

## 5.1.1Physical channels

An uplink physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS 36.212 [3] and the present document TS 36.211. The following uplink physical channels are defined:

-Physical Uplink Shared Channel, PUSCH

-Physical Uplink Control Channel, PUCCH

-Short Physical Uplink Control Channel, SPUCCH

-Physical Random Access Channel, PRACH

## 5.1.2Physical signals

An uplink physical signal is used by the physical layer but does not carry information originating from higher layers. The following uplink physical signals are defined:

-Reference signal

## 5.2Slot structure and physical resources

## 5.2.1Resource grid

The transmitted signal in each slot is described by one or several resource grids of  subcarriers and  SC-FDMA symbols. The resource grid is illustrated in Figure 5.2.1-1. The quantity  depends on the uplink transmission bandwidth configured in the cell and shall fulfil

where  and  are the smallest and largest uplink bandwidths, respectively, supported by the current version of this specification. The set of allowed values for  is given by TS 36.101 [7].

The number of SC-FDMA symbols in a slot depends on the cyclic prefix length configured by the higher layer parameter UL-CyclicPrefixLength and is given in Table 5.2.3-1.

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed. There is one resource grid per antenna port. The antenna ports used for transmission of a physical channel or signal depends on the number of antenna ports configured for the physical channel or signal as shown in Table 5.2.1-1. The index  is used throughout clause 5 when a sequential numbering of the antenna ports is necessary.

Figure 5.2.1-1: Uplink resource grid

Table 5.2.1-1: Antenna ports used for different physical channels and signals

## 5.2.2Resource elements

Each element in the resource grid is called a resource element and is uniquely defined by the index pair  in a slot where  and  are the indices in the frequency and time domains, respectively. Resource element  on antenna port  corresponds to the complex value . When there is no risk for confusion, or no particular antenna port is specified, the index  may be dropped. Quantities  corresponding to resource elements not used for transmission of a physical channel or a physical signal in a slot shall be set to zero.

## 5.2.3Resource blocks

A physical resource block is defined as consecutive SC-FDMA symbols in the time domain and consecutive subcarriers in the frequency domain, where  and  are given by Table 5.2.3-1. A physical resource block in the uplink thus consists of  resource elements, corresponding to one slot in the time domain and 180 kHz in the frequency domain.

Table 5.2.3-1: Resource block parameters

The relation between the physical resource block number  in the frequency domain and resource elements  in a slot is given by

5.2.3AResource unit

Resource units are used to describe the mapping of PUSCH using sub-PRB allocations to resource elements for BL/CE UEs. A resource unit is defined as  SC-FDMA symbols in the time domain and consecutive subcarriers in the frequency domain, where  and  are given by Table 5.2.3A-1.

Table 5.2.3A-1: Supported combinations of , , and  for PUSCH using sub-PRB allocations for Frame Structure type 1 and Frame Structure type 2.

## 5.2.4Narrowbands and widebands

A narrowband is defined as six non-overlapping consecutive physical resource blocks in the frequency domain. The total number of uplink narrowbands in the uplink transmission bandwidth configured in the cell is given by

The narrowbands are numbered  in order of increasing physical resource-block number where narrowband is composed of physical resource-block indices

where

If , a wideband is defined as four non-overlapping narrowbands in the frequency domain. The total number of uplink widebands in the uplink transmission bandwidth configured in the cell is given by

and the widebands are numbered  in order of increasing narrowband number where wideband  is composed of narrowband indices  where .

If , then  and the single wideband is composed of the  non-overlapping narrowband(s).

## 5.2.5Guard period for narrowband and wideband retuning

For BL/CE UEs, a guard period of at most  SC-FDMA symbols is created for Tx-to-Tx frequency retuning between two consecutive subframes.

-If the higher layer parameter ce-RetuningSymbols is set, then  equals ce-RetuningSymbols, otherwise .

-If the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz, then the rules for guard period creation defined in the remainder of this clause do not apply for retuning between narrowbands but for retuning between widebands and for transmissions involving multiple widebands.

-If a UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig and the allocation resources are not fully within one narrowband, the rules for guard period creation defined in the remainder of this clause apply for retuning between tuning narrowbands, where

-In case of CEModeA, the tuning narrowband is defined as the 6 consecutive PRBs starting from  defined in 8.1.1 of [4] with the center frequency set in the middle.RBstart

-In case of CEModeB, the tuning narrowband is defined as the 6 consecutive PRBs with the center frequency set in the middle of allocated two PRBs.

-If the UE retunes from a first narrowband carrying PUSCH to a second narrowband carrying PUSCH, or if the UE retunes from a first narrowband carrying PUCCH to a second narrowband carrying PUCCH,

-if , a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe;

-if , a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

-If the UE retunes from a first narrowband carrying PUCCH to a second narrowband carrying PUSCH,

-if the PUCCH uses a shortened PUCCH format and , a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe;

-if the PUCCH uses a shortened PUCCH format and , a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe and the first SC-FDMA symbol in the second subframe;

-if the PUCCH uses a normal PUCCH format, a guard period is created by the UE not transmitting the first  SC-FDMA symbols in the second subframe.

-If the UE retunes from a first narrowband carrying PUSCH to a second narrowband carrying PUCCH,

-a guard period is created by the UE not transmitting the last  SC-FDMA symbols in the first subframe.

-For CEModeA, if the PUSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz,

-If the PUSCH resource allocation is within a 5 MHz wideband, the center frequency of the transmission bandwidth is the center frequency of the wideband;

-If the PUSCH resource allocation spans two 5 MHz widebands, the center frequency of transmission bandwidth is in the center of PUSCH resource allocation.

Furthermore, for BL/CE UEs configured with the higher layer parameter srs-UpPtsAdd, a guard period of at most  SC-FDMA symbols is created for Tx-to-Tx frequency retuning between a first special subframe and a second uplink subframe for frame structure type 2 according to:

-If the UE retunes from a first narrowband carrying SRS in the last UpPTS symbol to a second narrowband carrying PUSCH,

-a guard period is created by the UE not transmitting the first  SC-FDMA symbols in the second subframe.

-If the UE retunes from a first narrowband carrying SRS in the last but one UpPTS symbol, but not in the last UpPTS symbol, to a second narrowband carrying PUSCH,

-if , a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe;

-if , a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

-If the UE retunes from a first narrowband carrying SRS to a second narrowband carrying PUCCH,

-if , a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe;

-if , a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

For , and for SRS transmission in a special subframe, a BL/CE UE is not expected to be configured with a first SRS transmission in symbol l and a second SRS transmission in any of symbols if the first SRS transmission and the second SRS transmission use different narrowbands.

## 5.3Physical uplink shared channel

The baseband signal representing the physical uplink shared channel is defined in terms of the following steps:

-scrambling

-modulation of scrambled bits to generate complex-valued symbols

-mapping of the complex-valued modulation symbols onto one or several transmission layers

-transform precoding to generate complex-valued symbols

-precoding of the complex-valued symbols

-mapping of precoded complex-valued symbols to resource elements

-generation of complex-valued time-domain SC-FDMA signal for each antenna port

Figure 5.3-1: Overview of uplink physical channel processing

## 5.3.1Scrambling

For each codeword , the block of bits , where  is the number of bits transmitted in codeword  on the physical uplink shared channel in subframe(s)/slot/subslot, shall be scrambled with a UE-specific scrambling sequence prior to modulation, resulting in a block of scrambled bits  according to the following pseudo code

Set i = 0

while

if // ACK/NACK or Rank Indication placeholder bits

else

if // ACK/NACK or Rank Indication repetition placeholder bits

else// Data or channel quality coded bits, Rank Indication coded bits or ACK/NACK coded bits

end if

end if

i = i + 1

end while

where x and y are tags defined in TS 36.212 [3] clause 5.2.2.6 and where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe where  corresponds to the RNTI associated with the PUSCH transmission as described in clause 8 in TS 36.213 [4]. For AUL PUSCH, nRNTI=0.

For BL/CE UEs,

-if the PUSCH transmission is using sub-PRB allocations, the scrambling sequence generator shall be initialised with

cinit=nRNTI⋅214+q⋅213+ iMRU⋅MslotsUL / 2  mod 10⋅29+NIDcell

at the first valid uplink subframe of every  subframes comprising the allocated UL resource unit(s), where, and N is the number of BL/CE UL subframes for the PUSCH transmission as determined in clause 8.0 in [4].MRU⋅MslotsUL / 2 i=0, 1, …,N-1

-otherwise, the same scrambling sequence is applied per subframe to PUSCH for a given block of  subframes. The subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies . For the block of  subframes, the scrambling sequence generator shall be initialised with

where

and  is the absolute subframe number of the first uplink subframe intended for PUSCH. The PUSCH transmission spans  consecutive subframes including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission. For a BL/CE UE configured in CEModeA, . For a BL/CE UE configured with CEModeB,  for frame structure type 1 and  for frame structure type 2.

For PUSCH with a subframe duration, up to two codewords can be transmitted in one subframe, i.e., . In the case of single-codeword transmission, .

## 5.3.2Modulation

For each codeword, the block of scrambled bits  shall be modulated as described in clause 7.1, resulting in a block of complex-valued symbols . Table 5.3.2-1 specifies the modulation mappings applicable for the physical uplink shared channel. For sub-PRB allocations only π/2 BPSK and QPSK are supported.

Table 5.3.2-1: Uplink modulation schemes

## 5.3.2ALayer mapping

The complex-valued modulation symbols for each of the codewords to be transmitted are mapped onto one or two layers. Complex-valued modulation symbols  for codeword  shall be mapped onto the layers ,  where  is the number of layers and  is the number of modulation symbols per layer.

## 5.3.2A.1Layer mapping for transmission on a single antenna port

For transmission on a single antenna port, a single layer is used, , and the mapping is defined by

with .

## 5.3.2A.2Layer mapping for spatial multiplexing

For spatial multiplexing, the layer mapping shall be done according to Table 5.3.2A.2-1. The number of layers  is less than or equal to the number of antenna ports  used for transmission of the physical uplink shared channel. The case of a single codeword mapped to multiple layers is only applicable when the number of antenna ports used for PUSCH is four, except for slot-PUSCH and subslot-PUSCH transmission where a single codeword is used irrespective of the number of layers.

Table 5.3.2A.2-1: Codeword-to-layer mapping for spatial multiplexing

## 5.3.3Transform precoding

For each layer  the block of complex-valued symbols  is divided into  sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to

resulting in a block of complex-valued symbols . The variable, where  represents the bandwidth of the PUSCH in terms of resource blocks, and shall fulfil

where  is a set of non-negative integers.

In case of PUSCH transmissions using sub-PRB allocations for BL/CE UEs, the variable .

## 5.3.3APrecoding

The precoder takes as input a block of vectors ,  from the transform precoder and generates a block of vectors ,  to be mapped onto resource elements.

## 5.3.3A.1Precoding for transmission on a single antenna port

For transmission on a single antenna port, precoding is defined by

where , .

## 5.3.3A.2Precoding for spatial multiplexing

Precoding for spatial multiplexing is only used in combination with layer mapping for spatial multiplexing as described in clause 5.3.2A.2. Spatial multiplexing supports  or  antenna ports where the set of antenna ports used for spatial multiplexing is  and , respectively.

Precoding for spatial multiplexing is defined by

where , .

The precoding matrix  of size  is given by one of the entries in Table 5.3.3A.2-1 for  and by Tables 5.3.3A.2-2 through 5.3.3A.2-5 for  where the entries in each row are ordered from left to right in increasing order of codebook indices.

Table 5.3.3A.2-1: Codebook for transmission on antenna ports

Table 5.3.3A.2-2: Codebook for transmission on antenna ports  with

Table 5.3.3A.2-3: Codebook for transmission on antenna ports  with

Table 5.3.3A.2-4: Codebook for transmission on antenna ports  with

Table 5.3.3A.2-5: Codebook for transmission on antenna ports  with

## 5.3.4Mapping to physical resources

For each antenna port  used for transmission of the PUSCH in a subframe the block of complex-valued symbols  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in clause 5.1.1.1 in TS 36.213 [4], and mapped in sequence starting with  to physical resource blocks on antenna port  and assigned for transmission of PUSCH. The relation between the index  and the antenna port number  is given by Table 5.2.1-1. The mapping to resource elements  corresponding to the physical resource blocks assigned for transmission shall fulfil the following criteria:

-not used for transmission of reference signals, and

-not part of the last SC-FDMA symbol in a subframe, if the UE transmits SRS in the same subframe in the same serving cell, and

-not part of the last SC-FDMA symbol in a subframe configured with cell-specific SRS for non-BL/CE UEs and BL/CE UEs in CEModeA, if the PUSCH transmission partly or fully overlaps with the cell-specific SRS bandwidth, and

-not part of an SC-FDMA symbol reserved for possible trigger type 1 SRS transmission as specified in [4] in a UE-specific aperiodic SRS subframe in the same serving cell, and

-not part of an SC-FDMA symbol reserved for possible trigger type 0 SRS transmission as specified in [4] in a UE-specific periodic SRS subframe in the same serving cell when the UE is configured with multiple TAGs

-not part of the first SC-FDMA symbol in a subframe if the associated DCI indicates PUSCH starting position '01', '10', or '11' and does not indicate PUSCH mode 2.

-not part of the first SC-FDMA symbol in the second slot in a subframe if the associated DCI indicates PUSCH starting position '01', '10', or '11' and PUSCH mode 2.

-not part of the last SC-FDMA symbol in a subframe if the associated DCI indicates PUSCH ending symbol '1' and does not indicate PUSCH mode 3.

-not part of the second slot in a subframe if the associated DCI indicates PUSCH ending symbol '0' and PUSCH mode 3.

-not part of SC-FDMA symbols 5 to 13 in a subframe if the associated DCI indicates PUSCH ending symbol '1' and PUSCH mode 3.

The mapping to resource elements  shall be in increasing order of first the index , then the index . The mapping starts with the first slot in an uplink subframe, except for slot-PUSCH, subslot-PUSCH transmission, or PUSCH mode 2.

In case of PUSCH transmissions using sub-PRB allocations for BL/CE UEs, the mapping starts over in every valid uplink subframe composing an UL resource unit.

In case of slot-PUSCH, the mapping shall start at  in the slot assigned for transmission.

In case of PUSCH mode 2, the mapping shall start at  in the second slot of the subframe assigned for transmission.

In case of subslot-PUSCH, the mapping shall start at symbol  where the start of the mapping is dependent on the uplink subslot number in the subframe assigned for transmission and the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-1 where starting symbol index "4" for subslot #5 is applied if the UE has indicated the capability ul-pattern-ddd-r15.

Table 5.3.4-1: Starting symbol index for subslot-PUSCH transmission

In case of a semi-persistently scheduled subslot-PUSCH, and semi-persistent scheduling (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]) with a configured periodicity of 1 subslot (i.e. semiPersistSchedIntervalUL-STTI set to sTTI1), the mapping shall start at symbol  depending on the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-2.

In case of a semi-persistently scheduled subslot-PUSCH and semi-persistent scheduling (the higher layer parameter sps-ConfigUL-sTTI-r15 is configured, see TS 36.331 [9]) with repetitions enabled (the higher layer parameter totalNumberPUSCH-SPS-STTI-UL-Repetitions is configured), the mapping shall start at symbol  depending on the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-2.

Table 5.3.4-2: Starting symbol index for subslot-PUSCH transmission in case of semi-persistent scheduling with a configured periodicity of 1 subslot

In case of subslot-PUSCH and semi-persistent scheduling with a configured periodicity longer than 1 subslot the mapping shall start at symbol  according to the first row of Table 5.3.4-2 (i.e. equivalent to a signalling of DMRS-pattern field set to '00').

For the UpPTS, the mapping shall start at symbol  and if dmrsLess-UpPts is set to true the mapping shall end at symbol  in the second slot of a special subframe, otherwise, the mapping shall end at symbol  in the second slot of a special subframe.

For BL/CE UEs, the PUSCH transmission is restricted as follows:

-For CEModeA, if the PUSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz, the maximum number of allocatable PRBs for PUSCH is 24 PRBs. The allocatable PRBs include the PRBs belonging to the narrowbands defined in clause 5.2.4 and the odd PRB at the center of the uplink system bandwidth in case of odd total number of uplink PRBs. If a resource assignment or frequency hopping would result in a PUSCH resource allocation outside the allocatable PRBs then the PUSCH transmission in that subframe is dropped.

-For all other cases, the maximum number of allocatable PRBs for PUSCH is 6 PRBs restricted to one of the narrowbands defined in clause 5.2.4.

For BL/CE UEs in CEModeB, resource elements in the last SC-FDMA symbol in a subframe configured with cell-specific SRS shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

For BL/CE UEs, if one or more SC-FDMA symbol(s) are left empty due to guard period for narrowband or wideband retuning, the affected SC-FDMA symbol(s) shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

For a UE configured with SRS carrier switching, if the first symbol in a subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the first SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with SRS carrier switching, if the last symbol in a subframe is counted in the PUSCH mapping and the last symbol in the subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with SRS carrier switching, if the last symbol in a subframe is not counted in the PUSCH mapping and the second-to-last symbol in the subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the second-to-last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with PUSCH Mode 1, if DCI indicates PUSCH mode 1 enabled and the corresponding transmission of PUSCH starts in the second slot of a subframe, the resource elements in the first slot of the subframe shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with autonomous uplink,

-if the UE indicates PUSCH ending symbol '1' in uplink control information, or endingSymbolAUL is set to '12', the resource elements in the last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH;

-if the UE indicates PUSCH starting symbol '1' in uplink control information, the resource elements in the first SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

If uplink frequency-hopping is disabled or the resource blocks allocated for PUSCH transmission are not contiguous in frequency, the set of physical resource blocks to be used for transmission is given by  where  is obtained from the uplink scheduling grant as described in clause 8.1 in TS 36.213 [4].

If uplink frequency-hopping with type 1 PUSCH hopping is enabled, the set of physical resource blocks to be used for transmission is given by clause 8.4.1 in TS 36.213 [4].

If uplink frequency-hopping with predefined hopping pattern is enabled, the set of physical resource blocks to be used for transmission in slot  is given by the scheduling grant together with a predefined pattern according to

where  is obtained from the scheduling grant as described in clause 8.1 in TS 36.213 [4]. The parameter pusch-HoppingOffset,, is provided by higher layers. The size  of each sub-band is given by,

where the number of sub-bands  is given by higher layers. The function  determines whether mirroring is used or not. The parameter Hopping-mode provided by higher layers determines if hopping is "inter-subframe" or "intra and inter-subframe".

The hopping function and the function are given by

where  and the pseudo-random sequence  is given by clause 7.2 and CURRENT_TX_NB indicates the transmission number for the transport block transmitted in slot as defined in [8]. The pseudo-random sequence generator shall be initialised with  for frame structure type 1 and  for frame structure type 2 at the start of each frame.

For BL/CE UEs, the PRB resources for PUSCH transmission in the first subframe are obtained from the DCI as described in clauses 5.3.3.1.10 and 5.3.3.1.11 in [3], or from higher layers in PUR-Config when PUSCH is transmitted using preconfigured uplink resources. Each of the  PUSCH codewords is transmitted with repetitions, where  is the number of transport blocks defined in clause 8.0 of TS 36.213 [4]. The PUSCH transmission spans  consecutive subframes, including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission if . NTB≥1NTBNabsPUSCH≥NTBNrepPUSCH

-If uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with  associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 8.0 in [4], the PUSCH transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

-In a subframe that is partially reserved, the reserved SC-FDMA symbols shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

-In case the UE is a BL/CE UE configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15 or subPRB-Allocation in PUR-PUSCH-Config, the PUSCH transmission spans  consecutive subframes including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission, where  is the number of scheduled TBs if ce-PUSCH-MultiTB-Config is enabled and multiple TBs are scheduled, otherwise . NabsPUSCH≥NTBNrepPUSCHMRUMslotsUL/2NTBNTB=1

-For BL/CE UE in CEModeA,

-If PUSCH is transmitted using preconfigured uplink resources,

-PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

-Else, if PUSCH scheduled by DCI format 6-0A is associated with PUR-RNTI,

-PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set and the frequency hopping flag in DCI format 6-0A indicates frequency hopping, otherwise frequency hopping is disabled.

-Else,

-PUSCH frequency hopping is enabled when the higher-layer parameter pusch-HoppingConfig is set and the frequency hopping flag in DCI format 6-0A indicates frequency hopping, otherwise frequency hopping is disabled.

-For BL/CE UE in CEModeB,

-If PUSCH is transmitted using preconfigured uplink resources,

-PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

-Else, if PUSCH scheduled by DCI format 6-0B is associated with PUR-RNTI,

-PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

-Else,

-PUSCH frequency hopping is enabled when the higher-layer parameter pusch-HoppingConfig is set, otherwise frequency hopping is disabled.

-If frequency hopping is not enabled for PUSCH, all PUSCH repetitions are located at the same PRB resources.

-If a BL/CE UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig, the UE is not expected to have the frequency hopping enabled for PUSCH with the resource allocation including the center PRB not belonging to any narrowband.

-If frequency hopping is enabled for PUSCH and the UE is not configured with CEModeA and higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

-PUSCH is transmitted in uplink subframe  within the  consecutive subframes using the same number of consecutive PRBs as in the previous subframe starting from the PRB resources of the narrowband  with the same RIV as that of narrowband . The narrowband  is defined as

where  is the absolute subframe number of the first UL subframe intended for carrying the PUSCH and  and  are cell-specific higher-layer parameters. For the  consecutive subframes, the UE shall not transmit PUSCH in subframe  if it is not a BL/CE UL subframe.

-If frequency hopping is enabled for PUSCH and the UE is configured with CEModeA and higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

-Except when the PUSCH resource allocation includes the center PRB not belonging to any narrowband, PUSCH is transmitted in uplink subframe  within the  consecutive subframes using the same number of consecutive PRBs as in the previous subframe, where  is the narrowband index that starting PRB located in the absolute subframe number of the first UL subframe , defined as nNB(i0)i0

-If 0 or  with ,  NRBUL mod 2=NRBUL mod 2=1RBSTART<NRBUL2nNB(i0) =RBSTART-le6

-If with   NRBUL mod 2=1 RBSTART>NRBUL2,nNB(i0) =RBSTART-le-16

where  is the number of edge PRB(s) not belonging to narrowbands in one side of system bandwidth ,  is the number of narrowbands, the starting PRB index  and the length   of the allocated resources are defined in clause 8.1.1 of [4]. After hopping, the narrowband  in subframe  is defined asle=NRBUL2-6NNBUL2NRBULNNBULRBSTARTLCRBs

where  and  are cell-specific higher-layer parameters. For the   consecutive subframes, the UE shall not transmit PUSCH in subframe  if it is not a BL/CE UL subframe. After hopping, the resource blocks have the same relative location of starting PRB in  as in narrowband . nNB(i)nNB(i0)

-If frequency hopping is enabled for PUSCH and the UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

-If a frequency hopping leads to a split resource allocation, where some PRB(s) is (are) on one edge and some PRB(s) is (are) on the other edge of the system bandwidth, the PUSCH transmission is dropped in that subframe.

-If a frequency hopping leads to a resource allocation, where some PRB(s) is (are) not belonging to any narrowband, the PUSCH transmission is dropped in that subframe.

For BL/CE UEs, for PUSCH transmission corresponding to the random access response grant and its retransmission, frequency hopping of the PUSCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

-if PRACH CE level 0 or 1 is used for the last PRACH attempt,  is set to the higher layer parameter interval-UlHoppingConfigCommonModeA;

-if PRACH CE level 2 or 3 is used for the last PRACH attempt,  is set to the higher layer parameter interval-UlHoppingConfigCommonModeB.

For BL/CE UEs in CEModeB, for PUSCH transmission not associated with Temporary C-RNTI, for frame structure type 1, after a transmission duration of  time units (which may include subframes that are not BL/CE UL subframes), a gap of  time units shall be inserted, according to the UE capability ue-CE-NeedULGaps, as specified in TS 36.331 [9]. BL/CE UL subframes within the gap of  time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH.

For BL/CE UEs, for PUSCH transmission associated with Temporary C-RNTI for frame structure type 1, and if PRACH CE level 2 or 3 is used for the last PRACH attempt, after a transmission duration of  time units (which may include subframes that are not BL/CE UL subframes), a gap of  time units shall be inserted. BL/CE UL subframes within the gap of  time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH.

For UEs configured with PUSCH-EnhancementsConfig, the number of PUSCH subframe repetitions  and the PRB resources for PUSCH transmission in the first subframe are obtained from the DCI as described in clause 5.3.3.1.1C in [3]. The PUSCH transmission spans  consecutive subframes, including DL subframes where the UE postpones the PUSCH transmission in the case of frame structure type 2. PUSCH frequency hopping is enabled when the higher-layer parameters pusch-HoppingOffsetPUSCH-Enh and interval-ULHoppingPUSCH-Enh are set and the frequency hopping flag in DCI format 0C indicates frequency hopping, otherwise frequency hopping is disabled. If frequency hopping is not enabled for PUSCH, the PUSCH repetitions are located at the same PRB resources as in the first subframe. If frequency hopping is enabled for PUSCH, PUSCH is transmitted in uplink subframe  within the  consecutive subframes using the PRB resources starting at PRB index

nPRBi=nPRBi0if iNPRB,hopPUSCH-j0mod 2=0 nPRBi0+fPRB,hopPUSCHmod NPRBULif iNPRB,hopPUSCH-j0mod 2=1

j0=i0NPRB,hopPUSCH, i0≤i≤i0+ NabsPUSCH-1

where  is the absolute subframe number of the first UL subframe carrying the PUSCH and  is given by the higher-layer parameter interval-ULHoppingPUSCH-Enh and  is given by the higher-layer parameter pusch-HoppingOffsetPUSCH-Enh.

For BL/CE UEs communicating over NTN, for PUSCH transmission, for frame structure type 1, after a transmission duration of  time units (which may include subframes that are not BL/CE UL subframes), a transmission gap of  time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH, according to the single UE capability ntn-SegmentedPrecompensationGaps-r17, as specified in 3GPP TS 36.331 [9]. The quantity  is provided by higher layers, and the quantity  is configured by higher layers based on the UE capability, if signalled.NsegmentprecompensationNgapprecompensationNsegmentprecompensationNgapprecompensation

## 5.4Physical uplink control channel

The physical uplink control channel, PUCCH, carries uplink control information. Simultaneous transmission of PUCCH and PUSCH from the same UE is supported if enabled by higher layers. For frame structure type 2, the PUCCH is not transmitted in the UpPTS field.

The physical uplink control channel supports multiple formats as shown in Table 5.4-1 with different number of bits per subframe, where  represents the bandwidth of the PUCCH format 4 as defined by clause 5.4.2B, and  and  are defined in Table 5.4.2C-1.

Formats 2a and 2b are supported for normal cyclic prefix only.

Table 5.4-1: Supported PUCCH formats

All PUCCH formats use a cyclic shift, , which varies with the symbol number  and the slot number  according to

where the pseudo-random sequence  is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with , where  is given by clause 5.5.1.5 with  corresponding to the primary cell, at the beginning of each radio frame.

The physical resources used for PUCCH format 1/1a/1b and PUCCH format 2/2a/2b depends on two parameters,  and , given by higher layers. The variable  denotes the bandwidth in terms of resource blocks that are available for use by PUCCH formats 2/2a/2b transmission in each slot. The variable  denotes the number of cyclic shift used for PUCCH formats 1/1a/1b in a resource block used for a mix of formats 1/1a/1b and 2/2a/2b. The value of  is an integer multiple of  within the range of {0, 1, …, 7}, where  is provided by higher layers. No mixed resource block is present if . At most one resource block in each slot supports a mix of formats 1/1a/1b and 2/2a/2b. Resources used for transmission of PUCCH formats 1/1a/1b, 2/2a/2b, 3, 4, and 5 are represented by the non-negative indices , , ,  and , respectively.

## 5.4.1PUCCH formats 1, 1a and 1b

For PUCCH format 1, information is carried by the presence/absence of transmission of PUCCH from the UE. In the remainder of this clause,  shall be assumed for PUCCH format 1.

For PUCCH formats 1a and 1b, one or two explicit bits are transmitted, respectively. The block of bits  shall be modulated as described in Table 5.4.1-1, resulting in a complex-valued symbol. The modulation schemes for the different PUCCH formats are given by Table 5.4-1.

The complex-valued symbol  shall be multiplied with a cyclically shifted length  sequence  for each of the  antenna ports used for PUCCH transmission according to

where  is defined by clause 5.5.1 with and . The antenna-port specific cyclic shift  varies between symbols and slots as defined below.

The block of complex-valued symbols  shall be scrambled by  and block-wise spread with the antenna-port specific orthogonal sequence  according to

where

and

with  for the two slots in a subframe given by Table 5.4.1-1a. The sequence  is given by Table 5.4.1-2 and Table 5.4.1-3 and  is defined below.

Resources used for transmission of PUCCH format 1, 1a and 1b are identified by a resource index  from which the orthogonal sequence index  and the cyclic shift  are determined according to

where

The resource indices within the two resource blocks in the two slots of a subframe to which the PUCCH is mapped are given by

for  and by

for , where , with for normal CP and for extended CP.

The parameter deltaPUCCH-Shift  is provided by higher layers.

Table 5.4.1-1: Modulation symbol  for PUCCH formats 1a and 1b

Table 5.4.1-1a: The quantity  for PUCCH formats 1a and 1b

Table 5.4.1-2: Orthogonal sequences  for

Table 5.4.1-3: Orthogonal sequences  for

## 5.4.2PUCCH formats 2, 2a and 2b

The block of bits  shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits  according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe where  is C-RNTI.

The block of scrambled bits  shall be QPSK modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols .

Each complex-valued symbol  shall be multiplied with a cyclically shifted length  sequence  for each of the  antenna ports used for PUCCH transmission according to

where  is defined by clause 5.5.1 with and .

Resources used for transmission of PUCCH formats 2/2a/2b are identified by a resource index  from which the cyclic shift  is determined according to

where

and

for  and by

for .

For PUCCH formats 2a and 2b, supported for normal cyclic prefix only, the bit(s)  shall be modulated as described in Table 5.4.2-1 resulting in a single modulation symbol  used in the generation of the reference-signal for PUCCH format 2a and 2b as described in clause 5.5.2.2.1.

Table 5.4.2-1: Modulation symbol  for PUCCH formats 2a and 2b

## 5.4.2APUCCH format 3

The block of bits  shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits  according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe where  is the C-RNTI.

The block of scrambled bits  shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols  where .

The complex-valued symbols  shall be block-wise spread with the orthogonal sequences  and  resulting in  sets of  values each according to

where  for both slots in a subframe using normal PUCCH format 3 and , holds for the first and second slot, respectively, in a subframe using shortened PUCCH format 3. The orthogonal sequences  and  are given by Table 5.4.2A-1. Resources used for transmission of PUCCH format 3 are identified by a resource index  from which the quantities  and  are derived according to

Each set of complex-valued symbols shall be cyclically shifted according to

where  is given by Clause 5.4,  is the slot number within a radio frame and  is the SC-FDMA symbol number within a slot.

The shifted sets of complex-valued symbols shall be transform precoded according to

where  is the number of antenna ports used for PUCCH transmission, resulting in a block of complex-valued symbols .

Table 5.4.2A-1: The orthogonal sequence

## 5.4.2BPUCCH format 4

The block of bits  shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits  according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe where  is the C-RNTI.

The block of scrambled bits  shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols  where .

The block of complex-valued symbols  is divided into  sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to

where ,  and  are given by Table 5.4.2C-1 for normal PUCCH format 4 and shortened PUCCH format 4, resulting in a block of complex-valued symbols . The variable, where  represents the bandwidth of the PUCCH format 4 in terms of resource blocks, shall fulfil

where  is a set of non-negative integers.

## 5.4.2CPUCCH format 5

The block of bits  shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits  according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe where  is the C-RNTI.

The block of scrambled bits  shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols  where .

The complex-valued symbols  shall be divided into  sets, each corresponding to one SC-FDMA symbol. Block-wise spreading shall be applied according to

where ,  and  are given by Table 5.4.2C-1 for normal PUCCH format 5 and shortened PUCCH format 5, and  is given by Table 5.4.2C-2 with  provided by higher layers.

The block-wise spread complex-valued symbols shall be transform precoded according to

where , resulting in a block of complex-valued symbols .

Table 5.4.2C-1: The quantities  and

Table 5.4.2C-2: Orthogonal sequences

## 5.4.3Mapping to physical resources

The block of complex-valued symbols  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power  specified in Clause 5.1.2.1 in TS 36.213 [4], and mapped in sequence starting with  to resource elements. PUCCH uses one or more resource block in each of the two slots in a subframe. Within the physical resource block(s) used for transmission, the mapping of  to resource elements  on antenna port  and not used for transmission of reference signals shall be in increasing order of first , then  and finally the slot number, starting with the first slot in the subframe. The relation between the index  and the antenna port number  is given by Table 5.2.1-1.

For non-BL/CE UEs, except for PUCCH format 4, the physical resource blocks to be used for transmission of PUCCH in slot  are given by

For BL/CE UEs, PUCCH is transmitted with  repetitions.

-The BL/CE UE is not expected to transmit with  when ce-PDSCH-14HARQ-Config is configured. NrepPUCCH>1

The PUCCH transmission spans  consecutive subframes, including subframes that are not BL/CE UL subframes where the UE postpones the PUCCH transmission if . If the BL/CE UE is configured with ce-HARQ-AckDelay-r17 indicating Alt-2e, the UE does not postpone the PUCCH transmission.

-The quantity  is given

-by the higher layer parameter pucch-NumRepetitionCE-Format1 for PUCCH format 1/1a and pucch-NumRepetitionCE-Format2 for PUCCH format 2/2a/2b, if configured. Otherwise

-by the higher-layer parameter pucch-NumRepetitionCE-Msg4-Level0-r13, pucch-NumRepetitionCE-Msg4-Level1-r13, pucch-NumRepetitionCE-Msg4-Level2-r13 or pucch-NumRepetitionCE-Msg4-Level3-r13.

-If uplink resource reservation is enabled for the UE as specified in [9], then in case of PUCCH transmission with  associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUCCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 8.0 in [4], the PUCCH transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

-In a subframe that is partially reserved, the reserved SC-FDMA symbols shall be counted in the PUCCH mapping but not used for transmission of the PUCCH.

The physical resource blocks to be used for transmission of PUCCH in subframe  within the  consecutive subframes are given by

where  is the absolute subframe number of the first uplink subframe intended for PUCCH.

The variable  depends on the PUCCH format.

-Formats 1, 1a and 1b:

-Formats 2, 2a and 2b:

-Format 3:

-Format 5 (non-BL/CE UEs only):

For non-BL/CE UEs, for PUCCH format 4, the physical resource blocks to be used for transmission of PUCCH in slot  are given by

where  is obtained from [4].

Mapping of modulation symbols for the physical uplink control channel for PUCCH formats 1 – 3 is illustrated in Figure 5.4.3-1.

In case of simultaneous transmission of sounding reference signal and PUCCH format 1, 1a, 1b, 3, 4 or 5 when there is one serving cell configured, the shortened PUCCH format shall be used where the last SC-FDMA symbol in the second slot of a subframe shall be left empty.

In case of guard period for narrowband or wideband retuning for BL/CE UEs, if an SC-FDMA symbol is left empty due to guard period, the SC-FDMA symbol shall be counted in the PUCCH mapping but not used for transmission of the PUCCH. The SC-FDMA symbol affected by the guard period can be the first SC-FDMA symbol in the first slot of a subframe and/or the last SC-FDMA symbol in the second slot of a subframe.

For BL/CE UEs communicating over NTN, for PUCCH transmission, for frame structure type 1, after a transmission duration of  time units (which may include subframes that are not BL/CE UL subframes), a transmission gap of  time units shall be counted for the PUCCH resource mapping but not used for transmission of the PUCCH, according to the single UE capability ntn-SegmentedPrecompensationGaps-r17, as specified in 3GPP TS 36.331 [9]. The quantity  is provided by higher layers, and the quantity  is configured by higher layers based on the UE capability, if signalled.NsegmentprecompensationNgapprecompensationNsegmentprecompensationNgapprecompensation

Figure 5.4.3-1: Mapping to physical resource blocks for PUCCH formats 1 – 3 for non-BL/CE UEs.

## 5.4AShort Physical Uplink Control Channel

## 5.4A.1General

The short physical uplink control channel, SPUCCH, carries uplink control information. Simultaneous transmission of SPUCCH and PUSCH from the same UE where both SPUCCH and PUSCH is using either slot or subslot transmission is supported if enabled by higher layers (see simultaneousPUCCH-PUSCH in TS 36.331 [9]). For frame structure type 2 and in UpPTS, transmission of SPUCCH is not supported.

SPUCCH supports multiple formats as shown in Table 5.4A-1 and Table 5.4A-2 with different number of bits carried by each SPUCCH.

Table 5.4A-1: SPUCCH formats for slot transmission

Table 5.4A-2: SPUCCH formats for subslot transmission

The quantity  represents the bandwidth of the SPUCCH format 4 as defined by clause 5.4A.4.1, and  and  are defined in Table 5.4A.4.1-1 and Table 5.4A.4.2-1, respectively.

SPUCCH formats 1/1a/1b use a cyclic shift, , which varies with the symbol number  and the slot number  as described in clause 5.4.

## 5.4A.2SPUCCH formats 1,1a,1b

## 5.4A.2.1Slot-SPUCCH

Slot-SPUCCH format 1, 1a, 1b can be configured by higher layers to either have frequency hopping enabled or disabled (see n1SlotSPUCCH-FH-AN-List and n1SlotSPUCCH-NoFH-AN-List in TS 36.331 [9]).

In case slot-SPUCCH format 1, 1a, 1b and frequency hopping is enabled, the scrambled and block-wise spread complex-valued symbols  are generated as described in clause 5.4.1 for PUCCH format 1/1a/1b where ,  and.

In case slot-SPUCCH format 1, 1a, 1b and frequency hopping is disabled, the scrambled and block-wise spread complex-valued symbols  are generated as described in clause 5.4.1 for PUCCH format 1/1a/1b where .

Irrespective of frequency hopping being enabled or disabled,  is applied as described in clause 5.4.1 for the slot in which the slot-SPUCCH is transmitted in, i.e. either in the first or the second slot of the subframe.

Resources used for transmission of slot-SPUCCH format 1, 1a and 1b are identified by a resource index  from which the cyclic shift  is derived:

,

In case frequency hopping is enabled, the cyclic shift is determined as described in clause 5.4.2, assuming the condition  is fulfilled.

In case frequency hopping is disabled, the resource index  also indicates the orthogonal sequence index . Both the cyclic shift and the orthogonal sequence index is in this case determined as described in clause 5.4.1.

## 5.4A.2.2Subslot-SPUCCH

For subslot-SPUCCH formats 1a and 1b, one or two bits are communicated by SPUCCH resource selection. The resource set available for selection are configured by higher layers (see n1SubslotSPUCCH-AN-List and sr-SubslotSPUCCH-ResourceList in TS 36.331 [9]). For subslot-SPUCCH format 1, information is carried by the presence/absence of transmission of subslot-SPUCCH from the UE.

The sequence  is generated as described in clause 5.4.1, assuming .

The block of complex-valued symbols  shall be scrambled by  as described in clause 5.4.1 assuming , , and with replaced by , defined in Table 5.4A.2.2-1.

Table 5.4A.2.2-1: The quantity  for subslot-SPUCCH formats 1a and 1b

Resources used for transmission of SPUCCH format 1, 1a and 1b are identified by a resource index  from which the cyclic shift  is determined, as described in clause 5.4.2, assuming the condition  is fulfilled.The resource set for subslot-SPUCCH format 1/1a/1b is configured by higher layers (see n1SubslotSPUCCH-AN-List in TS 36.331 [9]):

-subslot-SPUCCH format 1:

-subslot-SPUCCH format 1a:

-subslot-SPUCCH format 1b:

Each resource indicates (a) bit state(s) as defined by Table 5.4A.2.2-2.

Table 5.4A.2.2-2: Subslot-SPUCCH resource for formats 1a and 1b

## 5.4A.3SPUCCH format 3

## 5.4A.3.1Slot-SPUCCH

The complex-valued modulation symbols  shall be generated as described in clause 5.4.2A.

Depending on if the slot-SPUCCH is transmitted in the first or the second slot of the subframe, different block-wise spreading with the orthogonal sequences  or  is applied. Each spreading results in  sets of  values each according to:

where

- (see clause 5.4.2A) if transmitted in the first slot, and (see clause 5.4.2A), if transmitted in the second slot.

-The orthogonal sequences  and  are given by Table 5.4.2A-1

Resources used for transmission of SPUCCH format 3 are identified by a resource index  from which the quantities  and  are derived according to clause 5.4A.3 by replacing  with .

Each set of complex-valued symbols shall be cyclically shifted and transform precoded according to clause 5.4.2A with  replaced by  in the transform precoding.

## 5.4A.4SPUCCH format 4

## 5.4A.4.1Slot-SPUCCH

The block of bits  shall be scrambled according to clause 5.4.2B.

The block of scrambled bits  shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols  where .

The block of complex-valued symbols  is divided into  (defined in Table 5.4A.4.1-1) sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to clause 5.4.2B replacing  with  and replacing  with .

The variable, where  represents the bandwidth of the SPUCCH format 4 in terms of resource blocks in the frequency domain, and is determined by higher layer signalling (n4numberOfPRB-r15, see TS 36.213 [4, Table 10.1.1-2] and TS 36.331 [9]), and shall fulfil

,

where,  is a set of non-negative integers.

Table 5.4A.4.1-1: The quantity  .

## 5.4A.4.2Subslot-SPUCCH

For subslot-SPUCCH the procedure of slot-SPUCCH in clause 5.4A.4.1 is followed except that:

-the block of complex-valued symbols  is divided into  (defined in Table 5.4A.4.2-1) sets, instead of  sets, and,

- is replaced by , in the transform precoding.

Table 5.4A.4.2-1: The quantity  .

## 5.4A.5Mapping to physical resources

The block of complex-valued symbols  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power  specified in Clause 5.1.2.1 of TS 36.213 [4], and mapped in sequence starting with  to resource elements.

SPUCCH uses one or more resource block in the frequency domain and is mapped to either a slot or a subslot in the time domain. Within the physical resource block(s) used for transmission, the mapping of  to resource elements  on antenna port  and not used for transmission of reference signals shall be in increasing order of first , then .

The starting symbol for each subslot number is provided by Table 5.4A.4.5-1 for subslot-SPUCCH.

For slot-SPUCCH the starting symbol is for the slot the SPUCCH is transmitted in.

Table 5.4A.5-1: Starting symbol for subslot-SPUCCH mapping

The relation between the index  and the antenna port number  is given by Table 5.2.1-1.

The physical resource blocks () within which the transmission of SPUCCH is carried out in slot  depends on the SPUCCH format and whether frequency hopping is enabled or not.

In case of slot-SPUCCH format 1, 1a, 1b and frequency hopping disabled, the PRB used is determined as described in clause 5.4.3 for PUCCH format 1, 1a, 1b.

In case of slot-SPUCCH format 3, the PRB used is given by

For the other SPUCCH formats, it is determined by Table 5.4A.5-2, Table 5.4A.5-3 and Table 5.4A.5-4.

Table 5.4A.5-2:  for slot-SPUCCH format 1, 1a, 1b with frequency hopping enabled

Table 5.4A.5-3:  for slot-SPUCCH format 4

Table 5.4A.5-4:  for subslot-SPUCCH format 1, 1a, 1b, 4

The variable  depends on the SPUCCH format as defined in Table 5.4A.5-5.

Table 5.4A.5-5:  for SPUCCH

In case of subslot-SPUCCH, there is a configuration restriction that each SPUCCH resource in the resource set, of up to four resources, , shall map to the same pair of PRBs () This restriction applies separately to each of n1SubslotSPUCCH-AN-List and sr-SubslotSPUCCH-Resource in TS 36.331 [9].

In case of simultaneous transmission of sounding reference signal and SPUCCH when there is one serving cell configured, the shortened SPUCCH format shall be used where the last SC-FDMA symbol in the second slot of a subframe shall be left empty.

## 5.5Reference signals

Two types of uplink reference signals are supported:

-Demodulation reference signal, associated with transmission of PUSCH or (S)PUCCH

-Sounding reference signal, not associated with transmission of PUSCH or (S)PUCCH

The same set of base sequences is used for demodulation and sounding reference signals.

## 5.5.1Generation of the reference signal sequence

Reference signal sequence  is defined by a cyclic shift  of a base sequence  according to

where

- is the length of the reference signal sequence, ,  is defined in clause 5.5.2.1.2, and,

- when either

-the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

-the Cyclic Shift Field mapping table for DMRS bit is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, and

- otherwise.

Multiple reference signal sequences are defined from a single base sequence through different values of .

Base sequences  are divided into groups, where  is the group number and  is the base sequence number within the group, such that each group contains one base sequence () of each length ,  and two base sequences () of each length , . The sequence group number  and the number  within the group may vary in time as described in clauses 5.5.1.3 and 5.5.1.4, respectively. The definition of the base sequence  depends on the sequence length.

## 5.5.1.1Base sequences of length  or larger

For, the base sequence  is given by

where the  root Zadoff-Chu sequence is defined by

with  given by

The length  of the Zadoff-Chu sequence is given by the largest prime number such that.

## 5.5.1.2Base sequences of length less than

For , , , and , the base sequence is given by

where the value of  is given by Table 5.5.1.2-1, Table 5.5.1.2-2, Table 5.5.1.2-3, and Table 5.5.1.2-4 for , , , and , respectively. For , the base sequence  is given by

Table 5.5.1.2-1: Definition of  for .

Table 5.5.1.2-2: Definition of  for

Table 5.5.1.2-3: Definition of  for

Table 5.5.1.2-4: Definition of  for

## 5.5.1.3Group hopping

The sequence-group number  in slot  is defined by a group hopping pattern  and a sequence-shift pattern  according to

There are 17 different hopping patterns and 30 different sequence-shift patterns. Sequence-group hopping can be enabled or disabled by means of the cell-specific parameter Group-hopping-enabled provided by higher layers. Sequence-group hopping for PUSCH can be disabled for a certain UE through the higher-layer parameter Disable-sequence-group-hopping despite being enabled on a cell basis unless the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure.

The group-hopping pattern  may be different for PUSCH, (S)PUCCH and SRS and is given by

where the pseudo-random sequence  is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with  at the beginning of each radio frame where  is given by clause 5.5.1.5.

The sequence-shift pattern  definition differs between PUCCH, PUSCH and SRS.

For SPUCCH/PUCCH, the sequence-shift pattern  is given by  where  is given by clause 5.5.1.5.

For PUSCH, the sequence-shift pattern  is given by , where  is configured by higher layers, if no value for  is provided by higher layers or if the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure, otherwise it is given by  with  given by clause 5.5.1.5.

For SRS, the sequence-shift pattern  is given by where  is given by clause 5.5.1.5.

## 5.5.1.4Sequence hopping

Sequence hopping only applies for reference-signals of length .

For reference-signals of length , the base sequence number  within the base sequence group is given by .

For reference-signals of length , the base sequence number  within the base sequence group in slot  is defined by

where the pseudo-random sequence  is given by clause 7.2. The parameter Sequence-hopping-enabled provided by higher layers determines if sequence hopping is enabled or not. Sequence hopping for PUSCH can be disabled for a certain UE through the higher-layer parameter Disable-sequence-group-hopping despite being enabled on a cell basis unless the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure.

For PUSCH or SPUCCH/PUCCH format 4 transmission with ≥ 6 RBs, the pseudo-random sequence generator shall be initialized with  at the beginning of each radio frame where  is given by clause 5.5.1.5.

For SRS, the pseudo-random sequence generator shall be initialized with  at the beginning of each radio frame where  is given by clause 5.5.1.5 and  is given by clause 5.5.1.3.

## 5.5.1.5Determining virtual cell identity for sequence generation

The definition of  depends on the type of transmission.

Transmissions associated with PUSCH:

- if no value for  is configured by higher layers or if the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure,

- otherwise.

Transmissions associated with SPUCCH/PUCCH:

- if no value for  is configured by higher layers,

- otherwise.

Basic sounding reference signals:

- if the higher-layer parameter srs-VirtualCellID is configured and srs-VirtualCellID-AllSRS is configured as TRUE, where  equals the higher-layer parameter srs-VirtualCellIDnIDRS=nIDSRSnIDSRS

- otherwise.nIDRS=NIDcell

Additional sounding reference signals:

- if no value for  is configured by the higher-layer parameter srs-VirtualCellIDnIDRS=NIDcellnIDSRS

- otherwise.nIDRS=nIDSRS

## 5.5.2Demodulation reference signal

## 5.5.2.1Demodulation reference signal for PUSCH

## 5.5.2.1.1Reference signal sequence

The PUSCH demodulation reference signal sequence  associated with layer  is defined by

where

and  if

-the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

-the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, or,

-subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]), and ifdma-Config-SPS is set.

In all other cases, .

Clause 5.5.1 defines the sequence  where, for PUSCH demodulation reference signal sequence,  when

-the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

-the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, or,

-subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]), and ifdma-Config-SPS is set.

In all other cases, .

The orthogonal sequence  is given by  for subslot-PUSCH/slot-PUSCH. In all other cases, it is given by  for DCI format 0 if the higher-layer parameter Activate-DMRS-with OCC is not set or if the temporary C-RNTI was used to transmit the most recent uplink-related DCI for the transport block associated with the corresponding PUSCH transmission. Otherwise,

-if higher-layer parameter ul-DMRS-IFDMA is not set,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI [3],

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is not present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 0, and

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 1.

The cyclic shift  in a slot  is given as if the ul-V-SPS-RNTI-r14 was used to transmit the most recent uplink-related DCI for the transport block associated with the corresponding PUSCH transmission. For PUSCH transmissions not using sub-PRB allocations, if pusch-CyclicShift in higher layer parameter PUR-PUSCH-Config is configured, then for PUSCH (re)transmission corresponding to preconfigured uplink resource it provides the value of  and the cyclic shift  in a slot  is given as .ncs,λ

Otherwise, the cyclic shift  in a slot  is given as  with

where the value of  is given by Table 5.5.2.1.1-2 according to the parameter cyclicShift provided by higher layers. For non-BL/CE UEs  is given using the most recent uplink-related DCI TS 36.212 [3] for the transport block associated with the corresponding PUSCH transmission, except for subslot-PUSCH/slot-PUSCH, as follows:

-if the higher-layer parameter ul-DMRS-IFDMA is not set,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is not present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 0, and

-if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI,  is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 1.

For subslot-PUSCH/slot-PUSCH for non-BL/CE UEs, is given by Table 5.5.2.1.1-4, using the cyclic shift field in the most recent uplink-related DCI. If the Cyclic Shift Field mapping table for DMRS bit field is set to 0, in Table 5.5.2.1.1-4 is ignored. If the Cyclic Shift Field mapping table for DMRS bit field is set to 1, both  and are given by Table 5.5.2.1.1-4.

For BL/CE UEs, a cyclic shift field of '000' shall be assumed when determining  from Table 5.5.2.1.1-1.

For subframe-based PUSCH transmission, the first row of Table 5.5.2.1.1-1 shall be used to obtain  and  if there is no uplink-related DCI for the same transport block associated with the corresponding PUSCH transmission, and

-if the initial PUSCH for the same transport block is semi-persistently scheduled and cyclicShiftSPS is not configured, or

-if the initial PUSCH for the same transport block is scheduled by the random-access response grant.

An exception applies if subframe-based PUSCH for the transport block is semi-persistently scheduled and the higher-layer parameter cyclicShiftSPS is configured. In this case, the value of  is given by Table 5.5.2.1.1-1 according to the higher-layer parameter cyclicShiftSPS.

An exception applies if subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (see TS 36.331, sps-ConfigUL-sTTI). In this case:

- is given by Table 5.5.2.1.1-1 according to the higher-layer parameter cyclicShiftSPS-STTI if the higher layer parameter ifdma-Config-SPS is not set, and,

- and are given by Table 5.5.2.1.1-3 according to the higher-layer parameter cyclicShiftSPS-STTI if the higher layer parameter ifdma-Config-SPS is set.

The quantity  is given by

where the pseudo-random sequence  is defined by clause 7.2. The application of  is cell-specific. The pseudo-random sequence generator shall be initialized with  at the beginning of each radio frame. The quantity  is given by  if no value for  is configured by higher layers for PUSCH/(S)PUCCH format 4/PUCCH format 5 or the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure, otherwise it is given by .

The vector of reference signals shall be precoded according to

where  is the number of antenna ports used for PUSCH transmission.

For PUSCH transmission using a single antenna port, ,  and .

For spatial multiplexing,  or  and the precoding matrix  shall be identical to the precoding matrix used in clause 5.3.3A.2 for precoding of the PUSCH in the same subframe.

Table 5.5.2.1.1-1: Mapping of Cyclic Shift Field in uplink-related DCI format to  and

Table 5.5.2.1.1-2: Mapping of cyclicShift to values

Table 5.5.2.1.1-3: Mapping of Cyclic Shift Field in uplink-related DCI format to , , and

Table 5.5.2.1.1-4:  for subslot-PUSCH/slot-PUSCH

## 5.5.2.1.2Mapping to physical resources

For each antenna port used for transmission of the PUSCH, the sequence  shall be multiplied with the amplitude scaling factor  and mapped in sequence starting with  to the resource blocks.

- when either

-the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or

-the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, and

- otherwise.

If higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, the mapping to resource elements , with  for normal cyclic prefix and  for extended cyclic prefix, in the subframe shall be in increasing order of first  for all values of  satisfying , then the slot number. The quantity  is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI.

In case of slot-PUSCH, the mapping to resource elements , with  for normal cyclic prefix, in the slot of the subframe where slot-PUSCH is transmitted shall be in increasing order of first  for all values of , except if the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7, which indicates the use of Table 5.5.2.1.1-4. In this case the mapping to resource element shall be in increasing order of first  only for values of  satisfying .

In case of subslot-PUSCH, the mapping to resource elements , in the subframe shall be in increasing order of first  for all values of , except if the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7, which indicates the use of Table 5.5.2.1.1-4. In this case the mapping to resource element shall be in increasing order of first  only for values of  satisfying . The value of  depends on the uplink subslot number and the DMRS-pattern field in the most recent uplink-related DCI, according to Table 5.5.2.1.2-1, or according to Table 5.5.2.1.2-2 in case of semi-persistent scheduling of subslot-PUSCH (i.e. higher layer patameter sps-ConfigUL-sTTI-r15 is configured, se TS 36.331 [9]) and with a configured periodicity of 1 subslot (i.e. semiPersistSchedIntervalUL-STTI-r15 set to sTTI1). In case of subslot-PUSCH and semi-persistent scheduling with a configured periodicity longer than 1 subslot, the mapping shall start at symbol  according to the first row of Table 5.5.2.1.2-2 (i.e. equivalent to a signalling of DMRS-pattern field set to '00'). In case no value of  is defined for the uplink subslot number, and in case no valid starting symbol index (see table 5.3.4-1), no reference signal is transmitted associated with the uplink-related DCI format.

Table 5.5.2.1.2-1: The quantity  for subslot-PUSCH

Table 5.5.2.1.2-2: The quantity  for subslot-PUSCH for semi-persistent scheduling

For all other cases, the set of physical resource blocks used in the mapping process and the relation between the index  and the antenna port number  shall be identical to the corresponding PUSCH transmission as defined in clause 5.3.4.

The mapping to resource elements , with , or with  according to Table 5.5.2.1.2-1 for subslot-PUSCH, for normal cyclic prefix and  for extended cyclic prefix, in the subframe shall be in increasing order of first, then the slot number, except for slot-PUSCH and subslot-PUSCH where the reference signal is only mapped to the slot where the slot-PUSCH/subslot-PUSCH is transmitted). No DM-RS shall be transmitted in UpPTS if dmrsLess-UpPts is set to true.

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with  associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

-In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

## 5.5.2.1ADemodulation reference signal for PUSCH with sub-PRB allocations

## 5.5.2.1A.1Reference signal sequence using modulation schemes other than π/2-BPSK

The reference signal sequence  for  is defined by a cyclic shift  of a base sequence according to

,

where  is given by Tables 5.5.2.1A.1-1 and 5.5.2.1A.1-2 for and , respectively. The cyclic shift  is derived from higher layer parameters threeTone-CyclicShift and sixTone-CyclicShift, respectively, as defined in Table 5.5.2.1A.1-3.

If group hopping is enabled, the base sequence index  is given by clause 5.5.2.1A.3.

If group hopping is not enabled, the base sequence index  is given by

- for

- for

Table 5.5.2.1A.1-1: Definition of  for

Table 5.5.2.1A.1-2: Definition of  for

Table 5.5.2.1A.1-3: Definition of

## 5.5.2.1A.2Reference signal sequence using π/2-BPSK modulation scheme

For  using π/2-BPSK modulation scheme,  is used to determine which 2 of 3 subcarriers will be used: NIDcellmod2

-0 indicates that the two subcarriers having the lowest indices among the three allocated are utilized.

-1 indicates that the two subcarriers having the highest indices among the three allocated are utilized.

The reference signal sequences  and  for   using 2 out of 3 subcarriers are defined by ru1(n)ru2(n)

ru1n=121+j1-2cnwn mod 16,       0≤n<NrepPUSCHMslotsULMRU

ru2n=(-1)n121+j1-2cnwn mod 16,       0≤n<NrepPUSCHMslotsULMRU

where the binary sequence  is defined by clause 7.2 and shall be initialised with  at the start of the PUSCH transmission using sub-PRB allocations for BL/CE UEs. The quantity  is given by Table 5.5.2.1A.2-1 where   if group hopping is not enabled, and by clause 5.5.2.1A.3 if group hopping is enabled for PUSCH using sub-PRB allocations for BL/CE UEs.u=NIDcellmod16

Table 5.5.2.1A.2-1: Definition of

The reference signal sequences for PUSCH using sub-PRB allocations for BL/CE UEs is given by clause 5.3.3, where  and  correspond to the complex-valued symbols at the input of the transform precoding. The resulting complex-valued symbols at the output of the transform precoding correspond to the sequence  which is mapped to physical resources as described in clause 5.5.2.1A.4.

## 5.5.2.1A.3Group hopping

For the reference signal for PUSCH transmission using sub-PRB allocations for BL/CE UEs, sequence-group hopping can be enabled where the sequence-group number  in slot  of a radio frame  is defined by a group hopping pattern  and a sequence-shift pattern  according tonffghn'

u=fghn'+fssmodMseqRU

where the number of reference signal sequences available for each resource unit size,  is given by Table 5.5.2.1A.3-1.MseqRU

Table 5.5.2.1A.3-1: Definition of  MseqRU

Sequence-group hopping can be enabled or disabled as described in clause 5.5.1.3.

The group-hopping pattern  is given byfghn'

fghn'=i=07c(8n'+i)∙2imodMseqRU

where  for  using QPSK modulation scheme. When using π/2-BPSK modulation scheme, for frame structure type 1,  is the slot number  of the first slot of the resource unit, and for frame structure type 2,  is the frame number  of the first slot of the resource unit. The pseudo-random sequence  is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with  at the beginning of the resource unit for using π/2-BPSK modulation scheme and in every even slot for  using QPSK modulation scheme.n'=nsn'nsn'nf cinit=NIDcellMseqRU

The sequence-shift pattern  is given by

fssns=NIDcell+∆ssmodMseqRU

where .

## 5.5.2.1A.4Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  and mapped in sequence starting with  to the sub-carriers.

The set of sub-carriers used in the mapping process shall be identical to the corresponding PUSCH transmissions using sub-PRB allocations for BL/CE UEs as defined in clause 5.3.4.

The mapping to resource elements  shall be in increasing order of first, then , and finally the slot number. The value of the symbol index  in a slot is 3.

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with  associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

-In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

## 5.5.2.2Demodulation reference signal for PUCCH

## 5.5.2.2.1Reference signal sequence

The PUCCH demodulation reference signal sequence  for PUCCH formats 1, 1a, 1b, 2, 2a, 2b, and 3 is defined by

where

and  is the number of antenna ports used for PUCCH transmission. For PUCCH formats 2a and 2b,  equals  for , where  is defined in clause 5.4.2. For all other cases,

The sequence is given by clause 5.5.1 with  and  where the expression for the cyclic shift  is determined by the PUCCH format.

For PUCCH formats 1, 1a and 1b,  is given by

where , ,  and  are defined by clause 5.4.1. The number of reference symbols per slot  and the sequence  are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-2, respectively.

For PUCCH formats 2, 2a and 2b,  is defined by clause 5.4.2. The number of reference symbols per slot  and the sequence  are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-3, respectively.

For PUCCH format 3,  is given by

where  is given by Table 5.5.2.2.1-4 and  and  for the first and second slot in a subframe, respectively, are obtained from clause 5.4.2A. The number of reference symbols per slot  and the sequence  are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-3, respectively.

Table 5.5.2.2.1-1: Number of PUCCH demodulation reference symbols per slot

Table 5.5.2.2.1-2: Orthogonal sequences  for PUCCH formats 1, 1a and 1b

Table 5.5.2.2.1-3: Orthogonal sequences  for PUCCH formats 2, 2a, 2b and 3.

Table 5.5.2.2.1-4: Relation between  and  for PUCCH format 3.

The PUCCH demodulation reference signal sequence  for PUCCH formats 4 and 5 is defined by

where

and

Clause 5.5.1 defines the sequence  where .

The cyclic shift  in a slot  is given as  with

where the values of and  are given by Clause 5.5.2.1.1 and

with  obtained as described in clause 5.4.2C.

## 5.5.2.2.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  and mapped in sequence starting with  to resource elements on antenna port . The mapping shall be in increasing order of first, then  and finally the slot number. The set of values for  and the relation between the index  and the antenna port number  shall be identical to the values used for the corresponding PUCCH transmission. The values of the symbol index  in a slot are given by Table 5.5.2.2.2-1.

Table 5.5.2.2.2-1: Demodulation reference signal location for different PUCCH formats.

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], then in case of PUCCH transmission with  associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUCCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

-In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

## 5.5.2.3Demodulation reference signal for SPUCCH

## 5.5.2.3.1Reference signal sequence

The SPUCCH demodulation reference signal sequence  for subslot-SPUCCH format 4, and, slotSPUCCH formats 1, 1a, 1b, 3 and 4 is as defined for  in clause 5.5.2.2.1 for PUCCH format 1, 1a, 1b, 2, 2a, 2b and 3, using the parameter settings in Table 5.5.2.3.1-1, and with the number of reference symbols  replaced by  and given by Table 5.5.2.3.1-2.

NOTE: Subslot-SPUCCH format 1/1a/1b does not employ a reference signal based design.

The sequence is given by clause 5.5.1 with , where the expression for the cyclic shift is determined depending on the SPUCCH format, see table 5.5.2.3.1-3.

Table 5.5.2.3.1-1: Parameters for SPUCCH demodulation reference signal

Table 5.5.2.3.1-2: Number of SPUCCH demodulation reference symbols  per slot or per subslot

Table 5.5.2.3.1-3:

## 5.5.2.3.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  and mapped in sequence starting with  to resource elements  on antenna port . The mapping shall be in increasing order of first, then . The set of values for  and the relation between the index  and the antenna port number  shall be identical to the values used for the corresponding SPUCCH transmission. The values of the symbol index  in a slot and a subslot are given by Table 5.5.2.3.2-1 and Table 5.5.2.3.2-2 respectively.

Table 5.5.2.3.2-1: Demodulation reference signal location for different slot-SPUCCH formats

Table 5.5.2.3.2-2: Demodulation reference signal location for different subslot-SPUCCH formats

## 5.5.3Sounding reference signal

Two types of sounding reference signals can be configured:

-basic sounding reference signal, supporting periodic or aperiodic transmission

-additional sounding reference signal, supporting aperiodic transmission only

Basic SRS corresponds to either SRS trigger type 0 or type 1 in clause 8.2 of [4]. Additional SRS corresponds to SRS trigger type 2 in clause 8.2 of [4].

## 5.5.3.1Sequence generation

## 5.5.3.1.1Sequence generation for basic SRS

The sounding reference signal sequence  is defined by clause 5.5.1, where  is the sequence-group number defined in clause 5.5.1.3,  is the base sequence number defined in clause 5.5.1.4, and . The cyclic shift  of the sounding reference signal is given as

,

where  is configured separately for periodic and each configuration of aperiodic sounding by the higher-layer parameters cyclicShift and cyclicShift-ap, respectively, for each UE and  is the number of antenna ports used for sounding reference signal transmission. The parameter  if  , otherwise . The parameter  is given by the higher layer parameter transmissionCombNum if configured, otherwise .

## 5.5.3.1.2Sequence generation for additional SRS

The sounding reference signal  is defined by clause 5.5.3.1.1 with the following exceptionsrSRS(p)n

- is given by the higher-layer parameter srs-CyclicShiftAddnSRScs

- is given by the higher-layer parameter srs-AntennaPortAddNap

- is given by the higher-layer parameter srs-TransmissionCombNumAddKTC

-the function  in clause 5.5.1.3 is given byfgh

fghns,l=0if group hopping is disabledi=072ic8nsNsymbUL+l+i mod 30if group hopping is enabled

where  is the SC-FDMA symbol index within the slot  and  is the number of SC-FDMA symbols per slotlnsNsymbUL

-the function  in clause 5.5.1.4 is given byv

v=cnsNsymbUL+lif group hopping is disabled and sequence hopping is enabled0otherwise

## 5.5.3.2Mapping to physical resources

## 5.5.3.2.1Mapping to physical resources for basic SRS

The sequence shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power  specified in clause 5.1.3.1 in TS 36.213 [4], and mapped in sequence starting with  to resource elements  on antenna port  according to

where  is the number of antenna ports used for sounding reference signal transmission and the relation between the index  and the antenna port  is given by Table 5.2.1-1. The set of antenna ports used for sounding reference signal transmission is configured independently for periodic and each configuration of aperiodic sounding. The quantity  is the frequency-domain starting position of the sounding reference signal and for  and  is the length of the sounding reference signal sequence defined as

where is given by Table 5.5.3.2-1 through Table 5.5.3.2-4 for each uplink bandwidth . The cell-specific parameter srs-BandwidthConfig,  and the UE-specific parameter srs-Bandwidth, are given by higher layers. For UpPTS,  shall be reconfigured to  if this reconfiguration is enabled by the cell-specific parameter srsMaxUpPts given by higher layers, otherwise if the reconfiguration is disabled ,where  is a SRS BW configuration and  is the set of SRS BW configurations from the Tables 5.5.3.2-1 to 5.5.3.2-4 for each uplink bandwidth ,  is the number of format 4 PRACH in the addressed UpPTS and derived from Table 5.7.1-4.

The frequency-domain starting position  is defined by

where for normal uplink subframes  is defined by

and for UpPTS by

The quantity  is given by

where the relation between the index  and the antenna port  is given by Table 5.2.1-1,  is given by the UE-specific parameter transmissionComb or transmissionComb-ap for periodic and each configuration of aperiodic transmission, respectively, provided by higher layers for the UE, and  is frequency position index. The variable  is equal to 0 for UpPTS in the first half frame and equal to 1 for UpPTS in the second half frame of a radio frame.

The frequency hopping of the sounding reference signal is configured by the parameter , provided by higher-layer parameter srs-HoppingBandwidth. Frequency hopping is not supported for aperiodic transmission, except for additional SRS. If frequency hopping of the sounding reference signal is not enabled (i.e., ), the frequency position index  remains constant (unless re-configured) and is defined by  where the parameter  is given by higher-layer parameters freqDomainPosition and freqDomainPosition-ap for periodic and each configuration of aperiodic transmission, respectively. If frequency hopping of the sounding reference signal is enabled (i.e., ), the frequency position indexes  are defined by

where  is given by Table 5.5.3.2-1 through Table 5.5.3.2-4 for each uplink bandwidth ,

where  regardless of the  value on Table 5.5.3.2-1 through Table 5.5.3.2-4, and

counts the number of UE-specific SRS transmissions, where  is UE-specific periodicity of SRS transmission defined in clause 8.2 of TS 36.213 [4],  is SRS subframe offset defined in Table 8.2-2 of TS 36.213 [4] and  is the maximum value of  for a certain configuration of SRS subframe offset.

The sounding reference signal shall be transmitted in the last symbol of the uplink subframe.

Table 5.5.3.2-1:  and , , values for the uplink bandwidth of

Table 5.5.3.2-2:  and , , values for the uplink bandwidth of

Table 5.5.3.2-3:  and , , values for the uplink bandwidth of

Table 5.5.3.2-4: and, , values for the uplink bandwidth of

## 5.5.3.2.2Mapping to physical resources for additional SRS

An additional SRS spans one or more SC-FDMA symbols in the time domain, where

-the starting SC-FDMA symbol  within the subframe is given by the higher-layer parameter srs-StartPosAdd;l0

-the duration  in number of SC-FDMA symbols, including potential guard symbols, is given by the higher-layer parameter srs-DurationAdd.N

Mapping to physical resources shall be done according to clause 5.5.3.2.1 with the following exceptions:

-frequency hopping between SC-FDMA symbols is supported and if a UE is configured by higher layer parameter srs-GuardSymbolFH-Add, a guard symbol is added between every frequency hop;

-antenna switching within a subframe is supported and if a UE is configured by higher layer parameter srs-GuardSymbolAS-Add, a guard symbol is added between every antenna switching;

- where  is the additional SRS transmission number not counting guard symbol(s) within the subframe with  corresponding to the starting SC-FDMA symbol , and  is the repetition factor given by the higher-layer parameter srs-RepNumAdd;nSRS=l'Rl'l'=0l0R∈1,2,3,4,6,7,8,9,12,13

- is given by the higher-layer parameter srs-BandwidthAdd;BSRS

- is given by the higher-layer parameter srs-HoppingBandwidthAdd;bhop

- is the number of frequency hops with the same antenna/antenna pair for additional SRS, derived from  if antenna switching is not configured for additional SRS, and from  if antenna switching is configured for additional SRS, where  is the repetition factor given by the higher-layer parameter srs-RepNumAdd,  is the number of antenna switches for additional SRS defined in 8.2 of [4],  is the guard-symbol configuration for antenna switching given by the higher-layer parameter srs-GuardSymbolAS,  is the guard symbol configuration for frequency hopping given by the higher-layer parameter srs-GuardSymbolFH, and  is given by the higher-layer parameter srs-DurationAdd;NFHN=RNFH+NFH-1GFHN=RNASNFH+NAS-1GAS+NFH-1NASGFH+NAS-1(1-GAS)GFHRNASGAS∈0, 1GFH∈0, 1N

- is given by the higher-layer parameter srs-FreqDomainPosAdd;nRRC

- is given by the higher-layer parameter srs-AntennaPortAdd;Nap

- is given by the higher-layer parameter srs-CyclicShiftAdd;nSRScs

- is given by the higher-layer parameter srs-TransmissionCombNumAdd;KTC

- is given by the higher-layer parameter srs-TransmissionCombAdd.kTC

## 5.5.3.3Sounding reference signal subframe configuration

The cell-specific subframe configuration period  and the cell-specific subframe offset  for the transmission of sounding reference signals are listed in Tables 5.5.3.3-1 and 5.5.3.3-2, for frame structures type 1 and 2 respectively, where the parameter srs-SubframeConfig is provided by higher layers. Sounding reference signal subframes are the subframes satisfying. For frame structure type 2, a sounding reference signal is transmitted only in uplink subframes or UpPTS.

Table 5.5.3.3-1: Frame structure type 1 sounding reference signal subframe configuration

Table 5.5.3.3-2: Frame structure type 2 sounding reference signal subframe configuration

## 5.6SC-FDMA baseband signal generation

This clause applies to all uplink physical signals and uplink physical channels except the physical random access channel and PUSCH using sub-PRB allocations for BL/CE UEs.

The time-continuous signal  for antenna port  in SC-FDMA symbol  in an uplink slot is defined by

for where , ,  and  is the content of resource element  on antenna port .

For frame structure type 3, if the associated DCI indicates PUSCH starting position other than '00' or if 'autonomous PUSCH' is configured,  is given by

where

and were  is given by TS36.213 [4] if 'autonomous PUSCH' is configured.

The quantity  is given by clause 8.1. The UE behaviour if  is undefined.

The SC-FDMA symbols in a slot shall be transmitted in increasing order of , starting with , where SC-FDMA symbol starts at time  within the slot.

Table 5.6-1 lists the values of that shall be used.

Table 5.6-1: SC-FDMA parameters

## 5.6ASC-FDMA baseband signal generation for PUSCH using sub-PRB allocations

## 5.6A.1Modulation schemes other than π/2-BPSK

For , the time-continuous signal  for antenna port  in SC-FDMA symbol  in an uplink slot is defined by clause 5.6 with  replaced by .

## 5.6A.2Modulation scheme π/2-BPSK

For  and π/2-BPSK modulation only 2-of-3 adjacent subcarriers are selected as described in 5.5.2.1A.2. The time-continuous signal  in SC-FDMA symbol  in an uplink slot is defined by MscRU=3

for  where , ,  is given by Table 5.6-1, and  and  are respectively the modulation value for subcarrier index  and  for symbol , and the values of  used on  and  are respectively obtained by subtracting  from the resulting set of allocated subcarriers as described in Table 8.1.6-1 of [4], and  represents the lower subcarrier index among the selected subcarriers and  is the subcarrier index adjacent to it. The phase rotation  is given byak,lk+1

ϕ=π2l mod 2+φavgkl

φavgkl=φavgkl-1+2πΔfk+1N+NCP,lTs  when  l>0

φavgk0=0

l=0,1,…,NTBNrepPUSCHMRUMslotsULMsymbUL-1

l= l mod MsymbUL

where  is the number of transport blocks defined in clause 8.0 of TS 36.213 [4]. If  >1 and interleaving between codewords is applied according to clause 8.0 of TS 36.213 [4], then the symbol counter  is reset at the start of the first PUSCH codeword transmission and incremented for each symbol during the transmission of the  PUSCH codewords. For other cases, the symbol counter  is reset at the start of each PUSCH codeword transmission and incremented for each symbol during the transmission of the PUSCH codeword.NTBNTBNTB

The SC-FDMA symbols in a slot shall be transmitted in increasing order of , starting with , where SC-FDMA symbol  starts at time  within the slot.

## 5.7Physical random access channel

## 5.7.1Time and frequency structure

The physical layer random access preamble, illustrated in Figure 5.7.1-1, consists of a cyclic prefix of length and a sequence part of length. The parameter values are listed in Table 5.7.1-1 and depend on the frame structure and the random access configuration. Higher layers control the preamble format.

Figure 5.7.1-1: Random access preamble format

Table 5.7.1-1: Random access preamble parameters

The transmission of a random access preamble, if triggered by the MAC layer, is restricted to certain time and frequency resources. These resources are enumerated in increasing order of the subframe number within the radio frame and the physical resource blocks in the frequency domain such that index 0 correspond to the lowest numbered physical resource block and subframe within the radio frame. PRACH resources within the radio frame are indicated by a PRACH configuration index, where the indexing is in the order of appearance in Table 5.7.1-2 and Table 5.7.1-4.

For non-BL/CE UEs there are up to two PRACH configurations in a cell. The first PRACH configuration is configured by higher layers with a PRACH configuration index (prach-ConfigurationIndex) and a PRACH frequency offset  (prach-FrequencyOffset). The second PRACH configuration (if any) is configured by higher layers with a PRACH configuration index (prach-ConfigurationIndexHighSpeed) and a PRACH frequency offset  (prach-FrequencyOffsetHighSpeed).

For BL/CE UEs, for each PRACH coverage enhancement level, there is a PRACH configuration configured by higher layers with a PRACH configuration index (prach-ConfigurationIndex), a PRACH frequency offset  (prach-FrequencyOffset), a number of PRACH repetitions per attempt  (numRepetitionPerPreambleAttempt) and optionally a PRACH starting subframe periodicity  (prach-StartingSubframe). PRACH of preamble format 0-3 is transmitted  times, whereas PRACH of preamble format 4 is transmitted one time only.

For BL/CE UEs and for each PRACH coverage enhancement level, if frequency hopping is enabled for a PRACH configuration by the higher-layer parameter prach-HoppingConfig, the value of the parameter  depends on the SFN and the PRACH configuration index and is given by

-In case the PRACH configuration index is such that a PRACH resource occurs in every radio frame when calculated as below from Table 5.7.1-2 or Table 5.7.1-4,

-otherwise

where  is the system frame number corresponding to the first subframe for each PRACH repetition,  corresponds to a cell-specific higher-layer parameter prach-HoppingOffset. If frequency hopping is not enabled for the PRACH configuration then .

For frame structure type 1 with preamble format 0-3, for each of the PRACH configurations there is at most one random access resource per subframe. Table 5.7.1-2 lists the preamble formats according to Table 5.7.1-1 and the subframes in which random access preamble transmission is allowed for a given configuration in frame structure type 1. The start of the random access preamble shall be aligned with the start of the corresponding uplink subframe at the UE assuming , where  is defined in clause 8.1. For PRACH configurations 0, 1, 2, 15, 16, 17, 18, 31, 32, 33, 34, 47, 48, 49, 50 and 63 the UE may for handover purposes assume an absolute value of the relative time difference between radio frame  in the current cell and the target cell of less than . The first physical resource block  allocated to the PRACH opportunity considered for preamble formats 0, 1, 2 and 3 is defined as .

Table 5.7.1-2: Frame structure type 1 random access configuration for preamble formats 0-3

For frame structure type 2 with preamble formats 0-4, for each of the PRACH configurations there might be multiple random access resources in an UL subframe (or UpPTS for preamble format 4) depending on the UL/DL configuration [see table 4.2-2]. Table 5.7.1-3 lists PRACH configurations allowed for frame structure type 2 where the configuration index corresponds to a certain combination of preamble format, PRACH density value,  and version index, . For frame structure type 2 with PRACH configuration indices 0, 1, 2, 20, 21, 22, 30, 31, 32, 40, 41, 42, 48, 49, 50, or with PRACH configuration indices 51, 53, 54, 55, 56, 57 in UL/DL configuration 3, 4, 5, the UE may for handover purposes assume an absolute value of the relative time difference between radio frame in the current cell and the target cell is less than .

Table 5.7.1-3: Frame structure type 2 random access configurations for preamble formats 0-4

Table 5.7.1-4 lists the mapping to physical resources for the different random access opportunities needed for a certain PRACH density value, . Each quadruple of the format  indicates the location of a specific random access resource, where  is a frequency resource index within the considered time instance,  indicates whether the resource is reoccurring in all radio frames, in even radio frames, or in odd radio frames, respectively,  indicates whether the random access resource is located in first half frame or in second half frame, respectively, and where  is the uplink subframe number where the preamble starts, counting from 0 at the first uplink subframe between 2 consecutive downlink-to-uplink switch points, with the exception of preamble format 4 where  is denoted as (*). The start of the random access preamble formats 0-3 shall be aligned with the start of the corresponding uplink subframe at the UE assuming  and the random access preamble format 4 shall start  before the end of the UpPTS at the UE, where the UpPTS is referenced to the UE's uplink frame timing assuming.

The random access opportunities for each PRACH configuration shall be allocated in time first and then in frequency if and only if time multiplexing is not sufficient to hold all opportunities of a PRACH configuration needed for a certain density value  without overlap in time. For preamble format 0-3, the frequency multiplexing shall be done according to

where  is the number of uplink resource blocks, is the first physical resource block allocated to the PRACH opportunity considered and where  is the first physical resource block available for PRACH.

For preamble format 4, the frequency multiplexing shall be done according to

whereis the system frame number and whereis the number of DL to UL switch points within the radio frame.

For BL/CE UEs, only a subset of the subframes allowed for preamble transmission are allowed as starting subframes for the  repetitions. The allowed starting subframes for a PRACH configuration are determined as follows:

-Enumerate the subframes that are allowed for preamble transmission for the PRACH configuration as  where  and  correspond to the two subframes allowed for preamble transmission with the smallest and the largest absolute subframe number  , respectively.

-If a PRACH starting subframe periodicity  is not provided by higher layers, the periodicity of the allowed starting subframes in terms of subframes allowed for preamble transmission is . The allowed starting subframes defined over  are given by  where

-If a PRACH starting subframe periodicity  is provided by higher layers, it indicates the periodicity of the allowed starting subframes in terms of subframes allowed for preamble transmission. The allowed starting subframes defined over  are given by  where

-No starting subframe defined over  such that  is allowed.

Each random access preamble occupies a bandwidth corresponding to 6 consecutive resource blocks for both frame structures.

Table 5.7.1-4: Frame structure type 2 random access preamble mapping in time and frequency

## 5.7.2Preamble sequence generation

The random access preambles are generated from Zadoff-Chu sequences with zero correlation zone, generated from one or several root Zadoff-Chu sequences. The network configures the set of preamble sequences the UE is allowed to use.

There are up to two sets of 64 preambles available in a cell where Set 1 corresponds to higher layer PRACH configuration using prach-ConfigurationIndex and prach-FrequencyOffset and Set 2, if configured, corresponds to higher layer PRACH configuration using prach-ConfigurationIndexHighSpeed and prach-FrequencyOffsetHighSpeed. The set of 64 preamble sequences in a cell is found by including first, in the order of increasing cyclic shift, all the available cyclic shifts of a root Zadoff-Chu sequence with the logical index rootSequenceIndexHighSpeed (for Set 2, if configured) or with the logical index RACH_ROOT_SEQUENCE (for Set 1), where both rootSequenceIndexHighSpeed (if configured) and RACH_ROOT_SEQUENCE are broadcasted as part of the System Information. Additional preamble sequences, in case 64 preambles cannot be generated from a single root Zadoff-Chu sequence, are obtained from the root sequences with the consecutive logical indexes until all the 64 sequences are found. The logical root sequence order is cyclic: the logical index 0 is consecutive to 837. The relation between a logical root sequence index and physical root sequence index  is given by Tables 5.7.2-4 and 5.7.2-5 for preamble formats 0 – 3 and 4, respectively.

The  root Zadoff-Chu sequence is defined by

where the length  of the Zadoff-Chu sequence is given by Table 5.7.2-1. From the  root Zadoff-Chu sequence, random access preambles with zero correlation zones of length are defined by cyclic shifts according to

where the cyclic shift is given by

and  is given by Tables 5.7.2-2 and 5.7.2-3 for preamble formats 0-3 and 4, respectively, where the higher-layer parameters zeroCorrelationZoneConfig and zeroCorrelationZoneConfigHighSpeed shall be used for PRACH preamble Set 1 and Set 2 (if configured), respectively. Restricted set type B shall be used for PRACH preamble Set 2 (if configured), and the parameter High-speed-flag provided by higher layers determines if unrestricted set or restricted set type A shall be used for PRACH preamble Set 1.

The variable  is the cyclic shift corresponding to a Doppler shift of magnitude  and is given by

where  is the smallest non-negative integer that fulfils . The parameters for restricted sets of cyclic shifts depend on .

For restricted set type A and , the parameters are given by

For restricted set type A and , the parameters are given by

For restricted set type B and , the parameters are given by

For restricted set type B and , the parameters are given by

For restricted set type B and , the parameters are given by

For restricted set type B and , the parameters are given by

For restricted set type B and , the parameters are given by

For restricted set type B and , the parameters are given by

For all other values of , there are no cyclic shifts in the restricted set.

Table 5.7.2-1: Random access preamble sequence length

Table 5.7.2-2:  for preamble generation (preamble formats 0-3)

Table 5.7.2-3:  for preamble generation (preamble format 4)

Table 5.7.2-4: Root Zadoff-Chu sequence order for preamble formats 0 – 3

Table 5.7.2-5: Root Zadoff-Chu sequence order for preamble format 4

## 5.7.3Baseband signal generation

The time-continuous random access signal  is defined by

where,  is an amplitude scaling factor in order to conform to the transmit power  specified in clause 6.1 in TS 36.213 [4], and . The location in the frequency domain is controlled by the parameter  is derived from clause 5.7.1. The factor  accounts for the difference in subcarrier spacing between the random access preamble and uplink data transmission. The variable, the subcarrier spacing for the random access preamble, and the variable, a fixed offset determining the frequency-domain location of the random access preamble within the physical resource blocks, are both given by Table 5.7.3-1.

Table 5.7.3-1: Random access baseband parameters

## 5.8Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued SC-FDMA baseband signal for each antenna port or the complex-valued PRACH baseband signal is shown in Figure 5.8-1. The filtering required prior to transmission is defined by the requirements in TS 36.101 [7].

Figure 5.8-1: Uplink modulation
