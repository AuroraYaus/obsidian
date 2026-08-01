# 9 Sidelink

## 9.1 Overview

A sidelink is used for ProSe direct communication and ProSe direct discovery between UEs.

### 9.1.1 Physical channels

A sidelink physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS 36.212 [3] and the present document TS36.211. The following sidelink physical channels are defined:

- Physical Sidelink Shared Channel, PSSCH

- Physical Sidelink Control Channel, PSCCH

- Physical Sidelink Discovery Channel, PSDCH

- Physical Sidelink Broadcast Channel, PSBCH

Generation of the baseband signal representing the different physical sidelink channels is illustrated in Figrue 5.3-1.

### 9.1.2 Physical signals

A sidelink physical signal is used by the physical layer but does not carry information originating from higher layers. The following sidelink physical signals are defined:

- Demodulation reference signal

- Synchronization signal

### 9.1.3 Handling of simultaneous sidelink and uplink/downlink transmissions

For a given frequency, on an uplink subframe included in discTxGapConfig [9], a UE shall not transmit an uplink transmission that is not a PRACH transmission and that is partly or completely overlapping in time with a PSDCH transmission or a SLSS transmission for PSDCH by the same UE. Else, for a given carrier frequency and sidelink transmission mode 1 or 2 or sidelink discovery, a UE shall not transmit a sidelink signal or channel overlapping partly or completely in time with an uplink transmission from the same UE.

For a given carrier frequency, no PSDCH, PSCCH, or PSSCH transmission shall occur from a UE in a sidelink subframe configured for synchronization purposes by the higher-layer parameters

- syncOffsetIndicator1 or syncOffsetIndicator2 in [9] if the UE has no serving cell fulfilling the S criterion according to [10, clause 5.2.3.2], or

- syncOffsetIndicator in commSyncConfig or discSyncConfig which includes txParameters in [9] if the UE has a serving cell fulfilling the S criterion according to [10, clause 5.2.3.2]. The UE may assume the same configuration in commSyncConfig and discSyncConfig.

For a given carrier frequency, with the exception of PSSCH transmissions with transmission mode 1 and same sidelink cyclic prefix as PUSCH, no sidelink transmissions shall occur in sidelink subframe ![](media_svg/image1.svg) [公式: n] from a UE if uplink SRS is transmitted from the same UE in uplink subframe ![](media_svg/image1.svg) [公式: n].

A UE with limited transmission capabilities, on an uplink subframe included in discTxGapConfig [9], shall first prioritize a PSDCH transmission or a SLSS transmission for PSDCH over an uplink transmission that is not a PRACH transmission. Else, a UE with limited transmission capabilities shall at a given time first prioritize uplink transmissions, followed by sidelink transmission mode 1 or 2 or sidelink discovery.

A UE with limited transmission capabilities shall at a given time prioritize sidelink communication transmissions (PSSS, SSSS, PSBCH, PSSCH, PSCCH) over sidelink discovery transmissions (PSDCH).

A UE with limited reception capabilities, on a downlink subframe included in discRxGapConfig [9], shall first prioritize reception of PSDCH or 11reception of SLSS for PSDCH over downlink reception. Else, a UE with limited reception capabilities shall at a given time first prioritize downlink reception over sidelink reception.

A UE with limited reception capabilities shall at a given time first prioritize sidelink communication reception, sidelink discovery reception on carriers configured by the eNodeB, and last sidelink discovery reception on carriers not configured by the eNodeB.

## 9.2 Slot structure and physical resources

Sidelink transmissions are organized into radio frames with a duration of ![](media_svg/image2.svg) [公式≈: ^{T}f], each consisting of 20 slots of duration ![](media_svg/image3.svg) [公式≈: ^{T}slot]. A sidelink subframe consists of two consecutive slots, starting with an even-numbered slot.

### 9.2.1 Resource grid

A transmitted physical channel or signal in a slot is described by a resource grid of ![](media_svg/image4.svg) [公式≈: _{N}_{RB}SL_{N}_{sc}RB] subcarriers and ![](media_svg/image5.svg) [公式≈: ^{N}symb^{SL}] SC-FDMA symbols. The sidelink bandwidth ![](media_svg/image6.svg) [公式≈: _{N}_{RB}SL_{=}_{N}_{RB}UL] if the S criterion according to [10, clause 5.2.3.2] is fulfilled for a serving cell having the same uplink carrier frequency as the sidelink, otherwise a preconfigured value is used [9].

The sidelink cyclic prefix is configured independently for type 1 discovery, type 2B discovery, sidelink transmission mode 1, sidelink transmission mode 2, control signalling, and PSBCH and synchronization signals. Configuration is per resource pool for discovery, sidelink transmission mode 2, and control signalling. The PSBCH and synchronization signals always use the same cyclic prefix.

Only normal cyclic prefix is supported for PSSCH, PSCCH, PSBCH, and synchronization signals for a sidelink configured with transmission mode 3 or 4.

The resource grid is illustrated in Figure 5.2.1-1.

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed. There is one resource grid per antenna port. The antenna ports used for transmission of a physical channel or signal are shown in Table 9.2.1-1.

Table 9.2.1-1: Antenna ports used for different physical channels and signals

| Physical channel or signal | Antenna port number |
| --- | --- |
| PSSCH | 1000 |
| PSCCH | 1000 |
| PSDCH | 1000 |
| PSBCH | 1010 |
| Synchronization signals | 1020 |

### 9.2.2 Resource elements

Each element in the resource grid is called a resource element and is uniquely defined by the index pair ![](media_svg/image7.svg) [公式: (k,l)] in a slot where ![](media_svg/image8.svg) [公式≈: k=0,...,N_{RB}^{SL}N_{sc}^{RB}−1] and ![](media_svg/image9.svg) [公式≈: l=0,...,N_{symb}^{SL}−1] are the indices in the frequency and time domains, respectively. Resource element ![](media_svg/image7.svg) [公式: (k,l)] on antenna port ![](media_svg/image10.svg) [公式: p] corresponds to the complex value ![](media_svg/image11.svg) [公式≈: _{a}_{k}(_{,}p_{l})]. When there is no risk for confusion, or no particular antenna port is specified, the index ![](media_svg/image10.svg) [公式: p] may be dropped.

Quantities ![](media_svg/image11.svg) [公式≈: _{a}_{k}(_{,}p_{l})] corresponding to resource elements not used for transmission of a physical channel or a physical signal in a slot shall be set to zero.

### 9.2.3 Resource blocks

A physical resource block is defined as ![](media_svg/image12.svg) [公式≈: ^{N}symb^{SL}]consecutive SC-FDMA symbols in the time domain and ![](media_svg/image13.svg) [公式≈: _{N}_{sc}RB]consecutive subcarriers in the frequency domain, where ![](media_svg/image14.svg) [公式≈: ^{N}symb^{SL}] and ![](media_svg/image13.svg) [公式≈: _{N}_{sc}RB] are given by Table 9.2.3-1. A physical resource block in the sidelink thus consists of ![](media_svg/image15.svg) [公式≈: ^{N}symb^{SL}^{≠}^{N}sc^{RB}] resource elements, corresponding to one slot in the time domain and 180 kHz in the frequency domain.

Table 9.2.3-1: Resource block parameters

| Configuration | ![](media_svg/image16.svg) [公式≈: _{N}_{sc}RB] | ![](media_svg/image17.svg) [公式≈: ^{N}symb^{SL}] |
| --- | --- | --- |
| Normal cyclic prefix | 12 | 7 |
| Extended cyclic prefix | 12 | 6 |

The relation between the physical resource block number ![](media_svg/image18.svg) [公式≈: ^{n}PRB] in the frequency domain and resource elements ![](media_svg/image19.svg) [公式: (k,l)] in a slot is given by

![](media_svg/image20.svg) [公式≈: ^{n}^{PRB}^{=}^{⋅}^{⋅}⋅√N^{k}sc^{RB}^{∂}^{∂}∂∃]

### 9.2.4 Resource pool

The subframe pools and resource block pools are defined in [4].

For PSSCH, the number of the current slot in the subframe pool ![](media_svg/image21.svg) [公式≈: _{n}_{ss}PSSCH_{=}_{2}_{n}_{ssf}PSSCH_{+}_{i}], where ![](media_svg/image22.svg) [公式: i⎰{0,1}] is the number of the current slot within the current sidelink subframe ![](media_svg/image23.svg) [公式≈: n_{ssf}^{PSSCH}=jmod10] with ![](media_svg/image24.svg) [公式: j] equal to the subscript of ![](media_svg/image25.svg) [公式≈: _{l}PSSCH_{j}], defined in clauses 14.1.4 and 14.2.3 of [4] for sidelink transmission modes 1 and 2, respectively; and where  is the number of the current slot within the current sidelink subframe ![](media_svg/image27.svg) [公式≈: n_{ssf}^{PSSCH}=kmod10] with ![](media_svg/image28.svg) [公式: k] equal to the subscript of ![](media_svg/image29.svg) [公式≈: _{t}_{k}SL], defined in clauses 14.1.1.5 of [4] for sidelink transmission modes 3 and 4.

### 9.2.5 Guard period

The last SC-FDMA symbol in a sidelink subframe serves as a guard period and shall not be used for sidelink transmission.

## 9.3 Physical Sidelink Shared Channel

### 9.3.1 Scrambling

The block of bits ![](media_svg/image30.svg) [公式: b(0),...,b(M_{bit}−1)], where ![](media_svg/image31.svg) [公式≈: ^{M}bit] is the number of bits transmitted on the physical sidelink shared channel in one subframe shall be scrambled according to clause 5.3.1.

The scrambling sequence generator shall be initialised with ![](media_svg/image32.svg) [公式≈: c_{init}=n_{ID}^{X}∪2^{14}+n_{ssf}^{PSSCH}∪2^{9}+510] at the start of every PSSCH subframe where

- for sidelink transmission modes 1 and 2, ![](media_svg/image33.svg) [公式≈: ^{n}ID^{X}^{=}^{n}ID^{SA}] is destination identity obtained from the sidelink control channel, and

- for sidelink transmission modes 3 and 4, ![](media_svg/image34.svg) [公式≈: _{n}_{ID}X_{=}_{⊆}_{i}^{L}_{=}^{−}_{0}^{1}_{p}_{i}_{∪}_{2}L−1−i] with ![](media_svg/image35.svg) [公式: p] and ![](media_svg/image36.svg) [公式: L] given by clause 5.1.1 in [3] equals the decimal representation of CRC on the PSCCH transmitted in the same subframe as the PSSCH.

### 9.3.2 Modulation

Modulation shall be done according to clause 5.3.2. Table 9.3.2-1 specifies the modulation mappings applicable for the physical sidelink shared channel.

Table 9.3.2-1: PSSCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PSSCH | QPSK, 16QAM, 64QAM |

### 9.3.3 Layer mapping

Layer mapping shall be done according to clause 5.3.2A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.3.4 Transform precoding

Transform precoding shall be done according to clause 5.3.3 with ![](media_svg/image38.svg) [公式≈: _{M}_{RB}PUSCH] and ![](media_svg/image39.svg) [公式≈: _{M}_{sc}PUSCH] replaced by ![](media_svg/image40.svg) [公式≈: _{M}_{RB}PSSCH] and ![](media_svg/image41.svg) [公式≈: _{M}_{sc}PSSCH], respectively.

### 9.3.5 Precoding

Precoding shall be done according to clause 5.3.3A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.3.6 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image42.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image43.svg) [公式≈: ^{Β}PSSCH] in order to conform to the transmit power ![](media_svg/image44.svg) [公式≈: ^{P}PSSCH] specified in [4], and mapped in sequence starting with ![](media_svg/image45.svg) [公式: z(0)] to physical resource blocks on antenna port ![](media_svg/image46.svg) [公式: p] and assigned for transmission of PSSCH. The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] corresponding to the physical resource blocks assigned for transmission and not used for transmission of reference signals shall be in increasing order of first the index ![](media_svg/image48.svg) [公式: k], then the index![](media_svg/image49.svg) [公式: l], starting with the first slot in the subframe. If Transmission Format of SCI format 1 is set to 1, the resource elements in the last SC-FDMA symbol within a subframe shall not considered in the mapping process. Otherwise, the resource elements in the last SC-FDMA symbol within a subframe shall be counted in the mapping process but not transmitted.

If sidelink frequency hopping is disabled the set of physical resource blocks to be used for transmission is given by ![](media_svg/image50.svg) [公式≈: ^{n}PRB^{=}^{n}VRB^{±}] where ![](media_svg/image51.svg) [公式≈: ^{n}VRB^{±}] is obtained from [4, clause 14.1.1.2.1].

If sidelink frequency hopping with type 1 hopping is enabled, the set of physical resource blocks to be used for transmission is given by [4].

If sidelink frequency hopping with predefined hopping pattern is enabled, the set of physical resource blocks to be used for transmission is given by the sidelink control information together with a predefined pattern in clause 5.3.4 with the following exceptions:

- only inter-subframe hopping shall be used

- the number of subbands ![](media_svg/image52.svg) [公式: N_{sb}⎰{1,2,4}] is given by higher layers as described in [4, clause 14.1.1.2]

- the quantity ![](media_svg/image53.svg) [公式: N_{RB}^{HO}⎰{0,...,110}] is given by higher layers as described in [4, clause 14.1.1.2]

- the quantity ![](media_svg/image54.svg) [公式≈: _{n}_{s}_{=}_{n}_{ss}PSSCH] where ![](media_svg/image55.svg) [公式≈: _{n}_{ss}PSSCH] is given by clause 9.2.4

- the quantity ![](media_svg/image56.svg) [公式≈: CURRENT_TX_NB=n_{ssf}^{PSSCH}]

- the pseudo-random sequence generator is initialized at the start of each slot fulfilling ![](media_svg/image57.svg) [公式≈: _{n}_{ss}PSSCH_{=}_{0}] with the initialization value ![](media_svg/image58.svg) [公式≈: c_{init}⎰{0,1,...,503,510}] given by hoppingParameter-r12 in [9]

- the quantity ![](media_svg/image59.svg) [公式≈: ^{n}VRB] shall be replaced by ![](media_svg/image60.svg) [公式≈: ^{n}VRB^{±}], given by [4, clause 14.1.1.2.1]

- for sidelink transmission mode 1

- ![](media_svg/image61.svg) [公式≈: _{N}_{RB}UL_{=}_{N}_{RB}SL]

- for sidelink transmission mode 2

- ![](media_svg/image62.svg) [公式≈: _{N}_{RB}UL_{=}_{M}_{RB}PSSCH_RP] where ![](media_svg/image63.svg) [公式≈: _{M}_{RB}PSSCH_RP] is given by [4, clause 14.1.3]

- the quantity ![](media_svg/image64.svg) [公式≈: ^{n}PRB] shall be replaced by ![](media_svg/image65.svg) [公式≈: ^{n}PRB^{±}], given by [4, clause 14.1.1.4]

- the physical resource block to use for transmission ![](media_svg/image66.svg) [公式≈: _{n}_{PRB}_{=}_{m}_{n}PSSCH_{±}_{PRB}] with ![](media_svg/image67.svg) [公式≈: _{m}PSSCH_{j}] given by [4, clause 14.1.3]

## 9.4 Physical Sidelink Control Channel

### 9.4.1 Scrambling

The block of bits ![](media_svg/image30.svg) [公式: b(0),...,b(M_{bit}−1)], where ![](media_svg/image31.svg) [公式≈: ^{M}bit] is the number of bits transmitted on the physical sidelink control channel in one subframe shall be scrambled according to clause 5.3.1.

The scrambling sequence generator shall be initialised with ![](media_svg/image68.svg) [公式≈: c_{init}=510] at the start of every PSCCH subframe.

### 9.4.2 Modulation

Modulation shall be done according to clause 5.3.2. Table 9.4.2-1 specifies the modulation mappings applicable for the physical sidelink control channel.

Table 9.4.2-1: PSCCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PSCCH | QPSK |

### 9.4.3 Layer mapping

Layer mapping shall be done according to clause 5.3.2A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.4.4 Transform precoding

Transform precoding shall be done according to clause 5.3.3 with ![](media_svg/image38.svg) [公式≈: _{M}_{RB}PUSCH] and ![](media_svg/image39.svg) [公式≈: _{M}_{sc}PUSCH] replaced by ![](media_svg/image69.svg) [公式≈: _{M}_{RB}PSCCH] and ![](media_svg/image70.svg) [公式≈: _{M}_{sc}PSCCH], respectively.

### 9.4.5 Precoding

Precoding shall be done according to clause 5.3.3A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.4.6 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image42.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image71.svg) [公式≈: ^{Β}PSCCH] in order to conform to the transmit power ![](media_svg/image72.svg) [公式≈: ^{P}PSCCH] specified in [4], and mapped in sequence starting with ![](media_svg/image45.svg) [公式: z(0)] to physical resource blocks on antenna port ![](media_svg/image46.svg) [公式: p] and assigned for transmission of PSCCH. The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] corresponding to the physical resource blocks assigned for transmission and not used for transmission of reference signals shall be in increasing order of first the index ![](media_svg/image48.svg) [公式: k], then the index![](media_svg/image49.svg) [公式: l], starting with the first slot in the subframe. Resource elements in the last SC-FDMA symbol within a subframe shall be counted in the mapping process but not transmitted.

## 9.5 Physical Sidelink Discovery Channel

### 9.5.1 Scrambling

The block of bits ![](media_svg/image30.svg) [公式: b(0),...,b(M_{bit}−1)], where ![](media_svg/image31.svg) [公式≈: ^{M}bit] is the number of bits transmitted on the physical sidelink discovery channel in one subframe shall be scrambled according to clause 5.3.1.

The scrambling sequence generator shall be initialised with ![](media_svg/image73.svg) [公式≈: c_{init}=510] at the start of each PSDCH subframe.

### 9.5.2 Modulation

Modulation shall be done according to clause 5.3.2. Table 9.5.2-1 specifies the modulation mappings applicable for the physical sidelink discovery channel.

Table 9.5.2-1: Sidelink modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PSDCH | QPSK |

### 9.5.3 Layer mapping

Layer mapping shall be done according to clause 5.3.2A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.5.4 Transform precoding

Transform precoding shall be done according to clause 5.3.3 with ![](media_svg/image38.svg) [公式≈: _{M}_{RB}PUSCH] and ![](media_svg/image39.svg) [公式≈: _{M}_{sc}PUSCH] replaced by ![](media_svg/image74.svg) [公式≈: _{M}_{RB}PSDCH] and ![](media_svg/image75.svg) [公式≈: _{M}_{sc}PSDCH], respectively.

### 9.5.5 Precoding

Precoding shall be done according to clause 5.3.3A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.5.6 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image42.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image76.svg) [公式≈: ^{Β}PSDCH] in order to conform to the transmit power ![](media_svg/image77.svg) [公式≈: ^{P}PSDCH] specified in [4], and mapped in sequence starting with ![](media_svg/image45.svg) [公式: z(0)] to physical resource blocks on antenna port ![](media_svg/image46.svg) [公式: p] and assigned for transmission of PSDCH. The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] corresponding to the physical resource blocks assigned for transmission and not used for transmission of reference signals shall be in increasing order of first the index ![](media_svg/image48.svg) [公式: k], then the index![](media_svg/image49.svg) [公式: l], starting with the first slot in the subframe. Resource elements in the last SC-FDMA symbol within a subframe shall be counted in the mapping process but not transmitted.

The set of physical resource blocks that shall be used are given by [4, clause 14.3.1].

## 9.6 Physical Sidelink Broadcast Channel

### 9.6.1 Scrambling

The block of bits ![](media_svg/image30.svg) [公式: b(0),...,b(M_{bit}−1)], where ![](media_svg/image31.svg) [公式≈: ^{M}bit] is the number of bits transmitted on the physical sidelink broadcast channel in one subframe, shall be scrambled according to clause 5.3.1. The scrambling sequence generator shall be initialised at the start of every PSBCH subframe with ![](media_svg/image78.svg) [公式≈: ^{c}init^{=}^{N}ID^{SL}].

### 9.6.2 Modulation

Modulation shall be done according to clause 5.3.2. Table 9.6.2-1 specifies the modulation mappings applicable for the physical sidelink broadcast channel.

Table 9.6.2-1: PSBCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PSBCH | QPSK |

### 9.6.3 Layer mapping

Layer mapping shal be done according to clause 5.3.2A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.6.4 Transform precoding

Transform precoding shall be done according to clause 5.3.3 with ![](media_svg/image38.svg) [公式≈: _{M}_{RB}PUSCH] and ![](media_svg/image39.svg) [公式≈: _{M}_{sc}PUSCH] replaced by ![](media_svg/image79.svg) [公式≈: _{M}_{RB}PSBCH] and ![](media_svg/image80.svg) [公式≈: _{M}_{sc}PSBCH], respectively.

### 9.6.5 Precoding

Precoding shall be done according to clause 5.3.3A assuming a single antenna port, ![](media_svg/image37.svg) [公式: Υ=1].

### 9.6.6 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image42.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image81.svg) [公式≈: ^{Β}PSBCH] in order to conform to the transmit power ![](media_svg/image82.svg) [公式≈: ^{P}PSBCH] specified in [4], and mapped in sequence starting with ![](media_svg/image45.svg) [公式: z(0)] to physical resource blocks on antenna port ![](media_svg/image46.svg) [公式: p]. The PSBCH shall use the same set of resource blocks as the synchronization signal. The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] corresponding to the physical resource blocks used for the PSBCH and not used for transmission of reference signals or synchronization signals shall be in increasing order of first the index ![](media_svg/image48.svg) [公式: k], then the index ![](media_svg/image49.svg) [公式: l], starting with the first slot in the subframe. The resource-element index ![](media_svg/image48.svg) [公式: k] given by

![](media_svg/image83.svg) [公式≈: k=k±−36+^{N}^{RB}^{SL}_{2}^{N}^{sc}^{RB},k±=0,1,...,71]

Resource elements in the last SC-FDMA symbol within a subframe should be counted in the mapping process but not transmitted.

## 9.7 Sidelink Synchronization Signals

A physical-layer sidelink synchronization identity is represented by ![](media_svg/image84.svg) [公式: N_{ID}^{SL}⎰{0,1,...,335}], divided into two sets id_net and id_oon consisting of identities ![](media_svg/image85.svg) [公式: {0,1,...,167}] and ![](media_svg/image86.svg) [公式: {168,169,...,335}], respectively.

### 9.7.1 Primary sidelink synchronization signal

The primary sidelink synchronization signal is transmitted in two adjacent SC-FDMA symbols in the same subframe.

#### 9.7.1.1 Sequence generation

Each of the two sequences ![](media_svg/image87.svg) [公式: d_{i}(0),...,d_{i}(61),i=1,2] used for the primary sidelink synchronization signal in the two SC-FDMA symbols is given by clause 6.11.1.1 with root index ![](media_svg/image88.svg) [公式: u=26] if ![](media_svg/image89.svg) [公式: N_{ID}^{SL}≥167] and ![](media_svg/image90.svg) [公式: u=37] otherwise.

#### 9.7.1.2 Mapping to resource elements

The sequence ![](media_svg/image91.svg) [公式: d_{i}(n)] shall be multiplied with the amplitude scaling factor ![](media_svg/image92.svg) [公式≈: 7262∪Β_{PSBCH}] and mapped to resource elements on antenna port 1020 in the first slot in the subframe according to

![](media_svg/image93.svg) [公式≈: ^{a}^{k}^{,}^{k}^{l}^{l}^{=}^{=}^{=}^{d}^{n}^{√}^{⌠}_{∞}^{1}0^{i}^{−}^{,}^{(},^{2}1^{n}^{31}^{)}^{,}^{+}extended^{normal}^{N}^{RB}^{SL}^{n}^{2}^{N}^{=}^{cyclic}^{sc}^{RB}^{0}cyclic^{,...,}^{61}^{prefix}prefix]

### 9.7.2 Secondary sidelink synchronization signal

The secondary sidelink synchronization signal is transmitted in two adjacent SC-FDMA symbols in the same subframe.

#### 9.7.2.1 Sequence generation

Each of the two sequences ![](media_svg/image94.svg) [公式: d_{i}(0),...,d_{i}(61),i=1,2] used for the secondary sidelink synchronization signal is given by clause 6.11.2.1 assuming

- subframe 0 with ![](media_svg/image95.svg) [公式≈: N_{ID}^{(1)}=N_{ID}^{SL}mod168] and ![](media_svg/image96.svg) [公式≈: NID^{(2)}=√NID^{SL}168∃] for transmission modes 1 and 2, and

- subframe 5 for transmission modes 3 and 4.

#### 9.7.2.2 Mapping to resource elements

The sequence ![](media_svg/image91.svg) [公式: d_{i}(n)] shall be multiplied with the amplitude scaling factor ![](media_svg/image97.svg) [公式≈: ^{Β}SSSS] in order to conform to the transmit power specified in clause 14.4 in TS 36.213 [4] and mapped to resource elements on antenna port 1020 in the second slot in the subframe according to

![](media_svg/image98.svg) [公式≈: ^{a}^{k}^{,}^{k}^{l}^{l}^{=}^{=}^{=}^{d}^{n}^{√}^{⌠}_{∞}3^{4}^{i}^{−}^{(},^{,}4^{n}^{5}^{31}^{)}^{,}^{+}extended^{normal}^{N}^{RB}^{SL}^{n}^{2}^{N}^{=}^{cyclic}^{sc}^{RB}^{0}cyclic^{,...,}^{61}^{prefix}prefix]

## 9.8 Demodulation reference signals

Demodulation reference signals associated with PSSCH, PSCCH, PSDCH, and PSBCH transmission shall be transmitted according to PUSCH in clause 5.5.2.1 with the following exceptions:

- The parameters in Tables 9.8-1, 9.8-2, and 9.8-3 shall be used.

- The term PUSCH shall be replaced by PSSCH, PSCCH, PSDCH or PSBCH, depending on the physical channel to which the reference signal is associated.

- Antenna ports are given by Table 9.2-1.

- The set of physical resource blocks used in the mapping process shall be identical to the corresponding PSSCH/PSCCH/PSDCH/PSBCH transmission.

- The index ![](media_svg/image99.svg) [公式: k] in the mapping process in clause 5.5.2.1.2 corresponding to the case where higher-layer parameter ul-DMRS-IFDMA is not set shall be identical to that for the corresponding PSSCH/PSCCH/PSDCH/PSBCH transmission.

- For sidelink transmission modes 3 and 4 on the PSSCH and PSCCH, the mapping shall use ![](media_svg/image100.svg) [公式: l=2] and ![](media_svg/image101.svg) [公式: l=5] for the first slot in the subframe and ![](media_svg/image102.svg) [公式: l=1] and ![](media_svg/image103.svg) [公式: l=4] for the second slot in the subframe.

- For sidelink transmission modes 3 and 4 on the PSBCH, the mapping shall use ![](media_svg/image104.svg) [公式: l=4] and ![](media_svg/image105.svg) [公式: l=6] for the first slot in the subframe and ![](media_svg/image106.svg) [公式: l=2] for the second slot in the subframe.

- For sidelink transmission modes 1 and 2, the pseudo-random sequence generator in clause 5.5.1.3 shall be initialized at the start of each slot fulfilling ![](media_svg/image107.svg) [公式≈: _{n}_{ss}PSSCH_{=}_{0}]. For sidelink transmission modes 3 and 4 the pseudo-random sequence generator in clause 5.5.1.3 shall be initialized at the start of each slot fulfilling ![](media_svg/image108.svg) [公式≈: n_{ss}^{PSSCH}mod2=0].

- For sidelink transmission modes 3 and 4 on the PSCCH, the cyclic shift ![](media_svg/image109.svg) [公式≈: ^{n}cs,Λ] to be applied for all DM-RS in a subframe shall be chosen according to clause 14.2.1 of [4].

- For sidelink transmission modes 1and 2 and sidelink discovery, the quantity ![](media_svg/image110.svg) [公式: m] in clause 5.5.2.1.1 takes the values ![](media_svg/image111.svg) [公式: m=0,1] and for sidelink transmission modes 3and 4, the quantity ![](media_svg/image110.svg) [公式: m] in clause 5.5.2.1.1 takes the values ![](media_svg/image112.svg) [公式: m=0,1,2,3] for PSSCH and ![](media_svg/image113.svg) [公式: m=0,1,2] for PSBCH.

- For sidelink transmission modes 3 and 4, the quantity ![](media_svg/image114.svg) [公式≈: ^{n}ID^{X}] equals the decimal representation of CRC on the PSCCH transmitted in the same subframe as the PSSCH according to ![](media_svg/image34.svg) [公式≈: _{n}_{ID}X_{=}_{⊆}_{i}^{L}_{=}^{−}_{0}^{1}_{p}_{i}_{∪}_{2}L−1−i] with ![](media_svg/image35.svg) [公式: p] and ![](media_svg/image36.svg) [公式: L] given by clause 5.1.1 in [3].

Table 9.8-1: Reference signal parameters for PSSCH.

| Parameter in clause 5.5.2.1 |  | PSSCH |  |
| --- | --- | --- | --- |
|  |  | Sidelink transmission modes 1 and 2 | Sidelink transmission  modes 3 and 4 |
| Group hopping |  | enabled | enabled |
|  | ![](media_svg/image115.svg) [公式≈: _{n}_{ID}RS] | ![](media_svg/image116.svg) [公式≈: _{n}_{ID}SA] | ![](media_svg/image114.svg) [公式≈: ^{n}ID^{X}] |
|  | ![](media_svg/image117.svg) [公式≈: ^{n}s] | ![](media_svg/image118.svg) [公式≈: _{n}_{ss}PSSCH] | ![](media_svg/image119.svg) [公式≈: _{2}_{n}_{ss}PSSCH] first DM-RS symbol in a slot![](media_svg/image120.svg) [公式≈: _{2}_{n}_{ss}PSSCH_{+}_{1}] second DM-RS symbol in a slot |
|  | ![](media_svg/image121.svg) [公式≈: ^{f}ss] | ![](media_svg/image122.svg) [公式: n_{ID}^{SA}mod30] | ![](media_svg/image123.svg) [公式≈: _{√}n_{ID}^{X}16_{∃}mod30] |
| Sequence hopping |  | disabled | disabled |
| Cyclic shift | ![](media_svg/image109.svg) [公式≈: ^{n}cs,Λ] | ![](media_svg/image124.svg) [公式≈: _{√}n_{ID}^{SA}2_{∃}mod8] | ![](media_svg/image125.svg) [公式≈: _{√}n_{ID}^{X}2_{∃}mod8] |
| Orthogonal sequence | ![](media_svg/image126.svg) [公式: {w^{Λ}(∪)}] | ![](media_svg/image127.svg) [公式≈: {_{{}+_{+}1_{1}+_{−}_{1}1_{}}}if_{if}n_{n}_{ID}^{SA}_{ID}_{SA}mod_{mod}2_{2}=_{=}_{1}0] | ![](media_svg/image128.svg) [公式≈: {_{{}+_{+}1_{1}+_{−}1_{1}+_{+}1_{1}+_{−}_{1}1_{}}}if_{if}n_{n}_{ID}^{X}_{ID}_{X}mod_{mod}2_{2}=_{=}_{1}0] |
| Reference signal length | ![](media_svg/image129.svg) [公式≈: _{M}_{sc}RS] | ![](media_svg/image130.svg) [公式≈: _{M}_{sc}PSSCH] | ![](media_svg/image130.svg) [公式≈: _{M}_{sc}PSSCH] |
| Number of layers | ![](media_svg/image131.svg) [公式: Υ] | 1 | 1 |
| Number of antenna ports | ![](media_svg/image132.svg) [公式: P] | 1 | 1 |

Table 9.8-2: Reference signal parameters for PSCCH.

| Parameter in clause 5.5.2.1 |  | PSCCH |  |
| --- | --- | --- | --- |
|  |  | Sidelink transmission modes 1 and 2 | Sidelink transmission modes 3 and 4 |
| Group hopping |  | disabled | disabled |
|  | ![](media_svg/image115.svg) [公式≈: _{n}_{ID}RS] | - | - |
|  | ![](media_svg/image117.svg) [公式≈: ^{n}s] | - | - |
|  | ![](media_svg/image121.svg) [公式≈: ^{f}ss] | 0 | 8 |
| Sequence hopping |  | disabled | disabled |
| Cyclic shift | ![](media_svg/image109.svg) [公式≈: ^{n}cs,Λ] | 0 | {0, 3, 6, 9} |
| Orthogonal sequence | ![](media_svg/image126.svg) [公式: {w^{Λ}(∪)}] | ![](media_svg/image133.svg) [公式: {+1+1}] | ![](media_svg/image134.svg) [公式: {+1+1+1+1}] |
| Reference signal length | ![](media_svg/image129.svg) [公式≈: _{M}_{sc}RS] | ![](media_svg/image135.svg) [公式≈: _{M}_{sc}PSCCH] | ![](media_svg/image135.svg) [公式≈: _{M}_{sc}PSCCH] |
| Number of layers | ![](media_svg/image131.svg) [公式: Υ] | 1 | 1 |
| Number of antenna ports | ![](media_svg/image132.svg) [公式: P] | 1 | 1 |

Table 9.8-3: Reference signal parameters for PSDCH and PSBCH.

| Parameter in clause 5.5.2.1 |  | PSDCH | PSBCH |  |
| --- | --- | --- | --- | --- |
|  |  |  | Sidelink transmission  modes 1 and 2 | Sidelink transmission  modes 3 and 4 |
| Group hopping |  | disabled | disabled | disabled |
|  | ![](media_svg/image121.svg) [公式≈: ^{f}ss] | 0 | ![](media_svg/image136.svg) [公式≈: _{√}N_{ID}^{SL}16_{∃}mod30] | ![](media_svg/image136.svg) [公式≈: _{√}N_{ID}^{SL}16_{∃}mod30] |
| Sequence hopping |  | disabled | disabled | disabled |
| Cyclic shift | ![](media_svg/image109.svg) [公式≈: ^{n}cs,Λ] | 0 | ![](media_svg/image137.svg) [公式≈: _{√}N_{ID}^{SL}2_{∃}mod8] | ![](media_svg/image137.svg) [公式≈: _{√}N_{ID}^{SL}2_{∃}mod8] |
| (Orthogonal) sequence | ![](media_svg/image138.svg) [公式: {λw^{Λ}(m)λ}] | ![](media_svg/image133.svg) [公式: {+1+1}] | ![](media_svg/image139.svg) [公式≈: {_{{}+_{+}1_{1}+_{−}_{1}1_{}}}if_{if}N_{N}_{ID}^{SL}_{ID}_{SL}mod_{mod}2_{2}=_{=}_{1}0] | ![](media_svg/image140.svg) [公式≈: {_{{}+_{+}1_{1}+_{−}_{1}1_{+}+_{1}1_{}}}if_{if}N_{N}_{ID}^{SL}_{ID}_{SL}mod_{mod}2_{2}=_{=}_{1}0] |
| Reference signal length | ![](media_svg/image129.svg) [公式≈: _{M}_{sc}RS] | ![](media_svg/image141.svg) [公式≈: _{M}_{sc}PSDCH] | ![](media_svg/image142.svg) [公式≈: _{M}_{sc}PSBCH] | ![](media_svg/image142.svg) [公式≈: _{M}_{sc}PSBCH] |
| Number of layers | ![](media_svg/image131.svg) [公式: Υ] | 1 | 1 | 1 |
| Number of antenna ports | ![](media_svg/image132.svg) [公式: P] | 1 | 1 | 1 |

## 9.9 SC-FDMA baseband signal generation

The time-continuous signal ![](media_svg/image143.svg) [公式≈: s_{l}^{(}^{p}^{)}(t)] for antenna port ![](media_svg/image144.svg) [公式: p] in SC-FDMA symbol ![](media_svg/image145.svg) [公式: l] in a sidelink slot is defined by clause 5.6 with ![](media_svg/image146.svg) [公式≈: _{N}_{RB}UL] replaced by ![](media_svg/image147.svg) [公式≈: _{N}_{RB}SL].

The cyclic prefix length for each sidelink channel or signal may differ from that configured for uplink transmissions.

## 9.10 Timing

Transmission of a sidelink radio frame number ![](media_svg/image148.svg) [公式: i] from the UE shall start ![](media_svg/image149.svg) [公式≈: ^{(}^{N}TA,SL^{+}^{N}TA offset^{)}^{∪}^{T}s] seconds before the start of the corresponding timing reference frame at the UE. The UE is not required to receive sidelink or downlink transmissions earlier than ![](media_svg/image150.svg) [公式: 624T_{s}] after the end of a sidelink transmission.

For PSDCH transmission and sidelink synchronization signal transmission for PSDCH:

if the UE has a serving cell fulfilling the S criterion according to [10, clause 5.2.3.2]

- the timing of reference radio frame ![](media_svg/image148.svg) [公式: i] equals that of downlink radio frame ![](media_svg/image148.svg) [公式: i] of the cell c as given in Clause 14.3.1 of [4] and

- ![](media_svg/image151.svg) [公式≈: ^{N}TA offset] is given by clause 8.1,

otherwise

- the timing of reference radio frame ![](media_svg/image148.svg) [公式: i] is implicitly obtained from [4] and

- ![](media_svg/image152.svg) [公式≈: ^{N}TA offset^{=}^{0}].

For all other sidelink transmissions:

if the UE has a serving cell fulfilling the S criterion according to [10, clause 5.2.3.2]

- the timing of reference radio frame ![](media_svg/image148.svg) [公式: i] equals that of downlink radio frame ![](media_svg/image148.svg) [公式: i] in the cell with the same uplink carrier frequency as the sidelink and

- ![](media_svg/image151.svg) [公式≈: ^{N}TA offset] is given by clause 8.1,

otherwise

- the timing of reference radio frame ![](media_svg/image148.svg) [公式: i] is implicitly obtained from [4] and

- ![](media_svg/image153.svg) [公式≈: ^{N}TA offset^{=}^{0}].

![](media/image154.emf)

Figure 9.9-1: Sidelink timing relation.

The quantity ![](media_svg/image155.svg) [公式≈: ^{N}TA,SL] differs between channels and signals according to

![](media_svg/image156.svg) [公式≈: _{N}_{TA,}_{SL}_{=}√_{⌠}_{∞}_{0}N_{TA}for _{for }_{all}PSSCH_{other }in _{cases}sidelink transmission mode1]

# 10 Narrowband IoT

## 10.0 General

### 10.0.1 Frame structure

#### 10.0.1.1 Frame structure type 1

Frame structure type 1 is applicable to FDD and IoT NTN TDD operation only.

#### 10.0.1.2 Frame structure type 2

Frame structure type 2 is applicable to TDD operation only.

The following restrictions apply:

- Uplink-downlink configuration 0 and 6 are not supported.

- UpPTS is not used for NPUSCH or NPRACH.

- DwPTS and UpPTS in special subframe configuration 10 is not used for transmissions.

- On an NB-IoT carrier for which higher-layer parameter operationModeInfo indicates inband-SamePCI or inband-DifferentPCI, or higher-layer parameter inbandCarrierInfo is present, or on an NB-IoT carrier for SystemInformationBlockType1-NB for which sib1-carrierInfo indicates non-anchor and the value of the higher layer parameter sib-GuardbandInfo is set to sib-GuardbandInbandSamePCI or sib-GuardbandinbandDiffPCI, DwPTS in special subframe configuration 0 and 5 for normal cyclic prefix is not used for NPDCCH and NPDSCH transmission, in addition when npdsch-16QAM-Config-r17 is configured DwPTS in special subframe configuration 9 for normal cyclic prefix is not used for NPDSCH transmission with 16QAM.

- Higher-layer parameter symbolBitmap does not apply to special subframes.

## 10.1 Uplink

### 10.1.1 Overview

#### 10.1.1.1 Physical channels

The following narrowband physical channels are defined:

- Narrowband Physical Uplink Shared Channel, NPUSCH

- Narrowband Physical Random-Access Channel, NPRACH

#### 10.1.1.2 Physical signals

The following uplink narrowband physical signals are defined:

- Narrowband demodulation reference signal

### 10.1.2 Slot structure and physical resources

#### 10.1.2.1 Resource grid

A transmitted physical channel or signal in a slot is described by one or several resource grids of ![](media_svg/image157.svg) [公式≈: _{N}_{sc}UL] subcarriers and ![](media_svg/image158.svg) [公式≈: ^{N}symb^{UL}] SC-FDMA symbols. The resource grid is illustrated in Figure 10.1.2.1-1. The slot number within a radio frame is denoted ![](media_svg/image117.svg) [公式≈: ^{n}s] where ![](media_svg/image159.svg) [公式: n_{s}⎰{0,1,...,19}] for ![](media_svg/image160.svg) [公式: δf=15kHz] and ![](media_svg/image161.svg) [公式: n_{s}⎰{0,1,...,4}] for ![](media_svg/image162.svg) [公式: δf=3.75kHz].

![](media/image163.emf)

Figure 10.1.2.1-1: Uplink resource grid for NB-IoT

The uplink bandwidth in terms of subcarriers ![](media_svg/image164.svg) [公式≈: _{N}_{sc}UL], and the slot duration ![](media_svg/image165.svg) [公式≈: ^{T}slot] are given in Table 10.1.2.1-1.

Table 10.1.2.1-1: NB-IoT parameters.

| Subcarrier spacing | ![](media_svg/image166.svg) [公式≈: _{N}_{sc}UL] | ![](media_svg/image167.svg) [公式≈: ^{T}slot] |
| --- | --- | --- |
| ![](media_svg/image168.svg) [公式: δf=3.75kHz] | ![](media_svg/image169.svg) [公式: 48] | ![](media_svg/image170.svg) [公式: 61440∪T_{s}] |
| ![](media_svg/image171.svg) [公式: δf=15kHz] | ![](media_svg/image172.svg) [公式: 12] | ![](media_svg/image173.svg) [公式: 15360∪T_{s}] |

A single antenna port ![](media_svg/image174.svg) [公式: p=0] is used for all uplink transmissions.

#### 10.1.2.2 Resource elements

Each element in the resource grid is called a resource element and is uniquely defined by the index pair ![](media_svg/image7.svg) [公式: (k,l)] in a slot where ![](media_svg/image175.svg) [公式: k=0,...,N_{sc}^{UL}−1] and ![](media_svg/image176.svg) [公式≈: l=0,...,N_{symb}^{UL}−1] are the indices in the frequency and time domains, respectively. Resource element ![](media_svg/image7.svg) [公式: (k,l)] corresponds to the complex value ![](media_svg/image177.svg) [公式≈: ^{a}k,l]. Quantities ![](media_svg/image177.svg) [公式≈: ^{a}k,l] corresponding to resource elements not used for transmission of a physical channel or a physical signal in a slot shall be set to zero.

#### 10.1.2.3 Resource unit

Resource units are used to describe the mapping of the NPUSCH to resource elements. A resource unit is defined as ![](media_svg/image178.svg) [公式≈: ^{N}symb^{UL}^{N}slots^{UL}] SC-FDMA symbols in the time domain and ![](media_svg/image179.svg) [公式≈: _{N}_{sc}RU]consecutive subcarriers in the frequency domain, where ![](media_svg/image179.svg) [公式≈: _{N}_{sc}RU] and ![](media_svg/image180.svg) [公式≈: ^{N}symb^{UL}] are given by Tables 10.1.2.3-1 and 10.1.2.3-2 for frame structure types 1 and 2, respectively.

Table 10.1.2.3-1: Supported combinations of ![](media_svg/image179.svg) [公式≈: _{N}_{sc}RU], ![](media_svg/image181.svg) [公式≈: ^{N}slots^{UL}], and ![](media_svg/image182.svg) [公式≈: ^{N}symb^{UL}] for frame structure type 1.

| NPUSCH format |  | ![](media_svg/image184.svg) [公式≈: _{N}_{sc}RU] | ![](media_svg/image185.svg) [公式≈: ^{N}slots^{UL}] | ![](media_svg/image186.svg) [公式≈: ^{N}symb^{UL}] |
| --- | --- | --- | --- | --- |
| 1 | 3.75 kHz | 1 | 16 | 7 |
|  | 15 kHz | 1 | 16 |  |
|  |  | 3 | 8 |  |
|  |  | 6 | 4 |  |
|  |  | 12 | 2 |  |
| 2 | 3.75 kHz | 1 | 4 |  |
|  | 15 kHz | 1 | 4 |  |

Table 10.1.2.3-2: Supported combinations of $ N_{sc}^{RU}$, $ N_{slots}^{UL}$, and $ N_{symb}^{UL}$ for frame structure type 2.

| NPUSCH format |  | Supported uplink-downlink configurations |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 1 | 3.75 kHz | 1, 4 | 1 | 16 | 7 |
|  | 15 kHz | 1, 2, 3, 4, 5 | 1 | 16 |  |
|  |  |  | 3 | 8 |  |
|  |  |  | 6 | 4 |  |
|  |  |  | 12 | 2 |  |
| 2 | 3.75 kHz | 1, 4 | 1 | 4 |  |
|  | 15 kHz | 1, 2, 3, 4, 5 | 1 | 4 |  |

### 10.1.3 Narrowband physical uplink shared channel

The narrowband physical uplink shared channel supports two formats:

- NPUSCH format 1, used to carry the UL-SCH

- NPUSCH format 2, used to carry uplink control information

#### 10.1.3.1 Scrambling

Scrambling shall be done according to clause 5.3.1.

For a UE communicating over NTN in FDD operation and if the higher layer parameter npusch-OCC-Enabled is configured, OCC is indicated as enabled in DCI Format N0 as described in [3], and $ M_{rep}^{NPUSCH}\geq  2 $, the scrambling sequence shall be reinitialized with

$$ c_{init}=n_{RNTI}\cdot  2^{14}+\left ( n_{f}mod2\right ) \cdot  2^{13}+\lfloor  \frac {n_{s}}{2}\rfloor  \cdot  2^{9}+N_{ID}^{Ncell}$$

after every $ M_{identical}^{NPUSCH}N_{identical}^{NPUSCH}$ transmissions of the codeword with $ n_{s}$ and $ n_{f}$ set to the first slot and the frame, respectively, used for the transmission of the repetition. The quantity $ N_{identical}^{NPUSCH}$ is given by clause 10.1.3.6.

Otherwise, the scrambling sequence generator shall be initialised with

$$ c_{init}=n_{RNTI}\cdot  2^{14}+\left ( n_{f}mod2\right ) \cdot  2^{13}+\lfloor  \frac {n_{s}}{2}\rfloor  \cdot  2^{9}+N_{ID}^{Ncell}$$

where $ n_{s}$ is the first slot of the transmission of the codeword. In case of NPUSCH repetitions, the scrambling sequence shall be reinitialised according to the above formula after every $ M_{identical}^{NPUSCH}$ transmissions of the codeword with $ n_{s}$ and $ n_{f}$ set to the first slot and the frame, respectively, used for the transmission of the repetition. The quantity $ M_{identical}^{NPUSCH}$ is given by clause 10.1.3.6.

#### 10.1.3.2 Modulation

Modulation shall be done according to clause 5.3.2 resulting in a block of modulated symbols $ d^{\left ( q\right ) }\left ( 0\right ) , \ldots  ,d^{\left ( q\right ) }\left ( M_{symb}^{(q)}-1\right ) $. Table 10.1.3.2-1 specifies the modulation mappings applicable for the narrowband physical uplink shared channel.

The block of modulated symbols shall be multiplied with a code $ c_{SR}$ resulting in a block of modulation symbols $\hat {d}^{\left ( q\right ) }\left ( 0\right ) , \ldots  ,\hat {d}^{\left ( q\right ) }\left ( M_{symb}^{\left ( q\right ) }-1\right ) $ according to

$\hat {d}^{(q)}\left ( i\right ) =c_{SR}\left ( i\right ) d^{(q)}\left ( i\right ) $

where

- $ c_{SR}\left ( i\right ) =\left ( -1\right ) ^{i}, i=0, 1, \ldots  , 15 $ in case a positive scheduling request according to [4] is to be transmitted using NPUSCH format 2

- $ c_{SR}\left ( i\right ) =1 $ otherwise

Table 10.1.3.2-1: NPUSCH modulation schemes

| NPUSCH format | ![](media_svg/image190.svg) [公式≈: _{N}_{sc}RU] | Modulation scheme |
| --- | --- | --- |
| 1 | 1 | BPSK, QPSK |
|  | >1 | QPSK, 16QAM |
| 2 | 1 | BPSK |

#### 10.1.3.3 Layer mapping

Layer mapping shall be done according to clause 5.3.2A with ![](media_svg/image37.svg) [公式: Υ=1] using $\hat {d}^{\left ( q\right ) }\left ( 0\right ) , \ldots  ,\hat {d}^{\left ( q\right ) }\left ( M_{symb}^{\left ( q\right ) }-1\right ) $ instead of $ d^{\left ( q\right ) }\left ( 0\right ) , \ldots  ,d^{\left ( q\right ) }\left ( M_{symb}^{(q)}-1\right ) $.

#### 10.1.3.4 Transform precoding

Transform precoding shall be done according to clause 5.3.3 with ![](media_svg/image191.svg) [公式≈: _{M}_{RB}PUSCH_{=}_{1}] and ![](media_svg/image192.svg) [公式≈: _{M}_{sc}PUSCH] replaced by ![](media_svg/image193.svg) [公式≈: _{M}_{sc}NPUSCH].

#### 10.1.3.5 Precoding

Precoding shall be done according to clause 5.3.3A assuming a single antenna port.

#### 10.1.3.6 Mapping to physical resources

Each NPUSCH codeword can be mapped to one or more than one resource units, ![](media_svg/image194.svg) [公式≈: ^{N}RU], as given by clause 16.5.1.2 of TS 36.213 [4], each of which shall be transmitted ![](media_svg/image195.svg) [公式≈: _{M}_{rep}NPUSCH] times.

The block of complex-valued symbols ![](media_svg/image196.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image197.svg) [公式≈: ^{Β}NPUSCH] in order to conform to the transmit power ![](media_svg/image198.svg) [公式≈: ^{P}NPUSCH]specified in [4], and mapped in sequence starting with ![](media_svg/image199.svg) [公式: z(0)] to subcarriers assigned for transmission of NPUSCH. The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] corresponding to the subcarriers assigned for transmission and not used for transmission of reference signals, shall be in increasing order of first the index ![](media_svg/image48.svg) [公式: k], then the index![](media_svg/image49.svg) [公式: l], starting with the first slot in the assigned resource unit.

After mapping to ![](media_svg/image200.svg) [公式≈: ^{N}slots]slots, the ![](media_svg/image201.svg) [公式≈: ^{N}slots] slots shall be repeated ![](media_svg/image202.svg) [公式≈: ^{M}identical^{NPUSCH}^{−}^{1}] additional times, before continuing the mapping of ![](media_svg/image203.svg) [公式: z(∪)] to the following slot, where

![](media_svg/image204.svg) [公式≈: _{M}_{identical}NPUSCH_{=}√⌡_{⌠}_{⌡}_{∞}_{1}min(⊥Mrep^{NPUSCH}/2∀,4)N_{N}sc_{sc}^{RU}_{RU}>_{=}1_{1}]

![](media_svg/image205.svg) [公式≈: _{N}_{slots}_{=}√_{⌠}_{∞}1_{2}δ_{δ}f_{f}=_{=}_{15}3.75_{kHz}kHz]

For a UE communicating over NTN in FDD operation, if the higher layer parameter npusch-OCC-Enabled is configured, OCC is indicated as enabled in DCI Format N0 as described in [3], and $ M_{rep}^{NPUSCH}\geq  2 $,

- For $\Delta  f=15kHz $, after mapping to a slot, the slot shall be repeated $ N_{identical}^{NPUSCH}-1 $ additional times and pairs of slots shall be multiplied by $ q(m)$ before continuing the mapping of $ z(\cdot  )$ to the following slot, the process repeats for all the slots in the NPUSCH format 1 transmission before OCC is applied, where for $ N_{sc}^{RU}=1 $, $ M_{OCC}=2 $, $ N_{identical}^{NPUSCH}=M_{OCC}$, and $ q(m)$ equals $\left [ \begin {matrix}+1 & +1\end {matrix}\right ] $ or $\left [ \begin {matrix}+1 & -1\end {matrix}\right ] $ as indicated by the DCI Format N0 as described in TS36.212 [3].

- For $\Delta  f=3.75kHz $, after mapping to a data symbol, the data symbol shall be repeated $ N_{identical}^{NPUSCH}-1 $ additional times and pairs of data symbols shall be multiplied by $ q(m)$ while skipping the DMRS symbol and guard period within the slot, before continuing the mapping of $ z(\cdot  )$ to the following data symbol, the process repeats for all the data symbols in the NPUSCH Format 1 transmission before OCC is applied, where for $ N_{sc}^{RU}=1 $, $ M_{OCC}=2 $, $ N_{identical}^{NPUSCH}=M_{OCC}$, and $ q(m)$ equals $\left [ \begin {matrix}+1 & +1\end {matrix}\right ] $ or $\left [ \begin {matrix}+1 & -1\end {matrix}\right ] $ as indicated by the DCI Format N0 as described in TS36.212 [3].

For NPUSCH Format 1 and 2 on frame structure type 2 with ,

- the NPUSCH transmission is carried out in the first set of  slots spanning over two contiguous uplink subframes not overlapping with any uplink subframe configured as invalid;

- for TDD configuration 1 and 4, if the starting position for the NPUSCH is indicated as the second of the two contiguous uplink subframes, the NPUSCH transmission is postponed until the start of two consecutive uplink subframes.

If a mapping to ![](media_svg/image200.svg) [公式≈: ^{N}slots] slots or a repetition of the mapping contains a resource element which overlaps with

- any configured NPRACH resource according to nprach-ParametersList in SystemInformationBlockType2-NB, or

- any configured NPRACH resource according to nprach-ParametersList given by ul-ConfigList in SystemInformationBlockType22-NB and if the UE indicates multiCarrier-NPRACH as supported, or

- any configured NPRACH resource according to nprach-ParametersList given by ul-ConfigListMixed in SystemInformationBlockType22-NB and if the UE indicates multiCarrier-NPRACH and mixedOperationMode as supported, or

- any configured NPRACH resource according to nprach-ParametersListFmt2 in SystemInformationBlockType2-NB and if the UE indicates nprach-Format2 as supported, or

- any configured NPRACH resource according to nprach-ParametersListFmt2 given by ul-ConfigList in SystemInformationBlockType23-NB and if the UE indicates multiCarrier-NPRACH and nprach-Format2 as supported, or

- any configured NPRACH resource according to nprach-ParametersListFmt2 given by ul-ConfigListMixed in SystemInformationBlockType23-NB and if the UE indicatesmultiCarrier-NPRACH, mixedOperationMode and nprach-Format2as supported, or

- any configured NPRACH resource according to nprach-ParametersListTDD in SystemInformationBlockType2-NB, or

- any configured NPRACH resource according to nprach-ParametersListTDD in SystemInformationBlockType22-NB and if the UE indicates multiCarrier-NPRACH as supported, or

- any configured NPRACH resource configured for Early Data Transmission and if the NPUSCH transmission is during an Early Data Transmission procedure [12, Clause 7.3b],

then,

- for ![](media_svg/image208.svg) [公式: δf=3.75kHz],

- if a UE communicating over NTN in FDD operation, and the higher layer parameter npusch-OCC-Enabled is configured, and OCC is indicated as enabled in DCI Format N0 as described in [3], and $ M_{rep}^{NPUSCH}\geq  2 $, then the NPUSCH transmission in overlapped $ N_{slots}$ slots is postponed until the next $ N_{slots}$ slots starting with the first slot satisfying $\left ( 5n_{f}+n_{s}\right ) mod4=0 $ and not overlapping with any configured NPRACH resource,

- otherwise, the NPUSCH transmission in overlapped![](media_svg/image200.svg) [公式≈: ^{N}slots] slots is postponed until the next ![](media_svg/image200.svg) [公式≈: ^{N}slots] slots not overlapping with any configured NPRACH resource.

- for ![](media_svg/image209.svg) [公式: δf=15kHz] the NPUSCH transmission in overlapped ![](media_svg/image200.svg) [公式≈: ^{N}slots] slots is postponed until the next ![](media_svg/image200.svg) [公式≈: ^{N}slots] slots starting with the first slot satisfying $ n_{s}mod2=0 $ $ n_{s}mod2=0 $ and not overlapping with any configured NPRACH resource.

NPRACH gaps as defined in clause 10.1.6.1 are not part of the NPRACH resource. For frame structure type 2, the valid uplink subframes which are not used for NPRACH transmission when it is not possible to map G symbol groups back-to-back are not part of the NPRACH resource. The mapping of ![](media_svg/image196.svg) [公式≈: z(0),...,z(M_{symb}^{ap}−1)] is then repeated until $ M_{rep}^{NPUSCH}N_{RU}N_{slots}^{UL}$ slots have been transmitted. After transmissions and/or postponements due to NPRACH of ![](media_svg/image210.svg) [公式: 256∪30720T_{s}] time units, for frame structure type 1 for FDD, a gap of ![](media_svg/image211.svg) [公式: 40∪30720T_{s}] time units shall be inserted where the NPUSCH transmission is postponed. The portion of a postponement due to NPRACH which coincides with a gap is counted as part of the gap.

When higher layer parameter npusch-AllSymbols is set to false, resource elements in SC-FDMA symbols overlapping with a symbol configured with SRS according to srs-SubframeConfig shall be counted in the NPUSCH mapping but not used for transmission of the NPUSCH. When higher layer parameter npusch-AllSymbols is set to true, all symbols are transmitted.

If higher layer parameter resourceReservationConfigUL is configured, then in case of NPUSCH format 1 transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space with the Resource reservation field in the DCI set to 1 including NPUSCH format 1 transmission without a corresponding NPDCCH, or in case of NPUSCH format 2 transmission associated with C-RNTI using UE-specific NPDCCH search space,

- In a subframe for ![](media_svg/image209.svg) [公式: δf=15kHz] or a slot for ![](media_svg/image208.svg) [公式: δf=3.75kHz]that is overlapping with any fully reserved uplink subframe as defined in clause 16.5 in [4],

- for ![](media_svg/image209.svg) [公式: δf=15kHz], the NPUSCH transmission is postponed until the next NB-IoT uplink subframe that is not fully reserved.

- for ![](media_svg/image208.svg) [公式: δf=3.75kHz], if a UE communicating over NTN is configured with higher layer parameter npusch-OCC-Enabled, $ N_{Rep}>1 $ and OCC enabled is indicated in the corresponding DCI Format N0, the NPUSCH transmission in the 4 consecutive slots, with the first slot satisfying $(5n_{f}+n_{s}) mod 4=0 $ and including the overlapping slot, are postponed until the next four consecutive slots spanning over eight contiguous uplink subframes starting with the first slot satisfying $(5n_{f}+n_{s}) mod 4=0 $ and not overlapping with any uplink subframe that is fully reserved. Otherwise, the NPUSCH transmission in the slot is postponed until the next slot spanning over two contiguous uplink subframes not overlapping with any uplink subframe that is fully reserved.

- In a subframe for ![](media_svg/image209.svg) [公式: δf=15kHz] or a slot for ![](media_svg/image208.svg) [公式: δf=3.75kHz]that is not overlapping with any fully reserved uplink subframe, any SC-FDMA symbols overlapping with reserved symbols shall be counted in the NPUSCH mapping but not used for transmission of the NPUSCH.

For a UE communicating over NTN, after transmissions (and/or postponements due to NPRACH) of $ N_{segment}^{precompensation}$ time units, for frame structure type 1 for FDD, a transmission gap of $ N_{gap}^{precompensation}$ time units shall be counted for the NPUSCH resource mapping but not used for transmission of the NPUSCH according to the UE capability ntn-SegmentedPrecompensationGaps-r17 as specified in 3GPP TS 36.331 [9]. The quantity $ N_{segment}^{precompensation}$ is provided by higher layers, and the quantity of $ N_{gap}^{precompensation}$ is configured by higher layers based on the UE capability if signalled.

### 10.1.4 Demodulation reference signal

#### 10.1.4.1 Reference signal sequence

##### 10.1.4.1.1 Reference signal sequence for ![](media_svg/image212.svg) [公式: N_{sc}^{RU}=1]

The reference signal sequence ![](media_svg/image213.svg) [公式: r_{u}(n)]for ![](media_svg/image214.svg) [公式: N_{sc}^{RU}=1] is defined by

![](media_svg/image215.svg) [公式≈: rnjcnwnnMNN_{u}()112mod16,0=+−≥<^{1}_{2}()(())()_{repslotsRU}^{NPUSCHUL}]

where the binary sequence ![](media_svg/image216.svg) [公式: c(n)] is defined by clause 7.2 and shall be initialised with ![](media_svg/image217.svg) [公式≈: c_{init}=35] at the start of the NPUSCH transmission. The quantity ![](media_svg/image218.svg) [公式: w(n)] is given by Table 10.1.4.1.1-1 where ![](media_svg/image219.svg) [公式≈: u=N_{ID}^{Ncell}mod16] for NPUSCH format 2, and for NPUSCH format 1if group hopping is not enabled, and by clause 10.1.4.1.3 if group hopping is enabled for NPUSCH format 1.

Table 10.1.4.1.1-1: Definition of ![](media_svg/image220.svg) [公式: w(n)]

| ![](media_svg/image221.svg) [公式: u] | ![](media_svg/image222.svg) [公式: w(0),...,w(15)] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 |
| 2 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 |
| 3 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 |
| 4 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 |
| 5 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 |
| 6 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 |
| 7 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 |
| 8 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| 9 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 |
| 10 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 |
| 11 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 |
| 12 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 |
| 13 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 |
| 14 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 |
| 15 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 |

The reference signal sequence for NPUSCH format 1 is given by:

![](media_svg/image223.svg) [公式: r_{u}(n)=r_{u}(n)]

The reference signal sequence for NPUSCH format 2 is given by

![](media_svg/image224.svg) [公式: r_{u}(3n+m)=w(m)r_{u}(n),m=0,1,2]

where ![](media_svg/image225.svg) [公式: w(m)]is defined in Table 5.5.2.2.1-2 with the sequence index chosen according to $\left ( \sum  _{i=0}^{7}c\left ( 8n^{'}+i\right ) \cdot  2^{i}\right ) mod 3 $ with ![](media_svg/image226.svg) [公式≈: ^{c}init^{=}^{N}ID^{Ncell}]. For frame structure type 1, $ n^{'}=n_{s}$. For frame structure type 2, $ n^{'}=\left ( n_{s}+n_{f}\right ) mod 5 $ for ![](media_svg/image162.svg) [公式: δf=3.75kHz]and $ n^{'}=\left ( n_{s}+n_{f}\right ) mod 20 $ for ![](media_svg/image160.svg) [公式: δf=15kHz].

## 10.1.4.1.1.1 OCC reference signal sequence for $ N_{sc}^{RU}=1 $ with $\Delta  f=15kHz $

For a UE communicating over NTN, the OCC reference signal sequence $\hat {r}_{u,OCC}(n)$ for $ N_{sc}^{RU}=1 $ is defined by

$$\hat {r}_{u,OCC}\left ( M_{OCC}n+m\right ) =\hat {r}_{u}\left ( n\right ) q\left ( m\right ) $$

$$ n=0,1,\ldots  ,\frac {\left ( M_{rep}^{NPUSCH}N_{slots}^{UL}N_{RU}\right ) }{M_{OCC}}-1 $$

where

- $ M_{OCC}=2 $

- $ M_{rep}^{NPUSCH}\geq  2 $

- $ m=0, 1 $

- the subcarrier indication field in the DCI selects one of

- $ q(m)=\left [ \begin {matrix}1 & 1\end {matrix}\right ] $

- $ q(m)=\left [ \begin {matrix}1 & -1\end {matrix}\right ] $

For NPUSCH format 1 transmission with $\Delta  f=15kHz $, the start of the NPUSCH Format 1 transmission is as described in clause 16.5.1 of [4], when OCC is applied, after the start of the NPUSCH Format 1 transmission the DMRS symbols are transmitted according to $\hat {r}_{u,OCC}\left ( M_{OCC}n+m\right ) $.

## 10.1.4.1.1.2 OCC reference signal sequence for $ N_{sc}^{RU}=1 $ with $\Delta  f=3.75kHz $

For a UE communicating over NTN, the OCC reference signal sequence $\hat {r}_{u,OCC}(n)$ for $ N_{sc}^{RU}=1 $ is defined by

$$\hat {r}_{u,OCC}\left ( n\right ) ={\begin {matrix}\hat {r}_{u}\left ( n'\right )  & if\lfloor  \frac {n}{M_{OCC}}\rfloor  modM_{OCC}=p \\ 0 & otherwise\end {matrix}$$

$$ n=0,1,\ldots  ,M_{rep}^{NPUSCH}N_{slots}^{UL}N_{RU}-1 $$

$$ n^{'}=n-\lfloor  \frac {n}{M_{OCC}}\rfloor  -p $$

where

- $ M_{OCC}=2 $

- $ M_{rep}^{NPUSCH}\geq  2 $

- $ p=1 $ if the DCI indicates OCC sequence $\left [ \begin {matrix}1 & 1\end {matrix}\right ] $, otherwise $ p=0 $.

##### 10.1.4.1.2 Reference signal sequence for ![](media_svg/image227.svg) [公式: N_{sc}^{RU}>1]

The reference signal sequences ![](media_svg/image228.svg) [公式: r_{u}(n)]for ![](media_svg/image229.svg) [公式: N_{sc}^{RU}>1]is defined by a cyclic shift ![](media_svg/image230.svg) [公式: Α] of a base sequence according to

![](media_svg/image231.svg) [公式≈: rneenN_{u}(),0=≥<^{jnjn}^{ΑΦΠ}^{()4RU}_{sc}],

where ![](media_svg/image232.svg) [公式: Φ(n)] is given by Table 10.1.4.1.2-1 for ![](media_svg/image233.svg) [公式: N_{sc}^{RU}=3], Table 10.1.4.1.2-2 for ![](media_svg/image234.svg) [公式: N_{sc}^{RU}=6] and Table 5.5.1.2-1 for ![](media_svg/image235.svg) [公式: N_{sc}^{RU}=12].

If group hopping is not enabled, the base sequence index ![](media_svg/image236.svg) [公式: u] is given by higher layer parameters threeTone-BaseSequence, sixTone-BaseSequence, and twelveTone-BaseSequence for ![](media_svg/image233.svg) [公式: N_{sc}^{RU}=3], ![](media_svg/image234.svg) [公式: N_{sc}^{RU}=6], and ![](media_svg/image237.svg) [公式: N_{sc}^{RU}=12], respectively. If not signalled by higher layers, the base sequence is given by

![](media_svg/image238.svg) [公式≈: u=^{√}^{⌡}⌠_{⌡}_{∞}_{N}^{N}N_{ID}^{ID}ID_{Ncell}^{Ncell}^{Ncell}_{mod}^{mod}mod^{12}14_{30}_{for }for ^{for }_{N}N^{N}_{sc}_{RU}sc^{sc}^{RU}^{RU}_{=}=^{=}_{12}6^{3}]

If group hopping is enabled, the base sequence index ![](media_svg/image236.svg) [公式: u] is given by clause 10.1.4.1.3.

The cyclic shift ![](media_svg/image230.svg) [公式: Α] for ![](media_svg/image233.svg) [公式: N_{sc}^{RU}=3] and ![](media_svg/image234.svg) [公式: N_{sc}^{RU}=6] is derived from higher layer parameters threeTone-CyclicShift and sixTone-CyclicShift, respectively, as defined in Table 10.1.4.1.2-3. For ![](media_svg/image239.svg) [公式: N_{sc}^{RU}=12], if npusch-CyclicShift in PUR-Config-NB is configured for NPUSCH (re)transmission corresponding to preconfigured uplink resource it provides the value of $ n_{cs}$ and the cyclic shift $\alpha  $ in a slot ![](media_svg/image117.svg) [公式≈: ^{n}s] is given as $\alpha  =2\pi  n_{cs}/12 $, otherwise ![](media_svg/image240.svg) [公式: Α=0].

Table 10.1.4.1.2-1: Definition of ![](media_svg/image232.svg) [公式: Φ(n)] for ![](media_svg/image233.svg) [公式: N_{sc}^{RU}=3]

| $ u $ | $\varphi  \left ( 0\right ) , \varphi  \left ( 1\right ) , \varphi  \left ( 2\right ) $ |  |  |
| --- | --- | --- | --- |
| 0 | 1 | -3 | -3 |
| 1 | 1 | -3 | -1 |
| 2 | 1 | -3 | 3 |
| 3 | 1 | -1 | -1 |
| 4 | 1 | -1 | 1 |
| 5 | 1 | -1 | 3 |
| 6 | 1 | 1 | -3 |
| 7 | 1 | 1 | -1 |
| 8 | 1 | 1 | 3 |
| 9 | 1 | 3 | -1 |
| 10 | 1 | 3 | 1 |
| 11 | 1 | 3 | 3 |

Table 10.1.4.1.2-2: Definition of ![](media_svg/image232.svg) [公式: Φ(n)] for ![](media_svg/image234.svg) [公式: N_{sc}^{RU}=6]

| $ u $ | $\varphi  \left ( 0\right ) , \ldots  , \varphi  \left ( 5\right ) $ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1 | 3 | -3 |
| 1 | 1 | 1 | 3 | 1 | -3 | 3 |
| 2 | 1 | -1 | -1 | -1 | 1 | -3 |
| 3 | 1 | -1 | 3 | -3 | -1 | -1 |
| 4 | 1 | 3 | 1 | -1 | -1 | 3 |
| 5 | 1 | -3 | -3 | 1 | 3 | 1 |
| 6 | -1 | -1 | 1 | -3 | -3 | -1 |
| 7 | -1 | -1 | -1 | 3 | -3 | -1 |
| 8 | 3 | -1 | 1 | -3 | -3 | 3 |
| 9 | 3 | -1 | 3 | -3 | -1 | 1 |
| 10 | 3 | -3 | 3 | -1 | 3 | 3 |
| 11 | -3 | 1 | 3 | 1 | -3 | -1 |
| 12 | -3 | 1 | -3 | 3 | -3 | -1 |
| 13 | -3 | 3 | -3 | 1 | 1 | -3 |

Table 10.1.4.1.2-3: Definition of ![](media_svg/image230.svg) [公式: Α]

| ![](media_svg/image241.svg) [公式: N_{sc}^{RU}=3] |  | ![](media_svg/image242.svg) [公式: N_{sc}^{RU}=6] |  |
| --- | --- | --- | --- |
| threeTone-CyclicShift | ![](media_svg/image230.svg) [公式: Α] | sixTone-CyclicShift | ![](media_svg/image230.svg) [公式: Α] |
| 0 | ![](media_svg/image243.svg) [公式: 0] | 0 | ![](media_svg/image243.svg) [公式: 0] |
| 1 | ![](media_svg/image244.svg) [公式: 2Π/3] | 1 | ![](media_svg/image245.svg) [公式: 2Π/6] |
| 2 | ![](media_svg/image246.svg) [公式: 4Π/3] | 2 | ![](media_svg/image247.svg) [公式: 4Π/6] |
|  |  | 3 | ![](media_svg/image248.svg) [公式: 8Π/6] |

##### 10.1.4.1.3 Group hopping

For the reference signal for NPUSCH format 1, sequence-group hopping can be enabled where the sequence-group number ![](media_svg/image249.svg) [公式: u] in slot ![](media_svg/image117.svg) [公式≈: ^{n}s] of a radio frame $ n_{f}$ is defined by a group hopping pattern $ f_{gh}\left ( n^{'}\right ) $ and a sequence-shift pattern ![](media_svg/image250.svg) [公式≈: ^{f}ss] according to

$$ u=\left ( f_{gh}\left ( n^{'}\right ) +f_{ss}\right ) modN_{seq}^{RU}$$

where the number of reference signal sequences available for each resource unit size, ![](media_svg/image251.svg) [公式≈: ^{N}seq^{RU}]is given by Table 10.1.4.1.3-1.

Table 10.1.4.1.3-1: Definition of ![](media_svg/image252.svg) [公式≈: ^{N}seq^{RU}]

| ![](media_svg/image253.svg) [公式≈: _{N}_{sc}RU] | ![](media_svg/image254.svg) [公式≈: ^{N}seq^{RU}] |
| --- | --- |
| 1 | 16 |
| 3 | 12 |
| 6 | 14 |
| 12 | 30 |

Sequence-group hopping can be enabled or disabled by means of the cell-specific parameter groupHoppingEnabled provided by higher layers. Sequence-group hopping for NPUSCH can be disabled for a certain UE through the higher-layer parameter groupHoppingDisabled despite being enabled on a cell basis unless the NPUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure.

The group-hopping pattern $ f_{gh}\left ( n^{'}\right ) $ is given by

$ f_{gh}\left ( n^{'}\right ) =\left ( \sum  _{i=0}^{7}c\left ( 8n^{'}+i\right ) \cdot  2^{i}\right ) modN_{seq}^{RU}$

where $ n^{'}=n_{s}$ for ![](media_svg/image255.svg) [公式: N_{sc}^{RU}>1]. When $ N_{sc}^{RU}=1 $, for frame structure type 1, $ n^{'}$ is the slot number $ n_{s}$ of the first slot of the resource unit and for frame structure type 2, $ n^{'}$ is the frame number $ n_{f}$ of the first slot of the resource unit. The pseudo-random sequence ![](media_svg/image256.svg) [公式: c(i)] is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with $ c_{init}=\lfloor  \frac {N_{ID}^{Ncell}}{N_{seq}^{RU}}\rfloor  $ at the beginning of the resource unit for ![](media_svg/image257.svg) [公式: N_{sc}^{RU}=1]and in every even slot for ![](media_svg/image258.svg) [公式: N_{sc}^{RU}>1].

The sequence-shift pattern ![](media_svg/image250.svg) [公式≈: ^{f}ss] is given by

![](media_svg/image259.svg) [公式≈: f_{ss}=(N_{ID}^{Ncell}+δ_{ss})modN_{seq}^{RU}]

where ![](media_svg/image260.svg) [公式: δ_{ss}⎰{0,1,...,29}]is given by higher-layer parameter groupAssignmentNPUSCH. If no value is signalled, ![](media_svg/image261.svg) [公式: δ_{ss}=0].

#### 10.1.4.2 Mapping to physical resources

The sequence ![](media_svg/image262.svg) [公式: r(∪)] shall be multiplied with the amplitude scaling factor ![](media_svg/image263.svg) [公式≈: ^{Β}NPUSCH] and mapped in sequence starting with ![](media_svg/image264.svg) [公式: r(0)] to the sub-carriers. 
The set of sub-carriers used in the mapping process shall be identical to the corresponding NPUSCH transmission as defined in clause 10.1.3.6. 
The mapping to resource elements ![](media_svg/image19.svg) [公式: (k,l)] shall be in increasing order of first![](media_svg/image265.svg) [公式: k], then ![](media_svg/image266.svg) [公式: l], and finally the slot number. The values of the symbol index ![](media_svg/image266.svg) [公式: l] in a slot are given in Table 10.1.4.2-1.

Table 10.1.4.2-1: Demodulation reference signal location for NPUSCH.

| NPUSCH format | Values for ![](media_svg/image266.svg) [公式: l] |  |
| --- | --- | --- |
|  | ![](media_svg/image267.svg) [公式: δf=3.75kHz] | ![](media_svg/image268.svg) [公式: δf=15kHz] |
| 1 | 4 | 3 |
| 2 | 0,1,2 | 2,3,4 |

If higher layer parameter resourceReservationConfigUL is configured, then in case of NPUSCH format 1 transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space and the Resource reservation field in the DCI is set to 1 including NPUSCH format 1 transmission without a corresponding NPDCCH, or in case of NPUSCH format 2 transmission associated with C-RNTI using UE-specific NPDCCH search space,

- In a subframe for ![](media_svg/image209.svg) [公式: δf=15kHz]or a slot for ![](media_svg/image208.svg) [公式: δf=3.75kHz]that is overlapping with any fully reserved uplink subframe as defined in clause 16.5 in [4],

- for ![](media_svg/image209.svg) [公式: δf=15kHz], the demodulation reference signal transmission is postponed until the next NB-IoT uplink subframe that is not fully reserved.

- for ![](media_svg/image208.svg) [公式: δf=3.75kHz], the demodulation reference signal transmission in the slot is postponed until the next slot spanning over two contiguous uplink subframes not overlapping with any uplink subframe that is fully reserved.

- In a subframe for ![](media_svg/image209.svg) [公式: δf=15kHz]or a slot for ![](media_svg/image208.svg) [公式: δf=3.75kHz] that is not overlapping with any fully reserved uplink subframe, any demodulation reference signal transmission in SC-FDMA symbols overlapping with reserved symbols is dropped.

### 10.1.5 SC-FDMA baseband signal generation

For ![](media_svg/image269.svg) [公式: N_{sc}^{RU}>1], the time-continuous signal ![](media_svg/image270.svg) [公式: s_{l}(t)] in SC-FDMA symbol ![](media_svg/image145.svg) [公式: l] in a slot is defined by clause 5.6 with the quantity ![](media_svg/image271.svg) [公式≈: _{N}_{RB}UL_{N}_{sc}RB] replaced by ![](media_svg/image272.svg) [公式≈: _{N}_{sc}UL].

For ![](media_svg/image273.svg) [公式: N_{sc}^{RU}=1], the time-continuous signal ![](media_svg/image274.svg) [公式: s_{k}_{,}_{l}(t)] for sub-carrier index ![](media_svg/image275.svg) [公式: k]in SC-FDMA symbol ![](media_svg/image145.svg) [公式: l] in an uplink slot is defined by

![](media_svg/image276.svg) [公式≈: _{kkN}_{staee}_{kl}_{()UL}_{,}_{−}_{(}_{=+}_{)}_{=∪∪}_{⋅∂}_{√∃}_{kl}_{()}_{−}_{,}_{sc}j_{2}Φkl,jkftNT212Π(+δ−)(CP,sl)]

for ![](media_svg/image277.svg) [公式≈: 0≥t<(N_{CP}_{,}_{l}+N)T_{s}] where parameters for ![](media_svg/image278.svg) [公式: δf=15kHz] and ![](media_svg/image279.svg) [公式: δf=3.75kHz] are given in Table 10.1.5-1, ![](media_svg/image280.svg) [公式≈: ^{a}k^{(}^{−}^{)},l] is the modulation value of symbol ![](media_svg/image145.svg) [公式: l], and the phase rotation ![](media_svg/image281.svg) [公式≈: ^{Φ}k,l] is defined by

$$\varphi  _{k,j}=\rho  \left ( \hat {l}mod 2\right ) +\varphi  _{k}\left ( \hat {l}\right ) $$

$$\rho  ={\frac {\pi  }{2}for BPSK\\\frac {\pi  }{4}for QPSK $$

$$\varphi  _{k}\left ( \hat {l}\right ) ={0\hat {l}=0\\\varphi  _{k}\left ( \hat {l}-1\right ) +2\pi  \Delta  f\left ( k+1/2\right ) \left ( N+N_{CP,l}\right ) T_{s}\hat {l}>0 $$

$$\hat {l}=0,1,\ldots  ,N_{TB}M_{rep}^{NPUSCH}N_{RU}N_{slots}^{UL}N_{symb}^{UL}-1 $$

$$ l=\hat {l}modN_{symb}^{UL}$$

where $ N_{TB}$  is the number of transport blocks defined in 16.5.1 of TS 36.213 [4]. If $ N_{TB}$ >1 and interleaving between codewords is applied according to clause 16.5.1 of TS 36.213[4], then the symbol counter ![](media_svg/image282.svg) [公式≈: ^{~}l] is reset at the start of the first NPUSCH codeword transmission and incremented for each symbol during the transmission of the $ N_{TB}$ NPUSCH codewords. For other cases, the symbol counter ![](media_svg/image282.svg) [公式≈: ^{~}l] is reset to 0 at the start of each NPUSCH codeword transmission and incremented for each symbol during the transmission of the NPUSCH codeword.

Table 10.1.5-1: SC-FDMA parameters for ![](media_svg/image283.svg) [公式: N_{sc}^{RU}=1]

| Parameter | ![](media_svg/image284.svg) [公式: δf=3.75kHz] | ![](media_svg/image278.svg) [公式: δf=15kHz] |
| --- | --- | --- |
| ![](media_svg/image285.svg) [公式: N] | 8192 | 2048 |
| Cyclic prefix length ![](media_svg/image286.svg) [公式≈: ^{N}CP,l] | 256 | ![](media_svg/image287.svg) [公式: 160for  l=0]![](media_svg/image288.svg) [公式: 144for  l=1,2,...,6] |
| Set of values for ![](media_svg/image289.svg) [公式: k] | -24,-23,…,23 | -6,-5,…,5 |

The SC-FDMA symbols in a slot shall be transmitted in increasing order of ![](media_svg/image145.svg) [公式: l], starting with ![](media_svg/image290.svg) [公式: l=0], where SC-FDMA symbol ![](media_svg/image291.svg) [公式: l>0]starts at time ![](media_svg/image292.svg) [公式≈: ⊆^{l}_{l}_{±}^{−}_{=}^{1}_{0}^{(}^{N}CP,l±^{+}^{N}^{)}^{T}s] within the slot. For ![](media_svg/image293.svg) [公式: δf=3.75kHz], the remaining ![](media_svg/image294.svg) [公式: 2304T_{s}] in ![](media_svg/image167.svg) [公式≈: ^{T}slot] are not transmitted and used for guard period.

Only normal CP is supported for Narrowband IoT uplink in this release of the specification.

### 10.1.6 Narrowband physical random-access channel

#### 10.1.6.1 Time and frequency structure

The physical layer random access preamble is based on single-subcarrier frequency-hopping symbol groups. A symbol group is illustrated in Figure 10.1.6.1-1, consisting of a cyclic prefix of length ![](media_svg/image295.svg) [公式≈: ^{T}CP] and a sequence of ![](media_svg/image296.svg) [公式: N] identical symbols with total length![](media_svg/image297.svg) [公式≈: ^{T}SEQ]. The total number of symbol groups in a preamble repetition unit is denoted by $ P $. The number of time-contiguous symbol groups is given by $ G $.

The parameter values for frame structures 1 and 2 are listed in Tables 10.1.6.1-1 and 10.1.6.1-2, respectively.

![](media/image298.emf)

Figure 10.1.6.1-1: Random access symbol group

Table 10.1.6.1-1: Random access preamble parameters for frame structure type 1

| Preamble format |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 0 | 4 | 4 | 5 |  |  |
| 1 | 4 | 4 | 5 |  |  |
| 2 (note 1) | 6 | 6 | 3 |  | 3 $\cdot  24576T_{s}$ |
| Note 1: Not used for IoT NTN TDD operation with frame structure 1. |  |  |  |  |  |

Table 10.1.6.1-2: Random access preamble parameters for frame structure type 2

| Preamble format | Supported uplink-downlink configurations |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1, 2, 3, 4, 5 | 2 | 4 | 1 | $ 4768T_{s}$ |  |
| 1 | 1, 4 | 2 | 4 | 2 |  |  |
| 2 | 3 | 2 | 4 | 4 |  |  |
| 0-a | 1, 2, 3, 4, 5 | 3 | 6 | 1 |  |  |
| 1-a | 1, 4 | 3 | 6 | 2 |  |  |

The preamble consisting of $ P $ symbol groups shall be transmitted ![](media_svg/image319.svg) [公式≈: _{N}_{rep}NPRACH] times.

For IoT NTN TDD operation with frame structure 1, a preamble repetition unit shall be fully transmitted within the 8 consecutive uplink subframes of the 90 ms interval described in clause 4.4, whereas the transmission of a preamble repetition unit that is partially or not within the 8 consecutive uplink subframes shall be postponed until the next 8 consecutive uplink subframes of the 90 ms interval.

For frame structure type 2, when an invalid uplink subframe overlaps the transmission of $ G $ symbol groups without a gap, the $ G $ symbol groups are dropped. For frame structure type 2, the transmission of $ G $ symbol groups are aligned with the subframe boundary.

The transmission of a random-access preamble, if triggered by the MAC layer, is restricted to certain time and frequency resources.

A NPRACH configuration provided by higher layers contains the following:

- NPRACH resource periodicity ![](media_svg/image320.svg) [公式≈: _{N}_{period}NPRACH] (nprach-Periodicity),

- frequency location of the first subcarrier allocated to NPRACH ![](media_svg/image321.svg) [公式≈: ^{N}scoffset^{NPRACH}] (nprach-SubcarrierOffset),

- number of subcarriers allocated to NPRACH ![](media_svg/image322.svg) [公式≈: _{N}_{sc}NPRACH] (nprach-NumSubcarriers),

- number of starting sub-carriers allocated to UE initiated random access ![](media_svg/image323.svg) [公式≈: ^{N}sc_cont ^{NPRACH}] (nprach-NumCBRA-StartSubcarriers),

- number of NPRACH repetitions per attempt ![](media_svg/image319.svg) [公式≈: _{N}_{rep}NPRACH] (numRepetitionsPerPreambleAttempt),

- NPRACH starting time ![](media_svg/image324.svg) [公式≈: _{N}_{start}NPRACH] (nprach-StartTime),

- Fraction for calculating starting subcarrier index for the range of NPRACH subcarriers reserved for indication of UE support for multi-tone msg3 transmission ![](media_svg/image325.svg) [公式≈: _{N}_{MSG3}NPRACH] (nprach-SubcarrierMSG3-RangeStart).

NPRACH transmission can start only ![](media_svg/image326.svg) [公式≈: N_{start}^{NPRACH}∪30720T_{s}] time units after the start of a radio frame fulfilling ![](media_svg/image327.svg) [公式≈: n_{f}mod(N_{period}^{NPRACH}/10)=0]. For frame structure type 1 for FDD, after transmissions of ![](media_svg/image328.svg) [公式≈: 4∪64(T_{CP}+T_{SEQ})] time units for preamble formats 0 and 1, or $ 16\cdot  6(T_{CP}+T_{SEQ})$ time units for preamble format 2, a gap of ![](media_svg/image329.svg) [公式: 40∪30720T_{s}] time units shall be inserted.

NPRACH configurations where ![](media_svg/image330.svg) [公式≈: _{N}_{scoffset}NPRACH_{+}_{N}_{sc}NPRACH_{>}_{N}_{sc}UL] are invalid.

The NPRACH starting subcarriers allocated to UE initiated random access are split in two sets of subcarriers, ![](media_svg/image331.svg) [公式≈: ^{{}^{0}^{,}^{1}^{,...,}√^{N}sc_cont ^{NPRACH}^{N}MSG3^{NPRACH}∃^{−}^{1}^{}}] and ![](media_svg/image332.svg) [公式≈: ^{{}√^{N}sc_cont ^{NPRACH}^{N}MSG3^{NPRACH}∃^{,...,}^{N}sc_cont ^{NPRACH}^{−}^{1}^{}}], where the second set, if present, indicate UE support for multi-tone msg3 transmission.

The frequency location of the NPRACH transmission is constrained within ![](media_svg/image333.svg) [公式: N_{sc}^{RA}=12] sub-carriers, and within $ N_{sc}^{RA}=36 $ subcarriers when preamble format 2 as described in Table 10.1.6.1-1 is configured. Frequency hopping shall be used within the 12 subcarriers and 36 subcarriers when preamble format 2 as described in Table 10.1.6.1-1 is configured, where the frequency location of the ith symbol group is given by ![](media_svg/image334.svg) [公式≈: n_{sc}^{RA}(i)=n_{start}+n^{~}_{SC}^{RA}(i)] where ![](media_svg/image335.svg) [公式≈: nstart=Nscoffset^{NPRACH}+√ninitNsc^{RA}∃∪Nsc^{RA}]. The quantity $\hat {n}_{sc}^{RA}\left ( i\right ) $ depends on the frame structure.

For frame structure type 1:

- if $ G=4 $, $ P=4 $ for preamble formats 0 and 1 as described in Table 10.1.6.1-1:

![](media_svg/image336.svg) [公式≈: n^{~}sc_{f}^{RA}_{(}_{f}_{−}(_{(}_{1}i_{t})_{)}_{)}=_{=}_{=}_{⊇}_{⊕}_{⊕}_{⊗}_{0}^{√}^{⌡}^{⌡}^{⌡}⌠_{⌡}_{⌡}_{⌡}_{∞}^{(}^{n}n_{n}_{n}^{~}^{~}_{~}_{~}_{f}^{n}^{~}^{sc}sc_{sc}_{sc}^{RA}^{RA}_{RA}_{RA}_{(}^{sc}^{RA}_{t}_{−}^{(}(_{(}_{(}^{(}_{1}^{i}i_{i}_{i}^{0}_{)}^{−}−_{−}_{−}^{)}_{+}^{1}1_{1}_{1}^{+}^{)})_{)}_{)}_{⊇}_{⊕}_{⊕}_{⊗}^{+}−_{+}_{−}_{n}^{f}_{10}_{=}_{⊆}1^{1}^{(}_{6}_{6}_{10}^{i}_{t}_{+}^{/}_{t}_{9}_{+}^{4}_{c}_{1}^{)}_{(}_{n}^{)}^{mod}_{)}_{2}_{n}_{−}_{(}^{N}_{10}^{sc}_{t}^{RA}_{+}_{1}_{)}_{⇒}_{⇐}_{⇐}_{⇔}_{mod}^{i}^{i}i_{i}_{i}^{mod}^{mod}mod_{mod}_{mod}_{(}_{N}^{4}^{4}4_{4}_{4}_{sc}_{RA}^{=}^{=}=_{=}_{=}^{1}1^{0}_{2}_{2}_{−}^{,},^{3}3^{and}_{and}_{and}_{1}^{and}and_{)}_{+}_{1}^{i}_{n}_{n}_{~}_{~}_{⇒}_{⇐}_{⇐}_{⇔}_{sc}_{sc}^{n}n^{>}^{~}^{~}_{RA}_{RA}_{mod}^{sc}sc^{RA}^{RA}^{0}_{(}_{(}_{i}_{i}^{(}(_{−}_{−}^{i}i_{N}^{−}−_{1}_{1}_{sc}_{)}_{)}_{RA}^{1}1^{)})_{<}_{÷}^{mod}mod_{6}_{6}^{2}2^{=}=1^{0}]

where ![](media_svg/image337.svg) [公式≈: n^{~}_{SC}^{RA}(0)=n_{init}modN_{sc}^{RA}] with ![](media_svg/image338.svg) [公式≈: ^{n}init] being the subcarrier selected by the MAC layer from ![](media_svg/image339.svg) [公式≈: {0,1,...,N_{sc}^{NPRACH}−1}], and the pseudo random sequence ![](media_svg/image340.svg) [公式: c(n)] is given by clause 7.2. The pseudo random sequence generator shall be initialised with ![](media_svg/image341.svg) [公式≈: ^{c}init^{=}^{N}ID^{Ncell}].

- if $ G=6 $, $ P=6 $ for preamble format 2 as described in Table 10.1.6.1-1:

$\hat {n}_{SC}^{RA}\left ( i\right ) ={\begin {matrix}\left ( \hat {n}_{SC}^{RA}\left ( 0\right ) +f(i/6)\right ) modN_{sc}^{RA} & imod6=0andi>0 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +1 & imod6=1, 5and\hat {n}_{SC}^{RA}\left ( i-1\right ) mod2=0 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -1 & imod6=1, 5and\hat {n}_{SC}^{RA}\left ( i-1\right ) mod2=1 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +3 & imod6=2, 4and\lfloor  \frac {\hat {n}_{SC}^{RA}\left ( i-1\right ) }{3}\rfloor  mod2=0 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -3 & imod6=2, 4and\lfloor  \frac {\hat {n}_{SC}^{RA}\left ( i-1\right ) }{3}\rfloor  mod2=1 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +18 & imod6=3and\hat {n}_{SC}^{RA}\left ( i-1\right ) <18 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -18 & imod6=3and\hat {n}_{SC}^{RA}\left ( i-1\right ) \geq  18\end {matrix}$

$ f\left ( t\right ) =\left ( f\left ( t-1\right ) +\left ( \sum  _{n=10t+1}^{10t+9}c\left ( n\right ) 2^{n-\left ( 10t+1\right ) }\right ) mod\left ( N_{sc}^{RA}-1\right ) +1\right ) modN_{sc}^{RA}$

$ f\left ( -1\right ) =0 $

where  with  being the subcarrier selected by the MAC layer from , and the pseudo random sequence  is given by clause 7.2. The pseudo random sequence generator shall be initialised with .

For frame structure type 2:

- if $ G=2 $, $ P=4 $ for preamble formats 0, 1, and 2 as described in Table 10.1.6.1-2:

$\hat {n}_{SC}^{RA}\left ( i\right ) ={\begin {matrix}Y & imod8=0, 2andi>0 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +1 & imod8=1and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 2, 4, 6, 8, 10 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -1 & imod8=1and\hat {n}_{SC}^{RA}\left ( i-1\right ) =1, 3, 5, 7, 9, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +6 & imod8=3and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 1, 2, 3, 4, 5 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -6 & imod8=3and\hat {n}_{SC}^{RA}\left ( i-1\right ) =6, 7, 8, 9, 10, 11 \\ 2\lfloor  \frac {Y}{2}\rfloor  +1 & imod8=4and\hat {n}_{SC}^{RA}\left ( i-4\right ) =0, 2, 4, 6, 8, 10 \\ 2\lfloor  \frac {Y}{2}\rfloor   & imod8=4and\hat {n}_{SC}^{RA}\left ( i-4\right ) =1, 3, 5, 7, 9, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -1 & imod8=5and\hat {n}_{SC}^{RA}\left ( i-1\right ) =1, 3, 5, 7, 9, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +1 & imod8=5and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 2, 4, 6, 8, 10 \\ Ymod6+6 & imod8=6and\hat {n}_{SC}^{RA}\left ( i-4\right ) =0, 1, 2, 3, 4, 5 \\ Ymod6 & imod8=6and\hat {n}_{SC}^{RA}\left ( i-4\right ) =6, 7, 8, 9, 10, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -6 & imod8=7and\hat {n}_{SC}^{RA}\left ( i-1\right ) =6, 7, 8, 9, 10, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +6 & imod8=7and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 1, 2, 3, 4, 5\end {matrix}$

$ Y=\left ( ñ_{SC}^{RA}\left ( 0\right ) +f(i/2)\right ) modN_{sc}^{RA}$

$ f\left ( t\right ) =\left ( f\left ( t-1\right ) +\left ( \sum  _{n=10t+1}^{10t+9}c\left ( n\right ) 2^{n-\left ( 10t+1\right ) }\right ) mod\left ( N_{sc}^{RA}-1\right ) +1\right ) modN_{sc}^{RA}$

$ f\left ( -1\right ) =0 $

where  with  being the subcarrier selected by the MAC layer from , and the pseudo random sequence  is given by clause 7.2. The pseudo random sequence generator shall be initialised with .

- if $ G=3 $, $ P=6 $ for preamble formats 0-a, 1-a, as described in Table 10.1.6.1-2:

$\hat {n}_{SC}^{RA}\left ( i\right ) ={\begin {matrix}\left ( \hat {n}_{SC}^{RA}\left ( 0\right ) +f(i/3)\right ) modN_{sc}^{RA} & imod6=0, 3andi>0 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +1 & imod6=1and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 2, 4, 6, 8, 10 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -1 & imod6=2and\hat {n}_{SC}^{RA}\left ( i-2\right ) =0, 2, 4, 6, 8, 10 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -1 & imod6=1and\hat {n}_{SC}^{RA}\left ( i-1\right ) =1, 3, 5, 7, 9, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +1 & imod6=2and\hat {n}_{SC}^{RA}\left ( i-2\right ) =1, 3, 5, 7, 9, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +6 & imod6=4and\hat {n}_{SC}^{RA}\left ( i-1\right ) =0, 1, 2, 3, 4, 5 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -6 & imod6=5and\hat {n}_{SC}^{RA}\left ( i-2\right ) =0, 1, 2, 3, 4, 5 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) -6 & imod6=4and\hat {n}_{SC}^{RA}\left ( i-1\right ) =6, 7, 8, 9, 10, 11 \\ \hat {n}_{SC}^{RA}\left ( i-1\right ) +6 & imod6=5and\hat {n}_{SC}^{RA}\left ( i-2\right ) =6, 7, 8, 9, 10, 11\end {matrix}$

$ f\left ( t\right ) =\left ( f\left ( t-1\right ) +\left ( \sum  _{n=10t+1}^{10t+9}c\left ( n\right ) 2^{n-\left ( 10t+1\right ) }\right ) mod\left ( N_{sc}^{RA}-1\right ) +1\right ) modN_{sc}^{RA}$

$ f\left ( -1\right ) =0 $

where  with  being the subcarrier selected by the MAC layer from , and the pseudo random sequence  is given by clause 7.2. The pseudo random sequence generator shall be initialised with .

#### 10.1.6.2 Baseband signal generation

The time-continuous random-access signal ![](media_svg/image347.svg) [公式: s_{i}(t)] for symbol group ![](media_svg/image348.svg) [公式: i] is defined by

$ s_{i}\left ( t\right ) =\beta  _{NPRACH}e^{j2\pi  \left ( n_{SC}^{RA}\left ( i\right ) +Kk_{0}+\frac {1}{2}\right ) \Delta  f_{RA}\left ( t-T_{CP}\right ) }$

where $ 0\leq  t\leq  T_{SEQ}+T_{CP}$, ![](media_svg/image349.svg) [公式≈: ^{Β}NPRACH] is an amplitude scaling factor in order to conform to the transmit power ![](media_svg/image350.svg) [公式≈: ^{P}NPRACH] specified in clause 16.3.1 in TS 36.213 [4], ![](media_svg/image351.svg) [公式: k_{0}=−N_{sc}^{UL}2], ![](media_svg/image352.svg) [公式: K=δfδf_{RA}] accounts for the difference in subcarrier spacing between the random access preamble and uplink data transmission, and the location in the frequency domain controlled by the parameter ![](media_svg/image353.svg) [公式: n_{SC}^{RA}(i)] is derived from clause 10.1.6.1. The variable![](media_svg/image354.svg) [公式≈: ^{δ}^{f}RA] is given by Table 10.1.6.2-1.

Table 10.1.6.2-1: Random access baseband parameters

| Preamble format |  |  |
| --- | --- | --- |
|  | Frame Structure Type 1 | Frame Structure Type 2 |
| 0, 1 | 3.75 kHz |  |
| 0-a, 1-a |  | 3.75 kHz |
| 2 | 1.25 kHz | 3.75 kHz |

### 10.1.7 Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued baseband signal or the complex-valued NPRACH baseband signal is shown in Figure 5.8-1. The filtering required prior to transmission is defined by the requirements in TS36.101 [7].

## 10.2 Downlink

### 10.2.1 Overview

#### 10.2.1.1 Physical channels

A downlink narrowband physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS 36.212 [3] and the present document TS36.211.

The following downlink physical channels are defined:

- Narrowband Physical Downlink Shared Channel, NPDSCH

- Narrowband Physical Broadcast Channel, NPBCH

- Narrowband Physical Downlink Control Channel, NPDCCH

#### 10.2.1.2 Physical signals

A downlink narrowband physical signal corresponds to a set of resource elements used by the physical layer but does not carry information originating from higher layers. The following downlink physical signals are defined:

- Narrowband reference signal, NRS

- Narrowband synchronization signal

- Narrowband positioning reference signal, NPRS

- Narrowband wake up signal, NWUS

### 10.2.2 Slot structure and physical resource elements

#### 10.2.2.1 Resource grid

The transmitted signal on one antenna port in each slot is described by a resource grid of size one resource block as defined in clause 6.2.3.

Only ![](media_svg/image356.svg) [公式: δf=15kHz] is supported.

Narrowband positioning reference signals are transmitted on antenna port ![](media_svg/image357.svg) [公式: p=2006]. The channel over which a symbol on antenna port ![](media_svg/image357.svg) [公式: p=2006] is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only within ![](media_svg/image358.svg) [公式: M] consecutive subframes where

- if the higher layer parameter nprsBitmap is configured , ![](media_svg/image358.svg) [公式: M] equals the length of the nprsBitmap;

- if the higher layer parameter nprsBitmap is not configured, ![](media_svg/image359.svg) [公式≈: ^{M}^{=}^{N}NPRS] where ![](media_svg/image360.svg) [公式≈: ^{N}NPRS] is configured by higher layers.

#### 10.2.2.2 Resource elements

Resource elements are defined according to clause 6.2.2.

#### 10.2.2.3 Guard period for half-duplex FDD operation

Only type-B half-duplex FDD operation is supported.

#### 10.2.2.4 Guard period for TDD operation

For frame structure type 2, if a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig, a guard period is created by the UE by

- not receiving the first part of the first OFDM symbol of a downlink subframe immediately following an uplink subframe from the same UE for 15-kHz subcarrier spacing on an NB-IoT carrier for which higher-layer parameter operationModeInfo indicates guardband or standalone, or higher-layer parameter inbandCarrierInfo is not present.

### 10.2.3 Narrowband physical downlink shared channel

#### 10.2.3.1 Scrambling

Scrambling shall be done according to clause 6.3.1. If the NPDSCH is carrying the BCCH, the scrambling sequence generator shall be initialised with ![](media_svg/image361.svg) [公式≈: c_{init}=n_{RNTI}∪2^{15}+(N_{ID}^{Ncell}+1)((n_{f}mod61)+1)]. Otherwise, the scrambling sequence generator shall be initialised with ![](media_svg/image362.svg) [公式≈: c_{init}=n_{RNTI}∪2^{14}+n_{f}mod2∪2^{13}+_{√}n_{s}2_{∃}∪2^{9}+N_{ID}^{Ncell}] where![](media_svg/image117.svg) [公式≈: ^{n}s]is the first slot of the transmission of the codeword.

In case of NPDSCH repetitions and the NPDSCH carrying the BCCH, the scrambling sequence generator shall be reinitialized according to the expression above for each repetition.

In case of NPDSCH repetitions and the NPDSCH is not carrying the BCCH, the scrambling sequence generator shall be reinitialized according to the expression above after every $ min\left ( M_{rep}^{NPDSCH},4\right ) $ transmission of the codeword with![](media_svg/image117.svg) [公式≈: ^{n}s]and![](media_svg/image363.svg) [公式≈: ^{n}f] set to the first slot and the frame, respectively, used for the transmission of the repetition.

#### 10.2.3.2 Modulation

Modulation shall be done according to clause 6.3.2 using one of the modulation schemes in Table 10.2.3-1

Table 10.2.3-1: Modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| NPDSCH | QPSK, 16QAM |

#### 10.2.3.3 Layer mapping and precoding

Layer mapping and precoding shall be done according to clause 6.6.3 using the same set of antenna ports as the NPBCH.

#### 10.2.3.4 Mapping to resource elements

Each NPDSCH codeword can be mapped to one or more than one subframes, ![](media_svg/image364.svg) [公式≈: ^{N}SF], as given by clause 16.4.1.3 of TS 36.213 [4], each of which shall be transmitted $ M_{rep}^{NPDSCH}$ times.

For each of the antenna ports used for transmission of the physical channel, the block of complex-valued symbols ![](media_svg/image365.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}^{ap}−1)] shall be mapped to resource elements ![](media_svg/image366.svg) [公式: (k,l)] which meet all of the following criteria in the current subframe:

- the subframe is not used for transmission of NPBCH, NPSS, or NSSS, and

- except in a special subframe when $ M_{rep}^{NPDSCH}>1 $, they are assumed by the UE not to be used for NRS, and

- they are not overlapping with resource elements used for CRS as defined in clause 6 (if any), and

- the index ![](media_svg/image367.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image368.svg) [公式≈: ^{l}^{÷}^{l}DataStart] where ![](media_svg/image369.svg) [公式≈: ^{l}DataStart]is given by clause 16.4.1.4 of TS36.213 [4], and

- in addition, for frame structure type 2

- in a special subframe, if $ M_{rep}^{NPDSCH}=1 $, they are in DwPTS

- in a special subframe, if $ M_{rep}^{NPDSCH}>1 $, they are not NRS locations in subframes which are not special subframes.

The mapping of ![](media_svg/image370.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}^{ap}−1)] in sequence starting with ![](media_svg/image371.svg) [公式: y^{(}^{p}^{)}(0)] to resource elements ![](media_svg/image47.svg) [公式: (k,l)] on antenna port ![](media_svg/image10.svg) [公式: p] meeting the criteria above shall be in increasing order of first the index ![](media_svg/image265.svg) [公式: k] and then the index![](media_svg/image145.svg) [公式: l], starting with the first slot and ending with the second slot in a subframe. For NPDSCH not carrying BCCH, after mapping to a subframe, the subframe shall be repeated for $ min\left ( M_{rep}^{NPDSCH},4\right ) -1 $ additional subframes, before continuing the mapping of ![](media_svg/image372.svg) [公式: y^{(}^{p}^{)}(∪)] to the following subframe.

The resource elements in a special subframe that are not part of DwPTS are counted but not used in the mapping if $ M_{rep}^{NPDSCH}>1 $. When $ l=N_{symb}^{DL}-5,N_{symb}^{DL}-4 $, the resource elements in a special subframe assumed by the UE for NRSs are counted but not used in the mapping if $ M_{rep}^{NPDSCH}>1 $.

For frame structure type 1,

- for NPDSCH associated with C-RNTI when interferenceRandomisationConfig is used according to [9], or

- for NPDSCH associated with RA-RNTI, TC-RNTI or P-RNTI and transmitted in an NB-IoT carrier configured by SystemInformationBlockType22-NB, or

- for NPDSCH associated with C-RNTI in an NB-IoT carrier configured by SystemInformationBlockType22-NB when RadioResourceConfigDedicted-NB is not configured by higher layer, or

- for NPDSCH associated with PUR-RNTI/G-RNTI/ SC-RNTI/CB-RNTI, or

for frame structure type 2,

- for NPDSCH not carrying the BCCH,

define ![](media_svg/image373.svg) [公式≈: y_{n}^{(}_{f}^{p}_{,}^{)}_{n}_{s}(0),...,y_{n}^{(}_{f}^{p}_{,}^{)}_{n}_{s}(S−1)] as the block of complex-valued symbols mapped to subframe number $\lfloor  n_{s}/2\rfloor  $ and radio frame number ![](media_svg/image374.svg) [公式≈: ^{n}f]. Each complex-valued symbol ![](media_svg/image375.svg) [公式≈: y_{n}^{(}^{p}_{f}_{,}^{)}_{n}_{s}(i)] shall be multiplied with ![](media_svg/image376.svg) [公式≈: Θ_{n}_{f}_{,}_{n}_{s}(i)]before its transmission, with

![](media_svg/image377.svg) [公式≈: ^{Θ}^{n}^{f}^{,}^{n}^{s}^{(}^{i}^{)}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}⌡_{∞}−^{−}^{1}^{j}^{,}^{1}^{,}j^{if}^{,}^{if},^{if}if^{c}^{c}^{n}^{c}^{n}c^{f}^{n}^{f}^{,}_{n}^{n}^{,}^{f}^{n}^{s}_{f}^{,}^{s}^{n}_{,}^{(}_{n}^{s}^{(}_{s}^{2}^{(}^{2}(^{2}^{i}2^{i}^{)}^{i}^{)}i^{)}^{=})^{=}^{=}=^{0}^{1}^{0}1^{and}^{and}^{and}and^{c}^{c}^{n}^{c}^{n}c^{f}^{f}^{n}_{n}^{,}^{,}^{n}^{n}^{f}_{f}^{s}^{s}^{,}_{,}^{n}_{n}^{(}^{(}^{s}_{s}^{2}^{2}^{(}(^{2}2^{i}^{i}^{i}i^{+}^{+}^{+}+^{1}^{1}^{)}^{)}^{1}1^{)})^{=}^{=}^{=}=^{0}^{0}^{1}1]

where the scrambling sequence ![](media_svg/image378.svg) [公式≈: c_{n}_{f}_{,}_{n}_{s}(j),j=0,...2S−1]is given by clause 7.2 and shall be initialized at the start of each subframe with ![](media_svg/image379.svg) [公式≈: c_{init}=(n_{RNTI}+1)((10n_{f}+_{√}n_{s}/2_{∃})mod61+1)2^{9}+N_{ID}^{Ncell}].

The mapping of ![](media_svg/image370.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}^{ap}−1)] is then repeated until $ M_{rep}^{NPDSCH}N_{SF}$ subframes have been transmitted. For frame structure type 2, the resource elements in a special subframe that are not part of DwPTS are counted but not used in the repetition. When $ l=N_{symb}^{DL}-5,N_{symb}^{DL}-4 $, the resource elements in a special subframe assumed by the UE for NRSs are counted but not used in the repetition.

For NPDSCH carrying BCCH, the $ y^{\left ( p\right ) }\left ( (k-1)M_{symb}^{ap}\right ) , \ldots  ,y^{\left ( p\right ) }\left ( kM_{symb}^{ap}-1\right ) $ is mapped to ![](media_svg/image364.svg) [公式≈: ^{N}SF] subframes in sequence and then repeated until $ M_{rep}^{NPDSCH}N_{SF}$ subframes have been transmitted, where

- $ k=2 $ for mapping NPDSCH carrying SystemInformationBlockType1-NB to subframe #3 for frame structure type 1;

- $ k=1 $ otherwise.

The NPDSCH transmission can be configured by higher layers with transmission gaps where the NPDSCH transmission is postponed. There are no gaps in the NPDSCH transmission if ![](media_svg/image380.svg) [公式≈: ^{R}max^{<}^{N}gap,threshold]where ![](media_svg/image381.svg) [公式≈: ^{N}gap,threshold] is given by the higher layer parameter dl-GapThreshold and ![](media_svg/image382.svg) [公式≈: ^{R}max] is given by [4]. The gap starting frame and subframe is given by ![](media_svg/image383.svg) [公式≈: ^{(}^{10}^{n}f^{+}√^{n}s^{2}∃^{)}^{mod}^{N}gap,period^{=}^{0}] where the gap periodicity,![](media_svg/image384.svg) [公式≈: ^{N}gap,period], is given by the higher layer parameter dl-GapPeriodicity. The gap duration in number of subframes is given by ![](media_svg/image385.svg) [公式≈: ^{N}gap,duration^{=}^{N}gap,coeff^{N}gap,period], where ![](media_svg/image386.svg) [公式≈: ^{N}gap,coeff] is given by the higher layer parameter dl-GapDurationCoeff. For NPDSCH carrying the BCCH there are no gaps in the transmission.

The UE shall not expect NPDSCH in subframe ![](media_svg/image387.svg) [公式: i] if it is not a NB-IoT downlink subframe, except for transmissions of NPDSCH carrying SystemInformationBlockType1-NB in

- subframes 3 and 4 for frame structure type 1; and

- subframes 0, 4, and 5 for frame structure type 2.

In case of NPDSCH transmissions, in subframes that are not NB-IoT downlink subframes, the NPDSCH transmission is postponed until the next NB-IoT downlink subframe.

If higher layer parameter resourceReservationConfigDL is configured, then in case of NPDSCH transmission associated with C-RNTI using UE-specific NPDCCH search space with the Resource reservation field in the DCI set to 1,

- In a subframe that is fully reserved as defined in clause 16.4 in [4], the NPDSCH transmission is postponed until the next NB-IoT downlink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved OFDM symbols shall be counted in the NPDSCH mapping but not used for transmission of the NPDSCH.

### 10.2.4 Narrowband physical broadcast channel

#### 10.2.4.1 Scrambling

Scrambling shall be done according to clause 6.6.1 with ![](media_svg/image388.svg) [公式≈: ^{M}bit] denoting the number of bits to be transmitted on the NPBCH. ![](media_svg/image388.svg) [公式≈: ^{M}bit] equals 1600 for normal cyclic prefix. The scrambling sequence shall be initialised with ![](media_svg/image389.svg) [公式≈: ^{c}init^{=}^{N}ID^{Ncell}] in radio frames fulfilling![](media_svg/image390.svg) [公式: n_{f}mod64=0].

#### 10.2.4.2 Modulation

Modulation shall be done according to clause 6.6.2 using the modulation scheme in Table 10.2.4.2-1

Table 10.2.4.2-1: Modulation schemes for NPBCH

| Physical channel | Modulation schemes |
| --- | --- |
| NPBCH | QPSK |

#### 10.2.4.3 Layer mapping and precoding

Layer mapping and precoding shall be done according to clause 6.6.3 with ![](media_svg/image391.svg) [公式: P⎰{1,2}]. The UE shall assume antenna ports 2000 and 2001 are used for the transmission of the narrowband physical broadcast channel.

#### 10.2.4.4 Mapping to resource elements

The block of complex-valued symbols![](media_svg/image392.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}−1)] for each antenna port is transmitted in subframe 0 for frame structure type 1 or subframe 9 for frame structure type 2 during 64 consecutive radio frames starting in each radio frame fulfilling ![](media_svg/image393.svg) [公式: n_{f}mod64=0]. The quantity $ M_{symb}=800 $ for normal cyclic prefix. Define ![](media_svg/image394.svg) [公式≈: y^{(}_{f}^{p}^{)}(0),...,y^{(}_{f}^{p}^{)}(K−1)]as the block of complex-valued symbols to be transmitted in subframe 0 for frame structure type 1 or subframe 9 for frame structure type 2 of radio frame ![](media_svg/image395.svg) [公式: f=n_{f}mod64], as ![](media_svg/image396.svg) [公式≈: y^{(}_{f}^{p}^{)}(i)=Θ_{f}(i)y^{(}^{p}^{)}(K_{√}f/8_{∃}+i)], ![](media_svg/image397.svg) [公式: i=0,...,99] with ![](media_svg/image398.svg) [公式: K=100] for normal cyclic prefix, and

![](media_svg/image399.svg) [公式≈: ^{Θ}^{f}^{(}^{i}^{)}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}⌡_{∞}−^{−}^{1}^{j}^{,}^{1}^{,}j^{if}^{,}^{if},^{if}if^{c}^{c}^{c}^{f}c^{f}^{f}^{(}_{f}^{(}^{2}^{(}^{2}(^{2}^{i}2^{i}^{)}^{i}^{)}i^{)}^{=})^{=}^{=}=^{0}^{1}^{0}1^{and}^{and}^{and}and^{c}^{c}^{c}c^{f}^{f}^{f}_{f}^{(}^{(}^{2}^{2}^{(}(^{2}2^{i}^{i}^{i}i^{+}^{+}^{+}+^{1}^{1}^{)}^{)}^{1}1^{)})^{=}^{=}^{=}=^{0}^{0}^{1}1]

where the scrambling sequence ![](media_svg/image400.svg) [公式: c_{f}(j)], ![](media_svg/image401.svg) [公式: j=0,...,199] is given by clause 7.2, and shall be initialized at the start of each radio frame with ![](media_svg/image402.svg) [公式≈: c_{init}=(N_{ID}^{Ncell}+1)(n_{f}mod8+1)^{3}∪2^{9}+N_{ID}^{Ncell}]. The block of complex-valued symbols ![](media_svg/image403.svg) [公式≈: y^{(}_{f}^{p}^{)}(0),...,y^{(}_{f}^{p}^{)}(K−1)] shall be mapped in sequence starting with ![](media_svg/image404.svg) [公式≈: y^{(}_{f}^{p}^{)}(0)] to resource elements ![](media_svg/image405.svg) [公式: (k,l)]. The mapping to resource elements ![](media_svg/image406.svg) [公式: (k,l)] not reserved for transmission of reference signals shall be in increasing order of first the index![](media_svg/image265.svg) [公式: k], then the index ![](media_svg/image145.svg) [公式: l]. The first three OFDM symbols in a subframe shall not be used in the mapping process.

For the purpose of the mapping, the UE shall assume cell-specific reference signals for antenna ports 0-3 and narrowband reference signals for antenna ports 2000 and 2001 being present irrespective of the actual configuration. The frequency shift of the cell-specific reference signals shall be calculated by replacing ![](media_svg/image407.svg) [公式≈: _{N}_{ID}cell]with ![](media_svg/image408.svg) [公式≈: _{N}_{ID}Ncell] in the calculation of ![](media_svg/image409.svg) [公式≈: ^{v}shift]in clause 6.10.1.2.

### 10.2.5 Narrowband physical downlink control channel

#### 10.2.5.1 NPDCCH formats

The narrowband physical downlink control channel carries control information. A narrowband physical control channel is transmitted on an aggregation of one or two consecutive narrowband control channel elements (NCCEs), where a narrowband control channel element corresponds to 6 consecutive subcarriers in a subframe where NCCE 0 occupies subcarriers 0 through 5 and NCCE 1 occupies subcarriers 6 through 11. The NPDCCH supports multiple formats as listed in Table 10.2.5.1-1. For NPDCCH format 1, both NCCEs belong to the same subframe.

One or two NPDCCHs can be transmitted in a subframe.

Table 10.2.5.1-1: Supported NPDCCH formats

| NPDCCH format | Number of NCCEs |
| --- | --- |
| 0 | 1 |
| 1 | 2 |

#### 10.2.5.2 Scrambling

Scrambling shall be done according to clause 6.8.2. The scrambling sequence shall be initialised at the start of subframe k0 according to [4] Clause 16.6 and after every 4th NPDCCH subframe with ![](media_svg/image410.svg) [公式≈: ^{c}init^{=}√^{n}s^{2}∃^{2}^{9}^{+}^{N}ID^{Ncell}] where ![](media_svg/image411.svg) [公式≈: ^{n}s]is the first slot of the NPDCCH subframe in which scrambling is (re-)initialized.

#### 10.2.5.3 Modulation

Modulation shall be done according to clause 6.8.3 using the modulation scheme in Table 10.2.5.3-1

Table 10.2.5.3-1: Modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| NPDCCH | QPSK |

#### 10.2.5.4 Layer mapping and precoding

Layer mapping and precoding shall be done according to clause 6.6.3 using the same set of antenna ports as the NPBCH.

#### 10.2.5.5 Mapping to resource elements

The block of complex-valued symbols ![](media_svg/image412.svg) [公式≈: y(0),...,y(M_{symb}−1)] shall be mapped in sequence starting with ![](media_svg/image413.svg) [公式: y(0)] to resource elements ![](media_svg/image47.svg) [公式: (k,l)] on the associated antenna port which meet all of the following criteria:

- they are part of the NCCE(s) assigned for the NPDCCH transmission, and

- they are not used for transmission of NPBCH, NPSS, or NSSS, and

- except in a special subframe when NPDCCH is transmitted in more than one subframe, they are assumed by the UE not to be used for NRS, and

- they are not overlapping with resource elements used for CRS as defined in clause 6 (if any), and

- the index ![](media_svg/image367.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image414.svg) [公式≈: ^{l}^{÷}^{l}NPDCCHStart] where ![](media_svg/image415.svg) [公式≈: ^{l}NPDCCHStart]is given by clause 16.6.1 of TS 36.213 [4],

- in addition, for frame structure Type 2,

- in a special subframe where the NPDCCH is transmitted in one subframe, they are in DwPTS

- in a special subframe where the NPDCCH is transmitted in more than one subframe, they are not NRS locations when the subframe is not a special subframe.

The mapping to resource elements ![](media_svg/image47.svg) [公式: (k,l)] on antenna port ![](media_svg/image10.svg) [公式: p] meeting the criteria above shall be in increasing order of first the index ![](media_svg/image265.svg) [公式: k] and then the index![](media_svg/image145.svg) [公式: l], starting with the first slot and ending with the second slot in a subframe. Denote ![](media_svg/image416.svg) [公式≈: y_{n}_{f}_{,}_{n}_{s}(0),...,y_{n}_{f}_{,}_{n}_{s}(T−1)] as the complex-valued symbols that are mapped to resource elements meeting the criteria above in subframe $\lfloor  n_{s}/2\rfloor  $, with the insertion of <NIL> elements in the locations of resource elements which are not part of the NCCE(s) assigned for the NPDCCH transmission.

If the NPDCCH is transmitted in more than one subframe, the resource elements in a special subframe that are not part of DwPTS are counted but not used in the mapping. When $ l=N_{symb}^{DL}-5,N_{symb}^{DL}-4 $, the resource elements in a special subframe assumed by the UE for NRSs are counted but not used in the mapping if the NPDCCH is transmitted in more than one subframe.

For frame structure type 1,

- for NPDCCH associated with RA-RNTI, TC-RNTI, or P-RNTI and transmitted in an NB-IoT carrier configured by SystemInformationBlockType22-NB, or

- for NPDCCH associated with C-RNTI during random access procedure in a Type-2 CSS in an NB-IoT carrier configured by SystemInformationBlockType22-NB, or

- for NPDCCH associated with C-RNTI in an NB-IoT carrier configured by SystemInformationBlockType22-NB when RadioResourceConfigDedicted-NB is not configured by higher layer, or

- for NPDCCH associated with PUR-RNTI/G-RNTI/ SC-RNTI/CB-RNTI, or

- for NPDCCH associated with C-RNTI or SPS C-RNTI when interferenceRandomisationConfig is used according to [9], or

for frame structure type 2,

each complex-valued symbol ![](media_svg/image417.svg) [公式≈: y_{n}_{f}_{,}_{n}_{s}(i)],![](media_svg/image418.svg) [公式: i=0,...,T−1] shall be multiplied with ![](media_svg/image419.svg) [公式≈: Θ_{n}_{f}_{,}_{n}_{s}(i)],![](media_svg/image418.svg) [公式: i=0,...,T−1]where

![](media_svg/image377.svg) [公式≈: ^{Θ}^{n}^{f}^{,}^{n}^{s}^{(}^{i}^{)}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}⌡_{∞}−^{−}^{1}^{j}^{,}^{1}^{,}j^{if}^{,}^{if},^{if}if^{c}^{c}^{n}^{c}^{n}c^{f}^{n}^{f}^{,}_{n}^{n}^{,}^{f}^{n}^{s}_{f}^{,}^{s}^{n}_{,}^{(}_{n}^{s}^{(}_{s}^{2}^{(}^{2}(^{2}^{i}2^{i}^{)}^{i}^{)}i^{)}^{=})^{=}^{=}=^{0}^{1}^{0}1^{and}^{and}^{and}and^{c}^{c}^{n}^{c}^{n}c^{f}^{f}^{n}_{n}^{,}^{,}^{n}^{n}^{f}_{f}^{s}^{s}^{,}_{,}^{n}_{n}^{(}^{(}^{s}_{s}^{2}^{2}^{(}(^{2}2^{i}^{i}^{i}i^{+}^{+}^{+}+^{1}^{1}^{)}^{)}^{1}1^{)})^{=}^{=}^{=}=^{0}^{0}^{1}1]

where the scrambling sequence ![](media_svg/image420.svg) [公式≈: c_{n}_{f}_{,}_{n}_{s}(j),j=0,...2T−1] is given by clause 7.2 and shall be initialized at the start of each subframe with ![](media_svg/image421.svg) [公式≈: c_{init}=(N_{ID}^{Ncell}+1)((10n_{f}+_{√}n_{s}/2_{∃})mod8192+1)2^{9}+N_{ID}^{Ncell}].

The NPDCCH transmission can be configured by higher layers with transmissions gaps where the NPDCCH transmission is postponed. The configuration is the same as described for NPDSCH in clause 10.2.3.4.

The UE shall not expect NPDCCH in subframe ![](media_svg/image387.svg) [公式: i] if it is not a NB-IoT downlink subframe. In case of NPDCCH transmissions, in subframes that are not NB-IoT downlink subframes, the NPDCCH transmission is postponed until the next NB-IoT downlink subframe.

If higher layer parameter resourceReservationConfigDL is configured, then in case of NPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space,

- In a subframe that is fully reserved as defined in clause 16.4 in [4], the NPDCCH transmission is postponed until the next NB-IoT downlink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved OFDM symbols shall be counted in the NPDCCH mapping but not used for transmission of the NPDCCH.

### 10.2.6 Narrowband reference signal (NRS)

Before a UE obtains operationModeInfo:

- If frame structure type 1 is used in FDD, the UE may assume narrowband reference signals (NRSs) are transmitted in subframes #0 and #4 and in subframes #9 not containing NSSS.

- If frame structure type 2 is used, the UE may assume narrowband reference signals (NRSs) are transmitted in subframes #9 and in subframes #0 not containing NSSS.

- If frame structure type 1 is used in IoT NTN TDD, the UE may assume narrowband reference signals (NRSs) are transmitted in subframes #0, #3, #4, #6, #7, #8 and in subframes #9 not containing NSSS within the $ D $ consecutive downlink subframes according to the TDD pattern.

On an NB-IoT carrier for which a UE receives higher-layer parameter operationModeInfo indicating guardband or standalone.

- If frame structure type 1 is used in FDD, before the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0, #1, #3, #4 and in subframes #9 not containing NSSS.

- If frame structure type 2 is used, before the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #9, and in subframes #0 not containing NSSS, and in subframes #4 if subframes #4 is configured for SystemInformationBlockType1-NB transmissions.

- If frame structure type 1 is used, after the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0, #1, #3, #4, subframes #9 not containing NSSS, and in NB-IoT downlink subframes.

- If frame structure type 2 is used, after the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #9, subframes #0 not containing NSSS, in subframes #4 if subframes #4 is configured for SystemInformationBlockType1-NB transmissions, and in NB-IoT downlink subframes.

- If frame structure type 1 is used in IoT NTN TDD, the UE may assume narrowband reference signals (NRSs) are transmitted in subframes #0, #3, #4, #6, #7, #8 and in subframes #9 not containing NSSS within the $ D $ consecutive downlink subframes according to the TDD pattern.

On an NB-IoT carrier for SystemInformationBlockType1-NB for which sib1-carrierInfo-NB indicates non-anchor for frame structure type 2, before the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0 and #5. After the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0, #5, and in NB-IoT downlink subframes indicated by tdd-SI-SubframesBitmap.

On an NB-IoT carrier for which DL-CarrierConfigCommon-NB is present and no inbandCarrierInfo is present.

- If frame structure type 1 is used and when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI and higher-layer indicates nrs-NonAnchorConfig is enabled, the UE first determines the starting subframe of NPDCCH search space associated with NRS transmission according to [10].

- If higher-layer nB is configured as fourT, the UE may assume NRSs are transmitted in the 10th NB-IoT DL subframe before the determined starting subframe of NPDCCH search space.

- If higher-layer nB is configured as twoT, the UE may assume NRSs are transmitted in the 9th and 10th NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- If higher-layer nB is configured as oneT, the UE may assume NRSs are transmitted in the 6th, 7th, 8th, 9th and 10th NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- For other nB values, the UE may assume NRSs are transmitted in 10 NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- When an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI, the UE may assume NRSs are transmitted in the NPDCCH candidate where the UE finds a DCI with CRC scrambled by the P-RNTI. The UE may also assume NRSs are transmitted in 10 NB-IoT DL subframes before and in 4 NB-IoT DL subframes after the NPDCCH candidate where the UE finds a DCI with CRC scrambled by the P-RNTI, where NB-IoT DL subframes without NRS are not counted. If the DCI with CRC scrambled by the P-RNTI schedules a NPDSCH, the UE may assume NRSs are transmitted in the NB-IoT DL subframes carrying the NPDSCH as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- During the window controlled by higher layers where the UE shall attempt to decode the NPDCCH with DCI scrambled by RA-RNTI (see [8], clause 5.1.4), the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before and in 4 NB-IoT DL subframes after each Type-2 CSS, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by the RA-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by the RA-RNTI, as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted. In addition, when the UE attempts to decode a DCI with CRC scrambled by the RA-RNTI as well as receiving the NPDSCH scheduled by the DCI scrambled by the RA-RNTI, the UE may assume NRSs are transmitted in subframes #0, #1, #3, #4 and #9.

- During random access procedure, when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the temporary C-RNTI and/or the C-RNTI, before the DCI scrambled by temporary C-RNTI and/or C-RNTI is detected, the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before the start of each Type-2 CSS and in 4 NB-IoT DL subframes after the end of each Type-2 CSS until the mac-ContentionResolutionTimer expires, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by the temporary C-RNTI or C-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by the temporary C-RNTI or C-RNTI as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- During CB-Msg3-EDT Procedure, when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by CB-RNTI, before the DCI scrambled by CB-RNTI is detected, the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before the start of each Type-2 CSS and in 4 NB-IoT DL subframes after the end of each Type-2 CSS until the CB-Msg3ResponseTimer expires, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by CB-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by CB-RNTI as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- An NB-IoT UE may assume NRSs are transmitted in NB-IoT DL subframes that are used for Type1A-NPDCCH common search space, and Type2A-NPDCCH common search space, as well as in 10 NB-IoT DL subframes prior and in 4 NB-IoT DL subframes after each Type1A-NPDCCH common search space and Type2A-NPDCCH common search space. A UE may assume NRSs are transmitted in NB-IoT DL subframes carrying NPDSCH scheduled by DCI CRC scrambled by G-RNTI or SC-RNTI as well as 4 NB-IoT DL subframes prior and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- In other cases, if frame structure typ1 is used, the UE may assume NRSs are transmitted in subframes #0, #1, #3, #4, #9, and in NB-IoT downlink subframes and shall not expect NRSs in other downlink subframes.

On an NB-IoT carrier for which a UE receives higher-layer parameter operationModeInfo indicating inband-SamePCI or inband-DifferentPCI.

- If frame structure type 1 is used, before the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0, #4 and in subframes #9 not containing NSSS, and in subframes #3 which contain SystemInformationBlockType1-NB when additionalTransmissionSIB1 is configured as TRUE.

- If frame structure type 2 is used, before the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #9, and in subframes #0 not containing NSSS, and in subframes #4 if subframes #4 is configured for SystemInformationBlockType1-NB transmissions.

- If frame structure type 1 is used, after the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #0, #4, subframes #9 not containing NSSS, subframes #3 which contain SystemInformationBlockType1-NB when additionalTransmissionSIB1 is configured as TRUE, and in NB-IoT downlink subframes.

- If frame structure type 2 is used, after the UE obtains SystemInformationBlockType1-NB, the UE may assume narrowband reference signals are transmitted in subframes #9, subframes #0 not containing NSSS, in subframes #4 if subframes #4 is configured for SystemInformationBlockType1-NB transmissions, and in NB-IoT downlink subframes

On an NB-IoT carrier for which DL-CarrierConfigCommon-NB is present and inbandCarrierInfo is present:

- If frame structure type 1 is used, when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI and higher-layer indicates nrs-NonAnchorConfig is enabled, the UE first determines the starting subframe of NPDCCH search space associated with NRS transmission according to [10].

- If higher-layer nB is configured as fourT, the UE may assume NRSs are transmitted in the 10th NB-IoT DL subframe before the determined starting subframe of NPDCCH search space.

- If higher-layer nB is configured as twoT, the UE may assume NRSs are transmitted in 9th and 10th NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- If higher-layer nB is configured as oneT, the UE may assume NRSs are transmitted in 6th, 7th, 8th, 9th and 10th NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- For other nB values, the UE may assume NRSs are transmitted in 10 NB-IoT DL subframes before the determined starting subframe of NPDCCH search space.

- When an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI, the UE may assume NRSs are transmitted in the NPDCCH candidate where the UE finds a DCI with CRC scrambled by the P-RNTI. The UE may also assume NRSs are transmitted in10 NB-IoT DL subframes before and in 4 NB-IoT DL subframes after the NPDCCH candidate, where NB-IoT DL subframes without NRS are not counted. If the DCI with CRC scrambled by the P-RNTI schedules a NPDSCH, the UE may assume NRSs are transmitted in the NB-IoT DL subframes carrying the NPDSCH as well as 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- During the window controlled by higher layers where the UE shall attempt to decode the NPDCCH with DCI scrambled by RA-RNTI (see [8], clause 5.1.4), the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before and in 4 NB-IoT DL subframes after each Type-2 CSS, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by the RA-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by the RA-RNTI, as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted. In addition, when the UE attempts to decode a DCI with CRC scrambled by the RA-RNTI as well as receiving the NPDSCH scheduled by the DCI scrambled by the RA-RNTI, the UE may assume NRSs are transmitted in subframes #0, #4 and #9.

- During random access procedure, when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by the temporary C-RNTI and/or the C-RNTI, before the DCI scrambled by temporary C-RNTI and/or C-RNTI, is detected, the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before the start of each Type-2 CSS and in 4 NB-IoT DL subframes after the end of each Type-2 CSS until the mac-ContentionResolutionTimer expires, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by the temporary C-RNTI or C-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by the temporary C-RNTI or C-RNTI as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- During CB-Msg3-EDT Procedure, when an NB-IoT UE is configured by higher layers to decode NPDCCH with CRC scrambled by CB-RNTI, before the DCI scrambled by CB-RNTI, is detected, the UE may assume NRSs are transmitted in the Type-2 CSS configured by higher layers, as well as in 10 NB-IoT DL subframes before the start of each Type-2 CSS and in 4 NB-IoT DL subframes after the end of each Type-2 CSS until the CB-Msg3ResponseTimer expires, where NB-IoT DL subframes without NRS are not counted. If a DCI scrambled by CB-RNTI is detected, the UE may assume NRSs are transmitted in the NPDSCH scheduled by the DCI scrambled by CB-RNTI as well as in 4 NB-IoT DL subframes before and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- An NB-IoT UE may assume NRSs are transmitted in NB-IoT DL subframes that are used for Type1A-NPDCCH common search space, and Type2A-NPDCCH common search space, as well as in 10 NB-IoT DL subframes prior and in 4 NB-IoT DL subframes after each Type1A-NPDCCH common search space and Type2A-NPDCCH common search space, where NB-IoT DL subframes without NRS are not counted. A UE may assume NRSs are transmitted in NB-IoT DL subframes carrying NPDSCH scheduled by DCI CRC scrambled by G-RNTI or SC-RNTI as well as in 4 NB-IoT DL subframes prior and after the scheduled NPDSCH, where NB-IoT DL subframes without NRS are not counted.

- In other cases, if frame structure type 1 is used, the UE may assume NRSs are transmitted in subframes #0, #4, #9, and in NB-IoT downlink subframes and shall not expect NRSs in other downlink subframes.

On an NB-IoT carrier for which DL-CarrierConfigDedicated-NB is present and no inbandCarrierInfo is present:

- If frame structure type 1 is used, the UE may assume NRSs are transmitted in subframes #0, #1, #3, #4, #9, and in NB-IoT downlink subframes and shall not expect NRSs in other downlink subframes.

On an NB-IoT carrier for which DL-CarrierConfigDedicated-NB is present and inbandCarrierInfo is present:

- If frame structure type 1 is used, the UE may assume NRSs are transmitted in subframes #0, #4, #9, and in NB-IoT downlink subframes and shall not expect NRSs in other downlink subframes.

An NB-IoT UE may assume NRSs are not transmitted in subframes that are configured by higher layer parameter nprsBitmap for narrowband positioning reference signal transmission.

#### 10.2.6.1 Sequence generation

The narrowband reference sequence shall be initialised according to clause 6.10.1.1 where ![](media_svg/image422.svg) [公式≈: _{N}_{ID}cell] is replaced with ![](media_svg/image423.svg) [公式≈: _{N}_{ID}Ncell].

#### 10.2.6.2 Mapping to resource elements

Narrowband reference signals are transmitted on one or two antenna ports ![](media_svg/image424.svg) [公式: p⎰{2000,2001}].

If the higher layer indicates UE may assume that ![](media_svg/image425.svg) [公式≈: _{N}_{ID}cell] is equal to ![](media_svg/image426.svg) [公式≈: _{N}_{ID}Ncell], UE may assume

- the number of antenna ports for the cell-specific reference signals as defined in clause 6.10.1 is the same as for the narrowband reference signals,

- the antenna ports for cell-specific reference signals {0, 1} are equivalent to antenna ports for narrowband reference signals {2000, 2001}, respectively, and

- the cell-specific reference signals are available in all subframes where the narrowband reference signals are available.

If the higher layer does not indicate UE may assume that ![](media_svg/image425.svg) [公式≈: _{N}_{ID}cell] is equal to ![](media_svg/image426.svg) [公式≈: _{N}_{ID}Ncell], UE may assume

- the number of antenna port for the cell-specific reference signals as defined in clause 6.10.1 is obtained from the higher layer parameter eutra-NumCRS-Ports,

- the cell-specific reference signals are available in all subframes where the narrowband reference signals are available, and

the cell-specific frequency shift for cell-specific reference signals as defined in clause 6.10.1.2 is given by ![](media_svg/image427.svg) [公式≈: v_{shift}=N_{ID}^{Ncell}mod6].

The reference signal sequence ![](media_svg/image428.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image11.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference symbols for antenna port ![](media_svg/image10.svg) [公式: p] in slot ![](media_svg/image429.svg) [公式≈: ^{n}s] according to

![](media_svg/image430.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image431.svg) [公式≈: _{m}_{m}k_{l}_{±}=_{=}_{=}_{=}6_{0}_{m}_{N}_{,}m_{1}_{symb}_{DL}_{+}+_{N}(v_{RB}_{max,}_{−}+_{2}v_{,}_{DL}_{N}_{shift}_{symb}_{DL}_{−})_{1}mod_{−}_{1}6]

When frame structure type 2 is used, the following values of $ l $ apply for the generation of NRSs in special subframes

- $ l=N_{symb}^{DL}-5,N_{symb}^{DL}-4 $ in each slot for special subframe configurations {3, 4, 8}

- $ l=N_{symb}^{DL}-5,N_{symb}^{DL}-4 $ in the first slot for special subframe configurations {9, 10}

- $ l=N_{symb}^{DL}-2,N_{symb}^{DL}-1 $ in the first slot for special subframe configurations {1, 2, 6, 7}.

The variables $\nu  $ and ![](media_svg/image432.svg) [公式≈: ^{v}shift] define the position in the frequency domain for the different reference signals where $\nu  $ is given by

![](media_svg/image433.svg) [公式≈: _{v}_{=}^{√}^{⌡}⌡⌡_{⌠}_{⌡}_{⌡}_{⌡}_{∞}3if 2000 and 1,4_{3if 2001 and 2,5}^{0if 2000 and 2,5}_{0if 2001 and 1,4}^{plNN}plNN_{plNN}_{plNN}^{=⎰−−}=⎰−−_{=⎰−−}_{=⎰−−}_{{}_{{}^{{}{_{symbsymb}_{symbsymb}^{symbsymb}symbsymb_{DLDL}_{DLDL}^{DLDL}^{DLDL}_{}}}_{}}^{}}]

The cell-specific frequency shift is given by ![](media_svg/image434.svg) [公式≈: v_{shift}=N_{ID}^{Ncell}mod6].

Resource elements ![](media_svg/image435.svg) [公式: (k,l)] used for transmission of narrowband reference signals on any of the antenna ports in a slot shall not be used for any transmission on any other antenna port in the same slot and set to zero.

Narrowband reference signals shall not be transmitted in subframes containing NPSS or NSSS.

For frame structure type 2, narrowband reference signals shall not be transmitted in special subframe for configurations 0 and 5.

Figure 10.2.6.2-1 illustrates the resource elements used for reference signal transmission according to the above definition. The notation ![](media_svg/image436.svg) [公式≈: ^{R}p] is used to denote a resource element used for reference signal transmission on antenna port![](media_svg/image10.svg) [公式: p].

![](media/image437.emf)

Figure 10.2.6.2-1. Mapping of downlink narrowband reference signals (normal cyclic prefix)

### 10.2.6A Narrowband positioning reference signal (NPRS)

Narrowband positioning reference signals (NPRSs) shall only be transmitted in resource blocks in NB-IoT carriers configured for NPRS transmission. In a subframe configured for NPRS transmission, the starting positions of the OFDM symbols configured for NPRS transmission shall be identical to those in a subframe in which all OFDM symbols have the same cyclic prefix length as the OFDM symbols configured for NPRS transmission. NPRS are defined for ![](media_svg/image356.svg) [公式: δf=15kHz]and normal CP only.

NPRSs are transmitted on antenna port 2006.

#### 10.2.6A.1 Sequence generation

The NPRS sequence ![](media_svg/image438.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] is defined by

![](media_svg/image439.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,2N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image440.svg) [公式≈: ^{n}s] is the slot number within a radio frame, ![](media_svg/image49.svg) [公式: l] is the OFDM symbol number within the slot. The pseudo-random sequence ![](media_svg/image256.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

![](media_svg/image441.svg) [公式≈: cinit=2^{28}∪√NID^{NPRS}512∃+2^{10}∪(7∪(ns+1)+l+1)∪(2∪(NID^{NPRS}mod512)+1)+2∪(NID^{NPRS}mod512)+NCP]

at the start of each OFDM symbol where ![](media_svg/image442.svg) [公式≈: N_{ID}^{NPRS}⎰{0,1,...,4095}] equals ![](media_svg/image443.svg) [公式≈: _{N}_{ID}Ncell] unless configured by higher layers and where ![](media_svg/image444.svg) [公式: N_{CP}=1.]

#### 10.2.6A.2 Mapping to resource elements

For an NB-IoT carrier which is configured for NPRS transmission, the reference signal sequence ![](media_svg/image445.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image11.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference signal for antenna port ![](media_svg/image446.svg) [公式: p] in slot ![](media_svg/image447.svg) [公式≈: ^{n}s] according to, for Type 1 NPRS:

![](media_svg/image448.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m&apos;)]

or for Type 2 NPRS:

$ a_{k,l}^{(p)}=r_{l,n_{s}}\left ( \left ( m'+2(n_{f}mod 64)\right ) mod 220\right ) $

according to higher layer configuration, where

- when the higher layer parameter operationModeInfoNPRS for the configured NB-IoT carrier is set to in-band

![](media_svg/image449.svg) [公式≈: l^{k}_{m}_{m}=_{±}^{=}_{=}_{=}^{√}^{⌡}⌠_{⌡}_{∞}^{6}1_{0}^{3}_{2}_{m}^{m},_{,}^{,}_{,}_{1}2^{5}_{3},_{+}^{+}^{,}_{,}3^{6}_{5},_{2}^{(}_{,}5_{6}^{6},_{n}6^{−}_{PRB}_{&apos;}^{l}^{+}^{if}if_{if}_{+}^{v}^{n}n_{n}^{shift}_{N}^{s}s_{s}^{mod}mod_{mod}_{RB}_{max,}^{)}^{mod}_{DL}^{2}2_{2}^{=}=_{=}^{6}_{−}1_{1}^{0}_{n}_{~}and_{and}(_{(}1_{4}or_{PBCH}2PBCH_{antenna}antenna_{ports}ports_{)})]

where ![](media_svg/image450.svg) [公式≈: _{n}_{PRB}&apos;] is signalled by higher layers nprs-SequenceInfo, and ![](media_svg/image451.svg) [公式: n^{~}=1] if the higher layer parameter nprs-SequenceInfo indicates ![](media_svg/image452.svg) [公式≈: _{N}_{RB}DL]is odd, and ![](media_svg/image453.svg) [公式: n^{~}=0] if the higher layer parameter nprs-SequenceInfo indicates ![](media_svg/image454.svg) [公式≈: _{N}_{RB}DL]is even.

- when the higher layer parameter operationModeInfoNPRS for the configured NB-IoT carrier is set to standalone or guard-band

![](media_svg/image455.svg) [公式≈: _{l}k_{m}_{m}_{=}_{&apos;}=_{=}_{=}_{0}6_{0}_{m}_{,}m_{1}_{,}_{1}_{,}_{+}+_{2}_{N}_{,}(6_{3}_{RB}_{max,}_{,}−_{4}l_{,}_{DL}+_{5}_{,}v_{6}_{−}_{shift}_{1})mod6]

and where ![](media_svg/image456.svg) [公式≈: v_{shift}=N_{ID}^{NPRS}mod6]. If ![](media_svg/image457.svg) [公式≈: _{N}_{ID}NPRS]is not configured by higher layers, ![](media_svg/image458.svg) [公式≈: _{N}_{ID}NPRS_{=}_{N}_{ID}Ncell]. The number of PBCH antenna ports is signalled by higher layers.

If higher layer parameter nprsBitmap is not configured, resource elements in OFDM symbols 5 and 6 in each slot shall not be used for transmission of NPRS. If the configured periodicity of Type 1 NPRS is equal to that of Type 2 NPRS, the UE is not expected to be configured with overlapped resource elements between Type 1 NPRS and Type 2 NPRS. Otherwise, a resource element configured for Type 1 NPRS shall not be used for Type 2 NPRS.

![](media/image459.emf)

Figure 10.2.6A.2-1: Mapping of NPRS (operationModeInfoNPRS is set to in-band, nprsBitmap configured)

![](media/image460.emf)

Figure 10.2.6A.2-2: Mapping of NPRS (operationModeInfoNPRS is set to standalone or guard-band, nprsBitmap configured)

#### 10.2.6A.3 NPRS subframe configuration

On a NB-IoT DL carrier configured for NPRS transmission, an NB-IoT UE can assume NPRSs are transmitted in DL subframes configured by all higher layer parameters nprsBitmap, the NB-IoT carrier-specific subframe configuration period ![](media_svg/image461.svg) [公式≈: ^{T}NPRS^{,}] the NB-IoT-carrier-specific starting subframe offset ![](media_svg/image462.svg) [公式≈: ^{Α}NPRS^{,}] and the number of consecutive downlink subframes ![](media_svg/image463.svg) [公式≈: ^{N}NPRS] where NPRS shall be transmitted. If frame structure type 2 is used, the UE shall not assume NPRSs are transmitted in special subframes.

- If ![](media_svg/image464.svg) [公式≈: ^{T}NPRS], ![](media_svg/image462.svg) [公式≈: ^{Α}NPRS^{,}] and ![](media_svg/image465.svg) [公式≈: ^{N}NPRS] are not configured for an NB-IoT downlink carrier configured for NPRS transmission, an NB-IoT UE shall assume NPRSs are transmitted in downlink subframes configured by higher layer parameter nprsBitmap.

- If nprsBitmap is not configured for an NB-IoT downlink carrier configured for NPRS transmission, an NB-IoT UE shall assume NPRSs are transmitted in downlink subframes configured by the higher layer parameters ![](media_svg/image464.svg) [公式≈: ^{T}NPRS], ![](media_svg/image462.svg) [公式≈: ^{Α}NPRS^{,}] and ![](media_svg/image465.svg) [公式≈: ^{N}NPRS].

- If the higher layer parameter operationModeInfoNPRS for the configured NB-IoT carrier is set to in-band, the higher layer parameters nprsBitmap shall be configured.

- If ![](media_svg/image464.svg) [公式≈: ^{T}NPRS], ![](media_svg/image462.svg) [公式≈: ^{Α}NPRS^{,}] and ![](media_svg/image465.svg) [公式≈: ^{N}NPRS] are configured, the NPRS instances in the first subframe of the ![](media_svg/image466.svg) [公式≈: ^{N}NPRS] downlink subframes, shall satisfy ![](media_svg/image467.svg) [公式≈: (10n_{f}+_{√}n_{s}/2_{∃}−Α_{NPRS}T_{NPRS})modT_{NPRS}=0].

The NPRSs shall not be mapped to resource elements ![](media_svg/image468.svg) [公式: (k,l)] allocated to resource blocks of NPBCH, NPSS, NSSS, or SystemInformationBlock-Type1-NB regardless of their antenna port ![](media_svg/image10.svg) [公式: p].

### 10.2.6B Narrowband wake up signal (NWUS)

#### 10.2.6B.1 Sequence generation

The NWUS sequence $ w(m)$ in subframe $ x=0, 1, \ldots  , M-1 $ is defined by

$ w\left ( m\right ) =\theta  _{n_{f},n_{s}}\left ( m'\right ) \cdot  e^{-\frac {j\pi  un\left ( n+1\right ) }{131}}e^{\frac {j2\pi  gm}{132}}$

$ m=0, 1,\ldots  , 131 $

$ m^{'}=m+132x $

$ n=mmod132 $

$\theta  _{n_{f},n_{s}}\left ( m'\right ) ={\begin {matrix}\begin {matrix}1,ifc_{n_{f},n_{s}}\left ( 2m'\right ) =0andc_{n_{f},n_{s}}\left ( 2m'+1\right ) =0 \\ -1,ifc_{n_{f},n_{s}}\left ( 2m'\right ) =0andc_{n_{f},n_{s}}\left ( 2m'+1\right ) =1\end {matrix} \\ \begin {matrix}j,ifc_{n_{f},n_{s}}\left ( 2m'\right ) =1andc_{n_{f},n_{s}}\left ( 2m'+1\right ) =0 \\ -j,ifc_{n_{f},n_{s}}\left ( 2m'\right ) =1andc_{n_{f},n_{s}}\left ( 2m'+1\right ) =1\end {matrix}\end {matrix}$

$ u=\left ( N_{ID}^{Ncell}mod126\right ) +3 $

where $ M $ is the actual duration of NWUS as defined in [4]. For a UE not configured with group NWUS, $ g=0 $. For a UE configured with group NWUS, $ g=14\left ( N_{group}^{WUS}+1\right ) $ for $ 0\leq  N_{group}^{WUS}\leq  7 $, where $ N_{group}^{WUS}$ is determined by the UE group to which the UE is associated as determined by higher layers [10]. In a resource that is not shared with non-group NWUS, the common NWUS sequence shall be determined by $ g=126 $. In a resource that is shared with non-group NWUS, the common NWUS sequence is determined by higher layers [9].

The scrambling sequence $ c_{n_{f},n_{s}}\left ( i\right ) , i=0, 1, \ldots  , 2\cdot  132M-1 $ is given by clause 7.2, and shall be initialized at the start of the NWUS with

$ c_{init\_WUS}=(N_{ID}^{Ncell}+1)\left ( \left ( 10n_{f\_start\_PO}+\lfloor  \frac {n_{s\_start\_PO}}{2}\rfloor  \right ) mod2048+1\right ) 2^{9}+N_{ID}^{Ncell}+N_{ID}^{resource}\cdot  2^{29}$

where $ n_{f\_start\_PO}$ is the first frame of the first PO to which the NWUS is associated, $ n_{s\_start\_PO}$ is the first slot of the first PO to which the NWUS is associated and $ N_{ID}^{resource}$ indicates the group NWUS resource to which the UE is associated. For a UE not configured with group NWUS, $ N_{ID}^{resource}=0 $, whereas for a UE configured with group NWUS, $ N_{ID}^{resource}$ is determined by higher layers [10].

#### 10.2.6B.2 Mapping to resource elements

The same antenna port shall be used for all symbols of the NWUS within a subframe. The UE shall not assume that the NWUS is transmitted on the same antenna port as any of the downlink reference signals or synchronization signals. If only one NRS port is configured by the eNB, the UE may assume the transmission of all NWUS subframes is using the same antenna port; otherwise, the UE may assume the same antenna port is used for NWUS transmission in DL subframes w0+2n and w0+2n+1, where w0 is the first DL subframe of the NWUS transmission as specified in [4], and n=0,1,….

The NWUS sequence is mapped to the set of subframes in the actual NWUS duration as defined in [4], where in a subframe #4 in which SystemInformationBlockType1-NB is transmitted or a subframe in which an SI message is transmitted, the subframe is counted in the NWUS mapping but not used for transmission of NWUS.On an NB-IoT carrier for which a UE receives higher-layer parameter operationModeInfo indicating inband-SamePCI, inband-DifferentPCI, guardband or standalone or on an NB-IoT carrier for which DL-CarrierConfigCommon-NB is present, the NWUS sequence $ w\left ( m\right ) $ shall be mapped to resource elements $(k,l)$ in sequence, starting with $ w(0)$ in increasing order of first the index $ k=0,1,\ldots  ,N_{sc}^{RB}-1,$ over the 12 assigned subcarriers and then the index $ l=3, 4, \ldots  , 2N_{symb}^{DL}-1 $ in each subframe in which NWUS is transmitted.

Additionally, on an NB-IoT carrier for which a UE receives higher-layer parameter operationModeInfo indicating guardband or standalone, or on an NB-IoT carrier for which DL-CarrierConfigCommon-NB is present and no inbandCarrierInfo is present, the resource mapping for the first three OFDM symbols in the subframe is performed as follows:

- The resource element (k,7) is mapped to resource element (k,0) of every index k over 12 assigned subcarriers

- The resource element (k,8) is mapped to resource element (k,1) of every index k over 12 assigned subcarriers

- The resource element (k,9) is mapped to resource element (k,2) of every index k over 12 assigned subcarriers

A resource element $(k,l)$ overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted or NRSs according to clause 10.2.6 are transmitted shall not be used for NWUS transmission but is counted in the mapping process.

### 10.2.7 Synchronization signals

There are 504 unique physical-layer cell identities indicated by the narrowband secondary synchronization signal.

#### 10.2.7.1 Narrowband primary synchronization signal (NPSS)

##### 10.2.7.1.1 Sequence generation

The sequence ![](media_svg/image469.svg) [公式: d_{l}(n)] used for the narrowband primary synchronization signal is generated from a frequency-domain Zadoff-Chu sequence according to

![](media_svg/image470.svg) [公式≈: d_{l}(n)=S(l)∪e^{−}^{j}^{Π}^{un}^{11}^{(}^{n}^{+}^{1}^{)},n=0,1,...,10]

where the Zadoff-Chu root sequence index ![](media_svg/image471.svg) [公式: u=5] and ![](media_svg/image472.svg) [公式: S(l)]for different symbol indices ![](media_svg/image473.svg) [公式: l] is given by Table 10.2.7.1.1-1.

Table 10.2.7.1.1-1: Definition of ![](media_svg/image474.svg) [公式: S(l)].

| Cyclic prefix length | ![](media_svg/image475.svg) [公式: S(3),...,S(13)] |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 1 | 1 | 1 | 1 | -1 | -1 | 1 | 1 | 1 | -1 | 1 |

##### 10.2.7.1.2 Mapping to resource elements

The same antenna port shall be used for all symbols of the narrowband primary synchronization signal within a subframe.

UE shall not assume that the narrowband primary synchronization signal is transmitted on the same antenna port as any of the downlink reference signals. The UE shall not assume that the transmissions of the narrowband primary synchronization signal in a given subframe use the same antenna port, or ports, as the narrowband primary synchronization signal in any other subframe.

The sequences ![](media_svg/image476.svg) [公式: d_{l}(n)] shall be mapped to resource elements ![](media_svg/image405.svg) [公式: (k,l)] in increasing order of first the index ![](media_svg/image477.svg) [公式: k=0,1,...,N_{sc}^{RB}−2] and then the index ![](media_svg/image478.svg) [公式≈: l=3,4,...,2N_{symb}^{DL}−1] in subframe 5 in every radio frame. For resource elements ![](media_svg/image405.svg) [公式: (k,l)] overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted, the corresponding sequence element ![](media_svg/image479.svg) [公式: d(n)] is not used for the NPSS but counted in the mapping process.

#### 10.2.7.2 Narrowband secondary synchronization signal (NSSS)

##### 10.2.7.2.1 Sequence generation

The sequence ![](media_svg/image480.svg) [公式: d(n)] used for the narrowband secondary synchronization signal is generated from a frequency-domain Zadoff-Chu sequence according to

![](media_svg/image481.svg) [公式≈: d(n)=b_{q}(m)e^{−}^{j}^{2}^{ΠΘ}^{f}^{n}e^{−}^{j}^{Π}^{u}^{n}^{131}^{±}^{(}^{n}^{±}^{+}^{1}^{)}]

where

![](media_svg/image482.svg) [公式≈: _{u}n_{n}_{m}_{q}_{±}=_{=}_{=}_{=}_{=}0_{⋅}_{⋅}_{⋅}_{√}_{N}_{n}_{n},_{N}1_{ID}_{mod}_{mod}_{Ncell}_{126},...,_{ID}_{Ncell}131_{mod}_{128}_{131}_{∂}_{∂}_{∂}_{∃}_{126}_{+}_{3}]

The binary sequence ![](media_svg/image483.svg) [公式: b_{q}(m)] is given by Table 10.2.7.2.1-1. The cyclic shift ![](media_svg/image484.svg) [公式≈: ^{Θ}f]in frame number ![](media_svg/image485.svg) [公式≈: ^{n}f] is given by

![](media_svg/image486.svg) [公式≈: Θ_{f}=_{132}^{33}(n_{f}/2)mod4].

Table 10.2.7.2.1-1: Definition of ![](media_svg/image483.svg) [公式: b_{q}(m)].

| ![](media_svg/image487.svg) [公式: q] | ![](media_svg/image488.svg) [公式: b_{q}(0),...,b_{q}(127)] |
| --- | --- |
| 0 | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] |
| 1 | [1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1] |
| 2 | [1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1] |
| 3 | [1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1  -1  1  1  -1  1  -1  -1  1  -1  1  1  -1  1  -1  -1  1  1  -1  -1  1  -1  1  1  -1] |

##### 10.2.7.2.2 Mapping to resource elements

The same antenna port shall be used for all symbols of the narrowband secondary synchronization signal within a subframe.

The UE shall not assume that the narrowband secondary synchronization signal is transmitted on the same antenna port as any of the downlink reference signals. The UE shall not assume that the transmissions of the narrowband secondary synchronization signal in a given subframe use the same antenna port, or ports, as the narrowband secondary synchronization signal in any other subframe.

If indicated by higher layer, a UE may assume different precoders are applied for NSSS transmission in a number of consecutive NSSS occasions signalled by higher layer.

The sequence ![](media_svg/image479.svg) [公式: d(n)] shall be mapped to resource elements ![](media_svg/image405.svg) [公式: (k,l)] in sequence starting with ![](media_svg/image489.svg) [公式: d(0)] in increasing order of first the index ![](media_svg/image265.svg) [公式: k] over the 12 assigned subcarriers and then the index![](media_svg/image145.svg) [公式: l] over the assigned last ![](media_svg/image490.svg) [公式≈: _{N}_{symb}NSSS] symbols of subframe 9 for frame structure type 1 or subframe 0 for frame structure type 2  in radio frames fulfilling ![](media_svg/image491.svg) [公式: n_{f}mod2=0], where ![](media_svg/image492.svg) [公式≈: _{N}_{symb}NSSS] is given by Table 10.2.7.2.2-1.

Table 10.2.7.2.2-1: NSSS number of symbols

| Cyclic prefix length | ![](media_svg/image493.svg) [公式≈: _{N}_{symb}NSSS] |
| --- | --- |
| Normal | 11 |

For resource elements ![](media_svg/image494.svg) [公式: (k,l)] overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted, the corresponding sequence element ![](media_svg/image479.svg) [公式: d(n)] is not used for the NSSS but counted in the mapping process.

### 10.2.8 OFDM baseband signal generation

For an NB-IoT carrier

- for which the higher layer parameter operationModeInfo indicates 'inband-DifferentPCI ' and for all NB-IoT downlink physical channels and signals except NPRS,

- for which the higher layer parameter operationModeInfo indicates 'Guardband ' or 'Standalone ',

- for an NB-IoT carrier for which the higher layer parameter CarrierConfigDedicated-NB or DL-CarrierConfigCommon-NB is present and no inbandCarrierInfo is present, or

- for an NB-IoT carrier for which the higher layer parameters CarrierConfigDedicated-NB or DL-CarrierConfigCommon-NB is present and inbandCarrierInfo is present and the higher layers do not indicate ![](media_svg/image408.svg) [公式≈: _{N}_{ID}Ncell] is the same as ![](media_svg/image407.svg) [公式≈: _{N}_{ID}cell] and for all NB-IoT downlink physical channels and signals except NPRS,

the time-continuous signal ![](media_svg/image495.svg) [公式≈: s_{l}^{(}^{p}^{)}(t)] on antenna port ![](media_svg/image10.svg) [公式: p] in OFDM symbol ![](media_svg/image145.svg) [公式: l] in a downlink slot is defined by

![](media_svg/image496.svg) [公式≈: _{s}_{l}(p)_{(}_{t}_{)}_{=}_{k}^{⊥}_{=}^{N}_{−}^{sc}^{RB}_{⊆}_{√}_{N}^{/}_{sc}_{RB}^{2}^{∀}^{−}_{/}^{1}_{2}_{∃}_{a}_{k}(_{(}p_{−})_{)}_{,}_{l}_{∪}_{e}j2Π(k+1/2)δf(t−NCP,lTs)]

for![](media_svg/image497.svg) [公式≈: 0≥t<(N_{CP}_{,}_{l}+N)≠T_{s}] where ![](media_svg/image498.svg) [公式≈: k^{(}^{−}^{)}=k+√Nsc^{RB}2∃], $ N=2048 $, ![](media_svg/image278.svg) [公式: δf=15kHz] and ![](media_svg/image499.svg) [公式≈: _{a}_{k}(_{,}p_{l})] is the content of resource element ![](media_svg/image7.svg) [公式: (k,l)] on antenna port ![](media_svg/image500.svg) [公式: p].

Otherwise, the time-continuous signal ![](media_svg/image501.svg) [公式≈: ^{s}l^{(}&apos;^{p}^{)}^{(}^{t}^{)}] on antenna port ![](media_svg/image10.svg) [公式: p] in OFDM symbol ![](media_svg/image502.svg) [公式: l&apos;], where ![](media_svg/image503.svg) [公式≈: l&apos;=l+N_{symb}^{DL}(n_{s}mod4)⎰{0,...,27}] is the OFDM symbol index from the start of the last even-numbered subframe, is defined by

![](media_svg/image504.svg) [公式≈: _{s}_{l}(_{&apos;}p)_{(}_{t}_{)}_{=}_{k}_{=}_{−}_{√}_{N}_{⊆}_{RB}_{DL}−1_{N}_{sc}_{RB}_{/}_{2}_{∃}_{e}Θk(−),l&apos;_{a}_{k}(_{(}p_{−})_{)}_{,}_{l}_{&apos;}_{∪}_{e}j2Πkδf^{⊇}⊕⊕⊗t−NCP,l&apos;modNsymbDLTs^{⇒}⇐⇐⇔_{+}⊥NRB^{DL}_{⊆}N_{k}_{=}sc^{RB}_{1}/2∀_{e}Θk(+),l&apos;_{a}_{k}(_{(}p_{+})_{)}_{,}_{l}_{&apos;}_{∪}_{e}j2Πkδf^{⊇}⊕⊕⊗t−NCP,l&apos;modNsymbDLTs^{⇒}⇐⇐⇔]

for ![](media_svg/image505.svg) [公式≈: 0≥t<(N_{CP}_{,}_{l}+N)≠T_{s}] where ![](media_svg/image506.svg) [公式≈: k^{(}^{−}^{)}=k+√NRB^{DL}Nsc^{RB}2∃] and![](media_svg/image507.svg) [公式≈: k^{(}^{+}^{)}=k+√NRB^{DL}Nsc^{RB}2∃−1], ![](media_svg/image508.svg) [公式≈: ^{Θ}k,l&apos;^{=}^{j}^{2}^{Π}^{f}NB−IoT^{T}s^{⊇}^{⊕}_{⊕}_{⊗}^{l}^{&apos;}^{N}^{+}⊆_{i}_{=}^{l}^{&apos;}_{0}^{N}CP,imod7^{⇒}^{⇐}_{⇐}_{⇔}] if resource element ![](media_svg/image509.svg) [公式: (k,l&apos;)]is used for Narrowband IoT except for NPRS, and 0 otherwise including NPRS. The quantity $ f_{NB-IoT}$ is the frequency location of the center of the Narrowband IoT PRB minus the frequency location of the center of the LTE signal.

Only normal CP is supported for Narrowband IoT downlink in this release of the specification.

### 10.2.9 Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued OFDM baseband signal for each antenna port is shown in Figure 6.13-1. The filtering required prior to transmission is defined by the requirements in TS36.104 [6].

###### Annex A (informative):
Change history

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | TSG # | TSG Doc. | CR | Rev | Subject/Comment | Old | New |
| 2006-09-24 | - | - | - |  | Draft version created | - | 0.0.0 |
| 2006-10-09 | - | - | - |  | Updated skeleton | 0.0.0 | 0.0.1 |
| 2006-10-13 | - | - | - |  | Endorsed by RAN1 | 0.0.1 | 0.1.0 |
| 2006-10-23 | - | - | - |  | Inclusion of decision from RAN1#46bis | 0.1.0 | 0.1.1 |
| 2006-11-06 | - | - | - |  | Updated editor 's version | 0.1.1 | 0.1.2 |
| 2006-11-09 | - | - | - |  | Updated editor 's version | 0.1.2 | 0.1.3 |
| 2006-11-10 | - | - | - |  | Endorsed by RAN1#47 | 0.1.3 | 0.2.0 |
| 2006-11-27 | - | - | - |  | Editor 's version, including decisions from RAN1#47 | 0.2.0 | 0.2.1 |
| 2006-12-14 | - | - | - |  | Updated editor 's version | 0.2.1 | 0.2.2 |
| 2007-01-15 | - | - | - |  | Updated editor 's version | 0.2.2 | 0.2.3 |
| 2007-01-19 | - | - | - |  | Endorsed by RAN1#47bis | 0.2.3 | 0.3.0 |
| 2007-02-01 | - | - | - |  | Editor 's version, including decisions from RAN1#47bis | 0.3.0 | 0.3.1 |
| 2007-02-12 | - | - | - |  | Updated editor 's version | 0.3.1 | 0.3.2 |
| 2007-02-16 | - | - | - |  | Endorsed by RAN1#48 | 0.3.2 | 0.4.0 |
| 2007-02-16 | - | - | - |  | Editor 's version, including decisions from RAN1#48 | 0.4.0 | 0.4.1 |
| 2007-02-21 | - | - | - |  | Updated editor 's version | 0.4.1 | 0.4.2 |
| 2007-03-03 | RP_35 | RP-070169 |  |  | For information at RAN#35 | 0.4.2 | 1.0.0 |
| 2007-04-25 | - | - | - |  | Editor 's version, including decisions from RAN1#48bis and RAN1 TDD Ad Hoc | 1.0.0 | 1.0.1 |
| 2007-05-03 | - | - | - | - | Updated editor 's version | 1.0.1 | 1.0.2 |
| 2007-05-08 | - | - | - | - | Updated editor 's version | 1.0.2 | 1.0.3 |
| 2007-05-11 | - | - | - | - | Updated editor 's version | 1.0.3 | 1.0.4 |
| 2007-05-11 | - | - | - | - | Endorsed by RAN1#49 | 1.0.4 | 1.1.0 |
| 2007-05-15 | - | - | - | - | Editor 's version, including decisions from RAN1#49 | 1.1.0 | 1.1.1 |
| 2007-06-05 | - | - | - | - | Updated editor 's version | 1.1.1 | 1.1.2 |
| 2007-06-25 | - | - | - | - | Endorsed by RAN1#49bis | 1.1.2 | 1.2.0 |
| 2007-07-10 | - | - | - | - | Editor 's version, including decisions from RAN1#49bis | 1.2.0 | 1.2.1 |
| 2007-08-10 | - | - | - | - | Updated editor 's version | 1.2.1 | 1.2.2 |
| 2007-08-20 | - | - | - | - | Updated editor 's version | 1.2.2 | 1.2.3 |
| 2007-08-24 | - | - | - | - | Endorsed by RAN1#50 | 1.2.3 | 1.3.0 |
| 2007-08-27 | - | - | - | - | Editor 's version, including decisions from RAN1#50 | 1.3.0 | 1.3.1 |
| 2007-09-05 | - | - | - | - | Updated editor 's version | 1.3.1 | 1.3.2 |
| 2007-09-08 | RP_37 | RP-070729 | - | - | For approval at RAN#37 | 1.3.2 | 2.0.0 |
| 12/09/07 | RP_37 | RP-070729 |  |  | Approved version | 2.0.0 | 8.0.0 |
| 28/11/07 | RP_38 | RP-070949 | 0001 | - | Introduction of optimized FS2 for TDD | 8.0.0 | 8.1.0 |
| 28/11/07 | RP_38 | RP-070949 | 0002 | - | Introduction of scrambling sequences, uplink reference signal sequences, secondary synchronization sequences and control channel processing | 8.0.0 | 8.1.0 |
| 05/03/08 | RP_39 | RP-080219 | 0003 | 1 | Update of uplink reference-signal hopping, downlink reference signals, scrambling sequences, DwPTS/UpPTS lengths for TDD and control channel processing | 8.1.0 | 8.2.0 |
| 28/05/08 | RP_40 | RP-080432 | 0004 | - | Correction of the number of subcarriers in PUSCH transform precoding | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0005 | - | Correction of PHICH mapping | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0006 | - | Correction of PUCCH resource index for PUCCH format 2 | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0007 | 3 | Correction of the predefined hopping pattern for PUSCH | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0008 | - | Non-binary hashing functions | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0009 | 1 | PUCCH format 1 | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0010 | 1 | CR on Uplink DM RS hopping | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0012 | 1 | Correction to limitation of constellation size of ACK transmission in PUSCH | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0015 | 1 | PHICH mapping for one and two antenna ports in extended CP | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0016 | 1 | Correction of PUCCH in absent of mixed format | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0017 | - | Specification of CCE size and PHICH resource indication | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0018 | 3 | Correction of the description of frame structure type 2 | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0019 | - | On Delta^pucch_shift correction | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0021 | - | Corrections to Secondary Synchronization Signal Mapping | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0022 | - | Downlink VRB mapping to PRB for distributed transmission | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0023 | - | Clarification of modulation symbols to REs mapping for DVRB | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0024 | 1 | Consideration on the scrambling of PDSCH | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0025 | - | Corrections to Initialization of DL RS Scrambling | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0026 | 1 | CR on Downlink RS | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0027 | - | CR on Uplink RS | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0028 | 1 | Fixed timing advance offset for LTE TDD and half-duplex FDD | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0029 | 1 | Timing of random access preamble format 4 | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0030 | 1 | Uplink sounding RS bandwidth configuration | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0031 | - | Use of common RS when UE-specific RS are configured | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0032 | 1 | Uplink RS Updates | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0033 | - | Orthogonal cover sequence for shortened PUCCH format 1a and 1b | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0034 | - | Clarification of PDCCH mapping | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0035 | - | TDD PRACH time/frequency mapping | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0036 | - | Cell Specific Uplink Sounding RS Subframe Configuration | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0038 | - | PDCCH length for carriers with mixed MBSFN and Unicast Traffic | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0040 | - | Correction to the scrambling sequence generation for PUCCH, PCFICH, PHICH, MBSFN RS and UE specific RS | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0041 | - | PDCCH coverage in narrow bandwidths | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0042 | - | Closed-Loop and Open-Loop Spatial Multiplexing | 8.2.0 | 8.3.0 |
| 28/05/08 | RP_40 | RP-080432 | 0043 | - | Removal of small-delay CDD | 8.2.0 | 8.3.0 |
| 09/09/08 | RP_41 | RP-080668 | 48 | 1 | Frequency Shifting of UE-specific RS | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 49 | 1 | Correction of PHICH to RE mapping in extended CP subframe | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 50 | - | Corrections to for handling remaining Res | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 51 | - | PRACH configuration for frame structure type 1 | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 52 | 2 | Correction of PUCCH index generation formula | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 53 | - | Orthogonal cover sequence for shortened PUCCH format 1a and 1b | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 54 | - | Correction of mapping of ACK/NAK to binary bit values | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 56 | 2 | Remaining issues on SRS hopping | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 57 | 1 | Correction of n_cs(n_s) and OC/CS remapping for PUCCH formats 1/1a/1b and 2/2a/2b | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 59 | - | Corrections to Rank information scrambling in Uplink Shared Channel | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 60 | - | Definition on the slot number for frame structure type 2 | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 61 | - | Correction of the Npucch sequence upper limit for the formats 1/1a/1b | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 62 | 1 | Clarifications for DMRS parameters | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 63 | - | Correction of n_prs | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 64 | 1 | Introducing missing L1 parameters to 36.211 | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 65 | 3 | Clarification on reception of synchronization signals | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 66 | - | Correction to the downlink/uplink timing | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 67 | - | ACK/NACK Scrambling scheme on PUCCH | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 68 | - | DCI format1C | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 69 | - | Refinement for REG Definition for n = 4 | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 71 | - | Correcting Ncs value for PRACH preamble format 0-3 | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 73 | - | Correction of the half duplex timing advance offset value | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 74 | - | Correction to Precoding for Transmit Diversity | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 75 | - | Clarification on number of OFDM symbols used for PDCCH | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 77 | - | Number of antenna ports for PDSCH | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 78 | - | Correction to Type 2 PUSCH predetermined hopping for Nsb=1 operation | 8.3.0 | 8.4.0 |
| 09/09/08 | RP_41 | RP-080668 | 79 | - | PRACH frequency location | 8.3.0 | 8.4.0 |
| 03/12/08 | RP_42 | RP-081074 | 70 | 1 | Correction for the definition of UE-specific reference signals | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 72 | 2 | Corrections to precoding for large delay CDD | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 80 | - | Correction to the definition of nbar_oc for extended CP | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 81 | 1 | Specification of reserved REs not used for RS | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 82 | 2 | Clarification of the random access preamble transmission timing | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 83 | 1 | Indexing of PRACH resources within the radio frame | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 84 | 6 | Alignment of RAN1/RAN2 specification | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 86 | - | Clarification on scrambling of ACK/NAK bits for PUCCH format 2a/2b | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 87 | - | Correction of introduction of shortened SR | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 88 | - | Corrections to 36.211 | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 89 | - | Clarification on PUSCH DM RS Cyclic Shift Hopping | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 92 | 1 | Correction to the uplink DM RS assignment | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 93 | - | Clarify the RNTI used in scrambling sequence initialization | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 94 | 1 | On linkage Among UL Power Control Parameters | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 95 | - | Clarification on PUSCH pre-determined hopping pattern | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 96 | - | Clarification of SRS sequence-group and base sequence number | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 97 | 1 | SRS subframe configuration | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 98 | - | Remaining SRS details for TDD | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 99 | - | Clarifying UL VRB Allocation | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 100 | - | Clarification on PUCCH resource hopping | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 101 | - | Correction for definition of Qm and a pseudo code syntax error in Scrambling. | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 105 | 1 | Remaining Issues on SRS of TDD | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 106 | - | Correction of reference to RAN4 specification of supported uplink bandwidth | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 107 | - | General corrections to SRS | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 109 | 2 | Correction to PCFICH specification | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 110 | 1 | Correction to Layer Mapping for Transmit Diversity with Four Antenna Ports | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 111 | - | Correction of the mapping of cyclic shift filed in DCI format 0 to the dynamic cyclic shift offset | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 112 | - | DRS collision handling | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 113 | - | Clarification to enable reuse of non-active PUCCH CQI RBs for PUSCH | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 114 | 1 | PUSCH Mirror Hopping operation | 8.4.0 | 8.5.0 |
| 03/12/08 | RP_42 | RP-081074 | 108 | 1 | Extended and normal cyclic prefix in DL and UL for LTE TDD | 8.4.0 | 8.5.0 |
| 04/03/09 | RP_43 | RP-090234 | 115 | 1 | Alignment of PRACH configuration index for FS type 1 and type 2 | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 118 | 1 | Clarification for DRS Collision handling | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 121 | 1 | Removing inverse modulo operation | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 123 | 1 | Clarification on the use of preamble format 4 | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 124 | - | Clarification of RNTI used in scrambling sequence | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 125 | 1 | Clarifying PDCCH RE mapping | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 126 | - | Correction of preamble format 4 timing | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 127 | 2 | Corrections to SRS | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 128 | 2 | Clarification of PDSCH Mapping to Resource Elements | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 129 | 1 | Alignment with correct ASN1 parameter names | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 130 | - | Correction to PUCCH format 1 mapping to physical resources | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 132 | - | Correction to type-2 PUSCH hopping | 8.5.0 | 8.6.0 |
| 04/03/09 | RP_43 | RP-090234 | 134 | - | Alignment of SRS configuration | 8.5.0 | 8.6.0 |
| 27/05/09 | RP_44 | RP-090527 | 135 | - | Correction on UE behavior for PRACH 20ms periodicity | 8.6.0 | 8.7.0 |
| 15/09/09 | RP_45 | RP-090888 | 137 | 1 | Clarification on DMRS sequence for PUSCH | 8.7.0 | 8.8.0 |
| 15/09/09 | RP_45 | RP-090888 | 138 | 1 | Correction to PHICH resource mapping for TDD and to PHICH scrambling | 8.7.0 | 8.8.0 |
| 01/12/09 | RP_46 | RP-091168 | 142 | - | Clarification of the transmit condition for UE specific reference signals | 8.8.0 | 8.9.0 |
| 01/12/09 | RP_46 | RP-091172 | 139 | 2 | Introduction of LTE positioning | 8.9.0 | 9.0.0 |
| 01/12/09 | RP_46 | RP-091177 | 140 | 3 | Editorial corrections to 36.211 | 8.9.0 | 9.0.0 |
| 01/12/09 | RP_46 | RP-091257 | 141 | 1 | Introduction of enhanced dual layer transmission | 8.9.0 | 9.0.0 |
| 16/03/10 | RP_47 | RP-100209 | 144 | 1 | Removal of square brackets on positioning subframe periodicities | 9.0.0 | 9.1.0 |
| 16/03/10 | RP_47 | RP-100209 | 145 | - | Clarification of the CP length of empty OFDM symbols in PRS subframes | 9.0.0 | 9.1.0 |
| 16/03/10 | RP_47 | RP-100210 | 146 | - | Clarification of MBSFN subframe definition | 9.0.0 | 9.1.0 |
| 07/12/10 | RP_50 | RP-101320 | 148 | - | Introduction of Rel-10 LTE-Advanced features in 36.211 | 9.1.0 | 10.0.0 |
| 15/03/11 | RP_51 | RP-110254 | 149 | 1 | Correction on UE behavior for PRACH preamble format 4 | 10.0.0 | 10.1.0 |
| 15/03/11 | RP_51 | RP-110256 | 150 | - | Corrections to Rel-10 LTE-Advanced features in 36.211 | 10.0.0 | 10.1.0 |
| 01/06/11 | RP_52 | RP-110818 | 153 | 2 | PUSCH interaction with periodic SRS | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110819 | 154 | 1 | Correction on describing PUCCH format 3 | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110821 | 155 | 3 | Correction on codebooks for CSI-RS based feedback for up to 4 CSI-RS ports. | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110821 | 156 | - | Correction on overlapping non-zero-power and zero-power CSI-RS configurations | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110821 | 157 | - | Correction on CSI-RS configuration | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110821 | 158 | - | PDSCH transmission in MBSFN subframes | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110823 | 159 | - | Correction on implicit derivation of transmission comb per antenna port for SRS | 10.1.0 | 10.2.0 |
| 01/06/11 | RP_52 | RP-110823 | 160 | - | Uplink DMRS sequence in RACH procedure | 10.1.0 | 10.2.0 |
| 15/09/11 | RP_53 | RP-111229 | 162 | - | Corrections on DMRS for Extended CP | 10.2.0 | 10.3.0 |
| 15/09/11 | RP_53 | RP-111228 | 163 | - | Clarification of applicability of precoding power scaling factors for PDSCH | 10.2.0 | 10.3.0 |
| 15/09/11 | RP_53 | RP-111228 | 164 | - | Correction to modulation and upconversion on PRACH | 10.2.0 | 10.3.0 |
| 15/09/11 | RP_53 | RP-111229 | 165 | - | Clarification on cyclic prefix of PDSCH in MBSFN subframes | 10.2.0 | 10.3.0 |
| 15/09/11 | RP_53 | RP-111229 | 166 | 3 | Corrections on indication in scrambling identity field in DCI format 2B and 2C | 10.2.0 | 10.3.0 |
| 05/12/11 | RP_54 | RP-111668 | 167 | - | A correction to PDSCH precoding for CQI calculation | 10.3.0 | 10.4.0 |
| 05/12/11 | RP_54 | RP-111668 | 168 | - | Correction to figure of CSI-RS pattern in extended-CP subframe | 10.3.0 | 10.4.0 |
| 13/06/12 | RP_56 | RP-120736 | 169 | - | Correction to resource mapping for PDSCH | 10.4.0 | 10.5.0 |
| 13/06/12 | RP_56 | RP-120739 | 171 | - | Correction for DMRS group hopping and sequence hopping | 10.4.0 | 10.5.0 |
| 13/06/12 | RP_56 | RP-120738 | 172 | - | Correction to assumed CSI-RS transmissions in subframes used for paging | 10.4.0 | 10.5.0 |
| 04/09/12 | RP_57 | RP-121274 | 170 | 4 | Introduction of an additional special subframe configuration | 10.5.0 | 11.0.0 |
| 04/09/12 | RP_57 | RP-121272 | 173 | - | Inclusion of Rel-11 features | 10.5.0 | 11.0.0 |
| 04/12/12 | RP_58 | RP-121839 | 175 | - | Correction to assumed CSI-RS transmissions in secondary cells | 11.0.0 | 11.1.0 |
| 04/12/12 | RP_58 | RP-121846 | 176 | - | Correction to assumed CSI-RS transmissions in secondary cells | 11.0.0 | 11.1.0 |
| 26/02/13 | RP_59 | RP-130254 | 178 | - | Clarification of CSI RS mapping to resource elements | 11.1.0 | 11.2.0 |
| 26/02/13 | RP_59 | RP-130254 | 180 | - | Correction to CSI Reference Signals | 11.1.0 | 11.2.0 |
| 26/02/13 | RP_59 | RP-130255 | 181 | - | Additional clarifications/corrections for introducing Rel-11 features | 11.1.0 | 11.2.0 |
| 11/06/13 | RP_60 | RP-130752 | 182 | - | Correction to EPDCCH PRB pair indication | 11.2.0 | 11.3.0 |
| 11/06/13 | RP_60 | RP-130752 | 183 | - | CR on collision between EPDCCH and PSS/SSS/PBCH | 11.2.0 | 11.3.0 |
| 03/09/13 |  |  |  |  | MCC clean-up | 11.3.0 | 11.4.0 |
| 03/09/13 | RP_60 | RP-131250 | 185 | - | Correction to QCL behaviour on CRS | 11.3.0 | 11.4.0 |
| 03/12/13 | RP_62 | RP-131894 | 186 | - | Correction on the derivation of the non-MBSFN region by PCFICH | 11.4.0 | 11.5.0 |
| 03/12/13 | RP_62 | RP-131896 | 184 | 3 | Introduction of Rel 12 feature for Downlink MIMO Enhancement | 11.5.0 | 12.0.0 |
| 03/03/14 | RP_63 | RP-140286 | 187 | - | On PMCH starting symbol in an MBSFN subframe | 12.0.0 | 12.1.0 |
| 10/06/14 | RP_64 | RP-140858 | 189 | - | CR on antenna port definitions | 12.1.0 | 12.2.0 |
| 10/06/14 | RP_64 | RP-140858 | 190 | 1 | Clarification of downlink subframes | 12.1.0 | 12.2.0 |
| 10/06/14 | RP_64 | RP-140862 | 191 | - | Inclusion of eIMTA, TDD-FDD CA, and coverage enhancements | 12.1.0 | 12.2.0 |
| 10/09/14 | RP_65 | RP-141485 | 192 | - | Inclusion of low-cost MTC and 256QAM | 12.2.0 | 12.3.0 |
| 10/09/14 | RP_65 | RP-141477 | 194 | - | CR on port 5 UE-specific reference signal when PDSCH is overlapped with EPDCCH | 12.2.0 | 12.3.0 |
| 08/12/14 | RP_66 | RP-142098 | 195 | 3 | Clarification of PUSCH rate matching with SRS | 12.3.0 | 12.4.0 |
| 08/12/14 | RP_66 | RP-142106 | 197 | 4 | Inclusion of small-cell enhancements | 12.3.0 | 12.4.0 |
| 09/03/15 | RP_67 | RP-150366 | 196 | 7 | Inclusion of ProSe | 12.4.0 | 12.5.0 |
| 09/03/15 | RP_67 | RP-150364 | 198 | - | Correction on 256QAM applicability to PMCH | 12.4.0 | 12.5.0 |
| 09/03/15 | RP_67 | RP-150364 | 199 | - | Correction of discovery signal transmission | 12.4.0 | 12.5.0 |
| 15/06/15 | RP_68 | RP-150935 | 201 | - | Alignment of ProSe parameters | 12.5.0 | 12.6.0 |
| 14/09/15 | RP_69 | RP-151465 | 203 | - | Clarification on SRS BW configuration | 12.6.0 | 12.7.0 |
| 07/12/15 | RP_70 | RP-152036 | 209 | 1 | Modify max TA for dual connectivity | 12.7.0 | 12.8.0 |
| 07/12/15 | RP_70 | RP-152025 | 206 | 2 | Introduction of EB/FD-MIMO | 12.8.0 | 13.0.0 |
| 07/12/15 | RP_70 | RP-152027 | 208 | 1 | Introduction of Rel-13 eCA | 12.8.0 | 13.0.0 |
| 07/12/15 | RP_70 | RP-152125 | 204 | 2 | eD2D CR for 36.211 | 12.8.0 | 13.0.0 |
| 07/12/15 | RP_70 | RP-152258 | 205 | 4 | Introduction of LAA | 12.8.0 | 13.0.0 |

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2016-03 | RAN#71 | RP-160359 | 210 | - | F | Alignment eD2D CR for 36.211 | 13.1.0 |
| 2016-03 | RAN#71 | RP-160367 | 212 | - | F | Clarification on PDSCH collision with PSS/SSS/PBCH | 13.1.0 |
| 2016-03 | RAN#71 | RP-160357 | 213 | - | F | Correction on support of CA with up to 32 CCs | 13.1.0 |
| 2016-03 | RAN#71 | RP-160357 | 214 | - | F | Correction on PUCCH format 4 and 5 | 13.1.0 |
| 2016-03 | RAN#71 | RP-160360 | 217 | - | F | Correction on DRS subframe in 36.211 | 13.1.0 |
| 2016-03 | RAN#71 | RP-160360 | 218 | - | F | Correction on EPDCCH start symbol in LAA | 13.1.0 |
| 2016-03 | RAN#71 | RP-160360 | 219 | - | F | Correction to MBSFN subframe configuration | 13.1.0 |
| 2016-03 | RAN#71 | RP-160358 | 220 | - | F | CR on CSI-RS configuration for more than eight antenna ports in 36.211 | 13.1.0 |
| 2016-03 | RAN#71 | RP-160358 | 221 | - | F | CR on mismatch between 36.211 and 36.331 | 13.1.0 |
| 2016-03 | RAN#71 | RP-160358 | 222 | - | F | Clarification on additional SC-FDMA symbols in UpPTS for SRS | 13.1.0 |
| 2016-03 | RAN#71 | RP-160358 | 223 | - | F | Correction on Precoding and definition of DMRS ports | 13.1.0 |
| 2016-03 | RAN#71 | RP-160361 | 207 | 9 | B | Introduction of LC/CE MTC | 13.1.0 |
| 2016-06 | RAN#72 | RP-161063 | 216 | 2 | F | CR on CSI-RS transmission in DwPTS | 13.2.0 |
| 2016-06 | RAN#72 | RP-161067 | 224 | 8 | B | Introduction of NB-IoT | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 229 | 2 | F | Collision between PSS/SSS/PBCH and MPDCCH/PDSCH for MTC | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 230 | - | F | DMRS initialization of CSS for MTC | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 231 | - | F | Missing words in PRACH starting subframe paragraph for MTC | 13.2.0 |
| 2016-06 | RAN#72 | RP-161065 | 232 | - | F | Correction to EPDCCH procedures for LAA FS 3 | 13.2.0 |
| 2016-06 | RAN#72 | RP-161063 | 233 | - | F | Clarification on PDSCH mapping to resource elements | 13.2.0 |
| 2016-06 | RAN#72 | RP-161063 | 234 | - | F | CR on CSI-RS description in TS 36.211 | 13.2.0 |
| 2016-06 | RAN#72 | RP-161065 | 235 | - | F | Corrections on the support of ending partial subframe in LAA | 13.2.0 |
| 2016-06 | RAN#72 | RP-161063 | 236 | - | F | Clarification of CSI-RS on extended CP | 13.2.0 |
| 2016-06 | RAN#72 | RP-161063 | 237 | - | F | Correction on description about UpPTS length for preamble format 4 for PRACH | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 238 | - | F | Correction to TS 36.211 for eMTC | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 239 | - | F | Narrow band hopping | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 240 | 1 | F | CR on MPDCCH format for Rmax=1 and 2/4 PRBs | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 241 | 1 | F | Correction on RE mapping in MBSFN subframe for BL/CE UEs in CEModeB | 13.2.0 |
| 2016-06 | RAN#72 | RP-161063 | 242 | - | F | Correction on the description about DMRS | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 243 | - | F | CR for TS36.211 related to 2+4 PRB set | 13.2.0 |
| 2016-06 | RAN#72 | RP-161065 | 244 | - | F | CR on UE assumptions on number of CRS ports in DRS | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 245 | - | F | Some corrections for eMTC | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 247 | - | F | Clarification of MPDCCH over empty CRS tones in PBCH repetition | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 248 | - | F | Scrambling sequence initialization | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 249 | - | F | On MPDCCH AL for 8 EREGs per ECCE in TS 36.211 | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 250 | - | F | Overriding of valid-invalid subframes for R=1 | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 251 | - | F | Scrambling Sequence for paging MPDCCH and PDSCH | 13.2.0 |
| 2016-06 | RAN#72 | RP-161066 | 252 | - | F | Scrambling sequence initialization for PDSCH | 13.2.0 |
| 2016-09 | RAN#73 | RP-161563 | 253 | - | F | Correction on DMRS for NB-IoT in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 254 | 1 | F | Correction on NPRACH in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 255 | - | F | Correction on SC-FDMA signal generation for NB-IoT in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 256 | - | F | Corrections to RRC parameter names for NB-IoT in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 259 | - | F | MPDCCH search-space with Temporary C-RNTI | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 260 | - | F | Correction on NPBCH in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 261 | 1 | F | Correction on UL collisions in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 262 | 1 | F | Correction on NPSS mapping in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 263 | 1 | F | Corrections on the presence of NRS for standalone and guard band operation mode in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161561 | 264 | - | F | Correction on the determination of EPDCCH starting position | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 265 | - | F | Corrections on NPDCCH scrambling in TS 36.211 | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 272 | 1 | F | Frequency hopping for SI and paging messages for BL/CE UE | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 275 | - | F | Scrambling of DL DMRS for BL/CE UE | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 276 | - | F | Enable cross-subframe channel estimation for BL/CE UE | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 278 | - | F | Frequency hopping interval for MPDCCH during random access for BL/CE UE | 13.3.0 |
| 2016-09 | RAN#73 | RP-161565 | 279 | - | F | CR on the correction from SC-FDFMA to SC-FDMA | 13.3.0 |
| 2016-09 | RAN#73 | RP-161561 | 280 | - | F | Correction for PHICH resource reservation on the LAA cell in 36.211 for Rel-13 LAA | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 281 | - | F | Correction on MPDCCH transmission without repetition in special subframes | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 282 | 1 | F | Introduction of a reserved range of NPRACH sub-carriers for contention based access | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 283 | - | F | Clarification of valid subframe in eMTC | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 284 | - | F | Correction of NB-IoT antenna port mapping | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 285 | - | F | Clarification on PRACH system frame number | 13.3.0 |
| 2016-09 | RAN#73 | RP-161562 | 286 | - | F | PUCCH retuning with puncturing for BL/CE UE | 13.3.0 |
| 2016-09 | RAN#73 | RP-161563 | 287 | 1 | F | Phase difference between NRS and CRS | 13.3.0 |
| 2016-09 | RAN#73 | RP-161825 | 288 | 1 | B | Continuous uplink transmission in eMTC | 13.3.0 |
| 2016-09 | RAN#73 | RP-161571 | 266 | 2 | B | Introduction of eLAA | 14.0.0 |
| 2016-09 | RAN#73 | RP-161570 | 267 | 2 | B | Introduction of V2V support | 14.0.0 |
| 2016-12 | RAN#74 | RP-162368 | 0297 | - | F | CR on start timing of PUSCH | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0298 | - | A | Correction to DMRS for MPDCCH associated with P-RNTI – Rel-14 | 14.1.0 |
| 2016-12 | RAN#74 | RP-162359 | 0300 | - | A | Clarification on NPRACH and NPUSCH collision | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0302 | 1 | A | Clarification on i_0 value | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0304 | - | A | Correction of PRACH starting subframes for eMTC | 14.1.0 |
| 2016-12 | RAN#74 | RP-162359 | 0306 | - | A | Correction of NPRACH frequency hopping | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0307 | - | A | Correction on MPDCCH transmission without repetition | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0308 | - | A | Correction of typos due to wrong implementation of CR0283 "Clarification of valid subframe in eMTC " | 14.1.0 |
| 2016-12 | RAN#74 | RP-162356 | 0309 | - | A | Correction on NZP CSI-RS aggregation for Class A | 14.1.0 |
| 2016-12 | RAN#74 | RP-162367 | 0310 | 2 | B | Introduction of performance enhancements for high speed scenario | 14.1.0 |
| 2016-12 | RAN#74 | RP-162450 | 0311 | - | B | Introduction of further indoor positioning enhancements | 14.1.0 |
| 2016-12 | RAN#74 | RP-162365 | 0312 | 1 | B | Introduction of Multiuser Superposition Transmission (MUST) | 14.1.0 |
| 2016-12 | RAN#74 | RP-162359 | 0316 | 1 | A | Correction on NPDSCH Mapping to resource elements in 36.211 | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0320 | - | A | UL gap applicability for CE Mode A | 14.1.0 |
| 2016-12 | RAN#74 | RP-162355 | 0322 | - | A | CR on pseudo-random sequence generator for PUCCH format 4 and PUCCH format 5 and sequence group hopping for PUCCH format 4 | 14.1.0 |
| 2016-12 | RAN#74 | RP-162359 | 0324 | - | A | Clarification on vShift value for CRS | 14.1.0 |
| 2016-12 | RAN#74 | RP-162359 | 0326 | - | A | Correction to OFDM baseband signal generation of NB-IoT | 14.1.0 |
| 2016-12 | RAN#74 | RP-162358 | 0327 | - | A | Mapping of MPDCCH and PDSCH | 14.1.0 |
| 2016-12 | RAN#74 | RP-162364 | 0328 | - | B | Introduction of SRS switching between LTE component carriers | 14.1.0 |
| 2016-12 | RAN#74 | RP-162366 | 0329 | - | F | Corrections for V2V | 14.1.0 |
| 2017-03 | RAN#75 | RP-170605 | 0330 | 1 | B | Introduction of Uplink Capacity Enhancements for LTE | 14.2.0 |
| 2017-03 | RAN#75 | RP-170608 | 0331 | 1 | B | Introduction of eMBMS enhancements for LTE | 14.2.0 |
| 2017-03 | RAN#75 | RP-170623 | 0332 | 2 | B | Introduction of Further Enhanced MTC for LTE | 14.2.0 |
| 2017-03 | RAN#75 | RP-170624 | 0333 | 3 | B | Introduction of NB-IoT enhancements | 14.2.0 |
| 2017-03 | RAN#75 | RP-170622 | 0334 | 2 | B | Introduction of V2X | 14.2.0 |
| 2017-03 | RAN#75 | RP-170607 | 0335 | 2 | B | Introduction of eFD-MIMO | 14.2.0 |
| 2017-03 | RAN#75 | RP-170625 | 0336 | 2 | B | Introduction of Voice and Video enhancement for LTE | 14.2.0 |
| 2017-03 | RAN#75 | RP-170610 | 0338 | 2 | A | Correction on the scrambling of NPDSCH carrying the BCCH | 14.2.0 |
| 2017-03 | RAN#75 | RP-170609 | 0340 | - | A | Frequency hopping in eMTC | 14.2.0 |
| 2017-03 | RAN#75 | RP-170609 | 0342 | - | A | Retuning gap with shortened PUCCH format for BL/CE UE | 14.2.0 |
| 2017-03 | RAN#75 | RP-170609 | 0344 | - | A | Parameters for number of PUCCH repetitions for Msg4 for BL/CE UE – Superseded by CR0332r2 | 14.2.0 |
| 2017-03 | RAN#75 | RP-170609 | 0346 | - | A | Clarification on repetition and starting subframe of the MPDCCH search space | 14.2.0 |
| 2017-03 | RAN#75 | RP-170615 | 0347 | - | F | CR for SRS switching in 36.211 | 14.2.0 |
| 2017-03 | RAN#75 | RP-170617 | 0348 | - | F | CR on the new restricted sets of cyclic shifts for PRACH for high speed in 36.211 | 14.2.0 |
| 2017-03 | RAN#75 | RP-170612 | 0352 | - | A | Correction on single layer precoding for EPCCH | 14.2.0 |
| 2017-03 | RAN#75 | RP-170610 | 0354 | - | A | NPBCH symbol rotation for interference randomization in NB-IoT | 14.2.0 |
| 2017-03 | RAN#75 | RP-170617 | 0355 | - | F | Correction to PRACH resource configuration for high speed scenario in TS 36.211 | 14.2.0 |
| 2017-06 | RAN#76 | RP-171205 | 0356 | - | F | Correction on baseband generation for paging/random access non-anchor carriers | 14.3.0 |
| 2017-06 | RAN#76 | RP-171204 | 0357 | - | F | Correction of reference to PRS occasion group for OTDOA enhancements | 14.3.0 |
| 2017-06 | RAN#76 | RP-171204 | 0358 | - | F | Center frequency for PUSCH allocation in larger bandwidth mode in FeMTC | 14.3.0 |
| 2017-06 | RAN#76 | RP-171205 | 0359 | - | F | Clarification of NRS presence | 14.3.0 |
| 2017-06 | RAN#76 | RP-171194 | 0360 | - | F | Clarification and Correction on IFDMA UL-DMRS for eFD-MIMO | 14.3.0 |
| 2017-06 | RAN#76 | RP-171199 | 0363 | - | A | Clarification on PDSCH collision with PSS/SSS in TDD | 14.3.0 |
| 2017-06 | RAN#76 | RP-171195 | 0364 | - | F | Clarification on CDM-8 pattern for 24-ports CSI-RS in DwPTS | 14.3.0 |
| 2017-06 | RAN#76 | RP-171192 | 0365 | - | F | Correction on PUSCH symbol locations in UpPTS for UL capacity enhancement in TS 36.211 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171196 | 0366 | - | A | CR on correction of PRACH transmission across SFN boundary | 14.3.0 |
| 2017-06 | RAN#76 | RP-171204 | 0367 | - | F | Correction on resource mapping in case of retuning in 36.211 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171197 | 0369 | 1 | A | Correction on NB-IoT DMRS definition in 36.211 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171197 | 0371 | 1 | A | Correction on NB-IoT SC-FDMA baseband signal generation in 36.211 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171197 | 0373 | - | A | Clarification on the definition of the nprach-NumCBRA-StartSubcarriers | 14.3.0 |
| 2017-06 | RAN#76 | RP-171204 | 0374 | - | F | Parallel reception of MPDCCH and PDSCH for BL/CE UE | 14.3.0 |
| 2017-06 | RAN#76 | RP-171194 | 0375 | - | F | CR for precoding for spatial multiplexing using antenna ports with UE-specific reference signals in 36.211 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171194 | 0376 | - | F | Correction to CSI-RS configuration | 14.3.0 |
| 2017-06 | RAN#76 | RP-171196 | 0378 | - | A | Clarification of frequency hopping for "PDCCH order " initiated PUSCH | 14.3.0 |
| 2017-06 | RAN#76 | RP-171196 | 0380 | - | A | Correction on determination of number of repetitions PUCCH format 1 | 14.3.0 |
| 2017-06 | RAN#76 | RP-171204 | 0381 | - | F | Correction on PRS hopping | 14.3.0 |
| 2017-06 | RAN#76 | RP-171205 | 0383 | - | F | NRS presence assumptions on unicast non-anchor carriers | 14.3.0 |
| 2017-09 | RAN#77 | RP-171646 | 0384 | - | F | Correction of RRC parameter name for non-anchor carriers | 14.4.0 |
| 2017-09 | RAN#77 | RP-171638 | 0386 | 1 | F | Corrections on CDM8 sequence for 24 and 32 CSI-RS ports and CDM4 sequence | 14.4.0 |
| 2017-09 | RAN#77 | RP-171645 | 0387 | - | F | PRS and PDSCH/MPDCCH collision | 14.4.0 |
| 2017-09 | RAN#77 | RP-171640 | 0389 | - | A | NPUSCH transmission during NPRACH gaps | 14.4.0 |
| 2017-09 | RAN#77 | RP-171639 | 0391 | - | A | MPDCCH Frequency hopping for RRC connected contention-based RACH | 14.4.0 |
| 2017-09 | RAN#77 | RP-171646 | 0392 | 1 | F | Interference randomization for NPDCCH and NPDSCH | 14.4.0 |
| 2017-12 | RAN#78 | RP-172688 | 0395 | - | A | Clarification on DMRS ports associated with PDSCH | 14.5.0 |
| 2017-12 | RAN#78 | RP-172680 | 0396 | - | A | Correction on MPDCCH frequency hopping | 14.5.0 |
| 2017-12 | RAN#78 | RP-172685 | 0397 | - | F | SRS to SRS retuning in UpPTS | 14.5.0 |
| 2017-12 | RAN#78 | RP-172679 | 0398 | - | F | Correction on power boosting for UL DMRS | 14.5.0 |
| 2017-12 | RAN#78 | RP-172680 | 0402 | - | A | Correction on scrambling sequence identity for 2+4 PRBs sets in MPDCCH | 14.5.0 |
| 2017-12 | RAN#78 | RP-172680 | 0404 | - | A | Correction on resource elements reserved for CRS for PBCH with repetition | 14.5.0 |
| 2017-12 | RAN#78 | RP-172677 | 0405 | - | F | Introduction of new UE behavior for special subframe configuration 10 | 14.5.0 |
| 2017-12 | RAN#78 | RP-172691 | 0406 | - | F | Correction for PUSCH puncturing in SRS carrier switching | 14.5.0 |
| 2017-12 | RAN#78 | RP-172679 | 0407 | - | F | Correction on the scale factor for semi-OL rank-1 | 14.5.0 |
| 2017-12 | RAN#78 | RP-172680 | 0409 | - | A | UE uplink gap capability signaling description | 14.5.0 |
| 2017-12 | RAN#78 | RP-172693 | 0385 | 4 | B | Introduction of shortened processing time and shortened TTI into 36.211, s03-05 | 15.0.0 |
| 2017-12 | RAN#78 | RP-172693 | 0399 | 2 | B | Introduction of shortened processing time and shortened TTI into 36.211, s06-08 | 15.0.0 |
| 2018-03 | RAN#79 | RP-180195 | 0400 | 1 | B | Introduction of feCoMP into 36.211 | 15.1.0 |
| 2018-03 | RAN#79 | RP-180191 | 0416 | - | A | Clarification on the NPRACH starting subcarrier partitioning for multi-tone Msg3 transmission | 15.1.0 |
| 2018-03 | RAN#79 | RP-180189 | 0418 | - | A | Correction on CDM-8 Sequence Mapping for 24 and 32 ports | 15.1.0 |
| 2018-03 | RAN#79 | RP-180190 | 0419 | - | A | Clarification on PUSCH and PDSCH scrambling for BL/CE UEs | 15.1.0 |
| 2018-03 | RAN#79 | RP-180190 | 0420 | - | A | Clarification on the hopping parameter for PUSCH transmission corresponding to the RAR grant | 15.1.0 |
| 2018-03 | RAN#79 | RP-180199 | 0422 | - | A | Interference randomization in CSS | 15.1.0 |
| 2018-03 | RAN#79 | RP-180187 | 0424 | - | A | Correction on DM-RS in DwPTS in special subframe configuration 10 | 15.1.0 |
| 2018-03 | RAN#79 | RP-180191 | 0427 | - | A | Clarification on NPDCCH RE mapping | 15.1.0 |
| 2018-06 | RAN#80 | RP-181163 | 0430 | 1 | A | Correction on DMRS scrambling ID for semi-open loop transmission | 15.2.0 |
| 2018-06 | RAN#80 | RP-181173 | 0431 | - | B | Introduction of enhancements for high capacity stationary wireless link and introduction of 1024 QAM for LTE | 15.2.0 |
| 2018-06 | RAN#80 | RP-181169 | 0434 | - | A | Correction on PUSCH hopping parameter for eVoLTE | 15.2.0 |
| 2018-06 | RAN#80 | RP-181181 | 0437 | - | A | Collision with NPRACH in non-anchor carriers | 15.2.0 |
| 2018-06 | RAN#80 | RP-181181 | 0439 | - | A | On NRS presence in non-anchor carriers | 15.2.0 |
| 2018-06 | RAN#80 | RP-181170 | 0440 | 1 | F | Corrections to sTTI and SPT implementation | 15.2.0 |
| 2018-06 | RAN#80 | RP-181180 | 0441 | 1 | B | Introduction of enhancements to operation in unlicensed spectrum | 15.2.0 |
| 2018-06 | RAN#80 | RP-181167 | 0444 | 1 | A | Clarification on CSI-RS resource aggregation | 15.2.0 |
| 2018-06 | RAN#80 | RP-181174 | 0447 | - | B | Introduction of Even Further Enhanced MTC for LTE | 15.2.0 |
| 2018-06 | RAN#80 | RP-181166 | 0448 | - | B | Introduction Rel-15 Further NB-IoT enhancements | 15.2.0 |
| 2018-06 | RAN#80 | RP-181168 | 0449 | - | F | Correction on layer-to-port mapping for feCoMP | 15.2.0 |
| 2018-06 | RAN#80 | RP-181177 | 0450 | - | B | Introduction of HRLLC into 36.211 | 15.2.0 |
| 2018-09 | RAN#81 | RP-181792 | 0451 | - | B | Introduction of eV2X | 15.3.0 |
| 2018-09 | RAN#81 | RP-181796 | 0453 | - | A | Correction for interference randomization for NB-IoT | 15.3.0 |
| 2018-09 | RAN#81 | RP-181796 | 0455 | - | A | Correction to NPRS mapping | 15.3.0 |
| 2018-09 | RAN#81 | RP-181795 | 0456 | - | F | Correction on DL CP extension for FeLAA in 36.211 | 15.3.0 |
| 2018-09 | RAN#81 | RP-181795 | 0457 | - | F | Correction to determination of ending symbol for AUL transmissions | 15.3.0 |
| 2018-09 | RAN#81 | RP-181780 | 0459 | - | A | Rate matching for aperiodic CSI-RS | 15.3.0 |
| 2018-09 | RAN#81 | RP-181787 | 0460 | - | F | Corrections to sTTI and SPT | 15.3.0 |
| 2018-09 | RAN#81 | RP-181791 | 0461 | - | F | Corrections to eMTC | 15.3.0 |
| 2018-09 | RAN#81 | RP-181783 | 0462 | - | F | Corrections to NB-IoT | 15.3.0 |
| 2018-09 | RAN#81 | RP-181793 | 0463 | - | F | Corrections to HRLLC | 15.3.0 |
| 2018-12 | RAN#82 | RP-182518 | 0465 | - | A | Correction on aperiodic CSI-RS resource mapping in 36.211 | 15.4.0 |
| 2018-12 | RAN#82 | RP-182518 | 0467 | - | A | Correction to non-precoded NZP CSI-RS resource configurations | 15.4.0 |
| 2018-12 | RAN#82 | RP-182524 | 0468 | 1 | F | Corrections to LTE-MTC | 15.4.0 |
| 2018-12 | RAN#82 | RP-182519 | 0469 | 1 | F | Corrections to NB-IoT | 15.4.0 |
| 2018-12 | RAN#82 | RP-182518 | 0471 | - | A | Clarification on cyclic shift field mapping table for DMRS bit field in DCI format 0/4 | 15.4.0 |
| 2018-12 | RAN#82 | RP-182526 | 0472 | - | F | Correction on rate-matching around SPDCCH resources for PDSCH repetition | 15.4.0 |
| 2018-12 | RAN#82 | RP-182522 | 0473 | - | F | Correction on the number of CCEs for DMRS-based SPDCCH | 15.4.0 |
| 2018-12 | RAN#82 | RP-182522 | 0474 | - | F | Correction of SPDCCH rate-matching description | 15.4.0 |
| 2019-03 | RAN#83 | RP-190434 | 0476 | - | F | Correction of higher layer signalling for special subframe configuration 10 | 15.5.0 |
| 2019-03 | RAN#83 | RP-190437 | 0477 | - | F | DMRS sequence index for PUSCH sub-PRB allocation for LTE-MTC | 15.5.0 |
| 2019-03 | RAN#83 | RP-190436 | 0478 | - | F | CR on DMRS mapping for SPDCCH | 15.5.0 |
| 2019-06 | RAN#84 | RP-191269 | 0479 | - | F | Correction on NPRACH baseband signal generation | 15.6.0 |
| 2019-06 | RAN#84 | RP-191270 | 0480 | - | F | Handling of invalid PRB for frequency hopping of BL/CE UEs with PUSCH CE Mode A and flexible starting PRB | 15.6.0 |
| 2019-06 | RAN#84 | RP-191272 | 0483 | - | A | Correction for PUSCH frequency hopping in eMTC | 15.6.0 |
| 2019-06 | RAN#84 | RP-191273 | 0485 | - | A | Correction for PUSCH frequency hopping in VoLTE enhancements | 15.6.0 |
| 2019-09 | RAN#85 | RP-191939 | 0487 | - | F | Correction for PDSCH starting position in a subframe of FS3 | 15.7.0 |
| 2019-09 | RAN#85 | RP-191937 | 0490 | - | A | Clarification on localized MPDCCH DMRS port for 2+4 PRB set | 15.7.0 |
| 2019-09 | RAN#85 | RP-191945 | 0491 | - | F | Correction on higher layer parameter configuring short TTI length in 36.211 | 15.7.0 |
| 2019-09 | RAN#85 | RP-191936 | 0492 | - | F | Correction on DMRS for NPUSCH Format 2 in TDD NB-IoT | 15.7.0 |
| 2019-12 | RAN#86 | RP-192620 | 0495 | - | A | Clarification to postponing in subframes that are not BL/CE subframes | 15.8.0 |
| 2019-12 | RAN#86 | RP-192618 | 0497 | - | F | PUSCH frequency hopping configured with CEModeB and flexible starting PRB allocation | 15.8.0 |
| 2019-12 | RAN#86 | RP-192618 | 0498 | - | F | Correction of MWUS sequence generation | 15.8.0 |
| 2019-12 | RAN#86 | RP-192632 | 0500 | - | A | Correction on interference randomization on non-anchor carrier for NB-IoT | 15.8.0 |
| 2019-12 | RAN#86 | RP-192647 | 0501 | - | B | Introduction of additional MTC enhancements for LTE | 16.0.0 |
| 2019-12 | RAN#86 | RP-192648 | 0502 | - | B | Introduction of Additional enhancements for NB-IoT | 16.0.0 |
| 2019-12 | RAN#86 | RP-192649 | 0503 | - | B | Introduction of DL MIMO efficiency enhancements for LTE | 16.0.0 |
| 2019-12 | RAN#86 | RP-192650 | 0504 | - | B | Introduction of LTE terrestrial broadcast | 16.0.0 |
| 2020-03 | RAN#87-e | RP-200202 | 0507 | - | A | Correction on the resource block pair definition for 1.25 kHz subcarrier spacing | 16.1.0 |
| 2020-03 | RAN#87-e | RP-200178 | 0509 | - | A | Correction on Rel-15 NWUS/MWUS | 16.1.0 |
| 2020-03 | RAN#87-e | RP-200196 | 0510 | - | F | Miscellaneous corrections for Rel-16 LTE-MTC features in 36.211 | 16.1.0 |
| 2020-03 | RAN#87-e | RP-200197 | 0511 | - | F | Miscellaneous corrections for Rel-16 NB-IoT features in 36.211 | 16.1.0 |
| 2020-03 | RAN#87-e | RP-200199 | 0512 | - | F | Corrections to LTE terrestrial broadcast | 16.1.0 |
| 2020-03 | RAN#87-e | RP-200198 | 0513 | - | F | Corrections to DL MIMO efficiency enhancements for LTE | 16.1.0 |
| 2020-06 | RAN#88-e | RP-200704 | 0518 | - | A | Correction on NRS presence in non-anchor carriers for NB-IoT | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200681 | 0519 | - | A | CR on WUS transmission in TDD special subframe | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200681 | 0525 | - | A | CR on clarification of RSS transmission | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200681 | 0527 | - | A | CR on scrambling initialization for sub-PRB PUSCH | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200703 | 0532 | - | A | Correction on MBSFN region start symbol index of a MBSFN subframe | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200699 | 0533 | - | F | Corrections for Rel-16 NB-IoT features in 36.211 | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200701 | 0534 | 1 | F | Corrections to LTE terrestrial broadcast | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200698 | 0535 | - | F | Corrections to Rel-16 LTE-MTC features in 36.211 | 16.2.0 |
| 2020-06 | RAN#88-e | RP-200700 | 0536 | 1 | F | Corrections to DL MIMO efficiency enhancements for LTE | 16.2.0 |
| 2020-09 | RAN#89-e | RP-201821 | 0538 | - | A | Correction on semi-open-loop | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201818 | 0539 | - | F | Correction for PBCH repetition | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201818 | 0540 | - | F | Correction on MBSFN region | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201816 | 0541 | - | F | Corrections on NPDSCH/NPDCCH interference randomization | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201816 | 0542 | - | F | Correction on NPDSCH | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201817 | 0543 | - | F | Correction on higher layer parameters for additional SRS in 36.211 | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201817 | 0544 | - | F | Correction on terminology of additional SRS | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201815 | 0545 | - | F | Multi-TB scheduling and PUR spanning PUSCH transmission in LTE-MTC | 16.3.0 |
| 2020-09 | RAN#89-e | RP-201816 | 0546 | - | F | Correction on terms and higher layer parameters for NB-IoT in 36.211 | 16.3.0 |
| 2020-12 | RAN#90-e | RP-202394 | 0547 | - | F | CR on LTE-based 5G Terrestrial Broadcast | 16.4.0 |
| 2020-12 | RAN#90-e | RP-202394 | 0548 | - | F | Correction for 0.37kHz SCS | 16.4.0 |
| 2020-12 | RAN#90-e | RP-202400 | 0550 | - | A | Corrections on interference randomization for NB-IoT SPS | 16.4.0 |
| 2020-12 | RAN#90-e | RP-202393 | 0551 | - | F | Corrections on additional SRS symbols | 16.4.0 |
| 2020-12 | RAN#90-e | RP-202391 | 0552 | - | F | Alignment corrections for Rel-16 features | 16.4.0 |
| 2021-03 | RAN#91-e | RP-210060 | 0554 | - | A | Correction for support of 1024QAM for PDSCH | 16.5.0 |
| 2021-06 | RAN#92-e | RP-211241 | 0555 | - | F | Clarification of PUSCH PRB resources for PUR in LTE-MTC | 16.6.0 |
| 2021-06 | RAN#92-e | RP-211242 | 0556 | - | F | Correction on DMRS cyclic shift for PUR in NB-IoT | 16.6.0 |
| 2021-06 | RAN#92-e | RP-211246 | 0557 | - | F | Correction for 0.37kHz SCS | 16.6.0 |
| 2021-09 | RAN#93-e | RP-211848 | 0559 | 1 | F | Correction on PUSCH cyclic shift for eMTC PUR | 16.7.0 |
| 2021-09 | RAN#93-e | RP-211849 | 0561 | - | A | Clarification on NPUSCH postponement for NB-IoT | 16.7.0 |
| 2021-12 | RAN#94-e | RP-212974 | 0562 | - | B | Introduction of additional enhancements for NB-IoT and LTE-MTC | 17.0.0 |
| 2021-12 | RAN#94-e | RP-212976 | 0563 | - | B | Introduction of NB-IoT/eMTC support in Non-Terrestrial Networks | 17.0.0 |
| 2021-12 | RAN#94-e | RP-212975 | 0564 | - | B | Introduction of new bandwidths for LTE-based 5G terrestrial broadcast | 17.0.0 |
| 2022-03 | RAN#95-e | RP-220260 | 0566 | - | F | Correction to NB-IoT and LTE-MTC over NTN | 17.1.0 |
| 2022-03 | RAN#95-e | RP-220258 | 0567 | - | F | Correction to additional enhancements for NB-IoT and eMTC | 17.1.0 |
| 2022-06 | RAN#96 | RP-221609 | 0568 | - | F | Correction to NB-IoT and LTE-MTC over NTN | 17.2.0 |
| 2022-06 | RAN#96 | RP-221608 | 0569 | - | F | Correction to additional enhancements for NB-IoT and eMTC | 17.2.0 |
| 2023-03 | RAN#99 | RP-230448 | 0571 | - | F | CR on correction of UE capability parameter name in 36.211 | 17.3.0 |
| 2023-09 | RAN#101 | RP-232454 | 0573 | - | A | Correction on SRS identity for additional SRS symbols | 17.4.0 |
| 2024-03 | SA#103 |  |  |  |  | Update to Rel-18 version (MCC) | 18.0.0 |
| 2024-04 | SA#103 |  |  |  |  | MCC correction as v18.0.0 was promoted from v17.0.0 instead of the latest version of the spec, namely v17.4.0 | 18.0.1 |
| 2025-06 | RAN#108 | RP-251589 | 0574 | - | B | Introduction of IoT_NTN_Ph3 | 19.0.0 |
| 2025-06 | RAN#108 | RP-251569 | 0575 | - | B | Introduction of IoT_NTN_TDD | 19.0.0 |
| 2025-06 | RAN#108 | RP-251570 | 0576 | - | B | Introduction of LTE-based 5G Broadcast Phase 2 | 19.0.0 |
| 2025-09 | RAN#109 | RP-252634 | 0577 | 1 | B | Introduction of TEI19 for LTE-based 5G Broadcast [5GB CASMuting] | 19.1.0 |
| 2025-09 | RAN#109 | RP-252638 | 0578 | - | F | Corrections to IoT_NTN_Ph3 | 19.1.0 |
| 2025-09 | RAN#109 | RP-252624 | 0579 | - | F | Corrections to IoT_NTN_TDD | 19.1.0 |
| 2025-09 | RAN#109 | RP-252625 | 0580 | - | F | Corrections to LTE_terr_bcast_Ph2 | 19.1.0 |
| 2025-12 | RAN#110 | RP-253032 | 0581 | - | F | CR for Interference Randomization for non-anchor carrier in NB-IoT NTN | 19.2.0 |
| 2025-12 | RAN#110 | RP-253028 | 0582 | - | F | Corrections to IoT_NTN_Ph3-Core | 19.2.0 |
| 2025-12 | RAN#110 | RP-253030 | 0583 | - | F | Corrections to IoT_NTN_TDD-Core | 19.2.0 |
| 2025-12 | RAN#110 | RP-253029 | 0584 | - | F | Corrections to LTE_terr_bcast_Ph2-Core | 19.2.0 |
| 2026-03 | RAN#111 | RP-260177 | 0585 | - | F | Correction on collision of OCC transmission with reserved resource | 19.3.0 |
| 2026-03 | RAN#111 | RP-260583 | 0586 | - | F | Alignment of parameter names | 19.3.0 |
