# TS 38.101 38101-3-j60_sAnnexes

## Annex A (normative):Measurement channels

## A.1General

The throughput values defined in the measurement channels specified in Annex A, are calculated and are valid per datastream (codeword). For multi-stream (more than one codeword) transmissions, the throughput referenced in the minimum requirements is the sum of throughputs of all datastreams (codewords).

The UE category entry in the definition of the reference measurement channel in Annex A is only informative and reveals the UE categories, which can support the corresponding measurement channel. Whether the measurement channel is used for testing a certain UE category or not is specified in the individual minimum requirements.

## A.2UL reference measurement channels for E-UTRA TDD Config 2

## A.2.1General

The measurement channels in the following clauses are defined to derive the requirements in clause 6 (Transmitter Characteristics) and clause 7 (Receiver Characteristics). The measurement channels represent example configurations of physical channels for different data rates.

## A.2.2Reference measurement channels for E-UTRA

## A.2.2.1Full RB allocation

## A.2.2.1.1QPSK

Table A.2.2.1.1-1: Reference Channels for QPSK with full RB allocation

## A.2.2.1.216-QAM

Table A.2.2.1.2-1: Reference Channels for 16-QAM with full RB allocation

## A.2.2.1.364-QAM

Table A.2.2.1.3-1: Reference Channels for 64-QAM with full RB allocation

## A.2.2.1.4256 QAM

Table A.2.2.1.4-1: Reference Channels for 256 QAM with full RB allocation

## A.2.2.2Partial RB allocation

## A.2.2.2.1QPSK

Table A.2.2.2.1-1: Reference Channels for QPSK with partial RB allocation

A.2.2.2.216-QAM

Table A.2.2.2.2-1: Reference Channels for 16QAM with partial RB allocation

## A.2.2.2.364-QAM

Table A.2.2.2.3-1: Reference Channels for 64-QAM with partial RB allocation

## A.2.2.2.4256 QAM

Table A.2.2.2.4-1: Reference Channels for 256 QAM with partial RB allocation

## A.3DL reference measurement channels for E-UTRA

## A.3.1General

The number of available channel bits varies across the sub-frames due to PBCH and PSS/SSS overhead. The payload size per sub-frame is varied in order to keep the code rate constant throughout a frame.

Unless otherwise stated, no user data is scheduled on subframes #5 in order to facilitate the transmission of system information blocks (SIB).

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1.Calculate the number of channel bits Nch that can be transmitted during the first transmission of a given sub-frame.

2.Find A such that the resulting coding rate is as close to R as possible, that is,

,

subject to

a)A is a valid TB size according to clause 7.1.7 of TS 36.213 [6] assuming an allocation of NRB resource blocks.

b)C is the number of Code Blocks calculated according to clause 5.1.2 of TS 36.212 [5].

3.If there is more than one A that minimizes the equation above, then the larger value is chosen per default and the chosen code rate should not exceed 0.93.

4.For TDD, the measurement channel is based on DL/UL configuration ratio of 3DL+DwPTS (10 OFDM symbol SSF7): 1UL

## A.3.1.1QPSK

Table A.3.1.1-1: Fixed Reference Channel for Receiver Requirements (TDD)

## A.3.1.264-QAM

Table A.3.1.2-1: Fixed Reference Channel for Maximum input level for UE Categories ≥ 3 (TDD)

## A.3.1.3256-QAM

Table A.3.1.3-1: Fixed Reference Channel for Maximum input level for UE Categories 11/12 and UE DL categories ≥ 11 (TDD)

## Annex B:Void

## Annex C:Void

## Annex D:Void

## Annex E:Void

## Annex F:Void

## Annex G:Void

## Annex H (normative):Modified MPR behavior

The definitions of the bits in the modifiedMPR-Behaviour field have been moved to Annex H of 38.101-1[2].

## Annex I (normative):Dual uplink interferer

UE is mandated to support operation in dual and triple uplink mode for EN-DC configuration in NR FR1 listed in Table 5.5B.2-1, Table 5.5B.3-1, and Table 5.5B.4.1-1 and indicated by column single uplink allowed, Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.2-0, Table 7.3B.2.3.5.2-1 or NE-DC configuration in NR FR1 listed in Table 5.5B.4a.1-1 and indicated by column single uplink allowed if the intermodulation products caused by the dual uplink operation do not interfere with its own primary downlink transmission channel bandwidth of PCell or PSCell. For intermodulation products falling into any secondary downlink channel bandwidth, UE single UL capability is not considered.

Formula for determining if the EN-DC in NR FR1 configuration with dual uplink operation interferes with its own downlink reception.

Interference bandwidth: IBW = |a| * CBW1 + |b| * CBW2

-|a| + |b| = 2 (or 3)

-CBW1 and CBW2 are the transmission bandwidth configurations of the UL channels

Center frequency of IBW:  fIBW = |a * f1 + b * f2|

-f1 and f2 are center frequency of the transmission bandwidth configurations of each UL channel

The range of IMD 2 (or 3): [fIBW – IBW/2, fIBW + IBW/2]

NOTE 1:UE shall be able to apply operations which are configured by RRC reconfiguration and corresponding HARQ timing on the transmission bandwidth.

NOTE 2:For identified difficult band combination, during two adjacent RRC reconfiguration, the changing of transmission bandwidth should not introduce IM2 and IM3, which will result in UE changing from 2Tx to 1Tx. Otherwise, UE behavior is not specified.

For DC_3A_n3A intra-band non-contiguous EN-DC combination, only single switched UL is supported in Rel-15.

For DC_2A_n2A, DC_5A_n5A, DC_7A_n7A, DC_48A_n48A, DC_66A_n66A, DC_71A_n71A intra-band non-contiguous EN-DC combination, and DC_(n)5AA,  DC_(n)12AA, DC_(n)38AA, DC_(n)48AA intra-band contiguous EN-DC combination,only single switched UL is supported.

## Annex J:Void

## Annex K:Void

## Annex L (informative):Change history
