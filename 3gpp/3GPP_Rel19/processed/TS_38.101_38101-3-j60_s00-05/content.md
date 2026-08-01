# TS 38.101 38101-3-j60_s00-05

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

The present document establishes the minimum RF requirements for NR User Equipment (UE) Interworking operation with other radios. This includes but is not limited to additional requirements for carrier aggregation or NR dual connectivity between Range 1 and Range 2 and additional requirements due to NR non-standalone (NSA) operation mode with E-UTRA.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 38.101-1: "NR; User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone"

[3]3GPP TS 38.101-2: "NR; User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone"

[4]3GPP TS 36.101: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception"

[5]3GPP TS 38.521-3: "NR; User Equipment (UE) conformance specification; Radio transmission and reception; Part 3: Range 1 and Range 2 Interworking operation with other radios"

[6]Recommendation ITU-R M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000"

[7]3GPP TS 36.211: "E-UTRA; Physical channels and modulation"

[8]3GPP TS 36.331: " Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification"

[9]3GPP TS 38.331: "NR; Radio Resource Control (RRC) protocol specification"

[10]3GPP TS 38.213: "NR; Physical layer procedures for control"

[11]3GPP TS 38.306: "NR; User Equipment (UE) radio access capabilities"

[12]3GPP TS 38.133: "NR; Requirements for support of radio resource management"

[13]3GPP TS 38.211: "NR; Physical channels and modulation".

[14]3GPP TS 38.214: "NR; Physical layer procedures for data"

[15]3GPP TS 38.133: "NR; Requirements for support of radio resource management"

[16]3GPP TS 36.133: "Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements for support of radio resource management"

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

Con-current operation: The simultaneous transmission and reception of sidelink and Uu interfaces while operation is agnostic of the service used on each interface.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

ΔRIB,cAllowed reference sensitivity relaxation due to support for CA or DC operation, for serving cell c.

ΔTIB,cAllowed maximum configured output power relaxation due to support for CA or DC operation, for serving cell c

BWE-UTRA_ChannelChannel bandwidth of E-UTRA carrier

BWE-UTRA_Channel_CAChannel bandwidth of E-UTRA sub-block which is composed of intra-band contiguous CA E-UTRA carriers

BWNR_ChannelChannel bandwidth of NR carrier

BWNR_Channel_CAChannel bandwidth of NR sub-block which is composed of intra-band contiguous CA NR carriers

Ceil(x)Rounding upwards; ceil(x) is the smallest integer such that ceil(x) ≥ x

EN-DCACLRThe ratio of the filtered mean power centred on the aggregated sub-block bandwidth ENBW to the filtered mean power centred on an adjacent bandwidth of the same size ENBW

E-UTRAACLRE-UTRA ACLR

FCRF reference frequency for the carrier center on the channel raster

FDL_lowThe lowest frequency of the downlink operating band

FDL_highThe highest frequency of the downlink operating band

FUL_lowThe lowest frequency of the uplink operating band

FUL_highThe highest frequency of the uplink operating band

FOOBThe boundary between the NR out of band emission and spurious emission domains

LCRBTransmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resource blocks

Max()The largest of given numbers

Min()The smallest of given numbers

NRACLRNR ACLR

NRBTransmission bandwidth configuration, expressed in units of resource blocks

NRB_aggThe number of the aggregated RBs within the fully allocated aggregated channel bandwidth

for carrier 1 to j, where μ is defined in TS 38.211 [13]NRB_agg=1jNRBj*2μj

NRB,cThe transmission bandwidth configuration of component carrier c, expressed in units of resource blocks

for carrier j, where μ is defined in TS 38.211 [13]NRB,cj=NRBj*2μj

PCMAXThe configured maximum UE output power

RBstartIndicates the lowest RB index of transmitted resource blocks

WgapThe sub-block gap between the two sub-blocks

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

ACLRAdjacent Channel Leakage Ratio

ACSAdjacent Channel Selectivity

A-MPRAdditional Maximum Power Reduction

BCSBandwidth Combination Set

CACarrier Aggregation

CCComponent Carrier

DCDual Connectivity

EIRPEquivalent Isotropically Radiated Power

EN-DCE-UTRA/NR DC

EVMError Vector Magnitude

FDMFrequency Division Multiplexing

FRFrequency Range

ENBWThe aggregated bandwidth of an E-UTRA sub-block and an adjacent NR sub-block

ITSIntelligent Transportation System

ITU-RRadiocommunication Sector of the International Telecommunication Union

MBWMeasurement bandwidth defined for the protected band

MPRAllowed maximum power reduction

MSDMaximum Sensitivity Degradation

MCGMaster Cell Group

NRNew Radio

NSNetwork Signalling

NSANon-Standalone, a mode of operation where operation of an other radio is assisted with an other radio

OOBOut-of-band

OOBEOut-of-band emission

OTAOver The Air

PRBPhysical Resource Block

PSCCHPhysical Sidelink Control CHannel

PSSCHPhysical Sidelink Shared CHannel

REResource Element

REFSENSReference Sensitivity

RFRadio Frequency

RxReceiver

SCGSecondary Cell Group

SCSSubcarrier spacing

SEMSpectrum Emission Mask

SLSidelink

SULSupplementary uplink

TDMTime Division Multiplex

TxTransmitter

UEUser Equipment

UL MIMOUp Link Multiple Antenna transmission

ULSUPUplink sharing from UE perspective

## 4General

## 4.1Relationship between minimum requirements and test requirements

The present document is interwork specification for NR UE, covering RF characteristics and minimum performance requirements. Conformance to the present specification is demonstrated by fulfilling the test requirements specified in the conformance specification 3GPP TS 38.521-3 [5].

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification TS 38.521-3 [5] defines test tolerances. These test tolerances are individually calculated for each test. The test tolerances are used to relax the minimum requirements in this specification to create test requirements. For some requirements, including regulatory requirements, the test tolerance is set to zero.

The measurement results returned by the test system are compared - without any modification - against the test requirements as defined by the shared risk principle.

The shared risk principle is defined in Recommendation ITUR M.1545 [6].

## 4.2Applicability of minimum requirements

a)In this specification the Minimum Requirements are specified as general requirements and additional requirements. Where the Requirement is specified as a general requirement, the requirement is mandated to be met in all scenarios

b)For specific scenarios for which an additional requirement is specified, in addition to meeting the general requirement, the UE is mandated to meet the additional requirements.

c)The spurious emissions power requirements are for the long-term average of the power. For the purpose of reducing measurement uncertainty it is acceptable to average the measured power over a period of time sufficient to reduce the uncertainty due to the statistical nature of the signal

d)Terminal that supports EN-DC or NE-DC configuration shall meet E-UTRA requirements as specified in TS 36.101 [4] and NR requirements as in TS 38.101-1 [2] and TS 38.101-2 [3] unless otherwise specified in this specification

e)All the requirements for intra-band contiguous and non-contiguous EN-DC or NE-DC apply under the assumption of the same uplink-downlink and special subframe configurations in the E-UTRA and slot format indicated by UL-DL-configurationCommon and UL-DL-configurationDedicated in the NR for the EN-DC or NE-DC, a time offset between the two RATs configurations may be required.

f)For EN-DC or NE-DC combinations with CA configurations for E-UTRA and/or NR, all the requirements for E-UTRA and/or NR all the requirements for E-UTRA and/or NR intra-band contiguous and non-contiguous CA apply under the assumption of the same slot format indicated by UL-DL-configurationCommon and UL-DL-configurationDedicated in the PSCell and SCells for NR and the same uplink-downlink and special subframe configurations in Pcell and SCells for E-UTRA.

A terminal which supports an EN-DC or NE-DC configuration shall support:

If any subsets of the EN-DC or NE-DC configuration do not specify its own bandwidth combination sets in 5.3B, then the terminal shall support the same E-UTRA bandwidth combination sets it signals the support for in E-UTRA CA configuration part of E-UTRA – NR DC and shall support the same NR bandwidth combination sets it signals the support for in NR CA configuration part of E-UTRA – NR DC.

Else if one of the subsets of the EN-DC or NE-DC configuration specify its own bandwidth combination sets in 5.3B, then the terminal shall support a product set of channel bandwidth for each band specified by E-UTRA bandwidth combination sets, NR bandwidth combination sets, and EN-DC or NE-DC bandwidth combination sets it singnals the support.A terminal which supports an inter-band EN-DC or NE-DC configuration with a certain UL configuration shall support the all lower order DL configurations of the lower order EN-DC or NE-DC combinations, which have this certain UL configuration and the fallbacks of this UL configuration.

A terminal which supports NE-DC configurations shall meet the minimum requirements for corresponding EN-DC configuration, unless otherwise specified.

For CA or DC configurations, which include FR2 intra-band CA combinations with multiple FR2 sub-blocks, where at least one of the sub-blocks is a contiguous CA combination :

-if the field partialFR2-FallbackRX-Req is not present, the UE shall meet all applicable UE RF requirements for the highest order CA configuration and all associated fallback CA configurations;

-if the field partialFR2-FallbackRX-Req is present, for each FR2 intra-band CA configuration with multiple sub-blocks that the UE indicates support for explicitly in UE capability signalling: the in-gap UE RF requirements in clauses 7.5A, 7.5B, 7.6A, 7.6B apply as the equivalent requirements for the associated fallback FR2 intra-band CA configurations with the same number of sub-blocks, where at least one of the sub-blocks consists of a contiguous CA configuration. The UE shall meet all applicable UE RF requirements for fallback CA configurations with a lesser number of sub-blocks;

-regardless of the field partialFR2-FallbackRX-Req, the UE shall meet all DL out-of-gap requirements for all lower order fallback CA configurations.

Terminal that supports inter-band NR-DC between FR1 and FR2 configuration shall meet the requirements for corresponding CA configuration (suffix A), unless otherwise specified.

## 4.3Specification suffix information

Unless stated otherwise the following suffixes are used for indicating at 2nd level clause, shown in Table 4.3-1.

Table 4.3-1: Definition of suffixes

## 5Operating bands and channel arrangement

## 5.1General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE:Other operating bands and channel bandwidths may be considered in future releases.

Requirements throughout the RF specifications are in many cases defined separately for different frequency ranges (FR). The frequency ranges in which NR can operate according to this version of the specifications are identified as described in Table 5.1-1. Whenever the FR2 is referred, both FR2-1 and FR2-2 frequency sub-ranges shall be considered, unless otherwise stated.

Table 5.1-1: Definition of frequency ranges

The present specification covers band combinations including

-at least one FR1 operating band and one FR2 operating band for carrier aggregation and dual connectivity operations;

-at least one E-UTRA operating band for dual connectivity operations.

## 5.2Operating bands

NR is designed to operate in FR1 operating bands defined in TS 38.101-1 [2] and FR2 operating bands defined in TS 38.101-2 [3]. E-UTRA is designed to operate in operating bands defined in TS 36.101 [4].

## 5.2AOperating bands for CA

## 5.2A.1Inter-band CA between FR1 and FR2

NR carrier aggregation is designed to operate in the operating bands defined in Table 5.2A.11 and Table 5.2A.1-2. The band combinations include at least one FR1 operating band and one FR2 operating band.

Operating bands for CA including Band n90 are defined by the corresponding operating bands for CA including Band n41 with Band n90 replacing Band n41. For brevity the said operating bands for CA including Band n90 are not listed in the tables below but are covered by this specification.

If the mandatory simultaneous Rx/Tx capability applies for a lower order band combination, when the applicable lower order band combination is a band pair in a higher order band combination, the mandatory simultaneous Rx/Tx capability also applies for the band pairin the higher order band combination.

Table 5.2A.1-1: Band combinations for inter-band CA between FR1 and FR2 (two bands)

Table 5.2A.1-2: Band combinations for inter-band CA between FR1 and FR2 (three bands)

Table 5.2A.1-3: Band combinations for inter-band CA between FR1 and FR2 (four bands)

Table 5.2A.1-4: Band combinations for inter-band CA between FR1 and FR2 (five bands)

## 5.2BOperating bands for DC

## 5.2B.1General

The operating bands are specified in clause 5.5B for operation with EN-DC, NGEN-DC, NE-DC or NR-DC configured.

## 5.2B.2Void

## 5.2B.3Void

## 5.2B.4Void

## 5.2B.5Void

## 5.2B.6Void

## 5.2B.7Void

## 5.2EOperating bands for V2X

## 5.2E.1Intra-band V2X bands

NR V2X operation is designed to operate with E-UTRA sidelink in TDM mode on the operating bands combinations listed in Table 5.2E.1-1.

Table 5.2E.1-1: Intra-band V2X operating bands

## 5.2E.2Inter-band V2X bands

NR V2X operation is designed to operate concurrent with E-UTRA uplink/downlink on the operating bands combinations listed in Table 5.2E.2-1.

Table 5.2E.2-1: Inter-band con-current V2X operating bands

## 5.3UE Channel bandwidth

## 5.3AUE Channel bandwidth for CA

## 5.3A.1Inter-band CA between FR1 and FR2

For inter-band NR CA between FR1 and FR2, a carrier aggregation configuration is a combination of operating bands, each supporting a carrier aggregation bandwidth class as specified in clause 5.3A.5 of TS 38.101-1 [2] and clause 5.3A.4 of TS 38.101-2 [3] independently.

## 5.3BUE Channel bandwidth for DC

## 5.3B.0General

For intra-band contiguous EN-DC, the aggregated channel bandwidth is sum of the individual NR and E-UTRA channel bandwidths assuming nominal EN-DC channel with 0 kHz offset spacing as specified in clause 5.4.

ENBW = BWNR_Channel + BWE-UTRA_Channel

In the case where the NR sub-block and/or the E-UTRA sub-block itself is composed of intra-band contiguous CA carriers, the EN-DC aggregated channel bandwidth is the sum of the aggregated channel bandwidths of the NR and E-UTRA sub-blocks assuming nominal EN-DC channel spacing between the NR sub-block and E-UTRA sub-block.

ENBW = BWNR_Channel_CA + BWE-UTRA_Channel_CA

Intra-band contiguous EN-DC configurations are defined using intra-band contiguous EN-DC bandwidth class notation DC_(n)Xyz where the first EN-DC bandwidth class letter y indicates the number of contiguous E-UTRA carriers and the second EN-DC bandwidth class letter z indicates the number of contiguous NR carriers for the EN-DC combination of E-UTRA Band X and NR Band nX. Applicable contiguous intra-band EN-DC bandwidth classes are listed in Table 5.3B.0-1.

Table 5.3B.0-1: Intra-band contiguous EN-DC bandwidth classes

Unless otherwise specified, the aggregated channel bandwidth for the intra-band contiguous NE-DC follows the same definition of EN-DC.

Intra-band contiguous NE-DC configurations are defined using intra-band contiguous NE-DC bandwidth class notation DC_X(n)yz where the first NE-DC bandwidth class letter y indicates the number of contiguous NR carriers and the second NE-DC bandwidth class letter z indicates the number of contiguous E-UTRA carriers for the NE-DC combination of NR Band nX and E-UTRA Band X. Applicable contiguous intra-band NE-DC bandwidth classes are listed in Table 5.3B.0-1a.

Table 5.3B.0-1a: Intra-band contiguous NE-DC bandwidth classes

The UE channel bandwidths for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said UE channel bandwidths for band combinations with Band n90 are not listed in the tables below but are covered by this specification.

## 5.3B.1Intra-band EN-DC in FR1

## 5.3B.1.1General

The requirements for intra-band EN-DC in this specification are defined for EN-DC configurations with associated bandwidth combination sets.

For each EN-DC configuration, requirements are specified for all bandwidth combinations contained in a bandwidth combination set, which is indicated per supported band combination in the UE radio access capability. A UE can indicate support of several bandwidth combination sets per band combination.

## 5.3B.1.2BCS for Intra-band contiguous EN-DC

For intra-band contiguous EN-DC, an EN-DC configuration is consisting of an E-UTRA band and a corresponding NR band having the same frequency range which supports an intra-band contiguous EN-DC bandwidth class. For both the downlink and uplink, these EN-DC configurations comprise contigous EN-DC sub-blocks as specified in Table 5.3B.0-1 with possible additional E-UTRA sub-blocks in the downlink.

Bandwidth combination sets for intra-band contiguous EN-DC are specified in Table 5.3B.1.2-1. The EN-DC configurations and bandwidth combination sets in Table 5.3B.1.2-1 also apply to higher order EN-DC combinations that include inter-band and intra-band EN-DC on the downlink and inter-band EN-DC on the uplink. If no BCS is reported in the UE capabilities for an intra-band combination the default is that the UE supports BCS0.

Table 5.3B.1.2-1: EN-DC configurations and bandwidth combination sets defined for intra-band contiguous EN-DC

## 5.3B.1.3BCS for Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC, an EN-DC configuration is consisting of an E-UTRA band and a corresponding NR band having the same frequency range which supports E-UTRA and NR carriers, where E-UTRA configuration is indicated by using E-UTRA CA bandwidth class as defined in TS 36.101 [4] and NR configuration is indicated by using NR CA bandwidth class as defined in TS 38.101-1 [2].

Requirements for intra-band non-contiguous EN-DC are defined for the EN-DC configurations and bandwidth combination sets specified in Table 5.3B.1.3-1. The EN-DC configurations and bandwidth combination sets in Table 5.3B.1.3-1 also apply to higher order EN-DC combinations that include inter-band and intra-band EN-DC on the downlink and inter-band EN-DC on the uplink.  If no BCS is reported in the UE capabilities for an intra-band combination the default is that the UE supports BCS0.

Table 5.3B.1.3-1: EN-DC configurations and bandwidth combination sets defined for intra-band non-contiguous EN-DC

Table 5.3B.1.3-2: EN-DC configurations and bandwidth combination sets defined for mixed intra-band contiguous and non-contiguous EN-DC

## 5.3B.1aIntra-band NE-DC in FR1

## 5.3B.1a.1General

The requirements for intra-band NE-DC in this specification are defined for NE-DC configurations with associated bandwidth combination sets.

For each NE-DC configuration, requirements are specified for all bandwidth combinations contained in a bandwidth combination set, which is indicated per supported band combination in the UE radio access capability. A UE can indicate support of several bandwidth combination sets per band combination.

## 5.3B.1a.2BCS for Intra-band contiguous NE-DC

For intra-band contiguous NE-DC, an NE-DC configuration is a single operating band supporting an intra-band contiguous NE-DC bandwidth class.

Bandwidth combination sets for intra-band contiguous NE-DC are specified in Table 5.3B.1a.2-1. The NE-DC configurations and bandwidth combination sets in Table 5.3B.1a.2-1 also apply to higher order NE-DC combinations that include inter-band and intra-band EN-DC on the downlink and inter-band NE-DC on the uplink. If no BCS is reported in the UE capabilities for an intra-band combination the default is that the UE supports BCS0.

Table 5.3B.1a.2-1: NE-DC configurations and bandwidth combination sets defined for intra-band contiguous NE-DC

## 5.3CVoid

## 5.3DVoid

## 5.3EUE Channel bandwidth for V2X

## 5.3E.0General

The requirements specified in clause 5.3B are applicable to NR V2X UE.

## 5.3E.1Intra-band contiguous V2X in FR1

For intra-band contiguous E-UTRA NR V2X UE, an EN-DC bandwidth class in Table 5.3B.0-1 are considered to specify the V2X transmission/reception configurations.

Bandwidth combination sets and V2X transmission/reception configurations for intra-band contiguous V2X UE are specified in Table 5.3E.1-1.

Table 5.3E.1-1: E-UTRA-NR V2X configurations and bandwidth combination sets for intra-band contiguous V2X UE

## 5.3E.2Intra-band non-contiguous V2X in FR1

For intra-band non-contiguous E-UTRA NR V2X UE, an EN-DC bandwidth class in Table 5.3B.0-1 are considered to specify the V2X transmission/reception configurations.

Bandwidth combination sets and SL transmission/reception configurations for intra-band non-contiguous V2X are specified in Table 5.3E.2-1.

Table 5.3E.2-1: E-UTRA-NR V2X configurations and bandwidth combination sets for intra-band non-contiguous V2X UE

## 5.3E.3Inter-band V2X in FR1

For inter-band E-UTRA NR V2X UE, the each channel bandwidth for inter-band V2X operations in FR1 is specified in TS 36.101 [4] and TS 38.101-1 [2], respectively.

## 5.4Void

## 5.4AChannel arrangement for CA

The channel arrangement for CA operations in FR1 and FR2 as specified in TS 38.101-1 [2] and TS 38.101-2 [3], respectively.

## 5.4BChannel arrangement for DC

## 5.4B.0General

The channel arrangement for intra-band EN-DC operations in FR1 is specified in TS 36.101 [4] and TS 38.101-1 [2] , respectively.

## 5.4B.1Channel spacing for intra-band EN-DC carriers

The spacing between carriers will depend on the deployment scenario, the size of the frequency block available and the channel bandwidths. The nominal channel spacing between E-UTRA carrier and an adjacent NR carrier for intra-band contiguous EN-DC is defined as following:

-For NR operating bands with 100 kHz channel raster,

Nominal Channel spacing = (BWE-UTRA_Channel + BWNR_Channel)/2

-For NR operating bands with 15 kHz channel raster,

-Nominal Channel spacing = (BWE-UTRA_Channel + BWNR_Channel)/2+{-5kHz, 0kHz, 5kHz} for ∆FRaster equals to 15 kHz

-Nominal Channel spacing = (BWE-UTRA_Channel + BWNR_Channel)/2+{-10 kHz, 0 kHz, 10 kHz} for ∆FRaster equals to 30 kHz

where BWE-UTRA_Channel and BWNR_Channel are the channel bandwidths of the E-UTRA and NR carriers, ∆FRaster is the  band dependent channel raster granularity defined in TS38.101-1[2]. The channel spacing can be adjusted depending on the channel raster to optimize performance in a particular deployment scenario.

For intra-band non-contiguous EN-DC the channel spacing between E-UTRA and NR carriers shall be larger than the nominal channel spacing defined in this clause.

UE indicating [intraBandENDC-NominalSpacing] for a non-contiguous intra-band EN-DC configuration shall meet requirements for intra-band non-contiguous EN-DC with equal to or greater than nominal channel spacing

## 5.5Configuration

## 5.5AConfiguration for CA

## 5.5A.1Inter-band CA configurations between FR1 and FR2

Table 5.5A.1-1a: Void

Table 5.5A.1-1b: Void

Table 5.5A.1-1c: Void

Table 5.5A.1-1d: Void

Table 5.5A.1-1e: Void

Table 5.5A.1-1f: Void

Table 5.5A.1-1g: Void

Table 5.5A.1-1h: Void

Table 5.5A.1-1i: Void

Table 5.5A.1-1j: Void

Table 5.5A.1-1k: Void

Table 5.5A.1-1l: Void

Table 5.5A.1-1m: Void

Table 5.5A.1-1n: Void

Table 5.5A.1-1o: Void

Table 5.5A.1-1p: Void

Table 5.5A.1-2: Void

Table 5.5A.1-3: Void

Table 5.5A.1-4: Void

## 5.5A.1.0General

The configurations for operating bands for CA including Band n41 also apply for the corresponding operating bands for CA with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said configuration for operating bands for CA with Band n90 are not listed in the tables below but are covered by this specification.

The configuration tables for CA describe Bandwidth Combination Sets. Bandwidth Combination Set 4 and 5 contains all possible defined channel bandwidths for each FR1 band in the combination. The fact that BCS4 and BCS5 contains all channel bandwidths for each FR1 band does not alter if a bandwidth is mandatory or optional for a given band. Bandwidths that are identified as optional in Table 5.3.5-1 of TS 38.101-1 [2] for a given release are still optional for UEs that support BCS4 or BCS5, where the bandwidths the UE supports for each band, the maximum bandwidth and/or minimum bandwidth for the band in the band combination are indicated in the UE capabilities. The minimum bandwidth per CC and maximum aggregated FDD, TDD and total bandwidth per band combination may be indicated only for BCS5 and BCS5 as described in 38.306 [11] shall not be indicated together with BCS4 for a CA configuration. For inter-band CA combinations including intra-band CA and with BCS4 or BCS5 in the following configuration tables, the Bandwidth Combination Sets for the FR1 intra-band CA are BCS4 or BCS5, respectively, and the Bandwidth Combination Sets for the FR2 intra-band CA are BCS0.

In the CA configuration tables of clause 5.5A.1:

-Uplink CA configuration entries with "-" mean that any valid constituent band of the downlink inter-band CA combination can be configured as a single uplink carrier,

-Unless otherwise noted, all of the valid downlink constituent bands can be configured as a single uplink carrier,

-If an uplink CA configuration is supported, its fallback single uplink is also supported.

Unless stated otherwise, simultaneous Rx/Tx capability is mandatory for

-FR1+FR2 FDD-TDD CA combinations if FR1 FDD band (<4GHz) is aggregated with FR2 TDD bands.

-FR1+FR2 TDD-TDD CA combinations with FR1 bands up to 5GHz and FR2 bands above 24GHz.

## 5.5A.1.1Inter-band CA configurations between FR1 and FR2 (two bands)

## Table 5.5A.1.1-1a ~ Table 5.5A.1.1-1g

Table 5.5A.1.1-1a: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1b: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1c: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1d: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1e: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1f: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1g: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

## Table 5.5A.1.1-1h ~ Table 5.5A.1.1-1k

Table 5.5A.1.1-1h: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1i: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1j: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1k: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

## Table 5.5A.1.1-1l ~ Table 5.5A.1.1-1p

Table 5.5A.1.1-1l: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1m: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1n: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1o: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

Table 5.5A.1.1-1p: Inter-band CA configurations and bandwidth combinations sets between FR1 and FR2 (two bands)

The following notes are applied to the above tables:

NOTE 1:This UE channel bandwidth is optional in this release of the specification. (From Table 5.3.5-1 of 38.101-1)

NOTE 2:The CA configurations are given in Table 5.5A.1-1 of either TS 38.101-1 or TS 38.101-2 where unless otherwise stated BCS0 is referred to.

NOTE 3: The SCS of each channel bandwidth for NR FR1 and NR FR2 band refers to Table 5.3.5-1 of TS 38.101-1 and TS 38.101-2 respectively.

NOTE 4:This UE channel bandwidth is optional in this release of the specification.

NOTE 5:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a SCell part of DC or CA configuration (In Table 5.3.5-1 in 38.101-1).

NOTE 6: The delimiter “/” is only used in the uplink configurations for the sake of simplicity. For example, CA_nxA-nyA/B/C denotes CA_nxA-nyA, CA_nxA-nyB and CA_nxA-nyC, where nx and ny are two NR bands, ny is a FR2 band and A, B and C are the corresponding bandwidth classes respectively.

## 5.5A.1.2Inter-band CA configurations between FR1 and FR2 (three bands)

## Table 5.5A.1.2-1a

Table 5.5A.1.2-1a: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (three bands)

## Table 5.5A.1.2-1b

Table 5.5A.1.2-1b: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (three bands)

## Table 5.5A.1.2-1c

Table 5.5A.1.2-1c: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (three bands)

The following notes are applied to the above tables.

NOTE 1:The SCS of each channel bandwidth for NR FR1 and NR FR2 band refers to Table 5.3.5-1 of TS 38.101-1 and TS 38.101-2 respectively.

NOTE 2:The CA configurations are given in Table 5.5A.1-1 of either TS 38.101-1 or TS 38.101-2 where unless otherwise stated BCS0 is referred to.

NOTE 3: The delimiter “/” is only used in the uplink configurations for the sake of simplicity. For example, CA_nxA-nyA/B/C denotes CA_nxA-nyA, CA_nxA-nyB and CA_nxA-nyC, where nx and ny are two NR bands, ny is a FR2 band and A, B and C are the corresponding bandwidth classes respectively.

## 5.5A.1.3Inter-band CA configurations between FR1 and FR2 (four bands)

Table 5.5A.1.3-1a

Table 5.5A.1.3-1a: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (four bands)

Table 5.5A.1.3-1b

Table 5.5A.1.3-1b: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (four bands)

The following notes are applied to the above tables.

NOTE 1: The SCS of each channel bandwidth for NR FR1 and NR FR2 band refers to Table 5.3.5-1 of TS 38.101-1 and TS 38.101-2 respectively.

NOTE 2:The CA configurations are given in Table 5.5A.1-1 of either TS 38.101-1 or TS 38.101-2 where unless otherwise stated BCS0 is referred to.

NOTE 3: The delimiter “/” is only used in the uplink configurations for the sake of simplicity. For example, CA_nxA-nyA/B/C denotes CA_nxA-nyA, CA_nxA-nyB and CA_nxA-nyC, where nx and ny are two NR bands, ny is a FR2 band and A, B and C are the corresponding bandwidth classes respectively.

## 5.5A.1.4Inter-band CA configurations between FR1 and FR2 (five bands)

Table 5.5A.1.4-1: Inter-band CA configurations and bandwidth combination sets between FR1 and FR2 (five bands)

## 5.5BConfiguration for DC

## 5.5B.1General

The operating bands and bandwidth classes are specified for operation with EN-DC, NGEN-DC, NE-DC or NR-DC configured. The EN-DC, NGEN-DC or NE-DC band combinations include at least one E-UTRA operating band.

For EN-DC or NE-DC configurations indicated by column "Single Uplink allowed" (e.g., problematic band combinations as defined in TS 38.306 [11]) in tables in this clause the UE may indicate capability of not supporting simultaneous dual and triple uplink operation due to possible intermodulation interference to its own primary downlink channel bandwidth of PCell or PSCell if the intermodulation order is 2 or if the intermodulation order is 3 for the combinations when both operating bands are between 450 MHz – 960 MHz or between 1427 MHz – 2690 MHz. When LTE and NR transmissions collide, simultaneous dual transmissions may not be supported by UE for these EN-DC band combinations for which only single switched UL is supported.

In the case for EN-DC or NE-DC configurations listed in tables in this clause for which the intermodulation products caused by the dual and triple uplink operation fall into the receive band but do not interfere with its own primary downlink channel bandwidth of PCell or PSCell as defined in Annex I the UE is mandated to operate in dual and triple uplink mode. Single Uplink is also allowed for certain band combinations where intermodulation or reverse intermodulation products could create difficulty for meeting emission requirementsFor EN-DC combinations of order 3 or higher, "Single Uplink allowed" UL configurations captured in Table 5.5B.2-1, Table 5.5B.3-1, and Table 5.5B.4-1 apply.

If multiple UL DC configurations are listed for multiple DL DC configurations, valid uplink configurations are such that uplink does not have more carriers than downlink.

The configurations for operating bands for DC including Band n41 also apply for the corresponding operating bands for DC with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said configuration for operating bands for DC with Band n90 are not listed in the tables below but are covered by this specification.

Non contiguous resource allocation and almost contiguous allocation are not applicable for E UTRA or NR carrier part of intra band EN DC configuration.

If the mandatory simultaneous Rx/Tx capability applies for a lower order DC configuration, when the applicable lower order DC configuration is a band pair in a higher order DC configuration, the mandatory simultaneous Rx/Tx capability also applies for the band pair in the higher order DC configuration.

Unless stated otherwise, simultaneous Rx/Tx capability is mandatory for FDD-TDD EN-DC combinations. Simultaneous Rx/Tx capability is mandatory without signaling for FDD-FDD EN-DC combinations

For a higher order EN-DC band combination of which DC_20_n28/DC_28_n20/CA_20-28/CA_n20-n28 is a subset, the frequency range in band n28/28 is restricted for the higher order band combination to 703-733 MHz for the UL and 758-788 MHz for the DL.

For NR inter-band dual connectivity specified in 5.5B.7, the corresponding NR CA configurations in 5.5A.1, i.e., dual uplink inter-band carrier aggregation between FR1 and FR2 with uplink assigned to two NR bands, are applicable to Dual Connectivity.

NOTE 1:Requirements for the dual connectivity configurations are defined in the clause corresponding NR uplink CA between FR1 and FR2 configurations, unless otherwise specified.

## 5.5B.2Intra-band contiguous EN-DC

Table 5.5B.2-1: Intra-band contiguous EN-DC configurations

## 5.5B.2aIntra-band contiguous NE-DC

Table 5.5B.2a-1: Intra-band contiguous NE-DC configurations

## 5.5B.3Intra-band non-contiguous EN-DC

Table 5.5B.3-1: Intra-band non-contiguous EN-DC configurations

Table 5.5B.3-2: Intra-band EN-DC configurations for mixed intra-band contiguous and non-contiguous EN-DC

## 5.5B.4Inter-band EN-DC within FR1

5.5B.4.0 General

By default, power class 3 is applicable for the EN-DC configurations listed in the following sub-clauses. The applicability of higher power class(es) is described in the EN-DC configuration tables. For higher order EN-DC band combinations, the applicability of higher power class(es) is extended based on the following conditions:

For an inter-band EN-DC combination with intra-band CA, UE may support the same higher power class(es) that are defined for the inter-band EN-DC combination composed of the same band without intra-band CA.

For an inter-band EN-DC combination with 4 or more DL bands without intra-band CA, the higher power class(es) may be supported when the same higher power class(es) are specified for all its fallback combinations.

## 5.5B.4.1Inter-band EN-DC configurations within FR1 (two bands)

Table 5.5B.4.1-1: Inter-band EN-DC configurations within FR1 (two bands)

## 5.5B.4.2Inter-band EN-DC configurations within FR1 (three bands)

Table 5.5B.4.2-1: Inter-band EN-DC configurations within FR1 (three bands)

## 5.5B.4.3Inter-band EN-DC configurations within FR1 (four bands)

Table 5.5B.4.3-1: Inter-band EN-DC configurations within FR1 (four bands)

## 5.5B.4.4Inter-band EN-DC configurations within FR1 (five bands)

Table 5.5B.4.4-1: Inter-band EN-DC configurations within FR1 (five bands)

## 5.5B.4.5Inter-band EN-DC configurations within FR1 (six bands)

Table 5.5B.4.5-1: Inter-band EN-DC configurations within FR1 (six bands)

## 5.5B.4aInter-band NE-DC within FR1

## 5.5B.4a.1Inter-band NE-DC configurations within FR1 (two bands)

Table 5.5B.4a.1-1: Inter-band NE-DC configurations within FR1 (two bands)

## 5.5B.4a.2Inter-band NE-DC configurations within FR1 (three bands)

Table 5.5B.4a.2-1: Inter-band NE-DC configurations within FR1 (three bands)

## 5.5B.4a.3Inter-band NE-DC configurations within FR1 (four bands)

Table 5.5B.4a.3-1: Inter-band NE-DC configurations within FR1 (four bands)

## 5.5B.4a.4Inter-band NE-DC configurations within FR1 (five bands)

Table 5.5B.4a.4-1: Inter-band NE-DC configurations within FR1 (five bands)

## 5.5B.5Inter-band EN-DC including FR2

## 5.5B.5.1Inter-band EN-DC configurations including FR2 (two bands)

Table 5.5B.5.1-1: Inter-band EN-DC configurations including FR2 (two bands)

## 5.5B.5.2Inter-band EN-DC configurations including FR2 (three bands)

Table 5.5B.5.2-1: Inter-band EN-DC configurations including FR2 (three bands)

## 5.5B.5.3Inter-band EN-DC configurations including FR2 (four bands)

Table 5.5B.5.3-1: Inter-band EN-DC configurations including FR2 (four bands)

## 5.5B.5.4Inter-band EN-DC configurations including FR2 (five bands)

Table 5.5B.5.4-1: Inter-band EN-DC configurations including FR2 (five bands)

## 5.5B.5.5Void

## 5.5B.5aInter-band NE-DC including FR2

## 5.5B.5a.1Inter-band NE-DC configurations including FR2 (two bands)

Table 5.5B.5a.1-1: Inter-band NE-DC configurations including FR2 (two bands)

## 5.5B.5a.2Inter-band NE-DC configurations including FR2 (three bands)

Table 5.5B.5a.2-1: Inter-band NE-DC configurations including FR2 (three bands)

## 5.5B.5a.3Inter-band NE-DC configurations including FR2 (four bands)

Table 5.5B.5a.3-1: Inter-band NE-DC configurations including FR2 (four bands)

## 5.5B.5a.4Inter-band NE-DC configurations including FR2 (five bands)

Table 5.5B.5a.4-1: Inter-band NE-DC configurations including FR2 (five bands)

## 5.5B.6Inter-band EN-DC including FR1 and FR2

## 5.5B.6.1Void

## 5.5B.6.2Inter-band EN-DC configurations including FR1 and FR2 (three bands)

Table 5.5B.6.2-1: Inter-band EN-DC configurations including FR1 and FR2 (three bands)

## 5.5B.6.3Inter-band EN-DC configurations including FR1 and FR2 (four bands)

Table 5.5B.6.3-1: Inter-band EN-DC configurations including FR1 and FR2 (four bands)

## 5.5B.6.4Inter-band EN-DC configurations including FR1 and FR2 (five bands)

Table 5.5B.6.4-1: Inter-band EN-DC configurations including FR1 and FR2 (five bands)

## 5.5B.6.5Inter-band EN-DC configurations including FR1 and FR2 (six bands)

Table 5.5B.6.5-1: Inter-band EN-DC configurations including FR1 and FR2 (six bands)

## 5.5B.6aInter-band NE-DC including FR1 and FR2

## 5.5B.6a.1Void

## 5.5B.6a.2Inter-band NE-DC configurations including FR1 and FR2 (three bands)

Table 5.5B.6a.2-1: Inter-band NE-DC configurations including FR1 and FR2 (three bands)

## 5.5B.6a.3Inter-band NE-DC configurations including FR1 and FR2 (four bands)

Table 5.5B.6a.3-1: Inter-band NE-DC configurations including FR1 and FR2 (four bands)

## 5.5B.6a.4Inter-band NE-DC configurations including FR1 and FR2 (five bands)

Table 5.5B.6a.4-1: nter-band NE-DC configurations including FR1 and FR2 (five bands)

## 5.5B.6a.5Inter-band NE-DC configurations including FR1 and FR2 (six bands)

Table 5.5B.6a.5-1: Inter-band NE-DC configurations including FR1 and FR2 (six bands)

## 5.5B.7Inter-band NR-DC between FR1 and FR2

## 5.5B.7.0General

The configurations and bandwidth combination sets for the FR1-FR2 NR-DC combinations in the following sub-sections are defined in the tables for FR1-FR2 carrier aggregation in section 5.5A.1.

## 5.5B.7.1Inter-band NR-DC configurations between FR1 and FR2 (two bands)

Table 5.5B.7-1: Inter-band NR-DC configurations between FR1 and FR2 (two bands)

## 5.5B.7.2Inter-band NR-DC configurations between FR1 and FR2 (three bands)

Table 5.5B.7.2-1: Inter-band NR-DC configurations between FR1 and FR2 (three bands)

## 5.5B.7.3Inter-band NR-DC configurations between FR1 and FR2 (four bands)

Table 5.5B.7-3: Inter-band NR-DC configurations between FR1 and FR2 (four bands)

## 5.5B.7.4Inter-band NR-DC configurations between FR1 and FR2 (five bands)

Table 5.5B.7-4: Inter-band NR-DC configurations between FR1 and FR2 (five bands)

## 5.5CVoid

## 5.5DVoid

## 5.5EConfiguration for V2X operation

## 5.5E.1General

The operating bands and bandwidth classes are specified for V2X operation.

## 5.5E.2Intra-band contiguous V2X operation in FR1

Table 5.5E.2-1: Intra-band contiguous V2X configurations

## 5.5E.3Intra-band non-contiguous V2X operation in FR1

Table 5.5E.3-1: Intra-band non-contiguous V2X configurations

## 5.5E.4Inter-band V2X operation in FR1

## 5.5E.4.1Inter-band V2X configurations within FR1 (two bands)

Table 5.5E.4.1-1: Inter-band V2X configurations
