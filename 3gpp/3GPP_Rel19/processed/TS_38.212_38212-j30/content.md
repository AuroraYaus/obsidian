---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.212_38212-j30/content.md"
---
# TS 38.212 38212-j30

Contents

Foreword6

1Scope8

2References8

3Definitions of terms, symbols and abbreviations8

3.1Terms8

3.2Symbols9

3.3Abbreviations9

4Mapping to physical channels10

4.1Uplink10

4.2Downlink10

4.3Sidelink11

5General procedures11

5.1CRC calculation11

5.2Code block segmentation and code block CRC attachment12

5.2.1Polar coding12

5.2.2Low density parity check coding13

5.3Channel coding14

5.3.1Polar coding15

5.3.1.1Interleaving15

5.3.1.2Polar encoding16

5.3.2Low density parity check coding20

5.3.3Channel coding of small block lengths24

5.3.3.1Encoding of 1-bit information24

5.3.3.2Encoding of 2-bit information25

5.3.3.3Encoding of other small block lengths25

5.4Rate matching26

5.4.1Rate matching for Polar code26

5.4.1.1Sub-block interleaving26

5.4.1.2Bit selection27

5.4.1.3Interleaving of coded bits28

5.4.2Rate matching for LDPC code29

5.4.2.1Bit selection29

5.4.2.2Bit interleaving32

5.4.3Rate matching for channel coding of small block lengths33

5.5Code block concatenation33

6Uplink transport channels and control information34

6.1Random access channel34

6.2Uplink shared channel34

6.2.1Transport block CRC attachment34

6.2.2LDPC base graph selection34

6.2.3Code block segmentation and code block CRC attachment34

6.2.4Channel coding of UL-SCH35

6.2.5Rate matching35

6.2.6Code block concatenation35

6.2.7Data and control multiplexing35

6.3Uplink control information47

6.3.1Uplink control information on PUCCH47

6.3.1.1UCI bit sequence generation47

6.3.1.1.1HARQ-ACK/SR only47

6.3.1.1.2CSI only48

6.3.1.1.3HARQ-ACK/SR and CSI73

6.3.1.1.4UCI with different priority indexes74

6.3.1.2Code block segmentation and CRC attachment74

6.3.1.2.1UCI encoded by Polar code74

6.3.1.2.2UCI encoded by channel coding of small block lengths75

6.3.1.3Channel coding of UCI75

6.3.1.3.1UCI encoded by Polar code75

6.3.1.3.2UCI encoded by channel coding of small block lengths75

6.3.1.4Rate matching75

6.3.1.4.1UCI encoded by Polar code75

6.3.1.4.2UCI encoded by channel coding of small block lengths76

6.3.1.4.3UCI with different priority indexes encoded by Polar code77

6.3.1.4.4UCI with different priority indexes encoded by channel coding of small block lengths77

6.3.1.5Code block concatenation77

6.3.1.6Multiplexing of coded UCI bits to PUCCH78

6.3.2Uplink control information on PUSCH80

6.3.2.1UCI bit sequence generation80

6.3.2.1.1HARQ-ACK80

6.3.2.1.2CSI81

6.3.2.1.3CG-UCI115

6.3.2.1.3AUTO-UCI116

6.3.2.1.3BUEIRI116

6.3.2.1.4HARQ-ACK and CG-UCI/UTO-UCI116

6.3.2.1.5UCI with different priority indexes117

6.3.2.2Code block segmentation and CRC attachment119

6.3.2.2.1UCI encoded by Polar code119

6.3.2.2.2UCI encoded by channel coding of small block lengths119

6.3.2.3Channel coding of UCI119

6.3.2.3.1UCI encoded by Polar code119

6.3.2.3.2UCI encoded by channel coding of small block lengths119

6.3.2.4Rate matching119

6.3.2.4.1UCI encoded by Polar code120

6.3.2.4.2UCI encoded by channel coding of small block lengths135

6.3.2.5Code block concatenation138

6.3.2.6Multiplexing of coded UCI bits to PUSCH138

6.3.2.7Multiplexing of coded UCI bits with different priority indexes to PUSCH138

7Downlink transport channels and control information138

7.1Broadcast channel138

7.1.1PBCH payload generation139

7.1.2Scrambling140

7.1.3Transport block CRC attachment141

7.1.4Channel coding141

7.1.5Rate matching141

7.2Downlink shared channel and paging channel141

7.2.1Transport block CRC attachment141

7.2.2LDPC base graph selection142

7.2.3Code block segmentation and code block CRC attachment142

7.2.4Channel coding142

7.2.5Rate matching142

7.2.6Code block concatenation143

7.3Downlink control information143

7.3.1DCI formats143

7.3.1.0DCI size alignment144

7.3.1.0.1DCI size alignment for DCI formats for scheduling of sidelink148

7.3.1.1DCI formats for scheduling of PUSCH148

7.3.1.1.1Format 0_0148

7.3.1.1.2Format 0_1152

7.3.1.1.3Format 0_2226

7.3.1.1.4Format 0_3241

7.3.1.2DCI formats for scheduling of PDSCH251

7.3.1.2.1Format 1_0251

7.3.1.2.2Format 1_1257

7.3.1.2.3Format 1_2284

7.3.1.2.4Format 1_3289

7.3.1.3DCI formats for other purposes299

7.3.1.3.1Format 2_0299

7.3.1.3.2Format 2_1299

7.3.1.3.3Format 2_2299

7.3.1.3.4Format 2_3300

7.3.1.3.5Format 2_4301

7.3.1.3.6Format 2_5301

7.3.1.3.7Format 2_6301

7.3.1.3.8Format 2_7301

7.3.1.3.9Format 2_8302

7.3.1.3.10Format 2_9302

7.3.1.4DCI formats for scheduling of sidelink303

7.3.1.4.1Format 3_0303

7.3.1.4.2Format 3_1304

7.3.1.4.3Format 3_2305

7.3.1.5DCI formats for scheduling of MBS305

7.3.1.5.1Format 4_0305

7.3.1.5.2Format 4_1306

7.3.1.5.3Format 4_2306

7.3.2CRC attachment308

7.3.3Channel coding309

7.3.4Rate matching309

7.4Wake-up information309

7.4.1Channel coding310

7.4.2Rate matching310

7.4.2.1Rate matching for OOK modulation310

7.4.2.2Rate matching for sequence modulation310

7.4.3Line coding310

8Sidelink transport channels and control information311

8.1Sidelink broadcast channel311

8.1.1Void311

8.2Sidelink shared channel311

8.2.1Data and control multiplexing311

8.3Sidelink control information on PSCCH312

8.3.11st-stage SCI formats312

8.3.1.1SCI format 1-A312

8.3.1.2SCI format 1-B314

8.3.2CRC attachment315

8.3.3Channel coding315

8.3.4Rate Matching315

8.4Sidelink control information on PSSCH315

8.4.12nd-stage SCI formats315

8.4.1.1SCI format 2-A316

8.4.1.2SCI format 2-B316

8.4.1.3SCI format 2-C317

8.4.1.4SCI format 2-D318

8.4.2CRC attachment319

8.4.3Channel coding319

8.4.4Rate Matching319

8.4.5Multiplexing of coded 2nd-stage SCI bits to PSSCH320

Annex A (informative):Change history321

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

The present document specifies the coding, multiplexing and mapping to physical channels for 5G NR.

## 2References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

-References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

-For a specific reference, subsequent revisions do not apply.

-For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1]3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2]void.

[3]void.

[4]3GPP TS 38.211: "NR; Physical channels and modulation".

[5]3GPP TS 38.213: "NR; Physical layer procedures for control".

[6]3GPP TS 38.214: "NR; Physical layer procedures for data".

[7]void.

[8]3GPP TS 38.321: "NR; Medium Access Control (MAC) protocol specification".

[9]3GPP TS 38.331: "NR; Radio Resource Control (RRC) protocol specification".

[10]3GPP TS 38.473: "NG-RAN; F1 Application Protocol (F1AP)".

[11]3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[12]3GPP TS 23.287: "Architecture enhancements for 5G System (5GS) to support VehicletoEverything (V2X) services".

[13]3GPP TS 38.101-1: "NR; User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone".

[14]3GPP TS 37.213: "Physical layer procedures for shared spectrum channel access".

[15]3GPP TS 38.101-5: "NR; User Equipment (UE) radio transmission and reception; Part 5: Satellite access Radio Frequency (RF) and performance requirements"

## 3Definitions of terms, symbols and abbreviations

## 3.1Terms

For the purposes of the present document, the terms given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

## 3.2Symbols

Void.

## 3.3Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

BCHBroadcast Channel

CAPCChannel Access Priority Class

CBGCode Block Group

CBGTICode Block Group Transmission Information

CGConfigured Grant

CG-DFICG - Downlink Feedback Information

CG-UCICG - Uplink Control Information

CLI-RSSICross Link Interference – Received Signal Strength Indicator

CORESETControl Resource Ret

COTChannel Occupancy Time

CPCyclic Prefix

CQIChannel Quality Indicator

CRCCyclic Redundancy Check

CRICSI-RS Resource Indicator

CSIChannel State Information

CSI-PAICSI Prediction Accuracy Indicator

CSI-RSCSI - Reference Signal

DAIDownlink Assignment Index

DCIDownlink Control Information

DLDownlink

DL-SCHDownlink - Shared Channel

DMRSDemodulation Reference Signal

HARQHybrid Automatic repeat Request

HARQ-ACKHybrid Automatic repeat Request - Acknowledgement

LDPCLow Density Parity Check

LILayer Indicator

MBSMulticast Broadcast Services

MCSModulation and Coding Scheme

MRIMeasurement Resource Index

NCRNetwork-controlled repeater

OFDMOrthogonal Frequency Division Multiplex

PBCHPhysical Broadcast Channel

PCHPaging Channel

PDCCHPhysical Downlink Control Channel

PDSCHPhysical Downlink Shared Channel

PMIPrecoding Matrix Indicator

PRBPhysical Resource Block

PRACHPhysical Random Access Channel

PSBCHPhysical Sidelink Broadcast Channel

PSCCHPhysical Sidelink Control Channel

PSFCHPhysical Sidelink Feedback Channel

PSSCHPhysical Sidelink Shared Channel

PTRSPhase-Tracking Reference Signal

PUCCHPhysical Uplink Control Channel

PUSCHPhysical Uplink Shared Channel

RACHRandom Access Channel

RIRank Indicator

RSRPReference Signal Received Power

RS-PAIReference Signal Prediction Accuracy Indicator

SBFDSub-Band Full Duplex

SCISidelink Control Information

SFCISidelink Feedback Control Information

SFNSystem Frame Number

SGCSSquared Generalized Cosine Similarity

SLSidelink

SL-BCHSidelink - Broadcast Channel

SL PRSSidelink Positioning Reference Signal

SL-SCHSidelink - Shared Channel

SRScheduling Request

SRSSounding Reference Signal

SRS-RSRPSRS - Reference Signal Received Power

SSSynchronisation Signal

SULSupplementary Uplink

TCITransmission Configuration Indicator

TPCTransmit Power Control

TrCHTransport Channel

TRSTracking Reference Signal

UCIUplink Control Information

UEUser Equipment

UEIRIUE Initiated Report Indicator

ULUplink

UL-SCHUplink Shared Channel

UTO-UCIUnused Transmission Occasion - Uplink Control Information

VRBVirtual Resource Block

ZP CSI-RSZero power CSI-RS

## 4Mapping to physical channels

## 4.1Uplink

Table 4.1-1 specifies the mapping of the uplink transport channels to their corresponding physical channels. Table 4.1-2 specifies the mapping of the uplink control channel information to its corresponding physical channel.

Table 4.1-1

Table 4.1-2

## 4.2Downlink

Table 4.2-1 specifies the mapping of the downlink transport channels to their corresponding physical channels. Table 4.2-2 specifies the mapping of the downlink control channel information to its corresponding physical channel.

Table 4.2-1

Table 4.2-2

## 4.3Sidelink

Table 4.3-1 specifies the mapping of the sidelink transport channels to their corresponding physical channels. Table 4.3-2 specifies the mapping of the sidelink control information and sidelink feedback control information to their corresponding physical channels.

Table 4.3-1

Table 4.3-2

## 5General procedures

Data and control streams from/to MAC layer are encoded /decoded to offer transport and control services over the radio transmission link. Channel coding scheme is a combination of error detection, error correcting, rate matching, interleaving and transport channel or control information mapping onto/splitting from physical channels.

## 5.1CRC calculation

Denote the input bits to the CRC computation by , and the parity bits by , where  is the size of the input sequence and  is the number of parity bits. The parity bits are generated by one of the following cyclic generator polynomials:

- for a CRC length ;

- for a CRC length ;

- for a CRC length ;

- for a CRC length ;

- for a CRC length ;

- for a CRC length .

The encoding is performed in a systematic form, which means that in GF(2), the polynomial:

yields a remainder equal to 0 when divided by the corresponding CRC generator polynomial.

The bits after CRC attachment are denoted by , where . The relation between  and  is:

for

for .

## 5.2Code block segmentation and code block CRC attachment

## 5.2.1Polar coding

The input bit sequence to the code block segmentation is denoted by , where .

if

Number of code blocks: ;

else

Number of code blocks:

end if

;

for  to

;

end for

for  to

;

end for

;

for  to

for  to

;

;

end for

The sequence  is used to calculate the CRC parity bits  according to Clause 5.1 with a generator polynomial of length .

for  to

;

end for

end for

The value of  is no larger than 1706.

## 5.2.2Low density parity check coding

The input bit sequence to the code block segmentation is denoted by , where . If  is larger than the maximum code block size , segmentation of the input bit sequence is performed and an additional CRC sequence of  bits is attached to each code block.

For LDPC base graph 1, the maximum code block size is:

-.

For LDPC base graph 2, the maximum code block size is:

-.

Total number of code blocks C is determined by:

if

Number of code blocks:

else

Number of code blocks: .

end if

The bits output from code block segmentation are denoted by , where  is the code block number, and  is the number of bits for the code block number .

The number of bits  in each code block is calculated as:

;

For LDPC base graph 1,

.

For LDPC base graph 2,

if

;

elseif

;

elseif

;

else

;

end if

find the minimum value of  in all sets of lifting sizes in Table 5.3.2-1, denoted as , such that , and set  for LDPC base graph 1 and  for LDPC base graph 2;

The bit sequence  is calculated as:

;

for  to

for  to

;

;

end for

if

The sequence  is used to calculate the CRC parity bits  according to Clause 5.1 with the generator polynomial .

for  to

;

end for

end if

for  to -- Insertion of filler bits

;

end for

end for

## 5.3Channel coding

Usage of coding scheme for the different types of TrCH is shown in table 5.3-1. Usage of coding scheme for the different control information types is shown in table 5.3-2.

Table 5.3-1: Usage of channel coding scheme for TrCHs

Table 5.3-2: Usage of channel coding scheme for control information

## 5.3.1Polar coding

The bit sequence input for a given code block to channel coding is denoted by, where  is the number of bits to encode. After encoding the bits are denoted by, where  and the value of  is determined by the following:

Denote by  the rate matching output sequence length as given in Clause 5.4.1;

If  and

;

else

;

end if

;

;

where .

UE is not expected to be configured with , where   is the number of parity check bits defined in Clause 5.3.1.2.

## 5.3.1.1Interleaving

The bit sequence  is interleaved into bit sequence  as follows:

,

where the interleaving pattern  is given by the following:

if

,

else

;

for  to

if

;

;

end if

end for

end if

where  is given by Table 5.3.1.1-1 and .

Table 5.3.1.1-1: Interleaving pattern

## 5.3.1.2Polar encoding

The Polar sequence  is given by Table 5.3.1.2-1, where  denotes a bit index before Polar encoding for  and . The Polar sequence  is in ascending order of reliability , where  denotes the reliability of bit index .

For any code block encoded to  bits, a same Polar sequence  is used. The Polar sequence  is a subset of Polar sequence  with all elements  of values less than , ordered in ascending order of reliability .

Denote  as a set of bit indices in Polar sequence , and  as the set of other bit indices in Polar sequence , where  and  are given in Clause 5.4.1.1, , , and  is the number of parity check bits.

Denote  as the -th Kronecker power of matrix , where .

For a bit index  with , denote  as the -th row of  and  as the row weight of , where  is the number of ones in . Denote the set of bit indices for parity check bits as , where . A number of  parity check bits are placed in the  least reliable bit indices in . A number of  other parity check bits are placed in the bit indices of minimum row weight in , where  denotes the  most reliable bit indices in ; if there are more than  bit indices of the same minimum row weight in , the  other parity check bits are placed in the  bit indices of the highest reliability and the minimum row weight in .

Generate  according to the following:

;

if

; ; ; ; ;

for  to

; ; ; ; ; ;

if

if

;

else

;

;

;

end if

else

;

end if

end for

else

for  to

if

;

;

else

;

end if

end for

end if

The output after encoding  is obtained by . The encoding is performed in GF(2).

Table 5.3.1.2-1: Polar sequence  and its corresponding reliability

## 5.3.2Low density parity check coding

The bit sequence input for a given code block to channel coding is denoted by , where  is the number of bits to encode as defined in Clause 5.2.2. After encoding the bits are denoted by , where  for LDPC base graph 1 and  for LDPC base graph 2, and the value of  is given in Clause 5.2.2.

For a code block encoded by LDPC, the following encoding procedure applies:

1)Find the set with index  in Table 5.3.2-1 which contains .

2)for  to

if

;

else

;

;

end if

end for

3)Generate  parity bits  such that , where ;  is a column vector of all elements equal to 0. The encoding is performed in GF(2).

For LDPC base graph 1, a matrix of  has 46 rows with row indices and 68 columns with column indices . For LDPC base graph 2, a matrix of  has 42 rows with row indices and 52 columns with column indices . The elements in  with row and column indices given in Table 5.3.2-2 (for LDPC base graph 1) and Table 5.3.2-3 (for LDPC base graph 2) are of value 1, and all other elements in  are of value 0.

The matrix  is obtained by replacing each element of  with a  matrix, according to the following:

-Each element of value 0 in  is replaced by an all zero matrix of size ;

-Each element of value 1 in  is replaced by a circular permutation matrix  of size , where  and  are the row and column indices of the element, and  is obtained by circularly shifting the identity matrix of size  to the right  times. The value of  is given by . The value of  is given by Tables 5.3.2-2 and 5.3.2-3 according to the set index  and LDPC base graph.

4)for  to

;

end for

Table 5.3.2-1: Sets of LDPC lifting size

Table 5.3.2-2: LDPC base graph 1 () and its parity check matrices ()

Table 5.3.2-3: LDPC base graph 2 () and its parity check matrices ()

## 5.3.3Channel coding of small block lengths

The bit sequence input for a given code block to channel coding is denoted by , where  is the number of bits to encode. After encoding the bits are denoted by .

## 5.3.3.1Encoding of 1-bit information

For , the code block is encoded according to Table 5.3.3.1-1, where  and  is the modulation order for the code block.

Table 5.3.3.1-1: Encoding of 1-bit information

The "x" and "y" in Table 5.3.3.1-1 are placeholders for Clauses 6.3.1.1, 6.3.2.5.1, 6.3.2.6.1 of [4, TS 38.211] to scramble the information bits in a way that maximizes the Euclidean distance of the modulation symbols carrying the information bits.

## 5.3.3.2Encoding of 2-bit information

For , the code block is encoded according to Table 5.3.3.2-1, where , , and  is the modulation order for the code block.

Table 5.3.3.2-1: Encoding of 2-bit information

The "x" in Table 5.3.3.2-1 are placeholders for Clause 6.3.1.1 of [4, TS 38.211] to scramble the information bits in a way that maximizes the Euclidean distance of the modulation symbols carrying the information bits.

## 5.3.3.3Encoding of other small block lengths

For , the code block is encoded by , where , , and  represents the basis sequences as defined in Table 5.3.3.3-1.

Table 5.3.3.3-1: Basis sequences for (32, ) code

## 5.4Rate matching

## 5.4.1Rate matching for Polar code

The rate matching for Polar code is defined per coded block and consists of sub-block interleaving, bit collection, and bit interleaving. The input bit sequence to rate matching is . The output bit sequence after rate matching is denoted as .

## 5.4.1.1Sub-block interleaving

The bits input to the sub-block interleaver are the coded bits . The coded bits  are divided into 32 sub-blocks. The bits output from the sub-block interleaver are denoted as , generated as follows:

for  to

;

;

;

end for

where the sub-block interleaver pattern  is given by Table 5.4.1.1-1.

Table 5.4.1.1-1: Sub-block interleaver pattern

The sets of bit indices  and  are determined as follows, where , , and  are defined in Clause 5.3.1

if

if -- puncturing

for  to

;

end for

if

;

else

;

end if

else-- shortening

for  to

;

end for

end if

end if

;

comprises  most reliable bit indices in ;

;

## 5.4.1.2Bit selection

The bit sequence after the sub-block interleaver  from Clause 5.4.1.1 is written into a circular buffer of length .

Denoting by  the rate matching output sequence length, the bit selection output bit sequence , , is generated as follows:

if -- repetition

for  to

;

end for

else

if -- puncturing

for  to

;

end for

else-- shortening

for  to

;

end for

end if

end if

## 5.4.1.3Interleaving of coded bits

The bit sequence  is interleaved into bit sequence , as follows:

If

Denote  as the smallest integer such that ;

;

for  to

for  to

if

;

else

;

end if

;

end for

end for

;

for  to

for  to

if

;

end if

end for

end for

else

for  to

;

end for

end if

The value of  is no larger than 8192.

## 5.4.2Rate matching for LDPC code

The rate matching for LDPC code is defined per coded block and consists of bit selection and bit interleaving. The input bit sequence to rate matching is . The output bit sequence after rate matching is denoted as .

## 5.4.2.1Bit selection

The bit sequence after encoding  from Clause 5.3.2 is written into a circular buffer of length  for the -th coded block, where  is defined in Clause 5.3.2.

For the -th code block, let  if  and  otherwise, where, ,  is determined according to Clause 6.1.4.2 in [6, TS 38.214] for UL-SCH and Clause 5.1.3.2 in [6, TS 38.214] for DL-SCH/PCH, assuming the following:

For one TB for DL-SCH with PDSCH scheduled by DCI format 4_0/4_1/4_2:

-if the PDSCH is scheduled by DCI format 4_1/4_2:

-maximum number of layers is given by X, where:

-if the higher layer parameter maxMIMO-Layers of pdsch-ConfigMulticast is configured, X is given by that parameter;

-otherwise, X equals to 1;

-if the higher layer parameter mcs-Table given by a pdsch-ConfigMulticast or by pdsch-ConfigMTCH for at least one common frequency resource (CFR) is set to 'qam256', maximum modulation order  is assumed for DL-SCH; otherwise a maximum modulation order  is assumed for DL-SCH;Qm=8Qm=6

-if the PDSCH is scheduled by DCI format 4_0:

-maximum number of layers is 1;

-if the higher layer parameter mcs-Table given by a pdsch-ConfigMCCH is set to 'qam256', maximum modulation order  is assumed for DL-SCH; otherwise a maximum modulation order  is assumed for DL-SCH;Qm=8Qm=6

-if the higher layer parameter mcs-Table given by a pdsch-ConfigMTCH is set to 'qam256', maximum modulation order  is assumed for DL-SCH; otherwise a maximum modulation order  is assumed for DL-SCH;Qm=8Qm=6

- is given by Table 5.4.2.1-1, where the value of  for DL-SCH is determined according to the size of the associated CFR if configured to the UE;nPRB=nPRB,LBRMnPRB,LBRM

-maximum coding rate of 948/1024;

-;NRE=156∙nPRB

- is the number of code blocks of the transport block determined according to Clause 5.2.2.C

For one TB for UL-SCH, or for one TB for DL-SCH/PCH except for DL-SCH with PDSCH scheduled by DCI format 4_0/4_1/4_2:

-maximum number of layers for one TB for UL-SCH is given by the minimum of X and 4, where:

-if the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured and if neither the higher layer parameter multipanelSchemeSFN nor the higher layer parameter multipanelSchemeSDM is configured, X is given by that parameter;

-elseif the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured and if the higher layer parameter multipanelSchemeSFN is configured, X is given by max{maxMIMO-Layers, maxMIMO-LayersforSFN};

-elseif the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured and if the higher layer parameter multipanelSchemeSDM is configured, X is given by max{maxMIMO-Layers, 2*maxMIMO-LayersforSDM};

-elseif the higher layer parameter maxRank of pusch-Config of the serving cell is configured and if neither the higher layer parameter multipanelSchemeSFN nor the higher layer parameter multipanelSchemeSDM is configured, X is given by the maximum value of maxRank across all BWPs of the serving cell;

-elseif the higher layer parameter maxRank of pusch-Config of the serving cell is configured and if the higher layer parameter multipanelSchemeSFN is configured, X is given by max{maxRank, maxRankSFN} across all BWPs of the serving cell;

-elseif the higher layer parameter maxRank of pusch-Config of the serving cell is configured and if the higher layer parameter multipanelSchemeSDM is configured, X is given by max{maxRank, 2*maxRankSDM} across all BWPs of the serving cell;

-otherwise, X is given by the maximum number of layers for PUSCH supported by the UE for the serving cell;

-maximum number of layers for one TB for DL-SCH/PCH is given by the minimum of X and 4, where:

-if the higher layer parameter maxMIMO-Layers of PDSCH-ServingCellConfig of the serving cell is configured, X is given by that parameter;

-otherwise, X is given by the maximum number of layers for PDSCH supported by the UE for the serving cell;

-if the higher layer parameter mcs-Table-r17 or mcs-TableDCI-1-2-r17 given by a pdsch-Config for at least one DL BWP of the serving cell is set to 'qam1024', maximum modulation order  is assumed for DL-SCH, except if the UE indicated support for pdsch-1024QAM-2MIMO-FR1-r17 and X > 2, maximum modulation order  is assumed for DL-SCH, else if the higher layer parameter mcs-Table or mcs-TableDCI-1-2 given by a pdsch-Config for at least one DL BWP of the serving cell is set to 'qam256', maximum modulation order  is assumed for DL-SCH; otherwise a maximum modulation order  is assumed for DL-SCH; Qm=10Qm=8

-if the higher layer parameter mcs-Table or mcs-TableTransformPrecoder or mcs-TableDCI-0-2 or mcs-TableTransformPrecoderDCI-0-2 given by a pusch-Config or the higher layer parameter mcs-Table or mcs-TableTransformPrecoder given by configuredGrantConfig for at least one UL BWP of the serving cell is set to 'qam256', maximum modulation order  is assumed for UL-SCH; otherwise a maximum modulation order  is assumed for UL-SCH;

-maximum coding rate of 948/1024;

- is given by Table 5.4.2.1-1, where the value of  for DL-SCH is determined according to the initial downlink bandwidth part if there is no other downlink bandwidth part configured to the UE;

-;

- is the number of code blocks of the transport block determined according to Clause 5.2.2.

Table 5.4.2.1-1: Value of

Denoting by  the rate matching output sequence length for the -th coded block, where the value of  is determined as follows:

Set

for  to

if the -th coded block is not scheduled for transmission as indicated by CBGTI according to Clause 5.1.7.2 for DL-SCH and 6.1.5.2 for UL-SCH in [6, TS 38.214]:

;

else

if

;

else

;

end if

;

end if

end for

where:

- is the number of transmission layers that the transport block is mapped onto;

- is the modulation order;

- is the total number of coded bits available for transmission of the transport block;

- if CBGTI is not present in the DCI scheduling the transport block and  is the number of scheduled code blocks of the transport block if CBGTI is present in the DCI scheduling the transport block.

Denote by  the redundancy version number for this transmission ( = 0, 1, 2 or 3), the rate matching output bit sequence , , is generated as follows, where  is given by Table 5.4.2.1-2 according to the value of  and LDPC base graph:

;

;

while

if

;

;

end if

;

end while

Table 5.4.2.1-2: Starting position of different redundancy versions,

## 5.4.2.2Bit interleaving

The bit sequence  is interleaved to bit sequence , according to the following, where the value of  is the modulation order:

for  to

for  to

;

end for

end for

## 5.4.3Rate matching for channel coding of small block lengths

The input bit sequence to rate matching is . The output bit sequence after rate matching is denoted as , where  is the rate matching output sequence length. The bit sequence  is obtained by the following:

for  to

;

end for

## 5.5Code block concatenation

The input bit sequence for the code block concatenation block are the sequences , for  and , where  is the number of rate matched bits for the -th code block. The output bit sequence from the code block concatenation block is the sequence  for .

The code block concatenation consists of sequentially concatenating the rate matching outputs for the different code blocks. Therefore:

Set  and

while

Set

while

end while

end while

## 6Uplink transport channels and control information

## 6.1Random access channel

The sequence index for the random access channel is received from higher layers and is processed according to [4, TS 38.211].

## 6.2Uplink shared channel

## 6.2.1Transport block CRC attachment

Error detection is provided on each UL-SCH transport block through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by, where  is the payload size and  is the number of parity bits. The lowest order information bit  is mapped to the most significant bit of the transport block as defined in Clause 6.1.1 of [TS38.321].

The parity bits are computed and attached to the UL-SCH transport block according to Clause 5.1, by setting  to 24 bits and using the generator polynomial  if ; and by setting  to 16 bits and using the generator polynomial  otherwise.

The bits after CRC attachment are denoted by , where .

## 6.2.2LDPC base graph selection

For initial transmission of a transport block with coding rate  indicated by the MCS index according to Clause 6.1.4.1 in [6, TS 38.214] and subsequent re-transmission of the same transport block, each code block of the transport block is encoded with either LDPC base graph 1 or 2 according to the following:

-if , or if  and , or if , LDPC base graph 2 is used;

-otherwise, LDPC base graph 1 is used,

where  is the payload size as described in Clause 6.2.1.

## 6.2.3Code block segmentation and code block CRC attachment

The bits input to the code block segmentation are denoted by  where  is the number of bits in the transport block (including CRC).

Code block segmentation and code block CRC attachment are performed according to Clause 5.2.2.

The bits after code block segmentation are denoted by, where  is the code block number and  is the number of bits for code block number  according to Clause 5.2.2.

When the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the value of B is no larger than 3840 if  and no larger than 8448 otherwise, where coding rate  is indicated by the MCS index according to Clause 6.1.4.1 in [6, TS 38.214].R≤0.25R

## 6.2.4Channel coding of UL-SCH

Code blocks are delivered to the channel coding block. The bits in a code block are denoted by , where  is the code block number, and  is the number of bits in code block number . The total number of code blocks is denoted by  and each code block is individually LDPC encoded according to Clause 5.3.2.

After encoding the bits are denoted by , where the values of  is given in Clause 5.3.2.

## 6.2.5Rate matching

Coded bits for each code block, denoted as , are delivered to the rate match block, where  is the code block number, and  is the number of encoded bits in code block number . The total number of code blocks is denoted by  and each code block is individually rate matched according to Clause 5.4.2 by setting  if higher layer parameter rateMatching is set to limitedBufferRM and by setting  otherwise, if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1. When the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, each code block is individually rate matched per slot according to Clause 5.4.2 by setting:

- if higher layer parameter rateMatching is set to limitedBufferRM and by setting otherwise;ILBRM=1ILBRM=0

- as the total number of coded bits available for transmission of the transport block in the slot;G

- as given by Table 5.4.2.1-2 according to the value of  and LDPC base graph if the slot is the first slot within the  slots allocated for the transmission of TB processing over multiple slots, and setting if the slot is a slot except for the first one within the  slots, where  is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI,  denotes the index of starting coded bit in the previous slot within the  slots,  is the total number of coded bits available for transmission of the transport block in the previous slot within the  slots assuming no UCI multiplexing, and  denotes the number of skipped filler bits if any in the previous slot within the  slots according to Clause 5.4.2.1 by assuming no UCI multiplexing.k0rvidNsk0=k0'+H+τmodNcb NsNsk0'NsHNsτNs

After rate matching, the bits are denoted by, where is the number of rate matched bits for code block number .

## 6.2.6Code block concatenation

The input bit sequence for the code block concatenation block are the sequences , for  and where  is the number of rate matched bits for the -th code block.

Code block concatenation is performed according to Clause 5.5.

The bits after code block concatenation are denoted by, where  is the total number of coded bits for transmission.

## 6.2.7Data and control multiplexing

In case where there are more than one UL-SCH transport blocks for the PUSCH transmission, the UCI information is multiplexed only on the UL-SCH transport block with highest IMCS value for the initial PUSCH, where IMCS is as defined in Clause 6.1.4.1 in [6, TS 38.214]. In case the two transport blocks have the same IMCS value for the initial PUSCH, the UCI information is multiplexed with data only on the first transport block. The PUSCH for UCI multiplexing in this Clause refers to the UL-SCH transport block for UCI multiplexing.

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedure in this clause 6.2.7 applies by replacing CGUCI with UTO-UCI in all the notations and texts, and replacing "when higher layer parameter cg-UCI-Multiplexing is configured" with "when UTO-UCI and HARQ-ACK are transmitted on a PUSCH".

If a UE would multiplex UEIRI and HARQ-ACK in a PUSCH [5, TS 38.213], the procedure in this clause 6.2.7 applies by replacing CG-UCI with UEIRI in all the notations and texts, and replacing "when higher layer parameter cg-UCI-Multiplexing is configured" with "when UEIRI and HARQ-ACK are transmitted on a PUSCH". UE expects that at most one of CG-UCI, UTO-UCI, or UEIRI to overlap with a PUSCH.

Denote the coded bits for UL-SCH as .

Denote the coded bits for HARQ-ACK or jointly coded bits for HARQ-ACK and CG-UCI when the high layer parameter cg-UCI-Multiplexing is configured, if any, as .

Denote the coded bits for CSI part 1, if any, as .

Denote the coded bits for CSI part 2, if any, as .

Denote the coded bits for CG-UCI without HARQ-ACK, if any, as .g0CG-UCI,  g1CG-UCI,  g2CG-UCI, g3CG-UCI, …, gGCG-UCI-1CG-UCI

Denote the multiplexed data and control coded bit sequence as .

Denote  as the OFDM symbol index of the PUSCH transmission, starting from 0 to , where  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS.

Denote  as the subcarrier index of the PUSCH transmission, starting from 0 to , where  is expressed as a number of subcarriers.

Denote  as the set of resource elements, in ascending order of indices , available for transmission of data in OFDM symbol , for .

Denote  as the number of elements in set . Denote  as the -th element in .

Denote  as the set of resource elements, in ascending order of indices , available for transmission of UCI in OFDM symbol , for . Denote  as the number of elements in set . Denote  as the -th element in . For any OFDM symbol that carries DMRS of the PUSCH, . For any OFDM symbol that does not carry DMRS of the PUSCH, .

If frequency hopping is configured for the PUSCH,

-denote  as the OFDM symbol index of the first OFDM symbol after the first set of consecutive OFDM symbol(s) carrying DMRS in the first hop;

-denote  as the OFDM symbol index of the first OFDM symbol after the first set of consecutive OFDM symbol(s) carrying DMRS in the second hop;

-denote  as the OFDM symbol index of the first OFDM symbol that does not carry DMRS in the first hop;

-denote  as the OFDM symbol index of the first OFDM symbol that does not carry DMRS in the second hop;

-if HARQ-ACK is present for transmission on the PUSCH with UL-SCH or if both HARQ-ACK and CG-UCI are present on the same PUSCH with UL-SCH, let:

- and ;

-if CSI is present for transmission on the PUSCH with UL-SCH, let:

-;

-;

-; and

-;

-if CG-UCI is present for transmission on the PUSCH with UL-SCH and without HARQ-ACK, let:

- and GCG-UCI1=NL∙Qm∙GCG-UCI2∙NL∙QmGCG-UCI2=NL∙Qm∙GCG-UCI2∙NL∙Qm

-if only HARQ-ACK and CSI part 1 are present for transmission on the PUSCH without UL-SCH, let:

-;

-;

-; and

-;

-if HARQ-ACK, CSI part 1 and CSI part 2 are present for transmission on the PUSCH without UL-SCH, let:

-;

-;

-if the number of HARQ-ACK information bits is more than 2,; otherwise,

-;

- if the number of HARQ-ACK information bits is no more than 2, and  otherwise; and

- if the number of HARQ-ACK information bits is no more than 2, and  otherwise;

-if only CSI part 1 and CSI part 2 are present for transmission on the PUSCH without UL-SCH, let:

-;

-;

-; and

-;

-let , and denote ,  as the number of OFDM symbols of the PUSCH in the first and second hop, respectively;

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH;

-;

-;

-.

If frequency hopping is not configured for the PUSCH,

-denote  as the OFDM symbol index of the first OFDM symbol after the first set of consecutive OFDM symbol(s) carrying DMRS;

-denote  as the OFDM symbol index of the first OFDM symbol that does not carry DMRS;

-if HARQ-ACK is present for transmission on the PUSCH or if both HARQ-ACK and CG-UCI are present on the same PUSCH with UL-SCH, let ;

-if CSI is present for transmission on the PUSCH, let  and ;

-if CG-UCI is present for transmission on the PUSCH without HARQ-ACK, let ;GCG-UCI1=GCG-UCI

-let  and .

The multiplexed data and control coded bit sequence  is obtained according to the following:

Step 1:

Set  for ;

Set  for ;

Set  for ;

Set  for ;

if the number of HARQ-ACK information bits to be transmitted on PUSCH is 0, 1 or 2 bits and without CG-UCI:

the number of reserved resource elements for potential HARQ-ACK transmission is calculated according to Clause 6.3.2.4.2.1, by setting ;

denote  as the number of coded bits for potential HARQ-ACK transmission using the reserved resource elements;

if frequency hopping is configured for the PUSCH, let  and ;

if frequency hopping is not configured for the PUSCH, let ;

denote  as the set of reserved resource elements for potential HARQ-ACK transmission, in OFDM symbol , for ;

Set ;

Set ;

for ;

for  to

;

while

if

if

;

;

end if

if

;

;

end if

for  to

;

end for

end if

;

end while

end for

else

for ;

end if

Denote  as the number of elements in .

Step 2:

if HARQ-ACK is present for transmission on the PUSCH and the number of HARQ-ACK information bits is more than 2 or if both HARQ-ACK and CG-UCI are present on the same PUSCH with UL-SCH:

Set ;

Set ;

Set ;

for  to

;

while

if

if

;

;

end if

if

;

;

end if

for  to

;

for  to

;

;

;

end for

end for

;

for  to

;

end for

;

;

;

;

end if

;

end while

end for

end if

Step 2A:

If CG-UCI is present for transmission on the PUSCH without HARQ-ACK:

Set ;mcountCG-UCI1=0

Set ;mcountCG-UCI2=0

Set ;mcount,allCG-UCI=0

for  to i=1NhopPUSCH

;l=l(i)

while () mcountCG-UCIi<GCG-UCIi

if  MscUCIl>0

if GCG-UCI(i) -mcountCG-UCI1≥MscUCIl.NL.Qm

;d=1

;mcountRE=MscUCIl

end if

if GCG-UCI(i) -mcountCG-UCI1<MscUCIl.NL.Qm

;d=MscUCIl.NL.QmGCG-UCI(i) -mcountCG-UCIi

;mcountRE=GCG-UCI(i) -mcountCG-UCIiNL.Qm

end if

for  to  j=0mcountRE-1

;k=ΦlUCI(j.d)

for  to v=0NL.Qm-1

;gl,k,v=gmcount,allCG-UCICG-UCI

;mcount,allCG-UCI=mcount,allCG-UCI+1

;mcountCG-UCIi=mcountCG-UCIi+1

end for

end for

;Φl,tmpUCI=∅

for  to j=0mcountRE-1

;Φl,tmpUCI=Φl,tmpUCI∪ΦlUCI(j.d)

end for

;ΦlUCI=ΦlUCI\Φl,tmpUCI

;ΦlUL-SCH=ΦlUL-SCH\Φl,tmpUCI

;MscUCIl=ΦlUCI

;MscUL-SCHl=ΦlUL-SCH

end if

;l=l+1

end while

end for

end if

Step 3:

if CSI is present for transmission on the PUSCH:

Set ;

Set ;

Set ;

for  to

;

while

;

end while

while

if

if

;

;

end if

if

;

;

end if

;

for  to

;

for  to

;

;

;

end for

end for

;

for  to

;

end for

;

;

;

;

end if

;

end while

end for

Set ;

Set ;

Set ;

for  to

;

while

;

end while

while

if

if

;

;

end if

if

;

;

end if

for  to

;

for  to

;

;

;

end for

end for

;

for  to

;

end for

;

;

;

;

end if

;

end while

end for

end if

Step 4:

if UL-SCH is present for transmission on the PUSCH:

Set ;

for  to

if

for  to

;

for  to

;

;

end for

end for

end if

end for

end if

Step 5:

if HARQ-ACK is present for transmission on the PUSCH without CG-UCI and the number of HARQ-ACK information bits is no more than 2:

Set ;

Set ;

Set ;

for  to

;

while

if

if

;

;

end if

if

;

;

end if

for  to

;

for  to

;

;

;

end for

end for

end if

;

end while

end for

end if

Step 6:

Set ;

for  to

for  to

;

for  to

;

;

end for

end for

end for

## 6.3Uplink control information

## 6.3.1Uplink control information on PUCCH

The procedure in this clause applies to PUCCH formats 2/3/4.

The following clauses 6.3.1.2, 6.3.1.3 and 6.3.1.5 apply regardless of whether the higher layer parameter uci-MuxWithDiffPrio is configured or not. The following clauses 6.3.1.1, 6.3.1.4 and 6.3.1.6 apply by assuming uci-MuxWithDiffPrio is not configured, or uci-MuxWithDiffPrio is configured and the UCIs for transmission on a PUCCH are of the same priority index, unless stated otherwise.

If the UE is configured with a PUCCH-SCell, uci-MuxWithDiffPrio is replaced by uci-MuxWithDiffPrioSecondaryPUCCHgroup for the secondary PUCCH group in this clause.

If UEIRI is transmitted on a PUCCH, the procedure in this clause 6.3.1 applies by replacing SR with UEIRI in all the notations and texts, when applicable.

If joint indication information for SR and UEIRI as given by Clause 9.2.5.1 of [5, TS38.213] is transmitted on a PUCCH, the procedure in this clause 6.3.1 applies assuming SR representing the joint indication information for SR and UEIRI in all the notations and texts, when applicable.

## 6.3.1.1UCI bit sequence generation

## 6.3.1.1.1HARQ-ACK/SR only

If only HARQ-ACK bits are transmitted on a PUCCH, the UCI bit sequence  is determined by setting  for  and , where the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS38.213].

If only HARQ-ACK and SR bits are transmitted on a PUCCH, the UCI bit sequence  is determined by setting  for ,  for , and , where the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS 38.213], and the SR bit sequence  is given by Clause 9.2.5.1 of [5, TS 38.213].ai=oi-OACKSR

## 6.3.1.1.2CSI only

If cqi-BitsPerSubband is configured, this Clause 6.3.1.1.2 applies by taking Subband CQI as Subband differential CQI and replacing the corresponding number of bits 2 by 4.

If CSI-ReportSubConfig is configured, for a corresponding CSI sub-report, the bitwidth of a CSI field of the CSI sub-report is determined following the procedure in this clause 6.3.1.1.2 by taking configurations in CSI-ReportSubConfig when applicable. If CSI-ReportSubConfig configures a list of CSI-RS resource IDs, for the determination of the bitwidth of a CRI field, the value of  is the number of CSI-RS resources configured in the corresponding CSI-ReportSubConfig.KsCSI-RS

The bitwidth for PMI of codebookType=typeI-SinglePanel with 2 CSI-RS ports is 2 for Rank=1 and 1 for Rank=2, according to Clause 5.2.2.2.1 in [6, TS 38.214].

The bitwidth for PMI of codebookType=typeI-SinglePanel with more than 2 CSI-RS ports is provided in Table 6.3.1.1.2-1, where the values of and  are given by Clause 5.2.2.2.1 in [6, TS 38.214].

Table 6.3.1.1.2-1: PMI of codebookType=typeI-SinglePanel

The bitwidth for PMI of codebookType=typeI-SinglePanel-r19 is provided in Table 6.3.1.1.2-1A/1B for typeI-codebookMode=ModeA and typeI-codebookMode=ModeB respectively, where the values of  and  are given by Clause 5.2.2.2.1a in [6, TS 38.214].(N1, N2)(O1, O2)

Table 6.3.1.1.2-1A: PMI of codebookType=typeI-SinglePanel-r19 and typeI-codebookMode=ModeA

Table 6.3.1.1.2-1B: PMI of codebookType=typeI-SinglePanel-r19 and typeI-codebookMode=ModeB

The bitwidth for PMI of codebookType= typeI-MultiPanel is provided in Table 6.3.1.1.2-2, where the values of and  are given by Clause 5.2.2.2.2 in [6, TS 38.214].

Table 6.3.1.1.2-2: PMI of codebookType= typeI-MultiPanel

The bitwidth for PMI of codebookType= typeI-MultiPanel-r19 is provided in Table 6.3.1.1.2-2A, where the values of    and  are given by Clause 5.2.2.2.2a in [6, TS 38.214].(Ng, N1, N2)(O1, O2)

Table 6.3.1.1.2-2A: PMI of codebookType= typeI-MultiPanel-r19

The bitwidth for PMI with 1 CSI-RS port is 0.

The bitwidth for RI/LI/CQI/CRI of codebookType=typeI-SinglePanel or reportQuantity set to 'cri-RI-CQI' or 1 CSI-RS port is provided in Table 6.3.1.1.2-3.

Table 6.3.1.1.2-3: RI, LI, CQI, and CRI of codebookType=typeI-SinglePanel, orreportQuantity set to 'cri-RI-CQI', or 1 CSI-RS port

in Table 6.3.1.1.2-3 is the number of allowed rank indicator values according to Clause 5.2.2.2.1 [6, TS 38.214].  is the value of the rank. The value of  is the number of CSI-RS resources in the corresponding resource set. The values of the rank indicator field are mapped to allowed rank indicator values with increasing order, where '0' is mapped to the smallest allowed rank indicator value. For higher layer parameter reportQuantity set to 'cri-RI-CQI', the values of the rank indicator field are mapped to rank indicator values with increasing order, where '0' is mapped to rank-1.

Table 6.3.1.1.2-3A: RI, LI, CQI, and CRI associated with one CSI-RS resource pair andcsi-ReportMode= Mode 1 or Mode 2

Table 6.3.1.1.2-3B: RI, LI, CQI, and CRI associated with one CSI-RS resource andcsi-ReportMode= Mode 1 or Mode 2

in Table 6.3.1.1.2-3A is the number of allowed rank combination indicator values associated with one CSI-RS resource pair according to Clause 5.2.1.4.2 [6, TS 38.214]. The values of the rank combination indicator field are mapped to allowed rank combinations in the following order: {1,1}, {1,2}, {2,1},{2,2}, where '0' is mapped to the first allowed rank combination.  and  are the values of the first and the second rank associated with two CSIRS resources of the CSI-RS resource pair respectively.nRI,NCJTv1v2

in Table 6.3.1.1.2-3B is the number of allowed rank indicator values associated with one CSI-RS resource according to Clause 5.2.1.4.2 [6, TS 38.214]. v is the value of the rank associated with the CSI-RS resource. The values of the rank indicator field are mapped to allowed rank indicator values with increasing order, where '0' is mapped to the smallest allowed rank indicator value.nRI, sTRP

The value of N in Table 6.3.1.1.2-3A and Table 6.3.1.1.2-3B is the number of CSI-RS resource pairs configured within a CSI-RS resource set. The values of M1 and M2 in Table 6.3.1.1.2-3A and Table 6.3.1.1.2-3B are given by

-If sharedCMR = "Enabled", M1 = K1 and M2 = K2

-If sharedCMR is absent and N = 1, M1 = K1 - 1 and M2 = K2 - 1

-If sharedCMR is absent and N = 2,

-M1 = K1 - 2 and M2 = K2 - 2, if the two resource pairs do not share any CSI-RS resource

-M1 = K1 - 1 and M2 = K2 - 2, if the two resource pairs share the same CSI-RS resource from the first CSI-RS resource group

-M1 = K1 - 2 and M2 = K2 - 1, if the two resource pairs share the same CSI-RS resource from the second CSI-RS resource group

where the values of K1 and K2 are the numbers of CSI-RS resources in the first and second CSI-RS resource groups within the CSI-RS resource set respectively.

The bitwidth for RI/LI/CQI/CRI of codebookType=typeI-SinglePanel-r19 is provided in Table 6.3.1.1.2-3C.

Table 6.3.1.1.2-3C: RI, LI, CQI, and CRI of codebookType=typeI-SinglePanel-r19

The bitwidth for RI/LI/CQI/CRI of codebookType= typeI-MultiPanel or codebookType=typeI-MultiPanel-r19 is provided in Table 6.3.1.1.2-4.

Table 6.3.1.1.2-4: RI, LI, CQI, and CRI of codebookType=typeI-MultiPanel or codebookType=typeI-MultiPanel-r19

The bitwidth for RI/LI/CQI of codebookType= typeII or codebookType=typeII-PortSelection is provided in Table 6.3.1.1.2-5.

Table 6.3.1.1.2-5: RI, LI, and CQI of codebookType=typeII or typeII-PortSelection

The bitwidth for CRI, SSBRI, RSRP, differential RSRP, and CapabilityIndex are provided in Table 6.3.1.1.2-6.

Table 6.3.1.1.2-6: CRI, SSBRI, RSRP, and CapabilityIndex

The bitwidth for CRI, SSBRI, SINR, differential SINR, and CapabilityIndex are provided in Table 6.3.1.1.2-6A.

Table 6.3.1.1.2-6A: CRI, SSBRI, SINR, and CapabilityIndex

The bitwidth for MRI and CLI-RSSI are provided in Table 6.3.1.1.2-6B.

Table 6.3.1.1.2-6B: Bitwidth for MRI and CLI-RSSI

The bitwidth for predicted CRI, predicted SSBRI, predicted RSRP, differential predicted RSRP are provided in Table 6.3.1.1.2-6C.

Table 6.3.1.1.2-6C: Predicted CRI, Predicted SSBRI, Predicted RSRP and Differential predicted RSRP

The bitwidth for RS-PAI is provided in Table 6.3.1.1.2-6D.

Table 6.3.1.1.2-6D: RS-PAI

If CSI-ReportSubConfig is configured, for a corresponding CSI sub-report, the mapping order of CSI fields of one CSI sub-report is determined following the procedure in this clause 6.3.1.1.2, by replacing CSI report #n in the following Tables 6.3.1.1.2-7, 6.3.1.1.2-9 and 6.3.1.1.2-10 with CSI sub-report #n, and taking only Tables 6.3.1.1.2-1/1A/1B/2/2A/3/4 for the determination of the bitwidth of a CSI field.

Table 6.3.1.1.2-7: Mapping order of CSI fields of one CSI report,pmi-FormatIndicator=widebandPMI and cqi-FormatIndicator=widebandCQI or reportQuantityset to 'cri-RI-CQI' and cqi-FormatIndicator=widebandCQI

The number of zero padding bits  in Table 6.3.1.1.2-7 is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:

- and  is the set of rank values  that are allowed to be reported;

-, where  is the reported rank;

-For 2 CSI-RS ports, ;

-For more than 2 CSI-RS ports, ;

-if PMI is reported,  and ; otherwise, ;

-if PMI  is reported,  is obtained according to Tables 6.3.1.1.2-1/1A/1B/2/2A; otherwise, ;

-if PMI  is reported,  is obtained according to Tables 6.3.1.1.2-1/1A/1B/2/2A; otherwise, ;

-if CQI is reported,  is obtained according to Tables 6.3.1.1.2-3/3C/4; otherwise, ;

-if LI is reported,  is obtained according to Tables 6.3.1.1.2-3/3C/4; otherwise, .

Table 6.3.1.1.2-7A: Mapping order of CSI fields of one CSI report, pmi-FormatIndicator=widebandPMI, cqi-FormatIndicator=widebandCQI, csi-ReportMode= Mode 1 and numberOfSingleTRP-CSI-Mode1=0

The number of zero padding bits  in Table 6.3.1.1.2-7A is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OPOP=Nmax-Nreported

- and  is the set of rank combination values of  that are allowed to be reported;Nmax=maxr∈SRankB(r) SRankr={r1,r2}

- where R is the reported rank combination;Nreported=B(R)

-For 2 CSI-RS ports, ;Br=NPMI(r1)+NPMI(r2)+NCQIr+NLI(r1)+NLI(r2)

-For more than 2 CSI-RS ports, ; Br=NPMI,i1(r1)+NPMI,i1(r2)+NPMI,i2(r1)+NPMI,i2(r2)+NCQIr+NLI(r1)+NLI(r2)

-if PMI is reported,  and  ; otherwise,;NPMI1=2NPMI2=1 NPMI=0

-if PMI  is reported, and  are obtained according to Tables 6.3.1.1.2-1; otherwise, ;i1 NPMI,i1(r1)NPMI,i1(r2)NPMI,i1=0

-if PMI   is reported,  and  are obtained according to Tables 6.3.1.1.2-1; otherwise, ;i2NPMI,i2(r1)NPMI,i2(r2) NPMI,i2=0

-if CQI is reported,  is obtained according to Tables 6.3.1.1.2-3A; otherwise,;NCQIr NCQIr=0

-if LI is reported,  and  are obtained according to Tables 6.3.1.1.2-3A; otherwise , .NLI(r1)NLI(r2)NLI=0

Table 6.3.1.1.2-7B: Mapping order of CSI fields of one CSI report configured with valueOfM,pmi-FormatIndicator=widebandPMI and cqi-FormatIndicator=widebandCQI

The number of zero padding bits  for k-th reported CRI in Table 6.3.1.1.2-7B is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OP,kOP,k=Nmax-Nreported,k

-, where Q is the set of CRIs corresponding to the Ks resources and  is the maximum payload size of associated CSI fields for the j-th CRI;Nmax= maxj∈Q  (Nmax,j)Nmax,j

-, where  is the payload size of RI field for the j-th CRI,  and  is the set of rank values that are allowed to be reported for the j-th CRI obtained according to Table 6.3.1.1.2-3;Nmax,j=NRI(j)+maxrj∈Srank,jB(rj)NRI(j)Srank,jrj

-, where  is the reported rank for the k-th CRI;Nreported,k= NRI(k)+B(Rk)Rk

-For 2 CSI-RS ports, ;Br=NPMIr+NCQIr+NLIr

-For more than 2 CSI-RS ports, ;Br=NPMI,i1r+NPMI,i2r+NCQIr+NLIr

-if PMI is reported,  and ; otherwise, ;NPMI1=2NPMI2=1NPMIr=0

-if PMI  is reported,  is obtained according to Table 6.3.1.1.2-1; otherwise, ;i1NPMI,i1rNPMI,i1r=0

-if PMI  is reported,  is obtained according to Table 6.3.1.1.2-1; otherwise, ;i2NPMI,i2rNPMI,i2r=0

-if CQI is reported,  is obtained according to Table 6.3.1.1.2-3; otherwise, ;NCQIrNCQIr=0

-if LI is reported,  is obtained according to Table 6.3.1.1.2-3; otherwise, .NLIrNLIr=0

Table 6.3.1.1.2-8: Mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP or CRI/RSRP/CapabilityIndex or SSBRI/RSRP/CapabilityIndex reporting, or mapping order of CSI fields of one report for inter-cell SSBRI/RSRP reporting

Table 6.3.1.1.2-8A: Mapping order of CSI fields of one report for CRI/SINR or SSBRI/SINR or CRI/SINR/CapabilityIndex or SSBRI/SINR/CapabilityIndex reporting

Table 6.3.1.1.2-8B: Mapping order of CSI fields of one report for group-based CRI/RSRP or SSBRI/RSRP reporting

where the 1-bit resource set indicator, with value of 0 or 1, indicates the 1st or the 2nd channel measurement resource set respectively, from which CRI or SSBRI #1 of 1st resource group is reported from; and all remaining resource groups, if reported, follow the same mapping order as the 1st resource group where CRI or SSBRI #1 of all remaining resource groups is reported from the indicated channel measurement resource set. For all reported resource groups, CRI or SSBRI #1 and CRI or SSBRI #2 are reported from different channel measurement resource sets.

Table 6.3.1.1.2-8C: Mapping order of CSI fields of one report for SSBRI/RSRP or CRI/RSRP reporting for L1/L2triggered mobility

Table 6.3.1.1.2-8D: Mapping order of CSI fields of one report for MRI/CLI-RSSI reporting

Table 6.3.1.1.2-8E: Mapping order of CSI fields of one report for Predicted CRI/RSRP or Predicted SSBRI/RSRP reporting

Table 6.3.1.1.2-8F: Mapping order of CSI fields of one report for Time instance indicator/Predicted CRI/Predicted RSRP or Time instance indicator/Predicted SSBRI/Predicted RSRP reporting

Table 6.3.1.1.2-8G: Mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP reporting, if nrofReportedRS is configured

Table 6.3.1.1.2-8H: Mapping order of CSI fields of one report for RS-PAI reporting

Table 6.3.1.1.2-9: Mapping order of CSI fields of one CSI report, CSI part 1, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

Table 6.3.1.1.2-9A: Mapping order of CSI fields of one CSI report, CSI part 1, csi-ReportMode= Mode 1

Table 6.3.1.1.2-9B: Mapping order of CSI fields of one CSI report, CSI part 1, csi-ReportMode= Mode 2

The number of zero padding bits  in Table 6.3.1.1.2-9B is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OPOP=Nmax-Nreported(R)

-. is the set of rank and rank combination values r that are allowed to be reported.  is obtained according to Tables 6.3.1.1.2-3A/3B for rank combination indicator and rank indicator respectively.Nmax=maxr∈SRankN(r) SRank Nr

-is obtained according to Tables 6.3.1.1.2-3A for rank combination indicator and R is the reported rank combination.Nreported R

- is obtained according to Tables 6.3.1.1.2-3B for rank indicator and R is the reported rank.Nreported (R)

Table 6.3.1.1.2-9C: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 1, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

The number of zero padding bits  in Table 6.3.1.1.2-9C is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OP,kOP,k=Nmax-Nreported,k

-, where S is the set of CRIs corresponding to the Ks resources and  is the payload size of RI field for the i-th CRI obtained according to Table 6.3.1.1.2-3;Nmax=maxi∈SNiNi

- is the payload size of RI field for the k-th CRI obtained according to Table 6.3.1.1.2-3.Nreported,k

Table 6.3.1.1.2-10: Mapping order of CSI fields of one CSI report, CSI part 2 wideband, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

Table 6.3.1.1.2-10A: Mapping order of CSI fields of one CSI report,CSI part 2 wideband, csi-ReportMode= Mode 1

Table 6.3.1.1.2-10B: Mapping order of CSI fields of one CSI report,CSI part 2 wideband, csi-ReportMode= Mode 2

Table 6.3.1.1.2-10C: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 2 wideband, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

Table 6.3.1.1.2-11: Mapping order of CSI fields of one CSI report, CSI part 2 subband,pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

Table 6.3.1.1.2-11A: Mapping order of CSI fields of one CSI report, CSI part 2 subband,csi-ReportMode= Mode 1

Table 6.3.1.1.2-11B: Mapping order of CSI fields of one CSI report, CSI part 2 subband,csi-ReportMode= Mode 2

Table 6.3.1.1.2-11C: Mapping order of CSI fields of one CSI report containing CSI sub-report(s), CSI part 2 subband, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQINnsub

Table 6.3.1.1.2-11D: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 2 subband, pmi-FormatIndicator= subbandPMI or cqi-FormatIndicator=subbandCQI

If none of the CSI reports for transmission on a PUCCH is of two parts, the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-12, are mapped to the UCI bit sequence  starting with . The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to.

Table 6.3.1.1.2-12: Mapping order of CSI reports to UCI bit sequence ,without two-part CSI report(s)

If at least one of the CSI reports for transmission on a PUCCH is of two parts, two UCI bit sequences are generated,  and . The CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-13, are mapped to the UCI bit sequence  starting with . The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to. The CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-14, are mapped to the UCI bit sequence  starting with . The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to . If the length of UCI bit sequence  is less than 3 bits, zeros shall be appended to the UCI bit sequence until its length equals 3.

Table 6.3.1.1.2-13: Mapping order of CSI reports to UCI bit sequence , with two-part CSI report(s)

where CSI report #1, CSI report #2, …, CSI report #n in Table 6.3.1.1.2-13 correspond to the CSI reports in increasing order of CSI report priority values according to Clause 5.2.5 of [6, TS38.214].

Table 6.3.1.1.2-14: Mapping order of CSI reports to UCI bit sequence , with two-part CSI report(s)

where CSI report #1, CSI report #2, …, CSI report #n in Table 6.3.1.1.2-14 correspond to the CSI reports in increasing order of CSI report priority values according to Clause 5.2.5 of [6, TS38.214].

## 6.3.1.1.3HARQ-ACK/SR and CSI

If none of the CSI reports for transmission on a PUCCH is of two parts, the UCI bit sequence  is generated according to the following, where :

-if there is HARQ-ACK for transmission on the PUCCH, the HARQ-ACK bits are mapped to the UCI bit sequence , where  for , the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS38.213], and  is number of HARQ-ACK bits; if there is no HARQ-ACK for transmission on the PUCCH, set ;

-if there is SR for transmission on the PUCCH, set  for , where the SR bit sequence  is given by Clause 9.2.5.1 of [5, TS 38.213]; if there is no SR for transmission on the PUCCH, set ;ai=oi-OACKSR

-the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-12, are mapped to the UCI bit sequence  starting with , where  is the number of CSI bits.

If at least one of the CSI reports for transmission on a PUCCH is of two parts, two UCI bit sequences are generated,  and , according to the following, where  and :

-if there is HARQ-ACK for transmission on the PUCCH, the HARQ-ACK bits are mapped to the UCI bit sequence , where  for , the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS38.213], and  is number of HARQ-ACK bits; if there is no HARQ-ACK for transmission on the PUCCH, set ;

-if there is SR for transmission on the PUCCH, set  for , where the SR bit sequence  is given by Clause 9.2.5.1 of [5, TS 38.213]; if there is no SR for transmission on the PUCCH, set ;ai=oi-OACKSR

-the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-13, are mapped to the UCI bit sequence  starting with , where  is the number of CSI bits in CSI part 1 of all CSI reports;

-the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-14, are mapped to the UCI bit sequence  starting with , where  is the number of CSI bits in CSI part 2 of all CSI reports. If the length of UCI bit sequence  is less than 3 bits, zeros shall be appended to the UCI bit sequence until its length equals 3.

## 6.3.1.1.4UCI with different priority indexes

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1, and SR associated with priority index 1 if any are transmitted on a PUCCH, two UCI bit sequences are generated,  and , according to the following, where  and : a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(2), a1(2), a2(2), a3(2), …,aA(2)-12A(1)=OACK-HP+OSR-HPA(2)=OACK-LP

-the HARQ-ACK bits associated with priority index 1 are mapped to the UCI bit sequence , where   for , the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS 38.213], and  is the number of HARQ-ACK bits associated with priority index 1; a0(1), a1(1), a2(1), a3(1), …,aOACK-HP-11ai(1)=oiACK-HPi=0,1,…,OACK-HP-1o0ACK-HP, o1ACK-HP, …, oOACK-HP-1ACK-HPOACK-HP

-if there is SR associated with priority index 1 for transmission on the PUCCH, set  for  , where the SR bit sequence   is given by Clause 9.2.5.1 of [5, TS 38.213]; if there is no SR associated with priority index 1 for transmission on the PUCCH, set ;ai(1)=oi-OACK-HPSR-HPi=OACK-HP,OACK-HP+1,…,OACK-HP+OSR-HP-1o0SR-HP, o1SR-HP, …,oOSR-HP-1SR-HPOSR-HP=0

-the HARQ-ACK bits associated with priority index 0 are mapped to the UCI bit sequence , where   for , the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS 38.213], and  is the number of HARQ-ACK bits associated with priority index 0.a0(2), a1(2), a2(2), a3(2), …,aOACK-LP-12ai(2)=oiACK-LPi=0,1,…,OACK-LP-1o0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LPOACK-LP

## 6.3.1.2Code block segmentation and CRC attachment

The UCI bit sequence from clause 6.3.1.1 is denoted by , where  is the payload size. The procedure in Clause 6.3.1.2.1 applies for  and the procedure in Clause 6.3.1.2.2 applies for .

## 6.3.1.2.1UCI encoded by Polar code

If the payload size , code block segmentation and CRC attachment is performed according to Clause 5.2.1. If ( and ) or if , ; otherwise , where  is the rate matching output sequence length as given in Clauses 6.3.1.4.1 and 6.3.1.4.3.

If , the parity bits  in Clause 5.2.1 are computed by setting  to 6 bits and using the generator polynomial  in Clause 5.1, resulting in the sequence  where  is the code block number and  is the number of bits for code block number .

If , the parity bits  in Clause 5.2.1 are computed by setting  to 11 bits and using the generator polynomial  in Clause 5.1, resulting in the sequence  where  is the code block number and  is the number of bits for code block number .

## 6.3.1.2.2UCI encoded by channel coding of small block lengths

If the payload size , CRC bits are not attached.

The output bit sequence is denoted by , where  for  and .

## 6.3.1.3Channel coding of UCI

## 6.3.1.3.1UCI encoded by Polar code

Information bits are delivered to the channel coding block. They are denoted by  , where  is the code block number, and  is the number of bits in code block number . The total number of code blocks is denoted by  and each code block is individually encoded by the following:

If , the information bits are encoded via Polar coding according to Clause 5.3.1, by setting , , ,  if  and  if , where  is the rate matching output sequence length as given in Clauses 6.3.1.4.1 and 6.3.1.4.3.

If , the information bits are encoded via Polar coding according to Clause 5.3.1, by setting , , , and .

After encoding the bits are denoted by , where  is the number of coded bits in code block number .

## 6.3.1.3.2UCI encoded by channel coding of small block lengths

Information bits are delivered to the channel coding block. They are denoted by , where  is the number of bits.

The information bits are encoded according to Clause 5.3.3.

After encoding the bits are denoted by , where  is the number of coded bits.

## 6.3.1.4Rate matching

For PUCCH formats 2/3/4, the total rate matching output sequence length  is given by Table 6.3.1.4-1, where  , , and  are the number of symbols carrying UCI for PUCCH formats 2/3/4 respectively; ,  and are the number of PRBs that are determined by the UE for PUCCH formats 2/3/4 transmission respectively according to Clause 9.2 of [5, TS38.213]; and , , and  are the spreading factors for PUCCH format 2, PUCCH format 3, and PUCCH format 4, respectively.NPRBPUCCH,4 NSFPUCCH,2NSFPUCCH,3

Table 6.3.1.4-1: Total rate matching output sequence length

## 6.3.1.4.1UCI encoded by Polar code

The input bit sequence to rate matching is  where  is the code block number, and  is the number of coded bits in code block number .

Table 6.3.1.4.1-1: Rate matching output sequence length

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where  is the number of code blocks for UCI determined according to Clause 6.3.1.2.1 and the value of  is given by Table 6.3.1.4.1-1:

- is the number of bits for HARQ-ACK for transmission on the current PUCCH;

- is the number of bits for SR for transmission on the current PUCCH;

- is the number of bits for CSI part 1 for transmission on the current PUCCH;

- is the number of bits for CSI part 2 for transmission on the current PUCCH;

-if ,  ; otherwise,  is the number of CRC bits determined according to Clause 6.3.1.2.1, where  equals  for "CSI (CSI of two parts)", equals  for "HARQ-ACK, CSI (CSI of two parts)", and equals  for "HARQ-ACK, SR, CSI (CSI of two parts)" respectively in Table 6.3.1.4.1-1;

- is the configured maximum PUCCH coding rate;

- is given by Table 6.3.1.4-1.

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number .

## 6.3.1.4.2UCI encoded by channel coding of small block lengths

The input bit sequence to rate matching is .

The value of  is determined according to Table 6.3.1.4.1-1 by setting .

Rate matching is performed according to Clause 5.4.3 by setting the rate matching output sequence length .

The output bit sequence after rate matching is denoted as .

## 6.3.1.4.3UCI with different priority indexes encoded by Polar code

The following procedure in this clause 6.3.1.4.3 applies if uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and SR associated with priority index 1 if any are transmitted on a PUCCH.

The input bit sequence to rate matching is  where  is the code block number, and  is the number of coded bits in code block number.dr0,dr1,dr2,dr3,…,dr(Nr-1)rNr r

Table 6.3.1.4.3-1: Rate matching output sequence length  for UCIs with different priority indexesEUCI

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where  is the number of code blocks for UCI determined according to Clause 6.3.1.2.1 and the value of  is given by Table 6.3.1.4.3-1:IBIL=1Er=EUCICUCICUCIEUCI

- is the number of bits for HARQ-ACK associated with priority index 1 for transmission on the current PUCCH;OACK-HP

- is the number of bits for SR associated with priority index 1 for transmission on the current PUCCH;OSR-HP

-if , =11; otherwise,  is the number of CRC bits determined according to clause 6.3.1.2.1, where  equals  for the case of "HARQ-ACK of priority index 1, HARQ-ACK of priority index 0", and equals  for the case of "HARQ-ACK of priority index 1, SR of priority index 1, HARQ-ACK of priority index 0" respectively in Table 6.3.1.4.3-1;A≥360LLAOACK-HPOACK-HP+OSR-HP

- is the configured maximum PUCCH coding rate of priority index 1;RUCImax-HP

- is given by Table 6.3.1.4-1.Etot

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number.fr0,fr1,fr2,…,fr(Er-1)Er r

## 6.3.1.4.4UCI with different priority indexes encoded by channel coding of small block lengths

The following procedure in this clause 6.3.1.4.4 applies if uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and SR associated with priority index 1 if any are transmitted on a PUCCH.

The input bit sequence to rate matching is .d0,d1,d2,…,dN-1

The value of  is determined according to Table 6.3.1.4.3-1 by setting =0.EUCIL

Rate matching is performed according to Clause 5.4.3 by setting the rate matching output sequence length . E=EUCI

The output bit sequence after rate matching is denoted as .f0,f1,f2,…,fE-1

## 6.3.1.5Code block concatenation

The input bit sequence for the code block concatenation block are the sequences, for  and where  is the number of rate matched bits for the -th code block.

Code block concatenation is performed according to Clause 5.5.

The bits after code block concatenation are denoted by, where  with the values of  and  given in Clauses 6.3.1.4.1 and 6.3.1.4.3. Let  be the total number of coded bits for transmission and . Set  for .

## 6.3.1.6Multiplexing of coded UCI bits to PUCCH

If CSI of two parts or UCIs with different priority indexes are transmitted on a PUCCH, the coded bits corresponding to UCI bit sequence  is denoted by and the coded bits corresponding to UCI bit sequence  is denoted by .

For PUCCH format 2 when uci-MuxWithDiffPrio is configured, the coded bit sequence  is generated for UCIs with different priority indexes by setting  for , and setting  for .g0,g1,g2,g3,…,gG-1gi=gi(1)i=0,1,…,G1-1gi=gi-G1(2)i=G1,G1+1,…,G1+G2-1

For PUCCH format 3/4, the coded bit sequence , where , is generated according to the following.

Table 6.3.1.6-1: PUCCH DMRS and UCI symbols

Denote  as UCI OFDM symbol index. Denote  as the number of elements in UCI symbol indices set  for , where  and  are given by Table 6.3.1.6-1 according to the PUCCH duration and the PUCCH DMRS configuration. Denote  as the number of OFDM symbols carrying UCI in the PUCCH. Denote  as the modulation order of the PUCCH.

For PUCCH formats 3/4, set  , where  is the number of PRBs that is determined by the UE for the corresponding PUCCH format transmission according to Clause 9.2 of [5, TS 38.213], and  is the spreading factor for the corresponding PUCCH format [4, TS 38.211], where .NUCIsymbol=12⋅NPRBPUCCH,s/NSFPUCCH,sNPRBPUCCH,sNSFPUCCH,ss∈3,4

Find the smallest such that .

Set ;

Set ;

Set ;

Set ;

for  to

if

for  to

for  to

;

;

end for

end for

elseif

if

;

else

;

end if

;

for  to

for  to

;

;

end for

end for

for  to

for  to

;

;

end for

end for

else

for  to

for  to

;

;

end for

end for

end if

end for

Set

for  to

for  to

for  to

;

;

end for

end for

end for

## 6.3.2Uplink control information on PUSCH

The following clauses 6.3.2.2, 6.3.2.3, and 6.3.2.5 apply regardless of whether the higher layer parameter uci-MuxWithDiffPrio is configured or not. The following clauses 6.3.2.1, 6.3.2.4, and 6.3.2.6 apply by assuming uci-MuxWithDiffPrio is not configured, or uci-MuxWithDiffPrio is configured and the UCIs for transmission on a PUSCH are of the same priority index, unless stated otherwise.

If the UE is configured with a PUCCH-SCell, uci-MuxWithDiffPrio is replaced by uci-MuxWithDiffPrioSecondaryPUCCHgroup for the secondary PUCCH group in this clause.

## 6.3.2.1UCI bit sequence generation

## 6.3.2.1.1HARQ-ACK

If HARQ-ACK bits are transmitted on a PUSCH, the UCI bit sequence  is determined as follows:

-If UCI is transmitted on PUSCH without UL-SCH and the UCI includes CSI part 1 without CSI part 2,

-if there is no HARQ-ACK bit given by Clause 9.1 of [5, TS 38.213], set , , and ;

-if there is only one HARQ-ACK bit  given by Clause 9.1 of [5, TS 38.213], set , , and ;

-otherwise, set  for  and , where the HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS 38.213].

## 6.3.2.1.2CSI

If cqi-BitsPerSubband is configured, this Clause 6.3.2.1.2 applies by taking Subband CQI as Subband differential CQI and replacing the corresponding number of bits 2 by 4.

If CSI-ReportSubConfig is configured, for a corresponding CSI sub-report, the bitwidth of a CSI field of the CSI sub-report is determined following the procedure in this clause 6.3.2.1.2 by taking configurations in CSI-ReportSubConfig when applicable. If CSI-ReportSubConfig configures a list of CSI-RS resource IDs, for the determination of the bitwidth of a CRI field, the value of  is the number of CSI-RS resources configured in the corresponding CSI-ReportSubConfig.KsCSI-RS

The bitwidth for PMI of codebookType=typeI-SinglePanel, codebookType=typeI-SinglePanel-r19, codebookType=typeI-MultiPanel and codebookType=typeI-MultiPanel-r19 is specified in Clause 6.3.1.1.2.

The bitwidth for RI/LI/CQI/CRI of codebookType=typeI-SinglePanel, codebookType=typeI-SinglePanel-r19, codebookType=typeI-MultiPanel and codebookType=typeI-MultiPanel-r19 is specified in Clause 6.3.1.1.2.

The bitwidth for PMI/RI/LI/CQI/CRI with 1 CSI-RS port is specified in Clause 6.3.1.1.2.

The bitwidth for PMI of codebookType=typeII is provided in Tables 6.3.2.1.2-1, where the values of , , , , , , and  are given by Clause 5.2.2.2.3 in [6, TS 38.214].

Table 6.3.2.1.2-1: PMI of codebookType= typeII

The bitwidth for PMI of codebookType=typeII-r16 and codebookType=etypeII-r19 is provided in Tables 6.3.2.1.2-1A, where the values of , , , , , and  are given by Clause 5.2.2.2.5 and 5.2.2.2.5a in [6, TS 38.214].(N1, N2)(O1, O2)LKNZN3Mll=1,…, υ

Table 6.3.2.1.2-1A: PMI of codebookType= typeII-r16 or codebookType=etypeII-r19

The bitwidth for PMI of codebookType=typeII-CJT is provided in Tables 6.3.2.1.2-1B, where the values of , , , , , , ,  and  are given by Clause 5.2.2.2.8 in [6, TS 38.214].(N1, N2)(O1, O2)O3KNZN3N0Lnσ(n)Mll=1,…, υ

Table 6.3.2.1.2-1B: PMI of codebookType= typeII-CJT

The bitwidth for PMI of codebookType=typeII-Doppler and codebookType=typeII-Doppler-r19 is provided in Tables 6.3.2.1.2-1C, where the values of , , , , , , Q and  are given by Clause 5.2.2.2.10 and 5.2.2.2.11a in [6, TS 38.214].(N1, N2)(O1, O2)LKNZN3N4Mll=1,…, υ

Table 6.3.2.1.2-1C: PMI of codebookType=typeII-Doppler or codebookType=typeII-Doppler-r19

The bitwidth for PMI of codebookType= typeII-PortSelection is provided in Tables 6.3.2.1.2-2, where the values of , , , , , , and  are given by Clause 5.2.2.2.4 in [6, TS 38.214].

Table 6.3.2.1.2-2: PMI of codebookType= typeII-PortSelection

The bitwidth for PMI of codebookType=typeII-PortSelection-r16 is provided in Tables 6.3.2.1.2-2A, where the values of ,, , , , and   are given by Clause 5.2.2.2.6 in [6, TS 38.214].PCSI-RS dLKNZN3Mll=1,…, υ

Table 6.3.2.1.2-2A: PMI of codebookType= typeII-PortSelection-r16

The bitwidth for PMI of codebookType=typeII-PortSelection-r17 and codebookType=typeII-FePortSelection-r19 is provided in Tables 6.3.2.1.2-2B, where the values of ,, , ,  and  are given by Clause 5.2.2.2.7 and 5.2.2.2.9a in [6, TS 38.214].PCSI-RS K1KNZN3NM

Table 6.3.2.1.2-2B: PMI of codebookType= typeII-PortSelection-r17 and typeII-FePortSelection-r19

If CSI-ReportSubConfig is configured, for a corresponding CSI sub-report, the mapping order of CSI fields of one CSI sub-report is determined following the procedure in this clause 6.3.2.1.2, by replacing CSI report #n in the following Tables 6.3.2.1.2-3 and 6.3.2.1.2-4 with CSI sub-report #n, and taking only Tables 6.3.1.1.2-1/1A/1B/2/2A/3/4 for the determination of the bitwidth of a CSI field.

The bitwidth for PMI of codebookType=typeII-CJT-PortSelection is provided in Tables 6.3.2.1.2-2C, where the values of ,,, , ,  and  are given by Clause 5.2.2.2.9 in [6, TS 38.214].PCSI-RS K1,n KNZN3NMσn

Table 6.3.2.1.2-2C: PMI of codebookType= typeII-CJT-PortSelection

The bitwidth for PMI of codebookType=typeII-Doppler-PortSelection is provided in Tables 6.3.2.1.2-2D, where the values of ,, , ,  and  are given by Clause 5.2.2.2.11 in [6, TS 38.214].PCSI-RS K1KNZN3NM

Table 6.3.2.1.2-2D: PMI of codebookType= typeII-Doppler-PortSelection

The bitwidth for MRI and SRS-RSRP are provided in Table 6.3.2.1.2-2E.

Table 6.3.2.1.2-2E: Bitwidth for MRI and SRS-RSRP

For CSI on PUSCH, two UCI bit sequences are generated,  and . The CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the UCI bit sequence  starting with . The CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-7, are mapped to the UCI bit sequence  starting with .

The mapping order of CSI fields of one report for CSI reporting for L1/L2triggered mobility and handover as defined in Clause 5.2.4a of [6, TS 38.214] is provided in Table 6.3.1.1.2-7 by taking only Tables 6.3.1.1.2-1/3 for the determination of the bitwidth of a CSI field. The mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP or CRI/RSRP/CapabilityIndex or SSBRI/RSRP/CapabilityIndex reporting is provided in Table 6.3.1.1.2-8. The mapping order of CSI fields of one report for inter-cell SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8. The mapping order of CSI fields of one report for CRI/SINR or SSBRI/SINR or CRI/SINR/CapabilityIndex or SSBRI/SINR/CapabilityIndex reporting is provided in Table 6.3.1.1.2-8A. The mapping order of CSI fields of one report for group-based CRI/RSRP or SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8B. The mapping order of CSI fields of one report for SSBRI/RSRP or CRI/RSRP reporting for L1/L2triggered mobility is provided in Table 6.3.1.1.2-8C. The mapping order of CSI fields of one report for MRI/CLI-RSSI is provided in Table 6.3.1.1.2-8D. The mapping order of CSI fields of one report for predicted CRI/RSRP or predicted SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8E. The mapping order of CSI fields of one report for time instance indicator/predicted CRI/predicted RSRP or time instance indicator/predicted SSBRI/predicted RSRP reporting is provided in Table 6.3.1.1.2-8F. The mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP if nrofReportedRS is configured is provided in Table 6.3.1.1.2-8G. The mapping order of CSI fields of one report for RS-PAI is provided in Table 6.3.1.1.2-8H. The procedure in clause 6.3.2 described for CSI part 1 is also applicable for one report for CRI/RSRP, SSBRI/RSRP, predicted CRI/RSRP, predicted SSBRI/RSRP, time instance indicator/predicted CRI/predicted RSRP, time instance indicator/predicted SSBRI/predicted RSRP, RS-PAI, CSI-PAI, CRI/SINR, SSBRI/SINR, MRI/SRS-RSRP, MRI/CLI-RSSI reporting, CSI reporting for L1/L2triggered mobility, CSI reporting for handover, TDCP reporting, delay offset reporting, frequency offset reporting, both delay offset and frequency offset reporting, and phase offset reporting.

Table 6.3.2.1.2-3: Mapping order of CSI fields of one CSI report, CSI part 1

Table 6.3.2.1.2-3A: Mapping order of CSI fields of one CSI report, CSI part 1, csi-ReportMode= Mode 1

Table 6.3.2.1.2-3B: Mapping order of CSI fields of one CSI report, CSI part 1, csi-ReportMode= Mode 2

The number of zero padding bits  in Table 6.3.2.1.2-3B is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OPOP=Nmax-Nreported(R)

-. is the set of rank and rank combination values r that are allowed to be reported.  is obtained according to Tables 6.3.1.1.2-3A/3B for rank combination indicator and rank indicator respectively.Nmax=maxr∈SRankN(r) SRank Nr

-is obtained according to Tables 6.3.1.1.2-3A for rank combination indicator and R is the reported rank combinationNreported (R)

- is obtained according to Tables 6.3.1.1.2-3B for rank indicator and R is the reported rank Nreported (R)

Table 6.3.2.1.2-3C: Mapping order of CSI fields of one CSI report for reportQuantity=tdcp

Table 6.3.2.1.2-3D: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 1

The number of zero padding bits  in Table 6.3.1.1.2-3D is 0 for 1 CSI-RS port and  for more than 1 CSI-RS port, where:OP,kOP,k=Nmax-Nreported,k

-, where S is the set of CRIs corresponding to the Ks-MR resources and  is the payload size of RI field for the i-th CRI obtained according to Table 6.3.2.1.2-8C or 6.3.2.1.2-8D;Nmax=maxi∈SNiNi

- is the payload size of RI field for the k-th CRI obtained according to Table 6.3.2.1.2-8C or 6.3.2.1.2-8D.Nreported,k

Table 6.3.2.1.2-3E: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-Dd

Table 6.3.2.1.2-3F: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-F

Table 6.3.2.1.2-3G: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-Dd-F

Table 6.3.2.1.2-3H: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-P

Table 6.3.2.1.2-3I: Mapping order of CSI fields of one report for CSI report configuration indicator/CRI/RSRP/Condition met indicator, or CSI report configuration indicator/SSBRI/RSRP/Condition met indicator

The number of zero padding bits  in Table 6.3.2.1.2-3I is 0 if there is only one CSI report configuration associated with the PUCCH carrying UEIRI; otherwise , where:OPOP=Nmax-Nreported

-, where S is the set of CSI report configurations associated with a same PUCCH resource configured by firstPUCCHResourceConfig-UEIBR, and  is the payload size of the report for the i-th CSI report configuration, obtained according to Table 6.3.2.1.2-3I prior to padding;Nmax=maxi∈SNiNi

- is the payload size of the current report, obtained according to Table 6.3.2.1.2-3I prior to padding.Nreported

Table 6.3.2.1.2-3J: Mapping order of CSI fields of one CSI report for reportQuantity=cli-SRS-RSRP

Table 6.3.2.1.2-3K: Mapping order of CSI fields of one CSI report for CSI-PAI

Table 6.3.2.1.2-4: Mapping order of CSI fields of one CSI report, CSI part 2 wideband

Table 6.3.2.1.2-4A: Mapping order of CSI fields of one CSI report, CSI part 2 wideband,csi-ReportMode= Mode 1

Table 6.3.2.1.2-4B: Mapping order of CSI fields of one CSI report, CSI part 2 wideband,csi-ReportMode= Mode 2

Table 6.3.2.1.2-4C: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 2 wideband

Table 6.3.2.1.2-5: Mapping order of CSI fields of one CSI report, CSI part 2 subband

Table 6.3.2.1.2-5A: Mapping order of CSI fields of one CSI report, CSI part 2 ofcodebookType=typeII-r16 or typeII-PortSelection-r16

Table 6.3.2.1.2-5B: Mapping order of CSI fields of one CSI report, CSI part 2 ofcodebookType=typeII-PortSelection-r17 or typeII-Doppler-PortSelection

Table 6.3.2.1.2-5C: Mapping order of CSI fields of one CSI report, CSI part 2 subband,ReportMode= Mode 1

Table 6.3.2.1.2-5D: Mapping order of CSI fields of one CSI report, CSI part 2 subband,ReportMode= Mode 2

Table 6.3.2.1.2-5E: Mapping order of CSI fields of one CSI report, CSI part 2 ofcodebookType=typeII-CJT

Table 6.3.2.1.2-5F: Mapping order of CSI fields of one CSI report, CSI part 2 ofcodebookType= typeII-Doppler

Table 6.3.2.1.2-5G: Mapping order of CSI fields of one CSI report, CSI part 2 ofcodebookType=typeII-CJT-PortSelection

Table 6.3.2.1.2-5H: Mapping order of CSI fields of one CSI report containing  CSI sub-report(s), CSI part 2 subbandNnsub

Table 6.3.2.1.2-5I: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 2 subband

Table 6.3.2.1.2-5J: Mapping order of CSI fields of one CSI report configured with valueOfM, CSI part 2 of codebookType=typeII-r16

Table 6.3.2.1.2-6: Mapping order of CSI reports to UCI bit sequence , with two-part CSI report(s)

where CSI report #1, CSI report #2, …, CSI report #n in Table 6.3.2.1.2-6 correspond to the CSI reports in increasing order of CSI report priority values according to Clause 5.2.5 of [6, TS38.214].

Table 6.3.2.1.2-7: Mapping order of CSI reports to UCI bit sequence , with two-part CSI report(s)

where CSI report #1, CSI report #2, …, CSI report #n in Table 6.3.2.1.2-7 correspond to the CSI reports in increasing order of CSI report priority values according to Clause 5.2.5 of [6, TS38.214].

The bitwidth for RI/CQI of codebookType= typeII-r16, codebookType=typeII-PortSelection-r16 or codebookType= eTypeII-r19 is provided in Table 6.3.2.1.2-8.

Table 6.3.2.1.2-8: RI and CQI of codebookType=typeII-r16, typeII-PortSelection-r16 or codebookType= eTypeII-r19

The bitwidth for RI/CQI of codebookType= typeII-CJT is provided in Table 6.3.2.1.2-8A.

Table 6.3.2.1.2-8A: RI and CQI of codebookType= typeII-CJT

The bitwidth for RI/CQI of codebookType= typeII-Doppler and codebookType= typeII-Doppler-r19 is provided in Table 6.3.2.1.2-8B.

Table 6.3.2.1.2-8B: RI and CQI of codebookType= typeII-Doppler or codebookType= typeII-Doppler-r19

The bitwidth for RI/LI/CQI/CRI of a CSI report configured with valueOfM and codebookType=typeI-SinglePanel is provided in Table 6.3.2.1.2-8C.

Table 6.3.2.1.2-8C: RI, LI, CQI, and CRI of a CSI report configured with valueOfM and cocodebookType=typeI-SinglePanel

The bitwidth for RI/CQI/CRI of a CSI report configured with valueOfM and codebookType= typeII-r16 is provided in Table 6.3.2.1.2-8D.

Table 6.3.2.1.2-8D: RI, CQI and CRI of a CSI report configured with valueOfM and codebookType=typeII-r16

The bitwidth for RI/CQI of codebookType=typeII-PortSelection-r17, typeII-Doppler-PortSelection or codebookType= typeII-FePortSelection-r19 is provided in Table 6.3.2.1.2-9.

Table 6.3.2.1.2-9: RI and CQI of codebookType=typeII-PortSelection-r17, typeII-Doppler-PortSelection, or codebookType= typeII-FePortSelection-r19

The bitwidth for RI/CQI of codebookType=typeII-CJT-PortSelection is provided in Table 6.3.2.1.2-9A.

Table 6.3.2.1.2-9A: RI and CQI of codebookType= typeII-CJT-PortSelection

The bitwidth for reportQuantity=tdcp is provided in Table 6.3.2.1.2-10.

Table 6.3.2.1.2-10: Amplitude and phase values for reportQuantity=tdcp

The bitwidth for reportQuantity=cjtc-Dd is provided in Table 6.3.2.1.2-11.

Table 6.3.2.1.2-11: Reference TRS resource set index, delay offset and inside/outside indicator for reportQuantity=cjtc-Dd

The bitwidth for reportQuantity=cjtc-F is provided in Table 6.3.2.1.2-12.

Table 6.3.2.1.2-12: Reference TRS resource set index, and frequency offset for reportQuantity=cjtc-F

The bitwidth for reportQuantity=cjtc-P is provided in Table 6.3.2.1.2-13.

Table 6.3.2.1.2-13: Reference CSI-RS resource index, and phase offset for reportQuantity=cjtc-P

The bitwidth for CRI, SSBRI, RSRP, differential RSRP, CSI report configuration indicator and Condition met indicator are provided in Table 6.3.2.1.2-14.

Table 6.3.2.1.2-14: CRI, SSBRI, RSRP, CapabilityIndex, CSI report configuration indicator and Condition met indicator

The bitwidth for CSI-PAI is provided in Table 6.3.2.1.2-15.

Table 6.3.2.1.2-15: CSI-PAI

## 6.3.2.1.3CG-UCI

For CG-UCI bits transmitted on a CG PUSCH when the higher layer parameter cg-RetransmissionTimer is configured, the CG-UCI bit sequence  is determined as follows:a0, a1, a2, a3, …,aA-1

-set   for  and , where the CG-UCI bit sequence  is given by Table 6.3.2.1.3-1, mapped in the order from upper part to lower part.ai=oiCG-UCIi=0,1, …, OCG-UCI-1A=OCG-UCIo0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCI

Table 6.3.2.1.3-1: Mapping order of CG-UCI fields

## 6.3.2.1.3AUTO-UCI

For UTO-UCI bits transmitted on a CG PUSCH when the higher layer parameter nrofBitsInUTO-UCI is configured, the UTO-UCI bit sequence  is determined as follows:a0, a1, a2, a3, …,aA-1

-set   for  and , where  is provided by nrofBitsInUTO-UCI, and the UTO-UCI bit sequence  is given by clause 9.3.1 of [5, TS 38.213].ai=oiUTO-UCIi=0,1, …, OUTO-UCI-1A=OUTO-UCIOUTO-UCIo0UTO-UCI, o1UTO-UCI, …, oOUTO-UCI-1UTO-UCI

## 6.3.2.1.3BUEIRI

If UEIRI bits are transmitted on a PUSCH, the UEIRI bit sequence  is determined as follows:a0, a1, a2, a3, …,aA-1

-set   for  and , where  is the number of PUCCH resources for UEIRI given by Clause 9 of [5, TS38.213], and the UEIRI bit sequence  is mapped to the PUCCH resources according to an ascending order of pucch-ResourceId. If the associated UEIRI of  is positive, ; otherwise, .ai=oiUEIRIi=0,1, …, OUEIRI-1A=OUEIRIOUEIRIo0UEIRI, o1UEIRI, …, oOUEIRI-1UEIRIoiUEIRIoiUEIRI=1oiUEIRI=0

## 6.3.2.1.4HARQ-ACK and CG-UCI/UTO-UCI

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedure in this clause 6.3.2.1.4 applies by replacing CG-UCI with UTO-UCI in all the notations and texts, replacing "When higher layer parameter cg-UCI-Multiplexing is configured" with "When UTO-UCI and HARQ-ACK have the same priority index and are jointly encoded and transmitted on a PUSCH" and replacing "is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part " with "is given by Clause 9.3.1 of [5, TS 38.213]".

If a UE would multiplex UEIRI and HARQ-ACK in a PUSCH [5, TS 38.213], the procedure in this clause 6.3.2.1.4 applies by replacing CG-UCI with UEIRI in all the notations and texts assuming higher layer parameter cg-UCI-Multiplexing is configured and replacing "is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part " with "is determined as described in clause 6.3.2.1.3B ".

When higher layer parameter cg-UCI-Multiplexing is configured, the UCI bit sequence  is determined as follows, where .a0, a1, a2, a3, …,aA-1 A=OCG-UCI+OACK

-The CG-UCI bits are mapped to the UCI bit sequence, where for . The CG-UCI bit sequence  is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part, and  is number of CG-UCI bits;a0, a1, a2, a3, …,aOCG-UCI-1 ai=oiCG-UCI i=0,1, …, OCG-UCI-1o0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCIOCG-UCI

-The HARQ-ACK bits are mapped to the UCI bit sequence , where  for . The HARQ-ACK bit sequence  is given by Clause 9.1 of [5, TS38.213], and  is number of HARQ-ACK bits.aOCG-UCI, aOCG-UCI+1,  …,aOCG-UCI+OACK-1ai+OCG-UCI=oiACKi=0,1, …, OACK-1o0ACK, o1ACK, …, oOACK-1ACKOACK

## 6.3.2.1.5UCI with different priority indexes

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedure in this clause 6.3.2.1.5 applies by replacing CG-UCI with UTO-UCI in all the notations and texts, and replacing "is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part" with "is given by clause 9.3.1 of [5, TS 38.213]".

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 1, the following UCI bit sequences are generated, , and   if any, according to the following:a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(2), a1(2), a2(2), a3(2), …,aA(2)-12

-If CSI part 1 is also transmitted on the PUSCH,

-Set  for  as the bit sequence of CSI part 1, where the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the UCI bit sequence  starting with .ai(1)i=0,1,…,A(1)-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(1)

-Set    for  and , where the HARQ-ACK bit sequence  associated with priority index 0 is given by Clause 9.1 of [5, TS 38.213].ai(2)=oiACK-LPi=0,1,…,OACK-LP-1A(2)=OACK-LPo0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LP

-Otherwise, set    for  and , where the HARQ-ACK bit sequence  associated with priority index 0 is given by Clause 9.1 of [5, TS 38.213].ai(1)=oiACK-LPi=0,1,…,OACK-LP-1A(1)=OACK-LPo0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LP

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 1, and CSI if any are transmitted on a PUSCH associated with priority index 0, the following UCI bit sequences are generated,,  if any, and   if any, according to the following: a0, a1, a2, a3, …,aA-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(2), a1(2), a2(2), a3(2), …,aA(2)-12

-If HARQ-ACK bits associated with priority index 1 and CSI are transmitted on the PUSCH without UL-SCH and the CSI includes CSI part 1 without CSI part 2, and there is only one HARQ-ACK bit associated with priority index 1 given by Clause 9.1 of [5, TS 38.213], set , , and ; otherwise, set   for  and , where the HARQ-ACK bit sequence  associated with priority index 1 is given by Clause 9.1 of [5, TS 38.213];a0=o0ACK-HPa1=0A=2ai=oiACK-HPi=0,1,…,OACK-HP-1A=OACK-HPo0ACK-HP, o1ACK-HP, …, oOACK-HP-1ACK-HP

-Set  for  as the bit sequence of CSI part 1, if CSI part 1 is also transmitted on the PUSCH, where the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the UCI bit sequence  starting with ;ai(1)i=0,1,…,A(1)-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(1)

-Set  for  as the bit sequence of CSI part 2, if CSI part 2 is also transmitted on the PUSCH, where the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-7, are mapped to the UCI bit sequence  starting with .ai(2)i=0,1,…,A(2)-1a0(2), a1(2), a2(2), a3(2), …,aA(1)-12a0(2)

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and/or CG-UCI associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH, the following UCI bit sequences are generated,, , and   if any, according to the following: a0, a1, a2, a3, …,aA-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(2), a1(2), a2(2), a3(2), …,aA(2)-12

-Set   for  and  if HARQ-ACK bits associated with priority index 1 are transmitted without CG-UCI associated with priority index 1, where the HARQ-ACK bit sequence  associated with priority index 1 is given by Clause 9.1 of [5, TS 38.213];ai=oiACK-HPi=0,1,…,OACK-HP-1A=OACK-HPo0ACK-HP, o1ACK-HP, …, oOACK-HP-1ACK-HP

-Set   for  and  if CG-UCI associated with priority index 1 is transmitted without HARQ-ACK bits associated with priority index 1, where the CG-UCI bit sequence  associated with priority index 1 is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part;ai=oiCG-UCIi=0,1,…,OCG-UCI-1A=OCG-UCIo0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCI

-Set  as follows, if both CG-UCI associated with priority index 1 and HARQ-ACK bits associated with priority index 1 are transmitted, where a0, a1, a2, a3, …,aA-1A=OCG-UCI+OACK-HP

-The CG-UCI bits are mapped to the UCI bit sequence , where for . The CG-UCI bit sequence  is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part, and  is number of CG-UCI bitsa0, a1, a2, a3, …,aOCG-UCI-1ai=oiCG-UCI i=0,1, …, OCG-UCI-1o0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCIOCG-UCI

-The HARQ-ACK bits are mapped to the UCI bit sequence , where  for . The HARQ-ACK bit sequence  associated with priority index 1 is given by Clause 9.1 of [5, TS 38.213].aOCG-UCI, aOCG-UCI+1,  …,aOCG-UCI+OACK-HP-1ai+OCG-UCI=oiACK-HPi=0,1, …, OACK-HP-1o0ACK-HP, o1ACK-HP, …, oOACK-HP-1ACK-HP

-If CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 1,

-Set  for  as the bit sequence of CSI part 1, where the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the UCI bit sequence  starting with .ai(1)i=0,1,…,A(1)-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(1)

-Set    for  and , where the HARQ-ACK bit sequence  associated with priority index 0 is given by Clause 9.1 of [5, TS 38.213].ai(2)=oiACK-LPi=0,1,…,OACK-LP-1A(2)=OACK-LPo0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LP

-Otherwise,

-Set    for  and , where the HARQ-ACK bit sequence  associated with priority index 0 is given by Clause 9.1 of [5, TS 38.213].ai(1)=oiACK-LPi=0,1,…,OACK-LP-1A(1)=OACK-LPo0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LP

-Set    for and , if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0, where the CSI part 1 sequence  is given by Table 6.3.2.1.2-6 by replacing , and the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the CSI part 1 sequence  starting with .ai(2)=ai(1)i=0,1,…,A1-1 A(2)=A(1)a0(1), a1(1), a2(1), a3(1), …,aA(1)-1(1)a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(1), a1(1), a2(1), a3(1), …,aA(1)-1(1)a0(1)

If uci-MuxWithDiffPrio is configured, and CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any, HARQ-ACK bits associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 0, the following UCI bit sequences are generated,, , and   if any, according to the following: a0, a1, a2, a3, …,aA-1a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(2), a1(2), a2(2), a3(2), …,aA(2)-12

-Set   for  and , where the HARQ-ACK bit sequence  associated with priority index 1 is given by Clause 9.1 of [5, TS 38.213];ai=oiACK-HPi=0,1,…,OACK-HP-1A=OACK-HPo0ACK-HP, o1ACK-HP, …, oOACK-HP-1ACK-HP

-Set   for  and  if CG-UCI associated with priority index 0 is transmitted without HARQ-ACK bits associated with priority index 0, where the CG-UCI bit sequence  associated with priority index 0 is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part;ai(1)=oiCG-UCIi=0,1, …, OCG-UCI-1A(1)=OCG-UCIo0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCI

-Set  as follows if both CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 are transmitted, where a0(1), a1(1), a2(1), a3(1), …,aA(1)-11A(1)=OCG-UCI+OACK-LP

-The CG-UCI bits are mapped to the UCI bit sequence , where for . The CG-UCI bit sequence  is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part, and  is number of CG-UCI bitsa0(1), a1(1), a2(1), a3(1), …,aOCG-UCI-11ai(1)=oiCG-UCI i=0,1, …, OCG-UCI-1o0CG-UCI, o1CG-UCI, …, oOCG-UCI-1CG-UCIOCG-UCI

-The HARQ-ACK bits are mapped to the UCI bit sequence , where  for . The HARQ-ACK bit sequence  associated with priority index 0 is given by Clause 9.1 of [5, TS 38.213].aOCG-UCI(1), aOCG-UCI+1(1),  …,aOCG-UCI+OACK-LP-11ai+OCG-UCI(1)=oiACK-LPi=0,1, …, OACK-LP-1o0ACK-LP, o1ACK-LP, …, oOACK-LP-1ACK-LP

-Set   for and , if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0, where the CSI part 1 sequence  is given by Table 6.3.2.1.2-6 by replacing , and the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.2.1.2-6, are mapped to the CSI part 1 sequence  starting with .ai(2)=ai(1)i=0,1,…,A1-1 A(2)=A(1)a0(1), a1(1), a2(1), a3(1), …,aA(1)-1(1)a0(1), a1(1), a2(1), a3(1), …,aA(1)-11a0(1), a1(1), a2(1), a3(1), …,aA(1)-1(1)a0(1)

## 6.3.2.2Code block segmentation and CRC attachment

Denote the bits of the payload by , where  is the payload size. The procedure in 6.3.2.2.1 applies for  and the procedure in Clause 6.3.2.2.2 applies for .

## 6.3.2.2.1UCI encoded by Polar code

Code block segmentation and CRC attachment is performed according to Clause 6.3.1.2.1.

## 6.3.2.2.2UCI encoded by channel coding of small block lengths

The procedure in Clause 6.3.1.2.2 applies.

## 6.3.2.3Channel coding of UCI

## 6.3.2.3.1UCI encoded by Polar code

Channel coding is performed according to Clause 6.3.1.3.1, except that the rate matching output sequence length  is given in Clause 6.3.2.4.1.

## 6.3.2.3.2UCI encoded by channel coding of small block lengths

Information bits are delivered to the channel coding block. They are denoted by , where  is the number of bits.

The information bits are encoded according to Clause 5.3.3.

After encoding the bits are denoted by , where  is the number of coded bits.

## 6.3.2.4Rate matching

In case where there are more than one UL-SCH transport blocks for the PUSCH transmission, the UCI information is multiplexed only on the UL-SCH transport block with highest IMCS value for the initial PUSCH, where IMCS is as defined in Clause 6.1.4.1 in [6, TS 38.214]. In case the two transport blocks have the same IMCS value for the initial PUSCH, the UCI information is multiplexed with data only on the first transport block. The PUSCH for UCI multiplexing in this Clause refers to the UL-SCH transport block for UCI multiplexing.

## 6.3.2.4.1UCI encoded by Polar code

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedures in this clause and the clauses it refers to apply by replacing CG-UCI with UTO-UCI in all the notations and texts, when applicable.

6.3.2.4.1.1HARQ-ACK

For HARQ-ACK transmission on PUSCH not using repetition type B with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1, the number of coded modulation symbols per layer for HARQ-ACK transmission, denoted as , is determined as follows:

where

- is the number of HARQ-ACK bits;

-if , ; otherwise  is the number of CRC bits for HARQ-ACK determined according to Clause 6.3.1.2.1;

-;

- is the number of code blocks for UL-SCH of the PUSCH transmission;

-if the DCI format scheduling the PUSCH transmission includes a CBGTI field indicating that the UE shall not transmit the -th code block, =0; otherwise,  is the -th code block size for UL-SCH of the PUSCH transmission;

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission;MscMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

- is configured by higher layer parameter scaling;

- is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission.

For HARQ-ACK transmission on PUSCH not using repetition type B with UL-SCH, and if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the number of coded modulation symbols per layer for HARQ-ACK transmission, denoted as , is determined as follows:QACK'

QACK'=minOACK+LACK∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIl1Nsr=0CUL-SCH-1Kr,α∙l=l0Nsymb,allPUSCH-1MscUCIl

where

- is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI;Ns

-is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK transmission;MscPT-RSl l

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK transmission;MscMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK transmission and is the total number of OFDM symbols of the PUSCH in the slot, including all OFDM symbols used for DMRS;MscUCIlll=0,1,2,…,Nsymb,allPUSCH-1Nsymb,allPUSCH

-is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK transmission;l0

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For HARQ-ACK transmission on an actual repetition of a PUSCH with repetition Type B with UL-SCH, the number of coded modulation symbols per layer for HARQ-ACK transmission, denoted as , is determined as follows:QACK'

QACK'=minOACK+LACK∙βoffsetPUSCH∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIlr=0CUL-SCH-1Kr,   α∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIl,  l=0Nsymb,actualPUSCH-1Msc,actualUCIl

where

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission assuming a nominal repetition without segmentation, and  is the total number of OFDM symbols in a nominal repetition of the PUSCH, including all OFDM symbols used for DMRS;Msc,nominalUCIlll=0, 1, 2, ⋯, Nsymb,nominalPUSCH-1Nsymb,nominalPUSCH

-for any OFDM symbol that carries DMRS of the PUSCH assuming a nominal repetition without segmentation, ;Msc,nominalUCIl=0

-for any OFDM symbol that does not carry DMRS of the PUSCH assuming a nominal repetition without segmentation,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission assuming a nominal repetition without segmentation,  is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission, assuming a nominal repetition without segmentation;Msc,nominalUCIl=MscPUSCH-Msc,nominalPT-RSl-Msc,nominalMutedlMsc,nominalPT-RSllMsc,nominalMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol  , for , in the actual repetition of the PUSCH transmission, and  is the total number of OFDM symbols in the actual repetition of the PUSCH transmission, including all OFDM symbols used for DMRS;Msc,actualUCIlll=0, 1, 2, ⋯, Nsymb,actualPUSCH-1Nsymb,actualPUSCH

-for any OFDM symbol that carries DMRS of the actual repetition of the PUSCH transmission, ;Msc,actualUCIl=0

-for any OFDM symbol that does not carry DMRS of the actual repetition of the PUSCH transmission,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the actual repetition of the PUSCH transmission,  is the number of muted subcarriers in OFDM symbol  in the actual repetition of the PUSCH transmission;Msc,actualUCIl=MscPUSCH-Msc,actualPT-RSl-Msc,actualMutedlMsc,actualPT-RSllMsc,actualMutedll

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For HARQ-ACK transmission on PUSCH without UL-SCH, the number of coded modulation symbols per layer for HARQ-ACK transmission, denoted as , is determined as follows:

where

- is the number of HARQ-ACK bits;

-if , ; otherwise  is the number of CRC bits for HARQ-ACK defined according to Clause 6.3.1.2.1;;

-;

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

- is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission;

- is the code rate of the PUSCH, determined according to Clause 6.1.4.1 of [6, TS38.214];

- is the modulation order of the PUSCH;

- is configured by higher layer parameter scaling.

The input bit sequence to rate matching is  where  is the code block number, and  is the number of coded bits in code block number .

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where

- is the number of code blocks for UCI determined according to Clause 5.2.1;

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH;

-.

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number .

6.3.2.4.1.2CSI part 1

For CSI part 1 transmission on PUSCH not using repetition type B with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1, the number of coded modulation symbols per layer for CSI part 1 transmission, denoted as , is determined as follows:

QCSI-1'=minOCSI-1+LCSI-1∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIlr=0CUL-SCH-1Kr,α∙l=0Nsymb,allPUSCH-1MscUCIl-QACK/CG-UCI'

where

- is the number of bits for CSI part 1;

-if , ; otherwise  is the number of CRC bits for CSI part 1 determined according to Clause 6.3.1.2.1;

-;

- is the number of code blocks for UL-SCH of the PUSCH transmission;

-if the DCI format scheduling the PUSCH transmission includes a CBGTI field indicating that the UE shall not transmit the -th code block, =0; otherwise, is the -th code block size for UL-SCH of the PUSCH transmission;

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- if HARQ-ACK is present for transmission on the same PUSCH with UL-SCH and without CG-UCI, where  is the number of coded modulation symbols per layer for HARQ-ACK transmitted on the PUSCH as defined in clause 6.3.2.4.1.1 if number of HARQ-ACK information bits is more than 2, and  if the number of HARQ-ACK information bits is no more than 2 bits, where  is the number of reserved resource elements for potential HARQ-ACK transmission in OFDM symbol , for , in the PUSCH transmission, defined in Clause 6.2.7; orQACK/CG-UCI'=QACK'QACK'

- if both HARQ-ACK and CG-UCI are present on the same PUSCH with UL-SCH, where  is the number of coded modulation symbols per layer for HARQ-ACK and CG-UCI transmitted on the PUSCH as defined in clause 6.3.2.4.1.5; orQACK/CG-UCI'=QACK'QACK'

- if CG-UCI is present on the same PUSCH with UL-SCH and without HARQ-ACK, where  is the number of coded modulation symbols per layer for CG-UCI transmitted on the PUSCH as defined in clause 6.3.2.4.1.4;QACK/CG-UCI'=QCG-UCI'QCG-UCI'

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

- is configured by higher layer parameter scaling.

For CSI part 1 transmission on PUSCH not using repetition type B with UL-SCH, and if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the number of coded modulation symbols per layer for CSI part 1 transmission, denoted as , is determined as follows:QCSI-part1'

QCSI-1'=minOCSI-1+LCSI-1∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIl1Nsr=0CUL-SCH-1Kr,α∙l=0Nsymb,allPUSCH-1MscUCIl-QACK/CG-UCI'

where

- is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI;Ns

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 1 transmission;MscPT-RSll

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 1 transmission;MscMutedll

-is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 1 transmission and is the total number of OFDM symbols of the PUSCH in the slot, including all OFDM symbols used for DMRS;MscUCIl ll=0,1,2,…,Nsymb,allPUSCH-1Nsymb,allPUSCH

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For CSI part 1 transmission on an actual repetition of a PUSCH with repetition Type B with UL-SCH, the number of coded modulation symbols per layer for CSI part 1 transmission, denoted as , is determined as follows: QCSI-part1'

QCSI-1'=minOCSI-1+LCSI-1∙βoffsetPUSCH∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIlr=0CUL-SCH-1Kr,   α∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIl-QACK/CG-UCI' ,  l=0Nsymb,actualPUSCH-1Msc,actualUCIl-QACK/CG-UCI'

where

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission assuming a nominal repetition without segmentation, and  is the total number of OFDM symbols in a nominal repetition of the PUSCH, including all OFDM symbols used for DMRS;Msc,nominalUCIlll=0, 1, 2, ⋯, Nsymb,nominalPUSCH-1Nsymb,nominalPUSCH

-for any OFDM symbol that carries DMRS of the PUSCH assuming a nominal repetition without segmentation, ;Msc,nominalUCIl=0

-for any OFDM symbol that does not carry DMRS of the PUSCH assuming a nominal repetition without segmentation,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission assuming a nominal repetition without segmentation,  is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission, assuming a nominal repetition without segmentation;Msc,nominalUCIl=MscPUSCH-Msc,nominalPT-RSl-Msc,nominalMutedlMsc,nominalPT-RSllMsc,nominalMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the actual repetition of the PUSCH transmission, and  is the total number of OFDM symbols in the actual repetition of the PUSCH transmission, including all OFDM symbols used for DMRS;Msc,actualUCIlll=0, 1, 2, ⋯, Nsymb,actualPUSCH-1Nsymb,actualPUSCH

-for any OFDM symbol that carries DMRS of the actual repetition of the PUSCH transmission, ;Msc,actualUCIl=0

-for any OFDM symbol that does not carry DMRS of the actual repetition of the PUSCH transmission,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the actual repetition of the PUSCH transmission,  is the number of muted subcarriers in OFDM symbol  in the actual repetition of the PUSCH transmission;Msc,actualUCIl=MscPUSCH-Msc,actualPT-RSl-Msc,actualMutedlMsc,actualPT-RSllMsc,actualMutedll

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For CSI part 1 transmission on PUSCH without UL-SCH, the number of coded modulation symbols per layer for CSI part 1 transmission, denoted as , is determined as follows:

if there is CSI part 2 to be transmitted on the PUSCH,

else

end if

where

- is the number of bits for CSI part 1;

-if , ; otherwise  is the number of CRC bits for CSI part 1 determined according to Clause 6.3.1.2.1;

-;

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- is the number of coded modulation symbols per layer for HARQ-ACK transmitted on the PUSCH if number of HARQ-ACK information bits is more than 2, and  if the number of HARQ-ACK information bits is no more than 2 bits, where  is the number of reserved resource elements for potential HARQ-ACK transmission in OFDM symbol , for , in the PUSCH transmission, defined in Clause 6.2.7;

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

- is the code rate of the PUSCH, determined according to Clause 6.1.4.1 of [6, TS38.214];

- is the modulation order of the PUSCH.

The input bit sequence to rate matching is  where  is the code block number, and  is the number of coded bits in code block number .

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where

- is the number of code blocks for UCI determined according to Clause 5.2.1;

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH;

-.

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number .

6.3.2.4.1.3CSI part 2

For CSI part 2 transmission on PUSCH not using repetition type B with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1, the number of coded modulation symbols per layer for CSI part 2 transmission, denoted as , is determined as follows:

QCSI-2'=minOCSI-2+LCSI-2∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIlr=0CUL-SCH-1Kr,α∙l=0Nsymb,allPUSCH-1MscUCIl-QACK/CG-UCI'-QCSI-1'

where

- is the number of bits for CSI part 2;

-if , ; otherwise  is the number of CRC bits for CSI part 2 determined according to Clause 6.3.1.2.1;

-;

- is the number of code blocks for UL-SCH of the PUSCH transmission;

-if the DCI format scheduling the PUSCH transmission includes a CBGTI field indicating that the UE shall not transmit the -th code block, =0; otherwise, is the -th code block size for UL-SCH of the PUSCH transmission;

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- if HARQ-ACK is present for transmission on the same PUSCH with UL-SCH and without CG-UCI, where  is the number of coded modulation symbols per layer for HARQ-ACK transmitted on the PUSCH as defined in clause 6.3.2.4.1.1 if number of HARQ-ACK information bits is more than 2, and  if the number of HARQ-ACK information bits is 1 or 2 bits; orQACK/CG-UCI'=QACK'QACK'

- if both HARQ-ACK and CG-UCI are present on the same PUSCH with UL-SCH, where  is the number of coded modulation symbols per layer for HARQ-ACK and CG-UCI transmitted on the PUSCH as defined in clause 6.3.2.4.1.5; orQACK/CG-UCI'=QACK'QACK'

- if CG-UCI is present on the same PUSCH with UL-SCH and without HARQ-ACK, where  is the number of coded modulation symbols per layer for CG-UCI transmitted on the PUSCH as defined in clause 6.3.2.4.1.4;QACK/CG-UCI'=QCG-UCI'QCG-UCI'

- is the number of coded modulation symbols per layer for CSI part 1 transmitted on the PUSCH;

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, .MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

- is configured by higher layer parameter scaling.

For CSI part 2 transmission on PUSCH not using repetition type B with UL-SCH, and if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the number of coded modulation symbols per layer for CSI part 2 transmission, denoted as , is determined as follows:QCSI-part2'

QCSI-2'=minOCSI-2+LCSI-2∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIl1Nsr=0CUL-SCH-1Kr,α∙l=0Nsymb,allPUSCH-1MscUCIl-QACK/CG-UCI'-QCSI-1'

where

- is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI;Ns

-is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 2 transmission;MscPT-RSl l

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 2 transmission;MscMutedll

-is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission of TB processing over multiple slots in the slot with the CSI part 2 transmission and is the total number of OFDM symbols of the PUSCH in the slot, including all OFDM symbols used for DMRS;MscUCIl ll=0,1,2,…,Nsymb,allPUSCH-1Nsymb,allPUSCH

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For CSI part 2 transmission on an actual repetition of a PUSCH with repetition Type B with UL-SCH, the number of coded modulation symbols per layer for CSI part 2 transmission, denoted as , is determined as follows:QCSI-part2'

QCSI-2'=minOCSI-2+LCSI-2∙βoffsetPUSCH∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIlr=0CUL-SCH-1Kr,   α∙l=0Nsymb,nominalPUSCH-1Msc,nominalUCIl-QACK/CG-UCI'-QCSI-1' ,  l=0Nsymb,actualPUSCH-1Msc,actualUCIl-QACK/CG-UCI'-QCSI-1'

where

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission assuming a nominal repetition without segmentation, and  is the total number of OFDM symbols in a nominal repetition of the PUSCH, including all OFDM symbols used for DMRS;Msc,nominalUCIlll=0, 1, 2, ⋯, Nsymb,nominalPUSCH-1Nsymb,nominalPUSCH

-for any OFDM symbol that carries DMRS of the PUSCH assuming a nominal repetition without segmentation, ;Msc,nominalUCIl=0

-for any OFDM symbol that does not carry DMRS of the PUSCH assuming a nominal repetition without segmentation,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission assuming a nominal repetition without segmentation,  is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission, assuming a nominal repetition without segmentation;Msc,nominalUCIl=MscPUSCH-Msc,nominalPT-RSl-Msc,nominalMutedlMsc,nominalPT-RSllMsc,nominalMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the actual repetition of the PUSCH transmission, and  is the total number of OFDM symbols in the actual repetition of the PUSCH transmission, including all OFDM symbols used for DMRS;Msc,actualUCIlll=0, 1, 2, ⋯, Nsymb,actualPUSCH-1Nsymb,actualPUSCH

-for any OFDM symbol that carries DMRS of the actual repetition of the PUSCH transmission, ;Msc,actualUCIl=0

-for any OFDM symbol that does not carry DMRS of the actual repetition of the PUSCH transmission,  where  is the number of subcarriers in OFDM symbol  that carries PTRS, in the actual repetition of the PUSCH transmission,  is the number of muted subcarriers in OFDM symbol  in the actual repetition of the PUSCH transmission;Msc,actualUCIl=MscPUSCH-Msc,actualPT-RSl-Msc,actualMutedlMsc,actualPT-RSllMsc,actualMutedll

-and all the other notations in the formula are defined the same as for PUSCH not using repetition type B and if numberOfSlotsTBoMS is not present in the resource allocation table.

For CSI part 2 transmission on PUSCH without UL-SCH, the number of coded modulation symbols per layer for CSI part 2 transmission, denoted as , is determined as follows:

where

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission;

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- is the number of coded modulation symbols per layer for HARQ-ACK transmitted on the PUSCH if number of HARQ-ACK information bits is more than 2, and  if the number of HARQ-ACK information bits is 1 or 2 bits;

- is the number of coded modulation symbols per layer for CSI part 1 transmitted on the PUSCH;

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;

-for any OFDM symbol that carries DMRS of the PUSCH, ;

-for any OFDM symbol that does not carry DMRS of the PUSCH, .MscUCIl=MscPUSCH-MscPT-RSl-MscMutedl

The input bit sequence to rate matching is  where  is the code block number, and  is the number of coded bits in code block number .

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where

- is the number of code blocks for UCI determined according to Clause 5.2.1;

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH;

-.

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number .

6.3.2.4.1.4CG-UCI

For CG-UCI transmission on PUSCH with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1, the number of coded modulation symbols per layer for CG-UCI transmission, denoted as , is determined as follows:QCG-UCI'

QCG-UCI'=minOCG-UCI+LCG-UCI∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIlr=0CUL-SCH-1Kr,α∙l=l0Nsymb,allPUSCH-1MscUCIl

where

- is the number of CG-UCI bits;OCG-UCI

- is the number of CRC bits for CG-UCI determined according to Clause 6.3.1.2.1;LCG-UCI

-;βoffsetPUSCH=βoffsetCG-UCI

- is the number of code blocks for UL-SCH of the PUSCH transmission;CUL-SCH

- is the r-th code block size for UL-SCH of the PUSCH transmission;Kr

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;MscPUSCH

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol l that carries PTRS, in the PUSCH transmission;MscPT-RSl

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol l, for =0,1,2,…, , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;MscUCIllNsymb,allPUSCH-1Nsymb,allPUSCH

-for any OFDM symbol that carries DMRS of the PUSCH, ;MscUCIl=0

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH- MscPT-RSl-MscMutedl

- is configured by higher layer parameter scaling;α

- is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission.l0

For CG-UCI transmission on PUSCH with UL-SCH, and if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the number of coded modulation symbols per layer for CG-UCI transmission, denoted as , is determined as follows:QCG-UCI'

QCG-UCI'=minOCG-UCI+LCG-UCI∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIl1Nsr=0CUL-SCH-1Kr,α∙l=l0Nsymb,allPUSCH-1MscUCIl

where

- is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI;Ns

-is the number of subcarriers in OFDM symbol that carries PTRS, in the PUSCH transmission of TB processing over multiple slots in the slot with the CG-UCI transmission;MscPT-RSl  l

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission of TB processing over multiple slots in the slot with the CG-UCI transmission;MscMutedll

-is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission of TB processing over multiple slots in the slot with the CG-UCI transmission and  is the total number of OFDM symbols of the PUSCH in the slot, including all OFDM symbols used for DMRS;MscUCIlll=0,1,2,…,Nsymb,allPUSCH-1Nsymb,allPUSCH

-is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission of TB processing over multiple slots in the slot with the CG-UCI transmission;l0

-and all the other notations in the formula are defined the same as for PUSCH with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table.

The input bit sequence to rate matching is  where r is the code block number, and  is the number of coded bits in code block number r. dr0, dr1, dr2, dr3, …, drNr-1Nr

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where IBIL=1Er=EUCICUCI

- is the number of code blocks for UCI determined according to Clause 5.2.1;CUCI

- is the number of transmission layers of the PUSCH;NL

- is the modulation order of the PUSCH;Qm

-.EUCI=NL∙QCG-UCI'∙Qm

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number r.fr0, fr1,fr2, …, frEr-1Er

6.3.2.4.1.5HARQ-ACK and CG-UCI

For HARQ-ACK and CG-UCI transmission on PUSCH with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table, or if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is equal to 1, the number of coded modulation symbols per layer for HARQ-ACK and CG-UCI transmission, denoted as , is determined as follows:QACK'

QACK'=minOACK+OCG-UCI+LACK∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIlr=0CUL-SCH-1Kr,α∙l=l0Nsymb,allPUSCH-1MscUCIl

where

- is the number of HARQ-ACK bits;OACK

- is the number of CG-UCI bits;OCG-UCI

-if , ; otherwise  is the number of CRC bits for HARQ-ACK and CG-UCI determined according to Clause 6.3.1.2.1;OACK+OCG-UCI≥360LACK=11LACK

-;βoffsetPUSCH=βoffsetHARQ-ACK

- is the number of code blocks for UL-SCH of the PUSCH transmission;CUL-SCH

- is the r-th code block size for UL-SCH of the PUSCH transmission;Kr

- is the scheduled bandwidth of the PUSCH transmission, expressed as a number of subcarriers;MscPUSCH

-If the PUSCH transmission is in SBFD symbols,  only includes subcarriers of the scheduled bandwidth that are both in the active UL BWP and in the UL sub-band, as described in Clause 6.1.2.2.1 in [6, TS 38.214];MscPUSCH

- is the number of subcarriers in OFDM symbol l that carries PTRS, in the PUSCH transmission;MscPT-RSl

- is the number of muted subcarriers in OFDM symbol , in the PUSCH transmission;MscMutedll

- is the number of resource elements that can be used for transmission of UCI in OFDM symbol l, for =0,1,2,…, , in the PUSCH transmission and  is the total number of OFDM symbols of the PUSCH, including all OFDM symbols used for DMRS;MscUCIllNsymb,allPUSCH-1Nsymb,allPUSCH

-for any OFDM symbol that carries DMRS of the PUSCH, ;MscUCIl=0

-for any OFDM symbol that does not carry DMRS of the PUSCH, ;MscUCIl=MscPUSCH- MscPT-RSl- MscMutedl

- is configured by higher layer parameter scaling;α

- is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission.l0

For HARQ-ACK and CG-UCI transmission on PUSCH with UL-SCH, and if numberOfSlotsTBoMS is present in the resource allocation table and the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI is larger than 1, the number of coded modulation symbols per layer for HARQ-ACK and CG-UCI transmission, denoted as , is determined as follows:QACK'

QACK'=minOACK+OCG-UCI+LACK∙βoffsetPUSCH∙l=0Nsymb,allPUSCH-1MscUCIl1Nsr=0CUL-SCH-1Kr,α∙l=l0Nsymb,allPUSCH-1MscUCIl

where

- is the value of numberOfSlotsTBoMS in the row indicated by the Time domain resource assignment field in DCI;Ns

-is the number of subcarriers in OFDM symbol  that carries PTRS, in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK and CG-UCI transmission;MscPT-RSl l

- is the number of muted subcarriers in OFDM symbol  in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK and CG-UCI transmission;MscMutedll

-is the number of resource elements that can be used for transmission of UCI in OFDM symbol , for , in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK and CG-UCI transmission and  is the total number of OFDM symbols of the PUSCH in the slot, including all OFDM symbols used for DMRS;MscUCIl ll=0,1,2,…,Nsymb,allPUSCH-1Nsymb,allPUSCH

-is the symbol index of the first OFDM symbol that does not carry DMRS of the PUSCH, after the first DMRS symbol(s), in the PUSCH transmission of TB processing over multiple slots in the slot with the HARQ-ACK and CG-UCI transmission;l0

-and all the other notations in the formula are defined the same as for PUSCH with UL-SCH and if numberOfSlotsTBoMS is not present in the resource allocation table.

The input bit sequence to rate matching is  where r is the code block number, and  is the number of coded bits in code block number r. dr0, dr1, dr2, dr3, …, drNr-1Nr

Rate matching is performed according to Clause 5.4.1 by setting  and the rate matching output sequence length to , where IBIL=1Er=EUCICUCI

- is the number of code blocks for UCI determined according to Clause 5.2.1;CUCI

- is the number of transmission layers of the PUSCH;NL

- is the modulation order of the PUSCH;Qm

-.EUCI=NL∙QACK'∙Qm

The output bit sequence after rate matching is denoted as  where  is the length of rate matching output sequence in code block number r.fr0, fr1,fr2, …, frEr-1Er

6.3.2.4.1.6UCI with different priority indexes

In this clause, is equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 1, and equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 0. is equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 0, and equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 1. βoffsetHARQ-ACK-LP βoffsetHARQ-ACK,0βoffsetHARQ-ACKβoffsetHARQ-ACK-HP βoffsetHARQ-ACK,1βoffsetHARQ-ACK

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 1:

-If CSI part 1 is also transmitted on the PUSCH,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.1.2, by assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.1.2 is 0 bit.

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.1.3, by taking HARQ-ACK with priority index 0 as CSI part 2 and replacing  by , and assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.1.3 is 0 bit.βoffsetPUSCHβoffsetHARQ-ACK-LP

-Otherwise, perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.1.2, by taking HARQ-ACK with priority index 0 as CSI-part 1 and replacing  by , and assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.1.2 is 0 bit.βoffsetPUSCHβoffsetHARQ-ACK-LP

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 1, and CSI if any are transmitted on a PUSCH associated with priority index 0:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.1.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.1.2, by taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH.

-Perform rate matching for CSI part 2 according to clause 6.3.2.4.1.3, by taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 2 is also transmitted on the PUSCH.

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and/or CG-UCI associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.1.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by , if HARQ-ACK bits associated with priority index 1 are transmitted without CG-UCI associated with priority index 1.βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CG-UCI with priority index 1 according to clause 6.3.2.4.1.4, if CG-UCI associated with priority index 1 is transmitted without HARQ-ACK bits associated with priority index 1.

-Perform rate matching for CG-UCI with priority index 1 and HARQ-ACK with priority index 1 according to clause 6.3.2.4.1.5, if both CG-UCI associated with priority index 1 and HARQ-ACK bits associated with priority index 1 are transmitted, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-If CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 1,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.1.2, by taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.1.3, by taking HARQ-ACK with priority index 0 as CSI part 2 and replacing  by , and taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.βoffsetPUSCHβoffsetHARQ-ACK-LP

-Otherwise,

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.1.2, by taking HARQ-ACK with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.βoffsetPUSCHβoffsetHARQ-ACK-LP,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.1.3, by taking CSI part 1 as CSI part 2 and replacing  by , taking HARQ-ACK with priority index 0 as CSI-part 1 and taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.βoffsetPUSCHβoffsetCSI-part1

If uci-MuxWithDiffPrio is configured, and CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any, HARQ-ACK bits associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 0:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.1.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CG-UCI associated with priority index 0 according to clause 6.3.2.4.1.2, if CG-UCI associated with priority index 0 is transmitted without HARQ-ACK bits associated with priority index 0, by taking CG-UCI associated with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 as HARQ-ACK.βoffsetPUSCHβoffsetCG-UCI,

-Perform rate matching for CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 according to clause 6.3.2.4.1.2, if both CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 are transmitted, by taking CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 as HARQ-ACK.βoffsetPUSCHβoffsetHARQ-ACK-LP,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.1.3, by taking CSI part 1 as CSI part 2 and replacing  by , taking CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any as CSI-part 1 and taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.βoffsetPUSCHβoffsetCSI-part1

## 6.3.2.4.2UCI encoded by channel coding of small block lengths

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedures in this clause and the clauses it refers to apply by replacing CG-UCI with UTO-UCI in all the notations and texts.

6.3.2.4.2.1HARQ-ACK

For HARQ-ACK transmission on PUSCH, the number of coded modulation symbols per layer for HARQ-ACK transmission, denoted as , is determined according to Clause 6.3.2.4.1.1, by setting the number of CRC bits .

The input bit sequence to rate matching is .

Rate matching is performed according to Clause 5.4.3, by setting the rate matching output sequence length , where

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH.

The output bit sequence after rate matching is denoted as .

6.3.2.4.2.2CSI part 1

For CSI part 1 transmission on PUSCH, the number of coded modulation symbols per layer for CSI part 1 transmission, denoted as , is determined according to Clause 6.3.2.4.1.2, by setting the number of CRC bits .

Rate matching is performed according to Clause 5.4.3, by setting the rate matching output sequence length , where

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH.

The output bit sequence after rate matching is denoted as .

6.3.2.4.2.3CSI part 2

For CSI part 2 transmission on PUSCH, the number of coded modulation symbols per layer for CSI part 2 transmission, denoted as , is determined according to Clause 6.3.2.4.1.3, by setting the number of CRC bits .

Rate matching is performed according to Clause 5.4.3, by setting the rate matching output sequence length , where

- is the number of transmission layers of the PUSCH;

- is the modulation order of the PUSCH.

The output bit sequence after rate matching is denoted as .

6.3.2.4.2.4CG-UCI

For CG-UCI transmission on PUSCH, the number of coded modulation symbols per layer for CG-UCI transmission, denoted as , is determined according to Clause 6.3.2.4.1.4, by setting the number of CRC bits .QCG-UCI'LCG-UCI=0

The input bit sequence to rate matching is .d0, d1, d2, …, dN-1

Rate matching is performed according to Clause 5.4.3, by setting the rate matching output sequence length

, whereE=NL∙QCG-UCI'∙Qm

- is the number of transmission layers of the PUSCH;NL

- is the modulation order of the PUSCH.Qm

The output bit sequence after rate matching is denoted as .f0, f1,f2, …, fE-1

6.3.2.4.2.5HARQ-ACK and CG-UCI

For HARQ-ACK and CG-UCI transmission on PUSCH, the number of coded modulation symbols per layer for HARQ-ACK and CG-UCI transmission, denoted as , is determined according to Clause 6.3.2.4.1.5, by setting the number of CRC bits .QACK'LACK=0

The input bit sequence to rate matching is .d0, d1, d2, …, dN-1

Rate matching is performed according to Clause 5.4.3, by setting the rate matching output sequence length , whereE=NL∙QACK'∙Qm

- is the number of transmission layers of the PUSCH;NL

- is the modulation order of the PUSCH.Qm

The output bit sequence after rate matching is denoted as .f0, f1,f2, …, fE-1

6.3.2.4.2.6UCI with different priority indexes

In this clause, is equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 1, and equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 0. is equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 0, and equal to  defined in [5, TS38.213] in case of PUSCH associated with priority index 1. βoffsetHARQ-ACK-LP βoffsetHARQ-ACK,0βoffsetHARQ-ACKβoffsetHARQ-ACK-HP βoffsetHARQ-ACK,1βoffsetHARQ-ACK

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 1:

-If CSI part 1 is also transmitted on the PUSCH,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.2.2, by assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.2.2 is 0 bit.

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.2.3, by taking HARQ-ACK with priority index 0 as CSI part 2 and replacing  by , and assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.2.3 is 0 bit.βoffsetPUSCHβoffsetHARQ-ACK-LP

-Otherwise, perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.2.2, by taking HARQ-ACK with priority index 0 as CSI-part 1 and replacing  by , and assuming the number of HARQ-ACK information bits to be transmitted on PUSCH in clause 6.3.2.4.2.2 is 0 bit.βoffsetPUSCHβoffsetHARQ-ACK-LP

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 1, and CSI if any are transmitted on a PUSCH associated with priority index 0:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.2.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.2.2, by taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH.

-Perform rate matching for CSI part 2 according to clause 6.3.2.4.2.3, by taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 2 is also transmitted on the PUSCH.

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and/or CG-UCI associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.2.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by , if HARQ-ACK bits associated with priority index 1 are transmitted without CG-UCI associated with priority index 1.βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CG-UCI with priority index 1 according to clause 6.3.2.4.2.4, if CG-UCI associated with priority index 1 is transmitted without HARQ-ACK bits associated with priority index 1.

-Perform rate matching for CG-UCI with priority index 1 and HARQ-ACK with priority index 1 according to clause 6.3.2.4.2.5, if both CG-UCI associated with priority index 1 and HARQ-ACK bits associated with priority index 1 are transmitted, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-If CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 1,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.2.2, by taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.2.3, by taking HARQ-ACK with priority index 0 as CSI part 2 and replacing  by , and taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.βoffsetPUSCHβoffsetHARQ-ACK-LP

-Otherwise,

-Perform rate matching for HARQ-ACK with priority index 0 according to clause 6.3.2.4.2.2, by taking HARQ-ACK with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 if any as HARQ-ACK, and taking CG-UCI associated with priority index 1 if any as CG-UCI.βoffsetPUSCHβoffsetHARQ-ACK-LP,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.2.3, by taking CSI part 1 as CSI part 2 and replacing  by , taking HARQ-ACK with priority index 0 as CSI-part 1 and taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.βoffsetPUSCHβoffsetCSI-part1

If uci-MuxWithDiffPrio is configured, and CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any, HARQ-ACK bits associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 0:

-Perform rate matching for HARQ-ACK with priority index 1 according to clause 6.3.2.4.2.1, by taking HARQ-ACK with priority index 1 as HARQ-ACK and replacing  by .βoffsetPUSCHβoffsetHARQ-ACK-HP

-Perform rate matching for CG-UCI associated with priority index 0 according to clause 6.3.2.4.2.2, if CG-UCI associated with priority index 0 is transmitted without HARQ-ACK bits associated with priority index 0, by taking CG-UCI associated with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 as HARQ-ACK.βoffsetPUSCHβoffsetCG-UCI,

-Perform rate matching for CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 according to clause 6.3.2.4.2.2, if both CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 are transmitted, by taking CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 as CSI-part 1 and replacing  by  and taking HARQ-ACK with priority index 1 as HARQ-ACK.βoffsetPUSCHβoffsetHARQ-ACK-LP,

-Perform rate matching for CSI part 1 according to clause 6.3.2.4.2.3, by taking CSI part 1 as CSI part 2 and replacing  by , taking CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any as CSI-part 1 and taking HARQ-ACK with priority index 1 as HARQ-ACK, if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.βoffsetPUSCHβoffsetCSI-part1

## 6.3.2.5Code block concatenation

Code block concatenation is performed according to Clause 6.3.1.5, except that the values of  and  given in Clause 6.3.2.4.1.

## 6.3.2.6Multiplexing of coded UCI bits to PUSCH

The coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7.

## 6.3.2.7Multiplexing of coded UCI bits with different priority indexes to PUSCH

If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedure in this clause 6.3.2.7 applies by replacing CG-UCI with UTO-UCI in all the notations and texts, when applicable.

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 1,

-If CSI part 1 is also transmitted on the PUSCH, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 0 as CSI part 2, and assuming the number of HARQ-ACK information in Clause 6.2.7 is 0 bit;

-Otherwise, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 0 as CSI-part 1, and assuming the number of HARQ-ACK information in Clause 6.2.7 is 0 bit.

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 1, and CSI if any are transmitted on a PUSCH associated with priority index 0, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 1 as HARQ-ACK.

If uci-MuxWithDiffPrio is configured, and HARQ-ACK bits associated with priority index 0, HARQ-ACK bits associated with priority index 1 and/or CG-UCI associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH,

-if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 1, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 1 as HARQ-ACK, and taking HARQ-ACK with priority index 0 as CSI part 2;

-otherwise, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 1 if any as HARQ-ACK, taking CG-UCI associated with priority index 1 if any as CG-UCI, taking HARQ-ACK with priority index 0 as CSI part 1, and taking CSI part 1 as CSI part 2 if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.

If uci-MuxWithDiffPrio is configured, and CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any, HARQ-ACK bits associated with priority index 1, and CSI part 1 if any are transmitted on a PUSCH associated with priority index 0, the coded UCI bits are multiplexed onto PUSCH according to the procedures in Clause 6.2.7 by taking HARQ-ACK with priority index 1 as HARQ-ACK, taking CG-UCI associated with priority index 0 and HARQ-ACK bits associated with priority index 0 if any as CSI part 1, and taking CSI part 1 as CSI part 2 if CSI part 1 is also transmitted on the PUSCH and the PUSCH is associated with priority index 0.

## 7Downlink transport channels and control information

## 7.1Broadcast channel

Data arrives to the coding unit in the form of a maximum of one transport block every 80ms. The following coding steps can be identified:

-Payload generation

-Scrambling

-Transport block CRC attachment

-Channel coding

-Rate matching

## 7.1.1PBCH payload generation

Denote the bits in a transport block delivered to layer 1 by , where  is the payload size generated by higher layers. The lowest order information bit  is mapped to the most significant bit of the transport block as defined in Clause 6.1.1 of [8, TS 38.321].

Generate the following additional timing related PBCH payload bits , where:

- are the 4th, 3rd, 2nd, and 1st LSB of SFN, respectively;

- is the half frame bit ;

-if  as defined in Clause 4.1 of [5, TS38.213], Lmax=10

is the MSB of  as defined in Clause 7.4.3.1 of [4, TS 38.211].aA+5kSSB

is reserved.aA+6

is the MSB of candidate SS/PBCH block index.aA+7

-else if  as defined in Clause 4.1 of [5, TS38.213], Lmax=20

is the MSB of  as defined in Clause 7.4.3.1 of [4, TS 38.211].aA+5kSSB

,  are the 5th and 4th bits of the candidate SS/PBCH block index, respectively.aA+6aA+7

-else if  as defined in Clause 4.1 of [5, TS38.213],Lmax=64

, ,  are the 6th, 5th, and 4th bits of the candidate SS/PBCH block index, respectively.aA+5aA+6aA+7

-else

is the MSB of  as defined in Clause 7.4.3.1 of [4, TS 38.211].aA+5kSSB

is reserved.aA+6

is the enabling/disabling bit for PDCCH repetition of Type0-PDCCH CSS set of searchSpaceZero as defined by Clause 13 of [5, TS38.213].aA+7

-end if

Let ; ; ; ; ;

for  to

if  is an SFN bit

;

;

elseif  is the half radio frame bit

elseif

;

;

else

;

;

end if

end for

where  is the number of candidate SS/PBCH blocks in a half frame according to Clause 4.1 of [5, TS38.213], and the value of  is given by Table 7.1.1-1.Lmax

Table 7.1.1-1: Value of PBCH payload interleaver pattern

## 7.1.2Scrambling

For PBCH transmission in a frame, the bit sequence  is scrambled into a bit sequence , where  for  and  is generated according to the following:

;

;

while

if  corresponds to any one of the bits belonging to the candidate SS/PBCH block index, the half frame index, and 2nd and 3rd least significant bits of the system frame number

;

else

;

;

end if

;

end while

The scrambling sequence  is given by Clause 5.2.1of [4, TS38.211] and initialized with  at the start of each SFN satisfying ;  for  or ,  for ,  for , and  for , where  is the number of candidate SS/PBCH blocks in a half frame according to Clause 4.1 of [5, TS38.213]; and  is determined according to Table 7.1.2-1 using the 3rd and 2nd LSB of the SFN in which the PBCH is transmitted.Lmax=4Lmax=8M=A-4Lmax=10M=A-5Lmax=20Lmax=64Lmax

Table 7.1.2-1: Value of  for PBCH scrambling

## 7.1.3Transport block CRC attachment

Error detection is provided on BCH transport blocks through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. The input bit sequence is denoted by , and the parity bits by, where  is the payload size and  is the number of parity bits.

The parity bits are computed and attached to the BCH transport block according to Clause 5.1 by setting  to 24 bits and using the generator polynomial , resulting in the sequence, where .

The bit sequence  is the input bit sequence  to the channel encoder, where  for  and .

## 7.1.4Channel coding

Information bits are delivered to the channel coding block. They are denoted by  , where  is the number of bits, and they are encoded via Polar coding according to Clause 5.3.1, by setting , , , and .

After encoding the bits are denoted by , where  is the number of coded bits.

## 7.1.5Rate matching

The input bit sequence to rate matching is .

The rate matching output sequence length .

Rate matching is performed according to Clause 5.4.1 by setting .

The output bit sequence after rate matching is denoted as .

## 7.2Downlink shared channel and paging channel

## 7.2.1Transport block CRC attachment

Error detection is provided on each transport block through a Cyclic Redundancy Check (CRC).

The entire transport block is used to calculate the CRC parity bits. Denote the bits in a transport block delivered to layer 1 by, and the parity bits by, where  is the payload size and  is the number of parity bits. The lowest order information bit  is mapped to the most significant bit of the transport block as defined in Clause 6.1.1 of [TS38.321].

The parity bits are computed and attached to the DL-SCH transport block according to Clause 5.1, by setting  to 24 bits and using the generator polynomial  if ; and by setting  to 16 bits and using the generator polynomial  otherwise.

The bits after CRC attachment are denoted by , where .

## 7.2.2LDPC base graph selection

For initial transmission of a transport block with coding rate  indicated by the MCS index according to Clause 5.1.3.1 in [6, TS 38.214] and subsequent re-transmission of the same transport block, each code block of the transport block is encoded with either LDPC base graph 1 or 2 according to the following:

-if , or if  and , or if , LDPC base graph 2 is used;

-otherwise, LDPC base graph 1 is used,

where  is the payload size in Clause 7.2.1.

## 7.2.3Code block segmentation and code block CRC attachment

The bits input to the code block segmentation are denoted by  where  is the number of bits in the transport block (including CRC).

Code block segmentation and code block CRC attachment are performed according to Clause 5.2.2.

The bits after code block segmentation are denoted by, where  is the code block number and  is the number of bits for code block number  according to Clause 5.2.2.

## 7.2.4Channel coding

Code blocks are delivered to the channel coding block. The bits in a code block are denoted by  , where  is the code block number, and  is the number of bits in code block number . The total number of code blocks is denoted by  and each code block is individually LDPC encoded according to Clause 5.3.2.

After encoding the bits are denoted by , where the values of  is given in Clause 5.3.2.

## 7.2.5Rate matching

Coded bits for each code block, denoted as , are delivered to the rate match block, where  is the code block number, and  is the number of encoded bits in code block number . The total number of code blocks is denoted by  and each code block is individually rate matched according to Clause 5.4.2 by setting .

After rate matching, the bits are denoted by, where is the number of rate matched bits for code block number .

## 7.2.6Code block concatenation

The input bit sequence for the code block concatenation block are the sequences , for  and where  is the number of rate matched bits for the -th code block.

Code block concatenation is performed according to Clause 5.5.

The bits after code block concatenation are denoted by, where  is the total number of coded bits for transmission.

## 7.3Downlink control information

A DCI transports downlink control information for one or more cells with one RNTI.

The following coding steps can be identified:

-Information element multiplexing

-CRC attachment

-Channel coding

-Rate matching

## 7.3.1DCI formats

The DCI formats defined in table 7.3.1-1 are supported.

Table 7.3.1-1: DCI formats

The fields defined in the DCI formats below are mapped to the information bits  to  as follows.

Each field is mapped in the order in which it appears in the description, including the zero-padding bit(s), if any, with the first field mapped to the lowest order information bit  and each successive field mapped to higher order information bits. The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to .

If the number of information bits in a DCI format is less than 12 bits, zeros shall be appended to the DCI format until the payload size equals 12.

The size of each DCI format except for DCI format 0_3/1_3 is determined by the configuration of the corresponding active bandwidth part of the scheduled cell and shall be adjusted as described in clause 7.3.1.0 if necessary.

For a cell set configured by higher layer parameter mc-DCI-SetofCellsToAddModList, the size of DCI format 0_3/1_3 is determined as follows and shall be adjusted as described in Clause 7.3.1.0 if necessary:

-If scheduledCellComboListDCI-0-3 for the cell set is configured, the size of DCI format 0_3 is determined by the configuration of the corresponding active bandwidth part(s) of the scheduled cells in the entry which results in the largest size among the entries in the higher layer parameter scheduledCellComboListDCI-0-3; Otherwise, the size of DCI format 0_3 is determined by the configuration of the corresponding active bandwidth part(s) of the cells configured by higher layer parameter scheduledCellListDCI-0-3 for the cell set.

-If scheduledCellComboListDCI-1-3 for the cell set is configured, the size of DCI format 1_3 is determined by the configuration of the corresponding active bandwidth part(s) of the scheduled cells in the entry which results in the largest size among the entries in the higher layer parameter scheduledCellComboListDCI-1-3; Otherwise, the size of DCI format 1_3 is determined by the configuration of the corresponding active bandwidth part(s) of the cells configured by higher layer parameter scheduledCellListDCI-1-3 for the cell set.

If a UE is configured with pdsch-HARQ-ACK-CodebookList-r16, pdsch-HARQ-ACK-Codebook is replaced by the relevant entry in pdsch-HARQ-ACK-CodebookList-r16 in this clause.

If a UE is configured with pdsch-HARQ-ACK-CodebookListMulticast-r17, pdsch-HARQ-ACK-Codebook is replaced by the relevant entry in pdsch-HARQ-ACK-CodebookListMulticast-r17 in this clause.

For a cell detected in cell search procedure with synchronization raster defined in Table 5.4.3.1-2 or Table 5.4.3.1-3 of [13, TS 38.101-1] or Table 5.4.3.1-2 of [15, TS 38.101-5], the size of CORESET 0 for the cell in this clause refers to the size of punctured CORESET 0 as defined in clause 7.3.2.2 of [4, TS 38.211] if any.

## 7.3.1.0DCI size alignment

If necessary, padding or truncation shall be applied to the DCI formats according to the following steps executed in the order below:

Step 0:

-Determine DCI format 0_0 monitored in a common search space according to clause 7.3.1.1.1 where  is the size of the initial UL bandwidth part.

-Determine DCI format 1_0 monitored in a common search space according to clause 7.3.1.2.1 where  is given by

-the size of CORESET 0 if CORESET 0 is configured for the cell; and

-the size of initial DL bandwidth part if CORESET 0 is not configured for the cell.

-If DCI format 0_0 is monitored in common search space and if the number of information bits in the DCI format 0_0 prior to padding is less than the payload size of the DCI format 1_0 monitored in common search space for scheduling the same serving cell, a number of zero padding bits are generated for the DCI format 0_0 until the payload size equals that of the DCI format 1_0.

-If DCI format 0_0 is monitored in common search space and if the number of information bits in the DCI format 0_0 prior to truncation is larger than the payload size of the DCI format 1_0 monitored in common search space for scheduling the same serving cell, the bitwidth of the frequency domain resource assignment field in the DCI format 0_0 is reduced by truncating the first few most significant bits such that the size of DCI format 0_0 equals the size of the DCI format 1_0.

Step 1:

-Determine DCI format 0_0 monitored in a UE-specific search space according to clause 7.3.1.1.1 where  is the size of the active UL bandwidth part.

-Determine DCI format 1_0 monitored in a UE-specific search space according to clause 7.3.1.2.1 where  is the size of the active DL bandwidth part.

-For a UE configured with supplementaryUplink in ServingCellConfig in a cell, if PUSCH is configured to be transmitted on both the SUL and the non-SUL of the cell and if the number of information bits in DCI format 0_0 in UE-specific search space for the SUL is not equal to the number of information bits in DCI format 0_0 in UE-specific search space for the non-SUL, a number of zero padding bits are generated for the smaller DCI format 0_0 until the payload size equals that of the larger DCI format 0_0.

-If DCI format 0_0 is monitored in UE-specific search space and if the number of information bits in the DCI format 0_0 prior to padding is less than the payload size of the DCI format 1_0 monitored in UE-specific search space for scheduling the same serving cell, a number of zero padding bits are generated for the DCI format 0_0 until the payload size equals that of the DCI format 1_0.

-If DCI format 1_0 is monitored in UE-specific search space and if the number of information bits in the DCI format 1_0 prior to padding is less than the payload size of the DCI format 0_0 monitored in UE-specific search space for scheduling the same serving cell, zeros shall be appended to the DCI format 1_0 until the payload size equals that of the DCI format 0_0

Step 2:

-Determine DCI format 0_1 monitored in a UE-specific search space according to clause 7.3.1.1.2.

-Determine DCI format 1_1 monitored in a UE-specific search space according to clause 7.3.1.2.2.

-For a UE configured with supplementaryUplink in ServingCellConfig in a cell, if PUSCH is configured to be transmitted on both the SUL and the non-SUL of the cell and if the number of information bits in format 0_1 for the SUL is not equal to the number of information bits in format 0_1 for the non-SUL, zeros shall be appended to smaller format 0_1 until the payload size equals that of the larger format 0_1.

-If the size of DCI format 0_1 monitored in a UE-specific search space equals that of a DCI format 0_0/1_0 monitored in another UE-specific search space, one bit of zero padding shall be appended to DCI format 0_1.

-If the size of DCI format 1_1 monitored in a UE-specific search space equals that of a DCI format 0_0/1_0 monitored in another UE-specific search space, one bit of zero padding shall be appended to DCI format 1_1.

Step 2A:

-Determine DCI format 0_2 monitored in a UE-specific search space according to clause 7.3.1.1.3.

-Determine DCI format 1_2 monitored in a UE-specific search space according to clause 7.3.1.2.3.

-For a UE configured with supplementaryUplink in ServingCellConfig in a cell, if PUSCH is configured to be transmitted on both the SUL and the non-SUL of the cell and if the number of information bits in format 0_2 for the SUL is not equal to the number of information bits in format 0_2 for the non-SUL, zeros shall be appended to smaller format 0_2 until the payload size equals that of the larger format 0_2.

Step 2B:

-If the cell is the serving cell for counting the size of one or both DCI format 0_3 and DCI format 1_3 as defined in Clause 10.1 of [5, TS38.213],

-Determine DCI format 0_3 monitored in a UE-specific search space according to clause 7.3.1.1.4.

-Determine DCI format 1_3 monitored in a UE-specific search space according to clause 7.3.1.2.4.

Step 3:

-If both of the following conditions are fulfilled the size alignment procedure is complete

-the total number of different DCI sizes configured to monitor is no more than 4 for the cell

-the total number of different DCI sizes with C-RNTI configured to monitor is no more than 3 for the cell

Step 4:

-Otherwise

Step 4A:

-Remove the padding bit (if any) introduced in step 2 above.

-Determine DCI format 1_0 monitored in a UE-specific search space according to clause 7.3.1.2.1 where  is given by

-the size of CORESET 0 if CORESET 0 is configured for the cell; and

-the size of initial DL bandwidth part if CORESET 0 is not configured for the cell.

-Determine DCI format 0_0 monitored in a UE-specific search space according to clause 7.3.1.1.1 where  is the size of the initial UL bandwidth part.

-If the number of information bits in the DCI format 0_0 monitored in a UE-specific search space prior to padding is less than the payload size of the DCI format 1_0 monitored in UE-specific search space for scheduling the same serving cell, a number of zero padding bits are generated for the DCI format 0_0 monitored in a UE-specific search space until the payload size equals that of the DCI format 1_0 monitored in a UE-specific search space.

-If the number of information bits in the DCI format 0_0 monitored in a UE-specific search space prior to truncation is larger than the payload size of the DCI format 1_0 monitored in UE-specific search space for scheduling the same serving cell, the bitwidth of the frequency domain resource assignment field in the DCI format 0_0 is reduced by truncating the first few most significant bits such that the size of DCI format 0_0 monitored in a UE-specific search space equals the size of the DCI format 1_0 monitored in a UE-specific search space.

Step 4B:

-If the total number of different DCI sizes configured to monitor is more than 4 for the cell after applying the above steps, or if the total number of different DCI sizes with C-RNTI configured to monitor is more than 3 for the cell after applying the above steps

-If the number of information bits in the DCI format 0_2 prior to padding is less than the payload size of the DCI format 1_2 for scheduling the same serving cell, a number of zero padding bits are generated for the DCI format 0_2 until the payload size equals that of the DCI format 1_2.

-If the number of information bits in the DCI format 1_2 prior to padding is less than the payload size of the DCI format 0_2 for scheduling the same serving cell, zeros shall be appended to the DCI format 1_2 until the payload size equals that of the DCI format 0_2.

Step 4C:

-If the total number of different DCI sizes configured to monitor is more than 4 for the cell after applying the above steps, or if the total number of different DCI sizes with C-RNTI configured to monitor is more than 3 for the cell after applying the above steps

-If the number of information bits in the DCI format 0_1 prior to padding is less than the payload size of the DCI format 1_1 for scheduling the same serving cell, a number of zero padding bits are generated for the DCI format 0_1 until the payload size equals that of the DCI format 1_1.

-If the number of information bits in the DCI format 1_1 prior to padding is less than the payload size of the DCI format 0_1 for scheduling the same serving cell, zeros shall be appended to the DCI format 1_1 until the payload size equals that of the DCI format 0_1.

Step 4D:

-If the total number of different DCI sizes configured to monitor is more than 4 for the cell after applying the above steps and the cell is the serving cell for counting the size of one or both DCI format 0_3 and DCI format 1_3 as defined in Clause 10.1 of [5, TS38.213], or if the total number of different DCI sizes with C-RNTI configured to monitor is more than 3 for the cell after applying the above steps and the cell is the serving cell for counting the size of one or both DCI format 0_3 and DCI format 1_3 as defined in Clause 10.1 of [5, TS38.213]

-If the number of information bits in the DCI format 0_3 prior to padding is less than the payload size of the DCI format 1_3 for scheduling the same cell set, a number of zero padding bits are generated for the DCI format 0_3 until the payload size equals that of the DCI format 1_3.

-If the number of information bits in the DCI format 1_3 prior to padding is less than the payload size of the DCI format 0_3 for scheduling the same cell set, zeros shall be appended to the DCI format 1_3 until the payload size equals that of the DCI format 0_3.

The UE is not expected to handle a configuration that, after applying the above steps, results in

-the total number of different DCI sizes configured to monitor is more than 4 for the cell; or

-the total number of different DCI sizes with C-RNTI configured to monitor is more than 3 for the cell; or

-the size of DCI format 0_0 in a UE-specific search space is equal to DCI format 0_1 in another UE-specific search space; or

-the size of DCI format 1_0 in a UE-specific search space is equal to DCI format 1_1 in another UE-specific search space; or

-the size of DCI format 0_0 in a UE-specific search space is equal to DCI format 0_2 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 0_0 and 0_2 are mapped to the same resource; or

-the size of DCI format 1_0 in a UE-specific search space is equal to DCI format 1_2 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 1_0 and 1_2 are mapped to the same resource; or

-the size of DCI format 0_1 in a UE-specific search space is equal to DCI format 0_2 in the same or another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 0_1 and 0_2 are mapped to the same resource; or

-the size of DCI format 1_1 in a UE-specific search space is equal to DCI format 1_2 in the same or another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 1_1 and 1_2 are mapped to the same resource; or

-the size of DCI format 0_0 in a UE-specific search space is equal to DCI format 0_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 0_0 and 0_3 are mapped to the same resource; or

-the size of DCI format 1_0 in a UE-specific search space is equal to DCI format 1_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 1_0 and 1_3 are mapped to the same resource; or

-the size of DCI format 0_1 in a UE-specific search space is equal to DCI format 0_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 0_1 and 0_3 are mapped to the same resource; or

-the size of DCI format 1_1 in a UE-specific search space is equal to DCI format 1_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 1_1 and 1_3 are mapped to the same resource.

-the size of DCI format 0_2 in a UE-specific search space is equal to DCI format 0_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 0_2 and 0_3 are mapped to the same resource; or

-the size of DCI format 1_2 in a UE-specific search space is equal to DCI format 1_3 in another UE-specific search space when at least one pair of the corresponding PDCCH candidates of DCI formats 1_2 and 1_3 are mapped to the same resource.

## 7.3.1.0.1DCI size alignment for DCI formats for scheduling of sidelink

If DCI format 3_0, and/or DCI format 3_1, and/or DCI format 3_2 is monitored on a cell, DCI size alignment for DCI format 3_0, DCI format 3_1, and DCI format 3_2 is performed as described in this clause after performing the DCI size alignment described in Clause 7.3.1.0. The size(s) of the DCI formats configured to monitor for a cell in this clause refers to that after performing the DCI size alignment described in Clause 7.3.1.0.

If DCI format 3_0, and/or DCI format 3_1, and/or DCI format 3_2 is monitored on a cell and the total number of DCI sizes of the DCI formats configured to monitor for the cell and DCI format 3_0, and/or DCI format 3_1, and/or DCI format 3_2 is more than 4, zeros shall be appended to DCI format 3_0 if configured, to DCI format 3_1 if configured, and to DCI format 3_2 if configured, until the payload size of DCI format 3_0, DCI format 3_1, and DCI format 3_2 equals that of the smallest DCI format configured to monitor for the cell that is larger than DCI format 3_0, DCI format 3_1, and DCI format 3_2.

The UE is not expected to handle a configuration that results in:

-the total number of different DCI sizes configured to monitor for the cell and DCI format 3_0, and/or DCI format 3_1, and/or DCI format 3_2 is more than 4; and

-the payload size of DCI format 3_0, and/or DCI format 3_1, and/or DCI format 3_2 is larger than the payload size of all other DCI formats configured to monitor for the cell.

## 7.3.1.1DCI formats for scheduling of PUSCH

## 7.3.1.1.1Format 0_0

DCI format 0_0 is used for the scheduling of PUSCH in one cell.

The following information is transmitted by means of the DCI format 0_0 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 0, indicating an UL DCI format

-Frequency domain resource assignment - number of bits determined by the following:

- bits if neither of the higher layer parameters useInterlacePUCCH-PUSCH in BWP-UplinkCommon and useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is configured, where  is defined in clause 7.3.1.0

-For PUSCH hopping with resource allocation type 1:

- MSB bits are used to indicate the frequency offset according to Clause 6.3 of [6, TS 38.214], where  if the higher layer parameter frequencyHoppingOffsetLists contains two offset values and  if the higher layer parameter frequencyHoppingOffsetLists contains four offset values

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

-For non-PUSCH hopping with resource allocation type 1:

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

-If any of the higher layer parameters useInterlacePUCCH-PUSCH in BWP-UplinkCommon and useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is configured

-5+Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 30 kHz.

-6+Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 15 kHz.

If the DCI format 0_0 is monitored in a UE-specific search space, the value of Y is determined by  where  is the number of RB sets contained in the active UL BWP as defined in clause 7 of [6, TS38.214]. If the DCI 0_0 is monitored in a common search space Y = 0.log2NRB-set,ULBWPNRB-set,ULBWP+12NRB-set,ULBWP

-Time domain resource assignment - 4 bits as defined in Clause 6.1.2.1 of [6, TS 38.214]

-Frequency hopping flag - 1 bit according to Table 7.3.1.1.1-3, as defined in Clause 6.3 of [6, TS 38.214]

-Modulation and coding scheme - 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits

-TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS 38.213]

-ChannelAccess-CPext - 2 bits indicating combinations of channel access type and CP extension as defined in Table 7.3.1.1.1-4, or Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1; 2 bits indicating channel access type as defined in Table 7.3.1.1.1-4B if ChannelAccessMode2-r17 is provided for operation in a cell in frequency range 2-2; 0 bit otherwise.

-Padding bits, if required.

-UL/SUL indicator - 1 bit for UEs configured with supplementaryUplink in ServingCellConfig in the cell as defined in Table 7.3.1.1.1-1 and the number of bits for DCI format 1_0 before padding is larger than the number of bits for DCI format 0_0 before padding; 0 bit otherwise. The UL/SUL indicator, if present, locates in the last bit position of DCI format 0_0, after the padding bit(s).

-If the UL/SUL indicator is present in DCI format 0_0 and the higher layer parameter pusch-Config is not configured on both UL and SUL the UE ignores the UL/SUL indicator field in DCI format 0_0, and the corresponding PUSCH scheduled by the DCI format 0_0 is for the UL or SUL for which high layer parameter pucch-Config is configured;

-If the UL/SUL indicator is not present in DCI format 0_0 and pucch-Config is configured, the corresponding PUSCH scheduled by the DCI format 0_0 is for the UL or SUL for which high layer parameter pucch-Config is configured.

-If the UL/SUL indicator is not present in DCI format 0_0 and pucch-Config is not configured, the corresponding PUSCH scheduled by the DCI format 0_0 is for the uplink on which the latest PRACH is transmitted.

The following information is transmitted by means of the DCI format 0_0 with CRC scrambled by TC-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 0, indicating an UL DCI format

-Frequency domain resource assignment - number of bits determined by the following:

-bits if the higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkCommon is not configured, where

- is the size of the initial UL bandwidth part.

-For PUSCH hopping with resource allocation type 1:

- MSB bits are used to indicate the frequency offset according to Table 8.3-1 in Clause 8.3 of [5, TS 38.213], where  if  and  otherwise

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

-For non-PUSCH hopping with resource allocation type 1:

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

-If the higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkCommon is configured

-5 bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 30 kHz

-6 bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 15 kHz

-Time domain resource assignment - 4 bits as defined in Clause 6.1.2.1 of [6, TS 38.214]

-Frequency hopping flag - 1 bit according to Table 7.3.1.1.1-3, as defined in Clause 6.3 of [6, TS 38.214]

-Modulation and coding scheme - 5 bits

-If the UE requests repetition of PUSCH scheduled by RAR UL grant [8, TS 38.321], 5 bits as defined in Clause 6.1.2.1 and Clause 6.1.4.1 of [6, TS 38.214];

-otherwise 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214].

-New data indicator - 1 bit, reserved

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits, reserved

-TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS 38.213]

-ChannelAccess-CPext - 2 bits indicating combinations of channel access type and CP extension as defined in Table 7.3.1.1.1-4, or Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1; 2 bits indicating channel access type as defined in Table 7.3.1.1.1-4B if ChannelAccessMode2-r17 is provided for operation in a cell in frequency range 2-2; 0 bit otherwise

-Padding bits, if required.

-UL/SUL indicator - 1 bit if the cell has two ULs and the number of bits for DCI format 1_0 before padding is larger than the number of bits for DCI format 0_0 before padding; 0 bit otherwise. The UL/SUL indicator, if present, locates in the last bit position of DCI format 0_0, after the padding bit(s).

-If 1 bit, reserved, and the corresponding PUSCH is always on the same UL carrier as the previous transmission of the same TB

Table 7.3.1.1.1-1: UL/SUL indicator

Table 7.3.1.1.1-2: Redundancy version

Table 7.3.1.1.1-3: Frequency hopping indication

Table 7.3.1.1.1-4: Channel access type & CP extension for DCI format 0_0 andDCI format 1_0 for frequency range 1

Table 7.3.1.1.1-4A: Channel access type & CP extension ifchannelAccessMode-r16 = "semiStatic" is provided

Table 7.3.1.1.1-4B: Channel access type for DCI format 0_0 andDCI format 1_0 for frequency range 2-2

## 7.3.1.1.2Format 0_1

DCI format 0_1 is used for the scheduling of one or multiple PUSCH in one cell, or indicating CG downlink feedback information (CG-DFI) to a UE.

The following information is transmitted by means of the DCI format 0_1 with CRC scrambled by C-RNTI or CS-RNTI or SP-CSI-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 0, indicating an UL DCI format

-Carrier indicator - 0 or 3 bits, as defined in Clause 10.1 of [5, TS38.213]. This field is reserved when this format is carried by PDCCH on the primary cell and the UE is configured for scheduling on the primary cell from an SCell, with the same number of bits as that in this format carried by PDCCH on the SCell for scheduling on the primary cell.

-DFI flag - 0 or 1 bit

-1 bit if the UE is configured to monitor DCI format 0_1 with CRC scrambled by CS-RNTI and for operation in a cell with shared spectrum channel access when the higher layer parameter cg-RetransmissionTimer is configured. For a DCI format 0_1 with CRC scrambled by CS-RNTI, the bit value of 0 indicates activating or releasing type 2 CG transmission and the bit value of 1 indicates CG-DFI. For a DCI format 0_1 with CRC scrambled by C-RNTI/SP-CSI-RNTI/MCS-C-RNTI and for operation in a cell with shared spectrum channel access, the bit is reserved.

-0 bit otherwise;

If DCI format 0_1 is used for indicating CG-DFI, all the remaining fields are set as follows:

-HARQ-ACK bitmap - 16 bits if nrofHARQ-Processes-v1700 in ConfiguredGrantConfig is not configured or 32 bits if nrofHARQ-Processes-v1700 in ConfiguredGrantConfig is configured, where the order of the bitmap to HARQ process index mapping is such that HARQ process indices are mapped in ascending order from MSB to LSB of the bitmap. For each bit of the bitmap, value 1 indicates ACK, and value 0 indicates NACK.

-TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS38.213]

-All the remaining bits in format 0_1 are set to zero.

Otherwise, all the remaining fields are set as follows:

-UL/SUL indicator - 0 bit for UEs not configured with supplementaryUplink in ServingCellConfig in the cell or UEs configured with supplementaryUplink in ServingCellConfig in the cell but only one carrier in the cell is configured for PUSCH transmission; otherwise, 1 bit as defined in Table 7.3.1.1.1-1.

-Bandwidth part indicator - 0, 1 or 2 bits as determined by the number of UL BWPs  configured by higher layers, excluding the initial UL bandwidth part. The bitwidth for this field is determined as bits, where

- if , in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;

If a UE does not support active BWP change via DCI, the UE ignores this bit field.

-Frequency domain resource assignment - number of bits determined by the following, where  is the size of the active UL bandwidth part:

-If higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is not configured

- bits if only resource allocation type 0 is configured, where  is defined in Clause 6.1.2.2.1 of [6, TS 38.214],

-bits if only resource allocation type 1 is configured, or  bits if resourceAllocation is configured as 'dynamicSwitch'.

-If resourceAllocation is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 6.1.2.2.1 of [6, TS 38.214].

-For resource allocation type 1, the  LSBs provide the resource allocation as follows:

-For PUSCH hopping with resource allocation type 1:

- MSB bits are used to indicate the frequency offset according to Clause 6.3 of [6, TS 38.214], where  if the higher layer parameter frequencyHoppingOffsetLists contains two offset values and  if the higher layer parameter frequencyHoppingOffsetLists contains four offset values

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

-For non-PUSCH hopping with resource allocation type 1:

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocation is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

-If the higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is configured

-5 + Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 30 kHz. The 5 MSBs provide the interlace allocation and the Y LSBs provide the RB set allocation.

-6 + Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 15 kHz. The 6 MSBs provide the interlace allocation and the Y LSBs provide the RB set allocation.

The value of Y is determined by  where   is the number of RB sets contained in the active UL BWP as defined in clause 7 of [6, TS38.214].log2NRB-set,ULBWPNRB-set,ULBWP+12 NRB-set,ULBWP

-Time domain resource assignment - 0, 1, 2, 3, 4, 5, or 6 bits

-If the higher layer parameter pusch-TimeDomainAllocationListDCI-0-1 is not configured and if the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH is not configured and if the higher layer parameter pusch-TimeDomainAllocationList is configured, 0, 1, 2, 3, or 4 bits as defined in Clause 6.1.2.1 of [6, TS38.214]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter pusch-TimeDomainAllocationList;

-If the higher layer parameter pusch-TimeDomainAllocationListDCI-0-1 is configured or if the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH is configured, 0, 1, 2, 3, 4, 5 or 6 bits as defined in Clause 6.1.2.1 of [6, TS38.214]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter pusch-TimeDomainAllocationListDCI-0-1 or pusch-TimeDomainAllocationListForMultiPUSCH; log2(I)

-otherwise the bitwidth for this field is determined as bits, where I is the number of entries in the default table.log2(I)

-Frequency hopping flag - 0 or 1 bit:

-0 bit if only resource allocation type 0 is configured, or if the higher layer parameter frequencyHopping is not configured and the higher layer parameter pusch-RepTypeIndicatorDCI-0-1 is not configured to pusch-RepTypeB, or if the higher layer parameter frequencyHoppingDCI-0-1 is not configured and pusch-RepTypeIndicatorDCI-0-1 is configured to pusch-RepTypeB, or if only resource allocation type 2 is configured;

-1 bit according to Table 7.3.1.1.1-3 otherwise, only applicable to resource allocation type 1, as defined in Clause 6.3 of [6, TS 38.214].

For transport block 1:

-Modulation and coding scheme - 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214]

-New data indicator - 1 bit if the number of scheduled PUSCH indicated by the Time domain resource assignment field is 1; otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined based on the maximum number of schedulable PUSCH among all entries in the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH, where each bit corresponds to one scheduled PUSCH as defined in clause 6.1.4 in [6, TS 38.214].

-Redundancy version - - number of bits determined by the following:

-2 bits as defined in Table 7.3.1.1.1-2 if the number of scheduled PUSCH indicated by the Time domain resource assignment field is 1;

-otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined by the maximum number of schedulable PUSCHs among all entries in the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH, where each bit corresponds to one scheduled PUSCH as defined in clause 6.1.4 in [6, TS 38.214] and redundancy version is determined according to Table 7.3.1.1.2-34.

For transport block 2 (only present if maxRank or maxMIMO-Layers is larger than 4):

-Modulation and coding scheme - 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part, maxRank is larger than 4 or the value of maxMIMO-Layers for the indicated bandwidth part is larger than 4 and the value of maxRank or maxMIMO-Layers for the active bandwidth part is no more than 4, the UE assumes zeros are padded when interpreting the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields for transport block 2 according to Clause 12 of [5, TS38.213], and the UE ignores the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields of transport block 2 for the indicated bandwidth part.

-Transform precoder indicator - 0 or 1 bit

-1 bit if the higher layer parameter dynamicTransformPrecoderFieldPresenceDCI-0-1 is configured to 'enabled ' and if the UE is configured to monitor DCI format 0_1 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI, where the bit value of 0 indicates that transform precoder is enabled and the bit value of 1 indicates that transform precoder is disabled. For a DCI format 0_1 with CRC scrambled by CS-RNTI and the value indicated by new data indicator field is 0, or for a DCI format 0_1 with CRC scrambled by SP-CSI-RNTI, the bit is reserved.

-0 bit otherwise.

-HARQ process number - 5 bits if higher layer parameter harq-ProcessNumberSizeDCI-0-1 or harq-ProcessNumberSizeDCI-0-1-Ext is configured; otherwise 4 bits

-1st downlink assignment index - 1, 2 or 4 bits:

-1 bit for semi-static HARQ-ACK codebook for unicast and multicast if pdsch-HARQ-ACK-Codebook = semiStatic is configured for both unicast and multicast and the higher layer parameter fdmed-ReceptionMulticast is not configured; otherwise for semi-static HARQ-ACK codebook for unicast;

-2 bits for dynamic HARQ-ACK codebook for unicast, or for enhanced dynamic HARQ-ACK codebook without UL-TotalDAI-Included configured;

-4 bits for enhanced dynamic HARQ-ACK codebook and with UL-TotalDAI-Included = true.

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookList for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-1 is configured, if the bit width of the 1st downlink assignment index in DCI format 0_1 for one HARQ-ACK codebook is not equal to that of the 1st downlink assignment index in DCI format 0_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 1st  downlink assignment index until the bit width of the 1st downlink assignment index in DCI format 0_1 for the two HARQ-ACK codebooks are the same.

-2nd downlink assignment index - 0, 2 or 4 bits:

-2 bits for dynamic HARQ-ACK codebook with two HARQ-ACK sub-codebooks for unicast, or for enhanced dynamic HARQ-ACK codebook with two HARQ-ACK sub-codebooks and without UL-TotalDAI-Included configured;

-4 bits for enhanced dynamic HARQ-ACK codebook with two HARQ-ACK sub-codebooks and with UL-TotalDAI-Included = true;

-0 bit otherwise.

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookList for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-1 is configured, if the bit width of the 2nd downlink assignment index in DCI format 0_1 for one HARQ-ACK codebook is not equal to that of the 2nd downlink assignment index in DCI format 0_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 2nd downlink assignment index until the bit width of the 2nd downlink assignment index in DCI format 0_1 for the two HARQ-ACK codebooks are the same.

-3rd downlink assignment index - 0, 1 or 2 bits:

-1 bit for semi-static HARQ-ACK codebook for multicast if the higher layer parameter fdmed-ReceptionMulticast is configured;

-2 bits for the dynamic HARQ-ACK codebook for multicast;

-0 bit otherwise.

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookListMulticast for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-1 is configured, if the bit width of the 3rd downlink assignment index in DCI format 0_1 for one HARQ-ACK codebook is not equal to that of the 3rd downlink assignment index in DCI format 0_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 3rd downlink assignment index until the bit width of the 3rd downlink assignment index in DCI format 0_1 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS38.213]

-Second TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS38.213] if higher layer parameter SecondTPCFieldDCI-0-1 is configured; 0 bit otherwise.

-SRS resource set indicator - 0 or 2 bits

-2 bits according to Table 7.3.1.1.2-36 if

-txConfig = nonCodeBook, and there are two SRS resource sets configured by srs-ResourceSetToAddModList and associated with the usage of value 'nonCodeBook', and is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided, or

-txConfig=codebook, and there are two SRS resource sets configured by srs-ResourceSetToAddModList and associated with usage of value 'codebook', and is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided;

-0 bit otherwise.

-SRS resource indicator -number of bits determined by the following:

- bits according to Tables 7.3.1.1.2-28/28A/29/29B/30/30B/31/31B/31C/31D/31E/31F if the higher layer parameter txConfig = nonCodebook, where

- is the number of configured SRS resources in the SRS resource set indicated by SRS resource set indicator field if present,

- is the number of configured SRS resources in the SRS resource set associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_1, if the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel,NSRS

-otherwise  is the number of configured SRS resources in the SRS resource set configured by higher layer parameter srs-ResourceSetToAddModList and associated with the higher layer parameter usage of value 'nonCodeBook', NSRS

and

-if UE supports operation with maxMIMO-Layers and the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured,

-Lmax is given by max{maxMIMO-Layers, maxMIMO-LayersforSDM} if maxMIMO-LayersforSDM is configured

-Lmax is given by max{maxMIMO-Layers, maxMIMO-LayersforSFN} if maxMIMO-LayersforSFN is configured

-Lmax is given by maxMIMO-Layers otherwise

-otherwise, Lmax is given by the maximum number of layers for PUSCH supported by the UE for the serving cell for non-codebook based operation.

- bits according to Tables 7.3.1.1.2-32, 7.3.1.1.2-32A and 7.3.1.1.2-32B if the higher layer parameter txConfig = codebook, where

- is the number of configured SRS resources in the SRS resource set indicated by SRS resource set indicator field if present,

- is the number of configured SRS resources in the SRS resource set associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_1, if the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel,NSRS

-otherwise  is the number of configured SRS resources in the SRS resource set configured by higher layer parameter srs-ResourceSetToAddModList and associated with the higher layer parameter usage of value 'codeBook'.NSRS

When the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel, and there are two SRS resource sets configured by srs-ResourceSetToAddModList and associated with usage of value 'codebook' or 'nonCodeBook', the first SRS resource set is associated with coresetPoolIndex value 0 and the second SRS resource set is associated with coresetPoolIndex value 1, where the first and the second SRS resource sets are respectively the ones with lower and higher srs-ResourceSetId of the two SRS resources sets.

-Second SRS resource indicator - number of bits determined by the following:

- bits according to Tables 7.3.1.1.2-28/29A/30A/31A with the same number of layers indicated by SRS resource indicator field if the higher layer parameter txConfig = nonCodebook, the higher layer paramtere maxMIMO-LayersforSDM is not configured, and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set, andlog2(maxk∈{1,2,…,min⁡{Lmax,NSRS}}NSRSk)NSRS

-if UE supports operation with maxMIMO-Layers and the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured,

-Lmax is given by maxMIMO-LayersforSFN if maxMIMO-LayersforSFN is configured

-Lmax is given by maxMIMO-Layers otherwise

-otherwise, Lmax is given by the maximum number of layers for PUSCH supported by the UE for the serving cell for non-codebook based operation.

- bits according to Tables 7.3.1.1.2-28/29 if the higher layer parameter txConfig = nonCodebook, the higher layer paramtere maxMIMO-LayersforSDM is configured and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set, and Lmax is given by maxMIMO-LayersforSDM.NSRS

- bits according to Tables 7.3.1.1.2-32, 7.3.1.1.2-32A and 7.3.1.1.2-32B if the higher layer parameter txConfig = codebook and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set.log2(NSRS)NSRS

-0 bit otherwise.

-Precoding information and number of layers - number of bits determined by the following:

-0 bits if the higher layer parameter txConfig = nonCodeBook;

-0 bits for 1 antenna port and if the higher layer parameter txConfig = codebook;

-4, 5, or 6 bits according to Table 7.3.1.1.2-2 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} if multipanelSchemeSDM is configured, and codebookSubset;

-4 or 5 bits according to Table 7.3.1.1.2-2A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} = 2 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} = 2 if multipanelSchemeSDM is configured, transform precoder is disabled, and according to the values of higher layer parameter codebookSubset;

-4 or 6 bits according to Table 7.3.1.1.2-2B for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=3 or 4, transform precoder is disabled, and according to the values of higher layer parameter codebookSubset;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} = 1 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} = 1 if multipanelSchemeSDM is configured, and codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-3A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} = 1 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} = 1 if multipanelSchemeSDM is configured, and the values of higher layer parameter codebookSubset;

-2 or 4 bits according to Table7.3.1.1.2-4 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} if multipanelSchemeSDM is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-4A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, transform precoder is disabled, maxRank=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} = 2 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} = 2 if multipanelSchemeSDM is configured, and codebookSubset=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN}=1 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM}=1 if multipanelSchemeSDM is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-5A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRank, maxRankSFN} = 1 if multipanelSchemeSFN is configured or max{maxRank, maxRankSDM} = 1 if multipanelSchemeSDM is configured, and the values of higher layer parameter codebookSubset;

-7 bits according to Table 7.3.1.1.2-5B for 8 antenna ports, if CodebookTypeUL= codebook1, transform precoder is disabled, maxRank = 8, and according to codebook1;

-7 bits according to Table 7.3.1.1.2-5C for 8 antenna ports, if CodebookTypeUL= codebook1, transform precoder is disabled, maxRank = 7, and according to codebook1;

-7 bits according to Table 7.3.1.1.2-5D for 8 antenna ports, if CodebookTypeUL= codebook1, transform precoder is disabled, maxRank = 4, 5 or 6, and according to maxRank;

-4, 6 or 7 bits according to Table 7.3.1.1.2-5E for 8 antenna ports, if CodebookTypeUL= codebook1, transform precoder is enabled or maxRank = 1, 2 or 3 if transform precoder is disabled, and according to transform precoder and maxRank;

-8 bits according to Table 7.3.1.1.2-5F for 8 antenna ports, if CodebookTypeUL= codebook4, transform precoder is disabled, maxRank = 5, 6, 7 or 8, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to maxRank;

-6 or 7 or 8 bits according to Table 7.3.1.1.2-5G for 8 antenna ports, if CodebookTypeUL= codebook4, transform precoder is disabled, maxRank = 2, 3 or 4, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to maxRank;

-3 bits according to Table 7.3.1.1.2-5H for 8 antenna ports, if CodebookTypeUL= codebook4, transform precoder is enabled or maxRank = 1 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower.

-10 bits according to Table 7.3.1.1.2-5I for 8 antenna ports, if CodebookTypeUL=codebook2, transform precoder is disabled, maxRank = 5, 6, 7 or 8, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to maxRank;

-5, 9 or 10 bits according to Table 7.3.1.1.2-5J for 8 antenna ports, if CodebookTypeUL=codebook2, transform precoder is enabled or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to transform precoder and maxRank;

-10 bits according to Table 7.3.1.1.2-5K for 8 antenna ports, if CodebookTypeUL=codebook3, transform precoder is disabled, maxRank = 5, 6, 7 or 8, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to maxRank;

-4, 7, 9 or 10 bits according to Table 7.3.1.1.2-5L for 8 antenna ports, if CodebookTypeUL=codebook3, transform precoder is enabled or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to transform precoder and maxRank;

-6 or 7 or 8 bits according to Table 7.3.1.1.2-5M for 8 antenna ports, if CodebookTypeUL=codebook4, transform precoder is disabled, maxRank = 2, 3 or 4, ul-FullPowerTransmission is configured to fullpowerMode1, and according to maxRank;

-4 bits according to Table 7.3.1.1.2-5N for 8 antenna ports, if CodebookTypeUL=codebook4, transform precoder is enabled or maxRank = 1 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1.

-6, 9 or 10 bits according to Table 7.3.1.1.2-5O for 8 antenna ports, if CodebookTypeUL=codebook2, transform precoder is enabled or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1, and according to transform precoder and maxRank;

-5, 7, 9 or 10 bits according to Table 7.3.1.1.2-5P for 8 antenna ports, if CodebookTypeUL=codebook3, transform precoder is enabled or maxRank = 1, 2, 3, or 4 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1, and according to transform precoder and maxRank;

-8 or 9 bits according to Table 7.3.1.1.2-5Q for 8 antenna ports, if CodebookTypeUL=codebook4, transform precoder is disabled, maxRank = 5, 6, 7 or 8, ul-FullPowerTransmission is configured to fullpowerMode1, and according to maxRank;

-10 bits according to Table 7.3.1.1.2-5R for 8 antenna ports, if CodebookTypeUL=codebook2, transform precoder is disabled, maxRank = 5, 6, 7 or 8, ul-FullPowerTransmission is configured to fullpowerMode1, and according to maxRank;

-10 bits according to Table 7.3.1.1.2-5S for 8 antenna ports, if CodebookTypeUL=codebook3, transform precoder is disabled, maxRank = 5, 6, 7, or 8, ul-FullPowerTransmission is configured to fullpowerMode1, and according to maxRank;

-3 bits according to Table 7.3.1.1.2-5T for 3 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank;

-2 bits according to Table 7.3.1.1.2-5U for 3 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank;

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, maxRank is configured to be larger than 2, and at least one SRS resource with 4 antenna ports or 8 antenna ports is configured in the SRS resource set indicated by SRS resource set indicator field if present, otherwise in an SRS resource set with usage set to 'codebook', and an SRS resource with 2 antenna ports is indicated via SRI in the same SRS resource set, then Table 7.3.1.1.2-4 is used.

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, maxRank is configured to be larger than 4, and at least one SRS resource with 8 antenna ports is configured in the SRS resource set with usage set to 'codebook', and an SRS resource with 4 antenna ports is indicated via SRI in the same SRS resource set, then Table 7.3.1.1.2-2 is used.

For the higher layer parameter txConfig = codebook, if different SRS resources with different number of antenna ports are configured, the bitwidth is determined according to the maximum number of ports in an SRS resource among the configured SRS resources in all SRS resource set(s) with usage set to 'codebook'. If the number of ports for a configured SRS resource in the set is less than the maximum number of ports in an SRS resource among the configured SRS resources, a number of most significant bits with value set to '0' are inserted to the field.

When the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel, and there are two SRS resource sets configured by srs-ResourceSetToAddModList and associated with usage of value 'codebook' or 'nonCodeBook', the Precoding information and number of layers field is associated with the SRS resource set that is associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_1.

For the higher layer parameter txConfig = codebook, when the Transform precoder indicator field is present, if the bit width of the Precoding information and number of layers field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Precoding information and number of layers field for the case with smaller bit width until the bit width of the Precoding information and number of layers field for the two cases are the same.

-Second Precoding information - number of bits determined by the following:

-0 bits if SRS resource set indicator field is not present;

-0 bits if the higher layer parameter txConfig = nonCodeBook;

-0 bits for 1 antenna port and if the higher layer parameter txConfig = codebook;

-3, 4, or 5 bits according to Table 7.3.1.1.2-2C with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN if multipanelSchemeSFN is configured, and codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-2D with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN=2 if multipanelSchemeSFN is configured, transform precoder is disabled, and according to the values of higher layer parameter codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-2E with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=3 or 4, transform precoder is disabled, and according to the values of higher layer parameter codebookSubset;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN if multipanelSchemeSFN is configured, and codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-3A with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN=1 if multipanelSchemeSFN is configured, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameter codebookSubset;

-1 or 3 bits according to Table7.3.1.1.2-4B with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN if multipanelSchemeSFN is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-4C with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, transform precoder is disabled, maxRank=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN=2 if multipanelSchemeSFN is configured, and codebookSubset=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN if multipanelSchemeSFN is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-5A with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRank=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN=1 if multipanelSchemeSFN is configured, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameter codebookSubset;

-2 bits according to Table 7.3.1.1.2-5V with the same number of layers indicated by Precoding information and number of layers field for 3 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank;

-2 bits according to Table 7.3.1.1.2-5U with the same number of layers indicated by Precoding information and number of layers field for 3 antenna ports, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank;

-4, 5, or 6 bits according to Table 7.3.1.1.2-2 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankSDM if multipanelSchemeSDM is configured, and codebookSubset;

-4 or 5 bits according to Table 7.3.1.1.2-2A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRankSDM = 2 if multipanelSchemeSDM is configured, transform precoder is disabled, and according to the values of higher layer parameter codebookSubset;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRankSDM if multipanelSchemeSDM is configured, and codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-3A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRankSDM = 1 if multipanelSchemeSDM is configured, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameter codebookSubset;

-2 or 4 bits according to Table7.3.1.1.2-4 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankSDM if multipanelSchemeSDM is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-4A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, transform precoder is disabled, maxRankSDM = 2 if multipanelSchemeSDM is configured, and codebookSubset=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and maxRankSDM= 1 if multipanelSchemeSDM is configured, and codebookSubset;

-2 bits according to Table 7.3.1.1.2-5A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission = fullpowerMode1, maxRankSDM = 1 if multipanelSchemeSDM is configured, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameter codebookSubset;

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, maxRank is configured to be larger than 2, and at least one SRS resource with 4 antenna ports is configured in the SRS resource set indicated by SRS resource set indicator field, and an SRS resource with 2 antenna ports is indicated via Second SRS resource indicator field in the same SRS resource set, then Table 7.3.1.1.2-4B is used.

For the higher layer parameter txConfig = codebook, if different SRS resources with different number of antenna ports are configured, the bitwidth is determined according to the maximum number of ports in an SRS resource among the configured SRS resources in the second SRS resource set with usage set to 'codebook' as defined in Table 7.3.1.1.2-36. If the number of ports for a configured SRS resource in the set is less than the maximum number of ports in an SRS resource among the configured SRS resources, a number of most significant bits with value set to '0' are inserted to the field.

For the higher layer parameter txConfig = codebook, when the Transform precoder indicator field is present, if the bit width of the Second Precoding information field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Second Precoding information field for the case with smaller bit width until the bit width of the Second Precoding information field for the two cases are the same.

-Antenna ports - number of bits determined by the following

-2 bits as defined by Tables 7.3.1.1.2-6, if transform precoder is enabled, dmrs-Type=1, and maxLength=1, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-2 bits as defined by Tables 7.3.1.1.2-6A, if transform precoder is enabled and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=1, where nSCID is the scrambling identity for antenna ports defined in Clause 6.4.1.1.1.2, TS 38.211 [4];

-4 bits as defined by Tables 7.3.1.1.2-7, if transform precoder is enabled, dmrs-Type=1, and maxLength=2, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-4 bits as defined by Tables 7.3.1.1.2-7A, if transform precoder is enabled and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=2, where nSCID is the scrambling identity for antenna ports defined in Clause 6.4.1.1.1.2, TS 38.211 [4];

-3 bits as defined by Tables 7.3.1.1.2-8/9/10/10A/11 according to the value of rank, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=1;

-4 bits as defined by Tables 7.3.1.1.2-12/13/14/14A/15/15A/15B/15C/15D according to the value of rank, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=2;

-4 bits as defined by Tables 7.3.1.1.2-16/17/18/18A/19/19A/19B according to the value of rank, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=1;

-5 bits as defined by Tables 7.3.1.1.2-20/21/22/22A/23/23A/23B/23C/23D according to the value of rank, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=2.

-4 bits as defined by Tables 7.3.1.1.2-38/39/40/40A/41/42/43/44/45, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=1;

-5 bits as defined by Tables 7.3.1.1.2-46/47/48/48A/49/50/51/52/53, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=2;

-5 bits as defined by Tables 7.3.1.1.2-54/55/56/56A/57/58/59/60/61, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=1;

-6 bits as defined by Tables 7.3.1.1.2-62/63/64/64A/65/66/67/68/69, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=2.

where the number of CDM groups without data of values 1, 2, and 3 in Tables 7.3.1.1.2-6 to 7.3.1.1.2-23 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively, and the value of rank is:

-the sum of the value determined according to the SRS resource indicator field and the value determined according to the second SRS resource indicator field, if txConfig = nonCodebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "10"

-the sum of the value determined according to the Precoding information and number of layers field and the value determined according to the Second Precoding information, if txConfig = codebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "10"

-determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and multipanelSchemeSDM is not configured, or if the higher layer parameter txConfig = nonCodebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "00" or “01”,

-determined according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook and multipanelSchemeSDM is not configured, or if the higher layer parameter txConfig = codebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "00" or "01".

If a UE is configured with both dmrs-UplinkForPUSCH-MappingTypeA and dmrs-UplinkForPUSCH-MappingTypeB, the bitwidth of this field equals , where  is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeA and  is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeB. A number of  zeros are padded in the MSB of this field, if the mapping type of the PUSCH corresponds to the smaller value of  and .

When the Transform precoder indicator field is present, if the bit width of the Antenna ports field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Antenna ports field for the case with smaller bit width until the bit width of the Antenna ports field for the two cases are the same.

-SRS request - 2 bits as defined by Table 7.3.1.1.2-24 for UEs not configured with supplementaryUplink in ServingCellConfig in the cell; 3 bits for UEs configured with supplementaryUplink in ServingCellConfig in the cell where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24. This bit field may also indicate the associated CSI-RS according to Clause 6.1.1.2 of [6, TS 38.214].

-SRS offset indicator - 0, 1 or 2 bits.

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214],  where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-CSI request - 0, 1, 2, 3, 4, 5, or 6 bits determined by higher layer parameter reportTriggerSize.

-CBG transmission information (CBGTI) - 0 bit if higher layer parameter codeBlockGroupTransmission for PUSCH is not configured or if the number of scheduled PUSCH indicated by the Time domain resource assignment field is larger than 1; otherwise, 2, 4, 6, or 8 bits as defined in Clause 6.1.5 of [6, TS38.214], determined by higher layer parameter maxCodeBlockGroupsPerTransportBlock and maxRank or maxMIMO-Layers for PUSCH.

-PTRS-DMRS association - number of bits determined as follows

-0 bit if PTRS-UplinkConfig is not configured in either dmrs-UplinkForPUSCH-MappingTypeA or dmrs-UplinkForPUSCH-MappingTypeB and transform precoder is disabled, or if transform precoder is enabled, or if maxRank=1 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, or if maxMIMO-Layers=1 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, or if maxRank=1 and maxRankSFN=1, or if maxMIMO-Layers=1 and maxMIMO-LayersforSFN=1, or if maxRank=1 and maxRankSDM=1 when two PTRS ports are configured by maxNrofPorts-SDM, or if maxMIMO-Layers=1 and maxMIMO-LayersforSDM=1 when two PTRS ports are configured by maxNrofPorts-SDM;

-1 or 2 or 4 bits otherwise, where Table 7.3.1.1.2-25/7.3.1.1.2-25A/7.3.1.1.2-25B/7.3.1.1.2-26/7.3.1.1.2-26A/7.3.1.1.2-26B are used to indicate the association between PTRS port(s) and DMRS port(s), and the DMRS ports are indicated by the Antenna ports field.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 2, 4, or 8 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or "01", and maxRank<=4 or maxMIMO-Layers<=4, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25 and 7.3.1.1.2-26.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 4 or 8 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRank=3 or 4 or maxMIMO-Layers=3 or 4, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25 and 7.3.1.1.2-26.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 2, 4, or 8 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRank=2 or maxMIMO-Layers=2, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, the MSB of this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or "01", maxRank<=3 or maxMIMO-Layers<=3, this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25.

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or "01", maxRank<=3 or maxMIMO-Layers<=3, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-26B.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRank=3 or maxMIMO-Layers=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRank=2 or maxMIMO-Layers=2, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, the MSB of this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port and DMRS port corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRank<=3 or maxMIMO-Layers<=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-26B.

-2 bits when two PTRS ports are configured by maxNrofPorts-SDM in PTRS-UplinkConfig, the SRS resource set indicator field is present and equals "10" and multipanelSchemeSDM is configured, the MSB of this field indicates the association between PTRS port 0 and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port 1 and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-2 bits when one PTRS port is configured by maxNrofPorts-SDM in PTRS-UplinkConfig, SRS resource set indicator field is present and equals "10" and multipanelSchemeSDM is configured, this field indicates the association between PTRS port and DMRS ports corresponding to SRS resource indicator field and Second SRS resource indicator field and/or Precoding information and number of layers field and Second Precoding information field according to Table 7.3.1.1.2-25.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig, SRS resource set indicator field is present and equals "10", multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25 and 7.3.1.1.2-26.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig, the SRS resource set indicator field is absent, maxRank>4 or maxMIMO-Layers>4, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port and DMRS port(s) corresponding to the selected codeword according to Table 7.3.1.1.2-25B, where the selected codeword is the codeword with higher MCS for the initial PUSCH if the MCS indices of the two codewords are different for the initial PUSCH, or codeword 0 otherwise.

-4 bits when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig, the SRS resource set indicator field is absent, maxRank>4 or maxMIMO-Layers>4, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Table 7.3.1.1.2-26A.

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and the "PTRS-DMRS association" field is present for the indicated bandwidth part but not present for the active bandwidth part, the UE assumes the "PTRS-DMRS association" field is not present for the indicated bandwidth part.

When the Transform precoder indicator field is present, if the bit width of PTRS-DMRS association field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the PTRS-DMRS association field for the case with smaller bit width until the bit width of the PTRS-DMRS association field for the two cases are the same.

-Second PTRS-DMRS association

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 4 or 8 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRank>2 or maxMIMO-Layers>2, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRank=3 or maxMIMO-Layers=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRank<=3 or maxMIMO-Layers<=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-0 bit otherwise.

Tables 7.3.1.1.2-25 and 7.3.1.1.2-26/7.3.1.1.2-26B are used to indicate the association between PTRS port(s) and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second precoding information field when one PT-RS port and two PT-RS ports are configured by maxNrofPorts in PTRS-UplinkConfig respectively, and the DMRS ports are indicated by the Antenna ports field.

-beta_offset indicator - 0 if the higher layer parameter betaOffsets = semiStatic; otherwise 2 bits as defined by Table 9.3-3 in [5, TS 38.213].

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookList or by pdsch-HARQ-ACK-CodebookListMulticast for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-1 is configured, if the bit width of the beta_offset indicator in DCI format 0_1 for one HARQ-ACK codebook is not equal to that of the beta_offset indicator in DCI format 0_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller beta_offset indicator until the bit width of the beta_offset indicator in DCI format 0_1 for the two HARQ-ACK codebooks are the same.

-DMRS sequence initialization – 0 bit if transform precoder is enabled by higher layers and the Transform precoder indicator field is not present; 1 bit if transform precoder is disabled by higher layers or if the Transform precoder indicator field is present. If the Transform precoder indicator field is present and set to '0', the bit is reserved.

-UL-SCH indicator - 0 or 1 bit as follows

-0 bit if the number of scheduled PUSCH indicated by the Time domain resource assignment field is larger than 1;

-1 bit otherwise. A value of "1" indicates UL-SCH shall be transmitted on the PUSCH and a value of "0" indicates UL-SCH shall not be transmitted on the PUSCH. If a UE does not support triggering SRS only in DCI, except for DCI format 0_1 with CRC scrambled by SP-CSI-RNTI, the UE is not expected to receive a DCI format 0_1 with UL-SCH indicator of "0" and CSI request of all zero(s). If a UE supports triggering SRS only in DCI, except for DCI format 0_1 with CRC scrambled by SP-CSI-RNTI, the UE is not expected to receive a DCI format 0_1 with UL-SCH indicator of "0", CSI request of all zero(s) and SRS request of all zero(s). The UE is not expected to receive a DCI format 0_1 with UL-SCH indicator of "0", when the indicated number of layers is larger than 4.

-ChannelAccess-CPext-CAPC - 0, 1, 2, 3, 4, 5 or 6 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-0-1 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.1.2-35 or Table 7.3.1.1.2-35A are configured by the higher layer parameter ul-AccessConfigListDCI-0-1.log2(I)

-Open-loop power control parameter set indication - 0 or 1 or 2 bits.

-0 bit if the higher layer parameter p0-PUSCH-SetList is not configured;

-1 or 2 bits otherwise,

-1 bit if SRS resource indicator is present in the DCI format 0_1;

-1 or 2 bits as determined by higher layer parameter olpc-ParameterSetDCI-0-1 if SRS resource indicator is not present in the DCI format 0_1.

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-0-1 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-Invalid symbol pattern indicator - 0 bit if higher layer parameter invalidSymbolPatternIndicatorDCI-0-1 is not configured; otherwise 1 bit as defined in Clause 6.1.2.1 in [6, TS 38.214].

-Minimum applicable scheduling offset indicator - 0 or 1 bit

-0 bit if higher layer parameter minimumSchedulingOffsetK2 is not configured;

-1 bit if higher layer parameter minimumSchedulingOffsetK2 is configured. The 1 bit indication is used to determine the minimum applicable K2 for the active UL BWP and the minimum applicable K0 value for the active DL BWP, if configured respectively, according to Table 7.3.1.1.2-33. If the minimum applicable K0 is indicated, the minimum applicable value of the aperiodic CSI-RS triggering offset for an active DL BWP shall be the same as the minimum applicable K0 value.

-SCell dormancy indication - 0 bit if higher layer parameter dormancyGroupWithinActiveTime is not configured; otherwise 1, 2, 3, 4 or 5 bits bitmap determined according to the number of different DormancyGroupID(s) provided by higher layer parameter dormancyGroupWithinActiveTime, where each bit corresponds to one of the SCell group(s) configured by higher layers parameter dormancyGroupWithinActiveTime, with MSB to LSB of the bitmap corresponding to the first to last configured SCell group in ascending order of DormancyGroupID. The field is only present when this format is carried by PDCCH on the primary cell within DRX Active Time and the UE is configured with at least two DL BWPs for an SCell.

-Sidelink assignment index - 0, 1 or 2 bits:

-1 bit if the UE is configured with pdsch-HARQ-ACK-Codebook = semi-static and, in addition,  the UE is configured with a SL configured grant type 1 or to monitor DCI format 3_0 with CRC scrambled by SL-RNTI or SL-CS-RNTI;

-2 bits if the UE is configured with pdsch-HARQ-ACK-Codebook = dynamic and, in addition, the UE is configured with a SL configured grant type 1 or to monitor DCI format 3_0 with CRC scrambled by SL-RNTI or SL-CS-RNTI;

-0 bit otherwise.

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-0 bit, otherwise

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-0-1 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

A UE does not expect that the bit width of a field in DCI format 0_1 with CRC scrambled by CS-RNTI is larger than corresponding bit width of same field in DCI format 0_1 with CRC scrambled by C-RNTI for the same serving cell. If the bit width of a field in the DCI format 0_1 with CRC scrambled by CS-RNTI is not equal to that of the corresponding field in the DCI format 0_1 with CRC scrambled by C-RNTI for the same serving cell, a number of most significant bits with value set to '0' are inserted to the field in DCI format 0_1 with CRC scrambled by CS-RNTI until the bit width equals that of the corresponding field in the DCI format 0_1 with CRC scrambled by C-RNTI for the same serving cell.

If the number of information bits in DCI format 0_1 scheduling a single PUSCH prior to padding is not equal to the number of information bits in DCI format 0_1 scheduling multiple PUSCHs for the same serving cell, zeros shall be appended to the DCI format 0_1 with smaller size until the payload size is the same for scheduling a single PUSCH and multiple PUSCHs.

For a UE configured with scheduling on the primary cell from an SCell, if prior to padding the number of information bits in DCI format 0_1 carried by PDCCH on the primary cell is not equal to the number of information bits in DCI format 0_1 carried by PDCCH on the SCell for scheduling on the primary cell, zeros shall be appended to the DCI format 0_1 with smaller size until the payload size is the same.

-If application of step 4C in clause 7.3.1.0 results in additional zero padding for DCI format 0_1 for scheduling on the primary cell, corresponding zeros shall be appended to both DCI format 0_1 monitored on the primary cell and DCI format 0_1 monitored on the SCell for scheduling on the primary cell.

-If the SCell is deactivated and firstActiveDownlinkBWP-Id is not set to dormant BWP, the UE determines the number of information bits in DCI format 0_1 carried by PDCCH on the primary cell based on a DL BWP provided by firstActiveDownlinkBWP-Id for the SCell. If the active DL BWP of the SCell is a dormant DL BWP, or if the SCell is deactivated and firstActiveDownlinkBWP-Id is set to dormant BWP, the UE determines the number of information bits in DCI format 0_1 carried by PDCCH on the primary cell based on a DL BWP provided by firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a DL BWP provided by firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.1.2-1: Bandwidth part indicator

Table 7.3.1.1.2-2: Precoding information and number of layers or Second Precoding information, for 4 antenna ports, if transform precoder is disabled, maxRank = 2 or 3 or 4 or max{maxRank, maxRankSFN} = 2 or 3 or 4 or max{maxRank, maxRankSDM} = 2 or 3 or 4 or maxRankSDM= 2, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-2A: Precoding information and number of layers for 4 antenna ports or Second Precoding information,, if transform precoder is disabled, maxRank = 2 or max{maxRank, maxRankSFN} = 2 or max{maxRank, maxRankSDM} = 2 or maxRankSDM= 2, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-2B: Precoding information and number of layers for 4 antenna ports, if transform precoder is disabled, maxRank = 3 or 4, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-2C: Second precoding information, for 4 antenna ports, if transform precoder is disabled, maxRank = 2 or 3 or 4 or maxRankSFN = 2, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-2D: Second precoding information for 4 antenna ports, if transform precoder is disabled, maxRank = 2 or maxRankSFN = 2, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-2E: Second precoding information for 4 antenna ports, if transform precoder is disabled, maxRank = 3 or 4, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-3: Precoding information and number of layers or Second Precoding information, for 4 antenna ports, if transform precoder is enabled and ul-FullPowerTransmission is either not configured or configured to fullpowerMode2 or configured to fullpower, or if transform precoder is disabled, maxRank = 1 or max{maxRank, maxRankSFN} = 1 or max{maxRank, maxRankSDM} = 1 or maxRankSDM= 1 or maxRankSFN= 1, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-3A: Precoding information and number of layers or Second Precoding information, for 4 antenna ports, if transform precoder is enabled and ul-FullPowerTransmission = fullpowerMode1, or if transform precoder is disabled, maxRank = 1 or max{maxRank, maxRankSFN} = 1 or max{maxRank, maxRankSDM} = 1 or maxRankSDM= 1 or maxRankSFN= 1, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-4: Precoding information and number of layers or Second Precoding information, for 2 antenna ports, if transform precoder is disabled, maxRank = 2 or max{maxRank, maxRankSFN} = 2 or max{maxRank, maxRankSDM} = 2 or maxRankSDM= 2, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-4A: Precoding information and number of layers or Second Precoding information, for 2 antenna ports, if transform precoder is disabled, maxRank = 2 or max{maxRank, maxRankSFN} = 2 or max{maxRank, maxRankSDM} = 2 or maxRankSDM= 2, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-4B: Second precoding information, for 2 antenna ports, if transform precoder is disabled, maxRank = 2 or maxRankSFN = 2, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-4C: Second precoding information, for 2 antenna ports, if transform precoder is disabled, maxRank = 2 or maxRankSFN = 2, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-5: Precoding information and number of layers or Second Precoding information, for 2 antenna ports, if transform precoder is enabled and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, or if transform precoder is disabled, maxRank = 1 or max{maxRank, maxRankSFN} = 1 or max{maxRank, maxRankSDM} = 1 or maxRankSDM= 1 or maxRankSFN= 1, and and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-5A: Precoding information and number of layers or Second Precoding information, for 2 antenna ports or Second Precoding information, if transform precoder is enabled and ul-FullPowerTransmission = fullpowerMode1, or if transform precoder is disabled, maxRank = 1 or max{maxRank, maxRankSFN} = 1 or max{maxRank, maxRankSDM} = 1 or maxRankSDM= 1 or maxRankSFN= 1, and ul-FullPowerTransmission = fullpowerMode1

Table 7.3.1.1.2-5B: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 8, and CodebookTypeUL=codebook1

Table 7.3.1.1.2-5C: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 7, and CodebookTypeUL=codebook1

Table 7.3.1.1.2-5D: Precoding information and number of layers, for 8 antenna ports,if transform precoder is disabled, maxRank = 4, 5 or 6, CodebookTypeUL=codebook1

Table 7.3.1.1.2-5E: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled or maxRank=1 or 2 or 3 if transform precoder is disabled, CodebookTypeUL=codebook1

Table 7.3.1.1.2-5F: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7 or 8, and CodebookTypeUL=codebook4

Table 7.3.1.1.2-5G: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 2, 3 or 4, CodebookTypeUL=codebook4, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-5H: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled or maxRank=1 if transform is disabled, CodebookTypeUL=codebook4, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-5I: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7 or 8, and CodebookTypeUL=codebook2

Table 7.3.1.1.2-5J: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled, or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, CodebookTypeUL=codebook2, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-5K: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7 or 8, and CodebookTypeUL=codebook3

Table 7.3.1.1.2-5L: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled, or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, CodebookTypeUL=codebook3, and ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower

Table 7.3.1.1.2-5M: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 2, 3 or 4, CodebookTypeUL=codebook4, and ul-FullPowerTransmission configured to fullpowerMode1

Table 7.3.1.1.2-5N: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled or maxRank=1 if transform is disabled, CodebookTypeUL=codebook4, and ul-FullPowerTransmission configured to fullpowerMode1

Table 7.3.1.1.2-5O: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled, or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, CodebookTypeUL=codebook2, and ul-FullPowerTransmission configured to fullpowerMode1

Table 7.3.1.1.2-5P: Precoding information and number of layers, for 8 antenna ports, if transform precoder is enabled, or maxRank = 1, 2, 3 or 4 if transform precoder is disabled, CodebookTypeUL=codebook3, and ul-FullPowerTransmission is configured to fullpowerMode1

Table 7.3.1.1.2-5Q: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7, 8, CodebookTypeUL=codebook4, and ul-FullPowerTransmission is configured to fullpowerMode1

Table 7.3.1.1.2-5R: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7, 8, CodebookTypeUL=codebook2, and ul-FullPowerTransmission is configured to fullpowerMode1

Table 7.3.1.1.2-5S: Precoding information and number of layers, for 8 antenna ports, if transform precoder is disabled, maxRank = 5, 6, 7, 8, CodebookTypeUL=codebook3, and ul-FullPowerTransmission is configured to fullpowerMode1

Table 7.3.1.1.2-5T: Precoding information and number of layers, for 3 antenna ports, if transform precoder is disabled, maxRank = 2 or 3, and ul-FullPowerTransmission is not configured or configured to fullpower

Table 7.3.1.1.2-5U: Precoding information and number of layers or Second Precoding information, for 3 antenna ports, if transform precoder is enabled and ul-FullPowerTransmission is not configured or configured to fullpower, or if transform precoder is disabled, maxRank = 1, and ul-FullPowerTransmission is not configured or configured to fullpower

Table 7.3.1.1.2-5V: Second precoding information, for 3 antenna ports, if transform precoder is disabled, maxRank = 2 or 3, and ul-FullPowerTransmission is not configured or configured to fullpower

Table 7.3.1.1.2-6: Antenna port(s), transform precoder is enabled, dmrs-Type=1, maxLength=1,except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured andπ/2-BPSK modulation is used

Table 7.3.1.1.2-6A: Antenna port(s), transform precoder is enabled, dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2-BPSK modulation is used, dmrs-Type=1, maxLength=1

Table 7.3.1.1.2-7: Antenna port(s), transform precoder is enabled, dmrs-Type=1, maxLength=2,except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured andπ/2-BPSK modulation is used

Table 7.3.1.1.2-7A: Antenna port(s), transform precoder is enabled, dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2-BPSK modulation is used, dmrs-Type=1, maxLength=2

Table 7.3.1.1.2-8: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=1, rank = 1

Table 7.3.1.1.2-9: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=1, rank = 2

Table 7.3.1.1.2-10: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is notconfigured, dmrs-Type=1, dmrs-TypeEnh is not configured,maxLength=1, rank = 3

Table 7.3.1.1.2-10A: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is configured, dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=1, rank = 3

Table 7.3.1.1.2-11: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=1, rank = 4

Table 7.3.1.1.2-12: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 1

Table 7.3.1.1.2-13: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 2

Table 7.3.1.1.2-14: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is not configured, dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=2, rank = 3

Table 7.3.1.1.2-14A: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is configured, dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=2, rank = 3

Table 7.3.1.1.2-15: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 4

Table 7.3.1.1.2-15A: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 5

Table 7.3.1.1.2-15B Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 6

Table 7.3.1.1.2-15C: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 7

Table 7.3.1.1.2-15D: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is not configured, maxLength=2, rank = 8

Table 7.3.1.1.2-16: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=1, rank=1

Table 7.3.1.1.2-17: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=1, rank=2

Table 7.3.1.1.2-18: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is notconfigured, dmrs-Type=2, dmrs-TypeEnh is not configured,maxLength=1, rank =3

Table 7.3.1.1.2-18A: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is configured, dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=1, rank =3

Table 7.3.1.1.2-19: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=1, rank =4

Table 7.3.1.1.2-19A: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=1, rank = 5

Table 7.3.1.1.2-19B: Antenna port(s), transform precoder is disabled, dmrs-Type=2,enhanced-dmrs-Typedmrs-TypeEnh is not configured, maxLength=1, rank = 6

Table 7.3.1.1.2-20: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank=1

Table 7.3.1.1.2-21: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank=2

Table 7.3.1.1.2-22: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is notconfigured, dmrs-Type=2, dmrs-TypeEnh is not configured,maxLength=2, rank=3

Table 7.3.1.1.2-22A: Antenna port(s), transform precoder is disabled, multipanelSchemeSDM is configured, dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=2, rank=3

Table 7.3.1.1.2-23: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank=4

Table 7.3.1.1.2-23A: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank = 5

Table 7.3.1.1.2-23B Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank = 6

Table 7.3.1.1.2-23C: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank = 7

Table 7.3.1.1.2-23D: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is not configured, maxLength=2, rank = 8

Table 7.3.1.1.2-24: SRS request

Table 7.3.1.1.2-25: PTRS-DMRS association or Second PTRS-DMRS association for UL PTRS port 0

Table 7.3.1.1.2-25A: PTRS-DMRS association for UL PTRS port 0 or for the actual UL PT-RS port if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, or PTRS-DMRS association for UL PTRS port 0 and 1 if multipanelSchemeSDM is configured and maxNrofPorts-SDM is set to 2

Table 7.3.1.1.2-25B: PTRS-DMRS association for UL PTRS port 0, maxRank>4 or maxMIMO-Layers>4

Table 7.3.1.1.2-26: PTRS-DMRS association or Second PTRS-DMRS association for UL PTRS ports 0 and 1

Table 7.3.1.1.2-26A: PTRS-DMRS association for UL PTRS ports 0 and 1, maxRank>4 or maxMIMO-Layers>4

Table 7.3.1.1.2-26B: PTRS-DMRS association or Second PTRS-DMRS association for the actual UL PTRS port

Table 7.3.1.1.2-27: void

Table 7.3.1.1.2-28: SRI indication or Second SRI indication, for non-codebook based PUSCH transmission,

Table 7.3.1.1.2-28A: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=1

Table 7.3.1.1.2-29: SRI indication or Second SRI indication, fornon-codebook based PUSCH transmission,

Table 7.3.1.1.2-29A: Second SRI indication for non-codebook based PUSCH transmission, Lmax=2

Table 7.3.1.1.2-29B: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=2

Table 7.3.1.1.2-29B-1: SRI(s) for 2 layers, NSRS>4

Table 7.3.1.1.2-30: SRI indication for non-codebook based PUSCH transmission,

Table 7.3.1.1.2-30A: Second SRI indication for non-codebook based PUSCH transmission, if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, Lmax=3

Table 7.3.1.1.2-30B: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=3

Table 7.3.1.1.2-30B-1: SRI combinations for 3 layers, NSRS>4

Table 7.3.1.1.2-31: SRI indication for non-codebook based PUSCH transmission,

Table 7.3.1.1.2-31A: Second SRI indication for non-codebook based PUSCH transmission,if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, Lmax=4

Table 7.3.1.1.2-31B: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=4

Table 7.3.1.1.2-31B-1: SRI combinations for 4 layers, NSRS>4

Table 7.3.1.1.2-31C: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=5

Table 7.3.1.1.2-31C-1: SRI combinations for 5 layers, NSRS>4

Table 7.3.1.1.2-31D: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=6

Table 7.3.1.1.2-31D-1: SRI combinations for 6 layers, NSRS>6

Table 7.3.1.1.2-31E: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=7

Table 7.3.1.1.2-31F: SRI indication, for non-codebook based PUSCH transmission, , NSRS>4Lmax=8

Table 7.3.1.1.2-32: SRI indication or Second SRI indication, for codebook based PUSCH transmission, if ul-FullPowerTransmission is not configured, or ul-FullPowerTransmission = fullpowerMode1, or ul-FullPowerTransmission = fullpowerMode2, or ul-FullPowerTransmission = fullpower and NSRS=2

Table 7.3.1.1.2-32A: SRI indication or Second SRI indication, for codebook based PUSCH transmission, if ul-FullPowerTransmission = fullpowerMode2 and NSRS=3

Table 7.3.1.1.2-32B: SRI indication or Second SRI indication, for codebook based PUSCH transmission, if ul-FullPowerTransmission = fullpowerMode2 and NSRS=4

Table 7.3.1.1.2-33: Joint indication of minimum applicable scheduling offset K0/K2

Table 7.3.1.1.2-34: Redundancy version

Table 7.3.1.1.2-35: Allowed entries for DCI format 0_1/0_3 and DCI format 0_2, configured byhigher layer parameter ul-AccessConfigListDCI-0-1 and ul-AccessConfigListDCI-0-2, respectively,in frequency range 1

Table 7.3.1.1.2-35A: Allowed entries for DCI format 0_1, DCI format 0_2 and DCI format 0_3, configured by higher layer parameter ul-AccessConfigListDCI-0-1 in frequency range 2-2

Table 7.3.1.1.2-36: SRS resource set indication

Table 7.3.1.1.2-37: SRS offset indicator

Table 7.3.1.1.2-38: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 1

Table 7.3.1.1.2-39: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 2

Table 7.3.1.1.2-40: Antenna port(s), transform precoder is disabled, dmrs-Type=1, multipanelSchemeSDM is not configured, dmrs-TypeEnh is configured, maxLength=1, rank = 3

Table 7.3.1.1.2-40A: Antenna port(s), transform precoder is disabled, dmrs-Type=1, multipanelSchemeSDM is configured, dmrs-TypeEnh is configured, maxLength=1, rank = 3

Table 7.3.1.1.2-41: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 4

Table 7.3.1.1.2-42: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 5

Table 7.3.1.1.2-43: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 6

Table 7.3.1.1.2-44: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 7

Table 7.3.1.1.2-45: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1, rank = 8

Table 7.3.1.1.2-46: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 1

Table 7.3.1.1.2-47: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 2

Table 7.3.1.1.2-48: Antenna port(s), transform precoder is disabled, dmrs-Type=1, multipanelSchemeSDM is not configured, dmrs-TypeEnh is configured, maxLength=2, rank = 3

Table 7.3.1.1.2-48A: Antenna port(s), transform precoder is disabled, dmrs-Type=1, multipanelSchemeSDM is configured, dmrs-TypeEnh is configured, maxLength=2, rank = 3

Table 7.3.1.1.2-49: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 4

Table 7.3.1.1.2-50: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 5

Table 7.3.1.1.2-51: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 6

Table 7.3.1.1.2-52: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 7

Table 7.3.1.1.2-53: Antenna port(s), transform precoder is disabled, dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2, rank = 8

Table 7.3.1.1.2-54: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 1

Table 7.3.1.1.2-55: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 2

Table 7.3.1.1.2-56: Antenna port(s), transform precoder is disabled, dmrs-Type=2, multipanelSchemeSDM is not configured, dmrs-TypeEnh is configured, maxLength=1, rank = 3

Table 7.3.1.1.2-56A: Antenna port(s), transform precoder is disabled, dmrs-Type=2, multipanelSchemeSDM is configured, dmrs-TypeEnh is configured, maxLength=1, rank = 3

Table 7.3.1.1.2-57: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 4

Table 7.3.1.1.2-58: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 5

Table 7.3.1.1.2-59: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 6

Table 7.3.1.1.2-60: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 7

Table 7.3.1.1.2-61: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1, rank = 8

Table 7.3.1.1.2-62: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 1

Table 7.3.1.1.2-63: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 2

Table 7.3.1.1.2-64: Antenna port(s), transform precoder is disabled, dmrs-Type=2, multipanelSchemeSDM is not configured, dmrs-TypeEnh is configured, maxLength=2, rank = 3

Table 7.3.1.1.2-64A: Antenna port(s), transform precoder is disabled, dmrs-Type=2, multipanelSchemeSDM is configured, dmrs-TypeEnh is configured, maxLength=2, rank = 3

Table 7.3.1.1.2-65: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 4

Table 7.3.1.1.2-66: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 5

Table 7.3.1.1.2-67: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 6

Table 7.3.1.1.2-68: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 7

Table 7.3.1.1.2-69: Antenna port(s), transform precoder is disabled, dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2, rank = 8

## 7.3.1.1.3Format 0_2

DCI format 0_2 is used for the scheduling of PUSCH in one cell.

The following information is transmitted by means of the DCI format 0_2 with CRC scrambled by C-RNTI or CS-RNTI or SP-CSI-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 0, indicating an UL DCI format

-Carrier indicator - 0, 1, 2 or 3 bits determined by higher layer parameter carrierIndicatorSizeDCI-0-2, as defined in Clause 10.1 of [5, TS38.213]. This field is reserved when this format is carried by PDCCH on the primary cell and the UE is configured for scheduling on the primary cell from an SCell, with the same number of bits as that in this format carried by PDCCH on the SCell for scheduling on the primary cell.

-UL/SUL indicator - 0 bit for UEs not configured with supplementaryUplink in ServingCellConfig in the cell or UEs configured with supplementaryUplink in ServingCellConfig in the cell but only one carrier in the cell is configured for PUSCH transmission; otherwise, 1 bit as defined in Table 7.3.1.1.1-1.

-Bandwidth part indicator - 0, 1 or 2 bits as determined by the number of UL BWPs  configured by higher layers, excluding the initial UL bandwidth part. The bitwidth for this field is determined as bits, where nBWP, RRClog2(nBWP)

-if , in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;nBWP=nBWP, RRC+1 nBWP, RRC≤3

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;nBWP=nBWP, RRC

If a UE does not support active BWP change via DCI, the UE ignores this bit field.

-Frequency domain resource assignment - number of bits determined by the following:

- bits if only resource allocation type 0 is configured, where  is defined in Clause 6.1.2.2.1 of [6, TS 38.214]NRBGNRBG

- bits if only resource allocation type 1 is configured, or  bits if resourceAllocationDCI-0-2-r16 is configured as 'dynamicSwitch', where   is the size of the active UL bandwidth part,  is defined as in clause 4.4.4.4 of [4, TS 38.211] and  is given by higher layer parameter resourceAllocationType1GranularityDCI-0-2. If the higher layer parameter resourceAllocationType1GranularityDCI-0-2 is not configured,  is equal to 1.log2NRBG, K1NRBG, K1+1/2max log2NRBG, K1NRBG, K1+1/2, NRBG+1NRBG, K1=NRBUL, BWP+NUL, BWPstartmodK1/K1,NRBUL, BWPNUL, BWPstartK1K1

-If resourceAllocationDCI-0-2-r16 is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 6.1.2.2.1 of [6, TS 38.214].NRBG

-For resource allocation type 1, the  LSBs provide the resource allocation as follows:log2NRBG, K1NRBG, K1+1/2

-For PUSCH hopping with resource allocation type 1:

-MSB bits are used to indicate the frequency offset according to Clause 6.3 of [6, TS 38.214], where  if the higher layer parameter frequencyHoppingOffsetListsDCI-0-2 contains two offset values and if the higher layer parameter frequencyHoppingOffsetListsDCI-0-2 contains four offset valuesNUL_hop NUL_hop=1NUL_hop=2

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]log2NRBG, K1NRBG, K1+1/2-NUL_hop

-For non-PUSCH hopping with resource allocation type 1:

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]log2NRBG, K1NRBG, K1+1/2

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocationDCI-0-2-r16 is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

-Time domain resource assignment - 0, 1, 2, 3, 4, 5 or 6 bits as defined in Clause 6.1.2.1 of [6, TS38.214]. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter pusch-TimeDomainAllocationListDCI-0-2 if the higher layer parameter is configured, or I is the number of entries in the higher layer parameter PUSCH-TimeDomainResourceAllocationList if the higher layer parameter PUSCH-TimeDomainResourceAllocationList is configured and the higher layer parameter pusch-TimeDomainAllocationListDCI-0-2 is not configured; otherwise I is the number of entries in the default table.log2(I)

-Frequency hopping flag - 0 or 1 bit:

-0 bit if the higher layer parameter frequencyHoppingDCI-0-2 is not configured;

-1 bit according to Table 7.3.1.1.1-3 otherwise, only applicable to resource allocation type 1, as defined in Clause 6.3 of [6, TS 38.214].

-Modulation and coding scheme -5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-0-2

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-Transform precoder indicator - 0 or 1 bit

-1 bit if the higher layer parameter dynamicTransformPrecoderFieldPresenceDCI-0-2 is configured to 'enabled' and if the UE is configured to monitor DCI format 0_2 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI, where the bit value of 0 indicates that transform precoder is enabled and the bit value of 1 indicates that transform precoder is disabled. For a DCI format 0_2 with CRC scrambled by CS-RNTI and the value indicated by new data indicator field is 0, or for a DCI format 0_2 with CRC scrambled by SP-CSI-RNTI, the bit is reserved.

-0 bit otherwise.

-HARQ process number - number of bits determined by the following:

-5 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-0-2-v1700 if configured;

-0, 1, 2, 3, 4 or 5 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-0-2-Ext if configured;

-otherwise 0, 1, 2, 3 or 4 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-0-2.

-Downlink assignment index - 0, 1, 2 or 4 bits

-0 bit if the higher layer parameter downlinkAssignmentIndexDCI-0-2 is not configured;

-1, 2, 3, 4, 5 or 6 bits otherwise,

-1st downlink assignment index - 1 or 2 bits:

-1 bit for semi-static HARQ-ACK codebook for unicast and multicast if pdsch-HARQ-ACK-Codebook = semiStatic is configured for both unicast and multicast and the higher layer parameter fdmed-ReceptionMulticast is not configured; otherwise for semi-static HARQ-ACK codebook for unicast;

-2 bits for dynamic HARQ-ACK codebook for unicast.

-2nd downlink assignment index - 0 or 2 bits

-2 bits for dynamic HARQ-ACK codebook with two HARQ-ACK sub-codebooks for unicast;

-0 bit otherwise.

-3rd downlink assignment index - 0, 1 or 2 bits

-1 bit for semi-static HARQ-ACK codebook for multicast if the higher layer parameter fdmed-ReceptionMulticast is configured;

-2 bits for the dynamic HARQ-ACK codebook for multicast;

-0 bit otherwise.

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookList for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-2 is configured, if the bit width of the 1st or 2 nd Downlink assignment index in DCI format 0_2 for one HARQ-ACK codebook is not equal to that of the 1st or 2 nd Downlink assignment index in DCI format 0_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 1st or 2 nd Downlink assignment index until the bit width of the 1st or 2 nd Downlink assignment index in DCI format 0_2 for the two HARQ-ACK codebooks are the same.

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookListMulticast for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-2 is configured, if the bit width of the 3rd downlink assignment index in DCI format 0_2 for one HARQ-ACK codebook is not equal to that of the 3rd downlink assignment index in DCI format 0_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 3rd downlink assignment index until the bit width of the 3rd downlink assignment index in DCI format 0_2 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS38.213]

-Second TPC command for scheduled PUSCH - 2 bits as defined in Clause 7.1.1 of [5, TS38.213] if higher layer parameter SecondTPCFieldDCI-0-2 is configured; 0 bit otherwise.

-SRS resource set indicator - 0 or 2 bits

-2 bits according to Table 7.3.1.1.2-36 if

-txConfig = nonCodeBook, and there are two SRS resource sets configured by srs-ResourceSetToAddModListDCI-0-2 and associated with the usage of value 'nonCodeBook', and is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided, or

-txConfig=codebook, and there are two SRS resource sets configured by srs-ResourceSetToAddModListDCI-0-2 and associated with usage of value 'codebook', and is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided;

-0 bit otherwise.

-SRS resource indicator - number of bits determined by the following:'

- bits according to Tables 7.3.1.1.2-28/28A/29/29B/30/30B/31/31B if the higher layer parameter txConfig = nonCodebook, where log2k=1minLmax, NSRS,0_2NSRS,0_2k

- is the number of configured SRS resources in the SRS resource set indicated by SRS resource set indicator field if present, NSRS, 0_2

- is the number of configured SRS resources in the SRS resource set associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_2, if the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel,NSRS

-otherwise  is the number of configured SRS resources in the SRS resource set configured by higher layer parameter srs-ResourceSetToAddModListDCI-0-2 and associated with the higher layer parameter usage of value 'nonCodeBook', where the SRS resource set is composed of the first  SRS resources together with other configurations in the SRS resource set, or in the SRS resource set with lower srs-ResourceSetId of two SRS resources sets, configured by higher layer parameter srs-ResourceSetToAddModList, if any, and associated with the higher layer parameter usage of value 'nonCodeBook', except for the higher layer parameters 'srs-ResourceSetId' and 'srs-ResourceIdList', NSRS, 0_2NSRS, 0_2

and

-if UE supports operation with maxMIMO-LayersDCI-0-2 and the higher layer parameter maxMIMO-LayersDCI-0-2 of PUSCH-ServingCellConfig of the serving cell is configured,

-Lmax is given by max{maxMIMO-LayersDCI-0-2, maxMIMO-LayersforSDM-DCI-0-2} if maxMIMO-LayersforSDM-DCI-0-2 is configured

-Lmax is given by max{maxMIMO-LayersDCI-0-2, maxMIMO-LayersforSFN-DCI-0-2} if maxMIMO-LayersforSFN-DCI-0-2 is configured

-Lmax is given by maxMIMO-LayersDCI-0-2 otherwise

-otherwise, Lmax is given by the maximum number of layers for PUSCH supported by the UE for the serving cell for non-codebook based operation.

- bits according to Tables 7.3.1.1.2-32/32A/32B if the higher layer parameter txConfig = codebook, where log2NSRS, 0_2

- is the number of configured SRS resources in the SRS resource set indicated by SRS resource set indicator field if present, NSRS, 0_2

- is the number of configured SRS resources in the SRS resource set associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_2, if the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel,NSRS

-otherwise  is the number of configured SRS resources in the SRS resource set configured by higher layer parameter srs-ResourceSetToAddModListDCI-0-2 and associated with the higher layer parameter usage of value 'codeBook', where the SRS resource set is composed of the first  SRS resources together with other configurations in the SRS resource set configured by higher layer parameter srs-ResourceSetToAddModList, if any, and associated with the higher layer parameter usage of value 'codeBook', except for the higher layer parameters 'srs-ResourceSetId' and 'srs-ResourceIdList'.NSRS, 0_2NSRS, 0_2

When the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel, and there are two SRS resource sets configured by srs-ResourceSetToAddModListDCI-0-2 and associated with usage of value 'codebook' or 'nonCodeBook', the first SRS resource set is associated with coresetPoolIndex value 0 and the second SRS resource set is associated with coresetPoolIndex value 1, where the first and the second SRS resource sets are respectively the ones with lower and higher srs-ResourceSetId of the two SRS resources sets, and the first and second SRS resource sets are composed of the first  SRS resources together with other configurations in the first and second SRS resource sets configured by higher layer parameter srs-ResourceSetToAddModList, if any, and associated with the higher layer parameter usage of value 'codebook' or 'nonCodeBook', respectively, except for the higher layer parameters 'srs-ResourceSetId' and 'srs-ResourceIdList'.NSRS, 0_2

-Second SRS resource indicator - number of bits determined by the following:

- bits according to Tables 7.3.1.1.2-28/29A/30A/31A with the same number of layers indicated by SRS resource indicator field if the higher layer parameter txConfig = nonCodebook, the higher layer parameter maxMIMO-LayersforSDM-DCI-0-2 is not configured, and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set, andlog2(maxk∈{1,2,…,min⁡{Lmax,NSRS,0_2}}NSRS,0_2k) NSRS, 0_2

-if UE supports operation with maxMIMO-LayersDCI-0-2 and the higher layer parameter maxMIMO-LayersDCI-0-2 of PUSCH-ServingCellConfig of the serving cell is configured,

-Lmax is given by maxMIMO-LayersforSFN-DCI-0-2 if maxMIMO-LayersforSFN-DCI-0-2 is configured

-Lmax is given by maxMIMO-LayersDCI-0-2 otherwise

-otherwise, Lmax is given by the maximum number of layers for PUSCH supported by the UE for the serving cell for non-codebook based operation.

- bits according to Tables 7.3.1.1.2-28/29 if the higher layer parameter txConfig = nonCodebook, the higher layer parameter maxMIMO-LayersforSDM-DCI-0-2 is configured and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set, where the second SRS resource set is composed of the first  SRS resources together with other configurations in the SRS resource set, or in the SRS resource set with higher srs-ResourceSetId of two SRS resources sets, configured by higher layer parameter srs-ResourceSetToAddModList, if any, and associated with the higher layer parameter usage of value 'nonCodeBook', except for the higher layer parameters 'srs-ResourceSetId' and 'srs-ResourceIdList', and Lmax is given by maxMIMO-LayersforSDM-DCI-0-2.log2k=1minLmax, NSRS,0_2NSRS,0_2kNSRS, 0_2NSRS, 0_2

- bits according to Tables 7.3.1.1.2-32/32A/32B if the higher layer parameter txConfig = codebook and SRS resource set indicator field is present, where  is the number of configured SRS resources in the second SRS resource set.log2NSRS, 0_2 NSRS, 0_2

-0 bit otherwise.

-Precoding information and number of layers - number of bits determined by the following:

-0 bits if the higher layer parameter txConfig = nonCodeBook;

-0 bits for 1 antenna port and if the higher layer parameter txConfig = codebook;

-4, 5, or 6 bits according to Table 7.3.1.1.2-2 for 4 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} if multipanelSchemeSDM is configured, and codebookSubsetDCI-0-2;

-4 or 5 bits according to Table 7.3.1.1.2-2A for 4 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, the values of higher layer parameters maxRankDCI-0-2=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} = 2 if multipanelSchemeSFN is configured or max{maxRanDCI-0-2k, maxRankSDM-DCI-0-2} = 2 if multipanelSchemeSDM is configured, transform precoder is disabled, and according to the value of higher layer parameter codebookSubsetDCI-0-2;

-4 or 6 bits according to Table 7.3.1.1.2-2B for 4 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2 respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, the values of higher layer parameters maxRankDCI-0-2=3 or 4, transform precoder is disabled, and according to the value of higher layer parameter codebookSubsetDCI-0-2;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 for 4 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} = 1 if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} = 1 if multipanelSchemeSDM is configured, and codebookSubsetDCI-0-2;

-3 or 4 bits according to Table 7.3.1.1.2-3A for 4 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} = 1 if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} = 1 if multipanelSchemeSDM is configured, and according to whether transform precoder is enabled or disabled, and the value of higher layer parameter codebookSubsetDCI-0-2;

-2 or 4 bits according to Table7.3.1.1.2-4 for 2 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} if multipanelSchemeSDM is configured, and codebookSubsetDCI-0-2;

-2 bits according to Table 7.3.1.1.2-4A for 2 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, transform precoder is disabled, the maxRankDCI-0-2=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} = 2 if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} = 2 if multipanelSchemeSDM is configured, and codebookSubsetDCI-0-2=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 for 2 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2}=1 if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2}=1 if multipanelSchemeSDM is configured, and codebookSubsetDCI-0-2;

-2 bits according to Table 7.3.1.1.2-5A for 2 antenna ports by replacing maxRank, maxRankSFN, maxRankSDM and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2, maxRankSDM-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSFN-DCI-0-2} = 1 if multipanelSchemeSFN is configured or max{maxRankDCI-0-2, maxRankSDM-DCI-0-2} = 1 if multipanelSchemeSDM is configured, and according to whether transform precoder is enabled or disabled, and the value of higher layer parameter codebookSubsetDCI-0-2.

-7 bits according to Table 7.3.1.1.2-5D for 8 antenna ports by replacing maxRank-n8 with maxRankDCI-0-2, if CodebookTypeUL=codebook1, transform precoder is disabled, maxRankDCI-0-2 =4, and according to maxRankDCI-0-2;

-4, 6 or 7 bits according to Table 7.3.1.1.2-5E for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook1, transform precoder is enabled or maxRankDCI-0-2 =1, 2 or 3 if transform precoder is disabled, and according to transform precoder and maxRankDCI-0-2;

-6 or 7 or 8 bits according to Table 7.3.1.1.2-5G for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook4, transform precoder is disabled, maxRankDCI-0-2=2, 3 or 4, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to maxRankDCI-0-2;

-3 bits according to Table 7.3.1.1.2-5H for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook4, transform precoder is enabled or maxRankDCI-0-2=1 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower.

-5, 9 or 10 bits according to Table 7.3.1.1.2-5J for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook2, transform precoder is enabled or maxRankDCI-0-2 =1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to transform precoder and maxRankDCI-0-2;

-4, 7, 9 or 10 bits according to Table 7.3.1.1.2-5L for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook3, transform precoder is enabled or maxRankDCI-0-2 =1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to transform precoder and maxRankDCI-0-2;

-6 or 7 or 8 bits according to Table 7.3.1.1.2-5M for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook4, transform precoder is disabled, maxRankDCI-0-2=2, 3 or 4, ul-FullPowerTransmission is configured to fullpowerMode1, and according to maxRankDCI-0-2;

-4 bits according to Table 7.3.1.1.2-5N for 8 antenna ports, if CodebookTypeUL=codebook4, transform precoder is enabled or maxRankDCI-0-2=1 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1.

-6, 9 or 10 bits according to Table 7.3.1.1.2-5O for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook2, transform precoder is enabled or maxRankDCI-0-2 =1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1, and according to transform precoder and maxRankDCI-0-2;

-5, 7, 9 or 10 bits according to Table 7.3.1.1.2-5P for 8 antenna ports by replacing maxRank with maxRankDCI-0-2, if CodebookTypeUL=codebook3, transform precoder is enabled or maxRankDCI-0-2 =1, 2, 3 or 4 if transform precoder is disabled, ul-FullPowerTransmission is configured to fullpowerMode1, and according to transform precoder and maxRankDCI-0-2;

-3 bits according to Table 7.3.1.1.2-5T for 3 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2;

-2 bits according to Table 7.3.1.1.2-5U for 3 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRankDCI-0-2;

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, the values of higher layer parameters maxRankDCI-0-2 is configured to be larger than 2, and at least one SRS resource with 4 antenna ports is configured in the SRS resource set indicated by SRS resource set indicator field if present, otherwise in an SRS resource set with usage set to 'codebook', and an SRS resource with 2 antenna ports is indicated via SRI in the same SRS resource set, then Table 7.3.1.1.2-4 is used by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2 respectively.

For the higher layer parameter txConfig = codebook, if different SRS resources with different number of antenna ports are configured, the bitwidth is determined according to the maximum number of ports in an SRS resource among the configured SRS resources in all SRS resource set(s) with usage set to 'codebook'. If the number of ports for a configured SRS resource in the set is less than the maximum number of ports in an SRS resource among the configured SRS resources, a number of most significant bits with value set to '0' are inserted to the field.

For the higher layer parameter txConfig = codebook, when the Transform precoder indicator field is present, if the bit width of the Precoding information and number of layers field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Precoding information and number of layers field for the case with smaller bit width until the bit width of the Precoding information and number of layers field for the two cases are the same.

When the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs, and is provided sTx-2Panel, and there are two SRS resource sets configured by srs-ResourceSetToAddModListDCI-0-2 and associated with usage of value 'codebook' or 'nonCodeBook', the Precoding information and number of layers field is associated with the SRS resource set that is associated with the coresetPoolIndex value for the CORESET used for the PDCCH carrying the DCI format 0_2.

-Second Precoding information - number of bits determined by the following:

-0 bits if SRS resource set indicator field is not present;

-0 bits if the higher layer parameter txConfig = nonCodeBook;

-0 bits for 1 antenna port and if the higher layer parameter txConfig = codebook;

-3, 4, or 5 bits according to Table 7.3.1.1.2-2C with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2 if multipanelSchemeSFN is configured, and codebookSubsetDCI-0-2;

-3 or 4 bits according to Table 7.3.1.1.2-2D with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, the values of higher layer parameters maxRankDCI-0-2=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2=2 if multipanelSchemeSFN is configured, transform precoder is disabled, and according to the value of higher layer parameter codebookSubsetDCI-0-2;

-3 or 4 bits according to Table 7.3.1.1.2-2E with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2 respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, maxRankDCI-0-2=3 or 4, transform precoder is disabled, and according to the value of higher layer parameter codebookSubsetDCI-0-2;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2 if multipanelSchemeSFN is configured, and codebookSubsetDCI-0-2;

-3 or 4 bits according to Table 7.3.1.1.2-3A with the same number of layers indicated by Precoding information and number of layers field for 4 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2=1 if multipanelSchemeSFN is configured, and the value of higher layer parameter codebookSubsetDCI-0-2;

-1 or 3 bits according to Table7.3.1.1.2-4B with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2 if multipanelSchemeSFN is configured, and codebookSubsetDCI-0-2;

-2 bits according to Table 7.3.1.1.2-4C with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, transform precoder is disabled, the maxRankDCI-0-2=2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2=2 if multipanelSchemeSFN is configured, and codebookSubsetDCI-0-2=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRankDCI-0-2 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2 if multipanelSchemeSFN is configured, and codebookSubsetDCI-0-2;

-2 bits according to Table 7.3.1.1.2-5A with the same number of layers indicated by Precoding information and number of layers field for 2 antenna ports by replacing maxRank, maxRankSFN and codebookSubset with maxRankDCI-0-2, maxRankSFN-DCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRankDCI-0-2=1 if neither multipanelSchemeSDM nor multipanelSchemeSFN is configured or maxRankSFN-DCI-0-2=1 if multipanelSchemeSFN is configured, and the value of higher layer parameter codebookSubsetDCI-0-2.

-2 bits according to Table 7.3.1.1.2-5V with the same number of layers indicated by Precoding information and number of layers field for 3 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRankDCI-0-2;

-2 bits according to Table 7.3.1.1.2-5U with the same number of layers indicated by Precoding information and number of layers field for 3 antenna ports by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2, respectively, if SRS resource set indicator field is present, txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRankDCI-0-2;

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, the values of higher layer parameters maxRankDCI-0-2 is configured to be larger than 2, and at least one SRS resource with 4 antenna ports is configured in the SRS resource set indicated by SRS resource set indicator field, and an SRS resource with 2 antenna ports is indicated via Second SRS resource indicator field in the same SRS resource set, then Table 7.3.1.1.2-4B is used by replacing maxRank and codebookSubset with maxRankDCI-0-2 and codebookSubsetDCI-0-2 respectively.

For the higher layer parameter txConfig = codebook, if different SRS resources with different number of antenna ports are configured, the bitwidth is determined according to the maximum number of ports in an SRS resource among the configured SRS resources in the second SRS resource set with usage set to 'codebook' as defined in Table 7.3.1.1.2-36. If the number of ports for a configured SRS resource in the set is less than the maximum number of ports in an SRS resource among the configured SRS resources, a number of most significant bits with value set to '0' are inserted to the field.

For the higher layer parameter txConfig = codebook, when the Transform precoder indicator field is present, if the bit width of the Second Precoding information field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Second Precoding information field for the case with smaller bit width until the bit width of the Second Precoding information field for the two cases are the same.

-Antenna ports - number of bits determined by the following:

-0 bit if higher layer parameter antennaPortsFieldPresenceDCI-0-2 is not configured;

-2, 3, 4, 5 or 6 bits otherwise,

-2 bits as defined by Tables 7.3.1.1.2-6, if transform precoder is enabled, dmrs-Type=1, and maxLength=1, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-2 bits as defined by 7.3.1.1.2-6A, if transform precoder is enabled, and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=1, where nSCID is the scrambling identity for antenna ports defined in Clause 6.4.1.1.1.2, in [4, TS38.211];

-4 bits as defined by Tables 7.3.1.1.2-7, if transform precoder is enabled, dmrs-Type=1, and maxLength=2, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-4 bits as defined by Tables 7.3.1.1.2-7A, if transform precoder is enabled, and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=2, where nSCID is the scrambling identity for antenna ports defined in Clause 6.4.1.1.1.2, in [4, TS38.211];

-3 bits as defined by Tables 7.3.1.1.2-8/9/10/10A/11 according to the value of rank, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=1;

-4 bits as defined by Tables 7.3.1.1.2-12/13/14/14A/15 according to the value of rank, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=2;

-4 bits as defined by Tables 7.3.1.1.2-16/17/18/18A/19 according to the value of rank, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=1;

-5 bits as defined by Tables 7.3.1.1.2-20/21/22/22A/23 according to the value of rank, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=2.

-4 bits as defined by Tables 7.3.1.1.2-38/39/40/40A/41, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=1;

-5 bits as defined by Tables 7.3.1.1.2-46/47/48/48A/49, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=2;

-5 bits as defined by Tables 7.3.1.1.2-54/55/56/56A/57, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=1;

-6 bits as defined by Tables 7.3.1.1.2-62/63/64/64A/65, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=2.

where the number of CDM groups without data of values 1, 2, and 3 in Tables 7.3.1.1.2-6 to 7.3.1.1.2-23 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively, and the value of rank is

-the sum of the value determined according to the SRS resource indicator field and the value determined according to the second SRS resource indicator field, if txConfig = nonCodebook and multipanelSchemeSDM is configured and SRS resource set indicator field equals "10"

-the sum of the value determined according to the Precoding information and number of layers field and the value determined according to the Second Precoding information, if txConfig = codebook and multipanelSchemeSDM is configured and SRS resource set indicator field equals "10"

-determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and multipanelSchemeSDM is not configured, , or if the higher layer parameter txConfig = nonCodebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "00" or “01”

-determined according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook and multipanelSchemeSDM is not configured, or if the higher layer parameter txConfig = codebook, multipanelSchemeSDM is configured and SRS resource set indicator field equals "00" or "01".

If a UE is configured with both dmrs-UplinkForPUSCH-MappingTypeA-DCI-0-2  and dmrs-UplinkForPUSCH-MappingTypeB-DCI-0-2 and is configured with antennaPortsFieldPresenceDCI-0-2, the bitwidth of this field equals , where   is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeA-DCI-0-2 and  is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeB-DCI-0-2. A number of zeros are padded in the MSB of this field, if the mapping type of the PUSCH corresponds to the smaller value of   and . maxxA,xBxAxBxA-xB xAxB

If a UE is not configured with higher layer parameter antennaPortsFieldPresenceDCI-0-2, antenna port(s) are defined assuming bit field index value 0 in Tables 7.3.1.1.2-6 to 7.3.1.1.2-23.

When the Transform precoder indicator field is present, if the bit width of the Antenna ports field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the Antenna ports field for the case with smaller bit width until the bit width of the Antenna ports field for the two cases are the same.

-SRS request - 0, 1, 2 or 3 bits

-0 bit if the higher layer parameter srs-RequestDCI-0-2 is not configured;

-1 bit as defined by Table 7.3.1.1.3-1 if higher layer parameter srs-RequestDCI-0-2 = 1 and for UEs not configured with supplementaryUplink in ServingCellConfig in the cell;

-2 bits if higher layer parameter srs-RequestDCI-0-2 = 1 and for UEs configured with supplementaryUplink in ServingCellConfig in the cell, where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second bit is defined by Table 7.3.1.1.3-1;

-2 bits as defined by Table 7.3.1.1.2-24 if higher layer parameter srs-RequestDCI-0-2 = 2 and for UEs not configured with supplementaryUplink in ServingCellConfig in the cell;

-3 bits if higher layer parameter srs-RequestDCI-0-2 = 2 and for UEs configured with supplementaryUplink in ServingCellConfig in the cell, where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24;

-SRS offset indicator - 0, 1 or 2 bits.

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214], where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-CSI request - 0, 1, 2, 3, 4, 5, or 6 bits determined by higher layer parameter reportTriggerSizeDCI-0-2.

-PTRS-DMRS association - number of bits determined as follows

-0 bit if PTRS-UplinkConfig is not configured in either dmrs-UplinkForPUSCH-MappingTypeA or dmrs-UplinkForPUSCH-MappingTypeB and transform precoder is disabled, or if transform precoder is enabled, or if maxRankDCI-0-2=1 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, or if maxMIMO-LayersDCI-0-2=1 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, or if maxRankDCI-0-2=1 and maxRankSFN-DCI-0-2=1, or if maxMIMO-LayersDCI-0-2=1 and maxMIMO-LayersforSFN-DCI-0-2=1, or if maxRankDCI-0-2=1 and maxRankSDM-DCI-0-2=1 when two PTRS ports are configured by maxNrofPorts-SDM, or if maxMIMO-LayersDCI-0-2=1 and maxMIMO-LayersforSDM-DCI-0-2=1 when two PTRS ports are configured by maxNrofPorts-SDM;

-1 or 2 bits otherwise, where Table 7.3.1.1.2-25/7.3.1.1.2-25A/7.3.1.1.2-25B/7.3.1.1.2-26/7.3.1.1.2-26B are used to indicate the association between PTRS port(s) and DMRS port(s), and the DMRS ports are indicated by the Antenna ports field.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 2, 4, or 8 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or “01” and maxRankDCI-0-2<=4 or maxMIMO-LayersDCI-0-2<=4, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Table 7.3.1.1.2-25 and 7.3.1.1.2-26.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 4 or 8 antenna ports, the SRS resource set indicator field is present and equals "10" or “11”, maxRankDCI-0-2=3 or 4 or maxMIMO-LayersDCI-0-2=3 or 4 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Table 7.3.1.1.2-25 and 7.3.1.1.2-26.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 2, 4, or 8 antenna ports, the SRS resource set indicator field is present and equals "10" or "11" and maxRankDCI-0-2=2 or maxMIMO-LayersDCI-0-2=2 and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, the MSB of this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or "01", maxRankDCI-0-2<=3 or maxMIMO-LayersDCI-0-2<=3, this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25.

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, SRS resource set indicator field is absent or SRS resource set indicator field is present and equals "00" or "01", maxRankDCI-0-2<=3 or maxMIMO-LayersDCI-0-2<=3, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-26B.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2=3 or maxMIMO-LayersDCI-0-2=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-25.

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2=2 or maxMIMO-LayersDCI-0-2=2, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, the MSB of this field indicates the association between PTRS port and DMRS port corresponding to SRS resource indicator and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port and DMRS port corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, the SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2<=3 or maxMIMO-LayersDCI-0-2<=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Tables 7.3.1.1.2-26B.

-2 bits when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig, the SRS resource set indicator field is present and equals "10" and multipanelSchemeSDM is configured, the MSB of this field indicates the association between PTRS port 0 and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field, and the LSB of this field indicates the association between PTRS port 1 and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second Precoding information field, according to Table 7.3.1.1.2-25A.

-2 bits when one PTRS port is configured by maxNrofPorts-SDM in PTRS-UplinkConfig, SRS resource set indicator field is present and equals "10" and multipanelSchemeSDM is configured, this field indicates the association between PTRS port and DMRS ports corresponding to SRS resource indicator field and Second SRS resource indicator field and/or Precoding information and number of layers field and Second Precoding information field according to Table 7.3.1.1.2-25.

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig, SRS resource set indicator field is present and equals "10", multipanelSchemeSFN is configured, this field indicates the association between PTRS port(s) and DMRS port(s) corresponding to SRS resource indicator field and/or Precoding information and number of layers field according to Table 7.3.1.1.2-25 and 7.3.1.1.2-26.

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and the "PTRS-DMRS association" field is present for the indicated bandwidth part but not present for the active bandwidth part, the UE assumes the "PTRS-DMRS association" field is not present for the indicated bandwidth part.

When the Transform precoder indicator field is present, if the bit width of PTRS-DMRS association field for the case with transform precoder enabled is not equal to that for the case with transform precoder disabled, a number of most significant bits with value set to '0' are inserted to the PTRS-DMRS association field for the case with smaller bit width until the bit width of the PTRS-DMRS association field for the two cases are the same.

-Second PTRS-DMRS association

-2 bits when one PTRS port or two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 4 or 8 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2>2 or maxMIMO-LayersDCI-0-2>2, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-2 bits when one PTRS port is configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2=3 or maxMIMO-LayersDCI-0-2=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-1 bit when two PTRS ports are configured by maxNrofPorts in PTRS-UplinkConfig for 3 antenna ports, PTRS-DMRS association field is present, SRS resource set indicator field is present and equals "10" or "11", maxRankDCI-0-2<=3 or maxMIMO-LayersDCI-0-2<=3, and neither multipanelSchemeSDM nor multipanelSchemeSFN is configured;

-0 bit otherwise.

Tables 7.3.1.1.2-25 and 7.3.1.1.2-26/7.3.1.1.2-26B are used to indicate the association between PTRS port(s) and DMRS port(s) corresponding to Second SRS resource indicator field and/or Second precoding information field when one PT-RS port and two PT-RS ports are configured by maxNrofPorts in PTRS-UplinkConfig respectively, and the DMRS ports are indicated by the Antenna ports field.

-beta_offset indicator - 0 bit if the higher layer parameter betaOffsetsDCI-0-2 = semiStaticDCI-0-2; otherwise 1 bit if 2 offset indexes are configured by higher layer parameter dynamicDCI-0-2 as defined by Table 9.3-3A in [5, TS 38.213], and 2 bits if 4 offset indexes are configured by higher layer parameter dynamicDCI-0-2 as defined by Table 9.3-3 in [5, TS 38.213].

When two HARQ-ACK codebooks are configured by pdsch-HARQ-ACK-CodebookList or by pdsch-HARQ-ACK-CodebookListMulticast for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-2 is configured, if the bit width of the beta_offset indicator in DCI format 0_2 for one HARQ-ACK codebook is not equal to that of the beta_offset indicator in DCI format 0_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller beta_offset indicator until the bit width of the beta_offset indicator in DCI format 0_2 for the two HARQ-ACK codebooks are the same.

-DMRS sequence initialization - 0 or 1 bit

-0 bit if the higher layer parameter dmrs-SequenceInitializationDCI-0-2 is not configured, or if transform precoder is enabled by higher layers and the Transform precoder indicator field is not present;

-1 bit if transform precoder is disabled by higher layers and the higher layer parameter dmrs-SequenceInitializationDCI-0-2 is configured, or if the Transform precoder indicator field is present and the higher layer parameter dmrs-SequenceInitializationDCI-0-2 is configured. If the Transform precoder indicator field is present and set to '0', the bit is reserved.

-UL-SCH indicator - 1 bit. A value of "1" indicates UL-SCH shall be transmitted on the PUSCH and a value of "0" indicates UL-SCH shall not be transmitted on the PUSCH. If a UE does not support triggering SRS only in DCI, except for DCI format 0_2 with CRC scrambled by SP-CSI-RNTI, the UE is not expected to receive a DCI format 0_2 with UL-SCH indicator of "0" and CSI request of all zero(s). If a UE supports triggering SRS only in DCI, except for DCI format 0_2 with CRC scrambled by SP-CSI-RNTI, the UE is not expected to recerive a DCI format 0_2 with UL-SCH indicator of "0", CSI request of all zero(s) and SRS request of all zero(s).

-ChannelAccess-CPext-CAPC - 0, 1, 2, 3, 4, 5 or 6 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-0-2 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or the number of entries in the high layer parameter ul-AccessConfigListDCI-0-1 for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.1.2-35 are configured by the higher layer parameter ul-AccessConfigListDCI-0-2 in frequency range 1. One or more entries from Table 7.3.1.1.2-35A are configured by the higher layer parameter ul-AccessConfigListDCI-0-1 in frequency range 2-2.log2(I)

-Open-loop power control parameter set indication - 0 or 1 or 2 bits.

-0 bit if the higher layer parameter p0-PUSCH-SetList is not configured;

-1 or 2 bits otherwise,

-1 bit if SRS resource indicator is present in the DCI format 0_2;

-1 or 2 bits as determined by higher layer parameter olpc-ParameterSetDCI-0-2 if SRS resource indicator is not present in the DCI format 0_2;

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-0-2 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-Invalid symbol pattern indicator - 0 bit if higher layer parameter invalidSymbolPatternIndicatorDCI-0-2 is not configured; otherwise 1 bit as defined in Clause 6.1.2.1 in [6, TS 38.214].

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-0 bit, otherwise

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-0-2 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

A UE does not expect that the bit width of a field in DCI format 0_2 with CRC scrambled by CS-RNTI is larger than corresponding bit width of same field in DCI format 0_2 with CRC scrambled by C-RNTI for the same serving cell. If the bit width of a field in the DCI format 0_2 with CRC scrambled by CS-RNTI is not equal to that of the corresponding field in the DCI format 0_2 with CRC scrambled by C-RNTI for the same serving cell, a number of most significant bits with value set to '0' are inserted to the field in DCI format 0_2 with CRC scrambled by CS-RNTI until the bit width equals that of the corresponding field in the DCI format 0_2 with CRC scrambled by C-RNTI for the same serving cell.

For a UE configured with scheduling on the primary cell from an SCell, if prior to padding the number of information bits in DCI format 0_2 carried by PDCCH on the primary cell is not equal to the number of information bits in DCI format 0_2 carried by PDCCH on the SCell for scheduling on the primary cell, zeros shall be appended to the DCI format 0_2 with smaller size until the payload size is the same.

-If application of step 4B in clause 7.3.1.0 results in additional zero padding for DCI format 0_2 for scheduling on the primary cell, corresponding zeros shall be appended to both DCI format 0_2 monitored on the primary cell and DCI format 0_2 monitored on the SCell for scheduling on the primary cell.

-If the SCell is deactivated and firstActiveDownlinkBWP-Id is not set to dormant BWP, the UE determines the number of information bits in DCI format 0_2 carried by PDCCH on the primary cell based on a DL BWP provided by firstActiveDownlinkBWP-Id for the SCell. If the active DL BWP of the SCell is a dormant DL BWP, or if the SCell is deactivated and firstActiveDownlinkBWP-Id is set to dormant BWP, the UE determines the number of information bits in DCI format 0_2 carried by PDCCH on the primary cell based on a DL BWP provided by firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a DL BWP provided by firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.1.3-1: 1 bit SRS request in DCI format 0_2 and DCI format 1_2

## 7.3.1.1.4Format 0_3

DCI format 0_3 is used for the scheduling of one or multiple PUSCHs in one cell, or multiple PUSCHs in multiple cells with one or multiple PUSCHs per cell.

The following information is transmitted by means of the DCI format 0_3 with CRC scrambled by C-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 0, indicating an UL DCI format

-Scheduled cell set indicator - bits, where  is the number of cell sets which are configured by higher layer parameter mc-DCI-SetofCellsToAddModList to be respectively scheduled by DCI format 0_3/1_3 from the cell on which this format is carried by PDCCH. If present, this field is used to indicate the scheduled cell set according to Table 7.3.1.1.4-1; otherwise, the scheduled cell set is the cell set configured to be scheduled by DCI format 0_3/1_3 from the cell by higher layer parameter mc-DCI-SetofCellsToAddModList.  log2NsetNset

-Scheduled cells indicator - number of bits determined by the following:

-0 bit if the higher layer parameter scheduledCellComboListDCI-0-3 for the scheduled cell set is not configured;

-otherwise  bits indicating the scheduled cells in the scheduled cell set according to Table 7.3.1.1.4-2, where  is the number of entries in the higher layer parameter scheduledCellComboListDCI-0-3. If only one entry is configured in the higher layer parameter scheduledCellComboListDCI-0-3, the scheduled cells are the cells configured by higher layer parameter scheduledCellComboListDCI-0-3.log2IULIUL

-Bandwidth part indicator - 0, 1 or 2 bits determined as , where log2nBWP, max

- if , is the maximum number of UL BWPs configured by higher layers, excluding the initial UL bandwidth part, across all the cells configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set, in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;nBWP, max=nBWP,RRCmax+1nBWP,RRCmax≤3nBWP,RRCmax

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;nBWP, max=nBWP,RRCmax

The field is only applicable to a scheduled cell with the number of configured UL BWPs larger than 1, including the initial UL bandwidth part, and is applied to the applicable scheduled cells in the scheduled cell set independently. If a UE does not support active BWP change via DCI, the UE ignores this bit field. If this field indicates a code point that does not correspond to a configured BWP of a scheduled cell, the UE ignores this bit field for the scheduled cell, and operates on the active BWP of the scheduled cell.

-Frequency domain resource assignment - number of bits determined by the following, where  is the size of the active UL bandwidth part:NRBUL, BWP

-block number 1, block number 2,…, block number NcellUL

If scheduledCellComboListDCI-0-3 for the scheduled cell set is configured with more than one entry,  is the number of scheduled cells indicated by Scheduled cells indicator field; if scheduledCellComboListDCI-0-3 for the scheduled cell set is configured with only one entry, is the number of cells configured by higher layer parameter scheduledCellComboListDCI-0-3; otherwise,  is the number of cells configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set. Each block corresponds to the frequency domain resource assignment for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the frequency domain resource assignment for the cell with the smallest serving cell index. Each block is defined by the following fields: NcellUL NcellULNcellUL

-If higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is not configured

- bits if only resource allocation type 0 is configured, where  is defined in Clause 6.1.2.2.1 of [6, TS 38.214]NRBGNRBG

- bits if only resource allocation type 1 is configured, or  bits if resourceAllocationDCI-0-3 is configured as 'dynamicSwitch', where   is the size of the active UL bandwidth part,  is defined as in clause 4.4.4.4 of [4, TS 38.211] and  is given by higher layer parameter resourceAllocationType1GranularityDCI-0-3. If the higher layer parameter resourceAllocationType1GranularityDCI-0-3 is not configured,  is equal to 1.log2NRBG, K1NRBG, K1+1/2max log2NRBG, K1NRBG, K1+1/2, NRBG+1NRBG, K1=NRBUL, BWP+NUL, BWPstartmodK1/K1,NRBUL, BWPNUL, BWPstartK1K1

-If resourceAllocationDCI-0-3 is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 6.1.2.2.1 of [6, TS 38.214].NRBG

-For resource allocation type 1, the  LSBs provide the resource allocation as follows:log2NRBG, K1NRBG, K1+1/2

-For PUSCH hopping with resource allocation type 1:

-MSB bits are used to indicate the frequency offset according to Clause 6.3 of [6, TS 38.214], where  if the higher layer parameter frequencyHoppingOffsetLists contains two offset values and if the higher layer parameter frequencyHoppingOffsetLists contains four offset valuesNUL_hop NUL_hop=1NUL_hop=2

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]log2NRBG, K1NRBG, K1+1/2-NUL_hop

-For non-PUSCH hopping with resource allocation type 1:

- bits provide the frequency domain resource allocation according to Clause 6.1.2.2.2 of [6, TS 38.214]log2NRBG, K1NRBG, K1+1/2

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocationDCI-0-3 is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

-If the higher layer parameter useInterlacePUCCH-PUSCH in BWP-UplinkDedicated is configured

-5 + Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 30 kHz. The 5 MSBs provide the interlace allocation and the Y LSBs provide the RB set allocation.

-6 + Y bits provide the frequency domain resource allocation according to Clause 6.1.2.2.3 of [6, TS 38.214] if the subcarrier spacing for the active UL bandwidth part is 15 kHz. The 6 MSBs provide the interlace allocation and the Y LSBs provide the RB set allocation.

The value of Y is determined by  where   is the number of RB sets contained in the active UL BWP as defined in clause 7 of [6, TS38.214].log2NRB-set,ULBWPNRB-set,ULBWP+12 NRB-set,ULBWP

If the higher layer parameter scheduledCellComboListDCI-0-3 for the scheduled cell set is not configured, each block is also used to indicate whether the corresponding cell is scheduled or not as follows:

-if all bits of a block are set to 0 for resource allocation type 0, or set to 1 for resource allocation type 1, or set to 0 or 1 for dynamic switch resource allocation type, or set to 0 for resource allocation type 2 with μ=1, or set to 1 for resource allocation type 2 with μ=0, the cell corresponding to the block is not scheduled;

-otherwise, the cell corresponding to the block is scheduled.

-Time domain resource assignment - bits, where   is the number of entries in the higher layer parameter tdra-FieldIndexListDCI-0-3. This field is used to indicate an entry in the higher layer parameter tdra-FieldIndexListDCI-0-3 according to Table 7.3.1.1.4-3. Each entry in the higher layer parameter tdra-FieldIndexListDCI-0-3 contains the ‘Time domain resource assignment’ index for each BWP of each cell in the scheduled cell set, where the ‘Time domain resource assignment’ indexes for all the cells are placed according to an ascending order of a serving cell index, and the 'Time domain resource assignment' indexes for all the BWPs of a cell are placed according to an ascending order of the higher layer parameter BWP-Id. log2(ITDRA) ITDRA

-Frequency hopping flag - 0 or 1 bit

-0 bit if the higher layer parameter frequencyHopping is not configured for any cell configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set;

-1 bit according to Table 7.3.1.1.1-3 otherwise, only applicable to resource allocation type 1, as defined in Clause 6.3 of [6, TS 38.214].

The field is only applicable to a scheduled cell configured with frequencyHopping, and is applied to the applicable scheduled cells independently.

-Modulation and coding scheme - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellUL

Each block corresponds to the modulation and coding scheme for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the modulation and coding scheme for the cell with the smallest serving cell index. Each block is 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214].

-New data indicator - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellUL

Each block corresponds to the new data indicator for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the new data indicator for the cell with the smallest serving cell index. If pusch-TimeDomainAllocationListForMultiPUSCH-DCI-0-3 is configured for a cell, the number of bits for the corresponding block is equal to the maximum number of schedulable PUSCHs among all entries in the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH-DCI-0-3 for the cell, where each bit corresponds to one scheduled PUSCH as defined in clause 6.1.4 in [6, TS 38.214]; otherwise, the corresponding block is 1 bit.

-Redundancy version - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellUL

Each block corresponds to the redundancy version for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the redundancy version for the cell with the smallest serving cell index. The number of bits for each block is determined by following:

-if pusch-TimeDomainAllocationListForMultiPUSCH-DCI-0-3 is configured for a cell, the number of bits for the corresponding block is determined by , where  is the maximum number of schedulable PUSCHs among all entries in the higher layer parameter pusch-TimeDomainAllocationListForMultiPUSCH-DCI-0-3 for the cell,  is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-0-3 for the cell, and each  bit(s) corresponds to one scheduled PUSCH as defined in clause 6.1.4 in [6, TS 38.214],mA×mBmAmBmB

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-otherwise, the corresponding block is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-0-3 configured for the cell,

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-HARQ process number - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellUL

Each block corresponds to the HARQ process number for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the HARQ process number for the cell with the smallest serving cell index. Each block is 0, 1, 2, 3, 4 or 5 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-0-3 or harq-ProcessNumberSizeDCI-0-3-Ext configured for the cell corresponding to the block.

-1st downlink assignment index - 1 or 2 bits

-1 bit for semi-static HARQ-ACK codebook;

-2 bits for dynamic HARQ-ACK codebook.

When two HARQ-ACK codebooks are configured for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-3 is configured, if the bit width of the 1st downlink assignment index in DCI format 0_3 for one HARQ-ACK codebook is not equal to that of the 1st downlink assignment index in DCI format 0_3 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 1st downlink assignment index until the bit width of the 1st downlink assignment index in DCI format 0_3 for the two HARQ-ACK codebooks are the same.

-2nd downlink assignment index - 0 or 2 bits:

-2 bits for dynamic HARQ-ACK codebook with two HARQ-ACK sub-codebooks;

-0 bit otherwise.

When two HARQ-ACK codebooks are configured for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-3 is configured, if the bit width of the 2nd downlink assignment index in DCI format 0_3 for one HARQ-ACK codebook is not equal to that of the 2nd downlink assignment index in DCI format 0_3 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller 2nd  downlink assignment index until the bit width of the 2nd downlink assignment index in DCI format 0_3 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUSCH - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellUL

Each block corresponds to the TPC command for the scheduled PUSCH for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the TPC command for the scheduled PUSCH for the cell with the smallest serving cell index. Each block is 2 bits as defined in Clause 7.1.1 of [5, TS38.213].

-SRS resource indicator - number of bits determined by the following:

-If sri-DCI0-3= type1a is configured by higher layer,

-bits applying to the scheduled cells with  independently, where  is the number of cells configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set,  is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined below. maxr∈{1,2,…,NcellUL,2}Msr Msr>0NcellUL, 2rr=1Msr

-If sri-DCI0-3= type2 is configured by higher layer,

-block number 1, block number 2,…, block number  NcellUL

Each block corresponds to the SRS resource indicator for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the SRS resource indicator for the cell with the smallest serving cell index. Each block is defined below.

above for the case of sri-DCI0-3= type1a or each block above for the case of sri-DCI0-3= type2 is defined by the following:Msr

- bits according to Tables 7.3.1.1.2-28/29/30/31 if the higher layer parameter txConfig = nonCodebook, where  is the number of configured SRS resources in the first SRS resource set configured by higher layer parameter srs-ResourceSetToAddModList, and associated with the higher layer parameter usage of value 'nonCodeBook' andlog2k=1minLmax, NSRSNSRSkNSRS

-if UE supports operation with maxMIMO-Layers and the higher layer parameter maxMIMO-Layers of PUSCH-ServingCellConfig of the serving cell is configured, Lmax is given by that parameter

-otherwise, Lmax is given by the maximum number of layers for PUSCH supported by the UE for the serving cell for non-codebook based operation.

- bits according to Tables 7.3.1.1.2-32, 7.3.1.1.2-32A and 7.3.1.1.2-32B if the higher layer parameter txConfig = codebook, where  is the number of configured SRS resources in the first SRS resource set configured by higher layer parameter srs-ResourceSetToAddModList, and associated with the higher layer parameter usage of value 'codeBook'.log2NSRSNSRS

-Precoding information and number of layers - number of bits determined by the following:

-If tpmi-DCI0-3= type1a is configured by higher layer,

-bits applying to the scheduled cells with  independently, where  is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined below.  maxr∈{1,2,…,NcellUL,2}Mpr Mpr>0rr=1Mpr

-If tpmi-DCI0-3= type2 is configured by higher layer,

-block number 1, block number 2,…, block number   NcellUL

Each block corresponds to the precoding information and number of layers for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the precoding information and number of layers for the cell with the smallest serving cell index. Each block is defined below.

above for the case of tpmi-DCI0-3= type1a or each block above for the case of tpmi-DCI0-3= type2 is defined by the following:Mpr

-0 bits if the higher layer parameter txConfig = nonCodeBook;

-0 bits for 1 antenna port and if the higher layer parameter txConfig = codebook;

-4, 5, or 6 bits according to Table 7.3.1.1.2-2 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank, and codebookSubset;

-4 or 5 bits according to Table 7.3.1.1.2-2A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, maxRank=2, transform precoder is disabled, and according to the value of higher layer parameter codebookSubset;

-4 or 6 bits according to Table 7.3.1.1.2-2B for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, maxRank=3 or 4, transform precoder is disabled, and according to the value of higher layer parameter codebookSubset;

-2, 4, or 5 bits according to Table 7.3.1.1.2-3 for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank and codebookSubset;

-3 or 4 bits according to Table 7.3.1.1.2-3A for 4 antenna ports, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRank=1, and the value of higher layer parameter codebookSubset;

-2 or 4 bits according to Table7.3.1.1.2-4 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, transform precoder is disabled, and according to the values of higher layer parameters maxRank and codebookSubset;

-2 bits according to Table 7.3.1.1.2-4A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, transform precoder is disabled, maxRank=2, and codebookSubset=nonCoherent;

-1 or 3 bits according to Table7.3.1.1.2-5 for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission is not configured or configured to fullpowerMode2 or configured to fullpower, and according to whether transform precoder is enabled or disabled, and the values of higher layer parameters maxRank and codebookSubset;

-2 bits according to Table 7.3.1.1.2-5A for 2 antenna ports, if txConfig = codebook, ul-FullPowerTransmission =fullpowerMode1, and according to whether transform precoder is enabled, or disabled and maxRank=1, and the value of higher layer parameter codebookSubset.

For the higher layer parameter txConfig=codebook, if ul-FullPowerTransmission is configured to fullpowerMode2, maxRank is configured to be larger than 2, and at least one SRS resource with 4 antenna ports is configured in an SRS resource set with usage set to 'codebook', and an SRS resource with 2 antenna ports is indicated via SRI in the same SRS resource set, then Table 7.3.1.1.2-4 is used.

For the higher layer parameter txConfig = codebook, if different SRS resources with different number of antenna ports are configured, the bitwidth is determined according to the maximum number of ports in an SRS resource among the configured SRS resources in an SRS resource set with usage set to 'codebook'. If the number of ports for a configured SRS resource in the set is less than the maximum number of ports in an SRS resource among the configured SRS resources, a number of most significant bits with value set to '0' are inserted to the field.

-Antenna ports - number of bits determined by the following:

-If antennaPortsDCI0-3= type1a is configured by higher layer,

-bits applying to the scheduled cells independently, where  is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined below. maxr∈{1,2,…,NcellUL,2}MAr rr=1MAr

-If antennaPortsDCI0-3= type2 is configured by higher layer,

-block number 1, block number 2,…, block number  NcellUL

Each block corresponds to the Antenna ports information for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the Antenna ports information for the cell with the smallest serving cell index. Each block is defined below.

above for the case of antennaPortsDCI0-3= type1a or each block above for the case of antennaPortsDCI0-3= type2 is defined by the following:MAr

-2 bits as defined by Tables 7.3.1.1.2-6, if transform precoder is enabled, dmrs-Type=1, and maxLength=1, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-2 bits as defined by Tables 7.3.1.1.2-6A, if transform precoder is enabled and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=1, where nSCID is the scrambling identity for antenna ports defined in clause 6.4.1.1.1.2, TS38.211];

-4 bits as defined by Tables 7.3.1.1.2-7, if transform precoder is enabled, dmrs-Type=1, and maxLength=2, except that dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured and π/2 BPSK modulation is used;

-4 bits as defined by Tables 7.3.1.1.2-7A, if transform precoder is enabled and dmrs-UplinkTransformPrecoding and tp-pi2BPSK are both configured, π/2 BPSK modulation is used, dmrs-Type=1, and maxLength=2, where nSCID is the scrambling identity for antenna ports defined in clause 6.4.1.1.1.2, TS38.211];

-3 bits as defined by Tables 7.3.1.1.2-8/9/10/11, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=1, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-4 bits as defined by Tables 7.3.1.1.2-12/13/14/15, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is not configured, and maxLength=2, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-4 bits as defined by Tables 7.3.1.1.2-16/17/18/19, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=1, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-5 bits as defined by Tables 7.3.1.1.2-20/21/22/23, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is not configured, and maxLength=2, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-4 bits as defined by Tables 7.3.1.1.2-38/39/40/40A/41, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=1, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-5 bits as defined by Tables 7.3.1.1.2-46/47/48/48A/49, if transform precoder is disabled, dmrs-Type=1, dmrs-TypeEnh is configured, and maxLength=2, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-5 bits as defined by Tables 7.3.1.1.2-54/55/56/56A/57, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=1, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook;

-6 bits as defined by Tables 7.3.1.1.2-62/63/64/64A/65, if transform precoder is disabled, dmrs-Type=2, dmrs-TypeEnh is configured, and maxLength=2, and the value of rank is determined according to the SRS resource indicator field if the higher layer parameter txConfig = nonCodebook and according to the Precoding information and number of layers field if the higher layer parameter txConfig = codebook.

where the number of CDM groups without data of values 1, 2, and 3 in Tables 7.3.1.1.2-6 to 7.3.1.1.2-23 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively.

If a UE is configured with both dmrs-UplinkForPUSCH-MappingTypeA and dmrs-UplinkForPUSCH-MappingTypeB, the bitwidth of this field equals , where  is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeA and   is the "Antenna ports" bitwidth derived according to dmrs-UplinkForPUSCH-MappingTypeB. A number of  zeros are padded in the MSB of this field, if the mapping type of the PUSCH corresponds to the smaller value of  and .maxxA,xBxAxBxA-xBxAxB

-SRS request -bits, where  is the number of entries in the higher layer parameter srs-RequestListDCI-0-3, or 0 bit if the higher layer parameter srs-RequestListDCI-0-3 is not configured. This field is used to indicate an entry in the higher layer parameter srs-RequestListDCI-0-3 according to Table 7.3.1.1.4-4. Each entry in the higher layer parameter srs-RequestListDCI-0-3 contains the ‘SRS request’ index for each cell in the scheduled cell set, where the ‘SRS request’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘SRS request’ index is defined by the following: log2(ISRS) ISRS

-2 bits as defined by Table 7.3.1.1.2-24 for UEs not configured with supplementaryUplink in ServingCellConfig in the cell; 3 bits for UEs configured with supplementaryUplink in ServingCellConfig in the cell where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24. This bit field may also indicate the associated CSI-RS according to Clause 6.1.1.2 of [6, TS 38.214].

-SRS offset indicator -bits, where is the number of entries in the higher layer parameter srs-OffsetListDCI-0-3, or 0 bit if the higher layer parameter srs-OffsetListDCI-0-3 is not configured. This field is used to indicate an entry in the higher layer parameter srs-OffsetListDCI-0-3 according to Table 7.3.1.1.4-5. Each entry in the higher layer parameter srs-OffsetListDCI-0-3 contains the ‘SRS offset indicator’ index for each cell in the scheduled cell set, where the ‘SRS offset indicator’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘SRS offset indicator’ index is defined by the following:    log2(Ioffset) Ioffset

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214],  where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-CSI request - 0, 1, 2, 3, 4, 5, or 6 bits determined by higher layer parameter reportTriggerSize. This field is applied to the cell with the smallest serving cell index among the scheduled cells indicated by Scheduled cells indicator field or Frequency domain resource assignment field.

-PTRS-DMRS association - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellUL

Each block corresponds to the PTRS-DMRS association information for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the PTRS-DMRS association information for the cell with the smallest serving cell index. Each block is defined by the following:

-0 bit if PTRS-UplinkConfig is not configured in either dmrs-UplinkForPUSCH-MappingTypeA or dmrs-UplinkForPUSCH-MappingTypeB and transform precoder is disabled, or if transform precoder is enabled, or if maxRank=1;

-2 bits otherwise, where Table 7.3.1.1.2-25 and 7.3.1.1.2-26 are used to indicate the association between PTRS port(s) and DMRS port(s) when one PT-RS port and two PT-RS ports are configured by maxNrofPorts in PTRS-UplinkConfig respectively, and the DMRS ports are indicated by the Antenna ports field.

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and the "PTRS-DMRS association" field is present for the indicated bandwidth part but not present for the active bandwidth part, the UE assumes the "PTRS-DMRS association" field is not present for the indicated bandwidth part.

-beta_offset indicator  -  0 or 2 bits

-0 bit if betaOffsets = semiStatic is configured in uci-OnPUSCH-ListDCI-0-3 for all the cells configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set;

-otherwise 2 bits as defined by Table 9.3-3 in [5, TS 38.213].

When two HARQ-ACK codebooks are configured for the same serving cell and if higher layer parameter priorityIndicatorDCI-0-3 is configured, if the bit width of the beta_offset indicator in DCI format 0_3 for one HARQ-ACK codebook is not equal to that of the beta_offset indicator in DCI format 0_3 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller beta_offset indicator until the bit width of the beta_offset indicator in DCI format 0_3 for the two HARQ-ACK codebooks are the same.

The field is only applicable to a scheduled cell configured with betaOffsets = dynamic in uci-OnPUSCH-ListDCI-0-3, and is applied to the applicable scheduled cells independently.

-DMRS sequence initialization - 1 bit if transform precoder is disabled at least for one cell configured by higher layer parameter ScheduledCellListDCI-0-3 in the scheduled cell set; otherwise, 0 bit.

This field is independently applied to all the scheduled cells with transform precoder disabled, and indicated by Scheduled cells indicator field or Frequency domain resource assignment field.

-UL-SCH indicator - 1 bit. A value of "1" indicates UL-SCH shall be transmitted on the PUSCH and a value of "0" indicates UL-SCH shall not be transmitted on the PUSCH. A UE is not expected to receive a DCI format 0_3 with UL-SCH indicator of "0" and CSI request of all zero(s). This field is applied to the PUSCH on the cell with the smallest serving cell index among the scheduled cells indicated by Scheduled cells indicator field or Frequency domain resource assignment field as defined in Clause 5.2.3 of [6, TS 38.214].

-ChannelAccess-CPext-CAPC -bits applying to the scheduled cells with  independently, where  is the number of cells configured by higher layer parameter scheduledCellListDCI-0-3 in the scheduled cell set,  is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined by the following: maxr∈{1,2,…,Ncell2}Mcr Mcr>0Ncell2rr=1Mcr

-0, 1, 2, 3, 4, 5 or 6 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-0-1 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.1.2-35 or Table 7.3.1.1.2-35A are configured by the higher layer parameter ul-AccessConfigListDCI-0-1.log2(I)

-Open-loop power control parameter set indication - bits applying to the scheduled cells with  independently, where  is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined by the following:maxr∈{1,2,…,NcellUL,2}Mor Mor>0rr=1Mor

-0 bit if the higher layer parameter p0-PUSCH-SetList is not configured for a serving cell associated to index ;r

-1 or 2 bits otherwise,

-1 bit if SRS resource indicator block number  is present in the DCI format 0_3 when SRI-DCI0-3= type2 or if  when SRI-DCI0-3= type1a;rMsr>0

-1 or 2 bits as determined by higher layer parameter olpc-ParameterSetDCI-0-1 if SRS resource indicator block number  is not present in the DCI format 0_3 when SRI-DCI0-3= type2 or if  when SRI-DCI0-3= type1a.rMsr=0

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-0-3 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213]. This field is applied to all the scheduled cells indicated by Scheduled cells indicator field or Frequency domain resource assignment field.

-Minimum applicable scheduling offset indicator - 0 or 1 bit

-0 bit if higher layer parameter minimumSchedulingOffsetK0DCI-0-3 is not configured;

-1 bit otherwise. The 1 bit indication is used to determine the minimum applicable K2 for the active UL BWP and the minimum applicable K0 for the active DL BWP, if configured respectively, according to Table 7.3.1.1.2-33. If the minimum applicable K0 is indicated, the minimum applicable value of the aperiodic CSI-RS triggering offset for an active DL BWP for each scheduled cell shall be the same as the minimum applicable K0.

-SCell dormancy indication - 0 bit if higher layer parameter dormancyDCI-0-3 or dormancyGroupWithinActiveTime is not configured; otherwise 1, 2, 3, 4, or 5 bits bitmap determined according to the number of different DormancyGroupID(s) provided by higher layer parameter dormancyGroupWithinActiveTime, where each bit corresponds to one of the SCell group(s) configured by higher layers parameter dormancyGroupWithinActiveTime, with MSB to LSB of the bitmap corresponding to the first to last configured SCell group in ascending order of DormancyGroupID. The field is only present when this format is carried by PDCCH on the primary cell within DRX Active Time and the UE is configured with at least two DL BWPs for an SCell.

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-0 bit if higher layer parameter pdcchMonAdaptDCI-0-3 is not enabled;

-otherwise,

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-0-3 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

If scheduledCellComboListDCI-0-3 for the cell set is configured, zeros shall be appended to DCI format 0_3 if needed until the payload size equals the size of DCI format 0_3 that is determined by the configuration of the corresponding active bandwidth part(s) of the scheduled cells in the entry which results in the largest size among the entries in the higher layer parameter scheduledCellComboListDCI-0-3.

If an SCell within the scheduled cell set is deactivated, the UE determines the bitwidth of the fields in DCI format 0_3 based on a UL BWP provided by firstActiveUplinkBWP-Id for the SCell. If the active DL BWP of an SCell within the scheduled cell set is a dormant DL BWP, the UE determines the bitwidth of the fields in DCI format 0_3 based on the UL BWP provided by BWP-id equal to firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a UL BWP provided by BWP-id equal to firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.1.4-1: Scheduled cell set indicator in DCI format 0_3 and DCI format 1_3

Table 7.3.1.1.4-2: Scheduled cells indicator in DCI format 0_3

Table 7.3.1.1.4-3: Time domain resource assignment in DCI format 0_3

Table 7.3.1.1.4-4: SRS request in DCI format 0_3

Table 7.3.1.1.4-5: SRS offset indicator in DCI format 0_3

## 7.3.1.2DCI formats for scheduling of PDSCH

## 7.3.1.2.1Format 1_0

DCI format 1_0 is used for the scheduling of PDSCH in one DL cell.

The following information is transmitted by means of the DCI format 1_0 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bits

-The value of this bit field is always set to 1, indicating a DL DCI format

-Frequency domain resource assignment -  bits where  is given by Clause 7.3.1.0

If the CRC of the DCI format 1_0 is scrambled by C-RNTI and the "Frequency domain resource assignment" field are of all ones, the DCI format 1_0 is for random access procedure initiated by a PDCCH order, with all remaining fields set as follows:

-Random Access Preamble index - 6 bits according to ra-PreambleIndex in Clause 5.1.2 of [8, TS38.321]

-UL/SUL indicator - 1 bit.

-If the Cell indicator field is absent or the Cell indicator field indicates serving cell, if the value of the "Random Access Preamble index" is not all zeros and if the UE is configured with supplementaryUplink in ServingCellConfig in the cell, this field indicates which UL carrier in the cell to transmit the PRACH according to Table 7.3.1.1.1-1;

-If the Cell indicator field indicates a candidate cell, if the value of the "Random Access Preamble index" is not all zeros and if the UE is configured with ltm-EarlyUL-SyncConfigSUL in LTM-Candidate for the candidate cell, this field indicates which UL carrier in the candidate cell to transmit the PRACH according to Table 7.3.1.1.1-1;

-Otherwise, this field is reserved.

-SS/PBCH index - 6 bits. If the value of the "Random Access Preamble index" is not all zeros, this field indicates the SS/PBCH that shall be used to determine the RACH occasion for the PRACH transmission; otherwise, this field is reserved.

-PRACH Mask index - 4 bits. If the value of the "Random Access Preamble index" is not all zeros, this field indicates the RACH occasion associated with the SS/PBCH indicated by "SS/PBCH index" for the PRACH transmission, according to Clause 5.1.1 of [8, TS38.321]; otherwise, this field is reserved

-Cell indicator - bits indicating the cell for the corresponding PRACH transmission if the UE is configured with higher layer parameter EarlyUL-SyncConfig, where C is the number of candidate cells configured with higher layer parameter EarlyUL-SyncConfig; 0 bit otherwise. The bit field index 0 of the cell indicator field is mapped to the serving cell, and other bit field indexes are mapped to the candidate cells configured with higher layer parameter EarlyUL-SyncConfig according to an ascending order of a candidate identity configured by ltm-CandidateId, with the bit field index 1 mapped to the candidate cell with the smallest candidate identity.  log2C+1

-PRACH association indicator - 0 or 1 bit

-1bit if the UE is provided with tag2-Id, and the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for the first CORESETs, and is provided coresetPoolIndex with value 1 for the second CORESETs. This field is reserved if the cell indicated by Cell indicator field is a candidate cell.

-This field indicates the PCI associated with the PRACH transmission if the UE is provided SSB-MTC-AddtionalPCI. The bit field index 0 of this field is mapped to the PCI of the serving cell, and the bit field index 1 of this field is mapped to the additional PCI associated with active TCI states.

-This field indicates the PL-RS for the PRACH transmission if the UE is not provided SSB-MTC-AddtionalPCI. The bit field index 0 of this field is mapped to the DL RS that the DM-RS of the PDCCH order is quasi-collocated with, and the bit field index 1 of this field is mapped to the SS/PBCH indicated by the SS/PBCH index field in this DCI format.

-1bit if the UE is provided with tag2-Id and SSB-MTC-AddtionalPCI, and the UE is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided, and the UE is provided with PrachAssociationIndicator_InDCI_format_1_0, and the UE is not provided with pl-Offset for any TCI-State in dl-OrJointTCI-StateList or any TCI-UL-State in ul-TCI-State-List. This field is reserved if the cell indicated by Cell indicator field is a candidate cell.

-This field indicates the PCI and the PL-RS for the PRACH transmission. The bit field index 0 of this field is mapped to the PCI of the serving cell and the DL RS that the DM-RS of the PDCCH order is quasi-collocated with, and the bit field index 1 of this field is mapped to the additional PCI associated with active TCI states and the SS/PBCH indicated by the SS/PBCH index field in this DCI format.

-0 bit otherwise.

-PRACH retransmission indicator - 0 or 1 bit

-1bit if the UE is configured with higher layer parameter EarlyUL-SyncConfig. This field indicates initial transmission or retransmission of PRACH according to Table 7.3.1.2.1-3 if the cell indicated by Cell indicator field is a candidate cell, and this field is reserved if the value of Cell indicator field is zero.

-0 bit otherwise.

-Pathloss offset indicator – 0 or 1 bit

-1 bit if the UE is configured with higher layer parameter plOffsetInPrach_InDCI and at least one configured TCI state for the serving cell is configured with plOffset.

-If there is only one indicated joint/UL TCI state, the bit field index 0 of this field indicates that no pathloss offset is applied for the PRACH transmission, and the bit field index 1 of this field indicates that the pathloss offset configured in the indicated joint/UL TCI state is applied for the PRACH transmission.

-If there are two indicated joint/UL TCI states, the bit field index 0 of this field indicates that the pathloss offset configured in the first indicated joint/UL TCI state is applied for the PRACH transmission, and the bit field index 1 of this field indicates that the pathloss offset configured in the second indicated joint/UL TCI state is applied for the PRACH transmission.

-0 bit otherwise.

-PRACH resource indicator - 0 or 1 bit

-1 bit if the UE is configured with higher layer parameter rach-Config-Adapt. This field indicates the availability of the PRACH resource configured by rach-Config-Adapt according to Table 7.3.1.2.1-5.

-0 bit otherwise.

-RACH occasion indicator - 0 or 1 bit

-1 bit if the UE is configured with higher layer parameter sbfd-RACHSingleConfig or sbfd-RACHDualConfig. If the value of the "Random Access Preamble index" is not all zeros, this field indicates the RACH occasion for PRACH transmission according to Table 7.3.1.2.1-6; otherwise, this field is reserved.

-0 bit otherwise.

-Reserved bits - a number of bits as determined by the following:

-(12 -  -  -  -  - ) bits for operation in a cell with shared spectrum channel access in frequency range 1 or when the DCI format is monitored in common search space for operation in a cell in frequency range 2-2; Y1Y2Y3Y4Y5

-(10 -  -  -  -  - ) bits otherwise;Y1Y2Y3Y4Y5

where,

- if the UE is not configured with higher layer parameter EarlyUL-SyncConfig; +1 otherwise.Y1=0Y1=log2C+1

- if the "PRACH association indicator" field is not present in this DCI format;  otherwise.Y2=0Y2=1

- if the "Pathloss offset indicator" field is not present in this DCI format;  otherwise.Y3=0Y3=1

- if the "PRACH resource indicator" field is not present in this DCI format;  otherwise.Y4=0Y4=1

- if the "RACH occasion indicator " field is not present in this DCI format;  otherwise.Y5=0Y5=1

Otherwise, all remaining fields are set as follows:

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS 38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits

-Downlink assignment index - 2 bits as defined in Clause 9.1.3 of [5, TS 38.213], as counter DAI

-TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213]

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]

-PDSCH-to-HARQ_feedback timing indicator - 3 bits as defined in Clause 9.2.3 of [5, TS38.213]

-ChannelAccess-CPext - 2 bits indicating combinations of channel access type and CP extension as defined in Table 7.3.1.1.1-4, or Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1; 2 bits indicating channel access type as defined in Table 7.3.1.1.1-4B if ChannelAccessMode2-r17 is provided for operation in a cell in frequency range 2-2; 0 bits otherwise

-Reserved bits - 2 bits when the DCI format is monitored in common search space for operation in a cell in frequency range 2-2 and the number of bits for the field of 'ChannelAccess-CPext' is 0; 0 bits otherwise

The following information is transmitted by means of the DCI format 1_0 with CRC scrambled by P-RNTI:

-Short Messages Indicator - 2 bits according to Table 7.3.1.2.1-1. If rach-Config-Adapt is configured and this field is set to "00", all the remaining fields are reserved except the "Short Messages" field.

-Short Messages - 8 bits, according to Clause 6.5 of [9, TS38.331]. If only the scheduling information for Paging, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, all the bits in this bit field are reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "00" or "01", all the bits in this bit field are reserved, except the bit indicating the availability of the PRACH resource configured by rach-Config-Adapt according to Clause 6.5 of [9, TS38.331].

-Frequency domain resource assignment - bits. If only the short message, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, this bit field is reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "10", this bit field is reserved.

- is the size of CORESET 0

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]. If only the short message, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, this bit field is reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "10", this bit field is reserved.

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5. If only the short message, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, this bit field is reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "10", this bit field is reserved.

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS38.214], using Table 5.1.3.1-1. If only the short message, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, this bit field is reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "10", this bit field is reserved.

-TB scaling - 2 bits as defined in Clause 5.1.3.2 of [6, TS38.214]. If only the short message, and TRS availability indication if trs-ResourceSetConfig or trs-ResourceSetConfig-r18 is configured, are carried, this bit field is reserved. If rach-Config-Adapt is configured and the "Short Messages Indicator" field is set to "10", this bit field is reserved.

-TRS availability indication - 1, 2, 3, 4, 5, or 6 bits, where the number of bits is equal to one plus the highest value of all the indBitID(s) provided by the trs-ResourceSetConfig if configured or the number of bits is equal to one plus the highest value of all the indBitID-r18(s) provided by the trs-ResourceSetConfig-r18 if configured; 0 bits otherwise.

-Reserved bits - (8 - M) bits for operation in a cell with shared spectrum channel access in frequency range 1 or for operation in a cell in frequency range 2-2; (6 - M) bits for operation in a cell without shared spectrum channel access, where the value of M is the number of bits for the field of 'TRS availability indication' as defined above.

The following information is transmitted by means of the DCI format 1_0 with CRC scrambled by SI-RNTI:

-Frequency domain resource assignment - bits

- is the size of CORESET 0

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS38.214], using Table 5.1.3.1-1

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-System information indicator - 1 bit as defined in Table 7.3.1.2.1-2

-Reserved bits -  17 bits for operation in a cell with shared spectrum channel access in frequency range 1 or for operation in a cell in frequency range 2-2; otherwise 15 bits

The following information is transmitted by means of the DCI format 1_0 with CRC scrambled by RA-RNTI or MsgB-RNTI:

-Frequency domain resource assignment - bits

- is the size of CORESET 0 if CORESET 0 is configured for the cell and  is the size of initial DL bandwidth part if CORESET 0 is not configured for the cell

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS38.214], using Table 5.1.3.1-1

-TB scaling - 2 bits as defined in Clause 5.1.3.2 of [6, TS38.214]

-LSBs of SFN - 2 bits for the DCI format 1_0 with CRC scrambled by MsgB-RNTI as defined in Clause 8.2A of [5, TS 38.213] if msgB-responseWindow is configured to be larger than 10 ms; or 2 bits for the DCI format 1_0 with CRC scrambled by RA-RNTI as defined in Clause 8.2 of [5, TS 38.213] for operation in a cell with shared spectrum channel access if ra-ResponseWindow or ra-ResponseWindow-v1610 is configured to be larger than 10 ms; 0 bit otherwise

-Reserved bits - (16 - A) bits for operation in a cell without shared spectrum access in frequency range 1 and frequency range 2-1, (18 - A) for operation in a cell with shared spectrum access in frequency range 1 or for operation in a cell in frequency range 2-2, where the value of A is the number of bits for the field of 'LSBs of SFN' as defined above

The following information is transmitted by means of the DCI format 1_0 with CRC scrambled by TC-RNTI:

-Identifier for DCI formats - 1 bit

-The value of this bit field is always set to 1, indicating a DL DCI format

-Frequency domain resource assignment - bits

- is the size of CORESET 0

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits

-If the UE indicates the support of repetition of PDSCH scheduled by DCI format 1_0 with CRC scrambled by TC-RNTI, 5 bits as defined in Clause 5.1.2.1 and Clause 5.1.3.1 of [6, TS38.214];

-otherwise 5 bits as defined in Clause 5.1.3 of [6, TS38.214], using Table 5.1.3.1-1.

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits

-Downlink assignment index - 2 bits

-2 bits indicating the number of repetitions for PUCCH as defined in clause 9.2.6 of [5, TS38.213] according to Table 7.3.1.2.1-4, if the higher layer parameter numberOfMsg4HARQ-ACK-Repetitions is configured with at least two repetition factors and the UE has indicated capability of PUCCH repetition on common PUCCH resource [8, TS38.321];

-otherwise, reserved.

-TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS38.213]

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS38.213]

-PDSCH-to-HARQ_feedback timing indicator - 3 bits as defined in Clause 9.2.3 of [5, TS38.213]

-ChannelAccess-CPext - 2 bits indicating combinations of channel access type and CP extension as defined in Table 7.3.1.1.1-4, or Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1; 2 bits indicating channel access type as defined in Table 7.3.1.1.1-4B if ChannelAccessMode2-r17 is provided for operation in a cell in frequency range 2-2; otherwise 0 bit

-Reserved bits - 2 bits when the DCI format is monitored in common search space for operation in a cell in frequency range 2-2 and the number of bits for the field of 'ChannelAccess-CPext' is 0; 0 bits otherwise

Table 7.3.1.2.1-1: Short Message indicator

Table 7.3.1.2.1-2: System information indicator

Table 7.3.1.2.1-3: PRACH retransmission indicator

Table 7.3.1.2.1-4: Number of repetitions  as a function of 2 bits of Downlink assignment index fieldNPUCCHrepeat

Table 7.3.1.2.1-5: PRACH resource indicator

Table 7.3.1.2.1-6: RACH occasion indicator

## 7.3.1.2.2Format 1_1

DCI format 1_1 is used for the scheduling of one or multiple PDSCH in one cell.

The following information is transmitted by means of the DCI format 1_1 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bits

-The value of this bit field is always set to 1, indicating a DL DCI format

-Carrier indicator - 0 or 3 bits as defined in Clause 10.1 of [5, TS 38.213]. This field is reserved when this format is carried by PDCCH on the primary cell and the UE is configured for scheduling on the primary cell from an SCell, with the same number of bits as that in this format carried by PDCCH on the SCell for scheduling on the primary cell.

-Bandwidth part indicator - 0, 1 or 2 bits as determined by the number of DL BWPs  configured by higher layers, excluding the initial DL bandwidth part. The bitwidth for this field is determined as bits, where

- if , in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;

If a UE does not support active BWP change via DCI, the UE ignores this bit field.

-Frequency domain resource assignment - number of bits determined by the following, where  is the size of the active DL bandwidth part:

- bits if only resource allocation type 0 is configured, where  is defined in Clause 5.1.2.2.1 of [6, TS38.214],

-bits if only resource allocation type 1 is configured, or

- bits if resourceAllocation is configured as 'dynamicSwitch'.

-If resourceAllocation is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the LSBs provide the resource allocation as defined in Clause 5.1.2.2.1 of [6, TS 38.214].

-For resource allocation type 1, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.2 of [6, TS 38.214]

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocation is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

-Time domain resource assignment - 0, 1, 2, 3, 4, 5 or 6 bits

-If the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH is not configured and if the higher layer parameter pdsch-TimeDomainAllocationList is configured, 0, 1, 2, 3 or 4 bits as defined in Clause 5.1.2.1 of [6, TS 38.214]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter pdsch-TimeDomainAllocationList if the higher layer parameter is configured;

-if the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH is configured, 0, 1, 2, 3, 4, 5 or 6 bits as defined in Clause 5.1.2.1 of [6, TS38.214]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH;log2(I)

-otherwise I is the number of entries in the default table.

-VRB-to-PRB mapping - 0 or 1 bit:

-0 bit if only resource allocation type 0 is configured or if interleaved VRB-to-PRB mapping is not configured by high layers;

-1 bit according to Table 7.3.1.2.2-5 otherwise, only applicable to resource allocation type 1, as defined in Clause 7.3.1.6  of [4, TS 38.211].

-PRB bundling size indicator - 0 bit if the higher layer parameter prb-BundlingType is not configured or is set to 'staticBundling', or 1 bit if the higher layer parameter prb-BundlingType is set to 'dynamicBundling' according to Clause 5.1.2.3 of [6, TS 38.214].

-Rate matching indicator - 0, 1, or 2 bits according to higher layer parameters rateMatchPatternGroup1 and rateMatchPatternGroup2, where the MSB is used to indicate rateMatchPatternGroup1 and the LSB is used to indicate rateMatchPatternGroup2 when there are two groups.

-ZP CSI-RS trigger - 0, 1, or 2 bits as defined in Clause 5.1.4.2 of [6, TS 38.214]. The bitwidth for this field is determined as bits, where  is the number of aperiodic ZP CSI-RS resource sets configured by higher layer.

For transport block 1:

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3.1 of [6, TS 38.214]

-New data indicator - 1 bit if the number of scheduled PDSCH indicated by the Time domain resource assignment field is 1; otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined based on the maximum number of schedulable PDSCH among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH, where each bit corresponds to one scheduled PDSCH as defined in clause 5.1.3 in [6, TS 38.214].

-Redundancy version - number of bits determined by the following:

-2 bits as defined in Table 7.3.1.1.1-2 if the number of scheduled PDSCH indicated by the Time domain resource assignment field is 1;

-otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined by the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH, where each bit corresponds to one scheduled PDSCH as defined in clause 5.1.3 in [6, TS 38.214] and redundancy version is determined according to Table 7.3.1.1.2-34.

For transport block 2 (only present if maxNrofCodeWordsScheduledByDCI equals 2):

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3.1 of [6, TS 38.214]

-New data indicator - 1 bit if the number of scheduled PDSCH indicated by the Time domain resource assignment field is 1; otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined based on the maximum number of schedulable PDSCH among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH, where each bit corresponds to one scheduled PDSCH as defined in clause 5.1.3 in [6, TS 38.214].

-Redundancy version - number of bits determined by the following:

-2 bits as defined in Table 7.3.1.1.1-2 if the number of scheduled PDSCH indicated by the Time domain resource assignment field is 1;

-otherwise 2, 3, 4, 5, 6, 7 or 8 bits determined by the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH, where each bit corresponds to one scheduled PDSCH as defined in clause 5.1.3 in [6, TS 38.214] and redundancy version is determined according to Table 7.3.1.1.2-34.

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and the value of maxNrofCodeWordsScheduledByDCI for the indicated bandwidth part equals 2 and the value of maxNrofCodeWordsScheduledByDCI for the active bandwidth part equals 1, the UE assumes zeros are padded when interpreting the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields of transport block 2 according to Clause 12 of [5, TS38.213], and the UE ignores the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields of transport block 2 for the indicated bandwidth part.

-HARQ process number - 5 bits if higher layer parameter harq-ProcessNumberSizeDCI-1-1 or harq-ProcessNumberSizeDCI-1-1-Ext is configured; otherwise 4 bits

-Downlink assignment index - number of bits as defined in the following

-6 bits if more than one serving cell are configured in the DL and the higher layer parameter nfi-TotalDAI-Included is configured. The 4 MSB bits are the counter DAI and the total DAI for the scheduled PDSCH group, and the 2 LSB bits are the total DAI for the non-scheduled PDSCH group.

-4 bits if only one serving cell is configured in the DL and the higher layer parameter nfi-TotalDAI-Included is configured. The 2 MSB bits are the counter DAI for the scheduled PDSCH group, and the 2 LSB bits are the total DAI for the non-scheduled PDSCH group;

-4 bits if more than one serving cell are configured in the DL, the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic or pdsch-HARQ-ACK-Codebook-r16= enhancedDynamic, and nfi-TotalDAI-Included is not configured, where the 2 MSB bits are the counter DAI and the 2 LSB bits are the total DAI;

-4 bits if one serving cell is configured in the DL, and the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic, and the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for one or more first CORESETs and is provided coresetPoolIndex with value 1 for one or more second CORESETs, and is provided ackNackFeedbackMode = joint, where the 2 MSB bits are the counter DAI and the 2 LSB bits are the total DAI;

-2 bits if only one serving cell is configured in the DL, the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic or pdsch-HARQ-ACK-Codebook-r16=enhancedDynamic, and nfi-TotalDAI-Included is not configured, when the UE is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided or the UE is not configured with ackNackFeedbackMode = joint, where the 2 bits are the counter DAI;

-0 bits otherwise.

If the UE is configured with a PUCCH-SCell, the number of serving cells is determined within a PUCCH group.

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-Codebook is replaced by pdsch-HARQ-ACK-Codebook-secondaryPUCCHgroup-r16 if present for the secondary PUCCH group.

If higher layer parameter priorityIndicatorDCI-1-1 is configured, if the bit width of the Downlink assignment index in DCI format 1_1 for one HARQ-ACK codebook is not equal to that of the Downlink assignment index in DCI format 1_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller Downlink assignment index until the bit width of the Downlink assignment index in DCI format 1_1 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213]

-Second TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213] if higher layer parameter SecondTPCFieldDCI-1-1 is configured; 0 bit otherwise.

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]

-PDSCH-to-HARQ_feedback timing indicator - 0, 1, 2, or 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter dl-DataToUL-ACK.

If higher layer parameter priorityIndicatorDCI-1-1 is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 for one HARQ-ACK codebook is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 for the other HARQ-ACK codebook on the same cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 for the two HARQ-ACK codebooks are the same.

If higher layer parameter pucch-sSCellDyn is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 associated with one cell for PUCCH transmission is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 associated with the other cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_1 associated with the two cells are the same.

If the UE is configured with a PUCCH-SCell, pucch-sSCellDyn is replaced by pucch-sSCellDynSecondaryPUCCHgroup for the secondary PUCCH group.

-One-shot HARQ-ACK request - 0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-OneShotFeedback-r16 or pdsch-HARQ-ACK-EnhType3ToAddModList is configured;

-0 bit otherwise.

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-EnhType3ToAddModList is replaced by pdsch-HARQ-ACK-EnhType3SecondaryToAddModList for the secondary PUCCH group.

-Enhanced Type 3 codebook indicator - 0, 1, 2, or 3 bits.

-0 bit if pdsch-HARQ-ACK-EnhType3DCI-Field is not configured;

- bits otherwise, where  is the number of entries in the higher layer parameter pdsch-HARQ-ACK-EnhType3ToAddModList.log2(nCB)nCB

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-EnhType3DCI-Field is replaced by pdsch-HARQ-ACK-EnhType3DCI-FieldSecondaryPUCCHgroup for the secondary PUCCH group, and pdsch-HARQ-ACK-EnhType3ToAddModList is replaced by pdsch-HARQ-ACK-EnhType3SecondaryList for the secondary PUCCH group.

-PDSCH group index - 0 or 1 bit.

-1 bit if the higher layer parameter pdsch-HARQ-ACK-Codebook-r16= enhancedDynamic;

-0 bit otherwise.

-New feedback indicator - 0, 1 or 2 bits.

-1 bit if the higher layer parameter pdsch-HARQ-ACK-Codebook-r16= enhancedDynamic and the higher layer parameter nfi-TotalDAI-Included is not configured;

-2 bits if the higher layer parameter pdsch-HARQ-ACK-Codebook-r16= enhancedDynamic and the higher layer parameter nfi-TotalDAI-Included=true; the MSB corresponds to the scheduled PDSCH group, and the LSB corresponds to the non-scheduled PDSCH group, as defined in [TS38.213] clause 9.1.3.3

-0 bit otherwise.

-Number of requested PDSCH group(s) - 0 or 1 bit.

-1 bit if the higher layer parameter pdsch-HARQ-ACK-Codebook-r16= enhancedDynamic;

-0 bit otherwise.

-HARQ-ACK retransmission indicator - 0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-Retx is configured.

-0 bit otherwise.

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-Retx is replaced by pdsch-HARQ-ACK-RetxSecondaryPUCCHgroup for the secondary PUCCH group.

-Antenna port(s) - 4, 5, 6, 7 or 8 bits as defined by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 and Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A, where the number of CDM groups without data of values 1, 2, and 3 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively. The antenna ports  shall be determined according to the ordering of DMRS port(s) given by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 or Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A. When a UE not configured with dl-OrJointTCI-StateList receives an activation command that maps at least one codepoint of DCI field 'Transmission Configuration Indication' to two TCI states, or when a UE configured with dl-OrJointTCI-StateList is having two indicated TCI states, the UE shall use Table 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A; otherwise, it shall use Tables 7.3.1.2.2-1/2/3/4/7/8/9/10. The UE can receive an entry with DMRS ports equals to 1000, 1002, 1003 when two the UE is not configured with dl-OrJointTCI-StateList and TCI states are indicated in a codepoint of DCI field 'Transmission Configuration Indication', or when the UE configured with dl-OrJointTCI-StateList is having two indicated TCI states to be applied to PDSCH.

If a UE is configured with both dmrs-DownlinkForPDSCH-MappingTypeA and dmrs-DownlinkForPDSCH-MappingTypeB, the bitwidth of this field equals , where  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeA and  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeB. A number of  zeros are padded in the MSB of this field, if the mapping type of the PDSCH corresponds to the smaller value of  and .

-Transmission configuration indication - 0 bit if higher layer parameter tci-PresentInDCI is not enabled; otherwise 3 bits as defined in Clause 5.1.5 of [6, TS38.214].

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part,

-if the higher layer parameter tci-PresentInDCI is not enabled for the CORESET used for the PDCCH carrying the DCI format 1_1,

-the UE assumes tci-PresentInDCI is not enabled for all CORESETs in the indicated bandwidth part;

-otherwise,

-the UE assumes tci-PresentInDCI is enabled for all CORESETs in the indicated bandwidth part.

-TCI selection - 0 bit if higher layer parameter tci-SelectionPresentInDCI is not configured; otherwise 2 bits according to Table 7.3.1.2.2-11.

-SRS request - 2 bits as defined by Table 7.3.1.1.2-24 for UEs not configured with supplementaryUplink in ServingCellConfig in the cell; 3 bits for UEs configured with supplementaryUplink in ServingCellConfig in the cell where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24. This bit field may also indicate the associated CSI-RS according to Clause 6.1.1.2 of [6, TS 38.214].

-SRS offset indicator - 0, 1 or 2 bits.

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell  and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214],  where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-CBG transmission information (CBGTI) - 0 bit if higher layer parameter PDSCH-CodeBlockGroupTransmission for PDSCH is not configured, otherwise, 2, 4, 6, or 8 bits as defined in Clause 5.1.7 of [6, TS38.214], determined by the higher layer parameters maxCodeBlockGroupsPerTransportBlock and maxNrofCodeWordsScheduledByDCI for the PDSCH.

If higher layer parameter priorityIndicatorDCI-1-1 is configured, if the bit width of the CBG transmission information in DCI format 1_1 for one HARQ-ACK codebook is not equal to that of the CBG transmission information in DCI format 1_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller CBG transmission information until the bit width of the CBG transmission information in DCI format 1_1 for the two HARQ-ACK codebooks are the same.

-CBG flushing out information (CBGFI) - 1 bit if higher layer parameter codeBlockGroupFlushIndicator is configured as "TRUE", 0 bit otherwise.

If higher layer parameter priorityIndicatorDCI-1-1 is configured, if the bit width of the CBG flushing out information in DCI format 1_1 for one HARQ-ACK codebook is not equal to that of the CBG flushing out information in DCI format 1_1 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller CBG flushing out information until the bit width of the CBG flushing out information in DCI format 1_1 for the two HARQ-ACK codebooks are the same.

-DMRS sequence initialization - 1 bit.

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-1-1 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-ChannelAccess-CPext - 0, 1, 2, 3 or 4 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-1-1 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.2.2-6 or Table 7.3.1.2.2-6A are configured by the higher layer parameter ul-AccessConfigListDCI-1-1.log2(I)

-Minimum applicable scheduling offset indicator - 0 or 1 bit

-0 bit if higher layer parameter minimumSchedulingOffsetK0 is not configured;

-1 bit if higher layer parameter minimumSchedulingOffsetK0 is configured. The 1 bit indication is used to determine the minimum applicable K0 for the active DL BWP and the minimum applicable K2 value for the active UL BWP, if configured respectively, according to Table 7.3.1.1.2-33. If the minimum applicable K0 is indicated, the minimum applicable value of the aperiodic CSI-RS triggering offset for an active DL BWP shall be the same as the minimum applicable K0 value.

-SCell dormancy indication - 0 bit if higher layer parameter dormancyGroupWithinActiveTime is not configured; otherwise 1, 2, 3, 4 or 5 bits bitmap determined according to the number of different DormancyGroupID(s) provided by higher layer parameter dormancyGroupWithinActiveTime, where each bit corresponds to one of the SCell group(s) configured by higher layers parameter dormancyGroupWithinActiveTime, with MSB to LSB of the bitmap corresponding to the first to last configured SCell group in ascending order of DormancyGroupID. The field is only present when this format is carried by PDCCH on the primary cell within DRX Active Time and the UE is configured with at least two DL BWPs for an SCell.

If one-shot HARQ-ACK request is not present or set to '0', and all bits of frequency domain resource assignment are set to 0 for resource allocation type 0 or set to 1 for resource allocation type 1 or set to 0 or 1 for dynamic switch resource allocation type, this field is reserved and the following fields among the fields above are used for SCell dormancy indication, where each bit corresponds to one of the configured SCell(s), with MSB to LSB of the following fields concatenated in the order below corresponding to the SCell with lowest to highest SCell index

-Modulation and coding scheme of transport block 1

-New data indicator of transport block 1

-Redundancy version of transport block 1

-HARQ process number

-Antenna port(s)

-DMRS sequence initialization

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-0 bit, otherwise

-PUCCH Cell indicator - 0 or 1 bit.

-1 bit if higher layer parameter pucch-sSCellDyn is configured.

-0 bit otherwise.

If the UE is configured with a PUCCH-SCell, pucch-sSCellDyn is replaced by pucch-sSCellDynSecondaryPUCCHgroup for the secondary PUCCH group.

-Co-scheduled UE information – 0 or 3 bits

-3 bits as defined in Table 7.3.1.2.2-12 if higher layer parameter advReceiver-MU-MIMO-DCI-1-1 is configured. This field is reserved if two codewords are scheduled by this DCI format 1_1.

-0 bit otherwise.

-TPC command for SRS – 2 bits as defined in Clause 7.3.1 of [5, TS 38.213] if higher layer parameter tpcOfSrsClosedLoopIndex_InDCI_format_1_1 is configured; 0 bit otherwise.

-Closed loop indicator for SRS – 1 bit if higher layer parameter srsClosedLoopIndexIndicator_InDCI_format_1_1 and higher layer parameter enableTwoSeparatePowerControlAdjustmentStatesForSRS are both configured; 0 bit otherwise.

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-1-1 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

If DCI formats 1_1 are monitored in multiple search spaces associated with multiple CORESETs in a BWP for scheduling the same serving cell, zeros shall be appended until the payload size of the DCI formats 1_1 monitored in the multiple search spaces equal to the maximum payload size of the DCI format 1_1 monitored in the multiple search spaces.

If the number of information bits in DCI format 1_1 scheduling a single PDSCH prior to padding is not equal to the number of information bits in DCI format 1_1 scheduling multiple PDSCHs for the same serving cell, zeros shall be appended to the DCI format 1_1 with smaller size until the payload size is the same for scheduling a single PDSCH and multiple PDSCHs.

For a UE configured with scheduling on the primary cell from an SCell, if prior to padding the number of information bits in DCI format 1_1 carried by PDCCH on the primary cell is not equal to the number of information bits in DCI format 1_1 carried by PDCCH on the SCell for scheduling on the primary cell, zeros shall be appended to the DCI format 1_1 with smaller size until the payload size is the same:

-If application of step 4C in clause 7.3.1.0 results in additional zero padding for DCI format 1_1 for scheduling on the primary cell, corresponding zeros shall be appended to both DCI format 1_1 monitored on the primary cell and DCI format 1_1 monitored on the SCell for scheduling on the primary cell.

-If the SCell is deactivated and firstActiveDownlinkBWP-Id is not set to dormant BWP, the UE determines the number of information bits in DCI format 1_1 carried by PDCCH on the primary cell based on a DL BWP provided by firstActiveDownlinkBWP-Id for the SCell. If the active DL BWP of the SCell is a dormant DL BWP, or if the SCell is deactivated and firstActiveDownlinkBWP-Id is set to dormant BWP, the UE determines the number of information bits in DCI format 1_1 carried by PDCCH on the primary cell based on a DL BWP provided by firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a DL BWP provided by firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.2.2-1: Antenna port(s) (1000 + DMRS port), dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=1

Table 7.3.1.2.2-1A: Antenna port(s) (1000 + DMRS port), dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=1

Table 7.3.1.2.2-2: Antenna port(s) (1000 + DMRS port), dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=2

Table 7.3.1.2.2-2A: Antenna port(s) (1000 + DMRS port), dmrs-Type=1, dmrs-TypeEnh is not configured, maxLength=2

Table 7.3.1.2.2-3: Antenna port(s) (1000 + DMRS port), dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=1

Table 7.3.1.2.2-3A: Antenna port(s) (1000 + DMRS port), dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=1

Table 7.3.1.2.2-4: Antenna port(s) (1000 + DMRS port), dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=2

Table 7.3.1.2.2-4A: Antenna port(s) (1000 + DMRS port), dmrs-Type=2, dmrs-TypeEnh is not configured, maxLength=2

Table 7.3.1.2.2-5: VRB-to-PRB mapping

Table 7.3.1.2.2-6: Allowed entries for DCI format 1_1/1_3 and DCI format 1_2, configured by higher layer parameter ul-AccessConfigListDCI-1-1 and ul-AccessConfigListDCI-1-2, respectively, in frequency range 1

Table 7.3.1.2.2-6A: Allowed entries for DCI format 1_1, DCI format 1_2 and DCI format 1_3, configured by higher layer parameter ul-AccessConfigListDCI-1-1 in frequency range 2-2

Table 7.3.1.2.2-7: Antenna port(s) (1000 + DMRS port), dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1

Table 7.3.1.2.2-7A: Antenna port(s) (1000 + DMRS port), dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=1

Table 7.3.1.2.2-8: Antenna port(s) (1000 + DMRS port), dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2

Table 7.3.1.2.2-8A: Antenna port(s) (1000 + DMRS port), dmrs-Type=1,dmrs-TypeEnh is configured, maxLength=2

Table 7.3.1.2.2-9: Antenna port(s) (1000 + DMRS port), dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1

Table 7.3.1.2.2-9A: Antenna port(s) (1000 + DMRS port), dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=1

Table 7.3.1.2.2-10: Antenna port(s) (1000 + DMRS port), dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2

Table 7.3.1.2.2-10A: Antenna port(s) (1000 + DMRS port), dmrs-Type=2,dmrs-TypeEnh is configured, maxLength=2

Table 7.3.1.2.2-11: TCI selection

Table 7.3.1.2.2-12: Co-scheduled UE information

## 7.3.1.2.3Format 1_2

DCI format 1_2 is used for the scheduling of PDSCH in one cell.

The following information is transmitted by means of the DCI format 1_2 with CRC scrambled by C-RNTI or CS-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bits

-The value of this bit field is always set to 1, indicating a DL DCI format.

-Carrier indicator - 0, 1, 2 or 3 bits determined by higher layer parameter carrierIndicatorSizeDCI-1-2, as defined in Clause 10.1 of [5, TS38.213]. This field is reserved when this format is carried by PDCCH on the primary cell and the UE is configured for scheduling on the primary cell from an SCell, with the same number of bits as that in this format carried by PDCCH on the SCell for scheduling on the primary cell.

-Bandwidth part indicator - 0, 1 or 2 bits as determined by the number of DL BWPs  configured by higher layers, excluding the initial DL bandwidth part. The bitwidth for this field is determined as  bits, where nBWP, RRClog2(nBWP)

-if , in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;nBWP=nBWP, RRC+1 nBWP, RRC≤3

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;nBWP=nBWP, RRC

If a UE does not support active BWP change via DCI, the UE ignores this bit field.

-Frequency domain resource assignment - number of bits determined by the following:

- bits if only resource allocation type 0 is configured, where  is defined in Clause 5.1.2.2.1 of [6, TS 38.214];NRBGNRBG

- bits if only resource allocation type 1 is configured, or  bits if resourceAllocationDCI-1-2-r16 is configured as 'dynamicSwitch', where , is the size of the active DL bandwidth part, is defined as in clause 4.4.4.4 of [4, TS 38.211] and  is determined by higher layer parameter resourceAllocationType1GranularityDCI-1-2. If the higher layer parameter resourceAllocationType1GranularityDCI-1-2 is not configured,  is equal to 1.log2NRBG, K2NRBG, K2+1/2max log2NRBG, K2NRBG, K2+1/2, NRBG+1NRBG, K2=NRBDL, BWP+NDL, BWPstartmodK2/K2NRBDL, BWP NDL, BWPstart K2K2

-If resourceAllocationDCI-1-2-r16 is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.1 of [6, TS 38.214].NRBG

-For resource allocation type 1, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.2 of [6, TS 38.214]log2NRBG, K2NRBG, K2+1/2

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocationDCI-1-2-r16 is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

-Time domain resource assignment - 0, 1, 2, 3, or 4 bits as defined in Clause 5.1.2.1 of [6, TS 38.214]. The bitwidth for this field is determined as bits, where I is the number of entries in the higher layer parameter pdsch-TimeDomainAllocationListDCI-1-2 if the higher layer parameter is configured, or I is the number of entries in the higher layer parameter pdsch-TimeDomainAllocationList if the higher layer parameter pdsch-TimeDomainAllocationList is configured when the higher layer parameter pdsch-TimeDomainAllocationListDCI-1-2 is not configured; otherwise I is the number of entries in the default table.log2(I)

-VRB-to-PRB mapping - 0 or 1 bit:

-0 bit if the higher layer parameter vrb-ToPRB-InterleaverDCI-1-2 is not configured;

-1 bit according to Table 7.3.1.2.2-5 otherwise, only applicable to resource allocation type 1, as defined in Clause 7.3.1.6 of [4, TS 38.211].

-PRB bundling size indicator - 0 bit if the higher layer parameter prb-BundlingTypeDCI-1-2 is not configured or is set to 'static', or 1 bit if the higher layer parameter prb-BundlingTypeDCI-1-2 is set to 'dynamic' according to Clause 5.1.2.3 of [6, TS 38.214].

-Rate matching indicator - 0, 1, or 2 bits according to higher layer parameters rateMatchPatternGroup1DCI-1-2 and rateMatchPatternGroup2DCI-1-2, where the MSB is used to indicate rateMatchPatternGroup1DCI-1-2 and the LSB is used to indicate rateMatchPatternGroup2DCI-1-2 when there are two groups.

-ZP CSI-RS trigger - 0, 1, or 2 bits as defined in Clause 5.1.4.2 of [6, TS 38.214]. The bitwidth for this field is determined as  bits, where  is the number of aperiodic ZP CSI-RS resource sets configured by higher layer parameter aperiodicZP-CSI-RS-ResourceSetsToAddModListDCI-1-2.log2(nZP+1)nZP

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-1-2

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-HARQ process number - number of bits determined by the following:

-0, 1, 2, 3, 4 or 5 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-1-2-v1700 or harq-ProcessNumberSizeDCI-1-2-Ext if configured;

-otherwise 0, 1, 2, 3 or 4 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-1-2.

-Downlink assignment index - 0, 1, 2 or 4 bits

-0 bit if the higher layer parameter downlinkAssignmentIndexDCI-1-2 is not configured;

-1, 2 or 4 bits determined by higher layer parameter downlinkAssignmentIndexDCI-1-2 otherwise,

-4 bits if more than one serving cell are configured in the DL and the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic, where the 2 MSB bits are the counter DAI and the 2 LSB bits are the total DAI

-4 bits if only one serving cell is configured in the DL and the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic, and the UE is not provided coresetPoolIndex or is provided coresetPoolIndex with value 0 for one or more first CORESETs and is provided coresetPoolIndex with value 1 for one or more second CORESETs, and is provided ackNackFeedbackMode = joint, where the 2 MSB bits are the counter DAI and the 2 LSB bits are the total DAI.

-1 or 2 bits if only one serving cell is configured in the DL and the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic, when the UE is not configured with coresetPoolIndex or the value of coresetPoolIndex is the same for all CORESETs if coresetPoolIndex is provided or the UE is not configured with ackNackFeedbackMode = joint, where the 1 bit or 2 bits are the counter DAI.

If the UE is configured with a PUCCH-SCell, the number of serving cells is determined within a PUCCH group.

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-Codebook is replaced by pdsch-HARQ-ACK-Codebook-secondaryPUCCHgroup-r16 if present for the secondary PUCCH group.

If higher layer parameter priorityIndicatorDCI-1-2 is configured, if the bit width of the Downlink assignment index in DCI format 1_2 for one HARQ-ACK codebook is not equal to that of the Downlink assignment index in DCI format 1_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller Downlink assignment index until the bit width of the Downlink assignment index in DCI format 1_2 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213]

-Second TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213] if higher layer parameter SecondTPCFieldDCI-1-2 is configured; 0 bit otherwise.

-PUCCH resource indicator - 0 or 1 or 2 or 3 bits determined by higher layer parameter numberOfBitsForPUCCH-ResourceIndicatorDCI-1-2

If higher layer parameter pucch-sSCellPattern or pucch-sSCellDynDCI-1-2 is configured, if the bit width of the PUCCH resource indicator in DCI format 1_2 associated with one cell for PUCCH transmission is not equal to that of the PUCCH resource indicator in DCI format 1_2 associated with the other cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PUCCH resource indicator until the bit width of the PUCCH resource indicator in DCI format 1_2 associated with the two cells for PUCCH transmissions are the same.

If the UE is configured with a PUCCH-SCell, pucch-sSCellPattern is replaced by pucch-sSCellPatternSecondaryPUCCHgroup for the secondary PUCCH group.

-PDSCH-to-HARQ_feedback timing indicator - 0, 1, 2, or 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter DL-DataToUL-ACK-DCI-1-2.log2(I)

If higher layer parameter priorityIndicatorDCI-1-2 is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 for one HARQ-ACK codebook is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 for the other HARQ-ACK codebook on the same cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 for the two HARQ-ACK codebooks are the same.

If higher layer parameter pucch-sSCellDynDCI-1-2 is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 associated with one cell for PUCCH transmission is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 associated with the other cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_2 associated with the two cells are the same.

-One-shot HARQ-ACK request -0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-OneShotFeedbackDCI-1-2 or pdsch-HARQ-ACK-EnhType3DCI-1-2 is configured;

-0 bit otherwise.

-Enhanced Type 3 codebook indicator - 0, 1, 2, or 3 bits.

-0 bit if pdsch-HARQ-ACK-EnhType3DCI-Field-1-2 is not configured;

- bits otherwise, where  is the number of entries in the higher layer parameter pdsch-HARQ-ACK-EnhType3ToAddModList.log2(nCB)nCB

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-EnhType3ToAddModList is replaced by pdsch-HARQ-ACK-EnhType3SecondaryToAddModList for the secondary PUCCH group.

-HARQ-ACK retransmission indicator - 0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-retxDCI-1-2 is configured.

-0 bit otherwise.

-Antenna port(s) - 0, 4, 5, 6, 7 or 8 bits

-0 bit if higher layer parameter antennaPortsFieldPresenceDCI-1-2 is not configured;

-Otherwise 4, 5, 6, 7 or 8 bits as defined by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 and Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A, where the number of CDM groups without data of values 1, 2, and 3 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively. The antenna ports shall be determined according to the ordering of DMRS port(s) given by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 or Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A. When a UE not configured with dl-OrJointTCI-StateList receives an activation command that maps at least one codepoint of DCI field 'Transmission Configuration Indication' to two TCI states, or when a UE configured with dl-OrJointTCI-StateList is having two indicated TCI states, the UE shall use Table 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A; otherwise, it shall use Tables 7.3.1.2.2-1/2/3/4/7/8/9/10.p0,…,pv-1

-If a UE is configured with both dmrs-DownlinkForPDSCH-MappingTypeA-DCI-1-2 and dmrs-DownlinkForPDSCH-MappingTypeB-DCI-1-2 and is configured with higher layer parameter antennaPortsFieldPresenceDCI-1-2, the bitwidth of this field equals, where  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeA-DCI-1-2 and  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeB-DCI-1-2. A number of  zeros are padded in the MSB of this field, if the mapping type of the PDSCH corresponds to the smaller value of  and . maxxA,xBxAxBxA-xBxAxB

If a UE is not configured with higher layer parameter antennaPortsFieldPresenceDCI-1-2, antenna port(s) are defined assuming bit field index value 0 in Tables 7.3.1.2.2-1/2/3/4/7/8/9/10.

-Transmission configuration indication - 0 bit if higher layer parameter tci-PresentDCI-1-2 is not configured; otherwise 1 or 2 or 3 bits determined by higher layer parameter tci-PresentDCI-1-2 as defined in Clause 5.1.5 of [6, TS38.214].

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part,

-if the higher layer parameter tci-PresentDCI-1-2 is not configured for the CORESET used for the PDCCH carrying the DCI format 1_2,

-the UE assumes tci-PresentDCI-1-2 is not configured for all CORESETs in the indicated bandwidth part;

-otherwise,

-the UE assumes tci-PresentDCI-1-2 is configured for all CORESETs in the indicated bandwidth part with the same value configured for the CORESET used for the PDCCH carrying the DCI format 1_2.

-TCI selection - 0 bit if higher layer parameter tci-SelectionPresentInDCI is not configured; otherwise 2 bits according to Table 7.3.1.2.2-11.

-SRS request - 0, 1, 2 or 3 bits

-0 bit if the higher layer parameter srs-RequestDCI-1-2 is not configured;

-1 bit as defined by Table 7.3.1.1.3-1 if the higher layer parameter srs-RequestDCI-1-2 = 1 and for UEs not configured with supplementaryUplink in ServingCellConfig in the cell;

-2 bits if the higher layer parameter srs-RequestDCI-1-2 = 1 and for UEs configured with supplementaryUplink in ServingCellConfig in the cell, where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second bit is defined by Table 7.3.1.1.3-1;

-2 bits as defined by Table 7.3.1.1.2-24 if the higher layer parameter srs-RequestDCI-1-2 = 2 and for UEs not configured with supplementaryUplink in ServingCellConfig in the cell;

-3 bits if the higher layer parameter srs-RequestDCI-1-2 = 2 and for UEs configured with supplementaryUplink in ServingCellConfig in the cell, where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24;

-SRS offset indicator - 0, 1 or 2 bits.

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214],  where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-DMRS sequence initialization - 0 or 1 bit

-0 bit if the higher layer parameter dmrs-SequenceInitializationDCI-1-2 is not configured;

-1 bit otherwise.

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-1-2 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-0 bit, otherwise

-ChannelAccess-CPext - 0, 1, 2, 3 or 4 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-1-2 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or the number of entries in the high layer parameter ul-AccessConfigListDCI-1-1 for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.2.2-6 are configured by the higher layer parameter ul-AccessConfigListDCI-1-2 in frequency range 1. One or more entries from Table 7.3.1.1.2-6A are configured by the higher layer parameter ul-AccessConfigListDCI-1-1 in frequency range 2-2.log2(I)

-PUCCH Cell indicator - 0 or 1 bit.

-1 bit if higher layer parameter pucch-sSCellDynDCI-1-2 is configured.

-0 bit otherwise.

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-1-2 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

If DCI formats 1_2 are monitored in multiple search spaces associated with multiple CORESETs in a BWP for scheduling the same serving cell, zeros shall be appended until the payload size of the DCI formats 1_2 monitored in the multiple search spaces equal to the maximum payload size of the DCI format 1_2 monitored in the multiple search spaces.

For a UE configured with scheduling on the primary cell from an SCell, if prior to padding the number of information bits in DCI format 1_2 carried by PDCCH on the primary cell is not equal to the number of information bits in DCI format 1_2 carried by PDCCH on the SCell for scheduling on the primary cell, zeros shall be appended to the DCI format 1_2 with smaller size until the payload size is the same.

-If application of step 4B in clause 7.3.1.0 results in additional zero padding for DCI format 1_2 for scheduling on the primary cell, corresponding zeros shall be appended to both DCI format 1_2 monitored on the primary cell and DCI format 1_2 monitored on the SCell for scheduling on the primary cell.

-If the SCell is deactivated and firstActiveDownlinkBWP-Id is not set to dormant BWP, the UE determines the number of information bits in DCI format 1_2 carried by PDCCH on the primary cell based on a DL BWP provided by firstActiveDownlinkBWP-Id for the SCell. If the active DL BWP of the SCell is a dormant DL BWP, or if the SCell is deactivated and firstActiveDownlinkBWP-Id is set to dormant BWP, the UE determines the number of information bits in DCI format 1_2 carried by PDCCH on the primary cell based on a DL BWP provided by firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a DL BWP provided by firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.2.3-1: Redundancy version

## 7.3.1.2.4Format 1_3

DCI format 1_3 is used for the scheduling of one or multiple PDSCHs in one cell, or multiple PDSCHs in multiple cells with one or multiple PDSCHs per cell.

The following information is transmitted by means of the DCI format 1_3 with CRC scrambled by C-RNTI or MCS-C-RNTI:

-Identifier for DCI formats - 1 bits

-The value of this bit field is always set to 1, indicating a DL DCI format

-Scheduled cell set indicator -  bits, where  is the number of cell sets which are configured by higher layer parameter mc-DCI-SetofCellsToAddModList to be respectively scheduled by DCI format 0_3/1_3 from the cell on which this format is carried by PDCCH. If present, this field is used to indicate the scheduled cell set according to Table 7.3.1.1.4-1; otherwise, the scheduled cell set is the cell set configured to be scheduled by DCI format 0_3/1_3 from the cell by higher layer parameter mc-DCI-SetofCellsToAddModList. log2Nset Nset

-Scheduled cells indicator - number of bits determined by the following:

-0 bit if the higher layer parameter scheduledCellComboListDCI-1-3 for the scheduled cell set is not configured;

-otherwise  bits indicating the scheduled cells in the scheduled cell set according to Table 7.3.1.2.4-1, where  is the number of entries in the higher layer parameter scheduledCellComboListDCI-1-3. If only one entry is configured in the higher layer parameter scheduledCellComboListDCI-1-3, the scheduled cells are the cells configured by higher layer parameter scheduledCellComboListDCI-1-3.log2IDLIDL

-Bandwidth part indicator - 0, 1 or 2 bits determined as , where log2nBWP, max

- if ,  is the maximum number of DL BWPs configured by higher layers, excluding the initial DL bandwidth part, across all the cells configured by higher layer parameter scheduledCellListDCI-1-3 in the scheduled cell set, in which case the bandwidth part indicator is equivalent to the ascending order of the higher layer parameter BWP-Id;nBWP, max=nBWP,RRCmax+1nBWP,RRCmax≤3nBWP,RRCmax

-otherwise , in which case the bandwidth part indicator is defined in Table 7.3.1.1.2-1;nBWP, max=nBWP,RRCmax

The field is only applicable to a scheduled cell with the number of configured DL BWPs larger than 1, including the initial DL bandwidth part, and is applied to the applicable scheduled cells in the scheduled cell set independently. If a UE does not support active BWP change via DCI, the UE ignores this bit field. If this field indicates a code point that does not correspond to a configured BWP of a scheduled cell, the UE ignores this bit field for the scheduled cell, and operates on the active BWP of the scheduled cell.

-Frequency domain resource assignment - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellDL

If scheduledCellComboListDCI-1-3 for the scheduled cell set is configured with more than one entry,  is the number of scheduled cells indicated by Scheduled cells indicator field; if scheduledCellComboListDCI-1-3 for the scheduled cell set is configured with only one entry, is the number of cells configured by higher layer parameter scheduledCellComboListDCI-1-3; otherwise,  is the number of cells in the scheduled cell set configured by higher layer parameter scheduledCellListDCI-1-3. Each block corresponds to the frequency domain resource assignment for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the frequency domain resource assignment for the cell with the smallest serving cell index. Each block is defined by the following fields:  NcellDL NcellDLNcellDL

- bits if only resource allocation type 0 is configured, where  is defined in Clause 5.1.2.2.1 of [6, TS 38.214]NRBGNRBG

- bits if only resource allocation type 1 is configured, or  bits if resourceAllocationDCI-1-3 is configured as 'dynamicSwitch', where   is the size of the active DL bandwidth part,  is defined as in clause 4.4.4.4 of [4, TS 38.211] and  is given by higher layer parameter resourceAllocationType1GranularityDCI-1-3. If the higher layer parameter resourceAllocationType1GranularityDCI-1-3 is not configured,  is equal to 1.log2NRBG, K2NRBG, K2+1/2max log2NRBG, K2NRBG, K2+1/2, NRBG+1NRBG, K2=NRBDL, BWP+NDL, BWPstartmodK2/K2,NRBDL, BWPNDL, BWPstartK2K2

-If resourceAllocationDCI-1-3 is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.1 of [6, TS 38.214].NRBG

-For resource allocation type 1, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.2 of [6, TS 38.214].log2NRBG, K2NRBG, K2+1/2

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and if resourceAllocationDCI-1-3 is configured as 'dynamicSwitch' for the indicated bandwidth part, the UE assumes resource allocation type 0 for the indicated bandwidth part if the bitwidth of the "Frequency domain resource assignment" field of the active bandwidth part is smaller than the bitwidth of the "Frequency domain resource assignment" field of the indicated bandwidth part.

If the higher layer parameter scheduledCellComboListDCI-1-3 for the scheduled cell set is not configured, each block is also used to indicate whether the corresponding cell is scheduled or not as follows:

-if all bits of a block are set to 0 for resource allocation type 0 or set to 1 for resource allocation type 1 or set to 0 or 1 for dynamic switch resource allocation type, the cell corresponding to the block is not scheduled;

-otherwise, the cell corresponding to the block is scheduled.

-Time domain resource assignment - bits, where  is the number of entries in the higher layer parameter tdra-FieldIndexListDCI-1-3. This field is used to indicate an entry in the higher layer parameter tdra-FieldIndexListDCI-1-3 according to Table 7.3.1.2.4-2. Each entry in the higher layer parameter tdra-FieldIndexListDCI-1-3 contains the ‘Time domain resource assignment’ index for each BWP of each cell in the scheduled cell set, where the ‘Time domain resource assignment’ indexes for all the cells are placed according to an ascending order of a serving cell index, and the 'Time domain resource assignment' indexes for all the BWPs of a cell are placed according to an ascending order of the higher layer parameter BWP-Id. log2(ITDRA)  ITDRA

-VRB-to-PRB mapping - 0 or 1 bit

-0 bit if the higher layer parameter vrb-ToPRB-Interleaver is not configured for any cell configured by higher layer parameter scheduledCellListDCI-1-3 in the scheduled cell set;

-1 bit according to Table 7.3.1.2.2-5 otherwise, only applicable to resource allocation type 1, as defined in Clause 7.3.1.6 of [4, TS 38.211].

The field is only applicable to a scheduled cell configured with vrb-ToPRB-Interleaver, and is applied to the applicable scheduled cells independently.

-PRB bundling size indicator - 0 or 1 bit

-0 bit if the higher layer parameter prb-BundlingType is not configured or is set to 'staticBundling' for any cell configured by higher layer parameter scheduledCellListDCI-1-3 in the scheduled cell set;

-1 bit according to Clause 5.1.2.3 of [6, TS 38.214] otherwise.

The field is only applicable to a scheduled cell configured with prb-BundlingType set to 'dynamicBundling', and is applied to the applicable scheduled cells independently.

-Rate matching indicator -bits, where  is the number of entries in the higher layer parameter rateMatchListDCI-1-3, or 0 bit if the higher layer parameter rateMatchListDCI-1-3 is not configured. This field is used to indicate an entry in the higher layer parameter rateMatchListDCI-1-3 according to Table 7.3.1.2.4-3. Each entry in the higher layer parameter rateMatchListDCI-1-3 contains the ‘Rate matching indicator’ index for each cell configured with rateMatchPatternGroup1 or rateMatchPatternGroup2 on at least one DL BWP in the scheduled cell set, where the ‘Rate matching indicator’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘Rate matching indicator’ index is defined by the following:  log2(IRM) IRM

-0, 1, or 2 bits according to higher layer parameters rateMatchPatternGroup1 and rateMatchPatternGroup2, where the MSB is used to indicate rateMatchPatternGroup1 and the LSB is used to indicate rateMatchPatternGroup2 when there are two groups.

-ZP CSI-RS trigger -bits, where  is the number of entries in the higher layer parameter zp-CSI-RSListDCI-1-3, or 0 bit if the higher layer parameter zp-CSI-RSListDCI-1-3 is not configured. This field is used to indicate an entry in the higher layer parameter zp-CSI-RSListDCI-1-3 according to Table 7.3.1.2.4-4. Each entry in the higher layer parameter zp-CSI-RSListDCI-1-3 contains the ‘ZP CSI-RS trigger’ index for each cell configured with aperiodicZP-CSI-RS-ResourceSetsToAddModList on at least one DL BWP in the scheduled cell set, where the ‘ZP CSI-RS trigger’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘ZP CSI-RS trigger’ index is defined by the following:  log2(ICSIRS) ICSIRS

-0, 1, or 2 bits as defined in Clause 5.1.4.2 of [6, TS 38.214]. The bitwidth for this field is determined as  bits, where  is the number of aperiodic ZP CSI-RS resource sets configured by higher layer parameter aperiodicZP-CSI-RS-ResourceSetsToAddModList.log2(nZP+1)nZP

For transport block 1:

-Modulation and coding scheme - number of bits determined by the following:

-block number 1, block number 2,…, block number NcellDL

Each block corresponds to the modulation and coding scheme for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the modulation and coding scheme for the cell with the smallest serving cell index. Each block is 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214].

-New data indicator - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL

Each block corresponds to the new data indicator for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the new data indicator for the cell with the smallest serving cell index. If pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 is configured for a cell, the number of bits for the corresponding block is equal to the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for the cell, where each bit corresponds to one scheduled PDSCH as defined in clause 6.1.4 in [6, TS 38.214]; otherwise, the corresponding block is 1 bit.

-Redundancy version - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL

Each block corresponds to the redundancy version for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the redundancy version for the cell with the smallest serving cell index. The number of bits for each block is determined by following:

-if pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 is configured for a cell, the number of bits for the corresponding block is determined by , where  is the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for the cell,  is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-1-3 for the cell, and each  bit(s) corresponds to one scheduled PDSCH as defined in clause 6.1.4 in [6, TS 38.214],mA×mBmAmBmB

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-otherwise, the corresponding block is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-1-3 configured for the cell,

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

For transport block 2:

-Modulation and coding scheme - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL,3

If scheduledCellComboListDCI-1-3 for the scheduled cell set is configured with more than one entry,  is the number of scheduled cells indicated by Scheduled cells indicator field and configured with maxNrofCodeWordsScheduledByDCI = 2; if scheduledCellComboListDCI-1-3 for the scheduled cell set is configured with only one entry, is the number of cells configured by higher layer parameter scheduledCellComboListDCI-1-3 and configured with maxNrofCodeWordsScheduledByDCI = 2; otherwise, is the number of cells configured by higher layer parameter scheduledCellListDCI-1-3 in the scheduled cell set and configured with maxNrofCodeWordsScheduledByDCI = 2. Each block corresponds to the modulation and coding scheme for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the modulation and coding scheme for the cell with the smallest serving cell index. Each block is 5 bits as defined in Clause 6.1.4.1 of [6, TS 38.214].    NcellDL,3 NcellDL,3NcellDL,3

-New data indicator - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL,3

Each block corresponds to the new data indicator for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the new data indicator for the cell with the smallest serving cell index. If pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 is configured for a cell, the number of bits for the corresponding block is equal to the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for the cell, where each bit corresponds to one scheduled PDSCH as defined in clause 6.1.4 in [6, TS 38.214]; otherwise, the corresponding block is 1 bit.

-Redundancy version - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL,3

Each block corresponds to the redundancy version for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the redundancy version for the cell with the smallest serving cell index. The number of bits for each block is determined by following:

-if pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 is configured for a cell, the number of bits for the corresponding block is determined by , where  is the maximum number of schedulable PDSCHs among all entries in the higher layer parameter pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for the cell,  is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-1-3 for the cell, and each  bit(s) corresponds to one scheduled PDSCH as defined in clause 6.1.4 in [6, TS 38.214],mA×mBmAmBmB

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

-otherwise, the corresponding block is 0, 1 or 2 bits determined by higher layer parameter numberOfBitsForRV-DCI-1-3 configured for the cell,

-If 0 bit is configured, rvid to be applied is 0;

-1 bit according to Table 7.3.1.2.3-1;

-2 bits according to Table 7.3.1.1.1-2.

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part and the value of maxNrofCodeWordsScheduledByDCI for the indicated bandwidth part equals 2 and the value of maxNrofCodeWordsScheduledByDCI for the active bandwidth part equals 1, the UE assumes zeros are padded when interpreting the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields of transport block 2 according to Clause 12 of [5, TS38.213], and the UE ignores the "Modulation and coding scheme", "New data indicator", and "Redundancy version" fields of transport block 2 for the indicated bandwidth part.

-HARQ process number - number of bits determined by the following:

-block number 1, block number 2,…, block number  NcellDL

Each block corresponds to the HARQ process number for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the HARQ process number for the cell with the smallest serving cell index. Each block is 0, 1, 2, 3, 4 or 5 bits determined by higher layer parameter harq-ProcessNumberSizeDCI-1-3 or harq-ProcessNumberSizeDCI-1-3-Ext configured for the cell corresponding to the block.

-Downlink assignment index - number of bits as defined in the following

-4 bits if the higher layer parameter pdsch-HARQ-ACK-Codebook=dynamic, where the 2 MSB bits are the counter DAI and the 2 LSB bits are the total DAI;

-0 bits otherwise.

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-Codebook is replaced by pdsch-HARQ-ACK-Codebook-secondaryPUCCHgroup-r16 if present for the secondary PUCCH group.

If higher layer parameter priorityIndicatorDCI-1-3 is configured, if the bit width of the Downlink assignment index in DCI format 1_3 for one HARQ-ACK codebook is not equal to that of the Downlink assignment index in DCI format 1_3 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller Downlink assignment index until the bit width of the Downlink assignment index in DCI format 1_3 for the two HARQ-ACK codebooks are the same.

-TPC command for scheduled PUCCH - 2 bits as defined in Clause 7.2.1 of [5, TS 38.213]

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]

-PDSCH-to-HARQ_feedback timing indicator - 0, 1, 2, or 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter dL-DataToUL-ACK.log2(I)

If higher layer parameter priorityIndicatorDCI-1-3 is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 for one HARQ-ACK codebook is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 for the other HARQ-ACK codebook on the same cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 for the two HARQ-ACK codebooks are the same.

If higher layer parameter pucch-sSCellDynDCI-1-3 is configured, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 associated with one cell for PUCCH transmission is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 associated with the other cell for PUCCH transmission, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 1_3 associated with the two cells are the same.

-One-shot HARQ-ACK request - 0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-OneShotFeedbackDCI-1-3 or pdsch-HARQ-ACK-enhType3DCI-1-3 is configured;

-0 bit otherwise.

-Enhanced Type 3 codebook indicator - 0, 1, 2, or 3 bits.

-0 bit if pdsch-HARQ-ACK-enhType3DCIfieldDCI-1-3 is not configured;

- bits otherwise, where  is the number of entries in the higher layer parameter pdsch-HARQ-ACK-EnhType3ToAddModList.log2(nCB)nCB

If the UE is configured with a PUCCH-SCell, pdsch-HARQ-ACK-EnhType3ToAddModList is replaced by pdsch-HARQ-ACK-EnhType3SecondaryList for the secondary PUCCH group.

-HARQ-ACK retransmission indicator - 0 or 1 bit.

-1 bit if higher layer parameter pdsch-HARQ-ACK-retxDCI-1-3 is configured.

-0 bit otherwise.

-Antenna ports - number of bits determined by the following:

-If antennaPortsDCI-1-3= type1a is configured by higher layer,

-bits applying to the scheduled cells independently, where  is the number of cells configured by higher layer parameter scheduledCellListDCI-1-3 in the scheduled cell set,   is mapped to the cells according to an ascending order of a serving cell index with  corresponding to the cell with the smallest serving cell index, and  is defined below.maxr∈{1,2,…,NcellDL,2}MAr NcellDL,2rr=1MAr

-If antennaPortsDCI-1-3= type2 is configured by higher layer,

-block number 1, block number 2,…, block number   NcellDL

Each block corresponds to the Antenna ports information for a cell, and the blocks are placed according to an ascending order of a serving cell index, with block number 1 corresponding to the Antenna ports information for the cell with the smallest serving cell index. Each block is defined below.

above for the case of antennaPortsDCI-1-3= type1A or each block above for the case of antennaPortsDCI-1-3= type2 is defined by the following: MAr

-4, 5, 6, 7 or 8 bits as defined by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 and Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A, where the number of CDM groups without data of values 1, 2, and 3 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively. The antenna ports  shall be determined according to the ordering of DMRS port(s) given by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10 or Tables 7.3.1.2.2-1A/2A/3A/4A/7A/8A/9A/10A. p0,…,pv-1

If a UE is configured with both dmrs-DownlinkForPDSCH-MappingTypeA and dmrs-DownlinkForPDSCH-MappingTypeB, the bitwidth of this field equals , where  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeA and  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeB. A number of  zeros are padded in the MSB of this field, if the mapping type of the PDSCH corresponds to the smaller value of  and .maxxA,xBxAxBxA-xBxAxB

-Transmission configuration indication - number of bits determined by the following:

-0 bit if higher layer parameter tci-PresentInDCI is not enabled or if higher layer parameter tci-ListDCI-1-3 is not configured;

-otherwise bits, where  is the number of entries in the higher layer parameter tci-ListDCI-1-3. This field is used to indicate an entry in the higher layer parameter tci-ListDCI-1-3 according to Table 7.3.1.2.4-5. Each entry in the higher layer parameter tci-ListDCI-1-3 contains the ‘Transmission configuration indication’ index for each cell in the scheduled cell set, where the ‘Transmission configuration indication’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘Transmission configuration indication’ index is 3 bits as defined in Clause 5.1.5 of [6, TS38.214]. log2(ITCI) ITCI

If "Bandwidth part indicator" field indicates a bandwidth part other than the active bandwidth part,

-if the higher layer parameter tci-PresentInDCI is not enabled for the CORESET used for the PDCCH carrying the DCI format 1_3,

-the UE assumes tci-PresentInDCI is not enabled for all CORESETs in the indicated bandwidth part;

-otherwise,

-the UE assumes tci-PresentInDCI is enabled for all CORESETs in the indicated bandwidth part.

-SRS request -bits, where  is the number of entries in the higher layer parameter srs-RequestListDCI-1-3, or 0 bit if the higher layer parameter srs-RequestListDCI-1-3 is not configured. This field is used to indicate an entry in the higher layer parameter srs-RequestListDCI-1-3 according to Table 7.3.1.2.4-6. Each entry in the higher layer parameter srs-RequestListDCI-1-3 contains the ‘SRS request’ index for each cell in the scheduled cell set, where the ‘SRS request’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘SRS request’ index is defined by the following:  log2(ISRS) ISRS

-2 bits as defined by Table 7.3.1.1.2-24 for UEs not configured with supplementaryUplink in ServingCellConfig in the cell; 3 bits for UEs configured with supplementaryUplink in ServingCellConfig in the cell where the first bit is the non-SUL/SUL indicator as defined in Table 7.3.1.1.1-1 and the second and third bits are defined by Table 7.3.1.1.2-24. This bit field may also indicate the associated CSI-RS according to Clause 6.1.1.2 of [6, TS 38.214].

-SRS offset indicator -bits, where is the number of entries in the higher layer parameter srs-OffsetListDCI-1-3, or 0 bit if the higher layer parameter srs-OffsetListDCI-1-3 is not configured. This field is used to indicate an entry in the higher layer parameter srs-OffsetListDCI-1-3 according to Table 7.3.1.2.4-7. Each entry in the higher layer parameter srs-OffsetListDCI-1-3 contains the ‘SRS offset indicator’ index for each cell in the scheduled cell set, where the ‘SRS offset indicator’ indexes for all the cells are placed according to an ascending order of a serving cell index. Each ‘SRS offset indicator’ index is defined by the following:  log2(Ioffset) Ioffset

-0 bit if higher layer parameter AvailableSlotOffset is not configured for any aperiodic SRS resource set in the scheduled cell, or if higher layer parameter AvailableSlotOffset is configured for at least one aperiodic SRS resource set in the scheduled cell and the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) is 1;

-otherwise,  bits are used to indicate available slot offset according to Table 7.3.1.1.2-37 and Clause 6.2.1 of [6, TS 38.214], where K is the maximum number of entries of availableSlotOffsetList configured for all aperiodic SRS resource set(s) in the scheduled cell;log2(K)

-DMRS sequence initialization - 1 bit. This field is applied to all the scheduled cells indicated by Scheduled cells indicator field or Frequency domain resource assignment field independently.

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-1-3 is not configured; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-ChannelAccess-CPext - 0, 1, 2, 3 or 4 bits. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter ul-AccessConfigListDCI-1-1 or in Table 7.3.1.1.1-4A if channelAccessMode-r16 = "semiStatic" is provided, for operation in a cell with shared spectrum channel access in frequency range 1, or for operation in frequency range 2-2 if ChannelAccessMode2-r17 is provided; otherwise 0 bit. One or more entries from Table 7.3.1.2.2-6 or Table 7.3.1.2.2-6A are configured by the higher layer parameter ul-AccessConfigListDCI-1-1.log2(I)

-Minimum applicable scheduling offset indicator - 0 or 1 bit

-0 bit if higher layer parameter minimumSchedulingOffsetK0DCI-1-3 is not configured;

-1 bit otherwise. The 1 bit indication is used to determine the minimum applicable K0 for the active DL BWP and the minimum applicable K2 for the active UL BWP, if configured respectively, according to Table 7.3.1.1.2-33. If the minimum applicable K0 is indicated, the minimum applicable value of the aperiodic CSI-RS triggering offset for an active DL BWP for each scheduled cell shall be the same as the minimum applicable K0.

-SCell dormancy indication - 0 bit if higher layer parameter dormancyDCI-1-3 or dormancyGroupWithinActiveTime is not configured; otherwise 1, 2, 3, 4, or 5 bits bitmap determined according to the number of different DormancyGroupID(s) provided by higher layer parameter dormancyGroupWithinActiveTime, where each bit corresponds to one of the SCell group(s) configured by higher layers parameter dormancyGroupWithinActiveTime, with MSB to LSB of the bitmap corresponding to the first to the last configured SCell group in ascending order of DormancyGroupID. The field is only present when this format is carried by PDCCH on the primary cell within DRX Active Time and the UE is configured with at least two DL BWPs for an SCell.

If the “One-shot HARQ-ACK request” field is not present or set to '0', and if the “HARQ-ACK retransmission indicator” field is not present or set to ‘0’, and if all bits of the corresponding block(s) of the frequency domain resource assignment field are set to 0 for resource allocation type 0 or set to 1 for resource allocation type 1 or set to 0 or 1 for dynamic switch resource allocation type for one or more cells in the scheduled cell set, this field is reserved and the following fields, corresponding to the cell with smallest serving cell index among the one or more cells, among the fields above are used for SCell dormancy indication, where each bit corresponds to one of the configured SCell(s), with MSB to LSB of the following fields concatenated in the order below corresponding to the SCell with lowest to highest SCell index

-Modulation and coding scheme of transport block 1

-New data indicator of transport block 1

-Redundancy version of transport block 1

-HARQ process number

-Antenna port(s) if antennaPortsDCI1-3= type2 is configured by higher layer.

-PDCCH monitoring adaptation indication - 0, 1 or 2 bits

-0 bit if higher layer parameter pdcchMonAdaptDCI-1-3 is not enabled;

-otherwise,

-1 or 2 bits, if searchSpaceGroupIdList-r17 is not configured and if pdcch-SkippingDurationList is configured

-1 bit if the UE is configured with only one duration by pdcch-SkippingDurationList;

-2 bits if the UE is configured with more than one duration by pdcch-SkippingDurationList.

-1 or 2 bits, if pdcch-SkippingDurationList is not configured and if searchSpaceGroupIdList-r17 is configured

-1 bit if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0 and search space set(s) with group index 1, and if the UE is not configured by searchSpaceGroupIdList-r17 with any search space set with group index 2;

-2 bits if the UE is configured by searchSpaceGroupIdList-r17 with search space set(s) with group index 0, search space set(s) with group index 1 and search space set(s) with group index 2;

-2 bits, if pdcch-SkippingDurationList is configured and if searchSpaceGroupIdList-r17 is configured

-PUCCH Cell indicator - 0 or 1 bit.

-1 bit if higher layer parameter pucch-sSCellDynDCI-1-3 is configured.

-0 bit otherwise.

-Measurement gap cancellation – 0 bit if higher layer parameter mg-CancellationDCI-1-3 is not configured; otherwise 1 bit as defined in Clause 10.6 in [5, TS 38.213].

If scheduledCellComboListDCI-1-3 for the cell set is configured, zeros shall be appended to DCI format 1_3 if needed until the payload size equals the size of DCI format 1_3 that is determined by the configuration of the corresponding active bandwidth part(s) of the scheduled cells in the entry which results in the largest size among the entries in the higher layer parameter scheduledCellComboListDCI-1-3.

If an SCell within the scheduled cell set is deactivated and the firstActiveDownlinkBWP-Id corresponding to the SCell is not set to dormant BWP, the UE determines the bitwidth of the fields in DCI format 1_3 based on a DL BWP provided by firstActiveDownlinkBWP-Id for the SCell. If the active DL BWP of an SCell within the scheduled cell set is a dormant DL BWP, or if an SCell within the scheduled cell set is deactivated and the firstActiveDownlinkBWP-Id corresponding to the SCell is set to dormant BWP, the UE determines the bitwidth of the fields in DCI format 1_3 based on a DL BWP provided by firstWithinActiveTimeBWP-Id for the SCell if provided; otherwise, based on a DL BWP provided by firstOutsideActiveTimeBWP-Id for the SCell.

Table 7.3.1.2.4-1: Scheduled cells indicator in DCI format 1_3

Table 7.3.1.2.4-2: Time domain resource assignment in DCI format 1_3

Table 7.3.1.2.4-3: Rate matching indicator

Table 7.3.1.2.4-4: ZP CSI-RS trigger

Table 7.3.1.2.4-5: Transmission configuration indication

Table 7.3.1.2.4-6: SRS request in DCI format 1_3

Table 7.3.1.2.4-7: SRS offset indicator in DCI format 1_3

## 7.3.1.3DCI formats for other purposes

## 7.3.1.3.1Format 2_0

DCI format 2_0 is used for notifying the slot format, COT duration, available RB set, and search space set group switching.

The following information is transmitted by means of the DCI format 2_0 with CRC scrambled by SFI-RNTI:

-If the higher layer parameter slotFormatCombToAddModList is configured,

-Slot format indicator 1, Slot format indicator 2, …, Slot format indicator N,

-If the higher layer parameter availableRB-SetsToAddModList is configured,

-Available RB set Indicator 1, Available RB set Indicator 2, …, Available RB set Indicator N1,

-If the higher layer parameter co-DurationsPerCellToAddModList is configured

-COT duration indicator 1, COT duration indicator 2, …, COT duration indicator N2.

-If the higher layer parameter switchTriggerToAddModList is configured

-Search space set group switching flag 1, Search space set group switching flag 2, …, Search space set group switching flag M.

The size of DCI format 2_0 is configurable by higher layers up to 128 bits, according to Clause 11.1.1 of [5, TS 38.213].

## 7.3.1.3.2Format 2_1

DCI format 2_1 is used for notifying the PRB(s) and OFDM symbol(s) where UE may assume no transmission is intended for the UE.

The following information is transmitted by means of the DCI format 2_1 with CRC scrambled by INT-RNTI:

-Pre-emption indication 1, Pre-emption indication 2, …, Pre-emption indication N.

The size of DCI format 2_1 is configurable by higher layers up to 126 bits, according to Clause 11.2 of [5, TS 38.213]. Each pre-emption indication is 14 bits.

## 7.3.1.3.3Format 2_2

DCI format 2_2 is used for the transmission of TPC commands for PUCCH and PUSCH.

The following information is transmitted by means of the DCI format 2_2 with CRC scrambled by TPC-PUSCH-RNTI or TPC-PUCCH-RNTI:

-block number 1, block number 2,…, block number N

The parameter tpc-PUSCH or tpc-PUCCH  provided by higher layers determines the index to the block number for an UL of a cell, with the following fields defined for each block:

-Closed loop indicator   - 0 or 1 bit.

-For DCI format 2_2 with TPC-PUSCH-RNTI, 0 bit if the UE is not configured with high layer parameter twoPUSCH-PC-AdjustmentStates, in which case UE assumes each block in the DCI format 2_2 is of 2 bits; 1 bit otherwise, in which case UE assumes each block in the DCI format 2_2 is of 3 bits;

-For DCI format 2_2 with TPC-PUCCH-RNTI, 0 bit if the UE is not configured with high layer parameter twoPUCCH-PC-AdjustmentStates, in which case UE assumes each block in the DCI format 2_2 is of 2 bits; 1 bit otherwise, in which case UE assumes each block in the DCI format 2_2 is of 3 bits;

-TPC command -2 bits

The number of information bits in format 2_2 shall be equal to or less than the payload size of format 1_0 monitored in common search space in the same serving cell. If the number of information bits in format 2_2 is less than the payload size of format 1_0 monitored in common search space in the same serving cell, zeros shall be appended to format 2_2 until the payload size equals that of format 1_0 monitored in common search space in the same serving cell.

## 7.3.1.3.4Format 2_3

DCI format 2_3 is used for the transmission of a group of TPC commands for SRS transmissions by one or more UEs. Along with a TPC command, a SRS request may also be transmitted.

The following information is transmitted by means of the DCI format 2_3 with CRC scrambled by TPC-SRS-RNTI:

-block number 1, block number 2, …, block number

where the starting position of a block is determined by the parameter startingBitOfFormat2-3 or startingBitOfFormat2-3SUL-v1530 provided by higher layers for the UE configured with the block.

If the UE is configured with higher layer parameter srs-TPC-PDCCH-Group = typeA for an UL without PUCCH and PUSCH or an UL on which the SRS power control is not tied with PUSCH power control, one or two blocks are configured for the UE by higher layers where one block applies to non-SUL carriers and another block applies to SUL carriers, with the following fields defined for each block:

-SRS request - 0 or 2 bits. The presence of this field is according to the definition in Clause 11.4 of [5, TS38.213]. If present, this field is interpreted as defined by Table 7.3.1.1.2-24.

-TPC command number 1, TPC command number 2, ..., TPC command number N, where each TPC command applies to a respective UL carrier provided by higher layer parameter cc-IndexInOneCC-Set

-Closed loop indicator 1, Closed loop indicator 2, ..., Closed loop indicator , where each Closed loop indicator applies to a respective UL carrier provided by higher layer parameter cc-IndexInOneCC-Set. A Closed loop indicator is present only if the UE is configured with higher layer parameter enableTwoSeparatePowerControlAdjustmentStatesForSRS for the UL carrier.N1

If the UE is configured with higher layer parameter srs-TPC-PDCCH-Group = typeB for an UL without PUCCH and PUSCH or an UL on which the SRS power control is not tied with PUSCH power control, one block or more blocks is configured for the UE by higher layers where each block applies to an UL carrier, with the following fields defined for each block:

-SRS request - 0 or 2 bits. The presence of this field is according to the definition in Clause 11.4 of [5, TS38.213]. If present, this field is interpreted as defined by Table 7.3.1.1.2-24.

-TPC command -2 bits

-Closed loop indicator - 1 bit if the UE is configured with higher layer parameter enableTwoSeparatePowerControlAdjustmentStatesForSRS for the UL carrier; 0 bit otherwise.

The number of information bits in format 2_3 shall be equal to or less than the payload size of format 1_0 monitored in common search space in the same serving cell. If the number of information bits in format 2_3 is less than the payload size of format 1_0 monitored in common search space in the same serving cell, zeros shall be appended to format 2_3 until the payload size equals that of format 1_0 monitored in common search space in the same serving cell.

## 7.3.1.3.5Format 2_4

DCI format 2_4 is used for notifying the PRB(s) and OFDM symbol(s) where UE cancels the corresponding UL transmission from the UE according to Clause 11.2A of [5, TS 38.213].

The following information is transmitted by means of the DCI format 2_4 with CRC scrambled by CI-RNTI:

-Cancellation indication 1, Cancellation indication 2, …, Cancellation indication indication N.

The size of DCI format 2_4 is configurable by higher layers parameter dci-PayloadSizeForCI up to 126 bits, according to Clause 11.2A of [5, TS 38.213]. The number of bits for each cancellation indication is configurable by higher layer parameter ci-PayloadSize. For a UE, there is at most one cancellation indication for an UL carrier.

## 7.3.1.3.6Format 2_5

DCI format 2_5 is used for notifying the availability of soft resources as defined in Clause 9.3.1 of [10, TS 38.473]

The following information is transmitted by means of the DCI format 2_5 with CRC scrambled by AI-RNTI:

-Availability indicator 1, Availability indicator 2, …, Availability indicator N.

The size of DCI format 2_5 is configurable by higher layers up to 128 bits, according to Clause 14 of [5, TS 38.213].

## 7.3.1.3.7Format 2_6

DCI format 2_6 is used for notifying the power saving information outside DRX Active Time for one or more UEs.

The following information is transmitted by means of the DCI format 2_6 with CRC scrambled by PS-RNTI:

-block number 1, block number 2,…, block number N

where the starting position of a block is determined by the parameter ps-PositionDCI-2-6 provided by higher layers for the UE configured with the block.

If the UE is configured with higher layer parameter ps-RNTI and dci-Format2-6, one block is configured for the UE by higher layers, with the following fields defined for the block:

-Wake-up indication - 1 bit

-SCell dormancy indication - 0 bit if higher layer parameter dormancyGroupOutsideActiveTime is not configured; otherwise 1, 2, 3, 4 or 5 bits bitmap determined according to the number of different DormancyGroupID(s) provided by higher layer parameter dormancyGroupOutsideActiveTime, where each bit corresponds to one of the SCell group(s) configured by higher layers parameter dormancyGroupOutsideActiveTime, with MSB to LSB of the bitmap corresponding to the first to last configured SCell group in ascending order of DormancyGroupID.

The size of DCI format 2_6 is indicated by the higher layer parameter sizeDCI-2-6, according to Clause 10.3 of [5, TS 38.213].

## 7.3.1.3.8Format 2_7

DCI format 2_7 is used for notifying the paging early indication and TRS availability indication for one or more UEs.

The following information is transmitted by means of the DCI format 2_7 with CRC scrambled by PEI-RNTI:

-Paging indication field -  bit(s), whereNPOPEINSGPO

- is the number of paging occasions configured by higher layer parameter po-NumPerPEI as defined in Clause 10.4A in [5, TS 38.213];NPOPEI

-is the number of sub-groups of a paging occasion configured by higher layer parameter subgroupsNumPerPO.NSGPO

-Each bit in the field indicates one UE subgroup of a paging occasion.

-TRS availability indication - 1, 2, 3, 4, 5, or 6 bits, where the number of bits is equal to one plus the highest value of all the indBitID(s) provided by the trs-ResourceSetConfig or the number of bits is equal to one plus the highest value of all the indBitID-r18(s) provided by the trs-ResourceSetConfig-r18 if configured if configured; 0 bits otherwise.

The size of DCI format 2_7 is indicated by the higher layer parameter payloadSizeDCI-2-7, according to Clause 10.4A of [5, TS 38.213]. The number of information bits in format 2_7 shall be equal to or less than the payload size of format 2_7. If the number of information bits in format 2_7 is less than the size of format 2_7, the remaining bits are reserved.

## 7.3.1.3.9Format 2_8

DCI format 2_8 is used for notifying the aperiodic beam indication and associated time resources

The following information is transmitted by means of the DCI format 2_8 with CRC scrambled by NCR-RNTI:

-Beam index 1, Beam index 2, …, Beam index N

The bitwidth of each beam index field is determined by the higher layer parameter aperiodicBeamFieldWidth.

-Time resource indication 1, Time resource indication 2, …, Time resource indication N

The bitwidth of each time resource indication field is determined by max, where  is the number of time domain resources configured by aperiodicFwdConfig. The bit field indexes of a time resource indication field are mapped to the time domain resources configured by aperiodicFwdConfig according to an ascending order of a resource identity configured by aperiodicFwdTimeRsrcId, with the bit field index 0 mapped to the time resource with the smallest resource identity. log2I,1I

The N beam indexes are sequentially associated with the N time resource indications with one to one mapping.  N is configured by the higher layer parameter numberOfFields. The size of DCI format 2_8 is up to 128 bits.

## 7.3.1.3.10Format 2_9

DCI format 2_9 with CRC scrambled by cellDTRX-RNTI is used for activating or de-activating the cell DTX and/or DRX configuration of one or multiple serving cells for one or more UEs, and/or for providing NES-mode indication of the primary cell for one or more UEs. DCI format 2_9 with CRC scrambled by ssbPeriodicityIndication-RNTI is used for adapting SSB periodicity of one or multiple serving cells for one or more UEs.

The following information is transmitted by means of the DCI format 2_9 with CRC scrambled by cellDTRX-RNTI:

-block number 1, block number 2,…, block number N

where the starting position of a block associated with a serving cell is determined by the parameter positionInDCI-cellDTRX provided by higher layers for the UE.

If the UE is configured to monitor DCI 2_9 with CRC scrambled by cellDTRX-RNTI and for a DCI format 2_9 with CRC scrambled by cellDTRX-RNTI, one or more blocks are configured for the UE by higher layers, with the following fields defined for each block:

-Cell DTX/DRX indication - number of bits determined by the following:

-If higher layer parameter cellDTX-DRX-L1activation is configured

-2 bits as defined in Clause 11.5 of [5, TS38.213] if cellDTX-DRX-ConfigType is configured to dtxdrx for the associated serving cell of the block, with the MSB corresponding to cell DTX configuration and the LSB corresponding to cell DRX configuration;

-1 bit as defined in Clause 11.5 of [5, TS38.213] if cellDTX-DRX-ConfigType is configured to either dtx or drx for the associated serving cell of the block;

-0 bit otherwise.

-NES-mode indication – 1 bit indicating NES-specific CHO execution condition as defined in Clause 11.5 of [5, TS38.213], if the higher layer parameter nesEvent is configured and the associated serving cell of the block is primary cell; 0 bit otherwise.

The following information is transmitted by means of the DCI format 2_9 with CRC scrambled by ssbPeriodicityIndication-RNTI:

-block number 1, block number 2,…, block number N1

where the starting position of a block associated with a serving cell is determined by the parameter posInDCI-SSB-PeriodicityIndicationForScell provided by higher layers for the UE.

If the UE is configured to monitor DCI 2_9 with CRC scrambled by ssbPeriodicityIndication-RNTI and for a DCI format 2_9 with CRC scrambled by ssbPeriodicityIndication-RNTI, one or more blocks are configured for the UE by higher layers, with the following fields defined for each block:

-SSB periodicity indication - number of bits determined by the following:

-If higher layer parameter ssb-BurstPeriodicityList is configured

-1 bit as defined in Clause 11.6 of [5, TS38.213], if one additional SSB periodicity is configured by higher layer parameter ssb-BurstPeriodicityList;

-2 bits as defined in Clause 11.6 of [5, TS38.213], if two additional SSB periodicities are configured by higher layer parameter ssb-BurstPeriodicityList;

-0 bit otherwise.

The size of DCI format 2_9 is indicated by the higher layer parameter sizeDCI-2-9. If the number of information bits in format 2_9 is less than the size of format 2_9, the remaining bits are reserved.

## 7.3.1.4DCI formats for scheduling of sidelink

## 7.3.1.4.1Format 3_0

DCI format 3_0 is used for scheduling of NR PSCCH and NR PSSCH in one cell, or scheduling of NR PSCCH, NR PSSCH and NR SL PRS for a shared SL PRS resource pool in one cell.

The following information is transmitted by means of the DCI format 3_0 with CRC scrambled by SL-RNTI or SL-CS-RNTI:

-Resource pool index - bits, where I is the total number of resource pools for transmission configured by the higher layer parameter sl-TxPoolScheduling, if configured, and sl-DiscTxPoolScheduling, if configured.log2I

-Time gap - 3 bits determined by higher layer parameter sl-DCI-ToSL-Trans, as defined in clause 8.1.2.1 of [6, TS 38.214]

-HARQ process number - 4 bits.

-New data indicator - 1 bit.

-Lowest index of the subchannel allocation to the initial transmission - bits as defined in Clause 8.1.2.2 of [6, TS 38.214].log2(N subChannel SL)

-Lowest index of the RB set allocation to the initial transmission -  bits as defined in Clause 8.1.2.2 of [6, TS 38.214] if the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured to 'interlaceRB'; 0 bit otherwise.log2(NRBset)

-SCI format 1-A fields according to clause 8.3.1.1:

-Frequency resource assignment.

-Time resource assignment.

-PSFCH-to-HARQ feedback timing indicator - bits, where  is the number of entries in the higher layer parameter sl-PSFCH-ToPUCCH, as defined in clause 16.5 of [5, TS 38.213]log2Nfb_timingNfb_timing

-PUCCH resource indicator - 3 bits as defined in clause 16.5 of [5, TS 38.213].

-Configuration index - 0 bit if the UE is not configured to monitor DCI format 3_0 with CRC scrambled by SL-CS-RNTI; otherwise 3 bits as defined in clause 8.1.2 of [6, TS 38.214]. If the UE is configured to monitor DCI format 3_0 with CRC scrambled by SL-CS-RNTI, this field is reserved for DCI format 3_0 with CRC scrambled by SL-RNTI.

-Counter sidelink assignment index - 2 bits

-2 bits as defined in clause 16.5.2 of [5, TS 38.213] if the UE is configured with pdsch-HARQ-ACK-Codebook = dynamic

-2 bits as defined in clause 16.5.1 of [5, TS 38.213] if the UE is configured with pdsch-HARQ-ACK-Codebook = semi-static

-Padding bits, if required

If the total number of transmit resource pools provided in sl-TxPoolScheduling, if configured, and sl-DiscTxPoolScheduling, if configured, is larger than one, zeros shall be appended to the DCI format 3_0 until the payload size is equal to the size of a DCI format 3_0 given by a configuration of the transmit resource pool resulting in the largest number of information bits for DCI format 3_0.

If the UE is configured to monitor DCI format 3_1 and/or DCI format 3_2 and the number of information bits in DCI format 3_0 is less than the larger payload size of DCI format 3_1 if configured and DCI format 3_2 if configured, zeros shall be appended to DCI format 3_0 until the payload size equals the larger payload size of DCI format 3_1 if configured and DCI format 3_2 if configured.

## 7.3.1.4.2Format 3_1

DCI format 3_1 is used for scheduling of LTE PSCCH and LTE PSSCH in one cell.

The following information is transmitted by means of the DCI format 3_1 with CRC scrambled by SL Semi-Persistent Scheduling V-RNTI:

-Timing offset - 3 bits determined by higher layer parameter sl-TimeOffsetEUTRA-List, as defined in clause 16.6 of [5, TS 38.213]

-Carrier indicator -3 bits as defined in 5.3.3.1.9A of [11, TS 36.212].

-Lowest index of the subchannel allocation to the initial transmission -  bits as defined in 5.3.3.1.9A of [11, TS 36.212].

-Frequency resource location of initial transmission and retransmission, as defined in 5.3.3.1.9A of [11, TS 36.212]

-Time gap between initial transmission and retransmission, as defined in 5.3.3.1.9A of [11, TS 36.212]

-SL index - 2 bits as defined in 5.3.3.1.9A of [11, TS 36.212]

-SL SPS configuration index - 3 bits as defined in clause 5.3.3.1.9A of [11, TS 36.212].

-Activation/release indication - 1 bit as defined in clause 5.3.3.1.9A of [11, TS 36.212].

If the UE is configured to monitor DCI format 3_0 and/or DCI format 3_2 and the number of information bits in DCI format 3_1 is less than the larger payload size of DCI format 3_0 if configured and DCI format 3_2 if configured, zeros shall be appended to DCI format 3_1 until the payload size equals the larger payload size of DCI format 3_0 if configured and DCI format 3_2 if configured.

## 7.3.1.4.3Format 3_2

DCI format 3_2 is used for scheduling of NR PSCCH and NR SL PRS for a dedicated SL PRS resource pool in one cell.

The following information is transmitted by means of the DCI format 3_2 with CRC scrambled by SL-PRS-RNTI or SL-PRS-CS-RNTI:

-Resource pool index - bits, where I is the total number of dedicated SL PRS resource pools for transmission configured by the higher layer parameter sl-PRS-TxPoolScheduling, if configured.log2I

-Time gap - 3 bits determined by higher layer parameter sl-DCI-ToSL-Trans, as defined in clause 8.2.4.1.1 of [6, TS 38.214]

-First SL PRS indicator -  bits indicating the SL PRS resource ID for the first SL PRS transmission, where the value  is the total number of SL PRS resources within a slot in a dedicated SL PRS resource pool and provided by the higher layer parameter sl-PRS-ResourcesDedicatedSL-PRS-RP.log2NSL-PRSNSL-PRS

-SCI format 1-B fields according to clause 8.3.1.2:

-Time resource assignment

-Resource ID indication

-Configuration index – 0 bit if the UE is not configured to monitor DCI format 3_2 with CRC scrambled by SL-PRS-CS-RNTI; otherwise 3 bits as defined in clause 8.2.4.1 of [6, TS 38.214]. If the UE is configured to monitor DCI format 3_2 with CRC scrambled by SL-PRS-CS-RNTI, this field is reserved for DCI format 3_2 with CRC scrambled by SL-PRS-RNTI.

-Activation/release indication – 0 bit if the UE is not configured to monitor DCI format 3_2 with CRC scrambled with SL-PRS-CS-RNTI; otherwise 1 bit, where value 0 indicates release and value 1 indicates activation. If the UE is configured to monitor DCI format 3_2 with CRC scrambled with SL-PRS-CS-RNTI, this field is reserved for DCI format 3_2 with CRC scrambled by SL-PRS-RNTI.

-Padding bits, if required.

If the total number of transmit resource pools provided in sl-PRS-TxPoolScheduling, if configured, is larger than one, zeros shall be appended to the DCI format 3_2 until the payload size is equal to the size of a DCI format 3_2 given by a configuration of the transmit resource pool resulting in the largest number of information bits for DCI format 3_2.

If the UE is configured to monitor DCI format 3_0 and/or DCI format 3_1 and the number of information bits in DCI format 3_2 is less than the larger payload size of DCI format 3_0 if configured and DCI format 3_1 if configured, zeros shall be appended to DCI format 3_2 until the payload size equals the larger payload size of DCI format 3_0 if configured and DCI format 3_1 if configured.

## 7.3.1.5DCI formats for scheduling of MBS

## 7.3.1.5.1Format 4_0

DCI format 4_0 is used for the scheduling of PDSCH for broadcast or for multicast in RRC_INACTIVE state in DL cell.

The following information is transmitted by means of the DCI format 4_0 with CRC scrambled by MCCH-RNTI or G-RNTI for broadcast configured by MBS-SessionInfo, or by Multicast MCCH-RNTI:

-Frequency domain resource assignment -  bits where  equals to log2(NRBDL,CFR(NRBDL,CFR+1)2)NRBDL,CFR

-the size of CORESET 0 if CORESET 0 is configured for the cell; and

-the size of initial DL bandwidth part if CORESET 0 is not configured for the cell.

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS38.214]

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-MCCH change notification - 2 bits as defined in Clause 5.9.1.3 and Clause 5.10.1.3 of [9, TS38.331] if the CRC of the DCI format 4_0 is scrambled by MCCH-RNTI and Multicast MCCH-RNTI respectively. Otherwise, this bit field is reserved.

-Reserved bits - 14bits

## 7.3.1.5.2Format 4_1

DCI format 4_1 is used for the scheduling of PDSCH for multicast in DL cell.

The following information is transmitted by means of the DCI format 4_1 with CRC scrambled by G-RNTI for multicast or G-CS-RNTI configured by MBS-RNTI-SpecificConfig, or by G-RNTI for multicast configured by MBS-SessionInfoListMulticast:

-Frequency domain resource assignment - bits where  equals to log2(NRBDL,CFR(NRBDL,CFR+1)2)NRBDL,CFR

-the size of CORESET 0 if CORESET 0 is configured for the cell; and

-the size of initial DL bandwidth part if CORESET 0 is not configured for the cell.

-Time domain resource assignment - 4 bits as defined in Clause 5.1.2.1 of [6, TS38.214]

-VRB-to-PRB mapping - 1 bit according to Table 7.3.1.2.2-5

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3 of [6, TS38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits

-Downlink assignment index - 2 bits as defined in Clause 9.1.3 of [5, TS 38.213], as counter DAI

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS38.213]

-PDSCH-to-HARQ_feedback timing indicator - 3 bits as defined in Clause 9.2.3 of [5, TS38.213]

-Reserved bits - 3 bits

## 7.3.1.5.3Format 4_2

DCI format 4_2 is used for the scheduling of PDSCH for multicast in DL cell.

The following information is transmitted by means of the DCI format 4_2 with CRC scrambled by G-RNTI for multicast or G-CS-RNTI configured by MBS-RNTI-SpecificConfig:

-Frequency domain resource assignment - number of bits determined by the following, where  is the size of the common frequency resource as defined in Clause 18 of [5, TS38.213]. NRBDL,CFR

- bits if only resource allocation type 0 is configured, where  is defined in Clause 5.1.2.2.1 of [6, TS38.214], NRBGNRBG

- bits if only resource allocation type 1 is configured, or log2(NRBDL,CFR(NRBDL,CFR+1)2)

- bits if resourceAllocation in pdsch-ConfigMulticast is configured as 'dynamicSwitch'. maxlog2(NRBDL,CFR(NRBDL,CFR+1)2),NRBG+1

-If resourceAllocation in pdsch-ConfigMulticast is configured as 'dynamicSwitch', the MSB bit is used to indicate resource allocation type 0 or resource allocation type 1, where the bit value of 0 indicates resource allocation type 0 and the bit value of 1 indicates resource allocation type 1.

-For resource allocation type 0, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.1 of [6, TS 38.214].NRBG

-For resource allocation type 1, the  LSBs provide the resource allocation as defined in Clause 5.1.2.2.2 of [6, TS 38.214] log2(NRBDL,CFR(NRBDL,CFR+1)2)

-Time domain resource assignment - 0, 1, 2, 3, or 4 bits as defined in Clause 5.1.2.1 of [6, TS 38.214]. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter pdsch-TimeDomainAllocationList if the higher layer parameter is configured; otherwise I is the number of entries in the default table.log2(I)

-VRB-to-PRB mapping - 0 or 1 bit:

-0 bit if only resource allocation type 0 is configured or if vrb-ToPRB-Interleaver in pdsch-ConfigMulticast is not configured;

-1 bit according to Table 7.3.1.2.2-5 otherwise, only applicable to resource allocation type 1, as defined in Clause 7.3.1.6 of [4, TS 38.211].

-PRB bundling size indicator - 0 bit if the higher layer parameter prb-BundlingType is not configured in pdsch-ConfigMulticast or is set to 'staticBundling', or 1 bit if the higher layer parameter prb-BundlingType in pdsch-ConfigMulticast is set to 'dynamicBundling' according to Clause 5.1.2.3 of [6, TS 38.214].

-Rate matching indicator - 0, 1, or 2 bits according to higher layer parameters rateMatchPatternGroup1 and rateMatchPatternGroup2 in pdsch-ConfigMulticast, where the MSB is used to indicate rateMatchPatternGroup1 and the LSB is used to indicate rateMatchPatternGroup2 when there are two groups.

-ZP CSI-RS trigger - 0, 1, or 2 bits as defined in Clause 5.1.4.2 of [6, TS 38.214]. The bitwidth for this field is determined as  bits, where  is the number of aperiodic ZP CSI-RS resource sets configured in pdsch-ConfigMulticast.log2(nZP+1)nZP

For transport block 1:

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

For transport block 2 (only present if maxNrofCodeWordsScheduledByDCI configured in pdsch-ConfigMulticast equals 2):

-Modulation and coding scheme - 5 bits as defined in Clause 5.1.3.1 of [6, TS 38.214]

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-HARQ process number - 4 bits

-Downlink assignment index - number of bits as defined in the following

-2 bits if the higher layer parameter pdsch-HARQ-ACK-Codebook =dynamic is configured for multicast, where the 2 bits are the counter DAI;

-0 bits otherwise.

If higher layer parameter priorityIndicatorDCI-4-2 is configured in pdsch-ConfigMulticast, if the bit width of the Downlink assignment index in DCI format 4_2 for one HARQ-ACK codebook is not equal to that of the Downlink assignment index in DCI format 4_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller Downlink assignment index until the bit width of the Downlink assignment index in DCI format 4_2 for the two HARQ-ACK codebooks are the same.

-PUCCH resource indicator - 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]

-PDSCH-to-HARQ_feedback timing indicator - 0, 1, 2, or 3 bits as defined in Clause 9.2.3 of [5, TS 38.213]. The bitwidth for this field is determined as  bits, where I is the number of entries in the higher layer parameter dl-DataToUL-ACK in pucch-ConfigMulticast1 if configured or pucch-ConfigMulticast2 if configured; otherwise, I is the number of entries in the higher layer parameter dl-DataToUL-ACK in PUCCH-Config.log2(I)

If higher layer parameter priorityIndicatorDCI-4-2 is configured in pdsch-ConfigMulticast, if the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 4_2 for one HARQ-ACK codebook is not equal to that of the PDSCH-to-HARQ_feedback timing indicator in DCI format 4_2 for the other HARQ-ACK codebook, a number of most significant bits with value set to '0' are inserted to smaller PDSCH-to-HARQ_feedback timing indicator until the bit width of the PDSCH-to-HARQ_feedback timing indicator in DCI format 4_2 for the two HARQ-ACK codebooks are the same.

-Antenna port(s) - 4, 5, 6, 7 or 8 bits as defined by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10, where the number of CDM groups without data of values 1, 2, and 3 refers to CDM groups {0}, {0,1}, and {0, 1,2} respectively. The antenna ports  shall be determined according to the ordering of DMRS port(s) given by Tables 7.3.1.2.2-1/2/3/4/7/8/9/10.{p0,…,pv-1}

If a UE is configured with both dmrs-DownlinkForPDSCH-MappingTypeA and dmrs-DownlinkForPDSCH-MappingTypeB, the bitwidth of this field equals , where  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeA and  is the "Antenna ports" bitwidth derived according to dmrs-DownlinkForPDSCH-MappingTypeB. A number of  zeros are padded in the MSB of this field, if the mapping type of the PDSCH corresponds to the smaller value of  and .max⁡{xA,xB}xAxBxA-xBxAxB

-Transmission configuration indication - 0 bit if higher layer parameter tci-PresentInDCI in pdcch-ConfigMulticast is not enabled; otherwise 3 bits as defined in Clause 5.1.5 of [6, TS38.214].

-DMRS sequence initialization - 1 bit.

-Priority indicator - 0 bit if higher layer parameter priorityIndicatorDCI-4-2 is not configured in pdsch-ConfigMulticast; otherwise 1 bit as defined in Clause 9 in [5, TS 38.213].

-Enabling/disabling HARQ-ACK feedback indication -1 bit if higher layer parameter harq-FeedbackEnablerMulticast indicates dci-enabler, where value 1 indicates enabling HARQ-ACK feedback and value 0 indicates disabling HARQ-ACK feedback; 0 bit, otherwise.

The size of DCI format 4_2 is configurable by higher layer parameter sizeDCI-4-2 from 20 bits and up to 140 bits. If the number of information bits in DCI format 4_2 is less than the size of DCI format 4_2, the remaining bits are reserved.

## 7.3.2CRC attachment

Error detection is provided on DCI transmissions through a Cyclic Redundancy Check (CRC).

The entire payload is used to calculate the CRC parity bits. Denote the bits of the payload by, and the parity bits by, where  is the payload size and  is the number of parity bits. Let  be a bit sequence such that  for  and  for . The parity bits are computed with input bit sequence  and attached according to Clause 5.1 by setting  to 24 bits and using the generator polynomial . The output bit  is

for

for ,

where .

After attachment, the CRC parity bits are scrambled with the corresponding RNTI  , where  corresponds to the MSB of the RNTI, to form the sequence of bits . The relation between ck and bk is:

for k = 0, 1, 2, …,

for k = , ,,..., .

## 7.3.3Channel coding

Information bits are delivered to the channel coding block. They are denoted by  , where  is the number of bits, and they are encoded via Polar coding according to Clause 5.3.1, by setting , , , and .

After encoding the bits are denoted by , where  is the number of coded bits.

## 7.3.4Rate matching

The input bit sequence to rate matching is .

Rate matching is performed according to Clause 5.4.1 by setting .

The output bit sequence after rate matching is denoted as .

## 7.4Wake-up information

The wake-up information is carried by a wake-up signal as defined in clause 7.4.4 of [4, TS 38.211].

-For a UE configured with higher layer parameter lpwus-LPSS-StartRB and operating in the RRC_IDLE or RRC_INACTIVE state, the wake-up information bit sequence  is the binary sequence of the codepoint as defined by Clause 10.4C of [5, TS38.213], where  is the most significant bit and  isc0,c1,…,cK-1c0K

- if , where  is configured by higher layer parameter lpwus-PO-NumPerLO and  is configured by higher layer parameter lp-SubgroupsNumPerPO;maxlog2NPO, 1 NsubgroupPO=1NPONsubgroupPO

- if , where  is configured by higher layer parameter lp-SubgroupsNumPerPO; log2NPONsubgroupPO+1NsubgroupPO>1NsubgroupPO

-For a UE configured with higher layer parameter lpwus-StartRB and operating in the RRC_CONNECTED state, the wake-up information bit sequence  is the binary sequence of the codepoint as defined by Clause 10.4D of [5, TS38.213], where  is the most significant bit, isprovided by the higher layer parameter lpwus-NumOfBits.c0,c1,…,cK-1c0K

The following coding steps can be identified for the wake-up information:

-For the first bit block in case of OOK modulation

-Channel coding

-Rate matching

-Line coding

-For the second bit block in case of sequence modulation

-Rate matching

The first bit block and the second bit block, if both are present, are generated based on the same information bits.

## 7.4.1Channel coding

Information bits are delivered to the channel coding block. They are denoted by , where  is the number of bits and .c0,c1,…,cK-1KK≤5

The information bits are encoded according to Clause 5.3.3, where  is set to 1 when Table 5.3.3.1-1 or Table 5.3.3.2-1 is applied. Qm

After encoding the bits are denoted by , where  is the number of coded bits.d00,d01,…,d0N0-1N0

## 7.4.2Rate matching

## 7.4.2.1Rate matching for OOK modulation

The input bit sequence to rate matching is .d00,d01,…,d0N0-1

Rate matching is performed according to Clause 5.4.3 by setting the rate matching output sequence length , where , , whereE=E0E0=EWUSEWUS=NOS×MLP/2

-for a UE configured with higher layer parameter lpwus-LPSS-StartRB and operating in the RRC_IDLE or RRC_INACTIVE state,  is configured by higher layer parameter lpwus-ActualDuration and  is configured by higher layer parameter lpwus-MvalueAndSeqConfigFR1 or lpwus-MvalueAndSeqConfigFR2;NOSMLP

-for a UE configured with higher layer parameter lpwus-StartRB and operating in the RRC_CONNECTED state,  is configured by higher layer parameter lpwus-ActualDuration and  is configured by higher layer parameter lpwus-MvalueAndSeqConfigFR1 or lpwus-MvalueAndSeqConfigFR2.NOSMLP

The output bit sequence after rate matching is denoted as .f00,f01,f02,…,f0E0-1

## 7.4.2.2Rate matching for sequence modulation

Information bits for the second bit block are delivered to the rate matching block. They are denoted by , where  is the number of bits and .c0,c1,…,cK-1KK≤5

If the number of sequences configured by higher layer parameter lpwus-OverlaidSeqNum or lpwus-OverlaidSeqNum-SCS-60kHz or lpwus-OverlaidSeqNum-SCS-120kHz, denoted as , is larger than one, padding is performed and the bits after padding are denoted by, where , . The relation between  and  is:L1 d10,d11,…,d1N1-1N1=K+LL=-K  mod log2L1ckd1k

for d1k=0k=0,1,…, L-1

for .d1k=ck-L k=L,L+1,…, N1-1

Rate matching is performed according to Clause 5.4.3 by setting the rate matching output sequence length , where , is as defined in Clause 7.4.2.1, and the output bit sequence after rate matching is denoted as .E=E1 E1=EWUS×log2L1EWUS f10,f11,f12,…,f1E1-1

## 7.4.3Line coding

The input bit sequence to line coding block are the sequences . f00,f01,f02,…,f0E0-1

The bits after line coding are denoted by , where . g00,g01,…,g0G0-1 G0=2×E0

Line coding is performed according to the following by setting :i=0,1,…, E0-1

;g0(2i)=1-f0i

;g0(2i+1)= f0i

## 8Sidelink transport channels and control information

## 8.1Sidelink broadcast channel

The processing for SL-BCH transport channel follows the BCH according to clause 7.1, with the following changes:

-In Clause 7.1, 'maximum of one transport block every 80ms' is replaced with 'maximum of one transport block'.

-Clause 7.1.1 for PBCH payload generation is not performed.

-Clause 7.1.2 for scrambling is not performed.

-In clause 7.1.5, the rate matching output sequence length E = 1386 when higher layer parameter cyclicPrefix is configured, otherwise, E = 1782.

## 8.1.1Void

## 8.2Sidelink shared channel

The processing for SL-SCH transport channel follows the UL-SCH according to clause 6.2, with the following changes:

-Rate matching of SL-SCH follows the rate matching according to clause 6.2.5 by setting ILBRM=0

-Clause 6.2.7 is replaced by clause 8.2.1

## 8.2.1Data and control multiplexing

Denote the coded bits for SL-SCH as.  g0SL-SCH, g1SL-SCH, g2SL-SCH, g3SL-SCH,⋯, gGSL-SCH-1SL-SCH

Denote the coded bits for the 2nd-stage SCI, as .g0SCI2, g1SCI2, g2SCI2, g3SCI2,⋯, gGSCI2-1SCI2

Denote the multiplexed data and control coded bit sequence as , where G is the total number of coded bits for transmission.g0,g1,⋯,gG-1

Assuming that  is the number of layers onto which the SL-SCH transport block is mapped, the multiplexed data and control coded bit sequence  is obtained as follows:NLg0,g1,⋯,gG-1

Denote  is modulation order of the 2nd-stage SCI.QmSCI2

if , NL=1

for  to i=0GSCI2+GSL-SCH-1

if 0≤i<GSCI2

gi=giSCI2

end if

if GSCI2≤i≤GSCI2+GSL-SCH-1

gi=gi-GSCI2SL-SCH

end if

end for

end if

if ,NL=2

let Mcount,SCI2RE=GSCI2/QmSCI2

set mcountRE=0

for  to  i=0Mcount,SCI2RE-1

for  to v=0NL-1

for  to  q=0QmSCI2-1

if v=0

gmcountRE=gi∙QmSCI2+qSCI2

else

// placeholder bitgmcountRE=x

end if

mcountRE=mcountRE+1

end for

end for

end for

for  to  i=0GSL-SCH-1

gmcountRE=giSL-SCH

mcountRE=mcountRE+1

end for

end if

## 8.3Sidelink control information on PSCCH

SCI carried on PSCCH is a 1st-stage SCI, which transports sidelink scheduling information.

## 8.3.11st-stage SCI formats

The fields defined in each of the 1st-stage SCI formats below are mapped to the information bits  to as follows:a0aA-1

Each field is mapped in the order in which it appears in the description, with the first field mapped to the lowest order information bit and each successive field mapped to higher order information bits. The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to .a0 a0

## 8.3.1.1SCI format 1-A

SCI format 1-A is used for the scheduling of PSSCH and 2nd-stage-SCI on PSSCH

The following information is transmitted by means of the SCI format 1-A:

-Priority - 3 bits as specified in clause 5.4.3.3 of [12, TS 23.287] and clause 5.22.1.3.1 of [8, TS 38.321]. Value '000' of Priority field corresponds to priority value '1', value '001' of Priority field corresponds to priority value '2', and so on.

-Frequency resource assignment - number of bits determined by the following:

-If higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is not configured or configured to ‘contiguousRB’

- bits when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 2; otherwise  bits when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 3, as defined in clause 8.1.5 of [6, TS 38.214].log2(N subChannel SLN subChannel SL + 12)log2(N subChannel SLN subChannel SL + 12N subChannel SL + 16)

-If the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured to ‘interlaceRB’

-X + Y bits provide the frequency domain resource allocation according to Clause 8.1.5 of [6, TS 38.214], where the X MSBs provide the RB set allocation and the Y LSBs provide the sub-channel allocation,

-the value of X is determined by  when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 2, or determined by  when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 3, where  is the number of RB sets in a resource poollog2(NRBsetNRBset + 12) log2(NRBsetNRBset + 12NRBset + 16)NRBset

-the value of Y is determined by when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 2, or determined by  when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 3, as defined in clause 8.1.5 of [6, TS 38.214]. log2(N subChannel SLN subChannel SL + 12) log2(N subChannel SLN subChannel SL + 12N subChannel SL + 16)

-Time resource assignment - 5 bits when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 2; otherwise 9 bits when the value of the higher layer parameter sl-MaxNumPerReserve is configured to 3, as defined in clause 8.1.5 of [6, TS 38.214].

-Resource reservation period - bits as defined in clause 16.4 of [5, TS 38.213], where  is the number of entries in the higher layer parameter sl-ResourceReservePeriodList, if higher layer parameter sl-MultiReserveResource is configured; 0 bit otherwise.log2Nrsv_periodNrsv_period

-DMRS pattern - bits as defined in clause 8.4.1.1.2 of [4, TS 38.211], where  is the number of DMRS patterns configured by higher layer parameter sl-PSSCH-DMRS-TimePatternList. log2NpatternNpattern

-2nd-stage SCI format - 2 bits as defined in Table 8.3.1.1-1.

-Beta_offset indicator - 2 bits as provided by higher layer parameter sl-BetaOffsets2ndSCI and Table 8.3.1.1-2.

-Number of DMRS port - 1 bit as defined in Table 8.3.1.1-3.

-Modulation and coding scheme - 5 bits as defined in clause 8.1.3 of [6, TS 38.214].

-Additional MCS table indicator - as defined in clause 8.1.3.1 of [6, TS 38.214]: 1 bit if one MCS table is configured by higher layer parameter sl-Additional-MCS-Table; 2 bits if two MCS tables are configured by higher layer parameter sl-Additional-MCS-Table; 0 bit otherwise.

-PSFCH overhead indication - 1 bit as defined in clause 8.1.3.2 of [6, TS 38.214] if higher layer parameter sl-PSFCH-Period = 2 or 4; 0 bit otherwise.

-Reserved - a number of bits as determined by the following:

-bits as configured by higher layer parameter sl-NumReservedBits, with value set to zero, if higher layer parameter sl-IndicationUE-B is not configured, or if higher layer parameter sl-IndicationUE-B is configured to 'disabled', and if higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is not configured;Nreserved

- bits if higher layer parameter sl-IndicationUE-B is configured to 'enabled', and if higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured, with value set to zero.(Nreserved-2)

- bits otherwise, with value set to zero.(Nreserved-1)

-COT sharing flag – 0 or 1 bit

-1 bit if the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured;

-0 bit otherwise.

-Conflict information receiver flag - 0 or 1 bit

-1 bit if higher layer parameter sl-IndicationUE-B is configured to 'enabled', where the bit value of 0 indicates that the UE cannot be a UE to receive conflict information and the bit value of 1 indicates that the UE can be a UE to receive conflict information as defined in Clause 16.3.0 of [5, TS 38.213];

-0 bit otherwise.

Table 8.3.1.1-1: 2nd-stage SCI formats

Table 8.3.1.1-2: Mapping of Beta_offset indicator values to indexes in Table 9.3-2 of [5, TS38.213]

Table 8.3.1.1-3: Number of DMRS port(s)

## 8.3.1.2SCI format 1-B

SCI format 1-B is used for the scheduling of SL PRS for a dedicated SL PRS resource pool.

The following information is transmitted by means of the SCI format 1-B:

-Priority - 3 bits as specified in clause 5.7 of [12, TS 23.586] and clause 5.22 of [8, TS 38.321]. Value '000' of Priority field corresponds to priority value '1', value '001' of Priority field corresponds to priority value '2', and so on.

-Source ID – 12 or 24 bits determined by higher layer parameter sl-SRC-ID-LenDedicatedSL-PRS-RP, as defined in clause 16.4A of [5, TS 38.213].

-Destination ID – 24 bits as defined in clause 16.4A of [5, TS 38.213].

-Cast type indicator – 2 bits as defined in Table 8.3.1.2-1 and in clause 16.4A of [5, TS 38.213].

-Resource reservation period –  bits as defined in clause 16.4A of [5, TS 38.213], where  is the number of entries in the higher layer parameter sl-PRS-ResourceReservePeriodList, if higher layer parameter sl-PRS-ResourceReservePeriodList is configured; 0 bit otherwise.log2Nrsv_periodNrsv_period

-Time resource assignment – 5 bits when the value of the higher layer parameter sl-MaxNumPerReserveDedicatedSL-PRS-RP is configured to 2; otherwise 9 bits when the value of the higher layer parameter sl-MaxNumPerReserveDedicatedSL-PRS-RP is configured to 3, as defined in clause 8.2.4.2A of [6, TS 38.214].

-Resource ID indication –bits when the value of the higher layer parameter sl-MaxNumPerReserveDedicatedSL-PRS-RP is configured to 2; otherwise  bits when the value of the higher layer parameter sl-MaxNumPerReserveDedicatedSL-PRS-RP is configured to 3. The value  is the total number of SL PRS resources within a slot in a dedicated SL PRS resource pool and provided by the higher layer parameter sl-PRS-ResourcesDedicatedSL-PRS-RP. log2NSL-PRS 2log2NSL-PRSNSL-PRS

-SL PRS request – 1 bit as defined in clause 8.4.4 of [6, TS 38.214] when the higher layer parameter sl-SCI-basedSL-PRS-TxTriggerSCI1-B is provided; 0 bit otherwise.

-Reserved –  bits as configured by higher layer parameter sl-NumReservedBitsSCI1B-DedicatedSL-PRS-RP, with value set to zero.Nreserved

Table 8.3.1.2-1: Cast type indicator

## 8.3.2CRC attachment

CRC attachment is performed according to clause 7.3.2 except that scrambling is not performed.

## 8.3.3Channel coding

Channel coding is performed according to clause 7.3.3.

## 8.3.4Rate Matching

Rate matching is performed according to clause 7.3.4.

## 8.4Sidelink control information on PSSCH

SCI carried on PSSCH is a 2nd-stage SCI, which transports sidelink scheduling information, and/or inter-UE coordination related information.

## 8.4.12nd-stage SCI formats

The fields defined in each of the 2nd-stage SCI formats below are mapped to the information bits   to  as follows:a0aA-1

Each field is mapped in the order in which it appears in the description, with the first field mapped to the lowest order information bit and each successive field mapped to higher order information bits. The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to .a0 a0

## 8.4.1.1SCI format 2-A

SCI format 2-A is used for the decoding of PSSCH, with HARQ operation when HARQ-ACK information includes ACK or NACK, when HARQ-ACK information includes only NACK, or when there is no feedback of HARQ-ACK information.

The following information is transmitted by means of the SCI format 2-A:

-HARQ process number -  bits.4

-New data indicator - 1 bit.

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2.

-Source ID - 8 bits as defined in clause 8.1 of [6, TS 38.214].

-Destination ID - 16 bits as defined in clause 8.1 of [6, TS 38.214].

-HARQ feedback enabled/disabled indicator - 1 bit as defined in clause 16.3 of [5, TS 38.213].

-Cast type indicator - 2 bits as defined in Table 8.4.1.1-1 and in clause 8.1 of [6, TS 38.214].

-CSI request - 1 bit as defined in clause 8.2.1 of [6, TS 38.214] and in clause 8.1 of [6, TS 38.214].

If the 'COT sharing flag' field in SCI format 1-A is present and set to '1', all the remaining fields are present and set as follows:

-CAPC – 2 bits. Values '00', '01', '10' and '11' correspond to CAPC values '1', '2', '3' and '4' as defined in Table 4.5-1 of [14, TS 37.213], respectively.

-COT sharing cast type – 2 bits as defined in Table 8.4.1.1-1.

-COT sharing additional ID – 24 bits. The 16 LSBs provide layer 1 destination ID and the 8 MSBs provide layer 1 source ID, as defined in [6, TS 38.214]. The 8 MSBs are reserved when the COT sharing cast type field is set to '00' or '01'.

-Remaining COT duration –  bits as defined in clause 4.5.3 of [14, TS 37.213], where  is defined in Table 4.2-1 of Clause 4.2 of [4, TS 38.211].log2(10∙2μ)μ

Table 8.4.1.1-1: Cast type indicator or COT sharing cast type

## 8.4.1.2SCI format 2-B

SCI format 2-B is used for the decoding of PSSCH, with HARQ operation when HARQ-ACK information includes only NACK, or when there is no feedback of HARQ-ACK information.

The following information is transmitted by means of the SCI format 2-B:

-HARQ process number -  bits.4

-New data indicator - 1 bit.

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2.

-Source ID - 8 bits as defined in clause 8.1 of [6, TS 38.214].

-Destination ID - 16 bits as defined in clause 8.1 of [6, TS 38.214].

-HARQ feedback enabled/disabled indicator - 1 bit as defined in clause 16.3 of [5, TS 38.213].

-Zone ID - 12 bits as defined in clause 5.8.11 of [9, TS 38.331].

-Communication range requirement - 4 bits determined by higher layer parameter sl-ZoneConfigMCR-Index.

## 8.4.1.3SCI format 2-C

SCI format 2-C is used for the decoding of PSSCH, and providing inter-UE coordination information or requesting inter-UE coordination information. SCI format 2-C can be used only for unicast.

The following information is transmitted by means of the SCI format 2-C:

-HARQ process number - 4 bits

-New data indicator - 1 bit

-Redundancy version - 2 bits as defined in Table 7.3.1.1.1-2

-Source ID - 8 bits as defined in clause 8.1 of [6, TS 38.214]

-Destination ID - 16 bits as defined in clause 8.1 of [6, TS 38.214]

-HARQ feedback enabled/disabled indicator - 1 bit as defined in clause 16.3 of [5, TS 38.213]

-CSI request - 1 bit as defined in clause 8.2.1 of [6, TS 38.214] and in clause 8.1 of [6, TS 38.214]

-Providing/Requesting indicator - 1 bit, where value 0 indicates SCI format 2-C is used for providing inter-UE coordination information and value 1 indicates SCI format 2-C is used for requesting inter-UE coordination information

If the 'Providing/Requesting indicator' field is set to 0, all the remaining fields are set as follows:

-Resource combinations -number of bits determined by the following:

-If higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is not configured or configured to 'contiguousRB'

- bits as defined in Clause 8.1.5A of [6, TS 38.214];2∙log2(N subChannel SLN subChannel SL + 12N subChannel SL + 16)+9+Y

-If the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured to 'interlaceRB'

- bits as defined in Clause 8.1.5A of [6, TS 38.214];2∙log2(N subChannel SLN subChannel SL + 12N subChannel SL + 16)+log2(NRBsetNRBset + 12NRBset + 16)+9+Y

where

- and  is the number of entries in the higher layer parameter sl-ResourceReservePeriodList, if higher layer parameter sl-MultiReserveResource is configured; otherwise.Y=log2Nrsv_periodNrsv_period Y=0

- is provided by the higher layer parameter sl-NumSubchannel as defined in Clause 8.1.5 of [6, TS 38.214].N subChannel SL

- is the number of RB sets in a resource pool.NRBset

-First resource location - 8 bits as defined in Clause 8.1.5A of [6, TS 38.214].

-Reference slot location - ( bits as defined in Clause 8.1.5A of [6, TS 38.214], where  is defined in Table 4.2-1 of Clause 4.2 of [4, TS 38.211].10+log2(10∙2μ))μ

-Resource set type - 1 bit, where value 0 indicates preferred resource set and value 1 indicates non-preferred resource set.

-Lowest subChannel indices -  bits as defined in Clause 8.1.5A of [6, TS 38.214].2∙log2N subChannel SL

-Lowest RB set indices -  bits as defined in Clause 8.1.5A of [6, TS 38.214] if the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured to 'interlaceRB'; 0 bit otherwise.2∙log2NRBset

If the 'Providing/Requesting indicator' field is set to 1, all the remaining fields are set as follows:

-Priority - 3 bits as specified in clause 5.4.3.3 of [12, TS 23.287] and clause 5.22.1.3.1 of [8, TS 38.321]. Value '000' of Priority field corresponds to priority value '1', value '001' of Priority field corresponds to priority value '2', and so on.

-Number of subchannels - bits as defined in Clause 8.1.4A of [6, TS 38.214]. log2N subChannel SL

-Number of RB sets -  bits as defined in Clause 8.1.4A of [6, TS 38.214] if the higher layer parameter sl-TransmissionStructureForPSCCHandPSSCH in SL-BWP-Config is configured to 'interlaceRB'; 0 bit otherwise.log2NRBset

-Resource reservation period - bits as defined in Clause 8.1.4A of [6, TS 38.214], where  is the number of entries in the higher layer parameter sl-ResourceReservePeriodList, if higher layer parameter sl-MultiReserveResource is configured; 0 bit otherwise. log2Nrsv_periodNrsv_period

-Resource selection window location -  bits as defined in Clause 8.1.4A of [6, TS 38.214], where  is defined in Table 4.2-1 of Clause 4.2 of [4, TS 38.211].2∙10+log2(10∙2μ)μ

-Resource set type - 1 bit, where value 0 indicates a request for inter-UE coordination information providing preferred resource set and value 1 indicates a request for inter-UE coordination information providing non-preferred resource set, if higher layer parameter sl-DetermineResourceType is configured to 'ueb'; otherwise, 0 bit.

-Padding bits.

For operation in a same resource pool, zeros shall be appended to SCI format 2-C of which 'Providing/Requesting indicator' field is set to 1 until the payload size equals that of SCI format 2-C of which 'Providing/Requesting indicator' field is set to 0.

## 8.4.1.4SCI format 2-D

SCI format 2-D is used for the decoding of PSSCH and the scheduling of SL PRS for a shared SL PRS resource pool.

The following information is transmitted by means of the SCI format 2-D:

-SL PRS resource ID -bits, where the value  is the total number of SL PRS resource IDs within a slot in a shared SL PRS resource pool and provided by the higher layer parameter sl-PRS-ResourcesSharedSL-PRS-RP. log2NSL-PRS NSL-PRS

-SL PRS request – 1 bit as defined in clause 8.4.4 of [6, TS 38.214] when the higher layer parameter sl-SCI-basedSL-PRS-TxTriggerSCI2-D is provided; 0 bit otherwise.

-Embedded SCI format - 2 bits. This field indicates the embedded SCI format as defined in Table 8.4.1.4-1.

-Embedded SCI format payload - number of bits determined according to Table 8.4.1.4-1. This field is set to the associated payload of the embedded SCI format indicated by the ‘Embedded SCI format’ field as defined in Table 8.4.1.4-1.

Table 8.4.1.4-1: Embedded SCI format and payload

## 8.4.2CRC attachment

CRC attachment is performed according to clause 7.3.2 except that scrambling is not performed.

## 8.4.3Channel coding

Channel coding is performed according to clause 7.3.3.

## 8.4.4Rate Matching

For 2nd-stage SCI transmission on PSSCH with SL-SCH, the number of coded modulation symbols generated for 2nd-stage SCI transmission prior to duplication for the 2nd layer if present, denoted as , is determined as follows:QSCI2'

QSCI2'=minOSCI2+LSCI2∙βoffsetSCI2QmSCI2∙R, αl=0NsymbolPSSCH-1MscSCI2(l)+γ

where

- is the number of the 2nd-stage SCI bits OSCI2

- is the number of CRC bits for the 2nd-stage SCI, which is 24 bits. LSCI2

- is indicated in the corresponding 1st-stage SCI. βoffsetSCI2

- is the number of allocated PRBs of PSSCH transmission according to clause 8.1.3.2 in [6, TS 38.214], expressed as a number of subcarriers. MscPSSCH(l)nPRB

- is the number of subcarriers in OFDM symbol  that carry PSCCH and PSCCH DMRS associated with the PSSCH transmission.MscPSCCH(l)l

- is the number of resource elements that can be used for transmission of the 2nd-stage SCI in OFDM symbol , for  and for , in PSSCH transmission, where  = sl-lengthSymbols - 2, where sl-lengthSymbols is the number of sidelink symbols within the slot provided by higher layers as defined in [6, TS 38.214].  is the number of symbols for SL PRS provided by the higher layer parameter numSym-SL-PRS-2ndStageSCI if the 2nd-stage SCI is SCI format 2-D, and  = 0 otherwise. If sl-StartingSymbolFirst and sl-StartingSymbolSecond are provided for the SL-BWP,  = sl-NumRefSymbolLength - 2, where sl-NumRefSymbolLength is provided by higher layers. If higher layer parameter sl-PSFCH-Period = 2 or 4,  = 3 if "PSFCH overhead indication" field of SCI format 1-A indicates "1", and  = 0 otherwise. If higher layer parameter sl-PSFCH-Period = 0, . If higher layer parameter sl-PSFCH-Period is 1, .MscSCI2(l)ll=0,1,2⋯,NsymbolPSSCH-1NsymbolPSSCH=Nsymbsh-NsymbPSFCH-NsymbSL PRSNsymbshNsymbslotNsymbSL PRSNsymbSL PRSNsymbshNsymbslotNsymbPSFCHNsymbPSFCHNsymbPSFCH=0NsymbPSFCH=3

- =  -  MscSCI2(l)MscPSSCH(l)MscPSCCH(l)

- is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs.γ

- is the coding rate as indicated by "Modulation and coding scheme" field in SCI format 1-A.R

- is configured by higher layer parameter sl-Scaling.α

The input bit sequence to rate matching is , where  is the number of coded bits.d0, d1,d2,d3, ⋯,dN-1N

Rate matching is performed according to Clause 5.4.1 by setting .IBIL=1

The output bit sequence after rate matching is denoted as , where  and  is modulation order of the 2nd-stage SCI. A UE is not expected to have.g0SCI2, g1SCI2, g2SCI2, g3SCI2,⋯, gGSCI2-1SCI2GSCI2=QSCI2'∙ QmSCI2QmSCI2 GSCI2>4096

## 8.4.5Multiplexing of coded 2nd-stage SCI bits to PSSCH

The coded 2nd-stage SCI bits are multiplexed onto PSSCH according to the procedures in Clause 8.2.1.

## Annex A (informative):Change history
