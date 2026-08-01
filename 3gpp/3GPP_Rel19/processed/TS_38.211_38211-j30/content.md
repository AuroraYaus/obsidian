---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.211_38211-j30/content.md"
---
# TS 38.211 38211-j30

3GPP TS 38.211 V19.3.0 (2026-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Physical channels and modulation

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP..The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords

New Radio, Layer 1

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

Foreword8

1Scope9

2References9

3Definitions of terms, symbols and abbreviations9

3.1Terms9

3.2Symbols9

3.3Abbreviations11

4Frame structure and physical resources11

4.1General11

4.2Numerologies12

4.3Frame structure12

4.3.1Frames and subframes12

4.3.2Slots13

4.4Physical resources14

4.4.1Antenna ports14

4.4.2Resource grid14

4.4.3Resource elements14

4.4.4Resource blocks14

4.4.4.1General14

4.4.4.2Point A15

4.4.4.3Common resource blocks15

4.4.4.4Physical resource blocks15

4.4.4.5Virtual resource blocks15

4.4.4.6Interlaced resource blocks15

4.4.5Bandwidth part16

4.4.6Common MBS frequency resource16

4.5Carrier aggregation16

5Generic functions17

5.1Modulation mapper17

5.1.1π/2-BPSK17

5.1.2BPSK17

5.1.3QPSK17

5.1.416QAM17

5.1.564QAM17

5.1.6256QAM18

5.1.71024QAM18

5.2Sequence generation18

5.2.1Pseudo-random sequence generation18

5.2.2Low-PAPR sequence generation type 118

5.2.2.1Base sequences of length 36 or larger18

5.2.2.2Base sequences of length less than 3619

5.2.3Low-PAPR sequence generation type 222

5.2.3.1Sequences of length 30 or larger22

5.2.3.2Sequences of length less than 3022

5.3OFDM baseband signal generation26

5.3.1OFDM baseband signal generation for all channels except PRACH and RIM-RS26

5.3.2OFDM baseband signal generation for PRACH28

5.3.3OFDM baseband signal generation for RIM-RS30

5.4Modulation and upconversion31

6Uplink31

6.1Overview31

6.1.1Overview of physical channels31

6.1.2Overview of physical signals31

6.2Physical resources31

6.2.1Muting resource32

6.3Physical channels32

6.3.1Physical uplink shared channel32

6.3.1.1Scrambling32

6.3.1.2Modulation33

6.3.1.2aInter-slot cover code34

6.3.1.3Layer mapping34

6.3.1.4Transform precoding34

6.3.1.5Precoding35

6.3.1.6Mapping to virtual resource blocks60

6.3.1.7Mapping from virtual to physical resource blocks60

6.3.2Physical uplink control channel61

6.3.2.1General61

6.3.2.2Sequence and cyclic shift hopping61

6.3.2.2.1Group and sequence hopping61

6.3.2.2.2Cyclic shift hopping62

6.3.2.3PUCCH format 062

6.3.2.3.1Sequence generation62

6.3.2.3.2Mapping to physical resources63

6.3.2.4PUCCH format 163

6.3.2.4.1Sequence modulation63

6.3.2.4.2Mapping to physical resources64

6.3.2.5PUCCH format 264

6.3.2.5.1Scrambling64

6.3.2.5.2Modulation65

6.3.2.5.2ASpreading65

6.3.2.5.3Mapping to physical resources65

6.3.2.6PUCCH formats 3 and 466

6.3.2.6.1Scrambling66

6.3.2.6.2Modulation66

6.3.2.6.3Block-wise spreading66

6.3.2.6.4Transform precoding67

6.3.2.6.5Mapping to physical resources67

6.3.3Physical random-access channel68

6.3.3.1Sequence generation68

6.3.3.2Mapping to physical resources75

6.4Physical signals95

6.4.1Reference signals95

6.4.1.1Demodulation reference signal for PUSCH95

6.4.1.1.1Sequence generation95

6.4.1.1.2(void)97

6.4.1.1.3Precoding and mapping to physical resources97

6.4.1.2Phase-tracking reference signals for PUSCH102

6.4.1.2.1Sequence generation102

6.4.1.2.1.1Sequence generation if transform precoding is not enabled102

6.4.1.2.1.2Sequence generation if transform precoding is enabled102

6.4.1.2.2Mapping to physical resources103

6.4.1.2.2.1Precoding and mapping to physical resources if transform precoding is not enabled103

6.4.1.2.2.2Mapping to physical resources if transform precoding is enabled105

6.4.1.3Demodulation reference signal for PUCCH106

6.4.1.3.1Demodulation reference signal for PUCCH format 1106

6.4.1.3.1.1Sequence generation106

6.4.1.3.1.2Mapping to physical resources107

6.4.1.3.2Demodulation reference signal for PUCCH format 2107

6.4.1.3.2.1Sequence generation107

6.4.1.3.2.2Mapping to physical resources108

6.4.1.3.3Demodulation reference signal for PUCCH formats 3 and 4108

6.4.1.3.3.1Sequence generation108

6.4.1.3.3.2Mapping to physical resources108

6.4.1.4Sounding reference signal109

6.4.1.4.1SRS resource109

6.4.1.4.2Sequence generation109

6.4.1.4.3Mapping to physical resources111

6.4.1.4.4Sounding reference signal slot configuration117

7Downlink117

7.1Overview117

7.1.1Overview of physical channels117

7.1.2Overview of physical signals118

7.2Physical resources118

7.3Physical channels118

7.3.1Physical downlink shared channel118

7.3.1.1Scrambling118

7.3.1.2Modulation119

7.3.1.3Layer mapping120

7.3.1.4Antenna port mapping121

7.3.1.5Mapping to virtual resource blocks121

7.3.1.6Mapping from virtual to physical resource blocks121

7.3.2Physical downlink control channel (PDCCH)123

7.3.2.1Control-channel element (CCE)123

7.3.2.2Control-resource set (CORESET)123

7.3.2.3Scrambling125

7.3.2.4PDCCH modulation125

7.3.2.5Mapping to physical resources126

7.3.3Physical broadcast channel126

7.3.3.1Scrambling126

7.3.3.2Modulation126

7.3.3.3Mapping to physical resources126

7.4Physical signals126

7.4.1Reference signals126

7.4.1.1Demodulation reference signals for PDSCH126

7.4.1.1.1Sequence generation126

7.4.1.1.2Mapping to physical resources127

7.4.1.2Phase-tracking reference signals for PDSCH132

7.4.1.2.1Sequence generation132

7.4.1.2.2Mapping to physical resources132

7.4.1.3Demodulation reference signals for PDCCH133

7.4.1.3.1Sequence generation133

7.4.1.3.2Mapping to physical resources134

7.4.1.4Demodulation reference signals for PBCH134

7.4.1.4.1Sequence generation134

7.4.1.4.2Mapping to physical resources135

7.4.1.5CSI reference signals135

7.4.1.5.1General135

7.4.1.5.2Sequence generation135

7.4.1.5.3Mapping to physical resources135

7.4.1.6RIM reference signals139

7.4.1.6.1General139

7.4.1.6.2Sequence generation139

7.4.1.6.3Mapping to physical resources140

7.4.1.6.4RIM-RS configuration140

7.4.1.6.4.1General140

7.4.1.6.4.2Time-domain parameters and mapping from  to time-domain parameters140it

7.4.1.6.4.3Frequency-domain parameters and mapping from  to frequency-domain parameters141if

7.4.1.6.4.4Sequence parameters and mapping from  to sequence parameters142is

7.4.1.6.4.5Mapping between resource triplet and set ID142

7.4.1.7Positioning reference signals143

7.4.1.7.1General143

7.4.1.7.2Sequence generation143

7.4.1.7.3Mapping to physical resources in a downlink PRS resource143

7.4.1.7.4Mapping to slots in a downlink PRS resource set144

7.4.2Synchronization signals145

7.4.2.1Physical-layer cell identities145

7.4.2.2Primary synchronization signal145

7.4.2.2.1Sequence generation145

7.4.2.2.2Mapping to physical resources145

7.4.2.3Secondary synchronization signal145

7.4.2.3.1Sequence generation145

7.4.2.3.2Mapping to physical resources146

7.4.3SS/PBCH block146

7.4.3.1Time-frequency structure of an SS/PBCH block146

7.4.3.1.1Mapping of PSS within an SS/PBCH block147

7.4.3.1.2Mapping of SSS within an SS/PBCH block147

7.4.3.1.3Mapping of PBCH and DM-RS within an SS/PBCH block147

7.4.3.2Time location of an SS/PBCH block148

7.4.4Wake-up signal148

7.4.4.1Sequence generation148

7.4.4.1.1Generation of 148rZC,m(n)

7.4.4.1.2Generation of 149rWUS(n)

7.4.4.2Mapping to physical resources149

7.4.5Low-power synchronization signal149

7.4.5.1Sequence generation149

7.4.5.1.1Generation of 149rOOK(n)

7.4.5.1.2Generation of 150rZC(n)

7.4.5.1.3Generation of 150rLPSS(n)

7.4.5.2Mapping to physical resources150

8Sidelink151

8.1Overview151

8.1.1Overview of physical channels151

8.1.2Overview of physical signals151

8.2Physical resources151

8.2.1General151

8.2.2Numerologies151

8.2.3Frame structure152

8.2.3.1Frames and subframes152

8.2.3.2Slots152

8.2.4Antenna ports152

8.2.5Resource grid152

8.2.6Resource elements153

8.2.7Resource blocks153

8.2.8Bandwidth part153

8.3Physical channels153

8.3.1Physical sidelink shared channel153

8.3.1.1Scrambling153

8.3.1.2Modulation154

8.3.1.3Layer mapping154

8.3.1.4Precoding154

8.3.1.5Mapping to virtual resource blocks154

8.3.1.6Mapping from virtual to physical resource blocks155

8.3.2Physical sidelink control channel155

8.3.2.1Scrambling155

8.3.2.2Modulation155

8.3.2.3Mapping to physical resources155

8.3.3Physical sidelink broadcast channel155

8.3.3.1Scrambling155

8.3.3.2Modulation156

8.3.3.3Mapping to physical resources156

8.3.4Physical sidelink feedback channel156

8.3.4.1General156

8.3.4.2PSFCH format 0156

8.3.4.2.1Sequence generation156

8.3.4.2.2Mapping to physical resources156

8.4Physical signals157

8.4.1Reference signals157

8.4.1.1Demodulation reference signals for PSSCH157

8.4.1.1.1Sequence generation157

8.4.1.1.2Mapping to physical resources157

8.4.1.2Phase-tracking reference signals for PSSCH158

8.4.1.2.1Sequence generation158

8.4.1.2.2Mapping to physical resources158

8.4.1.3Demodulation reference signals for PSCCH159

8.4.1.3.1Sequence generation159

8.4.1.3.2Mapping to physical resources160

8.4.1.4Demodulation reference signals for PSBCH160

8.4.1.4.1Sequence generation160

8.4.1.4.2Mapping to physical resources160

8.4.1.5CSI reference signals161

8.4.1.5.1General161

8.4.1.5.2Sequence generation161

8.4.1.5.3Mapping to physical resources161

8.4.1.6Positioning reference signals161

8.4.1.6.1General161

8.4.1.6.2Sequence generation161

8.4.1.6.3Mapping to physical resources162

8.4.2Synchronization signals163

8.4.2.1Physical-layer sidelink synchronization identities163

8.4.2.2Sidelink primary synchronization signal163

8.4.2.2.1Sequence generation163

8.4.2.2.2Mapping to physical resources163

8.4.2.3Sidelink secondary synchronization signal163

8.4.2.3.1Sequence generation163

8.4.2.3.2Mapping to physical resources163

8.4.3S-SS/PSBCH block164

8.4.3.1Time-frequency structure of an S-SS/PSBCH block164

8.4.3.1.1Mapping of S-PSS within an S-SS/PSBCH block164

8.4.3.1.2Mapping of S-SSS within an S-SS/PSBCH block164

8.4.3.1.3Mapping of PSBCH and DM-RS within an S-SS/PSBCH block164

8.4.3.2Time location of an S-SS/PSBCH block165

8.5Timing165

Annex A (informative):Change history166

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

The present document describes the physical channels and signals for 5G-NR.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 38.201: "NR; Physical Layer – General Description"

[3]3GPP TS 38.202: "NR; Services provided by the physical layer"

[4]3GPP TS 38.212: "NR; Multiplexing and channel coding"

[5]3GPP TS 38.213: "NR; Physical layer procedures for control "

[6]3GPP TS 38.214: "NR; Physical layer procedures for data "

[7]3GPP TS 38.215: "NR; Physical layer measurements"

[8]3GPP TS 38.104: "NR; Base Station (BS) radio transmission and reception"

[9]void

[10]3GPP TS 38.306: "NR; User Equipment (UE) radio access capabilities"

[11]3GPP TS 38.321: "NR; Medium Access Control (MAC) protocol specification"

[12]3GPP TS 38.133: "NR; Requirements for support of radio resource management"

[13]3GPP TS 38.304: "NR; User Equipment (UE) procedures in Idle mode and RRC Inactive state"

[14]3GPP TS 38.101-1: "NR; User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone"

[15]3GPP TS 38.101-2: "NR; User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone"

[16]3GPP TS 38.101-5: "NR; User Equipment (UE) radio transmission and reception; Part 5: Satellite access Radio Frequency (RF) and performance requirements"

[17]3GPP TS 38.108: "Satellite Access Node radio transmission and reception"

## 3Definitions of terms, symbols and abbreviations

## 3.1Terms

For the purposes of the present document, the following definitions apply:

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

Resource element with frequency-domain index  and time-domain index  for antenna port  and subcarrier spacing configuration ; see clause 4.4.3pμ

Value of resource element  for antenna port and subcarrier spacing configuration ; see clause 4.4.3 pμ

Amplitude scaling for a physical channel/signal

PN sequence; see clause 5.2.1

Subcarrier spacing

Subcarrier spacing for random-access preambles

The ratio between  and ; see clause 4.1κ

Subcarrier index relative to a reference

OFDM symbol index relative to a reference

Subcarrier spacing configuration, μΔf=2μ∙15 [kHz]

Number of coded bits to transmit on a physical channel [for codeword ]Mbit(q)q

Number of modulation symbols to transmit on a physical channel [for codeword ]Msymb(q)q

Number of modulation symbols to transmit per layer for a physical channelMsymblayer

Scheduled bandwidth for uplink transmission, expressed as a number of subcarriers MscPUSCH

Scheduled bandwidth for uplink transmission, expressed as a number of resource blocksMRBPUSCH

Number of modulation symbols to transmit per antenna port for a physical channelMsymbap

Number of transmission layers

Size of bandwidth part ; see clause 4.4.4.4NBWP,isize

Start of bandwidth part ; see clause 4.4.4.4NBWP,istart

Cyclic prefix length; see clause 5.3.1NCP,lμ

The size of the resource grid; see clauses 4.4.2 and 5.3Ngrid,xsize,μ

The start of the resource grid; see clause 4.4.2Ngrid,xstart,μ

The number of PT-RS groups; see clause 6.3.1.4NgroupPT-RS

Physical layer cell identity; see clause 7.4.2.1NIDcell

Physical-layer sidelink identity; see clause 8.4.2.1NIDSL

Frequency-domain size of a control resource set; see clause 7.3.2.2NRBCORESET

Number of resource-element groups in a CORESET; see clause 7.3.2.2NREGCORESET

Number of samples per PT-RS group; see clause 6.3.1.4Nsampgroup

Number of subcarriers per resource block, see clause 4.4.4.1NscRB

Number of slots per subframe for subcarrier spacing configuration , see clause 4.3.2Nslotsubframe,μμ

Number of slots per frame for subcarrier spacing configuration , see clause 4.3.2Nslotframe,μμ

Time duration of a control resource set; see clause 7.3.2.2NsymbCORESET

Length of the PUCCH transmission in OFDM symbols; see clause 6.3.2.1NsymbPUCCH

Number of OFDM symbols per subframe for subcarrier spacing configuration ; see clause 4.3.1Nsymbsubframe,μμ

Number of symbols per slotNsymbslot

Timing advance between downlink and uplink; see clause 4.3.1NTA

A fixed offset used to calculate the timing advance; see clause 4.3.1NTA,offset

Network-controlled timing correction; see clause 4.3.1NTA,adjcommon

UE-derived timing correction; see clause 4.3.1NTA,adjUE

Minimum time from reception to transmission for a half-duplex UE; see clause 4.3.2NRx-Tx

System frame number (SFN)nf

Common resource block number for subcarrier spacing configuration , see clause 4.4.4.3nCRBμμ

Hyper-frame numbernHFN

Physical resource block number; see clause 4.4.4.4nPRB

Radio network temporary identifiernRNTI

Slot number within a subframe for subcarrier spacing configuration ; see clause 4.3.2nsμμ

Slot number within a frame for subcarrier spacing configuration ; see clause 4.3.2ns,fμμ

Antenna port numberp

Modulation order

Number of antenna ports

Low-PAPR base sequence; see clause 5.2.2ru,v(n)

Low-PAPR sequence; see clause 5.2.2ru,v(α,δ)(n)

The time-continuous signal on antenna port  and subcarrier spacing configuration  for OFDM symbol  in a subframe; see clause 5.3.1slp,μ(t)pμ

Basic time unit for NR; see clause 4.1

Radio frame duration; see clause 4.3.1

Basic time unit for LTE

Subframe duration; see clause 4.3.1

Slot duration; see clause 4.3.2

Timing advance between downlink and uplink; see clause 4.3.1

Precoding matrix for spatial multiplexing

## 3.3Abbreviations

For the purposes of the present document, the following abbreviations apply:

BWPBandwidth Part

CCEControl Channel Element

CORESETControl Resource Set

CRBCommon Resource Block

CSIChannel-State Information

CSI-RSCSI Reference Signal

DCIDownlink Control Information

DM-RSDemodulation Reference Signal

FR1Frequency Range 1 as defined in TS 38.104 [8]

FR2Frequency Range 2 as defined in TS 38.104 [8]

FR2-NTNFrequency Range 2 for Non-terrestrial networks as defined in TS 38.101-5 [16]

IABIntegrated Access and Backhaul

IAB-MTIAB Mobile Termination

IEInformation Element

NCRNetwork-Controlled repeater

NCR-MTNCR Mobile Termination

PBCHPhysical Broadcast Channel

PDCCHPhysical Downlink Control Channel

PDSCHPhysical Downlink Shared Channel

PRACHPhysical Random-Access Channel

PRBPhysical Resource Block

PSSPrimary Synchronization Signal

PT-RSPhase-tracking reference signal

PUCCHPhysical Uplink Control Channel

PUSCHPhysical Uplink Shared Channel

RARRandom Access Response

REGResource-Element Group

RIMRemote Interference Management

RIM-RSRemote Interference Management Reference Signal

SRSSounding Reference Signal

SSSSecondary Synchronization Signal

VRBVirtual Resource Block

## 4Frame structure and physical resources

## 4.1General

Throughout this specification, unless otherwise noted, the size of various fields in the time domain is expressed in time units  where  Hz and . The constant  where ,  and .Δfmax=480∙103

Throughout this specification, unless otherwise noted, statements using the term "UE" in clauses 4, 5, 6, or 7 are equally applicable to the IAB-MT part of an IAB-node and the NCR-MT part of an NCR node.

## 4.2Numerologies

Multiple OFDM numerologies are supported as given by Table 4.2-1 where  and the cyclic prefix for a downlink or uplink bandwidth part are obtained from the higher-layer parameters subcarrierSpacing and cyclicPrefix, respectively. μ

Table 4.2-1: Supported transmission numerologies.

## 4.3Frame structure

## 4.3.1Frames and subframes

Downlink, uplink, and sidelink transmissions are organized into frames with  duration, each consisting of ten subframes of  duration. The number of consecutive OFDM symbols per subframe is . Each frame is divided into two equally-sized half-frames of five subframes each with half-frame 0 consisting of subframes 0 – 4 and half-frame 1 consisting of subframes 5 – 9.Nsymbsubframe,μ=NsymbslotNslotsubframe,μ

There is one set of frames in the uplink and one set of frames in the downlink on a carrier.

Uplink frame number  for transmission from the UE shall start  before the start of the corresponding downlink frame at the UE whereTTA=NTA+NTA,offset+NTA,adjcommon+NTA,adjUETc

-  and  are given by clause 4.2 of [5, TS 38.213], except for msgA transmission on PUSCH where  shall be used;NTANTA,offsetNTA=0

- given by clause 4.2 of [5, TS 38.213] is derived from the higher-layer parameters ta-Common, ta-CommonDrift, and ta-CommonDriftVariant if configured, otherwise ;NTA,adjcommonNTA,adjcommon=0

- given by clause 4.2 of [5, TS 38.213] is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters if configured, or is computed by the UE based on UE position and gNB location provided by atg-gNB-Location if configured, otherwise .NTA,adjUENTA,adjUE=0

Figure 4.3.1-1: Uplink-downlink timing relation.

## 4.3.2Slots

For subcarrier spacing configuration , slots are numbered  in increasing order within a subframe and  in increasing order within a frame. There are  consecutive OFDM symbols in a slot where  depends on the cyclic prefix as given by Tables 4.3.2-1 and 4.3.2-2. The start of slot  in a subframe is aligned in time with the start of OFDM symbol  in the same subframe.nsμ∈0, …,Nslotsubframe,μ-1 ns,fμ∈0, …,Nslotframe,μ-1 nsμ

OFDM symbols in a slot in a downlink or uplink frame can be classified as 'downlink', 'flexible', or 'uplink'. Signaling of slot formats is described in clause 11.1 of [5, TS 38.213].

In a slot in a downlink frame, the UE shall assume that downlink transmissions only occur in 'downlink' or 'flexible' symbols.

In a slot in an uplink frame, the UE shall only transmit in 'uplink' or 'flexible' symbols.

A UE not capable of full-duplex communication and not supporting simultaneous transmission and reception as defined by parameter simultaneousRxTxInterBandENDC, simultaneousRxTxInterBandCA or simultaneousRxTxSUL [10, TS 38.306] among all cells within a group of cells is not expected to transmit in the uplink in one cell within the group of cells earlier than  after the end of the last received downlink symbol in the same or different cell within the group of cells where  is given by Table 4.3.2-3. NRx-TxTcNRx-Tx

A UE not capable of full-duplex communication and not supporting simultaneous transmission and reception as defined by parameter simultaneousRxTxInterBandENDC, simultaneousRxTxInterBandCA or simultaneousRxTxSUL [10, TS 38.306] among all cells within a group of cells is not expected to receive in the downlink in one cell within the group of cells earlier than  after the end of the last transmitted uplink symbol in the same or different cell within the group of cells where  is given by Table 4.3.2-3. NTx-RxTcNTx-Rx

For DAPS handover operation, a UE not capable of full-duplex communication is not expected to transmit in the uplink to a cell earlier than  after the end of the last received downlink symbol in the different cell where  is given by Table 4.3.2-3. NRx-TxTcNRx-Tx

For DAPS handover operation, a UE not capable of full-duplex communication is not expected to receive in the downlink from a cell earlier than  after the end of the last transmitted uplink symbol in the different cell where  is given by Table 4.3.2-3.NTx-RxTcNTx-Rx

A UE not capable of full-duplex communication is not expected to transmit in the uplink earlier than  after the end of the last received downlink symbol in the same cell where  is given by Table 4.3.2-3. NRx-TxTcNRx-Tx

A UE not capable of full-duplex communication is not expected to receive in the downlink earlier than  after the end of the last transmitted uplink symbol in the same cell where  is given by Table 4.3.2-3.NTx-RxTcNTx-Rx

Table 4.3.2-1: Number of OFDM symbols per slot, slots per frame, and slots per subframe for normal cyclic prefix.

Table 4.3.2-2: Number of OFDM symbols per slot, slots per frame, and slots per subframe for extended cyclic prefix.

Table 4.3.2-3: Transition time  and NRx-TxNTx-Rx

## 4.4Physical resources

## 4.4.1Antenna ports

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed.

Two antenna ports are said to be quasi co-located if the large-scale properties of the channel over which a symbol on one antenna port is conveyed can be inferred from the channel over which a symbol on the other antenna port is conveyed. The large-scale properties include one or more of delay spread, Doppler spread, Doppler shift, average gain, average delay, and spatial Rx parameters.

## 4.4.2Resource grid

For each numerology and carrier, a resource grid of  subcarriers and  OFDM symbols is defined, starting at common resource block  indicated by higher-layer signalling. There is one set of resource grids per transmission direction (uplink, downlink, or sidelink) with the subscript set to DL, UL, and SL for downlink, uplink, and sidelink, respectively. When there is no risk for confusion, the subscript  may be dropped. There is one resource grid for a given antenna port , subcarrier spacing configuration , and transmission direction (downlink, uplink, or sidelink). Nsymbsubframe,μ xxpμ

For uplink and downlink, the carrier bandwidth  for subcarrier spacing configuration  is given by the higher-layer parameter carrierBandwidth in the SCS-SpecificCarrier IE, or by the higher-layer parameter carrierBandwidth in OD-SIB1-Config IE if the PRACH transmission is for SIB1 request. The starting position  for subcarrier spacing configuration  is given by the higher-layer parameter offsetToCarrier in the SCS-SpecificCarrier IE, or by the higher-layer parameter offsetToCarrier in OD-SIB1-Config IE if the PRACH transmission is for SIB1 request.Ngridsize,μμNgridstart,μμ

The frequency location of a subcarrier refers to the center frequency of that subcarrier.

For the downlink, the higher-layer parameter txDirectCurrentLocation in the SCS-SpecificCarrier IE indicates the location of the transmitter DC subcarrier in the downlink for each of the numerologies configured in the downlink. Values in the range 0 – 3299 represent the number of the DC subcarrier and the value 3300 indicates that the DC subcarrier is located outside the resource grid.

For the uplink, the higher-layer parameter txDirectCurrentLocation in the UplinkTxDirectCurrentBWP IE indicates the location of the transmitter DC subcarrier in the uplink for each of the configured bandwidth parts, including whether the DC subcarrier location is offset by 7.5 kHz relative to the center of the indicated subcarrier or not. Values in the range 0 – 3299 represent the number of the DC subcarrier, the value 3300 indicates that the DC subcarrier is located outside the resource grid, and the value 3301 indicates that the position of the DC subcarrier in the uplink is undetermined.

## 4.4.3Resource elements

Each element in the resource grid for antenna port  and subcarrier spacing configuration  is called a resource element and is uniquely identified by  where  is the index in the frequency domain and  refers to the symbol position in the time domain relative to some reference point. Resource element  corresponds to a physical resource and the complex value . When there is no risk for confusion, or no particular antenna port or subcarrier spacing is specified, the indices  and  may be dropped, resulting in  or .pμ(k,l)p,μ(k,l)p,μak,l(p,μ)pμak,l(p)ak,l

## 4.4.4Resource blocks

## 4.4.4.1General

A resource block is defined as  consecutive subcarriers in the frequency domain. NscRB=12

## 4.4.4.2Point A

Point A serves as a common reference point for resource block grids and is obtained from:

-offsetToPointA for a PCell downlink where offsetToPointA represents the frequency offset between point A and the lowest subcarrier of the lowest resource block, which overlaps with the SS/PBCH block, or the SS/PBCH block after puncturing if applicable, used by the UE for initial cell selection, expressed in units of resource blocks assuming 15 kHz subcarrier spacing for FR1 and 60 kHz subcarrier spacing for FR2 and FR2-NTN;

-for operation without shared spectrum channel access in FR1, FR2-1 and FR2-NTN, the lowest resource block has the subcarrier spacing provided by the higher-layer parameter subCarrierSpacingCommon;

-for operation with shared spectrum channel access in FR1 or FR2, and for operation without shared spectrum channel access in FR2-2, the lowest resource block has the subcarrier spacing same as the SS/PBCH block used by the UE for initial cell selection;

-absoluteFrequencyPointA for all other cases where absoluteFrequencyPointA represents the frequency-location of point A expressed as in ARFCN.

## 4.4.4.3Common resource blocks

Common resource blocks are numbered from 0 and upwards in the frequency domain for subcarrier spacing configuration . The center of subcarrier 0 of common resource block 0 for subcarrier spacing configuration  coincides with 'point A'. μμ

The relation between the common resource block number  in the frequency domain and resource elements  for subcarrier spacing configuration  is given bynCRBμμ

where  is defined relative to point A such that  corresponds to the subcarrier centered around point A.k=0

## 4.4.4.4Physical resource blocks

Physical resource blocks for subcarrier spacing configuration  are defined within a bandwidth part and numbered from 0 to  where  is the number of the bandwidth part. The relation between the physical resource block  in bandwidth part  and the common resource block  is given byμNBWP,isize,μ-1inPRBμinCRBμ

nCRBμ=nPRBμ+NBWP,istart,μ

where  is the common resource block where bandwidth part  starts relative to common resource block 0. When there is no risk for confusion the index  may be dropped.NBWP,istart,μiμ

## 4.4.4.5Virtual resource blocks

Virtual resource blocks are defined within a bandwidth part and numbered from 0 to  where  is the number of the bandwidth part. NBWP,isize-1i

## 4.4.4.6Interlaced resource blocks

Multiple interlaces of resource blocks are defined where interlace  consists of common resource blocks , with  being the number of interlaces given by Table 4.4.4.6-1. The relation between the interlaced resource block  in bandwidth part  and interlace  and the common resource block  is given bym∈0,1,…,M-1m,M+m, 2M+m, 3M+m, …MnIRB,mμ∈0,1,…imnCRBμ

nCRBμ=MnIRB,mμ+NBWP,istart,μ+m-NBWP,istart,μ mod M

where  is the common resource block where bandwidth part starts relative to common resource block 0. When there is no risk for confusion the index  may be dropped. NBWP,istart,μμ

The UE expects that the number of common resource blocks in an interlace contained within bandwidth part  is no less than 10.i

Table 4.4.4.6-1: The number of resource block interlaces.

## 4.4.5Bandwidth part

A bandwidth part is a subset of contiguous common resource blocks defined in clause 4.4.4.3 for a given numerology  in bandwidth part  on a given carrier. The starting position  and the number of resource blocks  in a bandwidth part shall fulfil  and , respectively. Configuration of a bandwidth part is described in clause 12 of [5, TS 38.213].NBWP,istart,μNBWP,isize,μNgrid,xstart,μ≤NBWP,istart,μ<Ngrid,xstart,μ+Ngrid,xsize,μNgrid,xstart,μ<NBWP,istart,μ+NBWP,isize,μ≤Ngrid,xstart,μ+Ngrid,xsize,μ

A UE can be configured with up to four bandwidth parts in the downlink with a single downlink bandwidth part being active at a given time. The UE is not expected to receive PDSCH, PDCCH, or CSI-RS (except for RRM) outside an active bandwidth part.

A UE can be configured with up to four bandwidth parts in the uplink with a single uplink bandwidth part being active at a given time. If a UE is configured with a supplementary uplink, the UE can in addition be configured with up to four bandwidth parts in the supplementary uplink with a single supplementary uplink bandwidth part being active at a given time. The UE shall not transmit PUSCH or PUCCH outside an active bandwidth part. For an active cell, the UE shall not transmit SRS configured by SRS-Resource outside an active bandwidth part.

Unless otherwise noted, the description in this specification applies to each of the bandwidth parts. When there is no risk of confusion, the index  may be dropped from , , , and .μNBWP,istart,μNBWP,isize,μNgrid,xstart,μNgrid,xsize,μ

## 4.4.6Common MBS frequency resource

A common MBS frequency resource is a contiguous set of common resource blocks. The starting position  of the common MBS frequency resource  is defined relative to point A and the size of the common MBS frequency resource is given by . Resource blocks in a common MBS frequency resource are numbered in the same way as resource blocks in clause 4.4.4.4 with  and  replaced by  and , respectively.NMBS,istart,μiNMBS,isize,μNBWP,istart,μNBWP,isize,μNMBS,istart,μNMBS,isize,μ

A UE is not expected to receive PDSCH or PDCCH associated with MBS transmissions scheduled with G-RNTI, G-CS-RNTI, MCCH-RNTI, or Multicast-MCCH-RNTI outside the common MBS frequency resource.

## 4.5Carrier aggregation

Transmissions in multiple cells can be aggregated. Unless otherwise noted, the description in this specification applies to each of the serving cells.

For carrier aggregation of cells with unaligned frame boundaries, the slot offset  between a PCell/PScell and an SCell is determined by higher-layer parameter ca-SlotOffset for the SCell. The quantity  is defined as the maximum of the lowest subcarrier spacing configuration among the subcarrier spacings given by the higher-layer parameters scs-SpecificCarrierList configured for PCell/PSCell and the SCell, respectively. The slot offset  fulfillsNslot, offsetCAμoffsetNslot, offsetCA

-when the lowest subcarrier spacing configuration among the subcarrier spacings configured for the cell is  for both cells or  for both cells, the start of slot 0 for the cell whose point A has a lower frequency coincides with the start of slot  for the other cell where   if point A of the PCell/PSCell has a frequency lower than the frequency of point A for the SCell, otherwise ;μ=2μ=3qNslot, offsetCA mod Nslotframe,μoffsetq=-1q=1

-otherwise, the start of slot 0 for the cell with the lower subcarrier spacing of the lowest subcarrier spacing given by the higher-layer parameters scs-SpecificCarrierList configured for the two cells, or the Pcell/PSCell if both cells have the same lowest subcarrier spacing given by the higher-layer parameters scs-SpecificCarrierList configured for the two cells, coincides with the start of slot  for the other cell where   if the lowest subcarreier spacing configuration given by scs-SpecificCarrierList of the PCell/PSCell is smaller than or equal to the lowest subcarrier spacing given by scs-SpecificCarrierList for the SCell, otherwise .qNslot, offsetCA mod Nslotframe,μoffsetq=-1q=1

## 5Generic functions

## 5.1Modulation mapper

The modulation mapper takes binary digits, 0 or 1, as input and produces complex-valued modulation symbols as output.

## 5.1.1π/2-BPSK

In case of π/2-BPSK modulation, bit  is mapped to complex-valued modulation symbol  according to

## 5.1.2BPSK

In case of BPSK modulation, bit  is mapped to complex-valued modulation symbol  according to

## 5.1.3QPSK

In case of QPSK modulation, pairs of bits, , are mapped to complex-valued modulation symbols  according to

## 5.1.416QAM

In case of 16QAM modulation, quadruplets of bits, , are mapped to complex-valued modulation symbols  according to

## 5.1.564QAM

In case of 64QAM modulation, hextuplets of bits, , are mapped to complex-valued modulation symbols  according to

## 5.1.6256QAM

In case of 256QAM modulation, octuplets of bits, , are mapped to complex-valued modulation symbols  according to

## 5.1.71024QAM

In case of 1024QAM modulation, 10-tuplets of bits, , are mapped to complex-valued modulation symbols  according tob10i, b10i+1, b10i+2, b10i+3, b10i+4, b10i+5, b10i+6, b10i+7, b10i+8, b10i+9d(i)

di=16821-2b10i+016-1-2b10i+28-1-2b10i+44-1-2b10i+62-1-2b10i+8+j16821-2b10i+116-1-2b10i+38-1-2b10i+54-1-2b10i+72-1-2b10i+9

## 5.2Sequence generation

## 5.2.1Pseudo-random sequence generation

Generic pseudo-random sequences are defined by a length-31 Gold sequence. The output sequence  of length, where, is defined by

where  and the first m-sequence  shall be initialized with. The initialization of the second m-sequence, , is denoted by  with the value depending on the application of the sequence.NC=1600

## 5.2.2Low-PAPR sequence generation type 1

The low-PAPR sequence  is defined by a cyclic shift  of a base sequence  according to

where  is the length of the sequence. Multiple sequences are defined from a single base sequence through different values of  and . MZC=mNscRB2δαδ

Base sequences  are divided into groups, where  is the group number and  is the base sequence number within the group, such that each group contains one base sequence () of each length ,  and two base sequences () of each length , . The definition of the base sequence  depends on the sequence length .v=0MZC=mNscRB2δv=0,1MZC=mNscRB2δ

## 5.2.2.1Base sequences of length 36 or larger

For, the base sequence  is given byMZC≥3NscRB

where

The length  is given by the largest prime number such that.

## 5.2.2.2Base sequences of length less than 36

For  the base sequence is given by

where the value of  is given by Tables 5.2.2.2-1 to 5.2.2.2-4.

For , the base sequence  is given by

Table 5.2.2.2-1: Definition of  for.

Table 5.2.2.2-2: Definition of  for.

Table 5.2.2.2-3: Definition of  for

Table 5.2.2.2-4: Definition of  for

## 5.2.3Low-PAPR sequence generation type 2

The low-PAPR sequence  is defined by a base sequence  according to ru,v(α,δ)nru,vn

ru,v(α,δ)n=ru,vn,          0≤n<M

where  is the length of the sequence. M=mNscRB2δ

Base sequences  are divided into groups, where  is the group number and  is the base sequence number within the group, such that each group contains one base sequence () of length , . The sequence  is defined byru,vnu∈0,1,…,29vv=0M=mNscRB2δ12≤m2δru,v0,…,ru,vM-1

ru,vn=1Mi=0M-1ru,vie-j2πinMn=0,…,M-1

where the definition of  depends on the sequence length.ru,vi

## 5.2.3.1Sequences of length 30 or larger

For , the sequence  is obtained as the complex-valued modulations symbols resulting from π/2-BPSK modulation as defined in clause 5.1.1 applied to the binary sequence  given by clause 5.2.1, initialized with .M≥30ru,vicicinit

## 5.2.3.2Sequences of length less than 30

For , the sequence   is given byM=6ru,vi

ru,vi=ejφiπ8, 0≤i≤M-1

where the value of  is given by Table 5.2.3.2-1. φi

For , the sequence  is obtained as the complex-valued modulations symbols resulting from π/2-BPSK modulation as defined in clause 5.1.1 applied to the binary sequence  given by Tables 5.2.3.2-2 to 5.2.3.2-4.M∈12, 18, 24ru,vibi

Table 5.2.3.2-1: Definition of  for .φiM=6

Table 5.2.3.2-2: Definition of  for . biM=12

Table 5.2.3.2-3: Definition of  for .biM=18

Table 5.2.3.2-4: Definition of  for  biM=24

## 5.3OFDM baseband signal generation

## 5.3.1OFDM baseband signal generation for all channels except PRACH and RIM-RS

The time-continuous signal  on antenna port  and subcarrier spacing configuration  for OFDM symbol  in a subframe for any physical channel or signal except PRACH is defined bypμ

sl(p,μ)t=sl(p,μ)ttstart,lμ≤t<tstart,lμ+Tsymb,lμ0otherwisesl(p,μ)t=k=0Ngrid,xsize,μNscRB-1ak,l(p,μ)ej2πk+k0μ-Ngrid,xsize,μNscRB2Δft-NCP,lμTc-tstart,lμk0μ=Ngrid,xstart,μ+Ngrid,xsize,μ2NscRB-Ngrid,xstart,μ0+Ngrid,xsize,μ02NscRB2μ0-μTsymb,lμ=Nuμ+NCP,lμTc

where  at the start of the subframe, t=0

and

- is given by clause 4.2;

- is the subcarrier spacing configuration;

- is the largest  value among the subcarrier spacing configurations by scs-SpecificCarrierList for each of uplink and downlink and by sl-SCS-SpecificCarrierList for sidelink.μ0μ

The starting position of OFDM symbol  for subcarrier spacing configuration  in a subframe is given bylμ

tstart,lμ=0l=0tstart,l-1μ+Tsymb,l-1μotherwise

In case of cyclic prefix extension of the first OFDM symbol  allocated for PUSCH, SRS, PUCCH, PSCCH/PSSCH, PSFCH, or S-SS/PSBCH block transmission, the time-continuous signal  for the interval  preceding the first OFDM symbol for PUSCH, SRS, PUCCH, PSCCH/PSSCH, PSFCH, or S-SS/PSBCH block is given bylsext(p,μ)ttstart,lμ-Text≤t<tstart,lμ

sext(p,μ)t=sl(p,μ)t

where  refers to the signal in the previous subframe and t<0

-for dynamically scheduled PUSCH, SRS, and PUCCH transmissions

Text=minmaxText',0, Tsymb,(l-1)mod7∙2μμ

Text'=k=1CiTsymb,  l-kmod 7∙2μ μ-Δi

where  is given by Table 5.3.1-1 with  for ,  for , and  and  given by the higher-layer parameters cp-ExtensionC2 and cp-ExtensionC3, respectively, and  given by clause 4.3.1. For contention-based random access, or in absence of higher-layer configuration of  and , the value of shall be set to the largest integer fulfilling  for each of the values of . Text is applied to the first UL transmission scheduled by the scheduling DCI.ΔiC1=1μ∈0,1C1=2μ=2C2C3TTAC2C3CiText'<Tsymb,  (l-1)mod7∙2μ μi∈2,3

-for a PUSCH transmission using configured grant

Text=k=12μTsymb,  l-kmod 7∙2μ μ-Δi

where   is given by Table 5.3.1-2 with the index  given by the procedure in [6, TS 38.214].Δii

-for PSCCH/PSSCH, PSFCH, and S-SS/PSBCH block transmission

Text=maxk=1CiTsymb,  l-kmod 7∙2μ μ-Δi, 0

where   and  are given by Table 5.3.1-3 with the index  given by the procedure in [5, TS 38.213] or [6, TS 38.214].ΔiCii

Table 5.3.1-1: The variables  and  for uplink cyclic prefix extension CiΔi

Table 5.3.1-2: The variable  for uplink cyclic prefix extension with configured grants.Δi

Table 5.3.1-3: The variables  and  for sidelink cyclic prefix extension CiΔi

## 5.3.2OFDM baseband signal generation for PRACH

The time-continuous signal  on antenna port  for PRACH is defined bysl(p,μ)tp

sl(p,μ)t=k=0LRA-1ak(p,RA)ej2πk+Kk1+kΔfRAt-NCP,lRATc-tstartRAK=ΔfΔfRAk1=k0μ+NBWP,istart-Ngridstart,μNscRB-Ngridsize,μNscRB2+nRAstartNscRB+nRANRBRANscRBif LRA∈139, 839nRANRBRANscRBif LRA∈571, 1151 in FR2-2NRB,UL,n0+nRAstart,μ-NRB,UL,n0start,μNscRBif LRA∈571, 1151 in FR1k0μ=Ngridstart,μ+Ngridsize,μ2NscRB-Ngridstart,μ0+Ngridsize,μ02NscRB2μ0-μ

where  and

- is given by clause 6.3.3;

- is the subcarrier spacing of the initial uplink bandwidth part during initial access. If the PRACH transmission is for a candidate cell,  is provided by subcarrierSpacing in bwp-GenericParameters in EarlyUL-SyncConfig. If the PRACH transmission is for SIB1 request,  is provided by ul-SubCarrierSpacing in OD-SIB1-Config. Otherwise,  is the subcarrier spacing of the active uplink bandwidth part;ΔfΔfΔf

- is the  value provided by ul-SubCarrierSpacing in OD-SIB1-Config, if the PRACH transmission is for SIB1 request. Otherwise,  is the largest  value among the subcarrier spacing configurations by the higher-layer parameter scs-SpecificCarrierList;μ0μμ0μ

- is the lowest numbered resource block of the initial uplink bandwidth part and is derived by the higher-layer parameter initialUplinkBWP or initialUplinkBWP-RedCap during initial access and from the higher-layer parameters bwp-GenericParameters in EarlyUL-SyncConfig if the PRACH transmission is for a candidate cell and from the higher-layer parameters locationAndBandwidth in SIB1-RequestConfig, if the PRACH transmission is for SIB1 request. Otherwise,  is the lowest numbered resource block of the active uplink bandwidth part and is derived by the higher-layer parameter BWP-Uplink; NBWP,istartNBWP,istart

- is the frequency offset of the lowest PRACH transmission occasion in frequency domain relative to physical resource block 0 of the active uplink bandwidth part and is given by nRAstart

-the higher-layer parameter msgA-RO-FrequencyStart if configured and a type-2 random-access procedure is initiated as described in clause 8.1 of [5, TS 38.213];

-if the higher-layer parameter sbfd-RACH-SingleConfig is configured, for PRACH transmission in second PRACH occasions in SBFD symbols, the quantity  is given  by the sum of msg1-FrequencyStart and the index of the first resource block from the resource blocks that are both in the active uplink bandwidth part and in the uplink sub-band; nRAstart

-otherwise, the quantity  is given by msg1-FrequencyStart as described in clause 8.1 of [5 TS 38.213].nRAstart

- is the PRACH transmission occasion index in frequency domain for a given PRACH transmission occasion in one time instance as given by clause 6.3.3.2;

- is the number of resource blocks occupied and is given by the parameter allocation expressed in number of RBs for PUSCH in Table 6.3.3.2-1.

- is the start CRB index of uplink RB set  corresponding to the quantity . The UE assumes that the RB set is defined as when the UE is not provided IntraCellGuardBandsPerSCS for an UL carrier as described in Clause 7 of [6, TS 38.214]NRB,UL,nstart,μnRBn,ULstart,μ

- is the index of the RB set which contains the lowest PRACH transmission occasion in frequency domain indicated by . The UE may assume that  is configured such that each PRACH transmission occasion is fully contained within an RB set.n0nRAstartnRAstart

- and  are given by clause 6.3.3

- where NCP,lRA=NCPRA+n∙16κ

-for ,  n=0

-for kHz,  is the number of times the interval  overlaps with either time instance 0 or time instance  in a subframeΔfRA∈15,30,60,120,480,960ntstartRA,tstartRA+NuRA+NCPRATc

The starting position  of the PRACH preamble in a subframe (for ) or in a 60 kHz slot (for kHz) is given bytstartRAΔfRA∈60,120,480,960

where

-the subframe or 60 kHz slot is assumed to start at ;t=0

-a timing advance value  shall be assumed; NTA=0

- and  are given by clause 5.3.1;NuμNCP,l-1μ

- shall be assumed for  kHz, otherwise the value of  corresponds to  kHz and the symbol position  is given by∆fRA∈1.25, 5μ∆fRA∈15, 30, 60, 120, 480, 960

l=l0+ntRANdurRA+14nslotRA

where

- is given by the parameter "starting symbol" in Tables 6.3.3.2-2 to 6.3.3.2-4;

- is the PRACH transmission occasion within the PRACH slot, numbered in increasing order from 0 to  within a RACH slot where  is given Tables 6.3.3.2-2 to 6.3.3.2-4 for  and fixed to 1 for ;LRA∈139,571,1151

- is given by Tables 6.3.3.2-2 to 6.3.3.2-4;

- is given by

-if  kHz, then ∆fRA∈1.25, 5, 15, 60

-if  kHz and either of "Number of PRACH slots within a subframe" in Tables 6.3.3.2-2 to 6.3.3.2-3 or "Number of PRACH slots within a 60 kHz slot" in Table 6.3.3.2-4 is equal to 1, then , otherwise ∆fRA∈30, 120nslotRA=1nslotRA∈0,1

-if  kHz and ∆fRA∈480, 960

-the "Number of PRACH slots within a 60 kHz slot" in Table 6.3.3.2-4 is equal to 1, then  for  kHz and  for kHz, ornslotRA=7∆fRA=480nslotRA=15∆fRA=960

-the "Number of PRACH slots within a 60 kHz slot" in Table 6.3.3.2-4 is equal to 2, then  for kHz and  for kHz.nslotRA∈3,7∆fRA=480 nslotRA∈7,15∆fRA=960

If the preamble format given by Tables 6.3.3.2-2 to 6.3.3.2-4 is A1/B1, A2/B2 or A3/B3, then

-if , then the PRACH preamble with the corresponding PRACH preamble format from B1, B2 and B3 is transmitted in the PRACH transmission occasion;ntRA=NtRA,slot-1

-otherwise the PRACH preamble with the corresponding PRACH preamble format from A1, A2 and A3 is transmitted in the PRACH transmission occasion

## 5.3.3OFDM baseband signal generation for RIM-RS

The time-continuous signal  on antenna port  for RIM-RS is defined bysl(p,μ)tp

sl(p,μ)t=k=0LRIM-1ak(p,RIM)ej2πk+k1ΔfRIMt-NCPRIMTc-tstart,l0μ

where

tstart,l0RIM≤t<tstart,l0RIM+NuRIM+NCPRIMTc

NuRIM=2⋅2048κ⋅2-μ

NCPRIM=NCP,l0RIM+NCP,lRIM

l=0if l0=Nsymbslot-1l0+1otherwise

and

- where  is the subcarrier spacing configuration for the RIM-RS; ΔfRIM=15⋅2μ kHzμ∈0,1

- is the starting frequency offset of the RIM-RS as given by clause 7.4.1.6.4.3;k1

- is the length of the RIM-RS sequence where  is the bandwidth of the RIM-RS in resource blocks;LRIM=12NRBRIMNRBRIM

- is the starting symbol given by clause 7.4.1.6.3;l0

- is given by clause 5.3.1 with ;tstart,l0RIM=tstart,lμl=l0

- is given by clause 5.3.1 with .NCP,l0RIM=NCP,lμl=l0

## 5.4Modulation and upconversion

Modulation and upconversion to the carrier frequency  of the complex-valued OFDM baseband signal for antenna port , subcarrier spacing configuration , and OFDM symbol  in a subframe assumed to start at  is given by pμ

-for PRACH

Resl(p,μ)tej2πf0t

-for RIM-RS

Resl(p,μ)tej2πf0RIMt-tstart,l0μ-NCPRIMTc

where  is the configured reference point for RIM-RS;f0RIM

-for all other channels and signals

NOTE:For the uplink, the signal  and the baseband signals part thereof should be filtered per UE implementation, as required, to meet the minimum requirements as specified in [14, 38.101-1], [15, 38.101-2], and [16, 38.101-5] for the respective frequency range. sl(p,μ)t

## 6Uplink

## 6.1Overview

## 6.1.1Overview of physical channels

An uplink physical channel corresponds to a set of resource elements carrying information originating from higher layers. The following uplink physical channels are defined:

-Physical Uplink Shared Channel, PUSCH

-Physical Uplink Control Channel, PUCCH

-Physical Random Access Channel, PRACH

## 6.1.2Overview of physical signals

An uplink physical signal is used by the physical layer but does not carry information originating from higher layers. The following uplink physical signals are defined:

-Demodulation reference signals, DM-RS

-Phase-tracking reference signals, PT-RS

-Sounding reference signal, SRS

## 6.2Physical resources

The frame structure and physical resources the UE shall use when transmitting in the uplink transmissions are defined in Clause 4.

The following antenna ports are defined for the uplink:

-Antenna ports starting with 0 for demodulation reference signals for PUSCH

-Antenna ports starting with 1000 for SRS, PUSCH

-Antenna ports starting with 2000 for PUCCH

-Antenna port 4000 for PRACH

If PUSCH repetition Type B as described in clause 6.1 of [6, TS38.214] is applied to a physical channel, the UE transmission shall be such that the channel over which a symbol on the antenna port used for uplink transmission is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed if the two symbols correspond to the same actual repetition of a PUSCH transmission with repetition Type B.

If intra-slot frequency hopping is not enabled for a physical channel and PUSCH repetition Type B is not applied to the physical channel, the UE transmission shall be such that the channel over which a symbol on the antenna port used for uplink transmission is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed if the two symbols correspond to the same slot.

If intra-slot frequency hopping is enabled for a physical channel, the UE transmission shall be such that the channel over which a symbol on the antenna port used for uplink transmission is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols correspond to the same frequency hop, regardless of whether the frequency hop distance is zero or not.

If DM-RS bundling is applied to PUSCH and/or PUCCH repetitions and/or transport-block processing over multiple slots as described in clause 6.1.7 of [6, 38.214], the UE transmission shall be such that the channel over which a symbol on the antenna port used for uplink transmission is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed if the two symbols are transmitted within the same actual time-domain window.

If inter-slot OCC is applied to PUSCH as described in clause 6.1.2.1 of [6, 38.214], the UE transmission shall be such that the channel over which a symbol on the antenna port used for uplink transmission is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed if the two symbols are transmitted on slots within the same orthogonal cover code and the conditions listed in clause 6.4.2.3 of [16, 38.101-5] are fulfilled.

## 6.2.1Muting resource

A muting resource corresponds to a set of resource elements, defined by OFDM symbols in the time domain and a comb-2 in the frequency domain. The position in the slot of the up to two OFDM symbols, and the comb offset relative to the lowest indexed resource element of the PUSCH allocation, are given by the higher-layer parameters symbolPos and combOffset, respectively, in the PUSCH-MutingResources information element.

The UE is not expected to be configured with a muting resource within which resource elements overlap in time and frequency with a resource element used for PUSCH PT-RS when transform precoding is not enabled.

The UE shall ignore any resource elements of a muting resource that overlaps in time with an OFDM symbol used for any of

-PUSCH DM-RS

-PT-RS when transform precoding is enabled

## 6.3Physical channels

## 6.3.1Physical uplink shared channel

## 6.3.1.1Scrambling

Up to two codewords  can be transmitted. In case of single-codeword transmission, .q∈0,1q=0

For each codeword, the block of bits , where  is the number of bits in codeword  transmitted on the physical channel, shall be scrambled prior to modulation, resulting in a block of scrambled bits  according to the following pseudo codebq0,…,bqMbit(q)-1Mbitqqbq0,…,bqMbit(q)-1

Set i = 0

while i<Mbitq

if // UCI placeholder bitsbqi=x

=1bqi

else

if // UCI placeholder bitsbqi=y

= bqibqi-1

else

= ( +bqibqicqi)mod2

end if

end if

i = i + 1

end while

where x and y are tags defined in [4, TS 38.212] and where the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with cq(i)

cinit=nRNTI∙216+nRAPID∙210+nIDfor msgA on PUSCHnRNTI∙215+q∙214+nIDotherwise

where

- equals the higher-layer parameter dataScramblingIdentityPUSCH if configured and the RNTI equals the C-RNTI, MCS-C-RNTI, SP-CSI-RNTI or CS-RNTI, and the transmission is not scheduled using DCI format 0_0 in a common search space;nID∈0,1,…,1023

- equals the higher-layer parameter msgA-DataScramblingIndex if configured and the PUSCH transmission is triggered by a Type-2 random access procedure as described in clause 8.1A of [5, TS 38.213];nID∈0,1,…,1023

- otherwisenID=NIDcell

- is the index of the random-access preamble transmitted for msgA as described in clause 5.1.3A of [11, TS 38.321]nRAPID

and where  equals the RA-RNTI for msgA and otherwise corresponds to the RNTI associated with the PUSCH transmission as described in clause 6.1 of [6, TS 38.214] and clause 8.3 of [5, TS 38.213].

## 6.3.1.2Modulation

For each codeword , the block of scrambled bits  shall be modulated as described in clause 5.1 using one of the modulation schemes in Table 6.3.1.2-1, resulting in a block of complex-valued modulation symbols . qbq0,…,bqMbit(q)-1dq0,…,dq(Msymbq-1)

Table 6.3.1.2-1: Supported modulation schemes.

## 6.3.1.2aInter-slot cover code

The block of complex-valued modulation symbols  shall be multiplied with the quantity  to form the block of complex-valued modulation symbols .dq0,…,dq(Msymbq-1)widq0,…,dq(Msymbq-1)

If the UE transmits PUSCH using repetition type A with OCC

-the quantity  is obtained according to clause 6.1.2.1 of [6, 38.214];wi

otherwise,

-.wi=1

## 6.3.1.3Layer mapping

The complex-valued modulation symbols for each of the codewords to be transmitted shall be mapped onto up to four layers according to Table 7.3.1.3-1. Complex-valued modulation symbols  for codeword  shall be mapped onto the layers ,  where  is the number of layers and  is the number of modulation symbols per layer.dq0,…,dqMsymb(q)-1qxi=x0(i)…xυ-1(i)Ti=0,1,…,Msymblayer-1υMsymblayer

## 6.3.1.4Transform precoding

If transform precoding is not enabled according to 6.1.3 of [6, TS38.214],  for each layer , the total number of modulations symbols  equals .MsymblayerMsymblayer

If transform precoding is enabled according to 6.1.3 of [6, TS38.214],  and  depends on the configuration of phase-tracking reference signals.υ=1

If the procedure in [6, TS 38.214] indicates that phase-tracking reference signals are not being used, the block of complex-valued symbols  for the single layer  shall be divided into sets, each corresponding to one OFDM symbol and where set  contains  symbols and is mapped to the complex-valued symbols , corresponding to OFDM symbol  prior to transform precoding, with . x00,…,x0Msymblayer-1λ=0lMsc,lPUSCHxl0(i')li'∈0,1,…, Msc,lPUSCH-1

If the procedure in [6, TS 38.214] indicates that phase-tracking reference signals are being used, the block of complex-valued symbols  shall be divided into sets, each set corresponding to one OFDM symbol, and where set  contains  symbols and is mapped to the complex-valued symbols  corresponding to OFDM symbol   prior to transform precoding, with  and . The index  of PT-RS samples in set , the number of samples per PT-RS group , and the number of PT-RS groups  are defined in clause 6.4.1.2.2.2. The quantity  when OFDM symbol  contains one or more PT-RS samples, otherwise .x00,…,x0Msymblayer-1lMsc,lPUSCH-εlNsampgroupNgroupPTRSxl0(i')li'∈0,1,…, Msc,lPUSCH-1i'≠mmlNsampgroupNgroupPT-RS

Transform precoding shall be applied according to

yl(0)k=1Msc,lPUSCHi=0Msc,lPUSCH-1xl(0)ie-j2πikMsc,lPUSCH

k=0,…, Msc,lPUSCH-1

resulting in a set of blocks of complex-valued symbols  that shall be concatenated in order of increasing  to form  . The total number of modulations symbols  equals  with any PT-RS samples added.yl0(0), …, yl0(Msc,lPUSCH-1)ly00,…,y0(Msymblayer-1)MsymblayerMsymblayer

The variable, where  represents the bandwidth of the PUSCH in terms of resource blocks, and shall fulfil

where  is a set of non-negative integers.

The variable  equals  when OFDM symbol  is occupied by a muting resource, otherwise .Msc,lPUSCHMscPUSCH/2lMsc,lPUSCH=MscPUSCH

## 6.3.1.5Precoding

The block of vectors  shall be precoded according toy0i…yυ-1iT

z(p0)i⋮z(pρ-1)i=Wy(0)i⋮yυ-1i

where , . The set of antenna ports  shall be determined according to the procedure in [6, TS 38.214]. i=0,1,…,Msymbap-1Msymbap=Msymblayerp0,…,pρ-1

For non-codebook-based transmission, the precoding matrix  equals the identity matrix.W

For codebook-based transmission, the precoding matrix  depends on the number of antenna ports used for the transmission: W

-for single-layer transmission on a single antenna port, ;W=1

-for transmissions using 2, or 4 antenna ports,  is given by Tables 6.3.1.5-1 to 6.3.1.5-7; W

-for transmissions using 3 antenna ports when fourPortSRS-3Tx is configured,  is given by Tables 6.3.1.5-48 to 6.3.1.5-50;W

-for transmissions using 8 antenna ports,  is given byW

Wf(i)=W'i

where

-the subscripts  and  denote the row of the respective matrix;if(i)

- is given by Table 6.3.1.5-8;f(i)

-the intermediate precoding matrix  is given by Tables 6.3.1.5-9 to  6.3.1.5-24, 6.3.1.5-29 to 6.3.1.5-36, and 6.3.1.5-39 to 6.3.1.5-47 with  representing the all-zero matrix with  rows and  columns;W'0m×nmn

-the submatrices  are given by Tables 6.3.1.5-25 to 6.3.1.5-28 and 6.3.1.5-37 to 6.3.1.5-38.Wm,n

The TPMI index used in the tables above is obtained from the DCI scheduling the uplink transmission or the higher-layer parameters according to the procedure in [6, TS 38.214].

When the higher-layer parameter txConfig is not configured, the precoding matrix .W=1

Table 6.3.1.5-1: Precoding matrix  for single-layer transmission using two antenna ports.W

Table 6.3.1.5-2: Precoding matrix  for single-layer transmission using four antenna ports with transform precoding enabled.W

Table 6.3.1.5-3: Precoding matrix  for single-layer transmission using four antenna ports with transform precoding disabled.W

Table 6.3.1.5-4: Precoding matrix  for two-layer transmission using two antenna ports with transform precoding disabled.W

Table 6.3.1.5-5: Precoding matrix  for two-layer transmission using four antenna ports with transform precoding disabled.W

Table 6.3.1.5-6: Precoding matrix  for three-layer transmission using four antenna ports with transform precoding disabled.W

Table 6.3.1.5-7: Precoding matrix  for four-layer transmission using four antenna ports with transform precoding disabled.W

Table 6.3.1.5-8: The port mapping function  for transmission using 8 antenna ports.fi

Table 6.3.1.5-9: Intermediate precoding matrix  for codebook1=ng1n4n1 and single-layer transmission using eight antenna ports.W'

Table 6.3.1.5-10: Intermediate precoding matrix  for codebook1=ng1n4n1 and two-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-11: Intermediate precoding matrix  for codebook1=ng1n4n1 and three-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-12: Intermediate precoding matrix  for codebook1=ng1n4n1 and four-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-13: Intermediate precoding matrix  for codebook1=ng1n4n1 and five-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-14: Intermediate precoding matrix  for codebook1=ng1n4n1 and six-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-15: Intermediate precoding matrix  for codebook1=ng1n4n1 and seven-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-16: Intermediate precoding matrix  for codebook1=ng1n4n1 and eight-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-17: Intermediate precoding matrix  for codebook1=ng1n2n2 and single-layer transmission using eight antenna ports.W'

Table 6.3.1.5-18: Intermediate precoding matrix  for codebook1=ng1n2n2 and two-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-19: Intermediate precoding matrix  for codebook1=ng1n2n2 and three-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-20: Intermediate precoding matrix  for codebook1=ng1n2n2 and four-layer transmission using eight antenna ports with transform precoding disabled.W'

Table 6.3.1.5-21: Intermediate precoding matrix  for codebook1=ng1n2n2 and five-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-22: Intermediate precoding matrix  for codebook1=ng1n2n2 and six-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-23: Intermediate precoding matrix  for codebook1=ng1n2n2 and seven-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-24: Intermediate precoding matrix  for codebook1=ng1n2n2 and eight-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-25: Submatrices  for codebook2 and used in Tables 6.3.1.5-29 to 6.3.1.5-31.W1,i

Table 6.3.1.5-26: Submatrices  for codebook2 and used in Tables 6.3.1.5-30 to 6.3.1.5-33.W2,i

Table 6.3.1.5-27: Submatrices  for codebook2 and used in Tables 6.3.1.5-31, 6.3.1.5-33, 6.3.1.5-34, and 6.3.1.5-35.W3,i

Table 6.3.1.5-28: Submatrices  for codebook2 and used in Tables 6.3.1.5-32, 6.3.1.5-35, and 6.3.1.5-36.W4,i

Table 6.3.1.5-29: Intermediate precoding matrix  for codebook2 and single-layer transmission using eight antenna ports.W'

Table 6.3.1.5-30: Intermediate precoding matrix  for codebook2 and two-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-31: Intermediate precoding matrix  for codebook2 and three-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-32: Intermediate precoding matrix  for codebook2 and four-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-33: Intermediate precoding matrix  for codebook2 and five-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-34: Intermediate precoding matrix  for codebook2 and six-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-35: Intermediate precoding matrix  for codebook2 and seven-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-36: Intermediate precoding matrix  for codebook2 and eight-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-37: Submatrices  for codebook3 and used in Tables 6.3.1.5-39 to 6.3.1.5-45.W1,i

Table 6.3.1.5-38: Submatrices  for codebook3 and used in Tables 6.3.1.5-40 to 6.3.1.5-46.W2,i

Table 6.3.1.5-39: Intermediate precoding matrix  for codebook3 and single-layer transmission using eight antenna ports. W'

Table 6.3.1.5-40: Intermediate precoding matrix  for codebook3 and two-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-41: Intermediate precoding matrix  for codebook3 and three-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-42: Intermediate precoding matrix  for codebook3 and four-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-43: Intermediate precoding matrix  for codebook3 and five-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-44: Intermediate precoding matrix  for codebook3 and six-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-45: Intermediate precoding matrix  for codebook3 and seven-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-46: Intermediate precoding matrix  for codebook3 and eight-layer transmission using eight antenna ports with transform precoding disabled. W'

Table 6.3.1.5-47: Intermediate precoding matrix  for codebook4 and transmission using eight antenna ports. Up to 8 layers are supported with transform precoding disabled and up to one layer with transform precoding enabled.W'

Table 6.3.1.5-48: Precoding matrix  for single-layer transmission using three antenna ports with fourPortSRS-3Tx configured.W

Table 6.3.1.5-49: Precoding matrix  for two-layer transmission using three antenna ports with fourPortSRS-3Tx configured.W

Table 6.3.1.5-50: Precoding matrix  for three-layer transmission using three antenna ports with fourPortSRS-3Tx configured.W

## 6.3.1.6Mapping to virtual resource blocks

For each of the antenna ports used for transmission of the PUSCH, each symbol in the block of complex-valued symbols  shall be multiplied with  if the symbol corresponds to an OFDM symbol occupied by a muting resource, and by 1 otherwise, and further be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  in the virtual resource blocks assigned for transmission which meet all of the following criteria: 2(k',l)p,μ

-they are in the virtual resource blocks assigned for transmission, and

-the corresponding resource elements in the corresponding physical resource blocks are not used for transmission of the associated DM-RS, PT-RS, or DM-RS intended for other co-scheduled UEs as described in clause 6.4.1.1.3, and

-the corresponding resource elements in the corresponding physical resource blocks do not correspond to a muting resource.

The mapping to resource elements  allocated for PUSCH according to [6, TS 38.214] shall be in increasing order of first the index  over the assigned virtual resource blocks, where  is the first subcarrier in the lowest-numbered virtual resource block assigned for transmission, and then the index , with the starting position given by [6, TS 38.214]. (k',l)p,μk'k'=0

## 6.3.1.7Mapping from virtual to physical resource blocks

Virtual resource blocks shall be mapped to physical resource blocks according to non-interleaved mapping.

For non-interleaved VRB-to-PRB mapping for uplink resource allocation types 0 and 1 [6, TS 38.214], virtual resource block  is mapped to physical resource block  except for PUSCH scheduled by RAR UL grant or PUSCH scheduled by DCI format 0_0 with CRC scrambled by TC-RNTI in active uplink bandwidth part  starting at , including all resource blocks of the initial uplink bandwidth part starting at , and having the same subcarrier spacing and cyclic prefix as the initial uplink bandwidth part, in which case virtual resource block  is mapped to physical resource block . nniNBWP,istartNBWP,0startnn+NBWP,0start-NBWP,istart

For non-interleaved VRB-to-PRB mapping for uplink resource allocation type 2 [6, TS 38.214], virtual resource block  is mapped to physical resource block .nn

## 6.3.2Physical uplink control channel

## 6.3.2.1General

The physical uplink control channel supports multiple formats as shown in Table 6.3.2.1-1. In case intra-slot frequency hopping is configured for PUCCH formats 1, 3, or 4 according to clause 9.2.1 of [5, TS38.213], the number of symbols in the first hop is given by  where  is the length of the PUCCH transmission in OFDM symbols.

Table 6.3.2.1-1: PUCCH formats.

## 6.3.2.2Sequence and cyclic shift hopping

PUCCH formats 0, 1, 3, and 4 use sequences  given by clause 5.2.2 with  where the sequence group  and the sequence number  depend on the sequence hopping in clause 6.3.2.2.1 and the cyclic shift  depends on the cyclic shift hopping in clause 6.3.2.2.2.ru,vα,δ(n)δ=0uvα

## 6.3.2.2.1Group and sequence hopping

The sequence group  and the sequence number  within the group depends on the higher-layer parameter pucch-GroupHopping:u=fgh+fss mod 30v

-if pucch-GroupHopping equals 'neither'

where  is given by the higher-layer parameter hoppingId if configured, otherwise .nID=NIDcell

-if pucch-GroupHopping equals 'enable'

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized at the beginning of each radio frame with  where  is given by the higher-layer parameter hoppingId if configured, otherwise .nID=NIDcell

-if pucch-GroupHopping equals 'disable'

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized at the beginning of each radio frame with  where  is given by the higher-layer parameter hoppingId if configured, otherwise .cinit=25nID30+nID mod 30nID=NIDcell

The frequency hopping index  if intra-slot frequency hopping is disabled by the higher-layer parameter intraSlotFrequencyHopping. If frequency hopping is enabled by the higher-layer parameter intraSlotFrequencyHopping,  for the first hop and  for the second hop.nhop=0

## 6.3.2.2.2Cyclic shift hopping

The cyclic shift  varies as a function of the symbol and slot number according toα

αl=2πNscRBm0+mcs+mint+ncsns,fμ,l+l' mod NscRB

where

- is the slot number in the radio framens,fμ

- is the OFDM symbol number in the PUCCH transmission where  corresponds to the first OFDM symbol of the PUCCH transmission,ll=0

- is the index of the OFDM symbol in the slot that corresponds to the first OFDM symbol of the PUCCH transmission in the slot given by [5, TS 38.213]l'

- is given by [5, TS 38.213] for PUCCH format 0 and 1 while for PUCCH format 3 and 4 is defined in clause 6.4.1.3.3.1

- except for PUCCH format 0 when it depends on the information to be transmitted according to clause 9.2 of [5, TS 38.213].

- is given bymint

- for PUCCH formats 0 and 1 if PUCCH shall use interlaced mapping according to any of the higher-layer parameters useInterlacePUCCH-PUSCH in BWP-UplinkCommon or useInterlacePUCCH-PUSCH in BWP-UplinkDedicated, where  is the resource block number within the interlace;mint=5nIRBμnIRBμ

- otherwisemint=0

The function  is given by

ncsns,fμ,l=m=072mc8Nsymbslotns,fμ+8l+m

where the pseudo-random sequence  is defined by clause 5.2.1. The pseudo-random sequence generator shall be initialized with , where  is given by the higher-layer parameter hoppingId if configured, otherwise .nID=NIDcell

## 6.3.2.3PUCCH format 0

## 6.3.2.3.1Sequence generation

The sequence  shall be generated according to

xlMRBPUCCH,0NscRB+n=ru,vα,δnn=0,1,…,MRBPUCCH,0NscRB-1l=0for single-symbol PUCCH transmission0,1for double-symbol PUCCH transmission

where  is given by clause 6.3.2.2 with  depending on the information to be transmitted according to clause 9.2 of [5, TS 38.213]. The quantity  is given by clause 9.2.1 of [5, TS 38.213].ru,vα,δ(n)MRBPUCCH,0

## 6.3.2.3.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  assigned for transmission according to clause 9.2.1 of [5, TS 38.213] in increasing order of first the index  over the assigned physical resources spanning  resource blocks, and then the index  on antenna port . k,lp,μMRBPUCCH,0lp=2000

For interlaced transmission, the mapping operation shall be repeated for each resource block in the interlace and in the active bandwidth part over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], with the resource-block dependent sequence generated according to clause 6.3.2.2.

## 6.3.2.4PUCCH format 1

## 6.3.2.4.1Sequence modulation

The block of bits  shall be modulated as described in clause 5.1 using BPSK if  and QPSK if , resulting in a complex-valued symbol . The complex-valued symbol  shall be multiplied with a sequence  according toru,vα,δ(n)

yn=d0ru,vα,δnn=0,1,…,MRBPUCCH,1NscRB-1

where  is given by clause 6.3.2.2. The quantity  is given by clause 9.2.1 of [5, TS 38.213].ru,vα,δ(n)MRBPUCCH,1

The block of complex-valued symbols  shall be block-wise spread with the orthogonal sequence  according toy0,…,yMRBPUCCH,1NscRB-1

zm'MRBPUCCH,1NscRBNSF,0PUCCH,1+mMRBPUCCH,1NscRB+n=wimynn=0,1,…,MRBPUCCH,1NscRB-1m=0,1,…,NSF,m'PUCCH,1-1m'=0no intra-slot frequency hopping0,1intra-slot frequency hopping

where  is given by Table 6.3.2.4.1-1. Intra-slot frequency hopping shall be assumed when the higher-layer parameter intraSlotFrequencyHopping is provided, regardless of whether the frequency-hop distance is zero or not, and interlaced mapping is not enabled, otherwise no intra-slot frequency hopping shall be assumed.NSF,m'PUCCH,1

The orthogonal sequence  is given by Table 6.3.2.4.1-2 where  is the index of the orthogonal sequence to use according to clause 9.2.1 of [5, TS 38.213]. In case of a PUCCH transmission spanning multiple slots according to clause 9.2.6 of [5, TS38.213], the complex-valued symbol  is repeated for the subsequent slots.

Table 6.3.2.4.1-1: Number of PUCCH symbols and the corresponding .

Table 6.3.2.4.1-2: Orthogonal sequences  for PUCCH format 1.

## 6.3.2.4.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  which meet all of the following criteria: znβPUCCH,1znk,lp,μ

-they are in the resource blocks assigned for transmission,

-they are not used by the associated DM-RS

The mapping to resource elements  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], and then the index  on antenna port . k,lp,μklp=2000

For interlaced transmission, the mapping operation shall be repeated for each resource block in the interlace and in the active bandwidth part over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], with the resource-block dependent sequence generated according to clause 6.3.2.2.

## 6.3.2.5PUCCH format 2

## 6.3.2.5.1Scrambling

The block of bits , where  is the number of bits transmitted on the physical channel, shall be scrambled prior to modulation, resulting in a block of scrambled bits  according to the following pseudo codeb0,…,b(Mbit-1)Mbitb0,…,b(Mbit-1)

Set i = 0

while i<Mbit

if // UCI placeholder bitsbi=y

bi= bi-1

else

bi=bi+c(i) mod 2

end if

i = i + 1

end while

where y is the tag defined in [4, TS38.212] and the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with c(i)

cinit=nRNTI∙215+nID

where

- equals the higher-layer parameter dataScramblingIdentityPUSCH if configured,nID∈0,1,…,1023

- otherwisenID=NIDcell

and  is given by the C-RNTI.nRNTI

## 6.3.2.5.2Modulation

The block of scrambled bits  shall be modulated as described in clause 5.1 using QPSK, resulting in a block of complex-valued modulation symbols  where . b0,…,b(Mbit-1)d0,…,d(Msymb-1)Msymb=Mbit2

## 6.3.2.5.2ASpreading

Spreading shall be applied according to

zmNSFPUCCH,2+i=wnidmi=0,1,…,NSFPUCCH,2-1m=0,1,…,Msymb-1

resulting in a block of complex-valued symbols .z0,…,z(NSFPUCCH,2Msymb-1)

If the higher-layer parameter interlace1 is not configured, and the higher-layer parameter occ-Length is configured,

- is given by the higher-layer parameter occ-Length; NSFPUCCH,2∈2,4

- is given by Tables 6.3.2.5A-1 and 6.3.2.5A-2 where , the quantity  is the index of the orthogonal sequence to use given by the higher-layer parameter occ-Index, and  is the interlaced resource block number as defined in clause 4.4.4.6 within the interlace given by the higher-layer parameter Interlace0.wnin=n0+nIRB mod NSFPUCCH,2n0nIRB

otherwise  and NSFPUCCH,2=1wni=1.

Table 6.3.2.5A-1: Orthogonal sequences  for PUCCH format 2 when .wniNSFPUCCH,2=2

Table 6.3.2.5A-2: Orthogonal sequences  for PUCCH format 2 when .wniNSFPUCCH,2=4

## 6.3.2.5.3Mapping to physical resources

The block of complex-valued symbols  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  which meet all of the following criteria: z0,…,z(NSFPUCCH,2Msymb-1)z0k,lp,μ

-they are in the resource blocks assigned for transmission,

-they are not used by the associated DM-RS.

The mapping to resource elements  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], and then the index  on antenna port .k,lp,μ

## 6.3.2.6PUCCH formats 3 and 4

## 6.3.2.6.1Scrambling

The block of bits , where  is the number of bits transmitted on the physical channel, shall be scrambled prior to modulation, resulting in a block of scrambled bits  according to the following pseudo codeb0,…,b(Mbit-1)Mbitb0,…,b(Mbit-1)

Set i = 0

while i<Mbit

if // UCI placeholder bitsbi=y

bi= bi-1

else

bi=bi+c(i) mod 2

end if

i = i + 1

end while

where y is the tag defined in [4, TS38.212] and the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with c(i)

cinit=nRNTI∙215+nID

where

- equals the higher-layer parameter dataScramblingIdentityPUSCH if configured,nID∈0,1,…,1023

- otherwisenID=NIDcell

and  is given by the C-RNTI.nRNTI

## 6.3.2.6.2Modulation

The block of scrambled bits  shall be modulated as described in clause 5.1 using QPSK unless π/2-BPSK is configured, resulting in a block of complex-valued modulation symbols  where  for QPSK and  for π/2-BPSK. b0,…,b(Mbit-1)d0,…,d(Msymb-1)Msymb=Mbit2Msymb=Mbit

## 6.3.2.6.3Block-wise spreading

For both PUCCH format 3 and 4,   with  representing the bandwidth of the PUCCH in terms of resource blocks according to clauses 9.2.3, 9.2.5.1 and 9.2.5.2 of [5, TS 38.213] and shall for non-interlaced mapping fulfilMscPUCCH,s=MRBPUCCH,sNscRBMRBPUCCH,s

MRBPUCCH,s=2α2∙3α3∙5α5

where  is a set of non-negative integers and . For interlaced mapping,  if a single interlace is configured and  if two interlaces are configured.MRBPUCCH,3=10MRBPUCCH,3=20

For PUCCH format 3, if interlaced mapping is not configured, no block-wise spreading is applied and

where  is given by clauses 9.2.3, 9.2.5.1 and 9.2.5.2 of [5, TS 38.213] and .MRBPUCCH,3≥1NSFPUCCH,3=1

For PUCCH format 3 with interlaced mapping and PUCCH format 4, block-wise spreading shall be applied according to

ylMscPUCCH,s+k=wnkNSFPUCCH,sMscPUCCH,sdlMscPUCCH,sNSFPUCCH,s+k mod MscPUCCH,sNSFPUCCH,sk=0,1,…, MscPUCCH,s-1l=0,1,…,NSFPUCCH,sMsymbMscPUCCH,s-1

where

-for PUCCH format 3 with interlaced mapping,  if a single interlace is configured and ,  if two interlaces are configured;NSFPUCCH,3∈1,2,4NSFPUCCH,3=1wn=1

-for PUCCH format 4,  is given by the higher-layer parameter occ-Length; MRBPUCCH,4 is given by clause 9.2.1 of [5, TS 38.213] and  NSFPUCCH,4∈2,4

and  is given by Tables 6.3.2.6.3-1 and 6.3.2.6.3-2 for  where  is the index of the orthogonal sequence to use according to clause 9.2.1 of [5, TS 38.213]. The quantity  is given by the higher-layer parameter occ-Length if provided, otherwise .NSFPUCCH,s>1nNSFPUCCH,3∈2,4NSFPUCCH,3=1

Table 6.3.2.6.3-1: Orthogonal sequences  for PUCCH format 3 with interlaced mapping and PUCCH format 4 when .NSFPUCCH,s=2

Table 6.3.2.6.3-2: Orthogonal sequences  for PUCCH format 3 with interlaced mapping and PUCCH format 4 when .NSFPUCCH,s=4

## 6.3.2.6.4Transform precoding

The block of complex-valued symbols  shall be transform precoded according toy0,…,y(NSFPUCCH,sMsymb-1)

resulting in a block of complex-valued symbols . z0,…,z(NSFPUCCH,sMsymb-1)

## 6.3.2.6.5Mapping to physical resources

The block of modulation symbols  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  which meet all of the following criteria: z0,…,z(NSFPUCCH,sMsymb-1)z(0)(k,l)p,μ

-they are in the resource blocks assigned for transmission,

-they are not used by the associated DM-RS

The mapping to resource elements  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], and then the index  on antenna port . (k,l)p,μ

In case of intra-slot frequency hopping according to clause 9.2.1 of [5, TS 38.213],  OFDM symbols shall be transmitted in the first hop and  symbols in the second hop where  is the total number of OFDM symbols used in one slot for PUCCH transmission.

## 6.3.3Physical random-access channel

## 6.3.3.1Sequence generation

The set of random-access preambles  shall be generated according to

from which the frequency-domain representation shall be generated according to

where , , , or  depending on the PRACH preamble format as given by Tables 6.3.3.1-1 and 6.3.3.1-2.LRA=1151LRA=571

There are 64 preambles defined in each time-frequency PRACH occasion, enumerated in increasing order of first increasing cyclic shift  of a logical root sequence, and then in increasing order of the logical root sequence index, starting with the index obtained from the higher-layer parameter

-prach-RootSequenceIndex or rootSequenceIndex-BFR or by msgA-PRACH-RootSequenceIndex if configured and a type-2 random-access procedure is initiated as described in clause 8.1 of [5, TS 38.213], or by

-prach-RootSequenceIndex in EarlyUL-SyncConfig if the PRACH transmission is for a candidate cell, or by

-prach-RootSequenceIndex in RACH-ConfigTwoTA if the PRACH transmission is associated with an additional PCI different from serving cell PCI, or by

-prach-RootSequenceIndex in SIB1-RequestConfig if the PRACH transmission is for SIB1 request.

Additional preamble sequences, in case 64 preambles cannot be generated from a single root Zadoff-Chu sequence, are obtained from the root sequences with the consecutive logical indexes until all the 64 sequences are found. The logical root sequence order is cyclic; the logical index 0 is consecutive to . The sequence number  is obtained from the logical root sequence index according to Tables 6.3.3.1-3 to 6.3.3.1-4B.LRA-2

The cyclic shift  is given by

where  is given by Tables 6.3.3.1-5 to 6.3.3.1-7. The type of restricted sets (unrestricted, restricted type A, restricted type B) is given by

-the higher-layer parameter msgA-RestrictedSetConfig, if provided;

-or the higher-layer parameter ltm-restrictedSetConfig associated with a candidate cell indicated in Cell indicator field of a PDCCH order, if provided;

-or the higher-layer parameter twoTA-restrictedSetConfig associated with an additional PCI indicated in PRACH association indicator field of a PDCCH order, if provided;

-otherwise, the higher-layer parameter restrictedSetConfig.

Tables 6.3.3.1-1 and 6.3.3.1-2 indicate the type of restricted sets supported for the different preamble formats.

The variable  is given by

where  is the smallest non-negative integer that fulfils . The parameters for restricted sets of cyclic shifts depend on .

For restricted set type A, the parameters are given by:

-for

-for

For restricted set type B, the parameters are given by:

-for

-for

-for

-for

-for

-for

For all other values of , there are no cyclic shifts in the restricted set.

Table 6.3.3.1-1: PRACH preamble formats for  and  kHz.ΔfRA∈1.25, 5

Table 6.3.3.1-2: Preamble formats for  and  kHz where .LRA∈139, 571, 1151ΔfRA=15⋅2μμ∈0,1,2,3,5,6

Table 6.3.3.1-3: Mapping from logical index  to sequence number  for preamble formats with .

Table 6.3.3.1-4: Mapping from logical index  to sequence number  for preamble formats with .

Table 6.3.3.1-4A: Mapping from logical index  to sequence number  for preamble formats with .iuLRA=1151

Table 6.3.3.1-4B: Mapping from logical index  to sequence number  for preamble formats with .iuLRA=571

Table 6.3.3.1-5:  for preamble formats with  kHz.ΔfRA=1.25

Table 6.3.3.1-6:  for preamble formats with  kHz.ΔfRA=5

Table 6.3.3.1-7:  for preamble formats with  .LRA∈139, 571, 1151

## 6.3.3.2Mapping to physical resources

The preamble sequence shall be mapped to physical resources according to

where  is an amplitude scaling factor in order to conform to the transmit power specified in [5, TS38.213], and  is the antenna port. Baseband signal generation shall be done according to clause 5.3 using the parameters in Table 6.3.3.1-1 or Table 6.3.3.1-2 with  given by Table 6.3.3.2-1.

Random access preambles can only be transmitted in the time resources obtained from Tables 6.3.3.2-2 to 6.3.3.2-4 and depends on FR1, FR2, or FR2-NTN and the spectrum type as defined in [8, TS38.104] or [17, TS38.108]. The PRACH configuration index in Tables 6.3.3.2-2 to 6.3.3.2-4 is

-for Table 6.3.3.2-3 given by the higher-layer parameter prach-ConfigurationIndex, or by msgA-PRACH-ConfigurationIndex if configured; and

-for Tables 6.3.3.2-2 and 6.3.3.2-4 given by the higher-layer parameter prach-ConfigurationIndex, or by msgA-PRACH-ConfigurationIndex if configured.

For the IAB-MT part of an IAB-node, the following applies:

-if the higher-layer parameter prach-ConfigurationPeriodScaling-IAB is configured, the variable  used in  of Tables 6.3.3.2-2 to 6.3.3.2-4 shall be replaced by  , where  and  is given by the higher-layer parameter prach-ConfigurationPeriodScaling-IAB and the IAB-node does not expect  to be larger than 64;xnf mod x=y xIAB xIAB=δxδxIAB

-if the higher-layer parameter prach-ConfigurationFrameOffset-IAB is configured, the variable  used in  of Tables 6.3.3.2-2 to 6.3.3.2-4 shall be replaced by  where  is given by the higher-layer parameter prach-ConfigurationFrameOffset-IAB, and ;ynf mod x=yyIAB=y+Δy mod xΔy  x is the value used in nf mod x=y

-if the higher-layer parameter prach-ConfigurationSOffset-IAB is configured, the subframe number  from Tables 6.3.3.2-2 to 6.3.3.2-3 and the slot number  from Table 6.3.3.2-4 shall be replaced by  where  is given by the higher-layer parameter prach-ConfigurationSOffset-IAB, and  is the number of subframes in a frame when using Tables 6.3.3.2-2 to 6.3.3.2-3 and the number of slots in a frame for 60 kHz subcarrier spacing when using in Table 6.3.3.2-4.snsnsn+Δs mod LΔs∈0,1,…,L-1L

Random access preambles can only be transmitted in the frequency resources given by either the higher-layer parameter msg1-FrequencyStart or msgA-RO-FrequencyStart if configured as described in clause 8.1 of [5 TS 38.213]. The PRACH frequency resources , where  equals the higher-layer parameter msg1-FDM or msgA-RO-FDM if configured, are numbered in increasing order within the initial uplink bandwidth part during initial access, starting from the lowest frequency. Otherwise,  are numbered in increasing order within the active uplink bandwidth part, starting from the lowest frequency.nRA∈0,1,…,M-1MnRA

For operation with shared spectrum channel access, for , a UE expects to be provided with higher-layer parameter msg1-FrequencyStart or msgA-RO-FrequencyStart if configured, and higher-layer parameter msg1-FDM or msgA-RO-FDM if configured, such that a random-access preamble is confined within a single RB set. The UE assumes that the RB set is defined as when the UE is not provided intraCellGuardBandsPerSCS for an UL carrier as described in Clause 7 of [6, TS 38.214].LRA=139

For operation with shared spectrum channel access, for  or  and Type-2 random access, a UE expects to be provided with higher-layer parameter msgA-RO-FDM equals to one.LRA=5711151

For the purpose of slot numbering in the tables, the following subcarrier spacing shall be assumed:

-15 kHz for FR1

-60 kHz for FR2 and FR2-NTN.

For handover purposes to a target cell in paired or unpaired spectrum where the target cell uses , the UE may assume the absolute value of the time difference between radio frame  in the current cell and radio frame  in the target cell is less than  if the association pattern period in clause 8.1 of [5, TS 38.213] is not equal to 10 ms.Lmax=4ii153600Ts

For inter frequency handover purposes where the source cell is either in paired or unpaired spectrum and the target cell is in unpaired spectrum and uses , the UE may assume the absolute value of the time difference between radio frame  in the current cell and radio frame  in the target cell is less than Lmax=8ii76800Ts.

Table 6.3.3.2-1: Supported combinations of  and , and the corresponding value of .ΔfRAΔfk

Table 6.3.3.2-2: Random access configurations for FR1 and paired spectrum/supplementary uplink.

Table 6.3.3.2-3: Random access configurations for FR1 and unpaired spectrum.

Table 6.3.3.2-4: Random access configurations for FR2 and unpaired spectrum, and for FR2-NTN and paired spectrum.

## 6.4Physical signals

## 6.4.1Reference signals

## 6.4.1.1Demodulation reference signal for PUSCH

## 6.4.1.1.1Sequence generation

6.4.1.1.1.1Sequence generation when transform precoding is disabled

If transform precoding for PUSCH is not enabled, the sequence  shall be generated according to

.

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialized with

cinit=217Nsymbslotns,fμ+l+12NIDnSCIDλ+1+217λ2+2NIDnSCIDλ+nSCIDλmod 231

where  is the OFDM symbol number within the slot,  is the slot number within a frame, andns,fμ

- are given by the higher-layer parameters scramblingID0 and scramblingID1, respectively, in the DMRS-UplinkConfig IE if provided and the PUSCH is scheduled by DCI format 0_1, 0_2, or 0_3, or by a PUSCH transmission with a configured grant; NID0,NID1∈0,1,…,65535

- is given by the higher-layer parameter scramblingID0 in the DMRS-UplinkConfig IE if provided and the PUSCH is scheduled by DCI format 0_0 with the CRC scrambled by C-RNTI, MCS-C-RNTI, or CS-RNTI; NID0∈0,1,…,65535

- are, for each msgA PUSCH configuration, given by the higher-layer parameters msgA-ScramblingID0 and msgA-ScramblingID1, respectively, in the msgA-DMRS-Config IE if provided and the PUSCH transmission is triggered by a Type-2 random access procedure as described in clause 8.1A of [5, TS 38.213];NID0,NID1∈0,1,…,65535

-  otherwise;NIDnSCIDλ=NIDcell

- and  are given bynSCIDλ λ

-if the higher-layer parameter dmrs-Uplink in the DMRS-UplinkConfig IE is provided

nSCIDλ=nSCIDλ=0 or λ=21-nSCIDλ=1λ=λ

where  is the CDM group defined in clause 6.4.1.1.3.λ

-otherwise

nSCIDλ=nSCIDλ=0

The quantity  isnSCID∈0,1

-indicated by the DM-RS initialization field, if present, either in the DCI associated with the PUSCH transmission if DCI format 0_1, 0_2, or 0_3, in [4, TS 38.212] is used;

-indicated by the higher-layer parameter dmrs-SeqInitialization, if present, for a Type 1 PUSCH transmission with a configured grant;

-determined by the mapping between preamble(s) and a PUSCH occasion and the associated DMRS resource for a PUSCH transmission of Type-2 random access process in [5, TS 38.213];

-determined by the mapping between SS/PBCH block(s) and a PUSCH occasion and the associated DMRS resource for a configured-grant based PUSCH transmission in RRC_INACTIVE state [5, TS 38.213];

-determined by the mapping between SS/PBCH block(s) and a PUSCH occasion and the associated DMRS resource for a configured-grant based PUSCH transmission in RACH-less handover [5, TS 38.213];

-determined by the mapping between SS/PBCH block(s) and a PUSCH occasion and the associated DMRS resource for a configured-grant PUSCH transmission in RACH-less LTM cell switch [5, TS 38.213];

-otherwise .nSCID=0

6.4.1.1.1.2Sequence generation when transform precoding is enabled

If transform precoding for PUSCH is enabled, the reference-signal sequence  shall be generated according to

where  with  depends on the configuration:ru,vα,δ(n)δ=1

-if the higher-layer parameter dmrs-UplinkTransformPrecoding is configured, π/2-BPSK modulation is used for PUSCH, and the PUSCH transmission is not a msg3 transmission, and the transmission is not scheduled using DCI format 0_0 in a common search space,  is given by clause 5.2.3 with  given byru,vα,δ(n)cinit

cinit=217Nsymbslotns,fμ+l+12NIDnSCID+1+2NIDnSCID+nSCIDmod 231

where  unless given by the DCI according to clause 7.3.1.1.2 in  [4, TS38.212] for a transmission scheduled by DCI format 0_1, or given by the DCI according to clause 7.3.1.1.3 in  [4, TS38.212] for a transmission scheduled by DCI format 0_2 if the antenna ports field in the DCI format 0_2 is not 0 bit, or given by the DCI according to clause 7.3.1.1.4 in  [4, TS38.212] for a transmission scheduled by DCI format 0_3, or given by the higher-layer parameter antennaPort for a PUSCH transmission scheduled by a type-1 configured grant; andnSCID=0

- are given by the higher-layer parameters pi2BPSK-ScramblingID0 and pi2BPSK-ScramblingID1, respectively, in the DMRS-UplinkConfig IE if provided and the PUSCH is scheduled by DCI format 0_1, or by DCI format 0_2 if the antenna ports field in the DCI format 0_2 is not 0 bit, or by DCI format 0_3, or by a PUSCH transmission with a configured grant; NID0,NID1∈0,1,…,65535

- is given by the higher-layer parameter pi2BPSK-ScramblingID0 in the DMRS-UplinkConfig IE if provided and the PUSCH is scheduled by DCI format 0_0 with the CRC scrambled by C-RNTI, MCS-C-RNTI, or CS-RNTI, or by DCI format 0_2 if the antenna ports field in the DCI format 0_2 is  0 bit;NID0∈0,1,…,65535

- otherwise; NIDnSCID=NIDcell

-otherwise,  is given by clause 5.2.2 with .ru,vα,δ(n)α=0

The sequence group , where  is given byu=fgh+nIDRS mod 30nIDRS

- if  is configured by the higher-layer parameter nPUSCH-Identity in the DMRS-UplinkConfig IE, and nIDRS=nIDPUSCHnIDPUSCH

-the higher-layer parameter dmrs-UplinkTransformPrecoding is not configured or the higher-layer parameter dmrs-UplinkTransformPrecoding is configured and π/2-BPSK modulation is not used for PUSCH, and

-the PUSCH is neither scheduled by RAR UL grant nor scheduled by DCI format 0_0 with CRC scrambled by TC-RNTI according to clause 8.3 in [5, TS 38.213];

- if the higher-layer parameter dmrs-UplinkTransformPrecoding is configured, π/2-BPSK modulation is used for PUSCH, the PUSCH transmission is not a msg3 transmission, and the transmission is not scheduled using DCI format 0_0 in a common search space;nIDRS=NIDnSCID

- otherwisenIDRS=NIDcell

where  and the sequence number  are given by:v

-if neither group, nor sequence hopping is enabled

-if group hopping is enabled and sequence hopping is disabled

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame

-if sequence hopping is enabled and group hopping is disabled

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame.

The hopping mode is controlled by higher-layer parameters:

-for PUSCH transmission scheduled by RAR UL grant or by DCI format 0_0 with CRC scrambled by TC-RNTI, sequence hopping is disabled and group hopping is enabled or disabled by the higher-layer parameter groupHoppingEnabledTransformPrecoding;

-for all other transmissions, sequence hopping and group hopping are enabled or disabled by the respective higher-layer parameters sequenceHopping and sequenceGroupHopping if these parameters are provided, otherwise, the same hopping mode as for Msg3 shall be used.

The UE is not expected to handle the case of combined sequence hopping and group hopping.

The quantity  above is the OFDM symbol number in the slot except for the case of double-symbol DMRS in which case  is the OFDM symbol number in the slot of the first symbol of the double-symbol DMRS.ll

## 6.4.1.1.2(void)

## 6.4.1.1.3Precoding and mapping to physical resources

The sequence  shall be mapped to the intermediate quantity  according to ak,l(pj,μ)

-if transform precoding is not enabled,

-if the higher-layer parameter dmrs-TypeEnh is configured

ak,lpj,μ=wfk'wtl'r4n+k'k=8n+2k'+Δconfiguration type 112n+k'+Δconfiguration type 2, k'=0,112n+k'+Δ+4configuration type 2, k'=2,3k'=0,1,2,3l=l+l'n=0,1,…j=0,1,…,υ-1

-otherwise

ak,lpj,μ=wfk'wtl'r2n+k'k=4n+2k'+Δconfiguration type 16n+k'+Δconfiguration type 2k'=0,1l=l+l'n=0,1,…j=0,1,…,υ-1

-if transform precoding is enabled

ak,lp0,μ=wfk'wtl'r2n+k'k=4n+2k'+Δk'=0,1l=l+l'n=0,1,…

where , , and  are given by Tables 6.4.1.1.3-1 and 6.4.1.1.3-2 and the configuration type is given by the higher-layer parameter DMRS-UplinkConfig, and both  and  correspond to . The intermediate quantity  if Δ corresponds to any other antenna ports than. wfk'wtl'Δk'Δp0, …, pν-1ak,l(pj,μ)=0 pj

The intermediate quantity  shall be precoded, multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [6, TS 38.214], and mapped to physical resources according toak,l(pj,μ)βPUSCHDMRS

ak,lp0,μ⋮ak,lpρ-1,μ=βPUSCHDMRSWak,lp0,μ⋮ak,lpυ-1,μ

where

-the precoding matrix  is given by clause 6.3.1.5, W

-the set of antenna ports  is given by clause 6.3.1.5, andp0,…,pρ-1

-the set of antenna ports  is given by [6, TS 38.214];p0,…,pρ-1

and the following conditions are fulfilled:

-the resource elements  are within the common resource blocks allocated for PUSCH transmission.ak,l(pj,μ)

The reference point for  is k

-subcarrier 0 in common resource block 0 if transform precoding is not enabled, and

-subcarrier 0 of the lowest-numbered resource block of the scheduled PUSCH allocation if transform precoding is enabled.

The reference point for  and the position  of the first DM-RS symbol depends on the mapping type:l

-for PUSCH mapping type A:

- is defined relative to the start of the slot if frequency hopping is disabled and relative to the start of each hop in case frequency hopping is enabled

- is given by the higher-layer parameter dmrs-TypeA-Position

-for PUSCH mapping type B:

- is defined relative to the start of the scheduled PUSCH resources if frequency hopping is disabled and relative to the start of each hop in case frequency hopping is enabled

-

The position(s) of the DM-RS symbols is given by  and duration  whereld

- is the duration between the first OFDM symbol of the slot and the last OFDM symbol of the scheduled PUSCH resources in the slot for PUSCH mapping type A according to Tables 6.4.1.1.3-3 and 6.4.1.1.3-4 if intra-slot frequency hopping is not used, or ld

- is the duration of scheduled PUSCH resources for PUSCH mapping type B according to Tables 6.4.1.1.3-3 and 6.4.1.1.3-4 if intra-slot frequency hopping is not used, orld

- is the duration per hop according to Table 6.4.1.1.3-6 if intra-slot frequency hopping is used. ld

-if the higher-layer parameter maxLength in DMRS-UplinkConfig is not configured, or for a msgA transmission msgA-MaxLength in msgA-DMRS-Config is not configured, the tables shall be used according to single-symbol DM-RS

-if the higher-layer parameter maxLength in DMRS-UplinkConfig is equal to 'len2', the associated DCI or configured grant configuration determines whether single-symbol or double-symbol DM-RS shall be used

-if the higher-layer parameter msgA-MaxLength in msgA-DMRS-Config is equal to 'len2', double-symbol DM-RS shall be used

-if the higher-layer parameter dmrs-AdditionalPosition is not set to 'pos0' and intra-slot frequency hopping is enabled according to clause 7.3.1.1.2 in [4, TS 38.212] and by higher layer, Tables 6.4.1.1.3-6 shall be used assuming dmrs-AdditionalPosition is equal to 'pos1' for each hop.

For PUSCH mapping type A,

-the case dmrs-AdditionalPosition is equal to 'pos3' is only supported when dmrs-TypeA-Position is equal to 'pos2';

- symbols in Table 6.4.1.1.3-4 is only applicable when dmrs-TypeA-Position is equal to 'pos2'.ld=4

For msgA transmitted using PUSCH mapping type A,

-the case msgA-DMRS-AdditionalPosition is equal to 'pos3' is only supported when dmrs-TypeA-Position is equal to 'pos2';

-'dmrs-AdditionalPosition' in Tables 6.4.1.1.3-3 to 6.4.1.1.3-6 shall be replaced by msgA-DMRS-AdditionalPosition;

-only PUSCH DM-RS configuration type 1 is supported;

-only basic DM-RS multiplexing in Table 6.4.1.1.3-5 is supported.

For msgA transmitted using PUSCH mapping type B,

-'dmrs-AdditionalPosition' in Tables 6.4.1.1.3-3 to 6.4.1.1.3-6 shall be replaced by msgA-DMRS-AdditionalPosition;

-only PUSCH DM-RS configuration type 1 is supported;

-only basic DM-RS multiplexing in Table 6.4.1.1.3-5 is supported.

The time-domain index , and the supported antenna ports  are given by Table 6.4.1.1.3-5. l'pj

Table 6.4.1.1.3-1: Parameters for PUSCH DM-RS configuration type 1.

Table 6.4.1.1.3-2: Parameters for PUSCH DM-RS configuration type 2.

Table 6.4.1.1.3-3: PUSCH DM-RS positions  within a slot for single-symbol DM-RS and intra-slot frequency hopping disabled.

Table 6.4.1.1.3-4: PUSCH DM-RS positions  within a slot for double-symbol DM-RS and intra-slot frequency hopping disabled.

Table 6.4.1.1.3-5: PUSCH DM-RS time index .l'

Table 6.4.1.1.3-6: PUSCH DM-RS positions  within a slot for single-symbol DM-RS and intra-slot frequency hopping enabled.

## 6.4.1.2Phase-tracking reference signals for PUSCH

## 6.4.1.2.1Sequence generation

## 6.4.1.2.1.1Sequence generation if transform precoding is not enabled

If transform precoding is not enabled, the precoded phase-tracking reference signal for subcarrier  on layer  is given by

r(pj)m=rmif j=j' or j=j"0otherwise

where

-antenna ports  or  associated with PT-RS transmission are given by clause 6.2.3 of [6, TS 38.214]

- is given by clause 6.4.1.1.1.1

-at the position of the first DM-RS symbol in absence of PUSCH intra-slot frequency hopping

-at the position of the first DM-RS symbol in hop  in presence of PUSCH intra-slot frequency hopping h∈0,1

## 6.4.1.2.1.2Sequence generation if transform precoding is enabled

If transform precoding is enabled, the phase-tracking reference signal  to be mapped in position  before transform precoding, where  depends on the number of PT-RS groups , the number of samples per PT-RS group , and  according to Table 6.4.1.2.2.2-1, shall be generated according tommNgroupPT-RSMscPUSCH

.

where the pseudo-random sequence  is defined in clause 5.2.1 and  is given by Table 6.4.1.2.1.2-1. The pseudo-random sequence generator shall be initialized with

cinit=217Nsymbslotns,fμ+l+12NID+1+2NIDmod231

where  is the lowest OFDM symbol number in the PUSCH allocation in slot  that contains PT-RS according to clause 6.4.1.2.2.2 and  is given by the higher-layer parameter nPUSCH-Identity. ns,fμNID

Table 6.4.1.2.1.2-1: The orthogonal sequence .

## 6.4.1.2.2Mapping to physical resources

## 6.4.1.2.2.1Precoding and mapping to physical resources if transform precoding is not enabled

The UE shall transmit phase-tracking reference signals only in the resource blocks used for the PUSCH, and only if the procedure in [6, TS 38.214] indicates that phase-tracking reference signals are being used.

The PUSCH PT-RS shall be mapped to resource elements according to

-if the higher-layer parameter dmrs-TypeEnh is configured

ak,lpo,μ⋮ak,lpρ-1,μ=δβPT-RSWr(p0)(4n+k')⋮r(pυ-1)(4n+k')

k=8n+2k'+Δconfiguration type 112n+k'+Δconfiguration type 2, k'∈0, 112n+k'+Δ+4configuration type 2, k'∈2, 3

-otherwise

ak,lpo,μ⋮ak,lpρ-1,μ=δβPT-RSWr(p0)(2n+k')⋮r(pυ-1)(2n+k')

k=4n+2k'+Δconfiguration type 16n+k'+Δconfiguration type 2

when all the following conditions are fulfilled

- is within the OFDM symbols allocated for the PUSCH transmissionl

-resource element  is not used for DM-RSk,l

- and  correspond to k'Δp0, …, pν-1

The quantities  and  are given by Tables 6.4.1.1.3-1 and 6.4.1.1.3-2, the configuration type is given by the higher-layer parameter dmrs-Type in the DMRS-UplinkConfig IE, and the precoding matrix  is given by clause 6.3.1.5. The quantity  is an amplitude scaling factor to conform with the transmit power specified in clause 6.2.3 of [6, TS 38.214]. The quantity  if  corresponds to an OFDM symbol occupied by a muting resource, otherwise .k'ΔWβPT-RSδ=2lδ=1

The set of time indices  defined relative to the start of the PUSCH allocation is defined byl

1. set and i=0 lref=0

2. if any symbol in the interval  overlaps with a symbol used for DM-RS according to clause 6.4.1.1.3maxlref+i-1LPT-RS+1, lref,…,lref+iLPT-RS

-set i=1

-set  to the symbol index of the DM-RS symbol in case of a single-symbol DM-RS or to the symbol index of the second DM-RS symbol in case of a double-symbol DM-RSlref

-repeat from step 2 as long as  is inside the PUSCH allocationlref+iLPT-RS

3. add  to the set of time indices for PT-RSlref+iLPT-RS

4. increment  by onei

5. repeat from step 2 above as long as  is inside the PUSCH allocationlref+iLPT-RS

where  is defined in Table 6.2.3.1-1 of [6, TS 38.214].LPT-RS∈1,2,4

For the purpose of PT-RS mapping, the resource blocks allocated for PUSCH transmission are numbered from 0 to  from the lowest scheduled resource block to the highest. The corresponding subcarriers in this set of resource blocks are numbered in increasing order starting from the lowest frequency from 0 to . The subcarriers to which the PT-RS shall be mapped are given byNscRBNRB-1

where

-

- is given by Table 6.4.1.2.2.1-1 for the DM-RS port associated with the PT-RS port according to clause 6.2.3 in [6, TS 38.214]. If the higher-layer parameter resourceElementOffset in PTRS-UplinkConfig is not configured, the column corresponding to 'offset00' shall be used.

-is the RNTI associated with the DCI scheduling the transmission using C-RNTI, CS-RNTI, MCS-C-RNTI, SP-CSI-RNTI, or is the CS-RNTI in case of configured grant

- is the number of resource blocks scheduledNRB

- is given by [6, TS 38.214].KPT-RS∈2,4

Table 6.4.1.2.2.1-1: The parameter  .

## 6.4.1.2.2.2Mapping to physical resources if transform precoding is enabled

The UE shall transmit phase-tracking reference signals only in the resource blocks and OFDM symbols used for the PUSCH, and only if the procedure in [6, TS 38.214] indicates that phase-tracking reference signals are being used.

The sequence  shall be multiplied by  and mapped to  complex valued symbols in  whereNsampgroupNgroupPT-RS

- are the complex-valued symbols in OFDM symbol  before transform precoding according to clause 6.3.1.4

- depends on the number of PT-RS groups , the number of samples per PT-RS group , and  according to Table 6.4.1.2.2.2-1m

- is the ratio between amplitude of one of the outermost constellation points for the modulation scheme used for PUSCH and one of the outermost constellation points for π/2-BPSK as defined in clause 6.2.3 of [TS 38.214]

The set of time indices  for which PT-RS shall be transmitted is defined relative to the start of the PUSCH allocation and is defined by

1. set  and

2. if any symbol in the interval  overlaps with a symbol used for DM-RS according to clause 6.4.1.1.3maxlref+i-1LPT-RS+1, lref,…,lref+iLPT-RS

-set i=1

-set  to the symbol index of the DM-RS symbol in case of a single-symbol DM-RS and to the symbol index of the second DM-RS symbol in case of a double-symbol DM-RS

-repeat from step 2 as long as  is inside the PUSCH allocation

3. add  to the set of time indices for PT-RS

4. increment  by one

5. repeat from step 2 above as long as  is inside the PUSCH allocation

where  is given by the higher-layer parameter timeDensityTransformPrecoding in the PTRS-UplinkConfig IE.LPT-RS∈1,2LPT-RS∈1,2

Table 6.4.1.2.2.2-1: PT-RS symbol mapping.

## 6.4.1.3Demodulation reference signal for PUCCH

## 6.4.1.3.1Demodulation reference signal for PUCCH format 1

## 6.4.1.3.1.1Sequence generation

The reference signal sequence is defined by

zm'NSF,0PUCCH,1MRBPUCCH,1NscRB+mMRBPUCCH,1NscRB+n=wimru,vα,δnn=0,1,…,MRBPUCCH,1NscRB-1m=0,1,…, NSF,m'PUCCH,1-1m'=0no intra-slot frequency hopping0,1intra-slot frequency hopping

where  is given by Table 6.4.1.3.1.1-1,  by clause 9.2.1 of [5, TS 38.213], and the sequence  is given by clause 5.2.2. NSF,m'PUCCH,1MRBPUCCH,1ru,vα,δ(n)

Intra-slot frequency hopping shall be assumed when the higher-layer parameter intraSlotFrequencyHopping is enabled, regardless of whether the frequency-hop distance is zero or not, otherwise no intra-slot frequency hopping shall be assumed.

The orthogonal sequence  is given by Table 6.3.2.4.1.-2 with the same index  as used in clause 6.3.2.4.1.

Table 6.4.1.3.1.1-1: Number of DM-RS symbols and the corresponding .

## 6.4.1.3.1.2Mapping to physical resources

The sequence shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with  to resource elements  in a slot on antenna port  according tok,lp,μ

ak,l(p,μ)=βPUCCH,1zml=0,2,4,…

where  corresponds to the first OFDM symbol of the PUCCH transmission and  shall be within the resource blocks assigned for PUCCH transmission according to [5, TS 38.213]. l=0k,lp,μ

For interlaced transmission, the mapping operation shall be repeated for each resource block in the interlace and in the active bandwidth part over the assigned physical resource blocks according to clause 9.2.1 of [5, TS 38.213], with the resource-block dependent sequence generated according to clause 6.3.2.2.

## 6.4.1.3.2Demodulation reference signal for PUCCH format 2

## 6.4.1.3.2.1Sequence generation

The reference-signal sequence  shall be generated according tozlm

zlmNSFPUCCH,2+i=wnirlmrlm=121-2c2m+j121-2c2m+1i=0,1,…,NSFPUCCH,2-1m=0,1,…

where the pseudo-random sequence  is defined in clause 5.2. The pseudo-random sequence generator shall be initialized with

cinit=217Nsymbslotns,fμ+l+12NID0+1+2NID0 mod 231

where  is the OFDM symbol number within the slot,  is the slot number within the radio frame, and  and  are defind in clause 6.3.2.5.2A.ns,fμwniNSFPUCCH,2

The quantity  is given by the higher-layer parameter scramblingID0 in the DMRS-UplinkConfig IE if provided and by  otherwise. If a UE is configured with both dmrs-UplinkForPUSCH-MappingTypeA and dmrs-UplinkForPUSCH-MappingTypeB, scramblingID0 is obtained from dmrs-UplinkForPUSCH-MappingTypeB.NID0∈0,1,…,65535NIDcell

## 6.4.1.3.2.2Mapping to physical resources

The sequence shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with  to resource elements  in a slot on antenna port  according toβPUCCH,2zl0k,lp,μ

ak,lp,μ=βPUCCH,2zl(m)k=3m+1

where  is defined relative to subcarrier 0 of common resource block 0 and  shall be within the resource blocks assigned for PUCCH transmission according to clause 9.2.1 of [5, TS 38.213]. k,lp,μ

## 6.4.1.3.3Demodulation reference signal for PUCCH formats 3 and 4

## 6.4.1.3.3.1Sequence generation

The reference-signal sequence  shall be generated according torlm

where  is given by clause 6.3.2.6.3 and  depends on the configuration:MscPUCCH,sru,vα,δ(m)

-if the higher-layer parameter dmrs-UplinkTransformPrecodingPUCCH is configured, and -BPSK is used for PUCCH,  is given by clause 5.2.3 with  and  given by clause 6.4.1.3.2.1. The sequence group  and the sequence number  depend on the sequence hopping in clause 6.3.2.2.1.π2ru,vα,δ(m)δ=0cinituv

-otherwise, for PUCCH format 3, PUCCH format 4 with =1, and PUCCH format 4 with >1 when -BPSK is not used for PUCCH,  is given by clause 6.3.2.2 and the cyclic shift  varies with the symbol number and slot number according to clause 6.3.2.2.2 with MRBPUCCH,4MRBPUCCH,4π2ru,vα,δ(m)α

- for PUCCH format 3 without interlaced mapping;m0=0

- obtained from Table 6.4.1.3.3.1-1 with the orthogonal sequence index  given by clause 6.3.2.6.3 for PUCCH format 3 with interlaced mapping and PUCCH format 4. m0n

Table 6.4.1.3.3.1-1: Cyclic shift index  for PUCCH format 3 with interlaced mapping and PUCCH format 4.m0

## 6.4.1.3.3.2Mapping to physical resources

The sequence shall be multiplied with the amplitude scaling factor , , in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with  to resource elements  on antenna port  according tok,lp,μ

where

- is defined relative to subcarrier 0 of the lowest-numbered resource block assigned for PUCCH transmission,

- is given by Table 6.4.1.3.3.2-1 for the case with and without intra-slot frequency hopping and with and without additional DM-RS as described in clause 9.2.1 of [TS 38.213], where  corresponds to the first OFDM symbol of the PUCCH transmission.

The resource elements  shall be within the resource blocks assigned for PUCCH transmission according to clause 9.2.1 of [5, TS 38.213]. k,lp,μ

Table 6.4.1.3.3.2-1: DM-RS positions for PUCCH format 3 and 4.

## 6.4.1.4Sounding reference signal

## 6.4.1.4.1SRS resource

An SRS resource is configured by the SRS-Resource IE or the SRS-PosResource IE and consists of

- antenna ports , where the number of antenna ports is given by the higher-layer parameter nrofSRS-Ports or nrofSRS-Ports-n8 if configured, otherwise , and  when the SRS resource is in a SRS resource set with higher-layer parameter usage in SRS-ResourceSet not set to 'nonCodebook', or determined according to [6, TS 38.214] when the SRS resource is in a SRS resource set with higher-layer parameter usage in SRS-ResourceSet set to 'nonCodebook'.NapSRS∈1,2,4,8pii=0NapSRS-1NapSRS=1pi=1000+i

-, the number of hops for SRS Tx hopping for an SRS resource configured by SRS-PosResource and given by the higher-layer parameter numberOfHops if configured, otherwise .NhopNhop=1

- consecutive OFDM symbols given by the field nrofSymbols contained in the higher-layer parameter resourceMapping. If ,  is the number of consecutive OFDM symbol per hop.NsymbSRS∈1,2,4,8,10,12,14Nhop>1NsymbSRS

-, the starting position in the time domain given by  where the offset  counts symbols backwards from the end of the slot and is given by the field startPosition contained in the higher-layer parameter resourceMapping and . If   is the starting position of each hop in the time domain, determined by the field startPosition for each SRS transmission hop.l0l0=Nsymbslot-1-loffsetloffset∈0,1,…,13loffset≥NsymbSRS-1Nhop>1l0

-, the frequency-domain starting position of the sounding reference signal.k0

## 6.4.1.4.2Sequence generation

The sounding reference signal sequence for an SRS resource, or if numberOfHops for SRS-PosResource is provided, for a given hop within an SRS resource, shall be generated according to

r(pi)n,l'=wTDM(pi)l'ru,v(αi,δ)n

0≤n≤Msc,bSRS-1

l'∈0,1,…,NsymbSRS-1

where  is given by clause 6.4.1.4.3,  is given by clause 5.2.2 with  and the transmission comb number  is contained in the higher-layer parameter transmissionComb. The quantity  is the OFDM symbol number within the SRS resource.Msc,bSRSru,vα,δ(n)δ=log2KTCKTC∈2,4,8l'∈0,1,…,NsymbSRS-1

The quantity  is given bywTDMpil'

-if the higher-layer parameter nrofSRS-Ports-n8 equals ports8tdm

wTDMpil'=1if l'∈0,2,…,NsymbSRS-2 and pi∈{1000, 1001, 1004, 1005}1if l'∈1,3,…,NsymbSRS-1 and pi∈{1002, 1003, 1006, 1007}0otherwise

-otherwise

wTDMpil'=1

The cyclic shift  for antenna port  is given as αipi

αi=2πnSRScs,inSRScs,max+fcshnf, ns,fμ,l'KnSRScs,max

where

nSRScs,i=nSRScs+nSRScs,maxpi-10004NapSRS/4 mod nSRScs,maxif NapSRS=8 and nSRScs,max=6nSRScs+nSRScs,maxpi-10002NapSRS2 mod nSRScs,maxif NapSRS=4 and nSRScs,max=6; or if NapSRS=8 and nSRScs,max=12nSRScs+nSRScs,maxpi-1000NapSRS mod nSRScs,maxotherwise

where  is contained in the higher layer parameter transmissionComb. The maximum number of cyclic shifts  is given by Table 6.4.1.4.2-1.nSRScs∈0,1,…,nSRScs,max-1nSRScs,max

The quantities  and  are given bypiNapSRS

-if the higher-layer parameter nrofSRS-Ports-n8 equals ports8tdm

pi=1000+pi mod 2if pi-1000<4 1000+pi mod 2+2if pi-1000≥4NapSRS=4

-otherwise

pi=piNapSRS=NapSRS

The quantity  is given byfcshnf ,ns,fμ,l'

-if the higher-layer parameter cyclicShiftHopping is not configured:

fcshnf,ns,fμ,l'=0

-if the higher-layer parameter cyclicShiftHopping is configured:

fcshnf ,ns,fμ,l'= scshSRSm=07c8nf mod 128Nslotframe,μNsymbslot+ns,fμNsymbslot+l0+l'+m2mmod ncshSRS

where  and is the th entry and the cardinality of the set scshSRSnncshSRS (n+1)

Scsh={scshSRS0, scshSRS1, …,scshSRSncshSRS-1}

respectively, where  is given by the higher-layer parameter hoppingSubset in the cyclicShiftHopping IE if configured, otherwise . The higher-layer parameter hoppingSubset in the cyclicShiftHopping  IE includes a bitmap of  bits with  non-zero bits, where if the th non-zero bit is the :th bit in the bitmap, then .ScshScsh={0, 1,…,KnSRScs,max-1}nSRScs,max1<ncshSRS<nSRScs,max(n+1)tscshSRSn=t-1

The pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame for which , where the cyclic-shift hopping identity  is contained in the higher-layer parameter cyclicShiftHopping.cicinit=nIDhopnf mod 128=0nIDhop

If the higher-layer parameter hoppingFinerGranularity is configured, , otherwise .K=2K=1

The sequence group  and the sequence number  in clause 5.2.2 depends on the higher-layer parameter groupOrSequenceHopping in the SRS-Resource IE or the SRS-PosResource IE. The SRS sequence identity  is given by the higher layer parameter sequenceId in the SRS-Resource IE. u=fghns,fμ,l'+nIDSRSmod 30vnIDSRS∈0, 1, …, 65535

-if groupOrSequenceHopping equals 'neither', neither group, nor sequence hopping shall be used and

-if groupOrSequenceHopping equals 'groupHopping', group hopping but not sequence hopping shall be used and

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame.cicinit=nIDSRS

-if groupOrSequenceHopping equals 'sequenceHopping', sequence hopping but not group hopping shall be used and

where the pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame. cicinit=nIDSRS

Table 6.4.1.4.2-1: Maximum number of cyclic shifts  as a function of .nSRScs,maxKTC

## 6.4.1.4.3Mapping to physical resources

Throughout this clause, when the higher layer parameter numberOfHops is provided for SRS-PosResource, the sounding reference signal sequence definitions applies to a given hop.

When SRS is transmitted on a given SRS resource, the sequence  for each OFDM symbol  and for each of the antenna ports of the SRS resource shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with  to resource elements  in a slot for each of the antenna ports  according torpi(n,l')l'

aKTCk'+k0pi,  l'+l0(pi)=1NapSRSβSRSrpi(k',l')if k'=0, 1, …, Msc,bSRS-1 and l'=0,1,…,NsymbSRS-10otherwise

where

-for an SRS resource in an SRS resource set with the higher-layer parameter fourPortSRS-3Tx is configured, NapSRS=NapSRS-1

-otherwise, NapSRS=NapSRS

The length of the sounding reference signal sequence is given by

Msc,bSRS=mSRS,bNscRBKTCPF

where  is given by a selected row of Table 6.4.1.4.3-1 with  where  is given by the field b-SRS contained in the higher-layer parameter freqHopping if configured, otherwise . The row of the table is selected according to the index  given by the field c-SRS contained in the higher-layer parameter freqHopping. The quantity   is given by the higher-layer parameter FreqScalingFactor if configured, otherwise . When FreqScalingFactor is configured, the UE expects the length of the SRS sequence to be a multiple of 6.mSRS,bBSRS=0PF∈2, 4PF=1

The frequency-domain starting position  is defined byk0(pi)

k0(pi)=k0(pi)+noffsetFH+noffsetRPFS+noffset2FH

where

k0pi=nshiftNscRB+kTCpi+koffsetl'+fcohnf,ns,fμ,l'' mod KTC

andkTCpi=kTC+3KTC4 mod KTCif NapSRS=8, pi∈1003, 1007, and nSRScs,max=6kTC+KTC2 mod KTCif NapSRS=8, pi∈1002, 1006, and nSRScs,max=6kTC+KTC4 mod KTCif NapSRS=8, pi∈1001, 1005, and nSRScs,max=6kTC+KTC2 mod KTCif NapSRS=8, pi∈1001, 1003, 1005, 1007, and nSRScs,max=12kTC+KTC2 mod KTCif NapSRS=8, pi∈1001, 1003, 1005, 1007, nSRScs,max=8, and nSRScs≥nSRScs,max2kTC+KTC2 mod KTCif NapSRS=4, pi∈1001, 1003, and nSRScs,max=6 kTC+KTC2 mod KTC if NapSRS=4, pi∈1001, 1003,  nSRScs,max∈8, 12,and nSRScs≥nSRScs,max2kTCotherwise

noffsetFH=b=0BSRSmSRS,bNscRBnb

noffsetRPFS=NscRBmSRS,BSRSkF+khopmod PFPF

noffset2FH=ninithop+nSRSTxHopping mod Nhop-ninithopmSRS,0-moverlaphopNscRB

and

- is given by the higher-layer parameter StartRBIndex if configured, otherwise ; kF∈0,1,…,PF-1kF=0

- is given by Table 6.4.1.4.3-3 withkhop

khop=nSRSb'=bhopBSRSNb' mod PFNbhop=1

if the higher-layer parameter enableStartRBHopping is configured, otherwise .khop=0

- is given by the higher-layer parameter overlapValue in TxHoppingConfig.moverlaphop∈0,1,2,4

- is the hop transmission counter in the time domain, where  corresponds to the hop with starting symbol and slot offset configured by resourceMapping and resourceType in SRS-PosResource,  corresponds to the order of the higher-layer parameter SlotOffsetForRemainingHops in slotOffsetForRemainingHopsList, wherein the UE expects to be configured with the starting slot offset and starting symbol of the  hops in an ascending order sequentially in time domain.nSRSTxHopping=0,1,…,Nhop-1nSRSTxHopping=0nSRSTxHopping=1,2,…,Nhop-1 Nhop

- is the initial hop index.ninithop=nshiftmSRS,0-moverlaphop

The quantity  is given byfcohnf,ns,fμ,l''

-if the higher-layer parameter combOffsetHopping is not configured:

fcohnf, ns,fμ,l''=0

-if the higher-layer parameter combOffsetHopping is configured:

fcohnf ,ns,fμ,l''= scohSRSm=07c8nf mod 128Nslotframe,μNsymbslot+ns,fμNsymbslot+l0+l''+m2mmod ncohSRS

where  and is the th entry and the cardinality of the set scohSRSnncohSRS n+1

Scoh={scohSRS0, scohSRS1, …,scohSRSncohSRS-1}

respectively, where  is given by the higher-layer parameter hoppingSubset in the combOffsetHopping IE if configured, otherwise . The higher-layer parameter hoppingSubset in the combOffsetHopping IE includes a bitmap of  bits with  non-zero bits, where if the th non-zero bit is the :th bit in the bitmap, then .ScohScoh={0, 1,…,KTC-1}KTC1<ncohSRS<KTC(n+1)tscohSRSn=t-1

The pseudo-random sequence  is defined by clause 5.2.1 and shall be initialized with  at the beginning of each radio frame for which , where the comb offset hopping identity  is contained in the higher-layer parameter combOffsetHopping.cicinit=nIDhopnf mod 128=0nIDhop

If the higher-layer parameter hoppingWithRepetition is set to repetition, , otherwise .l''=l'RRl''=l'

If numberOfHops is configured:

-The reference point for  is the lowest subcarrier of the configured bandwidth for SRS with Tx hopping configured by the parameter bwp in SRS-PosTx-Hopping.k0(pi)=0

otherwise:

-If  the reference point for  is subcarrier 0 in common resource block 0, otherwise the reference point is the lowest subcarrier of the BWP. NBWPstart≤nshiftk0(pi)=0

If the SRS is configured by the IE SRS-PosResource, the quantity  is given by Table 6.4.1.4.3-2, otherwise .koffsetl'koffsetl'=0

The frequency domain shift value  adjusts the SRS allocation with respect to the reference point grid and is contained in the higher-layer parameter freqDomainShift in the SRS-Resource IE or the SRS-PosResource IE. The transmission comb offset  is contained in the higher-layer parameter transmissionComb in the SRS-Resource IE or the SRS-PosResource IE and  is a frequency position index.nshiftkTC∈0,1,…,KTC-1nb

Frequency hopping of the sounding reference signal is configured by the parameter , given by the field b-hop contained in the higher-layer parameter freqHopping if configured, otherwise .bhop∈0,1,2,3bhop=0

If , frequency hopping is disabled and the frequency position index  remains constant (unless re-configured) and is defined bybhop≥BSRSnb

for all  OFDM symbols of the SRS resource. The quantity  is given by the higher-layer parameter freqDomainPosition if configured, otherwise , and the values of  and  for  are given by the selected row of Table 6.4.1.4.3-1 corresponding to the configured value of .NsymbSRSnRRC=0mSRS,bNbb=BSRS

If , frequency hopping is enabled and the frequency position indices  are defined bybhop<BSRSnb

nb=4nRRCmSRS,b mod Nbb≤bhopFbnSRS+4nRRCmSRS,b mod Nbotherwise

where  is given by Table 6.4.1.4.3-1,Nb

and where  regardless of the value of . The quantity  counts the number of SRS transmissions. For the case of an SRS resource configured as aperiodic by the higher-layer parameter resourceType, it is given by  within the slot in which the  symbol SRS resource is transmitted. The quantity  is given by  if the higher-layer parameter nrofSRS-Ports-n8 equals ‘ports8tdm’, otherwise . The quantity  is the repetition factor given by the field repetitionFactor if configured, otherwise .Nbhop=1NbnSRSnSRS=l'sRNsymbSRSss=2s=1R≤NsymbSRSsR=NsymbSRS

For the case of an SRS resource configured as periodic or semi-persistent by the higher-layer parameter resourceType, the SRS counter is given by

nSRS=Nslotframe,μnf+ns,fμ-ToffsetTSRSNsymbSRSsR+l'sR

for slots that satisfy . The periodicity  in slots and slot offset  are given in clause 6.4.1.4.4.

Table 6.4.1.4.3-1: SRS bandwidth configuration.

Table 6.4.1.4.3-2: The offset  for SRS as a function of  and .koffsetl'KTCl'

Table 6.4.1.4.3-3: The quantity  as a function of .khopkhop

## 6.4.1.4.4Sounding reference signal slot configuration

Throughout this clause, when the higher layer parameter numberOfHops is provided for SRS-PosResource, the sounding reference signal slot configuration applies to a given hop.

For an SRS resource configured as periodic or semi-persistent by the higher-layer parameter resourceType, a periodicity  (in slots) and slot offset  are configured according to the higher-layer parameter periodicityAndOffset-p or periodicityAndOffset-sp in the SRS-Resource IE, or periodicityAndOffset-p or periodicityAndOffset-sp in the SRS-PosResource IE. Candidate slots in which the configured SRS resource may be used for SRS transmission are the slots satisfying

Nslotframe,μnf+ns,fμ-Toffset mod TSRS=0

and, if the higher-layer parameter srs-PosPeriodicConfigHyperSFN-Index is configured for a periodicity larger than or equal to   slots, also2μ∙10240

nHFN+NSRSHFN mod 2=0

where  is given by the higher-layer parameter srs-PosPeriodicConfigHyperSFN-Index and  is the hyper-frame number.NSRSHFN∈0,1nHFN

SRS is transmitted as described in clause 6.2.1 of [6, TS 38.214].

## 7Downlink

## 7.1Overview

## 7.1.1Overview of physical channels

A downlink physical channel corresponds to a set of resource elements carrying information originating from higher layers. The following downlink physical channels are defined:

-Physical Downlink Shared Channel, PDSCH

-Physical Broadcast Channel, PBCH

-Physical Downlink Control Channel, PDCCH.

## 7.1.2Overview of physical signals

A downlink physical signal corresponds to a set of resource elements used by the physical layer but does not carry information originating from higher layers.

The following downlink physical signals are defined:

-Demodulation reference signals, DM-RS

-Phase-tracking reference signals, PT-RS

-Positioning reference signal, PRS

-Channel-state information reference signal, CSI-RS

-Primary synchronization signal, PSS

-Secondary synchronization signal, SSS

-Wake-up signal, WUS

-Low-power synchronization signal, LPSS

## 7.2Physical resources

The frame structure and physical resources the UE shall assume when receiving downlink transmissions are defined in Clause 4.

The following antenna ports are defined for the downlink:

-Antenna ports starting with 1000 for PDSCH

-Antenna ports starting with 2000 for PDCCH

-Antenna ports starting with 3000 for channel-state information reference signals

-Antenna ports starting with 4000 for SS/PBCH block transmission

-Antenna ports starting with 5000 for positioning reference signals

The UE shall not assume that two antenna ports are quasi co-located with respect to any QCL type unless specified otherwise.

For DM-RS associated with a PDSCH, the channel over which a PDSCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within the same resource as the scheduled PDSCH, in the same slot, and in the same PRG as described in clause 5.1.2.3 of [6, TS 38.214].

For DM-RS associated with a PDCCH, the channel over which a PDCCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within resources for which the UE may assume the same precoding being used as described in clause 7.3.2.2.

For DM-RS associated with a PBCH, the channel over which a PBCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within a SS/PBCH block transmitted within the same slot, and with the same block index according to clause 7.4.3.1.

## 7.3Physical channels

## 7.3.1Physical downlink shared channel

## 7.3.1.1Scrambling

Up to two codewords  can be transmitted. In case of single-codeword transmission, .

For each codeword , the UE shall assume the block of bits , where  is the number of bits in codeword  transmitted on the physical channel, are scrambled prior to modulation, resulting in a block of scrambled bits according tobq0, …, bq(Mbitq-1)Mbit(q)bq0, …, bq(Mbitq-1)

b(q)i=b(q)i+c(q)(i) mod 2

where the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized withcq(i)

cinit=nRNTI⋅215+q⋅214+nID

where

- equals the higher-layer parameter dataScramblingIdentityPDSCH if configured and the RNTI equals the C-RNTI, MCS-C-RNTI, or CS-RNTI, and the transmission is not scheduled using DCI format 1_0 in a common search space;

- equals the higher-layer parameter dataScramblingIdentityPDSCH in pdsch-ConfigMulticast if configured in a common MBS frequency resource for multicast and the RNTI equals the G-RNTI or the G-CS-RNTI;nID∈0,1,…,1023

- equals the higher-layer parameter dataScramblingIdentityPDSCH in pdsch-ConfigMCCH or pdsch-ConfigMTCH if configured in a common MBS frequency resource for broadcast and the RNTI equals the MCCH-RNTI or G-RNTI, respectively;nID∈0,1,…,1023

- equalsnID∈0,1,…,1023

-the higher-layer parameter dataScramblingIdentityPDSCH if the codeword is scheduled using a CORESET with CORESETPoolIndex equal to 0;

-the higher-layer parameter dataScramblingIdentityPDSCH2 if the codeword is scheduled using a CORESET with CORESETPoolIndex equal to 1;

if the higher-layer parameters dataScramblingIdentityPDSCH and dataScramblingIdentityPDSCH2 are configured together with the higher-layer parameter CORESETPoolIndex containing two different values, and the RNTI equals the C-RNTI, MCS-C-RNTI, or CS-RNTI, and the transmission is not scheduled using DCI format 1_0 in a common search space;

- otherwisenID=NIDcell

and where  corresponds to the RNTI associated with the PDSCH transmission as described in clause 5.1 of [6, TS 38.214].

## 7.3.1.2Modulation

For each codeword , the UE shall assume the block of scrambled bits  are modulated as described in clause 5.1 using one of the modulation schemes in Table 7.3.1.2-1, resulting in a block of complex-valued modulation symbols . qbq0, …, bq(Mbitq-1)dq0,…,dq(Msymbq-1)

Table 7.3.1.2-1: Supported modulation schemes.

## 7.3.1.3Layer mapping

The UE shall assume that complex-valued modulation symbols for each of the codewords to be transmitted are mapped onto one or several layers according to Table 7.3.1.3-1. Complex-valued modulation symbols  for codeword  shall be mapped onto the layers ,  where  is the number of layers and  is the number of modulation symbols per layer.dq0,…,dq(Msymbq-1)qxi=x0(i)…xυ-1(i)Ti=0,1,…,Msymblayer-1υMsymblayer

Table 7.3.1.3-1: Codeword-to-layer mapping for spatial multiplexing.

## 7.3.1.4Antenna port mapping

The block of vectors ,  shall be mapped to antenna ports according tox0(i)…xυ-1(i)Ti=0,1,…,Msymblayer-1

where , . The set of antenna ports  shall be determined according to the procedure in [4, TS 38.212]. i=0,1,…,Msymbap-1Msymbap=Msymblayer

## 7.3.1.5Mapping to virtual resource blocks

The UE shall, for each of the antenna ports used for transmission of the physical channel, assume the block of complex-valued symbols  conform to the downlink power allocation specified in [6, TS 38.214] and are mapped in sequence starting with  to resource elements  in the virtual resource blocks assigned for transmission which meet all of the following criteria: yp0, …, yp(Msymbap-1)yp0k',lp,μ

-they are in the virtual resource blocks assigned for transmission;

-the corresponding physical resource blocks are declared as available for PDSCH according to clause 5.1.4 of [6, TS 38.214];

-the corresponding resource elements in the corresponding physical resource blocks are

-not used for transmission of the associated DM-RS or DM-RS intended for other co-scheduled UEs as described in clause 7.4.1.1.2;

-not used for non-zero-power CSI-RS, which is according to clause 7.4.1.5 and not configured by the TRS-ResourceSet IE, if the corresponding physical resource blocks are for a PDSCH scheduled by a PDCCH with the CRC scrambled by C-RNTI, MCS-C-RNTI, CS-RNTI, G-RNTI for multicast, G-CS-RNTI, or a PDSCH with SPS, except if the non-zero-power CSI-RS is a CSI-RS configured by the higher-layer parameter CSI-RS-Resource-Mobility in the MeasObjectNR IE or except if the non-zero-power CSI-RS is an aperiodic non-zero-power CSI-RS resource;

-not used for PT-RS according to clause 7.4.1.2;

-not declared as 'not available for PDSCH according to clause 5.1.4 of [6, TS 38.214];

-not the assigned PRBs that are in the active DL BWP and outside the DL sub-band(s) in SBFD symbols [6, TS38.214].

The mapping to resource elements  allocated for PDSCH according to [6, TS 38.214] and not reserved for other purposes shall be in increasing order of first the index  over the assigned virtual resource blocks, where  is the first subcarrier in the lowest-numbered virtual resource block assigned for transmission, and then the index . (k',l)p,μk'k'=0l

## 7.3.1.6Mapping from virtual to physical resource blocks

The UE shall assume the virtual resource blocks are mapped to physical resource blocks according to the indicated mapping scheme, non-interleaved or interleaved mapping. If no mapping scheme is indicated, the UE shall assume non-interleaved mapping.

For non-interleaved VRB-to-PRB mapping, virtual resource block  is mapped to physical resource block , except for PDSCH transmissions scheduled with DCI format 1_0 in a common search space in which case virtual resource block  is mapped to physical resource block  where  is the lowest-numbered physical resource block in the control resource set where the corresponding DCI was received. When two PDCCH candidates from two linked common search space sets as indicated by the higher-layer parameter searchSpaceLinking are detected, and the two linked common search space sets are associated with different control resource sets, the control resource set with the lowest number among the two linked control resource sets is used to determine .nnnn+NstartCORESETNstartCORESETNstartCORESET

For interleaved VRB-to-PRB mapping, the mapping process is defined by:

-Resource block bundles are defined as

-for PDSCH transmissions scheduled with DCI format 1_0 with the CRC scrambled by SI-RNTI in Type0-PDCCH common search space in CORESET 0, the set of  resource blocks in CORESET 0 are divided into  resource-block bundles in increasing order of the resource-block number and bundle number where  is the bundle size and  is the size of CORESET 0.NBWP,initsizeNbundle=NBWP,initsizeLL=2NBWP,initsize

-resource block bundle  consists of  resource blocks if  and  resource blocks otherwise,Nbundle-1NBWP,initsize mod LNBWP,initsize mod L>0L

-all other resource block bundles consists of  resource blocks.L

-for PDSCH transmissions scheduled with DCI format 1_0 in any common search space in bandwidth part  with starting position , other than Type0-PDCCH common search space in CORESET 0, the set of  virtual resource blocks , where  is the size of CORESET 0 if CORESET 0 is configured for the cell and the size of initial downlink bandwidth part if CORESET 0 is not configured for the cell, are divided into  virtual resource-block bundles in increasing order of the virtual resource-block number and virtual bundle number and the set of  physical resource blocks  are divided into  physical resource-block bundles in increasing order of the physical resource-block number and physical bundle number, where ,  is the bundle size, and  is the lowest-numbered physical resource block in the control resource set where the corresponding DCI was received. When two PDCCH candidates from two linked search space sets as indicated by the higher-layer parameter searchSpaceLinking are detected, and the two linked search space sets are associated with different control resource sets, the control resource set with the lowest number among the two linked control resource sets is used to determine .iNBWP,istartNBWP,initsize0,1,…,NBWP,initsize-1NBWP,initsizeNbundleNBWP,initsizeNstartCORESET, NstartCORESET+1,…,NstartCORESET+NBWP,initsize-1NbundleNbundle=NBWP,initsize+NBWP,istart+NstartCORESET mod LLL=2NstartCORESETNstartCORESET

-resource block bundle 0 consists of  resource blocks,L-NBWP,istart+NstartCORESET mod L

-resource block bundle  consists of  resource blocks if  and  resource blocks otherwise,Nbundle-1NBWP,initsize+NBWP,istart+NstartCORESET mod LNBWP,initsize+NBWP,istart+NstartCORESET mod L>0L

-all other resource block bundles consists of  resource blocks.L

-for all other PDSCH transmissions, the set of  resource blocks in bandwidth part  with starting position  are divided into  resource-block bundles in increasing order of the resource-block number and bundle number where  is the bundle size for bandwidth part  provided by the higher-layer parameter vrb-ToPRB-Interleaver for DCI formats 1_0, 1_1, and 1_3 in a UE-specific search space, or vrb-ToPRB-InterleaverDCI-1-2 for DCI format 1_2, andNBWP,isizeNBWP,istartNbundle=NBWP,isize+NBWP,istart mod LiLi

-resource block bundle 0 consists of  resource blocks,

-resource block bundle  consists of  resource blocks if  and  resource blocks otherwise,

-all other resource block bundles consists of  resource blocks.

-Virtual resource blocks in the interval  are mapped to physical resource blocks according to

-virtual resource block bundle  is mapped to physical resource block bundle

-virtual resource block bundle  is mapped to physical resource block bundle  where

-The UE is not expected to be configured with  simultaneously with a PRG size of 4 as defined in [6, TS 38.214]Li=2

The UE may assume that the same precoding in the frequency domain is used within a PRB bundle and the bundle size is determined by clause 5.1.2.3 in [6, TS 38.214]. The UE shall not make any assumption that the same precoding is used for different bundles of common resource blocks.

For PDSCH transmissions scheduled by DCI format 4_1 or 4_2, and using G-RNTI or G-CS-RNTI, the quantities  and   in this clause are replaced by  and , respectively, and  is the bundle size for the common MBS frequency resource provided by the higher-layer parameter vrb-ToPRB-Interleaver in pdsch-ConfigMulticast.NBWP,istartNBWP,isizeNMBS,istartNMBS,isizeLi

For PDSCH transmissions scheduled by DCI format 4_0, and using G-RNTI for broadcast, MCCH-RNTI, or Multicast-MCCH-RNTI, the quantities  and   in this clause are replaced by  and , respectively, and .NBWP,istartNBWP,isizeNMBS,istartNMBS,isizeLi=2

## 7.3.2Physical downlink control channel (PDCCH)

## 7.3.2.1Control-channel element (CCE)

A physical downlink control channel consists of one or more control-channel elements (CCEs) as indicated in Table 7.3.2.1-1.

Table 7.3.2.1-1: Supported PDCCH aggregation levels.

## 7.3.2.2Control-resource set (CORESET)

A control-resource set consists of  resource blocks in the frequency domain and  symbols in the time domain.NRBCORESETNsymbCORESET∈1,2,3

A control-channel element consists of 6 resource-element groups (REGs) where a resource-element group equals one resource block during one OFDM symbol. Resource-element groups within a control-resource set are numbered in increasing order in a time-first manner, starting with 0 for the first OFDM symbol and the lowest-numbered resource block in the control resource set.

A UE can be configured with multiple control-resource sets. Each control-resource set is associated with one CCE-to-REG mapping only.

The CCE-to-REG mapping for a control-resource set can be interleaved or non-interleaved and is described by REG bundles:

-REG bundle  is defined as REGs  where  is the REG bundle size, , and  is the number of REGs in the CORESETiiL, iL+1, …, iL+L-1Li=0,1,…,NREGCORESETL-1NREGCORESET=NRBCORESETNsymbCORESET

-CCE  consists of REG bundles  where  is an interleaverf6jL, f6jL+1, …, f(6jL+6L-1)f(∙)

For non-interleaved CCE-to-REG mapping,  and .L=6fx=x

For interleaved CCE-to-REG mapping,  for  and  for . The interleaver is defined by L∈2,6NsymbCORESET=1L∈NsymbCORESET,6NsymbCORESET∈2,3

fx=rC+c+nshift mod NREGCORESETLx=cR+rr=0,1,…,R-1c=0,1,…,C-1C=NREGCORESET(LR)

where .R∈2, 3, 6

The UE is not expected to handle configurations resulting in the quantity  not being an integer.C

For a CORESET configured by the ControlResourceSet IE:

- is given by the higher-layer parameter frequencyDomainResources;NRBCORESET

- is given by the higher-layer parameter duration, where  is supported only if the higher-layer parameter dmrs-TypeA-Position equals 'pos3';NsymbCORESETNsymbCORESET=3

-interleaved or non-interleaved mapping is given by the higher-layer parameter cce-REG-MappingType;

- equals 6 for non-interleaved mapping and is given by the higher-layer parameter reg-BundleSize for interleaved mapping;L

- is given by the higher-layer parameter interleaverSize;R

- is given by the higher-layer parameter shiftIndex if provided, otherwise ;nshift∈0,1,…,274nshift=NIDcell

-for both interleaved and non-interleaved mapping:

-if the higher-layer parameter precoderGranularity equals sameAsREG-bundle the UE may assume the same precoding being used within a REG bundle

-if the higher-layer parameter precoderGranularity equals allContiguousRBs,

-the UE may assume the same precoding being used across the all resource-element groups within the set of contiguous resource blocks in the CORESET;

-the UE may assume that no resource elements in the CORESET overlap with an SSB;

-if the UE is not provided with the higher-layer parameter pdcch-CandidateReceptionWithCRS-Overlap, the UE may assume that no resource elements in the CORESET overlap with LTE cell-specific reference signals as indicated by the higher-layer parameter lte-CRS-ToMatchAround, lte-CRS-PatternList1, lte-CRS-PatternList2, lte-CRS-PatternList3, or lte-CRS-PatternList4.

For CORESET 0 configured by the ControlResourceSetZero IE:

- and  are defined by clause 13 of [5, TS 38.213];NRBCORESETNsymbCORESET

-the UE may assume interleaved mapping;

-;L=6

-;R=2

-;nshift=NIDcell

-the UE may assume normal cyclic prefix when CORESET 0 is configured by MIB or SIB1;

-the UE may assume the same precoding being used within a REG bundle.

For CORESET 0 on a carrier where the SS/PBCH block is detected at sync raster points defined in Tables 5.4.3.1-2 or 5.4.3.1-3 of [14, TS 38.101-1] or Table 5.4.3.1-2 of [16, TS 38.101-5], and configured by the ControlResourceSetZero IE:

- and  are defined by Table 13-0 in clause 13 of [5, TS 38.213];NRBCORESETNsymbCORESET

-if  on a carrier with a channel bandwidth of 3 MHz, the CORESET is obtained by applying the description above assuming interleaved mapping with ;NRBCORESET=12R=2

-if  on a carrier with a channel bandwidth of 3 MHz, the CORESET is obtained by applying the description above assuming interleaved mapping with  or non-interleaved mapping as defined by clause 13 of [5, TS 38.213], followed by puncturing the 9 highest-numbered resource blocks to obtain the 15 resource blocks forming CORESET 0;NRBCORESET=24R=2

-if  on a carrier with a channel bandwidth of 5 MHz, the CORESET is obtained by applying the description above assuming interleaved mapping with , followed by puncturing the 4 highest-numbered resource blocks to obtain the 20 resource blocks forming CORESET 0;NRBCORESET=24R=2

-;L=6

-;nshift=NIDcell

-the UE may assume normal cyclic prefix when CORESET 0 is configured by MIB or SIB1;

-the UE may assume the same precoding being used within a REG bundle.

## 7.3.2.3Scrambling

The UE shall assume the block of bits , where  is the number of bits transmitted on the physical channel, is scrambled prior to modulation, resulting in a block of scrambled bits  according tob0, …, b(Mbit-1)Mbitb0, …, b(Mbit-1)

bi=bi+c(i) mod 2

where the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with

where

-for a UE-specific search space as defined in clause 10 of [5, TS 38.213],  equals the higher-layer parameter pdcch-DMRS-ScramblingID if configured;

-for a PDCCH with the CRC scrambled by G-RNTI, G-CS-RNTI, MCCH-RNTI, or Multicast-MCCH-RNTI in a common search space as defined in clause 10 of [5, TS 38.213],  equals the higher-layer parameter pdcch-DMRS-ScramblingID if configured in a common MBS frequency resource;nID∈0,1,…,65535

- otherwisenID=NIDcell

and where

- is given by the C-RNTI for a PDCCH in a UE-specific search space if the higher-layer parameter pdcch-DMRS-ScramblingID is configured, and

- otherwise.

## 7.3.2.4PDCCH modulation

The UE shall assume the block of bits  to be QPSK modulated as described in clause 5.1.3, resulting in a block of complex-valued modulation symbols .b0,…,bMbit-1d0,…,d(Msymb-1)

## 7.3.2.5Mapping to physical resources

The UE shall assume the block of complex-valued symbols  to be scaled by a factor  and mapped to resource elements  used for the monitored PDCCH and not used for the associated PDCCH DMRS in increasing order of first , then . The antenna port .d0,…,d(Msymb-1)k,lp,μ

## 7.3.3Physical broadcast channel

## 7.3.3.1Scrambling

The UE shall assume the block of bits, where  is the number of bits transmitted on the physical broadcast channel, are scrambled prior to modulation, resulting in a block of scrambled bits  according to b0, …, b(Mbit-1) b0, …, b(Mbit-1)

bi=bi+c(i+vMbit) mod 2

where the scrambling sequence  is given by clause 5.2. The scrambling sequence shall be initialized with  at the start of each SS/PBCH block wherecinit=NIDcell

-for ,  is the two least significant bits of the candidate SS/PBCH block indexLmax=4v

-for ,  is the three least significant bits of the candidate SS/PBCH block indexLmax>4v

with  being the maximum number of candidate SS/PBCH blocks in a half frame, as described in [5, TS 38.213].Lmax

## 7.3.3.2Modulation

The UE shall assume the block of bits  are QPSK modulated as described in clause 5.1.3, resulting in a block of complex-valued modulation symbols .  b0, …, b(Mbit-1)dPBCH0,…,dPBCH(Msymb-1)

## 7.3.3.3Mapping to physical resources

Mapping to physical resources is described in clause 7.4.3.

## 7.4Physical signals

## 7.4.1Reference signals

## 7.4.1.1Demodulation reference signals for PDSCH

## 7.4.1.1.1Sequence generation

The UE shall assume the sequence  is defined byrn

.

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialized withci

cinit=217Nsymbslotns,fμ+l+12NIDnSCIDλ+1+217λ2+2NIDnSCIDλ+nSCIDλmod 231

where  is the OFDM symbol number within the slot,   is the slot number within a frame, andlns,fμ

- are given by the higher-layer parameters scramblingID0 and scramblingID1, respectively, in the DMRS-DownlinkConfig IE if provided and the PDSCH is scheduled by PDCCH using DCI format 1_1, 1_2, or 1_3 with the CRC scrambled by C-RNTI, MCS-C-RNTI, or CS-RNTI;NID0,NID1∈0,1,…,65535

- is given by the higher-layer parameter scramblingID0 in the DMRS-DownlinkConfig IE if provided and the PDSCH is scheduled by PDCCH using DCI format 1_0 with the CRC scrambled by C-RNTI, MCS-C-RNTI, or CS-RNTI;NID0∈0,1,…,65535

- are given by the higher-layer parameters scramblingID0 and scramblingID1, respectively, in the DMRS-DownlinkConfig IE in pdsch-ConfigMulticast if provided in a common MBS frequency resource for multicast and the PDSCH is scheduled by PDCCH using DCI format 4_2 with the CRC scrambled by G-RNTI or G-CS-RNTI;NID0,NID1∈0,1,…,65535

- is given by the higher-layer parameter scramblingID0 in the DMRS-DownlinkConfig IE in pdsch-ConfigMulticast if provided in a common MBS frequency resource for multicast and the PDSCH is scheduled by PDCCH using DCI format 4_1 with the CRC scrambled by G-RNTI or G-CS-RNTI;NID0∈0,1,…,65535

- is given by the higher-layer parameter scramblingID0 in pdsch-ConfigMCCH or pdsch-ConfigMTCH if provided in a common MBS frequency resource for broadcast and the PDSCH is scheduled by PDCCH with the CRC scrambled by MCCH-RNTI or G-RNTI, respectively;NID0∈0,1,…,65535

- otherwise; NIDnSCIDλ=NIDcell

- given bynSCIDλ and λ are

-if the higher-layer parameter dmrs-Downlink in the DMRS-DownlinkConfig IE is provided

nSCIDλ=nSCIDλ=0 or λ=21-nSCIDλ=1

λ=λ

where λ is the CDM group defined in clause 7.4.1.1.2.

-otherwise by

nSCIDλ=nSCID

λ=0

The quantity  is given by the DM-RS sequence initialization field, if present, in the DCI associated with the PDSCH transmission if DCI format 1_1, 1_2, 1_3, or 4_2 in [4, TS 38.212] is used, otherwise .nSCID∈0, 1nSCID=0

## 7.4.1.1.2Mapping to physical resources

The UE shall assume the PDSCH DM-RS being mapped to physical resources according to configuration type 1 or configuration type 2 as given by the higher-layer parameter dmrs-Type.

The UE shall assume the sequence  is scaled by a factor  to conform with the transmission power specified in [6, TS 38.214] and mapped to resource elements  according toβPDSCHDMRSk,lp,μ

-if the higher-layer parameter dmrs-TypeEnh is configured and the PDSCH is not scheduled by DCI format 1_0, 4_0, or 4_1

ak,lpj,μ=βPDSCHDMRSwfk'wtl'r4n+k'k=8n+2k'+Δconfiguration type 112n+k'+Δconfiguration type 2, k'=0,112n+k'+Δ+4configuration type 2, k'=2,3k'=0,1,2,3l=l+l'n=0,1,…j=0,1,…,υ-1

-otherwise

ak,lpj,μ=βPDSCHDMRSwfk'wtl'r2n+k'k=4n+2k'+Δconfiguration type 16n+k'+Δconfiguration type 2k'=0,1l=l+l'n=0,1,…j=0,1,…,υ-1

where , , and  are given by Tables 7.4.1.1.2-1 and 7.4.1.1.2-2 and the following conditions are fulfilled:Δ

-the resource elements are within the common resource blocks allocated for PDSCH transmission

The reference point for  is k

-subcarrier 0 of the lowest-numbered resource block in CORESET 0 if the corresponding PDCCH is associated with CORESET 0 and Type0-PDCCH common search space and is addressed to SI-RNTI;

-otherwise, subcarrier 0 in common resource block 0

The reference point for  and the position  of the first DM-RS symbol depends on the mapping type:

-for PDSCH mapping type A:

- is defined relative to the start of the slot

-if the higher-layer parameter dmrs-TypeA-Position is equal to 'pos3' and  otherwise

-for PDSCH mapping type B:

- is defined relative to the start of the scheduled PDSCH resources

-

The position(s) of the DM-RS symbols is given by  and duration  whereld

-for PDSCH mapping type A,  is the duration between the first OFDM symbol of the slot and the last OFDM symbol of the scheduled PDSCH resources in the slot ld

-for PDSCH mapping type B,  is the duration of the scheduled PDSCH resourcesld

and according to Tables 7.4.1.1.2-3 and 7.4.1.1.2-4.

For PDSCH mapping type A

-the case dmrs-AdditionalPosition equals to 'pos3' is only supported when dmrs-TypeA-Position is equal to 'pos2';

- and  symbols in Tables 7.4.1.1.2-3 and 7.4.1.1.2-4 respectively is only applicable when dmrs-TypeA-Position is equal to 'pos2';ld=3ld=4

-single-symbol DM-RS,  except if all of the following conditions are fulfilled in which case :l1=11l1=12

-the higher-layer parameter lte-CRS-ToMatchAround, lte-CRS-PatternList1, lte-CRS-PatternList2, lte-CRS-PatternList3, or lte-CRS-PatternList4 is configured; and

-the higher-layer parameter dmrs-AdditionalPosition is equal to 'pos1' and ; andl0=3

-the UE has indicated it is capable of additionalDMRS-DL-Alt

For PDSCH mapping type B

-if the PDSCH duration   OFDM symbols for normal cyclic prefix or  OFDM symbols for extended cyclic prefix, and the front-loaded DM-RS of the PDSCH allocation collides with resources reserved for a search space set associated with a CORESET,  shall be incremented such that the first DM-RS symbol occurs immediately after the CORESET and until no collision with any CORESET occurs, andld∈2,3,4,5,6,7,8,9,10,11,12,13ld∈2,4,6

-if the PDSCH duration  is 2 symbols, the UE is not expected to receive a DM-RS symbol beyond the second symbol;ld

-if the PDSCH duration  is 5 symbols and if one additional single-symbol DMRS is configured, the UE only expects the additional DM-RS to be transmitted on the 5th symbol when the front-loaded DM-RS symbol is in the 1st symbol of the PDSCH duration, otherwise the UE should expect that the additional DM-RS is not transmitted;ld

-if the PDSCH duration  is 7 symbols for normal cyclic prefix or 6 symbols for extended cyclic prefix: ld

-if one additional single-symbol DM-RS is configured, the UE only expects the additional DM-RS to be transmitted on the 5th or 6th symbol when the front-loaded DM-RS symbol is in the 1st or 2nd symbol, respectively, of the PDSCH duration, otherwise the UE should expect that the additional DM-RS is not transmitted;

-if the PDSCH duration   OFDM symbols, the UE is not expected to receive the front-loaded DM-RS beyond the 4th symbol;ld∈5,6,7,8,9,10,11,12,13

-if the PDSCH duration  is 12 or 13 symbols, the UE is not expected to receive DM-RS mapped to symbol 12 or later in the slot;ld

-for all values of the PDSCH duration  other than 2, 5, and 7 symbols, the UE is not expected to receive DM-RS beyond the :th symbol;ld(ld-1)

-if the PDSCH duration  is less than or equal to 4 OFDM symbols, only single-symbol DM-RS is supported. ld

-if the higher-layer parameter lte-CRS-ToMatchAround, lte-CRS-PatternList1, lte-CRS-PatternList2, lte-CRS-PatternList3, or lte-CRS-PatternList4 is configured, the PDSCH duration  symbols for normal cyclic prefix, the subcarrier spacing configuration , single-symbol DM-RS is configured, and at least one PDSCH DM-RS symbol in the PDSCH allocation collides with a symbol containing resource elements as indicated by the higher-layer parameter lte-CRS-ToMatchAround, lte-CRS-PatternList1, lte-CRS-PatternList2, lte-CRS-PatternList3, or lte-CRS-PatternList4, then  shall be incremented by one in all slots.ld=10μ=0l

The time-domain index  and the supported antenna ports  are given by Table 7.4.1.1.2-5 where l'p

-single-symbol DM-RS is used if the higher-layer parameter maxLength in the DMRS-DownlinkConfig IE is not configured;

-single-symbol or double-symbol DM-RS is determined by the associated DCI if the higher-layer parameter maxLength in the DMRS-DownlinkConfig IE is equal to 'len2';

-basic or enhanced DM-RS multiplexing is controlled by the higher-layer parameter dmrs-TypeEnh.

In absence of CSI-RS configuration, and unless otherwise configured, the UE may assume PDSCH DM-RS and SS/PBCH block to be quasi co-located with respect to Doppler shift, Doppler spread, average delay, delay spread, and, when applicable, spatial Rx parameters. Unless specified otherwise, the UE may assume that the PDSCH DM-RS within the same CDM group are quasi co-located with respect to Doppler shift, Doppler spread, average delay, delay spread, and spatial Rx (when applicable). The UE may assume that DMRS ports associated with a TCI state as described in clause 5.1.6.2 of [6, TS 38.214] of a PDSCH are QCL with QCL Type A, Type D (when applicable) and average gain.

The UE may assume that no DM-RS collides with the SS/PBCH block.

Table 7.4.1.1.2-1: Parameters for PDSCH DM-RS configuration type 1.

Table 7.4.1.1.2-2: Parameters for PDSCH DM-RS configuration type 2.

Table 7.4.1.1.2-3: PDSCH DM-RS positions  for single-symbol DM-RS.

Table 7.4.1.1.2-4: PDSCH DM-RS positions  for double-symbol DM-RS.

Table 7.4.1.1.2-5: PDSCH DM-RS time index  and antenna ports .l'p

## 7.4.1.2Phase-tracking reference signals for PDSCH

## 7.4.1.2.1Sequence generation

The phase-tracking reference signal for subcarrier  is given byk

-If the higher-layer parameter dmrs-TypeEnh is configured

rk=r4m+k'

-otherwise

rk=r2m+k'

where  is the demodulation reference signal given by clause 7.4.1.1.2 at position  and subcarrier .r∙l0k

## 7.4.1.2.2Mapping to physical resources

The UE shall assume phase-tracking reference signals being present only in the resource blocks used for the PDSCH, and only if the procedure in [6, TS 38.214] indicates phase-tracking reference signals being used.

If present, the UE shall assume the PDSCH PT-RS is scaled by a factor  to conform with the transmission power specified in clause 4.1 of [6, TS 38.214] and mapped to resource elements according toβPT-RSk,lp,μ

ak,l(p,μ)=βPT-RSrk

when all the following conditions are fulfilled

- is within the OFDM symbols allocated for the PDSCH transmissionl

-resource element    is not used for DM-RS, non-zero-power CSI-RS (except for those configured for mobility measurements or with resourceType in corresponding CSI-ResourceConfig configured as 'aperiodic'), zero-power CSI-RS, SS/PBCH block, a detected PDCCH according to clause 5.1.4.1 of [6, TS38.214], or is declared as 'not available' by clause 5.1.4 of [6, TS 38.214]k,lp,μ

The set of time indices  defined relative to the start of the PDSCH allocation is defined byl

1.set  and i=0lref=0

2.if any symbol in the interval  overlaps with a symbol used for DM-RS according to clause 7.4.1.1.2maxlref+i-1LPT-RS+1,lref,…,lref+iLPT-RS

-set i=1

-set  to the symbol index of the DM-RS symbol in case of a single-symbol DM-RS and to the symbol index of the second DM-RS symbol in case of a double-symbol DM-RSlref

-repeat from step 2 as long as  is inside the PDSCH allocationlref+iLPT-RS

3.add  to the set of time indices for PT-RSlref+iLPT-RS

4.increment  by one

5.repeat from step 2 above as long as  is inside the PDSCH allocationlref+iLPT-RS

where .LPT-RS∈1,2,4

For the purpose of PT-RS mapping, the resource blocks allocated for PDSCH transmission are numbered from 0 to  from the lowest scheduled resource block to the highest. The corresponding subcarriers in this set of resource blocks are numbered in increasing order starting from the lowest frequency from 0 to . The subcarriers to which the UE shall assume the PT-RS is mapped are given by

where

-i=0,1,2,…

- is given by Table 7.4.1.2.2-1 for the DM-RS port associated with the PT-RS port according to clause 5.1.6.3 in [6, TS 38.214]. If the higher-layer parameter resourceElementOffset in the PTRS-DownlinkConfig IE is not configured, the column corresponding to 'offset00' shall be used.

- is the RNTI associated with the DCI scheduling the transmission

- is the number of resource blocks scheduled

- is given by [6, TS 38.214].KPT-RS∈2,4

Table 7.4.1.2.2-1: The parameter .

## 7.4.1.3Demodulation reference signals for PDCCH

## 7.4.1.3.1Sequence generation

The UE shall assume the reference-signal sequence  for OFDM symbol  is defined byrlml

.

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialized withci

cinit=217Nsymbslotns,fμ+l+12NID+1+2NIDmod231

where  is the OFDM symbol number within the slot,  is the slot number within a frame, andlns,fμ

- is given by the higher-layer parameter pdcch-DMRS-ScramblingID if provided;NID∈0,1,…,65535

- is given by the higher-layer parameter pdcch-DMRS-ScramblingID if configured for a common search space in a common MBS frequency resource;NID∈0,1,…,65535

- otherwise.NID=NIDcell

## 7.4.1.3.2Mapping to physical resources

The UE shall assume the sequence  is mapped to resource elements  according torlmk,lp,μ

where the following conditions are fulfilled

-they are within the resource element groups constituting the PDCCH the UE attempts to decode if the higher-layer parameter precoderGranularity equals sameAsREG-bundle,

-all resource-element groups within the set of contiguous resource blocks in the CORESET where the UE attempts to decode the PDCCH if the higher-layer parameter precoderGranularity equals allContiguousRBs.

The reference point for  is k

-subcarrier 0 of the lowest-numbered resource block in the CORESET if the CORESET is configured by the PBCH or by the controlResourceSetZero field in the PDCCH-ConfigCommon IE  or by the controlResourceSetZero field in the OD-SIB1-Config,

-subcarrier 0 in common resource block 0 otherwise

The quantity  is the OFDM symbol number within the slot.l

The antenna port .p=2000

A UE not attempting to detect a PDCCH in a CORESET shall not make any assumptions on the presence or absence of DM-RS in the CORESET.

In absence of CSI-RS configuration, and unless otherwise configured, the UE may assume PDCCH DM-RS and SS/PBCH block to be quasi co-located with respect to Doppler shift, Doppler spread, average delay, delay spread, and, when applicable, spatial Rx parameters.

## 7.4.1.4Demodulation reference signals for PBCH

## 7.4.1.4.1Sequence generation

The UE shall assume the reference-signal sequence  for an SS/PBCH block is defined by

where  is given by clause 5.2. The scrambling sequence generator shall be initialized at the start of each SS/PBCH block occasion with

where

-for ,  where  is the number of the half-frame in which the PBCH is transmitted in a frame with  for the first half-frame in the frame and  for the second half-frame in the frame, and  is the two least significant bits of the candidate SS/PBCH block index as defined in [5, TS 38.213]Lmax=4

-for ,  where  is the three least significant bits of the candidate SS/PBCH block index as defined in [5, TS 38.213]Lmax>4

with  being the maximum number of candidate SS/PBCH blocks in a half frame, as described in [5, TS 38.213]. Lmax

## 7.4.1.4.2Mapping to physical resources

Mapping to physical resources is described in clause 7.4.3.

## 7.4.1.5CSI reference signals

## 7.4.1.5.1General

Zero-power (ZP) and non-zero-power (NZP) CSI-RS are defined

-for a non-zero-power CSI-RS configured by the NZP-CSI-RS-Resource IE or by the CSI-RS-Resource-Mobility field in the CSI-RS-ResourceConfigMobility IE or by the TRS-ResourceSet IE, the sequence shall be generated according to clause 7.4.1.5.2 and mapped to resource elements according to clause 7.4.1.5.3

-for a zero-power CSI-RS configured by the ZP-CSI-RS-Resource IE, the UE shall assume that the resource elements defined in clause 7.4.1.5.3 are not used for PDSCH transmission subject to clause 5.1.4.2 of [6, TS 38.214]. The UE performs the same measurement/reception on channels/signals except PDSCH regardless of whether they collide with ZP CSI-RS or not.

## 7.4.1.5.2Sequence generation

The UE shall assume the reference-signal sequence  is defined by

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialised with

cinit=210Nsymbslotns,fμ+l+12nID+1+nIDmod231

at the start of each OFDM symbol where  is the slot number within a radio frame,  is the OFDM symbol number within a slot, and  equals the higher-layer parameter scramblingID or sequenceGenerationConfig.ns,fμ

## 7.4.1.5.3Mapping to physical resources

For each CSI-RS resource configured, the UE shall assume the sequence  being mapped to resources elements  according to r(m)k,lp,μ

ak,lp,μ=βCSIRSwfkq'wtlq'rl,ns,fm'm'=nα+kq'+kqρNscRBk=nNscRB+kq+kq'l=lq+lq'α=ρfor N=12ρfor N>1n=0,1,…

when the following conditions are fulfilled:

-the resource element  is within the resource blocks occupied by the CSI-RS resource for which the UE is configuredk,lp,μ

The reference point for  is subcarrier 0 in common resource block 0.k=0

The value of  is given by the higher-layer parameter density in the CSI-RS-ResourceMapping IE or the CSI-RS-CellMobility IE.ρ

The number of ports  per CSI-RS resource is given by the higher-layer parameter nrofPorts and the number of CSI-RS resources by the total number of CSI-RS ports NNtot

-if , there is one CSI-RS resource with  CSI-RS ports, , and ;Ntot∈1, 2, 4, 8, 12, 16, 24, 32Nq=0Ntot=N

-if , the aggregated resource for the  ports is formed by aggregating  CSI-RS resources with  CSI-RS ports each, where the possible combinations of , , and  are given by Table 7.4.1.5.3-6, and where  is the CSI-RS resource index within the aggregated CSI-RS resource.Ntot∈48, 64, 128Ntot=KNKNNtotKNq=0,…,K-1

For NZP CSI-RS configured by the TRS-ResourceSet IE, the density  and number of ports .ρ=3N=1

The UE is not expected to receive CSI-RS and DM-RS on the same resource elements.

The UE shall assume  for a non-zero-power CSI-RS where  is selected such that the power offset specified by the higher-layer parameter powerControlOffsetSS in the NZP-CSI-RS-Resource IE or in the TRS-ResourceSet IE, if provided, is fulfilled.

The quantities , , , and  are given by Tables 7.4.1.5.3-1 to 7.4.1.5.3-5 where each  in a given row of Table 7.4.1.5.3-1 corresponds to a CDM group of size 1 (no CDM) or size 2, 4, or 8. The CDM type is provided by the higher layer parameter cdm-Type in the CSI-RS-ResourceMapping IE. For NZP CSI-RS configured by the TRS-ResourceSet IE, the CDM type is 'noCDM'. The indices  and  index resource elements within a CDM group.k'l'wf(k')wt(l')k,lk'l'

The time-domain locations  and  are provided by the higher-layer parameters firstOFDMSymbolInTimeDomain and firstOFDMSymbolInTimeDomain2, respectively, in the CSI-RS-ResourceMapping IE or the CSI-RS-ResourceConfigMobility IE and defined relative to the start of a slot. For NZP CSI-RS configured by TRS-ResourceSet IE, the time-domain location  is provided by the higher-layer parameter firstOFDMSymbolInTimeDomain or firstOFDMSymbolInTimeDomain+4.l0∈0,1, …, 13l1∈2, 3, …, 12l0∈0,1, …, 13

The frequency-domain location is given by a bitmap provided by the higher-layer parameter frequencyDomainAllocation in the CSI-RS-ResourceMapping IE, the CSI-RS-ResourceConfigMobility IE, or the TRS-ResourceSet IE, with the bitmap and value of  in Table 7.4.1.5.3-1 given byki

-,  for row 1 of Table 7.4.1.5.3-1ki-1=fi

-,  for row 2 of Table 7.4.1.5.3-1ki-1=fi

-,  for row 4 of Table 7.4.1.5.3-1ki-1=4fi

-,  for all other caseski-1=2fi

where  is the bit number of the  bit in the bitmap set to one, repeated across every  of the resource blocks configured for CSI-RS reception by the UE. The starting position and number of the resource blocks in which the UE shall assume that CSI-RS is transmitted are given by the higher-layer parameters freqBand and density in the CSI-RS-ResourceMapping IE for the bandwidth part given by the higher-layer parameter BWP-Id in the CSI-ResourceConfig IE or given by the higher-layer parameters nrofPRBs in the CSI-RS-CellMobility IE where the the startPRB given by csi-rs-MeasurementBW is relative to common resource block 0. For NZP CSI-RS configured by TRS-ResourceSet IE, the starting position and number of the resource blocks in which the CSI-RS can be transmitted are given by the higher-layer parameters nrofRBs, and startingRB in the TRS-ResourceSet IE, where startingRB is relative to common resource block 0 and the density .fiith1ρρ=3

The UE shall assume that a CSI-RS is transmitted using antenna ports  numbered according top

p=3000+p'

where

-if the number of CSI-RS ports  Ntot∈1, 2, 4, 8, 12, 16, 24, 32

p'=p

-if the number of CSI-RS ports Ntot∈48, 64, 128

-if the higher-layer parameter portMappingMethod equals ‘method1’ and  is an integer where  is as defined in Table 5.2.2.2.1a-1 of [6, TS 38.214]N1KN1

p' = p+qN/20≤p<N/2p+K+q-1N/2N/2≤p<N

where  is the number of the CSI-RS resource within the aggregated CSI-RS resource.q=0,1,…,K-1

-if the higher-layer parameter portMappingMethod equals ‘method2’

p'=N2pN2'+qN2' + p mod N2'

N2'=N2K

where  is the number of the CSI-RS resource within the aggregated CSI-RS resource,  is an integer, and  is as defined in Table 5.2.2.2.1a-1 of [6, TS 38.214].q=0,1,…,K-1N2KN2

where

p=s+jL j=0,1,…,NL-1s=0,1,…,L-1

and where   is the sequence index provided by Tables 7.4.1.5.3-2 to 7.4.1.5.3-5,  is the CDM group size, and  is the number of CSI-RS ports. The CDM group index  given in Table 7.4.1.5.3-1 corresponds to the time/frequency locations  for a given row of the table. The CDM groups are numbered in order of increasing frequency domain allocation first and then increasing time domain allocation. sL∈1, 2, 4, 8Njk,l

For a CSI-RS resource configured as periodic or semi-persistent by the higher-layer parameter resourceType, configured by the higher-layer parameter CSI-RS-CellMobility, or configured by the higher-layer parameter TRS-ResourceSet, the UE shall assume that the CSI-RS is transmitted in slots satisfying

Nslotframe,μnf+ns,fμ-Toffset mod TCSI-RS=0

where the periodicity  (in slots) and slot offset  are obtained from the higher-layer parameter CSI-ResourcePeriodicityAndOffset, slotConfig, periodicityAndOffset. The UE shall assume that CSI-RS is transmitted in a candidate slot as described in clause 11.1 of [5, TS 38.213], clause 10.4B of [5, TS 38.213]. TCSI-RSToffset

The UE may assume that antenna ports within a CSI-RS resource are quasi co-located with QCL Type A, Type D (when applicable), and average gain.

Table 7.4.1.5.3-1: CSI-RS locations within a slot.

Table 7.4.1.5.3-2: The sequences  and  for cdm-Type equal to 'noCDM'.wf(k')wt(l')

Table 7.4.1.5.3-3: The sequences  and  for cdm-Type equal to 'fd-CDM2'.wf(k')wt(l')

Table 7.4.1.5.3-4: The sequences  and  for cdm-Type equal to 'cdm4-FD2-TD2'.wf(k')wt(l')

Table 7.4.1.5.3-5: The sequences  and  for cdm-Type equal to 'cdm8-FD2-TD4'.wf(k')wt(l')

Table 7.4.1.5.3-6: The supported combinations of , , and  when the number of CSI-RS ports is 48, 64, or 128.NtotKN

## 7.4.1.6RIM reference signals

## 7.4.1.6.1General

RIM-RS can be used by an gNB to measure inter-cell interference and to provide information about the experienced interference to other gNBs. Up to two different types of RIM-RS can be configured where

-the first RIM-RS type can be used to convey information,

-the second RIM-RS type depends on configuration only.

## 7.4.1.6.2Sequence generation

The RIM-RS receiver shall assume the reference-signal sequence  is defined byrm

rm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialised with  cm

cinit=210fntRIM+nSCID mod 231

where

- is given by clause 7.4.1.6.4.4; nSCID∈0,1,…,210-1

- where the pseudo-random sequence  is given by clause 5.2.1,  initialized with  where the multiplier factor  and the offset ;fntRIM=i=0202iciciciniti=γntRIM+δ mod 231γ∈0,1,…,231-1δ∈0,1,…,231-1

- is the number of RIM-RS transmission periods since  where ntRIM=tRSRIM-trefRIMTperRIMtrefRIM

- is the time in seconds relative to  of 00:00:00 on 1 January 1900, calculated as continuous time without leap second and traceable to a common time reference, andtRSRIM-trefRIMtrefRIM

- is the RIM-RS transmission periodicity in seconds assuming that the first RIM-RS transmission period starts at , and where   is given by clause 7.4.1.6.4.2.TperRIM=NslotPt1000⋅2μtrefRIMNslotPt

## 7.4.1.6.3Mapping to physical resources

The RIM-RS receiver shall assume the reference signal being mapped to physical resources according to

ak(p,RIM)=βRIMrk

k=0,1,…,LRIM-1

where   is an amplitude scaling factor in order to control the RIM-RS transmission power and  is the antenna port. Baseband signal generation shall be done according to clause 5.3.3.βRIMp

The starting position  for RIM-RS type  in slot  in a frame is given byl0i∈1,2ns,fμ

l0=ToffsetUD,RIM mod Nsymbslot

in slots satisfying

1024Nslotframe,μnfRIM+Nslotframe,μnfRIM+ns,fμ-Toffset+ToffsetUD,RIMNsymbslot mod NslotPt=0

where

- counts the number of times the SFN periods within the RIM-RS transmission period;nfRIM∈0,1,…,NslotPt1024Nslotframe,μ-1

- where  is the symbol offset of the reference point after the starting boundary of the uplink-downlink switching period in which the RIM-RS is mapped to and  is obtained as described in clause 7.4.1.6.4.2;ToffsetUD,RIM=NrefUD,RIM-Nsymb,refRIM,iNrefUD,RIM∈2,3,…,20⋅2⋅14-1Nsymb,refRIM, i

- is the total number of slots in a RIM-RS transmission period as defined in clause 7.4.1.6.4.2;NslotPt

- is the slot offset of the uplink-downlink switching period with index  with respect to the starting boundary of the RIM-RS transmission period and is defined in clause 7.4.1.6.4.2;ToffsetitRIM

- is the RIM-RS transmission periodicity in units of uplink-downlink switching period as defined in clause 7.4.1.6.4.2. Pt

## 7.4.1.6.4RIM-RS configuration

## 7.4.1.6.4.1General

A resource for RIM-RS transmission is defined by the indices , , and  used as indices into configured lists of time, frequency, and sequence parameters, respectively.itRIM∈0,1,…,Pt-1ifRIM∈0,1,…,NfRIM-1isRIM∈0,1,…,NsRIM,i-1

All RIM-RS resources occupy the same number of resource blocks, . At most 32 RIM-RS resources can be configured within a 10 ms period.NRBRIM

## 7.4.1.6.4.2Time-domain parameters and mapping from  to time-domain parametersit

RIM-RS are transmitted periodically with the RIM-RS transmission period  defined in units of the uplink-downlink switching period determined from one or two configured uplink-downlink periods. Pt

-If a single uplink-downlink period is configured for RIM-RS purposes,

- is the RIM-RS transmission periodicity in terms of uplink-downlink switching periods given byPt

Pt=2μPtTper,1RIM1024Nslotframe,μ1024Nslotframe,μ2μTper,1RIM

where  ms;Tper,1RIM∈0.5,0.625,1,1.25, 2, 2.5,4, 5,10,20

- is the total number of slots in a RIM-RS transmission period;NslotPt=2μPtTper,1RIM

- is the slot offset of the uplink-downlink switching period with index  with respect to the starting boundary of the RIM-RS transmission period Toffset=2μitRIMTper,1RIMitRIM

-If two uplink-downlink periods are configured for RIM-RS purposes,

- is the RIM-RS transmission periodicity in terms of  pairs of uplink-downlink switching periods and is given byPtPt2

Pt=2μPtTper,1RIM+Tper,2RIM21024Nslotframe,μ1024Nslotframe,μ2μTper,1RIM+Tper,2RIM2

where each pair consists of a first period of  ms and a second period of  ms and where  divides 20 ms;Tper,1RIM∈0.5,0.625,1,1.25, 2, 2.5, 3,4, 5,10,20Tper,2RIM∈0.5,0.625,1,1.25, 2, 2.5, 3,4, 5,10Tper,1RIM+Tper,2RIM

- is the total number of slots in a RIM-RS transmission period;NslotPt=2μPtTper,1RIM+Tper,2RIM2

- is the slot offset of the uplink-downlink switching period with index  with respect to the starting boundary of the RIM-RS transmission period Toffset=2μitRIM2Tper,1RIM+Tper,2RIM+2μitRIM mod 2Tper,1RIMitRIM

The intermediate quantity  is given byPt

Pt=NsetIDRIM,1NfRIMNsRIM,1R1+NsetIDRIM,2NfRIMNsRIM,2R2if EnoughIndication is disabled2NsetIDRIM,1NfRIMNsRIM,1R1+NsetIDRIM,2NfRIMNsRIM,2R2if EnoughIndication is enabled

where

- and  are the total number of setIDs for RIM-RS type 1 and RIM-RS type 2, respectively;NsetIDRIM,1NsetIDRIM,2

- is the number of candidate frequency resources configured in the network;NfRIM∈1,2,4

- is the number of candidate sequences assigned for RIM-RS type  in the network;NsRIM,i∈1,2,…,8i∈1,2

- and  are the number of consecutive uplink-downlink switching periods for RIM-RS type 1 and RIM-RS type 2, respectively. If near-far functionality is not configured, , otherwise  and the first and second half of the  consecutive uplink-downlink switching periods are for near functionality and far functionality, respectively.R1R2Ri∈1,2,4Ri∈2,4,8Ri

The quantity  is obtained from entry  in a list of configured symbol offsets for RIM-RS .Nsymb,refRIM, iri

## 7.4.1.6.4.3Frequency-domain parameters and mapping from  to frequency-domain parametersif

The frequency-domain parameter  in clause 5.3.3 is the frequency offset relative to a configured reference point for RIM-RS and is obtained from entry  in a list of configured frequency offsets expressed in units of resource blocks. k1ifRIM

The number of candidate frequency resources configured in the network, , shall fulfilNfRIM

NfRIM≤Ngridsize,μNRBsc⋅2μ⋅1540⋅103+Ngridsize,μNRBsc⋅2μ⋅1580⋅103+1

If , the frequency difference between any pair of configured frequency offsets in the list is not smaller than . NfRIM>1NRBRIM

The number of resource blocks for RIM-RS is given by

NRBRIM=min96,Ngrid,DLsize,μfor  μ=0NRBRIM∈min48,Ngrid,DLsize,μ, min96,Ngrid,DLsize,μfor  μ=1

## 7.4.1.6.4.4Sequence parameters and mapping from  to sequence parametersis

The scrambling identity  clause 7.4.1.6.2 is obtained from entry  in a list of configured scrambling identities.nSCIDisRIM

## 7.4.1.6.4.5Mapping between resource triplet and set ID

The resource indices , , and  are determined from the index  in the set ID  according toitRIMifRIMisRIMrnsetID

itRIM=Tstart+nsetIDNsRIM mod NtRIMRi+rifRIM=nsetIDNtRIMNsRIM mod NfRIMisRIM=Sstart+nsetID mod NsRIM

where

- is given byNtRIM

NtRIM=NsetIDRIM,1NfRIMNsRIM,1for RIM-RS type 1 and if EnoughIndication is disabled2NsetIDRIM,1NfRIMNsRIM,1for RIM-RS type 1 and if EnoughIndication is enabled   NsetIDRIM,2NfRIMNsRIM,2for RIM-RS type 2

- is the number of candidate frequency resources configured in the network;NfRIM∈1,2,4

- is the number of sequence candidates for the current RIM-RS resource given byNsRIM

NsRIM=NsRIM,1for RIM-RS type 1 and if EnoughIndication is disabledNsRIM,12for RIM-RS type 1 and if EnoughIndication is enabled   NsRIM,2for RIM-RS type 2

- is the starting time offset given byTstart

Tstart=0for RIM-RS type 1NsetIDRIM,1NfRIMNsRIM,1R1for RIM-RS type 2 and if EnoughIndication is disabled 2NsetIDRIM,1NfRIMNsRIM,1R1for RIM-RS type 2 and if EnoughIndication is enabled

- is given bySstart

Sstart=NsRIM,12if EnoughIndication is enabled and 'enough mitigation' is to be indicated 0otherwise

where  is the number of candidate sequences assigned for RIM-RS type 1NsRIM,1

- is the number of consecutive uplink-downlink periods for RIM-RS type  as given by clause 7.4.1.6.4.2;Rii

-.r∈0,1,…,Ri-1

The set ID is determined from the resource triplet according to

nsetID=isRIM-Sstart+NsRIMitRIM-TstartRi+NtRIMNsRIMifRIM

## 7.4.1.7Positioning reference signals

## 7.4.1.7.1General

A positioning frequency layer consists of one or more downlink PRS resource sets, each of which consists of one or more downlink PRS resources as described in [6, TS 38.214].

## 7.4.1.7.2Sequence generation

The UE shall assume the reference-signal sequence  is defined byrm

rm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialised withci

cinit=222nID,seqPRS1024+210Nsymbslotns,fμ+l+12nID,seqPRS mod 1024+1+nID,seqPRS mod 1024 mod 231

where  is the slot number, the downlink PRS sequence ID  is given by the higher-layer parameter dl-PRS-SequenceID, and  is the OFDM symbol within the slot to which the sequence is mapped.ns,fμnID,seqPRS∈0,1,…,4095l

## 7.4.1.7.3Mapping to physical resources in a downlink PRS resource

For each downlink PRS resource configured, the UE shall assume the sequence  is scaled with a factor  and mapped to resources elements  according to rmβPRSk,lp,μ

ak,lp,μ=βPRS rmm=0, 1, …k=mKcombPRS+koffsetPRS+k' mod KcombPRSl=lstartPRS, lstartPRS+1, …, lstartPRS+LPRS-1

when the following conditions are fulfilled:

-the resource element  is within the resource blocks occupied by the downlink PRS resource for which the UE is configured;k,lp,μ

-the symbol  is not used by any SS/PBCH block used by a serving cell for downlink PRS transmitted from the same serving cell or any SS/PBCH block from a non-serving cell whose time frequency location is provided to the UE by higher layers for downlink PRS transmitted from the same non-serving cell;l

-the slot number satisfies the conditions in clause 7.4.1.7.4.

and where

-the antenna port p=5000

- is the first symbol of the downlink PRS within a slot and given by the higher-layer parameter dl-PRS-ResourceSymbolOffset;lstartPRS

-the size of the downlink PRS resource in the time domain  is given by the higher-layer parameter dl-PRS-NumSymbols;LPRS∈1, 2,4,6,12

-the comb size  is given by the higher-layer parameter dl-PRS-CombSizeN-AndReOffset for a downlink PRS resource configured for RTT-based propagation delay compensation, otherwise by the higher-layer parameter dl-PRS-CombSizeN such that the combination  is one of {1, 2}, {2, 2},{4, 2}, {6, 2}, {12, 2}, {1, 4}, {4, 4}, {12, 4}, {1, 6}, {6, 6}, {12, 6}, {1, 12} and {12, 12};KcombPRS∈2, 4, 6,12LPRS,KcombPRS

-the resource-element offset  is obtained from the higher-layer parameter dl-PRS-CombSizeN-AndReOffset;koffsetPRS∈0,1,…,KcombPRS-1

-the quantity  is given by Table 7.4.1.7.3-1.k'

If the downlink PRS resource is configured for RTT based propagation delay compensation as described in clause 9 of [6, TS 38.214], the reference point for  is subcarrier 0 in common resource block 0; Otherwise, the reference point for  is the location of the point A of the positioning frequency layer, in which the downlink PRS resource is configured where point A is given by the higher-layer parameter dl-PRS-PointA.k=0k=0

Table 7.4.1.7.3-1: The frequency offset  as a function of .k'l-lstartPRS

## 7.4.1.7.4Mapping to slots in a downlink PRS resource set

For a downlink PRS resource in a downlink PRS resource set, the UE shall assume the downlink PRS resource being transmitted when the slot and frame numbers fulfil

Nslotframe,μnf+ns,fμ-ToffsetPRS-Toffset,resPRS mod TperPRS∈iTgapPRSi=0TrepPRS-1

and one of the following conditions are fulfilled:

-the higher-layer parameters dl-PRS-MutingOption1 and dl-PRS-MutingOption2 are not provided;

-the higher-layer parameter dl-PRS-MutingOption1 is provided with bitmap  but dl-PRS-MutingOption2 with bitmap  is not provided, and bit  is set;b1b2bi1

-the higher-layer parameter dl-PRS-MutingOption2 is provided with bitmap  but dl-PRS-MutingOption1 with bitmap  is not provided, and bit  is set;b2b1bi2

-the higher-layer parameters dl-PRS-MutingOption1 with bitmap  and dl-PRS-MutingOption2 with  are both provided, and both bit  and  are set.b1b2bi1bi2

where

- is bit  in the bitmap given by the higher-layer parameter dl-PRS-MutingOption1 where  is the size of the bitmap; bi1i=Nslotframe,μnf+ns,fμ-ToffsetPRS-Toffset,resPRS TmutingPRSTperPRSmod LL∈2, 4, 6, 8, 16, 32

- is bit  in the bitmap given by the higher-layer parameter dl-PRS-MutingOption2;bi2i=Nslotframe,μnf+ns,fμ-ToffsetPRS-Toffset,resPRS mod TperPRS TgapPRS mod TrepPRS

-the periodicity  and the slot offset  are given by the higher-layer parameter dl-PRS-Periodicity-and-ResourceSetSlotOffset;TperPRS∈2μ4, 5, 8, 10, 16, 20, 32, 40, 64, 80, 160, 320, 640, 1280, 2560, 5120, 10240ToffsetPRS∈0,1,…,TperPRS-1

-the downlink PRS resource slot offset  is given by the higher-layer parameter dl-PRS-ResourceSlotOffset; Toffset,resPRS

-the repetition factor  is given by the higher-layer parameter dl-PRS-ResourceRepetitionFactor;TrepPRS∈1,2,4,6,8,16,32

-the muting repetition factor  is given by the higher-layer parameter dl-PRS-MutingBitRepetitionFactor;TmutingPRS

-the time gap  is given by the higher-layer parameter dl-PRS-ResourceTimeGap;TgapPRS∈1,2,4,8,16,32

For a downlink PRS resource in a downlink PRS resource set configured for RTT-based propagation delay compensation, the UE shall assume the downlink PRS resource being transmitted as described in clause 9 of [6, TS 38.214]; otherwise, the UE shall assume the downlink PRS resource being transmitted as described in clause 5.1.6.5 of [6, TS 38.214].

## 7.4.2Synchronization signals

## 7.4.2.1Physical-layer cell identities

There are 1008 unique physical-layer cell identities given by

where  and .NID(1)∈0,1,…,335NID(2)∈0,1,2

## 7.4.2.2Primary synchronization signal

## 7.4.2.2.1Sequence generation

The sequence  for the primary synchronization signal is defined by

where

and

## 7.4.2.2.2Mapping to physical resources

Mapping to physical resources is described in clause 7.4.3.

## 7.4.2.3Secondary synchronization signal

## 7.4.2.3.1Sequence generation

The sequence  for the secondary synchronization signal is defined by

where

and

## 7.4.2.3.2Mapping to physical resources

Mapping to physical resources is described in clause 7.4.3.

## 7.4.3SS/PBCH block

## 7.4.3.1Time-frequency structure of an SS/PBCH block

In the time domain, an SS/PBCH block consists of 4 OFDM symbols, numbered in increasing order from 0 to 3 within the SS/PBCH block, where PSS, SSS, and PBCH with associated DM-RS are mapped to symbols as given by Table 7.4.3.1-1.

In the frequency domain, an SS/PBCH block consists of 240 contiguous subcarriers with the subcarriers numbered in increasing order from 0 to 239 within the SS/PBCH block. The quantities  and  represent the frequency and time indices, respectively, within one SS/PBCH block. The UE may assume that the complex-valued symbols corresponding to resource elements denoted as 'Set to 0' in Table 7.4.3.1-1 are set to zero. The quantity  in Table 7.4.3.1-1 is given by . The quantity  is the subcarrier offset from subcarrier 0 in common resource block  to the lowest-numbered subcarrier of the SS/PBCH block, or the SS/PBCH block after puncturing if applicable, where  is obtained from the higher-layer parameter offsetToPointA. klvv=NIDcell mod 4kSSBNCRBSSBNCRBSSB

-For operation with shared spectrum channel access in FR2-2 and for operation without shared spectrum channel access, the 4 least significant bits of  are given by the higher-layer parameter ssb-SubcarrierOffset and for FR1 the most significant bit of  is given by  in the PBCH payload as defined in clause 7.1.1 of [4, TS 38.212]. kSSBkSSBaA+5

-For operation with shared spectrum channel access in FR1, the 4 least significant bits of  are given by the higher-layer parameter ssb-SubcarrierOffset and the most significant bit of  is given by  in the PBCH payload as defined in clause 7.1.1 of [4, TS 38.212]. If  ,  ; otherwise, .kSSBkSSBaA+5kSSB≥24kSSB=kSSBkSSB=2kSSB2

If ssb-SubcarrierOffset is not provided,  is derived from the frequency difference between the SS/PBCH block and Point A.kSSB

The UE may assume that the complex-valued symbols corresponding to resource elements that are part of a common resource block partially or fully overlapping with an SS/PBCH block, or an SS/PBCH block after puncturing if applicable, and not used for SS/PBCH transmission are set to zero in the OFDM symbols partially or fully overlapping with OFDM symbols where SS/PBCH is transmitted.

For an SS/PBCH block, the UE shall assume

-antenna port  is used for transmission of PSS, SSS, PBCH and DM-RS for PBCH,p=4000

-the same cyclic prefix length and subcarrier spacing for the PSS, SSS, PBCH and DM-RS for PBCH,

-for SS/PBCH block type A,  and  with the quantities , and  expressed in terms of 15 kHz subcarrier spacing, andμ∈0,1kSSB∈0, 1, 2, …, 23kSSBNCRBSSB

-for SS/PBCH block type B in FR2-1 and FR2-NTN,  and  with the quantity  expressed in terms of the subcarrier spacing provided by the higher-layer parameter subCarrierSpacingCommon and  expressed in terms of 60 kHz subcarrier spacing; μ∈3,4kSSB∈0, 1, 2, …, 11kSSBNCRBSSB

-for SS/PBCH block type B in FR2-2,  and  with the quantity  expressed in terms of the SS/PBCH block subcarrier spacing and  expressed in terms of 60 kHz subcarrier spacing; μ∈3,5,6kSSB∈0,1,2,…,11kSSBNCRBSSB

-the centre of subcarrier 0 of resource block   coincides with the centre of subcarrier 0 of a common resource block with the subcarrier spacing NCRBSSB

-provided by the higher-layer parameter subCarrierSpacingCommon for operation without shared spectrum channel access in FR1, FR2-1 and FR2-NTN; and

-same as the subcarrier spacing of the SS/PBCH block for operation without shared spectrum access in FR2-2 and for operation with shared spectrum channel access.

-This common resource block overlaps with subcarrier 0 of the lowest-numbered resource block of the SS/PBCH block, or the SS/PBCH block after puncturing if applicable.

The UE may assume that SS/PBCH blocks transmitted with the same block index on the same center frequency location are quasi co-located with respect to Doppler spread, Doppler shift, average gain, average delay, delay spread, and, when applicable, spatial Rx parameters. The UE shall not assume quasi co-location for any other SS/PBCH block transmissions other than what is specified in [5, TS 38.213].

For cell search on a carrier with a channel bandwidth of 3 MHz, the UE is not expected to receive subcarriers 0 to 47 and 192 to 239 in any of the 4 OFDM symbols of the SS/PBCH block, where the remaining 12 resource blocks form the SS/PBCH block after puncturing.

Table 7.4.3.1-1: Resources within an SS/PBCH block for PSS, SSS, PBCH, and DM-RS for PBCH.

## 7.4.3.1.1Mapping of PSS within an SS/PBCH block

The UE shall assume the sequence of symbols constituting the primary synchronization signal to be scaled by a factor  to conform to the PSS power allocation specified in [5, TS 38.213] and mapped to resource elements  in increasing order of  where  and  are given by Table 7.4.3.1-1 and represent the frequency and time indices, respectively, within one SS/PBCH block.(k,l)p,μ

## 7.4.3.1.2Mapping of SSS within an SS/PBCH block

The UE shall assume the sequence of symbols  constituting the secondary synchronization signal to be scaled by a factor  and mapped to resource elements  in increasing order of  where  and  are given by Table 7.4.3.1-1 and represent the frequency and time indices, respectively, within one SS/PBCH block.(k,l)p,μ

## 7.4.3.1.3Mapping of PBCH and DM-RS within an SS/PBCH block

The UE shall assume the sequence of complex-valued symbols  constituting the physical broadcast channel to be scaled by a factor  to conform to the PBCH power allocation specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  which meet all the following criteria:dPBCH0, …,dPBCHMsymb-1 (k,l)p,μ

-they are not used for PBCH demodulation reference signals

The mapping to resource elements  not reserved for PBCH DM-RS shall be in increasing order of first the index  and then the index , where  and  represent the frequency and time indices, respectively, within one SS/PBCH block and are given by Table 7.4.3.1-1.(k,l)p,μ

The UE shall assume the sequence of complex-valued symbols  constituting the demodulation reference signals for the SS/PBCH block to be scaled by a factor of  to conform to the PBCH power allocation specified in [5, TS 38.213] and to be mapped to resource elements  in increasing order of first  and then  where  and  are given by Table 7.4.3.1-1 and represent the frequency and time indices, respectively, within one SS/PBCH block.βPBCHDM-RS(k,l)p,μ

## 7.4.3.2Time location of an SS/PBCH block

The locations in the time domain where a UE shall monitor for a possible SS/PBCH block are described in clauses 4.1, 4.4, and 11.6 of [5, TS 38.213].

## 7.4.4Wake-up signal

## 7.4.4.1Sequence generation

## 7.4.4.1.1Generation of rZC,m(n)

The sequence  is defined byrZC,m(n)

rZC,m(n)=xq(n+ncs) mod NZC

xqi=e-jπqi(i+1)NZC

n=0,1,…,MZC-1

where

- is the largest prime number such that NZCNZC<MZC

-MZC=NscWUSMWUS

The root sequence number  is configured by the higher-layer parameter root1 or root2 in lpwus-OverlaidSeqRoot, where root1 is used for the root sequence number when , and root2 is used otherwise.The cyclic shift  is given byq∈1, …, NZC-1cmP=0ncs

ncs=cm mod PNZCP

P=NseqNroot

where

- is the number of sequences configured by the higher-layer parameter lpwus-OverlaidSeqNum or lpwus-OverlaidSeqNum-SCS-60kHz or lpwus-OverlaidSeqNum-SCS-120kHzNseq

- if root2 in lpwus-OverlaidSeqRoot is configured, otherwise Nroot=2Nroot=1

The sequence number  if , otherwise it is given bycm=0Nseq=1

cm=i=0δ-1f1(i+δm)2δ-1-i

δ=log2Nseq

m=0,1,…,E1δ-1

where

- and  are given by clause 7.4.2.2 of [4, 38.212]f1iE1

## 7.4.4.1.2Generation of rWUS(n)

The block of complex-valued symbols  is defined byrWUS(0),…,rWUS(MbitMZC-1)

rWUSlNscWUS+k=1NscWUSi=0NscWUS-1rWUSlNscWUS+ie-j2πi(k-NscWUS2)NscWUS

k=0,1,…,NscWUS-1

l=0,1,…,MbitMWUS-1

NscWUS=11NscRB

where

rWUSmMZC+n=b(m)rZC,m(n)

m=m2

m=0,1,…,Mbit-1

n=0,1,…,MZC-1

The quantity  is given by the higher-layer parameter lpwus-MvalueAndSeqConfigFR1 or lpwus-MvalueAndSeqConfigFR2.MWUS∈1, 2, 4

The bit sequence  and the number of bits  corresponds to  and , respectively, in clause 7.4.3 of [4, 38.212].b0, …, b(Mbit-1)Mbitg00,g01,…,g0G0-1G0

## 7.4.4.2Mapping to physical resources

The UE shall assume the block of complex-valued symbols  is scaled by a factor  and mapped to resource elements  used for WUS transmission in increasing order of first  and then . rWUS(0),…,rWUS(MbitMZC-1)βWUSk,lp,μkl

## 7.4.5Low-power synchronization signal

## 7.4.5.1Sequence generation

## 7.4.5.1.1Generation of rOOK(n)

The sequence  is defined by Tables 7.4.5.1.1-1 to 7.4.5.1.1-3 with the quantity  given by the higher-layer parameter lpss-MvalueAndSeqConfig, the sequence length by the higher-layer parameter lpss-BinarySeqLen, and the configuration index by the higher-layer parameter lpss-BinarySeqIndex.rOOK0,…,rOOK(NOOK-1)MLPSS

Table 7.4.5.1.1-1: The sequence  for .rOOK0⋯rOOK(NOOK-1)MLPSS=1

Table 7.4.5.1.1-2: The sequence  for .rOOK0⋯rOOK(NOOK-1)MLPSS=2

Table 7.4.5.1.1-3: The sequence  for .rOOK0⋯rOOK(NOOK-1)MLPSS=4

## 7.4.5.1.2Generation of rZC(n)

If the quantity  is configured by the higher-layer parameter lpss-OverlaidSeqRoots, the sequence  is defined byqϵ1,…,NZC-1rZC(n)

rZC(n)=xqn mod NZC

xqi=e-jπqi(i+1)NZC

n=0,1,…,MZC-1

where

- is the largest prime number such that NZCNZC<MZC

-MZC=NscWUSMLPSS

## 7.4.5.1.3Generation of rLPSS(n)

The block of complex-valued symbols  is defined byrLPSS(0),…,rLPSS(NOOKMZC-1)

rLPSSlNscWUS+k=1NscWUSi=0NscWUS-1rLPSSlNscWUS+ie-j2πi(k-NscWUS2)NscWUS

k=0,1,…,NscWUS-1

l=0,1,…,NOOKMLPSS-1

NscWUS=11NscRB

where

rLPSSmMZC+n=rOOK(m)rZC(n)

m=0,1,…,NOOK-1

n=0,1,…,MZC-1

## 7.4.5.2Mapping to physical resources

The UE shall assume the block of complex-valued symbols  is scaled by a factor  and mapped to resource elements  used for LPSS transmission in increasing order of first  and then , then . rLPSS(0),…,rLPSS(NOOKMZC-1)βLPSSk,lp,μkl

## 8Sidelink

## 8.1Overview

## 8.1.1Overview of physical channels

A sidelink physical channel corresponds to a set of resource elements carrying information originating from higher layers. The following sidelink physical channels are defined:

-Physical Sidelink Shared Channel, PSSCH

-Physical Sidelink Broadcast Channel, PSBCH

-Physical Sidelink Control Channel, PSCCH

-Physical Sidelink Feedback Channel, PSFCH

## 8.1.2Overview of physical signals

A sidelink physical signal corresponds to a set of resource elements used by the physical layer but does not carry information originating from higher layers.

The following sidelink physical signals are defined:

-Demodulation reference signals, DM-RS

-Channel-state information reference signal, CSI-RS

-Phase-tracking reference signals, PT-RS

-Sidelink primary synchronization signal, S-PSS

-Sidelink secondary synchronization signal, S-SSS

-Sidelink positioning reference signal, SL PRS

## 8.2Physical resources

## 8.2.1General

In a shared SL PRS resource pool, the OFDM symbol immediately preceding the symbols which are configured for use by PSFCH if PSFCH is configured in this slot, and the last symbol configured for sidelink in a slot, serve as guard symbol(s). In a dedicated SL PRS resource pool, the last symbol configured for sidelink in a slot serves as a guard symbol. Otherwise, the OFDM symbol immediately following the last symbol used for PSSCH, PSFCH, or S-SSB serves as a guard symbol.

The first OFDM symbol of a PSSCH and its associated PSCCH is duplicated as described in clauses 8.3.1.5 and 8.3.2.3. The first OFDM symbol of a PSFCH is duplicated as described in clause 8.3.4.2.2.

The OFDM symbol immediately preceding an SL PRS resource in a dedicated SL PRS resource pool is generated as described in clause 8.4.1.6.3.

## 8.2.2Numerologies

Multiple OFDM numerologies are supported as given by Table 8.2.2-1 where  and the cyclic prefix for a sidelink bandwidth part are obtained from the higher-layer parameter sl-BWP. μ

Table 8.2.2-1: Supported transmission numerologies.

## 8.2.3Frame structure

## 8.2.3.1Frames and subframes

The frame and subframe structure for sidelink transmission is defined in clause 4.3.1.

## 8.2.3.2Slots

The slot structure for sidelink transmission is defined in clause 4.3.2.

## 8.2.4Antenna ports

An antenna port is defined in clause 4.4.1.

The following antenna ports are defined for the sidelink:

-Antenna ports starting with 1000 for PSSCH

-Antenna ports starting with 2000 for PSCCH

-Antenna ports starting with 3000 for CSI-RS

-Antenna ports starting with 4000 for S-SS/PSBCH block

-Antenna ports starting with 5000 for PSFCH

-Antenna ports starting with 6000 for SL PRS

For DM-RS associated with a PSBCH, the channel over which a PSBCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within a S-SS/PSBCH block transmitted within the same slot, and with the same block index.

For DM-RS associated with a PSSCH, the channel over which a PSSCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within the same frequency resource as the scheduled PSSCH and in the same slot.

For DM-RS associated with a PSCCH, the channel over which a PSCCH symbol on one antenna port is conveyed can be inferred from the channel over which a DM-RS symbol on the same antenna port is conveyed only if the two symbols are within the same frequency resource as the transmitted PSCCH and in the same slot.

## 8.2.5Resource grid

The resource grid for sidelink transmission is defined in clause 4.4.2.

For sidelink, the carrier bandwidth  and the starting position  for subcarrier spacing configuration  are obtained from the higher-layer parameter sl-SCS-SpecificCarrierList. Ngridsize,μNgridstart,μμ

For the sidelink, the higher-layer parameter sl-TxDirectCurrentLocation indicates the location of the transmitter DC subcarrier in the sidelink for each of the configured bandwidth parts. Values in the range 0 – 3299 represent the number of the DC subcarrier, the value 3300 indicates that the DC subcarrier is located outside the resource grid, and the value 3301 indicates that the position of the DC subcarrier in the sidelink is undetermined. The DC subcarrier location offset relative to the center of the indicated subcarrier is given by  if frequencyShift7p5khzSL is provided and by   otherwise, where  is given by the higher-layer parameter valueN.7.5+5N kHz5N kHzN∈-1,0,1

## 8.2.6Resource elements

Resource elements are defined in clause 4.4.3.

## 8.2.7Resource blocks

Resource blocks are defined in clause 4.4.4.

Point A for sidelink transmission/reception is obtained from the higher-layer parameter sl-AbsoluteFrequencyPointA.

## 8.2.8Bandwidth part

Configuration of the single bandwidth part for sidelink transmission is described in clause 16 of [5, TS 38.213].

## 8.3Physical channels

## 8.3.1Physical sidelink shared channel

## 8.3.1.1Scrambling

For the single codeword , the block of bits , where  is the number of bits in codeword  transmitted on the physical channel as defined in [4, TS 38.212], shall be scrambled prior to modulation.q=0bq0,…,bqMbit(q)-1Mbit(q)=Mbit,SCI2(q)+Mbit,data(q)q

Scrambling shall be done according to the following pseudo code

set  i=0

set j=0

while i<Mbitq

if // SCI placeholder bitsb(q)i=x

b(q)i=b(q)i-2

j=j+1

else

b(q)i=b(q)i+cq(i-Mi,jq) mod 2

end if

i = i + 1

end while

where the scrambling sequence  is given by clause 5.2.1 andcq(i)

-for 0≤i<Mbit,SCI2(q)

-Mi,jq=j

-The scrambling sequence generator shall be initialized with

cinit=215NID+1010

where  and the quantity  equals the decimal representation of the CRC on the PSCCH associated with the PSSCH according to  with  and  given by clause 8.3.2 in [4, TS 38.212].NID=NIDX mod 216NIDXNIDX=i=0L-1pi∙2L-1-ipL

-for Mbit,SCI2(q)≤i< Mbit(q)

-Mi,jq=Mbit,SCI2q

-The scrambling sequence generator shall be initialized with

cinit=215NID+1010

where  and the quantity  equals the decimal representation of the CRC on the PSCCH associated with the PSSCH according to  with  and  given by clause 8.3.2 in [4, TS 38.212].NID=NIDX mod 216NIDXNIDX=i=0L-1pi∙2L-1-ipL

## 8.3.1.2Modulation

For the single codeword , the block of scrambled bits shall be modulated, resulting in a block of complex-valued modulation symbols  where .q=0d(q)0,…,d(q)Msymb(q)-1Msymb(q)=Msymb,1(q)+Msymb,2(q)

Modulation for  shall be done as described in clause 5.1 using QPSK, where .0≤i<Mbit,SCI2(q)Msymb,1(q)=Mbit,SCI2(q)2

Modulation for   shall be done as described in clause 5.1 using one of the modulation schemes in Table 8.3.1.2-1 where .Mbit,SCI2(q)≤i< Mbit(q)Msymb,2(q)=Mbit,data(q)Qm

Table 8.3.1.2-1: Supported modulation schemes.

## 8.3.1.3Layer mapping

Layer mapping shall be done according to clause 7.3.1.3 with the number of layers , resulting in , .υ∈1,2xi=x(0)(i)…x(υ-1)(i)Ti=0,1,…,Msymblayer-1

## 8.3.1.4Precoding

The block of vectors  shall be precoded according to clasue 6.3.1.5 where the precoding matrix  equals the identity matrix and .x(0)(i)…x(υ-1)(i)TWMsymbap=Msymblayer

## 8.3.1.5Mapping to virtual resource blocks

For each of the antenna ports used for transmission of the PSSCH, the block of complex-valued symbols  shall be multiplied with the amplitude scaling factor   in order to conform to the transmit power specified in [5, TS 38.213] and mapped to resource elements  in the virtual resource blocks assigned for transmission, where  is the first subcarrier in the lowest-numbered virtual resource block assigned for transmission.z(p)0, …, z(p)(Msymbap-1)βDMRSPSSCH(k',l)p,μk'=0

The mapping operation shall be done in two steps:

-first, the complex-valued symbols corresponding to the bit for the 2nd-stage SCI in increasing order of first the index  over the assigned virtual resource blocks and then the index , starting from the first PSSCH symbol carrying an associated DM-RS and meeting all of the following criteria:k'l

-the corresponding resource elements in the corresponding physical resource blocks are not used for transmission of the associated DM-RS, PT-RS, or PSCCH;

-secondly, the complex-valued modulation symbols not corresponding to the 2nd -stage SCI shall be in increasing order of first the index  over the assigned virtual resource blocks, and then the index  with the starting position given by [6, TS 38.214] and meeting all of the following criteria:k'l

-the resource elements are not used for 2nd-stage SCI in the first step;

-the resource elements are not in the  symbols used for transmission of the associated SL PRS according to clause 8.2.4.1.1 of [6, TS 38.214];LSL-PRS

-the corresponding resource elements in the corresponding physical resource blocks are not used for transmission of the associated DM-RS, PT-RS, CSI-RS, or PSCCH.

The resource elements used for the PSSCH in the first OFDM symbol in the mapping operation above, including any DM-RS, PT-RS, or CSI-RS occurring in the first OFDM symbol, shall be duplicated in the OFDM symbol immediately preceding the first OFDM symbol in the mapping.

## 8.3.1.6Mapping from virtual to physical resource blocks

Virtual resource blocks shall be mapped to physical resource blocks according to non-interleaved mapping.

For non-interleaved VRB-to-PRB mapping, virtual resource block  is mapped to physical resource block .nn

## 8.3.2Physical sidelink control channel

## 8.3.2.1Scrambling

The block of bits , where  is the number of bits transmitted on the physical channel, shall be scrambled prior to modulation, resulting in a block of scrambled bits  according tob0,…,b(Mbit-1)Mbitb0,…,b(Mbit-1)

bi=bi+c(i) mod 2

where the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with ci

cinit=1010

## 8.3.2.2Modulation

The block of scrambled bits  shall be modulated as described in clause 5.1 using QPSK, resulting in a block of complex-valued modulation symbols  where . b0,…,b(Mbit-1)d0,…,d(Msymb-1)Msymb=Mbit2

## 8.3.2.3Mapping to physical resources

The set of complex-valued modulation symbols   shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  assigned for transmission according to clause 16.4 of [5, TS 38.213], and not used for the demodulation reference signals associated with PSCCH, in increasing order of first the index  over the assigned physical resources, and then the index  on antenna port. d0,…,d(Msymb-1)βDMRSPSCCHd0k,lp,μkl p=2000

The resource elements used for the PSCCH in the first OFDM symbol in the mapping operation above, including any DM-RS, PT-RS, or CSI-RS occurring in the first OFDM symbol, shall be duplicated in the immediately preceding OFDM symbol.

## 8.3.3Physical sidelink broadcast channel

## 8.3.3.1Scrambling

The block of bits, where  is the number of bits transmitted on the physical sidelink broadcast channel, shall be scrambled prior to modulation, resulting in a block of scrambled bits  according to b0, …, b(Mbit-1)Mbit b0, …, b(Mbit-1)

bi=bi+c(i) mod 2

where the scrambling sequence  is given by clause 5.2.1. The scrambling sequence generator shall be initialized with  at the start of each S-SS/PSBCH block.c(i)cinit=NIDSL

## 8.3.3.2Modulation

The block of bits  shall be QPSK modulated as described in clause 5.1.3, resulting in a block of complex-valued modulation symbols  where .  b0, …, b(Mbit-1)dPSBCH0,…,dPSBCH(Msymb-1)Msymb=Mbit2

## 8.3.3.3Mapping to physical resources

Mapping to physical resources is described in clause 8.4.3.

## 8.3.4Physical sidelink feedback channel

## 8.3.4.1General

## 8.3.4.2PSFCH format 0

## 8.3.4.2.1Sequence generation

The sequence  shall be generated according toxn

xn=ru,vα,δn

n=0,1,…,NscRB-1

where  is given by clause 6.3.2.2 with the following exceptions:ru,vα,δ(n)

- is given by clause 16.3 of [5, TS 38.213]; mcs

- is given by clause 16.3 of [5, TS 38.213];m0

- is given bymint

- if the higher-layer parameter sl-TransmissionStructureForPSFCH is configured and set to 'dedicatedInterlace' and where  is the resource block number within the interlace;mint=5nIRBμnIRBμ

- otherwisemint=0

-;l=0

- is the index of the OFDM symbol in the slot that corresponds to the second OFDM symbol of the PSFCH transmission in the slot given by [5, TS 38.213];l'

- and  with  given by the higher-layer parameter sl-PSFCH-HopID if configured; otherwise, .u=nID mod 30v=0nIDu=0

- with  given by the higher-layer parameter sl-PSFCH-HopID if configured; otherwise, .cinit=nIDnIDcinit=0

## 8.3.4.2.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  assigned for transmission of the second PSFCH symbol according to clause 16.3 of [5, TS 38.213] in increasing order of the index  over the assigned physical resources on antenna port. xnβPSFCHx0k,lp,μk p=5000

The resource elements used for the PSFCH in the OFDM symbol in the mapping operation above shall be duplicated in the immediately preceding OFDM symbol.

If the higher-layer parameter sl-TransmissionStructureForPSFCH is configured and set to 'dedicatedInterlace', the mapping operation shall be repeated for each resource block in the interlace and in the RB set over the assigned physical resource blocks according to clause 16.3 of [5, TS 38.213], with the resource-block dependent sequence generated according to clause 8.3.4.2.1.

If the higher-layer parameter sl-TransmissionStructureForPSFCH is configured and set to 'commonInterlace', the mapping operation shall be repeated for each resource block over the assigned physical resource blocks according to clause 16.3 of [5, TS 38.213], with the resource-block dependent sequence generated according to clause 8.3.4.2.1, where the cyclic shift  on each resource block in the first interlace is up to UE implementation.α

## 8.4Physical signals

## 8.4.1Reference signals

## 8.4.1.1Demodulation reference signals for PSSCH

## 8.4.1.1.1Sequence generation

The sequence  shall be generated according torlm

rlm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialized withcm

cinit=217Nsymbslotns,fμ+l+12NID+1+2NID mod 231

where  is the OFDM symbol number within the slot,  is the slot number within a frame, and  where the quantity  equals the decimal representation of CRC on the PSCCH associated with the PSSCH according to  with  and  given by clause 7.3.2 in [4, TS 38.212].lns,fμNID=NIDX mod 216NIDXNIDX=i=0L-1pi∙2L-1-ipL

## 8.4.1.1.2Mapping to physical resources

The sequence  shall be mapped to the intermediate quantity  according to clause 6.4.1.1.3 using configuration type 1 without transform precoding, and where , , and  are given by Table 8.4.1.1.2-2, and  is specified in clause 8.4.1.1.1.rmak,l(pj,μ)wfk'wtl'Δr(m)

The patterns used for the PSSCH DM-RS is indicated in the SCI as described in clause 8.3.1.1 of [4, TS 38.212].

The intermediate quantity  shall be precoded, multiplied with the amplitude scaling factor  specified in clause 8.3.1.5, and mapped to physical resources according toak,l(pj,μ)βDMRSPSSCH

ak,l(p0,μ)⋮ak,l(pρ-1,μ)=βDMRSPSSCHWak,l(p0,μ)⋮ak,l(pυ-1,μ)

where

-the precoding matrix  is given by clause 8.3.1.4, W

-the set of antenna ports  is given by clause 8.3.1.4, andp0,…,pρ-1

-the set of antenna ports  is given by [6, TS 38.214];p0,…,pυ-1

and the following conditions are fulfilled:

-the resource elements  are within the common resource blocks allocated for PSSCH transmission.ak,l(pj,μ)

The quantity  is defined relative to subcarrier 0 in common resource block 0 and the quantity  is defined relative to the start of the scheduled resources for transmission of PSSCH and the associated PSCCH, including the OFDM symbol duplicated as described in clauses 8.3.1.5 and 8.3.2.3.kl

The position(s) of the DM-RS symbols is given by  according to Table 8.4.1.1.2-1 where the number of PSSCH DM-RS is indicated in the SCI, and  is the duration of the scheduled resources for transmission of PSSCH according to clause 8.1.2.1 of [6, TS 38.214] and the associated PSCCH, including the OFDM symbol duplicated as described in clauses 8.3.1.5 and 8.3.2.3.lld

Table 8.4.1.1.2-1: PSSCH DM-RS time-domain location.

Table 8.4.1.1.2-2: Parameters for PSSCH DM-RS.

## 8.4.1.2Phase-tracking reference signals for PSSCH

## 8.4.1.2.1Sequence generation

The precoded sidelink phase-tracking reference signal for subcarrier  on layer  is given bykj

r(pj)m=rmif j=j' or j=j"0otherwise

where

-antenna ports  or  associated with PT-RS transmission are given by clause 8.2.3 of [6, TS 38.214];pj'pj',pj''

- is given by clause 8.4.1.1.1 at the position of the first PSSCH symbol carrying an associated DM-RS.rm

## 8.4.1.2.2Mapping to physical resources

The UE shall transmit phase-tracking reference signals only in the resource blocks used for the PSSCH, and only if the procedure in [6, TS 38.214] indicates that phase-tracking reference signals are being used.

The PSSCH PT-RS shall be mapped to resource elements according to

ak,lpo,μ⋮ak,lpρ-1,μ=βDMRSPSSCHWr(p0)(2n+k')⋮r(pυ-1)(2n+k')

k=4n+2k'+Δ

when all the following conditions are fulfilled

- is within the OFDM symbols allocated for the PSSCH transmission;l

-resource element  is not used for PSCCH, nor DM-RS associated with PSSCH;k,l

- and  correspond to k'Δp0, …, pυ-1

The precoding matrix  is given by clause 8.3.1.4. W

The set of time indices  defined relative to the start of the PSSCH allocation is defined byl

1. set and i=0 lref=0

2. if any symbol in the interval  overlaps with a symbol used for DM-RS according to clause 8.4.1.1.2max lref+i-1LPT-RS+1, lref,…,lref+iLPT-RS

-set i=1

-set  to the symbol index of the DM-RS symbollref

-repeat from step 2 as long as  is inside the PSSCH allocationlref+iLPT-RS

3. add  to the set of time indices for PT-RSlref+iLPT-RS

4. increment  by onei

5. repeat from step 2 above as long as  is inside the PSSCH allocationlref+iLPT-RS

where  is given by clause 8.4.3 of [6, TS 38.214].LPT-RS∈1,2,4

For the purpose of PT-RS mapping, the resource blocks allocated for PSSCH transmission are numbered from 0 to  from the lowest scheduled resource block to the highest. The corresponding subcarriers in this set of resource blocks are numbered in increasing order starting from the lowest frequency from 0 to . The subcarriers to which the PT-RS shall be mapped are given byNRB-1NscRBNRB-1

k=krefRE+iKPT-RS+krefRBNscRBkrefRB=NID mod KPT-RSif NRB mod KPT-RS=0NID mod NRB mod KPT-RSotherwise

where

-i=0,1,2,…

- is given by Table 8.4.1.2.2-1 for the DM-RS port associated with the PT-RS port according to clause 8.2.3 in [6, TS 38.214]. krefRE

- is the number of resource blocks scheduled;NRB

- is given by [6, TS 38.214];KPT-RS∈2,4

- where the quantity  equals the decimal representation of CRC on the PSCCH associated with the PSSCH according to  with  and  given by clause 7.3.2 in [4, TS 38.212].NID=NIDX mod 216NIDXNIDX=i=0L-1pi∙2L-1-ipL

PSSCH PT-RS shall not be mapped to resource elements containing PSCCH or PSCCH DMRS by puncturing PSSCH PT-RS.

A UE is not expected to receive sidelink CSI-RS and PSSCH PT-RS on the same resource elements.

Table 8.4.1.2.2-1: The parameter  .krefRE

## 8.4.1.3Demodulation reference signals for PSCCH

## 8.4.1.3.1Sequence generation

The sequence  shall be generated according torlm

rlm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialized withcm

cinit=217Nsymbslotns,fμ+l+12NID+1+2NID mod 231

where

- is the OFDM symbol number within the slot, l

- is the slot number within a frame, andns,fμ

- is given by the higher-layer parameter sl-DMRS-ScrambleID, or is given by the higher-layer parameter sl-DMRS-ScrambleID-DedicatedSL-PRS-RP when the resource pool is a dedicated SL PRS resource pool.NID∈{0,1,…,65535}

## 8.4.1.3.2Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with  to resource elements  in a slot on antenna port  according torlmβDMRSPSCCHrl0k,lp,μp=2000

ak,l(p,μ)=βDMRSPSCCHwf,i(k')rl3n+k'k=nNscRB+4k'+1k'=0,1,2n=0,1,…

where the following conditions are fulfilled

-they are within the resource elements constituting the PSCCH

The quantity  is given by Table 8.4.1.3.2-1 and  shall be randomly selected by the UE.wf,i(k')i∈0,1,2

The reference point for  is subcarrier 0 in common resource block 0.k

The quantity  is the OFDM symbol number within the slot. l

Table 8.4.1.3.2-1: The quantity .wf,i(k')

## 8.4.1.4Demodulation reference signals for PSBCH

## 8.4.1.4.1Sequence generation

The reference-signal sequence  for an S-SS/PSBCH block is defined byrm

rm=121-2c2m+j121-2c2m+1

where  is given by clause 5.2. The scrambling sequence generator shall be initialized at the start of each S-SS/PSBCH block occasion with cn

cinit=NIDSL

## 8.4.1.4.2Mapping to physical resources

Mapping to physical resources is described in clause 8.4.3.

## 8.4.1.5CSI reference signals

## 8.4.1.5.1General

## 8.4.1.5.2Sequence generation

The sequence  shall be generated according torm

rm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialised withci

cinit=210Nsymbslotns,fμ+l+12nID+1+nID mod 231

at the start of each OFDM symbol where  is the slot number within a radio frame,  is the OFDM symbol number within a slot, and  where the quantity  equals the decimal representation of CRC for the sidelink control information mapped to the PSCCH associated with the CSI-RS according to  with  and  given by clause 7.3.2 in [4, TS 38.212].ns,fμlnID=NIDX mod 210NIDXNIDX=i=0L-1pi∙2L-1-ipL

## 8.4.1.5.3Mapping to physical resources

Mapping to resource elements shall be done according to clause 7.4.1.5.3 with the following exceptions:

-only 1 and 2 antenna ports are supported, ;X∈1,2

-only density  is supported;ρ=1

-zero-power CSI-RS is not supported;

-the quantity  is an amplitude scaling factor to conform with the transmit power specified in clause 8.2.1 of [6, TS 38.214].βCSIRS

## 8.4.1.6Positioning reference signals

## 8.4.1.6.1General

A SL PRS resource refers to a time-frequency resource within a slot, used for SL PRS transmission.

## 8.4.1.6.2Sequence generation

The sequence  is defined byrm

rm=121-2c2m+j121-2c2m+1

where the pseudo-random sequence  is defined in clause 5.2.1. The pseudo-random sequence generator shall be initialised withci

cinit=222nID,seqSL-PRS1024+210Nsymbslotns,fμ+l+12nID,seqSL-PRS mod 1024+1+nID,seqSL-PRS mod 1024 mod 231

where

- is the slot number within the radio framens,fμ

- is the OFDM symbol number within the slot to which the sequence is mappedl

- is the sidelink PRS sequence ID, which, if not provided by higher layers, is obtained from the decimal representation of the CRC for the sidelink control information mapped to the PSCCH associated with the SL PRS according to  with  and  given by clause 7.3.2 in [4, TS 38.212].nID,seqSL-PRS∈0,1,…,4095nID,seqSL-PRS= i=0L-1pi∙2L-1-i mod 212pL

## 8.4.1.6.3Mapping to physical resources

The sequence shall be multiplied with the amplitude scaling factor  in order to conform to the transmit power specified in [5, TS 38.213] and mapped to resources elements  according to βSL-PRSk,lp,μ

ak,lp,μ=βSL-PRS rmm=0, 1, …k=mKcombSL-PRS+koffsetSL-PRS+k' mod KcombSL-PRSl=lstartSL-PRS, lstartSL-PRS+1, …, lstartSL-PRS+LSL-PRS-1

when the following conditions are fulfilled:

-the resource element  is within the common resource blocks occupied by the SL PRS resourcek,lp,μ

and where

-the comb size  is provided by the higher layer parameter sl-PRS-CombSizeN-AndReOffset for a shared SL PRS resource pool and by the higher layer parameter sl-CombSize for a dedicated SL PRS resource poolKcombSL-PRS

-the resource-element offset  koffsetSL-PRS∈0,1,…,KcombSL-PRS-1

-the frequency offset  is given by Table 8.4.1.6.3-1k'

-the starting symbol  is provided by the higher-layer parameter sl-PRS-starting-symbol for a dedicated SL PRS resource pool, or is determined such that the symbols {} are mapped to the last consecutive  symbols in the slot that can be used for SL PRS for a shared SL PRS resource pool as described in clause 8.2.4.1.1 in [6, TS38.214]lstartSL-PRSlstartSL-PRS, lstartSL-PRS+1,…,lstartSL-PRS+LSL-PRS-1LSL-PRS

-the number of symbols  is provided by the higher-layer parameter mNumberOfSymbols for a shared resource pool and by the higher layer parameter sl-NumberOfSymbols for a dedicated resource pool and limited to combinations  fulfilling LSL-PRSLSL-PRS,KcombSL-PRS

-in a dedicated SL PRS resource pool: {1, 2}, {2, 2}, {2, 4}, {4, 4}, {6, 6}, and combinations with  and  where  KcombSL-PRS∈ 2, 4, 6LSL-PRS∈3, 4, …, 9LSL-PRS>KcombSL-PRS

-in a shared SL PRS resource pool: {1, 1}, {1, 2}, {2, 1}, {2, 2}, {2, 4}, {4, 1}, {4, 2}, {4, 4}

-the antenna port p=6000

The reference point for  is subcarrier 0 in common resource block 0.k

For transmission of an SL PRS in a dedicated SL PRS resource pool, the content of the OFDM symbol immediately preceding the SL PRS resource shall be generated based on 8.4.1.6.2 and mapped to resource elements with

-the time-domain index  l=lstartSL-PRS-1

-the set of frequency-domain indices  shall be identical to those of the last OFDM symbol in the SL PRS resource k

-the amplitude scaling factor shall be same as the amplitude scaling factor  of the SL PRS resource.βSL-PRS

Table 8.4.1.6.3-1: The frequency offset  as a function of .k'l-lstartSL-PRS

## 8.4.2Synchronization signals

## 8.4.2.1Physical-layer sidelink synchronization identities

There are 672 unique physical-layer sidelink synchronization identities given by

NIDSL=NID,1SL+336NID,2SL

where  and . The sidelink synchronization identities are divided into two sets, id_net consisting of  and id_oon consisting of .NID,1SL∈0,1,…,335NID,2SL∈0,1NIDSL=0,1,…,335NIDSL=336,337,…,671

## 8.4.2.2Sidelink primary synchronization signal

## 8.4.2.2.1Sequence generation

The sequence  for the sidelink primary synchronization signal is defined by dS-PSSn

dS-PSSn=1-2xmm=n+22+43NID,2SL mod 1270≤n<127

where

xi+7=xi+4+xi mod 2

and

x6x5x4x3x2x1x0=1110110

## 8.4.2.2.2Mapping to physical resources

Mapping to physical resources is described in clause 8.4.3.

## 8.4.2.3Sidelink secondary synchronization signal

## 8.4.2.3.1Sequence generation

The sequence  for the sidelink secondary synchronization signal is defined by dS-SSSn

dS-SSSn=1-2x0n+m0 mod 1271-2x1n+m1 mod 127m0=15NID,1SL112+5NID,2SLm1=NID,1SL mod 1120≤n<127

where

x0i+7=x0i+4+x0i mod 2x1i+7=x1i+1+x1i mod 2

and

x06x05x04x03x02x01x00=0000001x16x15x14x13x12x11x10=0000001

## 8.4.2.3.2Mapping to physical resources

Mapping to physical resources is described in clause 8.4.3.

## 8.4.3S-SS/PSBCH block

## 8.4.3.1Time-frequency structure of an S-SS/PSBCH block

In the time domain, an S-SS/PSBCH block consists of  OFDM symbols, numbered in increasing order from 0 to  within the S-SS/PSBCH block, where S-PSS, S-SSS, and PSBCH with associated DM-RS are mapped to symbols as given by Table 8.4.3.1-1. The number of OFDM symbols in an S-SS/PSBCH block  for normal cyclic prefix and  for extended cyclic prefix. The first OFDM symbol in an S-SS/PSBCH block is the first OFDM symbol in the slot.NsymbS-SSBNsymbS-SSB-1NsymbS-SSB=13NsymbS-SSB=11

In the frequency domain, an S-SS/PSBCH block consists of 132 contiguous subcarriers with the subcarriers numbered in increasing order from 0 to 131 within the sidelink S-SS/PSBCH block. The quantities  and  represent the frequency and time indices, respectively, within one sidelink S-SS/PSBCH block. kl

For an S-SS/PSBCH block, the UE shall use

-antenna port 4000 for transmission of S-PSS, S-SSS, PSBCH and DM-RS for PSBCH;

-the same cyclic prefix length and subcarrier spacing for the S-PSS, S-SSS, PSBCH and DM-RS for PSBCH,

Table 8.4.3.1-1: Resources within an S-SS/PSBCH block for S-PSS, S-SSS, PSBCH, and DM-RS.

## 8.4.3.1.1Mapping of S-PSS within an S-SS/PSBCH block

The sequence of symbols  constituting the sidelink primary synchronization signal in one OFDM symbol shall be scaled by a factor  to conform to the S-PSS power allocation specified in [5, TS 38.213] and mapped to resource elements  in increasing order of  in each of the symbols , where  and  are given by Table 8.4.3.1-1 and represent the frequency and time indices, respectively, within one S-SS/PSBCH block.dS-PSS0, …, dS-PSS126βS-PSS(k,l)p,μklkl

## 8.4.3.1.2Mapping of S-SSS within an S-SS/PSBCH block

The sequence of symbols  constituting the sidelink secondary synchronization signal in one OFDM symbol shall be scaled by a factor  to conform to the S-SSS power allocation specified in [5, TS 38.213] and mapped to resource elements  in increasing order of  in each of the symbols , where  and  are given by Table 8.4.3.1-1 and represent the frequency and time indices, respectively, within one S-SS/PSBCH block.dS-SSS0, …, dS-SSS126βS-SSS(k,l)p,μklkl

## 8.4.3.1.3Mapping of PSBCH and DM-RS within an S-SS/PSBCH block

The sequence of complex-valued symbols  constituting the physical sidelink broadcast channel shall be scaled by a factor  to conform to the PSBCH power allocation specified in [5, TS 38.213] and mapped in sequence starting with  to resource elements  which meet all the following criteria:dPSBCH0, …,dPSBCHMsymb-1 βDMRSPSBCHdPSBCH0(k,l)p,μ

-they are not used for PSBCH demodulation reference signals

The mapping to resource elements  not reserved for PSBCH DM-RS shall be in increasing order of first the index  and then the index, where  and  represent the frequency and time indices, respectively, within one S-SS/PSBCH block and are given by Table 8.4.3.1-1.(k,l)p,μk lkl

The sequence of complex-valued symbols  constituting the demodulation reference signals for the S-SS/PSBCH block shall be scaled by a factor of  to conform to the PSBCH power allocation specified in [5, TS 38.213] and mapped to resource elements  in increasing order of first  and then  where  and  are given by Table 8.4.3.1-1 and represent the frequency and time indices, respectively, within one S-SS/PSBCH block.r0, …,r33NsymbS-SSB-4-1βDMRSPSBCH(k,l)p,μklkl

## 8.4.3.2Time location of an S-SS/PSBCH block

The locations in the time domain where a UE shall monitor for a possible S-SS/PSBCH block are described in clause 16.1  of [5, TS 38.213].

## 8.5Timing

Transmission of a sidelink radio frame number  from the UE shall start  seconds before the start of the corresponding timing reference frame at the UE. The UE is not required to receive sidelink or downlink transmissions earlier than the value of , which is given in [12, TS 38.133], after the end of a sidelink transmission.i(NTA,SL+NTA,offset)∙TcNTA,offset

For sidelink transmissions:

If the UE has a serving cell fulfilling the S criterion according to clause 8.2 of [13, TS 38.304]

-The timing of reference radio frame  equals that of downlink radio frame  in the cell with the same uplink carrier frequency as the sidelink andii

- is given by clause 4.3.1 of [TS 38.211],NTA,offset

Otherwise

-The timing of reference radio frame i and  value are given by clause 12.2.2, 12.2.3, 12.2.4 or 12.2.5 of [12, TS 38.133]. NTA,offset

Figure 8.5-1: Sidelink timing relation

The quantity  equals to 0.NTA,SL

## Annex A (informative):Change history
