# TS 36.323 36323-j00

3GPP TS 36.323 V19.0.0 (2025-09)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

Evolved Universal Terrestrial Radio Access (E-UTRA);

Packet Data Convergence Protocol (PDCP) specification

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.

This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords

LTE, E-UTRAN, radio

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

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Contents

Foreword6

1Scope7

2References7

3Definitions and abbreviations8

3.1Definitions8

3.2Abbreviations8

4General9

4.1Introduction9

4.2PDCP architecture9

4.2.1PDCP structure9

4.2.2PDCP entities10

4.3Services13

4.3.1Services provided to upper layers13

4.3.2Services expected from lower layers13

4.4Functions14

4.5Data available for transmission14

5PDCP procedures16

5.1PDCP Data Transfer Procedures16

5.1.1UL Data Transfer Procedures16

5.1.2DL Data Transfer Procedures17

5.1.2.1Procedures for DRBs17

5.1.2.1.1Void17

5.1.2.1.2Procedures for DRBs mapped on RLC AM when the reordering function is not used17

5.1.2.1.2aRN procedures for DRBs mapped on RLC AM18

5.1.2.1.3Procedures for DRBs mapped on RLC UM when the reordering function is not used19

5.1.2.1.3aRN procedures for DRBs mapped on RLC UM19

5.1.2.1.4Procedures for DRBs mapped on RLC AM or RLC UM, for LWA bearers and SLRB when the reordering function is used19

5.1.2.1.4.1Procedures when a PDCP PDU is received from the lower layers20

5.1.2.1.4.2Procedures when t-Reordering expires21

5.1.2.1.4.3Procedures when the value of t-Reordering is reconfigured22

5.1.2.2Procedures for SRBs22

5.1.2.2.1Procedures for SRBs when the reordering function is not used22

5.1.2.2.2Procedures for SRBs when the reordering function is used22

5.1.3SL Data Transmission Procedures23

5.1.4SL Data Reception Procedures23

5.2Re-establishment procedure23

5.2.1UL Data Transfer Procedures23

5.2.1.1Procedures for DRBs mapped on RLC AM23

5.2.1.2Procedures for DRBs mapped on RLC UM24

5.2.1.3Procedures for SRBs24

5.2.2DL Data Transfer Procedures25

5.2.2.1Procedures for DRBs mapped on RLC AM while the reordering function is not used25

5.2.2.1aProcedures for DRBs mapped on RLC AM while the reordering function is used25

5.2.2.2Procedures for DRBs mapped on RLC UM when the reordering function is not used25

5.2.2.2aProcedures for DRBs mapped on RLC UM when the reordering function is used26

5.2.2.3Procedures for SRBs26

5.2.2.4Procedures for LWA bearers26

5.3PDCP Status Report26

5.3.1Transmit operation26

5.3.2Receive operation27

5.4PDCP discard27

5.4aDuplicate PDCP discard27

5.5Robust Header Compression and Decompression28

5.5.1Supported header compression protocols and profiles28

5.5.2Configuration of ROHC28

5.5.3Protocol parameters28

5.5.4Header compression using ROHC29

5.5.5Header decompression using ROHC29

5.5.6PDCP Control PDU for interspersed ROHC feedback packet30

5.5.6.1Transmit Operation30

5.5.6.2Receive Operation30

5.6Ciphering and Deciphering30

5.6.0General30

5.6.1SL Ciphering and Deciphering for one-to-many communication30

5.6.2SL Ciphering and Deciphering for one-to-one communication31

5.6.3Handling of LWA end-marker PDCP Control PDU31

5.6.3.1Transmit operation31

5.6.3.2Receive Operation31

5.7Integrity Protection and Verification32

5.8Handling of unknown, unforeseen and erroneous protocol data32

5.9PDCP Data Recovery procedure32

5.10Status report for LWA33

5.10.1Transmit operation33

5.10.2LWA status report33

5.10.3Receive operation34

5.11Uplink Data compression and decompression34

5.11.1UDC protocol34

5.11.2Configuration of UDC34

5.11.3UDC header34

5.11.4Uplink data compression34

5.11.5Pre-defined dictionary35

5.11.6UDC buffer reset procedure35

5.11.7UDC checksum error handling35

5.12Uplink data switching35

5.13PDCP Reconfiguration35

5.14Ethernet header compression and decompression36

5.14.1Supported header compression protocols36

5.14.2Configuration of EHC36

5.14.3Protocol parameters36

5.14.4Header compression using EHC36

5.14.5Header decompression using EHC36

5.14.6PDCP Control PDU for EHC feedback packet37

5.14.6.1Transmit Operation37

5.14.6.2Receive Operation37

5.14.7Simultaneous configuration of ROHC and EHC37

6Protocol data units, formats and parameters37

6.1Protocol data units37

6.1.1PDCP Data PDU37

6.1.2PDCP Control PDU38

6.2Formats38

6.2.1General38

6.2.2Control plane PDCP Data PDU38

6.2.3User plane PDCP Data PDU with long PDCP SN (12 bits)39

6.2.4User plane PDCP Data PDU with short PDCP SN (7 bits)39

6.2.5PDCP Control PDU for interspersed ROHC feedback packet39

6.2.6PDCP Control PDU for PDCP status report40

6.2.7Void41

6.2.8RN user plane PDCP Data PDU with integrity protection41

6.2.9User plane PDCP Data PDU with extended PDCP SN (15 bits)41

6.2.10User plane PDCP Data PDU for SLRB42

6.2.11User plane PDCP Data PDU with further extended PDCP SN (18 bits)43

6.2.12PDCP Control PDU for LWA status report43

6.2.13PDCP Control PDU for LWA end-marker packet45

6.2.14User plane PDCP Data PDU with long PDCP SN (12 bits) for UDC45

6.2.15User plane PDCP Data PDU with extended PDCP SN (15 bits) for UDC46

6.2.16User plane PDCP Data PDU with further extended PDCP SN (18 bits) for UDC46

6.2.17PDCP Control PDU for UDC feedback packet46

6.2.18PDCP Control PDU for EHC feedback packet47

6.3Parameters47

6.3.1General47

6.3.2PDCP SN47

6.3.3Data47

6.3.4MAC-I48

6.3.5COUNT48

6.3.6R48

6.3.7D/C48

6.3.8PDU type48

6.3.9FMS49

6.3.10Bitmap49

6.3.11Interspersed ROHC feedback packet49

6.3.12PGK Index49

6.3.13PTK Identity50

6.3.14SDU Type50

6.3.15KD-sess ID50

6.3.16NMP50

6.3.17HRW50

6.3.18P50

6.3.19LSN51

6.3.21FU51

6.3.22FR51

6.3.23Checksum51

6.3.24FE52

7Variables, constants and timers52

7.1State variables52

7.2Timers53

7.3Constants53

Annex A (informative): An example of UDC Checksum calculation55

Annex B (informative): Change history56

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

The present document provides the description of the Packet Data Convergence Protocol (PDCP).

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

•References are either specific (identified by date of publication, edition number, version number, etc.) or non specific.

•For a specific reference, subsequent revisions do not apply.

•For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description".

[3]3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA) Radio Resource Control (RRC); Protocol Specification".

[4]3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA) Medium Access Control (MAC) protocol specification".

[5]3GPP TS 36.322: "Evolved Universal Terrestrial Radio Access (E-UTRA) Radio Link Control (RLC) protocol specification".

[6]3GPP TS 33.401: "3GPP System Architecture Evolution: Security Architecture".

[7]IETF RFC 5795: "The RObust Header Compression (ROHC) Framework".

[8]IETF RFC 6846: "RObust Header Compression (ROHC): A Profile for TCP/IP (ROHC-TCP)".

[9]IETF RFC 3095: "RObust Header Compression (ROHC): Framework and four profiles: RTP, UDP, ESP and uncompressed".

[10]IETF RFC 3843: "RObust Header Compression (ROHC): A Compression Profile for IP".

[11]IETF RFC 4815: "RObust Header Compression (ROHC): Corrections and Clarifications to RFC 3095".

[12]IETF RFC 5225: "RObust Header Compression (ROHC) Version 2: Profiles for RTP, UDP, IP, ESP and UDP Lite".

[13]3GPP TS 33.303: "Proximity-based Services; Security Aspects".

[14]3GPP TS 23.303: "Proximity-based Services; Stage 2".

[15]3GPP TS 36.360: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE-WLAN Aggregation Adaptation Protocol (LWAAP) specification".

[16]IETF RFC 1951: "DEFLATE Compressed Data Format Specification version 1.3".

[17]IETF RFC 3485: "The Session Initiation Protocol (SIP) and Session Description Protocol (SDP) Static Dictionary for Signaling Compression (SigComp)".

[18]IETF RFC 1979: "PPP Deflate Protocol".

[19]3GPP TS 38.323: "NR; Packet Data Convergence Protocol (PDCP) protocol specification".

## 3Definitions and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

DAPS bearer: a bearer whose radio protocols are located in both the source eNB and the target eNB during DAPS handover to use both source eNB and target eNB resources.

NB-IoT: NB-IoT allows access to network services via E-UTRA with a channel bandwidth limited to 200 kHz.

Split bearer: in dual connectivity, a bearer whose radio protocols are located in both the MeNB and the SeNB to use both MeNB and SeNB resources.

LWA bearer: in LTE-WLAN Aggregation, a bearer whose radio protocols are located in both the eNB and the WLAN to use both eNB and WLAN resources.

## 3.2Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

AILCAssistance Information bit for Local Cache

AMAcknowledged Mode

ARPAddress Resolution Protocol

CIDContext Identifier

DAPSDual Active Protocol Stack

DRBData Radio Bearer carrying user plane data

EHCEthernet Header Compression

EPSEvolved Packet System

E-UTRAEvolved UMTS Terrestrial Radio Access

E-UTRANEvolved UMTS Terrestrial Radio Access Network

eNBE-UTRAN Node B

FIFOFirst In First Out

FMSFirst missing PDCP SN

HFNHyper Frame Number

HRWHighest Received PDCP SN on WLAN

IETFInternet Engineering Task Force

IPInternet Protocol

L2Layer 2 (data link layer)

L3Layer 3 (network layer)

LWALTE-WLAN Aggregation

MACMedium Access Control

MAC-IMessage Authentication Code for Integrity

MCGMaster Cell Group

NB-IoTNarrow Band Internet of Things

NMPNumber of Missing PDCP SDUs

PDCPPacket Data Convergence Protocol

PDUProtocol Data Unit

PEKProSe Encryption Key

PGKProSe Group Key

ProSeProximity-based Services

PTKProSe Traffic Key

RReserved

RBRadio Bearer

RFCRequest For Comments

RLCRadio Link Control

RNRelay Node

ROHCRObust Header Compression

RRCRadio Resource Control

RTPReal Time Protocol

SAPService Access Point

SCGSecondary Cell Group

SDUService Data Unit

SLRBSidelink Radio Bearer carrying Sidelink Communication or V2X sidelink communication data

SNSequence Number

SRBSignalling Radio Bearer carrying control plane data

TCPTransmission Control Protocol

UDCUplink Data Compression

UDPUser Datagram Protocol

UEUser Equipment

UMUnacknowledged Mode

X-MACComputed MAC-I

## 4General

## 4.1Introduction

The present document describes the functionality of the PDCP. Functionality specified for the UE equally applies to the RN for functionality necessary for the RN. There is also functionality which is only applicable to the RN in its communication with the E-UTRAN, in which case the specification denotes the RN instead of the UE. RN-specific behaviour is not applicable to the UE. The functionality specified for the UE applies to communication on Uu interface and PC5 interface [14].

## 4.2PDCP architecture

## 4.2.1PDCP structure

Figure 4.2.1.1 represents one possible structure for the PDCP sublayer; it should not restrict implementation. The figure is based on the radio interface protocol architecture defined in TS 36.300 [2].

Figure 4.2.1.1 - PDCP layer, structure view

Each RB (i.e. DRB, SLRB and SRB, except for SRB0 and SRB1bis) is associated with one PDCP entity. Each PDCP entity is associated with one, two, or four (e.g uni-directional/bi-directional or split/non-split) RLC entities depending on the RB characteristic (i.e. uni-directional or bi-directional) or RLC mode:

-For split bearers or for RBs configured with PDCP duplication, each PDCP entity is associated with two (bi-directional) AM RLC entities, two (for same direction) UM RLC entities or four (uni-directional) UM RLC entities.

-For LWA bearers, each PDCP entity is associated with one (bi-directional) AM RLC entity or two (uni-directional) UM RLC entities and the LWAAP entity.

-For DAPS bearers, each PDCP entity is associated with two UM RLC entities (for same direction, one for source and one for target cell), four (uni-directional) UM RLC entities (two for each direction on source cell and target cell), or two AM RLC entities (bi-directional, one for source cell and one for target cell).

-Otherwise, each PDCP entity is associated with one UM RLC entity, two UM RLC entities (one for each direction), or one AM RLC entity (bi-directional).

PDCP entities are located in the PDCP sublayer. The PDCP sublayer is configured by upper layers, see TS 36.331 [3].

## 4.2.2PDCP entities

The PDCP entities are located in the PDCP sublayer. Several PDCP entities may be defined for a UE. Each PDCP entity carrying user plane data may be configured to use either uplink data compression (UDC) or to use header compression.

Each PDCP entity is carrying the data of one radio bearer. In this version of the specification, the robust header compression protocol (ROHC), Ethernet header compression (EHC), and UDC, are supported. Every PDCP entity uses at most one ROHC, one EHC, or one UDC compressor instance and at most one ROHC, one EHC, or one UDC decompressor instance. For DAPS bearers, the PDCP entity uses at most one ROHC compressor instance (i.e. use the ROHC compressor instance for source cell before uplink data switching, and use the ROHC compressor instance for target cell after uplink data switching) and at most two ROHC decompressor instances. UDC is not supported simultaneously with ROHC or EHC for the same radio bearer. ROHC and EHC are independently configured for the same radio bearer.

A PDCP entity is associated either to the control plane or the user plane depending on which radio bearer it is carrying data for.

Figure 4.2.2.1 represents the functional view of the PDCP entity for the PDCP sublayer; it should not restrict implementation. The figure is based on the radio interface protocol architecture defined in TS 36.300 [2].

For RNs, integrity protection and verification are also performed for the u-plane.

For split and LWA bearers, routing is performed in the transmitting PDCP entity, and reordering is performed in the receiving PDCP entity.

For PDCP duplication, submission of duplicates is performed in the transmitting PDCP entity, and duplicate discard is performed in the receiving PDCP entity.

For split bearers, except when PDCP duplication is configured and activated, when requested by lower layers to submit PDCP PDUs, the transmitting PDCP entity shall:

-if ul-DataSplitThreshold is configured and the data available for transmission is larger than or equal to ul-DataSplitThreshold:

-submit the PDCP PDUs to either the associated RLC entity configured for SCG or the associated RLC entity configured for MCG, whichever the PDUs were requested by;

-else:

-if ul-DataSplitDRB-ViaSCG is set to TRUE by upper layers, see TS 36.331 [3]:

-if the PDUs were requested by the associated lower layers configured for SCG:

-submit the PDCP PDUs to the associated RLC entity configured for SCG;

-else:

-if the PDUs were requested by the associated lower layers configured for MCG:

-submit the PDCP PDUs to the associated RLC entity configured for MCG.

For LWA bearers, when submitting PDCP PDUs to lower layers, the transmitting PDCP entity shall:

-if ul-LWA-DataSplitThreshold is configured and the data available for transmission is larger than or equal to ul-LWA-DataSplitThreshold:

-submit the PDCP PDUs to either the associated RLC entity upon request from lower layers or the associated LWAAP entity;

-else:

-if ul-LWA-DRB-ViaWLAN is set to TRUE by upper layers,see TS 36.331 [3]:

-submit the PDCP PDUs to the associated LWAAP entity;

-else:

-submit the PDCP PDUs to the associated RLC entity upon request from lower layers.

NOTE:The selection of PDCP PDUs submitted to the associated LWAAP entity is left up to the UE implementation.

For bearers configured with PDCP duplication, when requested by lower layers to submit the PDCP PDUs, the transmitting PDCP entity shall:

-if PDCP duplication is activated:

-if the PDCP PDU is a PDCP Data PDU:

-duplicate the PDCP Data PDU and submit the PDCP Data PDU to the associated RLC entities;

-else:

-submit the PDCP Control PDU to the primary RLC entity;

-else:

-submit the PDCP PDU to the associated RLC entity.

Figure 4.2.2.1 - PDCP layer, functional view

Figure 4.2.2.2 represents the functional view of the PDCP entity associated with the DAPS bearer for the PDCP sublayer; it should not restrict implementation. The figure is based on the radio interface protocol architecture defined in TS 36.300 [2].

For DAPS bearers, the PDCP entity is configured with two sets of ciphering functions and keys and two sets of header compression protocols.

For DAPS bearers, routing is performed in the transmitting PDCP entity, and reordering is performed in the receiving PDCP entity.

For DAPS bearers, when submitting PDCP PDUs to lower layers, the transmitting PDCP entity shall:

-if the uplink data switching has not been requested by upper layers:

-submit the PDCP PDU to the RLC entity associated with the source cell;

-else:

-if the PDCP PDU is a PDCP Data PDU:

-submit the PDCP Data PDU to the RLC entity associated with the target cell;

-else:

-if the PDCP Control PDU is associated with source cell:

-submit the PDCP Control PDU to the RLC entity associated with the source cell;

-else:

-submit the PDCP Control PDU to the RLC entity associated with the target cell.

Figure 4.2.2.2: PDCP layer associated with DAPS bearer, functional view

## 4.3Services

## 4.3.1Services provided to upper layers

PDCP provides its services to the RRC and user plane upper layers at the UE or to the relay at the evolved Node B (eNB). The following services are provided by PDCP to upper layers:

-transfer of user plane data;

-transfer of control plane data;

-header compression;

-uplink data compression;

-ciphering;

-integrity protection.

The maximum supported size of a PDCP SDU is 8188 octets, except in NB-IoT for which the maximum supported size of a PDCP SDU is 1600 octets. The maximum supported size of a PDCP Control PDU is 8188 octets except in NB-IoT for which the maximum supported size of PDCP Control PDU is 1600 octets.

## 4.3.2Services expected from lower layers

A PDCP entity expects the following services from lower layers per RLC entity (for a detailed description see TS 36.322 [5]):

-acknowledged data transfer service, including indication of successful delivery of PDCP PDUs;

-unacknowledged data transfer service;

-in-sequence delivery, except at re-establishment of lower layers;

-duplicate discarding, except at re-establishment of lower layers.

A PDCP entity expects the following services from the LWAAP entity (for a detailed description see TS 36.360 [15]):

-user plane data transfer service;

## 4.4Functions

The Packet Data Convergence Protocol supports the following functions:

-header compression and decompression of IP data flows using the ROHC protocol;

-header compression and decompression of Ethernet data flows using the EHC protocol;

-compression and decompression of uplink PDCP SDU;

-transfer of data (user plane or control plane);

-maintenance of PDCP SNs;

-in-sequence delivery of upper layer PDUs at re-establishment of lower layers;

-duplicate elimination of lower layer SDUs at re-establishment of lower layers for radio bearers mapped on RLC AM;

-ciphering and deciphering of user plane data and control plane data;

-integrity protection and integrity verification of control plane data;

-integrity protection and integrity verification of sidelink one-to-one communication data;

-for RNs, integrity protection and integrity verification of user plane data;

-timer based discard;

-duplicate transmission and duplicate discarding;

-for split and LWA bearers, routing and reordering;

-for DAPS bearers, routing and reordering.

PDCP uses the services provided by the RLC sublayer and the LWAAP sublayer.

PDCP is used for SRBs, DRBs, and SLRBs mapped on DCCH, DTCH, and STCH type of logical channels. PDCP is not used for any other type of logical channels. PDCP is not used for SRB1bis. DAPS PDCP is only used for DAPS DRB.

## 4.5Data available for transmission

For the purpose of MAC buffer status reporting, the UE shall consider PDCP Control PDUs, as well as the following as data available for transmission in the PDCP layer:

For SDUs for which no PDU has been submitted to lower layers:

-the SDU itself, if the SDU has not yet been processed by PDCP, or

-the PDU if the SDU has been processed by PDCP.

In addition, for radio bearers that are mapped on RLC AM, if the PDCP entity has previously performed the re-establishment procedure or uplink data switching procedure, the UE shall also consider the following as data available for transmission in the PDCP layer:

For SDUs for which a corresponding PDU has only been submitted to lower layers prior to the PDCP re-establishment, starting from the first SDU for which the delivery of the corresponding PDUs has not been confirmed by the lower layer, except the SDUs which are indicated as successfully delivered by the PDCP status report, if received:

-the SDU, if it has not yet been processed by PDCP, or

-the PDU once it has been processed by PDCP.

For radio bearers that are mapped on RLC AM, if the PDCP entity has previously performed the data recovery procedure, the UE shall also consider as data available for transmission in the PDCP layer, all the PDCP PDUs that have only been submitted to re-established AM RLC entity prior to the PDCP data recovery, starting from the first PDCP PDU whose successful delivery has not been confirmed by lower layers, except the PDUs which are indicated as successfully delivered by the PDCP status report, if received.

In addition, for bearers configured with PDCP duplication, when PDCP duplication is activated, for SDUs for which a PDU has only been submitted to lower layers associated with one logical channel, for the purpose of MAC buffer status reporting associated with the other logical channel the UE shall consider:

-the PDU, if the PDU has not yet been confirmed to be successfully delivered by those lower layers.

For split bearers, when indicating the data available for transmission to a MAC entity for BSR triggering and Buffer Size calculation, the UE shall:

-if ul-DataSplitThreshold is configured and the data available for transmission is larger than or equal to ul-DataSplitThreshold:

-indicate the data available for transmission to both the MAC entity configured for SCG and the MAC entity configured for MCG;

-else:

-if ul-DataSplitDRB-ViaSCG is set to TRUE by upper layer, see TS 36.331 [3]:

-indicate the data available for transmission to the MAC entity configured for SCG only;

-if ul-DataSplitThreshold is configured, indicate the data available for transmission as 0 to the MAC entity configured for MCG;

-else:

-indicate the data available for transmission to the MAC entity configured for MCG only;

-if ul-DataSplitThreshold is configured, indicate the data available for transmission as 0 to the MAC entity configured for SCG.

For uplink LWA bearers, when indicating the data available for transmission to the MAC entity for BSR triggering and Buffer Size calculation, the UE shall:

-if ul-LWA-DataSplitThreshold is configured and the data available for transmission is larger than or equal to ul-LWA-DataSplitThreshold:

-indicate the data available for transmission to the MAC entity;

-else:

-if ul-LWA-DRB-ViaWLAN is set to TRUE by upper layers, see TS 36.331 [3]:

-indicate the data available for transmission as 0 to the MAC entity;

-else:

-indicate the data available for transmission to the MAC entity.

NOTE:For LWA bearers, only the data that may be sent over LTE (i.e., excluding UL data already sent or decided to be sent over WLAN) is considered as "data available for transmission".

For bearers configured with PDCP duplication, when indicating the data available for transmission to a MAC entity for BSR triggering and Buffer Size calculation, the UE shall:

-if PDCP duplication is activated:

-indicate the data available for transmission to the MAC entity associated with the primary RLC entity and (if different) the MAC entity associated with the secondary RLC entity.

-else:

-if the two associated RLC entities belong to the different cell groups:

-if ul-DataSplitThreshold is configured and the data available for transmission is larger than or equal to ul-DataSplitThreshold:

-indicate the data available for transmission to both the MAC entity configured for SCG and the MAC entity configured for MCG.

-else:

-if ul-DataSplitDRB-ViaSCG is set to TRUE by upper layer, see TS 36.331 [3]:

-indicate the data available for transmission to the MAC entity configured for SCG only;

-if ul-DataSplitThreshold is configured, indicate the data available for transmission as 0 to the MAC entity configured for MCG.

-else:

-indicate the data available for transmission to the MAC entity configured for MCG only;

-if ul-DataSplitThreshold is configured, indicate the data available for transmission as 0 to the MAC entity configured for SCG.

-else:

-indicate the data available for transmission to the MAC entity.

For DAPS bearers, when indicating the data available for transmission to the MAC entity for BSR triggering and Buffer Size calculation, the UE shall:

-if the uplink data switching has not been requested by upper layers:

-indicate the data available for transmission to the MAC entity associated with the source cell;

-else:

-indicate the data available for transmission excluding the PDCP Control PDU for interspersed ROHC feedback associated with the source cell to the MAC entity associated with the target cell;

-indicate the data available for transmission of PDCP Control PDU for interspersed ROHC feedback associated with the source cell to the MAC entity assocaited with the source cell.

## 5PDCP procedures

## 5.1PDCP Data Transfer Procedures

## 5.1.1UL Data Transfer Procedures

At reception of a PDCP SDU from upper layers, the UE shall:

-start the discardTimer associated with this PDCP SDU (if configured);

For a PDCP SDU received from upper layers, the UE shall:

-associate the PDCP SN corresponding to Next_PDCP_TX_SN to this PDCP SDU;

NOTE:Associating more than half of the PDCP SN space of contiguous PDCP SDUs with PDCP SNs, when e.g., the PDCP SDUs are discarded or transmitted without acknowledgement, may cause HFN desynchronization problem. How to prevent HFN desynchronization problem is left up to UE implementation.

-perform header compression of the PDCP SDU (if configured) using ROHC as specified in the clause 5.5.4 and/or using EHC as specified in the clause 5.14.4;

-perform compression of the uplink PDCP SDU (if configured) as specified in the clause 5.11.4;

-perform integrity protection (if applicable), and ciphering (if applicable) using COUNT based on TX_HFN and the PDCP SN associated with this PDCP SDU as specified in the clause 5.7 and 5.6, respectively;

-increment Next_PDCP_TX_SN by one;

-if Next_PDCP_TX_SN > Maximum_PDCP_SN:

-set Next_PDCP_TX_SN to 0;

-increment TX_HFN by one;

-if PDCP duplication is activated for the corresponding bearer:

-submit a duplicate of the resulting PDCP Data PDU to lower layer.

-submit the resulting PDCP Data PDU to lower layer.

## 5.1.2DL Data Transfer Procedures

## 5.1.2.1Procedures for DRBs

## 5.1.2.1.1Void

## 5.1.2.1.2Procedures for DRBs mapped on RLC AM when the reordering function is not used

For DRBs mapped on RLC AM, when the reordering function is not used, at reception of a PDCP Data PDU from lower layers, the UE shall:

-if received PDCP SN – Last_Submitted_PDCP_RX_SN > Reordering_Window or 0 <= Last_Submitted_PDCP_RX_SN – received PDCP SN < Reordering_Window:

-if received PDCP SN > Next_PDCP_RX_SN:

-decipher the PDCP PDU as specified in the clause 5.6, using COUNT based on RX_HFN - 1 and the received PDCP SN;

-else:

-decipher the PDCP PDU as specified in the clause 5.6, using COUNT based on RX_HFN and the received PDCP SN;

-perform header decompression (if configured) using ROHC as specified in the clause 5.5.5 and/or using EHC as specified in the clause 5.14.5;

-discard this PDCP SDU;

-else if Next_PDCP_RX_SN – received PDCP SN > Reordering_Window:

-increment RX_HFN by one;

-use COUNT based on RX_HFN and the received PDCP SN for deciphering the PDCP PDU;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-else if received PDCP SN – Next_PDCP_RX_SN >= Reordering_Window:

-use COUNT based on RX_HFN – 1 and the received PDCP SN for deciphering the PDCP PDU;

-else if received PDCP SN >= Next_PDCP_RX_SN:

-use COUNT based on RX_HFN and the received PDCP SN for deciphering the PDCP PDU;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-if Next_PDCP_RX_SN is larger than Maximum_PDCP_SN:

-set Next_PDCP_RX_SN to 0;

-increment RX_HFN by one;

-else if received PDCP SN < Next_PDCP_RX_SN:

-use COUNT based on RX_HFN and the received PDCP SN for deciphering the PDCP PDU;

-if the PDCP PDU has not been discarded in the above:

-perform deciphering (if configured) for the PDCP PDU as specified in the clauses 5.6;

-perform header decompression (if configured) for the PDCP PDU using ROHC as specified in the clause 5.5.5 and/or using EHC as specified in the clause 5.14.5;

-if a PDCP SDU with the same PDCP SN is stored:

-discard this PDCP SDU;

-else:

-store the PDCP SDU;

-if the PDCP PDU received by PDCP is not due to the re-establishment of lower layers:

-deliver to upper layers in ascending order of the associated COUNT value:

-all stored PDCP SDU(s) with an associated COUNT value less than the COUNT value associated with the received PDCP SDU;

-all stored PDCP SDU(s) with consecutively associated COUNT value(s) starting from the COUNT value associated with the received PDCP SDU;

-set Last_Submitted_PDCP_RX_SN to the PDCP SN of the last PDCP SDU delivered to upper layers;.

-else if received PDCP SN = Last_Submitted_PDCP_RX_SN + 1 or received PDCP SN = Last_Submitted_PDCP_RX_SN – Maximum_PDCP_SN:

-deliver to upper layers in ascending order of the associated COUNT value:

-all stored PDCP SDU(s) with consecutively associated COUNT value(s) starting from the COUNT value associated with the received PDCP SDU;

-set Last_Submitted_PDCP_RX_SN to the PDCP SN of the last PDCP SDU delivered to upper layers.

## 5.1.2.1.2aRN procedures for DRBs mapped on RLC AM

For DRBs mapped on RLC AM, at reception of a PDCP Data PDU from lower layers, the RN should follow the procedures specified for a UE in 5.1.2.1.2 with the addition that for DRBs for which integrity verification is configured, the RN should, immediately after performing deciphering as specified in 5.6, also perform integrity verification as specified in 5.7 with the same COUNT value as used for deciphering.

In case of integrity verification failure, the RN should discard the PDCP Data PDU without performing header decompression and without delivering any stored PDCP SDU(s) to upper layers. The RN should also set the RX_HFN, Next_PDCP_RX_SN and Last_Submitted_PDCP_RX_SN to the respective values they had before the reception of the PDCP Data PDU.

## 5.1.2.1.3Procedures for DRBs mapped on RLC UM when the reordering function is not used

For DRBs mapped on RLC UM, at reception of a PDCP Data PDU from lower layers, the UE shall:

-if received PDCP SN < Next_PDCP_RX_SN:

-increment RX_HFN by one;

-decipher the PDCP Data PDU using COUNT based on RX_HFN and the received PDCP SN as specified in the clause 5.6;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-if Next_PDCP_RX_SN > Maximum_PDCP_SN:

-set Next_PDCP_RX_SN to 0;

-increment RX_HFN by one;

-perform header decompression (if configured) of the deciphered PDCP Data PDU using ROHC as specified in the clause 5.5.5 and/or using EHC as specified in the clause 5.14.5;

-deliver the resulting PDCP SDU to upper layer.

## 5.1.2.1.3aRN procedures for DRBs mapped on RLC UM

For DRBs mapped on RLC UM, at reception of a PDCP Data PDU from lower layers, the RN should follow the procedures specified for a UE in 5.1.2.1.3 with the addition that for DRBs for which integrity verification is configured, the RN should, immediately after performing deciphering as specified in 5.6, also perform integrity verification as specified in 5.7 with the same COUNT value as used for deciphering.

In case of integrity verification failure, the RN should discard the PDCP Data PDU without performing header decompression and set the RX_HFN and Next_PDCP_RX_SN to the respective values they had before the reception of the PDCP Data PDU.

## 5.1.2.1.4Procedures for DRBs mapped on RLC AM or RLC UM, for LWA bearers and SLRB when the reordering function is used

For DRBs mapped on RLC AM and RLC UM, for LWA bearers and when PDCP duplication is used, the PDCP entity shall use the reordering function as specified in this clause when:

-the PDCP entity is associated with two RLC entities; or

-the PDCP entity is configured for a LWA bearer; or

-the PDCP entity is associated with one AM RLC entity after it was, according to the most recent reconfiguration, associated with two AM RLC entities or configured for a LWA bearer without performing PDCP re-establishment; or

-the PDCP entity is configured with PDCP duplication; or

-the PDCP entity is configured for a DAPS bearer; or

-the PDCP entity is not configured for a DAPS bearer after it was, according to the most recent reconfiguration, configured for a DAPS bearer; or

-the PDCP entity is associated with at least one RLC entity configured with rlc-OutOfOrderDelivery.

For SLRBs mapped on RLC UM, the PDCP entity shall use the reordering function as specified in this clause when:

-the PDCP entity receives a PDCP SN which is not "0".

The PDCP entity shall not use the reordering function in other cases.

## 5.1.2.1.4.1Procedures when a PDCP PDU is received from the lower layers

For DRBs mapped on RLC AM or RLC UM, SLRB and for LWA bearers, or for DRBs and SRBs when PDCP duplication is used, when the reordering function is used, at reception of a PDCP Data PDU from lower layers, the UE shall:

-if received PDCP SN – Last_Submitted_PDCP_RX_SN > Reordering_Window or 0 <= Last_Submitted_PDCP_RX_SN – received PDCP SN < Reordering_Window:

-if the PDCP PDU was received on WLAN:

-if received PDCP SN > Next_PDCP_RX_SN:

-for the purpose of setting the HRW field in the LWA status report, use COUNT based on RX_HFN - 1 and the received PDCP SN;

-else:

-for the purpose of setting the HRW field in the LWA status report, use COUNT based on RX_HFN and the received PDCP SN;

-if received PDCP SN > Next_PDCP_RX_SN:

-decipher the PDCP PDU as specified in the clause 5.6, and perform integrity verification of the PDCP Data PDU (if applicable) using COUNT based on RX_HFN - 1 and the received PDCP SN.

-else:

-decipher the PDCP PDU as specified in the clause 5.6, and perform integrity verification of the PDCP Data PDU (if applicable) using COUNT based on RX_HFN and the received PDCP SN.

-if integrity verification fails:

-indicate the integrity verification failure to upper layer.

-discard the PDCP PDU;

-else if Next_PDCP_RX_SN – received PDCP SN > Reordering_Window:

-increment RX_HFN by one;

-use COUNT based on RX_HFN and the received PDCP SN for deciphering and integrity verification (if applicable) of the PDCP PDU;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-else if received PDCP SN – Next_PDCP_RX_SN >= Reordering_Window:

-use COUNT based on RX_HFN – 1 and the received PDCP SN for deciphering and integrity verification (if applicable) of the PDCP PDU.

-else if received PDCP SN >= Next_PDCP_RX_SN:

-use COUNT based on RX_HFN and the received PDCP SN for deciphering and integrity verification (if applicable) of the PDCP PDU;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-if Next_PDCP_RX_SN is larger than Maximum_PDCP_SN:

-set Next_PDCP_RX_SN to 0;

-increment RX_HFN by one.

-else if received PDCP SN < Next_PDCP_RX_SN:

-use COUNT based on RX_HFN and the received PDCP SN for deciphering and integrity verification of the PDCP PDU;

-if the PDCP PDU has not been discarded in the above:

-if a PDCP SDU with the same PDCP SN is stored:

-perform deciphering and integrity verification (if applicable) of the PDCP PDU;

-if integrity verification fails:

-indicate the integrity verification failure to upper layer.

-discard the PDCP PDU;

-else:

-perform deciphering and integrity verification (if applicable) of the PDCP PDU and store the resulting PDCP SDU;

-if integrity verification fails:

-indicate the integrity verification failure to upper layer;

-discard the PDCP Data PDU.

-if the PDCP PDU has not been discarded in the above:

-if received PDCP SN = Last_Submitted_PDCP_RX_SN + 1 or received PDCP SN = Last_Submitted_PDCP_RX_SN – Maximum_PDCP_SN:

-deliver to upper layers in ascending order of the associated COUNT value after performing header decompression (if configured) using ROHC as specified in the clause 5.5.5 and/or using EHC as specified in the clause 5.14.5:

-all stored PDCP SDU(s) with consecutively associated COUNT value(s) starting from the COUNT value associated with the received PDCP PDU;

-set Last_Submitted_PDCP_RX_SN to the PDCP SN of the last PDCP SDU delivered to upper layers;

-if t-Reordering is running:

-if the PDCP SDU with Reordering_PDCP_RX_COUNT – 1 has been delivered to upper layers:

-stop and reset t-Reordering;

-if t-Reordering is not running (includes the case when t-Reordering is stopped due to actions above):

-if there is at least one stored PDCP SDU:

-start t-Reordering;

-set Reordering_PDCP_RX_COUNT to the COUNT value associated to RX_HFN and Next_PDCP_RX_SN.

## 5.1.2.1.4.2Procedures when t-Reordering expires

When t-Reordering expires, the UE shall:

-deliver to upper layers in ascending order of the associated COUNT value after performing header decompression (if configured) using ROHC as specified in the clause 5.5.5 and/or using EHC as specified in the clause 5.14.5:

-all stored PDCP SDU(s) with associated COUNT value(s) less than Reordering_PDCP_RX_COUNT;

-all stored PDCP SDU(s) with consecutively associated COUNT value(s) starting from Reordering_PDCP_RX_COUNT;

-set Last_Submitted_PDCP_RX_SN to the PDCP SN of the last PDCP SDU delivered to upper layers;

-if there is at least one stored PDCP SDU:

-start t-Reordering;

-set Reordering_PDCP_RX_COUNT to the COUNT value associated to RX_HFN and Next_PDCP_RX_SN.

## 5.1.2.1.4.3Procedures when the value of t-Reordering is reconfigured

When the value of the t-Reordering is reconfigured by upper layers while the t-Reordering is running, the UE shall:

-stop and restart t-Reordering;

-set Reordering_PDCP_RX_COUNT to the COUNT value associated to RX_HFN and Next_PDCP_RX_SN.

## 5.1.2.2Procedures for SRBs

## 5.1.2.2.1Procedures for SRBs when the reordering function is not used

For SRBs, at reception of a PDCP Data PDU from lower layers, the UE shall:

-if received PDCP SN < Next_PDCP_RX_SN:

-decipher and verify the integrity of the PDU (if applicable) using COUNT based on RX_HFN + 1 and the received PDCP SN as specified in the clauses 5.6 and 5.7, respectively;

-else:

-decipher and verify the integrity of the PDU (if applicable) using COUNT based on RX_HFN and the received PDCP SN as specified in the clauses 5.6 and 5.7, respectively;

-if integrity verification is applicable and the integrity verification is passed successfully; or

-if integrity verification is not applicable:

-if received PDCP SN < Next_PDCP_RX_SN:

-increment RX_HFN by one;

-set Next_PDCP_RX_SN to the received PDCP SN + 1;

-if Next_PDCP_RX_SN > Maximum_PDCP_SN:

-set Next_PDCP_RX_SN to 0;

-increment RX_HFN by one;

-deliver the resulting PDCP SDU to upper layer;

-else, if integrity verification is applicable and the integrity verification fails:

-discard the received PDCP Data PDU;

-indicate the integrity verification failure to upper layer.

## 5.1.2.2.2Procedures for SRBs when the reordering function is used

For SRBs, the PDCP entity shall use the reordering function when:

-the PDCP entity is configured with PDCP duplication.

For SRBs, when the reordering function is used, at reception of a PDCP Data PDU from lower layers, the UE shall follow the procedures in clause 5.1.2.1.4.1.

## 5.1.3SL Data Transmission Procedures

For Sidelink transmission of the SLRB for which SL-V2X-TxProfile is not configured or configured as rel14, see TS 36.331 [3], the UE shall follow the procedures in clause 5.1.1 with following modifications:

-the requirement for maintaining Next_PDCP_TX_SN is not applicable;

-determine a PDCP SN ensuring that a PDCP SN value is not reused with the same key;

-perform ciphering (if configured) as specified in clause 5.6.1 and 5.6.2;

-perform the header compression (if configured) using ROHC if SDU Type is set to 000, i.e. IP SDUs.

For sidelink transmission of the SLRBs for which the indicated SL-V2X-TxProfile is rel15, see TS 36.331 [3], the UE shall follow the procedures in clause 5.1.1 with following modifications compared to above Sidelink transmission procedure:

-the requirement for maintaining Next_PDCP_TX_SN is applicable;

-for the SLRBs associated to packets which have PPPR value lower than the configured PPPR threshold threshSL-Reliability, see TS 36.331 [3], the PDCP entity duplicates the PDCP PDUs, and submits the PDCP PDUs to both associated RLC entities.

For sidelink transmission, the requirement for maintaining TX_HFN is not applicable.

## 5.1.4SL Data Reception Procedures

For Sidelink reception, the UE shall follow the procedures in clause 5.1.2.1.3 with following modifications, except if it receives a PDCP SN which is not "0":

-the requirements for maintaining Next_PDCP_RX_SN and RX_HFN are not applicable;

-perform the deciphering (if configured) as specified in clause 5.6.1 and 5.6.2;

-perform the header decompression (if configured) using ROHC if SDU Type is set to 000, i.e. IP SDUs.

Otherwise, if the UE receives a PDCP SN which is not "0", the Sidelink reception of the UE shall follow the procedures in clause 5.1.2.1.4.1 with following modifications compared to above Sidelink reception procedure:

-the requirements for maintaining Next_PDCP_RX_SN and RX_HFN are applicable;

-perform the re-ordering procedure as specified in clause 5.1.2.1.4.1.

## 5.2Re-establishment procedure

When upper layers request a PDCP re-establishment, the UE shall additionally perform once the procedures described in this clause for the corresponding RLC mode. After performing the procedures in this clause, the UE shall follow the procedures in clause 5.1.

## 5.2.1UL Data Transfer Procedures

For LWA bearers, the UE shall use the procedures corresponding to the associated RLC entity below.

## 5.2.1.1Procedures for DRBs mapped on RLC AM

When upper layers request a PDCP re-establishment, the UE shall:

-reset the ROHC protocol for uplink and start with an IR state in U-mode (if configured) [9] [11], except if upper layers indicate stored UE AS context is used and drb-ContinueROHC is configured, see TS 36.331 [3];

-reset the EHC protocol for uplink (if configured) if drb-ContinueEHC-UL is not configured, see TS 36.331 [3];

-reset the compression buffer to all zeros (if configured) and prefill the dictionary (if configured) as specified in clause 5.11.5;

-if connected as an RN, apply the integrity protection algorithm and key provided by upper layers (if configured) during the re-establishment procedure;

-if upper layers indicate stored UE AS context is used, set Next_PDCP_TX_SN, and TX_HFN to 0;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure;

-for LWA bearers, consider all PDCP SDUs submitted to the LWAAP entity as successfully delivered;

-from the first PDCP SDU for which the successful delivery of the corresponding PDCP PDU has not been confirmed by lower layers, perform retransmission or transmission of all the PDCP SDUs already associated with PDCP SNs in ascending order of the COUNT values associated to the PDCP SDU prior to the PDCP re-establishment as specified below:

-perform header compression of the PDCP SDU (if configured) using ROHC as specified in the clause 5.5.4 and/or using EHC as specified in the clause 5.14.4;

-perform compression of the uplink PDCP SDU (if configured) as specified in the clause 5.11.4;

-if connected as an RN, perform integrity protection (if configured) of the PDCP SDU using the COUNT value associated with this PDCP SDU as specified in the clause 5.7;

-perform ciphering of the PDCP SDU using the COUNT value associated with this PDCP SDU as specified in the clause 5.6;

-submit the resulting PDCP Data PDU to lower layer. If PDCP duplication is activated, duplicate the resulting PDCP Data PDUs and submit the PDCP Data PDUs to both associated RLC entities.

## 5.2.1.2Procedures for DRBs mapped on RLC UM

When upper layers request a PDCP re-establishment, the UE shall:

-reset the ROHC protocol for uplink and start with an IR state in U-mode [9] [11] if the DRB is configured with the ROHC protocol and drb-ContinueROHC is not configured, see TS 36.331 [3];

-reset the EHC protocol for uplink (if configured) if drb-ContinueEHC-UL is not configured, see TS 36.331 [3];

-set Next_PDCP_TX_SN, and TX_HFN to 0;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure;

-if connected as an RN, apply the integrity protection algorithm and key provided by upper layers (if configured) during the re-establishment procedure;

-for each PDCP SDU already associated with a PDCP SN but for which a corresponding PDU has not previously been submitted to lower layers:

-consider the PDCP SDUs as received from upper layer;

-perform transmission of the PDCP SDUs in ascending order of the COUNT value associated to the PDCP SDU prior to the PDCP re-establishment, as specified in the clause 5.1.1 without restarting the discardTimer.

## 5.2.1.3Procedures for SRBs

When upper layers request a PDCP re-establishment, the UE shall:

-set Next_PDCP_TX_SN, and TX_HFN to 0;

-discard all stored PDCP SDUs and PDCP PDUs;

-apply the ciphering and integrity protection algorithms and keys provided by upper layers during the re-establishment procedure.

## 5.2.2DL Data Transfer Procedures

## 5.2.2.1Procedures for DRBs mapped on RLC AM while the reordering function is not used

When upper layers request a PDCP re-establishment while the reordering function is not used, the UE shall:

-process the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers, as specified in the clause 5.1.2.1.2;

-reset the ROHC protocol for downlink and start with NC state in U-mode (if configured) [9] [11], except if upper layers indicate stored UE AS context is used and drb-ContinueROHC is configured,see TS 36.331 [3];

-reset the EHC protocol for downlink (if configured) if drb-ContinueEHC-DL is not configured, see TS 36.331 [3];

-if upper layers indicate stored UE AS context is used, set Next_PDCP_RX_SN, RX_HFN to 0 and Last_submitted_PDCP_RX_SN to Maximum_PDCP_SN;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure.

-if connected as an RN, apply the integrity protection algorithm and key provided by upper layers (if configured) during the re-establishment procedure.

## 5.2.2.1aProcedures for DRBs mapped on RLC AM while the reordering function is used

When upper layers request a PDCP re-establishment while the reordering function is used, the UE shall:

-process the PDCP Data PDU(s) that are received from lower layers due to the re-establishment of the lower layers, as specified in the clause 5.1.2.1.4;

-if the PDCP entity is to be associated with one AM RLC entity after PDCP re-establishment:

-stop and reset t-Reordering;

-if the PDCP entity is associated with at least one RLC entity configured with rlc-OutOfOrderDelivery:

-perform header decompression (if configured) using EHC for all stored PDCP SDUs if drb-ContinueEHC-DL is not configured in TS 36.331 [3];

-reset the EHC protocol for downlink (if configured) if drb-ContinueEHC-DL is not configured, see TS 36.331 [3];

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure.

## 5.2.2.2Procedures for DRBs mapped on RLC UM when the reordering function is not used

When upper layers request a PDCP re-establishment, the UE shall:

-process the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers, as specified in the clause 5.1.2.1.3;

-reset the ROHC protocol for downlink and start with NC state in U-mode [9] [11] if the DRB is configured with the ROHC protocol and drb-ContinueROHC is not configured, see TS 36.331 [3];

-reset the EHC protocol for downlink (if configured) if drb-ContinueEHC-DL is not configured, see TS 36.331 [3];

-set Next_PDCP_RX_SN, and RX_HFN to 0;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure.

-if connected as an RN, apply the integrity protection algorithm and key provided by upper layers (if configured) during the re-establishment procedure.

## 5.2.2.2aProcedures for DRBs mapped on RLC UM when the reordering function is used

When upper layers request a PDCP re-establishment when the reordering function is used, the UE shall:

-process the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers, as specified in the clause 5.1.2.1.4;

-stop and reset t-Reordering, if running;

-deliver all stored PDCP SDUs, if any, to upper layers in ascending order of associated COUNT values after performing header decompression using EHC (if configured) as specified in the clause 5.14.5;

-if the PDCP entity is associated with at least one RLC entity configured with rlc-OutOfOrderDelivery:

-reset the EHC protocol for downlink (if configured) if drb-ContinueEHC-DL is not configured, see TS 36.331 [3];

-set Next_PDCP_RX_SN, and RX_HFN to 0 and Last_submitted_PDCP_RX_SN to Maximum_PDCP_SN;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure.

## 5.2.2.3Procedures for SRBs

When upper layers request a PDCP re-establishment, the UE shall:

-discard the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers;

-set Next_PDCP_RX_SN, and RX_HFN to 0;

-discard all stored PDCP SDUs and PDCP PDUs;

-apply the ciphering and integrity protection algorithms and keys provided by upper layers during the re-establishment procedure.

## 5.2.2.4Procedures for LWA bearers

When upper layers request a PDCP re-establishment, the UE shall:

-process the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers, as specified in the clause 5.1.2.1.4;

-stop and reset t-Reordering, if running;

-if the PDCP entity is associated with UM RLC entity:

-deliver all stored PDCP SDUs, if any, to upper layers in ascending order of associated COUNT values;

-set Next_PDCP_RX_SN, RX_HFN to 0 and Last_submitted_PDCP_RX_SN to Maximum_PDCP_SN;

-apply the ciphering algorithm and key provided by upper layers during the re-establishment procedure.

## 5.3PDCP Status Report

## 5.3.1Transmit operation

When upper layers request a PDCP re-establishment or PDCP Data Recovery; or when PDCP status report is triggered by polling or periodic reporting; or when PDCP status report is triggered by WLAN Connection Status Reporting of temporary unavailability (suspended, see TS 36.331 [3]); or when upper layers request uplink data switching during DAPS handover, or when upper layers reconfigure the PDCP entity to release DAPS and daps-SourceRelease is configured in TS 36.331 [3], for radio bearers that are mapped on RLC AM, or when upper layers request uplink data switching during DAPS handover for radio bearers that are mapped on RLC UM, the UE shall:

-if the radio bearer is configured by upper layers to send a PDCP status report in the uplink (statusReportRequired, see TS 36.331 [3]) or the status report is triggered by PDCP status report polling or PDCP periodic status reporting or the status report is triggered by WLAN Connection Status Reporting of temporary unavailability (suspended, see TS 36.331 [3]) when wlan-SuspendTriggersStatusReport is configured, see TS 36.331 [3], compile a status report as indicated below after processing the PDCP Data PDUs that are received from lower layers due to the re-establishment of the lower layers as specified in the clause 5.2.2.1, and submit it to lower layers as the first PDCP PDU for the transmission, by:

-setting the FMS field to the PDCP SN of the first missing PDCP SDU;

-if there is at least one out-of-sequence PDCP SDU stored, allocating a Bitmap field of length in bits equal to the number of PDCP SNs from and not including the first missing PDCP SDU up to and including the last out-of-sequence PDCP SDUs, rounded up to the next multiple of 8, or up to and including a PDCP SDU for which the resulting PDCP Control PDU size is equal to 8188 bytes, whichever comes first;

-setting as '0' in the corresponding position in the bitmap field for all PDCP SDUs that have not been received as indicated by lower layers, and optionally PDCP SDUs for which decompression have failed;

-indicating in the bitmap field as '1' for all other PDCP SDUs.

## 5.3.2Receive operation

When a PDCP status report is received in the downlink, for radio bearers that are mapped on RLC AM:

-for each PDCP SDU, if any, with the bit in the bitmap set to '1', or with the associated COUNT value less than the COUNT value of the PDCP SDU identified by the FMS field, the successful delivery of the corresponding PDCP SDU is confirmed, and the UE shall process the PDCP SDU as specified in the clause 5.4.

PDCP status report receive operation is not applicable in NB-IoT.

## 5.4PDCP discard

When the discardTimer expires for a PDCP SDU, or the successful delivery of a PDCP SDU is confirmed by PDCP status report or LWA status report, the UE shall discard the PDCP SDU along with the corresponding PDCP PDU. If the corresponding PDCP PDU has already been submitted to lower layers, the discard is indicated to lower layers.

NOTE:For split and LWA bearers, discarding a PDCP SDU already associated with a PDCP SN causes a SN gap in the transmitted PDCP PDUs, which increases PDCP reordering delay in the receiving PDCP entity. It is up to UE implementation how to minimize SN gap after SDU discard.

## 5.4aDuplicate PDCP discard

For the transmitting PDCP entity associated with two RLC entities, the transmitting PDCP entity shall:

-if the successful delivery of a PDCP Data PDU is confirmed by one of the two associated RLC entities:

-discard the PDCP Data PDU and indicate to the other RLC entity to discard the duplicated PDCP Data PDU.

-if the deactivation of PDCP duplication is indicated:

-if the two associated RLC entities belong to the different cell groups:

-if ul-DataSplitDRB-ViaSCG is set to TRUE by upper layer, see TS 36.331 [3]:

-indicate to the MCG RLC entity to discard all duplicated PDCP Data PDUs.

-else:

-indicate to the SCG RLC entity to discard all duplicated PDCP Data PDUs.

-else:

-indicate to the secondary RLC entity to discard all duplicated PDCP Data PDUs.

## 5.5Robust Header Compression and Decompression

## 5.5.1Supported header compression protocols and profiles

The ROHC protocol is based on the Robust Header Compression (ROHC) framework [7]. There are multiple ROHC algorithms, called profiles, defined for the ROHC framework. Each profile is specific to the particular network layer, transport layer or upper layer protocol combination e.g. TCP/IP and RTP/UDP/IP.

The detailed definition of the ROHC channel is specified as part of the ROHC framework in RFC 5795 [7]. This includes how to multiplex different flows (header compressed or not) over the ROHC channel, as well as how to associate a specific IP flow with a specific context state during initialization of the compression algorithm for that flow.

The implementation of the functionality of the ROHC framework and of the functionality of the supported ROHC profiles is not covered in this specification.

In this version of the specification the support of the following profiles is described:

Table 5.5.1.1: Supported ROHC protocols and profiles

## 5.5.2Configuration of ROHC

PDCP entities associated with DRBs can be configured by upper layers, see TS 36.331 [3] to use ROHC either bidirectional (if headerCompression is configured) or uplink-only (if uplinkOnlyHeaderCompression is configured). If uplinkOnlyHeaderCompression is configured, the UE shall process the received PDCP Control PDU for interspersed ROHC feedback packet corresponding to the uplink ROHC as specified in clause 5.5.6.2, but shall not perform ROHC for the received PDCP Data PDU. PDCP entities associated with SLRBs can be configured to use ROHC for IP SDUs.

## 5.5.3Protocol parameters

RFC 5795 has configuration parameters that are mandatory and that must be configured by upper layers between compressor and decompressor peers [7]; these parameters define the ROHC channel. The ROHC channel is a unidirectional channel, i.e. there is one channel for the downlink, and one for the uplink if headerCompression is configured, and there is only one channel for the uplink if uplinkOnlyHeaderCompression is configured. There is thus one set of parameters for each channel, and the same values shall be used for both channels belonging to the same PDCP entity if headerCompression is configured.

These parameters are categorized in two different groups, as defined below:

-M:Mandatory and configured by upper layers.

-N/A: Not used in this specification.

The usage and definition of the parameters shall be as specified below.

-MAX_CID (M): This is the maximum CID value that can be used. One CID value shall always be reserved for uncompressed flows. The parameter MAX_CID is configured by upper layers (maxCID, see TS 36.331 [3]).

-LARGE_CIDS: This value is not configured by upper layers, but rather it is inferred from the configured value of MAX_CID according to the following rule:

If MAX_CID > 15 then LARGE_CIDS = TRUE else LARGE_CIDS = FALSE.

-PROFILES (M): Profiles are used to define which profiles are allowed to be used by the UE. The list of supported profiles is described in clause 5.5.1. The parameter PROFILES is configured by upper layers (profiles for uplink and downlink, rohc-Profiles in SL-Preconfiguration or SL-V2X-Preconfiguration for sidelink, see TS 36.331 [3]).

-FEEDBACK_FOR (N/A): This is a reference to the channel in the opposite direction between two compression endpoints and indicates to what channel any feedback sent refers to. Feedback received on one ROHC channel for this PDCP entity shall always refer to the ROHC channel in the opposite direction for this same PDCP entity.

-MRRU (N/A): ROHC segmentation is not used.

## 5.5.4Header compression using ROHC

The ROHC protocol generates two types of output packets:

-ROHC compressed packets, each associated with one PDCP SDU

-standalone packets not associated with a PDCP SDU, i.e. interspersed ROHC feedback packets

A ROHC compressed packet is associated with the same PDCP SN and COUNT value as the related PDCP SDU.

For DAPS bearers, the PDCP entity shall perform the header compression for the PDCP SDU using the ROHC protocol either configured for the source cell or configured for the target cell, based on to which cell the PDCP SDU is transmitted.

Interspersed ROHC feedback packets are not associated with a PDCP SDU. They are not associated with a PDCP SN and are not ciphered.

NOTE 1:If the MAX_CID number of ROHC contexts are already established for the compressed flows and a new IP flow does not match any established ROHC context, the compressor should associate the new IP flow with one of the ROHC CIDs allocated for the existing compressed flows or send PDCP SDUs belonging to the IP flow as uncompressed packet.

NOTE 2:For downlink, the ROHC protocol of the target cell should maintain the IR state if operating in U-mode and O-mode during DAPS handover before release of source cell.

## 5.5.5Header decompression using ROHC

If ROHC is configured by upper layers for PDCP entities associated with u-plane data the PDCP PDUs are de-compressed by the ROHC protocol after performing deciphering as explained in the clause 5.6.

For DAPS bearers, the PDCP entity shall perform the header decompression for the PDCP SDU using the ROHC protocol either configured for the source cell or configured for the target cell, based on from which cell the PDCP SDU is received.

## 5.5.6PDCP Control PDU for interspersed ROHC feedback packet

## 5.5.6.1Transmit Operation

When an interspersed ROHC feedback packet is generated by the ROHC protocol, the UE shall:

-submit to lower layers the corresponding PDCP Control PDU as specified in clause 6.2.5 i.e. without associating a PDCP SN, nor performing ciphering.

## 5.5.6.2Receive Operation

At reception of a PDCP Control PDU for interspersed ROHC feedback packet from lower layers, the UE shall:

-deliver the corresponding interspersed ROHC feedback packet to the associated header compression protocol without performing deciphering.

## 5.6Ciphering and Deciphering

## 5.6.0General

The ciphering function includes both ciphering and deciphering and is performed in PDCP. For the control plane, the data unit that is ciphered is the data part of the PDCP PDU (see clause 6.3.3) and the MAC-I (see clause 6.3.4). For the user plane, the data unit that is ciphered is the data part of the PDCP PDU (see clause 6.3.3); ciphering is not applicable to PDCP Control PDUs.

For RNs, for the user plane, in addition to the data part of the PDCP PDU, the MAC-I (see 6.3.4) is also ciphered if integrity protection is configured.

The ciphering algorithm and key to be used by the PDCP entity are configured by upper layers, see TS 36.331 [3] and the ciphering method shall be applied as specified in TS 33.401 [6].

The ciphering function is activated/suspended/resumed by upper layers (TS 36.331 [3]). When security is activated and not suspended, the ciphering function shall be applied to all PDCP PDUs indicated by upper layers, see TS 36.331 [3], for the downlink and the uplink, respectively.

NOTE:Security is suspended upon connection suspension (and resumed upon connection resumption).

For DAPS bearers, the PDCP entity shall perform the ciphering or deciphering for the PDCP SDU using the ciphering algorithm and key either configured for the source cell or configured for the target cell, based on to/from which cell the PDCP SDU is transmitted/received.

For downlink and uplink ciphering and deciphering, the parameters that are required by PDCP for ciphering are defined in TS 33.401 [6] and are input to the ciphering algorithm. The required inputs to the ciphering function include the COUNT value, and DIRECTION (direction of the transmission: set as specified in TS 33.401 [6]).The parameters required by PDCP which are provided by upper layers, see TS 36.331 [3], are listed below:

-BEARER (defined as the radio bearer identifier in TS 33.401 [6]. It will use the value RB identity –1 as in TS 36.331 [3]);

-KEY (the ciphering keys for the control plane and for the user plane are KRRCenc and KUPenc, respectively).

## 5.6.1SL Ciphering and Deciphering for one-to-many communication

For SLRB used for one-to-many communication, the ciphering function includes both ciphering and deciphering and is performed in PDCP as defined in TS 33.303 [13]. The data unit that is ciphered is the data part of the PDCP PDU (see clause 6.3.3). The ciphering function as specified in TS 33.401 [6] is applied with KEY (PEK), COUNT (derived from PTK Identity and PDCP SN as specified in TS 33.303 [13]), BEARER and DIRECTION (set to 0) as input. The ciphering function is configured by ProSe Function.

If ciphering is configured, the ciphering algorithm and related parameters including PGK, PGK Identity, and Group Member Identity are configured to the UE by ProSe Key Management Function. The UE shall set PTK Identity based on PGK, PGK Identity, and PDCP SN as specified in TS 33.303 [13]. The UE shall derive PTK from PGK using PTK Identity and Group Member Identity, and derive PEK from PTK using the ciphering algorithm. The PGK Index, PTK Identity, and PDCP SN are included in the PDCP PDU header.

If ciphering is not configured, PGK Index and PTK Identity shall be set to "0" in the PDCP PDU header.

If ciphering is not configured, for the SLRB for which SL-V2X-TxProfile is not configured or configured as rel14 (see TS 36.331 [3]), PDCP SN shall be set to "0" in the PDCP PDU header.

If ciphering is not configured, for the SLRB of which the indicated SL-V2X-TxProfile is rel15 (see TS 36.331 [3]), PDCP SN shall not be set to "0" in the PDCP PDU header.

## 5.6.2SL Ciphering and Deciphering for one-to-one communication

For SLRB used for one-to-one communication, the ciphering function includes both ciphering and deciphering and is performed in PDCP of SLRB that needs ciphering and deciphering as defined in TS 33.303 [13]. The data unit that is ciphered is the data part of the PDCP PDU (see clause 6.3.3). The ciphering function as specified in TS 33.401 [6] is applied with KEY (PEK), COUNT (derived from KD-sess Identity and PDCP SN as specified in TS 33.303 [13]), BEARER and DIRECTION (which value shall be set is specified in TS 33.303 [13]) as input.

For the SLRB that needs ciphering and deciphering, the UE shall derive the KEY (PEK) based on KD-sess and the algorithms determined by the initiating UE and the receiving UE as specified in TS 33.303 [13]. The KD-sess Identity and PDCP SN are included in the PDCP PDU header.

For the SLRB that does not need ciphering and deciphering, the UE shall set KD-sess Identity to "0" in the PDCP PDU header.

## 5.6.3Handling of LWA end-marker PDCP Control PDU

## 5.6.3.1Transmit operation

When upper layers request a PDCP re-establishment for a LWA bearer mapped on RLC AM where LWA configuration is retained with the same WT (handoverWithoutWT-Change, see TS 36.331 [3]), the UE shall:

-compile a LWA end-marker PDCP Control PDU by setting the LSN field to the PDCP SN of the last PDCP Data PDU for which the PDCP SN has been associated, and submit it to lower layers as the next PDCP PDU for the transmission after the PDCP Data PDU corresponding to LSN has been submitted to lower layers;

NOTE 1:Whether to submit the LWA end-marker PDCP Control PDU to RLC entity or LWAAP entity is left up to the UE implementation.

NOTE 2:The UE is expected to ensure the successful transmission of the LWA end-marker PDCP Control PDU e.g., using repeated transmission of the same LWA end-marker PDCP Control PDU.

-start using the key provided by upper layers during the re-establishment procedure for the ciphering of the data part of the uplink PDCP PDUs with associated COUNT values above the COUNT value corresponding to LSN.

## 5.6.3.2Receive Operation

When upper layers request a PDCP re-establishment for a LWA bearer mapped on RLC AM where LWA configuration is retained with the same WT (handoverWithoutWT-Change, see TS 36.331 [3]), after the LWA end-marker PDCP Control PDU is received, the UE shall start using the key provided by upper layers during the re-establishment procedure for the deciphering of the data part of downlink PDCP PDUs with associated COUNT values above the COUNT value corresponding to LSN.

NOTE 1:If PDCP re-establishment is completed before the LWA end-marker PDCP Control PDU is received, the behaviour is left up to UE implementation.

NOTE 2:After the LWA end-marker PDCP Control PDU is received, the handling of PDCP PDUs with associated COUNT values up to and including the COUNT value corresponding to LSN is left up to the UE implementation.

## 5.7Integrity Protection and Verification

The integrity protection function includes both integrity protection and integrity verification and is performed in PDCP for PDCP entities associated with SRBs and the SLRB that needs integrity protection. The data unit that is integrity protected is the PDU header and the data part of the PDU before ciphering.

For RNs, the integrity protection function is performed also for PDCP entities associated with DRBs if integrity protection is configured.

The integrity protection algorithm and key to be used by the PDCP entity are configured by upper layers, see TS 36.331 [3] and the integrity protection method shall be applied as specified in TS 33.401 [6].

The integrity protection function is activated/suspended/resumed by upper layers, see TS 36.331 [3]. When security is activated and not suspended, the integrity protection function shall be applied to all PDUs including and subsequent to the PDU indicated by upper layers, see TS 36.331 [3], for the downlink and the uplink, respectively.

NOTE:As the RRC message which activates the integrity protection function is itself integrity protected with the configuration included in this RRC message, this message needs first be decoded by RRC before the integrity protection verification could be performed for the PDU in which the message was received.

For downlink and uplink integrity protection and verification, the parameters that are required by PDCP for integrity protection are defined in TS 33.401 [6] and are input to the integrity protection algorithm. The required inputs to the integrity protection function include the COUNT value, and DIRECTION (direction of the transmission: set as specified in TS 33.401 [6]). The parameters required by PDCP which are provided by upper layers, see TS 36.331 [3], are listed below:

-BEARER (defined as the radio bearer identifier in TS 33.401 [6]. It will use the value RB identity –1 as in TS 36.331 [3]);

-KEY (KRRCint).

-for RNs, KEY (KUPint)

For the SLRB that needs integrity protection and verification, the parameters that are required by PDCP for integrity protection are defined in TS 33.401 [6] and are input to the integrity protection algorithm. The required inputs to the integrity protection function include the COUNT value and DIRECTION (which value shall be set is specified in TS 33.303 [13]). The parameters required by PDCP which are provided by upper layers, see TS 36.331 [3] are listed below:

-BEARER (defined as the radio bearer identifier in TS 33.401 [6]);

-KEY (PIK).

At transmission, the UE computes the value of the MAC-I field and at reception it verifies the integrity of the PDCP PDU by calculating the X-MAC based on the input parameters as specified above. If the calculated X-MAC corresponds to the received MAC-I, integrity protection is verified successfully.

## 5.8Handling of unknown, unforeseen and erroneous protocol data

When a PDCP entity receives a PDCP PDU that contains reserved or invalid values, the PDCP entity shall:

-discard the received PDU.

## 5.9PDCP Data Recovery procedure

When upper layers request a PDCP Data Recovery for a radio bearer, the UE shall:

-if the radio bearer is configured by upper layers to send a PDCP status report in the uplink (statusReportRequired, see TS 36.331 [3]), compile a status report as described in clause 5.3.1, and submit it to lower layers as the first PDCP PDU for the transmission;

-perform retransmission of all the PDCP PDUs previously submitted to re-established AM RLC entity in ascending order of the associated COUNT values from the first PDCP PDU for which the successful delivery has not been confirmed by lower layers.

After performing the above procedures, the UE shall follow the procedures in clause 5.1.1.

## 5.10Status report for LWA

## 5.10.1Transmit operation

When PDCP Data PDU with polling bit P set to 1 is received, the UE shall:

-if configured to send the PDCP status report in response to polling (statusPDU-TypeForPolling is configured and set to type1, see TS 36.331 [3])

-compile and transmit the PDCP status report as specified in clause 5.3.1;

-else if configured to send the LWA status report in response to polling (statusPDU-TypeForPolling is configured and set to type2, see TS 36.331 [3])

-compile and transmit the LWA status report as specified in clause 5.10.2.

When t-StatusReportType1 expires, the UE shall:

-compile and transmit the PDCP status report as specified in clause 5.3.1,

-start t-StatusReportType1 with value statusPDU-Periodicity-Type1;

When t-StatusReportType2 expires, the UE shall:

-compile and transmit the LWA status report as specified in clause 5.10.2,

-start t-StatusReportType2 with value statusPDU-Periodicity-Type2;

When t-StatusReportType1 is configured or reconfigured by upper layers, the UE shall:

-stop t-StatusReportType1, if running;

-start t-StatusReportType1 with value statusPDU-Periodicity-Type1;

When t-StatusReportType2 is configured or reconfigured by upper layers, the UE shall:

-stop t-StatusReportType2, if running;

-if statusPDU-Periodicity-Offset is configured by upper layers:

-start t-StatusReportType2 with value statusPDU-Periodicity-Type2 plus statusPDU-Periodicity-Offset;

-else:

-start t-StatusReportType2 with value statusPDU-Periodicity-Type2;

When periodic PDCP status report becomes disabled by upper layers, the UE shall:

-stop t-StatusReportType1, if running;

-stop t-StatusReportType2, if running;

## 5.10.2LWA status report

When LWA status report is triggered, the UE shall:

-compile a status report as indicated below, and submit it to lower layers as the first PDCP PDU for the transmission, by:

-setting the FMS field to the PDCP SN of the first missing PDCP SDU;

-setting the HRW field to the PDCP SN of the PDCP SDU received on WLAN with highest PDCP COUNT value or to FMS if no PDCP SDUs have been received on WLAN;

-setting the NMP field to the number of missing PDCP SDU(s) as described in 6.3.16.

## 5.10.3Receive operation

When a LWA status report is received in the downlink:

-for each PDCP SDU, if any, with the associated COUNT value less than the COUNT value of the PDCP SDU identified by the FMS field, the successful delivery of the corresponding PDCP SDU is confirmed, and the UE shall process the PDCP SDU as specified in 5.4.

## 5.11Uplink Data compression and decompression

## 5.11.1UDC protocol

The UDC protocol is based on IETF RFC 1951 (DEFLATE Compressed Data Format Specification) [16].

Static Huffman coding tree defined in [16] is used as the DEFLATE compression strategy.

UDC Data Block should be byte-alignment. Z_SYNC_FLUSH is used as the DEFLATE byte-alignment with corresponding reference [18], wherein the fixed last four bytes, 0x00 0x00 0xFF 0xFF, are removed before transmission.

## 5.11.2Configuration of UDC

The PDCP entities associated with DRBs can be configured by upper layers, see TS 36.331 [3], to use UDC. If UDC is configured, the UE shall apply UDC compression function (details see clause 5.11.4) to process the received PDCP SDU from upper layers corresponding to the configured DRB. The size of compression buffer is configured by upper layer via bufferSize. If pre-defined dictionary is configured by upper layers, the UE shall prefill the configured pre-defined dictionary in the compression buffer upon configuration of UDC. If pre-defined dictionary is not configured by upper layers, UE shall set the compression buffer to all zeros.

## 5.11.3UDC header

UDC header (1 byte) is added in UDC compression function followed by UDC data block (details see clause 5.11.4, 6.2.14, 6.2.15 and 6.2.16). The UDC header contains the information about whether the current PDCP SDU is compressed by UDC protocol or not. Only the compressed packets are stored in the buffer. The UDC header also contains a reset bit to inform the decompressor that the compression buffer has been reset. The validation bits (checksum) of the compression buffer are also contained in UDC header. Checksum mechanism could be used to resolve miss-match (if any) between the compression and de-compression buffers.

## 5.11.4Uplink data compression

The UDC protocol generates UDC packets, each associated with one PDCP SDU.

A UDC packet consists of a UDC header and a UDC data block. A UDC data block contains either DEFLATE compressed blocks generated from the original PDCP SDU by UDC protocol or original PDCP SDU for SDU not compressed by UDC protocol; the type is specified in FU field (details see clause 6.3.21) in UDC header. The FR field (details see clause 6.3.22) and the Checksum field (details see clause 6.3.23) in UDC header are used only if FU field is set to 1.

A UDC packet is associated with the same PDCP SN and COUNT values as the related PDCP SDU.

## 5.11.5Pre-defined dictionary

One standard dictionary for SIP and SDP and one operator defined dictionary can be used as pre-defined dictionaries in UDC. The standard dictionary for SIP and SDP consists of the first 3468 bytes of the dictionary for SigComp defined in RFC 3485 [17]. When UDC is configured, at most one dictionary, configured by upper layers, is put into the tail of the compression buffer. Also, the compression buffer acts as a FIFO and hence the content of the dictionary is to be totally pushed out of the compression buffer after the size of transmitted uncompressed packets compressed by UDC exceeds the compression buffer size. If the size of dictionary is larger than the compression buffer size, only the tail of the dictionary is inserted in the compression buffer.

## 5.11.6UDC buffer reset procedure

UDC works on the condition that compression buffer and de-compression buffer are synchronized. UDC buffer reset mechanism is to resynchronize buffer when error is detected. For resynchronization, UE shall reset the compression buffer to all zeros. After performing the reset, the FR field (details see clause 6.3.22) in UDC header of the first compressed PDU shall be set to 1.

## 5.11.7UDC checksum error handling

UDC checksum error notification PDCP control PDU indicates the compression buffer and de-compression buffer are out of synchronization. When receiving the notification, the UE shall trigger UDC buffer reset procedure to resynchonize the compression buffer.

## 5.11.8PDCP Control PDU for UDC feedback

At reception of a PDCP Control PDU for UDC feedback from lower layers, the receiving PDCP entity shall:

-deliver the corresponding UDC feedback to the UDC protocol without performing deciphering.

## 5.12Uplink data switching

For DAPS bearers, when upper layers request uplink data switching, the transmitting PDCP entity shall:

-for DRBs mapped on RLC AM, from the first PDCP SDU for which the successful delivery of the corresponding PDCP Data PDU has not been confirmed by the RLC entity associated with the source cell, perform retransmission or transmission of all the PDCP SDUs already associated with PDCP SNs in ascending order of the COUNT values associated to the PDCP SDU prior to uplink data switching to the RLC entity associated with the target cell as specified below:

-perform header compression of the PDCP SDU using ROHC as specified in the clause 5.5.4;

-perform ciphering of the PDCP SDU using the COUNT value associated with this PDCP SDU as specified in the clause 5.6;

-submit the resulting PDCP Data PDU to lower layer.

-for DRBs mapped on RLC UM, for each PDCP SDU already associated with a PDCP SN but for which a corresponding PDU has not previously been submitted to lower layers, perform transmission of PDCP SDU in ascending order of the COUNT values to the RLC entity associated with the target cell as specified below:

-perform header compression of the PDCP SDU using ROHC as specified in the clause 5.5.4;

-perform ciphering of the PDCP SDU using the COUNT value associated with this PDCP SDU as specified in the clause 5.6;

-submit the resulting PDCP Data PDU to lower layer.

## 5.13PDCP Reconfiguration

When upper layers reconfigure the PDCP entity to configure DAPS, the UE shall:

-establish a ciphering function for the radio bearer and apply the ciphering algorithm and key provided by upper layers for the ciphering function;

-establish a header compression protocol for the radio bearer and apply the header compression configuration provided by upper layers for the header compression protocol.

When upper layers reconfigure the PDCP entity to release DAPS, the UE shall:

-release the ciphering function associated to the released RLC entity for the radio bearer;

-release the header compression protocol associated to the released RLC entity for the radio bearer.

NOTE 1:The state variables which control the transmission and reception operation should not be reset, and the timers including t-Reordering and discardTimer keep running during PDCP entity reconfiguration procedure.

NOTE 2:Before releasing the header compression protocol and the ciphering function associated to the released RLC entity, how to handle all stored PDCP SDUs received from the released RLC entity is left up to UE implementation.

NOTE 3:Upon upper layers reconfigure the PDCP entity to release DAPS, the reordering function is still maintained.

## 5.14Ethernet header compression and decompression

## 5.14.1Supported header compression protocols

The EHC protocol is based on the Ethernet Header Compression (EHC) framework defined in [19].

## 5.14.2Configuration of EHC

PDCP entities associated with DRBs can be configured by upper layers TS 36.331 [3] to use EHC. Each PDCP entity carrying user plane data may be configured to use EHC. Every PDCP entity uses at most one EHC compressor instance and at most one EHC decompressor instance.

## 5.14.3Protocol parameters

The usage and definition of the parameters shall be as specified below.

-MAX_CID_EHC_UL: This is the maximum CID value that can be used for UL. One CID value shall always be reserved for uncompressed flows. The parameter MAX_CID_EHC_UL is configured by upper layers (maxCID-EHC-UL in TS 36.331 [3]);

## 5.14.4Header compression using EHC

If EHC is configured, the EHC protocol generates two types of output packets:

-EHC compressed packets (i.e. EHC full header packets and EHC compressed header packets), each associated with one PDCP SDU;

-standalone packets not associated with a PDCP SDU, i.e. EHC feedback packets.

An EHC compressed packet is associated with the same PDCP SN and COUNT value as the related PDCP SDU.

EHC feedback packets are not associated with a PDCP SDU. They are not associated with a PDCP SN and are not ciphered.

## 5.14.5Header decompression using EHC

If EHC is configured by upper layers for PDCP entities associated with user plane data, the PDCP Data PDUs are decompressed by the EHC protocol after performing deciphering as explained in clause 5.6.

## 5.14.6PDCP Control PDU for EHC feedback packet

## 5.14.6.1Transmit Operation

When an EHC feedback packet is generated by the EHC protocol, the transmitting PDCP entity shall:

-submit to lower layers the corresponding PDCP Control PDU as specified in clause 6.2.18, i.e., without associating a PDCP SN, nor performing ciphering.

## 5.14.6.2Receive Operation

At reception of a PDCP Control PDU for EHC feedback packet from lower layers, the receiving PDCP entity shall:

-deliver the corresponding EHC feedback packet to the EHC protocol without performing deciphering.

## 5.14.7Simultaneous configuration of ROHC and EHC

If both ROHC and EHC are configured for a DRB, the ROHC header shall be located after the EHC header. Figure 5.14.7.1 shows the location of the ROHC header and the EHC header in a PDCP Data PDU.

Figure 5.14.7.1: Location of ROHC header and EHC header in a PDCP Data PDU

If a PDCP SDU including non-IP Ethernet packet is received from upper layers, the EHC compressor shall bypass the ROHC compressor and submit the EHC compressed non-IP Ethernet packet to lower layers according to clause 5.1.1.

If a PDCP Data PDU including non-IP Ethernet packet is received from lower layers, the EHC decompressor shall bypass the ROHC decompressor and deliver the EHC decompressed non-IP Ethernet packet to upper layers according to clause 5.1.2.

## 6Protocol data units, formats and parameters

## 6.1Protocol data units

## 6.1.1PDCP Data PDU

The PDCP Data PDU is used to convey:

-a PDCP SDU SN; and

-for SLRBs used for one-to-many communication, PGK Index, PTK Identity, and SDU type; or

-for SLRBs used for one-to-one communication, KD-sess Identity, and SDU type; and

-user plane data containing an uncompressed PDCP SDU; or

-user plane data containing a compressed PDCP SDU; or

-control plane data; and

-a MAC-I field for SRBs; or

-for the SLRB that needs integrity protection for one-to-one communication, a MAC-I field; or

-for RNs, a MAC-I field for DRB (if integrity protection is configured);

## 6.1.2PDCP Control PDU

The PDCP Control PDU is used to convey:

-a PDCP status report indicating which PDCP SDUs are missing and which are not following a PDCP re-establishment.

-header compression control information, e.g. interspersed ROHC feedback or EHC feedback.

-a LWA status report.

-a LWA end-marker packet.

-data compression control information, e.g., UDC feedback.

## 6.2Formats

## 6.2.1General

A PDCP PDU is a bit string that is byte aligned (i.e. multiple of 8 bits) in length. In the figures in clause 6.2, bit strings are represented by tables in which the most significant bit is the leftmost bit of the first line of the table, the least significant bit is the rightmost bit on the last line of the table, and more generally the bit string is to be read from left to right and then in the reading order of the lines. The bit order of each parameter field within a PDCP PDU is represented with the first and most significant bit in the leftmost bit and the last and least significant bit in the rightmost bit.

PDCP SDUs are bit strings that are byte aligned (i.e. multiple of 8 bits) in length. A compressed or uncompressed SDU is included into a PDCP PDU from the first bit onward.

## 6.2.2Control plane PDCP Data PDU

Figure 6.2.2.1 shows the format of the PDCP Data PDU carrying data for control plane SRBs.

Figure 6.2.2.1: PDCP Data PDU format for SRBs

## 6.2.3User plane PDCP Data PDU with long PDCP SN (12 bits)

Figures 6.2.3.1 and 6.2.3.2 show the format of the downlink and uplink PDCP Data PDUs respectively, when a 12 bit SN length is used. These formats are applicable for PDCP Data PDUs carrying data from DRBs mapped on RLC AM or RLC UM.

Figure 6.2.3.1: PDCP Data PDU format for DRBs using a 12 bit SN (for downlink)

Figure 6.2.3.2: PDCP Data PDU format for DRBs using a 12 bit SN (for uplink)

## 6.2.4User plane PDCP Data PDU with short PDCP SN (7 bits)

Figure 6.2.4.1 shows the format of the PDCP Data PDU when a 7 bit SN length is used. This format is applicable for PDCP Data PDUs carrying data from DRBs mapped on RLC UM or in NB-IoT DRBs mapped on RLC AM and on RLC UM.

Figure 6.2.4.1: PDCP Data PDU format for DRBs using 7 bit SN

## 6.2.5PDCP Control PDU for interspersed ROHC feedback packet

Figure 6.2.5.1 shows the format of the PDCP Control PDU carrying one interspersed ROHC feedback packet. This format is applicable for DRBs mapped on RLC AM or RLC UM.

Figure 6.2.5.1: PDCP Control PDU format for interspersed ROHC feedback packet

## 6.2.6PDCP Control PDU for PDCP status report

Figure 6.2.6.1 shows the format of the PDCP Control PDU carrying one PDCP status report when a 12 bit SN length is used. This format is applicable for DRBs mapped on RLC UM and RLC AM.

Figure 6.2.6.2 shows the format of the PDCP Control PDU carrying one PDCP status report when a 15 bit SN length is used, and Figure 6.2.6.3 shows the format of the PDCP Control PDU carrying one PDCP status report when an 18 bit SN length is used. These formats are applicable for DRBs mapped on RLC AM.

Figure 6.2.6.1: PDCP Control PDU format for PDCP status report using a 12 bit SN

Figure 6.2.6.2: PDCP Control PDU format for PDCP status report using a 15 bit SN

Figure 6.2.6.3: PDCP Control PDU format for PDCP status report using an 18 bit SN

## 6.2.7Void

## 6.2.8RN user plane PDCP Data PDU with integrity protection

Figure 6.2.8.1 shows the format of the PDCP Data PDU for RNs when integrity protection is used. This format is applicable for PDCP Data PDUs carrying data from DRBs mapped on RLC AM or RLC UM.

Figure 6.2.8.1: PDCP Data PDU format for RN DRBs using integrity protection

## 6.2.9User plane PDCP Data PDU with extended PDCP SN (15 bits)

Figure 6.2.9.1 shows the format of the PDCP Data PDU when a 15 bit SN length is used. This format is applicable for PDCP Data PDUs carrying data from DRBs mapped on RLC AM.

Figure 6.2.9.1: PDCP Data PDU format for DRBs using a 15 bit SN

## 6.2.10User plane PDCP Data PDU for SLRB

Figure 6.2.10.1 shows the format of the PDCP Data PDU for SLRB used for one-to-many communication where a 16 bit SN length is used.

Figure 6.2.10.1: PDCP Data PDU format for SLRB used for one-to-many communication

Figure 6.2.10.2 shows the format of the PDCP Data PDU for SLRB used for one-to-one communication where a 16 bit SN length is used. MAC-I field is used only for the SLRB that needs integrity protection.

Figure 6.2.10.2: PDCP Data PDU format for SLRB used for one-to-one communication

## 6.2.11User plane PDCP Data PDU with further extended PDCP SN (18 bits)

Figure 6.2.11.1 shows the format of the PDCP Data PDU when an 18 bit SN length is used. This format is applicable for PDCP Data PDUs carrying data from DRBs mapped on RLC AM. The UE not supporting LWA shall consider the PDCP Data PDU invalid if the P bit is set to 1.

Figure 6.2.11.1: PDCP Data PDU format for DRBs using an 18 bit SN

## 6.2.12PDCP Control PDU for LWA status report

Figure 6.2.12.1 shows the format of the PDCP Control PDU carrying one LWA status report when a 12 bit SN length is used, Figure 6.2.12.2 shows the format of the PDCP Control PDU carrying one LWA status report when a 15 bit SN length is used, and Figure 6.2.12.3 shows the format of the PDCP Control PDU carrying one LWA status report when an 18 bit SN length is used. This format is applicable for LWA DRBs.

Figure 6.2.12.1: PDCP Control PDU format for LWA status report using a 12 bit SN

Figure 6.2.12.2: PDCP Control PDU format for LWA status report using a 15 bit SN

Figure 6.2.12.3: PDCP Control PDU format for LWA status report using an 18 bit SN

## 6.2.13PDCP Control PDU for LWA end-marker packet

Figure 6.2.13.1 shows the format of the PDCP Control PDU for LWA end-marker packet when a 12 bit SN length is used, Figure 6.2.13.2 shows the format of the PDCP Control PDU for LWA end-marker packet when a 15 bit SN length is used, and Figure 6.2.13.3 shows the format of the PDCP Control PDU for LWA end-marker packet when an 18 bit SN length is used.

Figure 6.2.13.1: PDCP Control PDU format for LWA end-marker packet using a 12 bit SN

Figure 6.2.13.2: PDCP Control PDU format for LWA end-marker packet using a 15 bit SN

Figure 6.2.13.3: PDCP Control PDU format for LWA end-marker packet using an 18 bit SN

## 6.2.14User plane PDCP Data PDU with long PDCP SN (12 bits) for UDC

Figure 6.2.14.1 shows the format of the PDCP Data PDU when a 12 bit SN length is used and UDC is configured. This format is applicable for uplink PDCP Data PDUs carrying data from DRBs configured with UDC.

Figure 6.2.14.1: PDCP Data PDU format for DRBs using a 12 bit SN (UDC configured)

## 6.2.15User plane PDCP Data PDU with extended PDCP SN (15 bits) for UDC

Figure 6.2.15.1 shows the format of the PDCP Data PDU when a 15 bit SN length is used and UDC is configured. This format is applicable for PDCP Data PDUs carrying data from DRBs configured with UDC.

Figure 6.2.15.1: PDCP Data PDU format for DRBs using a 15 bit SN (UDC configured)

## 6.2.16User plane PDCP Data PDU with further extended PDCP SN (18 bits) for UDC

Figure 6.2.16.1 shows the format of the PDCP Data PDU when an 18 bit SN length is used and UDC is configured. This format is applicable for uplink PDCP Data PDUs carrying data from DRBs configured with UDC.

Figure 6.2.16.1: PDCP Data PDU format for DRBs using an 18 bit SN (UDC configured)

## 6.2.17PDCP Control PDU for UDC feedback packet

Figure 6.2.17.1 shows the format of the PDCP Control PDU for UDC feedback packet. This format is applicable for DRBs configured with UDC.

Figure 6.2.17.1: PDCP Control PDU format for UDC feedback packet

## 6.2.18PDCP Control PDU for EHC feedback packet

Figure 6.2.18.1 shows the format of the PDCP Control PDU for EHC feedback packet. This format is applicable for DRBs mapped on RLC AM or RLC UM.

Figure 6.2.18.1: PDCP Control PDU format for EHC feedback packet

## 6.3Parameters

## 6.3.1General

If not otherwise mentioned in the definition of each field then the bits in the parameters shall be interpreted as follows: the left most bit string is the first and most significant and the right most bit is the last and least significant bit.

Unless otherwise mentioned, integers are encoded in standard binary encoding for unsigned integers. In all cases the bits appear ordered from MSB to LSB when read in the PDU.

## 6.3.2PDCP SN

Length: 5, 7, 12, 15, 16, or 18 bits as indicated in table 6.3.2.1 except for NB-IoT which uses 7 bit PDCP SN for DRB.

Table 6.3.2.1: PDCP SN length

## 6.3.3Data

Length: Variable

The Data field may include either one of the following:

-Uncompressed PDCP SDU (user plane data, or control plane data); or

-Compressed PDCP SDU (user plane data only); or

-UDC header and UDC Data Block if UDC is configured.

NOTE:All fields other than PDCP PDU header and MAC-I belong to Data field.‎

## 6.3.4MAC-I

Length: 32 bits

The MAC-I field carries a message authentication code calculated as specified in clause 5.7.

For control plane data that are not integrity protected, the MAC-I field is still present and should be padded with padding bits set to 0.

## 6.3.5COUNT

Length: 32 bits

For ciphering and integrity a COUNT value is maintained. The COUNT value is composed of a HFN and the PDCP SN. The length of the PDCP SN is configured by upper layers.

Figure 6.3.5.1: Format of COUNT

The size of the HFN part in bits is equal to 32 minus the length of the PDCP SN.

NOTE:When performing comparison of values related to COUNT, the UE takes into account that COUNT is a 32-bit value, which may wrap around (e.g., COUNT value of 232 - 1 is less than COUNT value of 0).

## 6.3.6R

Length: 1 bit

Reserved. In this version of the specification reserved bits shall be set to 0. Reserved bits shall be ignored by the receiver.

## 6.3.7D/C

Length: 1 bit

Table 6.3.7.1: D/C field

## 6.3.8PDU type

Length: 3 bits

Table 6.3.8.1: PDU type

## 6.3.9FMS

Length: 12 bits when a 12 bit SN length is used, 15 bits when a 15 bit SN length is used, and 18 bits when an 18 bit SN length is used

PDCP SN of the first missing PDCP SDU.

## 6.3.10Bitmap

Length: Variable

The length of the bitmap field can be 0.

The MSB of the first octet of the type "Bitmap" indicates whether or not the PDCP SDU with the SN (FMS + 1) modulo (Maximum_PDCP_SN + 1) has been received and, optionally decompressed correctly. The LSB of the first octet of the type "Bitmap" indicates whether or not the PDCP SDU with the SN (FMS + 8) modulo (Maximum_PDCP_SN + 1) has been received and, optionally decompressed correctly.

Table 6.3.10.1 Bitmap

The UE fills the bitmap indicating which SDUs are missing (unset bit - '0'), i.e. whether an SDU has not been received or optionally has been received but has not been decompressed correctly, and which SDUs do not need retransmission (set bit - '1'), i.e. whether an SDU has been received correctly and may or may not have been decompressed correctly.

## 6.3.11Interspersed ROHC feedback packet

Length: Variable

Contains one ROHC packet with only feedback, i.e. a ROHC packet that is not associated with a PDCP SDU as defined in clause 5.5.4.

## 6.3.12PGK Index

Length: 5 bits

## 5 LSBs of PGK Identity as specified in TS 33.303 [13].

## 6.3.13PTK Identity

Length: 16 bits

PTK Identity as specified in TS 33.303 [13].

## 6.3.14SDU Type

Length: 3 bits

PDCP SDU type, i.e. Layer-3 Protocol Data Unit type as specified in [14]. PDCP entity may handle the SDU differently per SDU Type, e.g. ROHC is applicable to IP SDU but not ARP SDU and Non-IP SDU.

Table 6.3.14.1: SDU Type

## 6.3.15KD-sess ID

Length: 16 bits

KD-sess Identity as specified in TS 33.303 [13].

## 6.3.16NMP

Length: 12 bits when a 12 bit SN length is used, 15 bits when a 15 bit SN length is used, and 18 bits when an 18 bit SN length is used.

Number of missing PDCP SDU(s) with associated COUNT value below the associated COUNT value corresponding to HRW, starting from and including the associated COUNT value corresponding to FMS.

## 6.3.17HRW

Length: 12 bits when a 12 bit SN length is used, 15 bits when a 15 bit SN length is used and 18 bits when an 18 bit SN length is used.

PDCP SN of the PDCP SDU received on WLAN with highest associated PDCP COUNT value.

## 6.3.18P

Length: 1 bit

Polling indication. The P field indicates whether the UE is requested to send a PDCP status report or a LWA status report for LWA. The field is not applicable to uplink PDCP PDUs and the UE shall set the P field to 0.

Table 6.3.18.1: P field

## 6.3.19LSN

Length: 12 bits when a 12 bit SN length is used, 15 bits when a 15 bit SN length is used, and 18 bits when an 18 bit SN length is used

PDCP SN of the last PDCP PDU for which the data part is ciphered with the key used before PDCP re-establishment. Only applicable for the case when upper layers request a PDCP re-establishment for a LWA bearer where LWA configuration is retained with the same WT.

6.3.20AILC

Length: 1 bit

The AILC field indicates that corresponding PDCP SDU in the uplink PDCP PDU may be transferred to the local cache entity when PDCP entity is configured by upper layers, i.e. ailc-BitConfig, as specified in TS 36.331 [3]. If the PDCP SDU may be transferred to the local cache entity, the AILC field shall be set to 1, otherwise to 0.

Table 6.3.20.1: AILC field

## 6.3.21FU

Length: 1 bit

Indication of whether this packet is compressed by UDC protocol or not. Value '1' means the packet is compressed by UDC protocol.

Table 6.3.21.1: FU field

## 6.3.22FR

Length: 1 bit

Indication of whether UDC compression buffer is reset or not. Value '1' means this is the first compressed packet after UDC buffer reset.

Table 6.3.22.1: FR field

## 6.3.23Checksum

Length: 4 bits

This field contains the validation bits for the compression buffer content: The checksum is calculated by the content of current compression buffer before the current packet is put into buffer.

The checksum is derived from the values of the first 4 bytes and the last 4 bytes in the whole compression buffer. The calculation is described as follows:

-Each byte is divided into two 4-bit numbers.

-The 16 4-bit numbers are added together to obtain a sum;

-The checksum is one's complement of the right-most 4 bits (i.e. 4 LSB) of the sum.

An example of checksum calculation is shown in Annex A.

## 6.3.24FE

Length: 1 bit

Indication of whether checksum error is detected or not. Value '1' means checksum error is detected and the UE shall reset the compression buffer.

Table 6.3.24.1: FE field

## 7Variables, constants and timers

## 7.1State variables

This clause describes the state variables used in PDCP entities in order to specify the PDCP protocol.

All state variables are non-negative integers.

The transmitting side of each PDCP entity shall maintain the following state variables:

a)Next_PDCP_TX_SN

The variable Next_PDCP_TX_SN indicates the PDCP SN of the next PDCP SDU for a given PDCP entity. At establishment of the PDCP entity, the UE shall set Next_PDCP_TX_SN to 0. For the PDCP entity mapped with SLRB of which the indicated SL-V2X-TxProfile is rel15 (see TS 36.331 [3]), the UE shall set Next_PDCP_TX_SN to 1 at establishment of the PDCP entity.

b)TX_HFN

The variable TX_HFN indicates the HFN value for the generation of the COUNT value used for PDCP PDUs for a given PDCP entity. At establishment of the PDCP entity, the UE shall set TX_HFN to 0.

The receiving side of each PDCP entity shall maintain the following state variables:

c)Next_PDCP_RX_SN

The variable Next_PDCP_RX_SN indicates the next expected PDCP SN by the receiver for a given PDCP entity. At establishment of the PDCP entity, the UE shall set Next_PDCP_RX_SN to 0. For the PDCP entity mapped with SLRB of which the indicated SL-V2X-TxProfile is rel15 (see TS 36.331 [3]), the UE shall set Next_PDCP_RX_SN to (x +1) modulo (Maximum_PDCP_SN + 1), where x is the SN of the first received PDCP Data PDU with SN not set to "0".

d)RX_HFN

The variable RX_HFN indicates the HFN value for the generation of the COUNT value used for the received PDCP PDUs for a given PDCP entity. At establishment of the PDCP entity, the UE shall set RX_HFN to 0.

e) Last_Submitted_PDCP_RX_SN

The variable Last_Submitted_PDCP_RX_SN indicates the SN of the last PDCP SDU delivered to the upper layers. At establishment of the PDCP entity, the UE shall set Last_Submitted_PDCP_RX_SN to Maximum_PDCP_SN. For the PDCP entity mapped with SLRB of which the indicated SL-V2X-TxProfile is rel15 (see TS 36.331 [3]), the UE shall set Last_Submitted_PDCP_RX_SN to (x – 0.5 * Reordering_Window) modulo (Maximum_PDCP_SN + 1), where x is the SN of the first received PDCP Data PDU with SN not set to "0". When upper layers reconfigure the PDCP entity to configure DAPS for a DRB mapped on RLC UM, the UE shall set Last_Submitted_PDCP_RX_SN to (Next_PDCP_RX_SN – 1) modulo (Maximum_PDCP_SN + 1).

f) Reordering_PDCP_RX_COUNT

This variable is used only when the reordering function is used. This variable holds the value of the COUNT following the COUNT value associated with the PDCP PDU which triggered t-Reordering. When upper layers reconfigure the PDCP entity to configure DAPS, the UE shall set Reordering_PDCP_RX_COUNT to the COUNT value associated to RX_HFN and Next_PDCP_RX_SN.

## 7.2Timers

The transmitting side of each PDCP entity for DRBs shall maintain the following timers:

a) discardTimer

The duration of the timer is configured by upper layers, see TS 36.331 [3]. In the transmitter, a new timer is started upon reception of an SDU from upper layer.

The receiving side of each PDCP entity shall maintain the following timers only when the reordering function is used:

b) t-Reordering

The duration of the timer is configured by upper layers, see(TS 36.331 [3], except for the case of Sidelink reception when the reordering function is used. For when the reordering function is used reception when the reordering function is used, the t-Reordering timer is determined by the UE implementation. This timer is used to detect loss of PDCP PDUs as specified in the clause 5.1.2.1.4. If t-Reordering is running, t-Reordering shall not be started additionally, i.e. only one t-Reordering per PDCP entity is running at a given time.

The receiving side of each PDCP entity associated with LWA bearers shall maintain the following timers:

c) t-StatusReportType1

The duration of the timer is configured by upper layers (statusPDU-Periodicity-Type1, see TS 36.331 [3]). This timer is used to trigger status report transmission for LWA as specified in the clause 5.10.

d) t-StatusReportType2

The duration of the timer is configured by upper layers (statusPDU-Periodicity-Type2 and statusPDU-Periodicity-Offset, see TS 36.331 [3]). If statusPDU-Periodicity-Offset is configured and it is the first run of the timer after (re)configuration, the duration of the timer is the sum of statusPDU-Periodicity-Type2 and statusPDU-Periodicity-Offset, see TS 36.331 [3], otherwise the duration of the timer is statusPDU-Periodicity-Type2. When configured, this timer is used to trigger status report transmission for LWA as specified in the clause 5.10.

## 7.3Constants

a) Reordering_Window

Indicates the size of the reordering window. The size equals to 16 when a 5 bit SN length is used, 64 when a 7 bit SN length is used, 2048 when a 12 bit SN length is used, 16384 when a 15 bit SN length is used, 32768 when a 16 bit SN length is used, or 131072 when 18 bit SN length is used, i.e. half of the PDCP SN space, for radio bearers that are mapped on RLC AM, for LWA bearers and for SLRBs when the reordering function is used.

b) Maximum_PDCP_SN is:

-262143 if the PDCP entity is configured for the use of 18 bits SNs

-65535 if the PDCP entity is configured for the use of 16 bits SNs

-32767 if the PDCP entity is configured for the use of 15 bits SNs

-4095 if the PDCP entity is configured for the use of 12 bit SNs

-127 if the PDCP entity is configured for the use of 7 bit SNs

-31 if the PDCP entity is configured for the use of 5 bit SNs

## Annex A (informative):An example of UDC Checksum calculation

The current UDC compression/decompression buffer has the following binary values for example:

Header <1,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1, ……, 0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0> Tail

The sum of the first 4 bytes and the last 4 bytes can be calculated:

1100+0101+0011+1111+0001+1001+0101+0001+0111+1101+1000+1010+1001+1111+1001+1100 = 10000110;

And checksum value will be one's complement of the right-most 4 bits (i.e. 4 LSB) of the above sum. Hence checksum is 1001.

## Annex B (informative):Change history
