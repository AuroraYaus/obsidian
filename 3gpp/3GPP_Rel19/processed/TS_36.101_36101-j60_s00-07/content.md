# TS 36.101 36101-j60_s00-07

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

The present document establishes the minimum RF characteristics and minimum performance requirements for E-UTRA User Equipment (UE).

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]ITU-R Recommendation SM.329, "Unwanted emissions in the spurious domain"

[3]ITU-R Recommendation M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000".

[4]3GPP TS 36.211: "Physical Channels and Modulation".

[5]3GPP TS 36.212: "Multiplexing and channel coding".

[6]3GPP TS 36.213: "Physical layer procedures".

[7]3GPP TS 36.331: " Requirements for support of radio resource management ".

[8]3GPP TS 36.307: " Requirements on User Equipments (UEs) supporting a release-independent frequency band".

[9]3GPP TS 36.423: "X2 application protocol (X2AP) ".

[10]3GPP TS 23.303: "Technical Specification Group Services and System Aspects; Proximity-based services (ProSe); Stage 2".

[11]3GPP TS36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2".

[12]3GPP TS36.104: "Base Station (BS) radio transmission and reception".

[13]ETSI TS 102 792: "Intelligent Transport Systems (ITS); Mitigation techniques to avoid interference between European CEN Dedicated Short Range Communication (CEN DSRC) equipment and Intelligent Transport Systems (ITS) operating in the 5 GHz frequency range".

[14]3GPP TS 36.306: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio access capabilities".

[15]3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”

[16]3GPP TS 23.256: “Support of Uncrewed Aerial Systems (UAS) connectivity, identification and tracking; Stage 2”.

[17]ECC Decision(22)07, "Harmonised technical conditions for the usage of aerial UE for communications based on LTE and 5G NR in the bands 703-733 MHz, 832-862 MHz, 880-915 MHz, 1710-1785 MHz, 1920-1980 MHz, 2500-2570 MHz and 2570-2620 MHz harmonised for MFCN", 7 March 2025.

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply in the case of a single component carrier. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

Aerial UE: UE supporting UAS (Uncrewed Aircraft Systems) with an aerial subscription as described in TS 23.401 [15] and supporting the respective mandatory capabilities as described in TS 36.306 [14]. The UE is considered to have an aerial subscription after the UE has performed a successful authentication and authorization of the aerial subscription as described in TS 23.256 [16].

Aggregated Channel Bandwidth: The RF bandwidth in which a UE transmits and receives multiple contiguously aggregated carriers.

Aggregated Transmission Bandwidth Configuration: The number of resource block allocated within the aggregated channel bandwidth.

Carrier aggregation: Aggregation of two or more component carriers in order to support wider transmission bandwidths.

Carrier aggregation band: A set of one or more operating bands across which multiple carriers are aggregated with a specific set of technical requirements.

Carrier aggregation bandwidth class: A class defined by the aggregated transmission bandwidth configuration and maximum number of component carriers supported by a UE.

Carrier aggregation configuration: A combination of CA operating band(s) and CA bandwidth class(es) supported by a UE.

Channel edge: The lowest and highest frequency of the carrier, separated by the channel bandwidth.

Channel bandwidth: The RF bandwidth supporting a single E-UTRA RF carrier with the transmission bandwidth configured in the uplink or downlink of a cell. The channel bandwidth is measured in MHz and is used as a reference for transmitter and receiver RF requirements.

Composite spectrum emission mask: Emission mask requirement for intraband non-contiguous carrier aggregation which is a combination of individual sub-block spectrum emissions masks.

Composite spurious emission requirement: Spurious emission requirement for intraband non-contiguous carrier aggregation which is a combination of individual sub-block spurious emission requirements.

Contiguous carriers: A set of two or more carriers configured in a spectrum block where there are no RF requirements based on co-existence for un-coordinated operation within the spectrum block.

Contiguous resource allocation: A resource allocation of consecutive resource blocks within one carrier or across contiguously aggregated carriers. The gap between contiguously aggregated carriers due to the nominal channel spacing is allowed.

Contiguous spectrum: Spectrum consisting of a contiguous block of spectrum with no sub-block gaps.

Enhanced downlink control channel performance requirements type A: This defines performance requirements for downlink control channel assuming as baseline receiver reference symbol based linear minimum mean square error interference rejection combining plus CRS interference cancellation.

Enhanced downlink control channel performance requirements type B: This defines performance requirements for downlink control channel assuming as baseline receiver reference symbol based enhanced linear minimum mean square error interference rejection combining plus CRS interference cancellation.

Enhanced performance requirements type A: This defines performance requirements assuming as baseline receiver reference symbol based linear minimum mean square error interference rejection combining.

Enhanced performance requirements type B: This defines performance requirements assuming as baseline receiver using network assisted interference cancelation and suppression.

Enhanced performance requirements type C: This defines performance requirements assuming as baseline receiver      inter-stream interference cancellation.

Inter-band carrier aggregation: Carrier aggregation of component carriers in different operating bands.

NOTE:Carriers aggregated in each band can be contiguous or non-contiguous.

Intra-band contiguous carrier aggregation: Contiguous carriers aggregated in the same operating band.

Intra-band non-contiguous carrier aggregation: Non-contiguous carriers aggregated in the same operating band.

Lower sub-block edge: The frequency at the lower edge of one sub-block. It is used as a frequency reference point for both transmitter and receiver requirements.

Category NB1/NB2 stand-alone operation: category NB1/NB2 is operating standalone when it utilizes its own spectrum, for example the spectrum used by GERAN systems as a replacement of one or more GSM carriers, as well as scattered spectrum for potential IoT deployment.

Category NB1/NB2 guard band operation: category NB1/NB2 is operating in guard band when it utilizes the unused resource block(s) within a E-UTRA carrier’s guard-band.

Category NB1/NB2 in-band operation: category NB1/NB2 is operating in-band when it utilizes the resource block(s) within a normal E-UTRA carrier or within a normal NR carrier plus 15 kHz at each edge (and not within NR minimum guard band).

Non-contiguous spectrum: Spectrum consisting of two or more sub-blocks separated by sub-block gap(s).

ProSe-enabled UE: A UE that supports ProSe requirements and associated procedures.

NOTE: As defined in TS 23.303 [10].

ProSe Direct Communication: A communication between two or more UEs in proximity that are ProSe-enabled.

NOTE: As defined in TS 23.303 [10].

ProSe Direct Discovery: A procedure employed by a ProSe-enabled UE to discover other ProSe-enabled UEs in its vicinity.

NOTE: As defined in TS 23.303 [10].

sTTI : A transmission time interval (TTI) of either one slot or one subslot as defined in TS 36.211 [4] on either uplink or downlink.

Sub-block: This is one contiguous allocated block of spectrum for transmission and reception by the same UE. There may be multiple instances of sub-blocks within an RF bandwidth.

Sub-block bandwidth: The bandwidth of one sub-block.

Sub-block gap: A frequency gap between two consecutive sub-blocks within an RF bandwidth, where the RF requirements in the gap are based on co-existence for un-coordinated operation.

Synchronized operation: Operation of TDD in two different systems, where no simultaneous uplink and downlink occur.

Unsynchronized operation: Operation of TDD in two different systems, where the conditions for synchronized operation are not met.

Upper sub-block edge: The frequency at the upper edge of one sub-block. It is used as a frequency reference point for both transmitter and receiver requirements.

V2X Communication: V2X (Vehicle to Everything) service is operating in ITS spectrum and/or LTE licensed operating bands.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

BWChannelChannel bandwidth

BWChannel,block Sub-block bandwidth, expressed in MHz. BWChannel,block= Fedge,block,high- Fedge,block,low.

BWChannel_CA Aggregated channel bandwidth, expressed in MHz.

BWGBVirtual guard band to facilitate transmitter (receiver) filtering above / below edge CCs.

Transmitted energy per RE for reference symbols during the useful part of the symbol, i.e. excluding the cyclic prefix, (average power normalized to the subcarrier spacing) at the eNode B transmit antenna connector

The averaged received energy per RE of the wanted signal during the useful part of the symbol, i.e. excluding the cyclic prefix, at the UE antenna connector; average power is computed within a set of REs used for the transmission of physical channels (including user specific RSs when present), divided by the number of REs within the set, and normalized to the subcarrier spacing

FFrequency

Fagg_alloc_lowAggregated Transmission Bandwidth Configuration. The lowest frequency of the simultaneously transmitted resource blocks.

Fagg_alloc_highAggregated Transmission Bandwidth Configuration. The highest frequency of the simultaneously transmitted resource blocks.

FInterferer (offset)Frequency offset of the interferer (between the center frequency of the interferer and the carrier frequency of the carrier measured)

FInterfererFrequency of the interferer

FIoffsetFrequency offset of the interferer (between the center frequency of the interferer and the closest edge of the carrier measured)

FCFrequency of the carrier centre frequency

FC_aggAggregated Transmission Bandwidth Configuration.  Center frequency of the aggregated carriers.

FC,block, highCenter frequency of the highest transmitted/received carrier in a sub-block.

FC,block, lowCenter frequency of the lowest transmitted/received carrier in a sub-block.

FC_low The centre frequency of the lowest carrier, expressed in MHz.

FC_high The centre frequency of the highest carrier, expressed in MHz.

FDL_lowThe lowest frequency of the downlink operating band

FDL_highThe highest frequency of the downlink operating band

FUL_lowThe lowest frequency of the uplink operating band

FUL_highThe highest frequency of the uplink operating band

Fedge,block,low The lower sub-block edge, where Fedge,block,low = FC,block,low - Foffset.

Fedge,block,high The upper sub-block edge, where Fedge,block,high = FC,block,high + Foffset.

Fedge_low The lower edge of aggregated channel bandwidth, expressed in MHz.

Fedge_high The higher edge of aggregated channel bandwidth, expressed in MHz.

Foffset Frequency offset from FC_high to the higher edge or FC_low to the lower edge.

Foffset,block,lowSeparation between lower edge of a sub-block and the center of the lowest component carrier within the sub-block

Foffset,block,highSeparation between higher edge of a sub-block and the center of the highest component carrier within the sub-block

Foffset_NS_23Frequency offset in MHz needed if NS_23 is used

FOOBThe boundary between the E-UTRA out of band emission and spurious emission domains.

The power spectral density of the total input signal (power averaged over the useful part of the symbols within the transmission bandwidth configuration, divided by the total number of RE for this configuration and normalised to the subcarrier spacing) at the UE antenna connector, including the own-cell downlink signal

The total transmitted power spectral density of the own-cell downlink signal (power averaged over the useful part of the symbols within the transmission bandwidth configuration, divided by the total number of RE for this configuration and normalised to the subcarrier spacing) at the eNode B transmit antenna connector

The total received power spectral density of the own-cell downlink signal (power averaged over the useful part of the symbols within the transmission bandwidth configuration, divided by the total number of RE for this configuration and normalised to the subcarrier spacing) at the UE antenna connector

The received power spectral density of the total noise and interference for a certain RE (average power obtained within the RE and normalized to the subcarrier spacing) as measured at the UE antenna connector

LCRBTransmission bandwidth which represents the length of a contiguous resource block allocation expressed in units of resources blocks

LCtoneTransmission bandwidth which represents the length of a contiguous sub-carrier allocation expressed in units of tones

NcpCyclic prefix length

NDL Downlink EARFCN

The power spectral density of a white noise source (average power per RE normalised to the subcarrier spacing), simulating interference from cells that are not defined in a test procedure, as measured at the UE antenna connector

The power spectral density of a white noise source (average power per RE normalized to the subcarrier spacing), simulating interference in non-CRS symbols in ABS subframe from cells that are not defined in a test procedure, as measured at the UE antenna connector.

The power spectral density of a white noise source (average power per RE normalized to the subcarrier spacing), simulating interference in CRS symbols in ABS subframe from all cells that are not defined in a test procedure, as measured at the UE antenna connector.

The power spectral density of a white noise source (average power per RE normalised to the subcarrier spacing), simulating interference in non-ABS subframe from cells that are not defined in a test procedure, as measured at the UE antenna connector

The power spectral density (average power per RE normalised to the subcarrier spacing) of the summation of the received power spectral densities of the strongest interfering cells explicitly defined in a test procedure plus , as measured at the UE antenna connector. The respective power spectral density of each interfering cell relative to  is defined by its associated DIP value, or the respective power spectral density of each interfering cell relative to  is defined by its associated Es/Noc value.

NOffs-DL Offset used for calculating downlink EARFCN

NOffs-UL Offset used for calculating uplink EARFCN

The power spectral density of a white noise source (average power per RE normalised to the subcarrier spacing) simulating eNode B transmitter impairments as measured at the eNode B transmit antenna connector

NRBTransmission bandwidth configuration, expressed in units of resource blocks

NRB_aggThe number of the aggregated RBs within the fully allocated Aggregated Channel bandwidth.

NRB_allocTotal number of simultaneously transmitted resource blocks in Channel bandwidth or Aggregated Channel Bandwidth.

NRB,cThe transmission bandwidth configuration of component carrier c, expressed in units of resource blocks

NRB,largest BWThe largest transmission bandwidth configuration of the component carriers in the bandwidth combination, expressed in units of resource blocks

NRXNumber of receiver antennas

NtoneTransmission bandwidth configuration for category NB1 and NB2, expressed in units of tones.

Ntone 3.75kHzTransmission bandwidth configuration for category NB1 and NB2 with 3.75 kHz sub-carrier spacing, expressed in units of tones.

Ntone 15kHz Transmission bandwidth configuration for category NB1 and NB2 with 15 kHz sub-carrier spacing, expressed in units of tones.

NULUplink EARFCN.

RavMinimum average throughput per RB.

PCMAXThe configured maximum UE output power.

PCMAX, cThe configured maximum UE output power for serving cell c.

PEMAX Maximum allowed UE output power signalled by higher layers. Same as IE P-Max, defined in [7].

PEMAX, cMaximum allowed UE output power signalled by higher layers for serving cell c. Same as IEP-Max, defined in [7].

PInterfererModulated mean power of the interferer

PPowerClassPPowerClass is the nominal UE power (i.e., no tolerance).

PPowerClass_DefaultPPowerClass_Default is the default nominal UE power (i.e., no tolerance) for the band.

PUMAXThe measured configured maximum UE output power.

PuwPower of an unwanted DL signal

PwPower of a wanted DL signal

RBstart Indicates the lowest RB index of transmitted resource blocks.

RBendIndicates the highest RB index of transmitted resource blocks.

Tno_hoppingTransmission period within a TTI duration when consecutive symbols are transmitted without applying any frequency hopping

ΔfOOBΔ Frequency of Out Of Band emission.

ΔPPowerClass Adjustment to maximum output power for a given power class.

ΔRIB,cAllowed reference sensitivity relaxation due to support for inter-band CA operation, for serving cell c.

ΔRIB,4RReference sensitivity adjustment due to support for 4 antenna ports.

ΔRIB,8RReference sensitivity adjustment due to support for 8 antenna ports.

ΔTIB,cAllowed maximum configured output power relaxation due to support for inter-band CA operation, for serving cell c.

TCAllowed operating band edge transmission power relaxation.

TC,c Allowed operating band edge transmission power relaxation for serving cell c.

TProSeAllowed operating band transmission power relaxation due to support of E-UTRA ProSe on an operating band.

According to Clause 5.2 in TS 36.213 [6]

According to Clause 5.2 in TS 36.213 [6]

Test specific auxiliary variable used for the purpose of downlink power allocation, defined in Annex C.3.2.

WgapSub-block gap size

Wgap_LSub-block gap size between lowest two CCs in frequency domain on CA_X-X-X

Wgap_HSub-block gap size between highest two CCs in frequency domain on CA_X-X-X

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

ABSAlmost Blank Subframe

ACLRAdjacent Channel Leakage Ratio

ACSAdjacent Channel Selectivity

A-MPRAdditional Maximum Power Reduction

AWGNAdditive White Gaussian Noise

BSBase Station

CACarrier Aggregation

CA_XIntra-band contiguous CA of component carriers in one sub-block within Band X where X is the applicable E-UTRA operating band

CA_X-XIntra-band non-contiguous CA of component carriers in two sub-blocks within Band X where X is the applicable E-UTRA operating band

CA_X-X-XIntra-band non-contiguous CA of component carriers in three sub-blocks within Band X where X is the applicable E-UTRA operating band

CA_X-X-X-XIntra-band non-contiguous CA of component carriers in four sub-blocks within Band X where X is the applicable E-UTRA operating band

CA_X-YInter-band CA of component carrier(s) in one sub-block within Band X and component carrier(s) in one sub-block within Band Y where X and Y are the applicable E-UTRA operating band

CA_X-X-YCA of component carriers in two sub-blocks within Band X and component carrier(s) in one sub-block within Band Y where X and Y are the applicable E-UTRA operating bands

CCComponent Carriers

CGCarrier Group

CPECustomer Premise Equipment

CPE_XCustomer Premise Equipment for E-UTRA operating band X

CWContinuous Wave

DCDual Connectivity

DC_X-YInter-band DC of component carrier(s) in one sub-block within Band X and component carrier(s) in one sub-block within Band Y where X and Y are the applicable E-UTRA operating band

DLDownlink

DIPDominant Interferer Proportion

EARFCN E-UTRA Absolute Radio Frequency Channel Number

EIRPEffective Isotropic Radiated Power

EPREEnergy Per Resource Element

E-UTRA Evolved UMTS Terrestrial Radio Access

EUTRANEvolved UMTS Terrestrial Radio Access Network

EVMError Vector Magnitude

FDDFrequency Division Duplex

FRCFixed Reference Channel

GNSSGlobal Navigation Satellite Systems

HDHalf-Duplex for Sidelink Operation

HD-FDDHalf- Duplex FDD

ITSIntelligent Transportation Systems

MCSModulation and Coding Scheme

MCGMaster Cell Group

MOPMaximum Output Power

MPRMaximum Power Reduction

MSDMaximum Sensitivity Degradation

OCNGOFDMA Channel Noise Generator

OFDMAOrthogonal Frequency Division Multiple Access

OOBOut-of-band

PAPower Amplifier

PCCPrimary Component Carrier

PMCHPhysical Multicast Channel

P-MPRPower Management Maximum Power Reduction

ProSeProximity-based Services

PSBCHPhysical Sidelink Broadcast CHannel

PSCCHPhysical Sidelink Control CHannel

PSDCHPhysical Sidelink Discovery CHannel

PSSPrimary Synchronization Signal

PSS_RAPSS-to-RS EPRE ratio for the channel PSS

SSSSSecondary Sidelink Synchronization Signal

PSSCHPhysical Sidelink Shared CHannel

PSSSPrimary Sidelink Synchronization Signal

REResource Element

REFSENSReference Sensitivity power level

r.m.sRoot Mean Square

SCCSecondary Component Carrier

SDOStandalone Downlink Only

SCGSecondary Cell Group

SINRSignal-to-Interference-and-Noise Ratio

SNRSignal-to-Noise Ratio

SSSSecondary Synchronization Signal

SSS_RASSS-to-RS EPRE ratio for the channel SSSSSSSSecondary Sidelink Synchronization Signal

TDDTime Division Duplex

UAVUncrewed Aerial Vehicle

UEUser Equipment

ULUplink

UL-MIMOUp Link Multiple Antenna transmission

UMTSUniversal Mobile Telecommunications System

UTRAUMTS Terrestrial Radio Access

UTRANUMTS Terrestrial Radio Access Network

V2XVehicle to Everything

xCH_RAxCH-to-RS EPRE ratio for the channel xCH in all transmitted OFDM symbols not containing cell-specific RS

xCH_RBxCH-to-RS EPRE ratio for the channel xCH in all transmitted OFDM symbols containing cell-specific RS

## 4General

## 4.1Relationship between minimum requirements and test requirements

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification TS 36.521-1 Annex F defines Test Tolerances. These Test Tolerances are individually calculated for each test. The Test Tolerances are used to relax the Minimum Requirements in this specification to create Test Requirements.

The measurement results returned by the Test System are compared - without any modification - against the Test Requirements as defined by the shared risk principle.

The Shared Risk principle is defined in ITU-R M.1545 [3].

## 4.2Applicability of minimum requirements

a)In this specification the Minimum Requirements are specified as general requirements and additional requirements. Where the Requirement is specified as a general requirement, the requirement is mandated to be met in all scenarios

b)For specific scenarios for which an additional requirement is specified, in addition to meeting the general requirement, the UE is mandated to meet the additional requirements.

c)The reference sensitivity power levels defined in subclause 7.3 are valid for the specified reference measurement channels.

d)NOTE: Receiver sensitivity degradation may occur when:

1)The UE simultaneously transmits and receives with bandwidth allocations less than the transmission bandwidth configuration (see Figure 5.6-1), and

2)Any part of the downlink transmission bandwidth is within an uplink transmission bandwidth from the downlink center subcarrier.

e)The spurious emissions power requirements are for the long term average of the power. For the purpose of reducing measurement uncertainty it is acceptable to average the measured power over a period of time sufficient to reduce the uncertainty due to the statistical nature of the signal.

f)The requirements in this specification for TDD operating bands apply for downlink and uplink operations using Frame Structure Type 2 [4] except for Band 46 operating with Frame Structure Type 3.

g)The requirements related to subslot TTI and/or slot TTI shall apply only if UE supports multiple TTI patterns. And these requirements only apply to subslot and/or slot TTI configurations

## 4.3Void

## 4.3AApplicability of feature-specific minimum requirements

The feature-specific requirements in clauses 5, 6 and 7 are specified as suffix, where:

a)Suffix A additional requirements need to support CA

b)Suffix B additional requirements need to support UL-MIMO

c)Suffix C additional requirements need to support Dual Connectivity

d)Suffix D additional requirements need to support ProSe

e)Suffix E additional requirements need to support UE category 0, category M1, category M2, and category 1bis

f)Suffix F additional requirements need to support UE category NB1 and NB2

g)Suffix G additional requirements need to support V2X Communication

h)Suffix H additional requirements needed to support LTE based 5G terrestrial broadcast

i)Suffix K additional requirements needed to support Aerial UEs (UAV)

A terminal which supports the above features needs to meet both the general requirements and the additional requirement applicable to the additional subclause (marked by suffix as assigned in bullets above) in clauses 5, 6 and 7. Where there is a difference in requirement between the general requirements and the additional subclause requirements (suffix related) in clauses 5, 6 and 7, the tighter requirements are applicable unless stated otherwise in the additional subclause.

A terminal which supports more than one of above features in clauses 5, 6 and 7 shall meet all of the separate corresponding requirements.

For a terminal supporting CA, compliance with minimum requirements for non-contiguous intra-band carrier aggregation in any given operating band does not imply compliance with minimum requirements for contiguous intra-band carrier aggregation in the same operating band.

For a terminal supporting CA, compliance with minimum requirements for contiguous intra-band carrier aggregation in any given operating band does not imply compliance with minimum requirements for non- contiguous intra-band carrier aggregation in the same operating band.

A terminal which supports a DL CA configuration shall support all the lower order fallback DL CA combinations and it shall support at least one bandwidth combination set for each of the constituent lower order DL combinations containing all the bandwidths specified within each specific combination set of the upper order DL combination.

A terminal which supports CA, for each supported CA configuration, shall support Pcell transmissions in each of the aggregated Component Carriers unless indicated otherwise in clause 5.6A.1.

Terminal supporting Dual Connectivity configuration shall meet the minimum requirements for corresponding CA configuration (suffix A), unless otherwise specified.

For a terminal that supports ProSe Direct Communication and/or ProSe Direct Discovery, the minimum requirements are applicable when

-the UE is associated with a serving cell on the ProSe carrier, or

-the UE is not associated with a serving cell on the ProSe carrier and is provisioned with the preconfigured radio parameters for ProSe Direct Communications and/or ProSe Direct Discovery that are associated with known Geographical Area, or

-the UE is associated with a serving cell on a carrier different than the ProSe carrier, and the radio parameters for ProSe Direct Discovery on the ProSe carrier are provided by the serving cell, or

-the UE is associated with a serving cell on a carrier different than the ProSe carrier, and has a non-serving cell selected on the ProSe carrier that supports ProSe Direct Discovery and/or ProSe Direct Communication.

When the ProSe UE is not associated with a serving cell on the ProSe carrier, and the UE does not have knowledge of its geographical area, or is provisioned with preconfigured radio parameters that are not associated with any Geographical Area, ProSe transmissions are not allowed, and the requirements in Section 6.3.3D apply.

A terminal that supports simultaneous E-UTRA ProSe sidelink transmissions and E-UTRA uplink transmissions for the inter-band E-UTRA ProSe/E-UTRA bands specified in Table 5.5D-2, shall meet the minimum requirements for the corresponding inter-band UL CA configuration (suffix A), unless otherwise specified. For transmitter characteristics specified in clause 6, the terminal is required to meet the conformance tests for the corresponding inter-band UL CA configuration and is not required to be retested with simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions.

A terminal that supports E-UTRA V2X intra-band multi-carrier operation including carrier aggregation for the band specified in Table 5.5G-3, shall meet the corresponding transmitter characteristics requirements (in subclauses with suffix G in Section 6) only when there are multiple active transmissions on all of the configured carrier components. When there is only one active transmission on one of the configured carrier components, the corresponding requirements for V2X single carrier operation apply for the corresponding active carrier component.

A terminal which supports MBMS (including 15 kHz, 7.5 kHz ,1.25 kHz, 2.5 kHz and 0.37 kHz subcarrier spacing), shall meet the minimum requirements in clauses 5 and 7. A terminal which supports MBMS is not required to support all kinds of subcarrier spacing.

A terminal that supports multiple TTI patterns in different carriers, different TTI patterns can only be used when the carriers are aggregated in inter-band manner. For intra-band carrier aggregation, only same TTI patterns and same TAG are allowed in aggregated carriers.

## 4.4RF requirements in later releases

The standardisation of new frequency bands and carrier aggregation configurations (downlink and uplink aggregation) may be independent of a release. However, in order to implement a UE that conforms to a particular release but supports a band of operation or a carrier aggregation configuration that is specified in a later release, it is necessary to specify some extra requirements. TS 36.307 [8] specifies requirements on UEs supporting a frequency band or a carrier aggregation configuration that is independent of release.

NOTE:For UEs conforming to the 3GPP release of the present document, some RF requirements of later releases may be mandatory independent of whether the UE supports the bands specif or carrier aggregation configurations ied in later releases or not. The set of RF requirements of later releases that is also mandatory for UEs conforming to the 3GPP release of the present document is determined by regional regulation.

## 5Operating bands and channel arrangement

## 5.1General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE:Other operating bands and channel bandwidths may be considered in future releases.

## 5.2Void

## 5.3Void

## 5.4Void

## 5.5Operating bands

E-UTRA is designed to operate in the operating bands defined in Table 5.5-1.

Table 5.5-1 E-UTRA operating bands

## 5.5AOperating bands for CA

E-UTRA carrier aggregation is designed to operate in the operating bands defined in Tables 5.5A-1, 5.5A-2, 5.5A-2a, 5.5A-2b, 5.5A-2c, 5.5A-2d, 5.5A-3, 5.5A-4 and 5.5A-5.

Table 5.5A-1: Intra-band contiguous CA operating bands

Table 5.5A-2: Inter-band CA operating bands (two bands)

Table 5.5A-2a: Inter-band CA operating bands (three bands)

Table 5.5A-2b: Inter-band CA operating bands (four bands)

Table 5.5A-2c: Inter-band CA operating bands (five bands)

Table 5.5A-2d: Inter-band CA operating bands (six bands)

Table 5.5A-3: Intra-band non-contiguous CA operating bands (with two sub-blocks)

Table 5.5A-4: Intra-band non-contiguous CA operating bands (with three sub-blocks)

Table 5.5A-5: Intra-band non-contiguous CA operating bands (with four sub-blocks)

## 5.5BOperating bands for UL-MIMO

E-UTRA UL-MIMO is designed to operate in the operating bands defined in Table 5.5B-1.

Table 5.5B-1: Void

## 5.5COperating bands for Dual Connectivity

E-UTRA dual connectivity is designed to operate in the operating bands defined in Table 5.5C-1.

Table 5.5C-1: Inter-band dual connectivity operating bands (two bands)

Table 5.5C-2: Inter-band dual connectivity operating bands (three bands)

## 5.5DOperating bands for ProSe

E-UTRA ProSe is designed to operate in the operating bands defined in Table 5.5D-1.

Table 5.5D-1 E-UTRA ProSe operating band

E-UTRA ProSe is designed to operate concurrent with E-UTRA uplink/downlink on the operating bands combinations listed in Table 5.5D-2.

Table 5.5D-2 Inter-band E-UTRA ProSe / E-UTRA operating bands

## 5.5EOperating bands for UE category 0, UE category M1 and M2 and UE category 1bis

UE category 0 is designed to operate in the E-UTRA operating bands 2, 3, 4, 5, 8, 13, 20, 25, 26, 28 and 111 in both half duplex FDD mode and full-duplex FDD mode and in bands 39, 40 and 41 in TDD mode. The E-UTRA bands are defined in Table 5.5-1.

UE category M1 and M2 is designed to operate in the E-UTRA operating bands 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 18, 19, 20, 21, 24, 25, 26, 27, 28, 31, 54, 66, 71, 72, 73, 74, 85, 87, 88, 106, 111 in both half duplex FDD mode and full-duplex FDD mode, and in bands 39, 40, 41, 42, 43 and 48 in TDD mode. The E-UTRA bands are defined in Table 5.5-1.

UE category 1bis is designed to operate in the E-UTRA operating bands 1, 2, 3, 4, 5, 7, 8, 12, 13, 18, 20, 26, 28, 31, 66, 72 and 111 in full duplex FDD mode and in bands 34, 39, 40 and 41 in TDD mode. The E-UTRA bands are defined in Table 5.5-1

## 5.5FOperating bands for category NB1 and NB2

Category NB1 and NB2 are designed to operate in the E-UTRA operating bands 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 17, 18, 19, 20, 21, 24, 25, 26, 28, 31, 41, 42, 43, 48, 54, 65, 66, 70, 71, 72, 73, 74, 85, 87, 88, 103, 106 and 111 which are defined in Table 5.5-1. Category NB1 and NB2 are designed to operate in the NR operating bands n1, n2, n3, n5, n7, n8, n12, n14, n18, n20, n24, n25, n26, n28, n31, n41, n54, n65, n66, n70, n71, n72, n74, n90.

Category NB1 and NB2 systems operate in HD-FDD duplex mode or in TDD mode.

In case UE receives network signaling value NS_04 or NS_06 on any of the operating bands listed in Table 5.5F-1 then the lower and upper limit of those bands are shown in Table 5.5F-1 to account for the USA emission requirements.

Table 5.5F-1 E-UTRA operating bands for NB-IoT in the USA

## 5.5GOperating bands for V2X Communication

E-UTRA V2X Communication is designed to operate in the the operating bands defined in Table 5.5G-1.

Table 5.5G-1 V2X operating band

E-UTRA V2X communication is designed to operate concurrent with E-UTRA uplink/downlink on the operating bands combinations listed in Table 5.5G-2.

Table 5.5G-2 Inter-band concurrent V2X operating bands

E-UTRA V2X communication is also designed to operate for intra-band multi-carrier operation in the operating bands defined in Table 5.5G-3.

Table 5.5G-3: V2X intra-band multi-carrier operation

## 5.5HOperating bands for LTE based 5G terrestrial broadcast

LTE based 5G terrestrial broadcast is designed to operate in the the operating bands defined in Table 5.5H-1.

Table 5.5H-1 LTE based 5G terrestrial broadcast operating bands

## 5.5KOperating bands for Aerial UE

Aerial UE is designed to operate in LTE operating bands as defined in Table 5.5-1, following applicable spectrum regulations, e.g., ECC Decision (22)07 [17] for CEPT countries.

## 5.6Channel bandwidth

Requirements in present document are specified for the channel bandwidths listed in Table 5.6-1.

Table 5.6-1: Transmission bandwidth configuration NRB in E-UTRA channel bandwidths

Figure 5.6-1 shows the relation between the Channel bandwidth (BWChannel) and the Transmission bandwidth configuration (NRB). The channel edges are defined as the lowest and highest frequencies of the carrier separated by the channel bandwidth, i.e. at FC +/- BWChannel /2.

TransmissionCenter subcarrier (corresponds to DC in baseband) is not transmitted in downlinkActive Resource BlocksResource blockTransmission bandwidth configuration [NRB]bandwidth [RB]Channel bandwidth [MHz] TransmissionCenter subcarrier (corresponds to DC in baseband) is not transmitted in downlinkActive Resource BlocksResource blockTransmission bandwidth configuration [NRB]bandwidth [RB]Channel bandwidth [MHz]

Figure 5.6-1: Definition of channel bandwidth and transmission bandwidth configuration for one EUTRA carrier

## 5.6.1Channel bandwidths per operating band

a)The requirements in this specification apply to the combination of channel bandwidths and operating bands shown in Table 5.6.1-1. The transmission bandwidth configuration in Table 5.6.1-1 shall be supported for each of the specified channel bandwidths. The same (symmetrical) channel bandwidth is specified for both the TX and RX path.

Table 5.6.1-1: E-UTRA channel bandwidth

b)The use of different (asymmetrical) channel bandwidth for the TX and RX is not precluded and is intended to form part of a later release.

## 5.6AChannel bandwidth for CA

For intra-band contiguous carrier aggregation Aggregated Channel Bandwidth, Aggregated Transmission Bandwidth Configuration and Guard Bands are defined as follows, see Figure 5.6A-1.

FC,lowLower EdgeHigher EdgeLowest Carrier Transmission Bandwidth Configuration, NRB,low  [RB]FC,highFoffset,lowHighest Carrier Transmission Bandwidth Configuration NRB,high [RB]Resource blockAggregated Channel Bandwidth, BWchannel_CA [MHz]Fedge,lowFedge,highFor each carrier, the center sub carrier (corresponds to DC in baseband) is not transmitted in downlinkFoffset,highGuard BandGuard BandAggregated Transmission Bandwidth Configuration, NRB_agg [RB]FC,lowLower EdgeHigher EdgeLowest Carrier Transmission Bandwidth Configuration, NRB,low  [RB]FC,highFoffset,lowHighest Carrier Transmission Bandwidth Configuration NRB,high [RB]Resource blockAggregated Channel Bandwidth, BWchannel_CA [MHz]Fedge,lowFedge,highFor each carrier, the center sub carrier (corresponds to DC in baseband) is not transmitted in downlinkFoffset,highGuard BandGuard BandAggregated Transmission Bandwidth Configuration, NRB_agg [RB]

Figure 5.6A-1. Definition of Aggregated channel bandwidth and aggregated channel bandwidth edges

The aggregated channel bandwidth, BWChannel_CA, is defined as

BWChannel_CA = Fedge,high - Fedge,low [MHz].

The lower bandwidth edge Fedge,low and the upper bandwidth edge Fedge,high of the aggregated channel bandwidth are used as frequency reference points for transmitter and receiver requirements and are defined by

Fedge,low = FC,low - Foffset,low

Fedge,high = FC,high + Foffset,high

The lower and upper frequency offsets depend on the transmission bandwidth configurations of the lowest and highest assigned edge component carrier and are defined as

Foffset,low = (0.18NRB,low  + f1)/2 + BWGB [MHz]

Foffset,high = (0.18NRB,high + f1)/2 + BWGB [MHz]

where f1 = f for the downlink with f the subcarrier spacing and f1 = 0 for the uplink, while NRB,low and NRB,high are the transmission bandwidth configurations according to Table 5.6-1 for the lowest and highest assigned component carrier, respectively. BWGB denotes the Nominal Guard Band and is defined in Table 5.6A-1, and the factor 0.18 is the PRB bandwidth in MHz.

NOTE:The values of BWChannel_CA for UE and BS are the same if the lowest and the highest component carriers are identical.

Aggregated Transmission Bandwidth Configuration is the number of the aggregated RBs within the fully allocated Aggregated Channel bandwidth and is defined per CA Bandwidth Class (Table 5.6A-1).

For intra-band non-contiguous carrier aggregation Sub-block Bandwidth and Sub-block edges are defined as follows, see Figure 5.6A-2.

Figure 5.6A-2. Non-contiguous intraband CA terms and definitions

The lower sub-block edge of the Sub-block Bandwidth (BWChannel,block) is defined as

Fedge,block, low = FC,block,low - Foffset,block, low.

The upper sub-block edge of the Sub-block Bandwidth is defined as

Fedge,block,high = FC,block,high + Foffset,block,high .

The Sub-block Bandwidth, BWChannel,block, is defined as follows:

BWChannel,block = Fedge,block,high - Fedge,block,low [MHz]

The lower and upper frequency offsets Foffset,block,low and Foffset,block,high depend on the transmission bandwidth configurations of the lowest and highest assigned edge component carriers within a sub-block and are defined as

Foffset,block,low = (0.18NRB,low + f1) /2 + BWGB [MHz]

Foffset,block,high = (0.18NRB,high + f1)/2 + BWGB [MHz]

where f1 = f for the downlink with f the subcarrier spacing and f1 = 0 for the uplink, while NRB,low and NRB,high are the transmission bandwidth configurations according to Table 5.6-1 for the lowest and highest assigned component carrier within a sub-block, respectively. BWGB denotes the Nominal Guard Band and is defined in Table 5.6A-1, and the factor 0.18 is the PRB bandwidth in MHz.

The sub-block gap size between two consecutive sub-blocks Wgap is defined as

Wgap = Fedge,block n+1,low - Fedge,block n,high [MHz]

Table 5.6A-1: CA bandwidth classes and corresponding nominal guard bands

The channel spacing between centre frequencies of contiguously aggregated component carriers is defined in subclause 5.7.1A.

## 5.6A.1Channel bandwidths per operating band for CA

The requirements for carrier aggregation in this specification are defined for carrier aggregation configurations with associated bandwidth combination sets. For inter-band carrier aggregation, a carrier aggregation configuration is a combination of operating bands, each supporting a carrier aggregation bandwidth class. For intra-band contiguous carrier aggregation, a carrier aggregation configuration is a single operating band supporting a carrier aggregation bandwidth class.

For each carrier aggregation configuration, requirements are specified for all bandwidth combinations contained in a bandwidth combination set, which is indicated per supported band combination in the UE radio access capability. A UE can indicate support of several bandwidth combination sets per band combination.

Requirements for intra-band contiguous carrier aggregation are defined for the carrier aggregation configurations and bandwidth combination sets specified in Table 5.6A.1-1. Requirements for inter-band carrier aggregation are defined for the carrier aggregation configurations and bandwidth combination sets specified in Table 5.6A.1-2, Table 5.6A.1-2a, Table 5.6A.1-2b and Table 5.6A.1-2c. Requirements for intra-band non-contiguous carrier aggregation are defined for the carrier aggregation configurations and bandwidth combination sets specified in Table 5.6A.1-3.

The DL component carrier combinations for a given CA configuration shall be symmetrical in relation to channel centre unless stated otherwise in Table 5.6A.1-1, Table 5.6A.1-2, Table 5.6A.1-2a, Table 5.6A.1-2b and Table 5.6A.1-2c.

Table 5.6A.1-1: E-UTRA CA configurations and bandwidth combination sets defined for intra-band contiguous CA

Table 5.6A.1-2: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (two bands)

Table 5.6A.1-2a: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (three bands)

Table 5.6A.1-2b: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (four bands)

Table 5.6A.1-2c: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (five bands)

Table 5.6A.1-2d: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (six bands)

Table 5.6A.1-3: E-UTRA CA configurations and bandwidth combination sets defined for non-contiguous intra-band CA (with two sub-blocks)

Table 5.6A.1-4: E-UTRA CA configurations and bandwidth combination sets defined for non-contiguous intra-band CA (with three sub-blocks)

Table 5.6A.1-5: E-UTRA CA configurations and bandwidth combination sets defined for non-contiguous intra-band CA (with four sub-blocks)

## 5.6BChannel bandwidth for UL-MIMO

The requirements specified in subclause 5.6 are applicable to UE supporting UL-MIMO.

## 5.6B.1Void

## 5.6CChannel bandwidth for Dual Connectivity

For E-UTRA DC bands specified in 5.5C, the corresponding E-UTRA CA configurations in 5.6A.1, i.e., dual uplink inter-band carrier aggregation with uplink assigned to two E-UTRA bands, are applicable to Dual Connectivity.

NOTE 1:Requirements for the dual connectivity configurations are defined in the section corresponding E-UTRA uplink CA configurations, unless otherwise specified.

NOTE 2:For TDD inter-band dual connectivity configurations, requirements are applicable only for synchronous operation.

## 5.6C.1Void

Table 5.6C.1-1: Void

Table 5.6C.1-2: Void

## 5.6DChannel bandwidth for ProSe

## 5.6D.1Channel bandwidths per operating band for ProSe

The ProSe combination of channel bandwidths and operating bands is shown in Table 5.6D.1-1 and Table 5.6D.1-2. The transmission bandwidth configuration in Table 5.6D.1-1 and Table 5.6D.1-2 shall be supported for each of the specified channel bandwidths. The same (symmetrical) channel bandwidth is specified for both the TX and RX path.

Table 5.6D.1-1 ProSe Direct Discovery channel bandwidth

Table 5.6D.1-2 ProSe Direct Communication channel bandwidth

## 5.6FChannel bandwidth for category NB1 and NB2

Channel bandwidth for Category NB1 and NB2 is 200 kHz.

For category NB1 and NB2, requirements in present document are specified for the channel bandwidth listed in Table 5.6F-1.

Table 5.6F-1: Transmission bandwidth configuration NRB, Ntone 15kHz and Ntone 3.75kHz in NB1 and NB2 channel bandwidth

Figure 5.6F-1 shows the relation between the Category NB1/NB2 channel bandwidth (BWChannel) and the Category NB1 /NB2 transmission bandwidth configuration (Ntone). The channel edges are defined as the lowest and highest frequencies of the carrier separated by the channel bandwidth, i.e. at FC +/- BWChannel /2.

Figure 5.6F-1 Definition of Channel Bandwidth and Transmission Bandwidth configuration

## 5.6GChannel bandwidth for V2X Communication

## 5.6G.1Channel bandwidths per operating band for V2X Communication

E-UTRA V2X Communication channel bandwidths and operating band is shown in Table 5.6G.1-1. The same (symmetrical) channel bandwidth is specified for both the TX and RX path.

Table 5.6G.1-1: V2X Communciation channel bandwidth

For V2X inter-band concurrent operation, the V2X Communication channel bandwidths for each operating band is specified in Table 5.6G.1-2.

Table 5.6G.1-2: Inter-band concurrent V2X configurations and bandwidth combination sets

V2X Bandwidth Class is specified in Table 5.6G.1-3 for V2X intra-band contiguous multi-carrier operation.

Table 5.6G.1-3: V2X bandwidth classes and corresponding nominal guard bands

For V2X intra-band multi-carrier operation, the V2X communication channel bandwidths for each operating band is specified in Table 5.6G.1-4.

Table 5.6G.1-4: V2X intra-band multi-carrier configurations

## 5.6HPMCH bandwidth for LTE based 5G terrestrial broadcast

Requirements in the present document are specified for the bandwidths listed in Table 5.6H-1.

Table 5.6H-1: Transmission bandwidth configuration NRB for LTE based 5G terrestrial broadcast

The LTE based 5G terrestrial broadcast network operates on 6, 7, and 8 MHz channels and the requirements in this specification apply according to configuration by the higher layer parameter pmch-Bandwidth (see TS 36.213 [6]) in the MBSFN area (see TS 36.331 [7]).

Note:  Upon configuration of the PMCH bandwidth, the UE is assumed to configure its baseband filtering to 10 MHz.  This assumption is not intended to restrict the UE implementation.

## 5.6H.1PMCH bandwidths per operating band for LTE based 5G terrestrial broadcast

LTE based 5G terrestrial broadcast bandwidths and operating bands are shown in Table 5.6H.1-1

Table 5.6H.1-1: LTE based 5G terrestrial broadcast bandwidths per operating band

## 5.7Channel arrangement

## 5.7.1Channel spacing

The spacing between carriers will depend on the deployment scenario, the size of the frequency block available and the channel bandwidths. The nominal channel spacing between two adjacent E-UTRA carriers is defined as following:

Nominal Channel spacing = (BWChannel(1) + BWChannel(2))/2

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective E-UTRA carriers. The channel spacing can be adjusted to optimize performance in a particular deployment scenario.

## 5.7.1AChannel spacing for CA

For intra-band contiguous carrier aggregation with two or more component carriers, the nominal channel spacing between two adjacent E-UTRA component carriers is defined as the following unless stated otherwise:

where BWChannel(1) and BWChannel(2) are the channel bandwidths of the two respective E-UTRA component carriers according to Table 5.6-1 with values in MHz. The channel spacing for intra-band contiguous carrier aggregation can be adjusted to any multiple of 300 kHz less than the nominal channel spacing to optimize performance in a particular deployment scenario.

For intra-band contiguous carrier aggregation with two or more component carriers in Band 46, the requirements apply for both 19.8 MHz and 20.1 MHz nominal carrier spacing between two 20 MHz component carriers, and for 15.0 MHz nominal carrier spacing between 10 MHz and 20 MHz component carriers.

For intra-band non-contiguous carrier aggregation the channel spacing between two or more E-UTRA component carriers in different sub-blocks shall be larger than the nominal channel spacing defined in this subclause.

## 5.7.1FChannel spacing for category NB1 and NB2

Nominal channel spacing for UE category NB1 and NB2 in stand-alone mode is 200 kHz. For in-band and guard-band cases the nominal channel spacing between two adjacent category NB1 or NB2 carriers is 180 kHz.

## 5.7.1HChannel spacing for LTE based 5G terrestrial broadcast

Nominal channel spacing between adjacent broadcast channels is defined as follows

Nominal Channel spacing = PMCH bandwidth

where PMCH bandwidth is the broadcast bandwidth for all broadcast carriers in the same geographical area is indicated by upper layer signaling pmch-Bandwidth in the MBSFN area (see TS 36.331 [7]).  The requirements in this specification do not apply for heterogeneous broadcast bandwidths in the same geographical area.

## 5.7.2Channel raster

The channel raster is 100 kHz for all bands, which means that the carrier centre frequency must be an integer multiple of 100 kHz.

## 5.7.2AChannel raster for CA

For carrier aggregation the channel raster is 100 kHz for all bands, which means that the carrier centre frequency must be an integer multiple of 100 kHz.

## 5.7.2FChannel raster for category NB1 and NB2

Channel raster for category NB1 and NB2 in-band, guard-band and standalone operation is 100 kHz.

## 5.7.3Carrier frequency and EARFCN

The carrier frequency in the uplink and downlink is designated by the E-UTRA Absolute Radio Frequency Channel Number (EARFCN) in the range 0 – 262143. The relation between EARFCN and the carrier frequency in MHz for the downlink is given by the following equation, where FDL_low and NOffs-DL are given in Table 5.7.3-1 and NDL is the downlink EARFCN.

FDL = FDL_low + 0.1(NDL – NOffs-DL)

The relation between EARFCN and the carrier frequency in MHz for the uplink is given by the following equation where FUL_low and NOffs-UL are given in Table 5.7.3-1 and NUL is the uplink EARFCN.

FUL = FUL_low + 0.1(NUL – NOffs-UL)

Table 5.7.3-1: E-UTRA channel numbers

## 5.7.3FCarrier frequency and EARFCN for category NB1 and NB2

The carrier frequency of category NB1/NB2 in the downlink is designated by the E-UTRA Absolute Radio Frequency Channel Number (EARFCN) in the range 0 – 262143 and the Offset of category NB1/NB2 Channel Number to EARFCN in the range {-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,-0.5,0,1,2,3,4,5,6,7,8,9} for FDD and in the range {-10,-9,-8.5,-8,-7,-6,-5,-4.5,-4,-3,-2,-1,-0.5,0,1,2,3,3.5,4,5,6,7,7.5,8,9} for TDD. The relation between EARFCN, Offset of category NB1/NB2 Channel Number to EARFCN and the carrier frequency in MHz for the downlink is given by the following equation, where FDL is the downlink carrier frequency of category NB1/NB2, FDL_low and NOffs-DL are given in table 5.7.3-1, NDL is the downlink EARFCN, MDL is the Offset of category NB1/NB2 Channel Number to downlink EARFCN.

FDL = FDL_low + 0.1(NDL – NOffs-DL) + 0.0025*(2MDL+1)

The carrier frequency of category NB1/NB2 in the uplink is designated by the E-UTRA Absolute Radio Frequency Channel Number (EARFCN) in the range 0 –262143, and the Offset of category NB1/NB2 Channel Number to EARFCN in the range {-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9} for FDD and in the range {-11,-10,-9.5,-9,-8.5, -8,-7.5,-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10, 11} for TDD. The relation between EARFCN, Offset of category NB1/NB2 Channel Number to EARFCN and the carrier frequency in MHz for the uplink is given by the following equation, where FUL is the uplink carrier frequency of category NB1/NB2, FUL_low and NOffs-UL are given in table 5.7.3-1, NUL is the uplink EARFCN, MUL is the Offset of category NB1/NB2 Channel Number to uplink EARFCN.

FUL = FUL_low + 0.1(NUL – NOffs-UL) + 0.0025*(2MUL)

NOTE 1:For category NB1/NB2, NDL or NUL is different than the value of EARFCN that corresponds to E-UTRA downlink or uplink carrier frequency for in-band and guard band operation.

NOTE 2:For FDD MDL = -0.5 is not applicable for in-band and guard band operation. For TDD MDL {-0.5,+3.5,-4.5,+7.5,-8.5} is not applicable for in-band and guard band operation.

NOTE 3:For the carrier including NPSS/NSSS for in-band and guard band operation, MDL is selected from {-2,-1,0,1}.

NOTE 4:For the carrier including NPSS/NSSS for stand-alone operation, MDL = -0.5.

## 5.7.3HCarrier frequency and EARFCN for LTE based 5G terrestrial broadcast

The EARFCN for applicable bands designated for LTE based 5G terrestrial broadcast according to Table 5.5H-1 are specified in Table 5.7.3H-1.

Table 5.7.3H-1: E-UTRA channel numbers for LTE based 5G terrestrial broadcast

## 5.7.4TX–RX frequency separation

a)The default E-UTRA TX channel (carrier centre frequency) to RX channel (carrier centre frequency) separation is specified in Table 5.7.4-1 for the TX and RX channel bandwidths defined in Table 5.6.1-1

Table 5.7.4-1: Default UE TX-RX frequency separation

b)The use of other TX channel to RX channel carrier centre frequency separation is not precluded and is intended to form part of a later release.

## 5.7.4ATX–RX frequency separation for CA

For intra-band contiguous carrier aggregation, the same TX-RX frequency separation as specified in Table 5.7.4-1 is applied to PCC and SCC, respectively.

## 5.7.4ETX–RX frequency separation for category M1 and M2

For the category M1 and M2 TX-RX frequency separation is flexible within the assigned channel bandwidth of E-UTRA carrier with the TX-RX frequency separation of the E-UTRA carriers as specified in Table 5.7.4-1.

## 5.7.4FTX–RX frequency separation for category NB1 and NB2

For in-band and guard-band operation mode, the category NB1 and NB2 TX-RX frequency separation is flexible within the assigned channel bandwidth of E-UTRA carrier with the TX-RX frequency separation of the E-UTRA carriers as specified in Table 5.7.4-1. For stand-alone operation mode the default TX-RX frequency separation is the same as Table 5.7.4-1.

## 6Transmitter characteristics

## 6.1General

Unless otherwise stated, the transmitter characteristics are specified at the antenna connector of the UE with a single or multiple transmit antenna(s). For UE with integral antenna only, a reference antenna with a gain of 0 dBi is assumed.

Unless otherwise stated, NB1 and NB2 requirements specified for an E-UTRA band shall also apply for the re-farmed NR band (e.g. if NB1/NB2 requirements are specified for E-UTRA band 1, they shall also apply for NR band n1).

The requirements of clause 6 do not apply to devices only supporting LTE based 5G terrestrial broadcast.

## 6.2Transmit power

## 6.2.1Void

## 6.2.2UE maximum output power

The following UE Power Classes define the maximum output power for any transmission bandwidth within the channel bandwidth for non CA configuration unless otherwise stated. The period of measurement shall be at least as defined in Table 6.2.2-0.

Table 6.2.2-0: Measurement period for UE maximum output power

Table 6.2.2-1: UE Power Class

The default power class PPowerClass_Default for an operating band is Power Class 3 unless otherwise stated.

For a power class 2 capable UE operating on Band 41, when an IE P-max as defined in TS 36.331 [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6, the requirements for power class 2 are not applicable, and the corresponding requirements for a power class 3 UE shall apply.

For each supported frequency band other than Band 14 and Band 41, the UE shall:

-if the UE supports a different power class than the default UE power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the band is a TDD band whose frame configuration is 0 or 6; or

-if the IE P-Max as defined in TS 36.331 [7] is not provided; or

-if the IE P-Max as defined in TS 36.331 [7] is provided and set to the maximum output power of the default power class or lower;

-meet all requirements for the default power class of the operating band in which the UE is operating and set its configured transmitted power as specified in sub-clause 6.2.5;

-else (i.e the IE P-Max as defined in TS 36.331 [7] is provided and set to the higher value than the maximum output power of the default power class):

-meet all requirements for the supported power class and set its configured transmitted power class as specified in sub-clause 6.2.5;

## 6.2.2AUE maximum output power for CA

The following UE Power Classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth.

The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least as defined in Table 6.2.2A-0a.

Table 6.2.2A-0a: Measurement period for UE maximum output power for CA

For inter-band carrier aggregation with one uplink component carrier assigned to one E-UTRA band the requirements in subclause 6.2.2 apply. For inter-band carrier aggregation with two uplink contiguous component carrier assigned to one E-UTRA band the requirements specified in Table 6.2.2A-1 apply for that band. For inter-band carrier aggregation with one uplink component carrier assigned to one E-UTRA band in Band 38, 40, 41 or 42, the requirements for power class 2 are not applicable and the corresponding requirements for a power class 3 UE shall apply. For inter-band carrier aggregation with one uplink component carrier assigned to one E-UTRA band in Band 3, 20, 28, or 31, the requirements for power class 1 are not applicable and the corresponding requirements for a power class 3 UE shall apply.

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector. The maximum output power is specified in Table 6.2.2A-0.

For E-UTRA CA bands including an uplink LAA Scell in Band 46, the UE shall meet the following additional requirements for transmission within the frequency ranges 5150-5350 MHz and 5470-5725 MHz:

-a maximum mean power density of 10 dBm in any 1 MHz band when the network signaling value NS_28 or NS_29 is indicated in the LAA Scell;

-a maximum mean power density of 11 dBm in any 1 MHz band when the network signaling value NS_30 is indicated in the LAA Scell;

the following additional requirements for transmission within the frequency range 5230-5250 MHz:

-a maximum mean power density of 4 dBm in any 1 MHz band when the network signaling value NS_31 is indicated in the LAA Scell;

the following additional requirements for transmission within the frequency ranges 5150-5230 MHz, 5250-5350 MHz, 5470-5725 MHz and 5725-5850 MHz:

-a maximum mean power density of 10 dBm in any 1 MHz band when the network signaling value NS_31 is indicated in the LAA Scell;

where the said network signaling values are specified in clause 6.2.4.

Table 6.2.2A-0: UE Power Class for uplink interband CA (two bands)

For uplink intra-band contiguous carrier aggregation the maximum output power is specified in Table 6.2.2A-1. For downlink intra-band contiguous carrier aggregation with a single uplink component carrier configured in the E-UTRA band, the maximum output power is specified in Table 6.2.2-1.

For a power class 2 capable UE operating with intra-band uplink contiguous CA bandwidth class C on Band 41, when an IE P-max as defined in TS 36.331 [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6, the requirements for power class 2 are not applicable, and the corresponding requirements for a power class 3 UE shall apply.

Table 6.2.2A-1: CA UE Power Class for intraband contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier on the PCC, the requirements in subclause 6.2.2 apply. For intra-band non-contiguous carrier aggregation with two uplink carriers the maximum output power is specified in Table 6.2.2A-2.

Table 6.2.2A-2: UE Power Class for intraband non-contiguous CA

## 6.2.2BUE maximum output power for UL-MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the maximum output power for any transmission bandwidth within the channel bandwidth is specified in Table 6.2.2B-1. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UE supporting UL-MIMO, the maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least as defined in Table 6.2.2B-0.

Table 6.2.2B-0: Measurement period for UE maximum output power for UL-MIMO

Table 6.2.2B-1: UE Power Class for UL-MIMO in closed loop spatial multiplexing scheme

The default power class for an operating band is Power Class 3 unless otherwise stated.

For a power class 2 capable UE operating on Band 41, when an IE P-max as defined in TS 36.331 [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6, the requirements for power class 2 are not applicable and the corresponding requirements for a power class 3 UE shall apply.

For each supported frequency band other than Band 41, the UE shall:

-if the UE supports a different power class than the UE default power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the band is a TDD band whose frame configuration is 0 or 6; or

-if the IE P-Max as defined in TS 36.331 [7] is not provided; or

-if the IE P-Max as defined in TS 36.331 [7] is provided and set to the maximum output power of the default power class or lower;

-meet all requirements for the default power class of the operating band in which the UE is operating and set its configured transmitted power as specified in sub-clause 6.2.5;

-else (i.e the IE P-Max as defined in TS 36.331 [7] is provided and set to the higher value than the maximum output power of the default power class):

-meet all requirements for the supported power class and set its configured transmitted power as specified in sub-clause 6.2.5;

Table 6.2.2B-2: UL-MIMO configuration in closed-loop spatial multiplexing scheme

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.2.2 apply.

## 6.2.2CVoid

<reserved for future use>

## 6.2.2DUE maximum output power for ProSe

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the UE maximum output power shall be as specified in Table 6.2.2A-0 in subclause 6.2.2A for the corresponding inter-band aggregation with uplink assigned to two bands.

If UE is configured to oprerate on single E-UTRA ProSe sidelink band or E-UTRA uplink band specidied in Table 5.5D-1, the requirements in subclause 6.2.2 apply.

## 6.2.2EUE maximum output power for Category M1 and M2 UE

The following UE Power Classes define the maximum output power for any transmission bandwidth within the channel bandwidth for non CA configuration and UL-MIMO unless otherwise stated. The period of measurement shall be at least one sub frame (1ms).

Table 6.2.2E-1: UE Power Class

## 6.2.2FUE maximum output power for category NB1 and NB2

Category NB1 and NB2 UE Power Classes are specified in Table 6.2.2F-1 and define the maximum output power for any transmission bandwidth within the category NB1 and NB2 channel bandwidth. For 3.75 kHz sub-carrier spacing the maximum output power is defined as mean power of measurement which period is atleast one slot (2ms) excluding the 2304Ts gap when UE is not transmitting. For 15kHz sub-carrier spacing the maximum output power is defined as mean power of measurement which period is atleast one sub-frame (1ms).

Table 6.2.2F-1: UE Power Class

## 6.2.2GUE maximum output power for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the allowed V2X UE maximum output power for shall be as applied in Table 6.2.2-1 in subclause 6.2.2.

For V2X UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the UE maximum output power shall be as specified in Table 6.2.2G-1 in subclause 6.2.2G for the corresponding inter-band concurrent operation with uplink assigned to two bands.

Table 6.2.2G-1: Inter-band concurrent V2X UE Power Class (two bands)

For intra-band contiguous multi-carrier operation, the maximum output power is defined in Table 6.2.2G-2.

Table 6.2.2G-2: V2X UE Power Class for intra-band contiguous multi-carrier operation

When a UE is configured for E-UTRA V2X sidelink transmissions in Band 47, the UE shall meet the following additional requirements for transmission within the frequency ranges 5855-5925 MHz:

-The maximum mean power spectral density shall be restricted to 23 dBm/MHz EIRP when the network signaling value NS_33 or NS_34 is indicated.

where the network signaling values are specified in clause 6.2.4G.

NOTE:The PSD limit in EIRP shall be converted to conducted requirement depend on the supported post antenna connector gain Gpost connector declared by the UE following the principle described in annex I.

For V2X UE supporting Transmit Diversity, if the UE transmits on two connectors at the same time, the maximum output power for any transmission bandwidth within the channel bandwidth is specified in Table 6.2.2G-3. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms).

Table 6.2.2G-3: V2X UE Power Class for Transmit Diversity scheme

If the UE transmits on one antenna connector at a time, the requirements in Table 6.2.2-1 shall apply to the active antenna connector.

## 6.2.2KUE maximum output power for Aerial UE

For Aerial UE, the requirements for power class 3 specified in clause 6.2.2 apply.

## 6.2.3UE maximum output power for modulation / channel bandwidth

For UE Power Class 1, 2 and 3, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2-1due to higher order modulation and transmit bandwidth configuration (resource blocks) is specified in Table 6.2.3-1.

Table 6.2.3-1: Maximum Power Reduction (MPR) for Power Class 1, 2 and 3

For PRACH, PUCCH and SRS transmissions, the allowed MPR is according to that specified for PUSCH QPSK modulation for the corresponding transmission bandwidth.

For each TTI pattern, the MPR shall be evaluated per Teval period as specified in table 6.2.3-2 and given by the maximum value taken over the transmission(s) within that period; the maximum MPR over TREF is then applied for TREF.

Table 6.2.3-2: MPR evaluation period

For UE Power Class 1 and 3 transmissions with non-contiguous resource allocation in single component carrier, the allowed Maximum Power Reduction (MPR) for the maximum output power in table 6.2.2-1, is specified as follows

MPR = CEIL {MA, 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA =8.00-10.12A; 0.00< A ≤ 0.33

## 5.67 - 3.07A; 0.33< A ≤0.77

3.31; 0.77< A ≤1.00

Where MA is defined as follows for 256 QAM

MA = 8.00-10.12A; 0.00< A ≤ 0.25

5.50; 0.25< A < 1.00

Where

A = NRB_alloc / NRB.

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB, i.e. MPR  [3.0, 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0]

The allowed MPR for transmission on an Scell in Band 46 or Band 49 within a component carrier of a nominal channel bandwidth of 10 MHz or 20 MHz is in accordance with 6.2.3-1 for RIV = ‘11111’ (10 MHz) and L = 10 (20 MHz) with L defined in Clause 8.1.4 of [6]. For all other possible values of the RIV defined in Clause 8.1.4 of [6] the allowed MPR is 2.5 dB for QPSK modulation, 3 dB for 16QAM modulation and 4 dB for 64QAM modulation (256QAM is FFS).

For a power class 2 capable UE operating on Band 41, when an IE P-max as defined in [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6, the requirements for power class 2 are not applicable, and the corresponding requirements for a power class 3 UE shall apply.

For each supported frequency band other than Band 14 and Band 41, the UE shall:

-if the UE supports a different power class than the default UE power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the band is a TDD band whose frame configuration is 0 or 6; or

-if the IE P-Max as defined in TS 36.331 [7] is not provided; or

-if the IE P-Max as defined in TS 36.331 [7] is provided and set to the maximum output power of the default power class or lower;

-meet all requirements for the default power class of the operating band in which the UE is operating and set its configured transmitted power as specified in sub-clause 6.2.5;

-else (i.e the IE P-Max as defined in TS 36.331 [7] is provided and set to the higher value than the maximum output power of the default power class):

-meet all requirements for the supported power class and set its configured transmitted power class as specified in sub-clause 6.2.5.

For UE Power Class 2 transmissions with non-contiguous resource allocation in single component carrier, the allowed Maximum Power Reduction (MPR) for the maximum output power is not specified in this version of the specification.

For the UE maximum output power modified by MPR, the power limits specified in subclause 6.2.5 apply.

## 6.2.3AUE Maximum Output power for modulation / channel bandwidth for CA

For inter-band carrier aggregation with one uplink component carrier assigned to one E-UTRA band, the requirements in subclause 6.2.3 apply. For inter-band carrier aggregation with two uplink contiguous component carrier assigned to one E-UTRA band specified in this clause for intra-band contiguous carrier aggregation apply for that band.

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the requirements in subclause 6.2.3 apply for each uplink component carrier.

For intra-band contiguous carrier aggregation the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2A-1due to higher order modulation and contiguously aggregated transmit bandwidth configuration (resource blocks) is specified in Table 6.2.3A-1 for UE power class 3 CA bandwidth classes B and C, in Table 6.2.3A-1a for UE power class 2 CA bandwidth class C, and Table 6.2.3A-2 for UE power class 3 CA bandwidth class D. In case the modulation format is different on different component carriers then the MPR is determined by the rules applied to higher order of those modulations.

Table 6.2.3A-1: Maximum Power Reduction (MPR) for Power Class 3

Table 6.2.3A-1a: Maximum Power Reduction (MPR) for Power Class 2

Table 6.2.3A-2: Maximum Power Reduction (MPR) for Class 3

For PUCCH and SRS transmissions, the allowed MPR is according to that specified for PUSCH QPSK modulation for the corresponding transmission bandwidth.

For UE power class 3 intra-band contiguous carrier aggregation bandwidth class C with non-contiguous resource allocation, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2A-1 is specified as follows

MPR = CEIL { min(MA, MIM5), 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA = 8.2; 0 ≤ A < 0.025

## 9.2 - 40A ; 0.025≤ A < 0.05

## 8 – 16A; 0.05≤ A < 0.25

## 4.83 – 3.33A; 0.25 ≤ A ≤ 0.4,

## 3.83 – 0.83A; 0.4 ≤ A ≤ 1,

Where MA is defined as follows for 256 QAM

MA = 8.2; 0 ≤ A < 0.025

## 9.2 - 40A; 0.025 ≤ A < 0.05

## 8 – 16A; 0.05 ≤ A < 0.16

5.5; 0.16 ≤ A < 1

and MIM5 is defined as follows

MIM5 =4.5; IM5 < 1.5 * BWChannel_CA

6.0; 1.5 * BWChannel_CA ≤ IM5 <  BWChannel_CA/2 + FOOB

MA; IM5 ≥ BWChannel_CA/2 + FOOB

For UE power class 2 intra-band contiguous carrier aggregation bandwidth class C with non-contiguous resource allocation, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2A-1 is specified as follows

MPR = CEIL { min(MA, MIM5), 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA = 8.2; 0 ≤ A < 0.04

## 9.2 - 40A ; 0.04 ≤ A < 0.075

## 8 – 16A; 0.075 ≤ A < 0.25

## 4.83 – 3.33A; 0.25 ≤ A ≤ 0.4,

## 3.83 – 0.83A; 0.4 ≤ A ≤ 1,

Where MA is defined FFS for 256 QAM

and MIM5 is defined as follows

MIM5 =5.0; IM5 < 1.5 * BWChannel_CA

6.0; 1.5 * BWChannel_CA ≤ IM5 <  BWChannel_CA/2 + FOOB

MA; IM5 ≥ BWChannel_CA/2 + FOOB

For UE power class 3 intra-band contiguous carrier aggregation bandwidth class B with non-contiguous resource allocation, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2A-1 is specified as follows

MPR = CEIL { MA, 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA =10.5 – 17.5A; 0 ≤ A < 0.2

## 8.5 – 7.5A ; 0.2 ≤ A < 0.6

## 5.5 – 2.5A ; 0.6 ≤ A ≤ 1

Where MA is defined as follows for 256 QAM

MA =10.5 – 17.5A; 0 ≤ A < 0.2

## 8.5 – 7.5A ; 0.2 ≤ A < 0.4

## 5.5  ; 0.4 ≤ A ≤ 1

Where

A = NRB_alloc / NRB_agg.

IM5 = max( | FC_agg  – (3*Fagg_alloc_low – 2*Fagg_alloc_high) |,  | FC_agg  – (3*Fagg_alloc_high – 2*Fagg_alloc_low) | )

FC_agg = (Fedge_high + Fedge_low)/2

For UE power class 3 intra-band contiguous carrier aggregation bandwidth class D with non-contiguous resource allocation, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.3A-2 is specified as follows

MPR = CEIL { min(MA, MIM5), 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA = 8.2; 0 ≤ A < 0.025

## 9.2 - 40A ; 0.025 ≤ A < 0.05

## 8 – 16A; 0.05≤ A < 0.25

4.0; 0.25 ≤ A < 1

Where MA is defined as follows for 256 QAM

MA =8.2 ; 0 ≤ A < 0.025

## 9.2 - 40A; 0.025 ≤ A < 0.05

## 8 – 16A; 0.05 ≤ A < 0.16

5.5; 0.16 ≤ A < 1

and MIM5 is defined as follows

MIM5 =4.5; IM5 < 1.5 * BWChannel_CA

6.0; 1.5 * BWChannel_CA ≤ IM5 <  BWChannel_CA/2 + FOOB

MA; IM5 ≥ BWChannel_CA/2 + FOOB

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB, i.e. MPR[3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5].

For intra-band non-contiguous carrier aggregation with one uplink carrier, the requirements in subclause 6.2.3 apply.

For intra-band non-contiguous carrier aggregation with two uplink carriers MPR is specified for E-UTRA CA configurations with a maximum possible WGAP ≤ 35 MHz; the allowed MPR is

MPR = CEIL {MN, 0.5}

where MN is defined as follows

MN=-0.125 N + 18.25; 2 ≤ N ≤ 50

-0.0333 N + 13.67; 50 < N ≤ 200

where N= NRB_alloc is the number of allocated resource blocks. Clause 6.2.3 does not apply in addition.

For intra-band non-contiguous carrier aggregation with two uplink carriers MPR is specified for E-UTRA CA configurations with a maximum possible 35 MHz <WGAP ≤ 100 MHz; the allowed MPR is given in Table 6.2.3A-3:

Table 6.2.3A-3 Maximum power reduction (MPR) for power class 3 with dual Tx for intra-band non contiguous CA with 35 MHz <WGAP ≤ 100 MHz

For intra-band carrier aggregation, the MPR is evaluated per Teval period specified in table 6.2.3A-3 and given by the maximum value taken over the transmission(s) on all component carriers within that period; the maximum MPR over TREF is then applied for TREF.

Table 6.2.3A-4: MPR evaluation period for CA

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the requirements specified in subclause 6.2.3 apply for the E-UTRA band supporting one component carrier, and for the E-UTRA band supporting two contiguous component carriers the requirements specified in subclause 6.2.3A apply.

For the UE maximum output power modified by MPR, the power limits specified in subclause 6.2.5A apply.

## 6.2.3BUE maximum output power for modulation / channel bandwidth for UL-MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2B-1 is specified in Table 6.2.3-1. The requirements shall be met with UL-MIMO configurations defined in Table 6.2.2B-2. For UE supporting UL-MIMO, the maximum output power is measured as the sum of the maximum output power at each UE antenna connector.

For the UE maximum output power modified by MPR, the power limits specified in subclause 6.2.5B apply.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.2.3 apply.

## 6.2.3DUE maximum output power for modulation / channel bandwidth for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, this subclause specifies the allowed Maximum Power Reduction (MPR) power for ProSe physical channels and signals due to higher order modulation and transmit bandwidth configuration (resource blocks).

The allowed MPR for the maximum output power for ProSe physical channels PSDCH, PSCCH, PSSCH, and PSBCH shall be as specified in subclause 6.2.3 for  PUSCH for the corresponding modulation and transmission bandwidth.

The allowed MPR for the maximum output power for ProSe physical signal PSSS shall be as be as specified in subclause 6.2.3 for PUSCH QPSK modulation for the corresponding transmission bandwidth.

The allowed MPR for the maximum output power for ProSe physical signal SSSS is specified in Table 6.2.3D-1.

For a power class 2 capable UE operating on Band 41, the corresponding requirements for a power class 3 UE apply when an IE P-max as defined in [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6.

For each supported frequency band other than Band 14 and Band 41, the UE shall:

-if the UE supports a different power class than the default UE power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the band is a TDD band whose frame configuration is 0 or 6; or

-if the IE P-Max as defined in TS 36.331 [7] is not provided; or

-if the IE P-Max as defined in TS 36.331 [7] is provided and set to the maximum output power of the default power class or lower;

-meet all requirements for the default power class of the operating band in which the UE is operating and set its configured transmitted power as specified in sub-clause 6.2.5;

-else (i.e the IE P-Max as defined in TS 36.331 [7] is provided and set to the higher value than the maximum output power of the default power class):

-meet all requirements for the supported power class and set its configured transmitted power class as specified in sub-clause 6.2.5.

Table 6.2.3D-1: Maximum Power Reduction (MPR) for SSSS for Power Class 1, 2 and 3

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.2.3D apply for ProSe transmission and the requirements in subclause 6.2.3 apply for uplink transmission.

## 6.2.3EUE maximum output power for modulation / channel bandwidth for category M1 and M2

For category M1 UE Power Class 3, 5 and 6, the allowed Maximum Power Reduction (MPR) for the maximum output power specified in Table 6.2.2E-1 due to higher order modulation and transmit bandwidth configuration (resource blocks) is specified in Tables 6.2.3E-1, 6.2.3E-2 and 6.2.3E-5 respectively.

For category M2 UE Power Class 3, 5 and 6, the allowed Maximum Power Reduction (MPR) for the maximum output power specified in Table 6.2.2E-1 due to higher order modulation and transmit bandwidth configuration (resource blocks) is specified in Table 6.2.3E-3, Table 6.2.3E-4 and Table 6.2.3E-6 respectively.

For subPRB allocation of category M1 UE of Power Class 3, there is no MPR applies. For subPRB allocation of category M2 UE of Power Class 3, the allowed MPR due to higher order modulation and transmit bandwidth configuration (subcarrier) is specified in in Table 6.2.3E-7.

Table 6.2.3E-1: Maximum Power Reduction (MPR) for category M1 UE for Power Class 2 and 3

Table 6.2.3E-2: Maximum Power Reduction (MPR) for category M1 for Power Class 5

Table 6.2.3E-3: Maximum Power Reduction (MPR) for category M2 UE for Power Class 2 and 3

Table 6.2.3E-4: Maximum Power Reduction (MPR) for category M2 UE for Power Class 5

Table 6.2.3E-5: Maximum Power Reduction (MPR) for category M1 for Power Class 6

Table 6.2.3E-6: Maximum Power Reduction (MPR) for category M2 UE for Power Class 6

Table 6.2.3E-7: Maximum Power Reduction (MPR) for category M2 UE for Power Class 3 for subPRB allocation

For PRACH, PUCCH and SRS transmissions, the allowed MPR is according to that specified for PUSCH QPSK modulation for the corresponding transmission bandwidth.

For each subframe, the MPR is evaluated per slot and given by the maximum value taken over the transmission(s) within the slot; the maximum MPR over the two slots is then applied for the entire subframe.

For the UE maximum output power modified by MPR, the power limits specified in subclause 6.2.5 apply.

No other MPR requirement than those specified in tables 6.2.3E-1 and Table 6.2.3E-2 and Table 6.2.3E-5 applies to category M1 and those specified in tables 6.2.3E-3 and Table 6.2.3E-4 and Table 6.2.3E-6 applies to category M2 UE.

## 6.2.3FUE maximum output power for modulation / channel bandwidth for category NB1 and NB2

For UE category NB1 and NB2 power class 3 and 5 the allowed Maximum Power Reduction (MPR) for the maximum output power given in Table 6.2.2F-1 is specified in Table 6.2.3F-1.

Table 6.2.3F-1: Maximum Power Reduction (MPR) for UE category NB1 and NB2 Power Class 3 and 5

For UE category NB1 and NB2 power class 6 the allowed Maximum Power Reduction (MPR) for the maximum output power given in Table 6.2.2F-1 is specified in Table 6.2.3F-2.

Table 6.2.3F-2: Maximum Power Reduction (MPR) for UE category NB1 and NB2 Power Class 6

For the UE maximum output power modified by MPR, the power limits specified in sub-clause 6.2.5F apply.

## 6.2.3GUE maximum output power for modulation / channel bandwidth for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, this subclause specifies the allowed Maximum Power Reduction (MPR) power for V2X physical channels and signals due to PSCCH and PSSCH simultaneous transmission.

## 6.2.3G.1MPR for Power class 3 V2X UE

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power for V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2.3G.1-1 for power class 3.

Table 6.2.3G.1-1: Maximum Power Reduction (MPR) for power class 3 V2X Communication (Contiguous PSCCH and PSSCH transmission)

For non-contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power for V2X physical channels PSCCH and PSSCH shall be as specified as follows

MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =4.5; 0.00< A ≤ 0.2

## 5.5 –5.833A; 0.2< A ≤0.6

2.0; 0.6< A ≤1.00

Where

A = NRB_alloc / NRB.

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

The allowed MPR for the maximum output power for V2X physical channels PSBCH and PSSS shall be as specified in subclause 6.2.3 for the corresponding modulation and transmission bandwidth.

The allowed MPR for the maximum output power for V2X physical signal SSSS is specified in Table 6.2.3D-1.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the allowed MPR requirements in subclause 6.2.3G apply for V2X  PSSCH and PSCCH transmission. The allowed MPR requirements in subclause 6.2.3D apply for other V2X sidelink transmission (PSBCH/PSSS/SSSS). The MPR requirements in subclause 6.2.3 apply for uplink transmission.

For intra-band contiguous multi-carrier operation bandwidth class B the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2.2G.1-2 due to higher order modulation is specified as follows.

Table 6.2.3G.1-2: Void

MPR = CEIL { MA, 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA = 6.5; 0 ≤ A < 0.1

## 8 - 15A ; 0.1 ≤ A < 0.2

## 5.75 – 3.75A; 0.2 ≤ A < 0.6

## 3.5      ; 0.6≤ A ≤ 1For intra-band contiguous multi-carrier operation bandwidth class C the allowed Maximum Power Reduction (MPR) for the maximum output power can be specified as follows. In case the modulation format is different on different component carriers then the MPR is determined by the rules applied to higher order of those modulations.

MPR = CEIL { MA, 0.5}

Where MA is defined as follows for QPSK, 16 QAM and 64 QAM

MA = 6.5; 0 ≤ A < 0.1

## 8.5 - 20A ; 0.1 ≤ A < 0.2

## 5.25 – 2.5A; 0.2 ≤ A < 0.6

## 3.5      ; 0.6≤ A ≤ 1

## 6.2.3G.2MPR for Power class 2 V2X UE

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power for V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2.3G.2-1 for power class 2.

Table 6.2.3G.2-1: Maximum Power Reduction (MPR) for power class 2 V2X Communication (Contiguous PSCCH and PSSCH transmission)

For non-contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power for V2X physical channels PSCCH and PSSCH shall be as specified as follows:

MPR = CEIL {MA, 0.5}

Where MA is defined as follows

For 10MHz channel bandwidth         MA =4.5         ; 0.0< A ≤ 0.2

## 8.5 – 20.0A; 0.2< A ≤0.3

## 2.5   ; 0.3< A ≤1.00

For 20MHz channel bandwidth         MA =9.0         ; 0.0< A ≤ 0.1

## 12.0 – 30.0A; 0.1< A ≤0.3

## 3.0   ; 0.3< A ≤1.00

Where

A = NRB_alloc / NRB.

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

## 6.2.3KUE maximum output power for modulation / channel bandwidth for Aerial UE

For Aerial UE of Power Class 3, the allowed MPR for the maximum output power in Table 6.2.2-1 due to higher order modulation and transmit bandwidth configuration is specified in clause 6.2.3.

## 6.2.4UE maximum output power with additional requirements

Additional ACLR and spectrum emission requirements can be signalled by the network to indicate that the UE shall also meet additional requirements in a specific deployment scenario. To meet these additional requirements, Additional Maximum Power Reduction (A-MPR) is allowed for the output power as specified in Table 6.2.2-1. Unless stated otherwise, an A-MPR of 0 dB shall be used.

For UE Power Class 1, 2 and 3 the specific requirements and identified subclauses are specified in Table 6.2.4-1 along with the allowed A-MPR values that may be used to meet these requirements. The allowed A-MPR values specified in tables of this clause are in addition to the allowed MPR requirements specified in subclause 6.2.3.

Table 6.2.4-1: Additional Maximum Power Reduction (A-MPR)

Table 6.2.4-2: A-MPR for "NS_07"

Table 6.2.4-3: A-MPR for "NS_10"

Table 6.2.4-4: A-MPR requirements for "NS_04" for Power Class 3 UE

Table 6.2.4-4a: A-MPR requirements for "NS_04" for Power Class 2 UE

For a power class 2 capable UE operating in Band 41, A-MPR according to Table 6.2.4-4 for power class 3 is allowed when an IE P-max as defined in [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6.

Table 6.2.4-5: A-MPR for "NS_11"

Table 6.2.4-6: A-MPR for "NS_12"

Table 6.2.4-7: A-MPR for "NS_13"

Table 6.2.4-8: A-MPR for "NS_14"

Table 6.2.4-9: A-MPR for "NS_15" for E-UTRA highest channel edge > 845 MHz and ≤ 849 MHz

Table 6.2.4-10: A-MPR for "NS_15" for E-UTRA highest channel edge ≤ 845 MHz

Table 6.2.4-11: A-MPR for "NS_16" with channel lower edge at ≥807 MHz and <808.5 MHz

Table 6.2.4-12: A-MPR for "NS_16" with channel lower edge at ≥808.5 MHz and <812 MHz

Table 6.2.4-13: A-MPR for "NS_16" with channel lower edge at ≥812 MHz

Table 6.2.4-14: A-MPR for "NS_19"

Table 6.2.4-15: A-MPR for "NS_20"

Table 6.2.4-16: A-MPR for "NS_21"

Table 6.2.4-17: A-MPR for "NS_22"

Table 6.2.4-18: A-MPR for "NS_05"

Table 6.2.4-18E: A-MPR requirements for "NS_05" for Cat-M2 power class 3 UE

Table 6.2.4-19: A-MPR for "NS_24"

Table 6.2.4-20: A-MPR for "NS_25"

Table 6.2.4-21: A-MPR for "NS_26"

Table 6.2.4-22: A-MPR for "NS_27"

Table 6.2.4-23: A-MPR for "NS_28"

Table 6.2.4-24: A-MPR for "NS_29"

Table 6.2.4-25: A-MPR for "NS_30"

Table 6.2.4-26: A-MPR for "NS_31"

Table 6.2.4-27: A-MPR for “NS_36”

Table 6.2.4-28: A-MPR for "NS_38"

Table 6.2.4-29: A-MPR for "NS_39"

Table 6.2.4-30a: A-MPR for "NS_40"

Table 6.2.4-30b: A-MPR for "NS_40"

Table 6.2.4-31: A-MPR for "NS_41"

Table 6.2.4-32: A-MPR for “NS_42”

Table 6.2.4-32a: Void

Table 6.2.4-32b: Void

Table 6.2.4-33: A-MPR for “NS_43”

Table 6.2.4-34: A-MPR requirements for “NS_44” for Power Class 2 UE

Table 6.2.4-34a: A-MPR for "NS_56"

Table 6.2.4-34b: A-MPR for "NS_06" for Power Class 1 UE in Band 12

Table 6.2.4-34c: A-MPR for "NS_06" for Power Class 2 UE

For PRACH, PUCCH and SRS transmissions, the allowed A-MPR is according to that specified for PUSCH QPSK modulation for the corresponding transmission bandwidth.

For each TTI pattern, the A-MPR shall be evaluated per Teval period as specified in table 6.2.4-35 and given by the maximum value taken over the transmission(s) within that period; the maximum A-MPR over the TREF is then applied for TREF.

Table 6.2.4-35: A-MPR evaluation period

For the UE maximum output power modified by A-MPR, the power limits specified in subclause 6.2.5 apply.

Table 6.2.4-36: A-MPR requirements for NS_UAV_70 (Power Class 3)

## 6.2.4AUE maximum output power with additional requirements for CA

Additional ACLR, spectrum emission and spurious emission requirements for carrier aggregation can be signalled by the network to indicate that the UE shall also meet additional requirements in a specific deployment scenario. To meet these additional requirements, Additional Maximum Power Reduction (A-MPR) is allowed for the CA Power Class as specified in Table 6.2.2A-1.

If for intra-band carrier aggregation the UE is configured for transmissions on a single serving cell, then subclauses 6.2.3 and 6.2 4 apply with the Network Signaling value indicated by the field additionalSpectrumEmission.

For intra-band contiguous aggregation with the UE configured for transmissions on two serving cells, the maximum output power reduction specified in Table 6.2.4A-1 is allowed for all serving cells of the applicable uplink CA configurations according to the CA network signalling value indicated by the field additionalSpectrumEmissionSCell-r10. Then clause 6.2.3A does not apply, i.e. the carrier aggregation MPR = 0dB, unless the value indicated is CA_NS_09 or CA_NS_31. For uplink 64 QAM and 256 QAM, the applied maximum output power reduction is obtained by taking the maximum value of MPR requirements specified in Table 6.2.3A-1 and A-MPR requirements specified in Table 6.2.4A-1.

Table 6.2.4A-1: Additional Maximum Power Reduction (A-MPR) for intra-band contiguous CA

If for intra-band non-contigous carrier aggregation the UE is configured for transmissions on a single serving cell, then subclauses 6.2.3 and 6.2 4 apply with the Network Signaling value indicated by the field additionalSpectrumEmission.

For intra-band non-contiguous carrier aggregation with the UE configured for transmissions on two serving cells, the maximum output power reduction specified in Table 6.2.4A-2 is allowed for all serving cells of the applicable uplink CA configurations according to the CA network signalling value indicated by the field additionalSpectrumEmissionSCell-r10. MPR as specified in subclause 6.2.3A is not allowed in addition, unless A-MPR is N/A.

Table 6.2.4A-2: Additional Maximum Power Reduction (A-MPR) for intra-band non-contiguous CA

If for inter-band carrier aggregation the UE is configured for transmissions on a single serving cell, then subclauses 6.2.3 and 6.2 4 apply with the Network Signaling value indicated by the field additionalSpectrumEmission.

For inter-band carrier aggregation with the UE configured for transmissions on two serving cells the maximum output power reduction specified in Table 6.2.4-1 is allowed for each serving cell of the applicable uplink CA configuration according to the Network Signaling value indicated by the field additionalSprectrumEmission for the PCC and the CA network signalling value indicated by the field additionalSpectrumEmissionSCell-r10 for the SCC. The value of additionalSpectrumEmissionSCell-r10 is equal to that of additionalSprectrumEmission configured on the SCC. MPR as specified in subclause 6.2.3A is allowed in addition.

For PUCCH and SRS transmissions, the allowed A-MPR is according to that specified for PUSCH QPSK modulation for the corresponding transmission bandwidth.

For intra-band carrier aggregation, the A-MPR shall be evaluated per Teval period as specified in table 6.2.4A-3 and given by the maximum value taken over the transmission(s) on all component carriers within that period; the maximum A-MPR over TREF is then applied for the entire TREF.

Table 6.2.4A-3: A-MPR evaluation Teval period

For combinations of intra-band and inter-band carrier aggregation with the UE configured for transmission on three serving cells (up to two contiguously aggregated carriers per band), the maximum output power reduction is specified as follows. For the band supporting one serving cell the maximum output power reduction specified in Table 6.2.4-1 is allowed according to the Network Signaling value indicated by the field additionalSprectrumEmission for the PCC and the CA network signalling value indicated by the field additionalSpectrumEmissionSCell-r10 for the SCC. The value of additionalSpectrumEmissionSCell-r10 is equal to that of additionalSprectrumEmission configured on the SCC. MPR as specified in subclause 6.2.3A is allowed in addition. For the band supporting intra-band contiguous aggregation with the UE configured for transmissions on two serving cells, the maximum output power reduction specified in Table 6.2.4A-1 is allowed for all serving cells of the applicable uplink CA configurations according to the CA network signalling value indicated by the field additionalSpectrumEmissionSCell-r10. Then clause 6.2.3A does not apply, i.e. the carrier aggregation MPR = 0dB, unless the value indicated is CA_NS_31. For uplink 64 QAM and 256 QAM, the applied maximum output power reduction is obtained by taking the maximum value of MPR requirements specified in Table 6.2.3A-1 and A-MPR requirements specified in Table 6.2.4A-1.

For the UE maximum output power modified by A-MPR specified in table 6.2.4A-1, the power limits specified in subclause 6.2.5A apply.

## 6.2.4A.1A-MPR for CA_NS_01 for CA_1C

If the UE is configured to CA_1C and it receives IE CA_NS_01 the allowed maximum output power reduction applied to transmissions on the PCC and the SCC for contiguously aggregated signals is specified in table 6.2.4A.1-1.

Table 6.2.4A.1-1: Contiguous allocation A-MPR for CA_NS_01

If the UE is configured to CA_1C and it receives IE CA_NS_01 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =-22.5 A + 17; 0 ≤ A < 0.20

-11.0 A + 14.7; 0.20 ≤ A < 0.70

-1.7 A + 8.2 ; 0.70 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.2A-MPR for CA_NS_02 for CA_1C

If the UE is configured to CA_1C and it receives IE CA_NS_02 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.2-1.

Table 6.2.4A.2-1: Contiguous allocation A-MPR for CA_NS_02

If the UE is configured to CA_1C and it receives IE CA_NS_02 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows:

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =-22.5 A + 17; 0 ≤ A < 0.20

-11.0 A + 14.7; 0.20 ≤ A < 0.70

-1.7 A + 8.2 ; 0.70 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.3A-MPR for CA_NS_03 for CA_1C

If the UE is configured to CA_1C and it receives IE CA_NS_03 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.3-1.

Table 6.2.4A.3-1: Contiguous allocation A-MPR for CA_NS_03

If the UE is configured to CA_1C and it receives IE CA_NS_03 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows:

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =-23.33A + 17.5; 0 ≤ A < 0.15

-7.65A + 15.15; 0.15 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.4A-MPR for CA_NS_04

If the UE is configured to CA_41C or any uplink inter-band CA configuration containing CA_41C and it receives IE CA_NS_04 the allowed maximum output power reduction applied to transmission on two component carriers for contiguously aggregated signals is specified in Table 6.2.4A.4-1 and Table 6.2.4A.4-1A for UE power class 3 and in Table 6.2.4A.4-2 for UE power class 2.

Table 6.2.4A.4-1: Contiguous Allocation A-MPR for CA_NS_04 (power class 3), Bandwidth Class C

Table 6.2.4A.4-1A: Contiguous Allocation A-MPR for CA_NS_04 (power class 3), Bandwidth Class D

Table 6.2.4A.4-2: Contiguous Allocation A-MPR for CA_NS_04 (power class 2)

If the UE is configured to CA_41C or any uplink inter-band CA configuration containing CA_41C and it receives IE CA_NS_04 the allowed maximum output power reduction applied to transmissions on two serving cells assigned to Band 41 with non-contiguous resource allocation is defined as follows for UE power class 3

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = 11 ; 0≤ A < 0.05

= -55.0A + 13.75; 0.05≤ A < 0.15

= -4.0A + 6.10 ; 0.15≤ A < 0.40

= -0.83A + 4.83; 0.40 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

If the UE is configured to CA_41D or any uplink inter-band CA configuration containing CA_41D and it receives IE CA_NS_04 the allowed maximum output power reduction applied to transmissions on two serving cells assigned to Band 41 with non-contiguous resource allocation is defined as follows for UE power class 3

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = 11.5 ; 0≤ A < 0.05

= -55.0A + 14.25; 0.05≤ A < 0.15

= -4.0A + 6.60 ; 0.15≤ A < 0.40

= -0.833A + 5.333; 0.40 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

If the UE is configured to CA_41C or any uplink inter-band CA configuration containing CA_41C and it receives IE CA_NS_04 the allowed maximum output power reduction applied to transmissions on two serving cells assigned to Band 41 with non-contiguous resource allocation is defined as follows for UE power class 2

A-MPR = CEIL {MA, 0.5}Where MA is defined as follows when the lower edge of the aggregated channel bandwidth (Table 5.6A-1) is less than or equal to the lower edge cutoff frequency specified in Table 6.2.4A.4-2 for the corresponding CA bandwidth combination

MA = 13.0 ; 0 ≤ A < 0.05

= -46.67A + 15.33; 0.05 ≤ A < 0.20

= -5.0A + 7.0 ; 0.20 ≤ A < 0.50

= 4.5; 0.50 ≤ A ≤ 1

And MA is defined as follows when the lower edge of the aggregated channel bandwidth exceeds the lower edge cutoff frequency specified in Table 6.2.4A.4-2 for the corresponding CA bandwidth combination

MA = 8.2 ; 0 ≤ A < 0.04

= -40.0A + 9.8; 0.04 ≤ A < 0.075

= -16.0A + 8.0 ; 0.075 ≤ A < 0.25

= -3.33A + 4.83; 0.25 ≤ A < 0.40

= -0.83A + 3.83; 0.40 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.5A-MPR for CA_NS_05 for CA_38C

If the UE is configured to CA_38C and it receives IE CA_NS_05 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.5-1.

Table 6.2.4A.5-1: Contigous Allocation A-MPR for CA_NS_05

If the UE is configured to CA_38C and it receives IE CA_NS_05 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = -14.17 A + 16.50; 0 ≤ A < 0.60

-2.50 A + 9.50; 0.60 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.6A-MPR for CA_NS_06

If the UE is configured to CA_7C and it receives IE CA_NS_06 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.6-1.

Table 6.2.4A.6-1: Contiguous Allocation A-MPR for CA_NS_06

If the UE is configured to CA_7C and it receives IE CA_NS_06 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows:

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =-13.33A + 17.5; 0 ≤ A < 0.15

-6.47A + 16.47; 0.15 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.7A-MPR for CA_NS_07

If the UE is configured to CA_39C or any uplink inter-band CA configuration containing CA_39C and it receives IE CA_NS_07 the allowed maximum output power reduction applied to transmission on two component carriers for contiguously aggregated signals is specified in Table 6.2.4A.7-1.

Table 6.2.4A.7-1: Contiguous Allocation A-MPR for CA_NS_07

If the UE is configured to CA_39C or any uplink inter-band CA configuration containing CA_39C and it receives IE CA_NS_07 the allowed maximum output power reduction applied to transmissions on two serving cells assigned to Band 39 with non-contiguous resource allocation is defined as follows

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = -16. 25A + 21; 0 ≤ A < 0. 80

-2.50 A + 10.00; 0.80 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg

## 6.2.4A.8A-MPR for CA_NS_08

If the UE is configured to CA_42C and it receives IE CA_NS_08 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.8-1.

Table 6.2.4A.8-1: Contiguous Allocation A-MPR for CA_NS_08

If the UE is configured to CA_42C and it receives IE CA_NS_08 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined as follows

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA =20; 0 ≤ A < 0.025

## 23 – 120A; 0.025 ≤ A < 0.05

## 17.53 – 10.59A; 0.05 ≤ A ≤ 0.9

8; 0.9 ≤ A ≤ 1

Where A = NRB_alloc / NRB_agg.

## 6.2.4A.9Void

## 6.2.4A.10A-MPR for CA_NS_10

If the UE is configured to CA_48C and it receives IE CA_NS_10 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.10-2 or Table 6.2.4A.10-3. Which table is determined by the position of the carrier centre frequency in Table 6.2.4A.10-1.

Table 6.2.4A.10-1: A-MPR regions for CA_48C

Table 6.2.4A.10-2: A-MPR regions for CA_48C at the band edge

Table 6.2.4A.10-3: A-MPR regions for CA_48C at the band center (“range for lower A-MPR”)

If the UE is configured to CA_48C and it receives IE CA_NS_10 the allowed maximum output power reduction applied to transmissions on the PCell and the SCell with non-contiguous resource allocation is defined with both an edge and a center scenario and is determined in Table 6.2.4A.10-4.

Table 6.2.4A.10-4: A-MPR regions for CA_48C

The Edge scenario is defined as follows

A-MPR = CEIL {MA, 0.5}

where MA is defined as follows

MA =      18.00 - 10.00 A; 0 ≤ A < 0.05

## 18.50 - 20.00 A;0.05 ≤ A < 0.2

## 15.50 - 5.00 A;0.2 ≤ A < 1

where A = NRB_alloc / NRB_agg.

The Center scenario is defined as follows

A-MPR = CEIL {MA, 0.5}

where MA is defined as follows

MA =      11.50 - 10.00 A; 0 ≤ A < 0.15

## 10.88 - 5.88 A;0.15 ≤ A < 1

where A = NRB_alloc / NRB_agg

For CA_48B contiguous resource allocation when 3560 MHz ≤ Fagg_alloc_low and Fagg_alloc_high <= 3690 MHz

if allocation is inner 1 then A-MPR = 0 dB where inner 1 is defined as

RBStart,Low = max(1, floor(LCRB/2))

where max() indicates the largest value of all arguments and floor(x) is the greatest integer less than or equal to x.

RBStart,High = NRB_agg – RBStart,Low – LCRB

with following conditions

RBStart,Low  ≤  RBStart  ≤  RBStart,High, and

LCRB  ≤  ceil(NRB_agg /2)

Inner 1 region exceptions thresholds are

RBstart < 12 or RBend ≥ 92 for BWChannel_CA = 20MHz

For which AMPR = 4 dB.

else A-MPR= 4 dB

For CA_48B contiguous resource allocation when Fagg_alloc_low < 3560 MHz

if allocation is inner 3 then A-MPR = 0 dB

Inner 3 region exceptions thresholds are

RBstart < 30 for BWChannel_CA = 20MHz

For which AMPR = 7dB.

where inner 3 is defined as

NRB_agg /4 < RBStart < NRB_agg 3/4  LCRB  AND LCRB < NRB_agg/4

else A-MPR = 7 dB.

For CA_48B contiguous resource allocation when Fagg_alloc_high > 3690 MHz

if allocation is inner 3 then A-MPR = 0 dB

Inner 3 region exceptions thresholds are

RBstart > 70 for BWChannel_CA = 20MHz

For which AMPR = 7dB.

where inner 3 is defined as

NRB_agg /4 < RBStart < NRB_agg 3/4  LCRB  AND LCRB < NRB_agg/4

else A-MPR = 7 dB.

For CA_48B non-contiguous resource allocation when 3560 MHz ≤ Fagg_alloc_low and  Fagg_alloc_high <= 3690 MHz

A = NRB_alloc / NRB_agg

A-MPR= 13.00;         0.00 <= A <= 0.08

## 13.78 - 9.78 A; 0.08 < A <= 1.00

For CA_48B non-contiguous resource allocation when Fagg_alloc_low < 3560 MHz or Fagg_alloc_high > 3690 MHz

A-MPR= 13.00;     0.00 <= A <= 0.08

## 14.13  -14.06 A; 0.08 < A <= 0.40

## 9.17 – 1.67 A;0.40 < A <= 1.00

## 6.2.4A.11A-MPR for CA_NS_11

If the UE is configured to CA_2C and it receives IE CA_NS_11 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.11-1.

Table 6.2.4A.11-1: Contiguous Allocation A-MPR for CA_NS_11

## 6.2.4A.12A-MPR for CA_NS_12

If the UE is configured to CA_28C and it receives IE CA_NS_12 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.12-1.

Table 6.2.4A.12-1: Contiguous Allocation A-MPR for CA_NS_12

## 6.2.4A.13A-MPR for CA_NS_13

If the UE is configured to CA_28C and it receives IE CA_NS_13 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.13-1.

Table 6.2.4A.13-1: Contiguous Allocation A-MPR for CA_NS_13

## 6.2.4A.14A-MPR for CA_NS_17

If the UE is configured to CA_28C and it receives IE CA_NS_17 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.14-1.

Table 6.2.4A.14-1: Contiguous Allocation A-MPR for CA_28C NS_17 (power class 3)

## 6.2.4A.15A-MPR for CA_NS_18

If the UE is configured to CA_28C and it receives IE CA_NS_178 the allowed maximum output power reduction applied to transmission on the PCC and the SCC for contiguously aggregated signals is specified in Table 6.2.4A.15-1.

Table 6.2.4A.15-1: Contiguous Allocation A-MPR for CA_28C with NS_18 (power class 3)

## 6.2.4BUE maximum output power with additional requirements for UL-MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the A-MPR values specified in subclause 6.2.4 shall apply to the maximum output power specified in Table 6.2.2B-1. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UE supporting UL-MIMO, the maximum output power is measured as the sum of the maximum output power at each UE antenna connector. Unless stated otherwise, an A-MPR of 0 dB shall be used.

For the UE maximum output power modified by A-MPR, the power limits specified in subclause 6.2.5B apply.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.2.4 apply.

## 6.2.4DUE maximum output power with additional requirements for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the allowed A-MPR for the maximum output power for ProSe physical channels PSDCH, PSCCH, PSSCH, and PSBCH shall be as specified in subclause 6.2.4 for  PUSCH for the corresponding modulation and transmission bandwidth.

The allowed A-MPR for the maximum output power for ProSe physical signal PSSS and SSSS shall be as be as specified in subclause 6.2.4 for PUSCH QPSK modulation for the corresponding transmission bandwidth.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.2.4D apply for ProSe transmission and the requirements in subclause 6.2.4 apply for uplink transmission.

## 6.2.4EUE maximum output power with additional requirements for category M1 and M2 UE

Additional ACLR and spectrum emission requirements can be signalled by the network to indicate that the UE shall also meet additional requirements in a specific deployment scenario. To meet these additional requirements, Additional Maximum Power Reduction (A-MPR) is allowed for the output power as specified in Table 6.2.2E-1 and Table 6.2.4E-2. Unless stated otherwise, an A-MPR of 0 dB shall be used.

For UE Power Class 3 and 5 the specific requirements and identified subclauses are specified in Table 6.2.4E-1 and Table 6.2.4E-2 along with the allowed A-MPR values that may be used to meet these requirements. The allowed A-MPR values specified below in Table 6.2.4E-1 and Table 6.2.4E-2 and from 6.2.4-2 to 6.2.4-15 are in addition to the allowed MPR requirements specified in subclause 6.2.3E.

Table 6.2.4E-1: Additional Maximum Power Reduction (A-MPR) for category M1 UE

Table 6.2.4E-2: Additional Maximum Power Reduction (A-MPR) for category M2 UE

Table 6.2.4E-3: A-MPR for "NS_04" for Cat-M1

Table 6.2.4E-4: A-MPR for "NS_07" for Cat-M1

Table 6.2.4E-5: A-MPR for "NS_12" for Cat-M1

For subPRB allocation, the allowed A-MPR values specified below in Table 6.2.4E-6 and Table 6.2.4E-7 for category M1 UE and category M2 UE respectively in addition to the allowed MPR requirements specified in subclause 6.2.3E.

Table 6.2.4E-6: Additional Maximum Power Reduction (A-MPR) for category M1 UE for subPRB allocation

Table 6.2.4E-7: Additional Maximum Power Reduction (A-MPR) for category M2 UE for subPRB allocation

Table 6.2.4E-8: A-MPR for "NS_03" for Cat-M1 with sub-PRB allocation

Table 6.2.4E-9: A-MPR for "NS_04" for Cat-M1 with sub-PRB allocation

Table 6.2.4E-10: A-MPR for "NS_03" for Cat-M2 with sub-PRB allocation

Table 6.2.4E-11: A-MPR for "NS_04" for Cat-M2 with sub-PRB allocation

Table 6.2.4E-12: A-MPR for "NS_07" for Cat-M2 with sub-PRB allocation

Table 6.2.4E-13: A-MPR for "NS_06" for Cat-M1 with sub-PRB allocation

Table 6.2.4E-14: A-MPR for "NS_12" for Cat-M1 with sub-PRB allocation

Table 6.2.4E-15: A-MPR for "NS_35" for Cat-M1 with sub-PRB allocation

Table 6.2.4E-16: A-MPR for "NS_38" for Cat-M1 with sub-PRB allocation for E-UTRA lowest channel edge > 1427 MHz and ≤ 1447 MHz

Table 6.2.4E-17: A-MPR for "NS_05" for Cat-M2 with sub-PRB allocation

Table 6.2.4E-18: A-MPR for "NS_06" for Cat-M2 with sub-PRB allocation

Table 6.2.4E-19: A-MPR for "NS_12" for Cat-M2 with sub-PRB allocation for E-UTRA lower channel edge >= 814.2 MHz and ≤ 829.2 MHz

Table 6.2.4E-20: A-MPR for "NS_13" for Cat-M2 with sub-PRB allocation for E-UTRA lower channel edge >= 819 MHz and ≤ 824 MHz

Table 6.2.4E-21: A-MPR for "NS_15" for Cat-M2 with sub-PRB allocation for E-UTRA highest channel edge > 834 MHz and ≤ 849 MHz

Table 6.2.4E-22: A-MPR for "NS_16" for Cat-M2 with sub-PRB allocation for E-UTRA lowest channel edge > 807 MHz and ≤ 812 MHz

Table 6.2.4E-23: A-MPR for “NS_07” for Cat-M1 with sub-PRB allocation

Table 6.2.4E-24: A-MPR for “NS_38” for Cat-M2 with sub-PRB allocation for E-UTRA lowest channel edge > 1427 MHz and ≤ 1447 MHz

Table 6.2.4E-25: A-MPR for “NS_56” for Cat-M1 allocation

Table 6.2.4E-26: A-MPR for “NS_56” for Cat-M1 allocation with subPRB

Table 6.2.4E-27: A-MPR for “NS_56” for Cat-M2 allocation with subPRB

Table 6.2.4E-28: A-MPR for “NS_27” for Cat-M1 allocation with subPRB allocation

No other A-MPR requirement than those specified in table 6.2.4E-1, table 6.2.4E-2, table 6.2.4E-6 and table 6.2.4E-7 applies to category M1 and M2 UE.

## 6.2.4FUE maximum output power with additional requirements for category NB1 and NB2 UE

Additional ACLR and spectrum emission requirements can be signalled by the network to indicate that the UE shall also meet additional requirements in a specific deployment scenario. To meet these additional requirements, Additional Maximum Power Reduction (A-MPR) is allowed for the output power are specified. For the agreed E-UTRA bands for category NB1 and NB2 UE an A-MPR of 0 dB shall be allowed unless specified otherwise.

For UE Power Class 3 and 5 the specific requirements and identified subclauses are specified in Table 6.2.4F-1 along with the allowed A-MPR values that may be used to meet these requirements. The allowed A-MPR values specified below in Table 6.2.4F-1 are in addition to the allowed MPR requirements specified in subclause 6.2.3F-1.

Table 6.2.4F-1: Additional Maximum Power Reduction (A-MPR) for category NB1 and NB2 UE

## 6.2.4GUE maximum output power with additional requirements for V2X Communication

For QPSK the MPR requirements specified in subclause 6.2.3G does not apply, i.e. MPR = 0dB. For 16QAM and 64 QAM, the applied maximum output power reduction is obtained by taking the maximum value of MPR requirements specified in subclause 6.2.3G and A-MPR requirements specified in subclause 6.2.4G.

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the maximum output power reduction specified as

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = A-MPRBase + Gpost connector * A-MPRStep

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

A-MPRBase  and A-MPRStep  are specified in Tables 6.2.4G-1, 6.2.4G-2, 6.2.4G-3 is allowed when network signalling value is provided. The supported post antenna connector gain Gpost connector is declared by the UE following the principle described in annex I.

NOTE: the A-MPRstep is the increase in A-MPR allowance to allow UE to meet tighter conducted A-SE and A-SEM requirements with higher value of declared Gpost connector. A-MPRBase is the default A-MPR value when no Gpost connector is declared.  A-MPRBase  and A-MPRstep vary depending on channel frequency and RB allocation. For channel frequencies and RB allocations that are close to the frequency range 5815-5855MHz, those value are much higher due to stringent emission requirement in this range.

Table 6.2.4G-1: Additional Maximum Power Reduction (A-MPR) for power class 3 V2X UE

Table 6.2.4G-2: A-MPR for NS_33

The allowed A-MPR for the maximum output power for V2X physical signal PSBCH and PSSS/SSSS shall be as be as specified in subclause 6.2.4 for the corresponding modulation and transmission bandwidth.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.2.4G apply for V2X  PSSCH and PSCCH transmission. The allowed A-MPR requirements in subclause 6.2.4D apply for other V2X sidelink transmission (PSBCH/PSSS/SSSS). The A-MPR requirements in subclause 6.2.4 apply for uplink transmission.

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the allowed A-MPR for the maximum output power for V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2.4G-3 and 6.2.4G-4 for V2X UE  power class 2.

Table 6.2.4G-3: Additional Maximum Power Reduction (A-MPR) for power class 2 V2X UE

## 6.2.5Configured transmitted power

The UE is allowed to set its configured maximum output power PCMAX,c for serving cell c. The configured maximum output power PCMAX,c is set within the following bounds:

PCMAX_L,c ≤  PCMAX,c  ≤  PCMAX_H,c with

PCMAX_L,c = MIN {PEMAX,c – TC,c,  (PPowerClass – ΔPPowerClass) – MAX(MPRc + A-MPRc + ΔTIB,c + TC,c + TProSe, P-MPRc)}

PCMAX_H,c = MIN {PEMAX,c,  PPowerClass – ΔPPowerClass}

where

-PEMAX,c is the value given by IE P-Max for serving cell c, defined in [7];

-PPowerClass is the maximum UE power specified in Table 6.2.2-1 without taking into account the tolerance specified in the Table 6.2.2-1;

-ΔPPowerClass = 3 dB for a power class 2 capable UE operating in Band 41, when P-max of 23 dBm or lower is indicated or if the uplink/downlink configuration is 0 or 6 in the cell; otherwise, ΔPPowerClass = 0 dB

-ΔPPowerClass = PPowerClass – PPowerClass_Default dB for UE operating in Band 14, when P-max of 23 dBm or lower is indicated in the cell; otherwise, ΔPPowerClass = 0 dB.

-MPRc and A-MPRc for serving cell c are specified in subclause 6.2.3 and subclause 6.2.4, respectively;

-TIB,c is the additional tolerance for serving cell c as specified in Table 6.2.5-2; TIB,c = 0 dB otherwise;

-TC,c = 1.5 dB when NOTE 2 in Table 6.2.2-1 applies;

-TC,c = 0 dB when NOTE 2 in Table 6.2.2-1 does not apply;

-TProSe = 0.1 dB when the UE supports ProSe Direct Discovery and/or ProSe Direct Communication on the corresponding E-UTRA ProSe band; TProSe = 0 dB otherwise.

-For a power class higher than default UE power class capable UE except for operating in Band 14 and Band 41, ΔPPowerClass = PPowerClass – PPowerClass_Default dB, when the band is a TDD band whose frame configuration is 0 or 6; or P-max is not indicated in the cell; or P-Max is provided and set to the maximum output power of the default power class or lower, otherwise, ΔPPowerClass = 0 dB.

P-MPRc is the allowed maximum output power reduction for

a)ensuring compliance with applicable electromagnetic energy absorption requirements and addressing unwanted emissions / self desense requirements in case of simultaneous transmissions on multiple RAT(s) for scenarios not in scope of 3GPP RAN specifications;

b)ensuring compliance with applicable electromagnetic energy absorption requirements in case of proximity detection is used to address such requirements that require a lower maximum output power.

The UE shall apply P-MPR c for serving cell c only for the above cases. For UE conducted conformance testing P-MPR shall be 0 dB

NOTE 1:P-MPRc was introduced in the PCMAX,c equation such that the UE can report to the eNB the available maximum output transmit power. This information can be used by the eNB for scheduling decisions.

NOTE 2: P-MPRc may impact the maximum uplink performance for the selected UL transmission path.

TREF and Teval are specified in Table 6.2.5-0 for different TTI patterns. For each TREF, the PCMAX_L,c for serving cell c is evaluated perTeval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_ L,c over the one or more Teval is then applied for the entire TREF. PPowerClass shall not be exceeded by the UE during any period of time.

Table 6.2.5-0: PCMAX evaluation window for different TTI patterns

The measured configured maximum output power PUMAX,c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL,c, T(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T(PCMAX_H,c).

where the tolerance T(PCMAX,c) for applicable values of PCMAX,c is specified in Table 6.2.5-1, and Table 6.2.5-1A. The tolerance TL,c is the absolute value of the lower tolerance for the applicable operating band as specified in Table 6.2.2-1.

Table 6.2.5-1: PCMAX tolerance

Table 6.2.5-1A: PCMAX tolerance for power class 5

Table 6.2.5-1B: PCMAX tolerance for power class 6 for category M1 and M2 UE

For the UE which supports inter-band carrier aggregation configurations with the uplink assigned to one or two E-UTRA bands the ΔTIB,c is defined for applicable bands in Table 6.2.5-2, Table 6.2.5-3 and Table 6.2.5-4 where unless otherwise stated, the same ΔTIB,c is applicable to E-UTRA band(s) part for CA configurations which have the same E-UTRA operating band combination.

Table 6.2.5-2: ΔTIB,c (two bands)

NOTE:The above additional tolerances do not apply to supported UTRA operating bands with frequency range below 1 GHz that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations when such bands are belonging only to band combination(s) where one band is <1GHz and another band is >1.7GHz and there is no harmonic relationship between the low band UL and high band DL. Otherwise the above additional tolerances also apply to supported UTRA operating bands that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations.

NOTE:To meet the TIB,c requirements for CA_3A-7A with state-of-the-art technology, an increase in power consumption of the UE may be required. It is also expected that as the state-of-the-art technology evolves in the future, this possible power consumption increase can be reduced or eliminated.

Table 6.2.5-3: ΔTIB,c (three bands)

Table 6.2.5-4: ΔTIB,c (four bands)

Table 6.2.5-5: ΔTIB,c (five bands)

NOTE:The above additional tolerances do not apply to supported UTRA operating bands with frequency range below 1 GHz that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations when such bands are belonging only to band combination(s) where one band is <1GHz and other bands are >1.7GHz and there is no harmonic relationship between the low band UL and high band DL. Otherwise the above additional tolerances also apply to supported UTRA operating bands that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations.

Table 6.2.5-6: ΔTIB,c (six bands)

## 6.2.5AConfigured transmitted power for CA

For uplink carrier aggregation the UE is allowed to set its configured maximum output power PCMAX,c for serving cell c and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c  on serving cell c shall be set as specified in subclause 6.2.5.

For uplink inter-band carrier aggregation, MPRc and A-MPRc apply per serving cell c and are specified in subclause 6.2.3 and subclause 6.2.4, respectively. P-MPR c accounts for power management for serving cell c. PCMAX,c  is calculated under the assumption that the transmit power is increased independently on all component carriers.

For uplink intra-band contiguous and non-contiguous carrier aggregation, MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR specified in subclause 6.2.3A and subclause 6.2.4A respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR. PCMAX,c  is calculated under the assumption that the transmit power is increased by the same amount in dB on all component carriers.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

For uplink inter-band carrier aggregation with one serving cell c per operating band when same TTI pattern is used in all aggregated serving cells,

PCMAX_L = MIN {10log10∑ MIN [ pEMAX,c/ (tC,c),  pPowerClass/(mprc·a-mprc·tC,c ·tIB,c·tProSe) , pPowerClass/pmprc], PPowerClass}

PCMAX_H = MIN{10 log10 ∑ pEMAX,c , PPowerClass}

where

-pEMAX,c is the linear value of PEMAX, c which is given by IE P-Max for serving cell c in [7];

-PPowerClass is the maximum UE power specified in Table 6.2.2A-1 without taking into account the tolerance specified in the Table 6.2.2A-1; pPowerClass is the linear value of PPowerClass;

-mpr c and a-mpr c are the linear values of MPR c and A-MPR c as specified in subclause 6.2.3 and subclause 6.2.4, respectively;

-pmprc is the linear value of P-MPR c;

-tC,c is the linear value of TC,ctC,c = 1.41 when NOTE 2 in Table 6.2.2-1 applies for a serving cell c, otherwise tC,c = 1;

-tIB,c  is the linear value of the inter-band relaxation term TIB,c of the serving cell c as specified in Table 6.2.5-2; otherwise tIB,c

- tProSe is the linear value of TProSe and applies as specified in subclause 6.2.5.

For uplink intra-band contiguous and non-contiguous carrier aggregation when same TTI pattern is used in all aggregated serving cells,

PCMAX_L  = MIN{10 log10 ∑ pEMAX,c  - TC , (PPowerClass – ΔPPowerClass) – MAX(MPR + A-MPR + ΔTIB,c + TC + TProSe, P-MPR ) }

PCMAX_H  = MIN{10 log10 ∑ pEMAX,c , PPowerClass}

where

-pEMAX,c is the linear value of PEMAX,c which is given by IE P-Max for serving cell c in [7];

-PPowerClass is the maximum UE power specified in Table 6.2.2A-1 without taking into account the tolerance specified in the Table 6.2.2A-1;

ΔPPowerClass = 3 dB for a power class 2 capable UE operating in Band 41, when P-max of 23 dBm or lower is indicated or if the uplink/downlink configuration is 0 or 6 in the cell; otherwise, ΔPPowerClass = 0 dB

-MPR and A-MPR are specified in subclause 6.2.3A and subclause 6.2.4A respectively;

-TIB,c is the additional tolerance for serving cell c as specified in Table 6.2.5-2;

-P-MPR is the power management term for the UE;

-TC is the highest value TC,c among all serving cells c in the TREF over all Teval durations. TC,c = 1.5 dB when NOTE 2 in Table 6.2.2A-1 applies to the serving cell c, otherwise TC,c = 0 dB;

- TProSe applies as specified in subclause 6.2.5.

For uplink inter-band carrier aggregation with one serving cell c per operating band when at least one different TTI patterns is used in aggregated cells, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of TTI length i, i = 1,2,3 and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in TTI p of serving cell c(i) on TTI length i shall be set within the following bounds:

PCMAX_L,c(i),i (p) ≤  PCMAX,c(i), i (p) ≤  PCMAX_H,c(i),i (p)

where PCMAX_L,c(i),i (p) and PCMAX_H,c(i),i (p) are the limits for a serving cell c(i) of TTI length i as specified in subclause 6.2.5.

The total UE configured maximum output power PCMAX (p,q,k) in a TTI p of TTI length 1 ,  a TTI q of TTI length 2 and a TTI k of TTI length 3 that overlap in time shall be set within the following bounds unless stated otherwise:

PCMAX_L(p,q,k) ≤  PCMAX (p,q,k)  ≤  PCMAX_H (p,q,k)

When p, q, k are of different lengths and belong to different cells:

PCMAX_L (p,q,k) = MIN {10 log10 [pCMAX_L,c(1),1 (p) + pCMAX_L,c(2),2 (q)+ + pCMAX_L,c(3),3 (k)], PPowerClass}

PCMAX_H (p,q,k) = MIN {10 log10 [pCMAX_H,c(1),1 (p) + pCMAX_H,c(2),2 (q) + pCMAX_H,c(3),3 (k)], PPowerClass}

where pCMAX_L,c(i),i and pCMAX_H,c(i),i are the respective limits PCMAX_L,c(i),iand PCMAX_H,c(i),i expressed in linear scale.

For combinations of intra-band and inter-band carrier aggregation with UE configured for transmission on three serving cells (up to two contiguously aggregated carriers per operating band),

For the case when p and q belong to the same band and k belongs to a different band but p, q and k are of the same TTI pattern.

PCMAX_L = MIN {10log10∑(pCMAX_L, Bi), PPowerClass}

PCMAX_H = MIN{10 log10 ∑ pEMAX,c , PPowerClass}

For the case when p and q belong to the same band and are of the same TTI pattern while k belong to a different band and is of different TTI pattern then:

PCMAX_L (p,q,k) = MIN {10 log10 [pCMAX_L,Bi(p) + pCMAX_L,c(3),3 (k)], PPowerClass}

PCMAX_H (p,q,k) = MIN {10 log10 [pCMAX_H,Bi (p) + pCMAX_H,c(3),3 (k)], PPowerClass}

where

-pEMAX,c is the linear value of PEMAX, c which is given by IE P-Max for serving cell c in [7];

-PPowerClass is the maximum UE power specified in Table 6.2.2A-0 without taking into account the tolerance specified in the Table 6.2.2A-0; pPowerClass is the linear value of PPowerClass;

- pCMAX_L, Bi is the linear values of PCMAX_L as specified in corresponding operating band. PCMAX_L,c specified for single carrier in subclause 6.2.5 applies for operating band supporting one serving cell. PCMAX_L specified for uplink intra-band contiguous carrier aggregation in subclause 6.2.5A applies for operating band supporting two contiguous serving cells.

- intra-band carriers use the same TTI patterns.

TREF and Teval are specified in Table 6.2.5A-0 when same and different TTI patterns are used in aggregated carriers. For each TREF, the PCMAX_L is evaluated per Teval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_L over the one or more Teval is then applied for the entire TREF. PPowerClass shall not be exceeded by the UE during any period of time.

Table 6.2.5A-0: PCMAX evaluation window for different TTI patterns

If the UE is configured with multiple TAGs and transmissions of the UE on TTI i for any serving cell in one TAG overlap some portion of the first symbol of the transmission on TTI i +1 for a different serving cell in another TAG, the UE minimum of PCMAX_L for TTIs i and i + 1 applies for any overlapping portion of TTIs i and i + 1. PPowerClass shall not be exceeded by the UE during any period of time.

In case PC2 and uplink intra-band contiguous CA capable UE receives pEMAX,c in Scell then that applies both to Scell and Pcell once the Scell is activated.

The measured maximum output power PUMAX over all serving cells with same TTI pattern shall be within the following range:

PCMAX_L  – MAX{TL, TLOW(PCMAX_L) }  ≤  PUMAX  ≤  PCMAX_H  +  THIGH(PCMAX_H)

PUMAX = 10 log10 ∑ pUMAX,c

where pUMAX,c  denotes the measured maximum output power for serving cell c expressed in linear scale. The tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX are specified in Table 6.2.5A-1 and Table 6.2.5A-2 for inter-band carrier aggregation and intra-band carrier aggregation, respectively. The tolerance TL is the absolute value of the lower tolerance for applicable E-UTRA CA configuration as specified in Table 6.2.2A-0, Table 6.2.2A-1 and Table 6.2.2A-2 for inter-band carrier aggregation, intra-band contiguous carrier aggregation and intra-band non-contiguous carrier aggregation, respectively.

The measured maximum output power PUMAX over all serving cells, when atleast one TTI has a different TTI pattern, shall be within the following range:

P’CMAX_L–  MAX{TL, TLOW (P’CMAX_L)} ≤  P’UMAX  ≤  P’CMAX_H + THIGH (P’CMAX_H)

P’UMAX = 10 log10 ∑ p’UMAX,c

where p’UMAX,c  denotes the average measured maximum output power for serving cell c expressed in linear scale over TREF. The tolerances TLOW(P’CMAX) and THIGH(P’CMAX) for applicable values of P’CMAX are specified in Table 6.2.5A-1 and Table 6.2.5A-2 for inter-band carrier aggregation and intra-band carrier aggregation, respectively. The tolerance TL is the absolute value of the lower tolerance for applicable E-UTRA CA configuration as specified in Table 6.2.2A-0, Table 6.2.2A-1 and Table 6.2.2A-2 for inter-band carrier aggregation, intra-band contiguous carrier aggregation and intra-band non-contiguous carrier aggregation, respectively.

where:

P’CMAX_L  = MIN{ MIN {10log10∑(pCMAX_L, Bi), PPowerClass} over all overlapping TTIs in TREF}

P’CMAX_H = MAX{ MIN{10 log10 ∑ pEMAX,c , PPowerClass} over all overlapping TTIs in TREF}

Table 6.2.5A-1: PCMAX tolerance for uplink inter-band CA (two bands)

Table 6.2.5A-2: PCMAX tolerance for uplink intra-band CA

## 6.2.5BConfigured transmitted power for UL-MIMO

For UE supporting UL-MIMO, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in subclause 6.2.5 shall apply to UE supporting UL-MIMO, where

-PPowerClass, ΔPPowerClass and TC,c are specified in subclause 6.2.2B;

-MPR,c is specified in subclause 6.2.3B;

-A-MPR,c is specified in subclause 6.2.4B.

The measured configured maximum output power PUMAX,c for serving cell c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL, T LOW(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T HIGH(PCMAX_H,c)

where TLOW(PCMAX_L,c) and THIGH(PCMAX_H,c) are defined as the tolerance and applies to PCMAX_L,c and PCMAX_H,c separately, while TL is the absolute value of the lower tolerance in Table 6.2.2B-1 for the applicable operating band.

For UE with two transmit antenna connectors in closed-loop spatial amultiplexing scheme, the tolerance is specified in Table 6.2.5B-1. The requirements shall be met with UL-MIMO configurations specified in Table 6.2.2B-2.

Table 6.2.5B-1: PCMAX,c tolerance in closed-loop spatial multiplexing scheme

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.2.5 apply.

## 6.2.5CConfigured transmitted power for Dual Connectivity

For inter-band dual connectivity with one uplink serving cell per CG, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in subframe p of  serving cell c(i) on CG i shall be set within the following bounds:

PCMAX_L,c(i),i (p) ≤  PCMAX,c(i), i (p) ≤  PCMAX_H,c(i),i (p)

where PCMAX_L,c(i),i (p) and PCMAX_H,c(i),i (p) are the limits for a serving cell c(i) of CG i as specified in subclause 6.2.5.

The total UE configured maximum output power PCMAX (p,q) in a subframe p of CG 1 and a subframe q of CG 2 that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L(p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) = MIN {10 log10 [pCMAX_L,c(1),1 (p) + pCMAX_L,c(2),2 (q)], PPowerClass}

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_H,c(1),1 (p) + pCMAX_H,c(2),2 (q)], PPowerClass}

where pCMAX_L,c(i),i is pCMAX_H,c(i),i are the respective limits PCMAX_L,c(i),i (p) and PCMAX_H,c(i),i (p) expressed in linear scale.

If the UE is configured in Dual Connectivity and synchronous transmissions of the UE on subframe p for a serving cell in one CG overlaps some portion of the first symbol of the transmission on subframe q +1 for a different serving cell in the other CG, the UE minimum of PCMAX_L between subframes pairs (p, q) and (p+1, q +1) respectively applies for any overlapping portion of subframes (p, q) and (p +1, q+1). PPowerClass shall not be exceeded by the UE during any period of time.

The measured total maximum output power PUMAX over both CGs is

PUMAX = 10 log10 [pUMAX,c(1),1 + pUMAX,c(2),2],

where pUMAX,c(i),i  denotes the measured output power of serving cell c(i) of CG i expressed in linear scale.

If the UE is configured in Dual Connectivity and synchronous transmissions

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5C-1. PCMAX_L may be modified for any overlapping portion of subframes (p, q) and (p +1, q+1).

If the UE is configured in Dual Connectivity and asynchronous transmissions, the subframes of the leading CG are taken as reference subframes for the measurement of the total configured output power PUMAX.  If subframe p of CG 1 and subframe q of CG 2 overlap in time in their respective slot 0 and

1.if p leads in time over q, then p is the reference subframe and the (p,q) and (p,q-1) pairs are considered for determining the PCMAX tolerance

2.if q leads in time over p, then q is the reference subframe and the (p-1,q) and (p,q) pairs are considered for determining the PCMAX tolerance;

for the reference subframe p duration (when subframe p in CG 1 leads):

P’CMAX_L   = MIN {PCMAX_L   (p,q) , PCMAX_L  (p,q-1)}

P’CMAX_H  = MAX {PCMAX_H   (p,q) , PCMAX_H  (p,q-1)}

while for the reference subframe q duration (when subframe q in CG 2 leads):

P’CMAX_L   = MIN {PCMAX_L   (p-1,q) , PCMAX_L  (p,q)}

P’CMAX_H  = MAX {PCMAX_H   (p-1,q) , PCMAX_H  (p,q)}

where PCMAX_L   and PCMAX_H are the applicable limits for each overlapping subframe pairs  (p,q) , (p, q-1) and (p-1,q). The measured total configured maximum output power PUMAX shall be within the following bounds:

P’CMAX_L   –  TLOW (P’CMAX_L)  ≤  PUMAX  ≤  P’CMAX_H + THIGH (P’CMAX_H)

with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5C-1.

Table 6.2.5C-1: PCMAX tolerance for inter-band Dual Connectivity

## 6.2.5DConfigured transmitted power for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the configured maximum output power PCMAX,c and power boundary requirement specified in subclause 6.2.5 shall apply to UE supporting ProSe, where

-MPRc is specified in subclause 6.2.3D;

-A-MPRc is specified in subclause 6.2.4D;

-TProSe = 0.1 dB.

For  and, PEMAX,c is the value given by IE P-Max for serving cell c, defined by [7], when present. PEMAX,c is the value given by IE maxTxPower, defined by [7], when the UE is not associated with a serving cell on the ProSe carrier .

For, PEMAX,c is the value given by the IE discMaxTxPower in [7].

For, PEMAX,c is the value given by the IE maxTxPower in [7] when the ProSe UE is not associated with a serving cell on the ProSe carrier. When the UE is associated with a serving cell, then PEMAX,c is the value given by the IE P-Max when PSBCH/SLSS transmissions is triggered for ProSe Direct communication as specified in [7], and is the value given by the IE discMaxTxPower in [7] otherwise.

For, the value is as calculated for  and applying the MPR for SSSS as specified in Section 6.2.3D.

When a UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the UE is allowed to set its configured maximum output power PCMAX,c,E-UTRA and PCMAX,c,ProSe for the configured E-UTRA uplink carrier and the configured E-UTRA ProSe carrier, respectively, and its total configured maximum output power PCMAX,c.

The configured maximum output power PCMAX c,E-UTRA(p) in subframe p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L,c,E-UTRA (p) ≤  PCMAX,c,E-UTRA (p) ≤  PCMAX_H,c,E-UTRA (p)

where PCMAX_L,c,E-UTRA and PCMAX_H,c,E-UTRA are the limits for a serving cell c as specified in subclause 6.2.5.

The configured maximum output power PCMAX c,ProSe (q) in subframe q for the configured E-UTRA ProSe carrier shall be set within the bounds:

PCMAX,c,ProSe (q) ≤  PCMAX_H,c,ProSe (q)

where PCMAX_H,c,ProSe is the limit as specified in subclause 6.2.5D.

The total UE configured maximum output power PCMAX (p,q) in a subframe p of an E-UTRA uplink carrier and a subframe q of an E-UTRA ProSe sidelink that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L (p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) =  PCMAX_L,c,E-UTRA (p)

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_H,c,E-UTRA (p) + pCMAX_H,c,ProSe (q)], PPowerClass}

where pCMAX_H,c,ProSe and pCMAX_H,c,E-UTRA are the limits PCMAX_H,c,ProSe (q) and PCMAX_H,c,E-UTRA (p) expressed in linear scale.

The measured total maximum output power PUMAX over both the E-UTRA uplink and E-UTRA ProSe carriers is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,ProSe],

where pUMAX,c,E-UTRA  denotes the measured output power of serving cell c for the configured E-UTRA uplink carrier, and pUMAX,c,ProSe denotes the measured output power for the configured E-UTRA ProSe carrier expressed in linear scale.

When a UE is configured for synchronous ProSe and uplink transmissions,

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5C-1. PCMAX_L may be modified for any overlapping portion of subframes (p, q) and (p +1, q+1).

When a UE is configured for asynchronous ProSe and uplink transmissions, the carrier configured for uplink transmission is taken as the reference. If subframe p for the E-UTRA uplink carrier and subframe q for the E-UTRA ProSe carrier overlap in time and

1.if uplink carrier leads in time over q, then p is the reference subframe and, the (p,q) and (p,q-1) pairs are considered for determining the PCMAX tolerance

2.if ProSe carrier leads in time over p, then p is the reference subframe and, the (p,q) and (p,q+1) pairs are considered for determining the PCMAX tolerance

For the reference subframe p duration when uplink carrier leads:

P'CMAX_L   = PCMAX_L,,cE-UTRA (p)

P'CMAX_H  = MAX {PCMAX_H   (p,q-1) , PCMAX_H  (p,q)}

For the reference subframe p duration when ProSe carrier leads:

P'CMAX_L   = PCMAX_L,cE-UTRA (p)

P'CMAX_H  = MAX {PCMAX_H   (p,q) , PCMAX_H  (p,q+1)}

where PCMAX_L,,cE-UTRA (p) and PCMAX_H are the applicable limits for each overlapping subframe pairs (p,q) , (p, q+1) , (p, q-1). The measured total configured maximum output power PUMAX shall be within the following bounds:

P’CMAX_L   –  TLOW (P’CMAX_L)  ≤  PUMAX  ≤  P’CMAX_H + THIGH (P’CMAX_H)

with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5C-1.

## 6.2.5FConfigured transmitted Power for category NB1 and NB2

For each slot i the category NB1and NB2 UE is allowed to set its configured maximum output power PCMAX,c. The configured maximum output power PCMAX,c is set within the following bounds:

PCMAX_L,c ≤  PCMAX,c  ≤  PCMAX_H,c

Where

PCMAX_L,c = MIN { PEMAX,c ,  PPowerClass – MPRc – A-MPRc}

PCMAX_H,c = MIN { PEMAX,c,  PPowerClass}

PEMAX,c is the value given to IE P-Max, defined in [7]

PPowerClass is the maximum category NB1 and NB2 UE power specified in Table 6.2.2F-1 without taking into account the associated tolerance

MPRc is specified in subclause 6.2.3F

A-MPRc = 0dB unless otherwise stated.

The measurement period for PUMAX,c is at least one sub-frame (1ms) for 15 KHz channel spacing, and at least a 2ms slot (excluding the 2304Ts gap when UE is not transmitting) respectively for the 3.75 KHz channel spacing. The measured maximum output power PUMAX,c shall be within the following bounds:

PCMAX_L,c –  T(PCMAX_L,c)  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T(PCMAX_H,c)

Where T(PCMAX) is defined by the tolerance table below and applies to PCMAX_L,c and PCMAX_H,c separately.

Table 6.2.5F-1: PCMAX tolerance for power class 3

Table 6.2.5F-2: PCMAX tolerance for power class 5

Table 6.2.5F-3: PCMAX tolerance for power class 6

## 6.2.5GConfigured transmitted power for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X  operating bands specified in Table 5.5G-1, the V2X UE is allowed to set its configured maximum output power PCMAX,c for component carrier c. The configured maximum output power PCMAX,c is set within the following bounds:

PCMAX_L,c ≤  PCMAX,c  ≤  PCMAX_H,c with

PCMAX_L,c = MIN {PEMAX,c – TC,c,  PPowerClass –– MAX(MPRc + A-MPRc + ΔTIB,c + TC,c + TProSe, P-MPRc), PRegulatory,c }

PCMAX_H,c = MIN {PEMAX,c,  PPowerClass,  PRegulatory,c }

where

-For the total transmitted power PCMAX,c of PSSCH and PSCCH, PEMAX,c is the value given by IE maxTxPower, defined by [7], when the UE is not associated with a serving cell on the V2X carrier.

-For, PEMAX,c is the value given by the IE maxTxPower in [7] when the UE is not associated with a serving cell on the V2X carrier.

-For, the value is as calculated for  and applying the MPR for SSSS as specified in Section 6.2.3D.

-PPowerClass is the maximum UE power specified in Table 6.2.2-1 without taking into account the tolerance specified in the Table 6.2.2-1;

-MPRc and A-MPRc for serving cell c are specified in subclause 6.2.3G and subclause 6.2.4G, respectively;

-TIB,c, TC,c, TProSe and P-MPRc are specified in subclause 6.2.5

-PRegulatory,c= 10 - Gpost connector dBm when the V2X UE is within the protected zone [13] of CEN DSRC tolling system and operating in Band 47; PRegulatory,c= 33 - Gpost connector dBm otherwise.

The maximum output power PCMAX,PSSCH and PCMAX,PSCCH are derived from PCMAX,c based on the PSD offset following subclause 14.1.1.5 in [6]. For all cases, the PSD difference between PSCCH and PSSCH shall be the same as the PSD offset value.

For the measured configured maximum output power PUMAX,c for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions, the same requirement as in subclause 6.2.5 shall be applied.

When a UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the UE is allowed to set its configured maximum output power PCMAX,c,E-UTRA and PCMAX,c,V2X for the configured E-UTRA uplink carrier and the configured E-UTRA V2X carrier, respectively, and its total configured maximum output power PCMAX,c. The TIB,c of PCMAX,c,E-UTRA is specified in Table 6.2.5G-1.

The configured maximum output power PCMAX c,E-UTRA(p) in subframe p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L,c,E-UTRA (p) ≤  PCMAX,c,E-UTRA (p) ≤  PCMAX_H,c,E-UTRA (p)

where PCMAX_L,c,E-UTRA and PCMAX_H,c,E-UTRA are the limits for a serving cell c as specified in subclause 6.2.5.

The configured maximum output power PCMAX c,V2X (q) in subframe q for the configured E-UTRA V2X carrier shall be set within the bounds:

PCMAX,c,V2X (q) ≤  PCMAX_H,c,V2X (q)

where PCMAX_H,c,V2X is the limit as specified in subclause 6.2.5G.

The total UE configured maximum output power PCMAX (p,q) in a subframe p of an E-UTRA uplink carrier and a subframe q of an E-UTRA V2X sidelink that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L (p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) =  PCMAX_L,c,E-UTRA (p)

PCMAX_H (p,q) = 10 log10 [pCMAX_H,c,E-UTRA (p) + pCMAX_H,c,V2X (q)]

where pCMAX_H,c,V2X and pCMAX_H,c,E-UTRA are the limits PCMAX_H,c,V2X (q) and PCMAX_H,c,E-UTRA (p) expressed in linear scale.

The measured total maximum output power PUMAX over both the E-UTRA uplink and E-UTRA V2X carriers is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,V2X],

where pUMAX,c,E-UTRA  denotes the measured output power of serving cell c for the configured E-UTRA uplink carrier, and pUMAX,c,V2X  denotes the measured output power for the configured E-UTRA V2X carrier expressed in linear scale.

When a UE is configured for synchronous V2X sidelink and uplink transmissions,

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5G-2. PCMAX_L may be modified for any overlapping portion of subframes (p, q) and (p +1, q+1).

When a UE is configured for asynchronous V2X and uplink transmissions, the subframe p for the E-UTRA uplink carrier and subframe q for the E-UTRA V2X carrier overlap in time and

1.if uplink carrier leads in time over q and V2X UE sidelink transmission has SCI whose “Priority” field is set to a value less than the high layer parameter thresSL-TxPrioritization,  then p is the reference subframe and the (p,q) and (p,q-1) pairs are considered for determining the PCMAX tolerance

2.if uplink carrier leads in time over q and V2X UE sidelink transmission has SCI whose “Priority” field is set to a value larger than the high layer parameter thresSL-TxPrioritization,  then q is the reference subframe and the (p,q) and (p+1,q) pairs are considered for determining the PCMAX tolerance

3.if V2X carrier leads in time over p and V2X UE sidelink transmission has SCI whose “Priority” field is set to a value less than the high layer parameter thresSL-TxPrioritization, then p is the reference subframe and the (p,q) and (p,q+1) pairs are considered for determining the PCMAX tolerance

4.if V2X carrier leads in time over p and V2X UE sidelink transmission has SCI whose “Priority” field is set to a value larger than the high layer parameter thresSL-TxPrioritization,, then q is the reference subframe and the (p-1,q) and (p,q) pairs are considered for determining the PCMAX tolerance

For the reference subframe p duration when uplink carrier leads:

P'CMAX_L   = PCMAX_L,,cE-UTRA (p)

P'CMAX_H  = MAX {PCMAX_H   (p,q-1) , PCMAX_H  (p,q)}

For the reference subframe p duration when V2X carrier leads:

P'CMAX_L   = PCMAX_L,c,E-UTRA (p)

P'CMAX_H  = MAX {PCMAX_H   (p,q) , PCMAX_H  (p,q+1)}

For the reference subframe q duration when uplink carrier leads:

P'CMAX_L   = PCMAX_L,c, E-UTRA (q)

P'CMAX_H  = MAX {PCMAX_H   (p,q) , PCMAX_H  (p+1,q)}

For the reference subframe q duration when V2X carrier leads:

P'CMAX_L   = PCMAX_L,c, E-UTRA (p)

P'CMAX_H  = MAX {PCMAX_H   (p-1,q) , PCMAX_H  (p,q)}

where PCMAX_L,,cE-UTRA (p) and PCMAX_H are the applicable limits for each overlapping subframe pairs above 4case with (p,q), (p, q-1) or (p,q), (p, q+1) or (p,q), (p+1,q) or (p,q), (p-1, q). The measured total configured maximum output power PUMAX shall be within the following bounds:

P’CMAX_L   –  TLOW (P’CMAX_L)  ≤  PUMAX  ≤  P’CMAX_H + THIGH (P’CMAX_H)

with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2.5G-2.

For intra-band contiguous multi-carrier operation, MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR specified in subclause 6.2.3G and subclause 6.2.4G respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR. PCMAX,c  is calculated under the assumption that the transmit power is increased by the same amount in dB on all component carriers.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

PCMAX_L  = MIN{10 log10 ∑ pEMAX,c  - TC , PPowerClass – MAX(MPR + A-MPR + ΔTIB,c + TC + TProSe, P-MPR ), PRegulatory }

PCMAX_H  = MIN{10 log10 ∑ pEMAX,c , PPowerClass, PRegulatory }

where

-pEMAX,c is the linear value of PEMAX,c which is given by IE maxTxPower in [7];

-PPowerClass is the maximum UE power specified in Table 6.2.2G-1 without taking into account the tolerance specified in the Table 6.2.2G-1;

-MPR and A-MPR are specified in subclause 6.2.3G and subclause 6.2.4G respectively;

-TIB,c is the additional tolerance for serving cell c as specified in Table 6.2.5-2;

-P-MPR is the power management term for the UE;

-TC is the highest value TC,c among all serving cells c in the subframe over both timeslots. TC,c = 1.5 dB when NOTE 2 in Table 6.2.2-1 applies, otherwise TC,c = 0 dB;

- TProSe applies as specified in subclause 6.2.5.

-PRegulatory= 10 - Gpost connector dBm when V2X UE is within the protected zone [13] of CEN DSRC tolling system and operating in Band 47; PRegulatory= 33 - Gpost connector dBm otherwise.

NOTE:The supported post antenna connector gain Gpost connector declared by the UE following the principle described in annex I.

Table 6.2.5G-1: ΔTIB,c for inter-band concurrent V2X operation (two bands)

For V2X UE supporting Transmit Diversity, the transmitted power is configured per each UE.

If the UE transmits on two antenna connectors at the same time, the tolerance is specified in Table 6.2.5G-2 and 6.2.5G-3 for PC2 and PC3 V2X UE respectively.

Table 6.2.5G-2: PCMAX,c tolerance in Transmit Diversity scheme for PC2 V2X UE

Table 6.2.5G-3: PCMAX,c tolerance in Transmit Diversity scheme for PC3 V2X UE

If the UE transmits on one antenna connector at a time, the requirements in Table 6.2.5-1 apply to the active antenna connector.

## 6.2.5KConfigured transmitted power for Aerial UE

For the Aerial UE, the requirements in clause 6.2.5 apply with the following modifications:

only requirements related to Power Class 3 UEs are applicable for Aerial UEs. In the current Release Aerial UEs that are not PC3 are not considered; and

when NS-PmaxListAerial is configured for the applicable operating band, the UE shall not consider the value of the additionalPmax in the NS-PmaxList IE. In such case, the value of additionalPmax to be considered is the one related to NS-PmaxListAerial, when configured, according to TS 36.331[7]; and

when determining the parameters in the formulas used to calculate the UE configured transmitted power, use clauses 6.2.3K and 6.2.4K in substituion to clauses 6.2.3 and 6.2.4, when UE is configured with NR-NS-PmaxValueAerial.for the operating band

Note: when UE is not configured with NS-PmaxListAerial for the operating band, the UE shall use the values of the additionalPmax in the NS-PmaxList IE, if configured, as described in clause 6.2.5

## 6.3Output power dynamics

## 6.3.1(Void)

## 6.3.2Minimum output power

The minimum controlled output power of the UE is defined as the broadband transmit power of the UE, i.e. the power in the channel bandwidth for all transmit bandwidth configurations (resource blocks), when the power is set to a minimum value.

## 6.3.2.1Minimum requirement

The minimum output power is defined as the mean power in one sub-frame (1ms). The minimum output power shall not exceed the values specified in Table 6.3.2.1-1.

Table 6.3.2.1-1: Minimum output power

## 6.3.2AUE Minimum output power for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands and intra-band contiguous and non-contiguous carrier aggregation, the minimum controlled output power of the UE is defined as the transmit power of the UE per component carrier, i.e., the power in the channel bandwidth of each component carrier for all transmit bandwidth configurations (resource blocks), when the power on both component carriers are set to a minimum value.

## 6.3.2A.1Minimum requirement for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the minimum output power is defined per carrier and the requirement is specified in subclause 6.3.2.1. If two contiguous component carriers are assigned to one E-UTRA band, the requirements in subclause 6.3.2A.1 apply for those component carriers.

For intra-band contiguous and non-contiguous carrier aggregation the minimum output power is defined as the mean power in one sub-frame (1ms). The minimum output power shall not exceed the values specified in Table 6.3.2A.1-1.

Table 6.3.2A.1-1: Minimum output power for intra-band contiguous and non-contiguous CA UE

## 6.3.2BUE Minimum output power for UL-MIMO

For UE supporting UL-MIMO, the minimum controlled output power is defined as the broadband transmit power of the UE, i.e. the sum of the power in the channel bandwidth for all transmit bandwidth configurations (resource blocks) at each transmit antenna connector, when the UE power is set to a minimum value.

## 6.3.2B.1Minimum requirement

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the minimum output power is defined as the sum of the mean power at each transmit connector in one sub-frame (1ms). The minimum output power shall not exceed the values specified in Table 6.3.2B.1-1.

Table 6.3.2B.1-1: Minimum output power

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.3.2 apply.

## 6.3.2CVoid

<reserved for future use>

## 6.3.2DUE Minimum output power for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the requirements in subclause 6.3.2 apply for ProSe transmission.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.3.2A apply as specified for the corresponding inter-band aggregation with uplink assigned to two bands.

## 6.3.2FUE Minimum output power for category NB1 and NB2

For category NB1 and NB2 UE the single-tone and multi-tone transmission minimum output power requirement for the channel bandwidth is -40 dBm. For 3.75kHz sub-carrier spacing the minimum output power is defined as mean power in one slot (2ms) excluding the 2304Ts gap when UE is not transmitting. For 15kHz sub-carrier spacing the minimum output power is defined as mean power in one sub-frame (1ms).

## 6.3.2GUE Minimum output power for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the minimum output power shall not exceed the values specified in Table 6.3.2G-1.

Table 6.3.2G-1: Minimum output power

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements specified in subclause 6.3.2 shall apply for the uplink and the requirements specified in subclause 6.3.2G shall apply for the sidelink.

For intra-band contiguous E-UTRA V2X multiple carrier transmissions, the requirements specified in subclause 6.3.2G shall apply for each sidelink carrier.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the minimum output power is defined as the sum of the mean power at each transmit connector in one sub-frame (1ms). The minimum output power shall not exceed the values specified for single carrier.

If the UE transmits on aone antenna connector at a time, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.3.3Transmit OFF power

Transmit OFF power is defined as the mean power when the transmitter is OFF. The transmitter is considered to be OFF when the UE is not allowed to transmit or during periods when the UE is not transmitting a sub-frame. During DTX and measurements gaps, the UE is not considered to be OFF.

## 6.3.3.1.Minimum requirement

The transmit OFF power is defined as the mean power in a duration of at least one sub-frame (1ms) excluding any transient periods. The transmit OFF power shall not exceed the values specified in Table 6.3.3.1-1.

Table 6.3.3.1-1: Transmit OFF power

## 6.3.3AUE Transmit OFF power for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands and intra-band contiguous and non-contiguous carrier aggregation, transmit OFF power is defined as the mean power per component carrier when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit or during periods when the UE is not transmitting a sub-frame. During measurements gaps, the UE is not considered to be OFF.

## 6.3.3A.1Minimum requirement for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, transmit OFF power requirement is defined per carrier and the requirement is specified in subclause 6.3.3.1. If two contiguous component carriers are assigned to one E-UTRA band, the requirements in subclause 6.3.3A.1 apply for those component carriers.

For intra-band contiguous and non-contiguous carrier aggregation the transmit OFF power is defined as the mean power in a duration of at least one sub-frame (1ms) excluding any transient periods. The transmit OFF power shall not exceed the values specified in Table 6.3.3A.1-1.

Table 6.3.3A.1-1: Transmit OFF power for intra-band contiguous and non-contiguos CA UE

## 6.3.3BUE Transmit OFF power for UL-MIMO

For UE supporting UL-MIMO, the transmit OFF power is defined as the mean power at each transmit antenna connector when the transmitter is OFF at all transmit antenna connectors. The transmitter is considered to be OFF when the UE is not allowed to transmit or during periods when the UE is not transmitting a sub-frame. During DTX and measurements gaps, the UE is not considered to be OFF.

## 6.3.3B.1Minimum requirement

The transmit OFF power is defined as the mean power at each transmit antenna connector in a duration of at least one sub-frame (1ms) excluding any transient periods. The transmit OFF power at each transmit antenna connector shall not exceed the values specified in Table 6.3.3B.1-1.

Table 6.3.3B.1-1: Transmit OFF power per antenna port

## 6.3.3DTransmit OFF power for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the Prose UE shall meet the Transmit OFF power at all times when the UE is not associated with a serving cell on the ProSe carrier and does not have knowledge of its geographical area or is provisioned with pre-configured radio parameters that are not associated with any known Geographical Area.

The requirements specified in subclause 6.3.3 shall apply to UE supporting ProSe when

-the UE is associated with a serving cell on the ProSe carrier, or

-the UE is not associated with a serving cell on the ProSe carrier and is provisioned with the preconfigured radio parameters for ProSe Direct Communications and/or ProSe Direct Discovery that are associated with known Geographical Area, or

-the UE is associated with a serving cell on a carrier different than the ProSe carrier, and the radio parameters for ProSe Direct Discovery on the ProSe carrier are provided by the serving cell, or

-the UE is associated with a serving cell on a carrier different than the ProSe carrier, and has a non-serving cell selected on the ProSe carrier that supports ProSe Direct Discovery and/or ProSe Direct Communication.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, transmit OFF power is defined as the mean power per component carrier when the transmitter is OFF on all component carriers. During measurement gaps and transmission/reception gaps for ProSe, the UE is not considered to be OFF. Transmit OFF power requirement as specified in subclause 6.3.3 apply per carrier.

## 6.3.3FTransmit OFF power for category NB1 and NB2

For category NB1 and NB2 UE the transmit OFF power requirement for the channel bandwidth is -50 dBm. For 3.75kHz sub-carrier spacing the transmit OFF power is defined as mean power in one slot (2ms) excluding the 2304Ts gap when UE is not transmitting. For 15kHz sub-carrier spacing the transmit OFF power is defined as mean power in one sub-frame (1ms).

## 6.3.3GTransmit OFF power for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the V2X UE shall meet the Transmit OFF power in subclause 6.3.3D.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.3.3A apply for as specified for the corresponding inter-band concurrent operation with uplink assigned to two bands.

For intra-band contiguous E-UTRA V2X multiple carrier transmissions, the requirements in subclause 6.3.3A apply as specified for the corresponding intra band contiguous carrier aggregation.

The transmit OFF power is defined as the mean power at each transmit antenna connector.

The transmit OFF power at each transmit antenna connector shall not exceed the values specified for single carrier.

## 6.3.4ON/OFF time mask

## 6.3.4.1General ON/OFF time mask

The General ON/OFF time mask defines the observation period between Transmit OFF and ON power and between Transmit ON and OFF power. ON/OFF scenarios include; the beginning or end of DTX, measurement gap, contiguous, and non contiguous transmission

The OFF power measurement period is defined in a duration of at least one subframe, or one slot or one subslot for sTTI, excluding any transient periods. The ON power is defined as the mean power over one subframe, or one slot or one subslot for sTTI, excluding any transient period.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

The transient period length shall be no longer than the specified value in Table 6.3.4.1-1.

Table 6.3.4.1-1: Transient period length depending on transmission length

Figure 6.3.4.1-1: General ON/OFF time mask for subframe TTI and for Frame Structure Type 1 and Frame Structure Type 2

For Frame Structure Type 3 the general ON/OFF mask is specified in 6.3.4.1-1A with the PUSCH starting position modified by relative to the start of the sub-frame as indicated in the associated DCI, where and the basic time unit are specified in [4]. At the end of the sub-frame  and  with  denoting the duration of the last SC-FDMA symbol when the bit indicating the PUSCH ending symbol in the associated DCI has value ‘0’ and ‘1’ as specified in [5], respectively; the OFF power requirement applies 5 s after the end of the last symbol transmitted.

Figure 6.3.4.1-1A: General ON/OFF time mask for subframe TTI and for Frame Structure Type 3

Figure 6.3.4.1-1B: General ON/OFF time mask for sTTI and for Frame Structure Type 1 and Frame Structure Type 2

## 6.3.4.2PRACH and SRS time mask

## 6.3.4.2.1PRACH time mask

The PRACH ON power is specified as the mean power over the PRACH measurement period excluding any transient periods as shown in Figure 6.3.4.2-1. The measurement period for different PRACH preamble format is specified in Table 6.3.4.2-1.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Table 6.3.4.2-1: PRACH ON power measurement period

Figure 6.3.4.2-1: PRACH ON/OFF time mask

## 6.3.4.2.2SRS time mask

In the case a single SRS transmission, the ON power is defined as the mean power over the symbol duration excluding any transient period; Figure 6.3.4.2.2-1 and Figure 6.3.4.2.2-1A.

In the case a dual SRS transmission, the ON power is defined as the mean power for each symbol duration excluding any transient period. Figure 6.3.4.2.2-2

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Figure 6.3.4.2.2-1: Single SRS time mask for Frame Structure Type 1 and Frame Structure Type 2

For Frame Structure Type 3 and single SRS transmission, the SRS time mask is specified in 6.3.4.2-2A; the OFF power requirement applies [5] s after the end of the SRS symbol.

Figure 6.3.4.2.2-1A: Single SRS time mask for Frame Structure Type 3

Figure 6.3.4.2.2-2: Dual SRS time mask for the case of UpPTS transmissions

For SRS transmission mapped to two or more OFDM symbols the ON power is defined as the mean power for each symbol duration excluding any transient period. For consecutive SRS transmissions without power change, Figure 6.3.4.2.2-3 applies.

SRSEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement on consecutive symbols20µs Transient periodSRSSRSSRS20µs Transient periodSRSEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement on consecutive symbols20µs Transient periodSRSSRSSRS20µs Transient period

Figure 6.3.4.2.2-3: Consecutive SRS time mask for the case when no power change is required

When power change between consecutive SRS transmissions is required, then Figure 6.3.4.2.2-4 and Figure 6.3.4.2.2-5 apply.

SRSSRS ON power requirement SRSSRS20µs20µs20µsSRSEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement SRS ON power requirement SRS ON power requirement 20µs Transient period20µs Transient period20µs Transient period20µs Transient period20µs Transient periodSRSSRS ON power requirement SRSSRS20µs20µs20µsSRSEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement SRS ON power requirement SRS ON power requirement 20µs Transient period20µs Transient period20µs Transient period20µs Transient period20µs Transient period

Figure 6.3.4.2.2-4: Consecutive SRS time mask for the case when power change is required

SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRSAnt. ‘x’SRS ON power requirement 20µs20µs20µsEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement SRS ON power requirement SRS ON power requirement 20µs Transient period20µs Transient period20µs Transient period20µs Transient period20µs Transient periodSRSAnt. ‘x’SRSAnt. ‘y’SRSAnt. ‘x’SRSAnt. ‘x’SRS ON power requirement 20µs20µs20µsEnd of OFF powerrequirement Start of OFF power requirementSRS ON power requirement SRS ON power requirement SRS ON power requirement 20µs Transient period20µs Transient period20µs Transient period20µs Transient period20µs Transient periodSRSAnt. ‘x’SRSAnt. ‘y’SRSAnt. ‘x’SRSAnt. ‘x’

Figure 6.3.4.2.2-5: Time mask for SRS antenna switching

The above transient period applies to all the transmit CCs in CA with the CC sounding SRS. UE RF requirements do not apply during this transient period.

## 6.3.4.3Slot / Sub frame boundary time mask for subframe TTI

The sub frame boundary time mask defines the observation period between the previous/subsequent sub–frame and the (reference) sub-frame. A transient period at a slot boundary within a sub-frame is only allowed in the case of Intra-sub frame frequency hopping. For the cases when the subframe contains SRS the time masks in subclause 6.3.4.4 apply.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Figure 6.3.4.3-1: Transmission power template for Frame Structure Type 1 and Frame Structure Type 2

For Frame Structure Type 3 the sub-frame boundary time mask is specified in Figure 6.3.4.3-1A when the bit indicating the PUSCH ending symbol in the associated DCI has value ‘1’ and the PUSCH starting position is modified by  in the following subframe (clause 6.3.4.1);  denotes the duration of the ending SC-FDMA symbol. the OFF power requirement applies 5 s after the end of the last symbol transmitted.

Figure 6.3.4.3-1A: Transmission power template when the bit in the associated DCI indcating the PUSCH ending symbol has value ‘1' for Frame Structure Type 3

For Frame Structure Type 3 the first slot boundary time mask is specified in Figure 6.3.4.3-1B when the PUSCH mode is 3 indicated in DCI [4]. The PUSCH starting position modified by relative to the start of the sub-frame as indicated in the associated DCI, where and the basic time unit are specified in TS 36.211 [4]. At the end of the first slot  or  with  denoting the duration of one SC-FDMA symbol when the bit indicating the PUSCH ending symbol in the associated DCI is either fourth or seventh symbol  as specified in TS 36.212 [5], respectively; the OFF power requirement applies 5 s after the end of the last symbol transmitted.tend=3∙Tsymb tend=0

Figure 6.3.4.3-1B: Transmission power template for the first slot in one subframe for Frame Structure Type 3

For Frame Structure Type 3 the second slot boundary time mask is specified in Figure 6.3.4.3-1C when the PUSCH mode is 2 indicated in DCI [4]. The PUSCH starting position modified by relative to the start of the second slot as indicated in the associated DCI, where and the basic time unit are specified in TS 36.211 [4]. At the end of the second slot   or  with  denoting the duration of one SC-FDMA symbol when the bit indicating the PUSCH ending symbol in the associated DCI is either thirteenth or fourteenth symbol  as specified in TS 36.212 [5], respectively; the OFF power requirement applies 5 s after the end of the last symbol transmitted.tend=Tsymb tend=0

For Frame Structure Type 3 the second slot boundary time mask specified in Figure 6.3.4.3-1C can also be applied  when the PUSCH mode is 1 indicated in DCI [4] and transmition starts at the eighth symbol. The PUSCH starting position  relative to the start of the second slot. At the end of the second slot   or   with  denoting the duration of one SC-FDMA symbol when the bit indicating the PUSCH ending symbol in the associated DCI is either thirteenth or fourteenth symbol as specified in TS 36.212 [5], respectively; the OFF power requirement applies 5 s after the end of the last symbol transmitted.tD=0tend=Tsymb tend=0

Figure 6.3.4.3-1C: Transmission power template for the second slot in one subframe for Frame Structure Type 3

## 6.3.4.4PUCCH / PUSCH / SRS time mask for subframe TTI

The PUCCH/PUSCH/SRS time mask defines the observation period between sounding reference symbol (SRS) and an adjacent PUSCH/PUCCH symbol and subsequent sub-frame. The time masks apply for all types of frame structures and their allowed PUCCH/PUSCH/SRS transmissions unless otherwise stated.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Figure 6.3.4.4-1: PUCCH/PUSCH/SRS time mask when there is a transmission before SRS but not after for Frame Structure Type 1 and Frame Structure Type 2

For Frame Structure Type 3 the PUSCH/SRS time mask when there is a transmission before SRS but not after is specified in Figure 6.3.4.4-1A; the OFF power requirement applies 5 s after the end of the last symbol transmitted.

Figure 6.3.4.4-1A: PUSCH/SRS time mask when there is a transmission before SRS but not after for Frame Structure Type 3

Figure 6.3.4.4-2: PUCCH/PUSCH/SRS time mask when there is transmission before and after SRS

Figure 6.3.4.4-3: PUCCH/PUSCH/SRS time mask when there is a transmission after SRS but not before

Figure 6.3.4.4-4: SRS time mask when there is FDD SRS blanking for Frame Structure Type 1 and Frame Structure Type 2

For Frame Structure Type 3 the PUSCH/SRS time mask with transmission after the SRS symbol and the PUSCH starting position modified by  in the following subframe (clause 6.3.4.1) is specified in Figure 6.3.4.4-4A when there is SRS blanking.

Figure 6.3.4.4-4A: SRS time mask when there is SRS blanking for Frame Structure Type 3

## 6.3.4.5Symbol / Subslot boundary time mask for subslot TTI

The subslot boundary time mask defines the observation period between the previous/subsequent subslot and the (reference) subslot. A transient period at a symbol boundary within a subslot is only allowed in the case of Intra-subslot frequency hopping. For the cases when the subslot contains SRS the time masks in subclause 6.3.4.6 apply.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Following time masks requirements shall be applied:

-the transient period shall be equally shared between  two consecutive Reference symbols or Data symbols (figure 6.3.4.5-1 and figure 6.3.4.5-4).

-Otherwise, the transient period shall be placed in the Reference symbol (figure 6.3.4.5-2 and figure 6.3.4.5-3).

Figure 6.3.4.5-1: Transmission power template for subslot TTI – transient period shared

Figure 6.3.4.5-2: Transmission power template for subslot TTI – transient period not shared

Figure 6.3.4.5-3: Transmission power template for subslot TTI – transient period not shared

Figure 6.3.4.5-4: Transmission power template for subslot TTI – transient period shared

## 6.3.4.6Subslot PUCCH / subslot PUSCH / SRS time mask for subslot TTI

The subslot PUCCH/subslot PUSCH/SRS time mask defines the observation period between sounding reference symbol (SRS) in the last symbol in subslot N and an adjacent subslot PUSCH/subslot PUCCH symbol in subslot N+1.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Following time masks requirement shall be applied when SRS is either transmitted or blanked:

-the transient period shall be placed in Reference symbol when the transient is in between Reference symbol and SRS (figure 6.3.4.6-1, figure 6.3.4.6-2, figure 6.3.4.6-5 and figure 6.3.4.6-7).

-the transient period shall be equally shared when the transien is in between  Data symbol and SRS (figure 6.3.4.6-3 and figure 6.3.4.6-4).

Figure 6.3.4.6-1: subslot PUSCH/SRS time mask when there is a Reference symbol before SRS (or SRS blanking) and data symbol after

Figure 6.3.4.6-2:subslot PUSCH/SRS time mask when there is a Reference symbol before SRS (or SRS blanking) and Reference symbol after

Figure 6.3.4.6-3: subslot PUSCH/SRS time mask when there is a data symbol before SRS (or SRS blanking) and data symbol after

Figure 6.3.4.6-4: subslot PUSCH/SRS time mask when there is a data symbol before SRS (or SRS blanking) and Reference symbol after

Figure 6.3.4.6-5: subslot PUSCH/SRS time mask when there is a no symbol before SRS

Figure 6.3.4.6-6: subslot PUSCH/SRS time mask when there is a no symbol after SRS

Figure 6.3.4.6-7: subslot PUSCH/SRS time mask when there is a no symbol before and after SRS

## 6.3.4.7Symbol / Slot boundary time mask for slot TTI

The slot boundary time mask defines the observation period between the previous/subsequent slot and the (reference) slot. A transient period at a symbol boundary within a slot is only allowed in the case of Intra slot frequency hopping. For the cases when the slot contains SRS the time masks in subclause 6.3.4.8 shall apply.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

For slot boundary, the time maks specified in subclause 6.3.4.4 shall apply with a transient time of 10µs intead of 20µs.

For frequency hopping within the slot, the time masks specified in subclause 6.3.4.5 shall apply.

## 6.3.4.8Slot PUCCH / slot PUSCH / SRS time mask for slot TTI

The slot PUCCH/slot PUSCH/SRS time mask defines the observation period between sounding reference symbol (SRS) and an adjacent slot PUSCH/slot PUCCH symbol and subsequent slot.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

The time masks specified in subclause 6.3.4.4 shall apply.

## 6.3.4.9Consecutive subslot and slot TTI or consecutive subslot and subframe TTI  time mask

The consecutive subslot and slot boundary time mask or consecutive subslot and subframe boundary time mask defines the observation period between the subslot and the slot or subframe.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3.

In this case, the transient period shall be placed in the subframe TTI or the slot TTI (figure 6.3.4.9-1)

Figure 6.3.4.9-1: subslot TTI and subframe TTI boundary

## 6.3.4.10Consecutive subframe and subslot TTI or consecutive slot and subslot TTI time mask

The consecutive subframe and subslot boundary time mask or consecutive slot and subslot boundary time mask defines the observation period between the slot or subframe and the subslot.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

Figure 6.3.4.10-1: Subframe TTI and subslot TTI boundary with SRS in last subframe TTI symbol and Reference Symbol in first subslot TTI symbol

Figure 6.3.4.10-2: Subframe TTI and subslot TTI boundary with SRS in last subframe TTI symbol and data Symbol in first subslot TTI symbol

When the last symbol of the Subframe or slot is not SRS then the transient period is placed in the Subframe or Slot.

Figure 6.3.4.10-3: subframe TTI and subslot TTI boundary

## 6.3.4.11Consecutive TTI and slot TTI or consecutive slot TTI and TTI time mask

The consecutive subframe and slot boundary time mask or consecutive slot and subframe boundary time mask defines the observation period between the subframe and the slot or the slot and the subframe.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3

The time masks at subframe boundary specified in subclause 6.3.4.3 or at slot boundary specified in subclause 6.3.4.7 shall apply.

## 6.3.4AON/OFF time mask for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands and intra-band contiguous and non-contiguous carrier aggregation, the general output power ON/OFF time mask specified in subclause 6.3.4.1 is applicable for each component carrier during the ON power period and the transient periods. The OFF period as specified in subclause 6.3.4.1 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3.4BON/OFF time mask for UL-MIMO

For UE supporting UL-MIMO, the ON/OFF time mask requirements in subclause 6.3.4 apply at each transmit antenna connector.

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the general ON/OFF time mask requirements specified in subclause 6.3.4.1 apply to each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.3.4 apply.

## 6.3.4DON/OFF time mask for ProSe

For ProSe Direct Discovery and ProSe Direct Communications, additional requirements on ON/OFF time masks for ProSe physical channels and signals are specified in this clause.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.3.4D apply for ProSe transmission and the requirements in subclause 6.3.4 apply for uplink transmission.

## 6.3.4D.1General time mask for ProSe

The General ON/OFF time mask defines the observation period between the Transmit OFF and ON power and between Transmit ON and OFF power for PSDCH, PSCCH, and PSSCH transmissions in a subframe wherein the last symbol is punctured to create a guard period.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3.

Figure 6.3.4D.1-1: PSDCH/PSCCH/PSSCH time mask

## 6.3.4D.2PSSS/SSSS time mask

The PSSS time mask / SSSS time mask defines the observation period between the Transmit OFF and ON power and between Transmit ON and OFF power for PSSS/SSSS transmissions in a subframe when not multiplexed with PSBCH in that subframe.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3.

Figure 6.3.4D.2-1: PSSS time mask for normal CP transmission (when not time-multiplexed with PSBCH)

Figure 6.3.4D.2-2: PSSS time mask for extended CP transmission (when not time-multiplexed with PSBCH)

Figure 6.3.4D.2-3: SSSS time mask (when not time-multiplexed with PSBCH)

## 6.3.4D.3PSSS / SSSS / PSBCH time mask

The PSSS/SSSS/PSBCH time mask defines the observation period between SSSS and adjacent PSSS/PSBCH symbols in a subframe, with last symbol punctured to create a guard period.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3.

Figure 6.3.4D.3-1: PSSS/SSSS/PBCH time mask for normal CP transmission

Figure 6.3.4D.3-2: PSSS/SSSS/PBCH time mask for extended CP transmission

## 6.3.4D.4PSSCH / SRS time mask

The PSSCH/SRS time mask defines the observation period between sounding reference symbol (SRS) and an adjacent PSSCH symbol and subsequent sub-frame.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2 and subclause 6.6.2.3.

The PSSCH/SRS time mask shall follow the PUSCH/PUCCH/SRS time mask as specified in subclause 6.3.4.4.

## 6.3.4FON/OFF time mask for category NB1 and NB2

## 6.3.4F.1General ON/OFF time mask

E-UTRA general ON/OFF time mask in subclause 6.3.4.1 applies for category NB1 and NB2 UE with an exception that for 3.75kHz sub-carrier spacing the transmit OFF power is defined as mean power in one slot (2ms) and for 15kHz sub-carrier spacing the transmit OFF power is defined as mean power in one sub-frame (1ms), excluding any transient periods. The ON power is defined as the mean power over one RU excluding any transient periods.

## 6.3.4F.2NPRACH time mask

The NPRACH ON power is specified as the mean power over the NPRACH measurement period excluding any transient periods as shown in Figure 6.3.4F.2-1. The measurement period for different NPRACH preamble format is specified in Table 6.3.4F.2-1.

There are no additional requirements on UE transmit power beyond that which is required in subclause 6.2.2F and subclause 6.6.2.3F.

Table 6.3.4F.2-1: NPRACH ON power measurement period

Figure 6.3.4F.2-1: NPRACH ON/OFF time mask

## 6.3.4GON/OFF time mask for V2X Communication

For V2X Communications, additional requirements on ON/OFF time masks for V2X physical channels and signals are specified in this clause.

The General ON/OFF time mask in subclause 6.3.4D.1 and PSSS/SSSS time mask in subcluse 6.3.4D.2 are applied for E-UTRA V2X sidelink UE.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.3.4G apply for the V2X sidelink transmission and the requirements in subclause 6.3.4 apply for the E-UTRA uplink transmission.

For intra-band contiguous multi-carrier operation the general ON/OFF time mask is applicable for each component carrier during the ON power period and the transient periods. The OFF period shall only be applicable for each component carrier when all the component carriers are OFF.

For V2X UE supporting Transmit Diversity, the ON/OFF time mask requirements apply at each transmit antenna connector.

If the UE transmits on two antenna connectorsat the same time, the general ON/OFF time mask requirements apply to each transmit antenna connector.

If the UE transmits on one antenna connector at a time, the general ON/OFF time mask requirements apply to the active antenna connector.

## 6.3.4G.1PSSS / SSSS / PSBCH time mask

The PSSS/SSSS/PSBCH time mask for V2X UE defines the observation period between SSSS and adjacent PSSS/PSBCH symbols in a subframe, with last symbol punctured to create a guard period.

Figure 6.3.4G.1-1: PSSS/SSSS/PSBCH time mask for normal CP transmission for V2X Service

Figure 6.3.4G.1-2: PSSS/SSSS/PSBCH time mask for extended CP transmission for V2X Service

## 6.3.5Power Control

## 6.3.5.1Absolute power tolerance

Absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame at the start of a contiguous transmission or non-contiguous transmission with a transmission gap larger than 20ms. This tolerance includes the channel estimation error (the absolute RSRP accuracy requirement specified in subclause 9.1 of TS 36.133). In the case of a PRACH transmission, the absolute tolerance is specified for the first preamble. The absolute power tolerance includes the channel estimation error (the absolute RSRP accuracy requirement specified in subclause 9.1 of TS 36.133).

## 6.3.5.1.1Minimum requirements

The minimum requirement for absolute power tolerance is given in Table 6.3.5.1.1-1 over the power range bounded by the Maximum output power as defined in subclause 6.2.2 and the Minimum output power as defined in subclause 6.3.2.

For operating bands under NOTE 2 in Table 6.2.2-1, the absolute power tolerance as specified in Table 6.3.5.1.1-1 is relaxed by reducing the lower limit by 1.5 dB when the transmission bandwidth is confined within FUL_low and FUL_low + 4 MHz or FUL_high – 4 MHz and FUL_high.

Table 6.3.5.1.1-1: Absolute power tolerance

## 6.3.5.2Relative Power tolerance

The relative power tolerance is the ability of the UE transmitter to set its output power in a target sub-frame relatively to the power of the most recently transmitted reference sub-frame if the transmission gap between these sub-frames is ≤ 20 ms.

For PRACH transmission, the relative tolerance is the ability of the UE transmitter to set its output power relatively to the power of the most recently transmitted preamble. The measurement period for the PRACH preamble is specified in Table 6.3.4.2-1.

## 6.3.5.2.1Minimum requirements

The requirements specified in Table 6.3.5.2.1-1 apply when the power of the target and reference sub-frames are within the power range bounded by the Minimum output power as defined in subclause 6.3.2 and the measured PUMAX as defined in subclause 6.2.5 (i.e, the actual power as would be measured assuming no measurement error). This power shall be within the power limits specified in subclause 6.2.5.

To account for RF Power amplifier mode changes 2 exceptions are allowed for each of two test patterns. The test patterns are a monotonically increasing power sweep and a monotonically decreasing power sweep over a range bounded by the requirements of minimum power and maximum power specified in subclauses 6.3.2 and 6.2.2. For these exceptions the power tolerance limit is a maximum of ±6.0 dB in Table 6.3.5.2.1-1

Table 6.3.5.2.1-1 Relative power tolerance for transmission (normal conditions)

The power step (ΔP) is defined as the difference in the calculated setting of the UE Transmit power between the target and reference sub-frames with the power setting according to subclause 5.1 of [TS 36.213]. The error is the difference between ΔP and the power change measured at the UE antenna port with the power of the cell-specific reference signals kept constant. The error shall be less than the relative power tolerance specified in Table 6.3.5.2.1-1.

For sub-frames not containing an SRS symbol, the power change is defined as the relative power difference between the mean power of the original reference sub-frame and the mean power of the target subframe not including transient durations. The mean power of successive sub-frames shall be calculated according to Figure 6.3.4.3-1 and Figure 6.3.4.1-1 if there is a transmission gap between the reference and target sub-frames.

If at least one of the sub-frames contains an SRS symbol, the power change is defined as the relative power difference between the mean power of the last transmission within the reference sub-frame and the mean power of the first transmission within the target sub-frame not including transient durations. A transmission is defined as PUSCH, PUCCH or an SRS symbol. The mean power of the reference and target sub-frames shall be calculated according to Figures 6.3.4.1-1, 6.3.4.2-1, 6.3.4.4-1, 6.3.4.4-2 and 6.3.4.4-3 for these cases.

## 6.3.5.3Aggregate power control tolerance

Aggregate power control tolerance is the ability of a UE to maintain its power in non-contiguous transmission within 21 ms in response to 0 dB TPC commands with respect to the first UE transmission, when the power control parameters specified in TS 36.213 are constant. For HD-FDD UEs that support coverage enhancement (CE), the requirements on aggregate power control tolerance in 6.3.5E.3 apply.

## 6.3.5.3.1Minimum requirement

The UE shall meet the requirements specified in Table 6.3.5.3.1-1 for aggregate power control over the power range bounded by the minimum output power as defined in subclause 6.3.2 and the maximum output power as defined in subclause 6.2.2.

Table 6.3.5.3.1-1: Aggregate power control tolerance

## 6.3.5APower control for CA

The requirements apply for one single PUCCH, PUSCH or SRS transmission of contiguous PRB allocation per component carrier with power setting in accordance with Clause 5.1 of [6].

## 6.3.5A.1Absolute power tolerance

The absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame at the start of a contiguous transmission or non-contiguous transmission with a transmission gap on each active component carriers larger than 20ms. For component carriers with Frame Structure Type 3 the absolute power toerlance requirements apply when the said transmission gaps are larger than 40 ms. The requirement can be tested by time aligning any transmission gaps on the component carriers.

When SRS carrier based switching is used, then the above mentioned absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame at the start of a contiguous transmission or non-contiguous transmission with a transmission gap on component carriers (to which SRS switching occurs) larger than 40ms.

## 6.3.5A.1.1Minimum requirements

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the absolute power control tolerance is specified on each component carrier exceed the minimum output power as defined in subclause 6.3.2A and the total power is limited by maximum output power as defined in subclause 6.2.2A. The requirements defined in Table 6.3.5.1.1-1 shall apply on each component carrier with all component carriers active. The requirements can be tested by time aligning any transmission gaps on all the component carriers.

For intra-band contiguous carrier aggregation bandwidth class B, C and D and intra-band non-contiguous carrier aggregation the absolute power control tolerance per component carrier is given in Table 6.3.5.1.1-1.

## 6.3.5A.2Relative power tolerance

## 6.3.5A.2.1Minimum requirements

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the relative power tolerance is specified when the power of the target and reference sub-frames on each component carrier exceed the minimum output power as defined in subclause 6.3.2A and the total power is limited by PUMAX as defined in subclause 6.2.5A. The requirements shall apply on each component carrier with all component carriers active. The UE transmitter shall have the capability of changing the output power independently on all component carriers in the uplink and:

a)the requirements for all combinations of PUSCH and PUCCH transitions per component carrier is given in Table 6.3.5.2.1-1.

b)for SRS the requirements for combinations of PUSCH/PUCCH and SRS transitions between subframes given in Table 6.3.5.2.1-1 apply per component carrier when the target and reference subframes are configured for either simultaneous SRS or simultaneous PUSCH.

c)for RACH the requirements apply for the primary cell and are given in Table 6.3.5.2.1-1.

For component carriers with Frame Structure Type 3 the requirements for the target sub-frame relative to the power of the most recently transmitted reference sub-frame shall be met with a transmission gap ≤ 40 ms.

For intra-band contiguous carrier aggregation bandwidth class B, C and D and intra-band non-contiguous carrier aggregation, the requirements apply when the power of the target and reference sub-frames on each component carrier exceed -20 dBm and the total power is limited by PUMAX as defined in subclause 6.2.5A. For the purpose of these requirements, the power in each component carrier is specified over only the transmitted resource blocks.

The UE shall meet the following requirements for transmission on both assigned component carriers when the average transmit power per PRB is aligned across both assigned carriers in the reference sub-frame:

a)for all possible combinations of PUSCH and PUCCH transitions per component carrier, the corresponding requirements given in Table 6.3.5.2.1-1;

b)for SRS transitions on each component carrier, the requirements for combinations of PUSCH/PUCCH and SRS transitions given in Table 6.3.5.2.1-1 with simultaneous SRS of constant SRS bandwidth allocated in the target and reference subrames;

c)for RACH on the primary component carrier, the requirements given in Table 6.3.5.2.1-1 for PRACH.

For a) and b) above, the power step P between the reference and target subframes shall be set by a TPC command and/or an uplink scheduling grant transmitted by means of an appropriate DCI Format.

For a), b) and c) above, two exceptions are allowed for each component carrier for a power per carrier ranging from -20 dBm to PUMAX,c as defined in subclause 6.2.5. For these exceptions the power tolerance limit is ±6.0 dB in Table 6.3.5.2.1-1.

## 6.3.5A.3Aggregate power control tolerance

Aggregate power control tolerance is the ability of a UE to maintain its power in non-contiguous transmission within 21 ms in response to 0 dB TPC commands with respect to the first UE transmission, when the power control parameters specified in [6] are constant on all active component carriers.

## 6.3.5A.3.1Minimum requirements

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the aggregate power tolerance is specified on each component carrier exceed the minimum output power as defined in subclause 6.3.2A and the total power is limited by maximum output power as defined in subclause 6.2.2A. The requirements defined in Table 6.3.5.3.1-1 shall apply on each component carrier with all component carriers active. The requirements can be tested by time aligning any transmission gaps on both the component carriers.

For intra-band contiguous carrier aggregation bandwidth class B, C and D and intra-band non-contiguous carrier aggregation, the aggregate power tolerance per component carrier is given in Table 6.3.5.3.1-1 with either simultaneous PUSCH or simultaneous PUCCH-PUSCH (if supported by the UE) configured. The average power per PRB shall be aligned across both assigned carriers before the start of the test. The requirement can be tested with the transmission gaps time aligned between component carriers.

## 6.3.5BPower control for UL-MIMO

For UE supporting UL-MIMO, the power control tolerance applies to the sum of output power at each transmit antenna connector.

The power control requirements specified in subclause 6.3.5 apply to UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme. The requirements shall be met with UL-MIMO configurations specified in Table 6.2.2B-2, wherein

-The Maximum output power requirements for UL-MIMO are specified in subclause 6.2.2B

-The Minimum output power requirements for UL-MIMO are specified in subclause 6.3.2B

-The requirements for configured transmitted power for UL-MIMO are specified in subclause 6.2.5B.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.3.5 apply.

## 6.3.5DPower Control for ProSe

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.3.5D apply for ProSe transmission and the requirements in subclause 6.3.5 apply for uplink transmission.

## 6.3.5D.1Absolute power tolerance

For ProSe transmissions, the absolute power tolerance requirements specified in subclause 6.3.5.1 shall apply for each ProSe transmission.

## 6.3.5EPower control for category M1 and M2

## 6.3.5E.1Absolute power tolerance

The absolute power tolerance requirements specified in subclause 6.3.5.1 apply, wherein

-The Maximum output power requirements are specified in subclause 6.2.2E

-The Minimum output power requirements are specified in subclause 6.3.2

-The requirements for configured transmitted power are specified in subclause 6.2.5.

## 6.3.5E.2Relative Power tolerance

The relative power tolerance requirements specified in subclause 6.3.5.2 apply, wherein

-The Maximum output power requirements are specified in subclause 6.2.2E

-The Minimum output power requirements are specified in subclause 6.3.2

-The requirements for configured transmitted power are specified in subclause 6.2.5.

## 6.3.5E.3Aggregate power control tolerance

Aggregate power control tolerance is the ability of a UE to maintain its power in non-contiguous transmission in response to 0 dB TPC commands with respect to the first UE transmission, when the power control parameters specified in TS 36.213 are constant.

For category M1 and M2 TDD and FD-FDD UEs, the aggregate power control tolerance requirements specified in Table 6.3.5E.3.1-0 apply. For category M1 and M2 HD-FDD UEs and for continuous uplink transmissions of duration ≤ 64 ms, the aggregate power control tolerance requirements specified in Table 6.3.5E.3.1-0 apply.

For category M1 and M2 HD-FDD UEs and for continuous uplink transmissions of duration > 64 ms, the aggregate power control tolerance requirements specified in Table 6.3.5E.3.1-1 apply.

## 6.3.5E.3.1Minimum requirement

The category M1 and M2 TDD and FD-FDD UEs shall meet the requirements specified in Table 6.3.5E.3.1-0 for aggregate power control over the power range bounded by the minimum output power as defined in subclause 6.3.2,  the maximum output power as defined in subclause 6.2.2E, and the requirements for configured transmitted power are specified in subclause 6.2.5.

The category M1 and M2 HD-FDD UEs and for continuous uplink transmissions of duration ≤ 64 ms, shall meet the requirements specified in Table 6.3.5E.3.1-0 for aggregate power control over the power range bounded by the minimum output power as defined in subclause 6.3.2,  the maximum output power as defined in subclause 6.2.2E, and the requirements for configured transmitted power are specified in subclause 6.2.5.

Table 6.3.5E.3.1-0: Aggregate power control tolerance

The category M1 and M2 HD-FDD UE and for continuous uplink transmissions of duration > 64 ms shall meet the requirements specified in Table 6.3.5E.3.1-1 for aggregate power control over the power range bounded by the minimum output power as defined in subclause 6.3.2 and the maximum output power as defined in subclause 6.2.2E.

Table 6.3.5E.3.1-1: Aggregate power control tolerance

## 6.3.5FPower Control for category NB1 and NB2

Power control requirements in this clause apply for category NB1 and NB2 UE.

## 6.3.5F.1Absolute power tolerance

The minimum requirement for absolute power tolerance is given in Table 6.3.5F.1-1 over the power range bounded by the Maximum output power as defined in subclause 6.2.2F and the Minimum output power as defined in subclause 6.3.2F.

Table 6.3.5F.1-1: Absolute power tolerance - I

In case of -15 dB ≤ Ês/Iot < -6 dB, the absolute power tolerance given in Table 6.3.5F.1-2 applies if the UE transmit power is not mandated to be PCMAX,c according to the UE uplink power control procedure or random access procedure in Section 16 of [6] (e.g. the lowest configured repetition level is used for NPRACH transmission or the number of repetitions of the allocated NPUSCH RUs is no more than 2).

Table 6.3.5F.1-2: Absolute power tolerance - II

## 6.3.5F.2Relative power tolerance

Category NB1 and NB2 UE relative power control requirement is defined for NPRACH power step values of 0, 2, 4 and 6 dB. For NPRACH transmission, the relative tolerance is the ability of the UE transmitter to set its output power relatively to the power of the most recently transmitted preamble. The measurement period for the NPRACH preamble is specified in Table 6.3.4F.2-1.

The requirements specified in Table 6.3.5F.2-1 apply when the power of the target and reference sub-frames are within the power range bounded by the Minimum output power as defined in subclause 6.3.2F and the maximum output power as defined in subclause 6.2.2F.

Table 6.3.5F.2-1: Relative power tolerance for category NB1 and NB2 NPRACH transmission (normal conditions)

The power step (ΔP) is defined as the difference in the calculated setting of the UE transmit power between the target and reference sub-frames. The error is the difference between ΔP and the power change measured at the UE antenna port with the power of the cell-specific reference signals kept constant. The error shall be less than the relative power tolerance specified in Table 6.3.5F.2-1.

## 6.3.5F.3Aggregate power control tolerance for category NB1 and NB2

Category NB1 and NB2 aggregate power control tolerance is the ability of a UE to maintain its output power in non-contiguous transmission with respect to the first UE transmission, when the uplink power control parameters as defined in TS 36.213 are constant and α is set to 0.

## 6.3.5F.3.1Minimum requirement

The UE shall meet the requirements specified in Table 6.3.5F.3.1-1 for aggregate power control over the power range bounded by the minimum output power as defined in subclause 6.3.2F and the maximum output power as defined in subclause 6.2.2F.

Table 6.3.5F.3.1-1: Aggregate power control tolerance for HD-FDD

Table 6.3.5F.3.1-2: Aggregate power control tolerance for TDD

## 6.3.5GPower Control for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table Table 5.5G-1, the requirements in subclause 6.3.5G.1 apply for E-UTRA V2X sidelink transmission.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.3.5G.1 apply for V2X sidelink transmission and the requirements in subclause 6.3.5 apply for the E-UTRA uplink transmission.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the power control tolerance for single carrier shall apply to the sum of output power at each transmit antenna connector.

If the UE transmitson one -antenna connector at a time, the requirements for single carrier shall apply to the active antenna connector.

## 6.3.5G.1Absolute power tolerance

Absolute power tolerance is the ability of the UE to set its output power to a specific value for each subframe.

For V2X sidelink communication transmissions in the operating bands specified in Table 5.5G-1, the minimum requirement for absolute power tolerance is given in Table 6.3.5G.1-1 over the power range bounded by the Maximum output power as defined in subclause 6.2.2G and the Minimum output power as defined in subclause 6.3.2G.

For operating bands under NOTE 2 in Table 6.2.2-1, the absolute power tolerance as specified in Table 6.3.5G.1-1 is relaxed by reducing the lower limit by 1.5 dB when the transmission bandwidth is confined within FUL_low and FUL_low + 4 MHz or FUL_high – 4 MHz and FUL_high.

Table 6.3.5G.1-1: Absolute power tolerance

For intra-band contiguous multi-carrier operation the absolute power control tolerance specified in Table 6.3.5G.1-1 shall apply for each component carrier.

## 6.4Void

## 6.5Transmit signal quality

## 6.5.1Frequency error

The UE modulated carrier frequency shall be accurate to within ±0.1 PPM observed over a period of one time slot (0.5 ms) compared to the carrier frequency received from the E-UTRA Node B

## 6.5.1A Frequency error for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the frequency error requirements defined in subclause 6.5.1 shall apply on each component carrier with all component carriers active.

For intra-band contiguous carrier aggregation the UE modulated carrier frequencies per band shall be accurate to within ±0.1 PPM observed over a period of one timeslot compared to the carrier frequency of primary component carrier received from the E-UTRA in the corresponding band.

For intra-band non-contiguous carrier aggregation the requirements in Section 6.5.1 applies per component carrier.

## 6.5.1BFrequency error for UL-MIMO

For UE(s) supporting UL-MIMO, the UE modulated carrier frequency at each transmit antenna connector shall be accurate to within ±0.1 PPM observed over a period of one time slot (0.5 ms) compared to the carrier frequency received from the E-UTRA Node B.

## 6.5.1DFrequency error for ProSe

The UE modulated carrier frequency for ProSe sidelink transmissions shall be accurate to within ±0.1 PPM observed over a period of one time slot (0.5 ms) compared to the carrier frequency received from the synchronization source. The synchronization source can be E-UTRA Node B or a ProSe UE transmitting sidelink synchronization signals.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.5.1D apply for ProSe transmission and the requirements in subclause 6.5.1 apply for uplink transmission.

## 6.5.1EFrequency error for UE category M1 and M2

For category M1 and M2 TDD UEs and FD-FDD UEs, the frequency error requirements in Clause 6.5.1 apply.

For category M1 and M2 HD-FDD UEs and for continuous uplink transmissions of duration ≤ 64 ms, the frequency error requirements in Clause 6.5.1 apply.

For category M1 and M2 HD-FDD UEs and for continuous uplink transmissions of duration > 64 ms, the UE modulated carrier frequency shall be accurate to within the limits in Table 6.5.1E-1 observed over a period of one time slot (0.5 ms) compared to the carrier frequency received from the E-UTRA Node B.

Table 6.5.1E-1: Frequency error requirement for HD-FDD UE category M1 and M2

## 6.5.1FFrequency error for UE category NB1 and NB2

For UE category NB1 and NB2, the UE modulated carrier frequency shall be accurate to within the following limits

Table 6.5.1F-1: Frequency error requirement for UE category NB1 and NB2

Observed over a period of one time slot (0.5 ms for 15 kHz sub-carrier spacing and 2 ms excluding the 2304Ts gap for 3.75 kHz sub-carrier spacing) and averaged over 72/LCtone slots (where LCtone = {1, 3, 6, 12} is the number of sub-carriers used for the transmission), compared to the carrier frequency received from the E-UTRA Node B.

## 6.5.1GFrequency error for V2X Communication

The UE modulated carrier frequency for V2X sidelink transmissions shall be accurate to within ±0.1 PPM observed over a period of one time slot (0.5 ms) compared to the absolute frequency in case of using GNSS synchronization source. The same requirements applied over a period of one time slot (0.5 ms) compared to the relative frequency in case of using the E-UTRA Node B or V2X UE sidelink synchronization signals.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.5.1G apply for V2X sidelink transmission and the requirements in subclause 6.5.1 apply for the E-UTRA uplink transmission.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the UE modulated carrier frequency at each transmit antenna connector shall be accurate to within ±0.1 PPM observed over a period of one time slot (0.5 ms) in case of using GNSS synchronization source. The same requirements applied over a period of one time slot (0.5 ms) compared to the relative frequency in case of using the E-UTRA Node B or V2X UE sidelink synchronization signals.

If the UE transmits on one antenna connector at a time, the requirements for single carrier shall apply to the active antenna connector.

## 6.5.2Transmit modulation quality

Transmit modulation quality defines the modulation quality for expected in-channel RF transmissions from the UE. The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage

-In-band emissions for the non-allocated RB

All the parameters defined in subclause 6.5.2 are defined using the measurement methodology specified in Annex F.

## 6.5.2.1Error Vector Magnitude

The Error Vector Magnitude is a measure of the difference between the reference waveform and the measured waveform. This difference is called the error vector. Before calculating the EVM the measured waveform is corrected by the sample timing offset and RF frequency offset. Then the carrier leakage shall be removed from the measured waveform before calculating the EVM.

The measured waveform is further modified by selecting the absolute phase and absolute amplitude of the Tx chain. The EVM result is defined after the front-end IDFT as the square root of the ratio of the mean error vector power to the mean reference power expressed as a %.

The basic EVM measurement interval in the time domain is one preamble sequence for the PRACH, and as specified in Table 6.5.2.1-1 for the PUCCH and PUSCH in the time domain. When the PUSCH or PUCCH transmission slot or subslot is shortened due to multiplexing with SRS, the EVM measurement interval is reduced by one symbol, accordingly. Likewise, when the PUSCH starting position is modified or when second last symbol is the ending symbol of the PUSCH subframe for Frame Structure Type 3, the EVM measurement interval is reduced accordingly. The PUSCH or PUCCH EVM measurement interval is also reduced when the mean power, modulation or allocation between slots or subslots is expected to change. In the case of PUSCH transmission, the measurement interval is reduced by a time interval equal to the sum of 5 μs and the applicable exclusion period defined in subclause 6.3.4, adjacent to the boundary where the power change is expected to occur. The PUSCH exclusion period is applied to the signal obtained after the front-end IDFT. In the case of PUCCH transmission with power change, the PUCCH EVM measurement interval is reduced by one symbol adjacent to the boundary where the power change is expected to occur.

Table 6.5.2.1-1: Measurement interval for EVM

## 6.5.2.1.1Minimum requirement

The RMS average of the basic EVM measurements for 10 subframes excluding any transient period for the average EVM case, and 60 subframes excluding any transient period for the reference signal EVM case, for the different modulations schemes shall not exceed the values specified in Table 6.5.2.1.1-1 for the parameters defined in Table 6.5.2.1.1-2. For EVM evaluation purposes, [all PRACH preamble formats 0-4 and] all PUCCH formats 1, 1a, 1b, 2, 2a and 2b are considered to have the same EVM requirement as QPSK modulated.

Table 6.5.2.1.1-1: Minimum requirements for Error Vector Magnitude

Table 6.5.2.1.1-2: Parameters for Error Vector Magnitude

## 6.5.2.2Carrier leakage

Carrier leakage is an additive sinusoid waveform that has the same frequency as a modulated waveform carrier frequency. The measurement interval is one slot in the time domain.

## 6.5.2.2.1Minimum requirements

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. The relative carrier leakage power shall not exceed the values specified in Table 6.5.2.2.1-1.

Table 6.5.2.2.1-1: Minimum requirements for relative carrier leakage power

## 6.5.2.3In-band emissions

The in-band emission is defined as the average across 12 sub-carrier and as a function of the RB offset from the edge of the allocated UL transmission bandwidth. The in-band emission is measured as the ratio of the UE output power in a non–allocated RB to the UE output power in an allocated RB.

The basic in-band emissions measurement interval is defined over one slot in the time domain. When the PUSCH or PUCCH transmission slot is shortened due to multiplexing with SRS, the in-band emissions measurement interval is reduced by one SC-FDMA symbol, accordingly. Likewise, when the PUSCH starting position is modified or when the second last symbol is the ending symbol of the PUSCH sub-frame for Frame Structure Type 3, the in-band emissions measurement interval is reduced accordingly.

## 6.5.2.3.1Minimum requirements

The relative in-band emission shall not exceed the values specified in Table 6.5.2.3.1-1.

Table 6.5.2.3.1-1: Minimum requirements for in-band emissions

NOTE:For Frame Structure 3 and operations in Band 46, in-band emissions requirements are not specified for the 10 MHz channel bandwidth.

## 6.5.2.4EVM equalizer spectrum flatness

The zero-forcing equalizer correction applied in the EVM measurement process (as described in Annex F) must meet a spectral flatness requirement for the EVM measurement to be valid. The EVM equalizer spectrum flatness is defined in terms of the maximum peak-to-peak ripple of the equalizer coefficients (dB) across the allocated uplink block. The basic measurement interval is the same as for EVM.

## 6.5.2.4.1Minimum requirements

The peak-to-peak variation of the EVM equalizer coefficients contained within the frequency range of the uplink allocation shall not exceed the maximum ripple specified in Table 6.5.2.4.1-1 for normal conditions. For uplink allocations contained within both Range 1 and Range 2, the coefficients evaluated within each of these frequency ranges shall meet the corresponding ripple requirement and the following additional requirement: the relative difference between the maximum coefficient in Range 1 and the minimum coefficient in Range 2 must not be larger than 5 dB, and the relative difference between the maximum coefficient in Range 2 and the minimum coefficient in Range 1 must not be larger than 7 dB (see Figure 6.5.2.4.1-1).

The EVM equalizer spectral flatness shall not exceed the values specified in Table 6.5.2.4.1-2 for extreme conditions. For uplink allocations contained within both Range 1 and Range 2, the coefficients evaluated within each of these frequency ranges shall meet the corresponding ripple requirement and the following additional requirement: the relative difference between the maximum coefficient in Range 1 and the minimum coefficient in Range 2 must not be larger than 6 dB, and the relative difference between the maximum coefficient in Range 2 and the minimum coefficient in Range 1 must not be larger than 10 dB (see Figure 6.5.2.4.1-1).

Table 6.5.2.4.1-1: Minimum requirements for EVM equalizer spectrum flatness (normal conditions)

Table 6.5.2.4.1-2: Minimum requirements for EVM equalizer spectrum flatness (extreme conditions)

f    FUL_High  FUL_High – 3(5) MHz     < 4(4) dBp-p     Range 1Range 2  max(Range 1)-min(Range 2) < 5(6) dB    max(Range 2)-min(Range 1) < 7(10) dB     < 8(12) dBp-p      f    FUL_High  FUL_High – 3(5) MHz     < 4(4) dBp-p     Range 1Range 2  max(Range 1)-min(Range 2) < 5(6) dB    max(Range 2)-min(Range 1) < 7(10) dB     < 8(12) dBp-p

Figure 6.5.2.4.1-1: The limits for EVM equalizer spectral flatness with the maximum allowed variation of the coefficients indicated (the ETC minimum requirement within brackets).

## 6.5.2ATransmit modulation quality for CA

For inter-band carrier aggregation with uplink assigned to two E-UTRA bands, the requirements shall apply on each component carrier as defined in clause 6.5.2 with all component carriers active. If two contiguous component carriers are assigned to one E-UTRA band, the requirements in subclauses 6.5.2A.1, 6.5.2A.2, and 6.5.2A.3 apply for those component carriers.

The requirements in this clause apply with PCC and SCC in the UL configured and activated: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

## 6.5.2A.1Error Vector Magnitude

For the intra-band contiguous and non-contiguous carrier aggregation, the Error Vector Magnitude requirement should be defined for each component carrier. Requirements only apply with PRB allocation in one of the component carriers. Similar transmitter impairment removal procedures are applied for CA waveform before EVM calculation as is specified for non-CA waveform in sub-section 6.5.2.1.

When a single component carrier is configured Table 6.5.2.1.1-1 apply.

The EVM requirements are according to Table 6.5.2A.1-1 if CA is configured in uplink with the parameters defined in Table 6.5.2.1.1-2.

Table 6.5.2A.1-1: Minimum requirements for Error Vector Magnitude

## 6.5.2A.2Carrier leakage for CA

Carrier leakage is an additive sinusoid waveform that is confined within the aggrecated transmission bandwidth configuration. The carrier leakage requirement is defined for each component carrier and is measured on the component carrier with PRBs allocated. The measurement interval is one slot in the time domain.

## 6.5.2A.2.1Minimum requirements

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. The relative carrier leakage power shall not exceed the values specified in Table 6.5.2A.2.1-1.

Table 6.5.2A.2.1-1: Minimum requirements for Relative Carrier Leakage Power

## 6.5.2A.3In-band emissions

## 6.5.2A.3.1Minimum requirement for CA

For intra-band contiguous carrier aggregation bandwidth class B, C and D, the requirements in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 apply within the aggregated transmission bandwidth configuration with both component carrier (s) active and one single contiguous PRB allocation of bandwidth  at the edge of the aggregated transmission bandwidth configuration.

The inband emission is defined as the interference falling into the non allocated resource blocks for all component carriers. The measurement method for the inband emissions in the component carrier with PRB allocation is specified in annex F. For a non allocated component carrier a spectral measurement is specified.

For intra-band non-contiguous carrier aggregation the requirements for in-band emissions should be defined for each component carrier. Requirements only apply with PRB allocation in one of the component carriers according to Table 6.5.2.3.1.

Table 6.5.2A.3.1-1: Minimum requirements for in-band emissions (allocated component carrier)

Table 6.5.2A.3.1-2: Minimum requirements for in-band emissions (not allocated component carrier)

## 6.5.2BTransmit modulation quality for UL-MIMO

For UE supporting UL-MIMO, the transmit modulation quality requirements are specified at each transmit antenna connector.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.5.2 apply.

The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage (caused by IQ offset)

-In-band emissions for the non-allocated RB

## 6.5.2B.1Error Vector Magnitude

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the Error Vector Magnitude requirements specified in Table 6.5.2.1.1-1 which is defined in subclause 6.5.2.1 apply at each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

## 6.5.2B.2Carrier leakage

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the Relative Carrier Leakage Power requirements specified in Table 6.5.2.2.1-1 which is defined in subclause 6.5.2.2 apply at each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

## 6.5.2B.3In-band emissions

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the In-band Emission requirements specified in Table 6.5.2.3.1-1 which is defined in subclause 6.5.2.3 apply at each transmit antenna connector. The requirements shall be met with the uplink MIMO configurations specified in Table 6.2.2B-2.

## 6.5.2B.4EVM equalizer spectrum flatness for UL-MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the EVM Equalizer Spectrum Flatness requirements specified in Table 6.5.2.4.1-1 and Table 6.5.2.4.1-2 which are defined in subclause 6.5.2.4 apply at each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

## 6.5.2DTransmit modulation quality for ProSe

The requirements in this clause apply to ProSe sidelink transmissions.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.5.2D apply for ProSe transmission and the requirements in subclause 6.5.2 apply for uplink transmission.

## 6.5.2D.1Error Vector Magnitude

For ProSe sidelink physical channels PSDCH, PSCCH, PSSCH, and PSBCH, the Error Vector Magnitude requirements shall be as specified for PUSCH in subclause 6.5.2.1 for the corresponding modulation and transmission bandwidth. When ProSe transmissions are shortened due to transmission gap of 1 symbol at the end of the subframe, the EVM measurement interval is reduced by one symbol, accordingly.

For PSBCH the duration over which EVM is averaged shall be 24 subframes.

This requirement is not applicable for ProSe physical signals PSSS and SSSS.

## 6.5.2D.2Carrier leakage

The requirements of subcaluse 6.5.2.2 shall apply for ProSe transmissions.

## 6.5.2D.3In-band emissions

For ProSe sidelink physical channels PSDCH, PSCCH, PSSCH, and PSBCH, the In-band emissions requirements shall be as specified for PUSCH in subclause 6.5.2.3 for the corresponding modulation and transmission bandwidth. When ProSe transmissions are shortened due to transmission gap of 1 symbol at the end of the subframe, the In-band emissions measurement interval is reduced by one symbol, accordingly.

## 6.5.2D.4EVM equalizer spectrum flatness for ProSe

The requirements of subcaluse 6.5.2.4 shall apply for ProSe transmissions.

## 6.5.2ETransmit modulation quality for category M1 and M2

## 6.5.2E.1Error Vector Magnitude

The Error Vector Magnitude is defined in section 6.5.2.1.

## 6.5.2E.2Carrier leakage

Carrier leakage is an additive sinusoid waveform that has the same frequency as a modulated waveform carrier frequency. For UE of UL Categories M1 and M2, the sinusoid waveform may lie at the center of the narrowband assigned for transmission. The measurement interval is one slot in the time domain.

## 6.5.2E.2.1Minimum requirements

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. The relative carrier leakage power at the center of the channel bandwidth or the center of the narrowband assigned for transmission shall not exceed the values specified in Table 6.5.2.2.1-1.

## 6.5.2E.3In-band emissions

The in-band emission is defined in clause 6.5.2.3 and measurement condition specified in Annex F.

## 6.5.2E.3.1Minimum requirements

The relative in-band emission when the center carrier frequency is either at the center of channel bandwidth or at the center of the narrowband assigned for transmission shall not exceed the values specified in Table 6.5.2E.3.1-1

Table 6.5.2E.3.1-1: Minimum requirements for in-band emissions

## 6.5.2FTransmit modulation quality for Category NB1 and NB2

## 6.5.2F.1Error Vector Magnitude

The RMS average of the basic EVM measurements for 240/LCtone slots excluding any transient period for the average EVM case, where LCtone = {1, 3, 6, 12} is the number of subcarriers for the category NB1 and NB2 transmission, for the different modulations schemes shall not exceed the values specified in Table 6.5.2.1.1-1 for the parameters defined in Table 6.5.2.1.1-2. For EVM evaluation purposes, both NPRACH formats are considered to have the same EVM requirement as QPSK modulated.

## 6.5.2F.2Carrier leakage

Carrier leakage is an additive sinusoid waveform that has the same frequency as a modulated waveform carrier frequency. The measurement interval is one slot in the time domain. The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. The relative carrier leakage power of category NB1 or NB2 UE shall not exceed the values specified in Table 6.5.2F.2-1.

Table 6.5.2F.2-1: Minimum requirements for relative carrier leakage power

## 6.5.2F.3In-band emissions

The in-band emission is defined as a function of the tone offset from the edge of the allocated UL transmission tone(s) within the transmission bandwidth configuration. The in-band emission is measured as the ratio of the UE output power in a non–allocated tone to the UE output power in an allocated tone. The basic in-band emissions measurement interval is defined over one slot in the time domain.

The category NB1 and NB2 UE relative in-band emission shall not exceed the values specified in Table 6.5.2F.3-1.

Table 6.5.2F.3-1: Minimum requirements for in-band emissions

## 6.5.2GTransmit modulation quality for V2X Communication

The requirements in this clause apply to V2X sidelink transmissions.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.5.2G apply for V2X sidelink transmission and the requirements in subclause 6.5.2 apply for the E-UTRA uplink transmission.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna-connectors at the same time, the transmit modulation quality requirements for single carrier shall apply to each transmit antenna connector.

If V2X UE transmits on one-antenna connector at a time, the requirements specified for single carrier apply to the active antenna connector.

## 6.5.2G.1Error Vector Magnitude

For V2X physical channels PSCCH, PSSCH and PSBCH, the Error Vector Magnitude requirements shall be as specified for PUSCH in subclause 6.5.2.1 for the corresponding modulation and transmission bandwidth.

For V2X sidelink physical channels PSCCH, PSSCH and PSBCH, the Error Vector Magnitude requirements shall be as specified separately for PSSCH and PSCCH for the corresponding modulation and transmission bandwidth. The measurement period for EVM of PSSCH and PSCCH is 15 subframes. The measurement period for reference signal EVM is 30 subframes. When V2X transmissions are shortened due to transmission gap of 1 symbol at the end of the subframe, the EVM measurement interval is reduced by one symbol, accordingly.

For PSBCH the duration over which EVM is averaged shall be 24 subframes.

For intra-band contiguous multi-carrier operation the EVM requirement shall apply for each component carrier.

## 6.5.2G.2Carrier leakage

The requirements of subcaluse 6.5.2.2 shall apply for V2X transmissions.

For intra-band contiguous multi-carrier operation the carrier leakage requirement of subcaluse 6.5.2A.2 shall apply.

## 6.5.2G.3In-band emissions

For V2X sidelink physical channels PSCCH, PSSCH and PSBCH, the In-band emissions requirements shall be as specified for PUSCH in subclause 6.5.2.3 for the corresponding modulation and transmission bandwidth. When V2X transmissions are shortened due to transmission gap of 1 symbol at the end of the subframe, the In-band emissions measurement interval is reduced by one symbol, accordingly.

For intra-band contiguous multi-carrier operation the in-band emission requirement of subcaluse 6.5.2A.3 shall apply.

## 6.5.2G.4EVM equalizer spectrum flatness

The requirements of subcaluse 6.5.2.4 shall apply for V2X transmissions.

For intra-band contiguous multi-carrier operation the EVM equalizer spectrum flatness requirement of subcaluse 6.5.2.4 shall apply for each component carrier.

## 6.6Output RF spectrum emissions

The output UE transmitter spectrum consists of the three components; the emission within the occupied bandwidth (channel bandwidth), the Out Of Band (OOB) emissions and the far out spurious emission domain.

Figure 6.6-1: Transmitter RF spectrum

## 6.6.1Occupied bandwidth

Occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel. The occupied bandwidth for all transmission bandwidth configurations (Resources Blocks) shall be less than the channel bandwidth specified in Table 6.6.1-1

Table 6.6.1-1: Occupied channel bandwidth

## 6.6.1.1Additional minimum requirement for E-UTRA (network signalled value “NS_29”)

For E-UTRA CA bands including one uplink LAA Scell in Band 46 with "NS_29" indicated, the occupied bandwidth for all transmission bandwidth configurations (Resources Blocks) shall be less than or equal to 19 MHz and 19.7MHz for E-UTRA carriers of 20 MHz bandwidth assigned within 5150-5350 MHz and 5470-5725 MHz, respectively.

## 6.6.1AOccupied bandwidth for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands the occupied bandwidth is defined per component carrier. Occupied bandwidth is the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on assigned channel bandwidth on the component carrier. The occupied bandwidth shall be less than the channel bandwidth specified in Table 6.6.1-1.

For intra-band contiguous carrier aggregation the occupied bandwidth is a measure of the bandwidth containing 99 % of the total integrated power of the transmitted spectrum. The OBW shall be less than the aggregated channel bandwidth defined in subclause 5.6A.

For intra-band non-contiguous carrier aggregation sub-block occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the sub-block. In case the sub-block consist of one component carrier the occupied bandwidth of the sub-block shall be less than the channel bandwidth specified in Table 6.6.1-1.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the occupied bandwidth is the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on each E-UTRA band. The OBW shall be less than the channel bandwidth as specified in Table 6.6.1-1 for the E-UTRA band supporting one component carrier. The OBW shall be less than the aggregated channel bandwidth as specified in subclause 5.6A for the E-UTRA band supporting two contiguous component carriers.

## 6.6.1BOccupied bandwidth for UL-MIMO

For UE supporting UL-MIMO, the requirements for occupied bandwidth is specified at each transmit antenna connector. The occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel at each transmit antenna connector.

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the occupied bandwidth at each transmitter antenna shall be less than the channel bandwidth specified in Table 6.6.1B-1. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

Table 6.6.1B-1: Occupied channel bandwidth

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.6.1 apply.

## 6.6.1FOccupied bandwidth for category NB1 and NB2

The occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel at the transmit antenna connector. Occupied bandwidth shall be less than the channel bandwidth of category NB1 and NB2 specified in Section 5.6F.

## 6.6.1GOccupied bandwidth for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table Table 5.5G-1, the requirements in subclause 6.6.1 apply for E-UTRA V2X sidelink transmission.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.6.1 apply for V2X sidelink transmission and the E-UTRA uplink transmission.

For intra-band contiguous multi-carrier operation, the occupied bandwidth is a measure of the bandwidth containing 99 % of the total integrated power of the transmitted spectrum. The OBW shall be less than the aggregated channel bandwidth defined in subclause 5.6A.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the requirements for occupied bandwidth is specified at each transmit antenna connector and the occupied bandwidth at each transmitter antenna shall be less than the channel bandwidth specified for single carrier.

If V2X UE transmits on one antenna connector at a time, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.6.2Out of band emission

The Out of band emissions are unwanted emissions immediately outside the assigned channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an Adjacent Channel Leakage power Ratio.

## 6.6.2.1Spectrum emission mask

The spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the  edge of the assigned E-UTRA channel bandwidth. For frequencies offset greater than ΔfOOB as specified in Table 6.6.2.1.1-1 the spurious requirements in subclause 6.6.3 are applicable.

## 6.6.2.1.1Minimum requirement

The power of any UE emission shall not exceed the levels specified in Table 6.6.2.1.1-1 for the specified channel bandwidth.

Table 6.6.2.1.1-1: General E-UTRA spectrum emission mask

NOTE: As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.1ASpectrum emission mask for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the spectrum emission mask of the UE is defined per component carrier while both component carriers are active and the requirements are specified in subclauses 6.6.2.1 and 6.6.2.2. If for some frequency spectrum emission masks of component carriers overlap then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency a component carrier spectrum emission mask overlaps with the channel bandwidth of another component carrier, then the emission mask does not apply for that frequency.

For intra-band contiguous carrier aggregation the spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the  edge of the aggregated channel bandwidth (Table 5.6A-1) For intra-band contiguous carrier aggregation the bandwidth class B, C and D, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.1A-0, Table 6.6.2.1A-1 and Table 6.6.2.1A-2 for the specified channel bandwidth.

Table 6.6.2.1A-0: General E-UTRA CA spectrum emission mask for Bandwidth Class B

Table 6.6.2.1A-1: General E-UTRA CA spectrum emission mask for Bandwidth Class C

Table 6.6.2.1A-2: General E-UTRA CA spectrum emission mask for Bandwidth Class D

For intra-band non-contiguous carrier aggregation transmission the spectrum emission mask requirement is defined as a composite spectrum emissions mask. Composite spectrum emission mask applies to frequencies up to  ΔfOOB starting from the edges of the sub-blocks. Composite spectrum emission mask is defined as follows

a)Composite spectrum emission mask is a combination of individual sub-block spectrum emissions masks

b)In case the sub-block consist of one component carrier the sub-lock general spectrum emission mask is defined in subclause 6.6.2.1.1

c)If for some frequency sub-block spectrum emission masks overlap then spectrum emission mask allowing higher power spectral density applies for that frequency

d)If for some frequency a sub-block spectrum emission mask overlaps with the sub-block bandwidth of another sub-block, then the emission mask does not apply for that frequency.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the spectrum emission mask of the UE is defined per E-UTRA band while all component carriers are active. For the E-UTRA band supporting one component carrier the requirements in subclauses 6.6.2.1 and 6.6.2.2 apply. For the E-UTRA band supporting two contiguous component carriers the requirements specified in subclause 6.6.2.1A apply. If for some frequency spectrum emission masks of single component carrier and two contiguous component carriers overlap then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency spectrum emission masks of single component carrier or two contiguous component carriers overlap then the emission mask does not apply for that frequency.

## 6.6.2.2Additional spectrum emission mask

This requirement is specified in terms of an "additional spectrum emission" requirement.

## 6.6.2.2.1Minimum requirement (network signalled value "NS_03", “NS_11”, "NS_20", and “NS_21”)

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_03", "NS_11", "NS_20" or "NS_21" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.1-1.

Table 6.6.2.2.1-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2.2Minimum requirement (network signalled value "NS_04")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.2-1.

Table 6.6.2.2.2-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2.3Minimum requirement (network signalled value "NS_06" or “NS_07”)

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_06" or “NS_07” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.3-1.

Table 6.6.2.2.3-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2.4Minimum requirement (network signalled value "NS_33" or “NS_34”)

The additional spectrum mask in Table 6.6.2.2.4-1 applies for E-UTRA V2X UE within 5 855 MHz to 5 950 MHz according to ETSI EN 302 571. Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_33" or “NS_34” is indicated in the cell, the power of any V2X UE emission shall not exceed the levels specified in Table 6.6.2.2.4-1.

Table 6.6.2.2.4-1: Additional requirements for 10MHz channel bandwidth

NOTE 1:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE 2:Additional SEM for V2X overrides any other requirements in frequency range 5855-5950MHz.

NOTE 3:The EIRP requirement is converted to conducted requirement depend on the supported post antenna connector gain Gpost connector declared by the UE following the principle described in annex I.

## 6.6.2.2.5Minimum requirement (network signalled value “NS_27” and “NS_43”)

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When “NS_27” or “NS_43” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.5-1.

Table 6.6.2.2.5-1: Additional requirements

## 6.6.2.2.6Minimum requirement (network signalled value "NS_28”)

When "NS_28” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.6-1 for E-UTRA channels assigned within the frequency ranges 5150-5350 and 5470-5725 MHz.

Table 6.6.2.2.6-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2.7Minimum requirement (network signalled value "NS_35")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_35" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2.7-1.

Table 6.6.2.2.7-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2AAdditional Spectrum Emission Mask for CA

This requirement is specified in terms of an "additional spectrum emission" requirement.

## 6.6.2.2A.1Minimum requirement (network signalled value "CA_NS_04")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "CA_NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2A.1-1.

Table 6.6.2.2A.1-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2A.2Minimum requirement CA_66B (network signalled value "CA_NS_09")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "CA_NS_09" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2A.2-1.

Table 6.6.2.2A.2-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2A.3Minimum requirement CA_66C (network signalled value "CA_NS_09")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "CA_NS_09" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2A.3-1.

Table 6.6.2.2A.3-1: Additional requirements

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2A.4Minimum requirement CA_48B and CA_48C (network signalled value "CA_NS_10")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "CA_NS_10" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2A.4-1.

Table 6.6.2.2A.4-1: Additional requirements for “CA_NS_10”

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.2A.5Minimum requirement CA_2C (network signalled value "CA_NS_11")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "CA_NS_11" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.2.2A.5-1.

Table 6.6.2.2A.5-1: Additional requirements for “CA_NS_11”

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.2.3Adjacent Channel Leakage Ratio

Adjacent Channel Leakage power Ratio (ACLR) is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency. ACLR requirements for one E-UTRA carrier are specified for two scenarios for an adjacent E-UTRA and /or UTRA channel as shown in Figure 6.6.2.3-1.

Figure 6.6.2.3-1: Adjacent Channel Leakage requirements for one E-UTRA carrier

## 6.6.2.3.1Minimum requirement E-UTRA

E-UTRA Adjacent Channel Leakage power Ratio (E-UTRAACLR) is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency at nominal channel spacing. The assigned E-UTRA channel power and adjacent E-UTRA channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.6.2.3.1-1, Table 6.6.2.3.1-2, and Table 6.6.2.3.1-3. If the measured adjacent channel power is greater than –50dBm then the E-UTRAACLR shall be higher than the value specified in Table 6.6.2.3.1-1, Table 6.6.2.3.1-2, and Table 6.6.2.3.1-3.

For a power class 2 capable UE operating on Band 41, when an IE P-max as defined in [7] of 23 dBm or lower is indicated in the cell or if the uplink/downlink configuration is 0 or 6, the requirements for power class 2 are not applicable,  and the corresponding requirements for a power class 3 UE shall apply.

For each supported frequency band other than Band 14 and Band 41, the UE shall:

-if the UE supports a different power class than the default UE power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the band is a TDD band whose frame configuration is 0 or 6; or

-if the IE P-Max as defined in TS 36.331 [7] is not provided; or

-if the IE P-Max as defined in TS 36.331 [7] is provided and set to the maximum output power of the default power class or lower;

-meet all requirements for the default power class of the operating band in which the UE is operating and set its configured transmitted power as specified in sub-clause 6.2.5;

-else (i.e the IE P-Max as defined in TS 36.331 [7] is provided and set to the higher value than the maximum output power of the default power class):

-meet all requirements for the supported power class and set its configured transmitted power class as specified in sub-clause 6.2.5.

Table 6.6.2.3.1-1: General requirements for E-UTRAACLR

Table 6.6.2.3.1-2: Additional E-UTRAACLR requirements for Power Class 1

Table 6.6.2.3.1-3: Additional E-UTRAACLR requirements for Power Class 2

## 6.6.2.3.1aAdditional minimum requirement for E-UTRA (network signalled value “NS_29”)

When "NS_29" is indicated in the cell, the UE emission shall meet the additional requirements specified in Table 6.6.2.3.1a-1 for E-UTRA channels assigned within the frequency ranges 5150-5350 MHz and 5470-5725 MHz. The assigned E-UTRA channel power and alternative adjacent E-UTRA channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.6.2.3.1a-1. If the measured alternative adjacent channel power is greater than –50dBm then the E-UTRAACLR2 shall be higher than the value specified in Table 6.6.2.3.1a-1.

Table 6.6.2.3.1a-1: Additional E-UTRAACLR requirement

## 6.6.2.3.1AVoid

## 6.6.2.3.1AaVoid

## 6.6.2.3.2Minimum requirements UTRA

UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the assigned E-UTRA channel frequency to the filtered mean power centred on an adjacent(s) UTRA channel frequency.

UTRA Adjacent Channel Leakage power Ratio is specified for both the first UTRA adjacent channel (UTRAACLR1) and the 2nd UTRA adjacent channel (UTRAACLR2). The UTRA channel power is measured with a RRC bandwidth filter with roll-off factor =0.22. The assigned E-UTRA channel power is measured with a rectangular filter with measurement bandwidth specified in Table 6.6.2.3.2-1. If the measured UTRA channel power is greater than –50dBm then the UTRAACLR shall be higher than the value specified in Table 6.6.2.3.2-1.

UTRAACLR is not applicable to the power class 3 UE operating in Band 7, 12, 13, 17, 20, 24, 27, 30, 33, 35, 36, 37, 38, 40, 43, 44, 45, 47, 48, 50, 51, 52, 53, 54, 68, 70, 71, 85, 87, 88, 106 and Scell operation in Band 46, 49.

UTRAACLR is not applicable to the power class 2 UE operating in Band 38, 40, 41, 42, 47 and Scell operation in Band 46.

UTRAACLR is not applicable to the power class 1 UE operating in Band 3, 12, 20, 28, 31, 40, 42, 72, 87, 88 and 106.

Table 6.6.2.3.2-1: Requirements for UTRAACLR1/2

## 6.6.2.3.2AMinimum requirement UTRA for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the assigned channel bandwidth on the component carrier to the filtered mean power centred on an adjacent channel frequency. The UTRA Adjacent Channel Leakage power Ratio is defined per carrier and the requirement is specified in subclause 6.6.2.3.2.

For intra-band contiguous carrier aggregation the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent(s) UTRA channel frequency.

For intra-band non-contiguous carrier aggregation when all sub-blocks consist of one component carrier the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the sum of the filtered mean powers centered on the assigned sub-block frequencies to the filtered mean power centred on an adjacent(s) UTRA channel frequency. UTRAACLR1/2 requirements are applicaple for all sub-blocks and are specified in Table 6.6.2.3.2A-2. UTRAACLR1 is required to be met in the sub-block gap when the gap bandwidth Wgap is 5MHz≤Wgap <15MHz. Both UTRAACLR1 and UTRAACLR2 are required to be met in the sub-block gap when the gap bandwidth Wgap is 15MHz≤Wgap.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is defined as follows. For the E-UTRA band supporting one component carrier, the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the assigned channel bandwidth of the component carrier to the filtered mean power centred on an adjacent(s) UTRA channel frequency and the requirements specified in subclause 6.6.2.3.2 apply. For the E-UTRA band supporting two contiguous component carriers the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent(s) UTRA channel frequency and the requirements specified in subclause 6.6.2.3.2A apply.

UTRA Adjacent Channel Leakage power Ratio is specified for both the first UTRA adjacent channel (UTRAACLR1) and the 2nd UTRA adjacent channel (UTRAACLR2). The UTRA channel power is measured with a RRC bandwidth filter with roll-off factor =0.22. The assigned aggregated channel bandwidth power is measured with a rectangular filter with measurement bandwidth specified in Table 6.6.2.3.2A-1 for intraband contiguous carrier aggregation or 6.6.2.3.2A-2 for intraband non-contiguous carrier aggregation. If the measured UTRA channel power is greater than –50dBm then the UTRAACLR shall be higher than the value specified in Table 6.6.2.3.2A-1 for intraband contiguous carrier aggregation or 6.6.2.3.2A-2 for intraband non-contiguous carrier aggregation.

For carrier aggregation with one or two uplink component carriers, the UTRAACLR requirements for the PC3 UE are not applicable to the uplink component carrier(s) assigned to one of the E-UTRA band in Band 7, 12, 13, 17, 20, 24, 27, 30, 33, 35, 36, 37, 38, 40, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 68, 70, 71, 85, 87, 88 and 106.

Table 6.6.2.3.2A-1: Requirements for UTRAACLR1/2

Table 6.6.2.3.2A-2: Requirements for intraband non-contiguous CA UTRAACLR1/2

## 6.6.2.3.3AMinimum requirements for CA E-UTRA

For intra-band contiguous carrier aggregation the carrier aggregation E-UTRA Adjacent Channel Leakage power Ratio (CA E-UTRAACLR) is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent aggregated channel bandwidth at nominal channel spacing. The assigned aggregated channel bandwidth power and adjacent aggregated channel bandwidth power are measured with rectangular filters with measurement bandwidths specified in Table 6.6.2.3.3A-1. If the measured adjacent channel power is greater than –50dBm then the E-UTRAACLR shall be higher than the value specified in Table 6.6.2.3.3A-1 and Table 6.6.2.3.3A-1a.

Table 6.6.2.3.3A-1: General requirements for CA E-UTRAACLR

Table 6.6.2.3.3A-1a: Additional requirements for CA E-UTRAACLR for UL CA_41C Power Class 2

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, E-UTRA Adjacent Channel Leakage power Ratio (E-UTRAACLR) is the ratio of the filtered mean power centred on the assigned channel bandwidth on a component carrier to the filtered mean power centred on an adjacent channel frequency. The E-UTRA Adjacent Channel Leakage power Ratio is defined per carrier and the requirement is specified in subclause 6.6.2.3.1.

For intra-band non-contiguous carrier aggregation when all sub-blocks consist of one component carrier the E-UTRA Adjacent Channel Leakage power Ratio (E-UTRAACLR) is the ratio of the sum of the filtered mean powers centred on the assigned sub-block frequencies to the filtered mean power centred on an adjacent channel frequency at nominal channel spacing. In case the sub-block gap bandwidth Wgap is smaller than of the sub-block bandwidth then for that sub-block no E-UTRAACLR requirement is set for the gap. In case the sub-block gab bandwidth Wgap is smaller than either of the sub-block bandwidths then no E- UTRAACLR requirement is set for the gap.The assigned E-UTRA sub-block power and adjacent E-UTRA channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.6.2.3.3A-2. If the measured adjacent channel power is greater than –50dBm then the E-UTRAACLR shall be higher than the value specified in Table 6.6.2.3.3A-2.

Table 6.6.2.3.3A-2: General requirements for non-contiguous intraband CA E-UTRAACLR

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the E-UTRA Adjacent Channel Leakage power Ratio (E-UTRAACLR) is defined as follows. For the E-UTRA band supporting one component carrier, the E-UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is the ratio of the filtered mean power centred on the assigned channel bandwidth of the component carrier to the filtered mean power centred on an adjacent channel frequency and the requirements in subclause 6.6.2.3.1 apply. For the E-UTRA band supporting two contiguous component carriers the E-UTRA Adjacent Channel Leakage power Ratio (E-UTRAACLR) is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent(s) aggregated channel bandwidth at nominal channel spacing and the requirements of CA E-UTRAACLR specified in subclause 6.6.2.3.3A apply.

## 6.6.2.4Void

## 6.6.2.4.1Void

## 6.6.2AVoid

<reserved for future use>

## 6.6.2BOut of band emission for UL-MIMO

For UE supporting UL-MIMO, the requirements for Out of band emissions resulting from the modulation process and non-linearity in the transmitters are specified at each transmit antenna connector.

For UEs with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements in subclause 6.6.2 apply to each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.6.3 apply.

## 6.6.2CVoid

<reserved for future use>

## 6.6.2DOut of band emission for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the requirements in subclause 6.6.2 apply.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the requirements in subclause 6.6.2 apply per E-UTRA ProSe sidelink and E-UTRA uplink transmission as specified for the corresponding inter-band aggregation with uplink assigned to two bands.

## 6.6.2FOut of band emission for category NB1 and NB2

## 6.6.2F.1Spectrum emission mask

The spectrum emission mask of the category NB1 and NB2 UE applies to frequencies (ΔfOOB) starting from the  edge of the assigned category NB1 or NB2 channel bandwidth. For frequencies greater than (ΔfOOB) as specified in Table 6.6.2F.1-1 the spurious requirements in subclause 6.6.3 are applicable.

The power of any category NB1 or NB2 UE emission shall not exceed the levels specified in Table 6.6.2F.1-1. The spectrum emission limit between each ΔfOOB is linearly interpolated.

Table 6.6.2F.1-1: category NB1 and NB2 UE spectrum emission mask

In addition to the spectrum emission mask requirement in Table 6.6.2F.1-1 a category NB1 or NB2 UE shall also meet the applicable E-UTRA spectrum emission mask requirement in sub-clause 6.6.2. E-UTRA spectrum emission requirement applies for frequencies that are Foffset away from edge of NB1 or NB2 channel edge as defined in Table 6.6.2F.1-2.

Table 6.6.2F.1-2: Foffset for category NB1 and NB2 UE spectrum emission mask

Note:Foffset in Table 6.6.2F.1-2 is used to guarantee co-existence for guard-band operation.

## 6.6.2F.2Additional Spectrum Emission Mask for Category NB1 and NB2

This requirement is specified in terms of an "additional spectrum emission" requirement.

## 6.6.2F.2.1Minimum requirement (network signalled value "NS_02")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell broadcast message.

When "NS_02" is indicated in the cell, the NB-IoT channel is deployed in the lower guard-band of a 10MHz E-UTRA channel and the separation between the two channel centres is equal to 4.695 MHz. The power of any UE emission shall not exceed the levels specified in Table 6.6.2.1.1-1 for the specified E-UTRA channel bandwidth and the levels specified in Table 6.6.2F.1-1 for the NB-IoT channel.

Note:UEs that meet the above emission requirement would automatically meet the E-UTRA additional spectrum emission masks as defined in 6.6.2.2 for the applicable operating bands.

## 6.6.2F.2.2Minimum requirement (network signalled value "NS_03")

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell broadcast message.

When "NS_03" is indicated in the cell, the NB-IoT channel is deployed in the upper guard-band of a 10MHz E-UTRA channel and the separation between the two channel centres is equal to 4.695 MHz. The power of any UE emission shall not exceed the levels specified in Table 6.6.2.1.1-1 for the specified E-UTRA channel bandwidth and the levels specified in Table 6.6.2F.1-1 for the NB-IoT channel.

Note:UEs that meet the above emission requirement would automatically meet the E-UTRA additional spectrum emission masks as defined in 6.6.2.2 for the applicable operating bands.

## 6.6.2F.3Adjacent Channel Leakage Ratio for category NB1 and NB2

Adjacent Channel Leakage power Ratio is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency. The assigned category NB1or NB2 channel power and adjacent channel power are measured with filters and measurement bandwidths specified in Table 6.6.2F.3-1. If the measured adjacent channel power is greater than –50dBm then the category NB1 or NB2 UE ACLR shall be higher than the value specified in Table 6.6.2F.3-1. GSMACLR requirement is intended for protection of GSM system. UTRAACLR requirement is intended for protection of UTRA and E-UTRA systems.

Table 6.6.2F.3-1: category NB1 and NB2 UE ACLR requirements

## 6.6.2GOut of band emission for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the requirements in subclause 6.6.2 apply except for the ACLR requirements for power class 2 V2X UE.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.6.2 apply per V2X sidelink transmission and E-UTRA uplink transmission as specified for the corresponding inter-band concurrent operation with uplink assigned to two bands.

For intra-band contiguous multi-carrier operation, the general CA spectrum emission mask for CA Bandwidth Class B specified in subclause 6.6.2.1A shall apply for V2X Bandwdith Class B, the general CA spectrum emission mask for CA Bandwidth Class C specified in subclause 6.6.2.1A shall apply for V2X Bandwdith Class C and C1.

For intra-band contiguous multi-carrier operation, the E-UTRA ACLR requirment for CA Bandwidth Class B specified in subclause 6.6.2.3.3A shall apply for V2X Bandwdith Class B, the general CA spectrum emission mask for CA Bandwidth Class C specified in subclause 6.6.2.3.3A shall apply for V2X Bandwdith Class C and C1.

For power class 2 V2X UE, the assigned channel power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.6.2G-1. If the measured adjacent channel power is greater than –50dBm then ACLR shall be higher than the value specified in Table 6.6.2G-1.

Table 6.6.2G-1: ACLR requirements for power class 2 V2X Communication

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the requirements specified for single carrier apply to each transmit antenna connector.

If V2X UE transmits on one antenna connector at a time, the requirements specified for single carrier shall  apply to the active antenna connector.

## 6.6.3Spurious emissions

Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products, but exclude out of band emissions unless otherwise stated. The spurious emission limits are specified in terms of general requirements inline with SM.329 [2] and E-UTRA operating band requirement to address UE co-existence.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.6.3.1Minimum requirements

Unless otherwise stated, the spurious emission limits apply for the frequency ranges that are more than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth. The spurious emission limits in Table 6.6.3.1-2 apply for all transmitter band configurations (NRB) and channel bandwidths.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

Table 6.6.3.1-1: Boundary between E-UTRA out of band and spurious emission domain

Table 6.6.3.1-2: Spurious emissions limits

## 6.6.3.1AMinimum requirements for CA

This clause specifies the spurious emission requirements for carrier aggregation.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the spurious emission requirement Table 6.6.3.1-2 apply for the frequency ranges that are more than FOOB as defined in Table 6.6.3.1-1 away from edges of the assigned channel bandwidth on a component carrier. If for some frequency a spurious emission requirement of individual component carrier overlaps with the spectrum emission mask or channel bandwidth of another component carrier then it does not apply.

NOTE:For inter-band carrier aggregation with uplink assigned to two E-UTRA bands the requirements in Table 6.6.3.1-2 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.6.3.1-2 would be considered to be verified by the measurements verifying the one uplink inter-band CA spurious emission requirement.

For intra-band contiguous carrier aggregation the spurious emission limits apply for the frequency ranges that are more than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth (Table 5.6A-1). For frequencies ΔfOOB greater than FOOB as specified in Table 6.6.3.1A-1the spurious emission requirements in Table 6.6.3.1-2 are applicable.

Table 6.6.3.1A-1: Boundary between E-UTRA out of band and spurious emission domain for intra-band contiguous carrier aggregation

For intra-band non-contiguous carrier aggregation transmission the spurious emission requirement is defined as a composite spurious emission requirement. Composite spurious emission requirement applies to frequency ranges that are more than FOOB away from the edges of the sub-blocks. Composite spurious emission requirement is defined as follows

a)Composite spurious emission requirement is a combination of individual sub-block spurious emission requirements

b)In case the sub-block consist of one component carrier the sub-lock spurious emission requirement and FOOB are defined in subclause 6.6.3.1

c)If for some frequency an individual sub-block spurious emission requirement overlaps with the general spectrum emission mask or the sub-block bandwidth of another sub-block then it does not apply

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band), the spurious emission requirememnt is defined as follows. For the E-UTRA band supporting one component carrier the requirements in Table 6.6.3.1-2 apply for frequency ranges that are more than FOOB (MHz) from the edges of assigned channel bandwidth as defined in Table 6.6.3.1-1. For the E-UTRA band supporting two contiguous component carriers the requirements in Table 6.6.3.1-2 apply for frequency ranges that are more than FOOB (MHz) from the edges of assigned aggregated channel bandwidth as defined in Table 6.6.3.1A-1. If for some frequency a spurious emission requirement of a single component carrier or two contiguous component carriers overlap with the spurious emission requirement or channel bandwidth of another component carrier or two contiguously aggregated carriers then it does not apply.

## 6.6.3.2Spurious emission band UE co-existence

This clause specifies the requirements for the specified E-UTRA band, for coexistence with protected bands.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

Table 6.6.3.2-1: Requirements

NOTE:The restriction on the maximum uplink transmission to 54 RB in Notes 21, 22, and 27 of Table 6.6.3.2-1 and the restriction on the single-tone uplink transmission to sub-carrier index > 2 in Note 44 of Table 6.6.3.2-1 are intended for conformance testing and may be applied to network operation to facilitate coexistence when the aggressor and victim bands are deployed in the same geographical area. The applicable spurious emission requirement of -15.5 dBm/5MHz is a least restrictive technical condition for FDD/TDD coexistence and may have to be revised in the future.

When "NS_33" or “NS 34” is configured from pre-configured radio parameters or the cell and the indication from upper layers has indicated that the UE is within the protection zone of CEN DSRC devices or HDR DSRC devices, the power of any V2X UE emission shall fulfil either one of the two set of conditions.

## 6.6.3.2ASpurious emission band UE co-existence for CA

This clause specifies the additional requirements for inter-band uplink carrier aggregation configurations with the single CC uplink assigned to two E-UTRA bands for coexistence with protected bands for the specified uplink carrier aggregation configurations in Table 6.6.3.2A-0. The intersection of the requirements for the individual bands specified in clause 6.6.3.2 shall also apply for the specified uplink carrier aggregation configurations. Intersection of a requirement means that both UL constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

As exceptions, the additional requirements in Table 6.6.3.2A-0 apply on each component carrier with all component carriers are active.

NOTE 1:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

NOTE 2:For inter-band carrier aggregation with uplink assigned to two E-UTRA bands the requirements in Table 6.6.3.2A-0 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.6.3.2A-0 and in clause 6.6.3.2 would be considered to be verified by the measurements verifying the one uplink inter-band CA UE to UE co-existence requirements.

Table 6.6.3.2A-0: Requirements for uplink inter-band carrier aggregation (two bands)

Table 6.6.3.2A-1: Requirements for intraband carrier aggregation

Table 6.6.3.2A-2: Requirements for intraband non-contiguous CA

## 6.6.3.3Additional spurious emissions

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.6.3.3.1 Minimum requirement (network signalled value "NS_05")

When "NS_05" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.1-1: Additional requirements (PHS)

Table 6.6.3.3.1-2: Void

## 6.6.3.3.2 Minimum requirement (network signalled value “NS_07”)

When "NS_07" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.2-1: Additional requirements

## 6.6.3.3.3 Minimum requirement (network signalled value “NS_08”)

When “NS 08” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.3-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.3-1: Additional requirement

## 6.6.3.3.4 Minimum requirement (network signalled value “NS_09”)

When “NS 09” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.4-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.4-1: Additional requirement

NOTE 1:Void.

NOTE 2:To improve measurement accuracy, A-MPR values for NS_09 specified in Table 6.2.4-1 in subclause 6.2.4 are derived based on 100 kHz RBW.

## 6.6.3.3.5 Minimum requirement (network signalled value "NS_12")

When “NS 12” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.5-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.5-1: Additional requirements

## 6.6.3.3.6 Minimum requirement (network signalled value “NS_13”)

When “NS 13” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.6-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.6-1: Additional requirements

## 6.6.3.3.7 Minimum requirement (network signalled value “NS_14”)

When “NS 14” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.7-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.7-1: Additional requirements

## 6.6.3.3.8 Minimum requirement (network signalled value “NS_15”)

When “NS 15” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.8-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.8-1: Additional requirements

## 6.6.3.3.9 Minimum requirement (network signalled value “NS_16”)

When “NS_16” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.9-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.9-1: Additional requirements

## 6.6.3.3.10 Minimum requirement (network signalled value “NS_17”)

When “NS_17” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.10-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.10-1: Additional requirements

## 6.6.3.3.11 Minimum requirement (network signalled value “NS_18”)

When “NS_18” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.11-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.11-1: Additional requirements

## 6.6.3.3.12 Minimum requirement (network signalled value “NS_19”)

When “NS_19” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.12-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.12-1: Additional requirements

## 6.6.3.3.13 Minimum requirement (network signalled value “NS_11”)

When “NS_11” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.13-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 and Table 6.6.3.1A-1 from the edge of the channel bandwidth.

Table 6.6.3.3.13-1: Additional requirements

## 6.6.3.3.14Minimum requirement (network signalled value “NS_20”)

When “NS_20” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.14-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 and Table 6.6.3.1A-1 from the edge of the channel bandwidth.

Table 6.6.3.3.14-1: Additional requirements

## 6.6.3.3.15Minimum requirement (network signalled value “NS_21”)

When “NS_21” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.15-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 and Table 6.6.3.1A-1 from the edge of the channel bandwidth.

Table 6.6.3.3.15-1: Additional requirements

## 6.6.3.3.16Minimum requirement (network signalled value "NS_22")

When "NS 22" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.16-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.16-1: Additional requirement

## 6.6.3.3.17Minimum requirement (network signalled value “NS_23”)

When "NS 23" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.17-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.17-1: Additional requirement

## 6.6.3.3.18Void

Table 6.6.3.3.18-1: Void

## 6.6.3.3.19Minimum requirement (network signalled value "NS_04")

When "NS 04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.19-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.19-1: Additional requirements

## 6.6.3.3.20Minimum requirement (network signalled value “NS_24”)

When "NS_24" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.20-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.20-1: Additional requirements

## 6.6.3.3.21Minimum requirement (network signalled value “NS_25”)

When "NS_25" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.21-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.21-1: Additional requirements

## 6.6.3.3.22Minimum requirement (network signalled value “NS_26”)

When "NS_26" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.22-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.22-1: Additional requirements

## 6.6.3.3.23Minimum requirement (network signalled value “NS_27” and “NS_43”)

When "NS_27" or “NS_43” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.23-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.23-1: Additional requirements

## 6.6.3.3.24Minimum requirement (network signalled value “NS_28”)

When "NS_28" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 5150-5350 MHz and 5470-5725 MHz shall not exceed the levels specified in Table 6.6.3.3.24-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.24-1: Additional requirements

## 6.6.3.3.25Minimum requirement (network signalled value “NS_29”)

When "NS_29" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 5150-5350 and 5470-5725 MHz shall not exceed the levels specified in Table 6.6.3.3.25-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.25-1: Additional requirements

## 6.6.3.3.26Minimum requirement (network signalled value “NS_30”)

When "NS_30" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 5150-5350 MHz, 5470-5725 MHz and 5725-5850 MHz shall not exceed the levels specified in Table 6.6.3.3.26-1, Table 6.6.3.3.26-2 and Table 6.6.3.3.26-3, respectively. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.26-1: Additional requirements for E-UTRA channels assigned within 5150-5350 MHz

Table 6.6.3.3.26-2: Additional requirements for E-UTRA channels assigned within 5470-5725 MHz

Table 6.6.3.3.26-3: Additional requirements for E-UTRA channels assigned within 5725-5850 MHz

## 6.6.3.3.27Minimum requirement (network signalled value “NS_31”)

When "NS_31" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 5150-5250 MHz, 5250-5350 MHz, 5470-5725 MHz and 5725-5850 MHz shall not exceed the levels specified in Table 6.6.3.3.27-1, Table 6.6.3.3.27-2, Table 6.6.3.3.27-3 and Table 6.6.3.3.27-4, respectively. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.27-1: Additional requirements for E-UTRA channels assigned within 5150-5250 MHz

Table 6.6.3.3.27-2: Additional requirements for E-UTRA channels assigned within 5250-5350 MHz

Table 6.6.3.3.27-3: Additional requirements for E-UTRA channels assigned within 5470-5725 MHz

Table 6.6.3.3.27-4: Additional requirements for E-UTRA channels assigned within 5725-5850 MHz

## 6.6.3.3.28Minimum requirement (network signalled value “NS_36”)

When "NS_36" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.28-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.28-1: Additional requirements

## 6.6.3.3.29Minimum requirement (network signalled value “NS_38”)

When "NS_38" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.29-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.29-1: Additional requirements

## 6.6.3.3.30Minimum requirement (network signalled value “NS_39”)

When "NS_39" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.30-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.30-1: Additional requirements

## 6.6.3.3.31Minimum requirement (network signalled value “NS_40” and “NS_41”)

When "NS_40" or "NS_41" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 1427-1432MHz (B51) and 1432-1452MHz (B50) shall not exceed the levels specified in Table 6.6.3.3.31-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.31-1: Additional requirements for E-UTRA channels assigned within 1427-1452MHz

## 6.6.3.3.32Minimum requirement (network signalled value “NS_42”)

When "NS_42" is indicated in the cell, the power of any UE emission for E-UTRA channels assigned within 1492-1517 MHz (B50) shall not exceed the levels specified in Table 6.6.3.3.32-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.32-1: Additional requirements for E-UTRA channels assigned within 1492-1517 MHz

## 6.6.3.3.33Minimum requirement (network signalled value “NS_44”)

When "NS_44" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.33-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.33-1: Additional requirements

## 6.6.3.3.34Minimum requirement (network signalled value “NS_45”)

When "NS_45" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Tables 6.6.3.3.35-1 and 6.6.3.3.35-2. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.34-1: Additional requirements for 1.4, 3 and 5 MHz channel bandwidths

Table 6.6.3.3.34-2: Additional requirements for 10 MHz channel bandwidth

## 6.6.3.3.35Minimum requirement (network signalled value “NS_56”)

When "NS_56" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.35-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.35-1: Additional requirements

## 6.6.3.3.36Minimum requirement (network signalled value “NS_62”)

When "NS_62" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3.36-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3.3.36-1: Additional requirements

## 6.6.3.3AAdditional spurious emissions for CA

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell reconfiguration message.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.6.3.3A.1Minimum requirement for CA_1C (network signalled value "CA_NS_01")

When "CA_NS_01" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.1-1: Additional requirements (PHS)

## 6.6.3.3A.2 Minimum requirement for CA_1C (network signalled value "CA_NS_02")

When "CA_NS_02" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.2-1: Additional requirements

## 6.6.3.3A.3Minimum requirement for CA_1C (network signalled value "CA_NS_03")

When "CA_NS_03" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.3-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.3-1: Additional requirements

## 6.6.3.3A.4Minimum requirement for CA_38C (network signalled value "CA_NS_05")

When "CA_NS_05" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.4-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth. This requirement is applicable for carriers with aggregated channel bandwidths confined in 2570 - 2615 MHz.

Table 6.6.3.3A.4-1: Additional requirements

## 6.6.3.3A.5Minimum requirement for CA_7C (network signalled value "CA_NS_06")

When "CA_NS_06" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.5-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.5-1: Additional requirements

## 6.6.3.3A.6Minimum requirement for CA_39C and CA_39C-41A (network signalled value "CA_NS_07")

When "CA_NS_07" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.6-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.6-1: Additional requirements

## 6.6.3.3A.7Minimum requirement for CA_42C (network signalled value "CA_NS_08")

When "CA_NS_08" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.7-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.7-1: Additional requirements

## 6.6.3.3A.8Minimum requirement for CA_41C and CA_41D (network signalled value "CA_NS_04")

When "CA_NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.8-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.8-1: Additional requirements

## 6.6.3.3A.9Void

## 6.6.3.3A.10Minimum requirement for CA_48B and CA_48C (network signalled value "CA_NS_10")

When "CA_NS_10" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.10-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.10-1: Additional requirements

## 6.6.3.3A.11Minimum requirement for CA_28C (network signalled value "CA_NS_12")

When "CA_NS_12" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.11-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.11-1: Additional requirements

## 6.6.3.3A.12Minimum requirement for CA_28C (network signalled value "CA_NS_13")

When "CA_NS_13" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3.3A.12-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1A-1 from the edge of the aggregated channel bandwidth.

Table 6.6.3.3A.12-1: Additional requirements

## 6.6.3AVoid

<reserved for future use>

## 6.6.3BSpurious emission for UL-MIMO

For UE supporting UL-MIMO, the requirements for Spurious emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products are specified at each transmit antenna connector.

For UEs with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements in subclause 6.6.3 apply to each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-1.

If UE is configured for transmission on single-antenna port, the general requirements in subclause 6.6.3 apply.

## 6.6.3CVoid

<reserved for future use>

## 6.6.3DSpurious emission for ProSe

When UE is configured for E-UTRA ProSe sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the requirements in subclause 6.6.3 apply.

When UE is configured for simultaneous E-UTRA ProSe sidelink and E-UTRA uplink transmissions for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, the UE co-existence requirements in Table 6.6.3.2A-0 in subclause 6.6.3.2A apply as specified for the corresponding inter-band aggregation with uplink assigned to two bands.

## 6.6.3FSpurious emission for category NB1 and NB2

When UE is configured for category NB1 or NB2 uplink transmissions the requirements in subclause 6.6.3 apply with an exception that boundary between category NB1 or NB2 out of band and spurious emission domain shall be FOOB = 1.7 MHz.

## 6.6.3F.1Additional spurious emissions

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.6.3F.1.2 Minimum requirement (network signalled value "NS_06")

When "NS_06" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3F.1.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3F.1.2-1 from the edge of the channel bandwidth.

Table 6.6.3F.1.2-1: Additional requirements

## 6.6.3GSpurious emission for V2X Communication

This clause specifies the additional requirements for inter-band concurrent V2X operation with the single CC uplink assigned to two E-UTRA bands for coexistence with protected bands for the specified simultaneous transmission of the inter-band concurrent V2X configurations in Table 6.6.3G-0. The intersection of the requirements for the individual bands specified in clause 6.6.3.2 shall also apply for the specified simultaneous transmission of the inter-band concurrent V2X. Intersection of a requirement means that both UL or sidelink transmission constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the requirements in subclause 6.6.3 apply.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the UE-coexistence requirements in Table 6.6.3G-0 in subclause 6.6.3G apply as as specified for the corresponding inter-band concurrent operation with uplink assigned to two bands.

NOTE:For inter-band concurrent V2X operation with uplink assigned to E-UTRA band and slidelink transmission assigned to E-UTRA V2X operating bands, the requirements in Table 6.6.3G-0 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.6.3G-0 and in clause 6.6.3.2 would be considered to be verified by the measurements verifying the one uplink inter-band concurrent UE to UE co-existence requirements.

Table 6.6.3G-0: Requirements for inter-band concurrent V2X operation

For intra-band contiguous multi-carrier operation, the boundary between E-UTRA out of band and spurious emission domain for intra-band contiguous carrier aggregation specified in Table 6.6.3.1A-1 shall apply.

For intra-band contiguous multi-carrier operation, the spurious emission requirements in Table 6.6.3G-1 shall apply for coexistence with protected bands.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

Table 6.6.3G-1: Requirements for intraband multi-carrier V2X operation

For V2X UEs supportingTransmit Diversity, the requirements specified for single carrier shall apply to each transmit antenna connector.

If V2X UE is configured for transmission on single-antenna connector, the general requirements specified for single carrier shall apply to the active antenna connector.

## 6.6.3KSpurious emission for Aerial UE

When "NS_UAV_46" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3K-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3K-1: Additional requirements for "NS_UAV_46"

When "NS_UAV_44" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3K-2. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3K-2: Additional requirements for "NS_UAV_44"

When "NS_UAV_70" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.6.3K-3. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.6.3K-3: Additional requirements for "NS_UAV_70"

## 6.6AVoid

## 6.6BVoid

## 6.7Transmit intermodulation

The transmit intermodulation performance is a measure of the capability of the transmitter to inhibit the generation of signals in its non linear elements caused by presence of the wanted signal and an interfering signal reaching the transmitter via the antenna.

## 6.7.1Minimum requirement

User Equipment(s) transmitting in close vicinity of each other can produce intermodulation products, which can fall into the UE, or eNode B receive band as an unwanted interfering signal. The UE intermodulation attenuation is defined by the ratio of the mean power of the wanted signal to the mean power of the intermodulation product when an interfering CW signal is added at a level below the wanted signal at each of the transmitter antenna port with the other antenna port(s) if any is terminated. Both the wanted signal power and the intermodulation product power are measured through E-UTRA rectangular filter with measurement bandwidth shown in Table 6.7.1-1.

The requirement of transmitting intermodulation is prescribed in Table 6.7.1-1.

Table 6.7.1-1: Transmit Intermodulation

## 6.7.1AMinimum requirement for CA

User Equipment(s) transmitting in close vicinity of each other can produce intermodulation products, which can fall into the UE, or eNode B receive band as an unwanted interfering signal. The UE intermodulation attenuation is defined by the ratio of the mean power of the wanted signal to the mean power of the intermodulation product on both component carriers when an interfering CW signal is added at a level below the wanted signal at each of the transmitter antenna port with the other antenna port(s) if any is terminated. Both the wanted signal power and the intermodulation product power are measured through rectangular filter with measurement bandwidth shown in Table 6.7.1A-1.

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the requirement is specified in Table 6.7.1-1 which shall apply on each component carrier with both component carriers active.

For intra-band contiguous carrier aggregation the requirement of transmitting intermodulation is specified in Table 6.7.1A-1.

Table 6.7.1A-1: Transmit Intermodulation

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per band) transmit intermodulations is defined as follows. For the E-UTRA band supporting one component carrier the requirement specified in Table 6.7.1-1 apply. For the E-UTRA band supporting two contiguous component carriers the requirements specified in Table 6.7.1A-1 apply.

## 6.7.1BMinimum requirement for UL-MIMO

For UE supporting UL-MIMO, the transmit intermodulation requirements are specified at each transmit antenna connector and the wanted signal is defined as the sum of output power at each transmit antenna connector.

For UEs with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements in subclause 6.7.1 apply to each transmit antenna connector. The requirements shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2.

If UE is configured for transmission on single-antenna port, the requirements in subclause 6.7.1 apply.

## 6.7.1FMinimum requirement for category NB1 and NB2

The UE category NB1 and NB2 transmitter intermodulation attenuation is defined by the ratio of the mean power of the wanted signal to the mean power of the intermodulation product as defined in Table 6.7.1F-1 when an interfering CW signal is added at a level below the wanted signal at the transmitter antenna port. Both the wanted signal power and the intermodulation product power are measured through rectangular filter with measurement bandwidth shown in Table 6.7.1F-1.

Table 6.7.1F-1: UE category NB1 and NB2 transmitter IM requirement

## 6.7.1GMinimum requirement for V2X Communication

When UE is configured for E-UTRA V2X sidelink transmissions non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table Table 5.5G-1, the requirements in subclause 6.7.1 apply for E-UTRA V2X sidelink transmission.

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA uplink transmissions for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 6.7.1 apply for V2X sidelink transmission and the E-UTRA uplink transmission.

For intra-band contiguous multi-carrier operation, the transmit intermodulation requirement for CA Bandwidth Class B specified in subclause 6.7.1A shall apply for V2X Bandwdith Class B, the general CA spectrum emission mask for CA Bandwidth Class C specified in subclause 6.7.1A shall apply for V2X Bandwdith Class C and C1.

For V2X UE supporting Transmit Diversity, if the UE transmits on two antenna connectors at the same time, the requirements specified for single carrier shall apply to each transmit antenna connector. If the UE transmits on one antenna connector, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.8Void

## 6.8AVoid

## 6.8BTime alignment error for UL-MIMO

For UE(s) with multiple transmit antenna connectors supporting UL-MIMO, this requirement applies to frame timing differences between transmissions on multiple transmit antenna connectors in the closed-loop spatial multiplexing scheme.

The time alignment error (TAE) is defined as the average frame timing difference between any two transmissions on different transmit antenna connectors.

## 6.8B.1Minimum Requirements

For UE(s) with multiple transmit antenna connectors, the Time Alignment Error (TAE) shall not exceed 130 ns.

## 6.8CVoid

## 6.8DVoid

## 6.8EVoid

## 6.8FVoid

## 6.8GTime alignment error

For V2X UE(s) with two  transmit antenna connectors in Transmit Diversity scheme, this requirement applies to frame timing differences between transmissions on two transmit antenna connectors.The Time Alignment Error (TAE) shall not exceed [260] ns.

## 7Receiver characteristics

## 7.1General

Unless otherwise stated the receiver characteristics are specified at the antenna connector(s) of the UE. For UE(s) with an integral antenna only, a reference antenna(s) with a gain of 0 dBi is assumed for each antenna port(s). UE with an integral antenna(s) may be taken into account by converting these power levels into field strength requirements, assuming a 0 dBi gain antenna. . For UEs with more than one receiver antenna connector, identical interfering signals shall be applied to each receiver antenna port if more than one of these is used (diversity).

The levels of the test signal applied to each of the antenna connectors shall be as defined in the respective sections below.

With the exception of subclause 7.3, the requirements shall be verified with the network signalling value NS_01 configured (Table 6.2.4-1).

All the parameters in clause 7 are defined using the UL reference measurement channels specified in Annexes A.2.2 and A.2.3, the DL reference measurement channels specified in Annex A.3.2 and using the set-up specified in Annex C.3.1.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks, an in-gap test refers to the case when the interfering signal is located at a negative offset with respect to the assigned lowest channel frequency of the highest sub-block and located at a positive offset with respect to the assigned highest channel frequency of the lowest sub-block.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks, an out-of-gap test refers to the case when the interfering signal(s) is (are) located at a positive offset with respect to the assigned channel frequency of the highest carrier frequency, or located at a negative offset with respect to the assigned channel frequency of the lowest carrier frequency.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks with channel bandwidth larger than or equal to 5 MHz, the existing adjacent channel selectivity requirements, in-band blocking requirements (for each case), and narrow band blocking requirements apply for in-gap tests only if the corresponding interferer frequency offsets with respect to the two measured carriers satisfy the following condition in relation to the sub-block gap size Wgap for at least one of these carriers j = 1,2, so that the interferer frequency position does not change the nature of the core requirement tested:

Wgap ≥ 2∙|FInterferer (offset),j|  – BWChannel(j)

where FInterferer (offset),j for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier j as specified in subclause 7.5.1, subclause 7.6.1 and subclause 7.6.3 for the respective requirement and BWChannel(j) the channel bandwidth of carrier j. FInterferer (offset),j for a sub-block with two or more contiguous component carriers is the interference frequency offset with respect to the carrier adjacent to the gap is specified in subclause 7.5.1A, 7.6.1A and 7.6.3A. The interferer frequency offsets for adjacent channel selectivity, each in-band blocking case and narrow- band blocking shall be tested separately with a single in-gap interferer at a time.

For a ProSe UE that supports both ProSe Direct Discovery and ProSe Direct Communication, the receiver characteristics specified in clause 7 for ProSe Direct Communication shall apply.

For ProSe Direct Discovery and ProSe Direct Communication on E-UTRA ProSe operating bands that correspond to TDD E-UTRA operating bands as specified in subclause 5.5D, the only additional requirement for ProSe specified in subcaluse 7.4.1D is applicable.

## 7.2Diversity characteristics

The requirements in Section 7 assume that the receiver is equipped with two Rx port as a baseline. These requirements apply to all UE categories unless stated otherwise. Additional requirements apply for UE(s) equipped with four Rx ports. These additional requirements also apply for supported band combinations for which the UE can operate using up to four Rx ports while configured with carrier aggregation. With the exception of subclause 7.9 all requirements shall be verified by using both (all) antenna ports simultaneously.

NOTE:for an operating band in which the UE can operate using up to four Rx ports, it suffices to verify for conformance the additional requirements applicable for four Rx ports [except for REFSENS].

NOTE:Implementation of 4 antenna ports for all operating bands supported by the UE is not mandated.

For a category 0, a category [M 1] , category 1bis, category NB1 and NB2 UE the requirements in Section 7 assume that the receiver is equipped with single Rx port.

## 7.3Reference sensitivity power level

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports for all UE categories except category 0, category M1, category M2, and category 1bis, or to the single antenna port for UE category 0, UE category M1, category M2, and UE category 1bis, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

The throughput for the REFSENS test is measured based on the Transmission Mode 1 unless specified otherwise.

## 7.3.1Minimum requirements (QPSK)

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1-1 and Table 7.3.1-2

Table 7.3.1-1: Reference sensitivity QPSK PREFSENS

For UE(s) equipped with 4 antenna ports, the minimum requirement for reference sensitivity in Table 7.3.1-1 shall be modified by the amount given in ΔRIB,4R in Table 7.3.1-1a for the applicable E-UTRA bands.

Table 7.3.1-1a: ΔRIB,4R

For UE(s) equipped with 8 antenna ports, the minimum requirement for reference sensitivity in Table 7.3.1-1 shall be modified by the amount given in ΔRIB,8R in Table 7.3.1-1aa for the applicable E-UTRA bands.

Table 7.3.1-1aa: ΔRIB,8R

For UE(s) supporting power class 1 in any of the E-UTRA bands given in table 7.3.1-1b, the following exceptions due to the high power leakage or blocking issue shall apply. The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1-1b and Table 7.3.1-2.

Table 7.3.1-1b: Reference sensitivity for power class 1 QPSK PREFSENS (Exception due to high power issue)

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3.1-1 (two antenna ports) and Table 7.3.1-1a (four antenna ports) shall be met for an uplink transmission bandwidth less than or equal to that specified in Table 7.3.1-2.

NOTE:Table 7.3.1-2 is intended for conformance tests and does not necessarily reflect the operational conditions of the network, where the number of uplink and downlink allocated resource blocks will be practically constrained by other factors. Typical receiver sensitivity performance with HARQ retransmission enabled and using a residual BLER metric relevant for e.g. Speech Services is given in the Annex G (informative).For the UE which supports inter-band carrier aggregation configuration with the uplink in one or two E-UTRA bands, the minimum requirement for reference sensitivity in Table 7.3.1-1 and Table 7.3.1-1a shall be increased by the amount given in ΔRIB,c in Table 7.3.1-1A, Table 7.3.1-1B and Table 7.3.1-1C for the applicable E-UTRA bands where unless otherwise stated, the same ΔRIB,c is applicable to E-UTRA band(s) part for CA configurations which have the same E-UTRA operating band combination.

Table 7.3.1-1A: ΔRIB,c (two bands)

NOTE:To meet the RIB,c requirements for CA_20A-28A state-of-the-art filter combiner technology is needed.

Table 7.3.1-1B: ΔRIB,c (three bands)

Table 7.3.1-1C: ΔRIB,c (four bands)

Table 7.3.1-1D: ΔRIB,c (five bands)

NOTE :The above additional tolerances do not apply to supported UTRA operating bands with frequency range below 1 GHz that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations when such bands are belonging only to band combination(s) where one band is <1GHz and other bands are >1.7GHz and there is no harmonic relationship between the low band UL and high band DL. Otherwise the above additional tolerances also apply to supported UTRA operating bands that correspond to the E-UTRA operating bands that belong to the supported inter-band carrier aggregation configurations.

Table 7.3.1-1E: ΔRIB,c (six bands)

Table 7.3.1-2: Uplink configuration for reference sensitivity

Unless given by Table 7.3.1-3, the minimum requirements specified in Tables 7.3.1-1, 7.3.1-1a and 7.3.1-2 shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

Table 7.3.1-3: Network signalling value for reference sensitivity

## 7.3.1AMinimum requirements (QPSK) for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1-1, Table 7.3.1-1a and Table 7.3.1-2. The reference sensitivity is defined to be met with all downlink component carriers active and one of the uplink carriers active. The uplink resource blocks shall be located as close as possible to the primary downlink operating band but confined within the transmission bandwidth configuration for the channel bandwidth (Table 5.6-1). The primary downlink operating band is the downlink band of the active uplink operating band. The UE shall meet the requirements specified in subclause 7.3.1 with the following exceptions.

For the bands supporting 4 antenna ports which are in Table 7.3.1-1a, the minimum requirements for reference sensitivity in the reference sensitivity exception tables shall be modified by the amount given in ΔRIB,4R in Table 7.3.1-1a for the applicable E-UTRA bands unless otherwise specified.

For the bands supporting 8 antenna ports which are in Table 7.3.1-1aa, the minimum requirements for reference sensitivity in the reference sensitivity exception tables shall be modified by the amount given in ΔRIB,8R in Table 7.3.1-1aa for the applicable E-UTRA bands unless otherwise specified.

For the UE that supports any of the E-UTRA CA configurations given in Table 7.3.1A-0a, exceptions to the requirements for a band(s) specified in subclause 7.3.1 are allowed when the band(s) is impacted by harmonic interference from the uplink transmission in a lower-frequency band of the same CA configuration. For these exceptions, the UE shall meet the requirements specified in Table 7.3.1A-0a and Table 7.3.1A-0b. These exceptions also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

Table 7.3.1A-0a: Reference sensitivity for carrier aggregation QPSK PREFSENS, CA (exceptions due to harmonic issue)

Table 7.3.1A-0b: Uplink configuration for the low band (exceptions due to harmonic issue)

For the UE that supports any of the E-UTRA CA configurations given in Table 7.3.1A-0bA, exceptions to the requirements for a band(s) specified in subclause 7.3.1 are allowed when the band(s) is impacted by the uplink being active within a specified frequency range as noted in Table 7.3.1A-0bA. For these exceptions, the UE shall meet the requirements specified in Table 7.3.1A-0bA and Table 7.3.1A-0bB. These exceptions also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

Table 7.3.1A-0bA: Reference sensitivity for carrier aggregation QPSK PREFSENS, CA (exceptions for two bands due to close proximity of UL to DL channel)

Table 7.3.1A-0bB: Uplink configuration for the uplink band (exceptions for two bands due to close proximity of UL to DL channel)

Table 7.3.1A-0bC: Void

Table 7.3.1A-0bD: Void

Table 7.3.1A-0bD1: Void

Table 7.3.1A-0bD2: Void

Table 7.3.1A-0bD3: Void

Table 7.3.1A-0bD4: Void

or the UE that supports any of the E-UTRA CA configurations given in Table 7.3.1A-0bE, exceptions to the requirements for a band(s) specified in subclause 7.3.1 are allowed when the band(s) is impacted by uplink being active in the applicable active UL bands of the same CA configuration in Table 7.3.1A-0bE. For these exceptions, the UE shall meet the reference sensitivities specified in Table 7.3.1A-0bE and Table 7.3.1A-0bF. These exceptions also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

Table 7.3.1A-0bE: Reference sensitivity for carrier aggregation QPSK PREFSENS, CA (exceptions due to cross band isolation issues of TDD and FDD bands)

Table 7.3.1A-0bF: Uplink configuration for reference sensitivity (exceptions due to cross band isolation issues of TDD and FDD bands)

For band combinations including operating bands without uplink band (as noted in Table 5.5-1), the requirements are specified in Table 7.3.1A-0d and for any uplink band with uplink configuration specified in Table 7.3.1-2. These requirements also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

Table 7.3.1A-0d: Reference sensitivity QPSK PREFSENS (CA with a SDL band)

Table 7.3.1A-0e: Void

For band combinations including operating band 46 (Table 5.5-1), the requirements are specified in Table 7.3.1A-0eA for the uplink in any band other than band 46 with the uplink configuration specified in Table 7.3.1-2 and Table 7.3.1A-0eC. These requirements also apply to any higher order CA or DC combination containing one of the combinations in this clause as subset.

For band combinations including operating band 49 (Table 5.5-1), the requirements are specified in Table 7.3.1A-0eA for the uplink in any band other than Band 49 with uplink configurations specified in Table 7.3.1-2 and measurement exclusion region in Table 7.3.1A-0eD. These requirements also apply to any higher order CA or DC combination containing one of the combinations in this clause as subset.

Table 7.3.1A-0eA: Reference sensitivity QPSK PREFSENS (CA with band 46 or Band 49)

Table 7.3.1A-0eB: Void

Table 7.3.1A-0eC specifies the Band 46 reference measurement exclusion region for different licensed component carriers and channel bandwidth. The exclusion region is defined according to the licensed component carrier channel bandwidth. The UL configurations to be adopted for the test are specified in Table 7.3.1-2. The exclusion region in Table 7.3.1A-0eC is specified for the case of 10MHz and 20MHz channel bandwidth in Band 46.

Table 7.3.1A-0eC: Band 46 Reference sensitivity measurement exclusion region in MHz.

Table 7.3.1A-0eD specifies the Band 49 reference measurement exclusion region for different licensed component carriers and channel bandwidth. The exclusion region is defined according to the licensed component carrier channel bandwidth. The UL configurations to be adopted for the test are specified in Table 7.3.1-2.

Table 7.3.1A-0eD: Band 49 reference sensitivity measurement exclusion region in MHz.

In all cases for single uplink inter-band CA, unless given by Table 7.3.1-3 for the band with the active uplink carrier, the applicable reference sensitivity requirements shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

For inter-band carrier aggregation with one component carrier per operating band (up to four downlinks) and the uplink assigned to two E-UTRA bands the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1-1, Table 7.3.1-1a and Table 7.3.1-2. The reference sensitivity is defined to be met with all downlink component carriers active and both of the uplink carriers active.

For E-UTRA CA configurations with uplink and downlink assigned to two E-UTRA bands given in Table 7.3.1A-0f, the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3.1A-0f. For E-UTRA CA configurations with uplink assigned to two E-UTRA bands and downlink assigned to three E-UTRA bands given in Table 7.3.1A-0g, the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3.1A-0g. For these test points the reference sensitivity requirement specified in Table 7.3.1-1 and Table 7.3.1-1a are relaxed by the amount of the corresponding parameter MSD given in Table 7.3.1A-0f and Table 7.3.1A-0g.

The allowed exceptions defined in Table 7.3.1A-0a and Table 7.3.1A-0b for inter-band carrier aggregation with a single active uplink are also applicable for dual uplink operation.

Table 7.3.1A-0f: 2DL/2UL interband Reference sensitivity QPSK PREFSENS and uplink/downlink configurations

Table 7.3.1A-0g: 3DL/2UL interband Reference sensitivity QPSK PREFSENS and uplink/downlink configurations

For intra-band contiguous carrier aggregation the throughput of each component carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1-1, Table 7.3.1-1a, Table 7.3.1-1A, Table 7.3.1-1B, Table 7.3.1-1C, Table 7.3.1A-0h and Table 7.3.1A-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the power levels in Table 7.3.1-1 and Table 7.3.1-1a also apply for an SCC assigned in the unpaired part. The requirement is verified using an uplink CA configuration with the largest number of carriers supported by the UE. Table 7.3.1A-0h, Table 7.3.1A-1 and Table 7.3.1A-2 specifies the maximum number of allocated uplink resource blocks for which the intra-band contiguous carrier aggregation reference sensitivity requirement shall be met. The PCC and SCC allocations as defined in Table 7.3.1A-0h, Table 7.3.1A-1 and Table 7.3.1A-2 form a contiguous allocation where TX–RX frequency separations of the component carriers are as defined in Table 5.7.4-1. In case downlink CA configuration has additional SCC(s) compared to uplink CA configuration those are configured furthers away from uplink band. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2 and the downlink PCC carrier center frequency shall be configured closer to uplink operating band than any of the downlink SCC center frequency. Unless given by Table 7.3.1-3, the reference sensitivity requirements shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

Table 7.3.1A-0h: Intra-band contiguous CA uplink configuration for reference sensitivity for Bandwidth Class B

Table 7.3.1A-1: Intra-band contiguous CA uplink configuration for reference sensitivity for Bandwidth Class C

Table 7.3.1A-2: Intra-band contiguous CA uplink configuration for reference sensitivity for Bandwidth Class D

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the throughput of each downlink component carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) and parameters specified in Table 7.3.1-1, Table 7.3.1-1a, Table 7.3.1-1A, Table 7.3.1-1B, Table 7.3.1-1C and Table 7.3.1A-3 with the reference sensitivity power level increased by  RIBNC given in Table 7.3.1A-3 for the SCC(s). For aggregation of more than two downlink FDD carriers with one uplink carrier the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3.1A-3. The requirements apply with all downlink carriers active. Unless given by Table 7.3.1-3, the reference sensitivity requirements shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

Table 7.3.1A-3: Intra-band non-contiguous CA with one uplink configuration for reference sensitivity

For intra-band non-contiguous carrier aggregation with two uplink and downlink carriers the reference sensitivity is defined to be met with both downlink and uplink carriers activated. The downlink PCC and SCC minimum requirements for reference sensitivity power level as specified in Table 7.3.1-1, Table 7.3.1-1a, Table 7.3.1-1A, Table 7.3.1-1B and Table 7.3.1-1C are increased by amount of ΔR2UL_PCC and ΔR2UL_SCC  which are defined in Table 7.3.1A-4 when uplink PCC and SCC allocations are according to the Table 7.3.1A-4.

Table 7.3.1A-4: Intra-band non-contiguous CA with two uplinks configuration for reference sensitivity

For combinations of intra-band and inter-band carrier aggregation, the requirement is defined with an uplink configuration in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contigous component carriers, Table 7.3.1A-1 when the uplink (up to two contiguously aggregated uplink carriers) is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when an uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. The carrier center frequency of PCC in the UL operating band is configured closer to the DL operating band when the uplink is active in band(s) supporting non-contiguous aggregation. For these uplink configurations, the UE shall meet the reference sensitivity requirements for intra-band non-contiguous carrier aggregation of two or more downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the requirements specified in subclause 7.3.1. For the two or more component carriers within the same band, RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) when the uplink is active in another band. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with all uplink carriers active in each band capable of UL operation. For component carriers configured in Band 46, the said requirements for intra-band carrier aggregation of downlink carriers are replaced by the requirements in Table 7.3.1A-0eA for the uplink in any band other than band 46 with the uplink configuration specified in Table 7.3.1-2. Unless given by Table 7.3.1-3, the reference sensitivity requirements shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

Table 7.3.1A-5: Void

Table 7.3.1A-6: Void

## 7.3.1BMinimum requirements (QPSK) for UL-MIMO

For UE with two transmitter antenna connectors in closed-loop spatial multiplexing scheme, the minimum requirements in Clause 7.3.1 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PUMAX is the total transmitter power over the two transmits power over the two transmit antenna connectors.

## 7.3.1DMinimum requirements (QPSK) for ProSe

When UE is configured for E-UTRA ProSe reception non-concurrent with E-UTRA uplink transmissions for E-UTRA ProSe operating bands specified in Table 5.5D-1, the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.6.2 with parameters specified in Table 7.3.1D-1 and Table 7.3.1D-2.

Table 7.3.1D-1: Reference sensitivity for ProSe Direct Discovery QPSK PREFSENS

Table 7.3.1D-2: Reference sensitivity for ProSe Direct Communication QPSK PREFSENS

NOTE:Table 7.3.1D-1/ Table 7.3.1D-2 is intended for conformance tests and does not necessarily reflect the operational conditions of the network, where the number of allocated resource blocks will be practically constrained by other factors.

For the UE which supports ProSe in an operating band as specified in Section 5.5D, and the UE also supports a E-UTRA downlink inter-band carrier aggregation configuration in Table 7.3.1-1A or Table 7.3.1-1B, the minimum requirement for reference sensitivity in Table 7.3.1D-1 and Table 7.3.1D-2 shall be increased by the amount given in ΔRIB,c in Table 7.3.1-1A and Table 7.3.1-1B for the corresponding E-UTRA ProSe band.

When UE is configured for E-UTRA ProSe reception on PCC for the inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, there are no further requirements for reference sensitivity beyond those specified above when only PCC is configured in Table 7.3.1D-1 and Table 7.3.1D-2.

When UE is configured for E-UTRA ProSe reception on SCC or a non-serving carrier concurrent with E-UTRA uplink for inter-band E-UTRA ProSe / E-UTRA bands specified in Table 5.5D-2, E-UTRA ProSe throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.6.2 with parameters specified in Table 7.3.1D-1 and Table 7.3.1D-2. The reference sensitivity is defined to be met with E-UTRA uplink assigned to one band (that differs from the ProSe operating band) and all E-UTRA downlink carriers active. The E-UTRA uplink resource blocks shall be located as close as possible to E-UTRA ProSe operating band but confined within the transmission bandwidth configuration for the channel bandwidth (Table 5.6-1). The uplink configuration for the E-UTRA operating band is specified in Table 7.3.1D-3.

NOTE:The E-UTRA uplink channel bandwidth and transmission bandwidth specified in this Table 7.3.1D-3 are intended for conformance tests and does not restrict the operating conditions of the network.

Table 7.3.1D-3: Uplink configuration for E-UTRA band / E-UTRA CA band

## 7.3.1EMinimum requirements (QPSK) for UE category 0, M1, M2 and 1bis

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.1E-1A/Table 7.3.1E-1B and Table 7.3.1E-2 for category 0,  Table 7.3.1E-3/Table 7.3.1E-4 for category M1, and Table 7.3.1E-6/Table 7.3.1E-7 for category 1bis, and Table 7.3.1E-8/Table 7.3.1E-9 for category M2.

Table 7.3.1E-1A: Reference sensitivity for FDD and TDD UE category 0 QPSK PREFSENS

Table 7.3.1E-1B: Reference sensitivity for HD-FDD UE category 0 QPSK PREFSENS

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3.1E-1A/Table 7.3.1E-1B shall be met for an uplink transmission bandwidth less than or equal to that specified in Table 7.3.1E-2.

Unless given by Table 7.3.1-3, the minimum requirements specified in Table 7.3.1E-1A/Table 7.3.1E-1B shall be verified with the network signalling value NS_01 (Table 6.2.4E-1) configured.

NOTE:Table 7.3.1E-2 is intended for conformance tests and does not necessarily reflect the operational conditions of the network, where the number of uplink and downlink allocated resource blocks will be practically constrained by other factors. Typical receiver sensitivity performance with HARQ retransmission enabled and using a residual BLER metric relevant for e.g. Speech Services is given in the Annex G (informative).

Table 7.3.1E-2: FDD and TDD UE category 0 Uplink configuration for reference sensitivity

Table 7.3.1E-3: Reference sensitivity for FDD and TDD UE category M1 QPSK PREFSENS

Table 7.3.1E-4: Reference sensitivity for HD-FDD UE category M1 QPSK PREFSENS

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3.1E-3/Table 7.3.1E-4 shall be met for an uplink transmission bandwidth less than or equal to that specified in Table 7.3.1E-5.

NOTE:Table 7.3.1E-5 is intended for conformance tests and does not necessarily reflect the operational conditions of the network, where the number of uplink and downlink allocated resource blocks will be practically constrained by other factors. Typical receiver sensitivity performance with HARQ retransmission enabled and using a residual BLER metric relevant for e.g. Speech Services is given in the Annex G (informative).

Table 7.3.1E-5: FDD and TDD UE category M1 Uplink configuration for reference sensitivity

Table 7.3.1E-6: Reference sensitivity for FDD and TDD UE category 1bis QPSK PREFSENS

Table 7.3.1E-7: FDD and TDD UE category 1bis Uplink configuration for reference sensitivity

Table 7.3.1E-8: Reference sensitivity for FDD /TDD UE category M2 QPSK PREFSENS

Table 7.3.1E-9: Reference sensitivity for HD-FDD category M2 QPSK PREFSENS

Table 7.3.1E-10: FDD/HD-FDD and TDD UE category M2 Uplink configuration for reference sensitivity

## 7.3.1FMinimum requirements for UE category NB1 and NB2

## 7.3.1F.1Reference sensitivity for UE category NB1 and NB2

The category NB1 and NB2 UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annex A.3.2  with received signal level as specified in Table 7.3.1F.1-1. Requirement in Table 7.3.1F.1-1 applies for any uplink configuration.

Table 7.3.1F.1-1: Reference sensitivity for UE category NB1 and NB2

## 7.3.1F.2Void

## 7.3.1GMinimum requirements (QPSK) for V2X

When UE is configured for E-UTRA V2X reception non-concurrent with E-UTRA uplink transmissions for E-UTRA V2X operating bands specified in Table 5.5G-1, the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.8.2 with parameters specified in Table 7.3.1G-1.

Table 7.3.1G-1: Reference sensitivity of E-UTRA V2X Bands (PC5)

Table 7.3.1.G-1a: Sidelink TX configuration for reference sensitivity of E-UTRA V2X Bands (PC5)

When UE is configured for E-UTRA V2X reception on V2X carrier concurrent with E-UTRA uplink and downlink for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2 with one or multiple contiguous carriers in V2X sidelink, E-UTRA V2X sidelink throughput for each component carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.8.2 with parameters specified in Table 7.3.1G-2. Also the E-UTRAdownlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3.3.2.

For the UE which supports V2X in an operating band as specified in Table 5.5G-2, and the UE also supports a E-UTRA downlink inter-band concurrent configuration in Table 7.3.1G-2A, the minimum requirement for reference sensitivity in Table 7.3.1G-1 and Table 7.3.1G-2 shall be increased by the amount given in ΔRIB,c in Table 7.3.1G-2A for the corresponding E-UTRA V2X band.

Table 7.3.1G-2: Reference sensitivity for V2X Communication QPSK PREFSENS

Table 7.3.1G-2A: ΔRIB,c (two bands)

The reference sensitivity is defined to be met with E-UTRA uplink assigned to one band (that differs from the V2X operating band) and all E-UTRA downlink carriers active. The E-UTRA uplink resource blocks shall be located as close as possible to E-UTRA V2X operating band but confined within the transmission bandwidth configuration for the channel bandwidth (Table 5.6-1). The uplink configuration for the E-UTRA operating band is specified in Table 7.3.1G-3 and 7.3.1G-4. The REFSENS of Uu downlink and PC5 sidelink will be tested at the same time.

Table 7.3.1G-3: Uplink configuration for REFSENS of E-UTRA V2X Bands

Table 7.3.1G-4: Sidelink TX configuration for REFSENS of E-UTRA V2X Bands

For intra-band contiguous multi-carrier operation, the reference sensitivity requirement specified in Table 7.3.1G-1 shall apply for each component carrier with all carriers active. The requirement is applied for multi-carrier intra-band concurrent receptions when 2 carrier transmissions are activated at the same time.

Table 7.3.1G-5: Sidelink TX configuration for REFSENS of E-UTRA V2X Bands for intra-band multi-carrier operation

## 7.3.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annexes A.3.18 with parameters specified in Table 7.3.1H-1.

Table 7.3.1H-1: Reference sensitivity for LTE based 5G terrestrial broadcast

## 7.3.2Void

## 7.4Maximum input level

This is defined as the maximum mean power received at the UE antenna port, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel.

## 7.4.1Minimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4.1-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.4.1-1: Maximum input level

## 7.4.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the maximum input level is defined with the uplink active on the band(s) other than the band whose downlink is being tested. For E-UTRA CA configurations including an operating band without uplink band or an operating band with an unpaired DL part, the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in subclause 7.4.1 for each component carrier while all downlink carriers are active.

For intra-band contiguous carrier aggregation maximum input level is defined as the powers received at the UE antenna port over the Transmission bandwidth configuration of each CC, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel over each component carrier.

The downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.4.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2.

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels over each component carrier as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4.1A-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Table 7.4.1A-1.

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the maximum input level requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in Table 7.4.1-1 and Table 7.4.1A-1 for one component carrier and two component carriers per sub-block, respectively. The throughput of each downlink component carrier shall be ≥ 95% of the maximum throughput of the specified reference measurement channel as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1). The requirements apply with all downlink carriers active.

Table 7.4.1A-1: Maximum input level for intra-band contiguous CA

For combinations of intra-band and inter-band carrier aggregation and one uplink assigned to one E-UTRA band, the requirement is defined with the uplink active in a band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For these uplink configurations, the UE shall meet the maximum input-level requirements for intra-band non-contiguous carrier aggregation of two or more downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the the requirements specified in subclause 7.4.1. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

## 7.4.1BMinimum requirements for UL-MIMO

For UE with two transmitter antenna connectors in closed-loop spatial multiplexing, the minimum requirements in Clause 7.4.1 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PCMAX_L is defined as the total transmitter power over the two transmit antenna connectors.

## 7.4.1DMinimum requirements for ProSe

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.6.2.

Table 7.4.1D-1: Maximum input level for ProSe

## 7.4.1FMinimum requirements for category NB1 and NB2

Category NB1 and NB2 UE maximum input level requirement is – 25 dBm. For this input level the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annex A.3.2.

## 7.4.1GMinimum requirements for V2X

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.8.2 with parameters specified in Table 7.4.1G-1.

Table 7.4.1G-1: Maximum input level

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.4.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.4.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, maximum input level is defined as the powers received at the UE antenna port over the Transmission bandwidth configuration of each CC, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel over each component carrier.

Table 7.4.1G-2: Maximum input level for intra-band contiguous multi-carrier for V2X UE

## 7.4.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annexes A.3.18 with parameters specified in Table 7.4.1H-1.

Table 7.4.1H-1: Maximum input level for LTE based 5G terrestrial broadcast

## 7.4AVoid

## 7.4A.1Void

## 7.5Adjacent Channel Selectivity (ACS)

Adjacent Channel Selectivity (ACS) is a measure of a receiver's ability to receive a E-UTRA signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

## 7.5.1Minimum requirements

The UE shall fulfil the minimum requirement specified in Table 7.5.1-1 for all values of an adjacent channel interferer up to –25 dBm. However it is not possible to directly measure the ACS, instead the lower and upper range of test parameters are chosen in Table 7.5.1-2 and Table 7.5.1-3 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1). For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.5.1-1: Adjacent channel selectivity

Table 7.5.1-2: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1-3: Test parameters for Adjacent channel selectivity, Case 2

## 7.5.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band, the adjacent channel requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in subclause 7.5.1 for each component carrier while all downlink carriers are active. For E-UTRA CA configurations including an operating band without uplink operation or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. For a component carrier configured in Band 46 or Band 49, the requirements specified in subclause 7.5.1 are replaced by the requirements in Table 7.5.1A-0a with test parameters in Table 7.5.1A-0b and Table 7.5.1A-0c.

Table 7.5.1A-0a: Adjacent channel selectivity

Table 7.5.1A-0b: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1A-0c: Test parameters for Adjacent channel selectivity, Case 2

For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the adjacent channel requirements of subclause 7.5.1A do not apply.

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.5.1A-2 and Table 7.5.1A-3 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2. The UE shall fulfil the minimum requirement specified in Table 7.5.1A-1 for an adjacent channel interferer on either side of the aggregated downlink signal at a specified frequency offset and for an interferer power up to -25 dBm. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.5.1A-2 and 7.5.1A-3. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Tables 7.5.1A-2 and 7.5.1A-3.

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the adjacent channel selectivity requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclauses 7.5.1 and 7.5.1A for one component carrier and two component carriers per sub-block, respectively. The UE shall fulfil the minimum requirements all values of a single adjacent channel interferer in-gap and out-of-gap up to a –25 dBm interferer power while all downlink carriers are active. For the lower range of test parameters (Case 1), the interferer power Pinterferer shall be set to the maximum of the levels given by the carriers of the respective sub-blocks as specified in Table 7.5.1-2 and Table 7.5.1A-2 for one component carrier and two component carriers per sub-block, respectively. The wanted signal power levels for the carriers of each sub-block shall then be adjusted relative to Pinterferer in accordance with the ACS requirement for each sub-block (Table 7.5.1-1 and Table 7.5.1A-1). For the upper range of test parameters (Case 2) for which the interferer power Pinterferer is -25 dBm (Table 7.5.1-3 and Table 7.5.1A-3) the wanted signal power levels for the carriers of each sub-block shall be adjusted relative to Pinterferer like for Case 1.

Table 7.5.1A-1: Adjacent channel selectivity

Table 7.5.1A-2: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1A-3: Test parameters for Adjacent channel selectivity, Case 2

For combinations of intra-band and inter-band carrier aggregation and one uplink carrier assigned to one E-UTRA band, the requirement is defined with the uplink active in each band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For these uplink configurations, the UE shall meet the adjacent channel selectivity requirements for intra-band non-contiguous carrier aggregation with RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) for the two or more non-contiguous downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the requirements specified in subclause 7.5.1. For contiguously aggregated component carriers configured in Band 46, the said requirements for intra-band contiguous carrier aggregation of downlink carriers are replaced by requirements in Table 7.5.1A-4 with test parameters in Table 7.5.1A-5 and Table 7.5.1A-6. For non-contiguously aggregated component carriers configured in Band 46, the said requirements are applied to each sub-block for in-gap and out-of-gap interferers. For the sub-block with a single component carrier, the requirement is replaced by Table 7.5.1A-0a with test parameters in Table 7.5.1A-0b and Table 7.5.1A-0c. For the sub-block with two or more contiguous component carriers, the requirement is replaced by Table 7.5.1A-4 with test parameters in Table 7.5.1A-5 and Table 7.5.1A-6. All downlink carriers shall be active throughout the tests and the requirements for downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

Table 7.5.1A-4: Adjacent channel selectivity

Table 7.5.1A-5: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1A-6: Test parameters for Adjacent channel selectivity, Case 2

## 7.5.1BMinimum requirements for UL-MIMO

For UE(s) with two transmitter antenna connectors in closed-loop spatial multiplexing scheme, the minimum requirements in Clause 7.5.1 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PCMAX_L is defined as the total transmitter power over the two transmit antenna connectors.

## 7.5.1DMinimum requirements for ProSe

The UE shall fulfil the minimum requirement specified in Table 7.5.1D-1 for all values of an adjacent channel interferer up to –25 dBm. However it is not possible to directly measure the ACS, instead the lower and upper range of test parameters are chosen in Table 7.5.1D-2 and Table 7.5.1D-3 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2.

Table 7.5.1D-1: Adjacent channel selectivity for ProSe

Table 7.5.1D-2: Test parameters for Adjacent channel selectivity for ProSe, Case 1

Table 7.5.1D-3: Test parameters for Adjacent channel selectivity for ProSe, Case 2

## 7.5.1FMinimum requirements for category NB1 and NB2

Category NB1 and NB2 UE shall fulfil the minimum requirement specified in Table 7.5.1F-1 for all values of an adjacent channel interferer up to –25 dBm. However it is not possible to directly measure the ACS, instead the lower and upper range of test parameters are chosen in Table 7.5.1F-1 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annex A.3.2.

Table 7.5.1F: Adjacent channel selectivity parameters for category NB1 and NB2

## 7.5.1GMinimum requirements for V2X

The V2X UE shall fulfil the minimum requirement specified in Table 7.5.1G-1 for all values of an adjacent channel interferer up to -22 dBm. However it is not possible to directly measure the ACS, instead the lower and upper range of test parameters are chosen in Table 7.5.1G-2 and Table 7.5.1G-3 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2.

Table 7.5.1G-1: Adjacent channel selectivity for V2X

Table 7.5.1G-2: Test parameters for Adjacent channel selectivity for V2X, Case 1

Table 7.5.1G-3: Test parameters for Adjacent channel selectivity for V2X, Case 2

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.5.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.5.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, the V2X UE shall fulfil the minimum requirement specified in Table 7.5.1G-4 to Table 7.5.1G-6 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2.

Table 7.5.1G-4: Adjacent channel selectivity for intra-band contiguous multi-carrier for V2X UE

Table 7.5.1G-5: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1G-6: Test parameters for Adjacent channel selectivity, Case 2

## 7.5.1HMinimum requirements for LTE based 5G terrestrial broadcast

The UE shall fulfil the minimum requirement specified in Table 7.5.1H-1 for all values of an adjacent channel interferer up to –22 dBm. However it is not possible to directly measure the ACS, instead the lower and upper range of test parameters are chosen in Table 7.5.1H-2 and Table 7.5.1H-3 where the throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annex A.3.18.

Table 7.5.1H-1: Adjacent channel selectivity for LTE based 5G terrestrial broadcast

Table 7.5.1H-2: Test parameters for Adjacent channel selectivity, Case 1

Table 7.5.1H-3: Test parameters for Adjacent channel selectivity, Case 2

## 7.6Blocking characteristics

The blocking characteristic is a measure of the receiver's ability to receive a wanted signal at its assigned channel frequency in the presence of an unwanted interferer on frequencies other than those of the spurious response or the adjacent channels, without this unwanted input signal causing a degradation of the performance of the receiver beyond a specified limit. The blocking performance shall apply at all frequencies except those at which a spurious response occur.

## 7.6.1In-band blocking

In-band blocking is defined for an unwanted interfering signal falling into the UE receive band or into the first 15 MHz below or above the UE receive band at which the relative throughput shall meet or exceed the minimum requirement for the specified measurement channels.

For CA configurations including Band 46, in-band blocking in Band 46 is defined for a 20 MHz unwanted interfering signal falling into the UE receive band or into the first 60 MHz below or above the UE receive band (Table 7.6.1.1A-0a and Table 7.6.1.1A-0b).

For CA configurations including Band 49, in-band blocking in Band 49 is defined for an unwanted interfering signal falling into the UE receive band or into the first 60 MHz below or above the UE receive band (Table 7.6.1.1A-0a and Table 7.6.1.1A-0b).

## 7.6.1.1Minimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.6.1.1-1 and 7.6.1.1-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.6.1.1-1: In band blocking parameters

Table 7.6.1.1-2: In-band blocking

For the UE which supports inter band CA configuration in Table 7.3.1-1A, PInterferer power defined in Table 7.6.1.1-2 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.6.1.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the in-band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. For adjacent downlink bands separated by less than 30 MHz the frequency separation between the center frequencies of adjacent component carriers belonging to different bands shall be ≥ BW1/2 + BW2/2 + 2FIoffset,case j for Case j interferers, j = 1,2, where BWk/2 are the channel bandwidths of carrier k, k = 1,2. The UE shall meet the requirements specified in subclause 7.6.1.1 for each component carrier while all downlink carriers are active. For the UE which supports inter band CA configuration in Table 7.3.1-1A, PInterferer power defined in Table 7.6.1.1-2 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A. For E-UTRA CA configurations including an operating band without uplink operation or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The requirements for the component carrier configured in the operating band without uplink operation are specified in Table 7.6.1.1A-0, Table 7.6.1.1A-0a and Table 7.6.1.1A-0b. The requirements for a component carrier configured in Band 49 are specified in Table 7.6.1.1A-0a and Table 7.6.1.1A-0b.

Table 7.6.1.1A-0: In-band blocking for additional operating bands for carrier aggregation

Table 7.6.1.1A-0a: In band blocking parameters for additional operating bands for carrier aggregation

Table 7.6.1.1A-0b: In-band blocking for additional operating bands for carrier aggregation

For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the in-band blocking requirements of subclause 7.6.1.1A do not apply.

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.6.1.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2. The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Tables 7.6.1.1A-1 and Tables 7.6.1.1A-2 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.6.1.1A-1 and 7.6.1.1A-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Tables 7.6.2.1A-1 and 7.6.2.1A-2.

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the in-band blocking requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclause 7.6.1.1 and in this subclause for one component carrier and two component carriers per sub-block, respectively. The requirements apply for in-gap and out-of-gap interferers while all downlink carriers are active.

Table 7.6.1.1A-1: In band blocking parameters

Table 7.6.1.1A-2: In-band blocking

For combinations of intra-band and inter-band carrier aggregation and one uplink carrier assigned to one E-UTRA band, the requirement is defined with the uplink active in the band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For these uplink configurations, the UE shall meet the in-band blocking requirements for intra-band non-contiguous carrier aggregation with RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) for the two or more non-contiguous downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the requirements specified in subclause 7.6.1. For contiguously aggregated component carriers configured in Band 46, the said requirements for intra-band contiguous carrier aggregation of downlink carriers are replaced by requirements in Table 7.6.1.1A-3 and 7.6.1.1A-4. For non-contiguously aggregated component carriers configured in Band 46, the said requirements are applied to each sub-block for in-gap and out-of-gap interferers. For the sub-block with a single component carrier, the requirement is replaced by Table 7.6.1.1A-0a and 7.6.1.1A-0b. For the sub-block with two or more contiguous component carriers, the requirement is replaced by Table 7.6.1.1A-3 and 7.6.1.1A-4. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of uplink operation.

Table 7.6.1.1A-3: In band blocking parameters

Table 7.6.1.1A-4: In-band blocking

## 7.6.1.1DMinimum requirements for ProSe

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2.

Table 7.6.1.1D-1: In band blocking parameters for ProSe Direct Discovery

Table 7.6.1.1D-2: In band blocking parameters for ProSe Direct Communication

Table 7.6.1.1D-3: In-band blocking for ProSe

For the UE which supports inter band CA configuration in Table 7.3.1-1A, PInterferer power defined in Table 7.6.1.1D-3 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.6.1.1FMinimum requirements for category NB1 and NB2

Category NB1 and NB2 UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annex A.3.2 with parameters specified in Table 7.6.1.1F-1.

Table 7.6.1.1F-1: In-band blocking parameters for category NB1 and NB2

## 7.6.1.1GMinimum requirements for V2X

The V2X UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with paramteters defined in Table 7.6.1.1G-1 and Table 7.6.1.1G-2.

Table 7.6.1.1G-1: In band blocking parameters

Table 7.6.1.1G-2: In-band blocking

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.6.1.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.6.1.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, the V2X UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with paramteters defined in Table 7.6.1.1G-3 and Table 7.6.1.1G-4.

Table 7.6.1.1G-3: In band blocking parameters for intra-band contiguous multi-carrier for V2X UE

Table 7.6.1.1G-4: In-band blocking for intra-band contiguous multi-carrier for V2X UE

## 7.6.1.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annex A.3.18 with parameters specified in Table 7.6.1.1H-1 and 7.6.1.1H-2.

Table 7.6.1.1H-1: In band blocking parameters

Table 7.6.1.1H-2: In-band blocking

## 7.6.2Out-of-band blocking

Out-of-band band blocking is defined for an unwanted CW interfering signal falling more than 15 MHz below or above the UE receive band. For the first 15 MHz below or above the UE receive band the appropriate in-band blocking or adjacent channel selectivity in subclause 7.5.1 and subclause 7.6.1 shall be applied.

For CA configurations including Band 46 or Band 49, out-of-band band blocking is defined for an unwanted CW interfering signal falling more than 60 MHz below or above the UE receive band (see Table 7.6.2.1A-0a). For the first 60 MHz below or above the UE receive band the appropriate in-band blocking or adjacent channel selectivity in subclause 7.5.1A and subclause 7.6.1A shall be applied.

## 7.6.2.1Minimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.6.2.1-1 and 7.6.2.1-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

For Table 7.6.2.1-2 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size, where  is the number of resource blocks in the downlink transmission bandwidth configuration (see Figure 5.6-1). For these exceptions the requirements of subclause 7.7 Spurious response are applicable.

For Table 7.6.2.1-2 in frequency range 4, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size, where  is the number of resource blocks in the downlink transmission bandwidth configurations (see Figure 5.6-1) and  is the number of resource blocks allocated in the uplink. For these exceptions the requirements of clause 7.7 spurious response are applicable.

Table 7.6.2.1-1: Out-of-band blocking parameters

Table 7.6.2.1-2: Out of band blocking

## 7.6.2.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band, the out-of-band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The throughput in the downlink measured shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.6.2.1-1 and 7.6.2.1A-0. For E-UTRA CA configurations including an operating band without uplink operation (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the uplink active in the band(s) capable of UL operation. For the E-UTRA CA configurations with band 46 or Band 49, the parameters specified in Table 7.6.2.1A-0 are replaced by those specified in Table 7.6.2.1A-0a. The UE shall meet these requirements for each component carrier while all downlink carriers are active.

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the out-of-band blocking requirements specified above shall be met with the transmitter power for the uplink set to 7 dB below PCMAX_L,c  for each serving cell c.

For E-UTRA CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the out-of-band blocking requirements of subclause 7.6.2.1A do not apply.

Table 7.6.2.1A-0: out-of-band blocking for inter-band carrier aggregation

Table 7.6.2.1A-0a: out-of-band blocking for inter-band carrier aggregation with band 46 or Band 49 and with one active uplink

For Table 7.6.2.1A-0 and Table 7.6.2.1A-0b in frequency ranges 1, 2 and 3, up to  exceptions per downlink are allowed for spurious response frequencies for one active uplink when measured using a step size of 1 MHz.

For Table 7.6.2.1A-0 in frequency ranges 1, 2 and 3, up to 2∙ exceptions per downlink are allowed for spurious response frequencies for two active uplinks when measured using a step size of 1 MHz. For these exceptions the requirements in clause 7.7.1A apply.

For intra-band contiguous carrier aggreagations the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.6.2.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2.

The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Tables 7.6.2.1A-1 and Tables 7.6.2.1A-2 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.6.2.1A-1 and 7.6.2.1A-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Tables 7.6.2.1A-1 and 7.6.2.1A-2.

For Table 7.6.2.1A-2 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7 Spurious response are applicable.

Table 7.6.2.1A-1: Out-of-band blocking parameters

Table 7.6.2.1A-2: Out of band blocking

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the out-of-band blocking requirements are defined with the uplink configuration in accordance with table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclauses 7.6.2.1 and 7.6.2.1A for one component carrier and two or more component carriers per sub-block, respectively. The requirements apply with all downlink carriers active.

For Table 7.6.2.1-2 in frequency range 1, 2 and 3, up to exceptions per assigned E-UTRA channel per sub-block of the E-UTRA CA configuration are allowed for spurious response frequencies for one active uplink when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7 spurious response are applicable.

For Table 7.6.2.1-2 in frequency range 4, up to exceptions per assigned E-UTRA channel per sub-block of the E-UTRA CA configuration are allowed for spurious response frequencies for one active uplink when measured using a 1MHz step size. For these exceptions the requirements of clause 7.7 spurious response are applicable.

For intra-band non-contiguous carrier aggregation with two uplink carriers and two or more downlink carriers, the out-of-band blocking requirements are defined with the uplink configuration of the PCC and SCC being in accordance with Table 7.3.1A-4 and powers of both carriers set to PCMAX_L,c – 7 dBm. The UE shall meet the requirements specified in subclause 7.6.2.1 for each component carrier while both downlink carriers are active.

For Table 7.6.2.1-2 in frequency range 1, 2 and 3, up to 2∙ exceptions per assigned E-UTRA channel per sub-block of the E-UTRA CA configuration are allowed for spurious response frequencies for two active uplinks in the same operating band when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7 spurious response are applicable.

For Table 7.6.2.1-2 in frequency range 4, up to 2∙ exceptions per assigned E-UTRA channel per sub-block of the E-UTRA CA configuration are allowed for spurious response frequencies for two active uplinks in the same operating band when measured using a 1MHz step size. For these exceptions the requirements of clause 7.7 spurious response are applicable.

For combinations of intra-band and inter-band carrier aggregation and the uplink assigned to one E-UTRA band, the requirement is defined with the uplink active in a band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For the two or more non-contiguous component carriers within the same band, Pwanted in Table 7.6.2.1A-0 is set using RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) while a band supporting contiguously aggregated carriers the out-of-band blocking parameters in Table 7.6.2.1-1 are replaced by those specified in Table 7.6.2.1A-1. For each downlink the UE shall meet the out-of-band blocking requirements applicable for inter-band carrier aggregation with one component carrier per operating band with the following exception. For each component carrier of the E-UTRA CA Configurations with band 46 or band 49, the requirements specified in Table 7.6.2.1A-0 are replaced by those in Table 7.6.2.1A-0a. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

## 7.6.2.1DMinimum requirements for ProSe

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2 with parameters specified in Tables 7.6.2.1D-1, 7.6.2.1D-2 and 7.6.2.1D-3.

For Table 7.6.2.1D-3 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size, where  is the number of resource blocks in the downlink transmission bandwidth configuration (see Figure 5.6-1). For these exceptions the requirements of subclause 7.7 Spurious response are applicable.

Table 7.6.2.1D-1: Out-of-band blocking parameters for ProSe Direct Discovery

Table 7.6.2.1D-2: Out-of-band blocking parameters for ProSe Direct Communication

Table 7.6.2.1D-3: Out of band blocking for ProSe

## 7.6.2.1FMinimum requirements for category NB1 and NB2

The category NB1 and NB2 UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3.2 with parameters specified in Table 7.6.2.1F-1.

For Table 7.6.2.1F-1 in frequency range 1, 2 and 3, up to 24 exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7.1F spurious response are applicable.

Table 7.6.2.1F-1: Out-of-band blocking parameters for category NB1 and NB2 UE

## 7.6.2.1GMinimum requirements for V2X

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Tables 7.6.2.1G-1, 7.6.2.1G-2.

For Table 7.6.2.1G-2 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size, where  is the number of resource blocks in the downlink transmission bandwidth configuration (see Figure 5.6-1). For these exceptions the requirements of subclause 7.7 spurious response are applicable.

Table 7.6.2.1G-1: Out-of-band blocking parameters

Table 7.6.2.1G-2: Out of band blocking

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.6.2.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.6.2.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, the V2X UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Tables 7.6.2.1G-3 and 7.6.2.1G-4.

For Table 7.6.2.1G-4 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7 spurious response are applicable.

Table 7.6.2.1G-3: Out-of-band blocking parameters for intra-band contiguous multi-carrier for V2X UE

Table 7.6.2.1G-4: Out of band blocking for intra-band contiguous multi-carrier for V2X UE

## 7.6.2.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annex A.3.18 with parameters specified in Table 7.6.2.1H-1 and 7.6.2.1H-2.

For Table 7.6.2.1H-2 in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size, where  is the number of resource blocks in the downlink transmission bandwidth configuration (see Figure 5.6H-1). For these exceptions the requirements of subclause 7.7 Spurious response are applicable.

Table 7.6.2.1H-1: Out-of-band blocking parameters

Table 7.6.2.1H-2: Out of band blocking

## 7.6.3Narrow band blocking

This requirement is measure of a receiver's ability to receive a E-UTRA signal at its assigned channel frequency in the presence of an unwanted narrow band CW interferer at a frequency, which is less than the nominal channel spacing.

## 7.6.3.1Minimum requirements

The relative throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.3.1-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.6.3.1-1: Narrow-band blocking

For the UE which supports inter-band CA configuration in Table 7.3.1-1A, PUW power defined in Table 7.6.3.1-1 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.6.3.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the narrow-band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in subclause 7.6.3.1 for each component carrier while all downlink carriers are active. For E-UTRA CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the narrow-band blocking requirements of subclause 7.6.3.1A do not apply. For E-UTRA CA configurations with a component carrier assigned in Band 46, narrow-band blocking requirements do not apply in the presence of a narrow-band interferer in Band 46.

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.6.3.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2. The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Table 7.6.3.1A-1 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.3.1A-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Table 7.6.3.1A-1.

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the narrow band blocking requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclauses 7.6.3.1 and 7.6.3.1A for one component carrier and two component carriers per sub-block, respectively. The requirements apply for in-gap and out-of-gap interferers while all downlink carriers are active.

Table 7.6.3.1A-1: Narrow-band blocking

For combinations of intra-band and inter-band carrier aggregation and one uplink carrier assigned to one E-UTRA band, the requirement is defined with the uplink active in a band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For these uplink configurations, the UE shall meet the narrow-band blocking requirements for intra-band non-contiguous carrier aggregation with RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) for the two or more non-contiguous downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the requirements specified in subclause 7.6.3. For E-UTRA CA configurations with component carriers assigned in Band 46, narrow-band blocking requirements do not apply in the presence of a narrow-band interferer in Band 46. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

## 7.6.3.1DMinimum requirements for ProSe

The relative throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2 with parameters specified in Table 7.6.3.1D-1 and Table 7.6.3.1D-2.

Table 7.6.3.1D-1: Narrow-band blocking for ProSe Direct Discovery

Table 7.6.3.1D-2: Narrow-band blocking for ProSe Direct Communication

For the UE which supports inter-band CA configuration in Table 7.3.1-1A, PUW power defined in Table 7.6.3.1D-1 and  Table 7.6.3.1D-2 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.6.3.1HMinimum requirements for LTE based 5G terrestrial broadcast

Narrow-band blocking requirements are not applicable to LTE based 5G terrestrial broadcast.

## 7.6AVoid

<Reserved for future use>

## 7.6BBlocking characteristics for UL-MIMO

For UE with two transmitter antenna connectors in closed-loop spatial multiplexing scheme, the minimum requirements in subclause 7.6 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PCMAX_L is defined as the total transmitter power over the two transmit antenna connectors.

## 7.7Spurious response

Spurious response is a measure of the receiver's ability to receive a wanted signal on its assigned channel frequency without exceeding a given degradation due to the presence of an unwanted CW interfering signal at any other frequency at which a response is obtained i.e. for which the out of band blocking limit as specified in subclause 7.6.2 is not met.

## 7.7.1Minimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.7.1-1 and 7.7.1-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.7.1-1: Spurious response parameters

Table 7.7.1-2: Spurious response

For the UE which supports inter-band CA configuration in Table 7.3.1-1A, Pinterferer power defined in Table 7.7.1-2 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.7.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the spurious response requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The throughput measured in each downlink with Finterferer in Table 7.6.2.1A-0 and Table 7.6.2.1A-0a at spurious response frequencies shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.7.1-1 and 7.7.1-2. The UE shall meet these requirements for each component carrier while all downlink carriers are active.

For inter-band carrier aggregation with one component carrier per operating band and the uplink active in two E-UTRA bands, the spurious response requirements applicable specified above shall be met with the transmitter power for the uplink set to 7 dB below PCMAX_L,c  for each serving cell c.

For E-UTRA CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the spurious response requirements of subclause 7.7.1A do not apply.

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.7.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggregation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.7.1A-1 and 7.7.1A-2. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Tables 7.7.1A-1 and 7.7.1A-2

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the spurious response requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclauses 7.7.1 and 7.7.1A for one component carrier and two component carriers per sub-block, respectively. The requirements apply with all downlink carriers active.

For intra-band non-contiguous carrier aggregation with two uplink carriers and two or more downlink carriers, the spurious response requirements applicable specified above shall be met with the transmitter powers for the uplinks set to PCMAX_L,c – 7 dBm.

Table 7.7.1A-1: Spurious response parameters

Table 7.7.1A-2: Spurious response

For combinations of intra-band and inter-band carrier aggregation and one uplink carrier assigned to one E-UTRA band, the requirement is defined with the uplink active in a band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. The downlink PCC shall be configured closer to the uplink operating band than the downlink SCC(s) when the uplink is active in band(s) supporting contiguous aggregation. For the two or more non-contiguous component carriers within the same band, Pwanted in Table 7.6.2.1A-0 is set using RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) while a band supporting contiguously aggregated carriers the out-of-band blocking parameters in Table 7.7.1-1 are replaced by those specified in Table 7.7.1A-1. For each downlink the UE shall meet the spurious-response requirements applicable for inter-band carrier aggregation with one component carrier per operating band. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

## 7.7.1BMinimum requirements for UL-MIMO

For UE with two transmitter antenna connectors in closed-loop spatial multiplexing scheme, the minimum requirements in Clause 7.7.1 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PCMAX_L is defined as the total transmitter power over the two transmit antenna connectors.

## 7.7.1DMinimum requirements for ProSe

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2 with parameters specified in Tables 7.7.1D-1, 7.7.1D-2, and 7.7.1D-3.

Table 7.7.1D-1: Spurious response parameters for ProSe Direct Discovery

Table 7.7.1D-2: Spurious response parameters for ProSe Direct Communication

Table 7.7.1D-3: Spurious response for ProSe

For the UE which supports inter-band CA configuration in Table 7.3.1-1A, Pinterferer power defined in Table 7.7.1D-3 is increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.7.1FMinimum requirements for UE category NB1 and NB2

The category NB1 and NB2 UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annexe A.3.2 with parameters specified in Tables 7.7.1F-1.

Table 7.7.1F-1: Spurious response parameters for UE category NB1 and NB2

## 7.7.1GMinimum requirements for V2X

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Tables 7.7.1G-1.

Table 7.7.1G-1: Spurious response parameters

Table 7.7.1G-2: Spurious response

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.7.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.7.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, the V2X UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Table 7.7.1G-3 and Table 7.7.1G-4.

Table 7.7.1G-3: Spurious response parameters for intra-band contiguous multi-carrier for V2X UE

Tables 7.7.1G-4: Spurious response for intra-band contiguous multi-carrier for V2X UE

## 7.7.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annex A.3.18 with parameters specified in Table 7.7.1H-1 and 7.7.1H-2.

Table 7.7.1H-1: Spurious response parameters for LTE based 5G terrestrial broadcast

Table 7.7.1H-2: Spurious response for LTE based 5G terrestrial broadcast

## 7.8Intermodulation characteristics

Intermodulation response rejection is a measure of the capability of the receiver to receiver a wanted signal on its assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal.

## 7.8.1Wide band intermodulation

The wide band intermodulation requirement is defined following the same principles using modulated E-UTRA carrier and CW signal as interferer.

## 7.8.1.1Minimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.8.1.1 for the specified wanted signal mean power in the presence of two interfering signals. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements only apply for carriers assigned in the paired part.

Table 7.8.1.1-1: Wide band intermodulation

For the UE which supports inter band CA configuration in Table 7.3.1-1A, Pinterferer1 and Pinterferer2 powers defined in Table 7.8.1.1-1 are increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.8.1AMinimum requirements for CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one E-UTRA band the wide band intermodulation requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in subclause 7.8.1.1 for each component carrier while all downlink carriers are active. For E-UTRA CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.5-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. For a component carrier configured in Band 46 or Band 49, the requirements specified in subclause 7.8.1.1 are replaced by the requirements in Table 7.8.1-1A-0.

Table 7.8.1.1A-0: Wide band intermodulation

For E-UTRA CA configurations listed in Table 7.3.1A-0a under conditions for which reference sensitivity for the operating band being tested is N/A, the wideband intermodulation requirements of subclause 7.8.1A do not apply.

For intra-band contiguous carrier aggegation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC, For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.8.1A-1 with the uplink configuration set according to Table 7.3.1A-1 for the applicable carrier aggreagation configuration. For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.1-2. The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Table 7.8.1A-1 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.8.1A-1. For operating bands with an unpaired DL part (as noted in Table 5.5-1), the requirements also apply for an SCC assigned in the unpaired part with parameters specified in Tables 7.8.1A-1.

Table 7.8.1A-1: Wide band intermodulation

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the wide band intermodulation requirements are defined with the uplink configuration in accordance with Table 7.3.1A-3. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in subclauses 7.8.1.1 and in this subclause for one component carrier and two or more component carriers per sub-block, respectively. The requirements apply for out-of-gap interferers while all downlink carriers are active.

For combinations of intra-band and inter-band carrier aggregation and one uplink carrier assigned to one E-UTRA band, the requirement is defined with the uplink active in a band other than that supporting the downlink(s) under test. The uplink configuration shall be in accordance with Table 7.3.1A-3 when the uplink is active in the band supporting two or more non-contiguous component carriers, Table 7.3.1A-1 when the uplink is active in a band supporting two contiguous component carriers and in accordance with Table 7.3.1-2 when the uplink is active in a band supporting one carrier per band. For these uplink configurations, the UE shall meet the wide-band intermodulation requirements for intra-band non-contiguous carrier aggregation with RIBNC = 0 dB for all sub-block gaps (Table 7.3.1A-3) for the two or more non-contiguous downlink sub-blocks, the requirements for intra-band contiguous carrier aggregation for the contiguously aggregated downlink carriers and for any remaining component carrier(s) the requirements specified in subclause 7.8.1. For contiguously aggregated component carriers configured in Band 46, the said requirements for intra-band contiguous carrier aggregation of two or more downlink carriers are replaced by requirements in Table 7.8.1A-2. For non-contiguously aggregated component carriers configured in Band 46, the said requirements are applied to each sub-block for out-of-gap interferers. For the sub-block with a single component carrier, the requirement is replaced by Table 7.8.1.1A-0. For the sub-block with two or more contiguous component carriers, the requirement is replaced by Table 7.8.1.1A-2. All downlink carriers shall be active throughout the tests and the requirements for the downlinks shall be met with the single uplink carrier active in each band capable of UL operation.

Table 7.8.1A-2: Wide band intermodulation

## 7.8.1BMinimum requirements for UL-MIMO

For UE(s) with two transmitter antenna connectors in closed-loop spatial multiplexing scheme, the minimum requirements in subclause 7.8.1 shall be met with the UL-MIMO configurations specified in Table 6.2.2B-2. For UL-MIMO, the parameter PCMAX_L is defined as the total transmitter power over the two transmit antenna connectors.

## 7.8.1DMinimum requirements for ProSe

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.6.2 with parameters specified in Table 7.8.1D-1, Table 7.8.1D-2, and Table 7.8.1D-3 for the specified wanted signal mean power in the presence of two interfering signals

Table 7.8.1D-1: Wide band intermodulation parameters for ProSe Direct Discovery

Table 7.8.1D-2: Wide band intermodulation for ProSe Direct Communication

Table 7.8.1D-3: Wide band intermodulation for ProSe

For the UE which supports inter band CA configuration in Table 7.3.1-1A, Pinterferer1 and Pinterferer2 powers defined in Table 7.8.1D-3 are increased by the amount given by ΔRIB,c in Table 7.3.1-1A.

## 7.8.1FMinimum requirements for category NB1 and NB2

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channel as specified in Annex A.3.2 with parameters specified in Table 7.8.1F-1 for the specified wanted signal mean power in the presence of two interfering signals.

Table 7.8.1F-1: Wide band intermodulation for category NB1 and NB2

## 7.8.1GMinimum requirements

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Table 7.8.1G-1 for the specified wanted signal mean power in the presence of two interfering signals

Table 7.8.1G-1: Wide band intermodulation

When UE is configured for simultaneous E-UTRA V2X sidelink and E-UTRA downlink reception for inter-band E-UTRA V2X / E-UTRA bands specified in Table 5.5G-2, the requirements in subclause 7.8.1G apply for the E-UTRA V2X sidelink reception and the requirements in subclause 7.8.1 apply for the E-UTRA downlink reception while all downlink carriers are active.

For intra-band contiguous multi-carrier operation, the V2X UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.8.2 with parameters specified in Table 7.8.1G-2 for the specified wanted signal mean power in the presence of two interfering signals.

Table 7.8.1G-2: Wide band intermodulation for intra-band contiguous multi-carrier for V2X UE

## 7.8.1HMinimum requirements for LTE based 5G terrestrial broadcast

The throughput shall be ≥ 95% of the maximum throughput as represented by a reported BLER of <5% for the reference measurement channels as specified in Annex A.3.18 with parameters specified in Table 7.8.1H-1.

Table 7.8.1H-1: Wide band intermodulation parameters

## 7.8.2Void

## 7.9Spurious emissions

The spurious emissions power is the power of emissions generated or amplified in a receiver that appear at the UE antenna connector.

## 7.9.1Minimum requirements

The power of any narrow band CW spurious emission shall not exceed the maximum level specified in Table 7.9.1-1

Table 7.9.1-1: General receiver spurious emission requirements

In addition, for a V2X UE operating in Region 1, the power of any spurious emission shall not exceed the levels specified in Table 7.9.1-2.

Table 7.9.1-2: Additional RX spurious emissions limits in Region 1

## 7.9.1AMinimum requirements

For E-UTRA CA configurations including an operating band without uplink band (as noted in Table 5.5-1), the power of any narrow band CW spurious emission shall not exceed the maximum level specified in Table 7.9.1A-1.

Table 7.9.1A-1: General receiver spurious emission requirements

## 7.10Receiver image

## 7.10.1Void

## 7.10.1AMinimum requirements for CA

Receiver image rejection is a measure of a receiver's ability to receive the E-UTRA signal on one component carrier while it is also configured to receive an adjacent aggregated carrier. Receiver image rejection ratio is the ratio of the wanted received power on a sub-carrier being measured to the unwanted image power received on the same sub-carrier when both sub-carriers are received with equal power at the UE antenna connector.

For intra-band contiguous carrier aggregation the UE shall fulfil the minimum requirement specified in Table 7.10.1A-1 for all values of aggregated input signal up to –22 dBm.

Table 7.10.1A-1: Receiver image rejection

## 7.10.1GMinimum requirements for V2X Communication

Receiver image rejection is a measure of a receiver's ability to receive the E-UTRA V2X signal on one component carrier while it is also configured to receive another aggregated carrier. Receiver image rejection ratio is the ratio of the wanted received power on a sub-carrier being measured to the unwanted image power received on the same sub-carrier when both sub-carriers are received with equal power at the UE antenna connector.

For intra-band contiguous multi-carrier operation, the UE shall fulfil the minimum requirement specified in Table 7.10.1G-1 for all values of aggregated input signal.

Table 7.10.1G-1: Receiver image rejection
