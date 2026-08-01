# TS 38.101 38101-1-j60_s00-0504

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

The present document establishes the minimum RF requirements for NR User Equipment (UE) operating on frequency Range 1.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

For a specific reference, subsequent revisions do not apply.

For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 38.101-2: "NR; User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone".

[3]3GPP TS 38.101-3: "NR; User Equipment (UE) radio transmission and reception; Part 3: Range 1 and Range 2 Interworking operation with other radios".

[4]3GPP TS 38.521-1: "NR; User Equipment (UE) conformance specification; Radio transmission and reception; Part 1: Range 1 Standalone".

[5]Recommendation ITU-R M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000".

[6]3GPP TS 38.211: "NR; Physical channels and modulation".

[7]3GPP TS 38.331: "Radio Resource Control (RRC) protocol specification".

[8]3GPP TS 38.213: "NR; Physical layer procedures for control".

[9]ITU-R Recommendation SM.329, "Unwanted emissions in the spurious domain".

[10]3GPP TS 38.214: "NR; Physical layer procedures for data".

[11]3GPP TS 36.101: Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception;

[12]ETSI TS 102 792: "Intelligent Transport Systems (ITS); Mitigation techniques to avoid interference between European CEN Dedicated Short Range Communication (CEN DSRC) equipment and Intelligent Transport Systems (ITS) operating in the 5 GHz frequency range".

[13]3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[14]3GPP TS 37.213: "Physical layer procedures for shared spectrum channel access".

[15]3GPP TS 38.306: "NR; User Equipment (UE) radio access capabilities".

[16]3GPP TS 38.104: "NR; Base Station (BS) radio transmission and reception".

[17]3GPP TS 23.256: "Support of Uncrewed Aerial Systems (UAS) connectivity, identification and tracking; Stage 2".

[18]ECC Decision(22)07, "Harmonised technical conditions for the usage of aerial UE for communications based on LTE and 5G NR in the bands 703-733 MHz, 832-862 MHz, 880-915 MHz, 1710-1785 MHz, 1920-1980 MHz, 2500-2570 MHz and 2570-2620 MHz harmonised for MFCN", 7 March 2025.

[19]ECC Decision(20)02: "Harmonised use of the paired frequency bands 874.4-880.0 MHz and 919.4-925.0 MHz and of the unpaired frequency band 1900-1910 MHz for Railway Mobile Radio (RMR)"

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

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

NOTE:Carriers aggregated in each band can be contiguous or non-contiguous.

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

NOTE:Vehicular UE does not refer to other UE form factors placed inside the vehicle.

Wideband operation: For a UE that supports shared spectrum channel access, wideband operation refers to operation within a channel larger than 20 MHz in which intra-cell guard bands may be configured to distinguish individual RB-sets

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

ΔFGlobalGranularity of the global frequency raster

ΔFRasterBand dependent channel raster granularity

ΔfOOBΔ Frequency of Out Of Band emission

ΔFTX-RXMaximum deviation to the Tx-Rx carrier center frequency separation for asymmetric uplink/downlink channel bandwidth operation

∆MPRcAllowed Maximum Power Reduction relaxation for serving cell c

ΔPPowerClassAdjustment to maximum output power for a given power class

RBThe starting frequency offset between the allocated RB and the measured non-allocated RB

ΔRIB,cAllowed reference sensitivity relaxation due to support for inter-band CA operation, for serving cell c

ΔRIBCAllowed relaxation to the power class 3 reference sensitivity level due to support for intra-band contiguous CA operation

ΔRIBNCAllowed relaxation to the power class 3 reference sensitivity level due to support for intra-band non-contiguous CA operation

ΔRIB,4RReference sensitivity adjustment due to support for 4 antenna ports

ΔRIB,8RReference sensitivity adjustment due to support for 8 antenna ports

ΔR1RReference sensitivity adjustment due to support for 1 antenna ports

ΔRLP-WUSReference sensitivity adjustment for specific bands with FDL_low higher than 2400 MHz

ΔRXR,2RReference sensitivity adjustment for two antenna ports XR UEs on bands defined in Table 7.3.2-2b

ΔShiftChannel raster offset

TCAllowed operating band edge transmission power relaxation

TC,cAllowed operating band edge transmission power relaxation for serving cell c

ΔTIB,cAllowed maximum configured output power relaxation due to support for inter-band CA operation, inter-band NR-DC operation and due to support for SUL operations, for serving cell c

BWChannelChannel bandwidth

BWChannel,blockSub-block bandwidth, expressed in MHz. BWChannel,block= Fedge,block,high- Fedge,block,low

BWChannel_CAThe intra-band contiguous CA aggregated channel bandwidth, expressed in MHz. BWChannel_CA = Fedge,high - Fedge,low.

BWSum_CAThe intra-band contiguous CA aggregated bandwidth defined as the sum of each CC’s channel bandwidth, expressed in MHz.

BWChannel,maxMaximum channel bandwidth supported among all bands in a release

BWGBmax(GBChannel,low, GBChannel,high)

BWDLChannel bandwidth for DL

BWULChannel bandwidth for UL

BWinterfererBandwidth of the interferer

Ceil(x)Rounding upwards; ceil(x) is the smallest integer such that ceil(x) ≥ x

Floor(x)Rounding downwards; floor(x) is the greatest integer such that floor(x) ≤ x

FCCenter frequency of a carrier for a numerology defined by the RF reference frequency on the channel raster mapped to the carrier according to sub-clause 5.4.2.2

FC,block, highFc of the highest transmitted/received carrier in a sub-block

FC,block, lowFc of the lowest transmitted/received carrier in a sub-block

FC,lowThe Fc of the lowest carrier, expressed in MHz

FC,highThe Fc of the highest carrier, expressed in MHz

FDL_lowThe lowest frequency of the downlink operating band

FDL_highThe highest frequency of the downlink operating band

FUL_lowThe lowest frequency of the uplink operating band

FUL_highThe highest frequency of the uplink operating band

Fedge,block,lowThe lower sub-block edge, where Fedge,block,low = FC,block,low - Foffset, low.

Fedge,block,highThe upper sub-block edge, where Fedge,block,high = FC,block,high + Foffset, high.

Fedge, lowThe lower edge of aggregated channel bandwidth, expressed in MHz. Fedge,low = FC,low - Foffset,low.

Fedge, highThe higher edge of aggregated channel bandwidth, expressed in MHz. Fedge,high = FC,high + Foffset,high.

FInterferer (offset)Frequency offset of the interferer (between the center frequency of the interferer and the carrier frequency of the carrier measured). For intra-band contiguous CA, the FInterferer (offset) is the frequency separation of the center frequency of the carrier closest to the interferer and the center frequency of the interferer

FInterfererFrequency of the interferer

FIoffsetFrequency offset of the interferer (between the center frequency of the interferer and the closest edge of the carrier measured)

FoffsetFrequency offset from FC,high to the higher edge or FC,low to the lower edge.

Foffset,highFrequency offset from FC,high to the upper UE RF Bandwidth edge, or from FC,block, high to the upper sub-block edge

Foffset,lowFrequency offset from FC,low to the lower UE RF Bandwidth edge, or from FC,block, low to the lower sub-block edge

FOOBThe boundary between the NR out of band emission and spurious emission domains

FREFRF reference frequency

FREF-OffsOffset used for calculating FREF

FREF, shiftRF reference frequency for Supplementary Uplink (SUL) bands, the uplink of all FDD bands, and TDD bands

Fuw (offset)The frequency separation of the center frequency of the carrier closest to the interferer and the center frequency of the interferer

Gn100post connectorDeclared value of the post chipset unit antenna connector gain for band n100, used for conversion of the radiated requirement into a conducted requirement (see principles described in annex M)

Gn101post connector Declared value of the post chipset unit antenna connector gain for band n101, used for conversion of the radiated requirement into a conducted requirement (see principles described in annex M)

GBChannelMinimum guard band defined in clause 5.3.3, expressed in kHz

GBChannel(i)Minimum guard band defined in clause 5.3.3 of carrier i

GBChannel,lowMinimum guard band defined in clause 5.3.3 for the lowest assigned component carrier in clause 5.3A.3

GBChannel,highMinimum guard band defined in clause 5.3.3 for the highest assigned component carrier in clause 5.3A.3

LCRBTransmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resources blocks

LCRB_aggIntra-band contiguous CA aggregated transmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resources blocks,  for contiguous CA component carrier 1 to j, where μ is defined in TS 38.211 [6]LCRB_agg=i=1jLCRBi*2μi

Max()The largest of given numbers

Min()The smallest of given numbers

Physical resource block number

NRACLRNR ACLR

NRBTransmission bandwidth configuration, expressed in units of resource blocks

NRB_aggThe number of the aggregated RBs within the fully allocated aggregated channel bandwidth

for carrier 1 to j, where μ is defined in TS 38.211 [6]NRB_agg=i=1jNRBi*2μi

NRB,cThe transmission bandwidth configuration of component carrier c, expressed in units of resource blocks

for carrier j, where μ is defined in TS 38.211 [6]NRB,cj=NRBj*2μj

NRB,LP-WUSTransmission bandwidth configuration for LP-WUS, expressed in units of resource blocks

NRB,largest BWThe largest transmission bandwidth configuration of the component carriers in the bandwidth combination, expressed in units of resource blocks

NRB,lowThe transmission bandwidth configurations according to Table 5.3.2-1 for the lowest assigned component carrier in clause 5.3A.3

NRB,highThe transmission bandwidth configurations according to Table 5.3.2-1 for the highest assigned component carrier in clause 5.3A.3

NREFNR Absolute Radio Frequency Channel Number (NR-ARFCN)

NREF-OffsOffset used for calculating NREF

PCMAXThe configured maximum UE output power

PCMAX, cThe configured maximum UE output power for serving cell c

PCMAX, f, cThe configured maximum UE output power for carrier f of serving cell c in each slot

PEIRPUE Effective Isotropic Radiated Power (EIRP)

PEMAXMaximum allowed UE output power signalled by higher layers

PEMAX, cMaximum allowed UE output power signalled by higher layers for serving cell c

PInterfererModulated mean power of the interferer

Plargest BWPower of the largest transmission bandwidth configuration of the component carriers in the bandwidth combination

PPowerClassThe nominal UE power (i.e., no tolerance)

Pmax,c,ACMaximum output power defined as the sum of measurement of all antenna connectors

Pmax,c,TABCMaximum carrier output power defined as the sum of measurement of all TAB connectors

Prated,c,ACRated maximum output power defined as the sum of power over all antenna connectors

Prated,c,TABCRated maximum output power defined as the sum of power over all TAB connectors

P-MPRcPower Management Maximum Power Reduction for serving cell c

PRBThe transmitted power per allocated RB, measured in dBm

PREFSENS_SL The REFSENS power for Sidelink

PUMAXThe measured configured maximum UE output power

PuwPower of an unwanted DL signal

PwPower of a wanted DL signal

Rext_lowThe lower-sided extension ratio for NRB and for the boundary of OOBE & Spurious emissions shifted

Rext_highThe higher-sided extension ratio for NRB and for the boundary of OOBE & Spurious emissions shifted

RBstartThe lowest RB index of transmitted resource blocks

RBstart_CAThe lowest RB index of transmitted resource blocks for intra-band contiguous CA

SCScSCS for the component carrier c, expressed in kHz

SCSlargest BWSCS for the largest transmission bandwidth configuration of the component carriers in the bandwidth combination, expressed in kHz

SCSlowSCS for the lowest assigned component carrier in clause 5.3A.3, expressed in kHz

SCShighSCS for the highest assigned component carrier in clause 5.3A.3, expressed in kHz

tpTransient Period value signalled by the UE

tpstartStart position of transient period relative to the symbol boundary

T(PCMAX, f, c)Tolerance for applicable values of PCMAX, f, c for configured maximum UE output power for carrier f of serving cell c

TL,cAbsolute value of the lower tolerance for the applicable operating band as specified in clause 6.2.1

SSREFSS block reference frequency position

UTRAACLRUTRA ACLR

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

ACLRAdjacent Channel Leakage Ratio

ACSAdjacent Channel Selectivity

A-MPRAdditional Maximum Power Reduction

ASCSAdjacent Subcarrier selectivity

ATGAir-To-Ground

BSBase Station

BWBandwidth

BWPBandwidth Part

CACarrier Aggregation

CA_nX-nYInter-band CA of component carrier(s) in one sub-block within Band nX and component carrier(s) in one sub-block within Band nY where nX and nY are the applicable NR operating bands

CCComponent Carriers

CGCarrier Group

CP-OFDMCyclic Prefix-OFDM

CWContinuous Wave

DCDual Connectivity

DFT-s-OFDMDiscrete Fourier Transform-spread-OFDM

DM-RSDemodulation Reference Signal

DTXDiscontinuous Transmission

E-UTRAEvolved UTRA

EIRPEquivalent Isotropically Radiated Power

(e)RedCapRedcap or eRedCap

eRedCapenhanced Reduced Capability

EVMError Vector Magnitude

FARFalse Alarm Rate

FRFrequency Range

FRCFixed Reference Channel

FRMCSFuture Railway Mobile Communication System

FWAFixed Wireless Access

GSCNGlobal Synchronization Channel Number

HDHalf Duplex

IBBIn-band Blocking

IDFTInverse Discrete Fourier Transformation

ITSIntelligent Transportation System

ITURRadiocommunication Sector of the International Telecommunication Union

LP-WURLow Power-Wake Up Receiver

LP-WUSLow Power-Wake Up Signal

LP-SSLow Power-Synchronization Signal

LRLP-WUR

MBWMeasurement bandwidth

MCGMaster Cell Group

MDRMiss-Detection Rate

MOPMaximum Output Power

MPRAllowed maximum power reduction

MRMain Radio

MSDMaximum Sensitivity Degradation

NRNew Radio

NR-ARFCNNR Absolute Radio Frequency Channel Number

NSNetwork Signalling

OCNGOFDMA Channel Noise Generator

OOBOut-of-band

OOKOn-Off keying

P-MPRPower Management Maximum Power Reduction

PRBPhysical Resource Block

PSPublic Safety

PSBCHPhysical Sidelink Broadcast CHannel

PSCCHPhysical Sidelink Control CHannel

PSFCHPhysical Sidelink Feedback CHannel

PSSCHPhysical Sidelink Shared CHannel

QAMQuadrature Amplitude Modulation

REResource Element

REFSENSReference Sensitivity

RedCapReduced Capability

RFRadio Frequency

RMRRailway Mobile Radio

RMSRoot Mean Square (value)

RSRPReference Signal Receiving PowerRxReceiver

RxReceiver

SCSingle Carrier

SCGSecondary Cell Group

SCSSubcarrier spacing

SDLSupplementary Downlink

SEMSpectrum Emission Mask

SLSidelink

SL-MIMOSidelink-Multiple Antenna transmission

SL-USidelink at unlicensed band

SNRSignal-to-Noise Ratio

SRSSounding Reference Symbol

SSSynchronization Symbol

S-SSBSidelink Synchronization Signal Block

SULSupplementary uplink

TABTransceiver Array Boundary

TAETime Alignment Error

TAGTiming Advance Group

TxTransmitter

TxDTx Diversity

UASUncrewed Aircraft Systems

UAVUncrewed Aerial Vehicle

UL MIMOUplink Multiple Antenna transmission

ULFPTxUplink Full Power Transmission

USSUAS Service Supplier

V2XVehicle to Everything

XReXtended Reality

## 4General

## 4.1Relationship between minimum requirements and test requirements

The present document is a Single-RAT specification for NR UE, covering RF characteristics and minimum performance requirements. Conformance to the present specification is demonstrated by fulfilling the test requirements specified in the conformance specification 3GPP TS 38.521-1 [4].

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification TS 38.521-1 [4] defines test tolerances. These test tolerances are individually calculated for each test. The test tolerances are used to relax the minimum requirements in this specification to create test requirements. For some requirements, including regulatory requirements, the test tolerance is set to zero.

The measurement results returned by the test system are compared - without any modification - against the test requirements as defined by the shared risk principle.

The shared risk principle is defined in Recommendation ITUR M.1545 [5].

## 4.2Applicability of minimum requirements

a)In this specification the Minimum Requirements are specified as general requirements and additional requirements. Where the Requirement is specified as a general requirement, the requirement is mandated to be met in all scenarios

b)For specific scenarios for which an additional requirement is specified, in addition to meeting the general requirement, the UE is mandated to meet the additional requirements.

c)The spurious emissions power requirements are for the long-term average of the power. For the purpose of reducing measurement uncertainty it is acceptable to average the measured power over a period of time sufficient to reduce the uncertainty due to the statistical nature of the signal

d)All the requirements for intra-band contiguous and non-contiguous CA apply under the assumption of the same slot format indicated by TDD-UL-DL-ConfigurationCommon and TDD-UL-DL-ConfigurationDedicated in the PCell and SCells for NR SA.

e)The requirements for Tx diversity are applied for UE which indicates Tx diversity capability by IE txDiversity-r16, txDiversity2Tx-r18 or txDiversity4Tx-r18. 2Tx requirements for TxD should be applied to UE indicating txDiversity-r16 or txDiversity2Tx-r18, and 4Tx requirements should be applied to UE indicating txDiversity4Tx-r18.

f)All the requirements for intra-band contiguous SL CA apply under the assumption of the same subcarrier spacing for SL CA.

## 4.3Specification suffix information

Unless stated otherwise, the suffixes shown in Table 4.3-1 are used for indicating at 2nd level clause. For shared spectrum channel access, suffixes A, B, and D are used for indicating at 3rd level clause. For V2X, suffixes A and F are used for indicating at 3rd level clause.

Table 4.3-1: Definition of suffixes

A terminal which supports the above features needs to meet both the general requirements and the additional requirement applicable to the additional clause (suffixes A to L) in clauses 5, 6 and 7. Where there is a difference in requirement between the general requirements and the additional clause requirements (suffixes A to L) in clauses 5, 6 and 7, the tighter requirements are applicable unless stated otherwise in the additional clause.

A terminal which supports advanced V2X services, public safety services and other commercial use cases related to NR sidelink operation shall meet all of the separate corresponding requirements in suffix E.

For a terminal that supports SUL for the band combination specified in Table 5.2C-1, the current version of the specification assumes the terminal is configured with active transmission either on UL carrier or SUL carrier at any time in one serving cell and the UE requirements for single carrier shall apply for the active UL or SUL carrier accordingly.

For a terminal that supports SUL band combinations specified in Table 5.2C-2, Table 5.2C-3 and Table 5.2C-4, the current version of the specification assumes the terminal is configured with active transmission either on UL carrier(s) or SUL carrier at any time, and the UE requirements for the active CA configuration or SUL carrier shall apply accordingly.

For a terminal that supports public safety service using sidelink, the minimum requirements are applicable when

-The UE is associated with a serving cell on PS carrier, or

-The UE is not associated with a serving cell on the PS carrier and is provisioned with the preconfigured radio parameters for PS that are associated with known Geographical Area, or

-The UE is associated with a serving cell on a carrier different than the PS carrier, and the radio parameters for PS that are provided by the serving cell, or

-The UE is associated with a serving cell on a carrier different than the PS carrier, and has a non-serving cell selected on the PS carrier with the preconfigured radio parameters.

When the advanced-V2X or PS UE is not associated with a serving cell on the V2X or PS carrier, and the UE does not have knowledge of its geographical area, or is provisioned with preconfigured radio parameters that are not associated with any Geographical Area, V2X or PS UE’ transmissions are not allowed, and the requirements in Section 6.3E.2 apply.

For a terminal that supports operation in shared spectrum, the current version of this specification assumes in the uplink sub-bands within a wideband channel shall be contiguously allocated to the UE.  The uplink requirements for one or more non-transmitted sub-bands between two transmitted sub-bands does not form a part of the current version of this specification.

Terminal that supports inter-band NR-DC configuration shall meet the minimum requirements for corresponding CA configuration (suffix A), unless otherwise specified.

A terminal which supports intra-band contiguous UL CA with UL MIMO shall meet the corresponding requirements in suffix H with all UL CCs with UL MIMO.

A terminal which supports intra-band contiguous UL CA with TxD shall meet the corresponding requirements in suffix A with all UL CCs with TxD.

A terminal which supports inter-band UL CA with UL MIMO shall meet the corresponding requirements in suffix H with all UL CCs with UL MIMO for the frequency band(s) said to be with UL MIMO.

## 5Operating bands and channel arrangement

## 5.1General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE:Other operating bands and channel bandwidths may be considered in future releases.

Requirements throughout the RF specifications are in many cases defined separately for different frequency ranges (FR). The frequency ranges in which NR can operate according to this version of the specification are identified as described in Table 5.1-1. Whenever the FR2 is referred, both FR2-1 and FR2-2 frequency sub-ranges shall be considered, unless otherwise stated.

Table 5.1-1: Definition of frequency ranges

The present specification covers FR1 operating bands.

## 5.2Operating bands

NR is designed to operate in the FR1 operating bands defined in Table 5.2-1.

Table 5.2-1: NR operating bands in FR1

## 5.2AOperating bands for CA

## 5.2A.0General

CA operating bands including Band n90 are defined by the corresponding CA operating bands including Band n41 with Band n90 replacing Band n41. For brevity the said CA operating bands including Band n90 are not listed in the tables below but are covered by this specification.

## 5.2A.1Intra-band CA

NR intra-band carrier aggregation is designed to operate in the operating bands defined in Table 5.2A.1-1 and Table 5.2A.1-2, where all operating bands are within FR1.

Table 5.2A.1-1: Intra-band contiguous CA operating bands in FR1

Table 5.2A.1-2: Intra-band non-contiguous CA operating bands in FR1

## 5.2A.2Inter-band CA

NR inter-band carrier aggregation is designed to operate in the operating bands defined in Table 5.2A.2.1-1, Table 5.2A.2.2-1, Table 5.2A.2.3-1, Table 5.2A.2.4-1 and Table 5.2A.2.5-1, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a lower order band combination, when the applicable lower order band combination is a band pair in a higher order band combination, the mandatory simultaneous Rx/Tx capability also applies for the band pair in the higher order band combination.

Unless stated otherwise, simultaneous Rx/Tx capability is mandatory for FR1+FR1 FDD-TDD and TDD-SDL CA combinations. Simultaneous Rx/Tx capability is mandatory without signaling for FR1+FR1 FDD-FDD and FDD-SDL CA combinations.  For low NR band inter-band CA configurations supported via switching featureSetCombinationLowBandSwitching-r19, the simultaneous Rx/Tx capability does not apply.

Table 5.2A.2-1: Void

Table 5.2A.2-2: Void

Table 5.2A.2-3: Void

## 5.2A.2.1Inter-band CA (two bands)

Table 5.2A.2.1-1: Inter-band CA operating bands involving FR1 (two bands)

## 5.2A.2.2Inter-band CA (three bands)

Table 5.2A.2.2-1: Inter-band CA operating bands involving FR1 (three bands)

## 5.2A.2.3Inter-band CA (four bands)

Table 5.2A.2.3-1: Inter-band CA operating bands involving FR1 (four bands)

## 5.2A.2.4Inter-band CA (five bands)

Table 5.2A.2.4-1: Inter-band CA operating bands involving FR1 (five bands)

## 5.2A.2.5Inter-band CA (six bands)

Table 5.2A.2.5-1: Inter-band CA operating bands involving FR1 (six bands)

## 5.2BOperating bands for DC

The operating bands are specified in clause 5.5B for operation with NR dual connectivity configured, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a band combination, the mandatory simultaneous Rx/Tx capability also applies for the band combination when the applicable band combination is a subset of a higher order band combination.

## 5.2COperating band combination for SUL

NR operation is designed to operate in the operating band combination defined in Table 5.2C-1, Table 5.2C-2, Table 5.2C-3 and Table 5.2C-4, where all operating bands are within FR1.

If the mandatory simultaneous Rx/Tx capability applies for a band combination, when the applicable lower order band combination is a band pair in a higher order band combination, the mandatory simultaneous Rx/Tx capability also applies for the band pair in the higher order band combination.

Table 5.2C-1: Operating band combination for SUL in FR1

Table 5.2C-2: Operating SUL band combination with intra-band non-contiguous CA in FR1

Table 5.2C-3: Operating SUL band combination with intra-band contiguous CA in FR1

Table 5.2C-4: Operating SUL band combination with inter-band CA in FR1

## 5.2DOperating bands for UL MIMO

NR is designed to support UL MIMO where all of the operating bands are in FR1 defined in Table 5.2D-1.

Table 5.2D-1: NR operating bands for UL MIMO in FR1

## 5.2EOperating band for V2X

## 5.2E.1V2X operating bands

NR V2X is designed to operate in the operating bands in FR1 defined in Table 5.2E.1-1.

Table 5.2E.1-1 V2X operating bands in FR1

## 5.2E.1ASidelink CA operating bands

For NR sidelink intra-band CA operation is designed to operate in the operating bands in FR1 defined in Table 5.2E.1A-1 and Table 5.2E.1A-2.

Table 5.2E.1A-1 Intra-band contiguous SL CA operating bands in FR1

Table 5.2E.1A-2 Intra-band non-contiguous SL CA operating bands in FR1

## 5.2E.1FOperating bands for Sidelink Unlicensed

NR Sidelink is designed to operate in the unlicensed operating bands in FR1 defined in Table 5.2E.1F-1.

Table 5.2E.1F-1. NR SL-U operating bands in FR1

## 5.2E.2V2X operating bands for concurrent operation

NR V2X operation is designed to operate concurrent with NR uplink/downlink on the operating bands combinations listed in Table 5.2E.2-1 and Table 5.2E.2-2.

Table 5.2E.2-1 Inter-band concurrent V2X operating bands

Table 5.2E.2-2 Intra-band concurrent V2X operating bands

## 5.2E.2FOperating bands for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, NR sidelink in the unlicensed operating band is designed to operate concurrently with NR uplink/downlink on the operating band combinations are listed in Table 5.2E.2F-1.

Table 5.2E.2F-1 SL-U Inter-band concurrent operating bands

## 5.2JOperating band for ATG

## 5.2J.1General

NR operating bands n1, n3, n34, n39, n41, n78, n79, which are defined in Table 5.2-1, can be applied for ATG operation.

## 5.2J.1AOperating band for ATG CA

NR carrier aggregation operating bands defined in Table 5.2J.1A.1-1 and Table 5.2J.1A.2-1, can be applied for ATG CA operation.

## 5.2J.1A.1Operating band for ATG intra-band CA

Table 5.2A.1-1: ATG intra-band contiguous CA operating bands

## 5.2J.1A.2Operating band for ATG inter-band CA

Table 5.2J.1A.2-1: ATG inter-band CA operating bands

## 5.2J.1DOperating band for ATG UL MIMO

NR operating bands in Table 5.2J.1D-1 to support UL MIMO, can be applied for ATG UL MIMO operation.

Table 5.2J.1D-1: NR operating bands for UL MIMO in FR1

## 5.2KOperating bands for Aerial UE

Aerial UE is designed to operate in NR operating bands as defined in Table 5.2-1, following applicable spectrum regulations, e.g. ECC Decision (22)07 [18] for CEPT countries.

## 5.2MOperating bands for LP-WUS/WUR

LP-WUS/WUR is designed to operate in the operating bands defined in Table 5.2-1, excluding bands n46, n47, n96, n102 and SDL bands.

## 5.3UE channel bandwidth

## 5.3.1General

The UE channel bandwidth supports a single NR RF carrier in the uplink or downlink at the UE. From a BS perspective, different UE channel bandwidths may be supported within the same spectrum for transmitting to and receiving from UEs connected to the BS. Transmission of multiple carriers to the same UE (CA) or multiple carriers to different UEs within the BS channel bandwidth can be supported.

From a UE perspective, the UE is configured with one or more BWP / carriers, each with its own UE channel bandwidth. The UE does not need to be aware of the BS channel bandwidth or how the BS allocates bandwidth to different UEs.

The placement of the UE channel bandwidth for each UE carrier is flexible but can only be completely within the BS channel bandwidth.

The relationship between the channel bandwidth, the guardband and the maximum transmission bandwidth configuration is shown in Figure 5.3.1-1.

Figure 5.3.1-1: Definition of the channel bandwidth and the maximum transmission bandwidth configuration for one NR channel

## 5.3.2Maximum transmission bandwidth configuration

The maximum transmission bandwidth configuration NRB for each UE channel bandwidth and subcarrier spacing is specified in Table 5.3.2-1.

Table 5.3.2-1: Maximum transmission bandwidth configuration NRB

## 5.3.3Minimum guardband and transmission bandwidth configuration

The minimum guardband for each UE channel bandwidth and SCS is specified in Table 5.3.3-1,

Table 5.3.3-1: Minimum guardband for each UE channel bandwidth and SCS (kHz)

NOTE:The minimum guardbands have been calculated using the following equation: GBChannel = (BWChannel x 1000 (kHz) - NRB x SCS x 12) / 2 - SCS/2, where NRB are from Table 5.3.2-1 and GBChannel expressed in kHz.

Figure 5.3.3-1: Void

The number of RBs configured in any channel bandwidth shall ensure that the minimum guardband specified in this clause is met.

Figure 5.3.3-2: UE PRB utilization

In the case that multiple numerologies are multiplexed in the same symbol due to BS transmission of SSB, the minimum guardband on each side of the carrier is the guardband applied at the configured channel bandwidth for the numerology that is received immediately adjacent to the guard.

If multiple numerologies are multiplexed in the same symbol and the UE channel bandwidth is >50 MHz, the minimum guardband applied adjacent to 15 kHz SCS shall be the same as the minimum guardband defined for 30 kHz SCS for the same UE channel bandwidth.

Figure 5.3.3-3 Guard band definition when transmitting multiple numerologies

NOTE:Figure 5.3.3-3 is not intended to imply the size of any guard between the two numerologies. Inter-numerology guard band within the carrier is implementation dependent.

For a UE supporting wideband operation, the nominal intra-cell guard bands and the corresponding sizes of the RB sets separated by the said guard bands are as specified in Table 5.3.3-2 for each UE channel bandwidth and sub-carrier spacing for the downlink, uplink and sidelink. The nominal intra-cell guard bands in Table 5.3.3-2 are applicable when the respective IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List for the uplink, downlink and sidelink are not provided, as specified in [10] clause 7.

Table 5.3.3-2: Nominal intra-cell guard bands for wideband operation

For a UE that supports shared spectrum channel access, there are no uplink, downlink or sidelink intra-cell guard bands for operation with 10 MHz and 20 MHz channel bandwidths; the maximum transmission bandwidth configurations for these channel bandwidths are in accordance with clause 5.3.2.

For each UE channel bandwidth and sub-carrier spacing given by Table 5.3.3-2, the maximum transmission bandwidth configuration of the carrier including intra-cell guard bands, if configured for the uplink, downlink and sidelink by the respective IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List, and corresponding RB-set(s) shall be in accordance with clause 5.3.2 with a minimum inter-cell guard band of the UE channel bandwidth as specified in Table 5.3.3-1 for the uplink, downlink and sidelink. Minimum requirements specified for wideband operation in Clause 6 and Clause 7 also apply for intra-cell guard bands larger than the nominal sizes in Table 5.3.3-2 as listed in Table 5.3.3-3 for each sub-carrier spacing; each guard band in order of CRB index must be larger than or equal to the corresponding nominal guard band specified in Table 5.3.3-2 for each channel bandwidth.

Table 5.3.3-3: Applicable intra-cell guard bands for wideband operation

If the UE is configured with zero width intra-cell guard bands for the uplink, downlink and sidelink by the IE intraCellGuardBandsUL-List, intraCellGuardBandsDL-List [7] and intraCellGuardBandsSL-List on a carrier greater than 20 MHz, the maximum transmission bandwidth configuration for the uplink, downlink and sidelink shall be in accordance with clause 5.3.2 with a minimum inter-cell guard band of the UE channel bandwidth as specified in Table 5.3.3-1.

## 5.3.4RB alignment

For each numerology, its common resource blocks are specified in Clause 4.4.4.3 in TS 38.211 [6], and the starting point of its transmission bandwidth configuration on the common resource block grid for a given channel bandwidth is indicated by an offset to "Reference point A" in the unit of the numerology. The UE transmission bandwidth configuration is indicated by the higher layer parameter carrierBandwidth [7] and will fulfil the minimum UE guardband requirement specified in Clause 5.3.3.

## 5.3.5UE channel bandwidth per operating band

The requirements in this specification apply to the combination of channel bandwidths, SCS and operating bands shown in Table 5.3.5-1. The transmission bandwidth configuration in Table 5.3.2-1 shall be supported for each of the specified channel bandwidths. The channel bandwidths are specified for both the TX and RX path.

Table 5.3.5-1 Channel bandwidths for each NR band

## 5.3.6Asymmetric channel bandwidths

The UE channel bandwidth can be asymmetric in downlink and uplink. In asymmetric channel bandwidth operation, the narrower carrier shall be confined within the frequency range of the wider channel bandwidth.

In FDD, the confinement is defined as a maximum deviation to the Tx-Rx carrier center frequency separation (defined in Table 5.4.4-1) as following:

ΔFTX-RX = | (BWDL – BWUL)/2 |

The operating bands and supported asymmetric channel bandwidth combinations are defined in Table 5.3.6-1.

Table 5.3.6-1: FDD asymmetric UL and DL channel bandwidth combinations

In TDD, the operating bands and supported asymmetric channel bandwidth combinations are defined in Table 5.3.6-2.

Table 5.3.6-2: TDD asymmetric UL and DL channel bandwidth combinations

## 5.3AUE channel bandwidth for CA

## 5.3A.1General

Figure 5.3A.1-1: Void

Figure 5.3A.1-2: Void

## 5.3A.2Maximum transmission bandwidth configuration for CA

For carrier aggregation, the maximum transmission bandwidth configuration is defined per component carrier and the requirement is specified in clause 5.3.2.

## 5.3A.3Minimum guardband and transmission bandwidth configuration for CA

For intra-band contiguous carrier aggregation, Aggregated Channel Bandwidth and Guard Bands are defined as follows, see Figure 5.3A.3-1.

FC, lowLower EdgeUpper  EdgeLowest Carrier Transmission Bandwidth Configuration [RB]FC, highFoffset, lowHighest Carrier Transmission Bandwidth Configuration [RB]Resource blockAggregated Channel Bandwidth, BWchannel_CA (MHz)Fedge, lowFedge, highFoffset, highFC, lowLower EdgeUpper  EdgeLowest Carrier Transmission Bandwidth Configuration [RB]FC, highFoffset, lowHighest Carrier Transmission Bandwidth Configuration [RB]Resource blockAggregated Channel Bandwidth, BWchannel_CA (MHz)Fedge, lowFedge, highFoffset, high

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

NOTE:The Foffset,low, Foffset,high and BWChannel_CA determined as per the above apply for all sub-carrier configurations μ ≤ μ0 configured for component carriers centred at FC,low /FC,high, where μ0 is the largest µ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths. The BWGB is used for determining the frequency offsets; it is also the minimum internal guard band at the lower/higher edge of BWChannel_CA when μ = μ0 is configured for the lower and upper component carriers.

In case there is no common μ value for both of the channel bandwidths, μ=1 is used for SCSlow, SCShigh, NRB,low, NRB,high, GBChannel,low and GBChannel,high.

For intra-band non-contiguous carrier aggregation Sub-block Bandwidth and Sub-block edges are defined as follows, see Figure 5.3A.3-2.

...Sub block nTransmission Bandwidth Configuration of the highest carrier in a sub-block [RB]Transmission Bandwidth Configuration of the lowest carrier in a sub-block  [RB]Fedge,block n, lowFC,block n,highFedge,block n,highFoffset,highFoffset,lowFC,block n,lowSub-block Bandwidth, BWChannel,block n (MHz)Lower Sub-block EdgeUpper Sub-block EdgeResource blockSub block n+1Foffset, lowFedge,block n+1, lowFC,block n+1,lowFC,block n+1,highFedge,block n+1,highFoffset,highSub-block Bandwidth, BWChannel,block n+1  (MHz)Lower Sub-block EdgeUpper Sub-block EdgeTransmission Bandwidth Configuration of the highest carrier in a sub-block [RB]Transmission Bandwidth Configuration of the lowest carrier in a sub-block  [RB]Resource block...Sub block nTransmission Bandwidth Configuration of the highest carrier in a sub-block [RB]Transmission Bandwidth Configuration of the lowest carrier in a sub-block  [RB]Fedge,block n, lowFC,block n,highFedge,block n,highFoffset,highFoffset,lowFC,block n,lowSub-block Bandwidth, BWChannel,block n (MHz)Lower Sub-block EdgeUpper Sub-block EdgeResource blockSub block n+1Foffset, lowFedge,block n+1, lowFC,block n+1,lowFC,block n+1,highFedge,block n+1,highFoffset,highSub-block Bandwidth, BWChannel,block n+1  (MHz)Lower Sub-block EdgeUpper Sub-block EdgeTransmission Bandwidth Configuration of the highest carrier in a sub-block [RB]Transmission Bandwidth Configuration of the lowest carrier in a sub-block  [RB]Resource blockFigure 5.3A.3-2: Definition of sub-block bandwidth for intra-band non-contiguous spectrum

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

NOTE:The Foffset,block,low, Foffset,block,high and BWChannel,block determined as per the above apply for all sub-carrier configurations μ ≤ μ0 configured for component carriers centred at FC,block,low /FC,block,high, where μ0 is the largest µ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths. The BWGB is used for determining the frequency offsets; it is also the minimum internal guard band at the lower/higher edge of BWChannel,block when μ = μ0 is configured for the lower and upper component carriers of the block.

The sub-block gap size between two consecutive sub-blocks Wgap is defined as

Wgap = Fedge,block n+1,low - Fedge,block n,high (MHz)

## 5.3A.4Void

## 5.3A.5UE channel bandwidth per operating band for CA

The requirements for carrier aggregation in this specification are defined for carrier aggregation configurations.

For intra-band contiguous carrier aggregation, a carrier aggregation configuration is a single operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5A.1. For each carrier aggregation configuration, requirements are specified for all aggregated channel bandwidths contained in a bandwidth combination set, a UE can indicate support of several bandwidth combination sets per carrier aggregation configuration. For intra-band non-contiguous carrier aggregation, a carrier aggregation configuration is a single operating band supporting two or more sub-blocks, each supporting a carrier aggregation bandwidth class.

For intra-band non-contiguous uplink carrier aggregation, frequency separation class (Fs) specified in Table 5.3A.5-2 indicates the maximum frequency span between lower edge of lowest component carrier and upper edge of highest component carrier that UE can support per band combination in uplink in non-contiguous intra-band operation when the signalling is absent for dualPA-Architecture IE.

For inter-band carrier aggregation, a carrier aggregation configuration is a combination of operating bands, each supporting a carrier aggregation bandwidth class.

Table 5.3A.5-1: NR CA bandwidth classes

Table 5.3A.5-2: NR intra-band non-contiguous UL CA frequency separation classes

## 5.3EChannel bandwidth for V2X

## 5.3E.1General

NR V2X operation channel bandwidths for each operating band are specified in Table 5.3E.1-1. The same (symmetrical) channel bandwidth is specified for both the transmission and reception path. The maximum channel bandwidth for SL operation in licensed band is 40MHz.

Table 5.3E.1-1 NR V2X operation channel bandwidths for each operating band

## 5.3E.1AChannel bandwidth for Sidelink CA

For sidelink intra-band contiguous carrier aggregation, a carrier aggregation configuration is a single ITS operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5E.1A.1.

For sidelink intra-band non-contiguous carrier aggregation, a carrier aggregation configuration is a single ITS operating band supporting a carrier aggregation bandwidth class with associated bandwidth combination sets specified in clause 5.5E.1A.2

The sidelink intra-band carrier aggregation bandwidth class follows Table 5.3A.5-1. For each carrier aggregation configuration, requirements are specified for all aggregated channel bandwidths contained in a bandwidth combination set.

## 5.3E.1FChannel bandwidth for Sidelink Unlicensed

NR SL-U Channel bandwidths for each band are specified in Table 5.3E.1F-1. The same (symmetrical) channel bandwidth is specified for both the transmission and reception path.

Table 5.3E.1F-1 NR SL-U channel bandwidth

## 5.3E.2Channel bandwidth for V2X concurrent operation

For NR V2X inter-band concurrent operation in FR1, the NR V2X channel bandwidths for each operating band are specified in Table 5.3E.2-1.

Table 5.3E.2-1: Inter-band concurrent operation configurations

For NR V2X intra-band concurrent operation in FR1, the NR V2X channel bandwidths for each operating band are specified in Table 5.3E.2-2.

Table 5.3E.2-2: Intra-band concurrent operation configurations

## 5.3E.2FChannel bandwidth for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the SL-U Channel bandwidths for each operating band are specified in Table 5.3E.2F-1.

Table 5.3E.2F-1 NR SL-U inter-band concurrent operating configurations

## 5.3IChannel bandwidth for (e)RedCap

The requirements in this specification apply to the combination of channel bandwidths, SCS and operating bands shown in Table 5.3.5-1 with maximum channel bandwidth of 20MHz. The transmission bandwidth configuration in Table 5.3.2-1 shall be supported for each of the specified channel bandwidths up to 20 MHz. When UE supports IE supportOfERedCap-r18 and does not support IE eRedCapNotReducedBB-BW-r18 the requirements in this specification apply with maximum 25RBs for 15 kHz SCS and 12 RBs for 30 kHz SCS for PDSCH and PUSCH as described in clause 17.1A of TS 38.213 [8]. The channel bandwidths are specified for both the TX and RX paths.

3MHz channel bandwidth is not applicable for (e)RedCap UE in the current release.

## 5.3MUE channel bandwidth for LP-WUS/WUR

## 5.3M.1General

The LP-WUS carrier bandwidth corresponding to the UE channel bandwidth for LP-WUS is defined as the sum of resource blocks (RBs) occupied by the LP-WUS signal and the guard RBs separating it from the NR signal. The LP-WUS carrier is embedded within the NR channel and is flexibly positionable, provided alignment with the NR PRB grid is maintained.

A guard RB is referred to as an ASCS guard RB when located between an NR RB and an LP-WUS RB, and as an ACS guard RB when positioned between the NR guardband as specified in Table 5.3.3-1 and an LP-WUS RB.

## 5.3M.2Maximum transmission bandwidth configuration

The maximum transmission bandwidth configuration NRB,LP-WUS for LP-WUS within each NR UE channel bandwidth and subcarrier spacing is specified in Table 5.3M.2-1.

Table 5.3M.2-1: Maximum transmission bandwidth configuration NRB,LP-WUS for LP-WUS

## 5.4Channel arrangement

## 5.4.1Channel spacing

## 5.4.1.1Channel spacing for adjacent NR carriers

The spacing between carriers will depend on the deployment scenario, the size of the frequency block available and the channel bandwidths. The nominal channel spacing between two adjacent NR carriers is defined as following:

-For NR operating bands with 100 kHz or 10 kHz channel raster,

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2

-For NR operating bands with 15 kHz channel raster,

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2+{-5 kHz, 0 kHz, 5 kHz} for ∆FRaster equals 15 kHz

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2+{-10 kHz, 0 kHz, 10 kHz} for ∆FRaster equals 30 kHz

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective NR carriers. The channel spacing can be adjusted depending on the channel raster to optimize performance in a particular deployment scenario.

For NR bands restricted to operation with shared-spectrum channel access, the maximum deviation from the nominal channel spacing is 40 kHz.

## 5.4.2Channel raster

## 5.4.2.1NR-ARFCN and channel raster

The global frequency channel raster defines a set of RF reference frequencies FREF. The RF reference frequency is used in signalling to identify the position of RF channels, SS blocks and other elements.

The global frequency raster is defined for all frequencies from 0 to 100 GHz. The granularity of the global frequency raster is ΔFGlobal.

RF reference frequencies are designated by an NR Absolute Radio Frequency Channel Number (NR-ARFCN) in the range (0…2016666) on the global frequency raster. The relation between the NR-ARFCN and the RF reference frequency FREF in MHz is given by the following equation, where FREF-Offs and NRef-Offs are given in Table 5.4.2.1-1 and NREF is the NR-ARFCN.

FREF = FREF-Offs + ΔFGlobal (NREF – NREF-Offs)

Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster

The channel raster defines a subset of RF reference frequencies that can be used to identify the RF channel position in the uplink and downlink. The RF reference frequency for an RF channel maps to a resource element on the carrier. For each operating band, a subset of frequencies from the global frequency raster are applicable for that band and forms a channel raster with a granularity ΔFRaster, which may be equal to or larger than ΔFGlobal.

For SUL bands except n95, n97, n98 and for the uplink of all FDD bands defined in Table 5.2-1, and for TDD bands n34, n39, n48, n90, n38 and n40

FREF, shift = FREF + Δshift, Δshift = 0 kHz or 7.5 kHz.

where Δshift is signalled by the network in higher layer parameter frequencyShift7p5khz [7]. For Band n34, n38, n39, n40, n48 FREF, shift is only applicable to uplink transmissions using a 15 kHz SCS.

The mapping between the channel raster and corresponding resource element is given in Clause 5.4.2.2. The applicable entries for each operating band are defined in Clause 5.4.2.3.

## 5.4.2.2Channel raster to resource element mapping

The mapping between the RF reference frequency on the channel raster and the corresponding resource element is given in Table 5.4.2.2-1 and can be used to identify the RF channel position. The mapping depends on the total number of RBs that are allocated in the channel and applies to both UL and DL. The mapping must apply to at least one numerology supported by the UE.

Table 5.4.2.2-1: Channel raster to resource element mapping

NRB is the maximum transmission bandwidth configuration specified in sub-clause 5.3.2, is the PRB index within the NRB, and  is the resource element index within this PRB.

## 5.4.2.3Channel raster entries for each operating band

The RF channel positions on the channel raster in each NR operating band are given through the applicable NR-ARFCN in Table 5.4.2.31, using the channel raster to resource element mapping in clause 5.4.2.2.

For NR operating bands with 100 kHz channel raster, ΔFRaster = 20 × ΔFGlobal. In this case every 20th NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.31 is given as <20>.

For NR operating bands with 15 kHz channel raster below 3GHz, ΔFRaster = I × ΔFGlobal, where I ϵ {3,6}. Every Ith NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.31 is given as < I >.

For NR operating bands with 15 kHz channel raster above 3GHz, ΔFRaster = I × ΔFGlobal, where I ϵ {1,2}. Every Ith  NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.3-1 is given as <I>.

In frequency bands with two or more ΔFRaster, the higher ΔFRaster: For 15 kHz and 30 kHz channel raster applies to channels using only the SCS that is equal to or larger than the higher ΔFRaster and SSB SCS is equal to the higher ∆FRaster.

Table 5.4.2.3-1: Applicable NR-ARFCN per operating band

Table 5.4.2.3-2: Allowed NREF (NR-ARFCN) for operation in Band n46

Table 5.4.2.3-3: Allowed NREF (NR-ARFCN) for operation in Band n96

Table 5.4.2.3-4: Allowed NREF (NR-ARFCN) for operation in Band n102

For NR operating bands with 100 kHz channel raster, Enhanced channel raster is defined with ΔFRaster = 2 × ΔFGlobal. In this case every 2th NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.35 is given as <2>.

Table 5.4.2.3-5: Applicable NR-ARFCN per operating band for enhanced channel raster

## 5.4.3Synchronization raster

## 5.4.3.1Synchronization raster and numbering

The synchronization raster indicates the frequency positions of the synchronization block that can be used by the UE for system acquisition when explicit signalling of the synchronization block position is not present.

A global synchronization raster is defined for all frequencies. The frequency position of the SS block is defined as SSREF with corresponding number GSCN. The parameters defining the SSREF and GSCN for all the frequency ranges are in Table 5.4.3.1-1 for above 3 MHz channel bandwidth and in Table 5.4.3.1-2 for 3 MHz channel bandwidth.

For band n100, additional parameters defining the SSREF and GSCN are specified in Table 5.4.3.1-3.

The resource element corresponding to the SS block reference frequency SSREF is given in clause 5.4.3.2. The synchronization raster and the subcarrier spacing of the synchronization block is defined separately for each band.

The synchronization raster and the corresponding SS block do not cover all possible RF channel bandwidths and locations on Enhanced channel raster.

Table 5.4.3.1-1: GSCN parameters for the global frequency raster for above 3 MHz channel bandwidth

Table 5.4.3.1-2: GSCN parameters for the global frequency for 3 MHz channel bandwidth

Table 5.4.3.1-3: Additional GSCN parameters for band n100

5.4.3.2Synchronization raster to synchronization block resource element mapping

The mapping between the synchronization raster and the corresponding resource element of the SS block is given in Table 5.4.3.2-1.

Table 5.4.3.2-1: Synchronization raster to SS block resource element mapping

is the subcarrier number of SS/PBCH block defined in TS 38.211 clause 7.4.3.1 [6].

## 5.4.3.3Synchronization raster entries for each operating band

The synchronization raster for above 3 MHz channel bandwidth for each band is give in Table 5.4.3.3-1. The distance between applicable GSCN entries is given by the <Step size> indicated in Table 5.4.3.3-1.

Table 5.4.3.3-1: Applicable SS raster entries per operating band for above 3 MHz channel bandwidth

The synchronization raster for channel bandwidth 3 MHz for each band is given in Table 5.4.3.3-2. The distance between applicable GSCN entries is given by the <Step size> indicated in Table 5.4.3.3-2.

Table 5.4.3.3-2: Applicable SS raster entries per operating band for 3 MHz channel bandwidth

## 5.4.4TX–RX frequency separation

The default TX channel (carrier centre frequency) to RX channel (carrier centre frequency) separation for operating bands is specified in Table 5.4.4-1.

Table 5.4.4-1: UE TX-RX frequency separation

## 5.4AChannel arrangement for CA

## 5.4A.1Channel spacing for CA

For intra-band contiguous carrier aggregation with two or more component carriers, the nominal channel spacing between two adjacent NR component carriers is defined as the following unless stated otherwise:

For NR operating bands with a 100 kHz or 10 kHz channel raster:

while for NR operating bands without a 100 kHz channel raster:

with

n = µ0

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective NR component carriers according to Table 5.3.2-1 with values in MHz, μ0  is the largest μ value among the subcarrier spacing configurations supported in the operating band for both of the channel bandwidths according to Table 5.3.5-1 and GBChannel(i) is the minimum guard band for channel bandwidth i according to Table 5.3.3-1 for the said μ value with μ as defined in TS 38.211. In case there is no common μ value for both of the channel bandwidths, μ0=1 is selected and GBChannel(i) is the minimum guard band for channel bandwidth i according to Table 5.3.3-1 for μ=1 with μ as defined in TS 38.211.

The bandwidth BWChannel(i) for determining the nominal channel spacing is the UE specific channel bandwidth, if configured by ServingCellConfig, the channel bandwidth of the NR component carrier otherwise.

The channel spacing for intra-band contiguous carrier aggregation can be adjusted to any multiple of least common multiple of channel raster, the enhanced channel raster if supported, and sub-carrier spacing less than the nominal channel spacing to optimize performance in a particular deployment scenario.

For intra-band contiguous carrier aggregation in NR bands restricted to operation with shared-spectrum channel access, the maximum deviation from the nominal channel spacing is 300 kHz.

For intra-band non-contiguous carrier aggregation, the channel spacing between two NR component carriers in different sub-blocks shall be larger than the nominal channel spacing defined in this clause.

## 5.4A.2Channel raster for CA

For inter-band and intra-band carrier aggregation, the channel raster requirements in clause 5.4.2 apply for each operating band.

## 5.4A.3Synchronization raster for CA

For inter-band and intra-band carrier aggregation, the synchronization raster requirements in clause 5.4.3 apply for each operating band.

## 5.4A.4Tx-Rx frequency separation for CA

For inter-band carrier aggregation, the Tx-Rx frequency separation requirements in clause 5.4.4 apply for each operating band.

For intra-band carrier aggregation, the same TX-RX frequency separation as specified in Table 5.4.4-1 is applied to PCC and SCC, respectively.

## 5.4BReserved

## 5.4CReserved

## 5.4DReserved

## 5.4EChannel arrangement for V2X

## 5.4E.1Channel spacing

For NR V2X, the channel spacing requirements in clause 5.4.1 apply for each operating band.

## 5.4E.1AChannel spacing for Sidelink CA

For NR sidelink CA operation, the channel spacing requirements in clause 5.4A.1 apply.

## 5.4E.1FChannel spacing for Sidelink Unlicensed

For NR SL-U operation, the channel spacing requirements in clause 5.4.1 apply for each operating band.

## 5.4E.2Channel raster

## 5.4E.2.1NR-ARFCN and channel raster

For NR V2X, the NR-ARFCN and channel raster requirements in clause 5.4.2.1 apply for each operating band.

For NR V2X UE, the reference frequency can be shifted by configuration.

FREF_V2X = FREF + Δshift + N * 5 kHz

where

Δshift = 0 kHz or 7.5 kHz indicated in IE (frequencyShift7p5khz), and

N can be set as one of following values {-1, 0, 1}, which are signalled by the network in higher layer parameters or configured by pre-configuration parameters.

## 5.4E.2.1AVoid

## 5.4E.2.1FVoid

## 5.4E.2.2Channel raster to resource element mapping

For NR V2X, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each operating band.

## 5.4E.2.2AVoid

## 5.4E.2.2FVoid

## 5.4E.2.3Channel raster entries for each operating band

For NR V2X, the channel raster entries requirements in clause 5.4.2.3 apply for each operating band.

The RF channel positions on the channel raster in each NR V2X operating band are given through the applicable NR-ARFCN in Table 5.4.2.3-1, using the channel raster to resource element mapping in clause 5.4.2.2.

For NR V2X operating band n47, ΔFRaster = I × ΔFGlobal, where I ϵ {1}. Every Ith NRARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster in Table 5.4.2.3-1 is given as <I>.

## 5.4E.2.3AVoid

## 5.4E.2.3FVoid

5.4E.2AChannel raster for Sidelink CA

5.4E.2A.1NR-ARFCN and channel raster for Sidelink CA

For NR SL intra-band contiguous CA operation, the NR-ARFCN and channel raster requirements in clause 5.4E.2.1 apply for each component carrier.

5.4E.2A.2Channel raster to resource element mapping for Sidelink CA

For NR SL intra-band contiguous CA operation, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each component carrier.

5.4E.2A.3Channel raster entries for each operating band for Sidelink CA

For NR SL intra-band contiguous CA operation, the channel raster entries requirements in clause 5.4E.2.3 apply for each component carrier.

5.4E.2FChannel raster for Sidelink Unlicensed

5.4E.2F.1NR-ARFCN and channel raster for Sidelink Unlicensed

For NR SL-U operation, the general requirements in clause 5.4.2 are applied.

NR-ARFCN and channel raster requirements in clause 5.4.2.1 are applied for NR SL-U with following exception:

-N*5kHz/7.5kHz frequency raster shift, which can be used in NR V2X in band n47 is not defined for NR SL-U operation in bands n46, n96, n102.

-Channel raster entries for each operating band requirements in clause 5.4.2.3 are applied for NR SL-U with following exception: Channel raster points for 10MHz CBW in band n46 as defined in Table 5.4.2.3-2 are not applicable for NR SL-U.

5.4E.2F.2Channel raster to resource element mapping for Sidelink Unlicensed

The mapping between the RF reference frequency on the channel raster and the corresponding resource element is given in Table 5.4.2.2-1 and can be used to identify the RF channel position. The mapping depends on the total number of RBs that are allocated in the channel and applies to both Tx and Rx for SL. The mapping must apply to at least one numerology supported by the UE.

5.4E.2F.3Channel raster entries for Sidelink Unlicensed

For NR SL-U operation, the channel raster entries requirements in clause 5.4.2.3 apply for each operating band.

## 5.4E.3Synchronization raster for V2X

There is no synchronization raster definition for NR V2X for both licensed bands and unlicensed bands.

## 5.4E.3ASynchronization raster for Sidelink CA

There is no synchronization raster definition for NR SL CA operating bands.

## 5.4E.3FSynchronization raster for Sidelink Unlicensed

There is no synchronization raster definition for NR SL-U operating bands n46, n96, n102.

## 5.4IChannel arrangement for (e)RedCap

## 5.4I.1Channel spacing for (e)RedCap

For (e)RedCap UEs, the channel spacing requirements in clause 5.4.1 apply for each operating band.

## 5.4I.2Channel raster for (e)RedCap

## 5.4I.2.1NR-ARFCN and channel raster

For (e)RedCap UEs, the NR-ARFCN and channel raster requirements in clause 5.4.2.1 apply for each operating band.

## 5.4I.2.2Channel raster to resource element mapping

For (e)RedCap UEs, the channel raster to resource element mapping requirements in clause 5.4.2.2 apply for each operating band.

## 5.4I.2.3Channel raster entries for each operating band

For (e)RedCap UEs, the RF channel positions on the channel raster in each NR operating band are given through the applicable NR-ARFCN in Table 5.4.2.31 and additional intermediary NR-ARFCN with a step size of <2> for operating bands that are included in Table 5.4.2.3-1 with a step size of <20>, using the channel raster to resource element mapping in clause 5.4I.2.2.

For NR operating bands included in Table 5.4.2.3-1 with a step size of <20>, the channel raster for (e)RedCap UEs is defined with ΔFRaster = 2 × ΔFGlobal. In this case every 2nd NR-ARFCN within the operating band are applicable for the channel raster within the operating band and the step size for the channel raster is given as <2>, every 10th of these channel raster entries coincides with entries defined in Table 5.4.2.3-1 for this operating band.

## 5.4I.3Synchronization raster for (e)RedCap

For (e)RedCap UEs, the synchronization raster requirements in clause 5.4.3 apply for each operating band. The synchronization raster and the corresponding SS block do not cover all possible RF channel bandwidths and locations on the channel raster defined in sub-clause 5.4I.2.

## 5.4I.4Tx-Rx frequency separation for (e)RedCap

For (e)RedCap UEs, the Tx-Rx frequency separation requirements in clause 5.4.4 apply for each operating band.
