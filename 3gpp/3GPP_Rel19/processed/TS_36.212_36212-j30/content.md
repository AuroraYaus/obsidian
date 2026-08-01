---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.212_36212-j30/content.md"
---
# TS 36.212 36212-j30

3GPP TS 36.212 V19.3.0 (2026-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

Evolved Universal Terrestrial Radio Access (E-UTRA);

Multiplexing and channel coding

(Release 19)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.Specifications and reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords

E-UTRA, radio, Layer 1

3GPP

Postal address

3GPP support office address

## 650 Route des Lucioles – Sophia Antipolis

Valbonne – France

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

3Definitions, symbols and abbreviations7

3.1Definitions7

3.2Symbols7

3.3Abbreviations8

4Mapping to physical channels9

4.1Uplink9

4.2Downlink9

4.3Sidelink10

5Channel coding, multiplexing and interleaving10

5.1Generic procedures10

5.1.1CRC calculation10

5.1.2Code block segmentation and code block CRC attachment11

5.1.3Channel coding12

5.1.3.1Tail biting convolutional coding13

5.1.3.2Turbo coding14

5.1.3.2.1Turbo encoder14

5.1.3.2.2Trellis termination for turbo encoder15

5.1.3.2.3Turbo code internal interleaver15

5.1.4Rate matching17

5.1.4.1Rate matching for turbo coded transport channels17

5.1.4.1.1Sub-block interleaver17

5.1.4.1.2Bit collection, selection and transmission18

5.1.4.2Rate matching for convolutionally coded transport channels and control information21

5.1.4.2.1Sub-block interleaver22

5.1.4.2.2Bit collection, selection and transmission23

5.1.5Code block concatenation24

5.2Uplink transport channels and control information24

5.2.1Random access channel24

5.2.2Uplink shared channel24

5.2.2.1Transport block CRC attachment25

5.2.2.2Code block segmentation and code block CRC attachment26

5.2.2.3Channel coding of UL-SCH26

5.2.2.4Rate matching26

5.2.2.5Code block concatenation26

5.2.2.6Channel coding of control information26

5.2.2.6.1Channel quality information formats for wideband CQI reports45

5.2.2.6.2Channel quality information formats for higher layer configured subband CQI reports67

5.2.2.6.3Channel quality information formats for UE selected subband CQI reports98

5.2.2.6.4Channel coding for CQI/PMI information in PUSCH120

5.2.2.6.5Channel coding for more than 11 bits of HARQ-ACK information121

5.2.2.6AChannel coding of AUL-UCI122

5.2.2.7Data and control multiplexing123

5.2.2.7AData and control multiplexing for Partial PUSCH Mode 1124

5.2.2.7BData and control multiplexing for AUL PUSCH125

5.2.2.8Channel interleaver126

5.2.3Uplink control information on PUCCH131

5.2.3.1Channel coding for UCI HARQ-ACK on PUCCH132

5.2.3.1AChannel coding for UCI HARQ-ACK on SPUCCH138

5.2.3.2Channel coding for UCI scheduling request141

5.2.3.3Channel coding for UCI channel quality information141

5.2.3.3.1Channel quality information formats for wideband reports142

5.2.3.3.2Channel quality information formats for UE-selected sub-band reports155

5.2.3.4Channel coding for UCI channel quality information and HARQ-ACK170

5.2.4Uplink control information on PUSCH without UL-SCH data171

5.2.4.1Channel coding of control information171

5.2.4.2Control information mapping173

5.2.4.3Channel interleaver173

5.3Downlink transport channels and control information173

5.3.1Broadcast channel173

5.3.1.1Transport block CRC attachment174

5.3.1.2Channel coding174

5.3.1.3Rate matching175

5.3.2Downlink shared channel, Paging channel and Multicast channel175

5.3.2.1Transport block CRC attachment176

5.3.2.2Code block segmentation and code block CRC attachment176

5.3.2.3Channel coding176

5.3.2.4Rate matching176

5.3.2.5Code block concatenation176

5.3.3Downlink control information177

5.3.3.1DCI formats177

5.3.3.1.1Format 0177

5.3.3.1.1AFormat 0A179

5.3.3.1.1BFormat 0B181

5.3.3.1.1CFormat 0C183

5.3.3.1.2Format 1184

5.3.3.1.3Format 1A186

5.3.3.1.3AFormat 1B189

5.3.3.1.4Format 1C190

5.3.3.1.4AFormat 1D191

5.3.3.1.5Format 2193

5.3.3.1.5AFormat 2A197

5.3.3.1.5BFormat 2B199

5.3.3.1.5CFormat 2C201

5.3.3.1.5DFormat 2D204

5.3.3.1.6Format 3206

5.3.3.1.7Format 3A207

5.3.3.1.7AFormat 3B207

5.3.3.1.8Format 4208

5.3.3.1.8AFormat 4A210

5.3.3.1.8BFormat 4B212

5.3.3.1.9Format 5214

5.3.3.1.9AFormat 5A214

5.3.3.1.10Format 6-0A215

5.3.3.1.11Format 6-0B218

5.3.3.1.12Format 6-1A220

5.3.3.1.13Format 6-1B226

5.3.3.1.14Format 6-2229

5.3.3.1.15Format 7-0A229

5.3.3.1.16Format 7-0B230

5.3.3.1.17Format 7-1A232

5.3.3.1.18Format 7-1B233

5.3.3.1.19Format 7-1C234

5.3.3.1.20Format 7-1D236

5.3.3.1.21Format 7-1E238

5.3.3.1.22Format 7-1F238

5.3.3.1.23Format 7-1G239

5.3.3.2CRC attachment240

5.3.3.3Channel coding241

5.3.3.4Rate matching241

5.3.4Control format indicator241

5.3.4.1Channel coding241

5.3.5HARQ indicator (HI)242

5.3.5.1Channel coding242

5.4Sidelink transport channels and control information242

5.4.1Sidelink broadcast channel242

5.4.1.1Transport block CRC attachment243

5.4.1.2Channel coding243

5.4.1.3Rate matching243

5.4.2Sidelink shared channel243

5.4.3Sidelink control information244

5.4.3.1SCI formats244

5.4.3.1.1SCI format 0244

5.4.3.1.2SCI format 1245

5.4.4Sidelink discovery channel245

6Narrowband IoT245

6.1Mapping to physical channels245

6.2Generic procedures246

6.3Uplink transport channels and control information246

6.3.1Random access channel246

6.3.2Uplink shared channel246

6.3.3Uplink control information on NPUSCH without UL-SCH data247

6.3.4Scheduling request248

6.4Downlink transport channels and control information248

6.4.1Broadcast channel248

6.4.2Downlink shared channel and Paging channel248

6.4.3Downlink control information249

6.4.3.1DCI Format N0249

6.4.3.2DCI Format N1250

6.4.3.3DCI Format N2251

Annex A (informative):Change history253

## Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

xthe first digit:

1presented to TSG for information;

2presented to TSG for approval;

3or greater indicates TSG approved document under change control.

Ythe second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

zthe third digit is incremented when editorial only changes have been incorporated in the document.

## 1Scope

The present document specifies the coding, multiplexing and mapping to physical channels for E-UTRA.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".

[3]3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[4]3GPP TS 36.306: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio access capabilities".

[5]3GPP TS36.321, "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification"

[6]3GPP TS36.331, "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC) protocol specification"

[7]3GPP TS23.285, "Technical Specification Group Services and System Aspects; Architecture enhancements for V2X services"

[8]3GPP TS 37.213: "Physical layer procedures for shared spectrum channel access".

## 3Definitions, symbols and abbreviations

## 3.1Definitions

For the purposes of the present document, the terms and definitions given in [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in [1].

BL/CE: A Bandwidth-reduced Low-complexity or Coverage Enhanced (BL/CE) UE is capable of coverage enhancement mode A support and intends to access a cell in a coverage enhancement mode or is configured in a coverage enhancement mode.

Non-BL/CE: A non-BL/CE UE is a UE that does not fulfil the conditions in the above definition of a BL/CE UE.

## 3.2Symbols

For the purposes of the present document, the following symbols apply:

Downlink bandwidth configuration, expressed in number of resource blocks [2]

Uplink bandwidth configuration, expressed in number of resource blocks [2]

Sidelink bandwidth configuration, expressed in number of resource blocks [2]

Number of sidelink subchannels configured on the resource pool of a subcarrier [2]

Resource block size in the frequency domain, expressed as a number of subcarriers

Number of SC-FDMA symbols carrying PUSCH in a subframe

Number of SC-FDMA symbols carrying PUSCH in the initial PUSCH transmission subframe

Number of SC-FDMA symbols in an uplink slot

Number of SC-FDMA symbols in a sidelink slot

Number of SC-FDMA symbols used for SRS transmission in a subframe (0 or 1).

## 3.3Abbreviations

For the purposes of the present document, the following abbreviations apply:

AULAutonomous Uplink

AUL-DFIAUL downlink feedback information

AUL-UCIAUL uplink control information

BCHBroadcast channel

CFIControl Format Indicator

COTChannel Occupancy Time

CPCyclic Prefix

CSIChannel State Information

DCIDownlink Control Information

DL-SCHDownlink Shared channel

EN-DCE-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR

EPDCCHEnhanced Physical Downlink Control channel

FDDFrequency Division Duplexing

HIHARQ indicator

LAALicensed-Assisted Access

MCHMulticast channel

MPDCCHMTC Physical Downlink Control Channel

MUSTMultiuser Superposition Transmission

NE-DCNR E-UTRA Dual Connectivity with MCG using NR and SCG using E-UTRA

NPBCHNarrowband Physical Broadcast channel

NPDCCHNarrowband Physical Downlink Control channel

NPDSCHNarrowband Physical Downlink Shared channel

NPRACHNarrowband Physical Random Access channel

NPUSCHNarrowband Physical Uplink Shared channel

OCCOrthogonal Cover Code

PBCHPhysical Broadcast channel

PCFICHPhysical Control Format Indicator channel

PCHPaging channel

PDCCHPhysical Downlink Control channel

PDSCHPhysical Downlink Shared channel

PHICHPhysical HARQ indicator channel

PMCHPhysical Multicast channel

PMIPrecoding Matrix Indicator

PRACHPhysical Random Access channel

PSBCHPhysical Sidelink Broadcast Channel

PSCCHPhysical Sidelink Control Channel

PSDCHPhysical Sidelink Discovery Channel

PSSCHPhysical Sidelink Shared Channel

PUCCHPhysical Uplink Control channel

PUSCHPhysical Uplink Shared channel

RACHRandom Access channel

RIRank Indication

SCISidelink Control Information

SL-BCHSidelink Broadcast Channel

SL-DCHSidelink Discovery Channel

SL-SCHSidelink Shared Channel

SPDCCHShort Physical Downlink Control channel

SPUCCHShort Physical Uplink Control channel

SRScheduling Request

SRSSounding Reference Signal

TDDTime Division Duplexing

TPMITransmitted Precoding Matrix Indicator

UCIUplink Control Information

UL-SCHUplink Shared channel

## 4Mapping to physical channels

The mapping to physical channels for Narrowband IoT is provided in clause 6.1.

## 4.1Uplink

Table 4.1-1 specifies the mapping of the uplink transport channels to their corresponding physical channels. Table 4.1-2 specifies the mapping of the uplink control channel information to its corresponding physical channel.

Table 4.1-1

Table 4.1-2

## 4.2Downlink

Table 4.2-1 specifies the mapping of the downlink transport channels to their corresponding physical channels. Table 4.2-2 specifies the mapping of the downlink control channel information to its corresponding physical channel.

Table 4.2-1

Table 4.2-2

## 4.3Sidelink

Table 4.3-1 specifies the mapping of the sidelink transport channels to their corresponding physical channels. Table 4.3-2 specifies the mapping of the sidelink control information to its corresponding physical channel.

Table 4.3-1

Table 4.3-2

## 5Channel coding, multiplexing and interleaving

Data and control streams from/to MAC layer are encoded /decoded to offer transport and control services over the radio transmission link. Channel coding scheme is a combination of error detection, error correcting, rate matching, interleaving and transport channel or control information mapping onto/splitting from physical channels.

## 5.1Generic procedures

This clause contains coding procedures which are used for more than one transport channel or control information type.

## 5.1.1CRC calculation

Denote the input bits to the CRC computation by, and the parity bits by. A is the size of the input sequence and L is the number of parity bits. The parity bits are generated by one of the following cyclic generator polynomials:

-gCRC24A(D) = [D24 + D23 + D18 + D17 + D14 + D11 + D10 + D7 + D6 + D5 + D4 + D3 + D + 1] and;

-gCRC24B(D) = [D24 + D23 + D6 + D5 + D + 1] for a CRC length L = 24 and;

-gCRC16(D) = [D16 + D12 + D5 + 1] for a CRC length L = 16.

-gCRC8(D) = [D8 + D7 + D4 + D3 + D + 1] for a CRC length of L = 8.

The encoding is performed in a systematic form, which means that in GF(2), the polynomial:

yields a remainder equal to 0 when divided by the corresponding length-24 CRC generator polynomial, gCRC24A(D) or gCRC24B(D), the polynomial:

yields a remainder equal to 0 when divided by gCRC16(D), and the polynomial:

yields a remainder equal to 0 when divided by gCRC8(D).

The bits after CRC attachment are denoted by, where B = A+ L. The relation between ak and bk is:

for k = 0, 1, 2, …, A-1

for k = A, A+1, A+2, ..., A+L-1.

## 5.1.2Code block segmentation and code block CRC attachment

The input bit sequence to the code block segmentation is denoted by, where B > 0. If B is larger than the maximum code block size Z, segmentation of the input bit sequence is performed and an additional CRC sequence of L = 24 bits is attached to each code block. The maximum code block size is:

-Z = 6144.

If the number of filler bits F calculated below is not 0, filler bits are added to the beginning of the first block.

Note that if B < 40, filler bits are added to the beginning of the code block.

The filler bits shall be set to <NULL> at the input to the encoder.

Total number of code blocks C is determined by:

if

L = 0

Number of code blocks:

else

L = 24

Number of code blocks: .

end if

The bits output from code block segmentation, for C  0, are denoted by , where r is the code block number, and Kr is the number of bits for the code block number r.

Number of bits in each code block (applicable for C  0 only):

First segmentation size: = minimum K in table 5.1.3-3 such that

if

the number of code blocks with length  is =1, ,

else if

Second segmentation size: = maximum K in table 5.1.3-3 such that

Number of segments of size: .

Number of segments of size: .

end if

Number of filler bits:

for k = 0 to F-1-- Insertion of filler bits

end for

k = F

s = 0

for r = 0 to C-1

if

else

end if

while

end while

if C >1

The sequence  is used to calculate the CRC parity bits  according to clause 5.1.1 with the generator polynomial gCRC24B(D). For CRC calculation it is assumed that filler bits, if present, have the value 0.

while

end while

end if

end for

## 5.1.3Channel coding

The bit sequence input for a given code block to channel coding is denoted by, where K is the number of bits to encode. After encoding the bits are denoted by, where D is the number of encoded bits per output stream and i indexes the encoder output stream. The relation between  and  and between K and D is dependent on the channel coding scheme.

The following channel coding schemes can be applied to TrCHs:

-tail biting convolutional coding;

-turbo coding.

Usage of coding scheme and coding rate for the different types of TrCH is shown in table 5.1.3-1. Usage of coding scheme and coding rate for the different control information types is shown in table 5.1.3-2.

The values of D in connection with each coding scheme:

-tail biting convolutional coding with rate 1/3: D = K;

-turbo coding with rate 1/3: D = K + 4.

The range for the output stream index i is 0, 1 and 2 for both coding schemes.

Table 5.1.3-1: Usage of channel coding scheme and coding rate for TrCHs

Table 5.1.3-2: Usage of channel coding scheme and coding rate for control information

## 5.1.3.1Tail biting convolutional coding

A tail biting convolutional code with constraint length 7 and coding rate 1/3 is defined.

The configuration of the convolutional encoder is presented in figure 5.1.3-1.

The initial value of the shift register of the encoder shall be set to the values corresponding to the last 6 information bits in the input stream so that the initial and final states of the shift register are the same. Therefore, denoting the shift register of the encoder by, then the initial value of the shift register shall be set to

Figure 5.1.3-1: Rate 1/3 tail biting convolutional encoder

The encoder output streams,  and  correspond to the first, second and third parity streams, respectively as shown in Figure 5.1.3-1.

## 5.1.3.2Turbo coding

## 5.1.3.2.1Turbo encoder

The scheme of turbo encoder is a Parallel Concatenated Convolutional Code (PCCC) with two 8-state constituent encoders and one turbo code internal interleaver. The coding rate of turbo encoder is 1/3. The structure of turbo encoder is illustrated in figure 5.1.3-2.

The transfer function of the 8-state constituent code for the PCCC is:

G(D) = ,

where

g0(D) = 1 + D2 + D3,

g1(D) = 1 + D + D3.

The initial value of the shift registers of the 8-state constituent encoders shall be all zeros when starting to encode the input bits.

The output from the turbo encoder is

for .

If the code block to be encoded is the 0-th code block and the number of filler bits is greater than zero, i.e., F > 0, then the encoder shall set ck, = 0, k = 0,…,(F-1) at its input and shall set , k = 0,…,(F-1) and , k = 0,…,(F-1) at its output.

The bits input to the turbo encoder are denoted by, and the bits output from the first and second 8-state constituent encoders are denoted by and, respectively. The bits output from the turbo code internal interleaver are denoted by, and these bits are to be the input to the second 8-state constituent encoder.

Figure 5.1.3-2: Structure of rate 1/3 turbo encoder (dotted lines apply for trellis termination only)

## 5.1.3.2.2Trellis termination for turbo encoder

Trellis termination is performed by taking the tail bits from the shift register feedback after all information bits are encoded. Tail bits are padded after the encoding of information bits.

The first three tail bits shall be used to terminate the first constituent encoder (upper switch of figure 5.1.3-2 in lower position) while the second constituent encoder is disabled. The last three tail bits shall be used to terminate the second constituent encoder (lower switch of figure 5.1.3-2 in lower position) while the first constituent encoder is disabled.

The transmitted bits for trellis termination shall then be:

, , ,

, , ,

, , ,

## 5.1.3.2.3Turbo code internal interleaver

The bits input to the turbo code internal interleaver are denoted by, where K is the number of input bits. The bits output from the turbo code internal interleaver are denoted by.

The relationship between the input and output bits is as follows:

, i=0, 1…, (K-1)

where the relationship between the output index i and the input index  satisfies the following quadratic form:

The parameters  and  depend on the block size K and are summarized in Table 5.1.3-3.

Table 5.1.3-3: Turbo code internal interleaver parameters

## 5.1.4Rate matching

## 5.1.4.1Rate matching for turbo coded transport channels

The rate matching for turbo coded transport channels is defined per coded block and consists of interleaving the three information bit streams,  and, followed by the collection of bits and the generation of a circular buffer as depicted in Figure 5.1.4-1. The output bits for each code block are transmitted as described in clause 5.1.4.1.2.

Figure 5.1.4-1. Rate matching for turbo coded transport channels

The bit stream is interleaved according to the sub-block interleaver defined in clause 5.1.4.1.1 with an output sequence defined as and where is defined in clause 5.1.4.1.1.

The bit stream  is interleaved according to the sub-block interleaver defined in clause 5.1.4.1.1 with an output sequence defined as.

The bit stream  is interleaved according to the sub-block interleaver defined in clause 5.1.4.1.1 with an output sequence defined as.

The sequence of bits  for transmission is generated according to clause 5.1.4.1.2.

## 5.1.4.1.1Sub-block interleaver

The bits input to the block interleaver are denoted by , where D is the number of bits. The output bit sequence from the block interleaver is derived as follows:

(1)Assign to be the number of columns of the matrix. The columns of the matrix are numbered 0, 1, 2,…,from left to right.

(2)Determine the number of rows of the matrix, by finding minimum integer  such that:

The rows of rectangular matrix are numbered 0, 1, 2,…,from top to bottom.

(3)If, then  dummy bits are padded such that yk = <NULL> for k = 0, 1,…, ND - 1. Then, , k = 0, 1,…, D-1, and the bit sequence yk is written into the matrix row by row starting with bit y0 in column 0 of row 0:

For and:

(4)Perform the inter-column permutation for the matrix based on the pattern that is shown in table 5.1.4-1, where P(j) is the original column position of the j-th permuted column. After permutation of the columns, the inter-column permuted matrix is equal to

(5)The output of the block interleaver is the bit sequence read out column by column from the inter-column permuted matrix. The bits after sub-block interleaving are denoted by, where  corresponds to, to… and.

For:

(4) The output of the sub-block interleaver is denoted by, where  and where

The permutation function P is defined in Table 5.1.4-1.

Table 5.1.4-1 Inter-column permutation pattern for sub-block interleaver

## 5.1.4.1.2Bit collection, selection and transmission

The circular buffer of length  for the r-th coded block is generated as follows:

for k = 0,…,

for k = 0,…,

for k = 0,…,

Denote the soft buffer size for the transport block by NIR bits and the soft buffer size for the r-th code block by Ncb bits. The size Ncb is obtained as follows, where C is the number of code blocks computed in clause 5.1.2:

- for DL-SCH, PCH transport channels, and MCH configured with pmch-TimeInterleavingN

- for UL-SCH, MCH not configured with pmch-TimeInterleavingN, SL-SCH and SL-DCH transport channels

For UE category 0, for DL-SCH associated with SI-RNTI and RA-RNTI and PCH transport channel, Ncb is always equal to Kw.

Where NIR for MCH configured with pmch-TimeInterleavingN is equal to:

,

Where the coefficient β is configured by pmch-TimeInterleaving-scalingfactorBeta, M is configured by pmch-TimeInterleavingM, and  is the total number of soft channel bits according to a reference UE category configured by pmch-TimeInterleaving-refUECat.

Where NIR for DL-SCH and PCH transport channels is equal to:

Where the coefficient  is 1 for subframe duration, 0.5 for slot duration and for subslot duration of initial PDSCH transmission. For retransmission of a transport block with slot or subslot duration, is 1 if the transport block has initially been transmitted with subframe duration. For retransmission of a transport block with subframe duration,  is 0.5 if the transport block has initially been transmitted with slot duration, and if the transport block has initially been transmitted with subslot duration.

If the UE signals ue-CategoryDL-v14xy indicating UE category M2, Nsoft is the total number of soft channel bits according to the UE category indicated by ue-CategoryDL-v14xy. Otherwise, if the UE signals ue-CategoryDL-v1310 indicating UE category M1, Nsoft is the total number of soft channel bits according to the UE category indicated by ue-CategoryDL-v1310. Otherwise, if the UE signals ue-CategoryDL-v13xy, and is configured with transmission mode 9 or transmission mode 10 and the higher layer parameter maxLayersMIMO-r10 is configured to eightLayers, Nsoft is the total number of soft channel bits according to the UE category indicated by ue-CategoryDL-v13xy. Otherwise, if the UE signals ue-CategoryDL-r12 indicating UE category 0, or if the UE signals ue-CategoryDL-r12 indicating UE category 14 and is configured by higher layers with altCQI-Table-r12 for the DL cell, Nsoft is the total number of soft channel bits according to the UE category indicated by ue-CategoryDL-r12. Otherwise, if the UE signals ue-Category-v11a0, and is configured by higher layers with altCQI-Table-r12  or altCQI-Table-1024QAM-r15 for the DL cell, Nsoft is the total number of soft channel bits according to the UE category indicated by ue-Category-v11a0. Otherwise, if the UE signals ue-Category-v1020, and is configured with transmission mode 9 or transmission mode 10, or is configured with transmission mode 3 or transmission mode 4 and the higher layer parameter maxLayersMIMO-r10 is configured to fourLayers, for the DL cell, Nsoft is the total number of soft channel bits [4] according to the UE category indicated by ue-Category-v1020 [6]. Otherwise, Nsoft is the total number of soft channel bits [4] according to the UE category indicated by ue-Category (without suffix) [6].

If Nsoft = 35982720 or 47431680,

KC= 5,

elseif Nsoft = 303562752,

KC= 32,

elseif Nsoft = 14616576,

if the UE is configured by higher layers with altCQI-Table-r12,

KC = 3/2

else

KC = 2

end if.

elseif Nsoft = 19488768,

if the UE is configured by higher layers with altCQI-Table-1024QAM-r15,

KC = 8/5

elseif the UE is configured by higher layers with altCQI-Table-r12,

KC = 2

else

KC = 8/3

end if.

elseif Nsoft = 7308288 and the UE is configured by higher layers with altCQI-Table-r12,

if the UE is capable of supporting no more than a maximum of two spatial layers for the DL cell in the transmission mode configured for the UE, or if the configured maximum number of layers indicated by the maxLayersMIMO-r10 field is no more than two,

KC = 3

else

KC = 3/2

end if.

elseif Nsoft = 7308288 and the UE is configured by higher layers with altCQI-Table-1024QAM-r15,

if the UE is capable of supporting no more than a maximum of two spatial layers for the DL cell in the transmission mode configured for the UE, or if the configured maximum number of layers indicated by the maxLayersMIMO-r10 field is no more than two,

KC = 12/5

else

KC = 6/5

end if.

elseif Nsoft = 3654144 and the UE is capable of supporting no more than a maximum of two spatial layers for the DL cell, or if the configured maximum number of layers indicated by the maxLayersMIMO-r10 field is no more than two,

KC = 2

else

KC = 1

End if.

For initial PDSCH transmission with subframe duration, KMIMO is equal to 2 if the UE is configured to receive PDSCH transmissions based on transmission modes 3, 4, 8, 9 or 10 as defined in clause 7.1 of [3], and is equal to 1 otherwise. For BL/CE UE KMIMO is equal to 1. For initial PDSCH transmission with slot/subslot duration, KMIMO is equal to 1.

MDL_HARQ is the maximum number of DL HARQ processes as defined in clause 7 of [3].

Mlimit is a constant equal to 8.

Denoting by E the rate matching output sequence length for the r-th coded block, and rvidx the redundancy version number for this transmission (rvidx = 0, 1, 2 or 3 for DL-SCH and PCH transport channels, or rvidx = 0, 1,…, N-1 for MCH configured with higher layer parameter pmch-TimeInterleavingN), the rate matching output bit sequence is , k = 0,1,..., .

Define by G the total number of bits available for the transmission of one transport block.

Set where Qm is equal to 1 for π/2-BPSK, 2 for QPSK, 4 for 16QAM, 6 for 64QAM, 8 for 256QAM, and 10 for 1024QAM, and where

-For transmit diversity:

-NL is equal to 2,

-Otherwise:

-NL is equal to the number of layers a transport block is mapped onto

Set, where C is the number of code blocks computed in clause 5.1.2.

if

set

else

set

end if

Set for DL-SCH and PCH transport channels, or  for MCH configured with higher layer parameter pmch-TimeInterleavingN, where  is the number of rows defined in clause 5.1.4.1.1, and .

Set k = 0 and j = 0

while {k < E}

if

k = k +1

end if

j = j +1

end while

## 5.1.4.2Rate matching for convolutionally coded transport channels and control information

The rate matching for convolutionally coded transport channels and control information consists of interleaving the three bit streams, ,  and , followed by the collection of bits and the generation of a circular buffer as depicted in Figure 5.1.4-2. The output bits are transmitted as described in clause 5.1.4.2.2.

Figure 5.1.4-2. Rate matching for convolutionally coded transport channels and control information

The bit stream  is interleaved according to the sub-block interleaver defined in clause 5.1.4.2.1 with an output sequence defined as  and where  is defined in clause 5.1.4.2.1.

The bit stream  is interleaved according to the sub-block interleaver defined in clause 5.1.4.2.1 with an output sequence defined as.

The bit stream  is interleaved according to the sub-block interleaver defined in clause 5.1.4.2.1 with an output sequence defined as.

The sequence of bits  for transmission is generated according to clause 5.1.4.2.2.

## 5.1.4.2.1Sub-block interleaver

The bits input to the block interleaver are denoted by, where D is the number of bits. The output bit sequence from the block interleaver is derived as follows:

(1)Assignto be the number of columns of the matrix. The columns of the matrix are numbered 0, 1, 2,…,from left to right.

(2)Determine the number of rows of the matrix, by finding minimum integer  such that:

The rows of rectangular matrix are numbered 0, 1, 2,…,from top to bottom.

(3)If, then dummy bits are padded such that yk = <NULL> for k = 0, 1,…, ND - 1. Then, , k = 0, 1,…, D-1, and the bit sequence yk is written into the matrix row by row starting with bit y0 in column 0 of row 0:

(4)Perform the inter-column permutation for the matrix based on the pattern that is shown in table 5.1.4-2, where P(j) is the original column position of the j-th permuted column. After permutation of the columns, the inter-column permuted matrix is equal to

(5)The output of the block interleaver is the bit sequence read out column by column from the inter-column permutedmatrix. The bits after sub-block interleaving are denoted by, where  corresponds to,  to… and

Table 5.1.4-2 Inter-column permutation pattern for sub-block interleaver

This block interleaver is also used in interleaving PDCCH modulation symbols. In that case, the input bit sequence consists of PDCCH symbol quadruplets [2].

## 5.1.4.2.2Bit collection, selection and transmission

The circular buffer of length  is generated as follows:

for k = 0,…,

for k = 0,…,

for k = 0,…,

Denoting by E the rate matching output sequence length, the rate matching output bit sequence is , k = 0,1,..., .

Set k = 0 and j = 0

while {k < E}

if

k = k +1

end if

j = j +1

end while

## 5.1.5Code block concatenation

The input bit sequence for the code block concatenation block are the sequences , for  and . The output bit sequence from the code block concatenation block is the sequence  for .

The code block concatenation consists of sequentially concatenating the rate matching outputs for the different code blocks. Therefore,

Set  and

while

Set

while

end while

end while

## 5.2Uplink transport channels and control information

If the UE is configured with a Master Cell Group (MCG) and Secondary Cell Group (SCG) [6], the procedures described in this clause are applied to the MCG and SCG, respectively. When the procedures are applied to a SCG, the term primary cell refers to the primary SCell (PSCell) of the SCG.

If the UE is configured with a PUCCH SCell [6], the procedures described in this clause are applied to the group of DL cells associated with the primary cell and the group of DL cells associated with the PUCCH SCell, respectively. When the procedures are applied to the group of DL cells associated with the PUCCH SCell, the term primary cell refers to the PUCCH SCell.

If the UE is configured with a LAA SCell, the procedures described in this clause are applied assuming the LAA SCell is an FDD SCell.

## 5.2.1Random access channel

The sequence index for the random access channel is received from higher layers and is processed according to [2].

## 5.2.2Uplink shared channel

Figure 5.2.2-1 shows the processing structure for the UL-SCH transport channel on one UL cell. If sub-PRB allocation is used, data arrives to the coding unit in the form of one transport block over a number of subframes per UL cell. Otherwise, data arrives to the coding unit in the form of a maximum of two transport blocks every transmission time interval (TTI) per UL cell. The following coding steps can be identified for each transport block of an UL cell:

-Add CRC to the transport block

-Code block segmentation and code block CRC attachment

-Channel coding of data and control information

-Rate matching

-Code block concatenation

-Multiplexing of data and control information

-Channel interleaver

The coding steps for one UL-SCH transport block are shown in the figure below. The same general processing applies for each UL-SCH transport block on each UL cell with restrictions as specified in [3].

Figure 5.2.2-1: Transport block processing for UL-SCH

## 5.2.2.1Transport block CRC attachment

Error detection is provided on each UL-SCH transport block through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by. A is the size of the transport block and L is the number of parity bits. The lowest order information bit a0 is mapped to the most significant bit of the transport block as defined in clause 6.1.1 of [5].

The parity bits are computed and attached to the UL-SCH transport block according to clause 5.1.1 setting L to 24 bits and using the generator polynomial gCRC24A(D).

## 5.2.2.2Code block segmentation and code block CRC attachment

The bits input to the code block segmentation are denoted by  where B is the number of bits in the transport block (including CRC).

Code block segmentation and code block CRC attachment are performed according to clause 5.1.2.

The bits after code block segmentation are denoted by, where r is the code block number and Kr is the number of bits for code block number r.

## 5.2.2.3Channel coding of UL-SCH

Code blocks are delivered to the channel coding block. The bits in a code block are denoted by  , where r is the code block number, and Kr is the number of bits in code block number r. The total number of code blocks is denoted by C and each code block is individually turbo encoded according to clause 5.1.3.2.

After encoding the bits are denoted by, withand whereis the number of bits on the i-th coded stream for code block number r, i.e..

## 5.2.2.4Rate matching

Turbo coded blocks are delivered to the rate matching block. They are denoted by, with, and where r is the code block number, i is the coded stream index, and  is the number of bits in each coded stream of code block number r. The total number of code blocks is denoted by C and each coded block is individually rate matched according to clause 5.1.4.1.

After rate matching, the bits are denoted by, where r is the coded block number, and where  is the number of rate matched bits for code block number r.

## 5.2.2.5Code block concatenation

The bits input to the code block concatenation block are denoted by  for  and where  is the number of rate matched bits for the r-th code block.

Code block concatenation is performed according to clause 5.1.5.

The bits after code block concatenation are denoted by , where G is the total number of coded bits for transmission of the given transport block over  transmission layers excluding the bits used for control transmission, when control information is multiplexed with the UL-SCH transmission.

## 5.2.2.6Channel coding of control information

Control data arrives at the coding unit in the form of channel quality information (CQI and/or PMI), HARQ-ACK and rank indication, and CSI-RS resource indication (CRI). Different coding rates for the control information are achieved by allocating different number of coded symbols for its transmission. When control data are transmitted in the PUSCH, the channel coding for HARQ-ACK, rank indication (including RI only, joint report of RI/i1, joint report of CRI/RI, joint report of CRI/RI/i1, joint report of CRI/RI/PTI, joint report of RI/i1,p-2, and joint report of RI/PTI), CRI and channel quality information  is done independently. Parameters i1,1-1 , i1,2-1 , i1,1-2 , i1,2-2 , i1,p-2 correspond to parameters , , , , and  in clause 7.2.4 of [3].

For the cases with TDD primary cell, the number of HARQ-ACK bits is determined as described in clause 7.3 of [3].

When the UE transmits HARQ-ACK bits, rank indicator bits or CRI bits, it shall determine the number of coded modulation symbols per layer  for HARQ-ACK, rank indicator, or CRI bits as follows.

For the case when only one transport block is transmitted in the PUSCH conveying the HARQ-ACK bits, rank indicator bits or CRI bits:

where

- is the number of HARQ-ACK bits, rank indicator bits or CRI bits, and

-is 4 for PUSCH with subframe duration, or for Partial PUSCH Mode 1.  is 2 for PUSCH with slot duration, or for Partial PUSCH Mode 2 or 3.  is 1 for PUSCH with subslot duration.

- is the scheduled bandwidth for PUSCH transmission in the current subframe/slot/subslot for the transport block, expressed as a number of subcarriers in [2], and

-is the number of SC-FDMA symbols per subframe/slot/subslot for initial PUSCH transmission for the same transport block, respectively, given by , where

- for PUSCH with slot duration, or for Partial PUSCH Mode 2 or 3, or

- for PUSCH with subslot duration,

- is the number of SC-FDMA symbols of the subslot as defined in clause 4.1 of [2],

- is the number of SC-FDMA symbols for DMRS of the subslot as defined in clause 5.5.2.1.2 of [2]

-otherwise .

- is equal to 1

-if UE configured with one UL cell is configured to send PUSCH and SRS in the same subframe/slot/subslot for initial transmission, or

-if UE transmits PUSCH and SRS in the same subframe/slot/subslot in the same serving cell for initial transmission, or

-if the PUSCH resource allocation for initial transmission even partially overlaps with the cell-specific SRS subframe and bandwidth configuration defined in clause 5.5.3 of [2], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the subframe/slot/subslot for initial transmission in the same serving cell is in a UE-specific type-1 SRS subframe as defined in Clause 8.2 of [3], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the subframe/slot/subslot for initial transmission in the same serving cell is in a UE-specific type-0 SRS subframe as defined in clause 8.2 of [3] and the UE is configured with multiple TAGs, and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe.

-Otherwise  is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH not starting from the beginning of the first symbol or the seventh symbol of the subframe for initial transmission, otherwise is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH up to the second to last symbol of the subframe for initial transmission and  is equal to 0, otherwise is equal to 0.

-, , and  are obtained from the initial PDCCH or EPDCCH or MPDCCH or SPDCCH for the same transport block. If there is no initial PDCCH or EPDCCH with DCI format 0/0A/0B/4A/4B or MPDCCH with DCI format 6-0A/6-0B or SPDCCH with DCI format 7-0A/7-0B for the same transport block, , , and  shall be determined from:

-the most recent semi-persistent scheduling assignment PDCCH or EPDCCH or MPDCCH or SPDCCH, when the initial PUSCH for the same transport block is semi-persistently scheduled, or,

-the random access response grant for the same transport block, when the PUSCH is initiated by the random access response grant, or

-the most recent AUL activation DCI as defined in [3], when the initial PUSCH for the same transport block is AUL PUSCH.

For the case when two transport blocks are transmitted in the PUSCH conveying the HARQ-ACK bits, rank indicator bits or CRI bits:

with

where

- is the number of HARQ-ACK bits, rank indicator bits or CRI bits, and

- if , if  with  where  is the modulation order of transport block "x", and  if  with  and .

- are the scheduled bandwidths or bandwidths assigned by the most recent AUL activation DCI as defined in [3] for PUSCH transmission in the initial sub-frame for the first and second transport block, respectively, expressed as a number of subcarriers in [2], and

-are the number of SC-FDMA symbols per subframe for initial PUSCH transmission for the first and second transport block given by , where

- for Partial PUSCH Mode 2 or 3,

-otherwise .

- is equal to 1

-if UE configured with one UL cell is configured to send PUSCH and SRS in the same subframe for initial transmission, or

-if UE transmits PUSCH and SRS in the same subframe in the same serving cell for initial transmission of transport block "x", or

-if the PUSCH resource allocation for initial transmission of transport bock "x" even partially overlaps with the cell-specific SRS subframe and bandwidth configuration defined in clause 5.5.3 of [2] , or

-if the subframe for initial transmission of transport block "x" in the same serving cell is a UE-specific type-1 SRS subframe as defined in Clause 8.2 of [3], or

-if the subframe for initial transmission of transport block "x" in the same serving cell is a UE-specific type-0 SRS subframe as defined in clause 8.2 of [3] and the UE is configured with multiple TAGs.

-Otherwise  is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH for the first and second transport block not starting from the beginning of the first symbol or the seventh symbol of the subframe for initial transmission, otherwise is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH for the first and second transport block up to the second to last symbol of the subframe for initial transmission and  is equal to 0, otherwise is equal to 0.

-, , and  are obtained from the initial PDCCH or EPDCCH for the corresponding transport block, or from the most recent AUL activation DCI as defined in [3], when the initial PUSCH for the corresponding transport block is AUL PUSCH.

For HARQ-ACK,  and , where is the modulation order of a given transport block. For UEs configured with no more than five DL cells,  shall be determined according to [3] depending on the number of transmission codewords for the corresponding PUSCH, the duration for the corresponding PUSCH (subslot/slot/subframe), and the beta offset indicator in SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot. For UEs configured with more than five DL cells,  shall be determined according to [3] depending on the number of transmission codewords for the corresponding PUSCH, the number of HARQ-ACK feedback bits, the duration for the corresponding PUSCH (subslot/slot/subframe), and the beta offset indicator in SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot.

For rank indication or CRI, ,  and , whereis the modulation order of a given transport block, and  shall be determined according to [3] depending on the number of transmission codewords for the corresponding PUSCH, the duration for the corresponding PUSCH, the beta offset indicator in SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot, and on the uplink power control subframe set for the corresponding PUSCH when two uplink power control subframe sets are configured by higher layers for the cell.

For HARQ-ACK

-Each positive acknowledgement (ACK) is encoded as a binary '1' and each negative acknowledgement (NACK) is encoded as a binary '0'

-If HARQ-ACK feedback consists of 1-bit of information, i.e., , it is first encoded according to Table 5.2.2.6-1.

-If HARQ-ACK feedback consists of 2-bits of information, i.e.,  with  corresponding to HARQ-ACK bit for codeword 0 and  corresponding to that for codeword 1, or if HARQ-ACK feedback consists of 2-bits of information as a result of the aggregation of HARQ-ACK bits corresponding to two DL cells with which the UE is configured by higher layers, or if HARQ-ACK feedback consists of 2-bits of information corresponding to two subframes for TDD, it is first encoded according to Table 5.2.2.6-2 where .

Table 5.2.2.6-1: Encoding of 1-bit HARQ-ACK

Table 5.2.2.6-2: Encoding of 2-bit HARQ-ACK

-If HARQ-ACK feedback consists of  bits of information as a result of the aggregation of HARQ-ACK bits corresponding to one or more DL cells with which the UE is configured by higher layers, i.e., , then a coded bit sequence  is obtained by using the bit sequence  as the input to the channel coding block described in clause 5.2.2.6.4. In turn, the bit sequence  is obtained by the circular repetition of the bit sequence  so that the total bit sequence length is equal to.

-If HARQ-ACK feedback consists of  bits of information as a result of the aggregation of HARQ-ACK bits corresponding to one or more DL cells with which the UE is configured by higher layers, i.e., , then the coded bit sequence  is obtained by using the bit sequence  as the input to the channel coding block described in clause 5.2.2.6.5.

-If HARQ-ACK feedback consists of  bits of information as a result of the aggregation of HARQ-ACK bits corresponding to one or more DL cells with which the UE is configured by higher layers, the coded bit sequence is denoted by . The CRC attachment, channel coding and rate matching of the HARQ-ACK bits are performed according to clauses 5.1.1 setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

The "x" and "y" in Table 5.2.2.6-1 and 5.2.2.6-2 are placeholders for [2] to scramble the HARQ-ACK bits in a way that maximizes the Euclidean distance of the modulation symbols carrying HARQ-ACK information.

For FDD or TDD HARQ-ACK multiplexing or the aggregation of more than one DL cell including at least one cell using FDD and at least one cell using TDD when HARQ-ACK consists of one or two bits of information, the bit sequence  is obtained by concatenation of multiple encoded HARQ-ACK blocks where  is the total number of coded bits for all the encoded HARQ-ACK blocks. The last concatenation of the encoded HARQ-ACK block may be partial so that the total bit sequence length is equal to.

For UEs configured by higher layers with dl-STTI-Length, if codebooksizeDeterminationSTTI-rel15 is configured as dai, the bit sequence  corresponding to PDSCH with slot/subslot duration is determined according to the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]; otherwise, the bit sequence  is determined as below.

For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, define the bit sequence  corresponding to PDSCH with slot/subslot duration as the result of the concatenation of HARQ-ACK bits for one or multiple DL cells configured with higher layer parameter dl-STTI-Length,  as the number of cells configured with dl-STTI-Length for the UE and  as the number of slot(s) or subslot(s) for which the UE needs to feed back HARQ-ACK bits in UL slot or subslot n for the c-th serving cell. For a cell using FDD and configured with dl-STTI-Length=subslot and ul-STTI-Length=subslot, or for a cell using FDD and configured with dl-STTI-Length=slot and ul-STTI-Length=slot, . For a cell using FDD and configured with dl-STTI-Length=subslot and ul-STTI-Length=slot, . For a cell using TDD, if slot n-4 in the cell is in a DL subframe, or slot n-4 is the first slot in a special subframe with special subframe configurations 1/2/3/4/6/7/8/9/10 and normal downlink CP, or slot n-4 is the second slot in a special subframe with special subframe configurations 3/4/8 and normal downlink CP, and  otherwise. o0sACK o1sACK, …, oosACK-1sACK

The bit sequence  is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell configured with dl-STTI-Length

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

HARQ-ACK bit of this cell

j = j + 1

l=l+1

end while

c = c + 1

end while

For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, define the bit sequence  corresponding to PDSCH with subframe duration as the result of the concatenation of HARQ-ACK bits for one or multiple DL cells. The bit sequence is determined as below for bit sequence  and spatial bundling is performed if the HARQ-ACK is to be transmitted on subslot PUSCH or if the HARQ-ACK is to be transmitted on slot PUSCH and spatial bundling is configured.o0sACK o1sACK, …, oosACK-1sACK

For UEs configured by higher layers with codebooksizeDetermination-r13 = dai, the bit sequence  corresponding to PDSCH with subframe duration is determined according to the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]. Otherwise, the bit sequence  is determined as below.

For FDD when the UE is not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, when HARQ ACK consists of 2 or more bits of information as a result of the aggregation of more than one DL cell, the bit sequence  corresponding to PDSCH with subframe duration is the result of the concatenation of HARQ-ACK bits for the multiple DL cells according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

Set  to the number of cells configured by higher layers for the UE

while c <

if transmission mode configured in cell – 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell

j = j + 1

else

if the PUSCH is with subframe or slot duration and the UE is not configured with spatial bundling on PUSCH by higher layers

HARQ-ACK bit corresponding to the first codeword of this cell

j = j + 1

HARQ-ACK bit corresponding to the second codeword of this cell

j = j + 1

else

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

j = j + 1

end if

end if

c = c + 1

end while

For the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD when the UE is not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, the bit sequence  is the result of the concatenation of HARQ-ACK bits for one or multiple DL cells. Define  as the number of cells configured by higher layers for the UE and  as the number of subframes for which the UE needs to feed back HARQ-ACK bits in UL subframe n for the c-th serving cell. For a cell using TDD, the subframes are determined by the DL-reference UL/DL configuration if the UE is configured with higher layer parameter eimta-HARQ-ReferenceConfig, and determined by the UL/DL configuration otherwise. For a cell using TDD,  if subframe n-4 in the cell, or subframe n-3 in the cell if higher layer parameter shortProcessingTime is configured for the cell, is a DL subframe or a special subframe with special subframe configurations 1/2/3/4/6/7/8/9/10 and normal downlink CP or a special subframe with special subframe configurations 1/2/3/5/6/7 and extended downlink CP, and  otherwise. For a cell using FDD, .

The bit sequence  is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

if

if transmission mode configured in cell  – 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell

j = j + 1

else

if the PUSCH is with subframe or slot duration and the UE is not configured with spatial bundling on PUSCH by higher layers

HARQ-ACK bit corresponding to the first codeword of this cell

j = j + 1

HARQ-ACK bit corresponding to the second codeword of this cell

j = j + 1

else

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

j = j + 1

end if

end if

end if

c = c + 1

end while

For the cases with TDD primary cell or EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured, when HARQ-ACK is for the aggregation of one or more DL cells and the UE is configured with PUCCH format 3, PUCCH format 4 or PUCCH format 5 [3], the bit sequence  is the result of the concatenation of HARQ-ACK bits for the one or more DL cells configured by higher layers and the multiple subframes as defined in [3].

Define  as the number of cells configured by higher layers for the UE and  as the number of subframes for which the UE needs to feed back HARQ-ACK bits as defined in Clause 7.3 of [3].

The number of HARQ-ACK bits for the UE to convey if it is configured with PUCCH format 3, PUCCH format 4 or PUCCH format 5 is computed as follows:

Set k = 0 – counter of HARQ-ACK bits

Set c=0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

while c <

set l = 0;

while l <

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

k = k + 1

else

k = k + 2

end if

l = l+1

end while

c = c + 1

end while

When PUCCH format 3 is configured, if k ≤ 20 when TDD is used in all the configured serving cell(s) of the UE, or if k ≤ 21 when FDD is used in at least one of the configured serving cells with TDD primary cell, or if k ≤ 21 when the UE is configured with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2; or when PUCCH format 4 or PUCCH format 5 is configured and when the UE is not configured with spatial bundling on PUSCH by higher layers, the multiplexing of HARQ-ACK bits is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell as defined in Clause 7.3 of [3]

j = j + 1

else

HARQ-ACK bits of this cell as defined in Clause 7.3 of [3]

j = j + 2

end if

l = l+1

end while

c = c + 1

end while

When PUCCH format 3 is configured, if k > 20 when TDD is used in all the configured serving cell(s) of the UE, or if k > 21 when FDD is used in at least one of the configured serving cells with TDD primary cell, or if k > 21 when the UE is configured with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, spatial bundling is applied to all subframes in all cells; or when PUCCH format 4 or PUCCH format 5 is configured and when the UE is configured with spatial bundling on PUSCH by higher layers; or when the PUSCH is subslot duration, the multiplexing of HARQ-ACK bits is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

if transmission mode configured in cell  – 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell as defined in Clause 7.3 of [3]

j = j + 1

else

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell as defined in Clause 7.3 of [3]

j = j + 1

end if

l = l+1

end while

c = c + 1

end while

For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, bit sequence is obtained by concatenation of the bit sequence  and , where  in the cases defined in clause 7.3 of [3]. In all other cases, the sequence of bits  is given by. For the cases with TDD primary cell with at least one cell configured with higher layer parameter dl-STTI-Length, the bit sequence  is as defined in [3].

For  or , the bit sequence  is obtained by setting .

For , the bit sequence  is obtained by setting  if i is even and  if i is odd.

For the cases with TDD primary cell when HARQ-ACK is for the aggregation of two DL cells and the UE is configured with PUCCH format 1b with channel selection, the bit sequence is obtained as described in clause 7.3 of [3].

For TDD HARQ-ACK bundling, a bit sequence  is obtained by concatenation of multiple encoded HARQ-ACK blocks where  is the total number of coded bits for all the encoded HARQ-ACK blocks. The last concatenation of the encoded HARQ-ACK block may be partial so that the total bit sequence length is equal to. A scrambling sequence  is then selected from Table 5.2.2.6-A with index , where  is determined as described in clause 7.3 of [3]. The bit sequence  is then generated by setting  if HARQ-ACK consists of 1-bit and  if HARQ-ACK consists of 2-bits and then scrambling  as follows

Set i, k to 0

while

if // place-holder repetition bit

else

if // a place-holder bit

else// coded bit

end if

end while

Table 5.2.2.6-A: Scrambling sequence selection for TDD HARQ-ACK bundling

When HARQ-ACK information is to be multiplexed with UL-SCH at a given PUSCH, the HARQ-ACK information is multiplexed in all layers of all transport blocks of that PUSCH, For a given transport block, the vector sequence output of the channel coding for HARQ-ACK information is denoted by , where ,  are column vectors of length  and where  is obtained as follows:

Set i, k to 0

while

-- temporary row vector

-- replicating the row vector NL times and transposing into a column vector

end while

where  is the number of layers onto which the UL-SCH transport block is mapped.

For rank indication (RI) (RI only, joint report of RI and i1, joint report of CRI and RI, joint report of CRI, RI and i1, joint report of CRI, RI, and PTI, joint report of RI and i1,p-2, and joint report of RI and PTI) or CRI

-The corresponding bit widths for CRI feedback for PDSCH transmissions are given by Tables 5.2.2.6.1-2A, 5.2.2.6.1-2C, 5.2.2.6.1-2G, 5.2.2.6.2-3A, 5.2.2.6.2-3C, 5.2.2.6.2-3G, 5.2.2.6.3-3A, 5.2.2.6.3-3C, 5.2.2.6.3-3G, 5.2.3.3.1-3E, 5.2.3.3.1-3H, 5.2.3.3.2-4E, and 5.2.3.3.2-4H.

-The corresponding bit widths for RI feedback for PDSCH transmissions are given by Tables 5.2.2.6.1-2, 5.2.2.6.1-2B, 5.2.2.6.1-2D, 5.2.2.6.1-2E, 5.2.2.6.1-2F, 5.2.2.6.2-3, 5.2.2.6.2-3B, 5.2.2.6.2-3D, 5.2.2.6.2-3E, 5.2.2.6.2-3F, 5.2.2.6.3-3, 5.2.2.6.3-3B, 5.2.2.6.3-3D, 5.2.2.6.3-3E, 5.2.2.6.3-3F, 5.2.3.3.1-3, 5.2.3.3.1-3A, 5.2.3.3.1-3B, 5.2.3.3.1-3B-1, 5.2.3.3.1-3C, 5.2.3.3.1-3D, 5.2.3.3.1-3F, 5.2.3.3.1-3G, 5.2.3.3.1-3I, 5.2.3.3.1-3J, 5.2.3.3.1-5, 5.2.3.3.2-4, 5.2.3.3.2-4A, 5.2.3.3.2-4B, 5.2.3.3.2-4C, 5.2.3.3.2-4D, 5.2.3.3.2-4F, 5.2.3.3.2-4G and 5.2.3.3.2-4I which are determined assuming the maximum number of layers as follows:

-If the maxLayersMIMO-r10 is configured for the DL cell, the maximum number of layers for subframe operation is determined according to maxLayersMIMO-r10 for the DL cell.

-If the UE is configured with ShortTTI and if the higher layer parameter maxLayersMIMO-sTTI-r15 is configured for the DL cell, the maximum number of layers for slot/subslot operation is determined according to maxLayersMIMO-sTTI-r15 for the DL cell.

-Else,

-If the UE is configured with transmission mode 9, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the configured number of CSI-RS ports and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the maximum of number of antenna port of the configured CSI-RS resources and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the configured number of CSI-RS ports and ue-Category (without suffix).

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the maximum of number of antenna port of the configured CSI-RS resources and ue-Category (without suffix).

-If the UE is configured with transmission mode 9, and higher layer parameter semiOpenLoop, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of 2 and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9, and higher layer parameter semiOpenLoop, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of 2 and ue-Category (without suffix).

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 with activatedResources>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the maximum of number of antenna ports of the activated CSI-RS resources and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 with activatedResources>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the maximum of number of antenna ports of the activated CSI-RS resources and ue-Category (without suffix).

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with activatedResources=1 or numberActivatedAperiodicCSI-RS-Resources>0, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the number of antenna port of the activated or selected CSI-RS resource and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with activatedResources=1 or numberActivatedAperiodicCSI-RS-Resources>0, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the number of antenna ports of the activated or selected CSI-RS resource and ue-Category (without suffix).

-If the UE is configured with transmission mode 9 and higher layer parameter eMIMO-Type and eMIMO-Type2, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the configured number of CSI-RS ports of eMIMO-Type2 and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 9 and higher layer parameter eMIMO-Type and eMIMO-Type2, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers is determined according to the minimum of the configured number of CSI-RS ports of eMIMO-Type2 and ue-Category (without suffix).

-If the UE is configured with transmission mode 10, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the configured number of CSI-RS ports for that CSI process and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the maximum of number of antenna port of the configured CSI-RS resources in that CSI process and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the configured number of CSI-RS ports for that CSI process and ue-Category (without suffix).

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the maximum of number of antenna port of the configured CSI-RS resources in that CSI process and ue-Category (without suffix).

-If the UE is configured with transmission mode 10, and higher layer parameter semiOpenLoop, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of 2 and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10, and higher layer parameter semiOpenLoop, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of 2 and ue-Category (without suffix).

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 with activatedResources>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the maximum of number of antenna ports of the activated CSI-RS resources in that CSI process and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 with activatedResources>1, and RI and CRI are transmitted in the same reporting instance, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the maximum of number of antenna port of the activated CSI-RS resources in that CSI process and ue-Category (without suffix).

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with activatedResources=1 or numberActivatedAperiodicCSI-RS-Resources>0, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the number of antenna ports of the activated or selected CSI-RS resource in that CSI process and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with activatedResources=1 or numberActivatedAperiodicCSI-RS-Resources>0, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the number of antenna port of the activated or selected CSI-RS resource in that CSI process and ue-Category (without suffix).

-If the UE is configured with transmission mode 10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and the supportedMIMO-CapabilityDL-r10 field is included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the configured number of CSI-RS ports of eMIMO-Type2 for that CSI process and the maximum of the reported UE downlink MIMO capabilities for the same band in the corresponding band combination.

-If the UE is configured with transmission mode 10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and the supportedMIMO-CapabilityDL-r10 field is not included in the UE-EUTRA-Capability, the maximum number of layers for each CSI process is determined according to the minimum of the configured number of CSI-RS ports of eMIMO-Type2 for that CSI process and ue-Category (without suffix)

-Otherwise the maximum number of layers is determined according to the minimum of the number of PBCH antenna ports and ue-Category (without suffix).

-If RI feedback consists of 1-bit of information, i.e., , it is first encoded according to Table 5.2.2.6-3. The  to RI mapping is given by Table 5.2.2.6-5.

-If RI feedback consists of 2-bits of information, i.e.,  with  corresponding to MSB of 2-bit input and  corresponding to LSB, it is first encoded according to Table 5.2.2.6-4 where . The  to RI mapping is given by Table 5.2.2.6-6A if the UE is configured with higher layer parameter feCoMP-CSI-Enabled, otherwise given by Table 5.2.2.6-6.

Table 5.2.2.6-3: Encoding of 1-bit RI

Table 5.2.2.6-4: Encoding of 2-bit RI

Table 5.2.2.6-5:  to RI mapping

Table 5.2.2.6-6: , to RI mapping

Table 5.2.2.6-6A: , to RI mapping

Table 5.2.2.6-7: , , to RI mapping

Table 5.2.2.6-8: , , ,to RI mapping

-If RI feedback for a given DL cell consists of 3-bits of information, i.e.,  with  corresponding to MSB of 3-bit input and  corresponding to LSB. The  to RI mapping is given by Table 5.2.2.6-7.

-If RI feedback for a given DL cell consists of 4-bits of information when the UE is configured with higher layer parameter feCoMP-CSI-Enabled, i.e.,  with  corresponding to MSB of 4-bit input and  corresponding to LSB, the  to RI mapping is given by Table 5.2.2.6-8.

-If RI feedback consists of  bits of information, i.e., , then a coded bit sequence  is obtained by using the bit sequence  as the input to the channel coding block described in clause 5.2.2.6.4.

-If RI feedback consists of  bits of information as a result of the aggregation of RI bits corresponding to multiple DL cells or multiple CSI processes, i.e., , then the coded bit sequence  is obtained by using the bit sequence  as the input to the channel coding block described in clause 5.2.2.6.5.

-If RI feedback consists of  bits of information as a result of the aggregation of RI bits corresponding to multiple DL cells or multiple CSI processes, i.e., , then the coded bit sequence is denoted by . The CRC attachment, channel coding and rate matching of the HARQ-ACK bits are performed according to clauses 5.1.1 setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

-A UE capable of supporting only up to 5 serving cells is not expected to support CRI/RI payload larger than 22 bits.

The "x" and "y" in Table 5.2.2.6-3 and 5.2.2.6-4 are placeholders for [2] to scramble the RI bits in a way that maximizes the Euclidean distance of the modulation symbols carrying rank information.

For the case where RI feedback for more than one DL cell is to be reported, the RI report for each DL cell is concatenated prior to coding in increasing order of cell index.

For the case where RI feedback for more than one CSI process is to be reported, the RI reports are concatenated prior to coding first in increasing order of CSI process index for each DL cell and then in increasing order of cell index.

For the case where RI feedback consists of one or two bits of information the bit sequence  is obtained by concatenation of multiple encoded RI blocks where  is the total number of coded bits for all the encoded RI blocks. The last concatenation of the encoded RI block may be partial so that the total bit sequence length is equal to.

For the case where RI feedback consists of bits of information, the bit sequence  is obtained by the circular repetition of the bit sequence  so that the total bit sequence length is equal to.

For the case where CRI feedback is to be reported, the same procedures for RI are applied for CRI. When rank information is to be multiplexed with UL-SCH at a given PUSCH, the rank information is multiplexed in all layers of all transport blocks of that PUSCH. For a given transport block, the vector sequence output of the channel coding for rank information is denoted by , where ,  are column vectors of length  and where . The vector sequence is obtained as follows:

Set i, j, k to 0

while

-- temporary row vector

-- replicating the row vector NL times and transposing into a column vector

end while

where  is the number of layers onto which the UL-SCH transport block is mapped.

The same processing procedures for RI and RI multiplexing with UL-SCH at a given PUSCH are applied for CRI, using CRI instead of RI in the equations.

For channel quality control information (CQI and/or PMI denoted as CQI/PMI);

When the UE transmits channel quality control information bits, it shall determine the number of modulation coded symbols per layer  for channel quality information as

where

- is the number of CQI/PMI bits, and

- is the number of CRC bits given by , and

-and , where  shall be determined according to [3] depending on the number of transmission codewords for the corresponding PUSCH, the duration of the corresponding PUSCH, and on the uplink power control subframe set for the corresponding PUSCH when two uplink power control subframe sets are configured by higher layers for the cell.

-If neither RI nor CRI is not transmitted then .

The variable "x" in  represents the transport block index corresponding to the highest IMCS value indicated by the initial UL grant. In case the two transport blocks have the same IMCS value in the corresponding initial UL grant, "x =1", which corresponds to the first transport block. , , and  are obtained from the initial PDCCH or EPDCCH or MPDCCH or SPDCCH for the same transport block. If there is no initial PDCCH or EPDCCH with DCI format 0/0A/0B/4A/4B or MPDCCH with DCI format 6-0A/6-0B or SPDCCH with DCI format 7-0A/7-0B for the same transport block, , , and  shall be determined from:

-the most recent semi-persistent scheduling assignment PDCCH or EPDCCH or MPDCCH or SPDCCH, when the initial PUSCH for the same transport block is semi-persistently scheduled, or,

-the random access response grant for the same transport block, when the PUSCH is initiated by the random access response grant, or

-the most recent AUL activation DCI as defined in [3], when the initial PUSCH for the same transport block is AUL PUSCH.

is the number of SC-FDMA symbols per subframe/slot/subslot for initial PUSCH transmission for the same transport block.

For UL-SCH data information , where

- is the number of layers the corresponding UL-SCH transport block is mapped onto, and

- is the scheduled bandwidth for PUSCH transmission in the current subframe/slot/subslot for the transport block, and

- is the number of SC-FDMA symbols in the current PUSCH transmission subframe/slot/subslot given by , where

- for PUSCH with slot duration, or for Partial PUSCH Mode 2 or 3, or

- for PUSCH with subslot duration,

- is the number of SC-FDMA symbols of the subslot as defined in clause 4.1 of [2],

- is the number of SC-FDMA symbols for DMRS of the subslot as defined in clause 5.5.2.1.2 of [2]

-otherwise .

- is equal to 1 for non-BL/CE UEs and BL/CE UEs in CEModeA

-if UE configured with one UL cell is configured to send PUSCH and SRS in the same subframe for the current subframe/slot/subslot, or

-if UE transmits PUSCH and SRS in the same subframe/slot/subslot for the current subframe in the same serving cell, or

-if the PUSCH resource allocation for the current subframe even partially overlaps with the cell-specific SRS subframe and bandwidth configuration defined in clause 5.5.3 of [2], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the current subframe/slot/subslot in the same serving cell is a UE-specific type-1 SRS subframe as defined in Clause 8.2 of [3], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the current subframe/slot/subslot in the same serving cell is a UE-specific type-0 SRS subframe as defined in clause 8.2 of [3] and the UE is configured with multiple TAGs, and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe.

-Otherwise  is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH not starting from the beginning of the first symbol or the seventh symbol of the current subframe, otherwise is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH up to the second to last symbol of the current subframe and  is equal to 0, otherwise is equal to 0.

In case of CQI/PMI report for more than one DL cell,  is the result of concatenating the CQI/PMI report for each DL cell in increasing order of cell index. For the case where CQI/PMI feedback for more than one CSI process is to be reported,  is the result of concatenating the CQI/PMI reports in increasing order of CSI process index for each DL cell and then in increasing order of cell index.

-If the payload size is less than or equal to 11 bits, the channel coding of the channel quality information is performed according to clause 5.2.2.6.4 with input sequence .

-For payload sizes greater than 11 bits, the CRC attachment, channel coding and rate matching of the channel quality information is performed according to clauses 5.1.1, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

The output sequence for the channel coding of channel quality information is denoted by , where  is the number of layers the corresponding UL-SCH transport block is mapped onto.

## 5.2.2.6.1Channel quality information formats for wideband CQI reports

If the parameter CQI-ReportModeAperiodic is configured to the value of rm12 by higher layers [6], the fields and the corresponding bit widths for channel quality information and rank indication feedback are described as below.

Table 5.2.2.6.1-1, Table 5.2.2.6.1-1A and Table 5.2.2.6.1-1B show the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 4, transmission mode 6, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, eMIMO-Type is set to 'CLASS B' for a CSI process with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.2.6.1-1-1 and Table 5.2.2.6.1-1A-1 show the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

Table 5.2.2.6.1-1B-1 and Table 5.2.2.6.1-1B-2 show the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE.

Table 5.2.2.6.1-1B-3 shows the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4 antenna ports with K>1, and higher layer parameter feCoMP-CSI-Enabled=true with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].For Table 5.2.2.6.1-1-1, Table 5.2.2.6.1-1A-1 and Table 5.2.2.6.1-1B-3, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.1-1C and Table 5.2.2.6.1-1D show the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE.

Table 5.2.2.6.1-1D-1 and Table 5.2.2.6.1-1D-2 show the fields and corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE.

Table 5.2.2.6.1-1E shows the fields and corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE.

For Table 5.2.2.6.1-1, Table 5.2.2.6.1-1-1, Table 5.2.2.6.1-1A, Table 5.2.2.6.1-1A-1, Table 5.2.2.6.1-1B, Table 5.2.2.6.1-1B-1, Table 5.2.2.6.1-1B-2, Table 5.2.2.6.1-1B-3, Table 5.2.2.6.1-1C, Table 5.2.2.6.1-D, Table 5.2.2.6.1-1D-1, Table 5.2.2.6.1-1D-2 and Table 5.2.2.6.1-1E,  is defined in clause 7.2 of [3]. For Table 5.2.2.6.1-1B-1, Table 5.2.2.6.1-1B-2, Table 5.2.2.6.1-1C, Table 5.2.2.6.1-D, Table 5.2.2.6.1-1D-1 and Table 5.2.2.6.1-1D-2, the codebook configuration  is defined in [3], and CodebookConfig is configured by higher layers [6]. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4. The parameters  are defined as  and  for  and ,  and  for  and , and  and  for .

Table 5.2.2.6.1-1: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 4, transmission mode 6, transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1-1: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1A: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 8 antenna ports with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.1-1A-1: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 8 antenna ports with K>1 and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-1B: Fields for channel quality information feedback for wideband CQI and subband PMI reports with 4 antenna ports (transmission mode 8, transmission mode 9 and transmission mode 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4 antenna ports with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1B-1: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.1-1B-2: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.1-1B-3: Fields for channel quality information feedback for wideband CQI and subband PMI reports with 4 antenna ports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4 antenna ports with K>1, and higher layer parameter feCoMP-CSI-Enabled=true with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1C: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.1-1D: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.1-1D-1: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled= TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.1-1D-2: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled= TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.1-1E: Fields for channel quality information feedback for wideband CQI and subband PMI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports with K=1 with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE)

If the parameter CQI-ReportModeAperiodic is configured to the value of rm10-v13xy by higher layers [6], the fields and the corresponding bit widths for channel quality information and rank indication feedback are described as below.

Table 5.2.2.6.1-1F shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true.

Table 5.2.2.6.1-1F-1 shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true.

Table 5.2.2.6.1-1G shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' with 2/4/8 antenna ports without PMI reporting.

Table 5.2.2.6.1-1G-1 shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true.

For Table 5.2.2.6.1-1F-1 and Table 5.2.2.6.1-1G-1, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.1-1F: Fields for channel quality information feedback for wideband CQI reports (transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-1F-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-1G: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' with 2/4/8 antenna ports without PMI reporting)

Table 5.2.2.6.1-1G-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true)

If the parameter CQI-ReportModeAperiodic is configured to the value of rm11-v13xx by higher layers [6], the fields and the corresponding bit widths for channel quality information and rank indication feedback are described as below.

Table 5.2.2.6.1-1H, Table 5.2.2.6.1-1I and Table 5.2.2.6.1-1J show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 4, transmission mode 5, transmission mode 6, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.2.6.1-1H-1, Table 5.2.2.6.1-1I-1 show the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

Table 5.2.2.6.1-1J-1 and Table 5.2.2.6.1-1J-2 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A'.

Table 5.2.2.6.1-1J-3 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.2.6.1-1J-4 shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

For Table 5.2.2.6.1-1H-1, Table 5.2.2.6.1-1I-1 and Table 5.2.2.6.1-1J-4, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.1-1K-1 and Table Table 5.2.2.6.1-1K-2 show the fields and the corresponding bit widths for channel quality information feedback for higher layer configured report for PDSCH transmission associated with transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.2.6.1-1K-3 and Table 5.2.2.6.1-1K-4 show the fields and the corresponding bit widths for channel quality information feedback for higher layer configured report for PDSCH transmission associated with transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration .

For Table 5.2.2.6.1-1H, Table 5.2.2.6.1-1I, Table 5.2.2.6.1-1J, Table 5.2.2.6.1-1J-1, Table 5.2.2.6.1-1J-2 and Table 5.2.2.6.1-1J-3, is defined in clause 7.2 of [3]. For Table 5.2.2.6.1-1J-1, Table 5.2.2.6.1-1J-2, Table 5.2.2.6.1-1K-3, Table 5.2.2.6.1-1K-4 and Table 5.2.2.6.1-1K-5, the codebook configuration  is defined in [3], and CodebookConfig is configured by higher layers [6]. The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2, 3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4.

Table 5.2.2.6.1-1H: Fields for channel quality information feedback for wideband CQI reports (transmission mode 4, transmission mode 5, transmission mode 6, transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1H-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1I: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.1-1I-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-1J: Fields for channel quality information feedback for wideband CQI reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1J-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.1-1J-2: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.1-1J-3: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.1-1J-4: Fields for channel quality information feedback for wideband CQI reports with 4 antenna ports (transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1K-1: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1K-2: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.1-1K-3: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.1-1K-4: Fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.1-1K-5 shows the fields and the corresponding bit widths for i1 for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports, where i1 is associated with Class A.

Table 5.2.2.6.1-1K-5: Fields for i1 feedback (transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with codebook configuration  , where i1 is associated with Class A)

Table 5.2.2.6.1-2 shows the fields and the corresponding bit width for the rank indication feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode set to 'multi-shot' with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList, and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports, and rank indication is associated with eMIMO-Type2, transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 with 2/4/8 antenna ports, transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports, and rank indication is associated with eMIMO-Type2.

Table 5.2.2.6.1-2A shows the fields and the corresponding bit width for the CRI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting for Class B CSI reporting with K>1 CSI-RS resources except with feCoMP-CSI-Enabled=true and one port per CSI-RS resource except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with the eMIMO-Type.

Table 5.2.2.6.1-2B shows the fields and the corresponding bit width for the joint CRI and RI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources except with feCoMP-CSI-Enabled=true and more than one port for at least one CSI-RS resource except with higher layer parameter csi-RS-NZP-mode configured.

Table 5.2.2.6.1-2C shows the fields and the corresponding bit width for the CRI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and the higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and one port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true. N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.1-2D shows the fields and the corresponding bit width for the joint CRI and RI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with PMI/RI reporting and the higher layer parameter csi-RS-NZP-modeis set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true. N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.1-2E shows the fields and the corresponding bit width for the rank indication feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' and eMIMO-Type2 is set to 'CLASS B', where rank indication is associated with the eMIMO-Type.

Table 5.2.2.6.1-2F shows the fields and the corresponding bit width for the joint CRI and RI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true. In the case of CRI=2, Rank indication in Table 5.2.2.6.1-2F corresponds to {RI0, RI1}, where RI0 is the rank indication for codeword 0 and RI1 is the rank indication for codeword 1.

Table 5.2.2.6.1-2G shows the fields and the corresponding bit width for the CRI feedback for wideband CQI reports for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and one port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true.

Table 5.2.2.6.1-2: Fields for rank indication feedback for wideband CQI reports (transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI or without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2, and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A')

Table 5.2.2.6.1-2A: Fields for CRI feedback for wideband CQI reports (transmission mode 9/10 configured with PMI/RI reporting for Class B CSI reporting with K>1 CSI-RS resources except with feCoMP-CSI-Enabled=true and 1 port per CSI-RS resource except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with the eMIMO-Type)

Table 5.2.2.6.1-2B: Fields for joint CRI and RI feedback for wideband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources except with feCoMP-CSI-Enabled=true and >1 ports for at least one CSI-RS resource except with higher layer parameter csi-RS-NZP-mode configured)

Table 5.2.2.6.1-2C: Fields for CRI feedback for wideband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and 1 port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-2D: Fields for joint CRI and RI feedback for wideband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and >1 ports for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-2E: Fields for rank indication feedback for wideband CQI reports (transmission mode 9/10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type set to 'CLASS A' and eMIMO-Type2 is set to 'CLASS B', where rank indication is associated with the eMIMO-Type)

Table 5.2.2.6.1-2F: Fields for joint CRI and RI feedback for wideband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and >1 ports for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.1-2G: Fields for CRI feedback for wideband CQI reports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources>1 and 1 port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

The channel quality bits in Table 5.2.2.6.1-1, Table 5.2.2.6.1-1-1, Table 5.2.2.6.1-1A, Table 5.2.2.6.1-1A-1, Table 5.2.2.6.1-1B, Table 5.2.2.6.1-1B-1, Table 5.2.2.6.1-1B-2, Table 5.2.2.6.1-1B-3, Table 5.2.2.6.1-1C, Table 5.2.2.6.1-1D, Table 5.2.2.6.1-1D-1, Table 5.2.2.6.1-1D-2, Table 5.2.2.6.1-1E, Table 5.2.2.6.1-1F, Table 5.2.2.6.1-1F-1, Table 5.2.2.6.1-1G, Table 5.2.2.6.1-1G-1, Table 5.2.2.6.1-1H, Table 5.2.2.6.1-1H-1, Table 5.2.2.6.1-1I, Table 5.2.2.6.1-1I-1, Table 5.2.2.6.1-1J, Table 5.2.2.6.1-1J-1, Table 5.2.2.6.1-1J-2, Table 5.2.2.6.1-1J-3, Table 5.2.2.6.1-1J-4, Table 5.2.2.6.1-1K-1, Table 5.2.2.6.1-1K-2, Table 5.2.2.6.1-1K-3, Table 5.2.2.6.1-1K-4, Table 5.2.2.6.1-2B, and Table 5.2.2.6.1-2D, form the bit sequence  with  corresponding to the first bit of the first field in the table,  corresponding to the second bit of the first field in the table, and  corresponding to the last bit in the last field in the table. The field of PMI shall be in the increasing order of the subband index [3]. The first bit of each field corresponds to MSB and the last bit LSB. The RI bits sequence in Table 5.2.2.6.1-2, Table 5.2.2.6.1-2B, Table 5.2.2.6.1-2D, Table 5.2.2.6.1-2E, Table 5.2.2.6.1-2F and the CRI sequence in Table 5.2.2.6.1-2A, Table 5.2.2.6.1-2C, Table 5.2.2.6.1-2G are encoded according to clause 5.2.2.6.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 except with feCoMP-CSI-Enabled=true, the number of antenna port in Table 5.2.2.6.1-2B (or Table 5.2.2.6.1-2F with feCoMP-CSI-Enabled=true) refers to the maximum number of antenna ports of K CSI-RS resources configured for the CSI-process for the UE.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 except with feCoMP-CSI-Enabled=true and with activatedResources>1, the number of antenna port in Table 5.2.2.6.1-2D refers to the maximum number of antenna ports of N CSI-RS resources activated for the CSI-process for the UE. N is the value of higher layer parameter activatedResources.

For a UE configured with the higher layer parameter shortTTI, the entries associated with codeword 1 in Table 5.2.2.6.1-1, Table 5.2.2.6.1-1A, Table 5.2.2.6.1-1B, Table 5.2.2.6.1-1B-1, Table 5.2.2.6.1-1B-2, Table 5.2.2.6.1-1C, Table 5.2.2.6.1-1D, Table 5.2.2.6.1-1D-1, Table 5.2.2.6.1-1D-2, Table 5.2.2.6.1-1E, Table 5.2.2.6.1-1G, Table 5.2.2.6.1-1H, Table 5.2.2.6.1-1I, Table 5.2.2.6.1-1J, Table 5.2.2.6.1-1J-1, Table 5.2.2.6.1-1J-2, Table 5.2.2.6.1-1J-3, Table 5.2.2.6.1-1K-1, Table 5.2.2.6.1-1K-2, Table 5.2.2.6.1-1K-3 and Table 5.2.2.6.1-1K-4 are not applicable.

## 5.2.2.6.2Channel quality information formats for higher layer configured subband CQI reports

Table 5.2.2.6.2-1 shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true.  in Table 5.2.2.6.2-1 is defined in clause 7.2 of [3].

Table 5.2.2.6.2-1A shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' without PMI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.2.6.2-1B shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true. The number of configured CSI-RS resources in a CSI process K is defined in [3].  in Table 5.2.2.6.2-1B is defined in clause 7.2 of [3].

Table 5.2.2.6.2-1B-1 shows the fields and the corresponding bit width for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true. The number of configured CSI-RS resources in a CSI process K is defined in [3].  in Table 5.2.2.6.2-1B-1 is defined in clause 7.2 of [3].

For Table 5.2.2.6.2-1B and Table 5.2.2.6.2-1B-1, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.2-1: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-1A Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' without PMI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-1B: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-1B-1: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-2, Table 5.2.2.6.2-2A and Table 5.2.2.6.2-2B show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 4, transmission mode 5, transmission mode 6, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.2.6.2-2-1 and Table 5.2.2.6.2-2A-1 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

Table 5.2.2.6.2-2B-1 and Table 5.2.2.6.2-2B-2 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE.

Table5.2.2.6.2-2B-3 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE.

Table5.2.2.6.2-2B-4 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' without alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table5.2.2.6.2-2B-5 and Table5.2.2.6.2-2B-6 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports.

Table 5.2.2.6.2-2B-7 and Table 5.2.2.6.2-2B-8 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE.

Table 5.2.2.6.2-2B-9 and Table 5.2.2.6.2-2B-10 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16 /20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled =TRUE.

Table 5.2.2.6.2-2B-11 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

For Table 5.2.2.6.2-2-1, Table 5.2.2.6.2-2A-1 and Table 5.2.2.6.2-2B-11, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

For Table 5.2.2.6.2-2, Table 5.2.2.6.2-2-1, Table 5.2.2.6.2-2A, Table 5.2.2.6.2-2A-1, Table 5.2.2.6.2-2B, Table 5.2.2.6.2-2B-1, Table 5.2.2.6.2-2B-2, Table 5.2.2.6.2-2B-3, Table 5.2.2.6.2-2B-4, Table 5.2.2.6.2-2B-5, Table 5.2.2.6.2-2B-6, Table 5.2.2.6.2-2B-7, Table 5.2.2.6.2-2B-8, Table 5.2.2.6.2-2B-9, Table 5.2.2.6.2-2B-10 and Table 5.2.2.6.2-2B-11, is defined in clause 7.2 of [3]. For Table 5.2.2.6.2-2B-1, Table 5.2.2.6.2-2B-2, Table 5.2.2.6.2-2B-5, Table 5.2.2.6.2-2B-6, Table5.2.2.6.2-2B-8, Table 5.2.2.6.2-2B-9 and Table 5.2.2.6.2-2B-10, the codebook configuration  is defined in [3], and CodebookConfig is configured by higher layers [6]. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4. The parameters  are defined as  and  for  and ,  and  for  and ,  and  for .

Table 5.2.2.6.2-2: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 4, transmission mode 5, transmission mode 6, transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2-1: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2A: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.2-2A-1: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-2B: Fields for channel quality information feedback for higher layer configured subband CQI reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2B-1: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2B-2: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2B-3: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.2-2B-4: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2B-5: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.2-2B-6: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.2-2B-7: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2B-8: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2B-9: Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with 8/12/16/20/24/28/32 antenna ports and higher layer parameter advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.2-2B-10 Fields for channel quality information feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.2-2B-11: Fields for channel quality information feedback for higher layer configured subband CQI reports with 4 antenna ports (transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2C, Table 5.2.2.6.2-2D and Table 5.2.2.6.2-2E show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 4, transmission mode 6, transmission mode 8 configured with subband PMI/RI reporting, transmission mode 9 configured with subband PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with subband PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with subband PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with subband PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.2.6.2-2C-1 and Table 5.2.2.6.2-2D-1 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with subband PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

Table 5.2.2.6.2-2E-1 and Table 5.2.2.6.2-2E-2 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with subband PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE.

Table5.2.2.6.2-2E-3 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with subband PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with subband PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.2.6.2-2E-4 and Table 5.2.2.6.2-2E-5 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE.

Table 5.2.2.6.2-2E-6 and Table 5.2.2.6.2-2E-7 show the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 9/10 configured with subband PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE.

Table 5.2.2.6.2-2E-9 shows the fields and the corresponding bit widths for the channel quality information feedback for higher layer configured report for PDSCH transmissions associated with transmission mode 10 configured with subband PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

For Table 5.2.2.6.2-2C-1, Table 5.2.2.6.2-2D-1 and Table 5.2.2.6.2-2E-9, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

For Table 5.2.2.6.2-2C, Table 5.2.2.6.2-2C-1, Table 5.2.2.6.2-2D, Table 5.2.2.6.2-2D-1, Table 5.2.2.6.2-2E, Table 5.2.2.6.2-2E-1, Table 5.2.2.6.2-2E-2, Table 5.2.2.6.2-2E-3, Table 5.2.2.6.2-2E-4, Table 5.2.2.6.2-2E-5, Table 5.2.2.6.2-2E-6, Table 5.2.2.6.2-2E-7 and Table 5.2.2.6.2-2E-9,  is defined in clause 7.2 of [3]. For Table 5.2.2.6.2-2E-1, Table 5.2.2.6.2-2E-2, Table 5.2.2.6.2-2E-5, Table 5.2.2.6.2-2E-6, Table 5.2.2.6.2-2E-7 and Table 5.2.2.6.2-2E-8, the codebook configuration  is defined in [3], and CodebookConfig is configured by higher layers [6]. The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2, 3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4. The parameters  are defined as  and  for  and ,  and  for  and ,  and  for .

Table 5.2.2.6.2-2C: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 4 and transmission mode 6 configured with subband PMI reporting, transmission mode 8 configured with subband PMI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9 and transmission 10 configured with subband PMI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with subband PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with subband PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2C-1: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 10 configured with subband PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2D: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports with 8 antenna ports (transmission mode 9 configured with subband PMI reporting except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with subband PMI reporting except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with subband PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with subband PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.2-2D-1: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports with 8 antenna ports (transmission mode 10 configured with subband PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-2E: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with subband PMI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with subband PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 with except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with subband PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-2E-1: Fields for channel quality information feedback for higher layer configured subband CQI reports and subband PMI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2E-2: Fields for channel quality information feedback for higher layer configured subband CQI reports and subband PMI reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2E-3: Fields for channel quality information feedback for higher layer configured subband CQI reports and subband PMI reports (transmission mode 9/10 configured and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 2/4/8 antenna ports and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.2-2E-4: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 9/10 configured with subband PMI reporting with 4 antenna ports, and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2E-5: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 9/10 configured with subband PMI reporting with 8 antenna ports, and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.2-2E-6: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 9/10 configured with higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled= TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.2-2E-7: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports (transmission mode 9/10 configured with higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled= TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.2-2E-8 shows the fields and the corresponding bit widths for i1 for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where i1is associated with Class A.

Table 5.2.2.6.2-2E-8: Fields for i1 feedback (transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with codebook configuration  , where i1 is associated with Class A)

Table 5.2.2.6.2-2E-9: Fields for channel quality information feedback for higher layer configured subband CQI and subband PMI reports with 4 antenna ports (transmission mode 10 configured with subband PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.2-3 shows the fields and the corresponding bit width for the rank indication feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2, transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 with 2/4/8 antenna ports, transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2.

Table 5.2.2.6.2-3A shows the fields and the corresponding bit width for the CSI-RS resource indication feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource except with feCoMP-CSI-Enabled=true and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with the eMIMO-Type.

Table 5.2.2.6.2-3B shows the fields and the corresponding bit width for the joint CRI and RI feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and 2/4/8 antenna ports except with higher layer parameter csi-RS-NZP-mode configured.

Table 5.2.2.6.2-3C shows the fields and the corresponding bit width for the CSI-RS resource indication feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources, and 1 antenna port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true. N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.2-3D shows the fields and the corresponding bit width for the joint CRI and RI feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true. N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.2-3E shows the fields and the corresponding bit width for the rank indication feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where rank indication is associated with the eMIMO-Type.

Table 5.2.2.6.2-3F shows the fields and the corresponding bit width for the joint CRI and RI feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true. In the case of CRI=2, Rank indication in Table 5.2.2.6.2-3F corresponds to {RI0, RI1}, where RI0 is the rank indication for codeword 0 and RI1 is the rank indication for codeword 1.

Table 5.2.2.6.2-3G shows the fields and the corresponding bit width for the CRI feedback for higher layer configured subband CQI reports for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true.

Table 5.2.2.6.2-3: Fields for rank indication feedback for higher layer configured subband CQI reports(transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI or without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources =1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2, and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A')

Table 5.2.2.6.2-3A: Fields for CRI feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource except with feCoMP-CSI-Enabled=true and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with the eMIMO-Type)

Table 5.2.2.6.2-3B: Fields for joint CRI and RI feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and 2/4/8 antenna ports except with higher layer parameter csi-RS-NZP-mode configured)

Table 5.2.2.6.2-3C: Fields for CRI feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-3D: Fields for joint CRI and RI feedback for higher layer configured subband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-3E: Fields for rank indication feedback for higher layer configured subband CQI reports (transmission mode 9/10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type set to 'CLASS A' and eMIMO-Type2 is set to 'CLASS B', where rank indication is associated with the eMIMO-Type)

Table 5.2.2.6.2-3F: Fields for joint CRI and RI feedback for higher layer configured subband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.2-3G: Fields for CRI feedback for higher layer configured subband CQI reports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

The channel quality bits in Table 5.2.2.6.2-1, Table 5.2.2.6.2-1B, Table 5.2.2.6.2-1B-1, Table 5.2.2.6.2-2, Table 5.2.2.6.2-2-1, Table 5.2.2.6.2-2A, Table 5.2.2.6.2-2A-1, Table 5.2.2.6.2-2B, Table 5.2.2.6.2-2C, Table 5.2.2.6.2-2C-1, Table 5.2.2.6.2-2D, Table 5.2.2.6.2-2D-1, Table 5.2.2.6.2-2E, Table 5.2.2.6.2-2B-1, Table 5.2.2.6.2-2B-2, Table 5.2.2.6.2-2B-3, Table 5.2.2.6.2-2B-4, Table 5.2.2.6.2-2B-5, Table 5.2.2.6.2-2B-6, Table 5.2.2.6.2-2B-7, Table 5.2.2.6.2-2B-8, Table 5.2.2.6.2-2B-9, Table 5.2.2.6.2-2B-10, Table 5.2.2.6.2-2B-11, Table 5.2.2.6.2-2E-1, Table 5.2.2.6.2-2E-2, Table 5.2.2.6.2-2E-3, Table 5.2.2.6.2-2E-4, Table 5.2.2.6.2-2E-5, Table 5.2.2.6.2-2E-6, Table 5.2.2.6.2-2E-7, Table 5.2.2.6.2-2E-9, Table 5.2.2.6.2-3B, and Table 5.2.2.6.2-3D form the bit sequence  with  corresponding to the first bit of the first field in each of the tables,  corresponding to the second bit of the first field in each of the tables, and  corresponding to the last bit in the last field in each of the tables. The field of the PMI and subband differential CQI shall be in the increasing order of the subband index [3]. The first bit of each field corresponds to MSB and the last bit LSB. The RI bits sequence in Tables 5.2.2.6.2-3, 5.2.2.6.2-3B, 5.2.2.6.2-3D, 5.2.2.6.2-3E, 5.2.2.6.2-3F and the CRI sequence in Tables 5.2.2.6.2-3A, 5.2.2.6.2-3C and 5.2.2.6.2-3G are encoded according to clause 5.2.2.6.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 except with feCoMP-CSI-Enabled=true, the number of antenna port in Table 5.2.2.6.2-3B (or Table 5.2.2.6.2-3F with feCoMP-CSI-Enabled=true) refers to the maximum number of antenna ports of K CSI-RS resources configured for the CSI-process for the UE.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 except with feCoMP-CSI-Enabled=true and with activatedResources>1, the number of antenna port in Table 5.2.2.6.2-3D refers to the maximum number of antenna ports of N CSI-RS resources activated for the CSI-process for the UE. N is the value of higher layer parameter activatedResources.

For a UE configured with the higher layer parameter shortTTI, the entries associated with codeword 1 in Table 5.2.2.6.2-1A, Table 5.2.2.6.2-2, Table 5.2.2.6.2-2A, Table 5.2.2.6.2-2B, Table 5.2.26.2-2B1, Table 5.2.26.2-2B2, Table 5.2.26.2-2B3, Table 5.2.26.2-2B4, Table 5.2.26.2-2B5, Table 5.2.26.2-2B6, Table 5.2.26.2-2B7, Table 5.2.26.2-2B8, Table 5.2.26.2-2B9, Table 5.2.26.2-2B10, Table 5.2.2.6.2-2C, Table 5.2.2.6.2-2D, Table 5.2.2.6.2-2E, Table 5.2.2.6.2-2E-1, Table 5.2.2.6.2-2E-2, Table 5.2.2.6.2-2E-3, Table 5.2.2.6.2-2E-4, Table 5.2.2.6.2-2E-5, Table 5.2.2.6.2-2E-6, Table 5.2.2.6.2-2E-7 and Table 5.2.2.6.2-2E-8 are not applicable.

## 5.2.2.6.3Channel quality information formats for UE selected subband CQI reports

Table 5.2.2.6.3-1 shows the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true, and transmission mode 6 for BL/CE UEs.  in Table 5.2.2.6.3-1 is defined in clause 7.2 of [3].

Table 5.2.2.6.3-1A shows the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports.

Table 5.2.2.6.3-1B show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true.

Table 5.2.2.6.3-1B-1 show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true.

For Table 5.2.2.6.3-1B and Table 5.2.2.6.3-1B-1, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.3-1: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port except with feCoMP-CSI-Enabled=true, and transmission mode 6 for BL/CE UEs)

Table 5.2.2.6.3-1A Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports)

Table 5.2.2.6.3-1B: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-1B-1: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-2, Table 5.2.2.6.3-2A and Table 5.2.2.6.3-2B show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 4, transmission mode 6, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna port except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, where the number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.2.6.3-2-1 and Table 5.2.2.6.3-2A-1 show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

Table 5.2.2.6.3-2B-1 shows the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3].

For Table 5.2.2.6.3-2-1, Table 5.2.2.6.3-2A-1 and Table 5.2.2.6.3-2B-1, in the case of CRI=2, the rank value corresponds to RI0 for codeword 0 and RI1 for codeword 1.

Table 5.2.2.6.3-2C and Table 5.2.2.6.3-2D show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE.

Table 5.2.2.6.3-2E shows the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.2.6.3-2F and Table 5.2.2.6.3-2G show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE.

Table 5.2.2.6.3-2H and Table 5.2.2.6.3-2I show the fields and the corresponding bit widths for the channel quality information feedback for UE selected subband CQI for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE.

For Table 5.2.2.6.3-2, Table 5.2.2.6.3-2-1, Table 5.2.2.6.3-2A, Table 5.2.2.6.3-2A-1, Table 5.2.2.6.3-2B,  Table 5.2.2.6.3-2B-1, Table 5.2.2.6.3-2C, Table 5.2.2.6.3-2D, Table 5.2.2.6.3-2E, Table 5.2.2.6.3-2F, Table 5.2.2.6.3-2G, Table 5.2.2.6.3-2H and Table 5.2.2.6.3-2I,  is defined in clause 7.2 of [3]. For Table 5.2.2.6.3-2C, Table 5.2.2.6.3-2D, Table 5.2.2.6.3-2G, Table 5.2.2.6.3-2H, Table 5.2.2.6.3-2I and Table 5.2.2.6.3-2J, the codebook configuration  is defined in [3], and CodebookConfig is configured by higher layers [6]. The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2, 3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4. The parameters  are defined as  and  for  and ,  and  for  and ,  and  for .

Table 5.2.2.6.3-2: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 4, transmission mode 6, transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.3-2-1: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and higher layer parameter feCoMP-CSI-Enabled=true, except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.3-2A: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.3-2A-1: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-2B: Fields for channel quality information feedback for UE selected subband CQI reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.3-2B-1: Fields for channel quality information feedback for UE selected subband CQI reports with 4 antenna ports (transmission mode 10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and higher layer parameter feCoMP-CSI-Enabled=true, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.2.6.3-2C: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.3-2D: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4, except with advancedCodebookEnabled=TRUE)

Table 5.2.2.6.3-2E: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.2.6.3-2F: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.3-2G: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.2.6.3-2H: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=True and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=1)

Table 5.2.2.6.3-2I: Fields for channel quality information feedback for UE selected subband CQI reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration  and CodebookConfig=2/3/4)

Table 5.2.2.6.3-2J shows the fields and the corresponding bit widths for i1 for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where i1 is associated with Class A.

Table 5.2.2.6.3-2J: Fields for i1 feedback (transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with codebook configuration  , where i1 is associated with Class A)

Table 5.2.2.6.3-3 shows the fields and the corresponding bit widths for the rank indication feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2, transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 with with 2/4/8 antenna ports, transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2.

Table 5.2.2.6.3-3A shows the fields and the corresponding bit widths for the CSI-RS resource indication feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource except with feCoMP-CSI-Enabled=true and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is assocated with the eMIMO-Type.

Table 5.2.2.6.3-3B shows the fields and the corresponding bit widths for the joint CRI and RI feedback for UE selected subband CQI report for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and 2/4/8 antenna ports except with higher layer parameter csi-RS-NZP-mode configured.

Table 5.2.2.6.3-3C shows the fields and the corresponding bit widths for the CSI-RS resource indication feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1 and with 1 antenna port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true . N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.3-3D shows the fields and the corresponding bit widths for the joint CRI and RI feedback for UE selected subband CQI report for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true . N is the value of higher layer parameter activatedResources.

Table 5.2.2.6.3-3E shows the fields and the corresponding bit width for the rank indication feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where rank indication is associated with the eMIMO-Type.

Table 5.2.2.6.3-3F shows the fields and the corresponding bit width for the joint CRI and RI feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true. In the case of CRI=2, Rank indication in Table 5.2.2.6.1-2F corresponds to {RI0, RI1}, where RI0 is the rank indication for codeword 0 and RI1 is the rank indication for codeword 1.

Table 5.2.2.6.3-3G shows the fields and the corresponding bit width for the CRI feedback for UE selected subband CQI reports for PDSCH transmissions associated with transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true.

Table 5.2.2.6.3-3: Fields for rank indication feedback for UE selected subband CQI reports(transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports and transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1, transmission mode 9/10 configured with PMI/RI or without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' with activatedResources=1 and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-ConfigNZP-ApList and the higher layer parameter csi-RS-NZP-mode is set to 'aperiodic' and more than one port for the activated CSI-RS resource, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and rank indication is associated with eMIMO-Type2, and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A')

Table 5.2.2.6.3-3A: Fields for CSI-RS resource indication feedback for UE selected subband CQI reports (transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource except with feCoMP-CSI-Enabled=true and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is assocated with the eMIMO-Type)

Table 5.2.2.6.3-3B: Fields for joint CRI and RI feedback for UE selected subband CQI report (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true, and except with higher layer parameter csi-RS-NZP-mode configured, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with feCoMP-CSI-Enabled=true and 2/4/8 antenna ports except with higher layer parameter csi-RS-NZP-mode configured)

Table 5.2.2.6.3-3C: Fields for CSI-RS resource indication feedback for UE selected subband CQI reports (transmission mode 9/10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-3D: Fields for joint CRI and RI feedback for UE selected subband CQI report (transmission mode 9/10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true , and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource except with feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-3E: Fields for rank indication feedback for UE selected subband CQI reports (transmission mode 9/10 and higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports, with eMIMO-Type set to 'CLASS A', where rank indication is associated with the eMIMO-Type)

Table 5.2.2.6.3-3F: Fields for joint CRI and RI feedback for UE selected subband CQI reports (transmission mode 10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and higher layer parameter feCoMP-CSI-Enabled=true except with higher layer parameter csi-RS-NZP-mode configured, transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and more than one port for at least one CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, transmission mode 10 configured without PMI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with PMI/RI reporting and higher layer parameter csi-RS-NZP-mode is set to 'multi-shot' and with activatedResources>1 and more than one port for at least one activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

Table 5.2.2.6.3-3G: Fields for CRI feedback for UE selected subband CQI reports (transmission mode 10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 CSI-RS resources and one port for each CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true, and transmission mode 10 configured with higher layer parameter csi-RS-NZP-mode set to 'multi-shot' and with activatedResources>1, and 1 antenna port per activated CSI-RS resource and higher layer parameter feCoMP-CSI-Enabled=true)

The channel quality bits in Table 5.2.2.6.3-1, Table 5.2.2.6.3-1B, Table 5.2.2.6.3-1B-1, Table 5.2.2.6.3-2, Table 5.2.2.6.3-2-1, Table 5.2.2.6.3-2A, Table 5.2.2.6.3-2A-1, Table 5.2.2.6.3-2B, Table 5.2.2.6.3-2B-1, Table 5.2.2.6.3-2C, Table 5.2.2.6.3-2D, Table 5.2.2.6.3-2E, Table 5.2.2.6.3-2F, Table 5.2.2.6.3-2G, Table 5.2.2.6.3-2H, Table 5.2.2.6.3-2I, Table 5.2.2.6.3-3B, and Table 5.2.2.6.3-3D form the bit sequence  with  corresponding to the first bit of the first field in each of the tables,  corresponding to the second bit of the first field in each of the tables, and  corresponding to the last bit in the last field in each of the tables. The field of PMI shall start with the wideband PMI followed by the PMI for the M selected subbands. The first bit of each field corresponds to MSB and the last bit LSB. The RI bits sequence in Table 5.2.2.6.3-3, Table 5.2.2.6.3-3B, Table 5.2.2.6.3-3D, Table 5.2.2.6.3-3E, Table 5.2.2.6.3-3F, and the CRI sequence in Table 5.2.2.6.3-3A, Table 5.2.2.6.3-3C and Table 5.2.2.6.3-3G are encoded according to clause 5.2.2.6.

For transmission mode 9/10 configured with Class B CSI reporting and K>1, the number of antenna port in Table 5.2.2.6.3-3B (or Table 5.2.2.6.3-3F with feCoMP-CSI-Enabled=true) refers to the maximum number of antenna ports of K CSI-RS resources configured for the CSI-process for the UE.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 except with feCoMP-CSI-Enabled=true and with activatedResources>1, the number of antenna port in Table 5.2.2.6.3-3D refers to the maximum number of antenna ports of N CSI-RS resources activated for the CSI-process for the UE. N is the value of higher layer parameter activatedResources.

For a UE configured with the higher layer parameter shortTTI, the entries associated with codeword 1 in Table 5.2.2.6.3-1A, Table 5.2.2.6.3-2, Table 5.2.2.6.3-2A, Table 5.2.2.6.3-2B, Table 5.2.2.6.3-2C, Table 5.2.2.6.3-2D, Table 5.2.2.6.3-2E, Table 5.2.2.6.3-2F, Table 5.2.2.6.3-2G, Table 5.2.2.6.3-2H and Table 5.2.2.6.3-2I are not applicable.

## 5.2.2.6.4Channel coding for CQI/PMI information in PUSCH

The channel quality bits input to the channel coding block are denoted by  where O is the number of bits. The number of channel quality bits depends on the transmission format. When PUCCH-based reporting format is used, the number of CQI/PMI bits is defined in clause 5.2.3.3.1 for wideband reports and in clause 5.2.3.3.2 for UE selected subbands reports. When PUSCH-based reporting format is used, the number of CQI/PMI bits is defined in clause 5.2.2.6.1 for wideband reports, in clause 5.2.2.6.2 for higher layer configured subbands reports and in clause 5.2.2.6.3 for UE selected subbands reports.

The channel quality information is first coded using a (32, O) block code. The code words of the (32, O) block code are a linear combination of the 11 basis sequences denoted Mi,n and defined in Table 5.2.2.6.4-1.

Table 5.2.2.6.4-1: Basis sequences for (32, O) code

The encoded CQI/PMI block is denoted by  where  and

where i = 0, 1, 2, …, B-1.

The output bit sequence  is obtained by circular repetition of the encoded CQI/PMI block as follows

where i = 0, 1, 2, …, NL·QCQI-1, where NL is the number of layers the corresponding UL-SCH transport block is mapped onto.

## 5.2.2.6.5Channel coding for more than 11 bits of HARQ-ACK information

The HARQ-ACK bits input to the channel coding block are denoted by  where  is the number of bits.

The sequences of bits  and  are encoded as follows

and

where i = 0, 1, 2, …, 31 and the basis sequences  are defined in Table 5.2.2.6.4-1.

The output bit sequence  is obtained by the concatenation and circular repetition of the bit sequences  and  as follows:

Set i = 0

while

i = i + 1

end while

Set i = 0

while

i = i + 1

end while

## 5.2.2.6AChannel coding of AUL-UCI

Control data arrives at the coding unit in the form of AUL uplink control information (AUL-UCI), , and is transmitted on AUL PUSCH as defined in [3].

When the UE transmits AUL-UCI bits in the AUL PUSCH, it shall determine the number of modulation coded symbols per layer  for AUL-UCI as

where

- is the number of AUL-UCI bits, and

- is the number of CRC bits given by , and

-and , where  shall be determined according to [3] depending on the number of transmission codewords for the corresponding AUL PUSCH, and where  is the modulation order of transport block "x".

- is the bandwidth assigned in the most recent AUL activation DCI as defined in [3] for PUSCH transmission for the transport block.

-, , and  are defined in 5.2.2.6.

The variable "x" in  represents the transport block index corresponding to the highest IMCS value indicated by the most recent AUL activation DCI. In case the two transport blocks have the same IMCS value in the corresponding AUL activation DCI, "x =1", which corresponds to the first transport block. , , and  are obtained from the most recent AUL activation DCI as defined in [3] for the same transport block.

For UL-SCH data information transmitted on the AUL PUSCH, , where  is the number of layers the corresponding UL-SCH transport block is mapped onto.

Table 5.2.2.6A-1 shows the fields and the corresponding bit widths for the AUL-UCI that is transmitted on the AUL PUSCH configured for 1 transport block and 2 transport blocks, respectively.

Table 5.2.2.6A-1: Fields for AUL-UCI

The CRC attachment, channel coding and rate matching of the AUL-UCI is performed according to clauses 5.1.1, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is , which is obtained by concatenating the fields as given in Table 5.2.2.6A-1. The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

The output sequence for the channel coding of AUL-UCI is denoted by , where  is the number of layers the corresponding UL-SCH transport block is mapped onto.

## 5.2.2.7Data and control multiplexing

The control and data multiplexing is performed such that HARQ-ACK information is present on both slots and is mapped to resources around the demodulation reference signals. In addition, the multiplexing ensures that control and data information are mapped to different modulation symbols.

The inputs to the data and control multiplexing are the coded bits of the control information denoted by and the coded bits of the UL-SCH denoted by . The output of the data and control multiplexing operation is denoted by , where  and  , and where,  are column vectors of length . H is the total number of coded bits allocated for UL-SCH data and CQI/PMI information across the  transmission layers of the transport block.

In case where more than one UL-SCH transport block are transmitted in a subframe of an UL cell, the CQI/PMI information is multiplexed with data only on the UL-SCH transport block with highest IMCS value on the initial grant or for the initial PUSCH. In case the two transport blocks have the same IMCS value in the corresponding initial UL grant or for the initial PUSCH, the CQI/PMI information is multiplexed with data only on the first transport block. For that UL-SCH transport block or in the case of single transport block transmission, and assuming that  is the number of layers onto which the UL-SCH transport block is mapped, the control information and the data shall be multiplexed as follows:

Set i, j, k to 0

while  -- first place the control information

end while

while  -- then place the data

end while

## 5.2.2.7AData and control multiplexing for Partial PUSCH Mode 1

If the control information is channel quality information and the control information is transmitted on the Partial PUSCH Mode 1, the UL-SCH data information and control information are multiplexed such that the CQI/PMI information is present only on the second slot of the subframe.

The inputs to the data and control multiplexing are the coded bits of the control information denoted by and the coded bits of the UL-SCH denoted by . The output for UL-SCH data information is denoted by , where  and  , and where,  are column vectors of length . The output for channel quality information is denoted by , where ,  are column vectors of length  and where .

For a UL-SCH transport block, and assuming that  is the number of layers onto which the UL-SCH transport block is mapped, the output for UL-SCH data information is obtained as follows:

Set i, k to 0

while

end while

In case where more than one UL-SCH transport block are transmitted in a subframe of an UL cell, the CQI/PMI information is multiplexed with data only on the UL-SCH transport block with highest IMCS value for the initial PUSCH. In case the two transport blocks have the same IMCS value for the initial PUSCH, the CQI/PMI information is multiplexed with data only on the first transport block. For that UL-SCH transport block or in the case of single transport block transmission, and assuming that  is the number of layers onto which the UL-SCH transport block is mapped, the output for the CQI/PMI information is obtained as follows:

Set i, k to 0

while

end while

## 5.2.2.7BData and control multiplexing for AUL PUSCH

If the control information is AUL-UCI and the control information is transmitted on the AUL PUSCH, the UL-SCH data information and control information are multiplexed such that the AUL-UCI is mapped from symbol 1 to symbol 12 of the subframe.

The inputs to the data and control multiplexing are the coded bits of the control information denoted by  and the coded bits of the UL-SCH denoted by . The output for UL-SCH data information is denoted by , where  and  , and where,  are column vectors of length . The output for AUL-UCI is denoted by , where ,  are column vectors of length  and where .

For a UL-SCH transport block, and assuming that  is the number of layers onto which the UL-SCH transport block is mapped, the output for UL-SCH data information is obtained as follows:

Set i, k to 0

while

end while

In case where more than one UL-SCH transport block are transmitted in a subframe of an UL cell, the AUL-UCI is multiplexed with data only on the UL-SCH transport block with highest IMCS value indicated by the AUL activation DCI. In case the two transport blocks have the same IMCS value in the corresponding AUL activation DCI, the AUL-UCI is multiplexed with data only on the first transport block. For that UL-SCH transport block or in the case of single transport block transmission, and assuming that  is the number of layers onto which the UL-SCH transport block is mapped, the output for the AUL-UCI is obtained as follows:

Set i, k to 0

while

end while

## 5.2.2.8Channel interleaver

The channel interleaver described in this clause in conjunction with the resource element mapping for PUSCH in [2] implements a time-first mapping of modulation symbols onto the transmit waveform while ensuring that

-if the PUSCH is Partial PUSCH Mode 1, the CQI/PMI and RI information are present only on the second slot of the subframe regardless of the number of actually transmitted slot(s) for the subframe based on the result of the channel access procedure in 4.2.1 defined in [8];

-if the PUSCH is Partial PUSCH Mode 2 or 3, the CQI/PMI and RI information are present only on the scheduled slot of the subframe;

-if the PUSCH is AUL PUSCH, the AUL-UCI is mapped from symbol 1 to symbol 12 of the subframe;

-otherwise, the HARQ-ACK and RI information are present on both slots in the subframe for PUSCH with subframe duration. HARQ-ACK information is mapped to resources around the uplink demodulation reference signals while RI information is mapped to resources around those used by HARQ-ACK.

The input to the channel interleaver are denoted by

-, , and , if the PUSCH is Partial PUSCH Mode 1;

-, and , if the PUSCH is AUL PUSCH;

-otherwise ,  and .

In case where more than one UL-SCH transport block are transmitted in a subframe of an UL cell, the HARQ-ACK and RI information are multiplexed with data on both UL-SCH transport blocks.

The number of modulation symbols per layer in the subframe is given by

- if the PUSCH for the subframe is Partial PUSCH Mode 1and the CQI/PMI is multiplexed with data on this UL-SCH transport block,

- if the PUSCH for the subframe is AUL PUSCH and the AUL-UCI is multiplexed with data on this UL-SCH transport block, and

- otherwise.

In the case sub-PRB allocation is used, H'= H's is the number of modulation symbols in a BL/CE subframe s of the S subframes allocated to a UL-SCH transport block, s = 0, 1, 2, …, S-1 [3]. The output bit sequence from the channel interleaver is derived as follows:

(1)Assign  to be the number of columns of the matrix. The columns of the matrix are numbered 0, 1, 2,…, from left to right.  is determined according to clause 5.2.2.6, or by higher layer parameter symPUSCH-UpPts for PUSCH transmission in UpPTS.

(2)The number of rows of the matrix is  and we define .

The rows of the rectangular matrix are numbered 0, 1, 2,…,  from top to bottom.

(3)If rank information is transmitted in this subframe/slot/subslot, the vector sequence  is written onto the columns depending on PUSCH duration and DMRS pattern for PUSCH with subslot duration and by sets of  rows starting from the last row and moving upwards according to the following pseudo-code.

Set i, j to 0.

Set r to

while i <

if the PUSCH is Partial PUSCH Mode 1

else

end if

if the duration of the PUSCH is subframe

else if the duration of the PUSCH is slot, or if the PUSCH is Partial PUSCH Mode 1, 2 or 3

else if the duration of the PUSCH is subslot

end if

end while

Where ColumnSet is given

-in Table 5.2.2.8-1A if the PUSCH is scheduled by DCI format 0A/0B/4A/4B and

-indexed left to right from 0 to 1 if the PUSCH is Partial PUSCH Mode 1, 2, or 3;

-indexed left to right from 0 to 3 otherwise;

-otherwise,

-in Table 5.2.2.8-1 indexed left to right from 0 to 3 for PUSCH with subframe duration,

-in Table 5.2.2.8-1 indexed left to right from 0 to 1 for PUSCH with slot duration,

-as {1} if DMRS pattern field of corresponding uplink DCI formats is '00' for subslot#0, '10' for subslot#1, '01' for subslot#2, '10' for subslot#4, '00' for subslot#5 in case  is equal to 0, or '01' for subslot#5, and as {0} otherwise, for PUSCH with subslot duration. NSRS

-as {1} for subslot #0 and subslot #5 in case  is equal to 0, and as {0} otherwise, for semi-persistently scheduled PUSCH with subslot duration.NSRS

(3a)If  CQI/PMI information is transmitted in this subframe with Partial PUSCH mode 1, the vector sequence  is written onto the  matrix by sets of  rows from the column with   to the column with  and rows 0 to  and skipping the matrix entries that are already occupied:yC'

where =C' NsymbUL/2-NstartPUSCH

The pseudocode is as follows:

Set i, k to 0.

while k < ,

if  is not assigned to RI symbols in step (3) and  i mod Cmux≥C'

k = k + 1

end if

i = i+1

end while

(3b) If AUL-UCI is transmitted in this subframe, the vector sequence  is written onto the  matrix by sets of  rows from the column with  to the column with  and rows 0 to :

The pseudocode is as follows:

Set i, k to 0.

while k < ,

if  and

k = k + 1

end if

i = i+1

end while

(4) Write the input vector sequence, for k = 0, 1,…, , into the  matrix by sets of  rows starting with the vector  in column 0 and rows 0 to and skipping the matrix entries that are already occupied:

The pseudocode is as follows:

Set i, k to 0.

while k <,

if  is not assigned to RI symbols, or CQI/PMI symbols in step (3a), or AUL-UCI symbols in step (3b)

k = k + 1

end if

i = i+1

end while

(5) If HARQ-ACK information is transmitted in this subframe/slot/subslot, the vector sequence  is written onto the columns depending on PUSCH duration and DMRS pattern for PUSCH with subslot duration, and by sets of  rows starting from the last row and moving upwards according to the following pseudo-code. Note that this operation overwrites some of the channel interleaver entries obtained in step (4).

Set i, j to 0.

Set r to  if  and  for PUSCH with subslot duration,  if  and for PUSCH with subslot duration, and  otherwise

while i <

if the duration of the PUSCH is subframe

else if the duration of the PUSCH is slot

else if the duration of the PUSCH is subslot,  and

else if the duration of the PUSCH is subslot,  and

r=QACK'-1-i

else if the duration of the PUSCH is subslot and  or

end if

end while

Where ColumnSet is given

-in Table 5.2.2.8-2 indexed left to right from 0 to 3 for PUSCH with subframe duration,

-in Table 5.2.2.8-2 indexed left to right from 0 to 1 for PUSCH with slot duration,

-as {1} if DMRS pattern field of corresponding uplink DCI formats is '01' for subslot#0, '11' for subslot#1, '10' for subslot#3, or '11' for subslot#4, and as {0} otherwise, for PUSCH with subslot duration.

-as {1} for subslot #1 and subslot #3 if the higher layer parameter semiPersistSchedIntervalUL is set to 1 subslot and MSB of DMRS pattern field of corresponding uplink DCI formats is '1', and as {0} otherwise, for semi-persistently scheduled PUSCH with subslot duration.

(6) The output of the block interleaver is the bit sequence read out column by column from the  matrix. The bits after channel interleaving are denoted by , where  is the number of layers the corresponding UL-SCH transport block is mapped onto.

Table 5.2.2.8-1: Column set for Insertion of rank information for PUSCH not scheduled using DCI Format 0A, 4A, 0B and 4B

Table 5.2.2.8-1A: Column set for Insertion of rank information for PUSCH scheduled using DCI Format 0A, 4A, 0B and 4B

Table 5.2.2.8-2: Column set for Insertion of HARQ-ACK information

The same channel interleaver procedures for RI are applied for CRI, using CRI instead of RI in the equations.

## 5.2.3Uplink control information on PUCCH

Data arrives to the coding unit in the form of indicators for measurement indication, scheduling request and HARQ acknowledgement.

Three forms of channel coding are used as shown in Figure 5.2.3-1,

-one for HARQ-ACK and for combination of HARQ-ACK and periodic CSI transmitted on PUCCH format 3, including the cases with scheduling request,

-another for the channel quality information CQI/PMI transmitted on PUCCH format 2,

-and another for combination of CQI/PMI and HARQ-ACK transmitted on PUCCH format 2/2a/2b.

A fourth form of channel coding is used as shown in Figure 5.2.3-2, for HARQ-ACK and for combination of HARQ-ACK and periodic CSI transmitted on PUCCH format 4 or PUCCH format 5 including the cases with scheduling request, or for periodic CSI transmitted on PUCCH format 4 or PUCCH format 5 including the cases with scheduling request.

Figure 5.2.3-1: Processing for UCI

Figure 5.2.3-2: Processing for UCI

## 5.2.3.1Channel coding for UCI HARQ-ACK on PUCCH

The HARQ-ACK bits are received from higher layers for each subframe of each cell. Each positive acknowledgement (ACK) is encoded as a binary '1' and each negative acknowledgement (NACK) is encoded as a binary '0'. For UEs configured with no more than five DL cells, or for UEs configured by higher layers with codebooksizeDetermination-r13 = cc, and for the case where PUCCH format 3, PUCCH format 4 or PUCCH format 5 [2] is configured by higher layers and is used for transmission of the HARQ-ACK feedback information, the HARQ-ACK feedback consists of the concatenation of HARQ-ACK bits for each of the serving cells. For UEs configured by higher layers with codebooksizeDetermination-r13 = dai, the HARQ-ACK feedback consists of the HARQ-ACK bits for the serving cells depending on the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]. For cells configured with transmission modes 1, 2, 5, 6 or 7 [3], i.e., single codeword transmission modes, 1 bit of HARQ-ACK information, , is used for that cell. For cells configured with other transmission modes, 2 bits of HARQ-ACK information are used for those cells, i.e.,  with  corresponding to HARQ-ACK bit for codeword 0 and  corresponding to that for codeword 1.

Define  as the number of HARQ-ACK feedback bits and  as the number of HARQ-ACK feedback bits including the possible concurrent transmission of scheduling request and/or periodic CSI when PUCCH format 3 is used for transmission of HARQ-ACK feedback (clause 10.1 in [3]), and  as the number of HARQ-ACK feedback bits including the possible concurrent transmission of scheduling request and/or periodic CSI when PUCCH format 4 is used for transmission of HARQ-ACK feedback (clause 10.1 in [3]), and  as the number of HARQ-ACK feedback bits including the possible concurrent transmission of scheduling request and/or periodic CSI when PUCCH format 5 is used for transmission of HARQ-ACK feedback (clause 10.1 in [3]).

For UEs configured by higher layers with codebooksizeDetermination-r13 = dai, the bit sequence  is determined according to the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]. Otherwise, the bit sequence  is determined as below.

For FDD when the UE is not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, the sequence of bits  is the result of the concatenation of HARQ-ACK bits for different cells according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

Set  to the number of cells configured by higher layers for the UE

while c <

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell

j = j + 1

else

if the UE is configured with spatial bundling on PUCCH by higher layers and if the UE is configured with PUCCH format 4 or PUCCH format 5 or PUCCH format 3 with more than 5 serving cells or if HARQ-ACK is to be transmitted on subslot SPUCCH as described in clause 5.2.3.1A

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

j = j + 1

else

HARQ-ACK bit corresponding to the first codeword of this cell

j = j + 1

HARQ-ACK bit corresponding to the second codeword of this cell

j = j + 1

end if

end if

c = c + 1

end while

For the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD when the UE is not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, the sequence of bits  is the result of the concatenation of HARQ-ACK bits for different cells. Define  as the number of cells configured by higher layers for the UE and  as the number of subframes for which the UE needs to feed back HARQ-ACK bits in UL subframe n for the c-th serving cell. For a cell using TDD, the subframes are determined by the DL-reference UL/DL configuration if the UE is configured with higher layer parameter eimta-HARQ-ReferenceConfig, and determined by the UL/DL configuration otherwise. For a cell using TDD,  if subframe n-4 in the cell, or subframe n-3 in the cell if higher layer parameter shortProcessingTime is configured for the cell, is a DL subframe or a special subframe with special subframe configurations 1/2/3/4/6/7/8/9/10 and normal downlink CP or a special subframe with special subframe configurations 1/2/3/5/6/7 and extended downlink CP, and  otherwise. For a cell using FDD, .

The sequence of bits  is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

if

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell

j = j + 1

else

if the UE is configured with spatial bundling on PUCCH by higher layers and if the UE is configured with PUCCH format 4 or PUCCH format 5 or PUCCH format 3 with more than 5 serving cells or if HARQ-ACK is to be transmitted on subslot SPUCCH as described in clause 5.2.3.1A

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

j = j + 1

else

HARQ-ACK bit corresponding to the first codeword of this cell

j = j + 1

HARQ-ACK bit corresponding to the second codeword of this cell

j = j + 1

end if

end if

c = c + 1

end while

For the cases with TDD primary cell or EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured, the sequence of bits  is obtained from the HARQ-ACK bits for different cells and different subframes.

Define  as the number of cells configured by higher layers for the UE and as the number of subframes for which the UE needs to feed back HARQ-ACK bits in cell c as defined in Clause 7.3 of [3].

The number of HARQ-ACK bits k and the number of HARQ-ACK bits after spatial bundling kb are computed as follows:

Set k = 0 – counter of HARQ-ACK bits

Set kb = 0 – counter of HARQ-ACK bits after spatial bundling

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

while c <

set l = 0;

while l <

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

k = k + 1

kb = kb + 1

else

k = k + 2

kb = kb + 1

end if

l = l+1

end while

c = c + 1

end while

In case the transmission of HARQ-ACK feedback using PUCCH format 3, PUCCH format 4 or PUCCH format 5 coincides with a sub-frame configured to the UE by higher layers for transmission of scheduling request, the number of scheduling request bit OSR is 1; otherwise OSR=0.

In case the transmission of HARQ-ACK feedback using PUCCH format 3, PUCCH format 4 or PUCCH format 5 coincides with a sub-frame configured to the UE by higher layers for transmission of periodic CSI, OCSI is the number of periodic CSI bit(s) for the CSI report as defined in clause 7.2.2 [3]; otherwise OCSI=0.

For PUCCH format 3, the number of HARQ-ACK feedback bits  is computed as follows:

If the UE is configured with more than 5 serving cells and spatial bundling on PUCCH is configured, then:

-,

else, set  when TDD is used in all the configured serving cell(s) of the UE and  when FDD is used in at least one of the configured serving cells with TDD primary cell  and  when the UE is configured with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2.

If  and , or if  and , or if  and , then

-

else,

-.

For PUCCH format 4 or PUCCH format 5,  if the UE is not configured with spatial bundling on PUCCH by higher layers; otherwise .

If  and the HARQ-ACK is to be transmitted on slot SPUCCH or PUCCH, the multiplexing of HARQ-ACK bits is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

if transmission mode configured in cell  -- 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell as defined in Clause 7.3 of [3]

j = j + 1

else

HARQ-ACK bit of this cell as defined in Clause 7.3 of [3]

j = j + 2

end if

l = l+1

end while

c = c + 1

end while

If  or if HARQ-ACK is to be transmitted on subslot SPUCCH as described in clause 5.2.3.1A, spatial bundling is applied to all subframes in all cells and the multiplexing of HARQ-ACK bits is performed according to the following pseudo-code

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

if transmission mode configured in cell  – 1 bit HARQ-ACK feedback for this cell

HARQ-ACK bit of this cell as defined in Clause 7.3 of [3]

j = j + 1

else

binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell as defined in Clause 7.3 of [3]

j = j + 1

end if

l = l+1

end while

c = c + 1

end while

In case the transmission of HARQ-ACK feedback using PUCCH format 3, PUCCH format 4 or PUCCH format 5 [2] coincides with a sub-frame configured to the UE by higher layers for transmission of scheduling request, the scheduling request bit (1 = positive SR; 0 = negative SR) is appended at the end of the sequence of concatenated HARQ-ACK bits.

In case the transmission of HARQ-ACK feedback using PUCCH format 3, PUCCH format 4 or PUCCH format 5 [2] coincides with a sub-frame configured to the UE by higher layers for transmission of periodic CSI, and periodic CSI is not dropped as defined in clause 7.3.2 and clause 10.1.1 of [3], the periodic CSI bits for the CSI report as defined in clause 7.2.2 [3] are appended at the end of the sequence of concatenated HARQ-ACK bits and scheduling request bit (if any), where in case of CSI report for more than one DL cell, the CSI report for each DL cell is appended in increasing order of cell index. As with the transmission of the scheduling request, the procedure above is used with ,  or  including the number of periodic CSI bits and scheduling request bit (if any).

For , the bit sequence  is obtained by setting .

For , the bit sequence  is obtained by setting  if i is even and  if i is odd.

For , the sequence of bits  is encoded as follows

where i = 0, 1, 2, …, 31 and the basis sequences  are defined in Table 5.2.2.6.4-1.

The output bit sequence  is obtained by circular repetition of the sequence

where i = 0, 1, 2, …, B-1 and where .

For , the sequences of bits  and  are encoded as follows

and

where i = 0, 1, 2, …, 23 and the basis sequences  are defined in Table 5.2.2.6.4-1.

The output bit sequence  where is obtained by the alternate concatenation of the bit sequences and  as follows

Set i, j = 0

while

,

,

i = i + 4

j = j + 2

end while

For , the bit sequence  is obtained by setting , and the output bit sequence after the rate matching is denoted by , where ,  is the modulation order of the PUCCH format 4,  is determined according to clause 5.2.4.1, and  represents the bandwidth of the PUCCH format 4 in terms of resource blocks [2]. The CRC attachment, channel coding and rate matching are performed according to clauses 5.1.1 by setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

For , the bit sequence  is obtained by setting , and the output bit sequence after the rate matching is denoted by , where ,  is the modulation order of the PUCCH format 5 and  is determined according to clause 5.2.4.1. The CRC attachment, channel coding and rate matching are performed according to clauses 5.1.1 by setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

When PUCCH format 3, PUCCH format 4 or PUCCH format 5 is not used for transmission of HARQ-ACK feedback, the HARQ-ACK bits are processed for transmission according to clause 10.1 in [3].

## 5.2.3.1AChannel coding for UCI HARQ-ACK on SPUCCH

The HARQ-ACK bits are received from higher layers for each subframe of each cell and for each slot or subslot of each cell if higher layer parameter dl-STTI-Length is configured for the cell. Each positive acknowledgement (ACK) is encoded as a binary '1' and each negative acknowledgement (NACK) is encoded as a binary '0'. For UEs configured with more than one DL cell and no more than five DL cells, or for UEs configured by higher layers with codebooksizeDeterminationSTTI-rel15 = cc, the HARQ-ACK feedback consists of the concatenation of HARQ-ACK bits for each of the serving cells. For UEs configured by higher layers with codebooksizeDeterminationSTTI-rel15 = dai, the HARQ-ACK feedback consists of the HARQ-ACK bits for the serving cells depending on the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]. For a cell configured with higher layer parameter dl-STTI-Length, 1 bit of HARQ-ACK information, , is used for that cell.

Define  as the number of HARQ-ACK feedback bits and as the number of HARQ-ACK feedback bits including the possible concurrent transmission of scheduling request when SPUCCH format 3 is used for transmission of HARQ-ACK feedback (clause 10.1 in [3]), and as the number of HARQ-ACK feedback bits including the possible concurrent transmission of scheduling request when SPUCCH format 4 is used for transmission of HARQ-ACK feedback (clause 10.1 in [3]).

For UEs configured by higher layers with codebooksizeDeterminationSTTI-rel15 = dai, the bit sequence  is determined according to the Downlink Assignment Index (DAI) as in Table 5.3.3.1.2-2 and as defined in [3]. Otherwise, the bit sequence  is determined as below.

For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, define the bit sequence  corresponding to PDSCH with slot/subslot duration as the result of the concatenation of HARQ-ACK bits for one or multiple DL cells configured with higher layer parameter dl-STTI-Length,  as the number of cells configured with dl-STTI-Length for the UE and  as the number of slot(s) or subslot(s) for which the UE needs to feed back HARQ-ACK bits in UL slot or subslot n for the c-th serving cell. For a cell using FDD and configured with dl-STTI-Length=subslot and ul-STTI-Length=subslot, or for a cell using FDD and configured with dl-STTI-Length=slot and ul-STTI-Length=slot, . For a cell using FDD and configured with dl-STTI-Length=subslot and ul-STTI-Length=slot, . For a cell using TDD, if slot n-4 in the cell is in a DL subframe, or slot n-4 is the first slot in a special subframe with special subframe configurations 1/2/3/4/6/7/8/9/10 and normal downlink CP, or slot n-4 is the second slot in a special subframe with special subframe configurations 3/4/8 and normal downlink CP, and  otherwise. o0sACK o1sACK, …, oosACK-1sACK

The bit sequence  is performed according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell configured with dl-STTI-Length

Set j = 0 – HARQ-ACK bit index

while c <

set l = 0;

while l <

HARQ-ACK bit of this cell

j = j + 1

l=l+1

end while

c = c + 1

end while

For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, define the bit sequence  as the result of the concatenation of HARQ-ACK bits corresponding to PDSCH with subframe duration for one or multiple DL cells. The bit sequence is determined as for bit sequence in clause 5.2.3.1 and spatial bundling is performed if the HARQ-ACK is to be transmitted on subslot SPUCCH or if the HARQ-ACK is to be transmitted on slot SPUCCH and spatial bundling is configured. For FDD with at least one cell configured with higher layer parameter dl-STTI-Length or for the aggregation of more than one DL cell including a primary cell using FDD and at least one secondary cell using TDD and at least one DL cell configured with higher layer parameter dl-STTI-Length, the sequence of bits  is the result of the concatenation of HARQ-ACK bits for different cells and is obtained by concatenation of the bit sequence  and  in the cases defined in clause 7.3 of [3]. In all other cases, the sequence of bits  is given by . o0sACK o1sACK, …, oosACK-1sACK

In case the transmission of HARQ-ACK feedback using SPUCCH format 3 or SPUCCH format 4 coincides with a slot/subslot configured to the UE by higher layers for transmission of scheduling request, the number of scheduling request bits OSR is 1; otherwise OSR=0, and the scheduling request bit (1 = positive SR; 0 = negative SR) is appended at the end of the sequence of concatenated HARQ-ACK bits.

For , the bit sequence is obtained by setting and is encoded as follows

where i = 0, 1, 2, …, B-1 and , the basis sequences  are defined in Table 5.2.2.6.4-1.

For SPUCCH format 4, the output sequence is of length E, where ,  is the modulation order of the SPUCCH format 4, is equal to for slot SPUCCH format 4 and equal to for subslot SPUCCH format 4, is determined according to clause 5.2.4.1, and  represents the bandwidth of the SPUCCH format 4 in terms of resource blocks [2].

For , the bit sequence  is obtained by setting and is encoded as follows

where i = 0, 1, 2, …, 31 and the basis sequences  are defined in Table 5.2.2.6.4-1.

The output bit sequence  is obtained by circular repetition of the sequence

,

where i = 0, 1, 2, …, E-1.

For , the bit sequence  is obtained by setting  if i is even and  if i is odd. The sequences of bits  and  are encoded as follows

and

where i = 0, 1, 2, …, 31 and the basis sequences  are defined in Table 5.2.2.6.4-1.

The output bit sequence is obtained by the concatenation and circular repetition of the bit sequences and  as follows

Set i = 0

while

i = i + 1

end while

while

i = i + 1

end while

For , the output bit sequence after the rate matching is denoted by . The CRC attachment, channel coding and rate matching are performed according to clauses 5.1.1 by setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

When SPUCCH format 3 or SPUCCH format 4 is not used for transmission of HARQ-ACK feedback, the HARQ-ACK bits are processed for transmission according to clause 10.1 in [3].

## 5.2.3.2Channel coding for UCI scheduling request

The scheduling request indication is received from higher layers and is processed according to [2].

## 5.2.3.3Channel coding for UCI channel quality information

The channel quality and possible concurrent scheduling request bits input to the channel coding block are denoted by  where A is the number of bits, and where the scheduling request bit (if present) is prepended to the sequence of channel quality bits. The number of channel quality bits depends on the transmission format as indicated in clause 5.2.3.3.1 for wideband reports and in clause 5.2.3.3.2 for UE-selected subbands reports.

For PUCCH format 2, the channel quality information is coded using a (20, A) code. The code words of the (20, A) code are a linear combination of the 13 basis sequences denoted Mi,n and defined in Table 5.2.3.3-1.

Table 5.2.3.3-1: Basis sequences for (20, A) code

After encoding the bits are denoted by  where  and with

where i = 0, 1, 2, …, B-1.

For PUCCH format 4, the output bit sequence after the rate matching is denoted by , where ,  is the modulation order of the PUCCH format 4,  is determined according to clause 5.2.4.1, and  represents the bandwidth of the PUCCH format 4 in terms of resource blocks [2]. The CRC attachment, channel coding and rate matching are performed according to clauses 5.1.1 by setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

For PUCCH format 5, the output bit sequence after the rate matching is denoted by , where ,  is the modulation order of the PUCCH format 5 and  is determined according to clause 5.2.4.1. The CRC attachment, channel coding and rate matching are performed according to clauses 5.1.1 by setting L to 8 bits, 5.1.3.1 and 5.1.4.2, respectively. The input bit sequence to the CRC attachment operation is . The output bit sequence of the CRC attachment operation is the input bit sequence to the channel coding operation. The output bit sequence of the channel coding operation is the input bit sequence to the rate matching operation.

## 5.2.3.3.1Channel quality information formats for wideband reports

Table 5.2.3.3.1-1 shows the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with a transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 9/10 configured without PMI with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI.

Table 5.2.3.3.1-1A shows the fields and the corresponding bit widths for the channel quality information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type.

Table 5.2.3.3.1-1: UCI fields for channel quality information feedback for wideband CQI reports (transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 9/10 configured without PMI with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI)

Table 5.2.3.3.1-1A: UCI fields for channel quality information feedback for wideband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type)

Table 5.2.3.3.1-2 shows the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 4, transmission mode 5, transmission mode 6, and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-2: UCI fields for channel quality information feedback for wideband CQI reports (transmission mode 4, transmission mode 5, transmission mode 6, and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-2A and Table 5.2.3.3.1-2B show the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, and transmission mode 10 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, or alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports , except with alternativeCodebookEnabledCLASSB_K1=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.3.3.1-2A-1and Table 5.2.3.3.1-2A-2 show the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9 /10 configured with PMI/RI reporting with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE.

Table 5.2.3.3.1-2A-3 and Table 5.2.3.3.1-2A-4 show the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled= TRUE.

Table 5.2.3.3.1-2A-5 and Table 5.2.3.3.1-2A-6 show the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled= TRUE.

Table 5.2.3.3.1-2B-1 shows the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-2A: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, and transmission mode 10 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE or advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports, except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.1-2A-1: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured PMI/RI with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and with codebook configuration , and CodebookConfig=1, except with advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-2A-2: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured PMI/RI with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and with codebook configuration , and CodebookConfig=2/3/4, except with advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-2A-3: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-2A-4: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-2A-5: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration and CodebookConfig=1)

Table 5.2.3.3.1-2A-6: UCI fields for transmission of wideband CQI and precoding information (i2) (transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration and CodebookConfig=2/3/4).

Table 5.2.3.3.1-2B: UCI fields for transmission of wideband CQI and precoding information (i1, i2) for transmission mode 9 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports, except with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.3.3.1-2B-1: UCI fields for transmission of wideband CQI and precoding information (i1) for transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-2C and Table 5.2.3.3.1-2D show the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions for 4 antenna ports associated with transmission modes 8, 9 and 10 configured with PMI/RI reporting and alternativeCodeBookEnabledFor4TX-r12=TRUE except with advancedCodebookEnabled=TRUE, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4 antenna ports with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, and alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-2E shows the fields and the corresponding bit widths for the channel quality and precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.3.3.1-2C: UCI fields for transmission of wideband CQI and precoding information (i2) with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE except with advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, and alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-2D: UCI fields for transmission of wideband CQI and precoding information (i1, i2) with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE except with advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, and alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-2E: UCI fields for transmission of wideband CQI and precoding information (transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.1-3 shows the fields and the corresponding bit widths for the rank indication feedback for wideband reports for PDSCH transmissions associated with transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' without PMI reporting with 2/4/8 antenna ports.

Table 5.2.3.3.1-3: UCI fields for rank indication feedback for wideband reports (transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting, transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' except with advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports)

Table 5.2.3.3.1-3A shows the fields and the corresponding bit widths for the joint transmission of rank indication and i1 for wideband reports for PDSCH transmissions associated with transmission mode 9 and transmission mode 10, transmission mode 9/10 configured with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12 =TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-3A: UCI fields for joint report of RI and i1 (transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12 =TRUE and transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12 =TRUE, transmission mode 9/10 configured with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12 =TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-3B shows the fields and the corresponding bit widths for the joint transmission of rank indication and i1 for wideband reports for PDSCH transmissions associated with transmission modes 8, 9 and 10 configured with PMI/RI reporting with 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12 =TRUE, transmission mode 9/10 configured with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12 =TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-3B-1 shows the fields and the corresponding bit widths for the joint transmission of rank indication and i1 for wideband reports for PDSCH transmissions associated with transmission modes 9 and 10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12 =TRUE.

Table 5.2.3.3.1-3B: UCI fields for joint report of RI and i1 with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12 =TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-3B-1: UCI fields for joint report of RI and i1 with 4/8 antenna ports (transmission modes 9 and 10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12 =TRUE)

Table 5.2.3.3.1-3C shows the fields and the corresponding bit widths for the joint report of CRI and rank indication feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0.

Table 5.2.3.3.1-3C: UCI fields for joint report of CRI and rank indication feedback for wideband reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0)

Table 5.2.3.3.1-3D shows the fields and the corresponding bit widths for the joint report of CRI , rank indication and i1 feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 ports, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.1-3D: UCI fields for joint report of CRI, rank indication and i1 feedback for wideband reports (transmission mode 9/10 configured with PMI/RI reporting with 8 ports, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, transmission mode 9/10 configured with PMI/RI reporting with 4 ports Class B CSI reporting with K>1 with alternativeCodeBookEnabledFor4TX-r12=TRUE, except with activatedResources>0)

Table 5.2.3.3.1-3E shows the fields and the corresponding bit widths for the CRI feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource, Class B CSI reporting with K>1 except with activatedResources>0, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with eMIMO-Type.

Table 5.2.3.3.1-3E: Fields for CRI feedback for wideband CQI reports (transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource for Class B CSI reporting with K>1 except with activatedResources>0, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with eMIMO-Type)

Table 5.2.3.3.1-3F shows the fields and the corresponding bit widths for the joint report of CRI and rank indication feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and with activatedResources>1, and transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and with activatedResources>1. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.1-3F: UCI fields for joint report of CRI and rank indication feedback for wideband reports (transmission mode 9/10 configured with PMI/RI or without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and with activatedResources>1)

Table 5.2.3.3.1-3G shows the fields and the corresponding bit widths for the joint report of CRI, rank indication and i1 feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 ports, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and with activatedResources>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.1-3G: UCI fields for joint report of CRI, rank indication and i1 feedback for wideband reports (transmission mode 9/10 configured with PMI/RI reporting with 8 ports, and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and with activatedResources>1, and transmission mode 9/10 configured with PMI/RI reporting with 4 ports Class B CSI reporting with K>1 and with activatedResources>1 with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.1-3H shows the fields and the corresponding bit widths for the CRI feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource, Class B CSI reporting with K>1 and with activatedResources>1. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.1-3H: Fields for CRI feedback for wideband CQI reports (transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource for Class B CSI reporting with K>1 and with activatedResources>1)

Parameters i1,1-1 , i1,2-1 , i1,1-2 , i1,2-2 , i1,p-2 correspond to parameters  ,  ,  , , and  in clause 7.2.4 of [3].

Table 5.2.3.3.1-3I and Table 5.2.3.3.1-3J show the fields and the corresponding bit widths for the joint report of rank indication and i1,p-2 feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE, and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE.

Table 5.2.3.3.1-3I: Fields for joint report of rank indication and i1,p-2 feedback for wideband reports (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled= TRUE)

Table 5.2.3.3.1-3J: Fields for joint report of rank indication and i1,p-2 feedback for wideband reports (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled= TRUE, and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports, and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-4 shows the fields and the corresponding bit widths for the precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A'.

For Table 5.2.3.3.1-4, 5.2.3.3.1-4B, 5.2.3.3.1-4C, 5.2.3.3.1-4D, the parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2,3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig=1,  for CodebookConfig=2/3/4. The parameters  are defined as  and  for  and ,  and  for  and ,  and  for .

Table 5.2.3.3.1-4: UCI fields for channel quality information feedback for precoding information (i1) (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration , except with advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-4A, Table 5.2.3.3.1-4B and Table 5.2.3.3.1-4C show the fields and the corresponding bit widths for the precoding matrix information feedback for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 4/8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE , and transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' and advancedCodebookEnabled=TRUE.

Table 5.2.3.3.1-4A: UCI fields for channel quality information feedback for precoding information (i1) (transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-4B: UCI fields for channel quality information feedback for precoding information (i1) (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter advancedCodebookEnabled=TRUE)

Table 5.2.3.3.1-4C: UCI fields for channel quality information feedback for precoding information (i1) (transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameters advancedCodebookEnabled and eMIMO-Type, and advancedCodebookEnabled=TRUE and eMIMO-Type is set to 'CLASS A' with codebook configuration )

Table 5.2.3.3.1-4D shows the fields and the corresponding bit widths for the joint transmission of i1 and rank indication for wideband reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where i1 and rank indication are associated with Class A.

Table 5.2.3.3.1-4D: UCI fields for channel quality information feedback for report of i1 and rank indication feedback (transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with codebook configuration , where i1and rank indication are associated with Class A)

The channel quality bits in Table 5.2.3.3.1-1 through Table 5.2.3.3.1-4C form the bit sequence  with  corresponding to the first bit of the first field in each of the tables,  corresponding to the second bit of the first field in each of the tables, and  corresponding to the last bit in the last field in each of the tables. The first bit of each field corresponds to MSB and the last bit LSB. The RI feedback for one bit is mapped according to Table 5.2.2.6-5 with  replaced by . The RI feedback for two bits is mapped according to Table 5.2.2.6-6 with ,  replaced by . The RI feedback for three bits is mapped according to Table 5.2.2.6-7 with , ,  replaced by . The same procedures for RI mapping are applied to CRI, replacing RI with CRI. The mapping for the jointly coded RI and i1 is provided in Table 7.2.2-1E of [3].

When multiplexed with UL-SCH, the channel coding and multiplexing for the transmission configurations in Table 5.2.3.3.1-3, Table 5.2.3.3.1-3A, Table 5.2.3.3.1-3B, Table 5.2.3.3.1-3B-1, Table 5.2.3.3.1-3C, Table 5.2.3.3.1-3D, Table 5.2.3.3.1-3F, Tables 5.2.3.3.1-3G, 5.2.3.3.1-3I, 5.2.3.3.1-3J and Table 5.2.3.3.1-4D is performed assuming RI transmission in clause 5.2.2.6. All other transmission configurations in this clause are coded and multiplexed assuming CQI/PMI transmission in clause 5.2.2.6.

For transmission mode 9/10 configured with Class B CSI reporting and K>1, the number of antenna port in Table 5.2.3.3.1-3C, 5.2.3.3.1-3D refers to the maximum number of antenna ports of K CSI-RS resources configured for the CSI-process for the UE.

For transmission mode 9/10 configured with Class B CSI reporting and K>1 and with numberActivatedCSI-RS-Resource>1, the number of antenna port in Table 5.2.3.3.1-3F, 5.2.3.3.1-3G refers to the maximum number of antenna ports of N CSI-RS resources activated for the CSI-process for the UE.

## 5.2.3.3.2Channel quality information formats for UE-selected sub-band reports

Table 5.2.3.3.2-1 shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI/RI reporting or configured with 1 antenna port.

Table 5.2.3.3.2-1A shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI reporting with 2/4/8 antenna ports.

Table 5.2.3.3.2-1: UCI fields for channel quality information feedback for UE-selected sub-band CQI reports (transmission mode 1, transmission mode 2, transmission mode 3, transmission mode 7, transmission mode 8 configured without PMI/RI reporting, transmission mode 9 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 10 configured without PMI/RI reporting or configured with 1 antenna port, transmission mode 9/10 configured without PMI/RI with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI/RI reporting or configured with 1 antenna port)

Table 5.2.3.3.2-1A: UCI fields for channel quality information feedback for UE-selected subband CQI reports (transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI reporting with 2/4/8 antenna ports)

Table 5.2.3.3.2-2 shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 4, transmission mode 5, transmission mode 6, and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-2: UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 4, transmission mode 5, transmission mode 6 and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-2A and Table 5.2.3.3.2-2B show the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=2/3/4, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, or K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE. The number of configured CSI-RS resources in a CSI process K is defined in [3] and alternativeCodebookEnabledCLASSB_K1 is configured by higher layers [6].

Table 5.2.3.3.2-2A-1 shows UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI reporting with 2/4/8 antenna ports.

Table 5.2.3.3.2-2B-1 shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=1.

Table 5.2.3.3.2-2C shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission modes 8, 9 and 10 configured with PMI/RI reporting and alternativeCodeBookEnabledFor4TX-r12 =TRUE, transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE , and with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-2A: UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1 except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-2A-1: UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4/8 antenna ports, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B' configured without PMI reporting with 2/4/8 antenna ports)

Table 5.2.3.3.2-2B: UCI fields for channel quality feedback for UE-selected sub-band reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports, transmission mode 10 configured with PMI/RI reporting with 8 antenna ports, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=2/3/4, and transmission mode 9/10 configured with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.2-2B-1: UCI fields for channel quality feedback for UE-selected sub-band reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=1)

Table 5.2.3.3.2-2C: UCI fields for channel quality feedback for UE-selected sub-band reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, and with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-2D shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-2D: UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-2E shows the fields and the corresponding bit widths for the sub-band channel quality information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4/8 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A'.

Table 5.2.3.3.2-2E: UCI fields for channel quality information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4/8 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A')

Table 5.2.3.3.2-3 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 4, transmission mode 5, transmission mode 6 and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-3: UCI fields for channel quality information feedback for UE-selected sub-band CQI reports (transmission mode 4, transmission mode 5, transmission mode 6 and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-3A and Table 5.2.3.3.2-3B show the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-3A-1 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.3.3.2-3A-2 shows the fields and the corresponding bit widths for the wide-band channel quality feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-3C shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission modes 8, 9 and 10 configured with PMI/RI reporting, 4 antenna ports and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1 with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-3C-1 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 4/8 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-3A: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE or alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-3A-1: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.2-3A-2: UCI fields for wide-band channel quality feedback for UE-selected sub-band reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with 2/4 antenna ports, and K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-3B: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9 configured with PMI/RI reporting with 8 antenna ports and transmission mode 10 configured with PMI/RI reporting with 8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.2-3B-1 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=1. The parameters  are defined as  for CodebookConfig=1.

Table 5.2.3.3.2-3B-2 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=2/3/4. . The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig =2,3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig =2,  for CodebookConfig =3,  for CodebookConfig =4. The parameters  in rank 5 to 8 are defined as  for CodebookConfig =2/3/4.

Table 5.2.3.3.2-3B-3 shows the fields and the corresponding bit widths for the wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with CodebookConfig=1/2/3/4. The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2, 3 and 4.

Table 5.2.3.3.2-3B-1: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration, and CodebookConfig=1)

Table 5.2.3.3.2-3B-2: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration , and CodebookConfig=2/3/4)

Table 5.2.3.3.2-3B-3: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS A' with codebook configuration , and CodebookConfig=1/2/3/4)

Table 5.2.3.3.2-3C: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports with 4 antenna ports (transmission modes 8, 9 and 10 configured with PMI/RI reporting and alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 4 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-3C-1: UCI fields for wide-band channel quality and precoding matrix information feedback for UE-selected sub-band reports with 4/8 antenna ports (transmission mode 9/10 configured with higher layer parameters semiOpenLoop and eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, and K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-4 shows the fields and the corresponding bit width for the rank indication feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 3, transmission mode 4, transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, transmission mode 9/10 configured without PMI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE for 2/4/8 antenna ports, transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured without PMI reporting with alternativeCodebookEnabledCLASSB_K1=TRUE for 2/4/8 antenna ports.

Table 5.2.3.3.2-4: UCI fields for rank indication feedback for UE-selected sub-band reports (transmission mode 3, transmission mode 4, and transmission mode 8 configured with PMI/RI reporting except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and alternativeCodebookEnabledCLASSB_K1=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI or without PMI reporting with 2/4/8 antenna ports with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.2-4A shows the fields and the corresponding bit width for the rank indication and precoder type indication (PTI) feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports and transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports, and transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, or K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE for 4Tx, transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE.

Table 5.2.3.3.2-4B shows the fields and the corresponding bit width for the rank indication and precoder type indication (PTI) feedback with 4 antenna ports for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 8, transmission mode 9 and transmission mode 10 configured with PMI/RI reporting and alternativeCodeBookEnabledFor4TX-r12 =TRUE, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE.

Table 5.2.3.3.2-4A: UCI fields for joint report of RI and PTI (transmission mode 9 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 10 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting with 2/4/8 antenna ports with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, or K>1, except with alternativeCodeBookEnabledFor4TX-r12=TRUE for 4Tx, transmission mode 9/10 configured with PMI/RI reporting with 8/12/16/20/24/28/32 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting with 2/4/8 antenna ports except with alternativeCodebookEnabledCLASSB_K1=TRUE)

Table 5.2.3.3.2-4B: UCI fields for joint report of RI and PTI with 4 antenna ports (transmission mode 8, transmission mode 9 and transmission mode 10 configured with PMI/RI reporting and alternativeCodeBookEnabledFor4TX-r12=TRUE, transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K=1 and except with alternativeCodebookEnabledCLASSB_K1=TRUE, K>1, with alternativeCodeBookEnabledFor4TX-r12=TRUE, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type2 configured with PMI/RI reporting except with alternativeCodebookEnabledCLASSB_K1=TRUE, with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-4C shows the fields and the corresponding bit widths for the joint report of CRI and rank indication feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and transmission mode 9/10 configured without PMI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0.

Table 5.2.3.3.2-4D shows the fields and the corresponding bit widths for the joint report of CRI , rank indication and PTI feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0.

Table 5.2.3.3.2-4C: UCI fields for joint report of CRI and rank indication feedback for UE-selected subband reports (transmission mode 9/10 configured with PMI/RI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, and transmission mode 9/10 configured without PMI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 except with activatedResources>0)

Table 5.2.3.3.2-4D: UCI fields for joint report of CRI, RI and PTI (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1, transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports with Class B CSI reporting with K>1with alternativeCodeBookEnabledFor4TX-r12=TRUE, except with activatedResources>0)

Table 5.2.3.3.2-4E shows the fields and the corresponding bit width for CRI feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource reporting for Class B CSI reporting with K>1 except with activatedResources>0, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with eMIMO-Type.

Table 5.2.3.3.2-4E: Fields for CRI feedback for transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource for Class B CSI reporting with K>1 except with activatedResources>0, and transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with K>1, where CRI is associated with eMIMO-Type)

Table 5.2.3.3.2-4F shows the fields and the corresponding bit widths for the joint report of CRI and rank indication feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and activatedResources>1, and transmission mode 9/10 configured without PMI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and activatedResources>1. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.2-4G shows the fields and the corresponding bit widths for the joint report of CRI , rank indication and PTI feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with PMI/RI reporting and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and activatedResources>1. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.2-4F: UCI fields for joint report of CRI and rank indication feedback for UE-selected subband reports (transmission mode 9/10 configured with PMI/RI or without PMI reporting with 2/4 antenna ports and higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and activatedResources>1)

Table 5.2.3.3.2-4G: UCI fields for joint report of CRI, RI and PTI (transmission mode 9/10 configured with PMI/RI reporting with 8 antenna ports with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B' with K>1 and activatedResources>1, and transmission mode 9/10 configured with PMI/RI reporting with 4 antenna ports with Class B CSI reporting with K>1 and with activatedResources>1 and with alternativeCodeBookEnabledFor4TX-r12=TRUE)

Table 5.2.3.3.2-4H shows the fields and the corresponding bit width for CRI feedback for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource reporting for Class B CSI reporting with K>1 and activatedResources>1. N is the value of higher layer parameter activatedResources.

Table 5.2.3.3.2-4H: Fields for CRI feedback for transmission mode 9/10 configured with 1 antenna port for each CSI-RS resource for Class B CSI reporting with K>1 and activatedResources>1)

Table 5.2.3.3.1-4I shows the fields and the corresponding bit widths for the joint transmission of rank indication and i1 for UE-selected sub-band reports for PDSCH transmissions associated with transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with 8/12/16/20/24/28/32 antenna ports and eMIMO-Type2 is set to 'CLASS B', where rank indication and i1 are associated with Class A. The parameters  in rank 1 and rank 2 are defined as  for CodebookConfig=1 and  for CodebookConfig =2, 3 and 4. The parameters  in rank 3 and 4 are defined as  for CodebookConfig=1,  for CodebookConfig=2,  for CodebookConfig=3,  for CodebookConfig=4.

Table 5.2.3.3.2-4I: UCI fields for channel quality information feedback for report of i1 and rank indication feedback (transmission mode 9/10 configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A' with codebook configuration , where i1 and rank indication are associated with Class A)

The channel quality bits in Table 5.2.3.3.2-1 through Table 5.2.3.3.2-3C-1 form the bit sequence  with  corresponding to the first bit of the first field in each of the tables,  corresponding to the second bit of the first field in each of the tables, and  corresponding to the last bit in the last field in each of the tables. The first bit of each field corresponds to MSB and the last bit LSB. The RI feedback for one bit is mapped according to Table 5.2.2.6-5 with  replaced by . The RI feedback for two bits is mapped according to Table 5.2.2.6-6 with ,  replaced by . The RI feedback for three bits is mapped according to Table 5.2.2.6-7 with , ,  replaced by . The same procedures for RI mapping are applied to CRI, replacing RI with CRI.

When multiplexed with UL-SCH, the channel coding and multiplexing for the transmission configurations in Table 5.2.3.3.2-4, Table 5.2.3.3.2-4A, Table 5.2.3.3.2-4B, Table 5.2.3.3.2-4C, Table 5.2.3.3.2-4D, Table 5.2.3.3.2-4F, Table 5.2.3.3.2-4G and Table 5.2.3.3.2-4I is performed assuming RI transmission in clause 5.2.2.6. All other transmission configurations in this clause are coded and multiplexed assuming CQI/PMI transmission in clause 5.2.2.6.

For transmission mode 9/10 configured with Class B CSI reporting and K>1, the number of antenna port in Table 5.2.3.3.2-4C, 5.2.3.3.2-4D refers to the maximum number of antenna ports of K CSI-RS resources configured for the CSI-process for the UE.

For transmission mode 9/10 configured with Class B CSI reporting and K>1, and with activatedResources>1, the number of antenna ports in Table 5.2.3.3.2-4F and Table 5.2.3.3.2-4G refers to the maximum number of antenna ports of N CSI-RS resources activated for the CSI-process for the UE.

## 5.2.3.4Channel coding for UCI channel quality information and HARQ-ACK

This clause defines the channel coding scheme for the simultaneous transmission of channel quality information and HARQ-ACK information in a subframe.

When normal CP is used for uplink transmission, the channel quality information is coded according to clause 5.2.3.3 with input bit sequence  and output bit sequence , where . The HARQ-ACK bits are denoted by  in case one HARQ-ACK bit or  in case two HARQ-ACK bits are reported per subframe. Each positive acknowledgement (ACK) is encoded as a binary '1' and each negative acknowledgement (NACK) is encoded as a binary '0'.

The output of this channel coding block for normal CP is denoted by , where

In case one HARQ-ACK bit is reported per subframe:

and

In case two HARQ-ACK bits are reported per subframe:

and

When extended CP is used for uplink transmission, the channel quality information and the HARQ-ACK bits are jointly coded. The HARQ-ACK bits are denoted by  in case one HARQ-ACK bit or  in case two HARQ-ACK bits are reported per subframe.

The channel quality information denoted by  is multiplexed with the HARQ-ACK bits to yield the sequence  as follows

and

and  in case one HARQ-ACK bit is reported per subframe, or

,  and  in case two HARQ-ACK bits are reported per subframe.

The sequence  is encoded according to clause 5.2.3.3 to yield the output bit sequence  where .

## 5.2.4Uplink control information on PUSCH without UL-SCH data

When control data are sent via PUSCH without UL-SCH data, the following coding steps can be identified:

-Channel coding of control information

-Control information mapping

-Channel interleaver

## 5.2.4.1Channel coding of control information

Control data arrives at the coding unit in the form of channel quality information (CQI and/or PMI), HARQ-ACK and rank indication. Different coding rates for the control information are achieved by allocating different number of coded symbols for its transmission. When the UE transmits HARQ-ACK bits or rank indicator bits, it shall determine the number of coded symbols  for HARQ-ACK or rank indicator as

where

- is the number of HARQ-ACK bits as defined in clause 5.2.2.6, or rank indicator bits,

- is the number of CQI bits including CRC bits assuming rank equals to 1 for all serving cells for which an aperiodic CSI report is triggered [3],

-is 4 for PUSCH with subframe duration,  is2 for PUSCH with slot duration, or for Partial PUSCH Mode 2 or 3.  is 1 for PUSCH with subslot duration,

- is the scheduled bandwidth for PUSCH transmission in the current subframe/slot/subslot expressed as a number of subcarriers in [2], and

-is the number of SC-FDMA symbols in the current PUSCH transmission subframe/slot/subslot given by , where

- for PUSCH with slot duration, or for Partial PUSCH Mode 2 or 3, or

- for PUSCH with subslot duration,

- is the number of SC-FDMA symbols of the subslot as defined in clause 4.1 of [2],

- is the number of SC-FDMA symbols for DMRS of the subslot as defined in clause 5.5.2.1.2 of [2]

-otherwise .

-is equal to 1

-if UE is configured to send PUSCH and SRS in the same subframe/slot/subslot for the current subframe, or

-if the PUSCH resource allocation for the current subframe/slot/subslot even partially overlaps with the cell-specific SRS subframe and bandwidth configuration defined in clause 5.5.3 of [2], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the current subframe/slot/subslot is within a UE-specific type-1 SRS subframe as defined in Clause 8.2 of [3], and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe, or

-if the current subframe/slot/subslot is within a UE-specific type-0 SRS subframe as defined in clause 8.2 of [3] and the UE is configured with multiple TAGs, and for PUSCH with slot/subslot duration if the current slot/subslot is the last slot/subslot in a subframe.

-Otherwise is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH not starting from the beginning of the first symbol or the seventh symbol of the current subframe, otherwise is equal to 0.

- is equal to 1 when the UE configured for uplink transmission on a LAA SCell is indicated to transmit the PUSCH up to the second to last symbol of the current subframe and  is equal to 0, otherwise is equal to 0.

For HARQ-ACK information  and []. For UEs configured with no more than five DL cells,  shall be determined according to [3] depending on the duration for the corresponding PUSCH (subframe/slot/subslot), and the beta offset indicator in PDCCH/SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot. For UEs configured with more than five DL cells,  shall be determined according to [3] depending on the number of HARQ-ACK feedback bits, the duration for the corresponding PUSCH (subframe/slot/subslot),and the beta offset indicator in PDCCH/SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot.

For rank indication or CRI, ,  and [], where  shall be determined according to [3] depending on the duration for the corresponding PUSCH (subframe/slot/subslot), and the beta offset indicator in PDCCH/SPDCCH with DCI format 7-0A/7-0B when the duration for the corresponding PUSCH is subslot.

For CQI and/or PMI information .

The channel coding and rate matching of the control data is performed according to clause 5.2.2.6. The coded output sequence for channel quality information is denoted by , the coded vector sequence output for HARQ-ACK is denoted by  and the coded vector sequence output for rank indication or CRI, is denoted by .

## 5.2.4.2Control information mapping

The input are the coded bits of the channel quality information denoted by . The output is denoted by , where  and , and where,  are column vectors of length . H is the total number of coded bits allocated for CQI/PMI information.

The control information shall be mapped as follows:

Set j, k to 0

while

end while

## 5.2.4.3Channel interleaver

The vector sequences ,  and  are channel interleaved according clause 5.2.2.8. The bits after channel interleaving are denoted by .

## 5.3Downlink transport channels and control information

If the UE is configured with a Master Cell Group (MCG) and Secondary Cell Group (SCG) [6], the procedures described in this clause are applied to the MCG and SCG, respectively. When the procedures are applied to a SCG, the term primary cell refers to the primary SCell (PSCell) of the SCG.

If the UE is configured with a PUCCH SCell [6], the procedures described in this clause are applied to the group of DL cells associated with the primary cell and the group of DL cells associated with the PUCCH SCell, respectively. When the procedures are applied to the group of DL cells associated with the PUCCH SCell, the term primary cell refers to the PUCCH SCell.

If the UE is configured with a LAA SCell, the procedures described in this clause are applied assuming the LAA SCell is an FDD SCell.

## 5.3.1Broadcast channel

Figure 5.3.1-1 shows the processing structure for the BCH transport channel. Data arrives to the coding unit in the form of a maximum of one transport block every transmission time interval (TTI) of 40ms, or 160ms for a MBMS-dedicated cell. The following coding steps can be identified:

-Add CRC to the transport block

-Channel coding

-Rate matching

The coding steps for BCH transport channel are shown in the figure below.

Figure 5.3.1-1: Transport channel processing for BCH

## 5.3.1.1Transport block CRC attachment

Error detection is provided on BCH transport blocks through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by. A is the size of the transport block and set to 24 bits and L is the number of parity bits. The lowest order information bit a0 is mapped to the most significant bit of the transport block as defined in clause 6.1.1 of [5].

The parity bits are computed and attached to the BCH transport block according to clause 5.1.1 setting L to 16 bits. After the attachment, the CRC bits are scrambled according to the eNodeB transmit antenna configuration with the sequence  as indicated in Table 5.3.1.1-1 to form the sequence of bits where

for k = 0, 1, 2, …, A-1

for k = A, A+1, A+2, ..., A+15.

Table 5.3.1.1-1: CRC mask for PBCH

## 5.3.1.2Channel coding

Information bits are delivered to the channel coding block. They are denoted by , where K is the number of bits, and they are tail biting convolutionally encoded according to clause 5.1.3.1.

After encoding the bits are denoted by, with, and where D is the number of bits on the i-th coded stream, i.e., .

## 5.3.1.3Rate matching

A tail biting convolutionally coded block is delivered to the rate matching block. This block of coded bits is denoted by, with, and where i is the coded stream index and D is the number of bits in each coded stream. This coded block is rate matched according to clause 5.1.4.2.

After rate matching, the bits are denoted by, where E is the number of rate matched bits as defined in clause 6.6.1 of [2].

## 5.3.2Downlink shared channel, Paging channel and Multicast channel

Figure 5.3.2-1 shows the processing structure for each transport block for the DL-SCH, PCH and MCH transport channels. Data arrives to the coding unit in the form of a maximum of two transport blocks every transmission time interval (TTI) per DL cell. The following coding steps can be identified for each transport block of a DL cell:

-Add CRC to the transport block

-Code block segmentation and code block CRC attachment

-Channel coding

-Rate matching

-Code block concatenation

The coding steps for PCH and MCH transport channels, and for one transport block of DL-SCH are shown in the figure below. The same processing applies for each transport block on each DL cell.

Figure 5.3.2-1: Transport block processing for DL-SCH, PCH and MCH

## 5.3.2.1Transport block CRC attachment

Error detection is provided on transport blocks through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by. A is the size of the transport block and L is the number of parity bits. The lowest order information bit a0 is mapped to the most significant bit of the transport block as defined in clause 6.1.1 of [5].

The parity bits are computed and attached to the transport block according to clause 5.1.1 setting L to 24 bits and using the generator polynomial gCRC24A(D).

## 5.3.2.2Code block segmentation and code block CRC attachment

The bits input to the code block segmentation are denoted by  where B is the number of bits in the transport block (including CRC).

Code block segmentation and code block CRC attachment are performed according to clause 5.1.2.

The bits after code block segmentation are denoted by, where r is the code block number and Kr is the number of bits for code block number r.

## 5.3.2.3Channel coding

Code blocks are delivered to the channel coding block. They are denoted by , where r is the code block number, and Kr is the number of bits in code block number r. The total number of code blocks is denoted by C and each code block is individually turbo encoded according to clause 5.1.3.2.

After encoding the bits are denoted by, with, and where  is the number of bits on the i-th coded stream for code block number r, i.e..

## 5.3.2.4Rate matching

Turbo coded blocks are delivered to the rate matching block. They are denoted by, with, and where r is the code block number, i is the coded stream index, and  is the number of bits in each coded stream of code block number r. The total number of code blocks is denoted by C and each coded block is individually rate matched according to clause 5.1.4.1.

After rate matching, the bits are denoted by, where r is the coded block number, and where  is the number of rate matched bits for code block number r.

## 5.3.2.5Code block concatenation

The bits input to the code block concatenation block are denoted by  for  and where  is the number of rate matched bits for the r-th code block.

Code block concatenation is performed according to clause 5.1.5.

The bits after code block concatenation are denoted by, where G is the total number of coded bits for transmission. This sequence of coded bits corresponding to one transport block after code block concatenation is referred to as one codeword in clause 6.3.1 of [2]. In case of multiple transport blocks per TTI, the transport block to codeword mapping is specified according to clause 5.3.3.1.5, 5.3.3.1.5A or 5.3.3.1.5B, depending on the DCI Format.

## 5.3.3Downlink control information

A DCI transports downlink, uplink or sidelink scheduling information, requests for aperiodic CQI reports, LAA common information, notifications of MCCH change [6] or uplink power control commands for one cell and one RNTI. The RNTI is implicitly encoded in the CRC.

Figure 5.3.3-1 shows the processing structure for one DCI. The following coding steps can be identified:

-Information element multiplexing

-CRC attachment

-Channel coding

-Rate matching

The coding steps for DCI are shown in the figure below.

Figure 5.3.3-1: Processing for one DCI

## 5.3.3.1DCI formats

The fields defined in the DCI formats below are mapped to the information bits a0 to aA-1 as follows.

Each field is mapped in the order in which it appears in the description, including the zero-padding bit(s), if any, with the first field mapped to the lowest order information bit a0 and each successive field mapped to higher order information bits. The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to a0.

## 5.3.3.1.1Format 0

DCI format 0 is used for the scheduling of PUSCH in one UL cell.

The following information is transmitted by means of the DCI format 0:

- Carrier indicator – 0 or 3 bits. This field is present according to the definitions in [3].

- Flag for format0/format1A differentiation – 1 bit, where value 0 indicates format 0 and value 1 indicates format 1A

- Frequency hopping flag – 1 bit as defined in clause 8.4 of [3]. This field is used as the MSB of the corresponding resource allocation field for resource allocation type 1.

- Resource block assignment and hopping resource allocation –  bits

- For PUSCH hopping (resource allocation type 0 only):

- NUL_hop MSB bits are used to obtain the value of  as indicated in clause 8.4 of [3]

-  bits provide the resource allocation of the first slot in the UL subframe

- For non-hopping PUSCH with resource allocation type 0:

-  bits provide the resource allocation in the UL subframe as defined in clause 8.1.1 of [3]

- For non-hopping PUSCH with resource allocation type 1:

- The concatenation of the frequency hopping flag field and the resource block assignment and hopping resource allocation field provides the resource allocation field in the UL subframe as defined in clause 8.1.2 of [3]

- Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3]

- New data indicator – 1 bit

- HARQ process number – 4 bits if higher layer parameter ul-STTI-Length is configured for the cell, otherwise 3 bits (this field is present when higher layer parameter shortProcessingTime is configured for the cell and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3])

- Redundancy version – 2 bits (this field is present when higher layer parameter shortProcessingTime is configured for the cell and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3])

- TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

- Cyclic shift for DM RS and OCC index and IFDMA configuration – 3 bits as defined in clause 5.5.2.1.1 of [2] (this field is not present when the format 0 CRC is scrambled by UL-SPS-V-RNTI)

- UL SPS configuration index – 3 bits as defined in clause 9.2.1 of [3]. (this field is present when the format 0 CRC is scrambled by UL-SPS-V-RNTI)

- UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0, or TDD operation with uplink-downlink configuration 6 and special subframe configuration 10 when the higher layer parameter symPUSCH-UpPts or shortProcessingTime is configured for the cell and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3])

- Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (this field is present only for the following cases: 1) TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation; or 2) EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3])

- CSI request – 1, 2, 3, 4 or 5 bits as defined in clause 7.2.1 of [3].

If UEs are not configured with CSI-RS-ConfigNZPAperiodic or if UEs are configured with CSI-RS-ConfigNZPAperiodic and numberActivatedAperiodicCSI-RS-Resources=1 for each CSI process,

the 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured by higher layers with more than one CSI process and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet, and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

the 3-bit field applies to UEs that are configured with more than five DL cells and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

otherwise the 1-bit field applies

If UEs are configured with CSI-RS-ConfigNZPAperiodic and numberActivatedAperiodicCSI-RS-Resources>1 for at least one CSI process,

the 4-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured by higher layers with more than one CSI process and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet, and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

the 5-bit field applies to UEs that are configured with more than five DL cells and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

otherwise the 3-bit field applies.

- SRS request – 0 or 1 bit. This field can only be present in DCI formats scheduling PUSCH which are mapped onto the UE specific search space given by the C-RNTI as defined in [3]. The interpretation of this field is provided in clause 8.2 of [3]

- Resource allocation type – 1 bit. This field is only present if . The interpretation of this field is provided in clause 8.1 of [3]

- Cyclic Shift Field mapping table for DMRS – 1 bit as defined in clause 5.5.2.1.1 of [2]. The 1-bit field applies to UEs that are configured with higher layer parameter UL-DMRS-IFDMA, and when the corresponding DCI format is mapped onto the UE-specific search space given by the C-RNTI as defined in [3]. When the format 0 CRC is scrambled by SPS C-RNTI, this field is set to zero.

If the number of information bits in format 0 mapped onto a given search space is less than the payload size of format 1A for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 1A), zeros shall be appended to format 0 until the payload size equals that of format 1A.

## 5.3.3.1.1AFormat 0A

DCI format 0A is used for the scheduling of PUSCH in a LAA SCell, or activating/releasing AUL transmission as defined in [3], or indicating AUL downlink feedback information (AUL-DFI) to a UE that is activated with AUL transmission.

The following information is transmitted by means of the DCI format 0A:

-Carrier indicator – 0 or 3 bits. This field is present according to the definitions in [3].

If the format 0A DCI is scrambled by C-RNTI

-Flag for format0A/format1A differentiation – 1 bit, where value 0 indicates format 0A and value 1 indicates format 1A;

Else

-Flag for AUL differentiation – 1 bit, where value 0 indicates activating/releasing AUL transmission and value 1 indicates AUL-DFI.

If the format 0A is used for the scheduling of PUSCH in a LAA SCell or activating/releasing AUL transmission for a UE, all the remaining fields are set as follows:

-PUSCH trigger A – 1 bit, where value 0 indicates non-triggered scheduling and value 1 indicates triggered scheduling as defined in clause 8.0 of [3].

-Timing offset – 4 bits as defined in clause 8.0 of [3].

-When the PUSCH trigger A is set to 0,

-The field indicates the absolute timing offset for the PUSCH transmission.

-Otherwise,

-The first two bits of the field indicate the timing offset, relative to the UL offset l as defined in clause 13A of [3], for the PUSCH transmission.

-The last two bits of the field indicate the time window within which the scheduling of PUSCH via triggered scheduling is valid.

-Resource block assignment – 5 or 6 bits provide the resource allocation in the UL subframe as defined in clause 8.1.4 of [3]

-Modulation and coding scheme – 5 bits as defined in clause 8.6 of [3]

-HARQ process number – 4 bits.

-New data indicator – 1 bit

-Redundancy version – 2 bits as defined in clause 8.6.1 of [3]

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-Cyclic shift for DM RS and OCC index – 3 bits as defined in clause 5.5.2.1.1 of [2]

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]. The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured by higher layers with more than one CSI process and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet, and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

the 3-bit field applies to UEs that are configured with more than five DL cells and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

otherwise the 1-bit field applies

-SRS request – 1 bit. The interpretation of this field is provided in clause 8.2 of [3]

-Partial PUSCH Mode – 2 bits as specified in Table 5.3.3.1.1A-3. This field is only present when at least one of laa-PUSCH-Mode1, laa-PUSCH-Mode2, and laa-PUSCH-Mode3 is configured. The UE is not expected to be indicated with a partial PUSCH mode that is not configured by RRC.

-PUSCH starting position – 2 bits

-as specified in Table 5.3.3.1.1A-2 if the 'Partial PUSCH Mode' field indicates Partial PUSCH Mode 2;

-as specified in Table 5.3.3.1.1A-1 otherwise.

-PUSCH ending symbol – 1 bit, where

-if the 'Partial PUSCH Mode' field indicates Partial PUSCH Mode 3, value 0 indicates symbol 6 of the subframe, and value 1 indicates symbol 3 of the subframe.

-otherwise value 0 indicates the last symbol of the subframe and value 1 indicates the second to last symbol of the subframe.

-Channel Access type – 1 bit as defined in clause 4.2 of [8]

-Channel Access Priority Class – 2 bits as defined in clause 4.2 of [8]

If the format 0A is used for indicating AUL-DFI to a UE that is activated with AUL transmission, all the remaining fields are set as follows:

-HARQ-ACK bitmap – 16 bits, where the order of the bitmap to HARQ process index mapping is such that HARQ process indices are mapped in ascending order from MSB to LSB of the bitmap. For each bit of the bitmap, value 1 indicates ACK, and value 0 indicates NACK.

-TPC command – 2 bits as defined in clause 5.1.1.1 of [3].

-All the remaining bits in format 0A are set to zero.

If the number of information bits in format 0A mapped onto a given search space is less than the payload size of format 1A for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 1A), zeros shall be appended to format 0A until the payload size equals that of format 1A.

Table 5.3.3.1.1A-1: PUSCH starting position

Table 5.3.3.1.1A-2: PUSCH starting position in the second slot

Table 5.3.3.1.1A-3: Partial PUSCH Mode

## 5.3.3.1.1BFormat 0B

DCI format 0B is used for the scheduling of PUSCH in each of multiple subframes in a LAA SCell.

The following information is transmitted by means of the DCI format 0B:

-Carrier indicator – 0 or 3 bits. This field is present according to the definitions in [3].

-PUSCH trigger A – 1 bit, where value 0 indicates non-triggered scheduling and value 1 indicates triggered scheduling as defined in clause 8.0 of [3].

-Timing offset – 4 bits as defined in clause 8.0 of [3].

-When the PUSCH trigger A is set to 0,

-The field indicates the absolute timing offset for the PUSCH transmission.

-Otherwise,

-The first two bits of the field indicate the timing offset, relative to the UL offset l as described in clause 13A of [3], for the PUSCH transmission.

-The last two bits of the field indicate the time window within which the scheduling of PUSCH via triggered scheduling is valid.

-Number of scheduled subframes – 1 or 2 bits. The 1-bit field applies when maxNumberOfSchedSubframes-Format0B-r14 is configured by higher layers to two, otherwise the 2-bit field applies.

-Resource block assignment – 5 or 6 bits provide the resource allocation in the UL subframe as defined in clause 8.1.4 of [3].

-Modulation and coding scheme – 5 bits as defined in clause 8.6 of [3].

-HARQ process number - 4 bits. The 4-bit applies to the first scheduled subframe, and the HARQ process numbers for other scheduled subframes are defined in clause 8.0 of [3].

-New data indicator – maxNumberOfSchedSubframes-Format0B-r14 bits. Each scheduled PUSCH corresponds to 1 bit.

-Redundancy version – maxNumberOfSchedSubframes-Format0B-r14 bits. Each scheduled PUSCH corresponds to 1 bit as defined in clause 8.6.1 of [3].

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3].

-Cyclic shift for DM RS and OCC index – 3 bits as defined in clause 5.5.2.1.1 of [2].

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]. The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured by higher layers with more than one CSI process and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet, and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

the 3-bit field applies to UEs that are configured with more than five DL cells and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

otherwise the 1-bit field applies.

-SRS request – 2 bits. The interpretation of this field is provided in clause 8.2 of [3].

-Partial PUSCH Mode 1 – 1 bit only present if laa-PUSCH-Mode1 is configured by higher layer, and applicable to each of the scheduled subframe(s), except for the first scheduled subframe in case the 'Partial PUSCH Mode 2' field is value 1 and the last scheduled subframe in case the 'Partial PUSCH Mode 3' field is value 1, where

-value 0 indicates the starting position of the PUSCH is determined following Partial PUSCH Mode 0 as defined in Table 5.3.3.1.1A-3;

-value 1 indicates the starting position of the PUSCH of the first transmitted subframe is determined following  Partial PUSCH Mode 1 as defined in Table 5.3.3.1.1A-3.

-Partial PUSCH Mode 2 – 1 bit. This field is only present if laa-PUSCH-Mode2 is configured by higher layer, and applicable to only the first scheduled subframe.

-Partial PUSCH Mode 3 – 1 bit. This field is only present if laa-PUSCH-Mode3 is configured by higher layer, and applicable to only the last scheduled subframe.

-PUSCH starting position – 2 bits

-as specified in Table 5.3.3.1.1A-2 applicable to only the first scheduled subframe, if the 'Partial PUSCH Mode 2' field is value 1;

-as specified in Table 5.3.3.1.1A-1 applicable to only the first scheduled subframe otherwise.

-PUSCH ending symbol – 1 bit, where

-if the 'Partial PUSCH Mode 3' field is value 1, value 0 indicates symbol 6 of the last scheduled subframe, and value 1 indicates symbol 3 of the last scheduled subframe;

-otherwise value 0 indicates the last symbol of the last scheduled subframe and value 1 indicates the second to last symbol of the last scheduled subframe.

-Channel Access type – 1 bit as defined in clause 4.2 of [8].

-Channel Access Priority Class – 2 bits as defined in clause 4.2 of [8].

If the number of information bits in format 0B is equal to the payload size for DCI format 1, 2, 2A, 2B, 2C or 2D associated with the configured DL transmission mode in the same serving cell, one zero bit shall be appended to format 0B.

## 5.3.3.1.1CFormat 0C

DCI format 0C is used for the scheduling of PUSCH in one UL cell.

The following information is transmitted by means of the DCI format 0C:

-Flag for format 0C/format1A differentiation – 1 bit, where value 0 indicates format 0C and value 1 indicates format 1A

-Resource allocation type – 1 bit. This field is only present if . The interpretation of this field is provided in clause 8.1 of [3]

-Frequency hopping flag – 1 bit as defined in clause 5.3.4 of [2]. This field is used as the MSB of the corresponding resource allocation field for resource allocation type 1.

-Resource block assignment –  bits

-For PUSCH with resource allocation type 0:

-bits provide the resource allocation in the UL subframe as defined in clause 8.1.1 of [3]

-For non-hopping PUSCH with resource allocation type 1:

-The concatenation of the frequency hopping flag field and the resource block assignment field provides the resource allocation field in the UL subframe as defined in clause 8.1.2 of [3]

-Modulation and coding scheme – 5 bits as defined in clause 8.6 of [3]

-Repetition number – 3 bits as defined in clause 8.0 of [3]

-HARQ process number – 3 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-Cyclic shift for DM RS and OCC index – 3 bits as defined in clause 5.5.2.1.1 of [2]

-UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0, or TDD operation with uplink-downlink configuration 6 and special subframe configuration 10 when the higher layer parameter symPUSCH-UpPts is configured)

-Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (This field is present only for the following cases: 1) TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation; or 2) EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]. The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured by higher layers with more than one CSI process and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet, and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

the 3-bit field applies to UEs that are configured with more than five DL cells and when the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3];

otherwise the 1-bit field applies

-SRS request –1 bit. The interpretation of this field is provided in clause 8.2 of [3]

-Modulation order override – 1 bit as defined in clause 8.6.1 of [3]

-Precoding information: number of bits as specified in Table 5.3.3.1.8-1. This field is present only if the higher layer parameter transmissionModeUL is configured to be transmission mode 2. Bit field as shown in Table 5.3.3.1.8-2 and Table 5.3.3.1.8-3, where only codeword 0 is enabled and the indexes corresponding to 1 layer are used. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2]. The transport block is mapped to codeword 0.

If the number of information bits in format 0C mapped onto a given search space is less than the payload size of format 1A for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 1A), zeros shall be appended to format 0C until the payload size equals that of format 1A.

## 5.3.3.1.2Format 1

DCI format 1 is used for the scheduling of one PDSCH codeword in one cell.

The following information is transmitted by means of the DCI format 1:

- Carrier indicator – 0 or 3 bits. This field is present according to the definitions in [3].

- Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

- Resource block assignment:

- For resource allocation type 0 as defined in clause 7.1.6.1 of [3]:

- bits provide the resource allocation

- For resource allocation type 1 as defined in clause 7.1.6.2 of [3]:

-  bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

- 1 bit indicates a shift of the resource allocation span

-  bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause 7.1.6.1 of [3]

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- HARQ process number – 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- New data indicator – 1 bit

- Redundancy version – 2 bits

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- MUST interference presence and power ratio – 0 or 2 bits as defined in clause 6.3.3 of [2]. This field is present only when the UE is configured for MUST-near operation and the number of antenna ports for CRS transmission in the serving cell is 2.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If the UE is not configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI and the number of information bits in format 1 is equal to that for format 0/1A, one bit of value zero shall be appended to format 1.

If the UE is configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI and the number of information bits in format 1 is equal to that for format 0/1A for scheduling the same serving cell and mapped onto the UE specific search space given by the C-RNTI as defined in [3], one bit of value zero shall be appended to format 1.

If the number of information bits in format 1 carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one or more zero bit(s) shall be appended to format 1 until the payload size of format 1 does not belong to one of the sizes in Table 5.3.3.1.2-1 and is not equal to that of format 0/1A mapped onto the same search space.

Table 5.3.3.1.2-1: Ambiguous Sizes of Information Bits

Table 5.3.3.1.2-2: Number of bits for Downlink Assignment Index

## 5.3.3.1.3Format 1A

DCI format 1A is used for the compact scheduling of one PDSCH codeword in one cell and random access procedure initiated by a PDCCH order. The DCI corresponding to a PDCCH order can be carried by PDCCH or EPDCCH.

The following information is transmitted by means of the DCI format 1A:

-Carrier indicator – 0 or 3 bits. This field is present according to the definitions in [3].

-Flag for format0/format1A differentiation or flag for format0A/format1A differentiation – 1 bit, where value 0 indicates format 0 or format 0A and value 1 indicates format 1A

Format 1A is used for random access procedure initiated by a PDCCH order only if format 1A CRC is scrambled with C-RNTI and all the remaining fields are set as follows:

- Localized/Distributed VRB assignment flag – 1 bit is set to '0'

- Resource block assignment – bits, where all bits shall be set to 1

- Preamble Index – 6 bits

- PRACH Mask Index – 4 bits, [5]

- All the remaining bits in format 1A for compact scheduling assignment of one PDSCH codeword are set to zero

Otherwise,

-Localized/Distributed VRB assignment flag – 1 bit as defined in 7.1.6.3 of [3]

-Resource block assignment – bits as defined in clause 7.1.6.3 of [3]:

- For localized VRB:

bits provide the resource allocation

- For distributed VRB:

- If  or if the format 1A CRC is scrambled by RA-RNTI, P-RNTI, SI-RNTI, SC-RNTI or G-RNTI:

- bits provide the resource allocation

- Else

- 1 bit, the MSB indicates the gap value, where value 0 indicates  and value 1 indicates

-  bits provide the resource allocation,

where  is defined in [2].

-Modulation and coding scheme – 5bits as defined in clause 7.1.7 of [3]. The MSB is set to 0 when the UE is configured with blindSubframePDSCH-Repetitions set to TRUE and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3] and the repetition number is greater than 1 and the higher layer parameter mcs-restrictionSubframePDSCH-Repetitions is configured to 1.

-HARQ process number – 4 bits if higher layer parameter dl-STTI-Length is configured for the cell and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3], otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured and the corresponding DCI is not mapped onto the UE specific search space given by the C-RNTI as defined in [3]), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3])

-New data indicator – 1 bit

-If the format 1A CRC is scrambled by RA-RNTI, P-RNTI, SI-RNTI, SC-RNTI or G-RNTI:

-If  and Localized/Distributed VRB assignment flag is set to 1

-the new data indicator bit indicates the gap value, where value 0 indicates  and value 1 indicates .

-Else the new data indicator bit is reserved.

-Else

-The new data indicator bit as defined in [5]

-Redundancy version – 2 bits

-TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

-If the format 1A CRC is scrambled by RA-RNTI, P-RNTI, or SI-RNTI:

-The most significant bit of the TPC command is reserved.

-The least significant bit of the TPC command indicates column of the TBS table defined of [3].

-If least significant bit is 0 then = 2 else= 3.

-Else if the format 1A CRC is scrambled by G-RNTI or SC-RNTI:

-The two bits of the TPC command are reserved

-Else

-The two bits including the most significant bit indicates the TPC command

-Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

-SRS request – 0 or 1 bit. This field can only be present in DCI formats scheduling PDSCH which are mapped onto the UE specific search space given by the C-RNTI as defined in [3]. The interpretation of this field is provided in clause 8.2 of [3]. This field is not present when the DCI is used for scheduling PDSCH in a LAA SCell.

-HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

-SRS timing offset – 3 bits as defined in [3]. This field is present only when the DCI format is used for scheduling PDSCH in a LAA SCell and the UE is configured with uplink transmission on the LAA Scell.

-Repetition number – 2 bits as defined in Table 5.3.3.1.17-1, where the number of transmissions for PDSCH is given by higher layer parameter maxNumber-SubframePDSCH-Repetitions for the value of '11'. This field is present only when the UE is configured with higher layer parameter blindSubframePDSCH-Repetitions set to TRUE and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3].

If the UE is not configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI, and the number of information bits in format 1A is less than that of format 0, zeros shall be appended to format 1A until the payload size equals that of format 0.

If the UE is configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI and the number of information bits in format 1A mapped onto a given search space is less than that of format 0 for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 1A until the payload size equals that of format 0, except when format 1A assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the UE is configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI and the number of information bits in format 1A mapped onto a given search space is less than that of format 0A for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 1A until the payload size equals that of format 0A, except when format 1A assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the UE is configured to decode PDCCH or EPDCCH with CRC scrambled by the C-RNTI and the number of information bits in format 1A mapped onto a given search space is less than that of format 0C for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 1A until the payload size equals that of format 0C, except when format 1A assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 1A carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 1A.

When the format 1A CRC is scrambled with a RA-RNTI, P-RNTI, SI-RNTI, SC-RNTI or G-RNTI then the following fields among the fields above are reserved:

- HARQ process number

- Downlink Assignment Index (used for cases with TDD primary cell and either FDD operation or TDD operation, and is not present for cases with FDD primary cell and either FDD operation or TDD operation)

## 5.3.3.1.3AFormat 1B

DCI format 1B is used for the compact scheduling of one PDSCH codeword in one cell with precoding information.

The following information is transmitted by means of the DCI format 1B:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Localized/Distributed VRB assignment flag – 1 bit as defined in clause 7.1.6.3 of [3]

- Resource block assignment – bits as defined in clause 7.1.6.3 of [3]

- For localized VRB:

bits provide the resource allocation

- For distributed VRB:

- For

- bits provide the resource allocation

- For

- 1 bit, the MSB indicates the gap value, where value 0 indicates  and value 1 indicates

-  bits provide the resource allocation

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- HARQ process number – 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- New data indicator – 1 bit

- Redundancy version – 2 bits

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- TPMI information for precoding – number of bits as specified in Table 5.3.3.1.3A-1

TPMI information indicates which codebook index is used in Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 of [2] corresponding to the single-layer transmission.

- PMI confirmation for precoding – 1 bit as specified in Table 5.3.3.1.3A-2

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If PMI confirmation indicates that the eNodeB has applied precoding according to PMI(s) reported by the UE, the precoding for the corresponding RB(s) in subframe n is according to the latest PMI(s) in an aperiodic CSI reported on or before subframe n-4.

Table 5.3.3.1.3A-1: Number of bits for TPMI information

Table 5.3.3.1.3A-2: Content of PMI confirmation

If the number of information bits in format 1B is equal to that for format 0/1A for scheduling the same serving cell and mapped onto the UE specific search space given by the C-RNTI as defined in [3], one bit of value zero shall be appended to format 1B.

If the number of information bits in format 1B carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one or more zero bit(s) shall be appended to format 1B until the payload size of format 1B does not belong to one of the sizes in Table 5.3.3.1.2-1 and is not equal to that of format 0/1A mapped onto the same search space.

## 5.3.3.1.4Format 1C

DCI format 1C is used for very compact scheduling of one PDSCH codeword, notifying MCCH change [6], notifying SC-MCCH change and direct indication [6] , reconfiguring TDD, and LAA common information.

The following information is transmitted by means of the DCI format 1C:

If the format 1C is used for very compact scheduling of one PDSCH codeword

-1 bit indicates the gap value, where value 0 indicates  and value 1 indicates

-For, there is no bit for gap indication

-Resource block assignment – bits as defined in 7.1.6.3 of [3] where  is defined in [2] and  is defined in [3]

-Modulation and coding scheme – 5 bits as defined in clause 7.1.7 of [3]

Else if the format 1C is used for notifying MCCH change and direct indication

-Information for MCCH change notification – 8 bits as defined in clause 5.8.1.3 of [6]

-Direct Indication information – 2 bits provide direct indication of system information update and other fields, as defined in clause 6.6a [6]. This field is only present for MBMS-dedicated cell or feMBMS/Unicast-mixed cell with  .

-Reserved information bits are added until the size is equal to that of format 1C used for very compact scheduling of one PDSCH codeword

Else if the format 1C is used for notifying SC-MCCH change

-Information for SC-MCCH change notification – 8 bits as defined in clause 5.8a.1.3 of [6]

-Reserved information bits are added until the size is equal to that of format 1C used for very compact scheduling of one PDSCH codeword

Else if the format 1C is used for reconfiguring TDD

-UL/DL configuration indication:

UL/DL configuration number 1, UL/DL configuration number 2,…, UL/DL configuration number I

Where each UL/DL configuration is 3 bits, ,  is equal to the payload size of format 1C used for very compact scheduling of one PDSCH codeword. The parameter eimta-UL-DL-ConfigIndex provided by higher layers determines the index to the UL/DL configuration indication for a serving cell.

-Zeros are added until the size is equal to that of format 1C used for very compact scheduling of one PDSCH codeword

Else

-Subframe configuration for LAA – 4 bits as defined in clause 13A of [3]

-UL duration and offset – 5 bits as defined in clause 13A of [3]. The field only applies to a UE configured with uplink transmission on a LAA SCell

-PUSCH trigger B – 1 bit as defined in clause 8.0 of [3]. The field only applies to a UE configured with uplink transmission on a LAA SCell

-COT sharing indication for AUL – 1 bit as defined in 4.2.1 of [8]. The field only applies to a UE configured with uplink transmission on a LAA SCell

-Reserved information bits are added until the size is equal to that of format 1C used for very compact scheduling of one PDSCH codeword

## 5.3.3.1.4AFormat 1D

DCI format 1D is used for the compact scheduling of one PDSCH codeword in one cell with precoding and power offset information.

The following information is transmitted by means of the DCI format 1D:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Localized/Distributed VRB assignment flag – 1 bit as defined in clause 7.1.6.3 of [3]

- Resource block assignment – bits as defined in clause 7.1.6.3 of [3]:

- For localized VRB:

bits provide the resource allocation

- For distributed VRB:

- For

- bits provide the resource allocation

- For

- 1 bit, the MSB indicates the gap value, where value 0 indicates  and value 1 indicates

-  bits provide the resource allocation

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- HARQ process number – 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- New data indicator – 1 bit

- Redundancy version – 2 bits

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- TPMI information for precoding – number of bits as specified in Table 5.3.3.1.4A-1

TPMI information indicates which codebook index is used in Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 of [2] corresponding to the single-layer transmission.

- Downlink power offset – 1 bit as defined in clause 7.1.5 of [3]

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

Table 5.3.3.1.4A-1: Number of bits for TPMI information

If the number of information bits in format 1D is equal to that for format 0/1A for scheduling the same serving cell and mapped onto the UE specific search space given by the C-RNTI as defined in [3], one bit of value zero shall be appended to format 1D.

If the number of information bits in format 1D carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one or more zero bit(s) shall be appended to format 1D until the payload size of format 1D does not belong to one of the sizes in Table 5.3.3.1.2-1 and is not equal to that of format 0/1A mapped onto the same search space.

## 5.3.3.1.5Format 2

The following information is transmitted by means of the DCI format 2:

-Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

-Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

-Resource block assignment:

-For resource allocation type 0 defined in clause 7.1.6.1 of [3]:

-bits provide the resource allocation

-For resource allocation type 1 as defined in clause 7.1.6.2 of [3]:

- bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

-1 bit indicates a shift of the resource allocation span

- bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause 7.1.6.1 of [3]

-TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

-Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

-HARQ process number - 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

-Transport block to codeword swap flag – 1 bit

In addition, for transport block 1:

-Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

-New data indicator – 1 bit

-Redundancy version – 2 bits

-MUST interference presence and power ratio – 0 or 2 bits as defined in clause 6.3.3 of [2]. This field is present only when the UE is configured for MUST-near operation and the number of antenna ports for CRS transmission in the serving cell is 2

In addition, for transport block 2:

-Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

-New data indicator – 1 bit

-Redundancy version – 2 bits

-MUST interference presence and power ratio – 0 or 2 bits as defined in clause 6.3.3 of [2]. This field is present only when the UE is configured for MUST-near operation and the number of antenna ports for CRS transmission in the serving cell is 2

Precoding information – number of bits as specified in Table 5.3.3.1.5-3

-HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

-Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If both transport blocks are enabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.51.

In case one of the transport blocks is disabled as specified in clause 7.1.7.2 of [3], the transport block to codeword swap flag is reserved and the transport block to codeword mapping is specified according to Table 5.3.3.1.52.

Table 5.3.3.1.5-1: Transport block to codeword mapping(two transport blocks enabled)

Table 5.3.3.1.5-2: Transport block to codeword mapping(one transport block enabled)

The interpretation of the precoding information field depends on the number of enabled codewords according to Table 5.3.3.1.5-4 and Table 5.3.3.1.5-5. Note that TPMI indicates which codebook index is used in Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 of [2]. For a single enabled codeword, indices 18 to 34 inclusive in Table 5.3.3.1.5-5 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers with closed-loop spatial multiplexing.

If the number of information bits in format 2 carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 2.

Some entries in Table 5.3.3.1.5-4 and Table 5.3.3.1.5-5 are used for indicating that the eNodeB has applied precoding according to PMI(s) reported by the UE. In these cases the precoding for the corresponding RB(s) in subframe n is according to the latest PMI(s) in an aperiodic CSI reported on or before subframe n-4. For aperiodic CSI mode 2-2: Precoding of scheduled resource blocks belonging to the reported preferred M subband(s) use precoder(s) according to the preferred M subband PMI indicated by the latest aperiodic CSI report; Precoding of scheduled resource blocks not belonging to the reported preferred M subband(s) use a precoder according to the wideband PMI indicated by the latest aperiodic CSI report.

Table 5.3.3.1.5-3: Number of bits for precoding information

Table 5.3.3.1.5-4: Content of precoding information field for 2 antenna ports

Table 5.3.3.1.5-5: Content of precoding information field for 4 antenna ports

## 5.3.3.1.5AFormat 2A

The following information is transmitted by means of the DCI format 2A:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

- Resource block assignment:

- For resource allocation type 0 as defined in clause 7.1.6.1 of [3]

- bits provide the resource allocation

- For resource allocation type 1 as defined in clause 7.1.6.2 of [3]

-  bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

- 1 bit indicates a shift of the resource allocation span

-  bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause 7.1.6.1 of [3]

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- HARQ process number - 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- Transport block to codeword swap flag – 1 bit

In addition, for transport block 1:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

In addition, for transport block 2:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

- Precoding information – number of bits as specified in Table 5.3.3.1.5A-1

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback. - MUST interference presence and power ratio – 0 or 2 bits as defined in clause 6.3.3 of [2]. This field is present only when the UE is configured for MUST-near operation and the number of antenna ports for CRS transmission in the serving cell is 2.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If both transport blocks are enabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.51.

In case one of the transport blocks is disabled, the transport block to codeword swap flag is reserved and the transport block to codeword mapping is specified according to Table 5.3.3.1.52.

The precoding information field is defined according to Table 5.3.3.1.5A2. For a single enabled codeword, index 1 in Table 5.3.3.1.5A-2 is only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers with large delay CDD.

For transmission with 2 antenna ports, the precoding information field is not present. The number of transmission layers is equal to 2 if both codewords are enabled; transmit diversity is used if codeword 0 is enabled while codeword 1 is disabled.

If the number of information bits in format 2A carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 2A.

Table 5.3.3.1.5A-1: Number of bits for precoding information

Table 5.3.3.1.5A-2: Content of precoding information field for 4 antenna ports

## 5.3.3.1.5BFormat 2B

The following information is transmitted by means of the DCI format 2B:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

- Resource block assignment:

- For resource allocation type 0 as defined in clause 7.1.6.1 of [3]

- bits provide the resource allocation

- For resource allocation type 1 as defined in clause 7.1.6.2 of [3]

-  bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

- 1 bit indicates a shift of the resource allocation span

-  bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause [7.1.6.1] of [3]

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- HARQ process number - 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- Scrambling identity– 1 bit as defined in clause 6.10.3.1 of [2]

- SRS request – [0-1] bit. This field can only be present for TDD operation and if present is defined in clause 8.2 of [3]

In addition, for transport block 1:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

In addition, for transport block 2:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- MUST interference presence and modulation (This field is present only when the UE is configured for MUST operation) – 0 or 2 bits. The field is defined in Table 5.3.3.1.5C-3, where the interfering antenna port is in {7,8} excluding the antenna port for transmission. The interfering antenna port has the same scrambling identity as indicated in the "Scrambling identity" field.

- SRS timing offset – 3 bits as defined in [3]. This field is present only when the DCI format is used for scheduling PDSCH in a LAA SCell and the UE is configured with uplink transmission on the LAA SCell.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If both transport blocks are enabled, the number of layers equals two; transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. Antenna ports 7 and 8 are used for spatial multiplexing.

In case one of the transport blocks is disabled, the number of layers equals one; the transport block to codeword mapping is specified according to Table 5.3.3.1.52; and the antenna port for single-antenna port transmission is according to Table 5.3.3.1.5B-1.

Table 5.3.3.1.5B-1: Antenna port for single-antenna port transmission (one transport block disabled)

If the number of information bits in format 2B carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 2B.

## 5.3.3.1.5CFormat 2C

The following information is transmitted by means of the DCI format 2C:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

- Resource block assignment:

- For resource allocation type 0 as defined in clause 7.1.6.1 of [3]

- bits provide the resource allocation

- For resource allocation type 1 as defined in clause 7.1.6.2 of [3]

-  bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

- 1 bit indicates a shift of the resource allocation span

-  bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause [7.1.6.1] of [3]

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- HARQ process number - 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- Antenna port(s), scrambling identity and number of layers – 3 bits as specified in Table 5.3.3.1.5C-1 where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2], or 4 bits as specified in Table 5.3.3.1.5C-2 where nSCID is the scrambling identity for antenna ports 7, 8, 11 and 13 defined in clause 6.10.3.1 of [2] when higher layer parameter dmrs-tableAlt is set to 1, or 1 bit as specified in Table 5.3.3.1.5C-6 where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2] when higher layer parameter semiOpenLoop is configured.

- SRS request – [0-1] bit. This field can only be present for TDD operation and if present is defined in clause 8.2 of [3]

In addition, for transport block 1:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

In addition, for transport block 2:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- MUST interference presence, antenna port, and modulation (this field is only present when the UE is configured for MUST operation) – 2 bits when higher layer parameter dmrs-tableAlt is not configured or is set to 0, 4 bits when higher layer parameter k-max is set to 1 and dmrs-tableAlt =1, or 6 bits when k-max is set to 3 and dmrs-tableAlt =1. For the 2 and 6 bit fields, two bits are defined for each interfering antenna port in Table 5.3.3.1.5C-3, where a single interfering antenna port is in {7,8} excluding the antenna port for transmission, and multiple interfering antenna ports are in {7,8,11,13} excluding the antenna ports for transmission. For the 6 bit field, the two or four LSB are reserved in the case of two or one interfering antenna port, respectively. Each pair of the used bits in 6 bit field from MSB to LSB is associated with one interfering antenna port in increasing order of port index. For the 4 bit field, two MSB are defined for interference presence and antenna port in Table 5.3.3.1.5C-4 where the single interfering antenna port is one of {7,8,11,13} excluding the antenna port for transmission, and two LSB are defined for interference modulation in 5.3.3.1.5C-5. The interfering antenna port(s) have the same scrambling identity and OCC length as indicated in the "Antenna port(s), scrambling identity and number of layers" field.

- SRS timing offset – 3 bits as defined in [3]. This field is present only when the DCI format is used for scheduling PDSCH in a LAA SCell and the UE is configured with uplink transmission on the LAA SCell.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If both transport blocks are enabled; transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. When higher layer parameter semiOpenLoop is configured, antenna ports 7 and 8 are used for spatial multiplexing.

In case one of the transport blocks is disabled; the transport block to codeword mapping is specified according to Table 5.3.3.1.52. For the single enabled codeword, Value = 4, 5, 6 in Table 5.3.3.1.5C-1 or Value = 12, 13,14 in Table 5.3.3.1.5C-2 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two, three or four layers, respectively. When higher layer parameter semiOpenLoop is configured, antenna ports 7 and 8 are used for transmit diversity.

If the number of information bits in format 2C carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 2C.

Table 5.3.3.1.5C-1: Antenna port(s), scrambling identity and number of layers indication

Table 5.3.3.1.5C-2: Antenna port(s), scrambling identity and number of layers indication

Table 5.3.3.1.5C-3: Content of MUST interference presence and modulation for an antenna port

Table 5.3.3.1.5C-4: Content of MUST interference presence and antenna port

Table 5.3.3.1.5C-5: Content of MUST interference modulation

Table 5.3.3.1.5C-6: Antenna port(s), scrambling identity and number of layers indication

## 5.3.3.1.5DFormat 2D

The following information is transmitted by means of the DCI format 2D:

- Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

- Resource allocation header (resource allocation type 0 / type 1) – 1 bit as defined in clause 7.1.6 of [3]

If downlink bandwidth is less than or equal to 10 PRBs, there is no resource allocation header and resource allocation type 0 is assumed.

- Resource block assignment:

- For resource allocation type 0 as defined in clause 7.1.6.1 of [3]

- bits provide the resource allocation

- For resource allocation type 1 as defined in clause 7.1.6.2 of [3]

-  bits of this field are used as a header specific to this resource allocation type to indicate the selected resource blocks subset

- 1 bit indicates a shift of the resource allocation span

-  bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause [7.1.6.1] of [3]

- TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

- Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2.

- HARQ process number - 4 bits if higher layer parameter dl-STTI-Length is configured for the cell, otherwise 3 bits (for cases with FDD primary cell not configured with EN-DC/NE-DC and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2), 4 bits (for cases with TDD primary cell, or for cases with EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

- Antenna port(s), scrambling identity and number of layers – 3 bits as specified in Table 5.3.3.1.5C-1 (or Table 5.3.3.1.5D-1 for two codewords when higher layer parameter qcl-Operation is set to 'typeC') where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2], or 4 bits as specified in Table 5.3.3.1.5C-2 (or Table 5.3.3.1.5D-2 for two codewords when higher layer parameter qcl-Operation is set to 'typeC') where nSCID is the scrambling identity for antenna ports 7, 8, 11 and 13 defined in clause 6.10.3.1 of [2] when higher layer parameter dmrs-tableAlt is set to 1, or 1 bit as specified in Table 5.3.3.1.5C-6 where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2] when higher layer parameter semiOpenLoop is configured.

- SRS request – [0-1] bit. This field can only be present for TDD operation and if present is defined in clause 8.2 of [3]

In addition, for transport block 1:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

In addition, for transport block 2:

- Modulation and coding scheme – 5 bits if higher layer parameter altMCS-Table is not configured, 6 bits otherwise, as defined in clause 7.1.7 of [3]

- New data indicator – 1 bit

- Redundancy version – 2 bits

- PDSCH RE Mapping and Quasi-Co-Location Indicator – 2 bits as defined in clauses 7.1.9 and 7.1.10 of [3]

- HARQ-ACK resource offset (this field is present when this format is carried by EPDCCH. This field is not present when this format is carried by PDCCH) – 2 bits as defined in clause 10.1 of [3]. The 2 bits are set to 0 when this format is carried by EPDCCH on a secondary cell, or when this format is carried by EPDCCH on the primary cell scheduling PDSCH on a secondary cell and the UE is configured with PUCCH format 3 for HARQ-ACK feedback.

- MUST interference presence, antenna port, and modulation (this field is only present when the UE is configured for MUST operation) – 2 bits when higher layer parameter dmrs-tableAlt is not configured or is set to 0, 4 bits when higher layer parameter k-max is set to 1 and dmrs-tableAlt =1, 6 bits when k-max is set to 3 and dmrs-tableAlt =1. For the 2 and 6 bit fields, two bits are defined for each interfering antenna port in Table 5.3.3.1.5C-3, where a single interfering antenna port is in {7,8} excluding the antenna port for transmission, and multiple interfering antenna ports are in {7,8,11,13} excluding the antenna ports for transmission. For the 6 bit field, the two or four LSB are reserved in the case of two or one interfering antenna port, respectively. Each pair of the used bits in 6 bit field from MSB to LSB is associated with one interfering antenna port in increasing order of port index. For the 4 bit field, two MSB are defined for interference presence and antenna port in Table 5.3.3.1.5C-4 where the single interfering antenna port is one of {7,8,11,13} excluding the antenna port for transmission, and two LSB are defined for interference modulation in 5.3.3.1.5C-5. The interfering antenna port(s) have the same scrambling identity and OCC length as indicated in the "Antenna port(s), scrambling identity and number of layers" field.

- SRS timing offset – 3 bits as defined in [3]. This field is present only when the DCI format is used for scheduling PDSCH in a LAA SCell and the UE is configured with uplink transmission on the LAA SCell.

- Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping – 2 bits as defined in clauses 7.1.9 and 7.2.7 of [3]. This field is present only when the UE is configured with csi-RS-ConfigZP-ApList.

If both transport blocks are enabled; transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. When higher layer parameter semiOpenLoop is configured, antenna ports 7 and 8 are used for spatial multiplexing.

In case one of the transport blocks is disabled; the transport block to codeword mapping is specified according to Table 5.3.3.1.52. For the single enabled codeword, Value = 4, 5, 6 in Table 5.3.3.1.5C-1 or Value = 12, 13,14 in Table 5.3.3.1.5C-2 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two, three or four layers, respectively. When higher layer parameter semiOpenLoop is configured, antenna ports 7 and 8 are used for transmit diversity.

If the number of information bits in format 2D carried by PDCCH belongs to one of the sizes in Table 5.3.3.1.2-1, one zero bit shall be appended to format 2D.

Table 5.3.3.1.5D-1: Antenna port(s), scrambling identity and number of layers indication

Table 5.3.3.1.5D-2: Antenna port(s), scrambling identity and number of layers indication

## 5.3.3.1.6Format 3

DCI format 3 is used for the transmission of TPC commands for PUCCH, SPUCCH corresponding to semi-persistently scheduled PDSCH with slot/subslot duration, semi-persistently scheduled PUSCH with slot/subslot duration, PUSCH with subframe duration with 2-bit power adjustments, and additional SRS symbols.

The following information is transmitted by means of the DCI format 3:

- TPC command number 1, TPC command number 2,…, TPC command number N

where , and where  is equal to the payload size of format 0 before CRC attachment when format 0 is mapped onto the common search space, including any padding bits appended to format 0. The parameter tpc-Index or tpc-Index-PUCCH-SCell-r13 or tpc-IndexSRS-Add provided by higher layers determines the index to the TPC command for a given UE.

If , a bit of value zero shall be appended to format 3.

For BL/CE UE, Lformat 0 and format 0 are replaced by Lformat 6-0A and format 6-0A, respectively, in the description above.

## 5.3.3.1.7Format 3A

DCI format 3A is used for the transmission of TPC commands for PUCCH, SPUCCH corresponding to semi-persistently scheduled PDSCH with slot/subslot duration, semi-persistently scheduled PUSCH with slot/subslot duration, PUSCH with subframe duration with single bit power adjustments, and additional SRS symbols.

The following information is transmitted by means of the DCI format 3A:

-TPC command number 1, TPC command number 2,…, TPC command number M

where , and where  is equal to the payload size of format 0 before CRC attachment when format 0 is mapped onto the common search space, including any padding bits appended to format 0. The parameter tpc-Index or tpc-Index-PUCCH-SCell-r13 or tpc-IndexSRS-Add provided by higher layers determines the index to the TPC command for a given UE.

For BL/CE UE, Lformat 0 and format 0 are replaced by Lformat 6-0A and format 6-0A, respectively, in the description above.

## 5.3.3.1.7AFormat 3B

DCI format 3B is used for the transmission of a group of TPC commands for SRS transmissions by one or more UEs. Along with a TPC command, a SRS request may also be transmitted.

The following information is transmitted by means of the DCI format 3B:

-block number 1, block number 2, …, block number

where the starting position of a block is determined by the parameter startingBitOfFormat3B or startingBitOfFormat3B-SRS-Add provided by higher layers for the UE configured with the block.

If a UE has more than 5 TDD SCells configured without PUCCH and without PUSCH, one block is configured for the UE by higher layers, with the following fields defined for the block:

-SRS request – 0 or 2 bits. This field is present, and if present interpreted, according to the definition in Clause 8.2 of [3].

-TPC command number 1, TPC command number 2, …, TPC command number n

The n TPC command fields correspond to a set of n TDD SCells without PUCCH and without PUSCH, with the set indicated by the SRS request field or determined by higher layers if there is no SRS request field present. A TPC command field has 1 bit if the parameter fieldTypeFormat3B or fieldTypeFormat3B-SRS-Add provided by higher layers has a value of 1 or 3, and 2 bits if the parameter fieldTypeFormat3B or fieldTypeFormat3B-SRS-Add has a value of 2 or 4.

If a UE has up to 5 TDD SCells configured without PUCCH and without PUSCH, one or more blocks each corresponding to an SCell are configured by higher layers, with the following fields defined for each block:

- SRS request - 0, 1, or 2 bits, where the number of bits is determined in Clause 8.2 of [3].

- TPC command - 1 or 2 bits, where the number of bits is 1 if the parameter fieldTypeFormat3B or fieldTypeFormat3B-SRS-Add provided by higher layers has a value of 1 or 3, and 2 if the parameter fieldTypeFormat3B or fieldTypeFormat3B-SRS-Add has a value of 2 or 4.

The size of format 3B is equal to , and where  is equal to the payload size of format 0 before CRC attachment when format 0 is mapped onto the common search space, including any padding bits appended to format 0.

## 5.3.3.1.8Format 4

DCI format 4 is used for the scheduling of PUSCH in one UL cell with multi-antenna port transmission mode,

The following information is transmitted by means of the DCI format 4:

-Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

-Resource block assignment -  bits, where P is the UL RBG size as defined in clause 8.1.2 of [3]

-For resource allocation type 0:

-The LSBs provide the resource allocation in the UL subframe as defined in clause 8.1.1 of [3]

-For resource allocation type 1:

-The  LSBs provide the resource allocation in the UL subframe as defined in clause 8.1.2 of [3]

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-Cyclic shift for DM RS and OCC index and IFDMA configuration – 3 bits as defined in clause 5.5.2.1.1 of [2]

-UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0, or TDD operation with uplink-downlink configuration 6 and special subframe configuration 10 when the higher layer parameter symPUSCH-UpPts or shortProcessingTime is configured for the cell)

-Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (this field is present only for the following cases: 1) TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation; or 2) EN-DC/NE-DC with FDD primary cell and higher layer parameter tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 configured)

-CSI request – 1, 2, 3, 4 or 5 bits as defined in clause 7.2.1 of [3].

If UEs are not configured with CSI-RS-ConfigNZPAperiodic or if UEs are configured with CSI-RS-ConfigNZPAperiodic and numberActivatedAperiodicCSI-RS-Resources=1 for each CSI process,

the 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 3-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 1-bit field applies

If UEs are configured with CSI-RS-ConfigNZPAperiodic and numberActivatedAperiodicCSI-RS-Resources>1 for at least one CSI process,

the 4-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 5-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 3-bit field applies.

-SRS request – 2 bits as defined in clause 8.2 of [3]

-Resource allocation type – 1 bit as defined in clause 8.1 of [3]

-Cyclic Shift Field mapping table for DMRS – 1 bit as defined in clause 5.5.2.1.1 of [2]. The 1-bit field applies to UEs that are configured with higher layer parameter UL-DMRS-IFDMA.

-HARQ process number – 4 bits if higher layer parameter ul-STTI-Length is configured for the cell, otherwise 3 bits (this field is present when higher layer parameter shortProcessingTime is configured for the cell)

-Redundancy version – 2 bits (this field is present when higher layer parameter shortProcessingTime is configured for the cell)

In addition, for transport block 1:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3]

-New data indicator – 1 bit

In addition, for transport block 2:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3]

-New data indicator – 1 bit

Precoding information and number of layers: number of bits as specified in Table 5.3.3.1.8-1. Bit field as shown in Table 5.3.3.1.8-2 and Table 5.3.3.1.8- 3. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2]. If both transport blocks are enabled, transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. In case one of the transport blocks is disabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.5-2. For a single enabled codeword, indices 24 to 39 in Table 5.3.3.1.8-3 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers.

Table 5.3.3.1.8-1: Number of bits for precoding information

Table 5.3.3.1.8-2: Content of precoding information field for 2 antenna ports

Table 5.3.3.1.8-3: Content of precoding information field for 4 antenna ports

If the number of information bits in format 4 is equal to the payload size for DCI format 1, 2, 2A, 2B, 2C or 2D associated with the configured DL transmission mode in the same serving cell, one zero bit shall be appended to format 4.

## 5.3.3.1.8AFormat 4A

DCI format 4 is used for the scheduling of PUSCH in a LAA SCell with multi-antenna port transmission mode, or activating/releasing AUL transmission for a UE with multi-antenna port transmission mode, or indicating AUL-DFI to a UE that is activated with AUL transmission with multi-antenna port transmission mode.

The following information is transmitted by means of the DCI format 4A:

-Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

If the format 4A DCI is scrambled by C-RNTI

-PUSCH trigger A – 1 bit, where value 0 indicates non-triggered scheduling and value 1 indicates triggered scheduling as defined in clause 8.0 of [3];

Else

-Flag for AUL differentiation – 1 bit, where value 0 indicates activating/releasing AUL transmission and value 1 indicates AUL-DFI.

If the format 4A is used for the scheduling of PUSCH in a LAA SCell or activating/releasing AUL transmission for a UE, all the remaining fields are set as follows:

-Timing offset – 4 bits as defined in clause 8.0 of [3].

-When the PUSCH trigger A is set to 0,

-The field indicates the absolute timing offset for the PUSCH transmission.

-Otherwise,

-The first two bits of the field indicate the timing offset, relative to the UL offset l as defined in clause 13A of [3], for the PUSCH transmission.

-The last two bits of the field indicate the time window within which the scheduling of PUSCH via triggered scheduling is valid.

-Resource block assignment – 5 or 6 bits provide the resource allocation in the UL subframe as defined in clause 8.1.4 of [3].

-HARQ process number – 4 bits.

-Redundancy version – 2 bits as defined in clause 8.6.1 of [3] which is common for both transport blocks.

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-Cyclic shift for DM RS and OCC index – 3 bits as defined in clause 5.5.2.1.1 of [2]

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]. The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 3-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 1-bit field applies.

-SRS request – 2 bits as defined in clause 8.2 of [3].

-Partial PUSCH Mode – 2 bits as specified in Table 5.3.3.1.1A-3. This field is only present when at least one of laa-PUSCH-Mode1, laa-PUSCH-Mode2, and laa-PUSCH-Mode3 is configured. The UE is not expected to be indicated with a partial PUSCH mode that is not configured by RRC.

-PUSCH starting position – 2 bits

-as specified in Table 5.3.3.1.1A-2 if the 'Partial PUSCH Mode' field indicates Partial PUSCH Mode 2;

-as specified in Table 5.3.3.1.1A-1 otherwise.

-PUSCH ending symbol – 1 bit, where

-if the 'Partial PUSCH Mode' field indicates Partial PUSCH Mode 3, value 0 indicates symbol 6 of the subframe, and value 1 indicates symbol 3 of the subframe.

-otherwise value 0 indicates the last symbol of the subframe and value 1 indicates the second to last symbol of the subframe.

-Channel Access type – 1 bit as defined in clause 4.2 of [8].

-Channel Access Priority Class – 2 bits as defined in clause 4.2 of [8].

In addition, for transport block 1:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3].

-New data indicator – 1 bit.

In addition, for transport block 2:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3].

-New data indicator – 1 bit.

Precoding information and number of layers: number of bits as specified in Table 5.3.3.1.8-1. Bit field as shown in Table 5.3.3.1.8-2 and Table 5.3.3.1.8- 3. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2]. If both transport blocks are enabled, transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. In case one of the transport blocks is disabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.5-2. For a single enabled codeword, indices 24 to 39 in Table 5.3.3.1.8-3 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers.

If the format 4A is used for indicating AUL-DFI to a UE that is activated with AUL transmission, all the remaining fields are set as follows:

-HARQ-ACK bitmap – 32 bits, where the order of the bitmap to HARQ process index mapping is such that HARQ process indices are mapped in ascending order from MSB to LSB of the bitmap. For each bit of the bitmap, value 1 indicates ACK, and value 0 indicates NACK.

-TPC command – 2 bits as defined in clause 5.1.1.1 of [3].

-Precoding information: number of bits as specified in Table 5.3.3.1.8-1. Bit field as shown in Table 5.3.3.1.8-2 and Table 5.3.3.1.8- 3. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2]. If both transport blocks are enabled, transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. In case one of the transport blocks is disabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.5-2. For a single enabled codeword, indices 24 to 39 in Table 5.3.3.1.8-3 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers.

-All the remaining bits in format 4A are set to zero.

If the number of information bits in format 4A is equal to the payload size for DCI format 1, 2, 2A, 2B, 2C or 2D associated with the configured DL transmission mode in the same serving cell, one zero bit shall be appended to format 4A.

## 5.3.3.1.8BFormat 4B

DCI format 4B is used for the scheduling of PUSCH with multi-antenna port transmission mode in each of multiple subframes in a LAA SCell.

The following information is transmitted by means of the DCI format 4B:

-Carrier indicator – 0 or 3 bits. The field is present according to the definitions in [3].

-PUSCH trigger A – 1 bit, where value 0 indicates non-triggered scheduling and value 1 indicates triggered scheduling as defined in clause 8.0 of [3].

-Timing offset – 4 bits as defined in clause 8.0 of [3].

-When the PUSCH trigger A is set to 0,

-The field indicates the absolute timing offset for the PUSCH transmission.

-Otherwise,

-The first two bits of the field indicate the timing offset, relative to the UL offset l as defined in clause 13A of [3], for the PUSCH transmission.

-The last two bits of the field indicate the time window within which the scheduling of PUSCH via triggered scheduling is valid.

-Number of scheduled subframes – 1 or 2 bits. The 1-bit field applies when maxNumberOfSchedSubframes-Format4B-r14 is configured by higher layers to two, otherwise the 2-bit field applies.

-Resource block assignment – 5 or 6 bits provide the resource allocation in the UL subframe as defined in clause 8.1.4 of [3].

-HARQ process number – 4 bits. The 4-bit applies to the first scheduled subframe, and the HARQ process numbers for other scheduled subframes are defined in clause 8.0 of [3].

-Redundancy version – maxNumberOfSchedSubframes-Format4B-r14 bits. Each scheduled PUSCH corresponds to 1 bit as defined in clause 8.6.1 of [3]. Redundancy version is common for both transport blocks.

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3].

-Cyclic shift for DM RS and OCC index – 3 bits as defined in clause 5.5.2.1.1 of [2].

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]. The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 3-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 1-bit field applies.

-SRS request – 2 bits as defined in clause 8.2 of [3].

-Partial PUSCH Mode 1 – 1 bit only present if laa-PUSCH-Mode1 is configured by higher layer, and applicable to each of the scheduled subframe(s), except for the first scheduled subframe in case the 'Partial PUSCH Mode 2' field is value 1 and the last scheduled subframe in case the 'Partial PUSCH Mode 3' field is value 1, where

-value 0 indicates the starting position of the PUSCH is determined following Partial PUSCH Mode 0 as defined in Table 5.3.3.1.1A-3;

-value 1 indicates the starting position of the PUSCH of the first transmitted subframe is determined following Partial PUSCH Mode 1 as defined in Table 5.3.3.1.1A-3.

-Partial PUSCH Mode 2 – 1 bit. This field is only present if laa-PUSCH-Mode2 is configured by higher layer, and applicable to only the first scheduled subframe.

-Partial PUSCH Mode 3 – 1 bit. This field is only present if laa-PUSCH-Mode3 is configured by higher layer, and applicable to only the last scheduled subframe.

-PUSCH starting position – 2 bits

-as specified in Table 5.3.3.1.1A-2 applicable to only the first scheduled subframe, if the 'Partial PUSCH Mode 2' field is value 1;

-as specified in Table 5.3.3.1.1A-1 applicable to only the first scheduled subframe otherwise.

-PUSCH ending symbol – 1 bit, where

-if the 'Partial PUSCH Mode 3' is value 1, value 0 indicates symbol 6 of the last scheduled subframe, and value 1 indicates symbol 3 of the last scheduled subframe;

-otherwise value 0 indicates the last symbol of the last scheduled subframe and value 1 indicates the second to last symbol of the last scheduled subframe.

-Channel Access type – 1 bit as defined in clause 4.2 of [8].

-Channel Access Priority Class – 2 bits as defined in clause 4.2 of [8].

In addition, for transport block 1:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3].

-New data indicator – maxNumberOfSchedSubframes-Format4B-r14 bits. Each scheduled PUSCH corresponds to 1 bit.

In addition, for transport block 2:

-Modulation and coding scheme and redundancy version – 5 bits as defined in clause 8.6 of [3].

-New data indicator – maxNumberOfSchedSubframes-Format4B-r14 bits. Each scheduled PUSCH corresponds to 1 bit.

Precoding information and number of layers: number of bits as specified in Table 5.3.3.1.8-1. Bit field as shown in Table 5.3.3.1.8-2 and Table 5.3.3.1.8- 3. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2]. If both transport blocks are enabled, transport block 1 is mapped to codeword 0; and transport block 2 is mapped to codeword 1. In case one of the transport blocks is disabled, the transport block to codeword mapping is specified according to Table 5.3.3.1.5-2. For a single enabled codeword, indices 24 to 39 in Table 5.3.3.1.8-3 are only supported for retransmission of the corresponding transport block if that transport block has previously been transmitted using two layers.

If the number of information bits in format 4B is equal to the payload size for DCI format 1, 2, 2A, 2B, 2C or 2D associated with the configured DL transmission mode in the same serving cell, one zero bit shall be appended to format 4B.

## 5.3.3.1.9Format 5

DCI format 5 is used for the scheduling of PSCCH, and also contains several SCI format 0 fields used for the scheduling of PSSCH.

The following information is transmitted by means of the DCI format 5:

- Resource for PSCCH – 6 bits as defined in clause 14.2.1 of [3]

-TPC command for PSCCH and PSSCH – 1 bit as defined in clauses 14.2.1 and 14.1.1 of [3]

- SCI format 0 fields according to 5.4.3.1.1:

- Frequency hopping flag

- Resource block assignment and hopping resource allocation

- Time resource pattern

If the number of information bits in format 5 mapped onto a given search space is less than the payload size of format 0 for scheduling the same serving cell, zeros shall be appended to format 5 until the payload size equals that of format 0 including any padding bits appended to format 0.

## 5.3.3.1.9AFormat 5A

DCI format 5A is used for the scheduling of PSCCH, and also contains several SCI format 1 fields used for the scheduling of PSSCH.

The following information is transmitted by means of the DCI format 5A:

-Carrier indicator –3 bits. This field is present according to the definitions in [3].

-Lowest index of the subchannel allocation to the initial transmission -  bits as defined in clause 14.1.1.4C of [3].

-SCI format 1 fields according to 5.4.3.1.2:

-Frequency resource location of initial transmission and retransmission.

-Time gap between initial transmission and retransmission.

-SL index – 2 bits as defined in clause 14.2.1 of [3] (this field is present only for cases with TDD operation with uplink-downlink configuration 0-6).

When the format 5A CRC is scrambled with SL-SPS-V-RNTI, the following fields are present:

-SL SPS configuration index – 3 bits as defined in clause 14.2.1 of [3].

-Activation/release indication – 1 bit, where value 0 indicates release and value 1 indicates activation.

If the number of information bits in format 5A mapped onto a given search space is less than the payload size of format 0 mapped onto the same search space, zeros shall be appended to format 5A until the payload size equals that of format 0 including any padding bits appended to format 0.

If the format 5A CRC is scrambled by SL-V-RNTI and if the number of information bits in format 5A mapped onto a given search space is less than the payload size of format 5A with CRC scrambled by SL-SPS-V-RNTI mapped onto the same search space and format 0 is not defined on the same search space, zeros shall be appended to format 5A until the payload size equals that of format 5A with CRC scrambled by SL-SPS-V-RNTI.

## 5.3.3.1.10Format 6-0A

DCI format 6-0A is used for the scheduling of PUSCH in one UL cell, for the indication of ACK feedback, and operation on preconfigured UL resources.

The following information is transmitted by means of the DCI format 6-0A:

-Flag format 6-0A/format 6-1A differentiation – 1 bit, where value 0 indicates format 6-0A and value 1 indicates format 6-1A

-Frequency hopping flag – 1 bit, where value 0 indicates frequency hopping is not enabled and value 1 indicates frequency hopping is enabled as defined in clause 5.3.4 of [2]. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Number of resource units – 2 bits, where value '00' indicates the format 6-0A DCI uses PRB resource allocation, otherwise the DCI format 6-0A uses sub-PRB resource allocation as defined in clause 8.1.6 of [3]. This field is present when ce-PUSCH-SubPRB-Config is configured by higher layers and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3], or when the DCI is mapped onto the UE-specific search space given by PUR-RNTI as defined in [3] and the UE is not configured with higher layer parameter numRUs = '00'.

-Resource block assignment –

-If the format 6-0A DCI uses sub-PRB resource allocation:

-+6 bits for PUSCH as defined in [3]

- MSB bits provide the narrowband index as defined in clause 5.2.4 of [2]

-6 bits provide the resource allocation within the indicated narrowband using UL resource allocation type 5 as defined in clause 8.1.6 of [3]

-Else if flexible starting PRB for PUSCH resource allocation is enabled by higher layers with  equal to  and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3],  bits for FDD PUSCH and  bits for TDD PUSCH provide the resource allocation using UL resource allocation type 0 as defined in clause 8.1.1 of [3]log2(6NRBUL)log2(5NRBUL)

-Otherwise,+5 bits for PUSCH as defined in [3]:

-If the 5 LSB bits indicate a value not larger than 20

- MSB bits provide the narrowband index as defined in clause 5.2.4 of [2]

-5 bits provide the resource allocation using UL resource allocation type 0 within the indicated narrowband

-Otherwise,

-+5 bits provide the resource allocation using UL resource allocation type 4 as defined in clause 8.1.5 of[ 3]

If format 6-0A CRC is scrambled by PUR-RNTI and Resource block assignment is set to all ones, the remaining fields are set as follows:

-ACK or Fallback indicator – 1 bit, where value 0 indicates ACK and value 1 indicates fallback as defined in clause 9.1.5.3 of [3]

-PUSCH repetition adjustment – 2 bits, this field refers to indices n1, n2, …, n4 in Table 8-2b of [3]

-Timing advance adjustment – 6 bits as defined in clause 4.2.3 of [3]. The field is only present if ACK or Fallback indicator is set to 0.

-All the remaining bits in format 6-0A are set to zero

Otherwise

-Modulation and coding scheme – 3 or 4 bits as defined in clause 8.6 of [3] . The 3-bit field applies when the format 6-0A DCI uses sub-PRB resource allocation, otherwise the 4-bit field applies.

-Repetition number – 2 or 3 bits as defined in clause 8.0 of [3]. The 3-bit field applies when ce-pdsch-puschEnhancement-config is configured by higher layers and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3], otherwise the 2-bit field applies.

-HARQ process number – 3 bits. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-New data indicator – 1 bit. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Redundancy version – 2 bits. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0)

-Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (This field is present only for cases with TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation. This field is reserved when the configured maximum repetition number is larger than 1 for MPDCCH, or when the higher layer parameter csi-NumRepetitionCE-r13 indicates more than one subframe)

-CSI request – 1 bit as defined in clause 7.2.1 of [3]. This field is reserved if the format 6-0A DCI uses sub-PRB resource allocation.

-SRS request –1 bit. The interpretation of this field is provided in clause 8.2 of [3]

-DCI subframe repetition number – 2 bits as defined in clause 9.1.5 of [3]

-Modulation order override – 1 bit as defined in clause 8.6.1 of [3]. This field is only present when ce-pdsch-puschEnhancement-config is configured by higher layers and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3]

-Scheduling TBs for Unicast – 12 bits. This field is only present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3]. This field schedules one TB if the CRC of the DCI is scrambled by SPS C-RNTI.

-If one TB is scheduled

-5 bits set to zero

-HARQ process number – 3 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-Frequency hopping flag – 1 bit, where value 0 indicates frequency hopping is not enabled and value 1 indicates frequency hopping is enabled as defined in clause 5.3.4 of [2]. If frequency hopping is not enabled by higher layers, this field is set to 0.

-If two TBs are scheduled

-2 bits set to zero

-HARQ index with offset – 6 bits provide the HARQ index + offset, with an offset of +8 and HARQ index as defined in 8.0 of [3]

-New data indicators – 2 bits, one for each scheduled TB in increasing order of HARQ process ID

-Redundancy version for TB 1 – 1 bit

-Redundancy version for TB 2 – 1 bit. If Repetition number is > 1 and frequency hopping is enabled by higher layers then this bit is a Frequency hopping flag for the TBs, and TB2 uses the redundancy version for TB1.

-If four TBs are scheduled

-1 bit set to zero

-HARQ index with offset – 7 bits provide the HARQ index + offset, with an offset of +36 and HARQ index as defined in 8.0 of [3]

-New data indicators – 4 bits, one for each scheduled TB in increasing order of HARQ process ID

-If six TBs are scheduled

-HARQ index with offset – 6 bits provide the HARQ index + offset, with an offset of +27 and HARQ index as defined in 8.0 of [3]

-New data indicators – 6 bits, one for each scheduled TB in increasing order of HARQ process ID

-If eight TBs are scheduled

-3 bits set to one

-New data indicators – 8 bits, one for each scheduled TB in increasing order of HARQ process ID

-Redundancy version for all TBs – 1 bit. If Repetition number is > 1 and frequency hopping is enabled by higher layers then this bit is a Frequency hopping flag for the TBs, and the redundancy version for all TBs starts at 0.

-Resource reservation – 1 bit as defined in clause 8.0 of [3]. This field is only present if UL resource reservation is enabled for the UE as specified in [6] and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

If ce-PUSCH-MultiTB-Config is not enabled and the Resource block assignment in format 6-0A is set to all ones, or ce-PUSCH-MultiTB-Config is enabled and mpdcch-UL-HARQ-ACK-FeedbackConfig is configured and the 6 MSB bits of the Scheduling TBs for Unicast Field are set to '110111', format 6-0A is used for the indication of ACK feedback. 8 bits including the 6 LSB bits of the Scheduling TBs for Unicast Field and 2 MSB bits of Repetition number are used to indicate HARQ-ACK by bitmap, where the order of the bitmap to HARQ process index mapping is such that HARQ process indices are mapped in ascending order from MSB to LSB of the bitmap. For each bit of the bitmap, value 1 indicates ACK, and value 0 is reserved. And all the remaining bits except Flag format 6-0A/format 6-1A differentiation and DCI subframe repetition number are set to zero.

If the number of information bits in format 6-0A mapped onto a given search space is less than the payload size of format 6-1A for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 6-1A), zeros shall be appended to format 6-0A until the payload size equals that of format 6-1A.

## 5.3.3.1.11Format 6-0B

DCI format 6-0B is used for the scheduling of PUSCH in one UL cell, for the indication of ACK feedback, and operation on preconfigured UL resources.

The following information is transmitted by means of the DCI format 6-0B:

-Flag for format 6-0B/format 6-1B differentiation – 1 bit, where value 0 indicates format 6-0B and value 1 indicates format 6-1B

-Flag for sub-PRB resource allocation – 1 bit, where value 1 indicates the format 6-0B DCI uses sub-PRB resource allocation and value 0 indicates the format 6-0B DCI does not use sub-PRB resource allocation. This field is present when ce-PUSCH-SubPRB-Config is configured by higher layers and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3], or when the DCI is mapped onto the UE-specific search space given by PUR-RNTI as defined in [3] and the UE is configured with higher layer parameter subPRB-Allocation = 'true'.

-Modulation and coding scheme – 4 bits as defined in clause 8.6 of [3]. The field is only present if format 6-0B CRC is scrambled by PUR-RNTI and for not sub-PRB resource allocation.

-Resource block assignment – The field is not present if format 6-0B CRC is scrambled by PUR-RNTI and Modulation and coding scheme is set to all ones for not sub-PRB resource allocation.

-If the flag for sub-PRB resource allocation is set to 1:

-+4 bits for PUSCH as defined in [3]

- MSB bits provide the narrowband index as defined in clause 5.2.4 of [2]

-4 bits provide the resource allocation within the indicated narrowband using UL resource allocation type 5 as defined in clause 8.1.6 of [3]

-Otherwise, +3 bits for PUSCH as defined in [3]:

- MSB bits provide the narrowband index as defined in clause 5.2.4 of [2]

-3 bits provide the resource allocation within the indicated narrowband as specified in clause 8.1.3 of [3]

If format 6-0B CRC is scrambled by PUR-RNTI and Resource block assignment is set to all ones for sub-PRB resource allocation or Modulation and coding scheme is set to all ones for not sub-PRB resource allocation, the remaining fields are set as follows:

-ACK or Fallback indicator – 1 bit, where value 0 indicates ACK and value 1 indicates fallback as defined in clause 9.1.5.3 of [3]

-PUSCH repetition adjustment – 3 bits, this field refers to indices n1, n2, …, n8 in Table 8-2c of [3]

-Timing advance adjustment – 6 bits as defined in clause 4.2.3 of [3]. The field is only present if ACK or Fallback indicator is set to 0.

-All the remaining bits in format 6-0B are set to zero

Otherwise

-Modulation and coding scheme – 3 or 4 bits as defined in clause 8.6 of [3]. The 3-bit field applies when the flag for sub-PRB resource allocation is present and set to 1, otherwise the 4-bit field applies. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3], or if format 6-0B CRC is scrambled by PUR-RNTI and for not sub-PRB resource allocation.

-Number of resource units – 1 bit as defined in clause 8.1.6 of [3]. This field is present when the flag for sub-PRB resource allocation is present and is reserved when the flag for sub-PRB resource allocation is set to 0.

-Repetition number – 3 bits as defined in clause 8.0 of [3]

-HARQ process number – 1 bit. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-New data indicator – 1 bit. The field is not present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-DCI subframe repetition number – 2 bits as defined in clause 9.1.5 of [3]

-Scheduling TBs for Unicast – 10 bits. This field is only present if ce-PUSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-If one TB is scheduled

-3 bits set to zero

-Modulation and coding scheme – 4 bits

-HARQ process number – 2 bits

-New data indicator – 1 bit

-If two TBs are scheduled

-1 bit set to zero

-Modulation and coding scheme with offset – 4 bits provide the Modulation and coding scheme + offset, with an offset of +3

-HARQ index – 3 bits provide the HARQ index as defined in 8.0 of [3]

-New data indicators – 2 bits, one for each scheduled TB in increasing order of HARQ process ID

-If three TBs are scheduled

-Modulation and coding scheme with offset – 5 bits provide the Modulation and coding scheme + offset, with an offset of +15

-HARQ index – 2 bits provide the HARQ index as defined in 8.0 of [3]

-New data indicators – 3 bits, one for each scheduled TB in increasing order of HARQ process ID

-If four TBs are scheduled

-Modulation and coding scheme with offset – 6 bits provide the Modulation and coding scheme + offset, with an offset of +52

-New data indicators – 4 bits, one for each scheduled TB in increasing order of HARQ process ID

-Resource reservation – 1 bit as defined in clause 8.0 of [3]. This field is only present if UL resource reservation is enabled for the UE as specified in [6] and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

If ce-PUSCH-MultiTB-Config is not enabled and the Modulation and coding scheme in format 6-0B is 4 bits and set to all ones, or ce-PUSCH-MultiTB-Config is enabled and mpdcch-UL-HARQ-ACK-FeedbackConfig is configured and the 6 MSB bits of the Scheduling TBs for Unicast Field are set to '111111', format 6-0B is used for the indication of ACK feedback. 4 LSB bits of the Scheduling TBs for Unicast Field are used to indicate 4 HARQ-ACK by bitmap, where the order of the bitmap to HARQ process index mapping is such that HARQ process indices are mapped in ascending order from MSB to LSB of the bitmap. For each bit of the bitmap, value 1 indicates ACK, and value 0 is reserved. And all the remaining bits except Flag for format 6-0B/format 6-1B differentiation and DCI subframe repetition number are set to zero.

If the number of information bits in format 6-0B mapped onto a given search space is less than the payload size of format 6-1B for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 6-1B), zeros shall be appended to format 6-0B until the payload size equals that of format 6-1B.

## 5.3.3.1.12Format 6-1A

DCI format 6-1A is used for the scheduling of one PDSCH codeword per TTI in one cell, random access procedure initiated by a PDCCH order, notifying SC-MCCH change, operation on preconfigured UL resources, and direct indication. The DCI corresponding to a PDCCH order can be carried by MPDCCH.

The following information is transmitted by means of the DCI format 6-1A:

Format 6-1A is used for direction indication only if the DCI CRC is scrambled by SI-RNTI and ce-ETWS-CMAS-RxInConn is configured by higher layers, and all the remaining fields are set as follows:

-Direct Indication information – 8 bits provide direct indication of fields, as defined in [6]

-Zeros are added until the size is equal to that of format 6-1A scrambled with C-RNTI when format 6-1A is mapped onto the common search space

Otherwise,

-Flag format 6-0A/format 6-1A differentiation – 1 bit, where value 0 indicates format 6-0A and value 1 indicates format 6-1A

Format 6-1A is used for random access procedure initiated by a PDCCH order only if format 6-1A CRC is scrambled with C-RNTI and all the remaining fields are set as follows:

-Resource block assignment – +5 bits, where all bits shall be set to 1

-Preamble Index – 6 bits

-PRACH Mask Index – 4 bits, [5]

-Starting CE level – 2 bits provide the PRACH starting CE level as defined in [5]

-All the remaining bits in format 6-1A for compact scheduling assignment of one PDSCH codeword are set to zero

Otherwise,

-Frequency hopping flag – 1 bit, where value 0 indicates frequency hopping is not enabled and value 1 indicates frequency hopping is enabled as defined in clause 6.4.1 of [2]. If the UE is configured with 64QAM for PDSCH and the repetition number field indicates no PDSCH repetition, this field is the MSB bit of the extended Modulation and coding scheme field, as specified in Table 7.1.7.1-1 of [3]. The field is not present if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Resource block assignment flag – 1 bit. This field is only present when the higher layer parameter ce-pdsch-maxBandwidth-config is configured and set to 20 MHz and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3].

-Resource block assignment –

-If ce-pdsch-maxBandwidth-config is set to 5 MHz or mpdcch-PDSCH-MaxBandwidth-SC-MTCH is set to 24 PRBs or the resource block assignment flag is set to 1, and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3],

-If ,  bits for PDSCH as defined in [3]:

- MSB bits provide the starting narrowband index as defined in clause 6.2.7 of [2]

-3 bit bitmap provides additional allocated narrowbands among the three narrowbands following the starting narrowband. The order of the bitmap to narrowband index mapping is such that the first narrowband after the starting narrowband to the third narrowband after the starting narrowband are mapped to MSB to LSB of the bitmap.

-5 bits provide the same resource allocation using DL resource allocation type 2 within each of the allocated narrowbands.

-Else if  , + 5 bits for PDSCH as defined below:

- MSB bits provide a bitmap of allocated narrowbands. The order of the bitmap to narrowband index mapping is such that narrowband index  to are mapped to MSB to LSB of the bitmap.

-5 bits provide the same resource allocation using DL resource allocation type 2 within each of the allocated narrowbands

-Otherwise, 5 bits for PDSCH as defined below:

-5 bits provide resource allocation using DL resource allocation type 2

-Else if the resource block assignment flag is set to 0:

- bits provide the RBG bitmap as defined in clause 7.1.6.1 of [3], where S = 9 if  and S = 6 otherwise

-Reserved information bits are added until the size is equal to the size of the resource block assignment with resource block assignment flag is set to 1

-Otherwise, +5 bits for PDSCH as defined in [3]:

- MSB bits provide the narrowband index as defined in clause 6.2.7 of [2]

-5 bits provide the resource allocation using DL resource allocation type 2 within the indicated narrowband

-Modulation and coding scheme – 4 bits as defined in clause 7.1.7 of [3]

-Repetition number – 2 bits as defined in clause 7.1.11 of [3]

-Number of scheduled TB for SC-MTCH – 3 bits, indicating from 1 to 8 TBs. This field is only present if higher layer parameter sc-MTCH-InfoList-MultiTB-r16 is enabled and the CRC of the DCI is scrambled by G-RNTI.

-HARQ process number – 3 bits (for cases with FDD primary cell), 4 bits (for cases with TDD primary cell, or for cases with FDD primary cell when ce-pdsch-tenProcesses-config or ce-PDSCH-14HARQ-Config is configured by higher layers and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3]). This field is not present when the format 6-1A CRC is scrambled with G-RNTI, or if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-New data indicator – 1 bit. This field is not present when the format 6-1A CRC is scrambled with G-RNTI, or if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Redundancy version – 2 bits. The field is not present if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-TPC command for PUCCH – 2 bits as defined in clause 5.1.2.1 of [3] . This field is not present when the format 6-1A CRC is scrambled with G-RNTI.

-If the format 6-1A CRC is scrambled by RA-RNTI:

-The most significant bit of the TPC command is reserved.

-The least significant bit of the TPC command indicates column of the TBS table defined of [3].

-If least significant bit is 0 then = 2 else = 3.

-Else

-The two bits including the most significant bit indicate the TPC command

-Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2. This field is reserved when ce-PDSCH-MultiTB-Config is enabled and multiple TBs are scheduled, or when the configured maximum repetition number is larger than 1 for MPDCCH, and not present when the format 6-1A CRC is scrambled with G-RNTI, or when the higher layer parameter csi-NumRepetitionCE-r13 indicates more than one subframe.

-Antenna port(s) and scrambling identity – 2 bits indicating the values 0 to 3, as specified in Table 5.3.3.1.5C-1. This field is present only if PDSCH transmission is configured with TM9 for DCI formats scheduling PDSCH which are mapped onto the UE specific search space given by the C-RNTI as defined in [3].

-SRS request –1 bit. The interpretation of this field is provided in clause 8.2 of [3]

-TPMI information for precoding – number of bits as specified in Table 5.3.3.1.3A-1.

-TPMI information indicates which codebook index is used in Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 of [2] corresponding to the single-layer transmission. This field is present only if PDSCH transmission is configured with TM6 for DCI formats scheduling PDSCH which are mapped onto the UE specific search space given by the C-RNTI as defined in [3].

-PMI confirmation for precoding – 1 bit as specified in Table 5.3.3.1.3A-2. This field is present only if PDSCH transmission is configured with TM6 for DCI formats scheduling PDSCH which are mapped onto the UE specific search space given by the C-RNTI as defined in [3].

-HARQ-ACK resource offset – 0 or 2 bits as defined in clause 10.1 of [3] (this field is 0 bits if Information for SC-MCCH change notification is present)

-Information for SC-MCCH change notification – 2 bits as defined in clause 5.8a of [6] (this field is present if the format 6-1A CRC is scrambled with G-RNTI)

-DCI subframe repetition number – 0 or 2 bits as defined in clause 9.1.5 of [3] (this field is 0 bits if Transport blocks in a bundle is present)

-Transport blocks in a bundle – 0 or 2 bits, where 2 bits indicate from 1 to 4 transport blocks in a bundle (this field is 2 bits when DCI Field "HARQ-ACK bundling flag" is set to 1, and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3]; otherwise this field is 0 bits).

-HARQ-ACK bundling flag – 1 bit, where value 0 indicates HARQ-ACK bundling is not enabled and value 1 indicates HARQ-ACK bundling is enabled as defined in clause 7.3 of [3]. This field is only present when the higher layer parameter ce-HarqAckBundling-config is configured and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3].

-HARQ-ACK delay – 3 bits as defined in 7.3 of [3]. This field is only present when the higher layer parameter ce-schedulingEnhancement-config or ce-HarqAckBundling-config is configured and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3] and the field "PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ" is not present.

-PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ – 5 or 7 bits as defined in Table 5.3.3.1.12-1 and Table 5.3.3.1.12-2. This field is only present when the higher layer parameter ce-PDSCH-14HARQ-Config is configured and the DCI is mapped onto the UE-specific search space given by the C-RNTI as defined in [3]. The field is 5 bits when ce-HARQ-AckDelay is Alt-2e and 7 bits when ce-HARQ-AckDelay is Alt-1.

-Multi-TB HARQ-ACK bundling size – 2 bits as defined in 7.3 of [3]. This field is only present if higher layer parameter ce-PDSCH-MultiTB-Config is configured as enabled and higher layer parameter harq-AckBundling is configured and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Scheduling TBs for Unicast – 12 bits. This field is only present if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3]. This field schedules one TB if the CRC of the DCI is scrambled by SPS C-RNTI.

-If one TB is scheduled

-5 bits set to zero

-HARQ process number – 3 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-Frequency hopping flag – 1 bit, where value 0 indicates frequency hopping is not enabled and value 1 indicates frequency hopping is enabled as defined in clause 6.4.1 of [2]. If the UE is configured with 64QAM for PDSCH and the repetition number field indicates no PDSCH repetition, this field is the MSB bit of the extended Modulation and coding scheme field, as specified in Table 7.1.7.1-1 of [3]. If the UE is not configured with 64QAM for PDSCH and frequency hopping is not enabled by higher layers, this field is set to 0.

-If two TBs are scheduled

-2 bits set to zero

-HARQ index with offset – 6 bits provide the HARQ index + offset, with an offset of +8 and HARQ index as defined in 7.1.7.2 of [3]

-New data indicators – 2 bits, one for each scheduled TB in increasing order of HARQ process ID

-Redundancy version for TB 1 – 1 bit

-Redundancy version for TB 2 – 1 bit. If the UE is configured with 64QAM for PDSCH and the repetition number field indicates no PDSCH repetition then this bit is the MSB bit of the extended Modulation and coding scheme field. If Repetition number is > 1 and frequency hopping is enabled by higher layers then this bit is a Frequency hopping flag for the TBs. In these cases TB2 uses the redundancy version for TB1.

-If four TBs are scheduled

-1 bit set to zero

-HARQ index with offset – 7 bits provide the HARQ index + offset, with an offset of +36 and HARQ index as defined in 7.1.7.2 of [3]

-New data indicators – 4 bits, one for each scheduled TB in increasing order of HARQ process ID

-If six TBs are scheduled

-HARQ index with offset – 6 bits provide the HARQ index + offset, with an offset of +27 and HARQ index as defined in 7.1.7.2 of [3]

-New data indicators – 6 bits, one for each scheduled TB in increasing order of HARQ process ID

-If eight TBs are scheduled

-3 bits set to one

-New data indicators – 8 bits, one for each scheduled TB in increasing order of HARQ process ID

-Redundancy version for all TBs – 1 bit. If the UE is configured with 64QAM for PDSCH and the repetition number field indicates no PDSCH repetition then this bit is the MSB bit of the extended Modulation and coding scheme field. If Repetition number is > 1 and frequency hopping is enabled by higher layers then this bit is a Frequency hopping flag for the TBs. In these cases the redundancy version for all TBs starts at 0.

-Multi-TB HARQ processes group – 1 bit, where value 0 indicates that the Scheduling TBs for Unicast Field applies to the first group of 8 HARQ process and value 1 indicates the second group. This field is only present for TDD operation with more than 8 maximum processes and if the Scheduling TBs for Unicast Field is present.

-Resource reservation – 1 bit as defined in clause 7.1 of [3]. This field is only present if DL resource reservation is enabled for the UE as specified in [6] and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

When the format 6-1A CRC is scrambled with a RA-RNTI or a CB-RNTI, then the following fields among the fields above are reserved:

-HARQ process number

-New data indicator

-Downlink Assignment Index

-HARQ-ACK resource offset

If the UE is not configured to decode MPDCCH with CRC scrambled by the C-RNTI or PUR-RNTI, and the format 6-1A CRC is not scrambled with a G-RNTI, and the number of information bits in format 6-1A is less than that of format 6-0A, zeros shall be appended to format 6-1A until the payload size equals that of format 6-0A.

If the UE is configured to decode MPDCCH with CRC scrambled by the C-RNTI or PUR-RNTI, and the format 6-1A CRC is not scrambled with a G-RNTI, and the number of information bits in format 6-1A mapped onto a given search space is less than that of format 6-0A for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 6-1A until the payload size equals that of format 6-0A.

Table 5.3.3.1.12-1: Content of "PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ" for ce-HARQ-AckDelay = Alt-2e

Table 5.3.3.1.12-2: Content of "PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ" for ce-HARQ-AckDelay = Alt-1

Table 5.3.3.1.12-3: PDSCH scheduling delay options

## 5.3.3.1.13Format 6-1B

DCI format 6-1B is used for the scheduling of one PDSCH codeword per TTI in one cell, notifying SC-MCCH change, operation on preconfigured UL resources, and direct indication.

The following information is transmitted by means of the DCI format 6-1B:

Format 6-1B is used for direction indication only if the DCI CRC is scrambled by SI-RNTI and ce-ETWS-CMAS-RxInConn is configured by higher layers, and all the remaining fields are set as follows:

-Direct Indication information – 8 bits provide direct indication of fields, as defined in [6]

-Zeros are added until the size is equal to 14+   +1 bits

Otherwise,

-Flag for format 6-0B/format 6-1B differentiation – 1 bit, where value 0 indicates format 6-0B and value 1 indicates format 6-1B

Format 6-1B is used for random access procedure initiated by a PDCCH order only if format 6-1B CRC is scrambled with C-RNTI and all the remaining fields are set as follows:

-Reserved bits – +2 bits, where all bits shall be set to 1

-Preamble Index – 6 bits

-PRACH Mask Index – 4 bits [5]

-Starting CE level – 2 bits provide the PRACH starting CE level as defined in [5]

-All the remaining bits in format 6-1B for compact scheduling assignment of one PDSCH codeword are set to zero

Otherwise,

-Modulation and coding scheme – 4 bits as defined in clause 7.1.7 of [3] . The field is not present if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-Resource block assignment –

-If ce-pdsch-maxBandwidth-config is set to 5 MHz or mpdcch-PDSCH-MaxBandwidth-SC-MTCH is set to 24 PRBs,

-If ,  bits for PDSCH as defined in [3]:

- MSB bits provide the wideband index as defined in clause 6.2.7 of [2]

-4 bits provide a narrowband bitmap for resource allocation within the indicated wideband

-Otherwise, bits for PDSCH as defined below:

-if = 1, 1 bit provides the resource allocation within the narrowband, where value 0 indicates RBs with PRB index {0, 1, 2, 3} and value 1 indicates that all 6 PRBs are used.

-Otherwise, bits provide allocated narrowbands

-Else if ce-pdsch-maxBandwidth-config is set to 20 MHz,

-If ,  bits for PDSCH as defined in [3]:

- bits provide a wideband combination index as defined in clause 7.1.6 of [3]

-4 bits provide a narrowband bitmap for resource allocation within each indicated wideband

-Otherwise,  bits for PDSCH as defined in [3]:

-If = 1, 1 bit provides the resource allocation within the narrowband, where value 0 indicates RBs with PRB index {0, 1, 2, 3} and value 1 indicates that all 6 PRBs are used.

-Otherwise,  bits provide a narrowband bitmap for resource allocation

-Otherwise, +1 bits for PDSCH as defined in [3]:

- MSB bits provide the narrowband index as defined in clause 6.2.7 of [2]

-1 bit provides the resource allocation within the indicated narrowband, where value 0 indicates RBs with PRB index {0, 1, 2, 3} and value 1 indicates that all 6 PRBs are used.

-Repetition number – 3 bits as defined in clause 7.1.11 of [3]

-Number of scheduled TB for SC-MTCH – 3 bits, indicating from 1 to 8 TBs. This field is only present if higher layer parameter sc-MTCH-InfoList-MultiTB-r16 is enabled and the CRC of the DCI is scrambled by G-RNTI.

-HARQ process number – 1 bit. This field is not present when the format 6-1B CRC is scrambled with G-RNTI, or if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-New data indicator – 1 bit. This field is not present when the format 6-1B CRC is scrambled with G-RNTI, or if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-HARQ-ACK resource offset – 0 or 2 bits as defined in clause 10.1 of [3] (this field is 0 bits if Information for SC-MCCH change notification is present). If downlinkHARQ-FeedbackDisabledDCI is configured, or if downlinkHARQ-FeedbackDisabledBitmap and downlinkHARQ-FeedbackDisabledDCI are configured, and the value is ‘3’, it functions as a HARQ feedback disabled indicator as defined in clause 7.3 of [3].

-Information for SC-MCCH change notification – 2 bits as defined in clause 5.8a of [6] (this field is present if the format 6-1B CRC is scrambled with G-RNTI)

-DCI subframe repetition number –2 bits as defined in clause 9.1.5 of [3]

-Scheduling TBs for Unicast – 10 bits. This field is only present if ce-PDSCH-MultiTB-Config is enabled and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

-If one TB is scheduled

-3 bits set to zero

-Modulation and coding scheme – 4 bits

-HARQ process number – 2 bits

-New data indicator – 1 bit

-If two TBs are scheduled

-1 bit set to zero

-Modulation and coding scheme with offset – 4 bits provide the Modulation and coding scheme + offset, with an offset of +3

-HARQ index – 3 bits provide the HARQ index as defined in 7.1.7.2 of [3]

-New data indicators – 2 bits, one for each scheduled TB in increasing order of HARQ process ID

-If three TBs are scheduled

-Modulation and coding scheme with offset – 5 bits provide the Modulation and coding scheme + offset, with an offset of +15

-HARQ index – 2 bits provide the HARQ index as defined in 7.1.7.2 of [3]

-New data indicators – 3 bits, one for each scheduled TB in increasing order of HARQ process ID

-If four TBs are scheduled

-Modulation and coding scheme with offset – 6 bits provide the Modulation and coding scheme + offset, with an offset of +52

-New data indicators – 4 bits, one for each scheduled TB in increasing order of HARQ process ID

-Resource reservation – 1 bit as defined in clause 7.1 of [3]. This field is only present if DL resource reservation is enabled for the UE as specified in [6] and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

When the format 6-1B CRC is scrambled with a RA-RNTI then the following fields among the fields above are reserved:

-HARQ process number

-New data indicator

-HARQ-ACK resource offset

If the UE is not configured to decode MPDCCH with CRC scrambled by the C-RNTI or PUR-RNTI, and the format 6-1B CRC is not scrambled with a G-RNTI, and the number of information bits in format 6-1B is less than that of format 6-0B, zeros shall be appended to format 6-1B until the payload size equals that of format 6-0B.

If the UE is configured to decode MPDCCH with CRC scrambled by the C-RNTI or PUR-RNTI, and the format 6-1B CRC is not scrambled with a G-RNTI, and the number of information bits in format 6-1B mapped onto a given search space is less than that of format 6-0B for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 6-1B until the payload size equals that of format 6-0B.

## 5.3.3.1.14Format 6-2

DCI format 6-2 is used for paging, direct indication, scheduling of one PDSCH codeword carrying SC-MCCH in one cell, and notifying SC-MCCH change.

The following information is transmitted by means of the DCI format 6-2:

-If the format 6-2 CRC is scrambled by P-RNTI:

-Flag for paging/direct indication differentiation – 1 bit, with value 0 for direct indication and value 1 for paging

-Else if the format 6-2 CRC is scrambled by a SC-RNTI:

-Information for SC-MCCH change notification – 1 bit as defined in clause 5.8a of [6]

-If the format 6-2 CRC is scrambled by P-RNTI and Flag=0:

-Direct Indication information – 8 bits provide direct indication of system information update and other fields, as defined in [6]

-Reserved information bits are added until the size is equal to that of format 6-2 with Flag=1

-If the format 6-2 CRC is scrambled by P-RNTI and Flag=1, or if the format 6-2 CRC is scrambled by SC-RNTI:

-Resource block assignment –  bits for the narrowband index as defined in clause 7.1.6 of [3]

-Modulation and coding scheme – 3 bits as defined in clause 7.1.7 of [3]

-Repetition number – 3 bits as defined in clause 7.1.11 of [3]

-DCI subframe repetition number – 2 bits as defined in clause 9.1.5 of [3]

## 5.3.3.1.15Format 7-0A

DCI format 7-0A is used for the scheduling of PUSCH with slot or subslot duration in one UL cell.

The following information is transmitted by means of the DCI format 7-0A:

-Flag for UL/DL differentiation – 1 bit, where value 0 indicates format 7-0A and value 1 indicates format 7-1A/B/C/D/E/F/G depending on the configured downlink transmission mode

-Resource block assignment –  bits provide the resource allocation in the UL slot or subslot as defined in clause 8.1.1 of [3], where  if , and  otherwise.(log2(NRBUL/P(NRBUL/P+1)/2))P=4NRBUL>15P=1

-Modulation and coding scheme – 5 bits as defined in clause 8.6 of [3]

-HARQ process number – 4 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-DMRS pattern – 2 bits as defined in clause 5.5.2.1.2 in [2] (The field is present only for PUSCH with subslot duration)

-Cyclic shift for DMRS and IFDMA configuration – 1 bit as defined in clause 5.5.2.1.1 of [2]

-UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0, or TDD operation with uplink-downlink configuration 6 and special subframe configuration 0, 5, 9 or 10)

-Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (this field is present only for cases with TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation)

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]:

The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 3-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 1-bit field applies

-SRS request – 0 or 1 bit as defined in clause 8.2 of [3] (this field is present only for TDD operation, if the UE has indicated the capability srs-DCI7-Triggering-FS2-r15 and the UE is configured with higher layer parameter srs-DCI7-TriggeringConfig-r15)

-Beta offet indicator – 1 bit as defined in clause 8.6.3 of [3] (this field is present only if UE is configured with ul-STTI-Length=subslot).

-Cyclic Shift Field mapping table for DMRS – 1 bit as defined in clause 5.5.2.1.1 of [2].

If the number of information bits in format 7-0A mapped onto a given search space is less than the payload size of format 7-1A/B/C/D/E/F/G depending on the configured downlink transmission mode for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 7-1A/B/C/D/E/F/G), zeros shall be appended to format 7-0A until the payload size equals that of format 7-1A/B/C/D/E/F/G.

If the number of information bits in format 7-0A carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-0A until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.16Format 7-0B

DCI format 7-0B is used for the scheduling of PUSCH with slot or subslot duration in one UL cell with multi-antenna port transmission mode.

The following information is transmitted by means of the DCI format 7-0B:

-Flag for UL/DL differentiation – 1 bit, where value 0 indicates format 7-0B and value 1 indicates format 7-1A/B/C/D/E/F/G depending on the configured downlink transmission mode

-Resource block assignment –  bits provide the resource allocation in the UL slot or subslot as defined in clause 8.1.1 of [3], where  if , and  otherwise.(log2(NRBUL/P(NRBUL/P+1)/2))P=4NRBUL>15P=1

-Modulation and coding scheme – 5 bits as defined in clause 8.6 of [3]

-HARQ process number – 4 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-TPC command for scheduled PUSCH – 2 bits as defined in clause 5.1.1.1 of [3]

-DMRS pattern – 2 bits as defined in clause 5.5.2.1.2 in [2] (The field is present only for PUSCH with subslot duration)

-Cyclic shift for DMRS and IFDMA configuration – 1 bit as defined in clause 5.5.2.1.1 of [2]

-UL index – 2 bits as defined in clauses 5.1.1.1, 7.2.1, and 8 of [3] (this field is present only for TDD operation with uplink-downlink configuration 0, or TDD operation with uplink-downlink configuration 6 and special subframe configuration 0, 5, 9 or 10)

-Downlink Assignment Index (DAI) – 2 bits as defined in clause 7.3 of [3] (this field is present only for cases with TDD primary cell and either TDD operation with uplink-downlink configurations 1-6 or FDD operation)

-CSI request – 1, 2 or 3 bits as defined in clause 7.2.1 of [3]:

The 2-bit field applies to UEs configured with no more than five DL cells and to

-UEs that are configured with more than one DL cell;

-UEs that are configured by higher layers with more than one CSI process;

-UEs that are configured with two CSI measurement sets by higher layers with the parameter csi-MeasSubframeSet;

the 3-bit field applies to UEs that are configured with more than five DL cells;

otherwise the 1-bit field applies

-SRS request – 2 bits as defined in clause 8.2 of [3] (this field is present only for TDD operation, if the UE has indicated the capability srs-DCI7-Triggering-FS2-r15 and the UE is configured with higher layer parameter srs-DCI7-TriggeringConfig-r15)

-Beta offet indicator – 1 bit as defined in clause 8.6.3 of [3] (this field is present only if UE is configured with ul-STTI-Length=subslot).

-Cyclic Shift Field mapping table for DMRS – 1 bit as defined in clause 5.5.2.1.1 of [2].

-Precoding information and number of layers: number of bits as specified in Table 5.3.3.1.8-1. Bit field are shown in Table 5.3.3.1.16-1 and Table 5.3.3.1.16- 2. Note that TPMI for 2 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-1 of [2], and TPMI for 4 antenna ports indicates which codebook index is to be used in Table 5.3.3A.2-2, Table 5.3.3A.2-3, Table 5.3.3A.2-4 and Table 5.3.3A.2-5 of [2].

Table 5.3.3.1.16-1: Content of precoding information field for 2 antenna ports

Table 5.3.3.1.16-2: Content of precoding information field for 4 antenna ports

If the number of information bits in format 7-0B mapped onto a given search space is less than the payload size of format 7-1A/B/C/D/E/F/G depending on the configured downlink transmission mode for scheduling the same serving cell and mapped onto the same search space (including any padding bits appended to format 7-1A/B/C/D/E/F/G), zeros shall be appended to format 7-0B until the payload size equals that of format 7-1A/B/C/D/E/F/G.

If the number of information bits in format 7-0B carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-0B until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.17Format 7-1A

DCI format 7-1A is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1A:

-Flag for DL/UL differentiation – 1 bit, where value 0 indicates format 7-0A/B depending on the configured uplink transmission mode and value 1 indicates the DL DCI format

-For resource allocation type 0 as defined in clause 7.1.6.1 of [3]:

-bits provide the resource allocation

where the value of P depends on the number of DL resource blocks as indicated in clause 7.1.6.1 of [3]

-For resource allocation type 2 as defined in clause 7.1.6.3 of [3]:

-bits provide the resource allocation

-one additional bit if

where  is defined in clause 7.1.6.3 of [3]

-Modulation and coding scheme – 5 bits as defined in clause 7.1.7 of [3]. The MSB is set to 0 when the UE is configured with blindSlotSubslotPDSCH-Repetitions set to TRUE and the repetition number is greater than 1 and the higher layer parameter mcs-restrictionSlotSubslotPDSCH-Repetitions is configured to 1.

-HARQ process number – 4 bits

-New data indicator – 1 bit

-Redundancy version – 2 bits

-TPC command for slot-SPUCCH or subslot-SPUCCH – 2 bits as defined in clause 5.1.2.1 of [3]

-Downlink Assignment Index – number of bits as specified in Table 5.3.3.1.2-2

-Used/Unused SPDCCH resource indication – 2 bits (This field is present if the DCI is mapped to SPDCCH and L1-based reuse indication is configured by higher layers)

-SPUCCH resource indication – 2 bit as defined in clause 10.1.2 of [3].

-Repetition number – 2 bits as defined in Table 5.3.3.1.17-1, where the number of transmissions for PDSCH is given by higher layer parameter maxNumber-SlotSubslotPDSCH-Repetitions for the value of '11'. This field is present only when the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions set to TRUE.

Table 5.3.3.1.17-1: Content of repetition number field

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1A mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1A until the payload size equals that of format 7-0A/B, except when format 7-1A assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1A carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1A until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.18Format 7-1B

DCI format 7-1B is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1B:

-The fields of format 7-1A

-Precoding information –1 bit for transmission with 2 antenna ports and 2 bits for transmission with 4 antenna ports.

For transmission with 4 antenna ports, the precoding information field is defined according to Table 5.3.3.1.18-1. For transmission with 2 antenna ports, the number of transmission layers is equal to 2 if precoding information is 1; transmit diversity is used if precoding information is 0.

Table 5.3.3.1.18-1: Content of precoding information field for 4 antenna ports

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1B mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1B until the payload size equals that of format 7-0A/B, except when format 7-1B assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1B carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1B until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.19Format 7-1C

DCI format 7-1C is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1C:

-The fields of format 7-1A

-Precoding information – 4 bits for 2 antenna ports and 6 bits for 4 antenna ports.

The precoding information field is defined in Table 5.3.3.1.19-1 and Table 5.3.3.1.19-2. Note that TPMI indicates which codebook index is used in Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 of [2].

Some entries in Table 5.3.3.1.5-4 and Table 5.3.3.1.5-5 are used for indicating that the eNodeB has applied precoding according to PMI(s) reported by the UE. In these cases the precoding for the corresponding RB(s) in slot/subslot n is according to the latest PMI(s) in an aperiodic CSI reported on or before slot n-4 if higher layer parameter ul-STTI-Length is configured as slot, or subslot n-k if higher layer parameter ul-STTI-Length is configured as subslot, where k is the minimum processing timing configured in higher layer parameter min-proc-TimelineSubslot. For aperiodic CSI mode 2-2: Precoding of scheduled resource blocks belonging to the reported preferred M subband(s) use precoder(s) according to the preferred M subband PMI indicated by the latest aperiodic CSI report; Precoding of scheduled resource blocks not belonging to the reported preferred M subband(s) use a precoder according to the wideband PMI indicated by the latest aperiodic CSI report.

Table 5.3.3.1.19-1: Content of precoding information field for 2 antenna ports

Table 5.3.3.1.19-2: Content of precoding information field for 4 antenna ports

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1C mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1C until the payload size equals that of format 7-0A/B, except when format 7-1C assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1C carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1C until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.20Format 7-1D

DCI format 7-1D is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1C:

-The fields of format 7-1A

-Precoding information – number of bits as the value specified in Table 5.3.3.1.3A-1 plus one

The precoding information field is defined in Table 5.3.3.1.20-1 and Table 5.3.3.1.20-2.

Table 5.3.3.1.20-1: Content of precoding information field for 2 antenna ports

Table 5.3.3.1.20-2: Content of precoding information field for 4 antenna ports

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1D mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1D until the payload size equals that of format 7-0A/B, except when format 7-1D assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1D carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1D until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.21Format 7-1E

DCI format 7-1E is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1E:

-The fields of format 7-1A

-SRS request – 0 or 1 bit as defined in clause 8.2 of [3] (this field is present only for TDD operation, if the UE has indicated the capability srs-DCI7-Triggering-FS2-r15 and the UE is configured with higher layer parameter srs-DCI7-TriggeringConfig-r15)

-Scrambling identity– 1 bit as defined in clause 6.10.3.1 of [2]

-Precoding information – 2 bits as specified in Table 5.3.3.1.21-1.

Table 5.3.3.1.21-1: Content of precoding information field

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1E mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1E until the payload size equals that of format 7-0A/B, except when format 7-1E assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1E carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1E until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.22Format 7-1F

DCI format 7-1F is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1F:

-The fields of format 7-1A

-SRS request – 0 or 1 bit as defined in clause 8.2 of [3] (this field is present only for TDD operation, if the UE has indicated the capability srs-DCI7-Triggering-FS2-r15 and the UE is configured with higher layer parameter srs-DCI7-TriggeringConfig-r15)

-DMRS position indicator – 1 bit, where the value 0 indicates the presence of DMRS and the value 1 indicates the absence of DMRS. (The field is present only if UE is configured with dl-STTI-Length=subslot). This field is set to 0 when the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions set to TRUE and the repetition number is greater than 1.

-Antenna port(s), scrambling identity and number of layers – 3 bits as specified in Table 5.3.3.1.22-2 if the UE is higher layer configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10, Table 5.3.3.1.22-3 if the UE is higher layer configured with slotSubslotPDSCH-TXDiv-4layer-TM9/10, or Table 5.3.3.1.22-1 otherwise, where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2], or 1 bit as specified in Table 5.3.3.1.5C-6 where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2] when higher layer parameter semiOpenLoop-STTI is configured.

When higher layer parameter semiOpenLoop-STTI is configured, antenna ports 7 and 8 are used for transmit diversity.

Table 5.3.3.1.22-1: Antenna port(s), scrambling identity and number of layers indication

Table 5.3.3.1.22-2: Antenna port(s), scrambling identity and number of layers indication if the UE is configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10

Table 5.3.3.1.22-3: Antenna port(s), scrambling identity and number of layers indication if the UE is configured with slotSubslotPDSCH-TXDiv-4layer-TM9/10

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1F mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1F until the payload size equals that of format 7-0A/B, except when format 7-1F assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1F carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1F until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.1.23Format 7-1G

DCI format 7-1G is used for the scheduling of one PDSCH codeword with slot or subslot duration in one cell.

The following information is transmitted by means of the DCI format 7-1G:

-The fields of format 7-1A

-SRS request – 0 or 1 bit as defined in clause 8.2 of [3] (this field is present only for TDD operation, if the UE has indicated the capability srs-DCI7-Triggering-FS2-r15 and the UE is configured with higher layer parameter srs-DCI7-TriggeringConfig-r15)

-DMRS position indicator – 1 bit, where the value 0 indicates the presence of DMRS and the value 1 indicates the absence of DMRS. (The field is present only if UE is configured with dl-STTI-Length=subslot). This field is set to 0 when the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions set to TRUE and the repetition number is greater than 1.

-Antenna port(s), scrambling identity and number of layers – 3 bits as specified in Table 5.3.3.1.22-2if the UE is higher layer configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10, Table 5.3.3.1.22-3 if the UE is higher layer configured with slotSubslotPDSCH-TXDiv-4layer-TM9/10, or Table 5.3.3.1.22-1 otherwise, where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2], or 1 bit as specified in Table 5.3.3.1.5C-6 where nSCID is the scrambling identity for antenna ports 7 and 8 defined in clause 6.10.3.1 of [2] when higher layer parameter semiOpenLoop-STTI is configured.

-PDSCH RE Mapping and Quasi-Co-Location Indicator – 2 bits as defined in clauses 7.1.9 and 7.1.10 of [3]

When higher layer parameter semiOpenLoop-STTI is configured, antenna ports 7 and 8 are used for transmit diversity.

If the UE is configured to decode SPDCCH CRC scrambled by the C-RNTI and the number of information bits in format 7-1G mapped onto a given search space is less than that of format 7-0A/B depending on the configured uplink transmission mode for scheduling the same serving cell and mapped onto the same search space, zeros shall be appended to format 7-1G until the payload size equals that of format 7-0A/B, except when format 7-1G assigns downlink resource on a secondary cell without an uplink configuration associated with the secondary cell.

If the number of information bits in format 7-1G carried by PDCCH is equal to the payload size of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4 mapped onto the UE specific search space given by C-RNTI or SPS C-RNTI as defined in [3] (including any padding bits appended to format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4), one or more zero bit(s) shall be appended to format 7-1G until the payload size is not equal to that of a configured format 0/0C/1/1A/1B/1D/2/2A/2B/2C/2D/4.

## 5.3.3.2CRC attachment

Error detection is provided on DCI transmissions through a Cyclic Redundancy Check (CRC).

The entire payload is used to calculate the CRC parity bits. Denote the bits of the payload by, and the parity bits by. A is the payload size and L is the number of parity bits.

The parity bits are computed and attached according to clause 5.1.1 setting L to 16 bits, resulting in the sequence, where B = A+ L.

In the case where closed-loop UE transmit antenna selection is not configured or applicable, after attachment, the CRC parity bits are scrambled with the corresponding RNTI  , where  corresponds to the MSB of the RNTI, to form the sequence of bits. The relation between ck and bk is:

for k = 0, 1, 2, …, A-1

for k = A, A+1, A+2,..., A+15.

In the case where closed-loop UE transmit antenna selection is configured and applicable, after attachment, the CRC parity bits with DCI format 0 or DCI format 6-0A are scrambled with the antenna selection mask  as indicated in Table 5.3.3.2-1 and the corresponding RNTI  to form the sequence of bits. The relation between ck and bk is:

for k = 0, 1, 2, …, A-1

for k = A, A+1, A+2,..., A+15.

Table 5.3.3.2-1: UE transmit antenna selection mask

## 5.3.3.3Channel coding

Information bits are delivered to the channel coding block. They are denoted by  , where K is the number of bits, and they are tail biting convolutionally encoded according to clause 5.1.3.1.

After encoding the bits are denoted by , with , and where D is the number of bits on the i-th coded stream, i.e., .

## 5.3.3.4Rate matching

A tail biting convolutionally coded block is delivered to the rate matching block. This block of coded bits is denoted by , with , and where i is the coded stream index and D is the number of bits in each coded stream. This coded block is rate matched according to clause 5.1.4.2.

After rate matching, the bits are denoted by , where E is the number of rate matched bits.

## 5.3.4Control format indicator

Data arrives each subframe to the coding unit in the form of an indicator for the time span, in units of OFDM symbols, of the DCI carried by PDCCH in that subframe of the corresponding DL cell. The CFI takes values CFI = 1, 2 or 3. For system bandwidths , the span of the DCI carried by PDCCH in units of OFDM symbols, 1, 2 or 3, is given by the CFI. For system bandwidths , the span of the DCI carried by PDCCH in units of OFDM symbols, 2, 3 or 4, is given by CFI+1.

The coding flow is shown in Figure 5.3.4-1.

Figure 5.3.4-1 Coding for CFI

## 5.3.4.1Channel coding

The control format indicator is coded according to Table 5.3.4-1.

Table 5.3.4-1: CFI code words

## 5.3.5HARQ indicator (HI)

Data arrives to the coding unit in the form of indicators for HARQ acknowledgement for one transport block.

The coding flow is shown in Figure 5.3.5-1.

Figure 5.3.5-1 Coding for HI

## 5.3.5.1Channel coding

The HI is coded according to Table 5.3.5-1, where for a positive acknowledgement HI = 1 and for a negative acknowledgement HI = 0.

Table 5.3.5-1: HI code words

## 5.4Sidelink transport channels and control information

## 5.4.1Sidelink broadcast channel

Figure 5.4.1-1 shows the processing structure for the SL-BCH transport channel. Data arrives to the coding unit in the form of a maximum of one transport block. The following coding steps can be identified:

-Add CRC to the transport block

-Channel coding

-Rate matching

The coding steps for SL-BCH transport channel are shown in the figure below. In addition, after rate matching PUSCH interleaving is applied according to clauses 5.2.2.7 and 5.2.2.8 without any control information in order to apply a time-first rather than frequency-first mapping, where  and the sequence of bits f is equal to e. For SL-BCH configured by higher layers for V2X sidelink,  is used.

Figure 5.4.1-1: Transport channel processing for SL-BCH

## 5.4.1.1Transport block CRC attachment

Error detection is provided on transport blocks through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by. A is the size of the transport block and L is the number of parity bits. The lowest order information bit a0 is mapped to the most significant bit of the transport block as defined in clause 6.1.1 of [5].

The parity bits are computed and attached according to clause 5.1.1 setting L to 16 bits, resulting in the sequence of bits where  for k = 0, 1, 2, …, K-1 and K=A+L.

## 5.4.1.2Channel coding

Information bits are delivered to the channel coding block. They are denoted by  , where K is the number of bits, and they are tail biting convolutionally encoded according to clause 5.1.3.1.

After encoding the bits are denoted by , with, and where D is the number of bits on the i-th coded stream, i.e., .

## 5.4.1.3Rate matching

A tail biting convolutionally coded block is delivered to the rate matching block. This block of coded bits is denoted by, with, and where i is the coded stream index and D is the number of bits in each coded stream. This coded block is rate matched according to clause 5.1.4.2.

After rate matching, the bits are denoted by, where E is the number of rate matched bits as defined in clause 9.6.1 of [2].

## 5.4.2Sidelink shared channel

The processing of the sidelink shared channel follows the downlink shared channel according to clause 5.3.2, with the following differences:

-Data arrives to the coding unit in the form of a maximum of one transport block every transmission time interval (TTI)

-In the step of code block concatenation, the sequence of coded bits corresponding to one transport block after code block concatenation is referred to as one codeword in clause 9.3.1 of [2].

-PUSCH interleaving is applied according to clauses 5.2.2.7 and 5.2.2.8 without any control information in order to apply a time-first rather than frequency-first mapping, where . For SL-SCH configured by higher layers for V2X sidelink, is used if the transmission format field of SCI format 1 is present and set to 1, otherwise  .

## 5.4.3Sidelink control information

An SCI transports sidelink scheduling information.

The processing for one SCI follows the downlink control information according to clause 5.3.3, with the following differences:

-In the step of CRC attachment, no scrambling is performed.

-PUSCH interleaving is applied according to clauses 5.2.2.7 and 5.2.2.8 without any control information in order to apply a time-first rather than frequency-first mapping, where  and the sequence of bits f is equal to e. For SCI format 1, .

## 5.4.3.1SCI formats

The fields defined in the SCI formats below are mapped to the information bits a0 to aA-1 as follows.

Each field is mapped in the order in which it appears in the description, with the first field mapped to the lowest order information bit a0 and each successive field mapped to higher order information bits. The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to a0.

## 5.4.3.1.1SCI format 0

SCI format 0 is used for the scheduling of PSSCH.

The following information is transmitted by means of the SCI format 0:

- Frequency hopping flag – 1 bit as defined in clause 14.1.1 of [3].

- Resource block assignment and hopping resource allocation –  bits

- For PSSCH hopping:

- NSL_hop MSB bits are used to obtain the value of  as indicated in clause 8.4 of [3]

-  bits provide the resource allocation in the subframe

- For non-hopping PSSCH:

-  bits provide the resource allocation in the subframe as defined in clause 8.1.1 of [3]

- Time resource pattern – 7 bits as defined in clause 14.1.1 of [3].

- Modulation and coding scheme – 5 bits as defined in clause 14.1.1 of [3]

- Timing advance indication – 11 bits as defined in clause 14.2.1 of [3]

- Group destination ID – 8 bits as defined by higher layers

## 5.4.3.1.2SCI format 1

SCI format 1 is used for the scheduling of PSSCH.

The following information is transmitted by means of the SCI format 1:

-Priority - 3 bits as defined in clause 4.4.5.1 of [7].

-Resource reservation – 4 bits as defined in clause 14.2.1 of [3].

-Frequency resource location of initial transmission and retransmission –  bits as defined in clause 14.1.1.4C of [3].

-Time gap between initial transmission and retransmission - 4 bits as defined in clause 14.1.1.4C of [3].

-Modulation and coding scheme – 5 bits as defined in clause 14.2.1 of [3].

-Retransmission index – 1 bit as defined in clause 14.2.1 of [3].

-Transmission format– 1 bit, where value 1 indicates a transmission format including rate-matching and TBS scaling, and value 0 indicates a transmission format including puncturing and no TBS-scaling. This field is only present if the transport mechanism selected by higher layers indicates the support of rate matching and TBS scaling.

-Reserved information bits are added until the size of SCI format 1 is equal to 32 bits. The reserved bits are set to zero.

## 5.4.4Sidelink discovery channel

The processing of the sidelink discovery channel follows the downlink shared channel according to clause 5.3.2, with the following differences:

-Data arrives to the coding unit in the form of a maximum of one transport block every transmission time interval (TTI).

-In the step of code block concatenation, the sequence of coded bits corresponding to one transport block after code block concatenation is referred to as one codeword in clause 9.5.1 of [2].

-PUSCH interleaving is applied according to clauses 5.2.2.7 and 5.2.2.8 without any control information in order to apply a time-first rather than frequency-first mapping, where .

## 6Narrowband IoT

## 6.1Mapping to physical channels

For Narrowband IoT, transport channels are mapped onto narrowband physical channels, the channel coding, multiplexing, and interleaving of which are specified in clauses 6.3 and 6.4 for the uplink and downlink, respectively. Table 6.1-1 specifies the mapping of the uplink transport channels to their corresponding physical channels. Table 6.1-2 specifies the mapping of the downlink transport channels to their corresponding physical channels.Table 6.1-3 specifies the mapping of control channel information to its corresponding physical channel.

Table 6.1-1

Table 6.1-2

Table 6.1-3

## 6.2Generic procedures

The generic procedures for channel coding, multiplexing and interleaving are as in clause 5.1 unless otherwise noted in clause 6.

Usage of coding scheme and coding rate for the different types of TrCH is shown in table 6.2-1. Usage of coding scheme and coding rate for the different control information types is shown in table 6.2-2.

Table 6.2-1: Usage of channel coding scheme and coding rate for TrCHs

Table 6.2-2: Usage of channel coding scheme and coding rate for control information.

## 6.3Uplink transport channels and control information

## 6.3.1Random access channel

The sequence for the random access channel is processed according to [2].

## 6.3.2Uplink shared channel

Figure 6.3.2-1 shows the processing structure for the UL-SCH transport channel. Data arrives to the coding unit in the form of a maximum of one transport block over a number of resource units per UL cell. The number of resource units is scheduled according to [3]. The following coding steps can be identified:

-CRC attachment

-Channel coding

-Rate matching

Figure 6.3.2-1: Transport block processing for UL-SCH

The CRC attachment, channel coding, and rate matching are performed according to clauses 5.2.2.1, 5.2.2.3, and 5.2.2.4, respectively, with the following differences:

-In clause 5.1.4.1.2 in the calculation of  , Qm is 2 for π/4-QPSK, and rvidx = 0 or 2.

In addition, after rate matching interleaving is applied per resource unit according to clauses 5.2.2.7 and 5.2.2.8 without any control information in order to apply a time-first rather than frequency-first mapping, where the input sequence to 5.2.2.7 is the portion of e for a resource unit instead of f, and where  is the number of SC-FDMA symbols for NPUSCH in a UL resource unit as given in clause 10.1.2.3 of [2].

## 6.3.3Uplink control information on NPUSCH without UL-SCH data

When control data is sent via NPUSCH without UL-SCH data and arrives to the coding unit in the form of an indicator for HARQ acknowledgement for one transport block, the coding flow is as shown in Figure 6.3.3-1.

Figure 6.3.3-1: Coding for HARQ-ACK

The one bit information of HARQ-ACK is coded according to Table 6.3.3-1, where for a positive acknowledgement = 1 and for a negative acknowledgement = 0.

Table 6.3.3-1: HARQ-ACK code words

## 6.3.4Scheduling request

The scheduling request indication is received from higher layers and is processed according to [2] and [3].

## 6.4Downlink transport channels and control information

## 6.4.1Broadcast channel

The processing structure for the BCH transport channel is according to Clause 5.3.1, with the following differences:

-The transmission time interval (TTI) is 640ms

-The size of the BCH transport block is set to 34 bits

-The CRC mask for NPBCH is selected according to 1 or 2 transmit antenna ports at eNodeB according to Table 5.3.1.1-1, where the transmit antenna ports are defined in clause 10.2.6 of [2]

-The number of rate matched bits is defined in clause 10.2.4.1 of [2].

## 6.4.2Downlink shared channel and Paging channel

Figure 6.4.2-1 shows the processing structure for each transport block for the DL-SCH and PCH transport channels. Data arrives to the coding unit in the form of a maximum of one transport blocks over a number of resource units per DL cell. The following coding steps can be identified for each transport block of a DL cell:

-CRC attachment

-Channel coding

-Rate matching

Figure 6.4.2-1: Transport block processing for DL-SCH and PCH

The CRC attachment, channel coding, and rate matching is performed according to clauses 5.1.1, 5.1.3.1 and 5.1.4.2, respectively. For the CRC attachment, the parity bits are computed and attached according to clause 5.1.1 setting L to 24 bits and using the generator polynomial , resulting in the sequence of bits where  for k = 0, 1, 2, …, K-1 and K=A+L.gCRC24A(D)

## 6.4.3Downlink control information

A DCI transports downlink or uplink scheduling information for one cell and one RNTI. The RNTI is implicitly encoded in the CRC. The processing structure for one DCI is according to Clause 5.3.3.

## 6.4.3.1DCI Format N0

DCI format N0 is used for the scheduling of NPUSCH and operation on preconfigured UL resources in one UL cell.

The following information is transmitted by means of the DCI format N0:

-Flag for format N0/format N1 differentiation – 1 bit, where value 0 indicates format N0 and value 1 indicates format N1

-Modulation and coding scheme – 4 bits as defined in clause 16.5.1.2 of [3]. This field is only present if format N0 CRC is scrambled by PUR-RNTI.

If format N0 CRC is scrambled by PUR-RNTI and Modulation and coding scheme is set to '1110', the remaining fields are set as follows:

-ACK or Fallback indicator – 1 bit, where value 0 indicates ACK and value 1 indicates fallback as defined in clause 16.6.4 of [3]

-NPUSCH repetition adjustment – 3 bits refer to  in Table 16.5.1.1-3 of [3]

-Timing advance adjustment – 6 bits as defined in clause 16.1.2 of [3]. The field is only present if ACK or Fallback indicator is set to 0.

-All the remaining bits in format N0 are set to one

Otherwise

-Modulation and coding scheme and Subcarrier indication for OCC – 10 bits. This field is only present if  and OCC enabled/disabled indicates OCC enabled.

-OCC sequence index – 1 bit, where value 0 indicates OCC sequence [1 1] and value 1 indicates OCC sequence [1 -1].

-Modulation and coding scheme and Subcarrier indication – 9 bits, as defined in 16.5.1.1 and 16.5.1.2 of [3].

-Subcarrier indication – 6 bits as defined in clause 16.5.1.1 of [3]. This field is not present if  and OCC enabled/disabled indicates OCC enabled. If higher layer parameter npusch-OCC-Enabled is configured and Repetition number field has a value > 0 and

-OCC enabled/disabled – 1 bit, where value 0 indicates OCC disabled and value 1 indicates OCC enabled.

-OCC sequence index – 1 bit, where value 0 indicates OCC sequence [1 1] and value 1 indicates OCC sequence [1 -1]. This field is only present if OCC enabled/disabled indicates OCC enabled.

-Subcarrier indication for OCC – 4 bits (for OCC enabled/disabled indicating OCC enabled) or 5 bits (for OCC enabled/disabled indicating OCC disabled).

-Resource assignment – 3 bits as defined in clause 16.5.1.1 of [3].

-Scheduling delay – 2 bits as defined in clause 16.5.1 of [3].

-Modulation and coding scheme – 4 bits as defined in clause 16.5.1.2 of [3]. This field is not present if format N0 CRC is scrambled by PUR-RNTI, or if  and OCC enabled/disabled indicates OCC enabled. If npusch-16QAM-Config is configured and the value is '1111', it functions as 16QAM indicator.

-Redundancy version – 1 bit as defined in clause 16.5.1.2 of [3]. If higher layer parameter npusch-OCC-Enabled is configured and Repetition number field has a value > 0 and , this field functions as OCC enabled/disabled, where value 0 indicates OCC disabled and value 1 indicates OCC enabled.

-Repetition number – 3 bits as defined in clause 16.5.1.1 of [3]. If 16QAM is indicated, it functions as Modulation and coding scheme for 16QAM as defined in 16.5.1.2 of [3].

-New data indicator – 1 bit. If multiple TB are scheduled, it functions as New data indicator for the first TB.

-DCI subframe repetition number – 2 bits as defined in clause 16.6 in [3]

-Number of scheduled TB for Unicast – 1 bit, where value 0 indicates a single TB is scheduled and value 1 indicates multiple TB are scheduled. This field is only present if higher layer parameter npusch-MultiTB-Config is enabled and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3]. The field is set to 0 if the CRC of the DCI is scrambled by SPS C-RNTI.

-HARQ process number – 1 bit. This field is only present if 2 HARQ processes are configured and the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3], or if Number of scheduled TB for Unicast is present. If multiple TB are scheduled, it functions as New data indicator for the second TB.

-Resource reservation – 1 bit as defined in clause 16.5 of [3]. This field is only present if higher layer parameter resourceReservationConfigUL is configured and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

If the number of information bits in format N0 mapped onto the UE specific search space given by the C-RNTI as defined in [3] is less than that of format N1 in the same search space, zeros shall be appended to format N0 until the payload size equals that of format N1.

## 6.4.3.2DCI Format N1

DCI format N1 is used for the scheduling of one NPDSCH codeword per TTI in one cell, random access procedure initiated by a NPDCCH order, notifying SC-MCCH change, and operation on preconfigured UL resources. The DCI corresponding to a NPDCCH order is carried by NPDCCH.

The following information is transmitted by means of the DCI format N1:

-If the format N1 CRC is scrambled by C-RNTI or RA-RNTI or PUR-RNTI:

-Flag for format N0/format N1 differentiation – 1 bit, where value 0 indicates format N0 and value 1 indicates format N1

-NPDCCH order indicator – 1 bit

-Else if the format N1 CRC is scrambled by a G-RNTI:

-Information for SC-MCCH change notification – 2 bits as defined in clause 5.8a of [6]

Format N1 is used for random access procedure initiated by a NPDCCH order only if NPDCCH order indicator is set to '1', format N1 CRC is scrambled with C-RNTI, and all the remaining fields are set as follows:

-Preamble format indicator – 1 bit, where value 0 indicates preamble format 0/1 and value 1 indicates preamble format 2. This field is only present if nprach-ParametersListFmt2 is configured and the UE indicates the nprach-Format2 capability.

-Starting number of NPRACH repetitions – 2 bits as defined in clause 16.3.2 of [3]

-Subcarrier indication of NPRACH – 6 or 8 bits, this field is 8 bits only if Preamble format indicator is present and set to 1, as defined in clause 16.3.2 of [3]

-Carrier indication of NPRACH – 4 bits as defined in clause 16.3.2 of [3]. This field is only present if ul-ConfigList is configured and the UE indicates the multiCarrier-NPRACH capability.

-All the remaining bits in format N1 are set to one

Otherwise,

-Scheduling delay – 3 bits as defined in clause 16.4.1 of [3]

-Resource assignment – 3 bits as defined in clause 16.4.1.3 of [3]

-Modulation and coding scheme – 4 bits as defined in clause 16.4.1.5 of [3]. If npdsch-16QAM-Config is configured and the value is '1111', it functions as 16QAM indicator.

-Repetition number – 4 bits as defined in clause 16.4.1.3 of [3]. If 16 QAM is indicated, it functions as Modulation and coding scheme for 16QAM as defined in 16.4.1.5 of [3].

-New data indicator – 1 bit. If multiple TB are scheduled, it functions as New data indicator for the first TB.

-HARQ-ACK resource – 4 bits as defined in clause 16.4.2 of [3]. If downlinkHARQ-FeedbackDisabledDCI-NB is configured, or if downlinkHARQ-FeedbackDisabledBitmap-NB and downlinkHARQ-FeedbackDisabledDCI-NB are configured, and the value is ‘15’, it functions as a HARQ feedback disabled indicator.

-DCI subframe repetition number – 2 bits as defined in clause 16.6 in [3]

-Number of scheduled TB for SC-MTCH – 3 bits, indicating from 1 to 8 TBs. This field is only present if higher layer parameter sc-mtch-InfoListMultiTB-r16 is enabled and the CRC of the DCI is scrambled by G-RNTI.

-Number of scheduled TB for Unicast – 1 bit, where value 0 indicates a single TB is scheduled and value 1 indicates multiple TB are scheduled. This field is only present if higher layer parameter npdsch-MultiTB-Config is enabled and the corresponding DCI is mapped onto the UE specific search space given by the C-RNTI as defined in [3]

-HARQ process number – 1 bit. This field is only present if 2 HARQ processes are configured and the corresponding DCI format is mapped onto the UE specific search space given by the C-RNTI as defined in [3], or if Number of scheduled TB for Unicast is present. If multiple TB are scheduled, it functions as New data indicator for the second TB.

-Resource reservation – 1 bit as defined in clause 16.4 of [3]. This field is only present if higher layer parameter resourceReservationConfigDL is configured and the DCI is mapped onto the UE-specific search space given by C-RNTI as defined in [3].

When the format N1 CRC is scrambled with a RA-RNTI or a CB-RNTI or a G-RNTI, then the following fields among the fields above are reserved for RA-RNTI or CB-RNTI, and not present for G-RNTI:

-New data indicator

-HARQ-ACK resource

If the number of information bits in format N1 mapped onto the same search space is less than that of format N0 and the format N1 CRC is not scrambled by G-RNTI, zeros shall be appended to format N1 until the payload size equals that of format N0.

## 6.4.3.3DCI Format N2

DCI format N2 is used for paging, direct indication, scheduling of one NPDSCH codeword carrying SC-MCCH in one cell, and notifying SC-MCCH change.

The following information is transmitted by means of the DCI format N2:

-If the format N2 CRC is scrambled by P-RNTI:

-Flag for paging/direct indication differentiation – 1 bit, with value 0 for direct indication and value 1 for paging

-Else if the format N2 CRC is scrambled by a SC-RNTI:

-Information for SC-MCCH change notification – 1 bit as defined in clause 5.8a of [6]

-If the format N2 CRC is scrambled by P-RNTI and Flag=0:

-Direct Indication information – 8 bits provide direct indication of system information update and other fields, as defined in [6]

-Reserved information bits are added until the size is equal to that of format N2 with Flag=1

-If the format N2 CRC is scrambled by P-RNTI and Flag=1, or if the format N2 CRC is scrambled by SC-RNTI:

-Resource assignment – 3 bits as defined in clause 16.4.1.3 of [3]

-Modulation and coding scheme – 4 bits as defined in clause 16.4.1.5 of [3]

-Repetition number – 4 bits as defined in clause 16.4.1.3 of [3]

-DCI subframe repetition number – 3 bits as defined in clause 16.6 of [3]

## Annex A (informative):Change history
