# 14 UE procedures related to Sidelink

A UE can be configured by higher layers with one or more PSSCH resource configuration(s). A PSSCH resource configuration can be for reception of PSSCH, or for transmission of PSSCH. The physical sidelink shared channel related procedures are described in Clause 14.1.

A UE can be configured by higher layers with one or more PSCCH resource configuration(s). A PSCCH resource configuration can be for reception of PSCCH, or for transmission of PSCCH and the PSCCH resource configuration is associated with either sidelink transmission mode 1,2,3 or sidelink transmission mode 4. The physical sidelink control channel related procedures are described in Clause 14.2.

A UE can be configured by higher layers with one or more PSDCH resource configuration(s). A PSDCH resource configuration can be for reception of PSDCH, or for transmission of PSDCH. The transmissions of PSDCH according to a PSDCH resource configuration are associated with either sidelink discovery type 1 or sidelink discovery type 2B. The physical sidelink discovery channel related procedures are described in Clause 14.3.

The physical sidelink synchronization related procedures are described in Clause 14.4.

Except in the case of secondary sidelink synchronization signal transmission, sidelink transmission power shall not change during a sidelink subframe. For a UE transmitting PSBCH, the transmit power of PSBCH (![](media_svg/image1.svg) [公式≈: ^{P}PSBCH]) is same as the transmit power of primary sidelink synchronisation signal ![](media_svg/image2.svg) [公式≈: ^{P}PSSS].

A UE is not expected to be configured with PSCCH resource configuration(s) such that, in a given subframe, the total number of resource blocks across the resource block pools (as described in Clause 14.2.3) indicated by the PSCCH resource configuration(s) exceeds 50 in sidelink transmission mode 1 or 2.

In sidelink transmission mode 3 or 4, a UE is

- not expected to attempt to decode more than 10 or 20 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r14.

- not expected to attempt to decode more than 100 or 136 RBs in a subframe depending on the configuration of v2x-HighReception-r14.

- not expected to attempt to decode more than 10 or 20 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

- not expected to attempt to decode more than 100 or 136 RBs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

- not expected to attempt to decode more than 15 or 30 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

- not expected to attempt to decode more than 150 or 204 RBs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

- not expected to combine PSCCH transmitted in different subframes.

- not required to perform PSSCH-RSRP measurement in a subframe that occurs before the reception of a successfully decoded associated SCI format 1.

If the UE does not indicate capability v2x-HighReception-r14 or v2x-HighReception-r15, it shall implement a mechanism to avoid systematic dropping of PSCCH when the number of PSCCH candidates exceeds the UE's capability. UE applies the PSSCH-RSRP measured in a subframe that occurs at the reception of a successfully decoded associated SCI format 1 to a subframe that is indicated by the SCI format 1 but occurs before the reception of the SCI format 1. UE applies the PSSCH-RSRP measured in a subframe that occurs at the reception of a successfully decoded associated SCI format 1 to a subframe that is indicated by the SCI format 1 if SCI format 1 scheduling the same transport block is successfully decoded in only one subframe. UE is not expected to decode PSSCH that occurs before the reception of a successfully decoded associated SCI format 1.

If a UE uplink transmission that is not a PRACH transmission in subframe n+1 of a serving cell overlaps in time domain with a PSDCH transmission or a SLSS transmission for PSDCH by the UE in subframen and subframe n+1 is included in discTxGapConfig [11], then the UE shall drop the uplink transmission in subframe n+1. Else, if a UE uplink transmission in subframe n+1 of a serving cell overlaps in time domain with sidelink transmission/reception for sidelink transmission mode 1 or 2 by the UE in subframen of the serving cell, then the UE shall drop the sidelink transmission/reception in subframe n.

If a UE uplink transmission of a serving cell overlaps in time domain with a sidelink transmission for sidelink transmission mode 3 or 4 of the same serving cell and the value in "Priority" field of the corresponding SCI is smaller than the high layer parameter thresSL-TxPrioritization, then the UE shall drop the uplink transmission. Else, if a UE uplink transmission of a serving cell overlaps in time domain with sidelink transmission for sidelink transmission mode 3 or 4 of the same serving cell, then the UE shall drop the sidelink transmission.

For a given carrier frequency, a UE is not expected to receive sidelink physical channels/signals with different cyclic prefix lengths in the same sidelink subframe.

For a given carrier frequency, in a sidelink subframe, if a UE has a sidelink transmission, the sidelink transmission shall occur only in contiguous physical resource blocks in sidelink transmission mode 1 or 2.

In sidelink transmission mode 1 or 2, if a UE's sidelink transmission does not occur on a serving cell with its uplink transmission(s), and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s), the UE shall adjust the sidelink transmission power such that its total transmission power does not exceed![](media_svg/image3.svg) [公式≈: ^{P}CMAX]defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the sidelink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission has SCI whose "Priority" field is set to a value smaller than the high layer parameter thresSL-TxPrioritization, and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s) occurring on serving cell(s) where the sidelink transmission does not occur, the UE shall adjust the uplink transmission power such that its total transmission power does not exceed![](media_svg/image3.svg) [公式≈: ^{P}CMAX]defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the uplink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission has SCI whose "Priority" field is set to a value greater than or equal to the high layer parameter thresSL-TxPrioritization, and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s) occurring on serving cell(s) where the sidelink transmission does not occur, the UE shall adjust the sidelink transmission power such that its total transmission power does not exceed![](media_svg/image3.svg) [公式≈: ^{P}CMAX]defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the sidelink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission on a carrier overlaps in time with sidelink transmission on other carrier(s) and its total transmission power exceeds![](media_svg/image3.svg) [公式≈: ^{P}CMAX]defined in [6], the UE shall adjust the transmission power of the sidelink transmission which has SCI whose "Priority" field is set to the largest value among all the "Priority" values of the overlapped sidelink transmissions such that its total transmission power does not exceed ![](media_svg/image3.svg) [公式≈: ^{P}CMAX]defined in [6]. In this case, calculation of the adjustment to the sidelink transmission power is not specified. If the transmission power still exceeds ![](media_svg/image3.svg) [公式≈: ^{P}CMAX] defined in [6] after this power adjustment, the UE shall drop the sidelink transmission with the largest "Priority" field in its SCI and repeat this procedure over the non-dropped carriers. It is not specified which sidelink transmission the UE adjusts when sidelink transmissions overlapping in time on two or more carriers have the same value for the "Priority" field.

## 14.1 Physical Sidelink Shared Channel related procedures

### 14.1.1 UE procedure for transmitting the PSSCH

If the UE transmits SCI format 0 on PSCCH according to a PSCCH resource configuration in subframe n belonging to a PSCCH period (described in Clause 14.2.3), then for the corresponding PSSCH transmissions

- the transmissions occur in a set of subframes in the PSCCH period and in a set of resource blocks within the set of subframes. The first PSSCH transport block is transmitted in the first four subframes in the set, the second transport block is transmitted in the next four subframes in the set, and so on.

- for sidelink transmission mode 1,

- the set of subframes is determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.4) and using time resource pattern (![](media_svg/image4.svg) [公式≈: ^{I}TRP]) in the SCI format 0 as described in Clause 14.1.1.1.

- the set of resource blocks is determined using Resource block assignment and hopping allocation in the SCI format 0 as described in Clause 14.1.1.2.

- for sidelink transmission mode 2,

- the set of subframes is determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.3) and using time resource pattern (![](media_svg/image4.svg) [公式≈: ^{I}TRP]) in the SCI format 0 as described in Clause 14.1.1.3.

- the set of resource blocks is determined using the resource block pool indicated by the PSSCH resource configuration (described in Clause 14.1.3) and using Resource block assignment and hopping allocation in the SCI format 0 as described in Clause 14.1.1.4.

- the modulation order is determined using the "modulation and coding scheme " field (![](media_svg/image5.svg) [公式≈: ^{I}MCS]) in SCI format 0. For![](media_svg/image6.svg) [公式: 028≥≥I_{MCS}], the modulation order is set to ![](media_svg/image7.svg) [公式: QQ±±=min(4,)_{m}], where ![](media_svg/image8.svg) [公式≈: ^{Q}m^{±}]is determined from Table 8.6.1-1.

- the TBS index (![](media_svg/image9.svg) [公式≈: ^{I}TBS]) is determined based on![](media_svg/image5.svg) [公式≈: ^{I}MCS]and Table 8.6.1-1, and the transport block size is determined using ![](media_svg/image9.svg) [公式≈: ^{I}TBS] and the number of allocated resource blocks (![](media_svg/image10.svg) [公式≈: ^{N}PRB]) using the procedure in Clause 7.1.7.2.1.

If the UE transmits SCI format 1 on PSCCH according to a PSCCH resource configuration in subframe n, then for the corresponding PSSCH transmissions of one TB

- for sidelink transmission mode 3,

- the set of subframes and the set of resource blocks are determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.5) and using "Retransmission index and Time gap between initial transmission and retransmission" field and "Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 as described in Clause 14.1.1.4A.

- for sidelink transmission mode 4,

- the set of subframes and the set of resource blocks are determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.5) and using "Retransmission index and Time gap between initial transmission and retransmission" field and "Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 as described in Clause 14.1.1.4B.

- if higher layer indicates that rate matching for the last symbol in the subframe is used for the given PSSCH

- Transmission Format of corresponding SCI format 1 is set to 1,

- the modulation order is determined using the "modulation and coding scheme " field (![](media_svg/image5.svg) [公式≈: ^{I}MCS]) in SCI format 1.

- for ![](media_svg/image11.svg) [公式: 028≥≥I_{MCS}], the TBS index (![](media_svg/image9.svg) [公式≈: ^{I}TBS]) is determined based on![](media_svg/image5.svg) [公式≈: ^{I}MCS]and Table 8.6.1-1,

- for ![](media_svg/image12.svg) [公式: 2931≥≥I_{MCS}], the TBS index (![](media_svg/image9.svg) [公式≈: ^{I}TBS]) is determined based on![](media_svg/image5.svg) [公式≈: ^{I}MCS]and Table 14.1.1-2,

- the transport block size is determined by using ![](media_svg/image9.svg) [公式≈: ^{I}TBS] and setting the Table 7.1.7.2.1-1 column indicator to ![](media_svg/image13.svg) [公式≈: max0.8,1_{{}⋅∂_{√∃}N_{PRB}±≠_{}}], where ![](media_svg/image14.svg) [公式≈: ^{N}PRB^{±}] to the total number of allocated PRBs based on the procedure defined in Clause 14.1.1.4A and 14.1.1.4B.

- otherwise

- Transmission Format of SCI format 1 is set to 0 if present,

- the modulation order is determined using the "modulation and coding scheme " field (![](media_svg/image5.svg) [公式≈: ^{I}MCS]) in SCI format 1. For![](media_svg/image11.svg) [公式: 028≥≥I_{MCS}], the modulation order is set to ![](media_svg/image15.svg) [公式: QQ±±=min(4,)_{m}], where ![](media_svg/image16.svg) [公式≈: ^{Q}m^{±}]is determined from Table 8.6.1-1.

- the TBS index (![](media_svg/image9.svg) [公式≈: ^{I}TBS]) is determined based on![](media_svg/image5.svg) [公式≈: ^{I}MCS]and Table 8.6.1-1, and the transport block size is determined using ![](media_svg/image9.svg) [公式≈: ^{I}TBS] and the number of allocated resource blocks (![](media_svg/image10.svg) [公式≈: ^{N}PRB]) using the procedure in Clause 7.1.7.2.1.

For sidelink transmission mode 3 and 4, the parameter ![](media_svg/image17.svg) [公式≈: ^{P}step] is given by table 14.1.1-1.

Table 14.1.1-1: Determination of![](media_svg/image18.svg) [公式≈: ^{P}step]for sidelink transmission mode 3 and 4

|  | ![](media_svg/image17.svg) [公式≈: ^{P}step] |
| --- | --- |
| TDD with UL/DL configuration 0 | 60 |
| TDD with UL/DL configuration 1 | 40 |
| TDD with UL/DL configuration 2 | 20 |
| TDD with UL/DL configuration 3 | 30 |
| TDD with UL/DL configuration 4 | 20 |
| TDD with UL/DL configuration 5 | 10 |
| TDD with UL/DL configuration 6 | 50 |
| Otherwise | 100 |

Table 14.1.1-2: Modulation and TBS index table for ![](media_svg/image12.svg) [公式: 2931≥≥I_{MCS}]

| MCS Index | Modulation Order | TBS Index |
| --- | --- | --- |
| 29 | 6 | 30 |
| 30 | 6 | 31 |
| 31 | 6 | 33 |

#### 14.1.1.1 UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 1

Within the PSCCH period (described in Clause 14.2.3), the subframes used for PSSCH are determined as follows:

- a subframe indicator bitmap ![](media_svg/image22.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] and![](media_svg/image23.svg) [公式≈: ^{N}TRP] are determined using the procedure described in Clause 14.1.1.1.1.

- a bitmap ![](media_svg/image24.svg) [公式≈: (b_{0},b_{1},...b_{L}_{PSSCH}_{−}_{1})] is determined using![](media_svg/image25.svg) [公式≈: ^{b}j^{=}^{b}^{±}jmodN_{TRP}] and a subframe ![](media_svg/image26.svg) [公式≈: _{l}PSSCH_{j}] in the subframe pool is used for PSSCH if ![](media_svg/image27.svg) [公式: b_{j}=1], otherwise the subframe ![](media_svg/image26.svg) [公式≈: _{l}PSSCH_{j}]is not used for PSSCH, where ![](media_svg/image28.svg) [公式≈: _{(}_{l}_{0}PSSCH_{,}_{l}_{1}PSSCH_{,....,.}_{l}_{L}PSSCH_{PSSCH}_{−}_{1}_{)}] and![](media_svg/image29.svg) [公式≈: ^{L}PSSCH] are described in Clause 14.1.4. The subframes used for PSSCH are denoted by![](media_svg/image30.svg) [公式≈: _{(}_{n}_{0}PSSCH_{,}_{n}_{1}PSSCH_{,....,.}_{n}_{N}PSSCH_{PSSCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and where![](media_svg/image31.svg) [公式≈: ^{N}PSSCH] is the number of subframes that can be used for PSSCH transmission in a PSCCH period and is a multiple of 4.

#### 14.1.1.1.1 Determination of subframe indicator bitmap

For FDD and TDD with UL/DL configuration belonging to {1,2,4,5},![](media_svg/image23.svg) [公式≈: ^{N}TRP] is 8, and the mapping between Time Resource pattern Index (![](media_svg/image4.svg) [公式≈: ^{I}TRP]) and subframe indicator bitmap![](media_svg/image32.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] is given by table 14.1.1.1.1-1.

For TDD with UL/DL configuration 0,![](media_svg/image33.svg) [公式≈: ^{N}TRP] is 7, and the mapping between Time Resource pattern Index (![](media_svg/image4.svg) [公式≈: ^{I}TRP]) and subframe indicator bitmap![](media_svg/image34.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] is given by table 14.1.1.1.1-2.

For TDD with UL/DL configuration belonging to {3,6},![](media_svg/image35.svg) [公式≈: ^{N}TRP] is 6, and the mapping between Time Resource pattern Index (![](media_svg/image4.svg) [公式≈: ^{I}TRP]) and subframe indicator bitmap![](media_svg/image36.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] is given by table 14.1.1.1.1-3.

Table 14.1.1.1.1-1: Time Resource pattern Index mapping for![](media_svg/image37.svg) [公式: N_{TRP}=8]

| ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | (1,0,0,0,0,0,0,0) | 37 | 4 | (1,1,1,0,1,0,0,0) | 74 | 4 | (0,1,1,1,0,0,0,1) |
| 1 | 1 | (0,1,0,0,0,0,0,0) | 38 | 4 | (1,1,0,1,1,0,0,0) | 75 | 4 | (1,1,0,0,1,0,0,1) |
| 2 | 1 | (0,0,1,0,0,0,0,0) | 39 | 4 | (1,0,1,1,1,0,0,0) | 76 | 4 | (1,0,1,0,1,0,0,1) |
| 3 | 1 | (0,0,0,1,0,0,0,0) | 40 | 4 | (0,1,1,1,1,0,0,0) | 77 | 4 | (0,1,1,0,1,0,0,1) |
| 4 | 1 | (0,0,0,0,1,0,0,0) | 41 | 4 | (1,1,1,0,0,1,0,0) | 78 | 4 | (1,0,0,1,1,0,0,1) |
| 5 | 1 | (0,0,0,0,0,1,0,0) | 42 | 4 | (1,1,0,1,0,1,0,0) | 79 | 4 | (0,1,0,1,1,0,0,1) |
| 6 | 1 | (0,0,0,0,0,0,1,0) | 43 | 4 | (1,0,1,1,0,1,0,0) | 80 | 4 | (0,0,1,1,1,0,0,1) |
| 7 | 1 | (0,0,0,0,0,0,0,1) | 44 | 4 | (0,1,1,1,0,1,0,0) | 81 | 4 | (1,1,0,0,0,1,0,1) |
| 8 | 2 | (1,1,0,0,0,0,0,0) | 45 | 4 | (1,1,0,0,1,1,0,0) | 82 | 4 | (1,0,1,0,0,1,0,1) |
| 9 | 2 | (1,0,1,0,0,0,0,0) | 46 | 4 | (1,0,1,0,1,1,0,0) | 83 | 4 | (0,1,1,0,0,1,0,1) |
| 10 | 2 | (0,1,1,0,0,0,0,0) | 47 | 4 | (0,1,1,0,1,1,0,0) | 84 | 4 | (1,0,0,1,0,1,0,1) |
| 11 | 2 | (1,0,0,1,0,0,0,0) | 48 | 4 | (1,0,0,1,1,1,0,0) | 85 | 4 | (0,1,0,1,0,1,0,1) |
| 12 | 2 | (0,1,0,1,0,0,0,0) | 49 | 4 | (0,1,0,1,1,1,0,0) | 86 | 4 | (0,0,1,1,0,1,0,1) |
| 13 | 2 | (0,0,1,1,0,0,0,0) | 50 | 4 | (0,0,1,1,1,1,0,0) | 87 | 4 | (1,0,0,0,1,1,0,1) |
| 14 | 2 | (1,0,0,0,1,0,0,0) | 51 | 4 | (1,1,1,0,0,0,1,0) | 88 | 4 | (0,1,0,0,1,1,0,1) |
| 15 | 2 | (0,1,0,0,1,0,0,0) | 52 | 4 | (1,1,0,1,0,0,1,0) | 89 | 4 | (0,0,1,0,1,1,0,1) |
| 16 | 2 | (0,0,1,0,1,0,0,0) | 53 | 4 | (1,0,1,1,0,0,1,0) | 90 | 4 | (0,0,0,1,1,1,0,1) |
| 17 | 2 | (0,0,0,1,1,0,0,0) | 54 | 4 | (0,1,1,1,0,0,1,0) | 91 | 4 | (1,1,0,0,0,0,1,1) |
| 18 | 2 | (1,0,0,0,0,1,0,0) | 55 | 4 | (1,1,0,0,1,0,1,0) | 92 | 4 | (1,0,1,0,0,0,1,1) |
| 19 | 2 | (0,1,0,0,0,1,0,0) | 56 | 4 | (1,0,1,0,1,0,1,0) | 93 | 4 | (0,1,1,0,0,0,1,1) |
| 20 | 2 | (0,0,1,0,0,1,0,0) | 57 | 4 | (0,1,1,0,1,0,1,0) | 94 | 4 | (1,0,0,1,0,0,1,1) |
| 21 | 2 | (0,0,0,1,0,1,0,0) | 58 | 4 | (1,0,0,1,1,0,1,0) | 95 | 4 | (0,1,0,1,0,0,1,1) |
| 22 | 2 | (0,0,0,0,1,1,0,0) | 59 | 4 | (0,1,0,1,1,0,1,0) | 96 | 4 | (0,0,1,1,0,0,1,1) |
| 23 | 2 | (1,0,0,0,0,0,1,0) | 60 | 4 | (0,0,1,1,1,0,1,0) | 97 | 4 | (1,0,0,0,1,0,1,1) |
| 24 | 2 | (0,1,0,0,0,0,1,0) | 61 | 4 | (1,1,0,0,0,1,1,0) | 98 | 4 | (0,1,0,0,1,0,1,1) |
| 25 | 2 | (0,0,1,0,0,0,1,0) | 62 | 4 | (1,0,1,0,0,1,1,0) | 99 | 4 | (0,0,1,0,1,0,1,1) |
| 26 | 2 | (0,0,0,1,0,0,1,0) | 63 | 4 | (0,1,1,0,0,1,1,0) | 100 | 4 | (0,0,0,1,1,0,1,1) |
| 27 | 2 | (0,0,0,0,1,0,1,0) | 64 | 4 | (1,0,0,1,0,1,1,0) | 101 | 4 | (1,0,0,0,0,1,1,1) |
| 28 | 2 | (0,0,0,0,0,1,1,0) | 65 | 4 | (0,1,0,1,0,1,1,0) | 102 | 4 | (0,1,0,0,0,1,1,1) |
| 29 | 2 | (1,0,0,0,0,0,0,1) | 66 | 4 | (0,0,1,1,0,1,1,0) | 103 | 4 | (0,0,1,0,0,1,1,1) |
| 30 | 2 | (0,1,0,0,0,0,0,1) | 67 | 4 | (1,0,0,0,1,1,1,0) | 104 | 4 | (0,0,0,1,0,1,1,1) |
| 31 | 2 | (0,0,1,0,0,0,0,1) | 68 | 4 | (0,1,0,0,1,1,1,0) | 105 | 4 | (0,0,0,0,1,1,1,1) |
| 32 | 2 | (0,0,0,1,0,0,0,1) | 69 | 4 | (0,0,1,0,1,1,1,0) | 106 | 8 | (1,1,1,1,1,1,1,1) |
| 33 | 2 | (0,0,0,0,1,0,0,1) | 70 | 4 | (0,0,0,1,1,1,1,0) | 107-127 | reserved | reserved |
| 34 | 2 | (0,0,0,0,0,1,0,1) | 71 | 4 | (1,1,1,0,0,0,0,1) |  |  |  |
| 35 | 2 | (0,0,0,0,0,0,1,1) | 72 | 4 | (1,1,0,1,0,0,0,1) |  |  |  |
| 36 | 4 | (1,1,1,1,0,0,0,0) | 73 | 4 | (1,0,1,1,0,0,0,1) |  |  |  |

Table 14.1.1.1.1-2: Time Resource pattern Index mapping for ![](media_svg/image40.svg) [公式: N_{TRP}=7]

| ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | reserved | reserved | 44 | 3 | (0,0,1,1,0,1,0) | 88 | 3 | (0,0,0,1,1,0,1) |
| 1 | 1 | (1,0,0,0,0,0,0) | 45 | 4 | (1,0,1,1,0,1,0) | 89 | 4 | (1,0,0,1,1,0,1) |
| 2 | 1 | (0,1,0,0,0,0,0) | 46 | 4 | (0,1,1,1,0,1,0) | 90 | 4 | (0,1,0,1,1,0,1) |
| 3 | 2 | (1,1,0,0,0,0,0) | 47 | 5 | (1,1,1,1,0,1,0) | 91 | 5 | (1,1,0,1,1,0,1) |
| 4 | 1 | (0,0,1,0,0,0,0) | 48 | 2 | (0,0,0,0,1,1,0) | 92 | 4 | (0,0,1,1,1,0,1) |
| 5 | 2 | (1,0,1,0,0,0,0) | 49 | 3 | (1,0,0,0,1,1,0) | 93 | 5 | (1,0,1,1,1,0,1) |
| 6 | 2 | (0,1,1,0,0,0,0) | 50 | 3 | (0,1,0,0,1,1,0) | 94 | 5 | (0,1,1,1,1,0,1) |
| 7 | 3 | (1,1,1,0,0,0,0) | 51 | 4 | (1,1,0,0,1,1,0) | 95 | 6 | (1,1,1,1,1,0,1) |
| 8 | 1 | (0,0,0,1,0,0,0) | 52 | 3 | (0,0,1,0,1,1,0) | 96 | 2 | (0,0,0,0,0,1,1) |
| 9 | 2 | (1,0,0,1,0,0,0) | 53 | 4 | (1,0,1,0,1,1,0) | 97 | 3 | (1,0,0,0,0,1,1) |
| 10 | 2 | (0,1,0,1,0,0,0) | 54 | 4 | (0,1,1,0,1,1,0) | 98 | 3 | (0,1,0,0,0,1,1) |
| 11 | 3 | (1,1,0,1,0,0,0) | 55 | 5 | (1,1,1,0,1,1,0) | 99 | 4 | (1,1,0,0,0,1,1) |
| 12 | 2 | (0,0,1,1,0,0,0) | 56 | 3 | (0,0,0,1,1,1,0) | 100 | 3 | (0,0,1,0,0,1,1) |
| 13 | 3 | (1,0,1,1,0,0,0) | 57 | 4 | (1,0,0,1,1,1,0) | 101 | 4 | (1,0,1,0,0,1,1) |
| 14 | 3 | (0,1,1,1,0,0,0) | 58 | 4 | (0,1,0,1,1,1,0) | 102 | 4 | (0,1,1,0,0,1,1) |
| 15 | 4 | (1,1,1,1,0,0,0) | 59 | 5 | (1,1,0,1,1,1,0) | 103 | 5 | (1,1,1,0,0,1,1) |
| 16 | 1 | (0,0,0,0,1,0,0) | 60 | 4 | (0,0,1,1,1,1,0) | 104 | 3 | (0,0,0,1,0,1,1) |
| 17 | 2 | (1,0,0,0,1,0,0) | 61 | 5 | (1,0,1,1,1,1,0) | 105 | 4 | (1,0,0,1,0,1,1) |
| 18 | 2 | (0,1,0,0,1,0,0) | 62 | 5 | (0,1,1,1,1,1,0) | 106 | 4 | (0,1,0,1,0,1,1) |
| 19 | 3 | (1,1,0,0,1,0,0) | 63 | 6 | (1,1,1,1,1,1,0) | 107 | 5 | (1,1,0,1,0,1,1) |
| 20 | 2 | (0,0,1,0,1,0,0) | 64 | 1 | (0,0,0,0,0,0,1) | 108 | 4 | (0,0,1,1,0,1,1) |
| 21 | 3 | (1,0,1,0,1,0,0) | 65 | 2 | (1,0,0,0,0,0,1) | 109 | 5 | (1,0,1,1,0,1,1) |
| 22 | 3 | (0,1,1,0,1,0,0) | 66 | 2 | (0,1,0,0,0,0,1) | 110 | 5 | (0,1,1,1,0,1,1) |
| 23 | 4 | (1,1,1,0,1,0,0) | 67 | 3 | (1,1,0,0,0,0,1) | 111 | 6 | (1,1,1,1,0,1,1) |
| 24 | 2 | (0,0,0,1,1,0,0) | 68 | 2 | (0,0,1,0,0,0,1) | 112 | 3 | (0,0,0,0,1,1,1) |
| 25 | 3 | (1,0,0,1,1,0,0) | 69 | 3 | (1,0,1,0,0,0,1) | 113 | 4 | (1,0,0,0,1,1,1) |
| 26 | 3 | (0,1,0,1,1,0,0) | 70 | 3 | (0,1,1,0,0,0,1) | 114 | 4 | (0,1,0,0,1,1,1) |
| 27 | 4 | (1,1,0,1,1,0,0) | 71 | 4 | (1,1,1,0,0,0,1) | 115 | 5 | (1,1,0,0,1,1,1) |
| 28 | 3 | (0,0,1,1,1,0,0) | 72 | 2 | (0,0,0,1,0,0,1) | 116 | 4 | (0,0,1,0,1,1,1) |
| 29 | 4 | (1,0,1,1,1,0,0) | 73 | 3 | (1,0,0,1,0,0,1) | 117 | 5 | (1,0,1,0,1,1,1) |
| 30 | 4 | (0,1,1,1,1,0,0) | 74 | 3 | (0,1,0,1,0,0,1) | 118 | 5 | (0,1,1,0,1,1,1) |
| 31 | 5 | (1,1,1,1,1,0,0) | 75 | 4 | (1,1,0,1,0,0,1) | 119 | 6 | (1,1,1,0,1,1,1) |
| 32 | 1 | (0,0,0,0,0,1,0) | 76 | 3 | (0,0,1,1,0,0,1) | 120 | 4 | (0,0,0,1,1,1,1) |
| 33 | 2 | (1,0,0,0,0,1,0) | 77 | 4 | (1,0,1,1,0,0,1) | 121 | 5 | (1,0,0,1,1,1,1) |
| 34 | 2 | (0,1,0,0,0,1,0) | 78 | 4 | (0,1,1,1,0,0,1) | 122 | 5 | (0,1,0,1,1,1,1) |
| 35 | 3 | (1,1,0,0,0,1,0) | 79 | 5 | (1,1,1,1,0,0,1) | 123 | 6 | (1,1,0,1,1,1,1) |
| 36 | 2 | (0,0,1,0,0,1,0) | 80 | 2 | (0,0,0,0,1,0,1) | 124 | 5 | (0,0,1,1,1,1,1) |
| 37 | 3 | (1,0,1,0,0,1,0) | 81 | 3 | (1,0,0,0,1,0,1) | 125 | 6 | (1,0,1,1,1,1,1) |
| 38 | 3 | (0,1,1,0,0,1,0) | 82 | 3 | (0,1,0,0,1,0,1) | 126 | 6 | (0,1,1,1,1,1,1) |
| 39 | 4 | (1,1,1,0,0,1,0) | 83 | 4 | (1,1,0,0,1,0,1) | 127 | 7 | (1,1,1,1,1,1,1) |
| 40 | 2 | (0,0,0,1,0,1,0) | 84 | 3 | (0,0,1,0,1,0,1) |  |  |  |
| 41 | 3 | (1,0,0,1,0,1,0) | 85 | 4 | (1,0,1,0,1,0,1) |  |  |  |
| 42 | 3 | (0,1,0,1,0,1,0) | 86 | 4 | (0,1,1,0,1,0,1) |  |  |  |
| 43 | 4 | (1,1,0,1,0,1,0) | 87 | 5 | (1,1,1,0,1,0,1) |  |  |  |

Table 14.1.1.1.1-3: Time Resource pattern Index mapping for ![](media_svg/image41.svg) [公式: N_{TRP}=6]

| ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] | ![](media_svg/image4.svg) [公式≈: ^{I}TRP] | ![](media_svg/image38.svg) [公式≈: ^{k}TRP] | ![](media_svg/image39.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | reserved | reserved | 22 | 3 | (0,1,1,0,1,0) | 44 | 3 | (0,0,1,1,0,1) |
| 1 | 1 | (1,0,0,0,0,0) | 23 | 4 | (1,1,1,0,1,0) | 45 | 4 | (1,0,1,1,0,1) |
| 2 | 1 | (0,1,0,0,0,0) | 24 | 2 | (0,0,0,1,1,0) | 46 | 4 | (0,1,1,1,0,1) |
| 3 | 2 | (1,1,0,0,0,0) | 25 | 3 | (1,0,0,1,1,0) | 47 | 5 | (1,1,1,1,0,1) |
| 4 | 1 | (0,0,1,0,0,0) | 26 | 3 | (0,1,0,1,1,0) | 48 | 2 | (0,0,0,0,1,1) |
| 5 | 2 | (1,0,1,0,0,0) | 27 | 4 | (1,1,0,1,1,0) | 49 | 3 | (1,0,0,0,1,1) |
| 6 | 2 | (0,1,1,0,0,0) | 28 | 3 | (0,0,1,1,1,0) | 50 | 3 | (0,1,0,0,1,1) |
| 7 | 3 | (1,1,1,0,0,0) | 29 | 4 | (1,0,1,1,1,0) | 51 | 4 | (1,1,0,0,1,1) |
| 8 | 1 | (0,0,0,1,0,0) | 30 | 4 | (0,1,1,1,1,0) | 52 | 3 | (0,0,1,0,1,1) |
| 9 | 2 | (1,0,0,1,0,0) | 31 | 5 | (1,1,1,1,1,0) | 53 | 4 | (1,0,1,0,1,1) |
| 10 | 2 | (0,1,0,1,0,0) | 32 | 1 | (0,0,0,0,0,1) | 54 | 4 | (0,1,1,0,1,1) |
| 11 | 3 | (1,1,0,1,0,0) | 33 | 2 | (1,0,0,0,0,1) | 55 | 5 | (1,1,1,0,1,1) |
| 12 | 2 | (0,0,1,1,0,0) | 34 | 2 | (0,1,0,0,0,1) | 56 | 3 | (0,0,0,1,1,1) |
| 13 | 3 | (1,0,1,1,0,0) | 35 | 3 | (1,1,0,0,0,1) | 57 | 4 | (1,0,0,1,1,1) |
| 14 | 3 | (0,1,1,1,0,0) | 36 | 2 | (0,0,1,0,0,1) | 58 | 4 | (0,1,0,1,1,1) |
| 15 | 4 | (1,1,1,1,0,0) | 37 | 3 | (1,0,1,0,0,1) | 59 | 5 | (1,1,0,1,1,1) |
| 16 | 1 | (0,0,0,0,1,0) | 38 | 3 | (0,1,1,0,0,1) | 60 | 4 | (0,0,1,1,1,1) |
| 17 | 2 | (1,0,0,0,1,0) | 39 | 4 | (1,1,1,0,0,1) | 61 | 5 | (1,0,1,1,1,1) |
| 18 | 2 | (0,1,0,0,1,0) | 40 | 2 | (0,0,0,1,0,1) | 62 | 5 | (0,1,1,1,1,1) |
| 19 | 3 | (1,1,0,0,1,0) | 41 | 3 | (1,0,0,1,0,1) | 63 | 6 | (1,1,1,1,1,1) |
| 20 | 2 | (0,0,1,0,1,0) | 42 | 3 | (0,1,0,1,0,1) | 64-127 | reserved | reserved |
| 21 | 3 | (1,0,1,0,1,0) | 43 | 4 | (1,1,0,1,0,1) |  |  |  |

#### 14.1.1.2 UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 1

The set of resource blocks is determined using the procedure described in Clause 14.1.1.2.1 and 14.1.1.2.2.

#### 14.1.1.2.1 PSSCH resource allocation for sidelink transmission mode 1

The resource allocation and hopping field of the SCI format 0 is used to determine a set of indices denoted by ![](media_svg/image42.svg) [公式≈: ^{n}VRB^{±}](0 ≤ ![](media_svg/image42.svg) [公式≈: ^{n}VRB^{±}]< ![](media_svg/image43.svg) [公式≈: _{N}_{RB}SL]), a starting index ![](media_svg/image44.svg) [公式≈: ^{R}^{B}START^{±}], and a number of allocated PRBs ![](media_svg/image45.svg) [公式≈: ^{L}CRBs^{±}] and ![](media_svg/image46.svg) [公式≈: _{N}_{RB}PSSCH]using the procedure in Clause 8.1.1, and 8.4 (for sidelink frequency hopping with type 1 or type 2 hopping) with the following exceptions:

- the term 'PUSCH' in Clauses 8.1.1 and 8.4 is replaced with 'PSSCH'.

- the quantity ![](media_svg/image47.svg) [公式≈: ^{n}VRB] in Clause 8.1.1 is replaced with ![](media_svg/image48.svg) [公式≈: ^{n}VRB^{±}] .

- the quantity ![](media_svg/image49.svg) [公式≈: _{N}_{RB}UL] in Clauses 8.1.1 and 8.4 is replaced with ![](media_svg/image50.svg) [公式≈: _{N}_{RB}SL].

- the quantity![](media_svg/image51.svg) [公式≈: ^{RB}START] in Clauses 8.1.1and 8.4 is replaced with ![](media_svg/image44.svg) [公式≈: ^{R}^{B}START^{±}].

- the quantity![](media_svg/image52.svg) [公式≈: ^{L}CRBs]in Clauses 8.1.1 and 8.4 is replaced with![](media_svg/image45.svg) [公式≈: ^{L}CRBs^{±}].

- the quantity ![](media_svg/image53.svg) [公式≈: _{N}_{RB}PUSCH] in Clause 8.4 is replaced with ![](media_svg/image54.svg) [公式≈: _{N}_{RB}PSSCH].

- the quantity ![](media_svg/image55.svg) [公式≈: _{N}_{RB}HO] is given by higher layer parameter rb-Offset-r12 associated with the corresponding PSSCH resource configuration.

- the quantity ![](media_svg/image56.svg) [公式≈: ^{N}sb] is given by higher layer parameter numSubbands-r12 associated with the corresponding PSSCH resource configuration.

#### 14.1.1.2.2 PSSCH frequency hopping for sidelink transmission mode 1

If sidelink frequency hopping with type 1 hopping is enabled, the set of physical resource blocks for PSSCH transmission is determined using Clause 8.4 with the following exceptions:

- the term 'PUSCH' is replaced with 'PSSCH'.

- only inter-subframe hopping shall be used.

- the quantity ![](media_svg/image57.svg) [公式≈: ^{RB}START] is replaced with ![](media_svg/image44.svg) [公式≈: ^{R}^{B}START^{±}].

- the quantity ![](media_svg/image49.svg) [公式≈: _{N}_{RB}UL]is replaced with ![](media_svg/image50.svg) [公式≈: _{N}_{RB}SL].

- the quantity ![](media_svg/image53.svg) [公式≈: _{N}_{RB}PUSCH] is replaced with ![](media_svg/image54.svg) [公式≈: _{N}_{RB}PSSCH].

- the quantity ![](media_svg/image55.svg) [公式≈: _{N}_{RB}HO] is given by higher layer parameter rb-Offset-r12 associated with the PSSCH resource configuration.

- the frequency hopping field in the SCI format 0 is used instead of DCI format 0.

- the quantity![](media_svg/image58.svg) [公式: n_{PRB}^{S1}(i)] is replaced with ![](media_svg/image59.svg) [公式≈: _{n}_{PRB}SL0].

- the quantity ![](media_svg/image60.svg) [公式: n_{PRB}(i)] is replaced with ![](media_svg/image61.svg) [公式≈: _{n}_{PRB}SL1].

- for odd ![](media_svg/image62.svg) [公式≈: _{n}_{ssf}PSSCH] (described in Clause 9.2.4 of [3]), the set of physical resource blocks for PSSCH transmission are ![](media_svg/image63.svg) [公式≈: ^{L}CRBs^{±}]contiguous resource blocks starting from PRB with index![](media_svg/image59.svg) [公式≈: _{n}_{PRB}SL0].

- for even ![](media_svg/image62.svg) [公式≈: _{n}_{ssf}PSSCH] (described in Clause 9.2.4 of [3]), the set of physical resource blocks for PSSCH transmission are ![](media_svg/image63.svg) [公式≈: ^{L}CRBs^{±}]contiguous resource blocks starting from PRB with index![](media_svg/image64.svg) [公式≈: _{n}_{PRB}SL1].

#### 14.1.1.3 UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 2

For FDD or for TDD, and the UE not configured with the higher layer parameter trpt-Subset-r12

- The allowed values of![](media_svg/image4.svg) [公式≈: ^{I}TRP] correspond to the values of ![](media_svg/image65.svg) [公式≈: ^{k}TRP]satisfying ![](media_svg/image66.svg) [公式≈: ^{k}TRP^{=}^{k}i] , for a value of ![](media_svg/image67.svg) [公式: i]in ![](media_svg/image68.svg) [公式: 0≥i<X_{TRP}], where ![](media_svg/image69.svg) [公式≈: ^{k}i] and ![](media_svg/image70.svg) [公式≈: ^{X}TRP] are determined from table 14.1.1.3-1.

For FDD or for TDD with UL/DL configuration belonging to {0,1,2,3,4,6}, and the UE configured with the higher layer parameter trpt-Subset-r12

- The allowed values of![](media_svg/image4.svg) [公式≈: ^{I}TRP] correspond to the values of ![](media_svg/image65.svg) [公式≈: ^{k}TRP]satisfying ![](media_svg/image66.svg) [公式≈: ^{k}TRP^{=}^{k}i] , for values of ![](media_svg/image67.svg) [公式: i] in ![](media_svg/image68.svg) [公式: 0≥i<X_{TRP}]satisfying ![](media_svg/image71.svg) [公式: a_{i}=1], ![](media_svg/image68.svg) [公式: 0≥i<X_{TRP}] and where ![](media_svg/image69.svg) [公式≈: ^{k}i] and ![](media_svg/image70.svg) [公式≈: ^{X}TRP] are determined from table 14.1.1.3-1, and![](media_svg/image72.svg) [公式≈: (a_{0},a_{1},...,a_{X}_{TRP}_{−}_{1})] is the bitmap indicated by trpt-Subset-r12.

Table 14.1.1.3-1: Determination of![](media_svg/image70.svg) [公式≈: ^{X}TRP] and ![](media_svg/image69.svg) [公式≈: ^{k}i] for sidelink transmission mode 2

|  | ![](media_svg/image70.svg) [公式≈: ^{X}TRP] | ![](media_svg/image73.svg) [公式≈: ^{k}0] | ![](media_svg/image74.svg) [公式≈: ^{k}1] | ![](media_svg/image75.svg) [公式≈: ^{k}2] | ![](media_svg/image76.svg) [公式≈: ^{k}3] | ![](media_svg/image77.svg) [公式≈: ^{k}4] |
| --- | --- | --- | --- | --- | --- | --- |
| FDD and TDD with UL/DL configuration 1,2,4,5 | 3 | 1 | 2 | 4 | - | - |
| TDD with UL/DL configuration 0 | 5 | 1 | 2 | 3 | 4 | 5 |
| TDD with UL/DL configuration 3,6 | 4 | 1 | 2 | 3 | 4 | - |

Within a PSCCH period, the subframes used for PSSCH are determined as follows:

- a subframe indicator bitmap ![](media_svg/image78.svg) [公式≈: (b_{0}±,b_{1}±,...b_{N}±_{TRP}_{−}_{1})] and![](media_svg/image23.svg) [公式≈: ^{N}TRP] are determined using the procedure described in Clause 14.1.1.1.1 from the allowed values of ![](media_svg/image4.svg) [公式≈: ^{I}TRP]described in this Clause.

- a bitmap ![](media_svg/image24.svg) [公式≈: (b_{0},b_{1},...b_{L}_{PSSCH}_{−}_{1})] is determined using![](media_svg/image25.svg) [公式≈: ^{b}j^{=}^{b}^{±}jmodN_{TRP}] and a subframe ![](media_svg/image26.svg) [公式≈: _{l}PSSCH_{j}] in the subframe pool is used for PSSCH if ![](media_svg/image27.svg) [公式: b_{j}=1], otherwise the subframe ![](media_svg/image26.svg) [公式≈: _{l}PSSCH_{j}]is not used for PSSCH, where ![](media_svg/image28.svg) [公式≈: _{(}_{l}_{0}PSSCH_{,}_{l}_{1}PSSCH_{,....,.}_{l}_{L}PSSCH_{PSSCH}_{−}_{1}_{)}] and![](media_svg/image29.svg) [公式≈: ^{L}PSSCH] are described in Clause 14.1.3. The subframes used for PSSCH are denoted by![](media_svg/image79.svg) [公式≈: _{(}_{n}_{0}PSSCH_{,}_{n}_{1}PSSCH_{,....,.}_{n}_{N}PSSCH_{PSSCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and where![](media_svg/image31.svg) [公式≈: ^{N}PSSCH] is the number of subframes that can be used for PSSCH transmission in a PSCCH period and is a multiple of 4.

#### 14.1.1.4 UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 2

The set of resource blocks within the resource block pool (defined in 14.1.3) is determined using the Clause 14.1.1.2.1 .

If sidelink frequency hopping with type 1 hopping is enabled, the set of physical resource blocks for PSSCH transmission is determined using Clause 14.1.1.2.2 with the following exceptions

- the quantity ![](media_svg/image49.svg) [公式≈: _{N}_{RB}UL]is replaced with ![](media_svg/image80.svg) [公式≈: _{M}_{RB}PSSCH_RP] (defined in 14.1.3).

- for odd ![](media_svg/image62.svg) [公式≈: _{n}_{ssf}PSSCH], the set of physical resource blocks for PSSCH transmission are given by ![](media_svg/image63.svg) [公式≈: ^{L}CRBs^{±}]contiguous resource blocks![](media_svg/image81.svg) [公式≈: ^{m}x^{,}^{m}x+1^{,..}^{m}x+L_{CRBs}±−1]belonging to the resource block pool, where ![](media_svg/image82.svg) [公式≈: _{x}_{=}_{n}_{PRB}SL0].

- for even ![](media_svg/image62.svg) [公式≈: _{n}_{ssf}PSSCH], the set of physical resource blocks for PSSCH transmission are given by ![](media_svg/image63.svg) [公式≈: ^{L}CRBs^{±}]contiguous resource blocks![](media_svg/image83.svg) [公式≈: ^{m}x^{,}^{m}x+1^{,..}^{m}x+L_{CRBs}±−1]belonging to the resource block pool, where ![](media_svg/image84.svg) [公式≈: _{x}_{=}_{n}_{PRB}SL1].

#### 14.1.1.4A UE procedure for determining subframes and resource blocks for transmitting PSSCH for sidelink transmission mode 3

If the UE has a configured sidelink grant (described in [8]) in subframe ![](media_svg/image85.svg) [公式≈: _{t}_{n}SL] with the corresponding PSCCH resource m (described in Clause 14.2.4), the resource blocks and subframes of the corresponding PSSCH transmissions are determined according to 14.1.1.4C.

If the UE has a configured sidelink grant (described in [8]) for an SL SPS configuration activated by Clause 14.2.1 and if a set of sub-channels in subframe ![](media_svg/image86.svg) [公式≈: _{t}_{m}SL] is determined as the time and frequency resource for PSSCH transmission corresponding to the configured sidelink grant (described in [8]) of the SL SPS configuration, the same set of sub-channels in subframes ![](media_svg/image87.svg) [公式≈: t_{m}^{SL}_{+}_{j}_{≠}_{P}_{SPS}&apos;] are also determined for PSSCH transmissions corresponding to the same sidelink grant where j=1, 2,…, ![](media_svg/image88.svg) [公式≈: ^{P}SPS^{&apos;}^{=}^{P}step^{≠}^{P}SPS^{/}^{100}], and ![](media_svg/image89.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] is determined by Clause 14.1.5. Here,  is the sidelink SPS interval of the corresponding SL SPS configuration.

#### 14.1.1.4B UE procedure for determining subframes and resource blocks for transmitting PSSCH and reserving resources for sidelink transmission mode 4

If the UE has a configured sidelink grant (described in [8]) in subframe ![](media_svg/image85.svg) [公式≈: _{t}_{n}SL]with the corresponding PSCCH resource m (described in Clause 14.2.4), the resource blocks and subframes of the corresponding PSSCH transmissions are determined according to 14.1.1.4C.

The number of subframes in one set of the time and frequency resources for transmission opportunities of PSSCH is given by ![](media_svg/image91.svg) [公式≈: ^{C}resel] where ![](media_svg/image91.svg) [公式≈: ^{C}resel]= 10*SL_RESOURCE_RESELECTION_COUNTER [8] if configured else ![](media_svg/image91.svg) [公式≈: ^{C}resel]is set to 1.

If a set of sub-channels in subframe ![](media_svg/image86.svg) [公式≈: _{t}_{m}SL] is determined as the time and frequency resource for PSSCH transmission corresponding to the configured sidelink grant (described in [8]), the same set of sub-channels in subframes ![](media_svg/image92.svg) [公式≈: t_{m}^{SL}_{+}_{j}_{≠}_{P}_{rsvp}&apos;_{_}_{TX}] are also determined for PSSCH transmissions corresponding to the same sidelink grant where j=1, 2,…, ![](media_svg/image93.svg) [公式≈: ^{C}resel^{−}^{1}], ![](media_svg/image94.svg) [公式≈: ^{P}rsvp^{&apos;}_TX^{=}^{P}step^{≠}^{P}rsvp_TX^{/}^{100}] , and ![](media_svg/image89.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] is determined by Clause 14.1.5. Here, ![](media_svg/image95.svg) [公式≈: ^{P}rsvp_TX] is the resource reservation interval indicated by higher layers.

If a UE is configured with high layer parameter cr-Limit and transmits PSSCH in subframe n, the UE shall ensure the following limits for any priority value k;

![](media_svg/image96.svg) [公式≈: _{⊆}_{ik}_{÷}CRiCRk()≥_{Limit}()]

where ![](media_svg/image97.svg) [公式: CR(i)] is the CR evaluated in subframe n-4 for the PSSCH transmissions with "Priority" field in the SCI set to i, and ![](media_svg/image98.svg) [公式≈: CRk_{Limit}()] corresponds to the high layer parameter cr-Limit that is associated with the priority value k and the CBR range which includes the CBR measured in subframe n-4. It is up to UE implementation how to meet the above limits, including dropping the transmissions in subframe n.

#### 14.1.1.4C UE procedure for determining subframes and resource blocks for PSSCH transmission associated with an SCI format 1

The set of subframes and resource blocks for PSSCH transmission is determined by the resource used for the PSCCH transmission containing the associated SCI format 1, and "Frequency resource location of the initial transmission and retransmission" field, "Retransmission index" field, "Time gap between initial transmission and retransmission" field of the associated SCI format 1 as described below.

"Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 is equal to resource indication value (RIV) corresponding to a starting sub-channel index (![](media_svg/image99.svg) [公式≈: _{n}_{subCH}start]) and a length in terms of contiguously allocated sub-channels (![](media_svg/image100.svg) [公式≈: ^{L}subCH] 1). The resource indication value is defined by

if ![](media_svg/image101.svg) [公式≈: ^{(}^{L}subCH^{−}^{1}^{)}^{≥}√^{N}subCH^{/}^{2}∃] then

![](media_svg/image102.svg) [公式≈: ^{RIV}^{=}^{N}subCH^{(}^{L}subCH^{−}^{1}^{)}^{+}^{n}subCH^{start}]

else

![](media_svg/image103.svg) [公式≈: ^{RIV}^{=}^{N}subCH^{(}^{N}subCH^{−}^{L}subCH^{+}^{1}^{)}^{+}^{(}^{N}subCH^{−}^{1}^{−}^{n}subCH^{start}^{)}]

where  is the total number of sub-channels in the pool determined by higher layer parameter numSubchannel.

For the SCI format 1 transmitted on the PSCCH resource m (described in subcaluse 14.2.4) in subframe ![](media_svg/image105.svg) [公式≈: _{t}_{n}SL], the set of subframes and sub-channels for the corresponding PSSCH are determined as follows:

- if  is zero,

- the time and frequency resources for the corresponding PSSCH is given by

- sub-channel(s) ![](media_svg/image107.svg) [公式≈: m,m+1,...,m+L_{subCH}−1] in subframe ![](media_svg/image105.svg) [公式≈: _{t}_{n}SL].

- else if "Retransmission index" in the SCI format 1 is zero,

- the time and frequency resources for the corresponding PSSCH is given by

- sub-channel(s) ![](media_svg/image108.svg) [公式≈: m,m+1,...,m+L_{subCH}−1] in subframe ![](media_svg/image105.svg) [公式≈: _{t}_{n}SL], and

- sub-channels ![](media_svg/image109.svg) [公式≈: ^{n}subCH^{start}^{,}^{n}subCH^{start}^{+}^{1}^{,}^{...,}^{n}subCH^{start}^{+}^{L}subCH^{−}^{1}] in subframe ![](media_svg/image110.svg) [公式≈: ^{t}n^{SL}+SF_{gap}].

- else if "Retransmission index" in the SCI format 1 is one,

- the time and frequency resources for the corresponding PSSCH is given by

- sub-channels ![](media_svg/image111.svg) [公式≈: ^{n}subCH^{start}^{,}^{n}subCH^{start}^{+}^{1}^{,}^{...,}^{n}subCH^{start}^{+}^{L}subCH^{−}^{1}] in subframe ![](media_svg/image112.svg) [公式≈: ^{t}n^{SL}−SF_{gap}], and

- sub-channels ![](media_svg/image108.svg) [公式≈: m,m+1,...,m+L_{subCH}−1] in subframe ![](media_svg/image105.svg) [公式≈: _{t}_{n}SL].

where  is the value indicated by "Time gap between initial transmission and retransmission" field the SCI format 1 and ![](media_svg/image114.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] is determined by Clause 14.1.5.

When sub-channel(s) ![](media_svg/image108.svg) [公式≈: m,m+1,...,m+L_{subCH}−1] are determined in a subframe for the transmission of PSSCH, the set of resource blocks determined for the PSSCH transmission is given by ![](media_svg/image115.svg) [公式≈: ^{N}PSSCH^{RB}] contiguous resource blocks with the physical resource block number ![](media_svg/image116.svg) [公式≈: ^{n}PRB^{=}^{n}subCHRBstart^{+}^{m}^{*}^{n}subCHsize^{+}^{j}^{+}^{Β}] for ![](media_svg/image117.svg) [公式≈: j=0,...,N_{PSSCH}^{RB}−1]. Here, ![](media_svg/image118.svg) [公式≈: ^{n}subCHRBstart] and ![](media_svg/image119.svg) [公式≈: ^{n}subCHsize] are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively. The parameters ![](media_svg/image115.svg) [公式≈: ^{N}PSSCH^{RB}] and ![](media_svg/image120.svg) [公式: Β] are given as follows:

- if a pool is (pre)configured such that a UE always transmits PSCCH and the corresponding PSSCH in adjacent resource blocks in a subframe, ![](media_svg/image121.svg) [公式: Β=2] and ![](media_svg/image122.svg) [公式≈: ^{N}PSSCH^{RB}] is the largest integer that fulfils

![](media_svg/image123.svg) [公式≈: ^{N}PSSCH^{RB}^{=}^{2}^{Α}^{2}^{∪}^{3}^{Α}^{3}^{∪}^{5}^{Α}^{5}^{≥}^{L}subCH^{*}^{n}subCHsize^{−}^{2}]

where ![](media_svg/image124.svg) [公式: Α_{2},Α_{3},Α_{5}] is a set of non-negative integers

- if a pool is (pre)configured such that a UE may transmit PSCCH and the corresponding PSSCH in non-adjacent resource blocks in a subframe, ![](media_svg/image125.svg) [公式: Β=0] and ![](media_svg/image122.svg) [公式≈: ^{N}PSSCH^{RB}] is the largest integer that fulfils

![](media_svg/image126.svg) [公式≈: ^{N}PSSCH^{RB}^{=}^{2}^{Α}^{2}^{∪}^{3}^{Α}^{3}^{∪}^{5}^{Α}^{5}^{≥}^{L}subCH^{*}^{n}subCHsize]

where ![](media_svg/image124.svg) [公式: Α_{2},Α_{3},Α_{5}] is a set of non-negative integers.

#### 14.1.1.5 UE procedure for PSSCH power control

For sidelink transmission mode 1 and PSCCH period i, the UE transmit power ![](media_svg/image127.svg) [公式≈: ^{P}PSSCH] for PSSCH transmission is given by the following

- if the TPC command field in configured sidelink grant (described in [8]) for PSCCH period i is set to 0

- ![](media_svg/image128.svg) [公式≈: ^{P}PSSCH^{=}^{P}CMAX,PSSCH]

- if the TPC command field in configured sidelink grant (described in [8]) for PSCCH period i is set to 1

- ![](media_svg/image129.svg) [公式≈: ^{P}PSSCH^{=}^{min}^{{}^{P}CMAX,PSSCH^{,}^{10}^{log}10^{(}^{M}PSSCH^{)}^{+}^{P}O_PSSCH,1^{+}^{Α}PSSCH,1^{∪}^{PL}^{}}] [dBm]

where ![](media_svg/image130.svg) [公式≈: ^{P}CMAX,PSSCH] is defined in [6], and ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH]is the bandwidth of the PSSCH resource assignment expressed in number of resource block and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}]is defined in Clause 5.1.1.1. ![](media_svg/image134.svg) [公式≈: ^{P}O_PSSCH,1] and ![](media_svg/image135.svg) [公式≈: ^{Α}PSSCH,1] are provided by higher layer parameters p0-r12 and alpha-r12, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 2, the UE transmit power ![](media_svg/image127.svg) [公式≈: ^{P}PSSCH] for PSSCH transmission is given by

![](media_svg/image136.svg) [公式≈: ^{P}PSSCH^{=}^{min}^{{}^{P}CMAX,PSSCH^{,}^{10}^{log}10^{(}^{M}PSSCH^{)}^{+}^{P}O_PSSCH,2^{+}^{Α}PSSCH,2^{∪}^{PL}^{}}] [dBm] ,

where ![](media_svg/image130.svg) [公式≈: ^{P}CMAX,PSSCH] is defined in [6], and ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH]is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image137.svg) [公式≈: ^{P}O_PSSCH,2] and ![](media_svg/image138.svg) [公式≈: ^{Α}PSSCH,2] are provided by higher layer parameters p0-r12 and alpha-r12, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 3, the UE transmit power ![](media_svg/image127.svg) [公式≈: ^{P}PSSCH] for PSSCH transmission is given by

![](media_svg/image139.svg) [公式≈: ^{P}^{PSSCH}^{=}^{+}^{10}^{min}^{log}^{√}^{⌡}⌠_{⌡}_{∞}^{10}^{P}^{⊇}^{⊕}^{⊕}^{⊕}^{⊗}CMAX^{M}^{PSSCH}^{,}^{10}^{+}^{M}^{log}^{10}^{PSSCH}^{10}10^{3}^{⊇}^{⊕}_{⊕}_{⊗}^{≠}^{M}^{M}PSSCH^{PSCCH}^{+}^{⇒}^{⇐}^{⇐}^{⇐}^{⇔}^{10}^{10}^{3}^{≠}^{M}PSCCH^{⇒}^{⇐}_{⇐}_{⇔}^{+}^{P}O_PSSCH,3^{+}^{Α}PSSCH,3^{∪}^{PL}^{∅}^{⌡}∇_{⌡}_{∈}] [dBm] ,

where ![](media_svg/image140.svg) [公式≈: ^{P}CMAX] is defined in [6], and ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH]is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image141.svg) [公式≈: ^{P}O_PSSCH,3] and ![](media_svg/image142.svg) [公式≈: ^{Α}PSSCH,3] are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 4, the UE transmit power ![](media_svg/image127.svg) [公式≈: ^{P}PSSCH] for PSSCH transmission in subframe n is given by

![](media_svg/image143.svg) [公式≈: ^{PA}^{PSSCH10}^{=+}^{10log}^{⊇⇒}^{⊕⇐}^{⊕⇐}^{⊕⇐}⊗⇔^{MM}PSSCHPSCCH^{+≠}^{M}^{10}^{PSSCH}^{10}^{3}] [dBm] ,

where ![](media_svg/image144.svg) [公式≈: ^{P}CMAX] is defined in [6], ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH] is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks, ![](media_svg/image145.svg) [公式≈: ^{M}PSCCH^{=}^{2}], and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image146.svg) [公式≈: ^{P}O_PSSCH,4] and ![](media_svg/image147.svg) [公式≈: ^{Α}PSSCH,4] are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration. If higher layer parameter maxTxpower is configured then

![](media_svg/image148.svg) [公式≈: ^{APPMMPPL}^{=+≠++∪}^{min,,10log10}^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}CMAX_10PSSCHPSCCHO_PSSCH,4,4MAXCBRPSSCH^{⊇⇒}⊕⇐_{⊗⇔}^{10}^{3}^{Α}]

else

![](media_svg/image149.svg) [公式≈: ^{APMMPPL}^{=+≠++∪}^{min,10log10}^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}CMAX10PSSCHPSCCHO_PSSCH,4,4^{⊇⇒}⊕⇐_{⊗⇔}^{10}^{3}^{Α}PSSCH]

where![](media_svg/image150.svg) [公式≈: ^{P}MAX_CBR] is set to a maxTxpower value based on the priority level of the PSSCH and the CBR range which includes the CBR measured in subframe n-4.

#### 14.1.1.6 UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink transmission mode 4 and in sensing measurement in sidelink transmission mode 3

In sidelink transmission mode 4, when requested by higher layers in subframe n for a carrier, the UE shall determine the set of resources to be reported to higher layers for PSSCH transmission according to the steps described in this Clause. Parameters ![](media_svg/image151.svg) [公式≈: ^{L}subCH] the number of sub-channels to be used for the PSSCH transmission in a subframe, ![](media_svg/image95.svg) [公式≈: ^{P}rsvp_TX] the resource reservation interval, and ![](media_svg/image152.svg) [公式: prio_{TX}] the priority to be transmitted in the associated SCI format 1 by the UE are all provided by higher layers (described in [8]). ![](media_svg/image91.svg) [公式≈: ^{C}resel] is determined according to Clause 14.1.1.4B.

In sidelink transmission mode 3, when requested by higher layers in subframe n for a carrier, the UE shall determine the set of resources to be reported to higher layers in sensing measurement according to the steps described in this Clause. Parameters ![](media_svg/image151.svg) [公式≈: ^{L}subCH], ![](media_svg/image95.svg) [公式≈: ^{P}rsvp_TX] and![](media_svg/image152.svg) [公式: prio_{TX}] are all provided by higher layers (described in [11]). ![](media_svg/image91.svg) [公式≈: ^{C}resel] is determined by![](media_svg/image91.svg) [公式≈: ^{C}resel]=10*SL_RESOURCE_RESELECTION_COUNTER, where SL_RESOURCE_RESELECTION_COUNTER is provided by higher layers [11].

If partial sensing is not configured by higher layers then the following steps are used:

1) A candidate single-subframe resource for PSSCH transmission ![](media_svg/image153.svg) [公式≈: ^{R}x,y] is defined as a set of ![](media_svg/image154.svg) [公式≈: ^{L}subCH] contiguous sub-channels with sub-channel x+j in subframe ![](media_svg/image155.svg) [公式≈: _{t}_{y}SL] where ![](media_svg/image156.svg) [公式≈: j=0,...,L_{subCH}−1]. The UE shall assume that any set of ![](media_svg/image157.svg) [公式≈: ^{L}subCH] contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the time interval ![](media_svg/image158.svg) [公式: [n+T_{1},n+T_{2}]] corresponds to one candidate single-subframe resource, where selections of ![](media_svg/image159.svg) [公式≈: ^{T}1] and ![](media_svg/image160.svg) [公式≈: ^{T}2] are up to UE implementations under ![](media_svg/image161.svg) [公式: T_{1}≥4] and ![](media_svg/image162.svg) [公式≈: TprioT_{2min2}()100_{TX}≥≥], if ![](media_svg/image163.svg) [公式≈: Tprio_{2min}()_{TX}] is provided by higher layers for ![](media_svg/image164.svg) [公式: prio_{TX}], otherwise ![](media_svg/image165.svg) [公式: 20≥T_{2}≥100]. UE selection of ![](media_svg/image166.svg) [公式≈: ^{T}2] shall fulfil the latency requirement. The total number of the candidate single-subframe resources is denoted by![](media_svg/image167.svg) [公式≈: ^{M}total].

2) The UE shall monitor subframes ![](media_svg/image168.svg) [公式≈: ^{t}^{SL}n±−10≠P_{step}],![](media_svg/image169.svg) [公式≈: ^{t}^{SL}n±−10≠P_{step}+1], …, ![](media_svg/image170.svg) [公式≈: ^{t}^{SL}n±−1] except for those in which its transmissions occur, where ![](media_svg/image171.svg) [公式: t^{SL}_{n}_{±}=n] if subframe n belongs to the set ![](media_svg/image172.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max})], otherwise subframe ![](media_svg/image173.svg) [公式≈: _{t}SL_{n}_{±}]is the first subframe after subframe n belonging to the set ![](media_svg/image174.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max})]. The UE shall perform the behaviour in the following steps based on PSCCH decoded and S-RSSI measured in these subframes.

3) The parameter ![](media_svg/image175.svg) [公式≈: ^{Th}a,b] is set to the value indicated by the i-th SL-ThresPSSCH-RSRP field in SL-ThresPSSCH-RSRP-List where $ i=(a-1)*8+b $.

4) The set ![](media_svg/image176.svg) [公式≈: ^{S}A] is initialized to the union of all the candidate single-subframe resources. The set ![](media_svg/image177.svg) [公式≈: ^{S}B] is initialized to an empty set.

5) The UE shall exclude any candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from the set ![](media_svg/image178.svg) [公式≈: ^{S}A] if it meets all the following conditions:

- the UE has not monitored subframe ![](media_svg/image179.svg) [公式≈: _{t}_{z}SL] in Step 2.

- there is an integer j which meets ![](media_svg/image180.svg) [公式≈: y+j≠P_{rsvp}^{&apos;}_{_}_{TX}=z+P_{step}≠k≠q] where j=0, 1, …, ![](media_svg/image181.svg) [公式≈: ^{C}resel^{−}^{1}], ![](media_svg/image94.svg) [公式≈: ^{P}rsvp^{&apos;}_TX^{=}^{P}step^{≠}^{P}rsvp_TX^{/}^{100}], k is any value allowed by the higher layer parameter restrictResourceReservationPeriod and q=1,2,…,Q. Here, ![](media_svg/image182.svg) [公式: Q=_{k}^{1}] if ![](media_svg/image183.svg) [公式: k<1] and ![](media_svg/image184.svg) [公式≈: n^{&apos;}−z≥P_{step}≠k], where ![](media_svg/image185.svg) [公式≈: ^{t}_{n}^{SL}&apos;^{=}^{n}] if subframe n belongs to the set ![](media_svg/image186.svg) [公式≈: t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max}], otherwise subframe ![](media_svg/image187.svg) [公式≈: ^{t}_{n}^{SL}&apos;] is the first subframe belonging to the set ![](media_svg/image186.svg) [公式≈: t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max}] after subframe n; and ![](media_svg/image188.svg) [公式: Q=1] otherwise.

6) The UE shall exclude any candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from the set ![](media_svg/image178.svg) [公式≈: ^{S}A] if it meets all the following conditions:

- the UE receives an SCI format 1 in subframe ![](media_svg/image189.svg) [公式≈: _{t}_{m}SL], and "Resource reservation" field and "Priority" field in the received SCI format 1 indicate the values ![](media_svg/image190.svg) [公式≈: ^{P}rsvp_RX] and ![](media_svg/image191.svg) [公式: prio_{RX}], respectively according to Clause 14.2.1.

- PSSCH-RSRP measurement according to the received SCI format 1 is higher than ![](media_svg/image192.svg) [公式≈: ^{Th}prio_{TX},prio_{RX}].

- the SCI format received in subframe ![](media_svg/image189.svg) [公式≈: _{t}_{m}SL]or the same SCI format 1 which is assumed to be received in subframe(s) ![](media_svg/image193.svg) [公式≈: ^{t}^{m}^{SL}^{+}^{q}^{≠}^{P}step^{≠}^{P}rsvp_RX] determines according to 14.1.1.4C the set of resource blocks and subframes which overlaps with ![](media_svg/image194.svg) [公式≈: R_{x}_{,}_{y}_{+}_{j}_{≠}_{P}_{rsvp}&apos;_{_}_{TX}] for q=1, 2, …, Q and j=0, 1, …, ![](media_svg/image181.svg) [公式≈: ^{C}resel^{−}^{1}]. Here, ![](media_svg/image195.svg) [公式≈: ^{Q}^{=}^{P}rsvp^{1}_RX]if ![](media_svg/image196.svg) [公式≈: ^{P}rsvp_RX^{<}^{1}] and ![](media_svg/image197.svg) [公式≈: ^{n}^{±}^{−}^{m}^{≥}^{P}step^{≠}^{P}rsvp_RX], where ![](media_svg/image198.svg) [公式: t^{SL}_{n}_{±}=n] if subframe n belongs to the set ![](media_svg/image199.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max})], otherwise subframe ![](media_svg/image200.svg) [公式≈: _{t}SL_{n}_{±}]is the first subframe after subframe n belonging to the set ![](media_svg/image199.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max})]; otherwise ![](media_svg/image201.svg) [公式: Q=1].

7) If the number of candidate single-subframe resources remaining in the set ![](media_svg/image202.svg) [公式≈: ^{S}A] is smaller than ![](media_svg/image203.svg) [公式≈: ^{0.2}^{∪}^{M}total], then Step 4 is repeated with ![](media_svg/image175.svg) [公式≈: ^{Th}a,b] increased by 3 dB.

8) For a candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] remaining in the set![](media_svg/image202.svg) [公式≈: ^{S}A], the metric ![](media_svg/image204.svg) [公式≈: ^{E}x,y] is defined as the linear average of S-RSSI measured in sub-channels x+k for ![](media_svg/image205.svg) [公式≈: k=0,...,L_{subCH}−1] in the monitored subframes in Step 2 that can be expressed by ![](media_svg/image206.svg) [公式≈: ^{t}y^{SL}−P_{step}*j] for a non-negative integer j if ![](media_svg/image207.svg) [公式≈: ^{P}rsvp_TX^{÷}^{100}], and ![](media_svg/image208.svg) [公式≈: ^{t}^{SL}^{y}^{−}^{P}rsvp^{&apos;}_TX^{*}^{j}] for a non-negative integer j otherwise.

9) The UE moves the candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] with the smallest metric ![](media_svg/image204.svg) [公式≈: ^{E}x,y] from the set ![](media_svg/image202.svg) [公式≈: ^{S}A] to ![](media_svg/image209.svg) [公式≈: ^{S}B]. This step is repeated until the number of candidate single-subframe resources in the set ![](media_svg/image209.svg) [公式≈: ^{S}B] becomes greater than or equal to ![](media_svg/image210.svg) [公式≈: ^{0.2}^{∪}^{M}total],

10) When the UE is configured by upper layers to transmit using resource pools on multiple carriers, it shall exclude a candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from ![](media_svg/image209.svg) [公式≈: ^{S}B] if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set ![](media_svg/image209.svg) [公式≈: ^{S}B] to higher layers.

If partial sensing is configured by higher layers then the following steps are used:

1) A candidate single-subframe resource for PSSCH transmission ![](media_svg/image153.svg) [公式≈: ^{R}x,y] is defined as a set of ![](media_svg/image154.svg) [公式≈: ^{L}subCH] contiguous sub-channels with sub-channel x+j in subframe ![](media_svg/image155.svg) [公式≈: _{t}_{y}SL] where ![](media_svg/image156.svg) [公式≈: j=0,...,L_{subCH}−1]. The UE shall determine by its implementation a set of subframes which consists of at least ![](media_svg/image211.svg) [公式: Y] subframes within the time interval ![](media_svg/image158.svg) [公式: [n+T_{1},n+T_{2}]] where selections of ![](media_svg/image159.svg) [公式≈: ^{T}1] and ![](media_svg/image160.svg) [公式≈: ^{T}2] are up to UE implementations under ![](media_svg/image161.svg) [公式: T_{1}≥4] and ![](media_svg/image162.svg) [公式≈: TprioT_{2min2}()100_{TX}≥≥], if ![](media_svg/image212.svg) [公式≈: Tprio_{2min}()_{TX}] is provided by higher layers for ![](media_svg/image213.svg) [公式: prio_{TX}], otherwise ![](media_svg/image165.svg) [公式: 20≥T_{2}≥100]. UE selection of ![](media_svg/image166.svg) [公式≈: ^{T}2] shall fulfil the latency requirement and ![](media_svg/image211.svg) [公式: Y] shall be greater than or equal to the high layer parameter minNumCandidateSF. The UE shall assume that any set of ![](media_svg/image157.svg) [公式≈: ^{L}subCH] contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the determined set of subframes correspond to one candidate single-subframe resource. The total number of the candidate single-subframe resources is denoted by![](media_svg/image167.svg) [公式≈: ^{M}total].

2) If a subframe ![](media_svg/image214.svg) [公式≈: _{t}_{y}SL] is included in the set of subframes in Step 1, the UE shall monitor any subframe ![](media_svg/image215.svg) [公式≈: ^{t}^{SL}ykP−≠_{step}] if k-th bit of the high layer parameter gapCandidateSensing is set to 1. The UE shall perform the behaviour in the following steps based on PSCCH decoded and S-RSSI measured in these subframes.

3) The parameter ![](media_svg/image175.svg) [公式≈: ^{Th}a,b] is set to the value indicated by the i-th SL-ThresPSSCH-RSRP field in SL-ThresPSSCH-RSRP-List where $ i=(a-1)*8+b $.

4) The set ![](media_svg/image176.svg) [公式≈: ^{S}A] is initialized to the union of all the candidate single-subframe resources. The set ![](media_svg/image177.svg) [公式≈: ^{S}B] is initialized to an empty set.

5) The UE shall exclude any candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from the set ![](media_svg/image178.svg) [公式≈: ^{S}A] if it meets all the following conditions:

- the UE receives an SCI format 1 in subframe ![](media_svg/image189.svg) [公式≈: _{t}_{m}SL], and "Resource reservation" field and "Priority" field in the received SCI format 1 indicate the values ![](media_svg/image190.svg) [公式≈: ^{P}rsvp_RX] and ![](media_svg/image191.svg) [公式: prio_{RX}], respectively according to Clause 14.2.1.

- PSSCH-RSRP measurement according to the received SCI format 1 is higher than ![](media_svg/image192.svg) [公式≈: ^{Th}prio_{TX},prio_{RX}].

- the SCI format received in subframe ![](media_svg/image189.svg) [公式≈: _{t}_{m}SL]or the same SCI format 1 which is assumed to be received in subframe(s) ![](media_svg/image193.svg) [公式≈: ^{t}^{m}^{SL}^{+}^{q}^{≠}^{P}step^{≠}^{P}rsvp_RX] determines according to 14.1.1.4C the set of resource blocks and subframes which overlaps with ![](media_svg/image194.svg) [公式≈: R_{x}_{,}_{y}_{+}_{j}_{≠}_{P}_{rsvp}&apos;_{_}_{TX}] for q=1, 2, …, Q and j=0, 1, …, ![](media_svg/image181.svg) [公式≈: ^{C}resel^{−}^{1}]. Here, ![](media_svg/image195.svg) [公式≈: ^{Q}^{=}^{P}rsvp^{1}_RX]if ![](media_svg/image196.svg) [公式≈: ^{P}rsvp_RX^{<}^{1}] and ![](media_svg/image216.svg) [公式≈: ^{y}^{&apos;}^{−}^{m}^{≥}^{P}step^{≠}^{P}rsvp_RX^{+}^{P}step], where ![](media_svg/image217.svg) [公式≈: ^{t}y^{SL}&apos;] is the last subframe of the ![](media_svg/image218.svg) [公式: Y] subframes , and ![](media_svg/image201.svg) [公式: Q=1] otherwise.

6) If the number of candidate single-subframe resources remaining in the set ![](media_svg/image202.svg) [公式≈: ^{S}A] is smaller than ![](media_svg/image203.svg) [公式≈: ^{0.2}^{∪}^{M}total], then Step 4 is repeated with ![](media_svg/image175.svg) [公式≈: ^{Th}a,b] increased by 3 dB.

7) For a candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] remaining in the set![](media_svg/image202.svg) [公式≈: ^{S}A], the metric ![](media_svg/image204.svg) [公式≈: ^{E}x,y] is defined as the linear average of S-RSSI measured in sub-channels x+k for ![](media_svg/image205.svg) [公式≈: k=0,...,L_{subCH}−1] in the monitored subframes in Step 2 that can be expressed by ![](media_svg/image206.svg) [公式≈: ^{t}y^{SL}−P_{step}*j] for a non-negative integer j.

8) The UE moves the candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] with the smallest metric ![](media_svg/image204.svg) [公式≈: ^{E}x,y] from the set ![](media_svg/image202.svg) [公式≈: ^{S}A] to ![](media_svg/image209.svg) [公式≈: ^{S}B]. This step is repeated until the number of candidate single-subframe resources in the set ![](media_svg/image209.svg) [公式≈: ^{S}B] becomes greater than or equal to ![](media_svg/image210.svg) [公式≈: ^{0.2}^{∪}^{M}total].

9) When the UE is configured by upper layers to transmit using resource pools on multiple carriers, it shall exclude a candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from ![](media_svg/image209.svg) [公式≈: ^{S}B] if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set ![](media_svg/image209.svg) [公式≈: ^{S}B] to higher layers.

If transmission based on random selection is configured by upper layers and when the UE is configured by upper layers to transmit using resource pools on multiple carriers, the following steps are used:

1) A candidate single-subframe resource for PSSCH transmission ![](media_svg/image153.svg) [公式≈: ^{R}x,y] is defined as a set of ![](media_svg/image154.svg) [公式≈: ^{L}subCH] contiguous sub-channels with sub-channel x+j in subframe ![](media_svg/image155.svg) [公式≈: _{t}_{y}SL] where ![](media_svg/image156.svg) [公式≈: j=0,...,L_{subCH}−1]. The UE shall assume that any set of ![](media_svg/image157.svg) [公式≈: ^{L}subCH] contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the time interval ![](media_svg/image158.svg) [公式: [n+T_{1},n+T_{2}]] corresponds to one candidate single-subframe resource, where selections of ![](media_svg/image159.svg) [公式≈: ^{T}1] and ![](media_svg/image160.svg) [公式≈: ^{T}2] are up to UE implementations under ![](media_svg/image161.svg) [公式: T_{1}≥4] and ![](media_svg/image162.svg) [公式≈: TprioT_{2min2}()100_{TX}≥≥], if ![](media_svg/image163.svg) [公式≈: Tprio_{2min}()_{TX}] is provided by higher layers for ![](media_svg/image164.svg) [公式: prio_{TX}], otherwise ![](media_svg/image165.svg) [公式: 20≥T_{2}≥100]. UE selection of ![](media_svg/image166.svg) [公式≈: ^{T}2] shall fulfil the latency requirement. The total number of the candidate single-subframe resources is denoted by![](media_svg/image167.svg) [公式≈: ^{M}total].

2) The set ![](media_svg/image176.svg) [公式≈: ^{S}A] is initialized to the union of all the candidate single-subframe resources. The set ![](media_svg/image177.svg) [公式≈: ^{S}B] is initialized to an empty set.

3) The UE moves the candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from the set ![](media_svg/image202.svg) [公式≈: ^{S}A] to ![](media_svg/image209.svg) [公式≈: ^{S}B].

4) The UE shall exclude a candidate single-subframe resource ![](media_svg/image153.svg) [公式≈: ^{R}x,y] from ![](media_svg/image209.svg) [公式≈: ^{S}B] if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set ![](media_svg/image209.svg) [公式≈: ^{S}B] to higher layers.

#### 14.1.1.7 Conditions for selecting resources when the number of HARQ transmissions is two in sidelink transmission mode 4

When a set of subframes ![](media_svg/image219.svg) [公式≈: t_{n}^{SL}_{+}_{j}_{≠}_{P}_{rsvp}&apos;_{_}_{TX}] for ![](media_svg/image220.svg) [公式: j=0,1,...,J−1] have been selected for a set of transmission opportunities of PSSCH, a set of subframes ![](media_svg/image221.svg) [公式≈: ^{t}n^{SL}+k+j≠P_{rsvp}^{&apos;}_{_}_{TX}] for ![](media_svg/image222.svg) [公式: j=0,1,...,J−1] for another set of transmission opportunities of PSSCH shall meet the conditions ![](media_svg/image223.svg) [公式: −≥≥1515k], ![](media_svg/image224.svg) [公式: k⎯0] and $ k $ mod $ P_{rsvp\_TX}^{'}\neq  0 $ where ![](media_svg/image94.svg) [公式≈: ^{P}rsvp^{&apos;}_TX^{=}^{P}step^{≠}^{P}rsvp_TX^{/}^{100}] and ![](media_svg/image225.svg) [公式: J] is the maximum number of transmission opportunities of PSSCH in a selected subframe set. Here, ![](media_svg/image95.svg) [公式≈: ^{P}rsvp_TX] is the resource reservation interval provided by higher layers.

### 14.1.2 UE procedure for receiving the PSSCH

For sidelink transmission mode 1, a UE upon detection of SCI format 0 on PSCCH can decode PSSCH according to the detected SCI format 0.

For sidelink transmission mode 2, a UE upon detection of SCI format 0 on PSCCH can decode PSSCH according to the detected SCI format 0, and associated PSSCH resource configuration configured by higher layers.

For sidelink transmission mode 3, a UE upon detection of SCI format 1 on PSCCH can decode PSSCH according to the detected SCI format 1, and associated PSSCH resource configuration configured by higher layers.

For sidelink transmission mode 4, a UE upon detection of SCI format 1 on PSCCH can decode PSSCH according to the detected SCI format 1, and associated PSSCH resource configuration configured by higher layers.

### 14.1.3 UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 2

For a PSCCH period associated with the PSCCH resource configuration (determined in Clause 14.2.3) which is also associated with the PSSCH resource configuration, the UE determines a PSSCH pool consisting of a subframe pool and resource block pool as follows.

- For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

- Within the PSCCH period, the uplink subframes with subframe index greater than or equal to ![](media_svg/image226.svg) [公式≈: ^{j}begin^{+}^{O}2] are denoted by![](media_svg/image227.svg) [公式≈: (l_{0},l_{1},....,.l_{N}_{±}_{−}_{1})] arranged in increasing order of subframe index, where ![](media_svg/image228.svg) [公式≈: ^{j}begin] is described in Clause 14.2.3 and ![](media_svg/image229.svg) [公式≈: ^{O}2] is the offsetIndicator-r12 indicated by the PSSCH resource configuration, where ![](media_svg/image230.svg) [公式: N^{±}]denotes the number of uplink subframes within the PSCCH period with subframe index greater than or equal to ![](media_svg/image226.svg) [公式≈: ^{j}begin^{+}^{O}2].

- A bitmap ![](media_svg/image231.svg) [公式≈: b_{0},b_{1},b_{2},...,b_{N}_{±}_{−}_{1}] is determined using![](media_svg/image232.svg) [公式≈: ^{b}j^{=}^{a}jmodN_{B}], for ![](media_svg/image233.svg) [公式: 0≥j<N±], where ![](media_svg/image234.svg) [公式≈: a_{0},a_{1},a_{2},...,a_{N}_{B}_{−}_{1}] and ![](media_svg/image235.svg) [公式≈: ^{N}B] are the bitmap and the length of the bitmap indicated by subframeBitmap-r12, respectively.

- A subframe ![](media_svg/image236.svg) [公式≈: ^{l}j] (![](media_svg/image237.svg) [公式: 0≥j<N±]) belongs to the subframe pool if ![](media_svg/image238.svg) [公式: b_{j}=1]. The subframes in the subframe pool are denoted by![](media_svg/image239.svg) [公式≈: _{(}_{l}_{0}PSSCH_{,}_{l}_{1}PSSCH_{,....,.}_{l}_{L}PSSCH_{PSSCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and![](media_svg/image29.svg) [公式≈: ^{L}PSSCH] denotes the number of subframes in the subframe pool.

- A PRB with index ![](media_svg/image240.svg) [公式: q] (![](media_svg/image241.svg) [公式: 0≥q<N_{RB}^{SL}]) belongs to the resource block pool if ![](media_svg/image242.svg) [公式: S1≥q<S1+M] or if ![](media_svg/image243.svg) [公式: S2−M<q≥S2], where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSSCH resource configuration respectively.

- The resource blocks in the resource block pool are denoted by![](media_svg/image244.svg) [公式≈: (m0^{PSSCH},m1^{PSSCH},....,mM^{PSSCH}_{RB}PSSCH_RP−1)] arranged in increasing order of resource block indices and ![](media_svg/image80.svg) [公式≈: _{M}_{RB}PSSCH_RP] is the number of resource blocks in the resource block pool.

14.1.4 UE procedure for determining subframe pool for sidelink transmission mode 1

For a PSCCH period associated with the PSCCH resource configuration (described in Clause 14.2.3) which is also associated with the PSSCH resource configuration, the UE determines a PSSCH pool consisting of a subframe pool as follows.

- For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

- Each uplink subframe with subframe index greater than or equal to ![](media_svg/image245.svg) [公式≈: _{l}_{L}PSCCH_{PSCCH}_{−}_{1}_{+}_{1}]belongs to the subframe pool for PSSCH, where ![](media_svg/image245.svg) [公式≈: _{l}_{L}PSCCH_{PSCCH}_{−}_{1}_{+}_{1}] and ![](media_svg/image246.svg) [公式≈: ^{L}PSCCH] are described in Clause 14.2.3.

- The subframes in the subframe pool for PSSCH are denoted by![](media_svg/image239.svg) [公式≈: _{(}_{l}_{0}PSSCH_{,}_{l}_{1}PSSCH_{,....,.}_{l}_{L}PSSCH_{PSSCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and![](media_svg/image29.svg) [公式≈: ^{L}PSSCH] denotes the number of subframes in the subframe pool.

### 14.1.5 UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 3 and 4

The set of subframes that may belong to a PSSCH resource pool for sidelink transmission mode 3 or 4 is denoted by ![](media_svg/image199.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},...,t_{T}^{SL}_{max})] where

- ![](media_svg/image247.svg) [公式: 0≥t_{i}^{SL}<10240],

- the subframe index is relative to subframe#0 of the radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

- the set includes all the subframes except the following subframes,

- subframes in which SLSS resource is configured,

- downlink subframes and special subframes if the sidelink transmission occurs in a TDD cell,

- reserved subframes which are determined by the following steps:

1) the remaining subframes excluding ![](media_svg/image248.svg) [公式≈: ^{N}slss] and ![](media_svg/image249.svg) [公式≈: ^{N}dssf] subframes from the set of all the subframes are denoted by ![](media_svg/image250.svg) [公式≈: ^{(}^{l}0^{,}^{l}1^{,...,}^{l}(10240−N_{slss}−N_{dssf}−1)^{)}] arranged in increasing order of subframe index, where ![](media_svg/image248.svg) [公式≈: ^{N}slss] is the number of subframes in which SLSS resource is configured within 10240 subframes and ![](media_svg/image249.svg) [公式≈: ^{N}dssf] is the number of downlink subframes and special subframes within 10240 subframes if the sidelink transmission occurs in a TDD cell.

2) a subframe ![](media_svg/image251.svg) [公式≈: l_{r}(0≥r<(10240−N_{slss}−N_{dssf}))] belongs to the reserved subframes if ![](media_svg/image252.svg) [公式≈: _{r}_{=}⋅_{⋅}_{√}m∪(10240_{N}−_{reserved}N_{slss}−N_{dssf})∂_{∂}_{∃}] where ![](media_svg/image253.svg) [公式≈: m=0,...,N_{reserved}−1] and ![](media_svg/image254.svg) [公式≈: ^{N}reserved^{=}^{(}^{10240}^{−}^{N}slss^{−}^{N}dssf^{)}^{mod}^{L}bitmap]. Here, ![](media_svg/image255.svg) [公式≈: ^{L}bitmap] the length of the bitmap is configured by higher layers.

- the subframes are arranged in increasing order of subframe index.

The UE determines the set of subframes assigned to a PSSCH resource pool as follows:

- A bitmap $\left ( b_{0},b_{1},\ldots  ,b_{L_{bitmap}-1}\right ) $ associated with the resource pool is used where ![](media_svg/image255.svg) [公式≈: ^{L}bitmap] the length of the bitmap is configured by higher layers.

- A subframe ![](media_svg/image256.svg) [公式≈: t_{k}^{SL}(0≥k<(10240−N_{slss}−N_{dssf}−N_{reserved}))] belongs to the subframe pool if ![](media_svg/image257.svg) [公式≈: ^{b}k&apos;^{=}^{1}] where ![](media_svg/image258.svg) [公式≈: k&apos;=kmodL_{bitmap}] .

The UE determines the set of resource blocks assigned to a PSSCH resource pool as follows:

- The resource block pool consists of  sub-channels where  is given by higher layer parameter numSubchannel.

- The sub-channel m for ![](media_svg/image259.svg) [公式≈: m=0,1,...,N_{subCH}−1] consists of a set of ![](media_svg/image260.svg) [公式≈: ^{n}subCHsize] contiguous resource blocks with the physical resource block number ![](media_svg/image261.svg) [公式≈: ^{n}PRB^{=}^{n}subCHRBstart^{+}^{m}^{*}^{n}subCHsize^{+}^{j}] for ![](media_svg/image262.svg) [公式≈: j=0,1,...,n_{subCHsize}−1] where ![](media_svg/image118.svg) [公式≈: ^{n}subCHRBstart] and ![](media_svg/image119.svg) [公式≈: ^{n}subCHsize] are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively

## 14.2 Physical Sidelink Control Channel related procedures

For sidelink transmission mode 1, if a UE is configured by higher layers to receive DCI format 5 with the CRC scrambled by the SL-RNTI, the UE shall decode the PDCCH/EPDCCH according to the combination defined in Table 14.2-1.

Table 14.2-1: PDCCH/EPDCCH configured by SL-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 5 | For PDCCH: Common and UE specific by C-RNTIFor EPDCCH: UE specific by C-RNTI |

For sidelink transmission mode 3, if a UE is configured by higher layers to receive DCI format 5A with the CRC scrambled by the SL-V-RNTI or SL-SPS-V-RNTI , the UE shall decode the PDCCH/EPDCCH according to the combination defined in Table 14.2-2. A UE is not expected to receive DCI format 5A with size larger than DCI format 0 in the same search space that DCI format 0 is defined on.

Table 14.2-2: PDCCH/EPDCCH configured by SL-V-RNTI or SL-SPS-V-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 5A | For PDCCH: Common and UE specific by C-RNTIFor EPDCCH: UE specific by C-RNTI |

The carrier indicator field value in DCI format 5A corresponds to v2x-InterFreqInfo.

### 14.2.1 UE procedure for transmitting the PSCCH

For sidelink transmission mode 1and PSCCH period i,

the UE shall determine the subframes and resource blocks for transmitting SCI format 0 as follows.

- SCI format 0 is transmitted in two subframes in the subframe pool and one physical resource block per slot in each of the two subframes, wherein the physical resource blocks belong to the resource block pool, where the subframe pool and the resource block pool are indicated by the PSCCH resource configuration (as defined in Clause 14.2.3)

- the two subframes and the resource blocks are determined using "Resource for PSCCH" field (![](media_svg/image263.svg) [公式≈: ^{n}PSCCH]) in the configured sidelink grant (described in [8]) as described in Clause 14.2.1.1.

the UE shall set the contents of the SCI format 0 as follows:

- the UE shall set the Modulation and coding scheme field according to the Modulation and coding scheme indicated by the higher layer parameter mcs-r12 if the parameter is configured by higher layers.

- the UE shall set the Frequency hopping flag according to the "Frequency hopping flag" field in the configured sidelink grant.

- the UE shall set the Resource block assignment and hopping resource allocation according to the "Resource block assignment and hopping resource allocation" field in the configured sidelink grant.

- the UE shall set the Time resource pattern according to the "Time resource pattern" field in the configured sidelink grant .

- the UE shall set the eleven-bit Timing advance indication to ![](media_svg/image264.svg) [公式≈: ^{I}^{TAI}^{=}^{⋅}^{⋅}√^{N}16^{TA}^{∂}^{∂}∃] to indicate sidelink reception timing adjustment value using the NTA (defined in [3]) value for the UE in the subframe that is no earlier than subframe ![](media_svg/image265.svg) [公式≈: _{l}_{b}PSCCH_{1}_{−}_{4}] (![](media_svg/image266.svg) [公式≈: _{l}_{b}PSCCH_{1}]described in Clause 14.2.1.1).

For sidelink transmission mode 2,

- SCI format 0 is transmitted in two subframes in the subframe pool and one physical resource block per slot in each of the two subframes, wherein the physical resource blocks belongs to the resource block pool, where the subframe pool and the resource block pool are indicated by the PSCCH resource configuration (as defined in Clause 14.2.3)

- the two subframes and the resource blocks are determined using the procedure described in Clause 14.2.1.2

- the UE shall set the eleven-bit Timing advance indication ![](media_svg/image267.svg) [公式≈: ^{I}TAI] in the SCI format 0 to zero.

For sidelink transmission mode 3,

- The UE shall determine the subframes and resource blocks for transmitting SCI format 1 as follows:

- SCI format 1 is transmitted in two physical resource blocks per slot in each subframe where the corresponding PSSCH is transmitted.

- If the UE receives in subframe n DCI format 5A with the CRC scrambled by the SL-V-RNTI, one transmission of PSCCH is in the PSCCH resource ![](media_svg/image268.svg) [公式≈: ^{L}Init] (described in Clause 14.2.4) in the first subframe $ t_{q}^{SL}$ that is included in ![](media_svg/image114.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] and that starts not earlier than $ T_{DL}-\frac {N_{TA}}{2}\times  T_{S}+\left ( 4+m\right ) \times  10^{-3}$. ![](media_svg/image268.svg) [公式≈: ^{L}Init] is the value indicated by "Lowest index of the sub-channel allocation to the initial transmission" associated with the configured sidelink grant (described in [8]) if the field "Lowest index of the sub-channel allocation to the initial transmission" in the corresponding DCI format 5A is present and $ L_{Init}=0 $ otherwise, ![](media_svg/image114.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] is determined by Clause 14.1.5, the value m is indicated by 'SL index' field in the corresponding DCI format 5A according to Table 14.2.1-1 if this field is present and m=0 otherwise, $ T_{DL}$ is the start of the downlink subframe carrying the DCI, and $ N_{TA}$ and $ T_{S}$ are described in [3].

- If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] in subframe ![](media_svg/image270.svg) [公式≈: ^{t}q^{SL}+SF_{gap}], where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant. ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] corresponds to the value ![](media_svg/image99.svg) [公式≈: _{n}_{subCH}start] determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

- If the UE receives in subframe n DCI format 5A with the CRC scrambled by the SL-SPS-V-RNTI , the UE shall consider the received DCI information as a valid sidelink semi-persistent activation or release only for the SPS configuration indicated by the SL SPS configuration index field. If the received DCI activates an SL SPS configuration, one transmission of PSCCH is in the PSCCH resource ![](media_svg/image268.svg) [公式≈: ^{L}Init] (described in Clause 14.2.4) in the first subframe $ t_{q}^{SL}$ that is included in ![](media_svg/image114.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] and that starts not earlier than $ T_{DL}-\frac {N_{TA}}{2}\times  T_{S}+\left ( 4+m\right ) \times  10^{-3}$. ![](media_svg/image268.svg) [公式≈: ^{L}Init] is the value indicated by "Lowest index of the sub-channel allocation to the initial transmission" associated with the configured sidelink grant (described in [8]) if the field "Lowest index of the sub-channel allocation to the initial transmission" in the corresponding DCI format 5A is present and $ L_{Init}=0 $ otherwise, ![](media_svg/image114.svg) [公式≈: (t_{0}^{SL},t_{1}^{SL},t_{2}^{SL},...)] is determined by Clause 14.1.5, the value m is indicated by 'SL index' field in the corresponding DCI format 5A according to Table 14.2.1-1 if this field is present and m=0 otherwise, $ T_{DL}$ is the start of the downlink subframe carrying the DCI, and $ N_{TA}$ and $ T_{S}$ are described in [3]..

- If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] in subframe ![](media_svg/image271.svg) [公式≈: ^{t}q^{SL}+SF_{gap}], where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant. ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] corresponds to the value ![](media_svg/image99.svg) [公式≈: _{n}_{subCH}start] determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

- The UE shall set the contents of the SCI format 1 as follows:

- the UE shall set the Modulation and coding scheme as indicated by higher layers.

- the UE shall set the "Priority" field according to the highest priority among those priority(s) indicated by higher layers corresponding to the transport block. Priority field '000' corresponds to priority '1', priority field '001' corresponds to priority '2', and so on.

- the UE shall set the Time gap between initial transmission and retransmission field, the Frequency resource location of the initial transmission and retransmission field, and the Retransmission index field such that the set of time and frequency resources determined for PSSCH according to Clause 14.1.1.4C is in accordance with the PSSCH resource allocation indicated by the configured sidelink grant.

- the UE shall set the Resource reservation according to table 14.2.1-2 based on indicated value X, where X is equal to the Resource reservation interval provided by higher layers divided by 100.

- Each transmission of SCI format 1 is transmitted in one subframe and two physical resource blocks per slot of the subframe.

- The UE shall randomly select the cyclic shift ![](media_svg/image272.svg) [公式≈: ^{n}cs,Λ] among {0, 3, 6, 9} in each PSCCH transmission.

For sidelink transmission mode 4,

- The UE shall determine the subframes and resource blocks for transmitting SCI format 1 as follows:

- SCI format 1 is transmitted in two physical resource blocks per slot in each subframe where the corresponding PSSCH is transmitted.

- If the configured sidelink grant from higher layer indicates the PSCCH resource in subframe ![](media_svg/image273.svg) [公式≈: _{t}_{n}SL], one transmission of PSCCH is in the indicated PSCCH resource m (described in Clause 14.2.4) in subframe ![](media_svg/image274.svg) [公式≈: _{t}_{n}SL].

- If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] in subframe ![](media_svg/image275.svg) [公式≈: ^{t}n^{SL}+SF_{gap}] where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant, ![](media_svg/image269.svg) [公式≈: ^{L}ReTX] corresponds to the value ![](media_svg/image99.svg) [公式≈: _{n}_{subCH}start] determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

- the UE shall set the contents of the SCI format 1 as follows:

- the UE shall set the Modulation and coding scheme as indicated by higher layers.

- the UE shall set the "Priority" field according to the highest priority among those priority(s) indicated by higher layers corresponding to the transport block. Priority field '000' corresponds to priority '1', priority field '001' corresponds to priority '2', and so on.

- the UE shall set the Time gap between initial transmission and retransmission field, the Frequency resource location of the initial transmission and retransmission field, and the Retransmission index field such that the set of time and frequency resources determined for PSSCH according to Clause 14.1.1.4C is in accordance with the PSSCH resource allocation indicated by the configured sidelink grant.

- the UE shall set the Resource reservation field according to table 14.2.1-2 based on indicated value X, where X is equal to the Resource reservation interval provided by higher layers divided by 100.

- Each transmission of SCI format 1 is transmitted in one subframe and two physical resource blocks per slot of the subframe.

- The UE shall randomly select the cyclic shift ![](media_svg/image272.svg) [公式≈: ^{n}cs,Λ] among {0, 3, 6, 9} in each PSCCH transmission.

Table 14.2.1-1: Mapping of DCI format 5A offset field to indicated value m

| SL index field in DCI format 5A | Indicated value m |
| --- | --- |
| '00' | 0 |
| '01' | 1 |
| '10' | 2 |
| '11' | 3 |

Table 14.2.1-2: Determination of the Resource reservation field in SCI format 1

| Resource reservation field in SCI format 1 | Indicated value X | Condition |
| --- | --- | --- |
| '0001', '0010', …, '1010' | Decimal equivalent of the field | The higher layer decides to keep the resource for the transmission of the next transport block and the value X meets ![](media_svg/image276.svg) [公式: 1≥X≥10]. |
| '1011' | 0.5 | The higher layer decides to keep the resource for the transmission of the next transport block and the value X is 0.5. |
| '1100' | 0.2 | The higher layer decides to keep the resource for the transmission of the next transport block and the value X is 0.2. |
| '0000' | 0 | The higher layer decides not to keep the resource for the transmission of the next transport block. |
| '1101', '1110', '1111' | Reserved |  |

#### 14.2.1.1 UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 1

For ![](media_svg/image277.svg) [公式≈: ^{0}^{≥}^{n}PSCCH^{<}√^{M}RB^{PSCCH}^{_}^{RP}^{/}^{2}∃^{∪}^{L}PSCCH],

- one transmission of the PSCCH is in resource block ![](media_svg/image278.svg) [公式≈: _{m}_{a}PSCCH_{1}]of subframe ![](media_svg/image279.svg) [公式≈: _{l}_{b}PSCCH_{1}] of the PSCCH period, where ![](media_svg/image280.svg) [公式≈: ^{a}^{1}^{=}√^{n}PSCCH^{/}^{L}PSCCH∃] and ![](media_svg/image281.svg) [公式≈: ^{b}^{1}^{=}^{n}PSCCH^{mod}^{L}PSCCH].

- the other transmission of the PSCCH is in resource block ![](media_svg/image282.svg) [公式≈: _{m}_{a}PSCCH_{2}] of subframe ![](media_svg/image283.svg) [公式≈: _{l}_{b}PSCCH_{2}] of the PSCCH period, where ![](media_svg/image284.svg) [公式≈: ^{a}^{2}^{=}√^{n}PSCCH^{/}^{L}PSCCH∃^{+}√^{M}RB^{PSCCH}^{_}^{RP}^{/}^{2}∃] and ![](media_svg/image285.svg) [公式≈: ^{b}^{2}^{=}^{(}^{n}PSCCH^{+}^{1}^{+}√^{n}PSCCH^{/}^{L}PSCCH∃^{mod}^{(}^{L}PSCCH^{−}^{1}^{)}^{)}^{mod}^{L}PSCCH].

where![](media_svg/image286.svg) [公式≈: _{(}_{l}_{0}PSCCH_{,}_{l}_{1}PSCCH_{,....,.}_{l}_{L}PSCCH_{PSCCH}_{−}_{1}_{)}],![](media_svg/image287.svg) [公式≈: (m0^{PSCCH},m1^{PSCCH},....,mM^{PSCCH}_{RB}PSCCH_RP−1)], ![](media_svg/image288.svg) [公式≈: ^{L}PSCCH]and ![](media_svg/image289.svg) [公式≈: _{M}_{RB}PSCCH_RP]are described in Clause 14.2.3.

#### 14.2.1.2 UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 2

The allowed values for PSCCH resource selection are given by 0,1… ![](media_svg/image290.svg) [公式≈: ^{(}√^{M}RB^{PSCCH}^{_}^{RP}^{/}^{2}∃^{∪}^{L}PSCCH^{−}^{1}^{)}] where ![](media_svg/image288.svg) [公式≈: ^{L}PSCCH]and ![](media_svg/image289.svg) [公式≈: _{M}_{RB}PSCCH_RP] described in Clause 14.2.3. The two subframes and the resource blocks are determined using selected resource value ![](media_svg/image291.svg) [公式≈: ^{n}PSCCH] (described in [8]) and the procedure described in Clause 14.2.1.1.

#### 14.2.1.3 UE procedure for PSCCH power control

For sidelink transmission mode 1 and PSCCH period i, the UE transmit power ![](media_svg/image292.svg) [公式≈: ^{P}PSCCH] for PSCCH transmission is given by the following

- if the TPC command field in the configured sidelink grant (described in [8]) for PSCCH period i is set to 0

- ![](media_svg/image293.svg) [公式≈: ^{P}PSCCH^{=}^{P}CMAX,PSCCH]

- if the TPC command field in the configured sidelink grant (described in [8]) for PSCCH period i is set to 1

- ![](media_svg/image294.svg) [公式≈: ^{P}PSCCH^{=}^{min}^{{}^{P}CMAX,PSCCH^{,}^{10}^{log}10^{(}^{M}PSCCH^{)}^{+}^{P}O_PSCCH,1^{+}^{Α}PSCCH,1^{∪}^{PL}^{}}] [dBm]

where ![](media_svg/image295.svg) [公式≈: ^{P}CMAX,PSCCH] is defined in [6], and ![](media_svg/image296.svg) [公式≈: ^{M}PSCCH]=1 and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image297.svg) [公式≈: ^{P}O_PSCCH,1] and ![](media_svg/image298.svg) [公式≈: ^{Α}PSCCH,1] are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSCCH resource configuration.

For sidelink transmission mode 2, the UE transmit power ![](media_svg/image299.svg) [公式≈: ^{P}PSCCH] for PSCCH transmission is given by

![](media_svg/image300.svg) [公式≈: ^{P}PSCCH^{=}^{min}^{{}^{P}CMAX,PSCCH^{,}^{10}^{log}10^{(}^{M}PSCCH^{)}^{+}^{P}O_PSCCH,2^{+}^{Α}PSCCH,2^{∪}^{PL}^{}}] [dBm] ,

where ![](media_svg/image301.svg) [公式≈: ^{P}CMAX,PSCCH] is the ![](media_svg/image302.svg) [公式≈: ^{P}CMAX,c]configured by higher layers and ![](media_svg/image303.svg) [公式≈: ^{M}PSCCH]=1 and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}]is defined in Clause 5.1.1.1. ![](media_svg/image304.svg) [公式≈: ^{P}O_PSCCH,2] and ![](media_svg/image305.svg) [公式≈: ^{Α}PSCCH,2] are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSCCH resource configuration.

For sidelink transmission mode 3, the UE transmit power ![](media_svg/image299.svg) [公式≈: ^{P}PSCCH] for PSCCH transmission is given by

![](media_svg/image306.svg) [公式≈: ^{P}^{PSCCH}^{+}^{=}^{min}^{10}^{log}^{√}^{⌡}⌠_{⌡}_{∞}^{P}^{10}CMAX^{⊇}^{⊕}^{⊕}^{⊕}^{⊗}^{M}^{,}^{PSSCH}^{10}^{10}^{10}^{log}^{3}^{+}^{≠}^{10}10^{M}^{10}^{⊇}^{⊕}_{⊕}_{⊗}^{3}^{PSCCH}^{M}^{≠}^{M}PSSCH^{PSCCH}^{+}^{10}^{⇒}^{⇐}^{⇐}^{⇐}^{⇔}^{10}^{3}^{≠}^{M}PSCCH^{⇒}^{⇐}_{⇐}_{⇔}^{+}^{P}O_PSSCH,3^{+}^{Α}PSSCH,3^{∪}^{PL}^{∅}^{⌡}∇_{⌡}_{∈}] [dBm],

where ![](media_svg/image307.svg) [公式≈: ^{P}CMAX] is defined in [6], ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH]is the bandwidth of the PSSCH resource assignment expressed in number of resource block, ![](media_svg/image308.svg) [公式≈: ^{M}PSCCH^{=}^{2}], and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image141.svg) [公式≈: ^{P}O_PSSCH,3] and ![](media_svg/image142.svg) [公式≈: ^{Α}PSSCH,3] are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 4, the UE transmit power ![](media_svg/image299.svg) [公式≈: ^{P}PSCCH] for PSCCH transmission in subframe n is given by

![](media_svg/image309.svg) [公式≈: ^{PB}^{PSCCH10}^{=+}^{10log}^{⊇⇒}^{⊕⇐}^{⊕⇐}^{⊕⇐}⊗⇔^{MM}PSSCHPSCCH^{10}^{10}^{3}^{+≠}^{≠}^{10}^{M}^{10}^{3}^{PSCCH}] [dBm],

where![](media_svg/image307.svg) [公式≈: ^{P}CMAX] is defined in [6], ![](media_svg/image131.svg) [公式≈: ^{M}PSSCH]is the bandwidth of the PSSCH resource assignment expressed in number of resource block, ![](media_svg/image308.svg) [公式≈: ^{M}PSCCH^{=}^{2}], and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image310.svg) [公式≈: ^{P}O_PSSCH,4] and ![](media_svg/image311.svg) [公式≈: ^{Α}PSSCH,4] are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration. If higher layer parameter maxTxpower is configured then

![](media_svg/image312.svg) [公式≈: ^{BPPMMPPL}^{=+≠++∪}^{min,,10log10}^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}CMAX_10PSSCHPSCCHO_PSSCH,4,4MAXCBRPSSCH^{⊇⇒}⊕⇐_{⊗⇔}^{10}^{3}^{Α}]

else

![](media_svg/image313.svg) [公式≈: ^{BPMMPPL}^{=+≠++∪}^{min,10log10}^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}CMAX10PSSCHPSCCHO_PSSCH,4,4^{⊇⇒}⊕⇐_{⊗⇔}^{10}^{3}^{Α}PSSCH]

where![](media_svg/image150.svg) [公式≈: ^{P}MAX_CBR] is set to a maxTxpower value based on the priority level of the PSSCH and the CBR range which includes the CBR measured in subframe n-4.

### 14.2.2 UE procedure for receiving the PSCCH

For each PSCCH resource configuration associated with sidelink transmission mode 1, a UE configured by higher layers to detect SCI format 0 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration, and using the Group destination IDs indicated by higher layers.

For each PSCCH resource configuration associated with sidelink transmission mode 2, a UE configured by higher layers to detect SCI format 0 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration, and using the Group destination IDs indicated by higher layers.

For each PSCCH resource configuration associated with sidelink transmission mode 3, a UE configured by higher layers to detect SCI format 1 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration.The UE is not required to decode more than one PSCCH at each PSCCH resource candidate. The UE shall not assume any value for the "Reserved bits" before decoding a SCI format 1.

For each PSCCH resource configuration associated with sidelink transmission mode 4, a UE configured by higher layers to detect SCI format 1 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration. The UE is not required to decode more than one PSCCH at each PSCCH resource candidate. The UE shall not assume any value for the "Reserved bits" before decoding a SCI format 1.

### 14.2.3 UE procedure for determining resource block pool and subframe pool for PSCCH

The following procedure is used for sidelink transmission mode 1 and 2.

A PSCCH resource configuration for transmission/reception is associated with a set of periodically occurring time-domain periods (known as PSCCH periods). The i-th PSCCH period begins at subframe with subframe index![](media_svg/image314.svg) [公式≈: j_{begin}=O+i∪P] and ends in subframe with subframe index ![](media_svg/image315.svg) [公式: j_{end}=O+(i+1)∪P−1], where

- ,

- the subframe index is relative to subframe#0 of the radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

- ![](media_svg/image317.svg) [公式: O] is the offsetIndicator-r12 indicated by the PSCCH resource configuration,

- ![](media_svg/image318.svg) [公式: P]is the sc-Period-r12 indicated by the PSCCH resource configuration.

For a PSCCH period, the UE determines a PSCCH pool consisting of a subframe pool and a resource block pool as follows.

- For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

- The first ![](media_svg/image319.svg) [公式: N^{±}]uplink subframes are denoted by![](media_svg/image320.svg) [公式≈: (l_{0},l_{1},...,l_{N}_{±}_{−}_{1})] arranged in increasing order of subframe index, where ![](media_svg/image321.svg) [公式: N^{±}]is the length of the bitmap subframeBitmap-r12 indicated by the PSCCH resource configuration.

- A subframe ![](media_svg/image322.svg) [公式≈: ^{l}j] (![](media_svg/image323.svg) [公式: 0≥j<N±]) belongs to the subframe pool if![](media_svg/image324.svg) [公式: a_{j}=1], where![](media_svg/image325.svg) [公式≈: (a_{0},a_{1},a_{2},...,a_{N}_{±}_{−}_{1})] is the bitmap subframeBitmap-r12 indicated by the PSCCH resource configuration. The subframes in the subframe pool are denoted by![](media_svg/image326.svg) [公式≈: _{(}_{l}_{0}PSCCH_{,}_{l}_{1}PSCCH_{,...,}_{l}_{L}PSCCH_{PSCCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and ![](media_svg/image327.svg) [公式≈: ^{L}PSCCH] is the number of subframes in the subframe pool. A PRB with index ![](media_svg/image240.svg) [公式: q] (![](media_svg/image241.svg) [公式: 0≥q<N_{RB}^{SL}]) belongs to the resource block pool if![](media_svg/image242.svg) [公式: S1≥q<S1+M] or if ![](media_svg/image243.svg) [公式: S2−M<q≥S2], where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSCCH resource configuration respectively.

- The resource blocks in the resource block pool are denoted by![](media_svg/image287.svg) [公式≈: (m0^{PSCCH},m1^{PSCCH},....,mM^{PSCCH}_{RB}PSCCH_RP−1)] arranged in increasing order of resource block indices and ![](media_svg/image289.svg) [公式≈: _{M}_{RB}PSCCH_RP] is the number of resource blocks in the resource block pool.

### 14.2.4 UE procedure for determining resource block pool for PSCCH in sidelink transmission mode 3 and 4

The following procedure is used for sidelink transmission mode 3 and 4.

If a pool is (pre)configured such that a UE always transmits PSCCH and the corresponding PSSCH in adjacent resource blocks in a subframe, the PSCCH resource m is the set of two contiguous resource blocks with the physical resource block number ![](media_svg/image328.svg) [公式≈: ^{n}PRB^{=}^{n}subCHRBstart^{+}^{m}^{*}^{n}subCHsize^{+}^{j}] for j=0 and 1 where ![](media_svg/image329.svg) [公式≈: ^{n}subCHRBstart] and ![](media_svg/image119.svg) [公式≈: ^{n}subCHsize] are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively.

If a pool is (pre)configured such that a UE may transmit PSCCH and the corresponding PSSCH in non-adjacent resource blocks in a subframe, the PSCCH resource m is the set of two contiguous resource blocks with the physical resource block number ![](media_svg/image330.svg) [公式≈: ^{n}PRB^{=}^{n}PSCCHstart^{+}^{2}^{*}^{m}^{+}^{j}] for j=0 and 1 where ![](media_svg/image331.svg) [公式≈: ^{n}PSCCHstart] is given by higher layer parameter startRBPSCCHPool.

## 14.3 Physical Sidelink Discovery Channel related procedures

## 14.3.1 UE procedure for transmitting the PSDCH

If a UE is configured by higher layers to transmit PSDCH according to a PSDCH resource configuration, in a PSDCH period ![](media_svg/image332.svg) [公式: i],

- the number of transmissions for a transport block on PSDCH is ![](media_svg/image333.svg) [公式: N_{SLD}^{TX}=n+1] where ![](media_svg/image334.svg) [公式: n]is given by the higher layer parameter numRetx-r12, and each transmission corresponds to one subframe belonging to a set of subframes, and in each subframe, the PSDCH is transmitted on two physical resource blocks per slot.

- for sidelink discovery type 1,

- the allowed values for PSDCH resource selection are given by 0,1… ![](media_svg/image335.svg) [公式: (N_{t}∪N_{f}−1)], where![](media_svg/image336.svg) [公式≈: ^{N}t^{=}√^{L}PSDCH^{/}^{N}SLD^{TX}∃] and ![](media_svg/image337.svg) [公式≈: _{N}_{f}_{=}_{√}_{M}_{RB}PSDCH_RP_{/}_{2}_{∃}], and

- the j-th transmission (![](media_svg/image338.svg) [公式: 1≥j≥N_{SLD}^{TX}]) for the transport block occurs in contiguous resource blocks ![](media_svg/image339.svg) [公式≈: _{m}_{2}PSDCH_{∪}_{a}_{(}_{j}_{i}_{)}]and ![](media_svg/image340.svg) [公式≈: _{m}_{2}PSDCH_{∪}_{a}_{(}_{j}_{i}_{)}_{+}_{1}]of subframe ![](media_svg/image341.svg) [公式≈: ^{l}N^{PSDCH}_{SLD}^{TX}∪b_{1}^{(}^{i}^{)}+j−1] of the PSDCH period, where

- ![](media_svg/image342.svg) [公式≈: a^{(}_{j}^{i}^{)}=((j−1)∪_{√}N_{f}/N_{SLD}^{TX}_{∃}+_{√}n_{PSDCH}/N_{t}_{∃})modN_{f}] and ![](media_svg/image343.svg) [公式≈: ^{b}1^{(}^{i}^{)}^{=}^{n}PSDCH^{mod}^{N}t] and using selected resource value ![](media_svg/image344.svg) [公式≈: ^{n}PSDCH] (described in [8]).

- ![](media_svg/image345.svg) [公式≈: _{(}_{l}_{0}PSDCH_{,}_{l}_{1}PSDCH_{,....,}_{l}_{L}PSDCH_{PSDCH}_{−}_{1}_{)}],![](media_svg/image346.svg) [公式≈: (m0^{PSDCH},m1^{PSDCH},....,mM^{PSDCH}_{RB}PSDCH_RP−1)],![](media_svg/image347.svg) [公式≈: ^{L}PSDCH]and![](media_svg/image348.svg) [公式≈: _{M}_{RB}PSDCH_RP]are described in Clause 14.3.3.

- for sidelink discovery type 2B,

- The j-th transmission (![](media_svg/image338.svg) [公式: 1≥j≥N_{SLD}^{TX}]) for the transport block occurs in contiguous resource blocks ![](media_svg/image349.svg) [公式≈: _{m}_{2}PSDCH_{∪}_{a}_{(}_{j}_{i}_{)}]and ![](media_svg/image340.svg) [公式≈: _{m}_{2}PSDCH_{∪}_{a}_{(}_{j}_{i}_{)}_{+}_{1}]of subframe ![](media_svg/image350.svg) [公式≈: ^{l}N^{PSDCH}_{SLD}^{TX}∪b_{1}^{(}^{i}^{)}+j−1] of the PSDCH period, where

- ![](media_svg/image351.svg) [公式≈: a_{1}^{(}^{i}^{)}=((N_{PSDCH}^{(}^{2}^{)}+n±)mod10+_{√}(a_{1}^{(}^{i}^{−}^{1}^{)}+N_{f}∪b_{1}^{(}^{i}^{−}^{1}^{)})N_{t}_{∃})modN_{f}]

- ![](media_svg/image352.svg) [公式≈: _{b}_{1}(i)_{=}_{(}_{N}_{PSDCH}(1)_{+}_{N}_{PSDCH}(3)_{∪}_{a}_{1}(i−1)_{+}_{N}_{f}_{∪}_{b}_{1}(i−1)_{)}_{mod}_{N}_{t}]

- ![](media_svg/image353.svg) [公式≈: a^{(}_{j}^{i}^{)}=((j−1)∪_{√}N_{f}/N_{SLD}^{TX}_{∃}+a_{1}^{(}^{i}^{)})modN_{f}] for ![](media_svg/image354.svg) [公式: 1<j≥N_{SLD}^{TX}]

- ![](media_svg/image336.svg) [公式≈: ^{N}t^{=}√^{L}PSDCH^{/}^{N}SLD^{TX}∃] and ![](media_svg/image337.svg) [公式≈: _{N}_{f}_{=}_{√}_{M}_{RB}PSDCH_RP_{/}_{2}_{∃}], and![](media_svg/image345.svg) [公式≈: _{(}_{l}_{0}PSDCH_{,}_{l}_{1}PSDCH_{,....,}_{l}_{L}PSDCH_{PSDCH}_{−}_{1}_{)}],![](media_svg/image346.svg) [公式≈: (m0^{PSDCH},m1^{PSDCH},....,mM^{PSDCH}_{RB}PSDCH_RP−1)],![](media_svg/image347.svg) [公式≈: ^{L}PSDCH]and![](media_svg/image348.svg) [公式≈: _{M}_{RB}PSDCH_RP]are described in Clause 14.3.3.

- ![](media_svg/image355.svg) [公式≈: _{a}_{1}(0)] and ![](media_svg/image356.svg) [公式≈: _{b}_{1}(0)] are given by higher layer parameters discPRB-Index and discSF-Index, respectively and that associated with the PSDCH resource configuration.

- ![](media_svg/image357.svg) [公式≈: ^{N}PSDCH^{(}^{1}^{)}],![](media_svg/image358.svg) [公式≈: ^{N}PSDCH^{(}^{2}^{)}] and![](media_svg/image359.svg) [公式≈: ^{N}PSDCH^{(}^{3}^{)}]are given by higher layer parameters a-r12, b-r12, and c-r12, repectively and that are associated with the PSDCH resource configuration.

- ![](media_svg/image360.svg) [公式: n^{±}] is the number of PSDCH periods since ![](media_svg/image361.svg) [公式≈: ^{N}PSDCH^{(}^{2}^{)}] was received.

- the transport block size is 232

For sidelink discovery, the UE transmit power ![](media_svg/image362.svg) [公式≈: ^{P}PSDCH] for PSDCH transmission is given by the following

![](media_svg/image363.svg) [公式≈: ^{P}PSDCH^{=}^{min}^{{}^{P}CMAX,PSDCH^{,}^{10}^{log}10^{(}^{M}PSDCH^{)}^{+}^{P}O_PSDCH,1^{+}^{Α}PSDCH,1^{∪}^{PL}^{}}] [dBm]

where ![](media_svg/image364.svg) [公式≈: ^{P}CMAX,PSDCH] is defined in [6], and ![](media_svg/image365.svg) [公式≈: ^{M}PSDCH]=2 and ![](media_svg/image132.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1 where ![](media_svg/image366.svg) [公式: c]

is the serving cell if the sidelink discovery transmission occurs on the uplink carrier frequency of a serving cell, or

is the cell indicated by higher layers on downlink carrier frequency indicated by discCarrierRef-r13[11] if sidelink discovery transmission does not occur on the uplink carrier frequency of a serving cell.

![](media_svg/image367.svg) [公式≈: ^{P}O_PSDCH,1] and ![](media_svg/image368.svg) [公式≈: ^{Α}PSDCH,1] are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSDCH resource configuration.

A UE shall drop any PSDCH transmissions that are associated with sidelink discovery type 1 in a sidelink subframe if the UE has a PSDCH transmission associated with sidelink discovery type 2B in that subframe.

## 14.3.2 UE procedure for receiving the PSDCH

For sidelink discovery type 1, for each PSDCH resource configuration associated with reception of PSDCH, a UE configured by higher layers to detect a transport block on PSDCH can decode the PSDCH according to the PSDCH resource configuration.

For sidelink discovery type 2B, for each PSDCH resource configuration associated with reception of PSDCH, a UE configured by higher layers to detect a transport block on PSDCH can decode the PSDCH according to the PSDCH resource configuration.

## 14.3.3 UE procedure for determining resource block pool and subframe pool for sidelink discovery

A PSDCH resource configuration for transmission/reception is associated with a set of periodically occurring time-domain periods (known as PSDCH periods). The i-th PSDCH period begins at subframe with subframe index![](media_svg/image369.svg) [公式≈: j_{begin}=O_{3}+i∪P] and ends in subframe with subframe index ![](media_svg/image370.svg) [公式≈: j_{end}=O_{3}+(i+1)∪P−1], where

- ![](media_svg/image371.svg) [公式≈: 0≥j_{begin}<10240],

- the subframe index is relative to subframe#0 of a radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

- ![](media_svg/image372.svg) [公式≈: ^{O}3] is the offsetIndicator-r12 indicated by the PSDCH resource configuration

- ![](media_svg/image318.svg) [公式: P]is the discPeriod-r12 indicated by the PSDCH resource configuration.

For a PSDCH period, the UE determines a discovery pool consisting of a subframe pool and a resource block pool for PSDCH as follows.

- For TDD, if the parameter tdd-Config-r12 is indicated by the PSDCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

- A bitmap ![](media_svg/image373.svg) [公式≈: b_{0},b_{1},b_{2},...,b_{N}_{±}_{−}_{1}] is obtained using![](media_svg/image374.svg) [公式≈: ^{b}j^{=}^{a}jmodN_{B}], for ![](media_svg/image375.svg) [公式: 0≥j<N±], where ![](media_svg/image376.svg) [公式≈: a_{0},a_{1},a_{2},...,a_{N}_{B}_{−}_{1}]and ![](media_svg/image377.svg) [公式≈: ^{N}B]are the bitmap and the length of the bitmap indicated by subframeBitmap-r12, respectively, and ![](media_svg/image378.svg) [公式: N±=N_{B}∪N_{R}], where ![](media_svg/image379.svg) [公式≈: ^{N}R]is the numRepetition-r12 indicated by the PSDCH resource configuration.

- The first ![](media_svg/image321.svg) [公式: N^{±}]uplink subframes are denoted by ![](media_svg/image320.svg) [公式≈: (l_{0},l_{1},...,l_{N}_{±}_{−}_{1})] arranged in increasing order of subframe index.

- A subframe ![](media_svg/image322.svg) [公式≈: ^{l}j] (![](media_svg/image323.svg) [公式: 0≥j<N±]) belongs to the subframe pool if ![](media_svg/image380.svg) [公式: b_{j}=1]. The subframes in the subframe pool are denoted by![](media_svg/image381.svg) [公式≈: _{(}_{l}_{0}PSDCH_{,}_{l}_{1}PSDCH_{,....,}_{l}_{L}PSDCH_{PSDCH}_{−}_{1}_{)}] arranged in increasing order of subframe index and ![](media_svg/image347.svg) [公式≈: ^{L}PSDCH] denotes the number of subframes in the subframe pool.

- A PRB with index ![](media_svg/image240.svg) [公式: q] (![](media_svg/image241.svg) [公式: 0≥q<N_{RB}^{SL}]) belongs to the resource block pool if![](media_svg/image242.svg) [公式: S1≥q<S1+M] or if ![](media_svg/image243.svg) [公式: S2−M<q≥S2], where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSDCH resource configuration respectively.

- The resource blocks in the resource block pool are denoted by![](media_svg/image346.svg) [公式≈: (m0^{PSDCH},m1^{PSDCH},....,mM^{PSDCH}_{RB}PSDCH_RP−1)] arranged in increasing order of resource block indices and ![](media_svg/image348.svg) [公式≈: _{M}_{RB}PSDCH_RP] is the number of resource blocks in the resource block pool.

## 14.4 Physical Sidelink Synchronization related procedures

The synchronization resource configuration(s) for the UE are given by the higher layer parameter SL-SyncConfig-r12 or v2x-SyncConfig.

A UE shall transmit sidelink synchronisation signals according to Clause 5.10.7 in [11].

A UE may assume that sidelink synchronization signals are signals transmitted by an eNB as described in Clause 6.11 of [3] or are signals transmitted by a UE as described in [11].

A UE is not expected to blindly detect the cyclic prefix length of sidelink synchronization signals transmitted by another UE.

For a sidelink synchronization resource configuration associated with PSDCH reception, if cell c is indicated by the parameter physCellId-r12 and if the parameter discSyncWindow-r12 is configured with value w1 for cell c, the UE may assume that sidelink synchronization signals are transmitted in cell c and that they are received within a reference synchronization window of size +/-w1 ms with respect to the sidelink synchronization resource of cell c indicated by higher layers. The sidelink synchronization identity associated with the sidelink synchronization resource is indicated by higher layers.

For PSDCH reception, if cell c is indicated by the parameter physCellId-r12 and if the parameter discSyncWindow-r12 is configured with value w2 for cell c, the UE may assume that PSDCH of UE in cell c is received within a reference synchronization window of size +/-w2 ms with respect to the discovery resource of cell c indicated by higher layers.

The UE transmit power of primary sidelink synchronization signal ![](media_svg/image2.svg) [公式≈: ^{P}PSSS] and the UE transmit power of secondary synchronization signal ![](media_svg/image382.svg) [公式≈: ^{P}SSSS] are given by

- If the UE is configured with sidelink transmission mode 1, and if the UE transmits sidelink synchronization signals in PSCCH period i, and if the TPC command field in the configured sidelink grant (described in [8]) for the PSCCH period i is set to 0

- ![](media_svg/image383.svg) [公式≈: ^{P}PSSS^{=}^{P}CMAX,PSBCH]

- ![](media_svg/image384.svg) [公式≈: ^{P}SSSS^{=}^{P}CMAX,SSSS]

- otherwise

- ![](media_svg/image385.svg) [公式≈: ^{P}PSSS^{=}^{min}^{{}^{P}CMAX,PSBCH^{,}^{10}^{log}10^{(}^{M}PSSS^{)}^{+}^{P}O_PSSS^{+}^{Α}PSSS^{∪}^{PL}^{}}] [dBm] ,

- ![](media_svg/image386.svg) [公式≈: ^{P}SSSS^{=}^{min}^{{}^{P}CMAX,SSSS^{,}^{10}^{log}10^{(}^{M}PSSS^{)}^{+}^{P}O_PSSS^{+}^{Α}PSSS^{∪}^{PL}^{}}] [dBm] ,

where ![](media_svg/image387.svg) [公式≈: ^{P}CMAX,PSBCH] and ![](media_svg/image388.svg) [公式≈: ^{P}CMAX,SSSS] are defined in [6]. ![](media_svg/image389.svg) [公式≈: ^{M}PSSS^{=}^{6}]and ![](media_svg/image390.svg) [公式: PL=PL_{c}] where![](media_svg/image133.svg) [公式: PL_{c}] is defined in Clause 5.1.1.1. ![](media_svg/image391.svg) [公式≈: ^{P}O_PSSS] and ![](media_svg/image392.svg) [公式≈: ^{Α}PSSS] are provided by higher layer parameters associated with the corresponding sidelink synchronization signal resource configuration.

If sidelink synchronization signals are transmitted for PSDCH, and if the PSDCH transmission does not occur on any serving cell configured for the UE, ![](media_svg/image366.svg) [公式: c] is the cell indicated by higher layers on downlink carrier frequency indicated by discCarrierRef [11]. Otherwise, ![](media_svg/image366.svg) [公式: c] is the serving cell on which the sidelink synchronization signals are transmitted. If sidelink synchronization signals are transmitted for PSDCH, then PSDCH and sidelink synchronization signal transmission occur on the same carrier frequency.

# 15 Void

# 16 UE Procedures related to narrowband IoT

Throughout this clause,

- for a NB-IoT UE in a IoT NTN TDD serving cell,

- the UE shall not assume any downlink physical signal or physical channel is present in any subframe other than within the D consecutive downlink subframes according to the frame structure type 1 for IoT NTN TDD and the value of D defined in [3],

- the UE shall not transmit any uplink physical signal or physical channel in any subframe other than within the U consecutive uplink subframes according to the frame structure type 1 for IoT NTN TDD and the value of U defined in [3].

- the term “DL subframe” includes the 𝐷 consecutive downlink subframes, the 𝑈 consecutive uplink subframes and guard period subframes as defined in [3].

- for a NB-IoT UE, the value of $ K_{offset}$ is given by,

- if the UE is configured with the higher layer parameter k-Offset,

- $ K_{offset}=K_{cell\_offset}-K_{UE\_offset}$ where

$ K_{cell\_offset}$ is the parameter k-Offset provided by higher layers, and

$ K_{UE\_offset}$ is the parameter Differential Koffset provided by higher layers, otherwise $ K_{UE\_offset}=0 $

- otherwise,

- $ K_{offset}=0 $.

If the UE is configured with higher layer parameter k-Offset, for an NPUSCH (re)transmission associated with the TC-RNTI, $ K_{offset}=$ k-Offset.

## 16.1 Synchronization procedures

### 16.1.1 Cell search

Cell search is the procedure by which a UE acquires time and frequency synchronization with a cell and detects the narrowband physical layer Cell ID.

If the higher layer parameter operationModeInfo indicates 'inband-SamePCI' or samePCI-Indicator indicates 'samePCI'' for a cell, the UE may assume that the physical layer cell ID is same as the narrowband physical layer cell ID for the cell.

The following signals are transmitted in the downlink to facilitate cell search for Narrowband IoT: the narrowband primary and narrowband secondary synchronization signals.

A UE may assume the antenna ports 2000 – 2001 and the antenna port for the narrowband primary/secondary synchronization signals of a serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift and average delay.

### 16.1.2 Timing synchronization

Upon reception of a timing advance command, the UE shall adjust uplink transmission timing for NPUSCH, and SR if configured with higher layer parameter sr-WithoutHARQ-ACK-Config, based on the received timing advance command.

The timing advance command indicates the change of the uplink timing relative to the current uplink timing as multiples of 16![](media_svg/image393.svg) [公式≈: ^{T}s]. The start timing of the random access preamble is specified in [3].

In case of random access response, an 11-bit timing advance command [8], TA, indicates NTA values by index values of TA = 0, 1, 2, ..., 1536, where an amount of the time alignment is given by NTA = TA 16. NTA is defined in [3].

In other cases, a 6-bit timing advance command [8] or the Timing advance adjustment field in DCI format N0 if present [4], TA, indicates adjustment of the current NTA value, NTA,old, to the new NTA value, NTA,new, by index values of TA = 0, 1, 2,..., 63, where NTA,new = NTA,old + (TA 31)16. Here, adjustment of NTA value by a positive or a negative amount indicates advancing or delaying the uplink transmission timing by a given amount respectively.

For a timing advance command reception ending in DL subframe n, the corresponding adjustment of the uplink transmission timing shall apply for the uplink NPUSCH transmissions starting from subframe n+12 +Koffset+1. When the UE's uplink NPUSCH transmissions in NB-IoT uplink slot n and NB-IoT uplink slot n+1 are overlapped due to the timing adjustment, the UE shall complete transmission of NB-IoT uplink slot n and not transmit the overlapped part of NB-IoT uplink slot n+1.

If the received downlink timing changes and is not compensated or is only partly compensated by the uplink timing adjustment without timing advance command as specified in [10], the UE changes NTA accordingly.

For a UE in a NTN serving cell, using serving satellite higher-layer ephemeris parameters, if configured, the UE determines $ N_{TA,adj}^{UE}$ (defined in [3]) using the serving satellite position and its own position to pre-compensate the two-way transmission delay on the service link. To pre-compensate the two-way transmission delay between the uplink time synchronization reference point and the serving satellite, the UE determines $ N_{TA,adj}^{common}$(defined in [3]) based on one-way propagation delay $ Delay_{common}\left ( t\right ) $ which can be obtained as:

$$ Delay_{common}\left ( t\right ) =\frac {1}{2}\left [ N_{TA}^{common}+N_{TA}^{commonDrift}\times  \left ( t-t_{epoch}\right ) +N_{TA}^{commonDriftVariation}\times  \left ( t-t_{epoch}\right ) ^{2}\right ] $$

where $ N_{TA}^{common}$, $ N_{TA}^{commonDrift}$, and $ N_{TA}^{commonDriftVariation}$ are given by the higher layer parameters nta-Common, nta-CommonDrift, and nta-CommonDriftVariation respectively, and $ t_{epoch}$ is the epoch time given by the higher layer parameter epochTime. $ Delay_{common}(t)$ provides a distance at time $ t $ between the serving satellite and the uplink time synchronization reference point divided by the speed of light. The uplink time synchronization reference point is the point where DL and UL are frame aligned with an offset given by $ N_{TA,offset}$.

For a NB-IoT UE communicating over NTN FDD, time and frequency pre-compensation is adjusted per uplink segment with a transmission duration of $ N_{segment}^{precompensation}$ time units, where the quantity $ N_{segment}^{precompensation}$ is provided by higher layers, as specified in 3GPP TS 36.331 [11].

In case of CB-Msg3 EDT procedure for a UE communicating over NTN, the start timing of a NPUSCH transmission using CB-Msg3 resource shall be aligned with the start of the corresponding uplink subframe at the UE by assuming $ N_{TA}=0 $.

## 16.2 Power control

### 16.2.1 Uplink power control

Uplink power control controls the transmit power of the different uplink physical channels.

#### 16.2.1.1 Narrowband physical uplink shared channel

##### 16.2.1.1.1 UE behaviour

The setting of the UE Transmit power for a Narrowband Physical Uplink Shared Channel (NPUSCH) transmission is defined as follows. For FDD or IoT NTN TDD, if the UE is capable of enhanced random access power control [12], and it is configured by higher layers, and for TN TDD, enhanced random access power control shall be applied for a UE which started the random access procedure in the first or second configured NPRACH repetition level.

The UE transmit power ![](media_svg/image394.svg) [公式≈: ^{P}NPUSCH,c^{(}^{i}^{)}] for NPUSCH transmission in NB-IoT UL slot i for the serving cell ![](media_svg/image395.svg) [公式: c]is given by:

For NPUSCH (re)transmissions corresponding to the random access response grant if enhanced random access power control is not applied, and for all other NPUSCH transmissions except for NPUSCH (re)transmission corresponding to preconfigured uplink resource, when the number of repetitions of the allocated NPUSCH RUs is greater than 2:

![](media_svg/image396.svg) [公式≈: ^{PiPi}NPUSCH,cCMAX,^{()()}^{=}c][dBm]

otherwise

$ P_{PUSCH,c}(i)=\operatorname {min}\left (\left \{ \&P_{CMAX,c}(i),\\\&10\operatorname {log_{10}}\left ((\right )M_{NPUSCH,c}(i))+P_{O\_NPUSCH,c}(j)+\alpha  _{c}(j)\cdot  PL_{c}+\Delta  _{TF,c}(i))\right \} \right )$ [dBm]

where,

- is the configured UE transmit power defined in [6] in NB-IoT UL slot i for serving cell ![](media_svg/image395.svg) [公式: c].

- $ M_{NPUSCH,c}(i)$ is the NPUSCH transmission resource bandwidth normalized by 15 kHz, where {1/4} is used for 3.75 kHz subcarrier spacing and {1, 3, 6, 12} are used for 15kHz subcarrier spacing

- $ P_{O\_NPUSCH,c}\left ( j\right ) $ is a parameter composed of the sum of a component ![](media_svg/image398.svg) [公式≈: ^{Pj}O_NOMINAL_NPUSCH,c^{()}] provided from higher layers and a component ![](media_svg/image399.svg) [公式≈: ^{Pj}O_UE_NPUSCH,c^{() }] provided by higher layers for j=1, 3 and for serving cell![](media_svg/image395.svg) [公式: c] where ![](media_svg/image400.svg) [公式: j⎰{1,2,3}]. For NPUSCH (re)transmissions corresponding to a dynamic scheduled grant or a semi-persistent grant then j=1, for NPUSCH (re)transmissions corresponding to the random access response grant then j=2 and for NPUSCH transmission using preconfigured uplink resource then j=3. $ P_{O\_UE\_NPUSCH,c}\left ( 2\right ) =0 $. If enhanced random access power control is not applied, $ P_{O\_NOMINAL\_NPUSCH,c}(2)=P_{O\_PRE}+∆_{PREAMBLE\_Msg3}$, where the parameter preambleInitialReceivedTargetPower [8] () and $∆_{PREAMBLE\_Msg3}$ are signalled from higher layers for serving cell ![](media_svg/image395.svg) [公式: c]. If enhanced random access power control is applied,

$$ P_{O\_NOMINAL\_NPUSCH,c}\left ( 2\right ) =MSG3\_RECEIVED\_TARGET\_POWER +\Delta  _{PREAMBLE\_Msg3}$$

- For CB-Msg3 transmissions, then j=4, and $ P_{O\_PUSCH,c}(4)$ is the parameter 
CB-MSG3_RECEIVED_TARGET_POWER provided by higher layers for serving cell ![](media_svg/image402.svg) [公式: c].

- For j=1, for NPUSCH format 2, ![](media_svg/image403.svg) [公式: Α_{c}(j)]=1; for NPUSCH format 1, ![](media_svg/image403.svg) [公式: Α_{c}(j)]is provided by higher layers for serving cell ![](media_svg/image395.svg) [公式: c]. For j=2,  For j=3, ![](media_svg/image403.svg) [公式: Α_{c}(j)] is the parameter alpha in PUR-Config-NB provided by higher layers for serving cell ![](media_svg/image395.svg) [公式: c]. For j=4, ![](media_svg/image405.svg) [公式: Α_{c}()j]is the parameter alpha in CB-Msg3-ConfigSIB-NB provided by higher layers for serving cell ![](media_svg/image402.svg) [公式: c].

- ![](media_svg/image406.svg) [公式: PL_{c}] is the downlink path loss estimate calculated in the UE for serving cell ![](media_svg/image395.svg) [公式: c] in dB and ![](media_svg/image406.svg) [公式: PL_{c}] = nrs-Power + nrs-PowerOffsetNonAnchor – NRSRP, where nrs-Power is provided by higher layers and Clause 16.2.2, and nrs-PowerOffsetNonAnchor is set to zero if it is not provided by higher layers and NRSRP is defined in [5] for serving cell ![](media_svg/image407.svg) [公式: c].

- If a NB-IoT UE is configured with npusch-16QAM-Config or pur-UL-16QAM-Config, then for NPUSCH (re)transmissions with QPSK and 16QAM,

- $\Delta  _{TF,c}\left ( i\right ) =10log_{10}\left ( \left ( 2^{BPRE\cdot  K_{s}}-1\right ) \right ) $ for ![](media_svg/image408.svg) [公式: K_{S}=1.25]and $∆_{TF,c}(i)=0 $ for ![](media_svg/image409.svg) [公式: K_{S}=0]where ![](media_svg/image410.svg) [公式≈: ^{K}S] is given by the parameter deltaMCS-Enabled provided by higher layers for serving cell ![](media_svg/image407.svg) [公式: c], and

- $ BPRE=K/N_{RE}$ where $ K $ is the code block size and $ N_{RE}$ is the number of resource elements determined as $ N_{RE}=(N_{symb}^{UL}-1)N_{slots}^{UL}N_{sc}^{RU}N_{RU}$ where $ N_{symb}^{UL}$, $ N_{slots}^{UL}$, $ N_{sc}^{RU}$ are defined in [3], and $ N_{RU}$ is defined in section 16.5.1.1

- otherwise $∆_{TF,c}(i)=0 $.

##### 16.2.1.1.2 Power headroom

If the UE transmits NPUSCH in NB-IoT UL slot ![](media_svg/image411.svg) [公式: i] for serving cell ![](media_svg/image412.svg) [公式: c], power headroom is computed using

![](media_svg/image413.svg) [公式: PHiPiPPLcCMAX,O_NPUSCH,c()()(1)(1)=−+∪ccc{Α}] [dB]

where, , ![](media_svg/image415.svg) [公式≈: ^{P}O_NPUSCH,c^{(1)}], ![](media_svg/image416.svg) [公式: Α_{c}(1)], and![](media_svg/image406.svg) [公式: PL_{c}], are defined in Clause 16.2.1.1.1.

The power headroom shall be rounded down to the closest value in the set [PH1, PH2, PH3, PH4] dB if enhanced PHR is not configured and [PH1, PH2, …, PH15, PH16] dB if enhanced PHR is configured as defined in [10]. The power headroom is delivered by the physical layer to higher layers.

#### 16.2.1.2 SR

##### 16.2.1.2.1 UE behaviour

If the UE is configured with higher layer parameter sr-WithoutHARQ-ACK-Config, the setting of the UE transmit power for SR transmission without HARQ-ACK is defined as follows.

The UE transmit power ![](media_svg/image417.svg) [公式≈: ^{Pi}SR,c^{()}] for SR transmission in NB-IoT UL slot i for the serving cell is given by:

![](media_svg/image419.svg) [公式≈: ^{Pi}^{SR,c}^{()min}^{=}^{√∅}^{⌡⌡}^{⌠∇}⌡⌡∞∈^{10log(())}^{Pi}^{CMAX,}10SR,cO_SR,cc^{c}^{(),}^{MiPPL}^{++∪}^{Α}c] [dBm]

where,

- ![](media_svg/image420.svg) [公式≈: ^{Pi}CMAX,c^{()}]is the configured UE transmit power defined in [6] in NB-IoT UL slot i for serving cell ![](media_svg/image395.svg) [公式: c].

- ![](media_svg/image421.svg) [公式≈: ^{Mi}SR,c^{()}]is {1/3} for NPRACH format 2 and {1}for NPRACH format 0/1.

- ![](media_svg/image422.svg) [公式≈: ^{P}O_SR,c]is signaled from higher layers for serving cell ![](media_svg/image395.svg) [公式: c].

- ![](media_svg/image423.svg) [公式≈: ^{Α}c] is signaled from higher layers for serving cell ![](media_svg/image395.svg) [公式: c].

-  is defined in Clause 16.2.1.1.1.

### 16.2.2 Downlink power allocation

The eNodeB determines the downlink transmit energy per resource element.

For an NB-IoT cell, the UE may assume NRS EPRE is constant across the downlink NB-IoT system bandwidth and constant across all subframes that contain NRS, until different NRS power information is received.

The downlink NRS EPRE can be derived from the downlink narrowband reference-signal transmit power given by nrs-Power + nrs-PowerOffsetNonAnchor, where the parameter nrs-Power is provided by higher layers and nrs-PowerOffsetNonAnchor is zero if it is not provided by higher layers. The downlink narrowband reference-signal transmit power is defined as the linear average over the power contributions (in [W]) of all resource elements that carry narrowband reference signals within the operating NB-IoT system bandwidth.

A UE may assume that the ratio of NWUS EPRE to NRS EPRE is 0 dB.

A UE may assume the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports if higher layer parameter nrs-PowerRatio is not configured.

If a UE is configured with the higher layer parameter nrs-PowerRatio in npdsch-16QAM-Config or pur-DL-16QAM-Config,

- the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs in symbols with NRS is given by $\frac {1}{5}\times  (6\rho  -1)$ for a cell with one NRS antenna port and $\frac {1}{4}\times  (6\rho  -1)$ for a cell with two NRS antenna ports, where $\rho  $ is given by the parameter nrs-PowerRatio.

- if higher layer parameter operationModeInfo indicates '10' or '11',

- the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatio in symbols without NRS

- otherwise,

- the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatio in symbols without NRS and CRS, and

- the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatioWithCRS in symbols with CRS.

A UE may assume the ratio of NPBCH EPRE to NRS EPRE among NPBCH REs (not applicable to NPBCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports.

A UE may assume the ratio of NPDCCH EPRE to NRS EPRE among NPDCCH REs (not applicable to NPDCCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports.

If higher layer parameter operationModeInfo indicates '00' or samePCI-Indicator indicates 'samePCI' for a cell, the ratio of NRS EPRE to CRS EPRE is given by the parameter nrs-CRS-PowerOffset if the parameter nrs-CRS-PowerOffset is provided by higher layers, and the ratio of NRS EPRE to CRS EPRE may be assumed to be 0 dB if the parameter nrs-CRS-PowerOffset is not provided by higher layers. If nrs-CRS-PowerOffset is provided by higher layers and is a non-integer value, the value of nrs-Power is 0.23 dBm higher than indicated.

## 16.3 Random access procedure

Prior to initiation of the non-synchronized physical random access procedure, Layer 1 shall receive the following information from the higher layers:

- Narrowband Random access channel parameters (NPRACH configuration)

### 16.3.1 Physical non-synchronized random access procedure

From the physical layer perspective, the L1 random access procedure encompasses the transmission of narrowband random access preamble and narrowband random access response. The remaining messages are scheduled for transmission by the higher layer on the shared data channel and are not considered part of the L1 random access procedure. A random access channel occupies one subcarrier per set of consecutive symbols reserved for narrowband random access preamble transmissions.

The following steps are required for the L1 random access procedure:

- Layer 1 procedure is triggered upon request of a narrowband preamble transmission by higher layers.

- A target narrowband preamble received power (NARROWBAND_PREAMBLE_RECEIVED_TARGET_POWER), a corresponding RA-RNTI and a NPRACH resource are indicated by higher layers as part of the request.

- If enhanced random access power control is not applied, for the lowest configured repetition level; and if enhanced random access power control is applied then for all configured repetition levels, a narrowband preamble transmission power PNPRACH is determined as 
PNPRACH = min{![](media_svg/image425.svg) [公式≈: ^{Pi}CMAX,c^{()}], NARROWBAND_PREAMBLE_RECEIVED_TARGET_POWER + ![](media_svg/image426.svg) [公式: PL_{c}] }_[dBm], where ![](media_svg/image427.svg) [公式≈: ^{Pi}CMAX,c^{()}] is the configured UE transmit power for narrowband IoT transmission defined in [6] for subframe i of serving cell ![](media_svg/image412.svg) [公式: c] and ![](media_svg/image428.svg) [公式: PL_{c}] is the downlink path loss estimate calculated in the UE for serving cell ![](media_svg/image412.svg) [公式: c]. If enhanced random access power control is not applied, for a repetition level other than the lowest configured repetition level, PNPRACH is set to ![](media_svg/image429.svg) [公式≈: ^{Pi}CMAX,c^{()}].

- The narrowband preamble is transmitted with transmission power PNPRACH commencing on the indicated NPRACH resource. The narrowband preamble is transmitted for the number of NPRACH repetitions for the associated NPRACH repetition level as indicated by higher layers.

Detection of a NPDCCH with DCI scrambled by RA-RNTI is attempted during a window controlled by higher layers (see [8], Clause 5.1.4). If detected, the corresponding DL-SCH transport block is passed to higher layers. The higher layers parse the transport block and indicate the Nr-bit uplink grant to the physical layer, which is processed according to Clause 16.3.3

### 16.3.2 Timing

For the L1 random access procedure, UE's uplink transmission timing after a random access preamble transmission is as follows.

a) If a NPDCCH with associated RA-RNTI is detected and the corresponding DL-SCH transport block ending in subframe n contains a response to the transmitted preamble sequence, the UE shall, according to the information in the response, transmit an UL-SCH transport block according to Clause 16.3.3.

b) If a random access response is received and the corresponding DL-SCH transport block ending in subframe n does not contain a response to the transmitted preamble sequence, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

c) If no NPDCCH scheduling random access response is received in subframe n, where subframe n is the last subframe of the random access response window, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

d) If an NPDCCH scheduling random access response with associated RA-RNTI is detected and the corresponding DL-SCH transport block reception ending in subframe n cannot be successfully decoded, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

In case a random access procedure is initiated by a "PDCCH order" ending in subframe n, the UE shall, if requested by higher layers, start transmission of random access preamble at the end of the first subframe $ n+k_{2}+K_{cell\_offset}$, ![](media_svg/image430.svg) [公式: k_{2}÷8], where a NPRACH resource is available.

The "PDCCH order" in DCI format N1 indicates to the UE,

- allocated subcarrier for NPRACH, ![](media_svg/image431.svg) [公式≈: ^{n}sc^{=}^{I}sc]where ![](media_svg/image432.svg) [公式≈: ^{I}sc] is the subcarrier indication field in the corresponding DCI, ![](media_svg/image433.svg) [公式: I_{sc}=48,49,...,63]is reserved for preamble format 0/1, ![](media_svg/image434.svg) [公式: I_{sc}=144,145,...,255]is reserved for preamble format 2 if nprach-ParametersListFmt2 is configured and the UE indicates the nprach-Format2 capability and Preamble format indicator is set to 1.

- a repetition number (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) for NPRACH determined by the repetition number field (![](media_svg/image436.svg) [公式≈: ^{I}Rep]) in the corresponding DCI according to Table 16.3.2-1 where R1, R2 (if any) and R3 (if any) are given by the higher layer parameter numRepetitionsPerPreambleAttempt for each NPRACH resource, respectively. R1 < R2 <R3.

Table 16.3.2-1: Number of repetitions (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) for NPRACH following a "PDCCH order"

| ![](media_svg/image437.svg) [公式≈: ^{I}Rep] | ![](media_svg/image435.svg) [公式≈: ^{N}Rep] |
| --- | --- |
| 0 | R1 |
| 1 | R2 |
| 2 | R3 |
| 3 | Reserved |

The UE shall transmit random access preamble on the NB-IoT carrier indicated by "Carrier indication of NPRACH" field, if the field is present in the "PDCCH order". If the value of "Carrier indication of NPRACH" is non-zero, it indicates a NPRACH carrier derived from SystemInformationBlockType22-NB [11] for which the index in the list is equal to the carrier indication. If the value of "Carrier indication of NPRACH" is zero, the uplink carrier used for NPRACH is derived from SystemInformationBlockType2-NB [11].

If nprach-ParametersListFmt2 is configured and the UE indicates the nprach-Format2 capability, the UE shall transmit the preamble format indicated by "Preamble format indicator" field, otherwise the UE shall transmit preamble format 0/1.

### 16.3.3 Narrowband random access response grant

The higher layers indicate the Nr-bit UL Grant to the physical layer, as defined in 3GPP TS36.321 [8]. 
This is referred to as the Narrowband Random Access Response Grant in the physical layer.

Nr-bit =15, and the content of these 15 bits starting with the MSB and ending with the LSB are as follows:

- Uplink subcarrier spacing ![](media_svg/image438.svg) [公式: δf] is '0'=3.75 kHz or '1'=15 kHz – 1 bit

- Subcarrier indication field ![](media_svg/image432.svg) [公式≈: ^{I}sc] as determined in Clause 16.5.1.1 – 6 bits

- Scheduling delay field (![](media_svg/image439.svg) [公式≈: ^{I}Delay]) as determined in Clause 16.5.1 with k0 = 12 for IDelay = 0 , where NB-IoT DL subframe n is the last subframe in which the NPDSCH associated with the Narrowband Random Access Response Grant is transmitted – 2 bits

- Msg3 repetition number ![](media_svg/image435.svg) [公式≈: ^{N}Rep] as determined in Clause 16.5.1.1 – 3 bits

- MCS index indicating TBS, modulation, and number of RUs for Msg3 – 3 bits

The redundancy version for the first transmission of Msg3 is 0.

If the UE is not using higher layer parameter edt-Parameters, or the UE is using higher layer parameter edt-parameters and ![](media_svg/image440.svg) [公式: 02≥≥I_{MCS}],

- the TBS, modulation, and number of RUs for Msg3 are determined according to Table 16.3.3-1

otherwise,

- if the UE is configured with higher layer parameter edt-SmallTBS-Enabled set to 'false',

- the TBS is given by higher layer parameter edt-TBS

- otherwise,

the UE selects a TBS from the allowed TBS values according to Table 16.3.3-2

the repetition number for Msg3 is the smallest integer multiple of L value that is equal to or larger than![](media_svg/image441.svg) [公式≈: ^{TBSTBSN}Msg3Msg3,maxRep^{∪}] where ![](media_svg/image442.svg) [公式≈: ^{TBS}Msg3] is the selected TBS for Msg3, and ![](media_svg/image443.svg) [公式≈: ^{TBS}Msg3,max] is given by higher layer parameter edt-TBS

- if ![](media_svg/image444.svg) [公式: δ=f15 kHz] and ![](media_svg/image445.svg) [公式: I_{sc}>11] and ![](media_svg/image446.svg) [公式≈: ^{N}Rep^{÷}^{8}], then ![](media_svg/image447.svg) [公式: L=4]is used in clause 16.5.1.2, otherwise ![](media_svg/image448.svg) [公式: L=1]is used

- the number of RUs for Msg3 are determined according to Table 16.3.3-3

π/4 QPSK modulation is used for ![](media_svg/image449.svg) [公式: δf=3.75kHz] and for ![](media_svg/image444.svg) [公式: δ=f15 kHz] with ![](media_svg/image450.svg) [公式: I_{sc}=0,1,...,11]; QPSK modulation is used for![](media_svg/image444.svg) [公式: δ=f15 kHz] with ![](media_svg/image445.svg) [公式: I_{sc}>11]

Table 16.3.3-1: MCS index for Msg3 NPUSCH

| MCS Index ![](media_svg/image5.svg) [公式≈: ^{I}MCS] | Modulation![](media_svg/image449.svg) [公式: δf=3.75kHz] or ![](media_svg/image444.svg) [公式: δ=f15 kHz]and![](media_svg/image450.svg) [公式: I_{sc}=0,1,...,11] | Modulation![](media_svg/image444.svg) [公式: δ=f15 kHz]and![](media_svg/image451.svg) [公式: I_{sc}>11] | Number of RUs![](media_svg/image452.svg) [公式≈: ^{N}RU] | TBS |
| --- | --- | --- | --- | --- |
| '000' | pi/2 BPSK | QPSK | 4 | 88 bits |
| '001' | pi/4 QPSK | QPSK | 3 | 88 bits |
| '010' | pi/4 QPSK | QPSK | 1 | 88 bits |
| '011' | reserved | reserved | reserved | reserved |
| '100' | reserved | reserved | reserved | reserved |
| '101' | reserved | reserved | reserved | reserved |
| '110' | reserved | reserved | reserved | reserved |
| '111' | reserved | reserved | reserved | reserved |

Table 16.3.3-2: EDT TBS for Msg3 NPUSCH with edt-SmallTBS-Enabled set to 'true'

| edt-TBS | edt-SmallTBS-Subset | Allowable TBS values |
| --- | --- | --- |
| 408 | not configured | 328, 408 |
| 504 | not configured | 328, 408, 504 |
| 504 | enabled | 408, 504 |
| 584 | not configured | 328, 408, 504, 584 |
| 584 | enabled | 408, 584 |
| 680 | not configured | 328, 456, 584, 680 |
| 680 | enabled | 456, 680 |
| 808 | not configured | 328, 504, 680, 808 |
| 808 | enabled | 504, 808 |
| 936 | not configured | 328, 504, 712, 936 |
| 936 | enabled | 504, 936 |
| 1000 | not configured | 328, 536, 776, 1000 |
| 1000 | enabled | 536, 1000 |

Table 16.3.3-3: MCS index for Msg3 NPUSCH and EDT

| MCS Index ![](media_svg/image5.svg) [公式≈: ^{I}MCS] | Number of RUs![](media_svg/image452.svg) [公式≈: ^{N}RU] |  |  |
| --- | --- | --- | --- |
|  | edt-TBS = 328, 408, 504, or 584 | edt-TBS = 680 | edt-TBS = 808, 936, or 1000 |
| '011' | 3 | 3 | 4 |
| '100' | 4 | 4 | 5 |
| '101' | 5 | 5 | 6 |
| '110' | 6 | 8 | 8 |
| '111' | 8 | 10 | 10 |

## 16.4 Narrowband physical downlink shared channel related procedures

A NB-IoT UE shall determine whether a downlink subframe or a TDD special subframe configured for NB-IoT DL transmission is a NB-IoT DL subframe as follows

- If the UE determines that the subframe contains NPSS/NSSS/NPBCH/ SystemInformationBlockType1-NB transmission, then the subframe is not assumed as a NB-IoT subframe.

- Else if the UE is in a IoT NTN TDD serving cell and the UE determines the subframe is not one of the D consecutive downlink subframes according to the frame structure type 1 for IoT NTN TDD and the value of D defined in [3], then the subframe is not assumed as a NB-IoT DL subframe.

- Else if higher layer parameter resourceReservationConfigDL is configured

- for NPDSCH transmission associated with C-RNTI using UE-specific NPDCCH search space

- if the Resource reservation field in the DCI is set to 0, then the subframe is assumed as a NB-IoT DL subframe

- else if the Resource reservation field in the DCI is set to 1, then the subframe is assumed as a NB-IoT DL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols are reserved in the subframe).

- for NPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space

- the subframe is assumed as a NB-IoT DL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols are reserved in the subframe).

- In all other cases, a NB-IoT UE shall assume a subframe as a NB-IoT DL subframe if

- for a NB-IoT carrier that a UE receives higher layer parameter operationModeInfo, the subframe is configured as NB-IoT DL subframe or the subframe is a TDD special subframe configured for NB-IoT DL transmission after the UE has obtained SystemInformationBlockType1-NB.

- the subframe is configured as NB-IoT DL subframe by the higher layer parameter downlinkBitmapNonAnchor.

- except when the UE is configured with higher layer parameter additionalTxSIB1-Config set to TRUE, subframe #3 not containing additional SystemInformationBlockType1-NB transmission is assumed as a NB-IoT DL subframe if the UE monitors a NPDCCH UE-specific search space or decodes NPDSCH transmission scheduled by NPDCCH in the UE-specific search space.

For a NB-IoT UE that supports twoHARQ-Processes-r14 or the UE is configured with higher layer parameter npdsch-MultiTB-Config, there shall be a maximum of 2 downlink HARQ processes.

### 16.4.1 UE procedure for receiving the narrowband physical downlink shared channel

A UE shall upon detection on a given serving cell of a NPDCCH with DCI format N1, N2 ending in subframe n intended for the UE, decode, starting in

- n+5 DL subframe for FDD or IoT NTN TDD,

- n+5 subframe for TN TDD,

the corresponding NPDSCH transmission in N consecutive NB-IoT DL subframe(s) ni with i = 0, 1, …, N-1 according to the NPDCCH information, where

- subframe n is the last subframe in which the NPDCCH is transmitted and is determined from the starting subframe of NPDCCH transmission and the DCI subframe repetition number field in the corresponding DCI;

- subframe(s) ni with i=0,1,…,N-1 are N consecutive NB-IoT DL subframe(s) excluding subframes used for SI messages or scheduling gap (if any) or processing gap (if any) where, n0<n1<…,nN-1 ,

- ![](media_svg/image453.svg) [公式≈: ^{NNNN}^{=}TBRepSF], where the value of ![](media_svg/image435.svg) [公式≈: ^{N}Rep] is determined as specified in Clause 16.4.1.3, the value of ![](media_svg/image454.svg) [公式≈: ^{N}SF]is determined by the resource assignment field in the corresponding DCI (see Clause 16.4.1.3), and the value of ![](media_svg/image455.svg) [公式≈: ^{N}TB]is determined by the Number of scheduled TB for Unicast field or Number of scheduled TB for SC-MTCH field, if present, in the corresponding DCI, ![](media_svg/image456.svg) [公式: N_{TB}=1] otherwise,

- k0 is the number of NB-IoT DL subframe(s) starting in DL subframe n+5 for FDD or IoT NTN TDD or subframe n+5 for TN TDD, until DL subframe n0, where k0 is determined by the scheduling delay field (![](media_svg/image439.svg) [公式≈: ^{I}Delay]) for DCI format N1, and k0 = 0 for DCI format N2. For DCI CRC scrambled by G-RNTI, k0 is determined by the scheduling delay field (![](media_svg/image439.svg) [公式≈: ^{I}Delay]) according to Table 16.4.1-1a, otherwise k0 is determined by the scheduling delay field (![](media_svg/image439.svg) [公式≈: ^{I}Delay]) according to Table 16.4.1-1. The value of ![](media_svg/image457.svg) [公式≈: ^{R}max]is according to Clause 16.6 for the corresponding DCI format N1,

- for ![](media_svg/image458.svg) [公式: N_{TB}>1],

- if the UE is configured with higher layer parameter multiTB-Config in npdsch-MultiTB-Config set to 'interleaved', and NPDSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI, and ![](media_svg/image459.svg) [公式≈: ^{N}Rep^{>}^{4}]

- NB-IoT DL subframes ![](media_svg/image460.svg) [公式≈: ^{n}gcNrl∪∪++(TB)] with ![](media_svg/image461.svg) [公式≈: lgcNgN=−=−=0,1,1,0,1,/41,4κκ_{RepSF}] are associated with TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]

- otherwise,

- NB-IoT DL subframes ![](media_svg/image463.svg) [公式≈: ^{n}rNNl∪+_{RepSF}] with ![](media_svg/image464.svg) [公式≈: lNN=−0,1,1κ_{RepSF}] are associated with TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]

- for ![](media_svg/image458.svg) [公式: N_{TB}>1] and NPDSCH corresponding to an NPDCCH with DCI CRC scrambled by G-RNTI,

- if multiTB-Gap is not configured and ![](media_svg/image465.svg) [公式≈: ^{NN}RepSF^{<}^{12}], a processing gap of 20ms is inserted after every 2 TBs

- otherwise, a scheduling gap with a length equal to the indicated value of multiTB-Gap is inserted between TBr and TBr+1, ![](media_svg/image466.svg) [公式: rN=−1,2,1κ_{TB}].

- If the scheduling gap or the processing gap overlaps with the NPDSCH transmission gap defined in [3], the overlapped part of the scheduling gap or processing gap is also counted as the part of NPDSCH transmission gap.

Table 16.4.1-1: ![](media_svg/image467.svg) [公式≈: ^{k}0]for DCI format N1.

| ![](media_svg/image439.svg) [公式≈: ^{I}Delay] | ![](media_svg/image467.svg) [公式≈: ^{k}0] |  |
| --- | --- | --- |
|  | ![](media_svg/image468.svg) [公式: R_{max}<128] | ![](media_svg/image469.svg) [公式: R_{max}÷128] |
| 0 | 0 | 0 |
| 1 | 4 | 16 |
| 2 | 8 | 32 |
| 3 | 12 | 64 |
| 4 | 16 | 128 |
| 5 | 32 | 256 |
| 6 | 64 | 512 |
| 7 | 128 | 1024 |

Table 16.4.1-1a: ![](media_svg/image467.svg) [公式≈: ^{k}0]for DCI format N1 with DCI CRC scrambled by G-RNTI.

| ![](media_svg/image439.svg) [公式≈: ^{I}Delay] | ![](media_svg/image467.svg) [公式≈: ^{k}0] |
| --- | --- |
| 0 | 0 |
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |

If a UE is configured with higher layer parameter twoHARQ-ProcessesConfig

- for FDD, the UE is not expected to receive transmissions in the Type B half duplex guard periods as specified in [3]

otherwise

- for FDD, the UE is not expected to receive transmissions in 3 DL subframes following the end of a NPUSCH transmission by the UE.

- for TDD, the UE is not expected to receive transmissions in 3 subframes following the end of a NPUSCH transmission by the UE.

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-2. 
The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by P-RNTI.

Table 16.4.1-2: NPDCCH and NPDSCH configured by P-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N2 | Type-1 Common | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the RA-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-3. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by RA-RNTI.

Table 16.4.1-3: NPDCCH and NPDSCH configured by RA-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N1 | Type-2 Common | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI except during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-4. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by C-RNTI.

Table 16.4.1-4: NPDCCH and NPDSCH configured by C-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N1 | UE specific by C-RNTI | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the Temporary C-RNTI and is not configured to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by Temporary C-RNTI.

If a UE is also configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by C-RNTI.

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the CB-RNTI during the CB-Msg3-EDT procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by CB-RNTI.

Table 16.4.1-5: NPDCCH and NPDSCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure, or CB-RNTI during CB-Msg3-EDT procedure

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N1 | Type-2 Common | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

For NPDSCH carrying SystemInformationBlockType1-NB and SI-messages, the UE shall decode NPDSCH according to the transmission scheme defined in Table 16.4.1-6. The scrambling initialization of NPDSCH is by SI-RNTI.

Table 16.4.1-6: NPDSCH configured by SI-RNTI

| Transmission scheme of NPDSCH |
| --- |
| If the number of NPBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the SC-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-7. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by SC-RNTI.

Table 16.4.1-7: NPDCCH and NPDSCH configured by SC-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N2 | Type-1A Common | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the G-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-8. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by G-RNTI.

Table 16.4.1-8: NPDCCH and NPDSCH configured by G-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N1 | Type-2A Common | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the PUR-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combination defined in Table 16.4.1-9. The scrambling initialization of the NPDSCH corresponding to these NPDCCHs is by PUR-RNTI.

Table 16.4.1-9: NPDCCH and NPDSCH configured by PUR-RNTI

| DCI format | Search Space | Transmission scheme of NPDSCH corresponding to NPDCCH |
| --- | --- | --- |
| DCI format N1 | UE specific by PUR-RNTI | If the number of NPBCH antenna ports is one, Single-antenna port, port 2000 is used (see Clause 16.4.1.1), otherwise Transmit diversity (see Clause 16.4.1.2). |

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by G-RNTI in subframes in which the UE monitors a Type1A-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI or G-RNTI in subframes in which the UE monitors a Type1-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by P-RNTI

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI or G-RNTI in subframes in which the UE monitors a Type2-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by C-RNTI, CB-RNTI, or Temporary C-RNTI.

The transmission schemes for NPDSCH are defined in the following Clauses.

#### 16.4.1.1 Single-antenna port scheme

For the single-antenna port transmission schemes (port 2000) of the NPDSCH, the UE may assume that an eNB transmission on the NPDSCH would be performed according to Clause 6.3.4.1 of [3].

#### 16.4.1.2 Transmit diversity scheme

For the transmit diversity transmission scheme of the NPDSCH, the UE may assume that an eNB transmission on the NPDSCH would be performed according to Clause 6.3.4.3 of [3]

#### 16.4.1.3 Resource allocation

The resource allocation information in DCI format N1, N2 (paging) for NPDSCH indicates to a scheduled UE

- a number of subframes (![](media_svg/image470.svg) [公式≈: ^{N}SF]) determined by the resource assignment field (![](media_svg/image471.svg) [公式≈: ^{I}SF]) in the corresponding DCI according to Table 16.4.1.3-1.

- a repetition number (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) determined by the repetition number field (![](media_svg/image437.svg) [公式≈: ^{I}Rep]) in the corresponding DCI according to Table 16.4.1.3-2, except for NPDSCH with 16QAM where $ N_{Rep}=1 $.

Table 16.4.1.3-1: Number of subframes (![](media_svg/image470.svg) [公式≈: ^{N}SF]) for NPDSCH.

| ![](media_svg/image471.svg) [公式≈: ^{I}SF] | ![](media_svg/image472.svg) [公式≈: ^{N}SF] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 8 |
| 7 | 10 |

Table 16.4.1.3-2: Number of repetitions (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) for NPDSCH.

| ![](media_svg/image437.svg) [公式≈: ^{I}Rep] | ![](media_svg/image435.svg) [公式≈: ^{N}Rep] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |
| 8 | 192 |
| 9 | 256 |
| 10 | 384 |
| 11 | 512 |
| 12 | 768 |
| 13 | 1024 |
| 14 | 1536 |
| 15 | 2048 |

For FDD or IoT NTN TDD, the number of repetitions for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-3.

Table 16.4.1.3-3: Number of repetitions for NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD.

| Value of schedulingInfoSIB1 | Number of NPDSCH repetitions |
| --- | --- |
| 0 | 4 |
| 1 | 8 |
| 2 | 16 |
| 3 | 4 |
| 4 | 8 |
| 5 | 16 |
| 6 | 4 |
| 7 | 8 |
| 8 | 16 |
| 9 | 4 |
| 10 | 8 |
| 11 | 16 |
| 12-15 | Reserved |

For FDD or IoT NTN TDD, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-4.

Table 16.4.1.3-4: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD.

| Number of NPDSCH repetitions | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell] | Starting radio frame number for SystemInformationBlockType1-NB repetitions (nf mod 256) |
| --- | --- | --- |
| 4 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 0 | 0 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 1 | 16 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 2 | 32 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 3 | 48 |
| 8 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | 0 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | 16 |
| 16 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | 0 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | 1 |

For the TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected, the number of repetitions and subframe index for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-5.

Table 16.4.1.3-5: Number of repetitions and subframe index for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

| Value of schedulingInfoSIB1 | Number of NPDSCH repetitions | Subframe index |
| --- | --- | --- |
| 0 | 4 | 0 |
| 1 | 8 | 0 |
| 2 | 16 | 0 |
| 3 | 4 | 0 |
| 4 | 8 | 0 |
| 5 | 16 | 0 |
| 6 | 4 | 0 |
| 7 | 8 | 0 |
| 8 | 16 | 0 |
| 9 | 4 | 0 |
| 10 | 8 | 0 |
| 11 | 16 | 0 |
| 12-15 | 16 | 4 |

For the TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-6.

Table 16.4.1.3-6: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

| Subframe index | Number of NPDSCH repetitions | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell] | Starting radio frame number for SystemInformationBlockType1-NB repetitions (nf mod 256) |
| --- | --- | --- | --- |
| 0 | 4 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 0 | 1 |
|  |  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 1 | 17 |
|  |  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 2 | 33 |
|  |  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 4 = 3 | 49 |
| 0 | 8 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | 1 |
|  |  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | 17 |
| 0 | 16 | Any | nf mod 256 = 1 |
| 4 | 16 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | nf mod 256 = 0 |
|  |  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | nf mod 256 = 1 |

For a higher layer configured TN TDD NB-IoT carrier, the number of repetitions and subframe index for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-7.

Table 16.4.1.3-7: Number of repetitions and subframe index for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

| Value of schedulingInfoSIB1 | Number of NPDSCH repetitions | Subframe index |
| --- | --- | --- |
| 0 | 8 | 0, 5 |
| 1 | 16 | 0, 5 |
| 2 | 8 | 0, 5 |
| 3 | 16 | 0, 5 |
| 4 | 8 | 0, 5 |
| 5 | 16 | 0, 5 |
| 6 | 8 | 0, 5 |
| 7 | 16 | 0, 5 |

For a higher layer configured TN TDD NB-IoT carrier, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-8.

Table 16.4.1.3-8: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

| Number of NPDSCH repetitions | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell] | Starting radio frame number for SystemInformationBlockType1-NB repetitions (nf mod 256) |
| --- | --- | --- |
| 8 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | 0 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | 16 |
| 16 | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 0 | 0 |
|  | ![](media_svg/image473.svg) [公式≈: _{N}_{ID}Ncell]mod 2 = 1 | 1 |

#### 16.4.1.4 NPDSCH starting position

The starting OFDM symbol for NPDSCH is given by index  in the first slot in a subframe ![](media_svg/image475.svg) [公式: k] and is determined as follows

- if subframe  is a subframe used for receiving SIB1-NB

- ![](media_svg/image477.svg) [公式≈: ^{l}DataStart^{=}^{3}]if the value of the higher layer parameter operationModeInfo is set to '00' or '01'

- ![](media_svg/image477.svg) [公式≈: ^{l}DataStart^{=}^{3}] if the value of the higher layer parameter operationModeInfo is set to '10' and the value of the higher layer parameter sib-GuardbandInfo is set to '10' or '11' for TN TDD

- ![](media_svg/image478.svg) [公式≈: ^{l}DataStart^{=}^{0}]otherwise

- elseif subframe ![](media_svg/image476.svg) [公式: k] is a special subframe for NPDSCH without repetition

- ![](media_svg/image479.svg) [公式≈: ^{l}DataStart^{=}^{min}^{(}^{2}^{,}^{l}DataStart^{&apos;}^{)}] where ![](media_svg/image480.svg) [公式≈: ^{l}DataStart^{&apos;}]is given by the higher layer parameter eutraControlRegionSize if the value of the higher layer parameter eutraControlRegionSize is present

- ![](media_svg/image478.svg) [公式≈: ^{l}DataStart^{=}^{0}]otherwise

- else

- ![](media_svg/image481.svg) [公式≈: ^{l}DataStart]is given by the higher layer parameter eutraControlRegionSize if the value of the higher layer parameter eutraControlRegionSize is present

- ![](media_svg/image478.svg) [公式≈: ^{l}DataStart^{=}^{0}]otherwise

#### 16.4.1.5 Modulation order and transport block size determination

To determine the modulation order in the NPDSCH, the UE shall

- if the UE is configured with higher layer parameter npdsch-16QAM-Config and the DCI is mapped onto the UE specific search space given by C-RNTI, or the UE is configured with higher layer parameter pur-DL-16QAM-Config and the DCI is mapped onto the UE specific search space given by PUR-RNTI,

- If the 4-bit "modulation and coding scheme" field (![](media_svg/image482.svg) [公式≈: ^{I}MCS]) in the DCI is set to ‘1111’,

- use modulation order, ![](media_svg/image483.svg) [公式≈: ^{Q}m]= 4

- otherwise

- use modulation order, ![](media_svg/image483.svg) [公式≈: ^{Q}m]= 2


- otherwise

- use modulation order, ![](media_svg/image483.svg) [公式≈: ^{Q}m]= 2.

To determine the transport block size in the NPDSCH, the UE shall first,

- if NPDSCH carries SystemInformationBlockType1-NB

- set ![](media_svg/image484.svg) [公式≈: ^{I}TBS] to the value of the parameter schedulingInfoSIB1 configured by higher-layers

- else if NPDSCH with 16QAM

- read the 4-bit "modulation and coding scheme for 16QAM" ($ I_{MCS}^{'}$) in the DCI

- If for the carrier on which NPSS/NSSS/NPBCH are detected the value of the higher layer parameter operationModeInfo is set to '00' or '01', or if the value of the higher layer parameter inbandCarrierInfo-r13 is configured for a higher layer configured carrier if any, set $ I_{TBS}=I_{MCS}^{'}+11 $, otherwise set $ I_{TBS}=I_{MCS}^{'}+14 $

- otherwise

- read the 4-bit "modulation and coding scheme" field (![](media_svg/image485.svg) [公式≈: ^{I}MCS]) in the DCI and set ![](media_svg/image486.svg) [公式≈: ^{I}TBS^{=}^{I}MCS].

and second,

- if NPDSCH carries SystemInformationBlockType1-NB

- use Clause 16.4.1.5.2 for determining its transport block size.

- otherwise,

- read the 3-bit "resource assignment" field (![](media_svg/image487.svg) [公式≈: ^{I}SF]) in the DCI and determine its TBS by the procedure in Clause 16.4.1.5.1.

For a NPDCCH UE-specific search space, if the UE is configured with higher layer parameter twoHARQ-ProcessesConfig, or the UE is configured with higher layer parameter npdsch-MultiTB-Config and single TB is scheduled in the corresponding DCI

- the NDI and HARQ process ID as signalled on NPDCCH, and the TBS, as determined above, shall be delivered to higher layers,

otherwise

- the NDI as signalled on NPDCCH, and the TBS, as determined above, shall be delivered to higher layers. If the UE is configured with higher layer parameter npdsch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, the HARQ process ID of 0 is for the first TB and HARQ process ID of 1 shall be assumed for the second TB, otherwise, HARQ process ID of 0 shall be assumed.

##### 16.4.1.5.1 Transport blocks not mapped for SystemInformationBlockType1-NB

The TBS is given by the (![](media_svg/image9.svg) [公式≈: ^{I}TBS],![](media_svg/image488.svg) [公式≈: ^{I}SF]) entry of Table 16.4.1.5.1-1.

If for the carrier on which NPSS/NSSS/NPBCH are detected the value of the higher layer parameter operationModeInfo is set to '00' or '01', or if the value of the higher layer parameter inbandCarrierInfo-r13 is configured for a higher layer configured carrier if any,

- if NPDSCH with 16QAM $ 11\leq  I_{TBS}\leq  17 $, otherwise ![](media_svg/image489.svg) [公式: 0≥I_{TBS}≥10];

otherwise,

- if NPDSCH with 16QAM $ 14\leq  I_{TBS}\leq  21 $, otherwise $ 0\leq  I_{TBS}\leq  13 $.

Table 16.4.1.5.1-1: Transport block size (TBS) table.

| ![](media_svg/image9.svg) [公式≈: ^{I}TBS] | ![](media_svg/image488.svg) [公式≈: ^{I}SF] |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 | 16 | 32 | 56 | 88 | 120 | 152 | 208 | 256 |
| 1 | 24 | 56 | 88 | 144 | 176 | 208 | 256 | 344 |
| 2 | 32 | 72 | 144 | 176 | 208 | 256 | 328 | 424 |
| 3 | 40 | 104 | 176 | 208 | 256 | 328 | 440 | 568 |
| 4 | 56 | 120 | 208 | 256 | 328 | 408 | 552 | 680 |
| 5 | 72 | 144 | 224 | 328 | 424 | 504 | 680 | 872 |
| 6 | 88 | 176 | 256 | 392 | 504 | 600 | 808 | 1032 |
| 7 | 104 | 224 | 328 | 472 | 584 | 680 | 968 | 1224 |
| 8 | 120 | 256 | 392 | 536 | 680 | 808 | 1096 | 1352 |
| 9 | 136 | 296 | 456 | 616 | 776 | 936 | 1256 | 1544 |
| 10 | 144 | 328 | 504 | 680 | 872 | 1032 | 1384 | 1736 |
| 11 | 176 | 376 | 584 | 776 | 1000 | 1192 | 1608 | 2024 |
| 12 | 208 | 440 | 680 | 904 | 1128 | 1352 | 1800 | 2280 |
| 13 | 224 | 488 | 744 | 1032 | 1256 | 1544 | 2024 | 2536 |
| 14 | 256 | 552 | 840 | 1128 | 1416 | 1736 | 2280 | 2856 |
| 15 | 280 | 600 | 904 | 1224 | 1544 | 1800 | 2472 | 3112 |
| 16 | 296 | 632 | 968 | 1288 | 1608 | 1928 | 2600 | 3240 |
| 17 | 336 | 696 | 1064 | 1416 | 1800 | 2152 | 2856 | 3624 |
| 18 | 376 | 776 | 1160 | 1544 | 1992 | 2344 | 3112 | 4008 |
| 19 | 408 | 840 | 1288 | 1736 | 2152 | 2600 | 3496 | 4264 |
| 20 | 440 | 904 | 1384 | 1864 | 2344 | 2792 | 3752 | 4584 |
| 21 | 488 | 1000 | 1480 | 1992 | 2472 | 2984 | 4008 | 4968 |

##### 16.4.1.5.2 Transport blocks mapped for SystemInformationBlockType1-NB

The TBS is given by the![](media_svg/image490.svg) [公式≈: ^{I}TBS]entry of Table 16.4.1.5.2-1 for FDD or IoT NTN TDD, and Table 16.4.1.5.2-2 for TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected and Table 16.4.1.5.2-3 for a higher layer configured TN TDD NB-IoT carrier.

Table 16.4.1.5.2-1: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD

| ![](media_svg/image9.svg) [公式≈: ^{I}TBS] | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBS | 208 | 208 | 208 | 328 | 328 | 328 | 440 | 440 | 440 | 680 | 680 | 680 | Reserved |  |  |  |

Table 16.4.1.5.2-2: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD

| ![](media_svg/image9.svg) [公式≈: ^{I}TBS] | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBS | 208 | 208 | 208 | 328 | 328 | 328 | 440 | 440 | 440 | 680 | 680 | 680 | 208 | 328 | 440 | 680 |

Table 16.4.1.5.2-3: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD

| ![](media_svg/image9.svg) [公式≈: ^{I}TBS] | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBS | 208 | 208 | 328 | 328 | 440 | 440 | 680 | 680 |

### 16.4.2 UE procedure for reporting ACK/NACK

The UE shall upon detection of a NPDSCH transmission ending in NB-IoT subframe n intended for the UE and for which an ACK/NACK shall be provided, start, after the end of

- ![](media_svg/image491.svg) [公式≈: nkK++−_{0offset}±1] DL subframe for FDD or IoT NTN TDD,

- ![](media_svg/image492.svg) [公式: k_{0}±−1] NB-IoT UL subframes following the end of n+12 subframe for TN TDD,

transmission of the NPUSCH carrying ACK/NACK response, and SR (if any) if the serving cell is FDD or IoT NTN TDD and the UE is configured with higher layer parameter sr-with-HARQ-ACK-Config, using NPUSCH format 2 in N consecutive NB-IoT UL slots, where

- ![](media_svg/image493.svg) [公式≈: ^{NNNN}^{=}TBRepslots^{±}^{ANUL}], where

- the value of ![](media_svg/image494.svg) [公式≈: ^{N}Rep^{AN}]is given by the higher layer parameter ack-NACK-NumRepetitions-Msg4 configured for the associated NPRACH resource for Msg4 NPDSCH transmission, and higher layer parameter ack-NACK-NumRepetitions otherwise,

- the value of ![](media_svg/image495.svg) [公式≈: ^{N}slots^{UL}] is the number of slots of the resource unit (defined in clause 10.1.2.3 of [3]), and

- if the UE is configured with higher layer parameter harq-ACK-Bundling in npdsch-MultiTB-Config, or if the UE is in a NTN serving cell and multiple TB are scheduled in the NPDCCH corresponding to the NPDSCH and the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the NPDSCH, then ![](media_svg/image496.svg) [公式: N_{TB}±=1], otherwise ![](media_svg/image497.svg) [公式≈: ^{NN}TBTB^{±}^{=}], where the value of ![](media_svg/image455.svg) [公式≈: ^{N}TB]is determined by the Number of scheduled TB for Unicast field if present in the NPDCCH corresponding to the NPDSCH, otherwise ![](media_svg/image456.svg) [公式: N_{TB}=1],

- allocated subcarrier for ACK/NACK and value of k0 is determined by the ACK/NACK resource field in the DCI format of the corresponding NPDCCH or the HARQ ACK resource field in the MAC CMR of CB-Msg4 [8] according to Table 16.4.2-1, and Table 16.4.2-2,

- for FDD or IoT NTN TDD, ![](media_svg/image498.svg) [公式: kk_{00}±=].

- for TN TDD, ![](media_svg/image499.svg) [公式: kk_{00}±=−12].

- For ![](media_svg/image500.svg) [公式: N_{TB}>1]

- if the UE is configured with higher layer parameter harq-AckBundling in npdsch-MultiTB-Config, and the NPDSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI,

- if the UE is in a NTN serving cell and if the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the NPDSCH, the UE shall generate an ACK for HARQ-ACK corresponding to the transport block

- the ACK/NACK response is generated by performing a logical AND operation of HARQ-ACKs corresponding to the TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]

- otherwise,

- if ![](media_svg/image496.svg) [公式: N_{TB}±=1]

- the ACK/NACK response is the HARQ-ACK corresponding to the transport block associated with the HARQ process with enabled HARQ-ACK information

- otherwise

- NB-IoT UL slots ![](media_svg/image501.svg) [公式≈: ^{n}^{rNNl}^{∪+}Repslots^{ANUL}] with ![](media_svg/image502.svg) [公式≈: lNN=−0,1,1κ_{Repslots}^{ANUL}] of the NPUSCH carry ACK/NACK response for TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]

except if the UE is in a NTN serving cell, and the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for all HARQ process(es) associated with transport block(s) in the NPDSCH, or the HARQ-ACK Resource field functions as HARQ feedback disabled indicator in DCI format N1 as specified in [4] in the NPDCCH corresponding to the NPDSCH.

Table 16.4.2-1: ACK/NACK subcarrier and ![](media_svg/image467.svg) [公式≈: ^{k}0]for NPUSCH with subcarrier spacing ![](media_svg/image449.svg) [公式: δf=3.75kHz].

| ACK/NACK resource field | ACK/NACK subcarrier | ![](media_svg/image467.svg) [公式≈: ^{k}0] |
| --- | --- | --- |
| 0 | 38 | 13 |
| 1 | 39 | 13 |
| 2 | 40 | 13 |
| 3 | 41 | 13 |
| 4 | 42 | 13 |
| 5 | 43 | 13 |
| 6 | 44 | 13 |
| 7 | 45 | 13 |
| 8 | 38 | 21 |
| 9 | 39 | 21 |
| 10 | 40 | 21 |
| 11 | 41 | 21 |
| 12 | 42 | 21 |
| 13 | 43 | 21 |
| 14 | 44 | 21 |
| 15 | 45 | 21 |

Table 16.4.2-2: ACK/NACK subcarrier and ![](media_svg/image467.svg) [公式≈: ^{k}0]for NPUSCH with subcarrier spacing ![](media_svg/image503.svg) [公式: δf=15kHz].

| ACK/NACK resource field | ACK/NACK subcarrier | ![](media_svg/image467.svg) [公式≈: ^{k}0] |
| --- | --- | --- |
| 0 | 0 | 13 |
| 1 | 1 | 13 |
| 2 | 2 | 13 |
| 3 | 3 | 13 |
| 4 | 0 | 15 |
| 5 | 1 | 15 |
| 6 | 2 | 15 |
| 7 | 3 | 15 |
| 8 | 0 | 17 |
| 9 | 1 | 17 |
| 10 | 2 | 17 |
| 11 | 3 | 17 |
| 12 | 0 | 18 |
| 13 | 1 | 18 |
| 14 | 2 | 18 |
| 15 | 3 | 18 |

## 16.5 Narrowband physical uplink shared channel related procedures

For a NB-IoT UE that supports twoHARQ-Processes-r14 or the UE is configured with higher layer parameter npusch-MultiTB-Config, there shall be a maximum of 2 uplink HARQ processes.

For a NB-IoT UE and NPUSCH transmission using preconfigured uplink resource, there shall be 1 uplink HARQ process.

A NB-IoT UE shall determine whether a subframe is a NB-IoT UL subframe as follows

- If higher layer parameter resourceReservationConfigUL is configured

- for NPUSCH format 1 transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space including NPUSCH format 1 transmission without a corresponding NPDCCH

- if the Resource reservation field in the DCI is set to 0, then the subframe is assumed as a NB-IoT UL subframe

- else if the Resource reservation field in the DCI is set to 1, then the subframe is assumed as a NB-IoT UL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols are reserved in the subframe).

- for NPUSCH format 2 transmission

- the subframe is assumed as a NB-IoT UL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols are reserved in the subframe).

- In all other cases,

- for TN TDD, a NB-IoT UE shall assume a subframe as a NB-IoT UL subframe if, for a NB-IoT carrier, it is configured as NB-IoT UL subframe by higher layers

- for FDD, a NB-IoT UE shall always assume a subframe as a NB-IoT UL subframe

- for IoT NTN TDD, a NB-IoT UE shall assume a subframe as a NB-IoT UL subframe if it is one of the U consecutive uplink subframes according to the frame structure type 1 for IoT NTN TDD and the value of U defined in [3].

### 16.5.1 UE procedure for transmitting format 1 narrowband physical uplink shared channel

NPUSCH format 1 transmission can be scheduled by a NPDCCH with DCI format N0, or the transmission can correspond to using preconfigured uplink resource configured by higher layers. Transmission using preconfigured uplink resource is initiated by higher layers as specified in [14] , while retransmission of transport blocks transmitted using preconfigured uplink resource are scheduled by a NPDCCH with DCI format N0.

A UE shall upon detection on a given serving cell of a NPDCCH with DCI format N0 ending in NB-IoT DL subframe n scheduling NPUSCH intended for the UE, perform, at the end of

- n+k0+Koffset DL subframe for FDD or IoT NTN TDD,

- k0 NB-IoT UL subframes following the end of n+8 subframe for TN TDD,

a corresponding NPUSCH transmission using NPUSCH format 1 in N consecutive NB-IoT UL slots ni with i = 0, 1, …, N-1 according to the NPDCCH information where

- subframe n is the last subframe in which the NPDCCH is transmitted and is determined from the starting subframe of NPDCCH transmission and the DCI subframe repetition number field in the corresponding DCI; and

- ![](media_svg/image504.svg) [公式≈: ^{NNNNN}^{=}TBRepRUslots^{UL}], where the value of ![](media_svg/image435.svg) [公式≈: ^{N}Rep] is determined as specified in Clause 16.5.1.1, the value of ![](media_svg/image505.svg) [公式≈: ^{N}RU]is determined by the resource assignment field in the corresponding DCI (see Clause 16.5.1.1), the value of ![](media_svg/image495.svg) [公式≈: ^{N}slots^{UL}] is the number of NB-IoT UL slots of the resource unit (defined in clause 10.1.2.3 of [3]) corresponding to the ![](media_svg/image506.svg) [公式≈: _{N}_{sc}RU] allocated number of subcarriers (as determined in Clause 16.5.1.1) in the corresponding DCI, and the value of ![](media_svg/image455.svg) [公式≈: ^{N}TB]is determined by the Number of scheduled TB for Unicast field, if present, in the corresponding DCI, ![](media_svg/image456.svg) [公式: N_{TB}=1] otherwise

- for FDD or IoT NTN TDD,

- if NPUSCH transmission with subcarrier spacing![](media_svg/image449.svg) [公式: δf=3.75kHz] and the UE configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled in the corresponding DCI,

- n0 is the first NB-IoT UL slot, $ n_{s}$, starting after the end of subframe n+k0+Koffset that fulfills $(5n_{f}+n_{s}) mod 4=0 $

- otherwise,

- n0 is the first NB-IoT UL slot starting after the end of subframe n+k0+Koffset

- for TN TDD, n0 is the first NB-IoT UL slot starting after k0 NB-IoT UL subframes following the end of n+8 subframe

- value of k0 is determined by the scheduling delay field (![](media_svg/image439.svg) [公式≈: ^{I}Delay]) in the corresponding DCI according to Table 16.5.1-1 for FDD or IoT NTN TDD and Table 16.5.1-1A for TN TDD

- For ![](media_svg/image500.svg) [公式: N_{TB}>1],

- if the UE is configured with higher layer parameter npusch-MultiTB-Config set to 'interleaved', and NPUSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI, and ![](media_svg/image507.svg) [公式≈: ^{NC}Rep^{>}] where ![](media_svg/image508.svg) [公式: C=1] for ![](media_svg/image509.svg) [公式: N_{sc}^{RU}=1], ![](media_svg/image510.svg) [公式: C=4] otherwise.

- NB-IoT UL slots ![](media_svg/image460.svg) [公式≈: ^{n}gcNrl∪∪++(TB)] with $ l=0,1,\ldots  g-1, c=0,1,\ldots  N_{Rep}/(CM_{OCC})-1, g=CM_{OCC}N_{RU}N_{slots}^{UL}$ are associated with TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]. $ M_{OCC}=2 $ if $ N_{sc}^{RU}=1 $ and the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled in the corresponding DCI, $ M_{OCC}=1 $ otherwise.

- otherwise,

- NB-IoT UL slots ![](media_svg/image511.svg) [公式≈: ^{n}^{rNNNl}^{∪+}RepRUslots^{UL}] with ![](media_svg/image512.svg) [公式≈: lNNN=−0,1,1κ_{RepRUslots}^{UL}] are associated with TBr+1 , ![](media_svg/image462.svg) [公式: rN=−0,1,1κ_{TB}]

Table 16.5.1-1: ![](media_svg/image467.svg) [公式≈: ^{k}0]for DCI format N0 for FDD or IoT NTN TDD.

| ![](media_svg/image439.svg) [公式≈: ^{I}Delay] | ![](media_svg/image467.svg) [公式≈: ^{k}0] |
| --- | --- |
| 0 | 8 |
| 1 | 16 |
| 2 | 32 |
| 3 | 64 |

Table 16.5.1-1A: ![](media_svg/image467.svg) [公式≈: ^{k}0]for DCI format N0 for TN TDD.

| ![](media_svg/image439.svg) [公式≈: ^{I}Delay] | ![](media_svg/image467.svg) [公式≈: ^{k}0] |
| --- | --- |
| 0 | 0 |
| 1 | 8 |
| 2 | 16 |
| 3 | 32 |

If a NPUSCH transmission without a corresponding NPDCCH collides partially or fully with a NPDSCH transmission, the NPUSCH transmission is dropped.

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-2 and transmit a corresponding NPUSCH. The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and the NPUSCH retransmission for the same transport block is by C-RNTI.

Table 16.5.1-2: NPDCCH and NPUSCH configured by C-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format N0 | UE specific by C-RNTI |

If a UE is configured to receive random access procedures initiated by "PDCCH orders", the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-3.

Table 16.5.1-3: NPDCCH configured as "PDCCH order" to initiate random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format N1 | UE specific by C-RNTI |

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the Temporary C-RNTI regardless of whether UE is configured or not configured to decode NPDCCH with the CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-4 and transmit the corresponding NPUSCH. The scrambling initialization of NPUSCH corresponding to these NPDCCHs is by Temporary C-RNTI.

If a Temporary C-RNTI is set by higher layers, the scrambling initialization of NPUSCH corresponding to the Narrowband Random Access Response Grant in Clause 16.3.3 and any NPUSCH retransmission(s) for the same transport block is by Temporary C-RNTI. Otherwise, the scrambling initialization of NPUSCH corresponding to the Narrowband Random Access Response Grant in Clause 16.3.3 and any NPUSCH retransmission(s) for the same transport block is by C-RNTI.

If a UE is also configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-4 and transmit the corresponding NPUSCH. The scrambling initialization of NPUSCH corresponding to these NPDCCH is by C-RNTI.

The scrambling initialization of NPUSCH corresponding to the CB-Msg3 is by CB-RNTI.

Table 16.5.1-4: NPDCCH and NPUSCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format N0 | Type-2 Common |

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the SPS C-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-5 and transmit a corresponding NPUSCH if a transport block corresponding to the HARQ process of the NPUSCH transmission is generated as described in [8]. 
The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and NPUSCH retransmission for the same transport block is by SPS C-RNTI. The scrambling initialization of initial transmission of this NPUSCH without a corresponding NPDCCH and the NPUSCH retransmission for the same transport block is by SPS C-RNTI.

Table 16.5.1-5: NPDCCH and NPUSCH configured by SPS C-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format N0 | UE specific by C-RNTI |

A UE may transmit NPUSCH on preconfigured uplink resources as configured by higher layers. The scrambling initialization of NPUSCH transmission using preconfigured uplink resource is by PUR-RNTI.

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the PUR-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-6 and in case the indication in the DCI corresponds to the retransmission of a transport block transmitted using preconfigured uplink resource, transmit a corresponding NPUSCH. The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and the NPUSCH retransmission for the same transport block is by PUR-RNTI.

Table 16.5.1-6: NPDCCH and NPUSCH configured by PUR-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format N0 | UE specific by PUR-RNTI |

#### 16.5.1.1 Resource allocation

The resource allocation information in uplink DCI format N0 for NPUSCH transmission or configured by higher layers for NPUSCH transmission using preconfigured uplink resource indicates to a scheduled UE, or configured by higher layers for CB-Msg3-EDT

- a set of contiguously allocated subcarriers (![](media_svg/image513.svg) [公式≈: ^{n}sc]) of a resource unit determined by the Subcarrier indication field, or by the Modulation and coding scheme and Subcarrier indication field, or by the higher layer parameter npusch-SubCarrierSetIndex in PUR-Config-NB, or by the higher layer parameter npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB

- a number of resource units (![](media_svg/image505.svg) [公式≈: ^{N}RU]) determined by the resource assignment field according to Table 16.5.1.1-2, or by the higher layer parameter npusch-NumRUsIndex in PUR-Config-NB, or by the higher layer parameter npusch-NumRUsIndex in CB-Msg3-ConfigSIB-NB

- a repetition number (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) determined by the repetition number field according to Table 16.5.1.1-3, and for a NPUSCH transmission using preconfigured uplink resource or for a NPUSCH transmission using CB-Msg3 resource, the UE shall use the repetition number configured by higher layers; except for NPUSCH with 16QAM where $ N_{Rep}=1 $

- OCC enabled/disabled if the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $.

The subcarrier spacing ![](media_svg/image514.svg) [公式: δf] of NPUSCH transmission is determined by

- the higher layer parameter npusch-SubCarrierSetIndex, in the case of NPUSCH transmission using preconfigured uplink resources and subsequent NPUSCH transmissions until a Narrowband Random Access Response Grant is received,

- the higher layer parameter npusch-SubCarrierSetList, in the case of NPUSCH transmission using CB-Msg3 resources and subsequent NPUSCH transmissions, or

- the uplink subcarrier spacing field in the Narrowband Random Access Response Grant according to Clause 16.3.3 otherwise.

For NPUSCH transmission with subcarrier spacing![](media_svg/image449.svg) [公式: δf=3.75kHz], ![](media_svg/image431.svg) [公式≈: ^{n}sc^{=}^{I}sc]where ![](media_svg/image432.svg) [公式≈: ^{I}sc] is the subcarrier indication field and ![](media_svg/image433.svg) [公式: I_{sc}=48,49,...,63]is reserved if the UE is not configured with higher layer parameter npusch-OCC-Enabled or the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}=1 $ or the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC disabled, or $ n_{sc}=\lfloor  \frac {I_{sc-MCS}}{10}\rfloor  $ where $ I_{sc-MCS}$ is the Modulation and coding scheme and Subcarrier indication field and $ I_{sc-MCS}=480,481,...,511 $ is reserved if the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled,, or nsc is configured by higher layers parameter npusch-SubCarrierSetIndex in PUR-Config-NB for NPUSCH transmissions using preconfigured uplink resources, or nsc is configured by higher layers parameter npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB for CB-Msg3-EDT.

For NPUSCH transmission with subcarrier spacing![](media_svg/image515.svg) [公式: δf=15kHz], the subcarrier indication field (![](media_svg/image432.svg) [公式≈: ^{I}sc]) in the DCI or npusch-SubCarrierSetIndex in PUR-Config-NB for NPUSCH transmissions using preconfigured uplink resources or npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB for CB-Msg3-EDT determines the set of contiguously allocated subcarriers (![](media_svg/image513.svg) [公式≈: ^{n}sc]) according to

- Table 16.5.1.1-1 if the UE is not configured with higher layer parameter npusch-OCC-Enabled or the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}=1 $,

- Table 16.5.1.1-4 if the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $, and OCC disabled,

- Table 16.5.1.1-5 otherwise.

Table 16.5.1.1-1: Allocated subcarriers for NPUSCH with ![](media_svg/image515.svg) [公式: δf=15kHz].

| Subcarrier indication field (![](media_svg/image432.svg) [公式≈: ^{I}sc]) | Set of Allocated subcarriers (![](media_svg/image513.svg) [公式≈: ^{n}sc]) |
| --- | --- |
| 0 – 11 | ![](media_svg/image432.svg) [公式≈: ^{I}sc] |
| 12-15 | ![](media_svg/image516.svg) [公式: 3(I_{sc}−12)+{0,1,2}] |
| 16-17 | ![](media_svg/image517.svg) [公式: 6(I_{sc}−16)+{0,1,2,3,4,5}] |
| 18 | ![](media_svg/image518.svg) [公式: {0,1,2,3,4,5,6,7,8,9,10,11}] |
| 19-63 | Reserved |

Table 16.5.1.1-2: Number of resource units (![](media_svg/image505.svg) [公式≈: ^{N}RU]) for NPUSCH.

| ![](media_svg/image519.svg) [公式≈: ^{I}RU] | ![](media_svg/image505.svg) [公式≈: ^{N}RU] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 8 |
| 7 | 10 |

Table 16.5.1.1-3: Number of repetitions (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) for NPUSCH.

| ![](media_svg/image436.svg) [公式≈: ^{I}Rep] | ![](media_svg/image435.svg) [公式≈: ^{N}Rep] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |

Table 16.5.1.1-4: Allocated subcarriers for NPUSCH with ![](media_svg/image515.svg) [公式: δf=15kHz]  when UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $, and OCC disabled.

| 5-LSB of Subcarrier indication field (![](media_svg/image432.svg) [公式≈: ^{I}sc]) | Set of Allocated subcarriers (![](media_svg/image513.svg) [公式≈: ^{n}sc]) |
| --- | --- |
| 0 – 11 | ![](media_svg/image432.svg) [公式≈: ^{I}sc] |
| 12-15 | ![](media_svg/image516.svg) [公式: 3(I_{sc}−12)+{0,1,2}] |
| 16-17 | ![](media_svg/image517.svg) [公式: 6(I_{sc}−16)+{0,1,2,3,4,5}] |
| 18 | ![](media_svg/image518.svg) [公式: {0,1,2,3,4,5,6,7,8,9,10,11}] |
| 19-31 | Reserved |

Table 16.5.1.1-5: Allocated subcarriers for NPUSCH with ![](media_svg/image515.svg) [公式: δf=15kHz]  when UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled.

| 4-LSB of Subcarrier indication field (![](media_svg/image432.svg) [公式≈: ^{I}sc]) | Set of Allocated subcarriers (![](media_svg/image513.svg) [公式≈: ^{n}sc]) |
| --- | --- |
| 0 – 11 | ![](media_svg/image432.svg) [公式≈: ^{I}sc] |
| 12-15 | Reserved |

#### 16.5.1.2 Modulation order, redundancy version and transport block size determination

To determine the modulation order, redundancy version and transport block size for the NPUSCH, the UE shall first

- read the "modulation and coding scheme" field () in the DCI or configured by higher layers for NPUSCH transmission using preconfigured uplink resource or NPUSCH transmission using CB-Msg3-EDT, or read the "Modulation and coding scheme and Subcarrier indication" field $\left ( I_{sc-MCS}\right ) $ in the DCI and set $ I_{MCS}=I_{sc-MCS}mod 10 $ if the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled and ![](media_svg/image449.svg) [公式: δf=3.75kHz], and

- read the "redundancy version" field (![](media_svg/image520.svg) [公式≈: ^{rv}DCI]) in the DCI, or initiate with $ rv_{DCI}=0 $ for NPUSCH transmission using preconfigured uplink resource or NPUSCH transmission using CB-Msg3-EDT, or when the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and ![](media_svg/image449.svg) [公式: δf=3.75kHz], and

- read the "resource assignment" field (![](media_svg/image519.svg) [公式≈: ^{I}RU]) in the DCI or configured by higher layers for NPUSCH transmission using preconfigured uplink resource or configured in higher layer parameter npusch-NumRUsIndex in CB-Msg3-Config-NB for NPUSCH transmission using CB-Msg3-EDT, and

- compute the total number of allocated subcarriers (![](media_svg/image506.svg) [公式≈: _{N}_{sc}RU]), number of resource units (![](media_svg/image505.svg) [公式≈: ^{N}RU]), and repetition number (![](media_svg/image435.svg) [公式≈: ^{N}Rep]) according to Clause 16.5.1.1.

If the UE is configured with higher layer parameter edt-Parameters and the most recent NPUSCH transmission including a transport block with EDT, the UE is not expected to receive a DCI indicating a NPUSCH retransmission as part of the contention based random access procedure with 3 ≤ IMCS ≤ 14.

If the UE is configured with higher layer parameter edt-Parameters, and for a NPUSCH retransmission of the same transport block including EDT as part of the contention based random access procedure with ![](media_svg/image521.svg) [公式: I_{MCS}=15] in the DCI,

- the modulation order is set to .

- if the UE is configured with higher layer parameter edt-SmallTBS-Enabled set to 'true', the repetition number for the NPUSCH retransmission is the smallest integer multiple of ![](media_svg/image523.svg) [公式: L] value that is equal to or larger than![](media_svg/image441.svg) [公式≈: ^{TBSTBSN}Msg3Msg3,maxRep^{∪}] where ![](media_svg/image442.svg) [公式≈: ^{TBS}Msg3] is the TBS corresponding to the NPUSCH transmission scheduled by the Narrowband Random Access Response Grant, and ![](media_svg/image443.svg) [公式≈: ^{TBS}Msg3,max] is given by the higher layer parameter edt-TBS.

elseif the UE is configured with higher layer parameter edt-Parameters, and if the DCI indicates a retransmission as part of the contention based random access procedure with ![](media_svg/image524.svg) [公式: 02≥≥I_{MCS}] and the most recent NPUSCH transmission including a transport block with EDT,

- the TBS and modulation are determined according to Table 16.3.3-1 in Clause 16.3.3, for ![](media_svg/image524.svg) [公式: 02≥≥I_{MCS}] and the transport block does not include EDT

elseif the UE is configured with higher layer parameter npusch-16QAM-Config, and the DCI is mapped onto the UE specific search space and ![](media_svg/image482.svg) [公式≈: ^{I}MCS] set to ‘1111’, or for NPUSCH transmission using preconfigured uplink resource and higher layer parameter pur-UL-16QAM-Config configured, ![](media_svg/image483.svg) [公式≈: ^{Q}m]= 4

otherwise, the UE shall use modulation order, ![](media_svg/image483.svg) [公式≈: ^{Q}m]= 2 if ![](media_svg/image525.svg) [公式: N_{sc}^{RU}>1]. The UE shall useand Table 16.5.1.2-1 to determine the modulation order to use for NPUSCH if ![](media_svg/image526.svg) [公式: N_{sc}^{RU}=1].

Table 16.5.1.2-1: Modulation and TBS index table for NPUSCH with ![](media_svg/image527.svg) [公式: N_{sc}^{RU}=1].

| MCS Index ![](media_svg/image5.svg) [公式≈: ^{I}MCS] | Modulation Order ![](media_svg/image483.svg) [公式≈: ^{Q}m] | TBS Index ![](media_svg/image9.svg) [公式≈: ^{I}TBS] |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 1 | 2 |
| 2 | 2 | 1 |
| 3 | 2 | 3 |
| 4 | 2 | 4 |
| 5 | 2 | 5 |
| 6 | 2 | 6 |
| 7 | 2 | 7 |
| 8 | 2 | 8 |
| 9 | 2 | 9 |
| 10 | 2 | 10 |

If the UE is configured with higher layer parameter npusch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, ![](media_svg/image520.svg) [公式≈: ^{rv}DCI] is used for each TB.

The NPUSCH associated with a TB is transmitted in N NB-IoT UL slots associated with the TB, ni , i=0,1,…,N-1. For the NPUSCH transmission in jth block of B consecutive NB-IoT UL slots associated with the TB ni ,![](media_svg/image528.svg) [公式: i=jB+b,b=0,1,κ,B−1,j=0,1,κ,^{N}_{L}^{Rep}−1,]![](media_svg/image529.svg) [公式≈: ^{BLNN}^{=}RUslots^{UL}], the redundancy version ![](media_svg/image530.svg) [公式: rv_{idx}(j)] associated with the TB is determined by, ![](media_svg/image531.svg) [公式≈: rv_{idx}(j)=2∪mod(rv_{DCI}+j,2)], where

- if ![](media_svg/image526.svg) [公式: N_{sc}^{RU}=1]

- if the UE is configured with higher layer parameter npusch-OCC-Enabled and $ N_{Rep}>1 $ and OCC enabled is indicated in corresponding DCI

- $ L=2 $

- otherwise

- $ L=1 $

- otherwise

- ![](media_svg/image532.svg) [公式≈: LN=min4,/2_{(}⊥∀_{⋅∂}_{Rep}_{)}].

Portion of NPUSCH codeword with ![](media_svg/image533.svg) [公式: rv_{idx}(j)] associated with a TB as defined in clause 6.3.2 in [4] mapped to slot ![](media_svg/image534.svg) [公式≈: ⋅_{⋅}_{√}_{L}b∂_{∂}_{∃}] of allocated ![](media_svg/image505.svg) [公式≈: ^{N}RU] resource unit(s) is transmitted in NB-IoT UL slots associated with the TB ni![](media_svg/image535.svg) [公式≈: i=jB+L^{⋅}_{⋅}_{√}_{L}^{b}^{∂}_{∂}_{∃}+l,l=0,1,κ,L−1] for ![](media_svg/image536.svg) [公式: δ=fkHz3.75]and ![](media_svg/image537.svg) [公式≈: ijBLllL=+++=−22mod(,2),0,1,...1^{⋅∂⋅∂}_{⋅∂⋅∂}_{√∃√∃}_{2}^{bb}_{LL}] for ![](media_svg/image538.svg) [公式: δ=fkHz15]

The UE shall use (![](media_svg/image9.svg) [公式≈: ^{I}TBS],![](media_svg/image539.svg) [公式≈: ^{I}RU]) and Table 16.5.1.2-2 to determine the TBS to use for the NPUSCH. ![](media_svg/image9.svg) [公式≈: ^{I}TBS]is given in Table 16.5.1.2-1 if ![](media_svg/image526.svg) [公式: N_{sc}^{RU}=1], or $ I_{TBS}=I_{MCS}^{'}+14 $ if NPUSCH with 16QAM except for NPUSCH transmission using preconfigured uplink resource in which case $ I_{TBS}$ is given by higher layers in PUR-Config-NB, or except for NPUSCH transmission using CB-Msg3-EDT resource in which case $ I_{TBS}$ is given by higher layer parameter npusch-MCS-r19 in CB-Msg3-Config-NB, ![](media_svg/image540.svg) [公式≈: ^{I}TBS^{=}^{I}MCS] otherwise. $ I_{MCS}^{'}$ is the value of the "modulation and coding scheme for 16QAM" in the DCI.

- If NPUSCH with 16QAM $ 14\leq  I_{TBS}\leq  21 $, otherwise $ 0\leq  I_{TBS}\leq  13 $.

Table 16.5.1.2-2: Transport block size (TBS) table for NPUSCH.

| ![](media_svg/image9.svg) [公式≈: ^{I}TBS] | ![](media_svg/image541.svg) [公式≈: ^{I}RU] |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 | 16 | 32 | 56 | 88 | 120 | 152 | 208 | 256 |
| 1 | 24 | 56 | 88 | 144 | 176 | 208 | 256 | 344 |
| 2 | 32 | 72 | 144 | 176 | 208 | 256 | 328 | 424 |
| 3 | 40 | 104 | 176 | 208 | 256 | 328 | 440 | 568 |
| 4 | 56 | 120 | 208 | 256 | 328 | 408 | 552 | 680 |
| 5 | 72 | 144 | 224 | 328 | 424 | 504 | 680 | 872 |
| 6 | 88 | 176 | 256 | 392 | 504 | 600 | 808 | 1000 |
| 7 | 104 | 224 | 328 | 472 | 584 | 712 | 1000 | 1224 |
| 8 | 120 | 256 | 392 | 536 | 680 | 808 | 1096 | 1384 |
| 9 | 136 | 296 | 456 | 616 | 776 | 936 | 1256 | 1544 |
| 10 | 144 | 328 | 504 | 680 | 872 | 1000 | 1384 | 1736 |
| 11 | 176 | 376 | 584 | 776 | 1000 | 1192 | 1608 | 2024 |
| 12 | 208 | 440 | 680 | 1000 | 1128 | 1352 | 1800 | 2280 |
| 13 | 224 | 488 | 744 | 1032 | 1256 | 1544 | 2024 | 2536 |
| 14 | 256 | 552 | 840 | 1128 | 1416 | 1736 | 2280 |  |
| 15 | 280 | 600 | 904 | 1224 | 1544 | 1800 | 2472 |  |
| 16 | 328 | 632 | 968 | 1288 | 1608 | 1928 | 2536 |  |
| 17 | 336 | 696 | 1064 | 1416 | 1800 | 2152 |  |  |
| 18 | 376 | 776 | 1160 | 1544 | 1992 | 2344 |  |  |
| 19 | 408 | 840 | 1288 | 1736 | 2152 | 2536 |  |  |
| 20 | 440 | 904 | 1384 | 1864 | 2344 |  |  |  |
| 21 | 488 | 1000 | 1480 | 1992 | 2536 |  |  |  |

For a NPDCCH UE-specific search space, if the UE is configured with higher layer parameter twoHARQ-ProcessesConfig, or the UE is configured with higher layer parameter npusch-MultiTB-Config and single TB is scheduled in the corresponding DCI

- the NDI and HARQ process ID as signalled on NPDCCH, and the RV and TBS, as determined above, shall be delivered to higher layers,

otherwise

- the NDI as signalled on NPDCCH, and the RV and TBS, as determined above, shall be delivered to higher layers. If the UE is configured with higher layer parameter npusch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, HARQ process ID of 0 shall be assumed for the first TB and HARQ process ID of 1 shall be assumed for the second TB.

### 16.5.2 UE procedure for NPUSCH retransmission

For a NPUSCH retransmission, the UE shall follow the HARQ information in DCI as specified in [8].

### 16.5.3 UE procedure for transmitting SR

If the UE is configured with higher layer parameter sr-WithoutHARQ-ACK-Config, the UE is configured with Narrowband Random access channel parameters (NPRACH configuration) for SR transmission by higher layers.

The UE shall, if requested by higher layers for transmitting SR, start transmission of a narrowband random access preamble on the NB-IoT carrier configured in sr-NPRACH-Resource at the next available NPRACH resource, unless the transmission would overlap with any subframe(s) of NPDSCH reception. The narrowband preamble is transmitted on the allocated subcarrier and a number of NPRACH repetitions for the associated NPRACH repetition level as indicated by higher layers. The narrowband random access preamble is transmitted with transmission power as determined in clause 16.2.1.2, commencing on the indicated NPRACH resource.

## 16.6 Narrowband physical downlink control channel related procedures

Throughout this clause, if a NB-IoT UE is configured with higher layer parameter k-Mac, Kmac = k-Mac otherwise, Kmac = 0.

A UE shall monitor a set of NPDCCH candidates (described in Clause 10.2.5.1 of [3]) as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the NPDCCHs in the set according to all the monitored DCI formats.

The set of NPDCCH candidates to monitor are defined in terms of NPDCCH search spaces.

The UE shall monitor one or more of the following search spaces

- a Type1-NPDCCH common search space,

- a Type1A-NPDCCH common search space,

- a Type2-NPDCCH common search space,

- a Type2A-NPDCCH common search space, and

- a NPDCCH UE-specific search space.

A UE is not required to simultaneously monitor a NPDCCH UE-specific search space and a Type-1-NPDCCH common search space.

A UE is not required to simultaneously monitor a NPDCCH UE-specific search space and a Type2-NPDCCH common search space.

A UE is not required to simultaneously monitor a Type-1-NPDCCH common search space and a Type2-NPDCCH common search space.

A UE is not required to monitor Type1A-NPDCCH common search space or Type2A-NPDCCH common search space in subframes in which the UE monitors a Type1-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by P-RNTI

A UE is not required to monitor Type1A-NPDCCH common search space or Type2A-NPDCCH common search space in subframes in which the UE monitors a Type2-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by C-RNTI, CB-RNTI, or Temporary C-RNTI.

A UE is not required to monitor Type2A-NPDCCH common search space in the same subframe in which it monitors Type1A-NPDCCH common search space.

UE is not required to monitor Type1A-NPDCCH common search space in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI.

UE is not required to monitor Type2A-NPDCCH common search space in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by G-RNTI or SC-RNTI.

Until UE receives higher layer configuration of NPDCCH UE-specific search space, the UE monitors NPDCCH according to the same configuration of NPDCCH search space as that for NPDCCH scheduling Msg4.

A UE is not required to monitor Type1-NPDCCH common search space or NWUS if the set of subframes comprising the NPDCCH candidates or the set of subframes where NWUS may be received include any subframes in which the UE has initiated an NPUSCH transmission using preconfigured uplink resource on a given serving cell.

A UE is not required to monitor Type-1 NPDCCH common search space or NWUS in subframes in which the UE monitors a UE-specific NPDCCH search space given by PUR-RNTI.

An NPDCCH search space ![](media_svg/image542.svg) [公式≈: _{NS}_{k}(L&apos;,R)] at aggregation level ![](media_svg/image543.svg) [公式: L&apos;] (![](media_svg/image544.svg) [公式: L&apos;2=] for TDD special subframe, ![](media_svg/image545.svg) [公式: L&apos;⎰{1,2}] otherwise), and repetition level ![](media_svg/image546.svg) [公式: R⎰{1,2,4,8,16,32,64,128,256,512,1024,2048}] is defined by a set of NPDCCH candidates where each candidate is repeated in a set of ![](media_svg/image547.svg) [公式: R]consecutive NB-IoT downlink subframes excluding subframes used for transmission of SI messages starting with subframe ![](media_svg/image548.svg) [公式: k].

For NPDCCH UE-specific search space, the aggregation and repetition levels defining the search spaces and the corresponding NPDCCH candidates are listed in Table 16.6-1 by substituting the value of ![](media_svg/image549.svg) [公式≈: ^{R}max]with the higher layer configured parameter npdcch-NumRepetitions, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-NumRepetitions in PUR-Config-NB.

For Type1-NPDCCH common search space and Type1A-NPDCCH common search space, the aggregation and repetition levels defining the search spaces are listed in Table 16.6-2 by substituting the value of ![](media_svg/image550.svg) [公式≈: ^{R}max]

- with the higher layer configured parameter npdcch-NumRepetitionPaging for Type1-NPDCCH common search space;

- with the higher layer configured parameter npdcch-NumRepetitions-SC-MCCH for Type1A-NPDCCH common search space.

For Type2-NPDCCH common search space and Type2A-NPDCCH common search space, the aggregation and repetition levels defining the search spaces and the corresponding monitored NPDCCH candidates are listed in Table 16.6-3 by substituting the value of ![](media_svg/image551.svg) [公式≈: ^{R}max]

- with the higher layer configured parameter npdcch-NumRepetitions-RA for Type2-NPDCCH common search space;

- with the higher layer configured parameter npdcch-NumRepetitions-SC-MTCH for Type2A-NPDCCH common search space.

The locations of starting subframe ![](media_svg/image548.svg) [公式: k] are given by ![](media_svg/image552.svg) [公式: k=k_{b}]where ![](media_svg/image553.svg) [公式≈: ^{k}b]is the ![](media_svg/image554.svg) [公式: b]th consecutive NB-IoT DL subframe from subframe ![](media_svg/image555.svg) [公式: k0], excluding subframes used for transmission of SI messages, and ![](media_svg/image556.svg) [公式: b=u∪R], and ![](media_svg/image557.svg) [公式: u=0,1,κ^{R}_{R}^{max}−1], and where

- subframe ![](media_svg/image555.svg) [公式: k0] is a subframe satisfying the condition ![](media_svg/image558.svg) [公式≈: (102modnnTT_{fs}+=∪⋅∂_{√∃})⋅∂_{√∃}Α_{offset}], where ![](media_svg/image559.svg) [公式: TRG=∪_{max}], T≥4.

- for NPDCCH UE-specific search space,

- ![](media_svg/image560.svg) [公式: G]is given by the higher layer parameter npdcch-StartSF-USS, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-StartSF-USS in PUR-Config-NB,

- ![](media_svg/image561.svg) [公式≈: ^{Α}offset]is given by the higher layer parameter npdcch-Offset-USS, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-Offset-USS in PUR-Config-NB,

- for NPDCCH Type2-NPDCCH common search space,

- ![](media_svg/image560.svg) [公式: G]is given by the higher layer parameter npdcch-StartSF-CSS-RA,

- ![](media_svg/image561.svg) [公式≈: ^{Α}offset]is given by the higher layer parameter npdcch-Offset-RA,

- for NPDCCH Type2A-NPDCCH common search space,

- ![](media_svg/image560.svg) [公式: G]is given by the higher layer parameter npdcch-startSF-SC-MTCH,

- ![](media_svg/image561.svg) [公式≈: ^{Α}offset]is given by the higher layer parameter npdcch-Offset-SC-MTCH,

For Type1-NPDCCH common search space,![](media_svg/image562.svg) [公式: kk=0]and is determined from locations of NB-IoT paging opportunity subframes.

For Type1A-NPDCCH common search space, ![](media_svg/image562.svg) [公式: kk=0]and subframe ![](media_svg/image555.svg) [公式: k0] is a subframe satisfying the condition ![](media_svg/image558.svg) [公式≈: (102modnnTT_{fs}+=∪⋅∂_{√∃})⋅∂_{√∃}Α_{offset}], where ![](media_svg/image559.svg) [公式: TRG=∪_{max}], T≥4 and

- ![](media_svg/image560.svg) [公式: G]is given by the higher layer parameter npdcch-StartSF-SC-MCCH,

- ![](media_svg/image561.svg) [公式≈: ^{Α}offset]is given by the higher layer parameter npdcch-Offset-SC-MCCH.

For UE-specific search space by C-RNTI,

if the UE is configured by higher layers with a NB-IoT carrier for monitoring of NPDCCH UE-specific search space,

- the UE shall monitor the NPDCCH UE-specific search space on the higher layer configured NB-IoT carrier,

- the UE is not expected to receive NPSS, NSSS, NPBCH on the higher layer configured NB-IoT carrier.

otherwise,

- the UE shall monitor the NPDCCH UE-specific search space on the same NB-IoT carrier on which NPSS/NSSS/NPBCH are detected.

For UE-specific search space by PUR-RNTI, the UE is configured by the higher layer parameter carrierConfig in PUR-Config-NB with a NB-IoT carrier for monitoring of NPDCCH UE-specific search space,

- the UE shall monitor the NPDCCH UE-specific search space on the higher layer configured NB-IoT carrier,

- the UE is not expected to receive NPSS, NSSS, NPBCH on the higher layer configured NB-IoT carrier if the NB-IoT carrier is not the same as the NB-IoT carrier on which NPSS/NSSS/NPBCH are detected.

If the UE has initiated a NPUSCH transmission using preconfigured uplink resource ending in subframe n, the UE shall monitor the NPDCCH UE-specific search space in a search space window starting in subframe n+4+Kmac with duration given by higher layer parameter pur-ResponseWindowTimer. Upon detection of a NPDCCH with DCI format N0 with CRC scrambled by PUR-RNTI intended for the UE within the search space window and the value of "modulation and coding scheme" field () in the corresponding DCI is set to '14', the UE is not required to monitor the NPDCCH UE-specific search space for the remaining search space window duration.

Table 16.6-1: NPDCCH UE- specific search space candidates

| ![](media_svg/image563.svg) [公式≈: ^{R}max] | ![](media_svg/image547.svg) [公式: R] | DCI subframe repetition number | NCCE indices of monitored NPDCCH candidates |  |
| --- | --- | --- | --- | --- |
|  |  |  | L'=1 | L'=2 |
| 1 | 1 | 00 | {0},{1} | {0,1} |
| 2 | 1 | 00 | {0},{1} | {0,1} |
|  | 2 | 01 | - | {0,1} |
| 4 | 1 | 00 | - | {0,1} |
|  | 2 | 01 | - | {0,1} |
|  | 4 | 10 | - | {0,1} |
| >=8 | ![](media_svg/image564.svg) [公式: R_{max}/8] | 00 | - | {0,1} |
|  | ![](media_svg/image565.svg) [公式: R_{max}/4] | 01 | - | {0,1} |
|  | ![](media_svg/image566.svg) [公式: R_{max}/2] | 10 | - | {0,1} |
|  | ![](media_svg/image567.svg) [公式≈: ^{R}max] | 11 | - | {0,1} |
| Note 1: {x}, {y} denotes NPDCCH Format 0 candidate with NCCE index 'x', and NPDCCH Format 0 candidate with NCCE index 'y' are monitoredNote 2: {x,y} denotes NPDCCH Format1 candidate corresponding to NCCEs 'x' and 'y' is monitored. |  |  |  |  |

Table 16.6-2: Type 1/Type 1A - NPDCCH common search space candidates

|  |  |  |  |  |  |  |  |  | NCCE indices of monitored NPDCCH candidates |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | L'=1 | L'=2 |
| 1 | 1 | - | - | - | - | - | - | - | - | {0,1} |
| 2 | 1 | 2 | - | - | - | - | - | - | - | {0,1} |
| 4 | 1 | 2 | 4 | - | - | - | - | - | - | {0,1} |
| 8 | 1 | 2 | 4 | 8 | - | - | - | - | - | {0,1} |
| 16 | 1 | 2 | 4 | 8 | 16 | - | - | - | -- | {0,1} |
| 32 | 1 | 2 | 4 | 8 | 16 | 32 | - | - | - | {0,1} |
| 64 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | - | - | {0,1} |
| 128 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | - | {0,1} |
| 256 | 1 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | - | {0,1} |
| 512 | 1 | 4 | 16 | 32 | 64 | 128 | 256 | 512 | - | {0,1} |
| 1024 | 1 | 8 | 32 | 64 | 128 | 256 | 512 | 1024 | - | {0,1} |
| 2048 | 1 | 8 | 64 | 128 | 256 | 512 | 1024 | 2048 | - | {0,1} |
| DCI subframe repetition number | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |  |  |
| Note 1: {x,y} denotes NPDCCH Format1 candidate corresponding to NCCEs 'x' and 'y' is monitored. |  |  |  |  |  |  |  |  |  |  |

Table 16.6-3: Type 2/Type 2A - NPDCCH common search space candidates

| ![](media_svg/image563.svg) [公式≈: ^{R}max] | ![](media_svg/image547.svg) [公式: R] | DCI subframe repetition number | NCCE indices of monitored NPDCCH candidates |  |
| --- | --- | --- | --- | --- |
|  |  |  | L'=1 | L'=2 |
| 1 | 1 | 00 | - | {0,1} |
| 2 | 1 | 00 | - | {0,1} |
|  | 2 | 01 | - | {0,1} |
| 4 | 1 | 00 | - | {0,1} |
|  | 2 | 01 | - | {0,1} |
|  | 4 | 10 | - | {0,1} |
| >=8 | ![](media_svg/image564.svg) [公式: R_{max}/8] | 00 | - | {0,1} |
|  | ![](media_svg/image565.svg) [公式: R_{max}/4] | 01 | - | {0,1} |
|  | ![](media_svg/image566.svg) [公式: R_{max}/2] | 10 | - | {0,1} |
|  | ![](media_svg/image567.svg) [公式≈: ^{R}max] | 11 | - | {0,1} |
| Note 1: {x,y} denotes NPDCCH Format1 candidate corresponding to NCCEs 'x' and 'y' is monitored. |  |  |  |  |

For a NPDCCH UE-specific search space, if a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig or npusch-MultiTB-Config and if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n, and if the corresponding NPUSCH format 1 transmission starts from n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k,

- if the corresponding NPDCCH with DCI format N0 with CRC scrambled by C-RNTI schedules two transport blocks as determined by the Number of scheduled TB for Unicast field if present, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+1 to subframe n+k-1, otherwise the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+k-2 to subframe n+k-1; and

the UE does not expect to receive a DCI Format N0 before subframe n+k-2 for which the corresponding NPUSCH format 1 transmission ends later than subframe n+k+255 if the corresponding NPDCCH with DCI format N0 schedules one transport block.

- for TN TDD, and if the corresponding NPUSCH format1 transmission ends in subframe n+m, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

otherwise

- if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n or receives a NPDSCH carrying a random access response grant ending in subframe n, and if the corresponding NPUSCH format 1 transmission starts from n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

- for TN TDD, if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n or receives a NPDSCH carrying a random access response grant ending in subframe n, and if the corresponding NPUSCH format 1 transmission ends in n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k.

For a NPDCCH UE-specific search space, if a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig or npdsch-MultiTB-Config

- and if the NB-IoT UE detects NPDCCH with DCI Format N1 ending in subframe n, and if a NPDSCH transmission starts from n+k,

- if the corresponding NPDCCH with DCI format N1 with CRC scrambled by C-RNTI schedules two transport blocks as determined by the Number of scheduled TB for Unicast field if present, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+1 to subframe n+k-1;

- otherwise, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+k-2 to subframe n+k-1;

otherwise

- if the NB-IoT UE detects NPDCCH with DCI Format N1 or N2 ending in subframe n, and if the corresponding NPDSCH transmission starts from n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

If a NB-IoT UE detects NPDCCH with DCI Format N1 ending in subframe n, and if the corresponding NPDSCH transmission starts from n+k, and

- for FDD or IoT NTN TDD, if the corresponding NPUSCH format 2 transmission starts from subframe n+m or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+m, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

- for TN TDD, if the corresponding NPUSCH format 2 transmission ends in subframe n+m the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

If a NB-IoT UE detects NPDCCH with DCI Format N1 for "PDCCH order" ending in subframe n, and

- for FDD or IoT NTN TDD, if the corresponding NPRACH transmission starts from subframe n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

- for TN TDD, if the corresponding NPRACH transmission ends in subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

If a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig

- and if the UE has a NPUSCH transmission ending in subframe n,

- the UE is not required to receive transmissions in the Type B half-duplex guard periods as specified in [3]for FDD ; and

- the UE is not expected to receive an NPDCCH with DCI format N0/N1 for the same HARQ process ID as the NPUSCH transmission in any subframe starting from subframe n+1 to subframe n+3, or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n+1 to subframe n+Kmac+3 except if the UE is configured with higher layer parameter uplinkHARQ-mode set to ‘HARQModeB’ for the same HARQ process ID, or if the NPUSCH transmission carries ACK/NACK response, as determined in clause 16.4.2, for the same HARQ process ID associated with a transport block scheduled in a NPDCCH scheduling a single transport block, and the UE is configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for the same HARQ process ID and configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB;

else if the UE is not using higher layer parameter edt-Parameters or if the UE is using higher layer parameter edt-Parameters and ![](media_svg/image440.svg) [公式: 02≥≥I_{MCS}]

- if the NB-IoT UE has a NPUSCH transmission ending in subframe n,

- the UE is not required to receive transmissions in the Type B half-duplex guard periods as specified in [3] for FDD; and

- the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+3 or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n+1 to subframe n+Kmac+3 except if the UE is configured with higher layer parameter uplinkHARQ-mode set to ‘HARQModeB’, or if the NPUSCH transmission carries ACK/NACK response as determined in clause 16.4.2 and the UE is configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information and configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB.

otherwise,

- If the NB-IoT UE has a NPUSCH transmission for Msg3 ending in subframe $ n^{'}$ with transport block size![](media_svg/image442.svg) [公式≈: ^{TBS}Msg3] , whereas if ![](media_svg/image443.svg) [公式≈: ^{TBS}Msg3,max]would have been selected the NPUSCH transmission would have ended in subframe n, the UE is not required to monitor NPDCCH in any subframe starting from subframe n'+1 to subframe n+3 or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n'+1 to subframe n+Kmac+3.

If a NB-IoT UE receives a NPDSCH transmission ending in subframe n, and if the UE is not required to transmit a corresponding NPUSCH format 2, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+12.

If a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig

- the UE is not required to monitor an NPDCCH candidate of an NPDCCH search space if the candidate ends in subframe n, and if the UE is configured to monitor NPDCCH candidates of another NPDCCH search space having starting subframe k0 before subframe n+5

otherwise

- the UE is not required to monitor NPDCCH candidates of an NPDCCH search space if an NPDCCH candidate of the NPDCCH search space ends in subframe n, and if the UE is configured to monitor NPDCCH candidates of another NPDCCH search space having starting subframe k0 before subframe n+5.

An NB-IoT UE is not required to monitor NPDCCH candidates of an NPDCCH search space during an NPUSCH UL gap.

An NB-IoT UE is not required to monitor NPDCCH candidates of a Type2A-NPDCCH common search space during the scheduling gap or the processing gap.

For an NB-IoT UE configured with higher layer parameter sr-WithoutHARQ-ACK-Config, if the transmission of a narrowband random access preamble for SR ends on subframe n,

- in case of frame structure type 1 with NPRACH format 0 and 1 when the number of NPRACH repetitions is greater than or equal to 64, or NPRACH format 2 when the number of NPRACH repetitions is greater than or equal to 16, the UE is not required to monitor NPDCCH UE-specific search space from subframe n to subframe n+40 or in a NTN serving cell, in any downlink subframes that overlap with uplink subframe n to subframe n+Kmac+40,

- otherwise, the UE is not required to monitor NPDCCH UE-specific search space from subframe n to subframe n+3 or in a NTN serving cell, in any downlink subframes that overlap with uplink subframe n to subframe n+Kmac+3.

### 16.6.1 NPDCCH starting position

The starting OFDM symbol for NPDCCH given by index ![](media_svg/image570.svg) [公式≈: ^{l}NPDCCHStart] in the first slot in a subframe ![](media_svg/image475.svg) [公式: k] and is determined as follows

- if higher layer parameter eutraControlRegionSize is present

- if subframe ![](media_svg/image476.svg) [公式: k] is a special subframe for NPDCCH without repetition

- ![](media_svg/image571.svg) [公式≈: ^{ll}NPDCCHStartNDPCCHStart^{=}^{min2,}(^{&apos;})] where ![](media_svg/image572.svg) [公式≈: ^{l}NPDCCHStart^{&apos;}]is given by the higher layer parameter eutraControlRegionSize

- else ![](media_svg/image570.svg) [公式≈: ^{l}NPDCCHStart] is given by the higher layer parameter eutraControlRegionSize

otherwise

- ![](media_svg/image573.svg) [公式≈: ^{l}NPDCCHStart^{=}^{0}]

### 16.6.2 NPDCCH control information procedure

A UE shall discard the NPDCCH if consistent control information is not detected.

### 16.6.3 NPDCCH validation for semi-persistent scheduling

A UE shall validate a Semi-Persistent Scheduling assignment NPDCCH only if all the following conditions are met:

- the CRC parity bits obtained for the NPDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI

- the new data indicator field is set to '0'.

Validation is achieved if all the fields for the used DCI format N0 are set according to Table 16.6.3-1 or Table 16.6.3-2.

If validation is achieved, the UE shall consider the received DCI information accordingly as a valid semi-persistent activation or release.

If validation is not achieved, the received DCI format shall be considered by the UE as having been received with a non-matching CRC.

Table 16.6.3-1: Special fields for Semi-Persistent Scheduling Activation NPDCCH Validation

|  | DCI format N0 |
| --- | --- |
| HARQ process number (present if UE is configured with 2 uplink HARQ processes) | set to '0' |
| Redundancy version | set to '0' |
| Modulation and coding scheme | set to '0000' |
| Resource assignment | set to '000' |

Table 16.6.3-2: Special fields for Semi-Persistent Scheduling Release NPDCCH Validation

|  | DCI format N0 |
| --- | --- |
| HARQ process number (present if UE is configured with 2 uplink HARQ processes) | set to '0' |
| Redundancy version | set to '0' |
| Repetition number | set to '000' |
| Modulation and coding scheme | set to '1111' |
| Subcarrier indication | Set to all '1's |

### 16.6.4 Preconfigured uplink resource ACK/fallback procedure

If a UE has initiated a NPUSCH transmission using preconfigured uplink resource on a given serving cell, and upon detection of a NPDCCH with DCI format N0 with CRC scrambled by PUR-RNTI intended for the UE within the PUR search space window as defined in Clause 16.6, and the value of "modulation and coding scheme" field () in the corresponding DCI set to '14', the UE shall deliver the PUR ACK/fallback indication and the NPUSCH repetition adjustment, as signaled on the NPDCCH, to the higher layers.

## 16.7 Assumptions independent of physical channel related to narrowband IoT

A UE may assume the antenna ports 2000 – 2001 of a serving cell are quasi co-located (as defined in [3]) with respect to delay spread, Doppler spread, Doppler shift, average gain, and average delay.

## 16.8 UE procedure for acquiring cell-specific reference signal sequence and raster offset

If the higher layer parameter operationModeInfo indicates inband-SamePCI for a cell, the UE may derive cell-specific reference signal sequence and raster offset from the higher layer parameter eutra-CRS-SequenceInfo according to Table 16.8-1, where E-UTRA PRB index ![](media_svg/image574.svg) [公式≈: ^{n}PRB^{±}] is defined as ![](media_svg/image575.svg) [公式: nPRB±=nPRB−√NRB^{DL}/2∃].

Table 16.8-1: Definition of eutra-CRS-SequenceInfo

| eutra-CRS-SequenceInfo | E-UTRA PRB index ![](media_svg/image574.svg) [公式≈: ^{n}PRB^{±}]for odd number of ![](media_svg/image576.svg) [公式≈: _{N}_{RB}DL] | Raster offset | eutra-CRS-SequenceInfo | E-UTRA PRB index ![](media_svg/image574.svg) [公式≈: ^{n}PRB^{±}]for even number of ![](media_svg/image577.svg) [公式≈: _{N}_{RB}DL] | Raster offset |
| --- | --- | --- | --- | --- | --- |
| 0 | -35 | -7.5 kHz | 14 | -46 | +2.5 kHz |
| 1 | -30 |  | 15 | -41 |  |
| 2 | -25 |  | 16 | -36 |  |
| 3 | -20 |  | 17 | -31 |  |
| 4 | -15 |  | 18 | -26 |  |
| 5 | -10 |  | 19 | -21 |  |
| 6 | -5 |  | 20 | -16 |  |
| 7 | 5 | +7.5 kHz | 21 | -11 |  |
| 8 | 10 |  | 22 | -6 |  |
| 9 | 15 |  | 23 | 5 | -2.5 kHz |
| 10 | 20 |  | 24 | 10 |  |
| 11 | 25 |  | 25 | 15 |  |
| 12 | 30 |  | 26 | 20 |  |
| 13 | 35 |  | 27 | 25 |  |
|  |  |  | 28 | 30 |  |
|  |  |  | 29 | 35 |  |
|  |  |  | 30 | 40 |  |
|  |  |  | 31 | 45 |  |

## 16.9 UE procedure for receiving narrowband wake up signal

A NB-IoT UE can be configured with up to two NWUS [14]. A UE may assume that no more than one NWUS sequence is transmitted per NWUS resource at a given time.

A NB-IoT UE using NWUS can assume the actual duration of NWUS is one of the values in the set listed in Table 16.9-1 corresponding to the maximum duration of NWUS, $ L_{NWUS\_max}$, configured by higher layers. There is a total of $ L_{NWUS\_max}$ NB-IoT DL subframes and subframes #4 carrying SystemInformationBlockType1-NB in the maximum duration of NWUS. The NWUS starts in subframe w0, where w0 is the latest subframe such that there is a total of ![](media_svg/image578.svg) [公式≈: (^{NL}IDNWUS_max^{resource}^{+}^{1})] NB-IoT DL subframes and subframes #4 carrying SystemInformationBlockType1-NB in the duration that ends in subframe (g0-1), where g0 is defined by [14] and $ N_{ID}^{resource}$ is the NWUS resource that the UE is associated to as defined in [3]. The UE may assume that NWUS and its associated NB-IoT paging occasion subframes are on the same NB-IoT carrier.

Table 16.9-1: Actual NWUS durations in NB-IoT DL subframes or subframes containing SystemInformationBlockType1-NB.

| $ L_{NWUS\_max}$ | Actual NWUS durations set |
| --- | --- |
| 1 | {1} |
| 2 | {1, 2} |
| 4 | {1, 2, 4} |
| 8 | {1, 2, 4, 8} |
| 16 | {1, 2, 4, 8, 16} |
| 32 | {1, 2, 4, 8, 16, 32} |
| 64 | {1, 2, 4, 8, 16, 32, 64} |
| 128 | {1, 2, 4, 8, 16, 32, 64, 128} |
| 256 | {1, 2, 4, 8, 16, 32, 64, 128, 256} |
| 512 | {1, 2, 4, 8, 16, 32, 64, 128, 256, 512} |
| 1024 | {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024} |

A NB-IoT UE using NWUS can assume there are at least 10 NB-IoT DL subframes between the end of the maximum duration of NWUS and the first associated NB-IoT paging occasion subframe.

## 16.10 GNSS measurement gap related procedures

For a NB-IoT UE in a NTN serving cell, when the UE receives a GNSS Measurement Command MAC CE in a NPDSCH ending in DL subframe n,

- if the UE shall not provide HARQ-ACK information for the HARQ process associated with the transport block in the NPDSCH carrying GNSS Measurement Command MAC CE,

- the UE shall assume the start of the measurement gap in subframe n+13

- otherwise,

- the UE shall assume the start of the measurement gap in subframe k+2, where k is the first DL subframe after the end of the transmission of the NPUSCH carrying ACK/NACK response for the HARQ process associated with the transport block in the NPDSCH.

For a NB-IoT UE in a NTN serving cell, the UE is not required to monitor NPDCCH within the GNSS measurement gap duration, until it reacquires GNSS position and a contention based Random Access is performed as specified in TS 36.321 [8].

# 17 Wake-up signal related procedures for BL/CE UE

A BL/CE UE can be configured with up to two MWUS [14]. A UE may assume that no more than one MWUS sequence is transmitted per MWUS resource at a given time.

A BL/CE UE using MWUS can assume the actual duration of MWUS is one of the values in the set listed in Table 17-1 corresponding to the maximum duration of MWUS, $ L_{MWUS\_max}$, configured by higher layers. There is a total of $ L_{MWUS\_max}$ BL/CE DL subframes in the maximum duration of MWUS. The MWUS starts in subframe w0, where w0 is the latest subframe such that there is a total of $ k\cdot  L_{MWUS\_max}$ BL/CE DL subframes in the duration that ends in subframe (g0-1), where g0 is defined by [14], $ k=1 $ if FDM-only MWUS resource configuration [14], $ k=\lceil  \frac {N_{ID}^{resource}+1}{2}\rceil  $ otherwise, and $ N_{ID}^{resource}$ is the MWUS resource that the UE is associated to as defined in [3]. The UE may assume that MWUS and its first associated paging occasion subframes are in the same narrowband. In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layer fdd-DownlinkOrTddSubframeBitmapBR, are not counted in maximum duration and actual duration of MWUS.

Table 17-1: Actual MWUS durations in BL/CE DL subframes.

| $ L_{MWUS\_max}$ | Actual MWUS durations set |
| --- | --- |
| 1 | {1} |
| 2 | {1, 2} |
| 4 | {1, 2, 4} |
| 8 | {1, 2, 4, 8} |
| 16 | {1, 2, 4, 8, 16} |
| 32 | {1, 2, 4, 8, 16, 32} |
| 64 | {1, 2, 4, 8, 16, 32, 64} |

# 18 GNSS measurement gap related procedures for BL/CE UE

For a BL/CE UE in a NTN FDD serving cell, when the UE receives a GNSS Measurement Command MAC CE in a PDSCH ending in DL subframe n,

- if the UE shall not provide HARQ-ACK information for the HARQ process associated with the transport block in the PDSCH carrying GNSS Measurement Command MAC CE,

- the UE shall assume the start of the measurement gap in subframe n+6

- otherwise,

- the UE shall assume the start of the measurement gap in subframe k+2, where k is the first DL subframe after the end of the HARQ-ACK transmission for the HARQ process associated with the transport block in the PDSCH.

For a BL/CE UE in a NTN FDD serving cell, the UE is not required to monitor MPDCCH within the GNSS measurement gap duration, until it reacquires GNSS position and a contention based Random Access is performed as specified in TS 36.321 [8].
