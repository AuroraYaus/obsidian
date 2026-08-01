---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.306_38306-j20/content.md"
---
# TS 38.306 38306-j20

3GPP TS 38.306 V19.2.0 (2026-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

User Equipment (UE) radio access capabilities

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

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

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersLTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Contents

Foreword6

1Scope7

2References7

3Definitions, symbols and abbreviations8

3.1Definitions8

3.2Symbols9

3.3Abbreviations9

4UE radio access capability parameters10

4.1Supported max data rate10

4.1.1General10

4.1.2Supported max data rate for DL/UL10

4.1.3Void12

4.1.4Total layer 2 buffer size for DL/UL12

4.1.5Supported max data rate for SL13

4.1.6Total layer 2 buffer size for NR SL13

4.2UE Capability Parameters14

4.2.1Introduction14

4.2.2General parameters16

4.2.3SDAP Parameters23

4.2.4PDCP Parameters24

4.2.5RLC parameters27

4.2.6MAC parameters28

4.2.6.1MAC-Parameters28

4.2.6.2MAC-ParametersPerBand33

4.2.7Physical layer parameters34

4.2.7.1BandCombinationList parameters34

4.2.7.2BandNR parameters49

4.2.7.2aSharedSpectrumChAccessParamsPerBand189

4.2.7.2bFR2-2-AccessParamsPerBand195

4.2.7.3CA-ParametersEUTRA199

4.2.7.4CA-ParametersNR200

4.2.7.5FeatureSetDownlink parameters294

4.2.7.6FeatureSetDownlinkPerCC parameters310

4.2.7.7FeatureSetUplink parameters318

4.2.7.8FeatureSetUplinkPerCC parameters342

4.2.7.9MRDC-Parameters351

4.2.7.10Phy-Parameters357

4.2.7.11Other PHY parameters376

4.2.7.12NRDC-Parameters379

4.2.7.13CarrierAggregationVariant381

4.2.7.14Phy-ParametersSharedSpectrumChAccess382

4.2.8Void384

4.2.9MeasAndMobParameters385

4.2.9aMeasAndMobParametersMRDC400

4.2.10Inter-RAT parameters404

4.2.10.1Void405

4.2.10.2Void405

4.2.11Void405

4.2.12Void405

4.2.13IMS Parameters405

4.2.14RRC buffer size405

4.2.15IAB Parameters405

4.2.15.1Mandatory IAB-MT features405

4.2.15.1aMandatory mobile IAB-MT features411

4.2.15.2General Parameters411

4.2.15.3SDAP Parameters411

4.2.15.4PDCP Parameters411

4.2.15.5BAP Parameters412

4.2.15.6MAC Parameters412

4.2.15.7Physical layer parameters412

4.2.15.7.1BandNR parameters412

4.2.15.7.2Phy-Parameters413

4.2.15.8MeasAndMobParameters Parameters415

4.2.15.9MR-DC Parameters415

4.2.15.10NRDC Parameters415

4.2.16Sidelink Parameters416

4.2.16.1Sidelink Parameters in NR416

4.2.16.1.1Sidelink General Parameters416

4.2.16.1.2Sidelink PDCP Parameters418

4.2.16.1.3Sidelink RLC Parameters419

4.2.16.1.4Sidelink MAC Parameters419

4.2.16.1.5Other PHY parameters420

4.2.16.1.6BandSidelink Parameters421

4.2.16.1.6aSharedSpectrumChAccessParamsSidelinkPerBand Parameters435

4.2.16.1.7BandCombinationListSidelinkEUTRA-NR Parameters438

4.2.16.2Sidelink Parameters in E-UTRA441

4.2.16.2.0General441

4.2.16.2.1BandSideLinkEUTRA parameters442

4.2.17SON parameters442

4.2.18UE-based performance measurement parameters443

4.2.19High speed parameters444

4.2.20Application layer measurement parameters445

4.2.21RedCap Parameters445

4.2.21.1Definition of RedCap UE445

4.2.21.2General parameters446

4.2.21.3PDCP parameters447

4.2.21.4RLC parameters447

4.2.21.5MeasAndMobParameters447

4.2.21.6Physical layer parameters448

4.2.21.6.1BandNR parameters448

4.2.21.7SON parameters451

4.2.22eRedCap Parameters452

4.2.22.1Definition of eRedCap UE452

4.2.22.2General parameters453

4.2.23NCR Parameters455

4.2.23.1Mandatory NCR-MT features455

4.2.23.2General Parameters462

4.2.23.3SDAP Parameters462

4.2.23.4PDCP Parameters462

4.2.23.5RLC Parameters462

4.2.23.6Physical layer Parameters463

4.2.23.6.1Phy-Parameters463

4.2.23.6.2BandNR parameters463

4.2.24Aerial UE Parameters464

4.2.25AI/ML Parameters465

5Optional features without UE radio access capability parameters465

5.1PWS features465

5.2UE receiver features466

5.3RRC connection466

5.4Other features467

5.5Sidelink Features468

5.6RRM measurement features469

5.7MDT and SON features472

5.8Extended DRX features474

5.9Sidelink Relay Features474

5.10MBS features474

5.11Idle/inactive measurement for voice fallback features475

5.12NCR features475

6Conditionally mandatory features without UE radio access capability parameters476

7Void478

8UE Capability Constraints478

Annex A (normative): Differentiation of capabilities480

A.1:TDD/FDD differentiation of capabilities in TDD-FDD CA480

A.2:FR1/FR2 differentiation of capabilities in FR1-FR2 CA481

A.3:TDD/FDD differentiation of capabilities for sidelink482

A.4:Sidelink capabilities applicable to Uu and PC5483

A.5:General differentiation of capabilities in Cross-Carrier operation487

Annex B (informative): UE capability indication for UE capabilities with both FDD/TDD and FR1/FR2 differentiations489

Annex C (informative): Change history491

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

The present document defines the NR UE Radio Access Capability Parameters.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 38.101-1: "NR; User Equipment (UE) radio transmission and reception Part 1: Range 1 Standalone".

[3]3GPP TS 38.101-2: "NR; User Equipment (UE) radio transmission and reception Part 2: Range 2 Standalone".

[4]3GPP TS 38.101-3: "NR; User Equipment (UE) radio transmission and reception Part 3: Range 1 and Range 2 Interworking operation with other radios".

[5]3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[6]3GPP TS 38.211: "NR; Physical channels and modulation".

[7]3GPP TS 37.340: "Evolved Universal Terrestrial Radio Access (E-UTRA) and NR Multi-connectivity".

[8]3GPP TS 38.321: "NR; Medium Access Control (MAC) protocol specification".

[9]3GPP TS 38.331: "NR; Radio Resource Control (RRC) protocol specification".

[10]3GPP TS 38.212: "NR; Multiplexing and channel coding".

[11]3GPP TS 38.213: "NR; Physical layer procedures for control".

[12]3GPP TS 38.214: "NR; Physical layer procedures for data".

[13]3GPP TS 38.215: "NR; Physical layer measurements".

[14]3GPP TS 36.101: "Evolved Universal Terrestrial Radio Access (E-UTRA) radio transmission and reception".

[15]3GPP TS 36.306: "Evolved Universal Terrestrial Radio Access (E-UTRA) User Equipment (UE) radio access capabilities".

[16]3GPP TS 38.323: "NR; Packet Data Convergence Protocol (PDCP) specification".

[17]3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA) Radio Resource Control (RRC); Protocol Specification".

[18]3GPP TS 38.101-4: "NR; User Equipment (UE) radio transmission and reception Part 4: Performance requirements".

[19]3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[20]3GPP TS 25.306: "UE radio access capabilities".

[21]3GPP TS 38.304: "User Equipment (UE) procedures in Idle mode and RRC Inactive state".

[22]3GPP TS 37.355: " LTE Positioning Protocol (LPP)".

[23]3GPP TS 38.340: "NR; Backhaul Adaptation Protocol (BAP) specification".

[24]3GPP TR 38.822: "NR; User Equipment (UE) feature list".

[25]3GPP TS 37.324: "E-UTRA and NR; Service Data Adaptation Protocol (SDAP) specification"

[26]3GPP TS 38.314: "NR; Layer 2 Measurements".

[27]3GPP TS 36.133: "Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements for support of radio resource management".

[28]3GPP TS 38.300: "NR; NR and NG-RAN Overall Description; Stage-2".

[29]3GPP TS 26.247: "Transparent end-to-end Packet-switched Streaming Service (PSS); Progressive Download and Dynamic Adaptive Streaming over HTTP (3GP-DASH)".

[30]3GPP TS 26.114: "IP Multimedia Subsystem (IMS); Multimedia Telephony; Media handling and interaction".

[31]3GPP TS 26.118: "Virtual Reality (VR) profiles for streaming applications".

[32]3GPP TS 37.213: "Physical layer procedures for shared spectrum channel access".

[33]3GPP TS 38.401: "NG-RAN; Architecture description".

[34]3GPP TS 38.101-5: "NR; User Equipment (UE) radio transmission and reception; Part 5: Satellite access Radio Frequency (RF) and performance requirements".

[35]3GPP TS 38.104: "NR; Base Station (BS) radio transmission and reception".

[36]3GPP TS 38.322: "NR; Radio Link Control (RLC) protocol specification".

[37]3GPP TS 23.501: "System Architecture for the 5G System; Stage 2".

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

eRedCap UE: a UE with enhanced reduced capabilities as specified in clause 4.2.22.1.

Fallback band combination: A Uu band combination that would result from another Uu band combination (parent band combination) by releasing at least one SCell or uplink configuration of SCell, or SCG, or SUL. A PC5 band combination that would result from another PC5 band combination (parent band combination) by releasing at least one sidelink carrier. An intra-band non-contiguous band combination is not considered to be a fallback band combination of an intra-band contiguous band combination. A fallback band combination supports the same channel bandwidth(s) for each carrier as its parent band combination(s).

Fallback per band feature set: A feature set per band that has same or lower capabilities than the reported capabilities from the reported feature set per band for a given band.

Fallback per CC feature set: A feature set per CC that has same or lower capabilities than the capabilities of UE (e.g. supported MIMO layers, BW, modulation order) while keeping the numerology the same from the reported feature set per CC for a given carrier per band. The supportedMinBandwidthDL/supportedMinBandwidthUL defines the lower bound of the bandwidth supported by the UE.

RedCap UE: The UE with reduced capabilities as specified in clause 4.2.21.1.

SON report(s): A SON report corresponds to one report from UE such as Random Access report, Radio Link Failure report, Connection Establishment Failure report, Mobility History Information report, Successful Handover report, and Successful PSCell change report.

Switching SCell (sSCell): The SCell configured with cross-carrier scheduling to PCell/PSCell.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

MaxDLDataRate:Maximum DL data rate

MaxDLDataRate_MN:Maximum DL data rate in the MN

MaxDLDataRate_SN:Maximum DL data rate in the SN

MaxULDataRate:Maximum UL data rate

MaxSLtxDataRate:Maximum SL data rate in transmission

MaxSLrxDataRate:Maximum SL data rate in reception

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

A-CSIAperiodic-CSI

AI/MLArtificial Intelligence/Machine Learning

ATGAir To Ground

BAPBackhaul Adaptation Protocol

BCBand Combination

BPSBody Proximity Sensing

BTBluetooth

CCSCross Carrier Scheduling

CLTMConditional L1/L2 Triggered Mobility

CMRChannel Measurement Resource

CPACConditional PSCell Addition/Change

DAPSDual Active Protocol Stack

DLDownlink

DSRDelay Status Report

EHCEthernet Header Compression

FSFeature Set

FSPCFeature Set Per Component-carrier

FWAFixed Wireless Access

GSOGeosynchronous Orbit

HSDNHigh Speed Dedicated Network

IAB-MTIntegrated Access Backhaul Mobile Termination

IDCIn-Device Coexistence

MACMedium Access Control

MHIMobility History Information

MBSMulticast/Broadcast Service

MCGMaster Cell Group

MNMaster Node

MO-SDTMobile Originated Small Data Transmission

MRBMBS Radio Bearer

MR-DCMulti-Radio Dual Connectivity

MSDMaximum Sensitivity Degradation

MT-SDTMobile Terminated Small Data Transmission

mTRPMultiple TRP

MUSIMMulti-Universal Subscriber Identity Module

NCJTNon-Coherent Joint Transmission

NCRNetwork Controlled Repeater

NCR-MTNCR Mobile Termination

NCSGNetwork Controlled Small Gap

NESNetwork Energy Savings

NGSONon-Geosynchronous Orbit

NTNNon-Terrestrial Network

P-CSIPeriodic CSI

PDCPPacket Data Convergence Protocol

PSIPDU Set Importance

QoEQuality of Experience

RLCRadio Link Control

RTTRound Trip Time

SCGSecondary Cell Group

SDAPService Data Adaptation Protocol

SDLSupplementary Downlink

SNSecondary Node

sTRPServing TRP

SULSupplementary Uplink

TNTerrestrial Network

TRPTransmit/Receive Point

UDCUplink Data Compression

ULUplink

VSATVery Small Aperture Terminal

WLANWireless Local Area Network

XReXtended Reality

## 4UE radio access capability parameters

## 4.1Supported max data rate

## 4.1.1General

The DL, UL and SL max data rate supported by the UE is calculated by band or band combinations supported by the UE. A UE supporting NR (NR SA, MR-DC) shall support the calculated DL and UL max data rate defined in 4.1.2. A UE supporting NR sidelink communication shall support the calculated SL max data rate defined in 4.1.5.

## 4.1.2Supported max data rate for DL/UL

For NR, the approximate data rate for a given number of aggregated carriers in a band or band combination is computed as follows.

wherein

J is the number of aggregated component carriers in a band or band combination

Rmax = 948/1024

For the j-th CC,

is the maximum number of supported layers given by maxNumberMIMO-LayersPDSCH for downlink and maximum of maxNumberMIMO-LayersCB-PUSCH and maxNumberMIMO-LayersNonCB-PUSCH for uplink.

is the maximum supported modulation order given by supportedModulationOrderDL for downlink and supportedModulationOrderUL for uplink.

is the scaling factor given by scalingFactor or scalingFactor-1024QAM-FR1 and can take the values 1, 0.8, 0.75, and 0.4.

is the numerology (as defined in TS 38.211 [6])

is the average OFDM symbol duration in a subframe for numerology , i.e. . Note that normal cyclic prefix is assumed.

is the maximum RB allocation in bandwidth  with numerology , as defined in 5.3 TS 38.101-1 [2], 5.3 TS 38.101-2 [3], and 5.3 TS 38.101-5 [34], where  is the UE supported maximum bandwidth in the given band or band combination.

is the overhead and takes the following values

0.14, for frequency range FR1 for DL

0.18, for frequency range FR2 for DL

0.08, for frequency range FR1 for UL

0.10, for frequency range FR2 for UL

NOTE 1:Only one of the UL or SUL carriers (the one with the higher data rate) is counted for a cell operating SUL.

NOTE 2:For UL Tx switching between carriers, only the supported MIMO layer combination across carriers that results in the highest combined data rate is counted for the carriers in the supported maximum UL data rate.

The approximate maximum data rate can be computed as the maximum of the approximate data rates computed using the above formula for each of the supported band or band combinations. For the CCs where UE supports pdsch-1024QAM-2MIMO-FR1-r17 for the concerned band, data rate shall be derived as maximum what UE would support if using 1024 QAM (when mcs-Table-r17 or mcs-TableDCI-1-2-r17 is configured) or 256 QAM.

For single carrier NR SA operation and except for UEs supporting supportOfERedCap-r18, the UE shall support a data rate for the carrier that is no smaller than the data rate computed using the above formula, with  and component  is no smaller than 4.J=1 CCvLayers(j)⋅Qmj⋅fj

NOTE 3: As an example, the value 4 in the component above can correspond to ,  and .vLayers(j)=1Qmj= 4fj=1

For single carrier NR SA operation and for UEs supporting supportOfERedCap-r18, the UE shall support a data rate for the carrier that is the data rate computed using the above formula, with  and:J=1 CC

if the UE supports eRedCapNotReducedBB-BW-r18:

-component  is 0.75 if , or;vLayers(j)⋅Qmj⋅fjvLayers(j)=1

-component  is 0.8 if ;vLayers(j)⋅Qmj⋅fjvLayers(j)=2

else:

-component  is 3.2, and;;vLayers(j)⋅Qmj⋅fj

- is 25 if μ = 0 or, 12 if μ = 1;

For EUTRA in case of MR-DC, the approximate data rate for a given number of aggregated carriers in a band or band combination is computed as follows.

Data rate (in Mbps) = 10-3*j=1JTBSj

wherein

J is the number of aggregated EUTRA component carriers in MR-DC band combination

is the total maximum number of DL-SCH transport block bits received or the total maximum number of UL-SCH transport block bits transmitted, within a 1ms TTI for j-th CC, as derived from TS 36.213 [19] based on the UE supported maximum MIMO layers for the j-th CC, and based on the maximum modulation order for the j-th CC and number of PRBs based on the bandwidth of the j-th CC according to indicated UE capabilities.TBSj

The approximate maximum data rate can be computed as the maximum of the approximate data rates computed using the above formula for each of the supported band or band combinations.

For MR-DC, the approximate maximum data rate is computed as the sum of the approximate maximum data rates from NR and EUTRA.

## 4.1.3Void

## 4.1.4Total layer 2 buffer size for DL/UL

The total layer 2 buffer size is defined as the sum of the number of bytes that the UE is capable of storing in the RLC transmission windows and RLC reception and reassembly windows and also in PDCP reordering windows for all radio bearers.

The required total layer 2 buffer size in MR-DC is the maximum value of the calculated values based on the following equations:

-MaxULDataRate_MN * RLCRTT_MN + MaxULDataRate_SN * RLCRTT_SN + MaxDLDataRate_SN * RLCRTT_SN + MaxDLDataRate_MN * (RLCRTT_SN + X2/Xn delay + Queuing in SN)

-MaxULDataRate_MN * RLCRTT_MN + MaxULDataRate_SN * RLCRTT_SN + MaxDLDataRate_MN * RLCRTT_MN + MaxDLDataRate_SN * (RLCRTT_MN + X2/Xn delay + Queuing in MN)

Otherwise it is calculated by MaxDLDataRate * RLC RTT + MaxULDataRate * RLC RTT.

NOTE:Additional L2 buffer required for preprocessing of data is not taken into account in above formula.

The required total layer 2 buffer size is determined as the maximum total layer 2 buffer size of all the calculated ones for each band combination and the applicable Feature Set combination in the supported MR-DC or NR band combinations. The RLC RTT for NR cell group corresponds to the smallest SCS numerology supported in the band combination and the applicable Feature Set combination.

wherein

X2/Xn delay + Queuing in SN = 25ms if SCG is NR, and 55ms if SCG is EUTRA

X2/Xn delay + Queuing in MN = 25ms if MCG is NR, and 55ms if MCG is EUTRA

RLC RTT for EUTRA cell group = 75ms

RLC RTT for NR cell group is defined in Table 4.1.4-1

Table 4.1.4-1: RLC RTT for NR cell group per SCS

## 4.1.5Supported max data rate for SL

For NR sidelink, the approximate data rate is computed as follows.

data rate (in Mbps)=10-6⋅vLayers⋅Qm⋅f⋅Rmax⋅NPRBBW,μ⋅12Tsμ⋅1-OH

wherein

Rmax = 948/1024,

is the the maximum number of supported layers for sidelink transmission (or reception) given by UE capability on supporting rank 2 PSSCH transmission and rankTwoReception,vLayers

is the maximum supported modulation order between 6 or 8 given by sl-Tx-256QAM and sl-Rx-256QAM,Qm

is the scaling factor for sidelink transmission and reception given by scalingFactorTxSidelink and scalingFactorRxSidelink respectively, as specified in TS 36.331 [17] and TS 38.331 [9], and can take the values 1, 0.8, 0.75, and 0.4.f

is the numerology (as defined in TS 38.211 [6])

is the average OFDM symbol duration in a subframe for numerology , i.e. . Note that normal cyclic prefix is assumed.

is the maximum possible RB allocation in bandwidth BW for PSSCH, where BW is the UE supported maximum bandwidth in the given band or band combination,NPRBBW,μ

is the overhead and takes the following valuesOH

0.217, for frequency range FR1 for SL

0.25, for frequency range FR2 for SL

## 4.1.6Total layer 2 buffer size for NR SL

The total layer 2 buffer size for NR sidelink communication is defined as the sum of the number of bytes that the UE is capable of storing in the RLC transmission windows and RLC reception and reassembly windows and also in PDCP reordering windows for all radio bearers for NR sidelink communication.

The required total layer 2 buffer size for NR sidelink communication is the maximum value of the calculated values based on the following equations:

MaxSLtxDataRate * RLC RTT + MaxSLrxDataRate * RLC RTT.

NOTE:Additional L2 buffer required for preprocessing of data is not taken into account in above formula.

The required total layer 2 buffer size for NR sidelink communication is determined as the maximum total layer 2 buffer size of all the calculated ones for each band combination and the applicable Feature Set combination in the supported NR sidelink band combinations. The RLC RTT for NR sidelink communication corresponds to the smallest SCS numerology supported in the band combination and the applicable Feature Set combination.

wherein

RLC RTT for NR sidelink communication is defined in Table 4.1.6-1

Table 4.1.6-1: RLC RTT for NR sidelink communication per SCS

## 4.2UE Capability Parameters

## 4.2.1Introduction

The following clauses define the UE radio access capability parameters. Only parameters for which there is the possibility for UEs to signal different values are considered as UE radio access capability parameters. Therefore, mandatory features without capability parameters that are the same for all UEs are not listed here.

The network needs to respect the signalled UE radio access capability parameters when configuring the UE and when scheduling the UE.

For capabilities that required to be set consistently for all FDD-FR1 bands (i.e. capabilities that are supposed to be per UE), the UE shall also set capability values for all SUL bands with same values for FDD-FR1 bands if SUL band is supported by the UE.

The UE may support different functionalities between FDD and TDD, and/or between FR1 and FR2. The UE shall indicate the UE capabilities as follows. In the table of UE capability parameter in subsequent clauses, "Yes" in the column by "FDD-TDD DIFF" and "FR1-FR2 DIFF" indicates the UE capability field can have a different value for between FDD and TDD or between FR1 and FR2 and "No" indicates if it cannot. "(Incl FR2-2 DIFF)" in the column by "FR1-FR2 DIFF" indicates the UE capability field can have a different value for between FR2-1 and FR2-2. Regarding to the per UE capabilities that are FDD/TDD differentiated(i.e. capabilities indicated as "Yes" in the column by "FDD-TDD DIFF"), the corresponding capabilities indicated by the FDD capability is applied to SUL/SDL if SUL/SDL band is supported by the UE. "FD" in the column indicates to refer the associated field description. "FR1 only" or "FR2 only" in the column indicates the associated feature is only supported in FR1 or FR2 and "TDD only" indicates the associated feature is only supported in TDD and not applicable to SUL/SDL carriers. "N/A" in the column indicates it is not applicable to the feature (e,g. the signalling supports the UE to have different values between FDD and TDD or between FR1 and FR2).

1>set all fields of UE-NR/MRDC-Capability except fdd-Add-UE-NR/MRDC/Sidelink-Capabilities, tdd-Add-UE-NR/MRDC/Sidelink-Capabilities, fr1-Add-UE-NR/MRDC-Capabilities and fr2-Add-UE-NR/MRDC-Capabilities, to include the values applicable for all duplex mode(s) and frequency range(s) that the UE supports;

1>if UE supports both FDD (or SUL/SDL) and TDD and if (some of) the UE capability fields have a different value for FDD (or SUL/SDL) and TDD:

2>if for FDD (and, if the UE supports SUL/SDL, for SUL/SDL), the UE supports additional functionality compared to what is indicated by the previous fields of UE-NR/MRDC-Capability/SidelinkParameters:

3>include field fdd-Add-UE-NR/MRDC/Sidelink-Capabilities and set it to include fields reflecting the additional functionality applicable for FDD;

2>if for TDD, the UE supports additional functionality compared to what is indicated by the previous fields of UE-NR/MRDC-Capability/SidelinkParameters:

3>include field tdd-Add-UE-NR/MRDC/Sidelink-Capabilities and set it to include fields reflecting the additional functionality applicable for TDD;

1>if UE supports both FR1 and FR2 and if (some of) the UE capability fields have a different value for FR1 and FR2:

2>if for FR1, the UE supports additional functionality compared to what is indicated by the previous fields of UE-NR/MRDC-Capability:

3>include field fr1-Add-UE-NR/MRDC-Capabilities and set it to include fields reflecting the additional functionality applicable for FR1;

2>if for FR2, the UE supports additional functionality compared to what is indicated by the previous fields of UE-NR/MRDC-Capability:

3>include field fr2-Add-UE-NR/MRDC-Capabilities and set it to include fields reflecting the additional functionality applicable for FR2;

NOTE 1:The fields which indicate "shall be set to 1" or "shall be set to supported" in the following tables means these features are purely mandatory and are assumed they are the same as mandatory without capability signalling.

NOTE 2:For the case where the UE is allowed to support different functionality between FDD and TDD and between FR1 and FR2 according to the specification, the UE capability indication is clarified in Annex B.

NOTE 2a:In this release of the specification, if the UE is allowed to support different functionalities between FDD and TDD, and/or between FR1 and FR2, these functionalities are signalled per band with the text "UE shall set the capability value consistently for all FDD-FR1 bands, all TDD-FR1 bands, all TDD-FR2-1 bands and all TDD-FR2-2 bands respectively".

For optional features, the UE radio access capability parameter indicates whether the feature has been implemented and successfully tested. For mandatory features with the UE radio access capability parameter, the parameter indicates whether the feature has been successfully tested. In the table of UE capability parameter in subsequent clauses, "Yes" in the column by "M" indicates the associated feature is mandatory and "No" indicates the associated feature is optional. "CY" in the column indicates the associated feature is conditional mandatory and the condition is described in the field description and the associated feature is considered mandatory with capability parameter, when the described condition is satisfied. "FD" in the column indicates to refer the associated field description. Some parameters in subsequent clauses are not related to UE features and in the case, "N/A" is indicated in the column.

UE capability parameters have hierarchical structure. In the table of UE capability parameter in subsequent clauses, "Per" indicates the level the associated parameter is included. "UE" in the column indicates the associated parameter is signalled per UE, "Band" indicates it is signalled per band, "BC" indicates it is signalled per band combination, "FS" indicates it is signalled per feature set (per band per band combination), "FSPC" indicates it is signalled per feature set per component carrier (per CC per band per band combination), and "FD" in the column indicates to refer the associated field description. "Per band and per band combination" indicates a UE capability parameter defined in both per band and per band combination with same feature components.

For a capability with same comprised parameter(s) defined "per band and per band combination":

-When the UE signals "per BC" but does not signal "per band" capability on some subset of the bands in the CA combination, the UE does not support the capability/comprised parameter(s) in the band without "per band" capability.

-When the UE signals "per band" but does not include "per BC" for a certain BC, the UE supports the capability/comprised parameter(s) as indicated in the "per band" without further per BC limitations. The UE shall also support the signalled "per band" capabilities in any CA combination composed of the respective band.

-When the UE signals both "per band" and "per BC" capability, if capability/ comprised parameter(s) is not counted across CCs, the minimum capability between "per BC" capability and "per band" capability is applied to a band for which the UE capability is signalled; if the comprised parameter(s) is counted across CCs and CA is not configured, the "per band" capability is applied regardless of reported "per BC" capability; if the comprised parameter(s) is counted across CCs of intra-band CA (all CCs over the CA are within the same band) and/or inter-band CA (all CCs over the CA are associated with more than one band), the "per band" capability is applied across CCs within the corresponding intra-band CA, the "per BC" capability is applied across CCs within the corresponding inter-band CA.

For "per band and per band combination" capabilities with prerequisite capability in "per band and per band combination", the UE shall indicate support of the prerequisite capability in the corresponding band/BC, respectively.

NOTE 3:Unless otherwise specified, for dependent capabilities with prerequisite capability in a finer granularity, the UE should indicate support of the prerequisite capability in at least one finer granularity. And the dependent capability is supported only in the finer granularity where the prerequisite capability is supported, e.g. a UE indicating support of supportNewDMRS-Port-r16 (dependent capability which is defined per band) should indicate at least one band combination where singleDCI-SDM-scheme-r16 (prerequisite capability which is defined per feature set) is supported in the corresponding band. In this case, supportNewDMRS-Port-r16 is considered supported only in the corresponding band of the band combination where singleDCI-SDM-scheme-r16 is supported.

## 4.2.2General parameters

## 4.2.3SDAP Parameters

## 4.2.4PDCP Parameters

## 4.2.5RLC parameters

## 4.2.6MAC parameters

## 4.2.6.1MAC-Parameters

## 4.2.6.2MAC-ParametersPerBand

## 4.2.7Physical layer parameters

## 4.2.7.1BandCombinationList parameters

## 4.2.7.2BandNR parameters

## 4.2.7.2aSharedSpectrumChAccessParamsPerBand

## 4.2.7.2bFR2-2-AccessParamsPerBand

## 4.2.7.3CA-ParametersEUTRA

## 4.2.7.4CA-ParametersNR

## 4.2.7.5FeatureSetDownlink parameters

## 4.2.7.6FeatureSetDownlinkPerCC parameters

## 4.2.7.7FeatureSetUplink parameters

## 4.2.7.8FeatureSetUplinkPerCC parameters

## 4.2.7.9MRDC-Parameters

## 4.2.7.10Phy-Parameters

## 4.2.7.11Other PHY parameters

## 4.2.7.12NRDC-Parameters

## 4.2.7.13CarrierAggregationVariant

## 4.2.7.14Phy-ParametersSharedSpectrumChAccess

## 4.2.8Void

## 4.2.9MeasAndMobParameters

## 4.2.9aMeasAndMobParametersMRDC

## 4.2.10Inter-RAT parameters

## 4.2.10.1Void

## 4.2.10.2Void

## 4.2.11Void

## 4.2.12Void

## 4.2.13IMS Parameters

NOTE:In this release of specification, IMS voice over split bearer is not supported for NR-DC, NE-DC, and L2 multi-path relay.

## 4.2.14RRC buffer size

The RRC buffer size is defined as the maximum overall RRC configuration size that the UE is required to store. The RRC buffer size is 45Kbytes.

## 4.2.15IAB Parameters

## 4.2.15.1Mandatory IAB-MT features

Table 4.2.15.1-1, Table 4.2.15.1-2 and Table 4.2.15.1-3 capture feature groups, which are mandatory for an IAB-MT. In addition, it is mandatory for an IAB-MT which is not a mobile IAB-MT to support the following features:

-Cell barring based on iab-Support, as specified in TS 38.331 [9].

-Inclusion of iab-NodeIndication, as specified in TS 38.331 [9].

All other feature groups or components of the feature groups as captured in TR 38.822 [24] as well as capabilities specified in this specification are optional for an IAB-MT, unless indicated otherwise.

Table 4.2.15.1-1: Layer-1 mandatory features for IAB-MT

Table 4.2.15.1-2: Layer-2 and Layer-3 mandatory features for IAB-MT

Table 4.2.15.1-3: RF/RRM mandatory features for IAB-MT

## 4.2.15.1aMandatory mobile IAB-MT features

Mobile IAB-MT shall apply the same capabilities as IAB-MT unless indicated otherwise. In addition, it is mandatory for mobile IAB-MT to support the following features:

-Acquisition of gNB-ID-Length from SIB1, as specified in TS 38.331 [9].

-Cell barring based on mobileIAB-Support, as specified in TS 38.331 [9].

-Inclusion of mobileIAB-NodeIndication, as specified in TS 38.331 [9].

All IAB-MT features and corresponding capabilities related to MR-DC and BAP header rewriting are not used by the mobile IAB-MT.

## 4.2.15.2General Parameters

## 4.2.15.3SDAP Parameters

## 4.2.15.4PDCP Parameters

## 4.2.15.5BAP Parameters

## 4.2.15.6MAC Parameters

## 4.2.15.7Physical layer parameters

## 4.2.15.7.1BandNR parameters

## 4.2.15.7.2Phy-Parameters

## 4.2.15.8MeasAndMobParameters Parameters

## 4.2.15.9MR-DC Parameters

## 4.2.15.10NRDC Parameters

## 4.2.16Sidelink Parameters

## 4.2.16.1Sidelink Parameters in NR

## 4.2.16.1.1Sidelink General Parameters

## 4.2.16.1.2Sidelink PDCP Parameters

## 4.2.16.1.3Sidelink RLC Parameters

## 4.2.16.1.4Sidelink MAC Parameters

## 4.2.16.1.5Other PHY parameters

## 4.2.16.1.6BandSidelink Parameters

## 4.2.16.1.6aSharedSpectrumChAccessParamsSidelinkPerBand Parameters

## 4.2.16.1.7BandCombinationListSidelinkEUTRA-NR Parameters

## 4.2.16.2Sidelink Parameters in E-UTRA

## 4.2.16.2.0General

## 4.2.16.2.1BandSideLinkEUTRA parameters

## 4.2.17SON parameters

## 4.2.18UE-based performance measurement parameters

## 4.2.19High speed parameters

## 4.2.20Application layer measurement parameters

## 4.2.21RedCap Parameters

## 4.2.21.1Definition of RedCap UE

RedCap UE is the UE with reduced capability:

-The maximum bandwidth is 20 MHz for FR1, and is 100 MHz for FR2. UE features and corresponding capabilities related to UE bandwidths wider than 20 MHz in FR1 or wider than 100 MHz in FR2 are not supported by RedCap UEs;

-The mandatory support (with capability signalling, enhancedChannelRaster-r18) of the channel raster as specified in TS 38.101-1 [2], clause 5.4I, for all bands supported by the UE;

-The maximum mandatory supported DRB number is 8;

-The mandatory supported PDCP SN length is 12 bits while 18 bits being optional;

-The mandatory supported RLC AM SN length is 12 bits while 18 bits being optional;

-For FR1, 1 DL MIMO layer if 1 Rx branch is supported, and 2 DL MIMO layers if 2 Rx branches are supported; for FR2, either 1 or 2 DL MIMO layers can be supported, while 2 Rx branches are always supported. For FR1 and FR2, UE features and corresponding capabilities related to more than 2 UE Rx branches or more than 2 DL MIMO layers, as well as UE features and capabilities related to more than 1 UE Tx branch or more than 1 UL MIMO layer are not supported by RedCap UEs;

-CA, MR-DC, DAPS, CPAC, IAB (i.e., the RedCap UE is not expected to act as IAB node), and NCR (i.e., the RedCap UE is not expected to act as NCR-MT) related UE features and corresponding capabilities are not supported by RedCap UEs. All other feature groups or components of the feature groups as captured in TR 38.822 [24] as well as capabilities specified in this specification remain applicable for RedCap UEs same as other UEs, unless indicated otherwise.

## 4.2.21.2General parameters

## 4.2.21.3PDCP parameters

## 4.2.21.4RLC parameters

## 4.2.21.5MeasAndMobParameters

## 4.2.21.6Physical layer parameters

## 4.2.21.6.1BandNR parameters

## 4.2.21.7SON parameters

## 4.2.22eRedCap Parameters

## 4.2.22.1Definition of eRedCap UE

eRedCap UE is the UE with reduced peak data rate and, with or without reduced baseband bandwidth in FR1:

-The maximum bandwidth is 20 MHz for FR1. UE features and corresponding capabilities related to UE bandwidths wider than 20 MHz in FR1 are not supported by eRedCap UEs. eRedCap UEs do not support operation in FR2 and in FR1 60kHz SCS.

-The mandatory support (with capability signalling, enhancedChannelRaster-r18) of the channel raster as specified in TS 38.101-1 [2], clause 5.4I, for all bands supported by the UE;

-The maximum mandatory supported DRB number is 8;

-The mandatory supported PDCP SN length is 12 bits while 18 bits being optional;

-The mandatory supported RLC AM SN length is 12 bits while 18 bits being optional;

-1 DL MIMO layer if 1 Rx branch is supported, and 2 DL MIMO layers if 2 Rx branches are supported. UE features and corresponding capabilities related to more than 2 UE Rx branches or more than 2 DL MIMO layers, as well as UE features and capabilities related to more than 1 UE Tx branch or more than 1 UL MIMO layer are not supported by eRedCap UEs;

-CA, MR-DC, DAPS, CPAC, IAB (i.e., the eRedCap UE is not expected to act as IAB node), and NCR (i.e., the eRedCap UE is not expected to act as NCR-MT) related UE features and corresponding capabilities are not supported by eRedCap UEs. All other feature groups or components of the feature groups as captured in TR 38.822 [24] as well as capabilities specified in this specification remain applicable for eRedCap UEs same as other UEs, unless indicated otherwise.

## 4.2.22.2General parameters

## 4.2.23NCR Parameters

## 4.2.23.1Mandatory NCR-MT features

Table 4.2.23.1-1, Table 4.2.23.1-2 and Table 4.2.23.1-3 capture feature groups, which are mandatory for an NCR-MT. In addition, it is mandatory for an NCR-MT to support the following features:

-Cell barring based on ncr-Support, as specified in TS 38.331 [9].

-Inclusion of ncr-NodeIndication, as specified in TS 38.331 [9].

CA, MR-DC, handover (e.g. CHO, DAPS, CPAC, etc), unlicensed band, HPUE Duty cycle, MPR related UE features and corresponding capabilities are not supported by an NCR-MT. 7.5kHz UL raster shift is not applicable to NCR-MT. All other feature groups or components of the feature groups as captured in TR 38.822 [24] as well as capabilities specified in this specification are optional for an NCR-MT, unless indicated otherwise.

Table 4.2.23.1-1: Layer-1 mandatory features for NCR-MT

Table 4.2.23.1-2: Layer-2 and Layer-3 mandatory features for NCR-MT

Table 4.2.23.1-3: RF and RRM mandatory features for NCR-MT

## 4.2.23.2General Parameters

## 4.2.23.3SDAP Parameters

## 4.2.23.4PDCP Parameters

## 4.2.23.5RLC Parameters

## 4.2.23.6Physical layer Parameters

## 4.2.23.6.1Phy-Parameters

## 4.2.23.6.2BandNR parameters

## 4.2.24Aerial UE Parameters

## 4.2.25AI/ML Parameters

## 5Optional features without UE radio access capability parameters

## 5.1PWS features

## 5.2UE receiver features

## 5.3RRC connection

## 5.4Other features

## 5.5Sidelink Features

## 5.6RRM measurement features

## 5.7MDT and SON features

## 5.8Extended DRX features

## 5.9Sidelink Relay Features

## 5.10MBS features

## 5.11Idle/inactive measurement for voice fallback features

## 5.12NCR features

## 6Conditionally mandatory features without UE radio access capability parameters

## 7Void

## 8UE Capability Constraints

The following table lists constraints indicating the UE capabilities that the UE shall support.

## Annex A (normative):Differentiation of capabilities

## A.1:TDD/FDD differentiation of capabilities in TDD-FDD CA

Annex A.1 specifies for which TDD and FDD serving cells a UE supporting TDD/FDD CA shall support a feature/capability for which it indicates support within the capability signalling.

A UE that indicates support for TDD/FDD CA (e.g. MCG or SCG):

-For the fields for which the UE is allowed to indicate different support for FDD and TDD, the UE shall support the feature on the PCell and/or SCell(s), as specified in tables A.1-1 in accordance to the following rules:

-PCell: the UE shall support the feature for the PCell, if the UE indicates support of the feature for the PCell duplex mode;

-PSCell: the UE shall support the feature for the PSCell, if the UE indicates support of the feature for the PSCell duplex mode;

-Per serving cell: the UE shall support the feature for a serving cell if the UE indicates support of the feature for the serving cell's duplex mode;

-All serving cells: UE shall support the feature for all serving cells in a CG if the UE indicates support of the feature for both TDD and FDD duplex modes;

-Associated serving cells: UE shall support the feature if the UE indicates support of the feature for all associated serving cells's duplex modes;

-For the fields where the UE is not allowed to indicate different support for FDD and TDD, the UE shall support the feature for PCell and SCell(s) if the UE indicates support of the feature via the common capability bit.

Table A.1-1: UE capabilities for which FDD/TDD differentiation is allowed

## A.2:FR1/FR2 differentiation of capabilities in FR1-FR2 CA

Annex A.2 specifies for which FR1 and FR2 serving cells a UE supporting FR1/FR2 CA shall support a feature/capability for which it indicates support within the capability signalling.

A UE that indicates support for FR1/FR2 CA (e.g. MCG or SCG):

-For the fields for which the UE is allowed to indicate different support for FR1 and FR2, the UE shall support the feature on the PCell and/or SCell(s), as specified in tables A.2-1 in accordance to the following rules:

-PCell: the UE shall support the feature for the PCell, if the UE indicates support of the feature for the PCell FR mode;

-Associated serving cells: UE shall support the feature if the UE indicates support of the feature for associated serving cells's FR modes;

-For the fields where the UE is not allowed to indicate different support for FR1 and FR2, the UE shall support the feature for PCell and SCell(s) if the UE indicates support of the feature via the common capability bit.

Table A.2-1: UE capabilities for which FR1/FR2 differentiation is allowed

## A.3:TDD/FDD differentiation of capabilities for sidelink

Annex A.3 specifies for which TDD and FDD serving cells for Uu interface and carrier for PC5 interface a UE supporting sidelink shall support a feature/capability for which it indicates support within the capability signalling.

A UE that indicates support for sidelink:

-For the fields for which the UE is allowed to indicate different support for FDD and TDD, the UE shall support the feature on the PCell and/or SCell(s) for Uu interface, as specified in tables A.3-1 in accordance to the following rules:

-Per serving cell: the UE shall support the feature for a serving cell if the UE indicates support of the feature for the serving cell's duplex mode;

-Associated serving cells: UE shall support the feature if the UE indicates support of the feature for all associated serving cells's duplex modes;

-For the fields where the UE is not allowed to indicate different support for FDD and TDD, the UE shall support the feature for PCell and SCell(s) for Uu interface and carrier for PC5 interface if the UE indicates support of the feature via the common capability bit.

Table A.3-1: Rel-16 UE capabilities for which FDD/TDD differentiation is allowed

## A.4:Sidelink capabilities applicable to Uu and PC5

Annex A.4 specifies for each sidelink related capability, in which interface (i.e., UECapabilityInformation in Uu RRC and UECapabilityInformationSidelink in PC5 RRC) a UE supporting sidelink shall report the concerned capability:

-UECapabilityInformation: the concerned sidelink capability is reported within UECapabilityInformation;

-UECapabilityInformationSidelink: the concerned sidelink capability is reported within UECapabilityInformationSidelink;

Table A.4-1: Sidelink capability reported in UECapabilityInformation/ UECapabilityInformationSidelink

## A.5:General differentiation of capabilities in Cross-Carrier operation

Annex A.5 specifies for which multiple serving cells a UE supporting cross-carrier operation shall support a feature/capability for which it indicates support within the capability signalling.

A UE that indicates support for cross-carrier operation in CA (e.g. MCG or SCG):

-For the fields for which the UE is allowed to indicate different support for different bands, the UE shall support the feature on the PCell and/or SCell(s) in cross-carrier operation, as specified in table A.5-1 in accordance to the following rules:

-Triggered serving cell: the UE shall support the feature if the UE indicates support of the feature for the band of the scheduled/triggered/indicated serving cell;

-Triggering&Triggered serving cells: UE shall support the feature if the UE indicates support of the feature for the band of both the scheduling/triggering/indicating serving cell and the scheduled/triggered/indicated serving cell;

Table A.5-1: General UE capabilities for which differentiation is allowed

## Annex B (informative):UE capability indication for UE capabilities with both FDD/TDD and FR1/FR2 differentiations

Annex B clarifies the UE capability indication for the case where the UE is allowed to support different functionality between FDD and TDD, and between FR1 and FR2. Table B-1 clarifies the setting of UE capability fields for cases where the UE supports the corresponding feature in different combinations of duplex mode and frequency range. There are two possible ways of UE capability indication in Case 3 and Case 8.

Table B-1: UE capability indication for UE capabilities with both FDD/TDD and FR1/FR2 differentiations

NOTE 1:For a UE capability which cannot be differentiated between FR2-1 and FR2-2, 'FR2 TDD' in Table B-1 includes both 'FR2-1 TDD' and 'FR2-2 TDD'.

NOTE 2:For a UE capability which can be differentiated between FR2-1 and FR2-2, 'FR2 TDD' in Table B-1 only means 'FR2-1 TDD'.

## Annex C (informative):Change history
