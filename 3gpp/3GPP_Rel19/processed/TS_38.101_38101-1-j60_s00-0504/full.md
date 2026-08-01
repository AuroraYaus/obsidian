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

shall  indicates a mandatory requirement to do something

shall not indicates an interdiction (prohibition) to do something

The constructions "shall" and "shall not" are confined to the context of normative provisions, and do not appear in Technical Reports.

The constructions "must" and "must not" are not used as substitutes for "shall" and "shall not". Their use is avoided insofar as possible, and they are not used in a normative context except in a direct citation from an external, referenced, non-3GPP document, or so as to maintain continuity of style when extending or modifying the provisions of such a referenced document.

should  indicates a recommendation to do something

should not indicates a recommendation not to do something

may  indicates permission to do something

need not indicates permission not to do something

The construction "may not" is ambiguous and is not used in normative elements. The unambiguous constructions "might not" or "shall not" are used instead, depending upon the meaning intended.

can  indicates that something is possible

cannot  indicates that something is impossible

The constructions "can" and "cannot" are not substitutes for "may" and "need not".

will  indicates that something is certain or expected to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

will not  indicates that something is certain or expected not to happen as a result of action taken by an agency the behaviour of which is outside the scope of the present document

might indicates a likelihood that something will happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

might not indicates a likelihood that something will not happen as a result of action taken by some agency the behaviour of which is outside the scope of the present document

In addition:

is (or any other verb in the indicative mood) indicates a statement of fact

is not (or any other negative verb in the indicative mood) indicates a statement of fact

The constructions "is" and "is not" do not indicate requirements.

# 1 Scope

The present document establishes the minimum RF requirements for NR User Equipment (UE) operating on frequency Range 1.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

For a specific reference, subsequent revisions do not apply.

For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.




[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TS 38.101-2: "NR; User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone".

[3] 3GPP TS 38.101-3: "NR; User Equipment (UE) radio transmission and reception; Part 3: Range 1 and Range 2 Interworking operation with other radios".

[4] 3GPP TS 38.521-1: "NR; User Equipment (UE) conformance specification; Radio transmission and reception; Part 1: Range 1 Standalone".

[5] Recommendation ITU-R M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000".

[6] 3GPP TS 38.211: "NR; Physical channels and modulation".

[7] 3GPP TS 38.331: "Radio Resource Control (RRC) protocol specification".

[8] 3GPP TS 38.213: "NR; Physical layer procedures for control".

[9] ITU-R Recommendation SM.329, "Unwanted emissions in the spurious domain".

[10] 3GPP TS 38.214: "NR; Physical layer procedures for data".

[11] 3GPP TS 36.101: Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception;

[12] ETSI TS 102 792: "Intelligent Transport Systems (ITS); Mitigation techniques to avoid interference between European CEN Dedicated Short Range Communication (CEN DSRC) equipment and Intelligent Transport Systems (ITS) operating in the 5 GHz frequency range".

[13] 3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[14] 3GPP TS 37.213: "Physical layer procedures for shared spectrum channel access".

[15] 3GPP TS 38.306: "NR; User Equipment (UE) radio access capabilities".

[16] 3GPP TS 38.104: "NR; Base Station (BS) radio transmission and reception".

[17] 3GPP TS 23.256: "Support of Uncrewed Aerial Systems (UAS) connectivity, identification and tracking; Stage 2".

[18] ECC Decision(22)07, "Harmonised technical conditions for the usage of aerial UE for communications based on LTE and 5G NR in the bands 703-733 MHz, 832-862 MHz, 880-915 MHz, 1710-1785 MHz, 1920-1980 MHz, 2500-2570 MHz and 2570-2620 MHz harmonised for MFCN", 7 March 2025.

[19] ECC Decision(20)02: "Harmonised use of the paired frequency bands 874.4-880.0 MHz and 919.4-925.0 MHz and of the unpaired frequency band 1900-1910 MHz for Railway Mobile Radio (RMR)"

# 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

Aerial UE: A UE supporting UAS (Uncrewed Aircraft Systems) as indicated by the capability aerialUE-Capability-r18 [15] and that has an aerial subscription as described in TS 23.256 [17]. The UE is considered to have access to UAS services after the UE have performed a successful authentication and authorization with the USS as described in TS 23.256 [17].

Aggregated Allocation Bandwidth: Total bandwidth of all allocated RBs in a transmission occasion. Can be calculated for two aggregated CCs as LCRB, 1* 12* SCS1 + LCRB,2 * 12 * SCS2 .

Aggregated Channel Bandwidth: The RF bandwidth in which a UE transmits and receives multiple contiguously aggregated carriers.

ATG UE: The terminals or user equipments which are mounted in aircraft and support ATG feature (i.e. UE capability airToGroundNetwork-r18) as defined in clause 4.2.2 from TS38.306[15].

Carrier aggregation: Aggregation of two or more component carriers in order to support wider transmission bandwidths.

Carrier aggregation band: A set of one or more operating bands across which multiple carriers are aggregated with a specific set of technical requirements.

Carrier aggregation bandwidth class: A class defined by the aggregated transmission bandwidth configuration and maximum number of component carriers supported by a UE.

Carrier aggregation configuration: A combination of CA operating band(s) and CA bandwidth class(es) supported by a UE.

Concurrent operation: The simultaneous transmission and reception of sidelink and Uu interfaces while operation is agnostic of the service used on each interface.

Contiguous carriers: A set of two or more carriers configured in a spectrum block where there are no RF requirements based on co-existence for un-coordinated operation within the spectrum block.

Contiguous resource allocation: A resource allocation of consecutive resource blocks within one carrier or across contiguously aggregated carriers. The gap between contiguously aggregated carriers due to the nominal channel spacing is allowed.

Contiguous spectrum: Spectrum consisting of a contiguous block of spectrum with no sub-block gap(s).

Enhanced channel raster: channel raster with a 10 kHz granularity in bands with a 100 kHz channel raster.

eRedCap UE: The UE with enhanced reduced capabilities as defined in clause 4.2.22.1 from TS38.306 [15].

Inter-band carrier aggregation: Carrier aggregation of component carriers in different operating bands.

NOTE: Carriers aggregated in each band can be contiguous or non-contiguous.

Inter-band concurrent operation: Operation of NR Uu carrier and NR Sidelink carrier in different operating bands.

Intra-band contiguous carrier aggregation: Contiguous carriers aggregated in the same operating band.

Intra-band non-contiguous carrier aggregation: Non-contiguous carriers aggregated in the same operating band.

Intra-band SL CA UE: UE that supports NR SL CA operation in a single band.

LP-WUS power boosting: difference between the average power of LP-WUS REs (which occupy certain REs within a NR transmission bandwidth configuration) and the average power over all REs (from both LP-WUS and the NR carrier containing the LP-WUS REs).

NR SL CA: Aggregation of two or more NR Sidelink component carriers in order to support wider transmission bandwidths

NR SL inter-band concurrent operating Band: Band combinations of NR Uu carrier and NR Sidelink carrier in different operating bands.

NR SL-U UE: UE that supports NR Sidelink operation in unlicensed bands (e.g. n46, n96, n102).

Railway Mobile Radio: railway operations encompassing GSM-R and its successor(s), including the Future Railway Mobile Communication System (FRMCS); in the context of this specification the Railway Mobile Radio is limited to NR operation in band n100, or n101.

RedCap UE: The UE with reduced capabilities as defined in clause 4.2.21.1 from TS38.306 [15].

Sub-band: For a UE that supports shared spectrum channel access in wideband operation, a sub-band is the set of RBs within an approximately 20 MHz segment of the channel where the wideband channel is uniformly divided into an integer number of 20 MHz sub-bands.  Sub-bands may be separately allocated in uplink and downlink.

Sub-block: This is one contiguous allocated block of spectrum for transmission and reception by the same UE. There may be multiple instances of sub-blocks within an RF bandwidth.

Sub-block bandwidth: The bandwidth of one sub-block.

Sub-block gap: A frequency gap between two consecutive sub-blocks within an RF bandwidth, where the RF requirements in the gap are based on co-existence for un-coordinated operation.

Two Rx antenna port XR UE: A non-(e)RedCap XR UE that is equipped with only two Rx antenna ports in frequency band(s) where 4 Rx antenna ports are required. The UE is intended to be worn on human head. When in use, is intended to be supported only by/behind the ears and by a nose-bridge resulting in a constrained form factor with limited volume available for Rx chains.

UE transmission bandwidth configuration: Set of resource blocks located within the UE channel bandwidth which may be used for transmitting or receiving by the UE.

Vehicular UE: A UE embedded in a vehicle, permanently connected to an embedded antenna system that radiates externally for NR operating bands.

NOTE: Vehicular UE does not refer to other UE form factors placed inside the vehicle.

Wideband operation: For a UE that supports shared spectrum channel access, wideband operation refers to operation within a channel larger than 20 MHz in which intra-cell guard bands may be configured to distinguish individual RB-sets

## 3.2 Symbols

For the purposes of the present document, the following symbols apply:

ΔFGlobal Granularity of the global frequency raster

ΔFRaster Band dependent channel raster granularity

ΔfOOB Δ Frequency of Out Of Band emission

ΔFTX-RX Maximum deviation to the Tx-Rx carrier center frequency separation for asymmetric uplink/downlink channel bandwidth operation

∆MPRc Allowed Maximum Power Reduction relaxation for serving cell c

ΔPPowerClass Adjustment to maximum output power for a given power class

RB The starting frequency offset between the allocated RB and the measured non-allocated RB

ΔRIB,c Allowed reference sensitivity relaxation due to support for inter-band CA operation, for serving cell c

ΔRIBC Allowed relaxation to the power class 3 reference sensitivity level due to support for intra-band contiguous CA operation

ΔRIBNC Allowed relaxation to the power class 3 reference sensitivity level due to support for intra-band non-contiguous CA operation

ΔRIB,4R Reference sensitivity adjustment due to support for 4 antenna ports

ΔRIB,8R Reference sensitivity adjustment due to support for 8 antenna ports

ΔR1R Reference sensitivity adjustment due to support for 1 antenna ports

ΔRLP-WUS Reference sensitivity adjustment for specific bands with FDL_low higher than 2400 MHz

ΔRXR,2R Reference sensitivity adjustment for two antenna ports XR UEs on bands defined in Table 7.3.2-2b

ΔShift Channel raster offset

TC Allowed operating band edge transmission power relaxation

TC,c Allowed operating band edge transmission power relaxation for serving cell c

ΔTIB,c Allowed maximum configured output power relaxation due to support for inter-band CA operation, inter-band NR-DC operation and due to support for SUL operations, for serving cell c

BWChannel Channel bandwidth

BWChannel,block Sub-block bandwidth, expressed in MHz. BWChannel,block= Fedge,block,high- Fedge,block,low

BWChannel_CA The intra-band contiguous CA aggregated channel bandwidth, expressed in MHz. BWChannel_CA = Fedge,high - Fedge,low.

BWSum_CA The intra-band contiguous CA aggregated bandwidth defined as the sum of each CC’s channel bandwidth, expressed in MHz.

BWChannel,max Maximum channel bandwidth supported among all bands in a release

BWGB max(GBChannel,low, GBChannel,high)

BWDL Channel bandwidth for DL

BWUL Channel bandwidth for UL

BWinterferer Bandwidth of the interferer

Ceil(x) Rounding upwards; ceil(x) is the smallest integer such that ceil(x) ≥ x

Floor(x) Rounding downwards; floor(x) is the greatest integer such that floor(x) ≤ x

FC Center frequency of a carrier for a numerology defined by the RF reference frequency on the channel raster mapped to the carrier according to sub-clause 5.4.2.2

FC,block, high Fc of the highest transmitted/received carrier in a sub-block

FC,block, low Fc of the lowest transmitted/received carrier in a sub-block

FC,low The Fc of the lowest carrier, expressed in MHz

FC,high The Fc of the highest carrier, expressed in MHz

FDL_low The lowest frequency of the downlink operating band

FDL_high The highest frequency of the downlink operating band

FUL_low The lowest frequency of the uplink operating band

FUL_high The highest frequency of the uplink operating band

Fedge,block,low The lower sub-block edge, where Fedge,block,low = FC,block,low - Foffset, low.

Fedge,block,high The upper sub-block edge, where Fedge,block,high = FC,block,high + Foffset, high.

Fedge, low The lower edge of aggregated channel bandwidth, expressed in MHz. Fedge,low = FC,low - Foffset,low.

Fedge, high The higher edge of aggregated channel bandwidth, expressed in MHz. Fedge,high = FC,high + Foffset,high.

FInterferer (offset) Frequency offset of the interferer (between the center frequency of the interferer and the carrier frequency of the carrier measured). For intra-band contiguous CA, the FInterferer (offset) is the frequency separation of the center frequency of the carrier closest to the interferer and the center frequency of the interferer

FInterferer Frequency of the interferer

FIoffset Frequency offset of the interferer (between the center frequency of the interferer and the closest edge of the carrier measured)

Foffset Frequency offset from FC,high to the higher edge or FC,low to the lower edge.

Foffset,high Frequency offset from FC,high to the upper UE RF Bandwidth edge, or from FC,block, high to the upper sub-block edge

Foffset,low Frequency offset from FC,low to the lower UE RF Bandwidth edge, or from FC,block, low to the lower sub-block edge

FOOB The boundary between the NR out of band emission and spurious emission domains

FREF RF reference frequency

FREF-Offs Offset used for calculating FREF

FREF, shift RF reference frequency for Supplementary Uplink (SUL) bands, the uplink of all FDD bands, and TDD bands

Fuw (offset) The frequency separation of the center frequency of the carrier closest to the interferer and the center frequency of the interferer

Gn100post connector Declared value of the post chipset unit antenna connector gain for band n100, used for conversion of the radiated requirement into a conducted requirement (see principles described in annex M)

Gn101post connector  Declared value of the post chipset unit antenna connector gain for band n101, used for conversion of the radiated requirement into a conducted requirement (see principles described in annex M)

GBChannel Minimum guard band defined in clause 5.3.3, expressed in kHz

GBChannel(i) Minimum guard band defined in clause 5.3.3 of carrier i

GBChannel,low Minimum guard band defined in clause 5.3.3 for the lowest assigned component carrier in clause 5.3A.3

GBChannel,high Minimum guard band defined in clause 5.3.3 for the highest assigned component carrier in clause 5.3A.3

LCRB Transmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resources blocks

LCRB_agg Intra-band contiguous CA aggregated transmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resources blocks, $ L_{CRB_{\_agg}}=\sum  _{i=1}^{j}L_{CRB_{i}}*2^{\mu  _{i}}$ for contiguous CA component carrier 1 to j, where μ is defined in TS 38.211 [6]

Max() The largest of given numbers

Min() The smallest of given numbers

![](media_svg/image1.svg) [公式≈: ^{n}PRB] Physical resource block number

NRACLR NR ACLR

NRB Transmission bandwidth configuration, expressed in units of resource blocks

NRB_agg The number of the aggregated RBs within the fully allocated aggregated channel bandwidth

$ N_{RB_{\_agg}}=\sum  _{i=1}^{j}N_{RB_{i}}*2^{\mu  _{i}}$ for carrier 1 to j, where μ is defined in TS 38.211 [6]

NRB,c The transmission bandwidth configuration of component carrier c, expressed in units of resource blocks

$ N_{RB,cj}=N_{RB_{j}}*2^{\mu  _{j}}$ for carrier j, where μ is defined in TS 38.211 [6]

NRB,LP-WUS Transmission bandwidth configuration for LP-WUS, expressed in units of resource blocks

NRB,largest BW The largest transmission bandwidth configuration of the component carriers in the bandwidth combination, expressed in units of resource blocks

NRB,low The transmission bandwidth configurations according to Table 5.3.2-1 for the lowest assigned component carrier in clause 5.3A.3

NRB,high The transmission bandwidth configurations according to Table 5.3.2-1 for the highest assigned component carrier in clause 5.3A.3

NREF NR Absolute Radio Frequency Channel Number (NR-ARFCN)

NREF-Offs Offset used for calculating NREF

PCMAX The configured maximum UE output power

PCMAX, c The configured maximum UE output power for serving cell c

PCMAX, f, c The configured maximum UE output power for carrier f of serving cell c in each slot

PEIRP UE Effective Isotropic Radiated Power (EIRP)

PEMAX Maximum allowed UE output power signalled by higher layers

PEMAX, c Maximum allowed UE output power signalled by higher layers for serving cell c

PInterferer Modulated mean power of the interferer

Plargest BW Power of the largest transmission bandwidth configuration of the component carriers in the bandwidth combination

PPowerClass The nominal UE power (i.e., no tolerance)

Pmax,c,AC Maximum output power defined as the sum of measurement of all antenna connectors

Pmax,c,TABC Maximum carrier output power defined as the sum of measurement of all TAB connectors

Prated,c,AC Rated maximum output power defined as the sum of power over all antenna connectors

Prated,c,TABC Rated maximum output power defined as the sum of power over all TAB connectors

P-MPRc Power Management Maximum Power Reduction for serving cell c

PRB The transmitted power per allocated RB, measured in dBm

PREFSENS_SL  The REFSENS power for Sidelink

PUMAX The measured configured maximum UE output power

Puw Power of an unwanted DL signal

Pw Power of a wanted DL signal

Rext_low The lower-sided extension ratio for NRB and for the boundary of OOBE & Spurious emissions shifted

Rext_high The higher-sided extension ratio for NRB and for the boundary of OOBE & Spurious emissions shifted

RBstart The lowest RB index of transmitted resource blocks

RBstart_CA The lowest RB index of transmitted resource blocks for intra-band contiguous CA

SCSc SCS for the component carrier c, expressed in kHz

SCSlargest BW SCS for the largest transmission bandwidth configuration of the component carriers in the bandwidth combination, expressed in kHz

SCSlow SCS for the lowest assigned component carrier in clause 5.3A.3, expressed in kHz

SCShigh SCS for the highest assigned component carrier in clause 5.3A.3, expressed in kHz

tp Transient Period value signalled by the UE

tpstart Start position of transient period relative to the symbol boundary

T(PCMAX, f, c) Tolerance for applicable values of PCMAX, f, c for configured maximum UE output power for carrier f of serving cell c

TL,c Absolute value of the lower tolerance for the applicable operating band as specified in clause 6.2.1

SSREF SS block reference frequency position

UTRAACLR UTRA ACLR

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

ACLR Adjacent Channel Leakage Ratio

ACS Adjacent Channel Selectivity

A-MPR Additional Maximum Power Reduction

ASCS Adjacent Subcarrier selectivity

ATG Air-To-Ground

BS Base Station

BW Bandwidth

BWP Bandwidth Part

CA Carrier Aggregation

CA_nX-nY Inter-band CA of component carrier(s) in one sub-block within Band nX and component carrier(s) in one sub-block within Band nY where nX and nY are the applicable NR operating bands

CC Component Carriers

CG Carrier Group

CP-OFDM Cyclic Prefix-OFDM

CW Continuous Wave

DC Dual Connectivity

DFT-s-OFDM Discrete Fourier Transform-spread-OFDM

DM-RS Demodulation Reference Signal

DTX Discontinuous Transmission

E-UTRA Evolved UTRA

EIRP Equivalent Isotropically Radiated Power

(e)RedCap Redcap or eRedCap

eRedCap enhanced Reduced Capability

EVM Error Vector Magnitude

FAR False Alarm Rate

FR Frequency Range

FRC Fixed Reference Channel

FRMCS Future Railway Mobile Communication System

FWA Fixed Wireless Access

GSCN Global Synchronization Channel Number

HD Half Duplex

IBB In-band Blocking

IDFT Inverse Discrete Fourier Transformation

ITS Intelligent Transportation System

ITUR Radiocommunication Sector of the International Telecommunication Union

LP-WUR Low Power-Wake Up Receiver

LP-WUS Low Power-Wake Up Signal

LP-SS Low Power-Synchronization Signal

LR LP-WUR

MBW Measurement bandwidth

MCG Master Cell Group

MDR Miss-Detection Rate

MOP Maximum Output Power

MPR Allowed maximum power reduction

MR Main Radio

MSD Maximum Sensitivity Degradation

NR New Radio

NR-ARFCN NR Absolute Radio Frequency Channel Number

NS Network Signalling

OCNG OFDMA Channel Noise Generator

OOB Out-of-band

OOK On-Off keying

P-MPR Power Management Maximum Power Reduction

PRB Physical Resource Block

PS Public Safety

PSBCH Physical Sidelink Broadcast CHannel

PSCCH Physical Sidelink Control CHannel

PSFCH Physical Sidelink Feedback CHannel

PSSCH Physical Sidelink Shared CHannel

QAM Quadrature Amplitude Modulation

RE Resource Element

REFSENS Reference Sensitivity

RedCap Reduced Capability

RF Radio Frequency

RMR Railway Mobile Radio

RMS Root Mean Square (value)

RSRP Reference Signal Receiving PowerRx Receiver

Rx Receiver

SC Single Carrier

SCG Secondary Cell Group

SCS Subcarrier spacing

SDL Supplementary Downlink

SEM Spectrum Emission Mask

SL Sidelink

SL-MIMO Sidelink-Multiple Antenna transmission

SL-U Sidelink at unlicensed band

SNR Signal-to-Noise Ratio

SRS Sounding Reference Symbol

SS Synchronization Symbol

S-SSB Sidelink Synchronization Signal Block

SUL Supplementary uplink

TAB Transceiver Array Boundary

TAE Time Alignment Error

TAG Timing Advance Group

Tx Transmitter

TxD Tx Diversity

UAS Uncrewed Aircraft Systems

UAV Uncrewed Aerial Vehicle

UL MIMO Uplink Multiple Antenna transmission

ULFPTx Uplink Full Power Transmission

USS UAS Service Supplier

V2X Vehicle to Everything

XR eXtended Reality

# 4 General

## 4.1 Relationship between minimum requirements and test requirements

The present document is a Single-RAT specification for NR UE, covering RF characteristics and minimum performance requirements. Conformance to the present specification is demonstrated by fulfilling the test requirements specified in the conformance specification 3GPP TS 38.521-1 [4].

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification TS 38.521-1 [4] defines test tolerances. These test tolerances are individually calculated for each test. The test tolerances are used to relax the minimum requirements in this specification to create test requirements. For some requirements, including regulatory requirements, the test tolerance is set to zero.

The measurement results returned by the test system are compared - without any modification - against the test requirements as defined by the shared risk principle.

The shared risk principle is defined in Recommendation ITUR M.1545 [5].

## 4.2 Applicability of minimum requirements

a) In this specification the Minimum Requirements are specified as general requirements and additional requirements. Where the Requirement is specified as a general requirement, the requirement is mandated to be met in all scenarios

b) For specific scenarios for which an additional requirement is specified, in addition to meeting the general requirement, the UE is mandated to meet the additional requirements.

c) The spurious emissions power requirements are for the long-term average of the power. For the purpose of reducing measurement uncertainty it is acceptable to average the measured power over a period of time sufficient to reduce the uncertainty due to the statistical nature of the signal

d) All the requirements for intra-band contiguous and non-contiguous CA apply under the assumption of the same slot format indicated by TDD-UL-DL-ConfigurationCommon and TDD-UL-DL-ConfigurationDedicated in the PCell and SCells for NR SA.

e) The requirements for Tx diversity are applied for UE which indicates Tx diversity capability by IE txDiversity-r16, txDiversity2Tx-r18 or txDiversity4Tx-r18. 2Tx requirements for TxD should be applied to UE indicating txDiversity-r16 or txDiversity2Tx-r18, and 4Tx requirements should be applied to UE indicating txDiversity4Tx-r18.

f) All the requirements for intra-band contiguous SL CA apply under the assumption of the same subcarrier spacing for SL CA.

## 4.3 Specification suffix information

Unless stated otherwise, the suffixes shown in Table 4.3-1 are used for indicating at 2nd level clause. For shared spectrum channel access, suffixes A, B, and D are used for indicating at 3rd level clause. For V2X, suffixes A and F are used for indicating at 3rd level clause.

Table 4.3-1: Definition of suffixes

| Clause suffix | Variant |
| --- | --- |
| None | Single Carrier |
| A | Carrier Aggregation (CA) |
| B | Dual-Connectivity (DC) |
| C | Supplementary Uplink (SUL) |
| D | UL MIMO |
| E | V2X |
| F | Shared spectrum channel access |
| G | Tx Diversity (TxD) |
| H | Carrier Aggregation (CA) with UL MIMO |
| I | (e)RedCap |
| J | ATG |
| K | Aerial UE (UAV) |
| L | Carrier Aggregation (CA) with Tx Diversity |
| M | LP-WUS/WUR |

A terminal which supports the above features needs to meet both the general requirements and the additional requirement applicable to the additional clause (suffixes A to L) in clauses 5, 6 and 7. Where there is a difference in requirement between the general requirements and the additional clause requirements (suffixes A to L) in clauses 5, 6 and 7, the tighter requirements are applicable unless stated otherwise in the additional clause.

A terminal which supports advanced V2X services, public safety services and other commercial use cases related to NR sidelink operation shall meet all of the separate corresponding requirements in suffix E.

For a terminal that supports SUL for the band combination specified in Table 5.2C-1, the current version of the specification assumes the terminal is configured with active transmission either on UL carrier or SUL carrier at any time in one serving cell and the UE requirements for single carrier shall apply for the active UL or SUL carrier accordingly.

For a terminal that supports SUL band combinations specified in Table 5.2C-2, Table 5.2C-3 and Table 5.2C-4, the current version of the specification assumes the terminal is configured with active transmission either on UL carrier(s) or SUL carrier at any time, and the UE requirements for the active CA configuration or SUL carrier shall apply accordingly.

For a terminal that supports public safety service using sidelink, the minimum requirements are applicable when

- The UE is associated with a serving cell on PS carrier, or

- The UE is not associated with a serving cell on the PS carrier and is provisioned with the preconfigured radio parameters for PS that are associated with known Geographical Area, or

- The UE is associated with a serving cell on a carrier different than the PS carrier, and the radio parameters for PS that are provided by the serving cell, or

- The UE is associated with a serving cell on a carrier different than the PS carrier, and has a non-serving cell selected on the PS carrier with the preconfigured radio parameters.

When the advanced-V2X or PS UE is not associated with a serving cell on the V2X or PS carrier, and the UE does not have knowledge of its geographical area, or is provisioned with preconfigured radio parameters that are not associated with any Geographical Area, V2X or PS UE’ transmissions are not allowed, and the requirements in Section 6.3E.2 apply.

For a terminal that supports operation in shared spectrum, the current version of this specification assumes in the uplink sub-bands within a wideband channel shall be contiguously allocated to the UE.  The uplink requirements for one or more non-transmitted sub-bands between two transmitted sub-bands does not form a part of the current version of this specification.

Terminal that supports inter-band NR-DC configuration shall meet the minimum requirements for corresponding CA configuration (suffix A), unless otherwise specified.

A terminal which supports intra-band contiguous UL CA with UL MIMO shall meet the corresponding requirements in suffix H with all UL CCs with UL MIMO.

A terminal which supports intra-band contiguous UL CA with TxD shall meet the corresponding requirements in suffix A with all UL CCs with TxD.

A terminal which supports inter-band UL CA with UL MIMO shall meet the corresponding requirements in suffix H with all UL CCs with UL MIMO for the frequency band(s) said to be with UL MIMO.

# 5 Operating bands and channel arrangement

## 5.1 General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE: Other operating bands and channel bandwidths may be considered in future releases.

Requirements throughout the RF specifications are in many cases defined separately for different frequency ranges (FR). The frequency ranges in which NR can operate according to this version of the specification are identified as described in Table 5.1-1. Whenever the FR2 is referred, both FR2-1 and FR2-2 frequency sub-ranges shall be considered, unless otherwise stated.

Table 5.1-1: Definition of frequency ranges

| Frequency range designation |  | Corresponding frequency range |
| --- | --- | --- |
| FR1 |  | 410 MHz – 7125 MHz |
| FR2 | FR2-1 | 24250 MHz – 52600 MHz |
|  | FR2-2 | 52600 MHz – 71000 MHz |

The present specification covers FR1 operating bands.

## 5.2 Operating bands

NR is designed to operate in the FR1 operating bands defined in Table 5.2-1.

Table 5.2-1: NR operating bands in FR1

| NR operating band | Uplink (UL) operating band BS receive / UE transmitFUL_low   –  FUL_high | Downlink (DL) operating band BS transmit / UE receiveFDL_low   –  FDL_high | Duplex Mode |
| --- | --- | --- | --- |
| n1 | 1920 MHz – 1980 MHz | 2110 MHz – 2170 MHz | FDD |
| n2 | 1850 MHz – 1910 MHz | 1930 MHz – 1990 MHz | FDD |
| n3 | 1710 MHz – 1785 MHz | 1805 MHz – 1880 MHz | FDD |
| n5 | 824 MHz – 849 MHz | 869 MHz – 894 MHz | FDD |
| n7 | 2500 MHz – 2570 MHz | 2620 MHz – 2690 MHz | FDD |
| n8 | 880 MHz – 915 MHz | 925 MHz – 960 MHz | FDD |
| n12 | 699 MHz – 716 MHz | 729 MHz – 746 MHz | FDD |
| n13 | 777 MHz – 787 MHz | 746 MHz – 756 MHz | FDD |
| n14 | 788 MHz – 798 MHz | 758 MHz – 768 MHz | FDD |
| n18 | 815 MHz – 830 MHz | 860 MHz – 875 MHz | FDD |
| n20 | 832 MHz – 862 MHz | 791 MHz – 821 MHz | FDD |
| n2416 | 1626.5 MHz – 1660.5 MHz | 1525 MHz – 1559 MHz | FDD |
| n25 | 1850 MHz – 1915 MHz | 1930 MHz – 1995 MHz | FDD |
| n26 | 814 MHz – 849 MHz | 859 MHz – 894 MHz | FDD |
| n28 | 703 MHz – 748 MHz | 758 MHz – 803 MHz | FDD |
| n2919 | N/A | 717 MHz – 728 MHz | SDL |
| n303 | 2305 MHz – 2315 MHz | 2350 MHz – 2360 MHz | FDD |
| n31 | 452.5 MHz – 457.5 MHz | 462.5 MHz – 467.5 MHz | FDD |
| n34 | 2010 MHz – 2025 MHz | 2010 MHz – 2025 MHz | TDD |
| n3810 | 2570 MHz – 2620 MHz | 2570 MHz – 2620 MHz | TDD |
| n39 | 1880 MHz – 1920 MHz | 1880 MHz – 1920 MHz | TDD |
| n40 | 2300 MHz – 2400 MHz | 2300 MHz – 2400 MHz | TDD |
| n41 | 2496 MHz – 2690 MHz | 2496 MHz – 2690 MHz | TDD |
| n4613 | 5150 MHz – 5925 MHz | 5150 MHz – 5925 MHz | TDD |
| n4711 | 5855 MHz – 5925 MHz | 5855 MHz – 5925 MHz | TDD |
| n48 | 3550 MHz – 3700 MHz | 3550 MHz – 3700 MHz | TDD |
| n501 | 1432 MHz – 1517 MHz | 1432 MHz – 1517 MHz | TDD |
| n51 | 1427 MHz – 1432 MHz | 1427 MHz – 1432 MHz | TDD |
| n53 | 2483.5 MHz – 2495 MHz | 2483.5 MHz – 2495 MHz | TDD |
| n54 | 1670 MHz – 1675 MHz | 1670 MHz – 1675 MHz | TDD |
| n654 | 1920 MHz – 2010 MHz | 2110 MHz – 2200 MHz | FDD |
| n666,7 | 1710 MHz – 1780 MHz | 2110 MHz – 2200 MHz | FDD |
| n6719 | N/A | 738 MHz – 758 MHz | SDL |
| n68 | 698 MHz – 728 MHz | 753 MHz – 783 MHz | FDD |
| n70 | 1695 MHz – 1710 MHz | 1995 MHz – 2020 MHz | FDD |
| n71 | 663 MHz – 698 MHz | 617 MHz – 652 MHz | FDD |
| n72 | 451 MHz – 456 MHz | 461 MHz – 466 MHz | FDD |
| n74 | 1427 MHz – 1470 MHz | 1475 MHz – 1518 MHz | FDD |
| n752,19 | N/A | 1432 MHz – 1517 MHz | SDL |
| n7619 | N/A | 1427 MHz – 1432 MHz | SDL |
| n7712 | 3300 MHz – 4200 MHz | 3300 MHz – 4200 MHz | TDD |
| n78 | 3300 MHz – 3800 MHz | 3300 MHz – 3800 MHz | TDD |
| n7917 | 4400 MHz – 5000 MHz | 4400 MHz – 5000 MHz | TDD |
| n80 | 1710 MHz – 1785 MHz | N/A | SUL |
| n81 | 880 MHz – 915 MHz | N/A | SUL |
| n82 | 832 MHz – 862 MHz | N/A | SUL |
| n83 | 703 MHz – 748 MHz | N/A | SUL |
| n84 | 1920 MHz – 1980 MHz | N/A | SUL |
| n85 | 698 MHz – 716 MHz | 728 MHz – 746 MHz | FDD |
| n86 | 1710 MHz – 1780 MHz | N/A | SUL |
| n87 | 410 MHz – 415 MHz | 420 MHz – 425 MHz | FDD |
| n88 | 412 MHz – 417 MHz | 422 MHz – 427 MHz | FDD |
| n89 | 824 MHz – 849 MHz | N/A | SUL |
| n905 | 2496 MHz – 2690 MHz | 2496 MHz – 2690 MHz | TDD |
| n919 | 832 MHz – 862 MHz | 1427 MHz – 1432 MHz | FDD |
| n929 | 832 MHz – 862 MHz | 1432 MHz – 1517 MHz | FDD |
| n939 | 880 MHz – 915 MHz | 1427 MHz – 1432 MHz | FDD |
| n949 | 880 MHz – 915 MHz | 1432 MHz – 1517 MHz | FDD |
| n958 | 2010 MHz – 2025 MHz | N/A | SUL |
| n9613,14 | 5925 MHz – 7125 MHz | 5925 MHz – 7125 MHz | TDD |
| n9715 | 2300 MHz – 2400 MHz | N/A | SUL |
| n9815 | 1880 MHz – 1920 MHz | N/A | SUL |
| n9922 | 1626.5 MHz – 1660.5 MHz | N/A | SUL |
| n10021 | 874.4 MHz – 880 MHz | 919.4 MHz – 925 MHz | FDD |
| n10121 | 1900 MHz – 1910 MHz | 1900 MHz – 1910 MHz | TDD |
| n10213,14 | 5925 MHz – 6425 MHz | 5925 MHz – 6425 MHz | TDD |
| n10417 | 6425 MHz – 7125 MHz | 6425 MHz – 7125 MHz | TDD |
| n105 | 663 MHz – 703 MHz | 612 MHz – 652 MHz | FDD |
| n106 | 896 MHz – 901 MHz | 935 MHz – 940 MHz | FDD |
| n1099 | 703 MHz – 733 MHz | 1432 MHz – 1517 MHz | FDD |
| n110 | 1390 MHz – 1395 MHz | 1432 MHz – 1435 MHz | FDD |
| NOTE 1: UE that complies with the NR Band n50 minimum requirements in this specification shall also comply with the NR Band n51 minimum requirements.NOTE 2: UE that complies with the NR Band n75 minimum requirements in this specification shall also comply with the NR Band n76 minimum requirements.NOTE 3: Uplink transmission is not allowed at this band for UE with external vehicle-mounted antennas.NOTE 4: A UE that complies with the NR Band n65 minimum requirements in this specification shall also comply with the NR Band n1 minimum requirements.NOTE 5: Unless otherwise stated, the applicability of requirements for Band n90 is in accordance with that for Band n41; a UE supporting Band n90 shall meet the requirements for Band n41. A UE supporting Band n90 shall also support band n41.NOTE 6: A UE that supports NR Band n66 shall receive in the entire DL operating band.NOTE 7: A UE that supports NR Band n66 and CA operation in any CA band shall also comply with the minimum requirements specified for the DL CA configurations CA_n66B and CA_n66(2A) in the current version of the specification.NOTE 8: This band is applicable in China only.NOTE 9: Variable duplex operation does not enable dynamic variable duplex configuration by the network, and is used such that DL and UL frequency ranges are supported independently in any valid frequency range for the band. NOTE 10: When this band is used for V2X SL service, the band is exclusively used for NR V2X in particular regions.NOTE 11: This band is unlicensed band used for V2X service. There is no expected network deployment in this band.NOTE 12: In the USA this band is restricted to 3450 – 3550 MHz and 3700 – 3980 MHz. In Canada this band is restricted to 3450 – 3650 MHz and 3650 – 3980 MHz.NOTE 13: This band is restricted to operation with shared spectrum channel access as defined in TS 37.213 [14].NOTE 14: This band is applicable only in countries/regions designating this band for shared-spectrum access use subject to country-specific conditions.NOTE 15: The requirements for this band are applicable only where no other NR or E-UTRA TDD operating band(s) are used within the frequency range of this band in the same geographical area. For scenarios where other NR or E-UTRA TDD operating band(s) are used within the frequency range of this band in the same geographical area, special co-existence requirements may apply that are not covered by the 3GPP specifications.NOTE 16: DL operation in this band is restricted to 1526 – 1536 MHz and UL operation is restricted to 1627.5 – 1637.5 MHz and 1646.5 – 1656.5 MHz.NOTE 17: For this band, CORESET#0 values from Table 13-5 or Table 13-6 in [8, TS 38.213] are applied regardless of the minimum channel bandwidth.NOTE 18: VoidNOTE 19: For SDL bands, downlink configuration for RRM performance testing is same as FDD.NOTE 20: Operating band n200 is a reserved value.NOTE 21: This band is applicable only in countries subject to ECC Decision (20)02 [19], for the FRMCS application.NOTE 22: UL operation in this band is restricted to 1627.5 – 1637.5 MHz and 1646.5 – 1656.5 MHz. |  |  |  |

## 5.2A Operating bands for CA

### 5.2A.0 General

CA operating bands including Band n90 are defined by the corresponding CA operating bands including Band n41 with Band n90 replacing Band n41. For brevity the said CA operating bands including Band n90 are not listed in the tables below but are covered by this specification.

### 5.2A.1 Intra-band CA

NR intra-band carrier aggregation is designed to operate in the operating bands defined in Table 5.2A.1-1 and Table5.2A.1-2, where all operating bands are within FR1.

Table 5.2A.1-1: Intra-band contiguous CA operating bands in FR1

| NR CA Band | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n1 | n1 |
| CA_n2 | n2 |
| CA_n3 | n3 |
| CA_n5 | n5 |
| CA_n7 | n7 |
| CA_n25 | n25 |
| CA_n38 | n38 |
| CA_n40 | n40 |
| CA_n41 | n41 |
| CA_n46 | n46 |
| CA_n48 | n48 |
| CA_n66 | n66 |
| CA_n71 | n71 |
| CA_n77 | n77 |
| CA_n78 | n78 |
| CA_n79 | n79 |
| CA_n96 | n96 |
| CA_n102 | n102 |
| CA_n104 | n104 |
| NOTE: The minimum requirements only apply for non simultaneous Tx/Rx between all carriers for TDD combinations. |  |

Table 5.2A.1-2: Intra-band non-contiguous CA operating bands in FR1

| NR CA Band | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n1(*) | n1 |
| CA_n3(*) | n3 |
| CA_n5(*) | n5 |
| CA_n7(*) | n7 |
| CA_n12(*) | n12 |
| CA_n25(*) | n25 |
| CA_n26(*) | n26 |
| CA_n41(*) | n41 |
| CA_n48(*) | n48 |
| CA_n66(*) | n66 |
| CA_n71(*) | n71 |
| CA_n77(*) | n77 |
| CA_n78(*) | n78 |
| CA_n96(*) | n96 |
| CA_n102(*) | n102 |
| NOTE 1: The minimum requirements only apply for non simultaneous Tx/Rx between all carriers for TDD combinations.NOTE 2: The notation CA_nX(*) in this table indicates intra-band non-contiguous CA for band nX. The configurations for each band are in 5.5A.2. |  |

### 5.2A.2 Inter-band CA

NR inter-band carrier aggregation is designed to operate in the operating bands defined in Table 5.2A.2.1-1, Table 5.2A.2.2-1, Table5.2A.2.3-1, Table 5.2A.2.4-1 and Table 5.2A.2.5-1, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a lower order band combination, when the applicable lower order band combination is a band pair in a higher order band combination, the mandatory simultaneous Rx/Tx capability also applies for the band pair in the higher order band combination.

Unless stated otherwise, simultaneous Rx/Tx capability is mandatory for FR1+FR1 FDD-TDD and TDD-SDL CA combinations. Simultaneous Rx/Tx capability is mandatory without signaling for FR1+FR1 FDD-FDD and FDD-SDL CA combinations.  For low NR band inter-band CA configurations supported via switching featureSetCombinationLowBandSwitching-r19, the simultaneous Rx/Tx capability does not apply.

Table 5.2A.2-1: Void

Table 5.2A.2-2: Void

Table 5.2A.2-3: Void

#### 5.2A.2.1 Inter-band CA (two bands)

Table 5.2A.2.1-1: Inter-band CA operating bands involving FR1 (two bands)

| NR CA Band | NR Band(Table 5.2-1) | DL interruption allowed (Note 8) |
| --- | --- | --- |
| CA_n1-n3 | n1, n3 |  |
| CA_n1-n5 | n1, n5 |  |
| CA_n1-n7 | n1, n7 |  |
| CA_n1-n8 | n1, n8 |  |
| CA_n1-n18 | n1, n18 |  |
| CA_n1-n20 | n1, n20 |  |
| CA_n1-n26 | n1, n26 |  |
| CA_n1-n28 | n1, n28 |  |
| CA_n1-n38 | n1, n38 |  |
| CA_n1-n40 | n1, n40 |  |
| CA_n1-n41 | n1, n41 |  |
| CA_n1-n46 | n1, n46 |  |
| CA_n1-n67 | n1, n67 |  |
| CA_n1-n71 | n1, n71 |  |
| CA_n1-n74 | n1, n74 |  |
| CA_n1-n75 | n1, n75 |  |
| CA_n1-n77 | n1, n77 | No |
| CA_n1-n78 | n1, n78 | No |
| CA_n1-n79 | n1, n79 | No |
| CA_n1-n102 | n1, n102 |  |
| CA_n1-n105 | n1, n105 |  |
| CA_n2-n5 | n2, n5 |  |
| CA_n2-n7 | n2, n7 |  |
| CA_n2-n12 | n2, n12 |  |
| CA_n2-n14 | n2, n14 |  |
| CA_n2-n29 | n2, n29 |  |
| CA_n2-n30 | n2, n30 |  |
| CA_n2-n41 | n2, n41 |  |
| CA_n2-n48 | n2, n48 |  |
| CA_n2-n66 | n2, n66 |  |
| CA_n2-n71 | n2, n71 |  |
| CA_n2-n77 | n2, n77 |  |
| CA_n2-n78 | n2, n78 |  |
| CA_n3-n5 | n3, n5 |  |
| CA_n3-n7 | n3, n7 |  |
| CA_n3-n8 | n3, n8 |  |
| CA_n3-n18 | n3, n18 |  |
| CA_n3-n20 | n3, n20 |  |
| CA_n3-n26 | n3, n26 |  |
| CA_n3-n28 | n3, n28 |  |
| CA_n3-n34 | n3, n34 |  |
| CA_n3-n38 | n3, n38 |  |
| CA_n3-n39 | n3, n39 |  |
| CA_n3-n40 | n3, n40 | No |
| CA_n3-n41 | n3, n41 | No |
| CA_n3-n67 | n3, n67 |  |
| CA_n3-n71 | n3, n71 |  |
| CA_n3-n74 | n3, n74 |  |
| CA_n3-n75 | n3, n75 |  |
| CA_n3-n77 | n3, n77 |  |
| CA_n3-n78 | n3, n78 | No |
| CA_n3-n79 | n3, n79 | No |
| CA_n3-n34 | n3, n34 | No |
| CA_n3-n102 | n3, n102 |  |
| CA_n3-n104 | n3, n104 |  |
| CA_n3-n105 | n3, n105 |  |
| CA_n5-n7 | n5, n7 |  |
| CA_n5-n8 | n5, n8 |  |
| CA_n5-n12 | n5, n12 |  |
| CA_n5-n13 | n5, n13 |  |
| CA_n5-n14 | n5, n14 |  |
| CA_n5-n25 | n5, n25 |  |
| CA_n5-n28 | n5, n28 |  |
| CA_n5-n2921 | n5, n29 |  |
| CA_n5-n30 | n5, n30 |  |
| CA_n5-n40 | n5, n40 |  |
| CA_n5-n41 | n5, n41 |  |
| CA_n5-n48 | n5, n48 |  |
| CA_n5-n66 | n5, n66 |  |
| CA_n5-n71 | n5, n71 |  |
| CA_n5-n77 | n5, n77 |  |
| CA_n5-n78 | n5, n78 | No |
| CA_n5-n79 | n5, n79 | No |
| CA_n5-n105 | n5, n105 |  |
| CA_n7-n8 | n7, n8 |  |
| CA_n7-n12 | n7, n12 |  |
| CA_n7-n20 | n7, n20 |  |
| CA_n7-n25 | n7, n25 |  |
| CA_n7-n26 | n7, n26 |  |
| CA_n7-n28 | n7, n28 |  |
| CA_n7-n29 | n7, n29 |  |
| CA_n7-n40 | n7, n40 |  |
| CA_n7-n466 | n7, n46 |  |
| CA_n7-n66 | n7, n66 |  |
| CA_n7-n67 | n7, n67 |  |
| CA_n7-n71 | n7, n71 |  |
| CA_n7-n75 | n7, n75 |  |
| CA_n7-n77 | n7, n77 |  |
| CA_n7-n78 | n7, n78 |  |
| CA_n7-n79 | n7, n79 |  |
| CA_n7-n102 | n7, n102 |  |
| CA_n7-n105 | n7, n105 |  |
| CA_n8-n20 | n8, n20 |  |
| CA_n8-n28 | n8, n28 |  |
| CA_n8-n34 | n8, n34 |  |
| CA_n8-n38 | n8, n38 |  |
| CA_n8-n39 | n8, n39 |  |
| CA_n8-n40 | n8, n40 |  |
| CA_n8-n41 | n8, n41 | No |
| CA_n8-n751 | n8, n75 |  |
| CA_n8-n77 | n8, n77 |  |
| CA_n8-n78 | n8, n78 | No |
| CA_n8-n79 | n8, n79 | No |
| CA_n8-n104 | n8, n104 |  |
| CA_n12-n25 | n12, n25 |  |
| CA_n12-n2921 | n12, n29 |  |
| CA_n12-n30 | n12, n30 |  |
| CA_n12-n41 | n12, n41 |  |
| CA_n12-n48 | n12, n48 |  |
| CA_n12-n66 | n12, n66 |  |
| CA_n12-n71 | n12, n71 |  |
| CA_n12-n77 | n12, n77 |  |
| CA_n12-n78 | n12, n78 |  |
| CA_n13-n25 | n13, n25 |  |
| CA_n13-n66 | n13, n66 |  |
| CA_n13-n77 | n13, n77 |  |
| CA_n14-n2921 | n14, n29 |  |
| CA_n14-n30 | n14, n30 |  |
| CA_n14-n66 | n14, n66 |  |
| CA_n14-n77 | n14, n77 |  |
| CA_n18-n28 | n18, n28 |  |
| CA_n18-n40 | n18, n40 |  |
| CA_n18-n41 | n18, n41 |  |
| CA_n18-n74 | n18, n74 |  |
| CA_n18-n7710 | n18, n77 |  |
| CA_n18-n7811 | n18, n78 |  |
| CA_n20-n282 | n20, n28 |  |
| CA_n20-n40 | n20, n40 |  |
| CA_n20-n41 | n20, n41 |  |
| CA_n20-n67 | n20, n67 |  |
| CA_n20-n71 | n20, n71 |  |
| CA_n20-n75 | n20, n75 |  |
| CA_n20-n77 | n20, n77 |  |
| CA_n20-n78 | n20, n78 |  |
| CA_n24-n41 | n24, n41 |  |
| CA_n24-n48 | n24, n48 |  |
| CA_n24-n77 | n24, n77 |  |
| CA_n25-n29 | n25, n29 |  |
| CA_n25-n38 | n25, n38 |  |
| CA_n25-n41 | n25, n41 |  |
| CA_n25-n466 | n25, n46 |  |
| CA_n25-n48 | n25, n48 |  |
| CA_n25-n66 | n25, n66 |  |
| CA_n25-n71 | n25, n71 |  |
| CA_n25-n77 | n25, n77 |  |
| CA_n25-n78 | n25, n78 |  |
| CA_n25-n85 | n25, n85 |  |
| CA_n26-n28 | n26, n28 |  |
| CA_n26-n29 | n26, n29 |  |
| CA_n26-n48 | n26, n48 |  |
| CA_n26-n66 | n26, n66 |  |
| CA_n26-n70 | n26, n70 |  |
| CA_n26-n71 | n26, n71 |  |
| CA_n26-n77 | n26, n77 |  |
| CA_n26-n78 | n26, n78 |  |
| CA_n28-n6721 | n28, n67 |  |
| CA_n28-n34 | n28, n34 |  |
| CA_n28-n38 | n28, n38 |  |
| CA_n28-n39 | n28, n39 |  |
| CA_n28-n40 | n28, n40 |  |
| CA_n28-n41 | n28, n41 |  |
| CA_n28-n466 | n28, n46 |  |
| CA_n28-n50 | n28, n50 |  |
| CA_n28-n7112 | n28, n71 |  |
| CA_n28-n74 | n28, n74 |  |
| CA_n28-n752 | n28, n75 |  |
| CA_n28-n77 | n28, n77 | No |
| CA_n28-n78 | n28, n78 | No |
| CA_n28-n79 | n28, n79 |  |
| CA_n28-n94 | n28, n94 |  |
| CA_n28-n102 | n28, n102 |  |
| CA_n28-n105 | n28, n105 |  |
| CA_n29-n30 | n29, n30 |  |
| CA_n29-n48 | n29, n48 |  |
| CA_n29-n66 | n29, n66 |  |
| CA_n29-n70 | n29, n70 |  |
| CA_n29-n7121 | n29, n71 |  |
| CA_n29-n77 | n29, n77 |  |
| CA_n30-n66 | n30, n66 |  |
| CA_n30-n77 | n30, n77 |  |
| CA_n34-n399 | n34, n39 |  |
| CA_n34-n40 | n34, n40 |  |
| CA_n34-n41 | n34, n41 |  |
| CA_n34-n791 | n34, n79 |  |
| CA_n38-n409 | n38, n40 |  |
| CA_n38-n66 | n38, n66 |  |
| CA_n38-n71 | n38, n71 |  |
| CA_n38-n781 | n38, n78 |  |
| CA_n38-n791 | n38, n79 |  |
| CA_n39-n40 | n39, n40 |  |
| CA_n39-n41 | n39, n41 | No |
| CA_n39-n791 | n39, n79 | No |
| CA_n40-n41 | n40, n41 |  |
| CA_n40-n71 | n40, n71 |  |
| CA_n40-n771 | n40, n77 |  |
| CA_n40-n781 | n40, n78 |  |
| CA_n40-n791,4 | n40, n79 | No |
| CA_n40-n105 | n40, n105 |  |
| CA_n41-n481 | n41, n48 |  |
| CA_n41-n501 | n41, n50 |  |
| CA_n41-n66 | n41, n66 |  |
| CA_n41-n70 | n41, n70 |  |
| CA_n41-n71 | n41, n71 |  |
| CA_n41-n74 | n41, n74 |  |
| CA_n41-n771 | n41, n77 |  |
| CA_n41-n781 | n41, n78 |  |
| CA_n41-n791,3 | n41, n79 | No |
| CA_n41-n85 | n41, n85 |  |
| CA_n41-n104 | n41, n104 |  |
| CA_n46-n481,6 | n46, n48 |  |
| CA_n46-n666 | n46, n66 |  |
| CA_n46-n771,6 | n46, n77 |  |
| CA_n46-n781,6 | n46, n78 |  |
| CA_n46-n969,16,17,18 | n46, n96 |  |
| CA_n46-n1029,16,18,20 | n46, n102 |  |
| CA_n48-n539 | n48, n53 |  |
| CA_n48-n66 | n48, n66 |  |
| CA_n48-n70 | n48, n70 |  |
| CA_n48-n71 | n48, n71 |  |
| CA_n48-n779,14,18 | n48, n77 |  |
| CA_n48-n961, 6 | n48, n96 |  |
| CA_n50-n78 | n50, n78 |  |
| CA_n66-n70 | n66, n70 |  |
| CA_n66-n71 | n66, n71 |  |
| CA_n66-n77 | n66, n77 |  |
| CA_n66-n78 | n66, n78 |  |
| CA_n66-n85 | n66, n85 |  |
| CA_n67-n78 | n67, n78 |  |
| CA_n70-n71 | n70, n71 |  |
| CA_n70-n77 | n70, n77 |  |
| CA_n70-n78 | n70, n78 |  |
| CA_n71-n77 | n71, n77 |  |
| CA_n71-n78 | n71, n78 |  |
| CA_n71-n85 | n71, n85 |  |
| CA_n74-n77 | n74, n77 |  |
| CA_n74-n78 | n74, n78 |  |
| CA_n75-n781 | n75, n78 |  |
| CA_n76-n781 | n76, n78 |  |
| CA_n77-n789 | n77, n78 |  |
| CA_n77-n795 | n77, n79 |  |
| CA_n77-n85 | n77, n85 |  |
| CA_n77-n102 | n77, n102 |  |
| CA_n78-n795 | n78, n79 |  |
| CA_n78-n92 | n78, n92 |  |
| CA_n78-n94 | n78, n94 |  |
| CA_n78-n102 | n78, n102 |  |
| CA_n78-n104 | n78, n104 |  |
| CA_n78-n105 | n78, n105 |  |
| CA_n100-n101 | n100, n101 |  |
| NOTE 1: Applicable for UE supporting inter-band carrier aggregation with mandatory simultaneous Rx/Tx capability.NOTE 2: The frequency range in band n28 is restricted for this band combination to 703-733 MHz for the UL and 758-788 MHz for the DL.NOTE 3: The frequency range below 2506 MHz for Band n41 is not used in this combination.NOTE 4: Applicable for frequency range above 4800 MHz for Band n79 in this combination.NOTE 5: For UEs supporting band n77, the minimum requirements apply only when there is non-simultaneous Rx/Tx operation between n78-n79 or n77-n79 NR carriers. This restriction applies also for these carriers when applicable NR CA configuration is part of a higher order configuration.NOTE 6: The PCell is allocated in the licensed band in this combination.NOTE 7: Void.NOTE 8: Applicable when dynamic Tx switching is conducted. The DL interruption requirement is specified in clause 8.2.2.2.10 of 38.133 [13].NOTE 9: Only applicable for UE supporting inter-band carrier aggregation without simultaneous Rx/Tx. Same restrictions are applied when applicable NR CA configuration is part of a higher order configurations.NOTE 10 The frequency range in band n77 is restricted for this band combination to 3520-3560 MHz, 3700-3800 MHz, 4000-4100 MHz.NOTE 11: The frequency range in band n78 is restricted for this band combination to 3520 -3560 MHz and 3700– 3800 MHz.NOTE 12: The implementation with 4 antennas is targeted for FWA form factor for this band combination.NOTE 13: VoidNOTE 14: The band n48 and n77 will synchronize their uplink and downlink configurations and in commonly TDD network coordinationNOTE 15: VoidNOTE 16: The minimum requirements for intra-band non-contiguous CA/DC apply for CA_n46-n96 or CA_n46-n102 and related higher order CA/DC configurations.NOTE 17: The combination is not used alone as fall back mode of other band combinations in which UL in Band 48 is not used.NOTE 18: The minimum requirements for inter-band CA apply when the maximum power spectral density imbalance between downlink carriers is within 6 dB. The power spectral density imbalance condition also applies for these carriers when applicable CA configuration is a subset of a higher order CA configuration.NOTE 19: VoidNOTE 20: The combination is not used alone as fall back mode of other band combinations in which UL in Band n78 is not used.NOTE 21: Concurrent operation between these bands is not applicable to UEs indicating support of low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19 for this band combination. |  |  |

#### 5.2A.2.2 Inter-band CA (three bands)

Table 5.2A.2.2-1: Inter-band CA operating bands involving FR1 (three bands)

| NR CA Band | NR Band(Table 5.2-1) | DL interruption allowed (Note 4) |
| --- | --- | --- |
| CA_n1-n3-n5 | n1, n3, n5 |  |
| CA_n1-n3-n7 | n1, n3, n7 |  |
| CA_n1-n3-n8 | n1, n3, n8 |  |
| CA_n1-n3-n18 | n1, n3, n18 |  |
| CA_n1-n3-n20 | n1, n3, n20 |  |
| CA_n1-n3-n26 | n1, n3, n26 |  |
| CA_n1-n3-n28 | n1, n3, n28 |  |
| CA_n1-n3-n38 | n1, n3, n38 |  |
| CA_n1-n3-n40 | n1, n3, n40 |  |
| CA_n1-n3-n413 | n1, n3, n41 |  |
| CA_n1-n3-n71 | n1, n3, n71 |  |
| CA_n1-n3-n75 | n1, n3, n75 |  |
| CA_n1-n3-n77 | n1, n3, n77 |  |
| CA_n1-n3-n783 | n1, n3, n78 | No for CA_n1-n78, CA_n3-n78 |
| CA_n1-n3-n793 | n1, n3, n79 |  |
| CA_n1-n3-n105 | n1, n3, n105 |  |
| CA_n1-n5-n7 | n1, n5, n7 |  |
| CA_n1-n5-n8 | n1, n5, n8 |  |
| CA_n1-n5-n28 | n1, n5, n28 |  |
| CA_n1-n5-n40 | n1, n5, n40 |  |
| CA_n1-n5-n78 | n1, n5, n78 | No for n1-n78, n5-n78 |
| CA_n1-n5-n79 | n1, n5, n79 |  |
| CA_n1-n5-n105 | n1, n5, n105 |  |
| CA_n1-n7-n8 | n1, n7, n8 |  |
| CA_n1-n7-n20 | n1, n7, n20 |  |
| CA_n1-n7-n28 | n1, n7, n28 |  |
| CA_n1-n7-n38 | n1, n7, n38 |  |
| CA_n1-n7-n40 | n1, n7, n40 |  |
| CA_n1-n7-n67 | n1, n7, n67 |  |
| CA_n1-n7-n75 | n1,n7, n75 |  |
| CA_n1-n7-n77 | n1,n7, n77 |  |
| CA_n1-n7-n783 | n1, n7, n78 |  |
| CA_n1-n7-n79 | n1, n7, n79 |  |
| CA_n1-n7-n105 | n1, n7, n105 |  |
| CA_n1-n8-n28 | n1, n8, n28 |  |
| CA_n1-n8-n40 | n1, n8, n40 |  |
| CA_n1-n8-n41 | n1, n8, n41 |  |
| CA_n1-n8-n77 | n1, n8, n77 |  |
| CA_n1-n8-n783 | n1, n8, n78 |  |
| CA_n1-n8-n79 | n1, n8, n79 |  |
| CA_n1-n18-n28 | n1, n18, n28 |  |
| CA_n1-n18-n41 | n1, n18, n41 |  |
| CA_n1-n18-n77 | n1, n18, n77 |  |
| CA_n1-n20-n41 | n1, n20, n41 |  |
| CA_n1-n20-n67 | n1, n20, n67 |  |
| CA_n1-n20-n71 | n1, n20, n71 |  |
| CA_n1-n20-n77 | n1, n20, n77 |  |
| CA_n1-n20-n78 | n1, n20, n78 |  |
| CA_n1-n26-n78 | n1, n26, n78 |  |
| CA_n1-n28-n38 | n1, n28, n38 |  |
| CA_n1-n28-n40 | n1, n28, n40 |  |
| CA_n1-n28-n413 | n1, n28, n41 |  |
| CA_n1-n28-n46 | n1, n28, n46 |  |
| CA_n1-n28-n75 | n1, n28, n75 |  |
| CA_n1-n28-n773 | n1, n28, n77 |  |
| CA_n1-n28-n783 | n1, n28, n78 |  |
| CA_n1-n28-n793 | n1, n28, n79 |  |
| CA_n1-n28-n102 | n1, n28, n102 |  |
| CA_n1-n38-n78 | n1, n38, n78 |  |
| CA_n1-n40-n41 | n1, n40, n41 |  |
| CA_n1-n40-n77 | n1, n40, n77 |  |
| CA_n1-n40-n78 | n1, n40, n78 |  |
| CA_n1-n40-n79 | n1, n40, n79 |  |
| CA_n1-n40-n105 | n1, n40, n105 |  |
| CA_n1-n41-n71 | n1, n41, n71 |  |
| CA_n1-n41-n773 | n1, n41, n77 |  |
| CA_n1-n41-n78 | n1, n41, n78 |  |
| CA_n1-n41-n79 | n1, n41, n79 |  |
| CA_n1-n46-n78 | n1, n46, n78 |  |
| CA_n1-n71-n77 | n1, n71, n77 |  |
| CA_n1-n71-n78 | n1, n71, n78 |  |
| CA_n1-n67-n78 | n1, n67, n78 |  |
| CA_n1-n75-n78 | n1, n75, n78 |  |
| CA_n1-n77-n79 | n1, n77, n79 |  |
| CA_n1-n78-n79 | n1, n78, n79 |  |
| CA_n1-n78-n102 | n1, n78, n102 |  |
| CA_n1-n78-n105 | n1, n78, n105 |  |
| CA_n2-n5-n30 | n2, n5, n30 |  |
| CA_n2-n5-n41 | n2, n5, n41 |  |
| CA_n2-n5-n48 | n2, n5, n48 |  |
| CA_n2-n5-n66 | n2, n5, n66 |  |
| CA_n2-n5-n77 | n2, n5, n77 |  |
| CA_n2-n7-n12 | n2, n7, n12 |  |
| CA_n2-n7-n66 | n2, n7, n66 |  |
| CA_n2-n7-n71 | n2, n7, n71 |  |
| CA_n2-n7-n77 | n2, n7, n77 |  |
| CA_n2-n12-n30 | n2, n12, n30 |  |
| CA_n2-n12-n41 | n2, n12, n41 |  |
| CA_n2-n12-n66 | n2, n12, n66 |  |
| CA_n2-n12-n71 | n2, n12, n71 |  |
| CA_n2-n12-n77 | n2, n12, n77 |  |
| CA_n2-n14-n30 | n2, n14, n30 |  |
| CA_n2-n14-n66 | n2, n14, n66 |  |
| CA_n2-n14-n77 | n2, n14, n77 |  |
| CA_n2-n29-n30 | n2, n29, n30 |  |
| CA_n2-n29-n66 | n2, n29, n66 |  |
| CA_n2-n29-n77 | n2, n29, n77 |  |
| CA_n2-n30-n66 | n2, n30, n66 |  |
| CA_n2-n30-n77 | n2, n30, n77 |  |
| CA_n2-n41-n66 | n2, n41, n66 |  |
| CA_n2-n41-n71 | n2, n41, n71 |  |
| CA_n2-n48-n66 | n2, n48, n66 |  |
| CA_n2-n48-n77 | n2, n48, n77 |  |
| CA_n2-n66-n71 | n2, n66, n71 |  |
| CA_n2-n66-n77 | n2, n66, n77 |  |
| CA_n2-n66-n78 | n2, n66, n78 |  |
| CA_n2-n71-n77 | n2, n71, n77 |  |
| CA_n2-n71-n78 | n2, n71, n78 |  |
| CA_n3-n5-n7 | n3, n5, n7 |  |
| CA_n3-n5-n28 | n3, n5, n28 |  |
| CA_n3-n5-n78 | n3, n5, n78 | No for n3-n78, n5-n78 |
| CA_n3-n5-n79 | n3, n5, n79 |  |
| CA_n3-n7-n8 | n3, n7, n8 |  |
| CA_n3-n7-n20 | n3, n7, n20 |  |
| CA_n3-n7-n26 | n3, n7, n26 |  |
| CA_n3-n7-n28 | n3, n7, n28 |  |
| CA_n3-n7-n38 | n3, n7, n38 |  |
| CA_n3-n7-n67 | n3, n7, n67 |  |
| CA_n3-n7-n75 | n3, n7, n75 |  |
| CA_n3-n7-n77 | n3, n7, n77 |  |
| CA_n3-n7-n783 | n3, n7, n78 |  |
| CA_n3-n7-n79 | n3, n7, n79 |  |
| CA_n3-n7-n105 | n3, n7, n105 |  |
| CA_n3-n8-n28 | n3, n8, n28 |  |
| CA_n3-n8-n39 | n3, n8, n39 |  |
| CA_n3-n8-n40 | n3, n8, n40 |  |
| CA_n3-n8-n41 | n3, n8, n41 |  |
| CA_n3-n8-n77 | n3, n8, n77 |  |
| CA_n3-n8-n783 | n3, n8, n78 |  |
| CA_n3-n8-n79 | n3, n8, n79 |  |
| CA_n3-n18-n28 | n3, n18, n28 |  |
| CA_n3-n18-n41 | n3, n18, n41 |  |
| CA_n3-n18-n77 | n3, n18, n77 |  |
| CA_n3-n20-n28 | n3, n20, n28 |  |
| CA_n3-n20-n41 | n3, n20, n41 |  |
| CA_n3-n20-n67 | n3, n20, n67 |  |
| CA_n3-n20-n71 | n3, n20, n71 |  |
| CA_n3-n20-n75 | n3, n20, n75 |  |
| CA_n3-n20-n77 | n3, n20, n77 |  |
| CA_n3-n20-n78 | n3, n20, n78 |  |
| CA_n3-n26-n78 | n3, n26, n38 |  |
| CA_n3-n28-n38 | n3, n28, n38 |  |
| CA_n3-n28-n403 | n3, n28, n40 |  |
| CA_n3-n28-n413 | n3, n28, n41 |  |
| CA_n3-n28-n75 | n3, n28, n75 |  |
| CA_n3-n28-n773 | n3, n28, n77 |  |
| CA_n3-n28-n783 | n3, n28, n78 |  |
| CA_n3-n28-n793 | n3, n28, n79 |  |
| CA_n3-n38-n40 | n3, n38, n40 |  |
| CA_n3-n39-n41 | n3, n39, n41 |  |
| CA_n3-n39-n79 | n3, n39, n79 |  |
| CA_n3-n40-n41 | n3, n40, n41 | No for CA n3-n40, CA n3-n41 |
| CA_n3-n40-n77 | n3, n40, n77 |  |
| CA_n3-n40-n78 | n3, n40, n78 |  |
| CA_n3-n40-n79 | n3, n40, n79 |  |
| CA_n3-n40-n105 | n3, n40, n105 |  |
| CA_n3-n41-n71 | n3, n41, n71 |  |
| CA_n3-n41-n773 | n3, n41, n77 |  |
| CA_n3-n41-n783 | n3, n41, n78 |  |
| CA_n3-n41-n793 | n3, n41, n79 | No |
| CA_n3-n67-n78 | n3, n67, n78 |  |
| CA_n3-n71-n77 | n3, n71, n77 |  |
| CA_n3-n71-n78 | n3, n71, n78 |  |
| CA_n3-n75-n78 | n3, n75, n78 |  |
| CA_n3-n77-n79 | n3, n77, n79 |  |
| CA_n3-n78-n79 | n3, n78, n79 |  |
| CA_n3-n78-n105 | n3, n78, n105 |  |
| CA_n5-n7-n25 | n5, n7, n25 |  |
| CA_n5-n7-n28 | n5, n7, n28 |  |
| CA_n5-n7-n40 | n5, n7, n40 |  |
| CA_n5-n7-n66 | n5, n7, n66 |  |
| CA_n5-n7-n77 | n5, n7, n77 |  |
| CA_n5-n7-n78 | n5, n7, n78 |  |
| CA_n5-n7-n105 | n5, n7, n105 |  |
| CA_n5-n12-n77 | n5, n12, n77 |  |
| CA_n5-n14-n77 | n5, n14, n77 |  |
| CA_n5-n25-n29 | n5, n25, n29 |  |
| CA_n5-n25-n41 | n5, n25, n41 |  |
| CA_n5-n25-n66 | n5, n25, n66 |  |
| CA_n5-n25-n77 | n5, n25, n77 |  |
| CA_n5-n25-n78 | n5, n25, n78 |  |
| CA_n5-n28-n78 | n5, n28, n78 |  |
| CA_n5-n28-n79 | n5, n28, n79 |  |
| CA_n5-n28-n105 | n5, n28, n105 |  |
| CA_n5-n29-n66 | n5, n29, n66 |  |
| CA_n5-n29-n77 | n5, n29, n77 |  |
| CA_n5-n30-n66 | n5, n30, n66 |  |
| CA_n5-n30-n77 | n5, n30, n77 |  |
| CA_n5-n40-n78 | n5, n40, n78 |  |
| CA_n5-n40-n105 | n5, n40, n105 |  |
| CA_n5-n41-n66 | n5, n41, n66 |  |
| CA_n5-n41-n77 | n5, n41, n77 |  |
| CA_n5-n48-n66 | n5, n48, n66 |  |
| CA_n5-n48-n77 | n5, n48, n77 |  |
| CA_n5-n66-n77 | n5, n66, n77 |  |
| CA_n5-n66-n78 | n5, n66, n78 |  |
| CA_n5-n78-n79 | n5, n78, n79 |  |
| CA_n5-n78-n105 | n5, n78, n105 |  |
| CA_n7-n8-n28 | n7, n8, n28 |  |
| CA_n7-n8-n40 | n7, n8, n40 |  |
| CA_n7-n8-n783 | n7, n8, n78 |  |
| CA_n7-n12-n25 | n7, n12, n25 |  |
| CA_n7-n12-n66 | n7, n12, n66 |  |
| CA_n7-n12-n71 | n7, n12, n71 |  |
| CA_n7-n12-n77 | n7, n12, n77 |  |
| CA_n7-n20-n67 | n7, n20, n67 |  |
| CA_n7-n20-n75 | n7, n20, n75 |  |
| CA_n7-n20-n78 | n7, n20, n78 |  |
| CA_n7-n25-n29 | n7, n25, n29 |  |
| CA_n7-n25-n66 | n7, n25, n66 |  |
| CA_n7-n25-n71 | n7, n25, n71 |  |
| CA_n7-n25-n77 | n7, n25, n77 |  |
| CA_n7-n25-n78 | n7, n25, n78 |  |
| CA_n7-n26-n78 | n7, n26, n78 |  |
| CA_n7-n28-n38 | n7, n28, n38 |  |
| CA_n7-n28-n40 | n7, n28, n40 |  |
| CA_n7-n28-n75 | n7, n28, n75 |  |
| CA_n7-n28-n78 | n7, n28, n78 |  |
| CA_n7-n29-n66 | n7, n29, n66 |  |
| CA_n7-n29-n77 | n7, n29, n77 |  |
| CA_n7-n40-n79 | n7, n40, n79 |  |
| CA_n7-n40-n105 | n7, n40, n105 |  |
| CA_n7-n46-n78 | n7, n46, n78 |  |
| CA_n7-n66-n71 | n7, n66, n71 |  |
| CA_n7-n66-n77 | n7, n66, n77 |  |
| CA_n7-n66-n78 | n7, n66, n78 |  |
| CA_n7-n67-n78 | n7, n67, n78 |  |
| CA_n7-n71-n77 | n7, n71, n77 |  |
| CA_n7-n75-n78 | n7, n75, n78 |  |
| CA_n7-n78-n79 | n7, n78, n79 |  |
| CA_n7-n78-n102 | n7, n78, n102 |  |
| CA_n7-n78-n105 | n7, n78, n105 |  |
| CA_n8-n20-n28 | n8, n20, n28 |  |
| CA_n8-n20-n75 | n8, n20, n75 |  |
| CA_n8-n28-n40 | n8, n28, n40 |  |
| CA_n8-n28-n75 | n8, n28, n75 |  |
| CA_n8-n28-n77 | n8, n28, n77 |  |
| CA_n8-n28-n783 | n8, n28, n78 |  |
| CA_n8-n38-n40 | n8, n38, n40 |  |
| CA_n8-n39-n40 | n8, n39, n40 |  |
| CA_n8-n39-n41 | n8, n39, n41 | No for CA n8-n41, CA n39-n41 |
| CA_n8-n39-n79 | n8, n39, n79 |  |
| CA_n8-n40-n41 | n8, n40, n41 |  |
| CA_n8-n40-n78 | n8, n40, n78 |  |
| CA_n8-n40-n79 | n8, n40, n79 |  |
| CA_n8-n41-n78 | n8, n41, n78 |  |
| CA_n8-n41-n793 | n8, n41, n79 | No |
| CA_n8-n78-n79 | n8, n78, n79 |  |
| CA_n12-n25-n41 | n12, n25, n41 |  |
| CA_n12-n25-n66 | n12, n25, n66 |  |
| CA_n12-n30-n66 | n12, n30, n66 |  |
| CA_n12-n30-n77 | n12, n30, n77 |  |
| CA_n12-n41-n66 | n12, n41, n66 |  |
| CA_n12-n41-n77 | n12, n41, n77 |  |
| CA_n12-n66-n77 | n12, n66, n77 |  |
| CA_n12-n71-n77 | n12, n71, n77 |  |
| CA_n13-n25-n66 | n13, n25, n66 |  |
| CA_n13-n25-n77 | n13, n25, n77 |  |
| CA_n13-n66-n77 | n13, n66, n77 |  |
| CA_n14-n30-n66 | n14, n30, n66 |  |
| CA_n14-n30-n77 | n14, n30, n77 |  |
| CA_n14-n66-n77 | n14, n66, n77 |  |
| CA_n18-n28-n41 | n18, n28, n41 |  |
| CA_n18-n28-n77 | n18, n28, n77 |  |
| CA_n18-n41-n77 | n18, n41, n77 |  |
| CA_n20-n28-n75 | n20, n28, n75 |  |
| CA_n20-n28-n78 | n20, n28, n78 |  |
| CA_n20-n41-n71 | n20, n41, n71 |  |
| CA_n20-n41-n77 | n20, n41, n77 |  |
| CA_n20-n41-n78 | n20, n41, n78 |  |
| CA_n20-n67-n78 | n20, n67, n78 |  |
| CA_n20-n71-n78 | n20, n71, n78 |  |
| CA_n20-n75-n78 | n20, n75, n78 |  |
| CA_n24-n41-n48 | n24, n41, n48 |  |
| CA_n24-n41-n77 | n24, n41, n77 |  |
| CA_n24-n48-n77 | n24, n48, n77 |  |
| CA_n25-n41-n77 | n25, n41, n77 |  |
| CA_n25-n29-n66 | n25, n29, n66 |  |
| CA_n25-n29-n77 | n25, n29, n77 |  |
| CA_n25-n38-n78 | n25, n38, n78 |  |
| CA_n25-n41-n66 | n25, n41, n66 |  |
| CA_n25-n41-n71 | n25, n41, n71 |  |
| CA_n25-n41-n77 | n25, n41, n77 |  |
| CA_n25-n41-n78 | n25, n41, n78 |  |
| CA_n25-n41-n85 | n25, n41, n85 |  |
| CA_n25-n48-n66 | n25, n48, n66 |  |
| CA_n25-n66-n71 | n25, n66, n71 |  |
| CA_n25-n66-n77 | n25, n66, n77 |  |
| CA_n25-n66-n78 | n25, n66, n78 |  |
| CA_n25-n66-n85 | n25, n66, n85 |  |
| CA_n25-n71-n77 | n25, n71, n77 |  |
| CA_n25-n71-n78 | n25, n71, n78 |  |
| CA_n25-n71-n85 | n25, n71, n85 |  |
| CA_n25-n77-n85 | n25, n77 n85 |  |
| CA_n26-n29-n66 | n26, n29, n66 |  |
| CA_n26-n29-n70 | n26, n29, n70 |  |
| CA_n26-n48-n66 | n26, n48, n66 |  |
| CA_n26-n48-n70 | n26, n48, n70 |  |
| CA_n26-n66-n70 | n26, n66, n70 |  |
| CA_n26-n66-n71 | n26, n66, n71 |  |
| CA_n26-n66-n77 | n26, n66, n77 |  |
| CA_n26-n70-n71 | n26, n70, n71 |  |
| CA_n26-n70-n77 | n26, n70, n77 |  |
| CA_n28-n38-n78 | n28, n38, n78 |  |
| CA_n28-n39-n40 | n28, n39, n40 |  |
| CA_n28-n39-n41 | n28, n39, n41 |  |
| CA_n28-n39-n79 | n28, n39, n79 |  |
| CA_n28-n40-n41 | n28, n40, n41 |  |
| CA_n28-n40-n71 | n28, n40, n71 |  |
| CA_n28-n40-n77 | n28, n40, n77 |  |
| CA_n28-n40-n78 | n28, n40, n78 |  |
| CA_n28-n40-n79 | n28, n40, n79 |  |
| CA_n28-n41-n773 | n28, n41, n77 |  |
| CA_n28-n41-n783 | n28, n41, n78 |  |
| CA_n28-n41-n793 | n28, n41, n79 |  |
| CA_n28-n46-n78 | n28, n46, n78 |  |
| CA_n28-n71-n77 | n28, n71, n77 |  |
| CA_n28-n75-n78 | n28, n75, n78 |  |
| CA_n28-n77-n79 | n28, n77, n79 |  |
| CA_n28-n78-n79 | n28, n78, n79 |  |
| CA_n28-n78-n102 | n28, n78, n102 |  |
| CA_n29-n30-n66 | n29, n30, n66 |  |
| CA_n29-n30-n77 | n29, n30, n77 |  |
| CA_n29-n66-n70 | n29, n66, n70 |  |
| CA_n29-n66-n71 | n29, n66, n71 |  |
| CA_n29-n66-n77 | n29, n66, n77 |  |
| CA_n29-n70-n71 | n29, n70, n71 |  |
| CA_n30-n66-n77 | n30, n66, n77 |  |
| CA_n34-n39-n40 | n34, n39, n40 |  |
| CA_n34-n39-n41 | n34, n39, n41 |  |
| CA_n34-n40-n41 | n34, n40, n41 |  |
| CA_n34-n41-n79 | n34, n41, n79 |  |
| CA_n38-n66-n78 | n38, n66, n78 |  |
| CA_n39-n40-n41 | n39, n40, n41 |  |
| CA_n39-n40-n79 | n39, n40, n79 |  |
| CA_n39-n41-n79 | n39, n41, n79 | No |
| CA_n40-n41-n791,2 | n40, n41, n79 | No for CA n40-n79, CA n41-n79 |
| CA_n40-n78-n79 | n40, n78, n79 |  |
| CA_n40-n78-n105 | n40, n78, n105 |  |
| CA_n41-n66-n71 | n41, n66, n71 |  |
| CA_n41-n66-n77 | n41, n66, n77 |  |
| CA_n41-n66-n78 | n41, n66, n78 |  |
| CA_n41-n66-n85 | n41, n66, n85 |  |
| CA_n41-n70-n78 | n41, n70, n78 |  |
| CA_n41-n71-n77 | n41, n71, n77 |  |
| CA_n41-n71-n78 | n41, n71, n78 |  |
| CA_n41-n71-n85 | n41, n71, n85 |  |
| CA_n41-n74-n77 | n41, n74, n77 |  |
| CA_n41-n77-n79 | n41, n77, n79 |  |
| CA_n41-n77-n85 | n41, n77, n85 |  |
| CA_n46-n48-n96 | n46, n48, n96 |  |
| CA_n46-n78-n102 | n46, n78, n102 |  |
| CA_n48-n66-n70 | n48, n66, n70 |  |
| CA_n48-n66-n71 | n48, n66, n71 |  |
| CA_n48-n66-n77 | n48, n66, n77 |  |
| CA_n48-n70-n71 | n48, n70, n71 |  |
| CA_n48-n70-n77 | n48, n70, n77 |  |
| CA_n48-n71-n77 | n48, n71, n77 |  |
| CA_n66-n70-n71 | n66, n70, n71 |  |
| CA_n66-n70-n77 | n66, n70, n77 |  |
| CA_n66-n70-n78 | n66, n70, n78 |  |
| CA_n66-n71-n77 | n66, n71, n77 |  |
| CA_n66-n71-n78 | n66, n71, n78 |  |
| CA_n66-n71-n85 | n66, n71, n85 |  |
| CA_n66-n77-n85 | n66, n77, n85 |  |
| CA_n70-n71-n77 | n70, n71, n77 |  |
| NOTE 1: The frequency range below 2506 MHz for Band n41 is not used in this band combination.NOTE 2: Applicable for frequency range above 4800 MHz for Band n79 in this band combination.NOTE 3: Applicable for UE supporting inter-band carrier aggregation with mandatory simultaneous Rx/Tx capabilityNOTE 4: Applicable when dynamic Tx switching is triggered across any 2 UL bands among the configured 2 or 3 UL bands. The DL interruption requirement is specified in clause 8.2.2.2 of 38.133 [13]. The nX-nY in the requirement of “No for nX-nY” refers to the two UL Bands nX and nY that are involved in dynamic Tx switching.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation without simultaneous Rx/Tx |  |  |

#### 5.2A.2.3 Inter-band CA (four bands)

Table 5.2A.2.3-1: Inter-band CA operating bands involving FR1 (four bands)

| NR CA Band | NR Band(Table 5.2-1) | DL interruption allowed (Note 2 |
| --- | --- | --- |
| CA_n1-n3-n5-n7 | n1, n3, n5, n7 |  |
| CA_n1-n3-n5-n28 | n1, n3, n5, n28 |  |
| CA_n1-n3-n5-n78 | n1, n3, n5, n78 | No for n1-n78, n3-n78, n5-n78 |
| CA_n1-n3-n7-n8 | n1, n3, n7, n8 |  |
| CA_n1-n3-n7-n20 | n1, n3, n7, n20 |  |
| CA_n1-n3-n7-n26 | n1, n3, n7, n26 |  |
| CA_n1-n3-n7-n28 | n1, n3, n7, n28 |  |
| CA_n1-n3-n7-n38 | n1, n3, n7, n38 |  |
| CA_n1-n3-n7-n67 | n1, n3, n7, n67 |  |
| CA_n1-n3-n7-n75 | n1, n3, n7, n75 |  |
| CA_n1-n3-n7-n77 | n1, n3, n7, n77 |  |
| CA_n1-n3-n7-n79 | n1, n3, n7, n79 |  |
| CA_n1-n3-n7-n781 | n1, n3, n7, n78 |  |
| CA_n1-n3-n7-n105 | n1, n3, n7, n105 |  |
| CA_n1-n3-n8-n41 | n1, n3, n8, n41 |  |
| CA_n1-n3-n8-n77 | n1, n3, n8, n77 |  |
| CA_n1-n3-n8-n781 | n1, n3, n8, n78 |  |
| CA_n1-n3-n18-n28 | n1, n3, n18, n28 |  |
| CA_n1-n3-n18-n41 | n1, n3, n18, n41 |  |
| CA_n1-n3-n18-n77 | n1, n3, n18, n77 |  |
| CA_n1-n3-n20-n41 | n1, n3, n20, n41 |  |
| CA_n1-n3-n20-n67 | n1, n3, n20, n67 |  |
| CA_n1-n3-n20-n71 | n1, n3, n20, n71 |  |
| CA_n1-n3-n20-n75 | n1, n3, n20, n75 |  |
| CA_n1-n3-n20-n77 | n1, n3, n20, n77 |  |
| CA_n1-n3-n20-n78 | n1, n3, n20, n78 |  |
| CA_n1-n3-n26-n78 | n1, n3, n26, n78 |  |
| CA_n1-n3-n28-n38 | n1, n3, n28, n38 |  |
| CA_n1-n3-n28-n40 | n1, n3, n28, n40 |  |
| CA_n1-n3-n28-n41 | n1, n3, n28, n41 |  |
| CA_n1-n3-n28-n75 | n1, n3, n28, n75 |  |
| CA_n1-n3-n28-n771 | n1, n3, n28, n77 |  |
| CA_n1-n3-n28-n78 | n1, n3, n28, n78 |  |
| CA_n1-n3-n28-n791 | n1, n3, n28, n79 |  |
| CA_n1-n3-n40-n77 | n1, n3, n40, n77 |  |
| CA_n1-n3-n40-n105 | n1, n3, n40, n105 |  |
| CA_n1-n3-n41-n71 | n1, n3, n41, n71 |  |
| CA_n1-n3-n41-n77 | n1, n3, n41, n77 |  |
| CA_n1-n3-n41-n78 | n1, n3, n41, n78 |  |
| CA_n1-n3-n41-n79 | n1, n3, n41, n79 |  |
| CA_n1-n3-n67-n78 | n1, n3, n67, n78 |  |
| CA_n1-n3-n71-n77 | n1, n3, n71, n77 |  |
| CA_n1-n3-n71-n78 | n1, n3, n71, n78 |  |
| CA_n1-n3-n75-n78 | n1, n3, n75, n78 |  |
| CA_n1-n3-n77-n79 | n1, n3, n77, n79 |  |
| CA_n1-n5-n7-n40 | n1, n5, n7, n40 |  |
| CA_n1-n5-n7-n78 | n1, n5, n7, n78 |  |
| CA_n1-n5-n7-n105 | n1, n5, n7, n105 |  |
| CA_n1-n5-n28-n78 | n1, n5, n28, n78 |  |
| CA_n1-n5-n28-n79 | n1, n5, n28, n79 |  |
| CA_n1-n5-n40-n78 | n1, n5, n40, n78 |  |
| CA_n1-n5-n40-n105 | n1, n5, n40, n105 |  |
| CA_n1-n5-n78-n79 | n1, n5, n78, n79 |  |
| CA_n1-n5-n78-n105 | n1, n5, n78, n105 |  |
| CA_n1-n7-n8-n40 | n1, n7, n8, n40 |  |
| CA_n1-n7-n8-n781 | n1, n7, n8, n78 |  |
| CA_n1-n7-n20-n67 | n1, n7, n20, n67 |  |
| CA_n1-n7-n20-n75 | n1, n7, n20, n75 |  |
| CA_n1-n7-n20-n78 | n1, n7, n20, n78 |  |
| CA_n1-n7-n26-n78 | n1, n7, n26, n78 |  |
| CA_n1-n7-n28-n38 | n1, n7, n28, n38 |  |
| CA_n1-n7-n28-n75 | n1, n7, n28, n75 |  |
| CA_n1-n7-n28-n78 | n1, n7, n28, n78 |  |
| CA_n1-n7-n40-n78 | n1, n7, n40, n78 |  |
| CA_n1-n7-n40-n105 | n1, n7, n40, n105 |  |
| CA_n1-n7-n67-n78 | n1, n7, n67, n78 |  |
| CA_n1-n7-n75-n78 | n1, n7, n75, n78 |  |
| CA_n1-n7-n78-n105 | n1, n7, n78, n105 |  |
| CA_n1-n8-n40-n78 | n1, n8, n40, n78 |  |
| CA_n1-n8-n41-n78 | n1, n8, n41, n78 |  |
| CA_n1-n8-n78-n79 | n1, n8, n78, n79 |  |
| CA_n1-n18-n28-n41 | n1, n18, n28, n41 |  |
| CA_n1-n18-n28-n77 | n1, n18, n28, n77 |  |
| CA_n1-n18-n41-n77 | n1, n18, n41, n77 |  |
| CA_n1-n20-n41-n71 | n1, n20, n41, n71 |  |
| CA_n1-n20-n41-n77 | n1, n20, n41, n77 |  |
| CA_n1-n20-n41-n78 | n1, n20, n41, n78 |  |
| CA_n1-n20-n67-n78 | n1, n20, n67, n78 |  |
| CA_n1-n20-n71-n78 | n1, n20, n71, n78 |  |
| CA_n1-n20-n75-n78 | n1, n20, n75, n78 |  |
| CA_n1-n28-n38-n78 | n1, n28, n38, n78 |  |
| CA_n1-n28-n40-n77 | n1, n28, n40, n77 |  |
| CA_n1-n28-n40-n78 | n1, n28, n40, n78 |  |
| CA_n1-n28-n41-n77 | n1, n28, n41, n77 |  |
| CA_n1-n28-n41-n79 | n1, n28, n41, n79 |  |
| CA_n1-n28-n75-n78 | n1, n28, n75, n78 |  |
| CA_n1-n28-n77-n79 | n1, n28, n77, n79 |  |
| CA_n1-n28-n78-n79 | n1, n28, n78, n79 |  |
| CA_n1-n41-n71-n77 | n1, n41, n71, n77 |  |
| CA_n1-n41-n71-n78 | n1, n41, n71, n78 |  |
| CA_n1-n41-n77-n79 | n1, n41, n77, n79 |  |
| CA_n2-n5-n30-n66 | n2, n5, n30, n66 |  |
| CA_n2-n5-n30-n77 | n2, n5, n30, n77 |  |
| CA_n2-n5-n48-n66 | n2, n5, n48, n66 |  |
| CA_n2-n5-n48-n77 | n2, n5, n48, n77 |  |
| CA_n2-n5-n66-n77 | n2, n5, n66, n77 |  |
| CA_n2-n12-n30-n66 | n2, n12, n30, n66 |  |
| CA_n2-n12-n30-n77 | n2, n12, n30, n77 |  |
| CA_n2-n12-n66-n77 | n2, n12, n66, n77 |  |
| CA_n2-n14-n30-n66 | n2, n14, n30, n66 |  |
| CA_n2-n14-n30-n77 | n2, n14, n30, n77 |  |
| CA_n2-n14-n66-n77 | n2, n14, n66, n77 |  |
| CA_n2-n29-n30-n66 | n2, n29, n30, n66 |  |
| CA_n2-n29-n30-n77 | n2, n29, n30, n77 |  |
| CA_n2-n29-n66-n77 | n2, n29, n66, n77 |  |
| CA_n2-n30-n66-n77 | n2, n30, n66, n77 |  |
| CA_n2-n41-n66-n71 | n2, n41, n66, n71 |  |
| CA_n2-n48-n66-n77 | n2, n48, n66, n77 |  |
| CA_n2-n66-n71-n77 | n2, n66, n71, n77 |  |
| CA_n2-n66-n71-n78 | n2, n66, n71, n78 |  |
| CA_n3-n5-n7-n78 | n3, n5, n7, n78 |  |
| CA_n3-n5-n28-n78 | n3, n5, n28, n78 |  |
| CA_n3-n5-n28-n79 | n3, n5, n28, n79 |  |
| CA_n3-n7-n8-n781 | n3, n7, n8, n78 |  |
| CA_n3-n7-n20-n67 | n3, n7, n20, n67 |  |
| CA_n3-n7-n20-n75 | n3, n7, n20, n75 |  |
| CA_n3-n7-n20-n78 | n3, n7, n20, n78 |  |
| CA_n3-n7-n26-n78 | n3, n7, n26, n78 |  |
| CA_n3-n7-n28-n38 | n3, n7, n28, n38 |  |
| CA_n3-n7-n28-n75 | n3, n7, n28, n75 |  |
| CA_n3-n7-n28-n78 | n3, n7, n28, n78 |  |
| CA_n3-n7-n40-n105 | n3, n7, n40, n105 |  |
| CA_n3-n7-n67-n78 | n3, n7, n67, n78 |  |
| CA_n3-n7-n75-n78 | n3, n7, n75, n78 |  |
| CA_n3-n7-n78-n105 | n3, n7, n78, n105 |  |
| CA_n3-n8-n39-n41 | n3, n8, n39, n41 |  |
| CA_n3-n8-n39-n79 | n3, n8, n39, n79 |  |
| CA_n3-n8-n41-n78 | n3, n8, n41, n78 |  |
| CA_n3-n8-n41-n79 | n3, n8, n41, n79 |  |
| CA_n3-n39-n41-n79 | n3, n39, n41, n79 |  |
| CA_n3-n18-n28-n41 | n3, n18, n28, n41 |  |
| CA_n3-n18-n28-n77 | n3, n18, n28, n77 |  |
| CA_n3-n18-n41-n77 | n3, n18, n41, n77 |  |
| CA_n3-n20-n41-n71 | n3, n20, n41, n71 |  |
| CA_n3-n20-n41-n77 | n3, n20, n41, n77 |  |
| CA_n3-n20-n41-n78 | n3, n20, n41, n78 |  |
| CA_n3-n20-n67-n78 | n3, n20, n67, n78 |  |
| CA_n3-n20-n71-n78 | n3, n20, n71, n78 |  |
| CA_n3-n20-n75-n78 | n3, n20, n75, n78 |  |
| CA_n3-n28-n40-n77 | n3, n28, n40, n77 |  |
| CA_n3-n18-n41-n77 | n3, n18, n41, n77 |  |
| CA_n3-n28-n41-n77 | n3, n28, n41, n77 |  |
| CA_n3-n28-n41-n79 | n3, n28, n41, n79 |  |
| CA_n3-n28-n75-n78 | n3, n28, n75, n78 |  |
| CA_n3-n28-n77-n79 | n3, n28, n77, n79 |  |
| CA_n3-n28-n41-n78 | n3, n28, n41, n78 |  |
| CA_n3-n41-n71-n77 | n3, n41, n71, n77 |  |
| CA_n3-n41-n71-n78 | n3, n41, n71, n78 |  |
| CA_n3-n41-n77-n79 | n3, n41, n77, n79 |  |
| CA_n5-n7-n40-n78 | n5, n7, n40, n78 |  |
| CA_n5-n7-n40-n105 | n5, n7, n40, n105 |  |
| CA_n5-n7-n66-n77 | n5, n7, n66, n77 |  |
| CA_n5-n7-n78-n105 | n5, n7, n78, n105 |  |
| CA_n5-n14-n30-n66 | n5, n14, n30, n66 |  |
| CA_n5-n25-n29-n66 | n5, n25, n29, n66 |  |
| CA_n5-n25-n66-n77 | n5, n25, n66, n77 |  |
| CA_n5-n25-n66-n78 | n5, n25, n66, n78 |  |
| CA_n5-n28-n78-n79 | n5, n28, n78, n79 |  |
| CA_n5-n30-n66-n77 | n5, n30, n66, n77 |  |
| CA_n5-n40-n78-n105 | n5, n40, n78, n105 |  |
| CA_n5-n48-n66-n77 | n5, n48, n66, n77 |  |
| CA_n7-n8-n40-n78 | n7, n8, n40, n78 |  |
| CA_n7-n12-n25-n66 | n7, n12, n25, n66 |  |
| CA_n7-n20-n67-n78 | n7, n20, n67, n78 |  |
| CA_n7-n20-n75-n78 | n7, n20, n75, n78 |  |
| CA_n7-n25-n29-n77 | n7, n25, n29, n77 |  |
| CA_n7-n25-n66-n71 | n7, n25, n66, n71 |  |
| CA_n7-n25-n66-n77 | n7, n25, n66, n77 |  |
| CA_n7-n25-n66-n78 | n7, n25, n66, n78 |  |
| CA_n7-n28-n75-n78 | n7, n28, n75, n78 |  |
| CA_n7-n29-n66-n77 | n7, n29, n66, n77 |  |
| CA_n7-n40-n78-n105 | n7, n40, n78, n105 |  |
| CA_n7-n66-n71-n77 | n7, n66, n71, n77 |  |
| CA_n8-n20-n28-n75 | n8, n20, n28, n75 |  |
| CA_n8-n39-n41-n79 | n8, n39, n41, n79 |  |
| CA_n12-n30-n66-n77 | n12, n30, n66, n77 |  |
| CA_n13-n25-n66-n77 | n13, n25, n66, n77 |  |
| CA_n14-n30-n66-n77 | n14, n30, n66, n77 |  |
| CA_n18-n28-n41-n77 | n18, n28, n41, n77 |  |
| CA_n20-n41-n71-n78 | n20, n41, n71, n78 |  |
| CA_n25-n29-n66-n77 | n25, n29, n66, n77 |  |
| CA_n25-n38-n66-n78 | n25, n38, n66, n78 |  |
| CA_n25-n41-n66-n71 | n25, n41, n66, n71 |  |
| CA_n25-n41-n66-n77 | n25, n41, n66, n77 |  |
| CA_n25-n41-n66-n78 | n25, n41, n66, n78 |  |
| CA_n25-n41-n66-n85 | n25, n41, n66, n85 |  |
| CA_n25-n41-n71-n77 | n25, n41, n71, n77 |  |
| CA_n25-n41-n71-n78 | n25, n41, n71, n78 |  |
| CA_n25-n41-n71-n85 | n25, n41, n71, n85 |  |
| CA_n25-n41-n77-n85 | n25, n41, n77, n85 |  |
| CA_n25-n66-n71-n77 | n25, n66, n71, n77 |  |
| CA_n25-n66-n71-n78 | n25, n66, n71, n78 |  |
| CA_n25-n66-n71-n85 | n25, n66, n71, n85 |  |
| CA_n25-n66-n77-n85 | n25, n66, n77, n85 |  |
| CA_n28-n40-n71-n77 | n28, n40, n71, n77 |  |
| CA_n28-n41-n77-n79 | n28, n41, n77, n79 |  |
| CA_n29-n30-n66-n77 | n29, n30, n66, n77 |  |
| CA_n29-n66-n70-n71 | n29, n66, n70, n71 |  |
| CA_n41-n66-n70-n78 | n41, n66, n70, n78 |  |
| CA_n41-n66-n71-n77 | n41, n66, n71, n77 |  |
| CA_n41-n66-n71-n78 | n41, n66, n71, n78 |  |
| CA_n41-n66-n71-n85 | n41, n66, n71, n85 |  |
| CA_n41-n66-n77-n85 | n41, n66, n77, n85 |  |
| CA_n48-n66-n70-n71 | n48, n66, n70, n71 |  |
| CA_n48-n66-n70-n77 | n48, n66, n70, n77 |  |
| CA_n48-n66-n71-n77 | n48, n66, n71, n77 |  |
| CA_n48-n70-n71-n77 | n48, n70, n71, n77 |  |
| NOTE 1: Applicable for UE supporting inter-band carrier aggregation with mandatory simultaneous Rx/Tx capability.NOTE 2: Applicable when dynamic Tx switching is triggered across any 2 UL bands among the configured 2, 3 or 4 UL bands. The DL interruption requirement is specified in clause 8.2.2.2 of 38.133 [3]. The nX-nY in the requirement of “No for nX-nY” refers to the two UL Bands nX and nY that are involved in dynamic Tx switching. |  |  |

#### 5.2A.2.4 Inter-band CA (five bands)

Table 5.2A.2.4-1: Inter-band CA operating bands involving FR1 (five bands)

| NR CA Band | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n1-n3-n5-n7-n78 | n1, n3, n5, n7, n78 |
| CA_n1-n3-n5-n28-n78 | n1, n3, n5, n28, n78 |
| CA_n1-n3-n7-n8-n781 | n1, n3, n7, n8, n78 |
| CA_n1-n3-n7-n20-n67 | n1, n3, n7, n20, n67 |
| CA_n1-n3-n7-n20-n75 | n1, n3, n7, n20, n75 |
| CA_n1-n3-n7-n20-n78 | n1, n3, n7, n20, n78 |
| CA_n1-n3-n7-n26-n78 | n1, n3, n7, n26, n78 |
| CA_n1-n3-n7-n28-n38 | n1, n3, n7, n28, n38 |
| CA_n1-n3-n7-n28-n75 | n1, n3, n7, n28, n75 |
| CA_n1-n3-n7-n28-n78 | n1, n3, n7, n28, n78 |
| CA_n1-n3-n7-n40-n78 | n1, n3, n7, n40, n78 |
| CA_n1-n3-n7-n40-n105 | n1, n3, n7, n40, n105 |
| CA_n1-n3-n7-n67-n78 | n1, n3, n7, n67, n78 |
| CA_n1-n3-n7-n75-n78 | n1, n3, n7, n75, n78 |
| CA_n1-n3-n7-n78-n105 | n1, n3, n7, n78, n105 |
| CA_n1-n3-n8-n41-n78 | n1, n3, n8, n41, n78 |
| CA_n1-n3-n20-n41-n71 | n1, n3, n20, n41, n71 |
| CA_n1-n3-n20-n41-n77 | n1, n3, n20, n41, n77 |
| CA_n1-n3-n20-n41-n78 | n1, n3, n20, n41, n78 |
| CA_n1-n3-n20-n71-n78 | n1, n3, n20, n71, n78 |
| CA_n1-n3-n20-n75-n78 | n1, n3, n20, n75, n78 |
| CA_n1-n3-n28-n40-n77 | n1, n3, n28, n40, n77 |
| CA_n1-n3-n28-n41-n77 | n1, n3, n28, n41, n77 |
| CA_n1-n3-n28-n41-n79 | n1, n3, n28, n41, n79 |
| CA_n1-n3-n28-n75-n78 | n1, n3, n28, n75, n78 |
| CA_n1-n3-n28-n77-n79 | n1, n3, n28, n77, n79 |
| CA_n1-n3-n40-n78-n105 | n1, n3, n40, n78, n105 |
| CA_n1-n3-n41-n71-n77 | n1, n3, n41, n71, n77 |
| CA_n1-n3-n41-n71-n78 | n1, n3, n41, n71, n78 |
| CA_n1-n3-n41-n77-n79 | n1, n3, n41, n77, n79 |
| CA_n1-n5-n7-n40-n78 | n1, n5, n7, n40, n78 |
| CA_n1-n5-n7-n40-n105 | n1, n5, n7, n40, n105 |
| CA_n1-n5-n7-n78-n105 | n1, n5, n7, n78, n105 |
| CA_n1-n20-n41-n71-n78 | n1, n20, n41, n71, n78 |
| CA_n1-n5-n28-n78-n79 | n1, n5, n28, n78, n79 |
| CA_n1-n5-n40-n78-n105 | n1, n5, n40, n78, n105 |
| CA_n1-n7-n20-n67-n78 | n1, n7, n20, n67, n78 |
| CA_n1-n7-n20-n75-n78 | n1, n7, n20, n75, n78 |
| CA_n1-n7-n28-n75-n78 | n1, n7, n28, n75, n78 |
| CA_n1-n7-n40-n78-n105 | n1, n7, n40, n78, n105 |
| CA_n1-n28-n41-n77-n79 | n1, n28, n41, n77, n79 |
| CA_n2-n5-n30-n66-n77 | n2, n5, n30, n66, n77 |
| CA_n2-n5-n48-n66-n77 | n2, n5, n48, n66, n77 |
| CA_n2-n12-n30-n66-n77 | n2, n12, n30, n66, n77 |
| CA_n2-n14-n30-n66-n77 | n2, n14, n30, n66, n77 |
| CA_n2-n29-n30-n66-n77 | n2, n29, n30, n66, n77 |
| CA_n3-n7-n20-n67-n78 | n3, n7, n20, n67, n78 |
| CA_n3-n7-n20-n75-n78 | n3, n7, n20, n75, n78 |
| CA_n3-n7-n40-n78-n105 | n3, n7, n40, n78, n105 |
| CA_n3-n8-n39-n41-n79 | n3, n8, n39, n41, n79 |
| CA_n3-n20-n41-n71-n78 | n3, n20, n41, n71, n78 |
| CA_n3-n28-n41-n77-n79 | n3, n28, n41, n77, n79 |
| CA_n5-n7-n40-n78-n105 | n5, n7, n40, n78, n105 |
| NOTE 1: Applicable for UE supporting inter-band carrier aggregation with mandatory simultaneous Rx/Tx capability. |  |

#### 5.2A.2.5 Inter-band CA (six bands)

Table 5.2A.2.5-1: Inter-band CA operating bands involving FR1 (six bands)

| NR CA Band | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n1-n3-n7-n28-n38-n78 | n1, n3, n7, n28, n38, n78 |
| CA_n1-n3-n7-n40-n78-n105 | n1, n3, n7, n40, n78, n105 |
| CA_n1-n3-n20-n41-n71-n78 | n1, n3, n20, n41, n71, n78 |
| CA_n1-n5-n7-n40-n78-n105 | n1, n5, n7, n40, n78, n105 |

## 5.2B Operating bands for DC

The operating bands are specified in clause 5.5B for operation with NR dual connectivity configured, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a band combination, the mandatory simultaneous Rx/Tx capability also applies for the band combination when the applicable band combination is a subset of a higher order band combination.

## 5.2C Operating band combination for SUL

NR operation is designed to operate in the operating band combination defined in Table 5.2C-1, Table 5.2C-2, Table 5.2C-3 and Table 5.2C-4, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a band combination, when the applicable lower order band combination is a band pair in a higher order band combination, the mandatory simultaneous Rx/Tx capability also applies for the band pair in the higher order band combination.

Table 5.2C-1: Operating band combination for SUL in FR1

| NR Band combination for SUL | NR Band(Table 5.2-1) |
| --- | --- |
| SUL_n1-n802 | n1, n80 |
| SUL_n1-n812 | n1, n81 |
| SUL_n1-n892 | n1, n89 |
| SUL_n3-n842 | n3, n84 |
| SUL_n5-n842 | n5, n84 |
| SUL_n8-n842 | n8, n84 |
| SUL_n24-n992 | n24, n99 |
| SUL_n41-n802 | n41, n80 |
| SUL_n41-n812 | n41, n81 |
| SUL_n41-n832 | n41, n83 |
| SUL_n41-n952 | n41, n95 |
| SUL_n41-n972 | n41, n97 |
| SUL_n41-n982 | n41, n98 |
| SUL_n41-n992 | n41, n99 |
| SUL_n48-n992 | n48, n99 |
| SUL_n77-n802 | n77, n80 |
| SUL_n77-n842 | n77, n84 |
| SUL_n77-n992 | n77, n99 |
| SUL_n78-n802 | n78, n80 |
| SUL_n78-n812 | n78, n81 |
| SUL_n78-n822 | n78, n82 |
| SUL_n78-n832 | n78, n83 |
| SUL_n78-n842 | n78, n84 |
| SUL_n78-n862 | n78, n86 |
| SUL_n78-n892 | n78, n89 |
| SUL_n79-n802 | n79, n80 |
| SUL_n79-n812 | n79, n81 |
| SUL_n79-n832 | n79, n83 |
| SUL_n79-n842 | n79, n84 |
| SUL_n79-n952 | n79, n95 |
| SUL_n79-n972 | n79, n97 |
| SUL_n79-n982 | n79, n98 |
| NOTE 1: If a UE is configured with both NR UL and NR SUL carriers in a cell, the switching time between NR UL carrier and NR SUL carrier is according to either uplinkTxSwitchingPeriod-r16 parameter within UE capability IE ULTxSwitchingBandPair-r16 if reported, or switchingPeriodFor1T-r18 parameter within UE capability IE ULTxSwitchingBandPair-r18 or ULTxSwitchingBandPair-v1840 if reported, otherwise 0 us.NOTE 2: For UE supporting SUL band combination simultaneous Rx/Tx capability is mandatory. |  |

Table 5.2C-2: Operating SUL band combination with intra-band non-contiguous CA in FR1

| NR Band combination for SUL | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n41(*)-n992 | n41, n99 |
| CA_n48(*)-n992 | n48, n99 |
| CA_n77(*)-n992 | n77, n99 |
| CA_n78(*)-n862 | n78, n86 |
| NOTE 1: If a UE is configured with both NR UL and NR SUL carriers in a cell, the switching time between NR UL carrier and NR SUL carrier is according to either uplinkTxSwitchingPeriod-r16 parameter within UE capability IE ULTxSwitchingBandPair-r16 if reported, or switchingPeriodFor1T-r18 parameter within UE capability IE ULTxSwitchingBandPair-r18 or ULTxSwitchingBandPair-v1840 if reported, otherwise 0 us.NOTE 2: For UE supporting SUL band combination simultaneous Rx/Tx capability is mandatory.NOTE 3: The notation CA_nX(*) in this table indicates intra-band non-contiguous CA for band nX. The configurations for each band are in table 5.5C-2. |  |

Table 5.2C-3: Operating SUL band combination with intra-band contiguous CA in FR1

| NR Band combination for SUL | NR Band(Table 5.2-1) |  |
| --- | --- | --- |
| CA_n41-n80 | n41, n80 |  |
| CA_n41-n81 | n41, n81 |  |
| CA_n41-n83 | n41, n83 |  |
| CA_n41-n95 | n41, n95 |  |
| CA_n41-n97 | n41, n97 |  |
| CA_n41-n98 | n41, n98 |  |
| CA_n78-n80 | n78, n80 |  |
| CA_n78-n81 | n78, n81 |  |
| CA_n78-n84 | n78, n84 |  |
| CA_n78-n89 | n78, n89 |  |
| CA_n79-n80 | n79, n80 |  |
| CA_n79-n83 | n79, n83 |  |
| CA_n79-n95 | n79, n95 |  |
| CA_n79-n97 | n79, n97 |  |
| CA_n79-n98 | n79, n98 |  |
| NOTE 1: If a UE is configured with both NR UL and NR SUL carriers in a cell, the switching time between NR UL carrier and NR SUL carrier is according to either uplinkTxSwitchingPeriod-r16 parameter within UE capability IE ULTxSwitchingBandPair-r16 if reported, or switchingPeriodFor1T-r18 parameter within UE capability IE ULTxSwitchingBandPair-r18 or ULTxSwitchingBandPair-v1840 if reported, otherwise 0 us.NOTE 2: For UE supporting SUL band combination simultaneous Rx/Tx capability is mandatory. |  |  |

Table 5.2C-4: Operating SUL band combination with inter-band CA in FR1

| NR Band combination for SUL | NR Band(Table 5.2-1) |
| --- | --- |
| CA_n1_n78-n80 | n1, n78, n80 |
| CA_n1_n78-n81 | n1, n78, n81 |
| CA_n1_n78-n84 | n1, n78, n84 |
| CA_n1_n78-n89 | n1, n78, n89 |
| CA_n3_n41-n80 | n3, n41, n80 |
| CA_n3_n78-n80 | n3, n78, n80 |
| CA_n3_n78-n84 | n3, n78, n84 |
| CA_n3_n79-n80 | n3, n79, n80 |
| CA_n5_n78-n84 | n5, n78, n84 |
| CA_n8_n78-n81 | n8, n78, n81 |
| CA_n8_n78-n84 | n8, n78, n84 |
| CA_n28_n41-n834 | n28, n41, n83 |
| CA_n28_n79-n834 | n28, n79, n83 |
| CA_n41_n79-n80 | n41, n79, n80 |
| CA_n41_n79-n83 | n41, n79, n83 |
| CA_n41_n79-n95 | n41, n79, n95 |
| CA_n41_n79-n97 | n41, n79, n97 |
| CA_n41_n79-n98 | n41, n79, n98 |
| CA_n78_n1-n80 | n1, n78, n80 |
| CA_n78_n1-n81 | n1, n78, n81 |
| CA_n78_n1-n89 | n1, n78, n89 |
| CA_n78_n3-n84 | n3, n78, n84 |
| CA_n78_n5-n84 | n5, n78, n84 |
| CA_n78_n8-n84 | n8, n78, n84 |
| CA_n79_n41-n80 | n41, n79, n80 |
| CA_n79_n41-n83 | n41, n79, n83 |
| CA_n79_n41-n95 | n41, n79, n95 |
| CA_n79_n41-n97 | n41, n79, n97 |
| CA_n79_n41-n98 | n41, n79, n98 |
| CA_n1-n3_n78-n80 | n1, n3, n78, n80 |
| CA_n1-n3_n78-n84 | n1, n3, n78, n84 |
| CA_n28-n41_n79-n834 | n28, n41, n79, n83 |
| CA_n28-n79_n41-n834 | n28, n41, n79, n83 |
| CA_n41-n95_n79-n98 | n41, n95, n79, n98 |
| CA_n41-n98_n79-n95 | n41, n98, n79, n95 |
| CA_n41-n83_n79-n95 | n41, n79, n83, n95 |
| CA_n41-n83_n79-n98 | n41, n79, n83, n98 |
| CA_n41_n95-n98 | n41, n95, n98 |
| CA_n78_n80-n84 | n78, n80, n84 |
| CA_n78_n81-n84 | n78, n81, n84 |
| CA_n78_n84-n89 | n78, n84, n89 |
| NOTE 1: If a UE is configured with a single cell consisting of a NR UL carrier and a corresponding NR SUL carrier, the switching time between NR UL carrier and the corresponding NR SUL carrier is according to either uplinkTxSwitchingPeriod-r16 parameter within UE capability IE ULTxSwitchingBandPair-r16 if reported, or switchingPeriodFor1T-r18 parameter within UE capability IE ULTxSwitchingBandPair-r18 or ULTxSwitchingBandPair-v1840 if reported, otherwise 0 us.NOTE 2: For UE supporting SUL band combination simultaneous Rx/Tx capability is mandatory.NOTE 3: Unless otherwise stated, the SUL channel bandwidth is same with the DL bandwidth of its associated NR band that shares the same UL frequency range.NOTE 4: Channels for both n28 and n83 are confined either to lowest 30MHz or to highest 30MHz of the band. |  |

## 5.2D Operating bands for UL MIMO

NR is designed to support UL MIMO where all of the operating bands are in FR1 defined in Table 5.2D-1.

Table 5.2D-1: NR operating bands for UL MIMO in FR1

| NR operating band |
| --- |
| n1 |
| n2 |
| n3 |
| n5 |
| n7 |
| n8 |
| n13 |
| n24 |
| n25 |
| n26 |
| n28 |
| n301 |
| n34 |
| n38 |
| n39 |
| n40 |
| n41 |
| n46 |
| n48 |
| n66 |
| n70 |
| n71 |
| n77 |
| n78 |
| n79 |
| n80 |
| n81 |
| n83 |
| n84 |
| n85 |
| n86 |
| n95 |
| n96 |
| n97 |
| n98 |
| n99 |
| n100 |
| n101 |
| n102 |
| n104 |
| n105 |
| NOTE 1: Uplink transmission is not allowed at this band for UE with external vehicle-mounted antennas.NOTE 2: Void. |

## 5.2E Operating band for V2X

### 5.2E.1 V2X operating bands

NR V2X is designed to operate in the operating bands in FR1 defined in Table5.2E.1-1.

Table 5.2E.1-1 V2X operating bands in FR1

| V2X Operating Band | Sidelink (SL) Transmission operating band |  |  | Sidelink (SL)  Reception operating band |  |  | Duplex Mode | Interface |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | FUL_low   –  FUL_high |  |  | FDL_low  –  FDL_high |  |  |  |  |
| n142 | 788 MHz | - | 798 MHz | 788 MHz | - | 798 MHz | HD | PC5 |
| n381 | 2570 MHz | - | 2620 MHz | 2570 MHz | - | 2620 MHz | HD | PC5 |
| n47 | 5855 MHz | - | 5925 MHz | 5855 MHz | - | 5925 MHz | HD | PC5 |
| n79 | 4400 MHz | - | 5000 MHz | 4400 MHz | - | 5000 MHz | HD | PC5 |
| NOTE 1: When this band is used for V2X SL service, the band is exclusively used for NR V2X in particular region.NOTE 2: When this band is used for public safety service, the NR band is operated with both in-coverage scenarios and out-of-coverage scenarios. |  |  |  |  |  |  |  |  |

### 5.2E.1A Sidelink CA operating bands

For NR sidelink intra-band CA operation is designed to operate in the operating bands in FR1 defined in Table 5.2E.1A-1 and Table 5.2E.1A-2.

Table 5.2E.1A-1 Intra-band contiguous SL CA operating bands in FR1

| NR SL CA Band | NR Band | Interface |
| --- | --- | --- |
| SLCA_n47 | n47 | PC5 |

Table 5.2E.1A-2 Intra-band non-contiguous SL CA operating bands in FR1

| NR SL CA Band | NR Band | Interface |
| --- | --- | --- |
| SLCA_n47(*) | n47 | PC5 |
| NOTE 1: The notation SLCA_nX(*) in this table indicates SL intra-band non-contiguous CA for band nX. The configurations for each band are in 5.5E.1A.2. |  |  |

### 5.2E.1F Operating bands for Sidelink Unlicensed

NR Sidelink is designed to operate in the unlicensed operating bands in FR1 defined in Table 5.2E.1F-1.

Table 5.2E.1F-1. NR SL-U operating bands in FR1

| NR SL-U operating band | Sidelink (SL) Transmission operating band | Sidelink (SL)  Reception operating band | Duplex Mode | Interface |
| --- | --- | --- | --- | --- |
|  | FUL_low   –  FUL_high | FDL_low  –  FDL_high |  |  |
| n461 | 5150 MHz – 5925 MHz | 5150 MHz – 5925 MHz | HD | PC5 |
| n961 | 5925 MHz – 7125 MHz | 5925 MHz – 7125 MHz | HD | PC5 |
| n1021 | 5925 MHz – 6425 MHz | 5925 MHz – 6425 MHz | HD | PC5 |
| NOTE 1: Direct connection between client devices and between vehicular devices in the shared spectrum bands or portions of the shared spectrum bands is subject to country-specific conditions and can be prohibited per region-specific regulatory rules, e.g., in USA and Canada. |  |  |  |  |

### 5.2E.2 V2X operating bands for concurrent operation

NR V2X operation is designed to operate concurrent with NR uplink/downlink on the operating bands combinations listed in Table 5.2E.2-1 and Table 5.2E.2-2.

Table 5.2E.2-1 Inter-band concurrent V2X operating bands

| V2X concurrent operating Band | NR or V2X Operating Band | Interface |
| --- | --- | --- |
| V2X_n1-n47 | n1 | Uu |
|  | n47 | PC5 |
| V2X_n3-n47 | n3 | Uu |
|  | n47 | PC5 |
| V2X_n5-n47 | n5 | Uu |
|  | n47 | PC5 |
| V2X_n8-n47 | n8 | Uu |
|  | n47 | PC5 |
| V2X_n34-n47 | n34 | Uu |
|  | n47 | PC5 |
| V2X_n39-n47 | n39 | Uu |
|  | n47 | PC5 |
| V2X_n40-n47 | n40 | Uu |
|  | n47 | PC5 |
| V2X_n41-n47 | n41 | Uu |
|  | n47 | PC5 |
| V2X_n71-n47 | n71 | Uu |
|  | n47 | PC5 |
| V2X_n78-n47 | n78 | Uu |
|  | n47 | PC5 |
| V2X_n79-n47 | n79 | Uu |
|  | n47 | PC5 |

Table 5.2E.2-2 Intra-band concurrent V2X operating bands

| V2X concurrent operating Band | NR or V2X Operating Band | Interface |
| --- | --- | --- |
| V2X_n79-n79 | n79 | Uu |
|  | n79 | PC5 |

### 5.2E.2F Operating bands for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, NR sidelink in the unlicensed operating band is designed to operate concurrently with NR uplink/downlink on the operating band combinations are listed in Table 5.2E.2F-1.

Table 5.2E.2F-1 SL-U Inter-band concurrent operating bands

| NR SL inter-band concurrent operating Band | NR Operating Band | Interface |
| --- | --- | --- |
| SL_n78-n46 | n78 | Uu |
|  | n46 | PC5 |

## 5.2J Operating band for ATG

### 5.2J.1 General

NR operating bands n1, n3, n34, n39, n41, n78, n79, which are defined in Table 5.2-1, can be applied for ATG operation.

### 5.2J.1A Operating band for ATG CA

NR carrier aggregation operating bands defined in Table 5.2J.1A.1-1 and Table 5.2J.1A.2-1, can be applied for ATG CA operation.

#### 5.2J.1A.1 Operating band for ATG intra-band CA

Table 5.2A.1-1: ATG intra-band contiguous CA operating bands

| NR ATG CA Band | NR ATG Band(Table 5.2-1) |
| --- | --- |
| CA_n79 | n79 |
| NOTE: The minimum requirements only apply for non simultaneous Tx/Rx between all carriers for TDD combinations. |  |

#### 5.2J.1A.2 Operating band for ATG inter-band CA

Table 5.2J.1A.2-1: ATG inter-band CA operating bands

| NR CA Band | NR Band(Table 5.2-1) | DL interruption allowed (Note 1) |
| --- | --- | --- |
| CA_n3-n39 | n3, n39 |  |
| NOTE 1: Applicable when dynamic Tx switching is conducted. The DL interruption requirement is specified in clause 8.2.2.2.10 of 38.133 [13]. |  |  |

### 5.2J.1D Operating band for ATG UL MIMO

NR operating bands in Table 5.2J.1D-1 to support UL MIMO, can be applied for ATG UL MIMO operation.

Table 5.2J.1D-1: NR operating bands for UL MIMO in FR1

| NR operating band |
| --- |
| n1 |
| n3 |
| n34 |
| n38 |
| n39 |
| n41 |
| n78 |
| n79 |

## 5.2K Operating bands for Aerial UE

Aerial UE is designed to operate in NR operating bands as defined in Table 5.2-1, following applicable spectrum regulations, e.g. ECC Decision (22)07 [18] for CEPT countries.

## 5.2M Operating bands for LP-WUS/WUR

LP-WUS/WUR is designed to operate in the operating bands defined in Table 5.2-1, excluding bands n46, n47, n96, n102 and SDL bands.

## 5.3 UE channel bandwidth

### 5.3.1 General

The UE channel bandwidth supports a single NR RF carrier in the uplink or downlink at the UE. From a BS perspective, different UE channel bandwidths may be supported within the same spectrum for transmitting to and receiving from UEs connected to the BS. Transmission of multiple carriers to the same UE (CA) or multiple carriers to different UEs within the BS channel bandwidth can be supported.

From a UE perspective, the UE is configured with one or more BWP / carriers, each with its own UE channel bandwidth. The UE does not need to be aware of the BS channel bandwidth or how the BS allocates bandwidth to different UEs.

The placement of the UE channel bandwidth for each UE carrier is flexible but can only be completely within the BS channel bandwidth.

The relationship between the channel bandwidth, the guardband and the maximum transmission bandwidth configuration is shown in Figure 5.3.1-1.

Figure 5.3.1-1: Definition of the channel bandwidth and the maximum transmission bandwidth configuration for one NR channel

### 5.3.2 Maximum transmission bandwidth configuration

The maximum transmission bandwidth configuration NRB for each UE channel bandwidth and subcarrier spacing is specified in Table 5.3.2-1.

Table 5.3.2-1: Maximum transmission bandwidth configuration NRB

| SCS (kHz) | 3MHz | 5MHz | 7MHz | 10MHz | 15MHz | 20MHz | 25MHz | 30MHz | 35MHz | 40 MHz | 45MHz | 50MHz | 60MHz | 70MHz | 80MHz | 90MHz | 100MHz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB | NRB |
| 15 | 15 | 25 | 35 | 52 | 79 | 106 | 133 | 160 | 188 | 216 | 242 | 270 | N/A | N/A | N/A | N/A | N/A |
| 30 | N/A | 11 | N/A | 24 | 38 | 51 | 65 | 78 | 92 | 106 | 119 | 133 | 162 | 189 | 217 | 245 | 273 |
| 60 | N/A | N/A | N/A | 11 | 18 | 24 | 31 | 38 | 44 | 51 | 58 | 65 | 79 | 93 | 107 | 121 | 135 |

### 5.3.3 Minimum guardband and transmission bandwidth configuration

The minimum guardband for each UE channel bandwidth and SCS is specified in Table 5.3.3-1,

Table 5.3.3-1: Minimum guardband for each UE channel bandwidth and SCS (kHz)

| SCS (kHz) | 3MHz | 5MHz | 7MHz | 10MHz | 15MHz | 20MHz | 25MHz | 30MHz | 35MHz | 40MHz | 45MHz | 50MHz | 60MHz | 70MHz | 80MHz | 90MHz | 100MHz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 142.5 | 242.5 | 342.5 | 312.5 | 382.5 | 452.5 | 522.5 | 592.5 | 572.5 | 552.5 | 712.5 | 692.5 | N/A | N/A | N/A | N/A | N/A |
| 30 | N/A | 505 | N/A | 665 | 645 | 805 | 785 | 945 | 925 | 905 | 1065 | 1045 | 825 | 965 | 925 | 885 | 845 |
| 60 | N/A | N/A | N/A | 1010 | 990 | 1330 | 1310 | 1290 | 1630 | 1610 | 1590 | 1570 | 1530 | 1490 | 1450 | 1410 | 1370 |

NOTE: The minimum guardbands have been calculated using the following equation: GBChannel = (BWChannel x 1000 (kHz) - NRB x SCS x 12) / 2 - SCS/2, where NRB are from Table 5.3.2-1 and GBChannel expressed in kHz.

Figure 5.3.3-1: Void

The number of RBs configured in any channel bandwidth shall ensure that the minimum guardband specified in this clause is met.

Figure 5.3.3-2: UE PRB utilization

In the case that multiple numerologies are multiplexed in the same symbol due to BS transmission of SSB, the minimum guardband on each side of the carrier is the guardband applied at the configured channel bandwidth for the numerology that is received immediately adjacent to the guard.

If multiple numerologies are multiplexed in the same symbol and the UE channel bandwidth is >50 MHz, the minimum guardband applied adjacent to 15 kHz SCS shall be the same as the minimum guardband defined for 30 kHz SCS for the same UE channel bandwidth.

Figure 5.3.3-3 Guard band definition when transmitting multiple numerologies

NOTE: Figure 5.3.3-3 is not intended to imply the size of any guard between the two numerologies. Inter-numerology guard band within the carrier is implementation dependent.

For a UE supporting wideband operation, the nominal intra-cell guard bands and the corresponding sizes of the RB sets separated by the said guard bands are as specified in Table 5.3.3-2 for each UE channel bandwidth and sub-carrier spacing for the downlink, uplink and sidelink. The nominal intra-cell guard bands in Table 5.3.3-2 are applicable when the respective IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List for the uplink, downlink and sidelink are not provided, as specified in [10] clause 7.

Table 5.3.3-2: Nominal intra-cell guard bands for wideband operation

| SCS(kHz) | 40 MHz | 60 MHz | 80 MHz | 100 MHz |
| --- | --- | --- | --- | --- |
| 15 | 105-6-105(216) | N/A | N/A | N/A |
| 30 | 50-6-50(106) | 50-6-50-6-50(162) | 50-6-50-5-50-6-50(217) | 50-6-50-6-49-6-50-6-50(273) |
| 60 | 23-5-23(51) | 23-5-23-5-23(79) | 23-5-23-5-23-5-23(107) | 23-5-23-5-23-5-23-5-23(135) |
| NOTE 1: The intra-cell guard band is denoted TBW0-GB0-…-GBN_RBset-2-TBWN_RBset-1 for N_RBset > 1 number of RB-sets with TBWr the maximum transmission bandwidth (PRB) of RB-set r and GBr the guard band (PRB) above the upper edge of RB-set r. The RB-set 0 is starting at the first common resource block (CRB) of the carrier as indicated by offsetToCarrier. The total transmission bandwidth configuration (size of resource grid) including guard bands is given in between parentheses. |  |  |  |  |

For a UE that supports shared spectrum channel access, there are no uplink, downlink or sidelink intra-cell guard bands for operation with 10 MHz and 20 MHz channel bandwidths; the maximum transmission bandwidth configurations for these channel bandwidths are in accordance with clause 5.3.2.

For each UE channel bandwidth and sub-carrier spacing given by Table 5.3.3-2, the maximum transmission bandwidth configuration of the carrier including intra-cell guard bands, if configured for the uplink, downlink and sidelink by the respective IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List, and corresponding RB-set(s) shall be in accordance with clause 5.3.2 with a minimum inter-cell guard band of the UE channel bandwidth as specified in Table 5.3.3-1 for the uplink, downlink and sidelink. Minimum requirements specified for wideband operation in Clause 6 and Clause 7 also apply for intra-cell guard bands larger than the nominal sizes in Table 5.3.3-2 as listed in Table 5.3.3-3 for each sub-carrier spacing; each guard band in order of CRB index must be larger than or equal to the corresponding nominal guard band specified in Table 5.3.3-2 for each channel bandwidth.

Table 5.3.3-3: Applicable intra-cell guard bands for wideband operation

| Parameter | Unit | SCS |  |
| --- | --- | --- | --- |
|  |  | 15 kHz | 30 kHz |
| Intra-cell guard band (size) | PRB | 6,7 | 5,6,7 |
| Transmission bandwidth (size) of RB-set | PRB | 104,105 | 49,50,51 |

If the UE is configured with zero width intra-cell guard bands for the uplink, downlink and sidelink by the IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List on a carrier greater than 20 MHz, the maximum transmission bandwidth configuration for the uplink, downlink and sidelink shall be in accordance with clause 5.3.2 with a minimum inter-cell guard band of the UE channel bandwidth as specified in Table 5.3.3-1.

### 5.3.4 RB alignment

For each numerology, its common resource blocks are specified in Clause 4.4.4.3 in TS 38.211 [6], and the starting point of its transmission bandwidth configuration on the common resource block grid for a given channel bandwidth is indicated by an offset to "Reference point A" in the unit of the numerology. The UE transmission bandwidth configuration is indicated by the higher layer parameter carrierBandwidth [7] and will fulfil the minimum UE guardband requirement specified in Clause 5.3.3.

### 5.3.5 UE channel bandwidth per operating band

The requirements in this specification apply to the combination of channel bandwidths, SCS and operating bands shown in Table 5.3.5-1. The transmission bandwidth configuration in Table 5.3.2-1 shall be supported for each of the specified channel bandwidths. The channel bandwidths are specified for both the TX and RX path.

Table 5.3.5-1 Channel bandwidths for each NR band

| NR Band | SCS (kHz) | UE Channel bandwidth (MHz) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 3 | 5 | 7 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |
| n1 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
| n2 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
| n3 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
| n5 | 15 | 34 | 5 | 74 | 10 | 15 | 20 | 253 |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 253 |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n7 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  | 50 |  |  |  |  |  |
| n8 | 15 |  | 5 |  | 10 | 15 | 20 | 253 | 303 | 353 |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 253 | 303 | 353 |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n12 | 15 | 34 | 5 |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n13 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n1410 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n18 | 15 |  | 5 |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n20 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n24 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n25 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 453 |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 453 |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 453 |  |  |  |  |  |  |
| n26 | 15 | 34 | 5 | 74 | 10 | 15 | 20 | 253 | 303 |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 253 | 303 |  |  |  |  |  |  |  |  |  |
| n28 | 15 | 34 | 5 |  | 10 | 15 | 207 | 257 | 307 |  | 404,7 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 207 | 257 | 307 |  | 404,7 |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n29 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n30 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n31 | 15 | 34 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n34 | 15 |  | 5 |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
| n3810 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  |  |  |  |  |  |  |
| n39 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
| n40 | 15 |  | 55 |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
| n41 | 15 |  | 54,11 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |
| n46 | 15 |  |  |  | 105 |  | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 105 |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
|  | 60 |  |  |  | 105 |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
| n4710 | 15 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  |  |  |  |  |  |  |
| n48 | 15 |  | 55 |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 5012 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 5012 | 6012 | 7012 | 8012 | 9012 | 10012 |
|  | 60 |  |  |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 5012 | 6012 | 7012 | 8012 | 9012 | 10012 |
| n50 | 15 |  | 55 |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 50 | 60 |  | 803 |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 |  | 30 |  | 40 |  | 50 | 60 |  | 803 |  |  |
| n51 | 15 |  | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n53 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n54 | 15 |  | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n65 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 |  |  |  |  |  | 50 |  |  |  |  |  |
| n66 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |  |  |  |  |  |  |
| n67 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n68 | 15 |  | 5 |  | 10 | 1513 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 1513 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n70 | 15 |  | 5 |  | 10 | 15 | 203 | 253 |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 203 | 253 |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 203 | 253 |  |  |  |  |  |  |  |  |  |  |
| n71 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 3012 | 3512 |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 3012 | 3512 |  |  |  |  |  |  |  |  |
| n72 | 15 | 34 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n74 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
| n75 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
| n76 | 15 |  | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n77 | 15 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
| n78 | 15 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
| n7910 | 15 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  | 50 | 60 | 704 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 |  | 20 |  | 30 |  | 40 |  | 50 | 60 | 704 | 80 | 90 | 100 |
| n80 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
| n81 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n82 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n83 | 15 |  | 5 |  | 10 | 15 | 207 | 257 | 307 |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 207 | 257 | 307 |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n84 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 | 45 | 50 |  |  |  |  |  |
| n85 | 15 | 34 | 5 |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n86 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
| n87 | 15 | 3 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n88 | 15 | 3 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n89 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n90 | 15 |  | 54 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 60 | 70 | 80 | 90 | 100 |
| n91 | 15 |  | 5 |  | 108 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n92 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n93 | 15 |  | 5 |  | 108 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n94 | 15 |  | 5 |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n95 | 15 |  | 5 |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 |  |  |  |  |  |  |  |  |  |  |  |  |
| n96 | 15 |  |  |  |  |  | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
|  | 60 |  |  |  |  |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
| n97 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
| n98 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 | 15 | 20 | 25 | 30 | 35 | 40 |  |  |  |  |  |  |  |
| n99 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n100 | 15 | 34 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n101 | 15 |  | 5 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n102 | 15 |  |  |  |  |  | 20 |  |  |  | 40 |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
|  | 60 |  |  |  |  |  | 20 |  |  |  | 40 |  |  | 60 |  | 80 |  | 1004 |
| n104 | 15 |  |  |  |  |  | 20 |  | 30 |  | 40 |  | 50 |  |  |  |  |  |
|  | 30 |  |  |  |  |  | 20 |  | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
|  | 60 |  |  |  |  |  | 20 |  | 30 |  | 40 |  | 50 | 60 | 70 | 80 | 90 | 100 |
| n105 | 15 |  | 5 |  | 10 | 15 | 20 | 253 | 303 | 353 |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 253 | 303 | 353 |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n106 | 15 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n109 | 15 |  | 5 |  | 10 | 15 | 20 | 25 | 30 |  | 403 |  | 503 |  |  |  |  |  |
|  | 30 |  |  |  | 10 | 15 | 20 | 25 | 30 |  | 403 |  | 503 |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n110 | 15 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NOTE 1: Void.NOTE 2: Void.NOTE 3: This UE channel bandwidth is applicable only to downlink.NOTE 4: This UE channel bandwidth is optional in this release of the specification.NOTE 5: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an SCell part of DC or CA configuration.NOTE 6: Void.NOTE 7: For UEs supporting up to 30 MHz channel bandwidth, the minimum requirements are specified for any NR UL channel bandwidth confined to 703-733 MHz or 718-748 MHz. For UEs supporting 40 MHz channel bandwidth, the minimum requirements are specified for any NR UL channel bandwidth confined to 703-743.04 MHz or 718-748MHz.NOTE 8: This UE channel bandwidth is applicable only to uplink.NOTE 9: Void.NOTE 10: For this band, UE channel bandwidths which are applicable to sidelink operation are specified in Table 5.3E.1-1.NOTE 11: Not all frequency positions of 5 MHz carriers are possible due limitations of the SSB position relative to the 5 MHz channels. 5 MHz channels with Fc such that 2499+N*1.2 ≤Fc<2499.3+N*1.2MHz for 0≤N<157 are not compatible with SSB positions and cannot be used for 5 MHz n41.NOTE 12: This UE channel Bandwidth is optional for uplink in this release of the specification.NOTE 13: For the 15 MHz bandwidth, the minimum requirements are specified for NR UL carrier frequencies confined to either 705.5 MHz or 710.5-720.5 MHz. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### 5.3.6 Asymmetric channel bandwidths

The UE channel bandwidth can be asymmetric in downlink and uplink. In asymmetric channel bandwidth operation, the narrower carrier shall be confined within the frequency range of the wider channel bandwidth.

In FDD, the confinement is defined as a maximum deviation to the Tx-Rx carrier center frequency separation (defined in Table 5.4.4-1) as following:

ΔFTX-RX = | (BWDL – BWUL)/2 |

The operating bands and supported asymmetric channel bandwidth combinations are defined in Table 5.3.6-1.

Table 5.3.6-1: FDD asymmetric UL and DL channel bandwidth combinations

| NR Band | Channel bandwidths for UL (MHz) | Channel bandwidths for DL (MHz) | Asymmetric channel bandwidth combination set |  |
| --- | --- | --- | --- | --- |
| n5 | 20 | 25 | 0 |  |
| n8 | 20 | 35 | 0 |  |
|  | 10, 15, 20 | 25, 35 | 1 |  |
|  | 10, 15, 20 | 25, 30, 35 | 2 |  |
| n24 | 10 | 5 | 0 |  |
| n25 | 40 | 45 | 0 |  |
| n26 | 20 | 25, 30 | 0 |  |
| n283 | 3 | 5 | 1 |  |
| n66 | 5, 10 | 20, 40 | 0 |  |
|  | 20 | 40 |  |  |
|  | 5, 10 | 20, 25, 30, 40 | 1 |  |
|  | 20, 25, 30 | 40 |  |  |
|  | 5, 10, 15 | 20, 25, 30, 35, 40 | 2 |  |
|  | 20, 25, 30 | 40 |  |  |
| n70 | 5, 10 | 15 | 0 |  |
|  | 5, 10, 15 | 20, 25 |  |  |
|  | 5, 15 | 10 | 1 |  |
|  | 10, 15 | 5 |  |  |
| n71 | 5 | 10 | 0 |  |
|  | 10 | 15 |  |  |
|  | 15 | 20 |  |  |
|  | 5 | 10 | 1 |  |
|  | 10 | 15 |  |  |
|  | 15 | 20 |  |  |
|  | 20 | 35 |  |  |
|  | 20 | 25, 30, 35 | 2 |  |
|  | 25 | 30, 35 | 3 |  |
| n911 | 10 | 5 | 0 |  |
| n921 | 5 | 10, 15, 20 | 0 |  |
|  | 10 | 15, 20 |  |  |
| n931 | 10 | 5 | 0 |  |
| n941 | 5 | 10, 15, 20 | 0 |  |
|  | 10 | 15, 20 |  |  |
| n105 | 20 | 25, 30, 35 | 0 |  |
| n1091 | 5 | 10, 15, 20, 25, 30, 40, 50 | 0 |  |
|  | 10 | 15, 20, 25, 30, 40, 50 |  |  |
|  | 15 | 20, 25, 30, 40, 50 |  |  |
|  | 20 | 25, 30, 40, 50 |  |  |
|  | 25 | 30, 40, 50 |  |  |
|  | 30 | 40, 50 |  |  |
| NOTE 1: The assignment of the paired UL and DL channels are subject to a TX-RX separation as specified in clause 5.4.4.NOTE 2: As indicated for asymmetricBandwidthCombinationSet in TS 38.306 [15], it is mandatory for UEs to support asymmetric channel BCS0 if there is an asymmetric BCS0 defined for the band.NOTE 3:  This BCS1 is limited to uplink 715-718 MHz and downlink 768-773 MHz. |  |  |  |  |

In TDD, the operating bands and supported asymmetric channel bandwidth combinations are defined in Table 5.3.6-2.

Table 5.3.6-2: TDD asymmetric UL and DL channel bandwidth combinations

| NR Band | Channel bandwidths for UL (MHz) | Channel bandwidths for DL (MHz) | Asymmetric channel bandwidth combination set |
| --- | --- | --- | --- |
| n50 | 60 | 80 | 0 |
| NOTE 1: Both centre frequency and BWP-ID shall match between DL and UL carriers as defined in TS 38.331 [7] cl. 6.3.2 and TS 38.213 [8] clause 12.NOTE 2: In a case a UE is configured with a full width of BWP within both UL/ DL channels, the centre frequency of UL/ DL channels shall be same.NOTE 3: A position of Point A is common between UL and DL carriers as defined in TS 38.331 [7] cl. 6.3.2.NOTE 4: The maximum transmission bandwidth configuration NRB for 60 MHz UL channel BW is reduced from the value defined in table 5.3.2-1 to 161 for 30kHz SCS for Asymmetric channel bandwidth combination set 0 for n50. |  |  |  |

## 5.3A UE channel bandwidth for CA

### 5.3A.1 General

Figure 5.3A.1-1: Void

Figure 5.3A.1-2: Void

### 5.3A.2 Maximum transmission bandwidth configuration for CA

For carrier aggregation, the maximum transmission bandwidth configuration is defined per component carrier and the requirement is specified in clause 5.3.2.

### 5.3A.3 Minimum guardband and transmission bandwidth configuration for CA

For intra-band contiguous carrier aggregation, Aggregated Channel Bandwidth and Guard Bands are defined as follows, see Figure 5.3A.3-1.

Figure 5.3A.3-1: Definition of Aggregated Channel Bandwidth for intra-band carrier aggregation

The aggregated channel bandwidth, BWChannel_CA, is defined as

BWChannel_CA = Fedge,high - Fedge,low (MHz).

The lower bandwidth edge Fedge, low and the upper bandwidth edge Fedge,high of the aggregated channel bandwidth are used as frequency reference points for transmitter and receiver requirements and are defined by:

Fedge,low = FC,low - Foffset,low

Fedge,high = FC,high + Foffset,high

The lower and upper frequency offsets depend on the transmission bandwidth configurations of the lowest and highest assigned edge component carrier and are defined as

Foffset,low = (NRB,low*12 + 1)*SCSlow/2 + BWGB (MHz)

Foffset,high = (NRB,high*12 - 1)*SCShigh/2 + BWGB (MHz)

BWGB = max(GBChannel,low, GBChannel,high)

NRB,low and NRB,high are the transmission bandwidth configurations according to Table 5.3.2-1 for the lowest and highest assigned component carrier, SCSlow and SCShigh are the sub-carrier spacing for the lowest and highest assigned component carrier respectively. SCSlow, SCShigh, NRB,low, NRB,high, GBChannel,low and GBChannel,high use the largest μ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths according to Table 5.3.5-1. GBChannel,low and GBChannel,high are the minimum guard band for the lowest and highest assigned component carrier according to Table 5.3.3-1 for the said μ value, respectively.

NOTE: The Foffset,low, Foffset,high and BWChannel_CA determined as per the above apply for all sub-carrier configurations μ ≤ μ0 configured for component carriers centred at FC,low /FC,high, where μ0 is the largest µ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths. The BWGB is used for determining the frequency offsets; it is also the minimum internal guard band at the lower/higher edge of BWChannel_CA when μ = μ0 is configured for the lower and upper component carriers.

In case there is no common μ value for both of the channel bandwidths, μ=1 is used for SCSlow, SCShigh, NRB,low, NRB,high, GBChannel,low and GBChannel,high.

For intra-band non-contiguous carrier aggregation Sub-block Bandwidth and Sub-block edges are defined as follows, see Figure 5.3A.3-2.


Figure 5.3A.3-2: Definition of sub-block bandwidth for intra-band non-contiguous spectrum

The lower sub-block edge of the Sub-block Bandwidth (BWChannel,block) is defined as

Fedge,block, low = FC,block,low - Foffset, low.

The upper sub-block edge of the Sub-block Bandwidth is defined as

Fedge,block,high = FC,block,high + Foffset,high.

The Sub-block Bandwidth, BWChannel,block, is defined as follows:

BWChannel,block = Fedge,block,high - Fedge,block,low (MHz)

The lower and upper frequency offsets Foffset,block,low and Foffset,block,high depend on the transmission bandwidth configurations of the lowest and highest assigned edge component carriers within a sub-block and are defined as:

Foffset,block,low =  (NRB,low*12 + 1)*SCSlow/2 + BWGB (MHz)

Foffset,block,high =  (NRB,high*12 - 1)*SCShigh/2 + BWGB(MHz)

BWGB = max(GBChannel,low, GBChannel,high)

where NRB,low and NRB,high are the transmission bandwidth configurations according to Table 5.3.2-1 for the lowest and highest assigned component carrier within a sub-block, respectively. SCSlow and SCShigh are the sub-carrier spacing for the lowest and highest assigned component carrier within a sub-block, respectively.  SCSlow, SCShigh, NRB,low, NRB,high, GBChannel,low and GBChannel,high use the largest μ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths according to Table 5.3.5-1. GBChannel,low and GBChannel,high are the minimum guard band for the lowest and highest assigned component carrier according to Table 5.3.3-1 for the said μ value, respectively. In case there is no common μ value for both of the channel bandwidths, μ=1 is used for SCSlow, SCShigh, NRB,low, NRB,high, GBChannel,low and GBChannel,high.

NOTE: The Foffset,block,low, Foffset,block,high and BWChannel,block determined as per the above apply for all sub-carrier configurations μ ≤ μ0 configured for component carriers centred at FC,block,low /FC,block,high, where μ0 is the largest µ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths. The BWGB is used for determining the frequency offsets; it is also the minimum internal guard band at the lower/higher edge of BWChannel,block when μ = μ0 is configured for the lower and upper component carriers of the block.

The sub-block gap size between two consecutive sub-blocks Wgap is defined as

Wgap = Fedge,block n+1,low - Fedge,block n,high (MHz)

### 5.3A.4 Void

### 5.3A.5 UE channel bandwidth per operating band for CA

The requirements for carrier aggregation in this specification are defined for carrier aggregation configurations.

For intra-band contiguous carrier aggregation, a carrier aggregation configuration is a single operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5A.1. For each carrier aggregation configuration, requirements are specified for all aggregated channel bandwidths contained in a bandwidth combination set, a UE can indicate support of several bandwidth combination sets per carrier aggregation configuration. For intra-band non-contiguous carrier aggregation, a carrier aggregation configuration is a single operating band supporting two or more sub-blocks, each supporting a carrier aggregation bandwidth class.

For intra-band non-contiguous uplink carrier aggregation, frequency separation class (Fs) specified in Table 5.3A.5-2 indicates the maximum frequency span between lower edge of lowest component carrier and upper edge of highest component carrier that UE can support per band combination in uplink in non-contiguous intra-band operation when the signalling is absent for dualPA-Architecture IE.

For inter-band carrier aggregation, a carrier aggregation configuration is a combination of operating bands, each supporting a carrier aggregation bandwidth class.


Table 5.3A.5-1: NR CA bandwidth classes

| NR CA bandwidth class | Aggregated channel bandwidth | Number of contiguous CC | Fallback group |
| --- | --- | --- | --- |
| A | BWChannel ≤ BWChannel,max | 1 | 1, 2, 34 |
| B | 20 MHz ≤ BWChannel_CA ≤ 100 MHz | 2 | 2, 34 |
| C | 100 MHz < BWChannel_CA ≤ 2 x BWChannel,max | 2 | 1, 34 |
| D | 200 MHz < BWChannel_CA ≤ 3 x BWChannel,max | 3 |  |
| E | 300 MHz < BWChannel_CA ≤ 4 x BWChannel,max | 4 |  |
| G | 100 MHz < BWChannel_CA ≤ 150 MHz | 3 | 2 |
| H | 150 MHz < BWChannel_CA ≤ 200 MHz | 4 |  |
| I | 200 MHz < BWChannel_CA ≤ 250 MHz | 5 |  |
| J | 250 MHz < BWChannel_CA ≤ 300 MHz | 6 |  |
| K | 300 MHz < BWChannel_CA ≤ 350 MHz | 7 |  |
| L | 350 MHz < BWChannel_CA ≤ 400 MHz | 8 |  |
| M3 | 50 MHz ≤ BWChannel_CA ≤ 200 MHz | 3 | 34 |
| N3 | 80 MHz ≤ BWChannel_CA ≤ 300 MHz | 4 |  |
| O3 | 100 MHz ≤ BWChannel_CA ≤ 400 MHz | 5 |  |
| NOTE 1: BWChannel, max is maximum channel bandwidth supported among all bands in a releaseNOTE 2: It is mandatory for a UE to be able to fallback to lower order NR CA bandwidth class configuration within a fallback group. It is not mandatory for a UE to be able to fallback to lower order NR CA bandwidth class configuration that belong to a different fallback group.NOTE 3: This bandwidth class is only applicable to bands identified for use with shared spectrum channel access in Table 5.2-1.NOTE 4: Fallback group 3 is only applicable to bands identified for use with shared spectrum channel access in Table 5.2-1. |  |  |  |

Table 5.3A.5-2: NR intra-band non-contiguous UL CA frequency separation classes

| NR NC UL CA frequency separation class | Maximum allowed frequency separation |
| --- | --- |
| I | 100 MHz |
| II | 200 MHz |
| III | [600MHz] |

## 5.3E Channel bandwidth for V2X

### 5.3E.1 General

NR V2X operation channel bandwidths for each operating band are specified in Table 5.3E.1-1. The same (symmetrical) channel bandwidth is specified for both the transmission and reception path. The maximum channel bandwidth for SL operation in licensed band is 40MHz.

Table 5.3E.1-1 NR V2X operation channel bandwidths for each operating band

| NR band / SCS / UE Channel bandwidth (MHz) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| NR Band | SCS(kHz) | 5 | 10 | 20 | 30 | 40 |
| n14 | 15 | 5 | 10 |  |  |  |
|  | 30 |  | 10 |  |  |  |
|  | 60 |  |  |  |  |  |
| n38 | 15 |  | 10 | 20 | 30 | 40 |
|  | 30 |  | 10 | 20 | 30 | 40 |
|  | 60 |  | 10 | 20 | 30 | 40 |
| n47 | 15 |  | 10 | 20 | 30 | 40 |
|  | 30 |  | 10 | 20 | 30 | 40 |
|  | 60 |  | 10 | 20 | 30 | 40 |
| n79 | 15 |  | 10 | 20 | 30 | 40 |
|  | 30 |  | 10 | 20 | 30 | 40 |
|  | 60 |  | 10 | 20 | 30 | 40 |

### 5.3E.1A Channel bandwidth for Sidelink CA

For sidelink intra-band contiguous carrier aggregation, a carrier aggregation configuration is a single ITS operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5E.1A.1.

For sidelink intra-band non-contiguous carrier aggregation, a carrier aggregation configuration is a single ITS operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5E.1A.2

The sidelink intra-band carrier aggregation bandwidth class follows Table 5.3A.5-1. For each carrier aggregation configuration, requirements are specified for all aggregated channel bandwidths contained in a bandwidth combination set.

### 5.3E.1F Channel bandwidth for Sidelink Unlicensed

NR SL-U Channel bandwidths for each band are specified in Table 5.3E.1F-1. The same (symmetrical) channel bandwidth is specified for both the transmission and reception path.

Table 5.3E.1F-1 NR SL-U channel bandwidth

|  |  | SL-U band /channel bandwidth |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NR SL-U Operating Band | SCS kHz | 10 MHz | 20 MHz | 30 MHz | 40 MHz | 50 MHz | 60 MHz | 80 MHz | 90 MHz | 100 MHz |
| n46 | 15 |  | 20 |  | 40 |  |  |  |  |  |
|  | 30 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
|  | 60 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
| n96 | 15 |  | 20 |  | 40 |  |  |  |  |  |
|  | 30 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
|  | 60 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
| n102 | 15 |  | 20 |  | 40 |  |  |  |  |  |
|  | 30 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
|  | 60 |  | 20 |  | 40 |  | 60 | 80 |  | 1001 |
| NOTE 1: This UE channel bandwidth is optional in this release of the specification. |  |  |  |  |  |  |  |  |  |  |

### 5.3E.2 Channel bandwidth for V2X concurrent operation

For NR V2X inter-band concurrent operation in FR1, the NR V2X channel bandwidths for each operating band are specified in Table 5.3E.2-1.

Table 5.3E.2-1: Inter-band concurrent operation configurations

| NR V2X inter-band concurrent operating configuration | NR Band | Interface | Channel bandwidth (MHz) (NOTE 1) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| V2X_n1A-n47A | n1 | Uu | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n3A-n47A | n3 | Uu | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n5A-n47A | n5 | Uu | 5, 10, 15, 20, 25 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n8A-n47A | n8 | Uu | 5, 10, 15, 20, 35 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n34A-n47A | n34 | Uu | 5, 10, 15 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n39A-n47A | n39 | Uu | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n40A-n47A | n40 | Uu | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n41A-n47A | n41 | Uu | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n71A-n47A | n71 | Uu | 5, 10, 15, 20 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |
| V2X_n78A-n47A | n78 | Uu | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  | n47 | PC5 | 10, 20, 30, 40 |  |

For NR V2X intra-band concurrent operation in FR1, the NR V2X channel bandwidths for each operating band are specified in Table 5.3E.2-2.

Table 5.3E.2-2: Intra-band concurrent operation configurations

| NR V2X intra-band concurrent operating configuration | NR Band | Interface | Channel bandwidth (MHz) (NOTE 1) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| V2X_n79B | n79 | Uu | 40, 50, 60, 80, 100 | 0 |
|  | n79 | PC5 | 10, 20, 30, 40 |  |
| NOTE 1:  The SCS of each channel bandwidth for NR band refers to Table 5.3.5-1. |  |  |  |  |

### 5.3E.2F Channel bandwidth for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the SL-U Channel bandwidths for each operating band are specified in Table 5.3E.2F-1.

Table 5.3E.2F-1 NR SL-U inter-band concurrent operating configurations

| NR SL inter-band concurrent operating configuration | NR Band | Interface | Channel bandwidth (MHz) (NOTE 1) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| SL_n78A-n46A | n78 | Uu | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  | n46 | PC5 | 20, 40, 60, 80, 100 |  |
| NOTE 1: The SCS of each channel bandwidth for NR band refers to Table 5.3.5-1. |  |  |  |  |

## 5.3I Channel bandwidth for (e)RedCap

The requirements in this specification apply to the combination of channel bandwidths, SCS and operating bands shown in Table 5.3.5-1 with maximum channel bandwidth of 20MHz. The transmission bandwidth configuration in Table5.3.2-1 shall be supported for each of the specified channel bandwidths up to 20 MHz. When UE supports IE supportOfERedCap-r18 and does not support IE eRedCapNotReducedBB-BW-r18 the requirements in this specification apply with maximum 25RBs for 15 kHz SCS and 12 RBs for 30 kHz SCS for PDSCH and PUSCH as described in clause 17.1A of TS 38.213 [8]. The channel bandwidths are specified for both the TX and RX paths.

3MHz channel bandwidth is not applicable for (e)RedCap UE in the current release.

## 5.3M UE channel bandwidth for LP-WUS/WUR

### 5.3M.1 General

The LP-WUS carrier bandwidth corresponding to the UE channel bandwidth for LP-WUS is defined as the sum of resource blocks (RBs) occupied by the LP-WUS signal and the guard RBs separating it from the NR signal. The LP-WUS carrier is embedded within the NR channel and is flexibly positionable, provided alignment with the NR PRB grid is maintained.

A guard RB is referred to as an ASCS guard RB when located between an NR RB and an LP-WUS RB, and as an ACS guard RB when positioned between the NR guardband as specified in Table 5.3.3-1 and an LP-WUS RB.

### 5.3M.2 Maximum transmission bandwidth configuration

The maximum transmission bandwidth configuration NRB,LP-WUS for LP-WUS within each NR UE channel bandwidth and subcarrier spacing is specified in Table 5.3M.2-1.

Table 5.3M.2-1: Maximum transmission bandwidth configuration NRB,LP-WUS for LP-WUS

| SCS (kHz) | 3MHz | 5MHz | 7MHz | 10MHz | 15MHz | 20MHz | 25MHz | 30MHz | 35MHz | 40 MHz | 45MHz | 50MHz | 60MHz | 70MHz | 80MHz | 90MHz | 100MHz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | NRB, LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB, LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS | NRB,  LP-WUS |
| 15 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | N/A | N/A | N/A | N/A | N/A |
| 30 | N/A | 11 | N/A | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 |
| 60 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 5.4 Channel arrangement

### 5.4.1 Channel spacing

#### 5.4.1.1 Channel spacing for adjacent NR carriers

The spacing between carriers will depend on the deployment scenario, the size of the frequency block available and the channel bandwidths. The nominal channel spacing between two adjacent NR carriers is defined as following:

- For NR operating bands with 100 kHz or 10 kHz channel raster,

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2

- For NR operating bands with 15 kHz channel raster,

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2+{-5 kHz, 0 kHz, 5 kHz} for ∆FRaster equals 15 kHz

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2+{-10 kHz, 0 kHz, 10 kHz} for ∆FRaster equals 30 kHz

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective NR carriers. The channel spacing can be adjusted depending on the channel raster to optimize performance in a particular deployment scenario.

For NR bands restricted to operation with shared-spectrum channel access, the maximum deviation from the nominal channel spacing is 40 kHz.

### 5.4.2 Channel raster

#### 5.4.2.1 NR-ARFCN and channel raster

The global frequency channel raster defines a set of RF reference frequencies FREF. The RF reference frequency is used in signalling to identify the position of RF channels, SS blocks and other elements.

The global frequency raster is defined for all frequencies from 0 to 100 GHz. The granularity of the global frequency raster is ΔFGlobal.

RF reference frequencies are designated by an NR Absolute Radio Frequency Channel Number (NR-ARFCN) in the range (0…2016666) on the global frequency raster. The relation between the NR-ARFCN and the RF reference frequency FREF in MHz is given by the following equation, where FREF-Offs and NRef-Offs are given in Table 5.4.2.1-1 and NREF is the NR-ARFCN.

FREF = FREF-Offs + ΔFGlobal (NREF – NREF-Offs)

Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster

| Frequency range (MHz) | ΔFGlobal (kHz) | FREF-Offs (MHz) | NREF-Offs | Range of NREF |
| --- | --- | --- | --- | --- |
| 0 – 3000 | 5 | 0 | 0 | 0 – 599999 |
| 3000 – 24250 | 15 | 3000 | 600000 | 600000 – 2016666 |

The channel raster defines a subset of RF reference frequencies that can be used to identify the RF channel position in the uplink and downlink. The RF reference frequency for an RF channel maps to a resource element on the carrier. For each operating band, a subset of frequencies from the global frequency raster are applicable for that band and forms a channel raster with a granularity ΔFRaster, which may be equal to or larger than ΔFGlobal.

For SUL bands except n95, n97, n98 and for the uplink of all FDD bands defined in Table 5.2-1, and for TDD bands n34, n39, n48, n90, n38 and n40

FREF, shift = FREF + Δshift, Δshift = 0 kHz or 7.5 kHz.

where Δshift is signalled by the network in higher layer parameter frequencyShift7p5khz [7]. For Band n34, n38, n39, n40, n48 FREF, shift is only applicable to uplink transmissions using a 15 kHz SCS.

The mapping between the channel raster and corresponding resource element is given in Clause 5.4.2.2. The applicable entries for each operating band are defined in Clause 5.4.2.3.

#### 5.4.2.2 Channel raster to resource element mapping

The mapping between the RF reference frequency on the channel raster and the corresponding resource element is given in Table 5.4.2.2-1 and can be used to identify the RF channel position. The mapping depends on the total number of RBs that are allocated in the channel and applies to both UL and DL. The mapping must apply to at least one numerology supported by the UE.

Table 5.4.2.2-1: Channel raster to resource element mapping

|  | NRBmod2 = 0 | NRBmod2 = 1 |
| --- | --- | --- |
| Resource element index ![](media_svg/image5.svg) [公式: k] | 0 | 6 |
| Physical resource block index ![](media_svg/image1.svg) [公式≈: ^{n}PRB] | ![](media_svg/image6.svg) [公式≈: ^{n}PRB^{=}^{⋅}⋅_{√}^{N}_{2}^{RB}^{∂}∂_{∃}] | ![](media_svg/image7.svg) [公式≈: ^{n}PRB^{=}^{⋅}⋅_{√}^{N}_{2}^{RB}^{∂}∂_{∃}] |

NRB is the maximum transmission bandwidth configuration specified in sub-clause 5.3.2, is the PRB index within the NRB, and ![](media_svg/image5.svg) [公式: k] is the resource element index within this PRB.

#### 5.4.2.3 Channel raster entries for each operating band

The RF channel positions on the channel raster in each NR operating band are given through the applicable NR-ARFCN in Table 5.4.2.31, using the channel raster to resource element mapping in clause 5.4.2.2.

For NR operating bands with 100 kHz channel raster, ΔFRaster = 20 × ΔFGlobal. In this case every 20th NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.31 is given as <20>.

For NR operating bands with 15 kHz channel raster below 3GHz, ΔFRaster = I × ΔFGlobal, where I ϵ {3,6}. Every Ith NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.31 is given as < I >.

For NR operating bands with 15 kHz channel raster above 3GHz, ΔFRaster = I × ΔFGlobal, where I ϵ {1,2}. Every Ith  NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.3-1 is given as <I>.

In frequency bands with two or more ΔFRaster, the higher ΔFRaster: For 15 kHz and 30 kHz channel raster applies to channels using only the SCS that is equal to or larger than the higher ΔFRaster and SSB SCS is equal to the higher ∆FRaster.

Table 5.4.2.3-1: Applicable NR-ARFCN per operating band

| NR operating band | ΔFRaster(kHz) | UplinkRange of NREF(First – <Step size> – Last) | DownlinkRange of NREF(First – <Step size> – Last) |
| --- | --- | --- | --- |
| n1 | 100 | 384000 – <20> – 396000 | 422000 – <20> – 434000 |
| n2 | 100 | 370000 – <20> – 382000 | 386000 – <20> – 398000 |
| n3 | 100 | 342000 – <20> – 357000 | 361000 – <20> – 376000 |
| n5 | 100 | 164800 – <20> – 169800 | 173800 – <20> – 178800 |
| n7 | 100 | 500000 – <20> – 514000 | 524000 – <20> – 538000 |
| n8 | 100 | 176000 – <20> – 183000 | 185000 – <20> – 192000 |
| n12 | 100 | 139800 – <20> – 143200 | 145800 – <20> – 149200 |
| n13 | 100 | 155400 – <20> – 157400 | 149200 – <20> – 151200 |
| n14 | 100 | 157600 – <20> – 159600 | 151600 – <20> – 153600 |
| n18 | 100 | 163000 – <20> – 166000 | 172000 – <20> – 175000 |
| n20 | 100 | 166400 – <20> – 172400 | 158200 – <20> – 164200 |
| n24 | 100 | 325300 – <20> – 332100 | 305000 – <20> – 311800 |
| n25 | 100 | 370000 – <20> – 383000 | 386000 – <20> – 399000 |
| n26 | 100 | 162800 – <20> – 169800 | 171800 – <20> – 178800 |
| n28 | 100 | 140600 – <20> – 149600 | 151600 – <20> – 160600 |
| n29 | 100 | N/A | 143400 – <20> – 145600 |
| n30 | 100 | 461000 – <20> – 463000 | 470000 – <20> – 472000 |
| n31 | 100 | 90500 – <20> – 91500 | 92500 – <20> – 93500 |
| n34 | 100 | 402000 – <20> – 405000 | 402000 – <20> – 405000 |
| n38 | 100 | 514000 – <20> – 524000 | 514000 – <20> – 524000 |
| n39 | 100 | 376000 – <20> – 384000 | 376000 – <20> – 384000 |
| n40 | 100 | 460000 – <20> – 480000 | 460000 – <20> – 480000 |
| n41 | 15 | 499200 – <3> – 537999 | 499200 – <3> – 537999 |
|  | 30 | 499200 – <6> – 537996 | 499200 – <6> – 537996 |
| n462 | 15 | 743334 – <1> – 795000 | 743334 – <1> – 795000 |
| n47 | 15 | 790334 – <1> – 795000 | 790334 – <1> – 795000 |
| n48 | 15 | 636667 – <1> – 646666 | 636667 – <1> – 646666 |
|  | 30 | 636668 – <2> – 646666 | 636668 – <2> – 646666 |
| n50 | 100 | 286400 – <20> – 303400 | 286400 – <20> – 303400 |
| n51 | 100 | 285400 – <20> – 286400 | 285400 – <20> – 286400 |
| n53 | 100 | 496700 – <20> – 499000 | 496700 – <20> – 499000 |
| n54 | 100 | 334000 – <20> – 335000 | 334000 – <20> – 335000 |
| n65 | 100 | 384000 – <20> – 402000 | 422000 – <20> – 440000 |
| n66 | 100 | 342000 – <20> – 356000 | 422000 – <20> – 440000 |
| n67 | 100 | N/A | 147600 – <20> – 151600 |
| n68 | 100 | 139600 – <20> – 145600 | 150600 – <20> – 156600 |
| n70 | 100 | 339000 – <20> – 342000 | 399000 – <20> – 404000 |
| n71 | 100 | 132600 – <20> – 139600 | 123400 – <20> – 130400 |
| n72 | 100 | 90200 – <20> – 91200 | 92200 – <20> – 93200 |
| n74 | 100 | 285400 – <20> – 294000 | 295000 – <20> – 303600 |
| n75 | 100 | N/A | 286400 – <20> – 303400 |
| n76 | 100 | N/A | 285400 – <20> – 286400 |
| n77 | 15 | 620000 – <1> – 680000 | 620000 – <1> – 680000 |
|  | 30 | 620000 – <2> – 680000 | 620000 – <2> – 680000 |
| n78 | 15 | 620000 – <1> – 653333 | 620000 – <1> – 653333 |
|  | 30 | 620000 – <2> – 653332 | 620000 – <2> – 653332 |
| n79 | 15 | 693334 – <1> – 733333 | 693334 – <1> – 733333 |
|  | 30 | 693334 – <2> – 733332 | 693334 – <2> – 733332 |
| n80 | 100 | 342000 – <20> – 357000 | N/A |
| n81 | 100 | 176000 – <20> – 183000 | N/A |
| n82 | 100 | 166400 – <20> – 172400 | N/A |
| n83 | 100 | 140600 – <20> –149600 | N/A |
| n84 | 100 | 384000 – <20> – 396000 | N/A |
| n85 | 100 | 139600 – <20> – 143200 | 145600 – <20> – 149200 |
| n86 | 100 | 342000 – <20> – 356000 | N/A |
| n87 | 100 | 82000 – <20> – 83000 | 84000 – <20> – 85000 |
| n88 | 100 | 82400 – <20> – 83400 | 84400 – <20> – 85400 |
| n89 | 100 | 164800 – <20> – 169800 | N/A |
| n90 | 15 | 499200 – <3> – 537999 | 499200 – <3> – 537999 |
|  | 30 | 499200 – <6> – 537996 | 499200 – <6> – 537996 |
|  | 100 | 499200 – <20> – 538000 | 499200 – <20> – 538000 |
| n91 | 100 | 166400 – <20> – 172400 | 285400 – <20> – 286400 |
| n92 | 100 | 166400 – <20> – 172400 | 286400 – <20> – 303400 |
| n93 | 100 | 176000 – <20> – 183000 | 285400 – <20> – 286400 |
| n94 | 100 | 176000 – <20> – 183000 | 286400 – <20> – 303400 |
| n95 | 100 | 402000 – <20> – 405000 | N/A |
| n963 | 15 | 795000 – <1> – 875000 | 795000 – <1> – 875000 |
| n97 | 100 | 460000 – <20> – 480000 | N/A |
| n98 | 100 | 376000 – <20> – 384000 | N/A |
| n99 | 100 | 325300 – <20> – 332100 | N/A |
| n100 | 100 | 174880 – <20> – 176000 | 183880 – <20> – 185000 |
| n101 | 100 | 380000 – <20> – 382000 | 380000 – <20> – 382000 |
| n1024 | 15 | 795000 – <1> – 828333 | 795000 – <1> – 828333 |
| n104 | 15 | 828334 – <1> – 875000 | 828334 – <1> – 875000 |
|  | 30 | 828334 – <2> – 875000 | 828334 – <2> – 875000 |
| n105 | 100 | 132600 – <20> – 140600 | 122400 – <20> – 130400 |
| n1065 | 100 | 179200 – <20> – 180200 | 187000 – <20> – 188000 |
| n109 | 100 | 140600 – <20> – 146600 | 286400 – <20> – 303400 |
| n110 | 100 | 278000 – <20> – 279000 | 286400 – <20> – 287000 |
| NOTE 1: The channel numbers that designate carrier frequencies so close to the operating band edges that the carrier extends beyond the operating band edge shall not be used.NOTE 2: The following NREF are allowed for operation in Band n46: see Table 5.4.2.3-2.NOTE 3: The following NREF are allowed for operation in Band n96: see Table 5.4.2.3-3.NOTE 4: The following NREF are allowed for operation in Band n102: see Table 5.4.2.3-4.NOTE 5: In the present version of the specification, only NREF  179800 and 187600 is applicable for 3 MHz channel bandwidth. |  |  |  |

Table 5.4.2.3-2: Allowed NREF (NR-ARFCN) for operation in Band n46

| Channel Bandwidth | Allowed NREF |
| --- | --- |
| 10 MHz | 782000, 788668 |
| 20 MHz | 744000, 745332, 746668, 748000, 749332, 750668, 752000, 753332, 754668, 756000, 765332, 766668, 768000, 769332, 770668, 772000, 773332, 774668, 776000, 777332, 778668, 780000, 781332, 783000, 784332, 785668, 787000, 788332, 789668, 791000, 792332, 793668 |
| 40 MHz | 744668, 746000, 748668, 751332, 754000, 755332, 766000, 767332, 770000, 772668, 775332, 778000, 780668, 783668, 786332, 787668, 790332, 793000 |
| 60 MHz | 745332, 746668, 748000, 752000, 753332, 754668, 766668, 768000, 769332, 773332, 774668, 778668, 780000, 784332, 785668, 791000, 792332 |
| 80 MHz | 746000, 747332, 752668, 754000, 767332, 768668, 774000, 779332, 785000, 791668 |
| 100 MHz | 746668, 753332, 768000, 791000 |
| NOTE: 10 MHz channel bandwidth shall only apply in certain regions where the absence of non 3GPP technologies can be guaranteed on a long-term basis in this version of specification. |  |

Table 5.4.2.3-3: Allowed NREF (NR-ARFCN) for operation in Band n96

| Channel Bandwidth | Allowed NREF |
| --- | --- |
| 20 MHz | 7956681, 797000, 798332, 799668, 801000, 802332, 803668, 805000, 806332, 807668, 809000, 810332, 811668, 813000, 814332, 815668, 817000, 818332, 819668, 821000, 822332, 823668, 825000, 826332, 827668, 829000, 830332, 831668, 833000, 834332, 835668, 837000, 838332, 839668, 841000, 842332, 843668, 845000, 846332, 847668, 849000, 850332, 851668, 853000, 854332, 855668, 857000, 858332, 859668, 861000, 862332, 863668, 865000, 866332, 867668, 869000, 870332, 871668, 873000, 874332 |
| 40 MHz | 797668, 800332, 803000, 805668, 808332, 811000, 813668, 816332, 819000, 821668, 824332, 827000, 829668, 832332, 835000, 837668, 840332, 843000, 845668, 848332, 851000, 853668, 856332, 859000, 861668, 864332, 867000, 869668, 872332 |
| 60 MHz | 798332, 799668, 803668, 805000, 809000, 810332, 814332, 815668, 819668, 821000, 825000, 826332, 830332, 831668, 835668, 837000, 841000, 842332, 846332, 847668, 851668, 853000, 857000, 858332, 862332, 863668, 867668, 869000, 873000 |
| 80 MHz | 799000, 804332, 809668, 815000, 820332, 825668, 831000, 836332, 841668, 847000, 852332, 857668, 863000, 868332 |
| 100 MHz | 799668, 803668, 810332, 814332, 821000, 825000, 831668, 835668, 842332, 846332, 853000, 857000,863668, 867668, 869000, 870332, 871668 |
| NOTE 1: NREF is only applicable for DL only operation |  |

Table 5.4.2.3-4: Allowed NREF (NR-ARFCN) for operation in Band n102

| Channel Bandwidth | Allowed NREF |
| --- | --- |
| 20 MHz | 7956681, 797000, 798332, 799668, 801000, 802332, 803668, 805000, 806332, 807668, 809000, 810332, 811668, 813000, 814332, 815668, 817000, 818332, 819668, 821000, 822332, 823668, 825000, 826332, 827668 |
| 40 MHz | 797668, 800332, 803000, 805668, 808332, 811000, 813668, 816332, 819000, 821668, 824332, 827000 |
| 60 MHz | 798332, 799668, 803668, 805000, 809000, 810332, 814332, 815668, 819668, 821000, 825000, 826332 |
| 80 MHz | 799000, 804332, 809668, 815000, 820332, 825668 |
| 100 MHz | 799668, 803668, 810332, 814332, 821000, 825000 |
| NOTE 1: NREF is only applicable for DL only operation |  |

For NR operating bands with 100 kHz channel raster, Enhanced channel raster is defined with ΔFRaster = 2 × ΔFGlobal. In this case every 2th NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.35 is given as <2>.

Table 5.4.2.3-5: Applicable NR-ARFCN per operating band for enhanced channel raster

| NR operating band | ΔFRaster(kHz) | UplinkRange of NREF(First – <Step size> – Last) | DownlinkRange of NREF(First – <Step size> – Last) | Mandatory support |
| --- | --- | --- | --- | --- |
| n1 | 10 | 384000 – <2> – 396000 | 422000 – <2> – 434000 | Yes |
| n2 | 10 | 370000 – <2> – 382000 | 386000 – <2> – 398000 | Yes |
| n3 | 10 | 342000 – <2> – 357000 | 361000 – <2> – 376000 | Yes |
| n5 | 10 | 164800 – <2> – 169800 | 173800 – <2> – 178800 | Yes |
| n7 | 10 | 500000 – <2> – 514000 | 524000 – <2> – 538000 |  |
| n8 | 10 | 176000 – <2> – 183000 | 185000 – <2> – 192000 |  |
| n12 | 10 | 139800 – <2> – 143200 | 145800 – <2> – 149200 |  |
| n13 | 10 | 155400 – <2> – 157400 | 149200 – <2> – 151200 |  |
| n14 | 10 | 157600 – <2> – 159600 | 151600 – <2> – 153600 |  |
| n18 | 10 | 163000 – <2> – 166000 | 172000 – <2> – 175000 |  |
| n20 | 10 | 166400 – <2> – 172400 | 158200 – <2> – 164200 |  |
| n24 | 10 | 325300 – <2> – 332100 | 305000 – <2> – 311800 |  |
| n25 | 10 | 370000 – <2> – 383000 | 386000 – <2> – 399000 | Yes |
| n26 | 10 | 162800 – <2> – 169800 | 171800 – <2> – 178800 | Yes |
| n28 | 10 | 140600 – <2> – 149600 | 151600 – <2> – 160600 | Yes |
| n29 | 10 | N/A | 143400 – <2> – 145600 |  |
| n30 | 10 | 461000 – <2> – 463000 | 470000 – <2> – 472000 |  |
| n34 | 10 | 402000 – <2> – 405000 | 402000 – <2> – 405000 |  |
| n38 | 10 | 514000 – <2> – 524000 | 514000 – <2> – 524000 |  |
| n39 | 10 | 376000 – <2> – 384000 | 376000 – <2> – 384000 |  |
| n40 | 10 | 460000 – <2> – 480000 | 460000 – <2> – 480000 |  |
| n50 | 10 | 286400 – <2> – 303400 | 286400 – <2> – 303400 |  |
| n53 | 10 | 496700 – <2> – 499000 | 496700 – <2> – 499000 |  |
| n65 | 10 | 384000 – <2> – 402000 | 422000 – <2> – 440000 |  |
| n66 | 10 | 342000 – <2> – 356000 | 422000 – <2> – 440000 | Yes |
| n67 | 10 | N/A | 147600 – <2> – 151600 |  |
| n68 | 10 | 139600 – <2> – 145600 | 150600 – <2> – 156600 |  |
| n70 | 10 | 339000 – <2> – 342000 | 399000 – <2> – 404000 |  |
| n71 | 10 | 132600 – <2> – 139600 | 123400 – <2> – 130400 | Yes |
| n74 | 10 | 285400 – <2> – 294000 | 295000 – <2> – 303600 |  |
| n75 | 10 | N/A | 286400 – <2> – 303400 |  |
| n80 | 10 | 342000 – <2> – 357000 | N/A |  |
| n81 | 10 | 176000 – <2> – 183000 | N/A |  |
| n82 | 10 | 166400 – <2> – 172400 | N/A |  |
| n83 | 10 | 140600 – <2> –149600 | N/A |  |
| n84 | 10 | 384000 – <2> – 396000 | N/A |  |
| n85 | 10 | 139600 – <2> – 143200 | 145600 – <2> – 149200 | Yes |
| n86 | 10 | 342000 – <2> – 356000 | N/A |  |
| n89 | 10 | 164800 – <2> – 169800 | N/A |  |
| n90 | 10 | 499200 – <2> – 538000 | 499200 – <2> – 538000 |  |
| n91 | 10 | 166400 – <2> – 172400 | 285400 – <2> – 286400 |  |
| n92 | 10 | 166400 – <2> – 172400 | 286400 – <2> – 303400 |  |
| n93 | 10 | 176000 – <2> – 183000 | 285400 – <2> – 286400 |  |
| n94 | 10 | 176000 – <2> – 183000 | 286400 – <2> – 303400 |  |
| n95 | 10 | 402000 – <2> – 405000 | N/A |  |
| n97 | 10 | 460000 – <2> – 480000 | N/A |  |
| n98 | 10 | 376000 – <2> – 384000 | N/A |  |
| n99 | 10 | 325300 – <2> – 332100 | N/A |  |
| n100 | 10 | 174880 – <2> – 176000 | 183880 – <2> – 185000 |  |
| n101 | 10 | 380000 – <2> – 382000 | 380000 – <2> – 382000 |  |
| n105 | 10 | 132600 – <2> – 140600 | 122400 – <2> – 130400 |  |
| n109 | 10 | 140600 – <2> – 146600 | 286400 – <2> – 303400 |  |
| NOTE 1: The channel numbers that designate carrier frequencies so close to the operating band edges that the carrier extends beyond the operating band edge shall not be used. These channel numbers shall also be such that the minimum guard band for each channel bandwidth and SCS specified in Table 5.3.3-1 are met for carriers located at the upper or lower edge of an operating band. |  |  |  |  |

### 5.4.3 Synchronization raster

#### 5.4.3.1 Synchronization raster and numbering

The synchronization raster indicates the frequency positions of the synchronization block that can be used by the UE for system acquisition when explicit signalling of the synchronization block position is not present.

A global synchronization raster is defined for all frequencies. The frequency position of the SS block is defined as SSREF with corresponding number GSCN. The parameters defining the SSREF and GSCN for all the frequency ranges are in Table 5.4.3.1-1 for above 3 MHz channel bandwidth and in Table 5.4.3.1-2 for 3 MHz channel bandwidth.

For band n100, additional parameters defining the SSREF and GSCN are specified in Table 5.4.3.1-3.

The resource element corresponding to the SS block reference frequency SSREF is given in clause 5.4.3.2. The synchronization raster and the subcarrier spacing of the synchronization block is defined separately for each band.

The synchronization raster and the corresponding SS block do not cover all possible RF channel bandwidths and locations on Enhanced channel raster.

Table 5.4.3.1-1: GSCN parameters for the global frequency raster for above 3 MHz channel bandwidth

| Frequency range | SS Block frequency position SSREF | GSCN | Range of GSCN |
| --- | --- | --- | --- |
| 0 – 3000 MHz | N * 1200kHz + M * 50 kHz,N=1:2499, M ϵ {1,3,5} 1 | 3N + (M-3)/2 | 22 – 7498 |
| 3000 – 24250 MHz | 3000 MHz + N * 1.44 MHzN = 0:14756 | 7499 + N | 7499 – 22255 |
| NOTE 1: The default value for operating bands with which only support SCS spaced channel raster(s) is M=3.NOTE 2: GSCN=2 (corresponding to ARFCN-ValueNR = 250) is a reserved value paired with reserved operating band n200. |  |  |  |

Table 5.4.3.1-2: GSCN parameters for the global frequency for 3 MHz channel bandwidth

| Range of frequencies (MHz) | SS block frequency position SSREF | GSCN | Range of GSCN |
| --- | --- | --- | --- |
| 0 – 1000, 1432 – 1435 | N * 600 kHz + M * 50 kHz + 300 kHz,N = 1:1665, M ϵ {1,3,5},N = 2388, M ϵ {3,5} orN = 2389, M ϵ {1}(Note 1) | 26638+3N + (M-3)/2 | 26640 – 31634, 33802 – 33804 |
| NOTE 1: Only applicable for 15 PRB transmission bandwidth configuration within 3 MHz channel bandwidth with punctured PBCH defined in TS 38.211 [6] clause 7.4.3.1.NOTE 2:  SCell with 15 PRB transmission bandwidth configuration within 3 MHz channel bandwidth will be configured only with SS Block frequency positions defined in this table. |  |  |  |

Table 5.4.3.1-3: Additional GSCN parameters for band n100

| SS Block frequency position SSREF(MHz) | GSCN | Note |
| --- | --- | --- |
| 920.73 | 41637 | Only applicable for 12 PRB transmission bandwidth configuration within 3 MHz channel (with 15 PRB maximum transmission bandwidth configuration) with punctured PBCH defined in TS 38.211 [6] clause 7.4.3.1. |
| 921.45 | 41638 | Only applicable for 20 PRB transmission bandwidth configuration within 5 MHz channel (with 25 PRB maximum transmission bandwidth configuration) with unpunctured PBCH defined in TS 38.211 [6] clause 7.4.3.1. |
| NOTE 1: SCell with 12 PRB transmission bandwidth configuration within 3 MHz channel bandwidth or 20 PRB transmission bandwidth configuration within 5 MHz channel bandwidth will be configured only in band n100 and only with SS Block frequency positions defined in this table. |  |  |

## 5.4.3.2 Synchronization raster to synchronization block resource element mapping

The mapping between the synchronization raster and the corresponding resource element of the SS block is given in Table 5.4.3.2-1.

Table 5.4.3.2-1: Synchronization raster to SS block resource element mapping

| Resource element index ![](media_svg/image5.svg) [公式: k] | 120 |
| --- | --- |

![](media_svg/image5.svg) [公式: k] is the subcarrier number of SS/PBCH block defined in TS 38.211 clause 7.4.3.1 [6].

#### 5.4.3.3 Synchronization raster entries for each operating band

The synchronization raster for above 3 MHz channel bandwidth for each band is give in Table 5.4.3.3-1. The distance between applicable GSCN entries is given by the <Step size> indicated in Table 5.4.3.3-1.

Table 5.4.3.3-1: Applicable SS raster entries per operating band for above 3 MHz channel bandwidth

| NR operating band | SS Block SCS | SS Block pattern1 | Range of GSCN(First – <Step size> – Last) |
| --- | --- | --- | --- |
| n1 | 15 kHz | Case A | 5279 – <1> – 5419 |
| n2 | 15 kHz | Case A | 4829 – <1> – 4969 |
| n3 | 15 kHz | Case A | 4517 – <1> – 4693 |
| n5 | 15 kHz | Case A | 2177 – <1> – 2230 |
|  | 30 kHz | Case B | 2183 – <1> – 2224 |
| n7 | 15 kHz | Case A | 6554 – <1> – 6718 |
| n8 | 15 kHz | Case A | 2318 – <1> – 2395 |
| n12 | 15 kHz | Case A | 1828 – <1> – 1858 |
| n13 | 15 kHz | Case A | 1871 – <1> – 1885 |
| n14 | 15 kHz | Case A | 1901 – <1> – 1915 |
| n18 | 15 kHz | Case A | 2156 – <1> – 2182 |
| n20 | 15 kHz | Case A | 1982 – <1> – 2047 |
| n24 | 15 kHz | Case A | 3818 – <1> – 3892 |
|  | 30 kHz | Case B | 3824 – <1> – 3886 |
| n25 | 15 kHz | Case A | 4829 – <1> – 4981 |
| n26 | 15 kHz | Case A | 2153 – <1> – 2230 |
| n28 | 15 kHz | Case A | 1901 – <1> – 2002 |
| n29 | 15 kHz | Case A | 1798 – <1> – 1813 |
| n30 | 15 kHz | Case A | 5879 – <1> – 5893 |
| n31 | 15kHz | Case A | 1161 – <1> – 1162 |
| n34 | 15 kHz | Case A | NOTE 5 |
|  | 30 kHz | Case C | 5036 – <1> – 5050 |
| n38 | 15 kHz | Case A | NOTE 2 |
|  | 30 kHz | Case C | 6437 – <1> – 6538 |
| n39 | 15 kHz | Case A | NOTE 6 |
|  | 30 kHz | Case C | 4712 – <1> – 4789 |
| n40 | 30 kHz | Case C | 5762 – <1> – 5989 |
| n41 | 15 kHz | Case A | 6246 – <3> – 6717 |
|  | 30 kHz | Case C | 6252 – <3> – 6714 |
| n463 | 30 kHz | Case C | 8993 – <1> – 9530 |
| n48 | 30 kHz | Case C | 7884 – <1> – 7982 |
| n50 | 30 kHz | Case C | 3590 – <1> – 3781 |
| n51 | 15 kHz | Case A | 3572 – <1> – 3574 |
| n53 | 15 kHz | Case A | 6215 – <1> – 6232 |
|  | 30 KHz | Case C | 6221 – <1> – 6226 |
| n54 | 15 kHz | Case A | 4181 – <1> – 4182 |
| n65 | 15 kHz | Case A | 5279 – <1> – 5494 |
| n66 | 15 kHz | Case A | 5279 – <1> – 5494 |
|  | 30 kHz | Case B | 5285 – <1> – 5488 |
| n67 | 15 kHz | Case A | 1850 – <1> – 1888 |
| n68 | 15 kHz | Case A | 1888 – <1> – 1951 |
| n70 | 15 kHz | Case A | 4993 – <1> – 5044 |
| n71 | 15 kHz | Case A | 1547 – <1> – 1624 |
| n72 | 15 kHz | Case A | 1157 – <1> – 1159 |
| n74 | 15 kHz | Case A | 3692 – <1> – 3790 |
| n75 | 15 kHz | Case A | 3584 – <1> – 3787 |
| n76 | 15 kHz | Case A | 3572 – <1> – 3574 |
| n77 | 30 kHz | Case C | 7711 – <1> – 8329 |
| n78 | 30 kHz | Case C | 7711 – <1> – 8051 |
| n79 | 30 kHz | Case C | 8480 – <16> – 88807 |
|  |  |  | 8475 – <1> – 88848 |
| n85 | 15 kHz | Case A | 1826 – <1> – 1858 |
| n87 | 15 kHz | Case A | 1055 – <1> – 1057 |
| n88 | 15 kHz | Case A | 1061 – <1> – 1062 |
| n90 | 15 kHz | Case A | 6246 – <1> – 671710 |
|  |  |  | 6245 – <1> – 671811 |
|  | 30 kHz | Case C | 6252 – <1> – 6714 |
| n91 | 15 kHz | Case A | 3572 – <1> – 3574 |
| n92 | 15 kHz | Case A | 3584 – <1> – 3787 |
| n93 | 15 kHz | Case A | 3572 – <1> – 3574 |
| n94 | 15 kHz | Case A | 3584 – <1> – 3787 |
| n964 | 30 kHz | Case C | 9531 – <1> – 10363 |
| n100 | 15 kHz | Case A | 2303 – <1> – 2307, 4163812 |
| n101 | 15 kHz | Case A | 4754 – <1> – 4768 |
|  | 30 kHz | Case C | 4760 – <1> – 4764 |
| n1029 | 30 kHz | Case C | 9531 – <1> – 9877 |
| n104 | 30 kHz | Case C | 9882 – <7> – 10358 |
| n105 | 15 kHz | Case A | 1535 – <1> – 1624 |
| n109 | 15 kHz | Case A | 3584 – <1> – 3787 |
| NOTE 1: SS Block pattern is defined in clause 4.1 in TS 38.213 [8].NOTE 2: The applicable SS raster entries are GSCN = {6432, 6443, 6457, 6468, 6479, 6493, 6507, 6518, 6532, 6543}.NOTE 3: The following GSCN are allowed for operation in band n46: GSCN = {8996, 9010, 9024, 9038, 9051, 9065, 9079, 9093, 9107, 9121, 9218, 9232, 9246, 9260, 9274, 9288, 9301, 9315, 9329, 9343, 9357, 9371, 9385, 9402, 9416, 9430, 9444, 9458, 9472, 9485, 9499, 9513}.NOTE 4: The following GSCN are allowed for operation in band n96: GSCN = {9548, 9562, 9576, 9590, 9603, 9617,9631, 9645, 9659, 9673, 9687, 9701, 9714, 9728, 9742, 9756, 9770, 9784, 9798, 9812, 9826, 9840, 9853, 9867, 9881, 9895, 9909, 9923, 9937, 9951, 9964, 9978, 9992, 10006, 10020, 10034, 10048, 10062, 10076, 10090, 10103, 10117, 10131, 10145, 10159, 10173, 10187, 10201, 10214, 10228, 10242, 10256, 10270, 10284, 10298, 10312, 10325, 10339, 10353}.NOTE 5: The applicable SS raster entries are GSCN = {5032, 5043, 5054}NOTE 6: The applicable SS raster entries are GSCN = {4707, 4715, 4718, 4729, 4732, 4743, 4747, 4754, 4761, 4768, 4772, 4782, 4786, 4793}NOTE 7: The SS raster entries apply for channel bandwidths larger than or equal to 40 MHzNOTE 8: The SS raster entries apply for channel bandwidths smaller than 40 MHzNOTE 9: The following GSCN are allowed for operation in band n102: GSCN = {9548, 9562, 9576, 9590, 9603, 9617,9631, 9645, 9659, 9673, 9687, 9701, 9714, 9728, 9742, 9756, 9770, 9784, 9798, 9812, 9826, 9840, 9853, 9867}.NOTE 10: The SS raster entries apply for channel bandwidths larger than or equal to 10 MHz.NOTE 11: The SS raster entries apply for channel bandwidth equal to 5 MHzNOTE 12: Only applicable for 20 PRB transmission bandwidth configuration within 5 MHz channel with unpunctured PBCH defined in TS 38.211 [6] clause 7.4.3.1. |  |  |  |

The synchronization raster for channel bandwidth 3 MHz for each band is given in Table 5.4.3.3-2. The distance between applicable GSCN entries is given by the <Step size> indicated in Table 5.4.3.3-2.

Table 5.4.3.3-2: Applicable SS raster entries per operating band for 3 MHz channel bandwidth

| NR operating band | SS Block SCS | SS Block pattern1 | Range of GSCN(First – <Step size> – Last) |
| --- | --- | --- | --- |
| n5 | 15 kHz | Case A | 30987 – <1> – 31100 |
| n12 | 15 kHz | Case A | 30288 – <1> – 30359 |
| n26 | 15 kHz | Case A | 30937 – <1> – 31100 |
| n28 | 15 kHz | Case A | 30432 – <1> – 30644 |
| n31 | 15 kHz | Case A | 28955 – <1> – 28967 |
| n72 | 15 kHz | Case A | 28947 – <1> – 28959 |
| n85 | 15 kHz | Case A | 30282 – <1> – 30359 |
| n87 | 15 kHz | Case A | 28743 – <1> – 28754 |
| n88 | 15 kHz | Case A | 28752 – <1> – 28764 |
| n100 | 15 kHz | Case A | 31240 – <1> – 31242,31244 – <1> – 31253, 416372 |
| n106 | 15 kHz | Case A | 31317 – <1> – 31329 |
| n110 | 15 kHz | Case A | 33802 – <1> – 33804 |
| NOTE 1: SS Block pattern is defined in clause 4.1 in TS 38.213 [8].NOTE 2: Only applicable for 12 PRB transmission bandwidth configuration within 3 MHz channel with punctured PBCH defined in TS 38.211 [6] clause 7.4.3.1. |  |  |  |

### 5.4.4 TX–RX frequency separation

The default TX channel (carrier centre frequency) to RX channel (carrier centre frequency) separation for operating bands is specified in Table 5.4.4-1.

Table 5.4.4-1: UE TX-RX frequency separation

| NR Operating Band | TX – RX  carrier centre frequency separation |
| --- | --- |
| n1 | 190 MHz |
| n2 | 80 MHz |
| n3 | 95 MHz |
| n5 | 45 MHz |
| n7 | 120 MHz |
| n8 | 45 MHz |
| n12 | 30 MHz |
| n13 | -31 MHz |
| n14 | -30 MHz |
| n18 | 45 MHz |
| n20 | -41 MHz |
| n24 | -101.5, -120.5 MHz |
| n25 | 80 MHz |
| n26 | 45 MHz |
| n28 | 55 MHz |
| n30 | 45 MHz |
| n31 | 10 MHz |
| n65 | 190 MHz |
| n66 | 400 MHz |
| n68 | 55 MHz |
| n70 | 300 MHz |
| n71 | -46 MHz |
| n72 | 10 MHz |
| n74 | 48 MHz |
| n85 | 30 MHz |
| n87 | 10 MHz |
| n88 | 10 MHz |
| n91 | 570 MHz – 595 MHz(NOTE 2) |
| n92 | 575 MHz – 680 MHz (μ = 0)580 MHz – 675 MHz (μ = 1)(NOTE 2) |
| n93 | 517 MHz – 547 MHz(NOTE 2) |
| n94 | 522 MHz – 632 MHz (μ = 0)527 MHz – 627 MHz (μ = 1)(NOTE 2) |
| n100 | 45 MHz |
| n105 | -51 MHz |
| n106 | 39 MHz |
| n109 | 704 MHz - 809 MHz (μ = 0)709 MHz - 804 MHz (μ = 1)(NOTE 2) |
| n110 | 40 MHz, 42 MHz |
| NOTE 1: VoidNOTE 2: The range of TX-RX frequency separation given paired UL and DL channel bandwidths BWUL and BWDL is given by the respective lower and upper limit FDL_low – FUL_high + 0.5(BWDL + BWUL) and FDL_high – FUL_low – 0.5(BWDL + BWUL). The UL and DL channel bandwidth combinations specified in Table 5.3.5-1 and 5.3.6-1 depend on the subcarrier spacing configuration μ [6]. |  |

## 5.4A Channel arrangement for CA

### 5.4A.1 Channel spacing for CA

For intra-band contiguous carrier aggregation with two or more component carriers, the nominal channel spacing between two adjacent NR component carriers is defined as the following unless stated otherwise:

For NR operating bands with a 100 kHz or 10 kHz channel raster:

![](media_svg/image9.svg) [公式≈: _{Nominal}_{channel}_{spacing}_{=}^{⋅}_{⋅}_{⋅}_{√}^{BW}Channel(1)^{+}^{BW}Channel(2)_{0}^{−}_{.}_{6}^{2}^{GB}Channel(1)^{−}^{GB}Channel(2)^{∂}_{∂}_{∂}_{∃}_{0}_{.}_{3}_{[MHz]}]

while for NR operating bands without a 100 kHz channel raster:

![](media_svg/image10.svg) [公式≈: _{Nominal}_{channel}_{spacing}_{=}^{⋅}_{⋅}_{⋅}_{√}^{BW}Channel(1)^{+}^{BW}Channel_{0}_{.}(_{015}2)^{−}_{*}^{2}_{2}^{GB}_{n}_{+}_{1}Channel(1)^{−}^{GB}Channel(2)^{∂}_{∂}_{∂}_{∃}_{0}_{.}_{015}_{*}_{2}n_{[MHz]}]

with

n = µ0

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective NR component carriers according to Table 5.3.2-1 with values in MHz, μ0  is the largest μ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths according to Table 5.3.5-1 and GBChannel(i) is the minimum guard band for channel bandwidth i according to Table 5.3.3-1 for the said μ value with μ as defined in TS 38.211. In case there is no common μ value for both of the channel bandwidths, μ0=1 is selected and GBChannel(i) is the minimum guard band for channel bandwidth i according to Table 5.3.3-1 for μ=1 with μ as defined in TS 38.211.

The bandwidth BWChannel(i) for determining the nominal channel spacing is the UE specific channel bandwidth, if configured by ServingCellConfig, the channel bandwidth of the NR component carrier otherwise.

The channel spacing for intra-band contiguous carrier aggregation can be adjusted to any multiple of least common multiple of channel raster, the enhanced channel raster if supported, and sub-carrier spacing less than the nominal channel spacing to optimize performance in a particular deployment scenario.

For intra-band contiguous carrier aggregation in NR bands restricted to operation with shared-spectrum channel access, the maximum deviation from the nominal channel spacing is 300 kHz.

For intra-band non-contiguous carrier aggregation, the channel spacing between two NR component carriers in different sub-blocks shall be larger than the nominal channel spacing defined in this clause.

### 5.4A.2 Channel raster for CA

For inter-band and intra-band carrier aggregation, the channel raster requirements in clause 5.4.2 apply for each operating band.

### 5.4A.3 Synchronization raster for CA

For inter-band and intra-band carrier aggregation, the synchronization raster requirements in clause 5.4.3 apply for each operating band.

### 5.4A.4 Tx-Rx frequency separation for CA

For inter-band carrier aggregation, the Tx-Rx frequency separation requirements in clause 5.4.4 apply for each operating band.

For intra-band carrier aggregation, the same TX-RX frequency separation as specified in Table 5.4.4-1 is applied to PCC and SCC, respectively.

## 5.4B Reserved

## 5.4C Reserved

## 5.4D Reserved

## 5.4E Channel arrangement for V2X

### 5.4E.1 Channel spacing

For NR V2X, the channel spacing requirements in clause 5.4.1 apply for each operating band.

### 5.4E.1A Channel spacing for Sidelink CA

For NR sidelink CA operation, the channel spacing requirements in clause 5.4A.1 apply.

### 5.4E.1F Channel spacing for Sidelink Unlicensed

For NR SL-U operation, the channel spacing requirements in clause 5.4.1 apply for each operating band.

### 5.4E.2 Channel raster

#### 5.4E.2.1 NR-ARFCN and channel raster

For NR V2X, the NR-ARFCN and channel raster requirements in clause 5.4.2.1 apply for each operating band.

For NR V2X UE, the reference frequency can be shifted by configuration.

FREF_V2X = FREF + Δshift + N * 5 kHz

where

Δshift = 0 kHz or 7.5 kHz indicated in IE (frequencyShift7p5khz), and

N can be set as one of following values {-1, 0, 1}, which are signalled by the network in higher layer parameters or configured by pre-configuration parameters.

#### 5.4E.2.1A Void

#### 5.4E.2.1F Void

#### 5.4E.2.2 Channel raster to resource element mapping

For NR V2X, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each operating band.

#### 5.4E.2.2A Void

#### 5.4E.2.2F Void

#### 5.4E.2.3 Channel raster entries for each operating band

For NR V2X, the channel raster entries requirements in clause 5.4.2.3 apply for each operating band.

The RF channel positions on the channel raster in each NR V2X operating band are given through the applicable NR-ARFCN in Table 5.4.2.3-1, using the channel raster to resource element mapping in clause 5.4.2.2.

For NR V2X operating band n47, ΔFRaster = I × ΔFGlobal, where I ϵ {1}. Every Ith NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.3-1 is given as <I>.

#### 5.4E.2.3A Void

#### 5.4E.2.3F Void

5.4E.2A Channel raster for Sidelink CA

5.4E.2A.1 NR-ARFCN and channel raster for Sidelink CA

For NR SL intra-band contiguous CA operation, the NR-ARFCN and channel raster requirements in clause 5.4E.2.1 apply for each component carrier.

5.4E.2A.2 Channel raster to resource element mapping for Sidelink CA

For NR SL intra-band contiguous CA operation, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each component carrier.

5.4E.2A.3 Channel raster entries for each operating band for Sidelink CA

For NR SL intra-band contiguous CA operation, the channel raster entries requirements in clause 5.4E.2.3 apply for each component carrier.

5.4E.2F Channel raster for Sidelink Unlicensed

5.4E.2F.1 NR-ARFCN and channel raster for Sidelink Unlicensed

For NR SL-U operation, the general requirements in clause 5.4.2 are applied.

NR-ARFCN and channel raster requirements in clause 5.4.2.1 are applied for NR SL-U with following exception:

- N*5kHz/7.5kHz frequency raster shift, which can be used in NR V2X in band n47 is not defined for NR SL-U operation in bands n46, n96, n102.

- Channel raster entries for each operating band requirements in clause 5.4.2.3 are applied for NR SL-U with following exception: Channel raster points for 10MHz CBW in band n46 as defined in Table 5.4.2.3-2 are not applicable for NR SL-U.

5.4E.2F.2 Channel raster to resource element mapping for Sidelink Unlicensed

The mapping between the RF reference frequency on the channel raster and the corresponding resource element is given in Table 5.4.2.2-1 and can be used to identify the RF channel position. The mapping depends on the total number of RBs that are allocated in the channel and applies to both Tx and Rx for SL. The mapping must apply to at least one numerology supported by the UE.

5.4E.2F.3 Channel raster entries for Sidelink Unlicensed

For NR SL-U operation, the channel raster entries requirements in clause 5.4.2.3 apply for each operating band.

### 5.4E.3 Synchronization raster for V2X

There is no synchronization raster definition for NR V2X for both licensed bands and unlicensed bands.

### 5.4E.3A Synchronization raster for Sidelink CA

There is no synchronization raster definition for NR SL CA operating bands.

### 5.4E.3F Synchronization raster for Sidelink Unlicensed

There is no synchronization raster definition for NR SL-U operating bands n46, n96, n102.










## 5.4I Channel arrangement for (e)RedCap

### 5.4I.1 Channel spacing for (e)RedCap

For (e)RedCap UEs, the channel spacing requirements in clause 5.4.1 apply for each operating band.

### 5.4I.2 Channel raster for (e)RedCap

#### 5.4I.2.1 NR-ARFCN and channel raster

For (e)RedCap UEs, the NR-ARFCN and channel raster requirements in clause 5.4.2.1 apply for each operating band.

#### 5.4I.2.2 Channel raster to resource element mapping

For (e)RedCap UEs, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each operating band.

#### 5.4I.2.3 Channel raster entries for each operating band

For (e)RedCap UEs, the RF channel positions on the channel raster in each NR operating band are given through the applicable NR-ARFCN in Table 5.4.2.31 and additional intermediary NR-ARFCN with a step size of <2> for operating bands that are included in Table 5.4.2.3-1 with a step size of <20>, using the channel raster to resource element mapping in clause 5.4I.2.2.

For NR operating bands included in Table 5.4.2.3-1 with a step size of <20>, the channel raster for (e)RedCap UEs is defined with ΔFRaster = 2 × ΔFGlobal. In this case every 2nd NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster is given as <2>, every 10th of these channel raster entries coincides with entries defined in Table 5.4.2.3-1 for this operating band.

### 5.4I.3 Synchronization raster for (e)RedCap

For (e)RedCap UEs, the synchronization raster requirements in clause 5.4.3 apply for each operating band. The synchronization raster and the corresponding SS block do not cover all possible RF channel bandwidths and locations on the channel raster defined in sub-clause 5.4I.2.

### 5.4I.4 Tx-Rx frequency separation for (e)RedCap

For (e)RedCap UEs, the Tx-Rx frequency separation requirements in clause 5.4.4 apply for each operating band.
