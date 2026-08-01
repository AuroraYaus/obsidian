# 6 Downlink

## 6.1 Overview

The smallest time-frequency unit for downlink transmission is denoted a resource element and is defined in clause 6.2.2.

A subset of the downlink subframes in a radio frame can be configured as MBSFN subframes by higher layers. For $\Delta  f\approx  0.37kHz $ the MBSFN region is defined as one slot of 3 ms. Except for $\Delta  f\approx  0.37kHz $, each MBSFN subframe is divided into a non-MBSFN region and an MBSFN region.

- For subframes using ![](media_svg/image1.svg) [公式: δf=15kHz], the non-MBSFN region spans the first one or two OFDM symbols in an MBSFN subframe where the length of the non-MBSFN region is given according to Clause 6.7.

- For subframes using ![](media_svg/image2.svg) [公式: δf=7.5kHz], $\Delta  f=2.5kHz $, ![](media_svg/image3.svg) [公式: δf=1.25kHz], or slots using $\Delta  f\approx  0.37kHz $, the non-MBSFN region is of zero size.

- The MBSFN region in an MBSFN subframe is defined as the OFDM symbols not used for the non-MBSFN region.

For an MBMS-dedicated cell, subframes where PSS/SSS/PBCH or PDSCH carrying system information are transmitted with ![](media_svg/image1.svg) [公式: δf=15kHz] are non-MBSFN subframes.

For frame structure type 3, MBSFN configuration shall not be applied to downlink subframes in which at least one OFDM symbol is not occupied or discovery signal is transmitted.

Unless otherwise specified, transmission in each downlink subframe shall use the same cyclic prefix length as used for downlink subframe #0.

### 6.1.1 Physical channels

A downlink physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS 36.212 [3] and the present document TS 36.211. 
The following downlink physical channels are defined:

- Physical Downlink Shared Channel, PDSCH

- Physical Broadcast Channel, PBCH

- Physical Multicast Channel, PMCH

- Physical Control Format Indicator Channel, PCFICH

- Physical Downlink Control Channel, PDCCH

- Physical Hybrid ARQ Indicator Channel, PHICH

- Enhanced Physical Downlink Control Channel, EPDCCH

- MTC Physical Downlink Control Channel, MPDCCH

- Short Physical Downlink Control Channel, SPDCCH

### 6.1.2 Physical signals

A downlink physical signal corresponds to a set of resource elements used by the physical layer but does not carry information originating from higher layers. The following downlink physical signals are defined:

- Reference signal

- Synchronization signal

- Discovery signal

- MTC wake-up signal, MWUS

## 6.2 Slot structure and physical resource elements

### 6.2.1 Resource grid

The transmitted signal in each slot is described by one or several resource grids of ![](media_svg/image4.svg) [公式≈: _{N}_{RB}DL_{N}_{sc}RB] subcarriers and ![](media_svg/image5.svg) [公式≈: _{N}_{sc}RB] OFDM symbols. The resource grid structure is illustrated in Figure 6.2.2-1. The quantity ![](media_svg/image6.svg) [公式≈: _{N}_{RB}DL] depends on the downlink transmission bandwidth configured in the cell and shall fulfil

![](media_svg/image7.svg) [公式≈: _{N}_{RB}min,DL_{≥}_{N}_{RB}DL_{≥}_{N}_{RB}max,DL]

where ![](media_svg/image8.svg) [公式≈: _{N}_{RB}min,DL_{=}_{6}] and ![](media_svg/image9.svg) [公式≈: _{N}_{RB}max,DL_{=}_{110}] are the smallest and largest downlink bandwidths, respectively, supported by the current version of this specification.

The set of allowed values for ![](media_svg/image6.svg) [公式≈: _{N}_{RB}DL] is given by TS36.104 [6]. The number of OFDM symbols in a slot depends on the cyclic prefix length and subcarrier spacing configured and is given in Table 6.2.3-1.

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed. For MBSFN reference signals, positioning reference signals, UE-specific reference signals associated with PDSCH, demodulation reference signals associated with SPDCCH, and demodulation reference signals associated with EPDCCH, there are limits given below within which the channel can be inferred from one symbol to another symbol on the same antenna port. There is one resource grid per antenna port. The set of antenna ports supported depends on the reference signal configuration in the cell:

- Cell-specific reference signals support a configuration of one, two, or four antenna ports and are transmitted on antenna ports ![](media_svg/image10.svg) [公式: p=0],![](media_svg/image11.svg) [公式: p⎰{0,1}], and ![](media_svg/image12.svg) [公式: p⎰{0,1,2,3}], respectively.

- MBSFN reference signals are transmitted on antenna port![](media_svg/image13.svg) [公式: p=4]. The channel over which a symbol on antenna port![](media_svg/image13.svg) [公式: p=4]is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols correspond to subframes (slots in case of 0.37 kHz subcarrier spacing) of the same MBSFN area.

- UE-specific reference signals associated with PDSCH intended for non-BL/CE UE are transmitted on antenna port(s) ![](media_svg/image14.svg) [公式: p=5], ![](media_svg/image15.svg) [公式: p=7], ![](media_svg/image16.svg) [公式: p=8], or one or several of ![](media_svg/image17.svg) [公式: p⎰{7,8,9,10,11,12,13,14}]. The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are within the same subframe and in the same PRG when PRB bundling is used or in the same PRB pair when PRB bundling is not used.

- UE-specific reference signals associated with PDSCH intended for BL/CE UE are transmitted on one or several of antenna port(s) ![](media_svg/image17.svg) [公式: p⎰{7,8,9,10,11,12,13,14}]. The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same set of![](media_svg/image18.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes and have the same PRB index.

- Demodulation reference signals associated with EPDCCH are transmitted on one or several of ![](media_svg/image19.svg) [公式: p⎰{107,108,109,110}]. The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same PRB pair.

- Demodulation reference signals associated with MPDCCH are transmitted on one or several of ![](media_svg/image19.svg) [公式: p⎰{107,108,109,110}]. The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same set of![](media_svg/image18.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes and have the same PRB index.

- Demodulation reference signals associated with SPDCCH are transmitted on ![](media_svg/image20.svg) [公式: p⎰{107}].

- Positioning reference signals are transmitted on antenna port![](media_svg/image21.svg) [公式: p=6]. The channel over which a symbol on antenna port![](media_svg/image21.svg) [公式: p=6] is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only within one positioning reference signal occasion consisting of ![](media_svg/image22.svg) [公式≈: ^{N}PRS] consecutive downlink subframes, where ![](media_svg/image23.svg) [公式≈: ^{N}PRS] is configured by higher layers.

- CSI reference signals support a configuration of 1, 2, 4, 8, 12, 16, 20, 24, 28, or 32 antenna ports and are transmitted on antenna ports ![](media_svg/image24.svg) [公式: p=15], ![](media_svg/image25.svg) [公式: p=15,16], ![](media_svg/image26.svg) [公式: p=15,...,18], ![](media_svg/image27.svg) [公式: p=15,...,22], ![](media_svg/image28.svg) [公式: p=15,...,26], ![](media_svg/image29.svg) [公式: p=15,...,30], ![](media_svg/image30.svg) [公式: p=15,...,34], ![](media_svg/image31.svg) [公式: p=15,...,38], ![](media_svg/image32.svg) [公式: p=15,...,42] and![](media_svg/image33.svg) [公式: p=15,...,46], respectively.

Two antenna ports are said to be quasi co-located if the large-scale properties of the channel over which a symbol on one antenna port is conveyed can be inferred from the channel over which a symbol on the other antenna port is conveyed. The large-scale properties include one or more of delay spread, Doppler spread, Doppler shift, average gain, and average delay.

### 6.2.2 Resource elements

Each element in the resource grid for antenna port ![](media_svg/image34.svg) [公式: p] is called a resource element and is uniquely identified by the index pair ![](media_svg/image35.svg) [公式: (k,l)] in a slot where ![](media_svg/image36.svg) [公式≈: k=0,...,N_{RB}^{DL}N_{sc}^{RB}−1] and ![](media_svg/image37.svg) [公式≈: l=0,...,N_{symb}^{DL}−1] are the indices in the frequency and time domains, respectively. Resource element ![](media_svg/image38.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] corresponds to the complex value![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})]. 
When there is no risk for confusion, or no particular antenna port is specified, the index ![](media_svg/image34.svg) [公式: p] may be dropped.

![](media/image40.emf)

Figure 6.2.2-1: Downlink resource grid

### 6.2.3 Resource blocks

Resource blocks are used to describe the mapping of certain physical channels to resource elements. Physical and virtual resource blocks are defined.

A physical resource block is defined as ![](media_svg/image41.svg) [公式≈: ^{N}symb^{DL}] consecutive OFDM symbols in the time domain and ![](media_svg/image42.svg) [公式≈: _{N}_{sc}RB]consecutive subcarriers in the frequency domain, where ![](media_svg/image41.svg) [公式≈: ^{N}symb^{DL}] and ![](media_svg/image42.svg) [公式≈: _{N}_{sc}RB] are given by Table 6.2.3-1. A physical resource block thus consists of ![](media_svg/image43.svg) [公式≈: ^{N}symb^{DL}^{≠}^{N}sc^{RB}] resource elements, corresponding to one slot in the time domain and 180 kHz in the frequency domain.

Physical resource blocks are numbered from 0 to ![](media_svg/image44.svg) [公式: N_{RB}^{DL}−1] in the frequency domain. The relation between the physical resource block number ![](media_svg/image45.svg) [公式≈: ^{n}PRB] in the frequency domain and resource elements ![](media_svg/image46.svg) [公式: (k,l)] in a slot is given by

![](media_svg/image47.svg) [公式≈: ^{n}^{PRB}^{=}^{⋅}^{⋅}⋅√N^{k}sc^{RB}^{∂}^{∂}∂∃]

Table 6.2.3-1: Physical resource blocks parameters

| Configuration |  | ![](media_svg/image42.svg) [公式≈: _{N}_{sc}RB] | ![](media_svg/image41.svg) [公式≈: ^{N}symb^{DL}] |
| --- | --- | --- | --- |
| Normal cyclic prefix | ![](media_svg/image48.svg) [公式: δf=15kHz] | 12 | 7 |
| Extended cyclic prefix | ![](media_svg/image48.svg) [公式: δf=15kHz] |  | 6 |
|  | ![](media_svg/image49.svg) [公式≈: ^{P}O_NOMINAL_PUSCH,c^{(}^{j}^{)}] | 24 | 3 |
|  | $\Delta  f=2.5kHz $ | 72 | 1 |
|  | ![](media_svg/image50.svg) [公式≈: ^{P}O_UE_PUSCH,c^{(}^{j}^{)}] | 144 | 1 |
|  | $\Delta  f\approx  0.37kHz $ | 486 | 1 |

Except for subcarrier spacing $\Delta  f=1.25kHz $ and $\Delta  f\approx  0.37kHz $, a physical resource-block pair is defined as the two physical resource blocks in one subframe having the same physical resource-block number ![](media_svg/image45.svg) [公式≈: ^{n}PRB].

A virtual resource block is of the same size as a physical resource block. Two types of virtual resource blocks are defined:

- Virtual resource blocks of localized type

- Virtual resource blocks of distributed type

For each type of virtual resource blocks, a pair of virtual resource blocks over two slots in a subframe is assigned together by a single virtual resource block number, ![](media_svg/image51.svg) [公式≈: ^{P}O_UE_PUSCH,c^{(}^{2}^{)}^{=}^{0}].

#### 6.2.3.1 Virtual resource blocks of localized type

Virtual resource blocks of localized type are mapped directly to physical resource blocks such that virtual resource block ![](media_svg/image52.svg) [公式≈: ^{P}O_NOMINAL_PUSCH,c^{(}^{2}^{)}^{=}^{P}O_PRE^{+}^{δ}PREAMBLE_Msg3] corresponds to physical resource block![](media_svg/image53.svg) [公式≈: ^{n}PRB^{=}^{n}VRB]. Virtual resource blocks are numbered from 0 to![](media_svg/image54.svg) [公式: N_{VRB}^{DL}−1], where ![](media_svg/image55.svg) [公式≈: ^{N}VRB^{DL}^{=}^{N}RB^{DL}].

#### 6.2.3.2 Virtual resource blocks of distributed type

Virtual resource blocks of distributed type are mapped to physical resource blocks as described below.

Table 6.2.3.2-1: RB gap values

| System BW (![](media_svg/image56.svg) [公式≈: _{N}_{RB}DL]) | Gap (![](media_svg/image57.svg) [公式≈: ^{N}gap]) |  |
| --- | --- | --- |
|  | 1st Gap (![](media_svg/image58.svg) [公式≈: ^{N}gap,1]) | 2nd Gap (![](media_svg/image59.svg) [公式≈: ^{N}gap,2]) |
| 6-10 | ![](media_svg/image60.svg) [公式≈: ⊥^{N}RB^{DL}^{/}^{2}∀] | N/A |
| 11 | 4 | N/A |
| 12-19 | 8 | N/A |
| 20-26 | 12 | N/A |
| 27-44 | 18 | N/A |
| 45-49 | 27 | N/A |
| 50-63 | 27 | 9 |
| 64-79 | 32 | 16 |
| 80-110 | 48 | 16 |

The parameter ![](media_svg/image61.svg) [公式≈: ^{N}gap] is given by Table 6.2.3.2-1. For ![](media_svg/image62.svg) [公式: 6≥N_{RB}^{DL}≥49], only one gap value ![](media_svg/image63.svg) [公式≈: ^{N}gap,1] is defined and ![](media_svg/image64.svg) [公式≈: ^{N}gap^{=}^{N}gap,1]. For ![](media_svg/image65.svg) [公式: 50≥N_{RB}^{DL}≥110], two gap values ![](media_svg/image63.svg) [公式≈: ^{N}gap,1] and ![](media_svg/image66.svg) [公式≈: ^{N}gap,2] are defined. Whether ![](media_svg/image64.svg) [公式≈: ^{N}gap^{=}^{N}gap,1] or ![](media_svg/image67.svg) [公式≈: ^{N}gap^{=}^{N}gap,2]is signaled as part of the downlink scheduling assignment as described in TS36.212 [3].

Virtual resource blocks of distributed type are numbered from 0 to![](media_svg/image68.svg) [公式: N_{VRB}^{DL}−1], where ![](media_svg/image69.svg) [公式≈: ^{N}VRB^{DL}^{=}^{N}VRB,^{DL}gap1^{=}^{2}^{∪}^{min(}^{N}gap^{,}^{N}RB^{DL}^{−}^{N}gap^{)}] for ![](media_svg/image64.svg) [公式≈: ^{N}gap^{=}^{N}gap,1] and ![](media_svg/image70.svg) [公式≈: ^{N}VRB^{DL}^{=}^{N}VRB,^{DL}gap2^{=}√^{N}RB^{DL}^{/}^{2}^{N}gap∃^{∪}^{2}^{N}gap] for ![](media_svg/image71.svg) [公式≈: ^{N}gap^{=}^{N}gap,2].

Consecutive ![](media_svg/image72.svg) [公式≈: ^{N}^{~}VRB^{DL}] VRB numbers compose a unit of VRB number interleaving, where ![](media_svg/image73.svg) [公式≈: ^{N}^{~}VRB^{DL}^{=}^{N}VRB^{DL}] for ![](media_svg/image74.svg) [公式≈: ^{N}gap^{=}^{N}gap,1] and ![](media_svg/image75.svg) [公式≈: ^{N}^{~}VRB^{DL}^{=}^{2}^{N}gap] for ![](media_svg/image71.svg) [公式≈: ^{N}gap^{=}^{N}gap,2]. Interleaving of VRB numbers of each interleaving unit is performed with 4 columns and ![](media_svg/image76.svg) [公式≈: ^{N}row] rows, where ![](media_svg/image77.svg) [公式: Nrow=⊥N^{~}VRB^{DL}/(4P)∀∪P], and ![](media_svg/image78.svg) [公式: P] is RBG size as described in TS36.213[4]. VRB numbers are written row by row in the rectangular matrix, and read out column by column. ![](media_svg/image79.svg) [公式≈: ^{N}null] nulls are inserted in the last ![](media_svg/image80.svg) [公式≈: ^{N}null^{/}^{2}] rows of the 2nd and 4th column, where ![](media_svg/image81.svg) [公式≈: ^{N}null^{=}^{4}^{N}row^{−}^{N}^{~}VRB^{DL}]. Nulls are ignored when reading out. The VRB numbers mapping to PRB numbers including interleaving is derived as follows:

For even slot number ![](media_svg/image82.svg) [公式≈: ^{n}s];

![](media_svg/image83.svg) [公式≈: _{n}~_{PRB}_{(}_{n}_{s}_{)}_{=}^{√}^{⌡}⌡_{⌠}_{⌡}_{⌡}_{∞}^{n}n_{n}_{n}^{~}^{~}_{~}_{~}^{PRB}PRB_{PRB}_{PRB}^{±}±_{±}_{±}_{±}_{±}^{−}−_{−}^{N}N_{N}^{row}row_{null}_{/}+_{2}Nnull/2^{,},_{,}_{,}^{N}N_{N}_{otherwise}^{null}null_{null}^{⎯}⎯_{⎯}^{0}0_{0}^{and}and_{and}^{n}n_{n}^{~}^{~}_{~}^{VRB}VRB_{VRB}^{÷}÷_{<}^{N}N_{N}^{~}^{~}_{~}^{VRB}VRB_{VRB}^{DL}^{DL}_{DL}^{−}−_{−}^{N}N_{N}^{null}null_{null}^{and}and_{and}^{n}n_{n}^{~}^{~}_{~}^{VRB}VRB_{VRB}^{mod}mod_{mod}^{2}2_{4}_{÷}^{=}=^{1}0_{2}],

where ![](media_svg/image84.svg) [公式≈: n^{~}PRB±=2Nrow∪(n^{~}VRBmod2)+√n^{~}VRB/2∃+N^{~}VRB^{DL}∪√nVRB/N^{~}VRB^{DL}∃],

and ![](media_svg/image85.svg) [公式≈: n^{~}PRB±±=Nrow∪(n^{~}VRBmod4)+√n^{~}VRB/4∃+N^{~}VRB^{DL}∪√nVRB/N^{~}VRB^{DL}∃],

where ![](media_svg/image86.svg) [公式≈: ^{n}^{~}VRB^{=}^{n}VRB^{mod}^{N}^{~}VRB^{DL}] and ![](media_svg/image87.svg) [公式≈: ^{n}VRB] is obtained from the downlink scheduling assignment as described in TS36.213[4].

For odd slot number ![](media_svg/image82.svg) [公式≈: ^{n}s];

![](media_svg/image88.svg) [公式≈: n^{~}PRB(ns)=(n^{~}PRB(ns−1)+N^{~}VRB^{DL}/2)modN^{~}VRB^{DL}+N^{~}VRB^{DL}∪√nVRB/N^{~}VRB^{DL}∃]

Then, for all ![](media_svg/image82.svg) [公式≈: ^{n}s];

![](media_svg/image89.svg) [公式≈: ^{n}^{PRB}^{(}^{n}^{s}^{)}^{=}^{√}^{⌡}^{⌠}⌡_{∞}^{n}n^{~}^{~}^{PRB}PRB^{(}(^{n}n^{s}s^{),})+Ngap−N^{~}VRB^{DL}/2,^{n}n^{~}^{~}^{PRB}PRB^{(}(^{n}n^{s}s^{)})^{<}÷^{N}N^{~}^{~}^{VRB}VRB^{DL}^{DL}^{/}/^{2}2].

Virtual resource blocks of distributed type are not applicable to BL/CE UEs.

### 6.2.4 Resource-element groups (REGs)

Resource-element groups are used for defining the mapping of control channels to resource elements.

A resource-element group is represented by the index pair ![](media_svg/image90.svg) [公式: (k±,l±)] of the resource element with the lowest index ![](media_svg/image91.svg) [公式: k] in the group with all resource elements in the group having the same value of ![](media_svg/image92.svg) [公式: l]. The set of resource elements ![](media_svg/image93.svg) [公式: (k,l)] in a resource-element group depends on the number of cell-specific reference signals configured as described below with ![](media_svg/image94.svg) [公式≈: ^{k}0^{=}^{n}PRB^{∪}^{N}sc^{RB}], ![](media_svg/image95.svg) [公式≈: ^{0}^{≥}^{n}PRB^{<}^{N}RB^{DL}].

- In the first OFDM symbol of the first slot in a subframe the two resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image97.svg) [公式: (k,l=0)] with ![](media_svg/image98.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+5] and ![](media_svg/image99.svg) [公式: k=k_{0}+6,k_{0}+7,...,k_{0}+11], respectively.

- In the second OFDM symbol of the first slot in a subframe in case of one or two cell-specific reference signals configured, the three resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image100.svg) [公式: (k,l=1)] with ![](media_svg/image101.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+3], ![](media_svg/image102.svg) [公式: k=k_{0}+4,k_{0}+5,...,k_{0}+7] and ![](media_svg/image103.svg) [公式: k=k_{0}+8,k_{0}+9,...,k_{0}+11], respectively.

- In the second OFDM symbol of the first slot in a subframe in case of four cell-specific reference signals configured, the two resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image104.svg) [公式: (k,l=1)] with ![](media_svg/image105.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+5] and ![](media_svg/image106.svg) [公式: k=k_{0}+6,k_{0}+7,...,k_{0}+11], respectively.

- In the third OFDM symbol of the first slot in a subframe, the three resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image107.svg) [公式: (k,l=2)] with ![](media_svg/image108.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+3], ![](media_svg/image102.svg) [公式: k=k_{0}+4,k_{0}+5,...,k_{0}+7] and ![](media_svg/image103.svg) [公式: k=k_{0}+8,k_{0}+9,...,k_{0}+11], respectively.

- In the fourth OFDM symbol of the first slot in a subframe in case of normal cyclic prefix, the three resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image109.svg) [公式: (k,l=3)] with ![](media_svg/image108.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+3], ![](media_svg/image102.svg) [公式: k=k_{0}+4,k_{0}+5,...,k_{0}+7] and ![](media_svg/image103.svg) [公式: k=k_{0}+8,k_{0}+9,...,k_{0}+11], respectively.

- In the fourth OFDM symbol of the first slot in a subframe in case of extended cyclic prefix, the two resource-element groups in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements ![](media_svg/image109.svg) [公式: (k,l=3)] with ![](media_svg/image105.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+5] and ![](media_svg/image106.svg) [公式: k=k_{0}+6,k_{0}+7,...,k_{0}+11], respectively.

Mapping of a symbol-quadruplet ![](media_svg/image110.svg) [公式: z(i),z(i+1),z(i+2),z(i+3)] onto a resource-element group represented by resource-element ![](media_svg/image90.svg) [公式: (k±,l±)] is defined such that elements ![](media_svg/image111.svg) [公式: z(i)] are mapped to resource elements ![](media_svg/image93.svg) [公式: (k,l)] of the resource-element group not used for cell-specific reference signals in increasing order of ![](media_svg/image112.svg) [公式: i] and ![](media_svg/image91.svg) [公式: k]. In case a single cell-specific reference signal is configured, cell-specific reference signals shall be assumed to be present on antenna ports 0 and 1 for the purpose of mapping a symbol-quadruplet to a resource-element group, otherwise the number of cell-specific reference signals shall be assumed equal to the actual number of antenna ports used for cell-specific reference signals. The UE shall not make any assumptions about resource elements assumed to be reserved for reference signals but not used for transmission of a reference signal.

For frame structure type 3, if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe, the above definition applies to the second slot of that subframe instead of the first slot.

### 6.2.4A Enhanced Resource-Element Groups (EREGs)

EREGs are used for defining the mapping of enhanced control channels to resource elements.

There are 16 EREGs, numbered from 0 to 15, per physical resource block pair. Number all resource elements, except resource elements carrying DM-RS for antenna ports ![](media_svg/image113.svg) [公式: p={107,108,109,110}] for normal cyclic prefix or ![](media_svg/image114.svg) [公式: p={107,108}] for extended cyclic prefix, in a physical resource-block pair cyclically from 0 to 15 in an increasing order of first frequency, then time. All resource elements with number ![](media_svg/image115.svg) [公式: i] in that physical resource-block pair constitutes EREG number ![](media_svg/image116.svg) [公式: i].

For frame structure type 3, if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe, the above definition applies to the second slot of that subframe instead of the first slot.

### 6.2.4B Short Resource-Element Groups (SREGs)

Short resource-element groups (SREGs) are used for defining the mapping of short control channels to resource elements.

One SREG is composed of all resource elements in a physical resource block in a given OFDM symbol. The set of resource elements ![](media_svg/image93.svg) [公式: (k,l)] in an SREG in physical resource block ![](media_svg/image96.svg) [公式≈: ^{n}PRB] consist of resource elements with  ![](media_svg/image117.svg) [公式: k=k_{0}+0,k_{0}+1,...,k_{0}+11] with ![](media_svg/image94.svg) [公式≈: ^{k}0^{=}^{n}PRB^{∪}^{N}sc^{RB}], ![](media_svg/image95.svg) [公式≈: ^{0}^{≥}^{n}PRB^{<}^{N}RB^{DL}], all having the same value of ![](media_svg/image118.svg) [公式: l].

### 6.2.5 Guard period for half-duplex FDD operation

For type A half-duplex FDD operation, a guard period is created by the UE by

- not receiving the last part of a downlink subframe immediately preceding an uplink subframe from the same UE.

For type B half-duplex FDD operation, guard periods, each referred to as a half-duplex guard subframe, are created by the UE by

- not receiving a downlink subframe immediately preceding an uplink subframe from the same UE, and

- not receiving a downlink subframe immediately following an uplink subframe from the same UE.

### 6.2.6 Guard Period for TDD Operation

For frame structure type 2, the GP field in Figure 4.2-1 serves as a guard period.

### 6.2.7 Narrowbands and widebands

A narrowband is defined as six non-overlapping consecutive physical resource blocks in the frequency domain. The total number of downlink narrowbands in the downlink transmission bandwidth configured in the cell is given by

![](media_svg/image119.svg) [公式≈: NNB^{DL}=^{⋅}⋅_{⋅}_{√}^{N}_{6}^{RB}^{DL}^{∂}∂_{∂}_{∃}]

The narrowbands are numbered ![](media_svg/image120.svg) [公式≈: n_{NB}=0,...,N_{NB}^{DL}−1] in order of increasing physical resource-block number where narrowband ![](media_svg/image121.svg) [公式≈: ^{n}NB]is composed of physical resource-block indices

![](media_svg/image122.svg) [公式≈: ^{√}^{⌡}⌠_{⌡}_{∞}^{6if mod20}6if mod21 and 2_{61if mod21 and 2}^{niiiN}niiiNnN_{niiiNnN}^{NB0RB}NB0RBNBNB_{NB0RBNBNB}^{+++=}+++=<_{++++=÷}^{DL}^{DLDL}_{DLDL}]

where

![](media_svg/image123.svg) [公式≈: _{i}_{0}i=_{=}0_{⋅}_{⋅}_{⋅}_{√},_{N}1,...,_{2}_{RB}_{DL}5_{∂}_{∂}_{∂}_{∃}_{−}_{6}_{N}_{2}_{NB}_{DL}]

and $\hat {i}$ is according to Table 6.2.7-1 for the narrowbands used for PDSCH resource allocation in CEModeB if the higher-layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig is set, otherwise $\hat {i}=0 $.

If ![](media_svg/image124.svg) [公式: N_{NB}^{DL}÷4], a wideband is defined as four non-overlapping narrowbands in the frequency domain. The total number of downlink widebands in the downlink transmission bandwidth configured in the cell is given by

![](media_svg/image125.svg) [公式≈: NWB^{DL}=^{⋅}⋅_{⋅}_{√}^{N}_{4}^{NB}^{DL}^{∂}∂_{∂}_{∃}]

and the widebands are numbered ![](media_svg/image126.svg) [公式≈: n_{WB}=0,...,N_{WB}^{DL}−1] in order of increasing narrowband number where wideband ![](media_svg/image127.svg) [公式≈: ^{n}WB] is composed of narrowband indices ![](media_svg/image128.svg) [公式: 4n_{WB}+i] where ![](media_svg/image129.svg) [公式: i=0,1,...,3].

If ![](media_svg/image130.svg) [公式: N_{NB}^{DL}<4], then ![](media_svg/image131.svg) [公式: N_{WB}^{DL}=1] and the single wideband is composed of the ![](media_svg/image132.svg) [公式≈: _{N}_{NB}DL] non-overlapping narrowband(s).

Table 6.2.7-1: Shift of narrowbands for PDSCH resource allocation in CEModeB  when higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig is set.

| System bandwidth $ N_{RB}^{DL}$ | Shift of narrowband $\hat {i}$ |
| --- | --- |
| 6 | 0 |
| 15 | -1 for narrowband #0;0 for narrowband #1 |
| 25 | 0 for narrowbands 0, 1;- 1 for narrowband 2, 3 |
| 50 | - 1 for all narrowbands |
| 75 | -1 for narrowbands 0, 1, …, 5;0 for narrowbands 6, 7, …, 11 |
| 100 | -2 for all narrowbands. |

### 6.2.8 Guard period for narrowband and wideband retuning

For BL/CE UEs, a guard period of at most ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] OFDM symbols is created for Rx-to-Rx and Tx-to-Rx frequency retuning between two consecutive subframes.

- If the higher layer parameter ce-RetuningSymbols is set, then ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] equals ce-RetuningSymbols, otherwise ![](media_svg/image134.svg) [公式≈: _{N}_{symb}retune_{=}_{2}].

- If the higher layer parameter ce-pdsch-maxBandwidth-config is set to 5 MHz, then the rules for guard period creation defined in the remainder of this clause apply not for retuning between narrowbands but for retuning between widebands and for transmissions involving multiple widebands.

- If the UE is configured with CEModeA and higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig, the rules for guard period creation defined in the remainder of this clause apply for retuning between tuning narrowbands defined for the allocation resources not fully within one narrowband defined in Clause 6.2.7 as the consecutive 6PRBs starting from $ RB_{start}$ if $ RB_{start}$ is aligned with RBG boundary, or the consecutive 6PRBs ending at $ RB_{start}+L_{CRBs}-1 $ if $ RB_{start}+L_{CRBs}-1 $ is aligned with RBG boundary, where $ RB_{start}$ and $ L_{CRBs}$ are defined in Table 7.1.6.3-2 [4].

- If the UE is configured with CEModeB and higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig, the rules for guard period creation defined in the remainder of this clause apply for retuning between the tuning narrowband defined as the narrowband shifted according to Table 6.2.7-1.

- If the UE retunes from a first downlink narrowband to a second downlink narrowband with a different center frequency, a guard period is created by the UE not receiving at most ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] OFDM symbols in the second narrowband.

- If the UE retunes from a first uplink narrowband to a second downlink narrowband with a different center frequency for frame structure type 2, a guard period is created by the UE not receiving at most ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] OFDM symbols in the second narrowband.

Furthermore, for BL/CE UEs configured with the higher layer parameter srs-UpPtsAdd, a guard period of at most ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] OFDM or SC-FDMA symbols is created for Rx-to-Tx frequency retuning within a special subframe for frame structure type 2. Primarily, the TDD guard period (GP) specified in clause 4.2 serves as the guard period for narrowband retuning, and if GP is not sufficient then additional guard period is created by the UE according to:

- If SRS is configured to be transmitted in the first UpPTS symbol, the additional guard period is created by the UE not receiving at most ![](media_svg/image133.svg) [公式≈: _{N}_{symb}retune] DwPTS symbols in the first narrowband.

- If SRS is configured to be transmitted in the second UpPTS symbol but not in the first UpPTS symbol, the additional guard period is created by the UE primarily by not transmitting the first UpPTS symbol and (if ![](media_svg/image135.svg) [公式≈: _{N}_{symb}retune_{=}_{2}]) secondarily by not receiving the last DwPTS symbol.

## 6.3 General structure for downlink physical channels

This clause describes a general structure, applicable to more than one physical channel.

The baseband signal representing a downlink physical channel is defined in terms of the following steps:

- scrambling of coded bits in each of the codewords to be transmitted on a physical channel

- modulation of scrambled bits to generate complex-valued modulation symbols

- mapping of the complex-valued modulation symbols onto one or several transmission layers

- precoding of the complex-valued modulation symbols on each layer for transmission on the antenna ports

- mapping of complex-valued modulation symbols for each antenna port to resource elements

- generation of complex-valued time-domain OFDM signal for each antenna port

![](media/image136.emf)

Figure 6.3-1: Overview of physical channel processing

### 6.3.1 Scrambling

For each codeword ![](media_svg/image137.svg) [公式: q], the block of bits ![](media_svg/image138.svg) [公式≈: b^{(}^{q}^{)}(0),...,b^{(}^{q}^{)}(M_{bit}^{(}^{q}^{)}−1)], where ![](media_svg/image139.svg) [公式≈: _{M}_{bit}(q)] is the number of bits in codeword ![](media_svg/image137.svg) [公式: q] transmitted on the physical channel in one subframe/slot/subslot, shall be scrambled prior to modulation, resulting in a block of scrambled bits ![](media_svg/image140.svg) [公式≈: b^{~}^{(}^{q}^{)}(0),...,b^{~}^{(}^{q}^{)}(M_{bit}^{(q)}−1)]according to

![](media_svg/image141.svg) [公式≈: b^{~}^{(}^{q}^{)}(i)=(b^{(}^{q}^{)}(i)+c^{(}^{q}^{)}(i))mod2]

where the scrambling sequence ![](media_svg/image142.svg) [公式: c^{(}^{q}^{)}(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised at the start of each subframe, where the initialisation value of ![](media_svg/image143.svg) [公式≈: ^{c}init] depends on the transport channel type according to

![](media_svg/image144.svg) [公式≈: _{c}_{init}_{=}√⌡_{⌠}_{⌡}_{∞}n_{√}_{n}RNTI_{s}_{2}_{∃}∪_{∪}2_{2}^{14}_{9}+_{+}q_{N}∪_{ID}_{MBSFN}2^{13}+√ns2∃∪2^{9}+NID^{cell}for _{for }PDSCH_{PMCH}]

where ![](media_svg/image145.svg) [公式≈: ^{n}RNTI] corresponds to the RNTI associated with the PDSCH transmission as described in clause 7.1 TS36.213[4].

For BL/CE UEs, the same scrambling sequence is applied per subframe to PDSCH for a given block of ![](media_svg/image146.svg) [公式≈: ^{N}acc] subframes. The subframe number of the first subframe in each block of ![](media_svg/image147.svg) [公式≈: ^{N}acc] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image149.svg) [公式≈: (^{niN}abs,1acc^{+=}δ)^{mod0}]. For the ![](media_svg/image150.svg) [公式≈: _{j}th] block of ![](media_svg/image146.svg) [公式≈: ^{N}acc] subframes, the scrambling sequence generator shall be initialised with

![](media_svg/image151.svg) [公式≈: c_{init}=n_{RNTI}∪2^{14}+q∪2^{13}+{(j_{0}+j)N_{acc}mod10}∪2^{9}+N_{ID}^{cell}]

where

![](media_svg/image152.svg) [公式≈: ^{i}^{j}^{j}^{δ}^{0}^{=}^{=}^{=}^{0}^{√}^{⌠}_{∞}^{√}^{,}^{1}^{(}^{0,}N^{,...,}^{i}^{0}_{acc}^{+}^{⋅}^{⋅}^{⋅}^{√}^{i}−^{i}^{δ}^{0}2^{)}^{+},^{N}^{N}^{acc}^{for }for ^{abs}^{PDSCH}^{N}^{∃}^{frame}frame^{acc}^{+}^{i}^{δ}^{structure}structure^{−}^{1}^{∂}^{∂}^{∂}^{∃}^{−}^{j}^{ type} type^{0}^{1}2^{or  }and^{N}N^{acc}_{acc}^{=}=^{1}10]

and ![](media_svg/image153.svg) [公式≈: ^{i}0] is the absolute subframe number of the first downlink subframe intended for PDSCH. The PDSCH transmission spans ![](media_svg/image154.svg) [公式≈: _{N}_{abs}PDSCH] consecutive subframes including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed.

For BL/CE UEs,

- if the PDSCH is carrying SIB1-BR

- ![](media_svg/image155.svg) [公式: N_{acc}=1]

- else if the PDSCH is carrying SI message (except for SIB1-BR) or if the PDSCH transmission is associated with P-RNTI or SC-RNTI:

- ![](media_svg/image156.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image157.svg) [公式: N_{acc}=10] for frame structure type 2

- otherwise

- ![](media_svg/image155.svg) [公式: N_{acc}=1]for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA

- ![](media_svg/image156.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image157.svg) [公式: N_{acc}=10] for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB

For PDSCH with a subframe duration, up to two codewords can be transmitted in one subframe, i.e., ![](media_svg/image158.svg) [公式: q⎰{0,1}]. In the case of single codeword transmission, ![](media_svg/image137.svg) [公式: q] is equal to zero.

### 6.3.2 Modulation

For each codeword ![](media_svg/image137.svg) [公式: q], the block of scrambled bits ![](media_svg/image140.svg) [公式≈: b^{~}^{(}^{q}^{)}(0),...,b^{~}^{(}^{q}^{)}(M_{bit}^{(q)}−1)]shall be modulated as described in clause 7.1 using one of the modulation schemes in Table 6.3.2-1, resulting in a block of complex-valued modulation symbols ![](media_svg/image159.svg) [公式≈: d^{(}^{q}^{)}(0),...,d^{(}^{q}^{)}(M_{symb}^{(q)}−1)].

Table 6.3.2-1: Modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PDSCH | QPSK, 16QAM, 64QAM, 256QAM, 1024QAM |
| PMCH | QPSK, 16QAM, 64QAM, 256QAM |

### 6.3.3 Layer mapping

The complex-valued modulation symbols for each of the codewords to be transmitted are mapped onto one or several layers. Complex-valued modulation symbols ![](media_svg/image159.svg) [公式≈: d^{(}^{q}^{)}(0),...,d^{(}^{q}^{)}(M_{symb}^{(q)}−1)] for codeword ![](media_svg/image137.svg) [公式: q] shall be mapped onto the layers ![](media_svg/image160.svg) [公式≈: x(i)={x^{(}^{0}^{)}(i)...x^{(}^{Υ}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image161.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] where ![](media_svg/image162.svg) [公式: Υ] is the number of layers and ![](media_svg/image163.svg) [公式≈: _{M}_{symb}layer] is the number of modulation symbols per layer, unless ![](media_svg/image164.svg) [公式: Υ=2] and "MUST interference presence and power ratio (MUSTIdx)" signalled in the associated DCI is '00' for only one codeword in which case ![](media_svg/image165.svg) [公式≈: x(i)={Α^{(}^{0}^{)}x^{(}^{0}^{)}(i)Α^{(}^{1}^{)}x^{(}^{1}^{)}(i)}^{T}], where ![](media_svg/image166.svg) [公式≈: _{Α}_{(}_{j}_{)}_{=}2_{2}(1_{−}−_{Β}Β)] for the layer ![](media_svg/image167.svg) [公式: j] for which MUSTIdx is '00', and ![](media_svg/image168.svg) [公式≈: ^{Α}^{(}^{j}^{)}^{=}2−^{2}Β] for the layer ![](media_svg/image169.svg) [公式: j] for which MUSTIdx is not '00'. The value of![](media_svg/image170.svg) [公式: Β] is determined from Table 6.3.3-1 using MUSTIdx and the modulation order of the codeword for which MUSTIdx is not '00'.

Table 6.3.3-1: Values for ![](media_svg/image171.svg) [公式: Β]

| MUSTIdx | Modulation order |  |  |
| --- | --- | --- | --- |
|  | QPSK | 16QAM | 64QAM |
| 01 | 8/10 | 32/42 | 128/170 |
| 10 | 50/58 | 144.5/167 | 40.5/51 |
| 11 | 264.5/289 | 128/138 | 288/330 |

#### 6.3.3.1 Layer mapping for transmission on a single antenna port

For transmission on a single antenna port, a single layer is used, ![](media_svg/image172.svg) [公式: Υ=1], and the mapping is defined by

![](media_svg/image173.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)]

with ![](media_svg/image174.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)].

#### 6.3.3.2 Layer mapping for spatial multiplexing

For spatial multiplexing, the layer mapping shall be done according to Table 6.3.3.2-1. The number of layers ![](media_svg/image162.svg) [公式: Υ] is less than or equal to the number of antenna ports ![](media_svg/image175.svg) [公式: P] used for transmission of the physical channel. The case of a single codeword mapped to multiple layers is only applicable when the number of cell-specific reference signals is four or when the number of UE-specific reference signals is two or larger. For subslot/slot-PDSCH, the number of codewords is always one.

Table 6.3.3.2-1: Codeword-to-layer mapping for spatial multiplexing

| Number of layers | Number of codewords | Codeword-to-layer mapping![](media_svg/image176.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] |  |
| --- | --- | --- | --- |
| 1 | 1 | ![](media_svg/image177.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)] | ![](media_svg/image178.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)] |
| 2 | 1 | ![](media_svg/image179.svg) [公式≈: ^{x}x^{(}^{(}^{0}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{0}^{0}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image180.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{2}] |
| 2 | 2 | ![](media_svg/image181.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)] | ![](media_svg/image182.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{=}^{M}symb^{(}^{1}^{)}] |
|  |  | ![](media_svg/image183.svg) [公式≈: x^{(}^{1}^{)}(i)=d^{(}^{1}^{)}(i)] |  |
| 3 | 1 | ![](media_svg/image184.svg) [公式≈: x^{x}^{x}^{(}^{(}^{(}^{0}^{2}^{1}^{)}^{)}^{)}^{(}^{(}(^{i}^{i}i^{)}^{)})^{=}^{=}=^{d}^{d}d^{(}^{(}^{(}^{0}^{0}^{0}^{)}^{)}^{)}^{(}^{(}(^{3}^{3}3^{i}^{i}i^{)}^{+}+^{1}2^{)})] | ![](media_svg/image185.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{3}] |
| 3 | 2 | ![](media_svg/image186.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)] | ![](media_svg/image187.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{=}^{M}symb^{(}^{1}^{)}^{2}] |
|  |  | ![](media_svg/image188.svg) [公式≈: x^{x}^{(}^{(}^{2}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{1}^{1}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] |  |
| 4 | 1 | ![](media_svg/image189.svg) [公式≈: ^{x}^{x}x^{x}^{(}^{(}^{(}^{(}^{0}^{2}^{3}^{1}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{i}^{i}^{i}i^{)}^{)}^{)})^{=}^{=}^{=}=^{d}^{d}^{d}d^{(}^{(}^{(}^{(}^{0}^{0}^{0}^{0}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{4}^{4}^{4}4^{i}^{i}^{i}i^{)}^{+}^{+}+^{1}3^{2}^{)})^{)}] | ![](media_svg/image190.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{4}] |
| 4 | 2 | ![](media_svg/image179.svg) [公式≈: ^{x}x^{(}^{(}^{0}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{0}^{0}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image191.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{2}^{=}^{M}symb^{(}^{1}^{)}^{2}] |
|  |  | ![](media_svg/image192.svg) [公式≈: ^{x}x^{(}^{(}^{2}^{3}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{1}^{1}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] |  |
| 5 | 2 | ![](media_svg/image179.svg) [公式≈: ^{x}x^{(}^{(}^{0}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{0}^{0}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image193.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{2}^{=}^{M}symb^{(}^{1}^{)}^{3}] |
|  |  | ![](media_svg/image194.svg) [公式≈: ^{x}x^{x}^{(}^{(}^{(}^{2}^{4}^{3}^{)}^{)}^{)}^{(}^{(}(^{i}^{i}i^{)}^{)})^{=}^{=}=^{d}^{d}d^{(}^{(}^{(}^{1}^{1}^{1}^{)}^{)}^{)}^{(}^{(}(^{3}^{3}3^{i}^{i}i^{)}^{+}+^{1}2^{)})] |  |
| 6 | 2 | ![](media_svg/image195.svg) [公式≈: x^{x}^{x}^{(}^{(}^{(}^{0}^{2}^{1}^{)}^{)}^{)}^{(}^{(}(^{i}^{i}i^{)}^{)})^{=}^{=}=^{d}^{d}d^{(}^{(}^{(}^{0}^{0}^{0}^{)}^{)}^{)}^{(}^{(}(^{3}^{3}3^{i}^{i}i^{)}^{+}+^{1}2^{)})] | ![](media_svg/image196.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{3}^{=}^{M}symb^{(}^{1}^{)}^{3}] |
|  |  | ![](media_svg/image197.svg) [公式≈: ^{x}x^{x}^{(}^{(}^{(}^{4}^{5}^{3}^{)}^{)}^{)}^{(}^{(}(^{i}^{i}i^{)}^{)})^{=}^{=}=^{d}^{d}d^{(}^{(}^{(}^{1}^{1}^{1}^{)}^{)}^{)}^{(}^{(}(^{3}^{3}3^{i}^{i}i^{)}^{+}+^{1}2^{)})] |  |
| 7 | 2 | ![](media_svg/image195.svg) [公式≈: x^{x}^{x}^{(}^{(}^{(}^{0}^{2}^{1}^{)}^{)}^{)}^{(}^{(}(^{i}^{i}i^{)}^{)})^{=}^{=}=^{d}^{d}d^{(}^{(}^{(}^{0}^{0}^{0}^{)}^{)}^{)}^{(}^{(}(^{3}^{3}3^{i}^{i}i^{)}^{+}+^{1}2^{)})] | ![](media_svg/image198.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{3}^{=}^{M}symb^{(}^{1}^{)}^{4}] |
|  |  | ![](media_svg/image199.svg) [公式≈: ^{x}x^{x}^{x}^{(}^{(}^{(}^{(}^{4}^{6}^{5}^{3}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{i}^{i}^{i}i^{)}^{)}^{)})^{=}^{=}^{=}=^{d}^{d}^{d}d^{(}^{(}^{(}^{(}^{1}^{1}^{1}^{1}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{4}^{4}^{4}4^{i}^{i}^{i}i^{)}^{+}^{+}+^{1}3^{2}^{)})^{)}] |  |
| 8 | 2 | ![](media_svg/image200.svg) [公式≈: ^{x}^{x}x^{x}^{(}^{(}^{(}^{(}^{0}^{2}^{3}^{1}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{i}^{i}^{i}i^{)}^{)}^{)})^{=}^{=}^{=}=^{d}^{d}^{d}d^{(}^{(}^{(}^{(}^{0}^{0}^{0}^{0}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{4}^{4}^{4}4^{i}^{i}^{i}i^{)}^{+}^{+}+^{1}3^{2}^{)})^{)}] | ![](media_svg/image201.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{4}^{=}^{M}symb^{(}^{1}^{)}^{4}] |
|  |  | ![](media_svg/image202.svg) [公式≈: ^{x}x^{x}^{x}^{(}^{(}^{(}^{(}^{7}^{4}^{6}^{5}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{i}^{i}^{i}i^{)}^{)}^{)})^{=}^{=}^{=}=^{d}^{d}^{d}d^{(}^{(}^{(}^{(}^{1}^{1}^{1}^{1}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{4}^{4}^{4}4^{i}^{i}^{i}i^{)}^{+}^{+}+^{1}3^{2}^{)})^{)}] |  |

#### 6.3.3.3 Layer mapping for transmit diversity

For transmit diversity, the layer mapping shall be done according to Table 6.3.3.3-1. There is only one codeword and the number of layers ![](media_svg/image162.svg) [公式: Υ] is equal to the number of antenna ports ![](media_svg/image175.svg) [公式: P] used for transmission of the physical channel.

Table 6.3.3.3-1: Codeword-to-layer mapping for transmit diversity

| Number of layers | Number of codewords | Codeword-to-layer mapping![](media_svg/image176.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] |  |
| --- | --- | --- | --- |
| 2 | 1 | ![](media_svg/image203.svg) [公式≈: ^{x}x^{(}^{(}^{1}^{0}^{)}^{)}(^{(}i^{i})^{)}=^{=}d^{d}^{(}^{(}^{0}^{0}^{)}^{)}(^{(}2^{2}i^{i}^{)}+1)] | ![](media_svg/image204.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{2}] |
| 4 | 1 | ![](media_svg/image205.svg) [公式≈: ^{x}^{x}^{x}x^{(}^{(}^{(}^{(}^{1}^{3}^{0}^{2}^{)}^{)}^{)}^{)}^{(}(^{(}^{(}^{i}i^{i}^{i}^{)})^{)}^{)}^{=}=^{=}^{=}^{d}d^{d}^{d}^{(}^{(}^{(}^{(}^{0}^{0}^{0}^{0}^{)}^{)}^{)}^{)}^{(}(^{(}^{(}^{4}4^{4}^{4}^{i}i^{i}^{i}^{)}^{+}+^{+}^{1}3^{2}^{)})^{)}] | ![](media_svg/image206.svg) [公式≈: ^{M}^{symb}^{layer}^{=}^{√}^{⌡}^{⌠}_{⌡}_{∞}(M_{symb}^{(}^{0}^{M}^{)}^{symb}^{(}^{0}+^{)}2)^{4}4if^{if}M^{M}_{symb}^{symb}^{(}^{(}^{0}^{0}^{)}^{)}mod^{mod}4^{4}⎯^{=}^{0}0]If ![](media_svg/image207.svg) [公式≈: M_{symb}^{(}^{0}^{)}mod4⎯0] two null symbols shall be appended to ![](media_svg/image208.svg) [公式≈: d^{(}^{0}^{)}(M_{symb}^{(}^{0}^{)}−1)] |

### 6.3.4 Precoding

The precoder takes as input a block of vectors![](media_svg/image209.svg) [公式≈: x(i)={x^{(}^{0}^{)}(i)...x^{(}^{Υ}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image176.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] from the layer mapping and generates a block of vectors![](media_svg/image210.svg) [公式≈: y(i)={...y^{(}^{p}^{)}(i)...}^{T}], ![](media_svg/image211.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1] to be mapped onto resources on each of the antenna ports, where ![](media_svg/image212.svg) [公式: y^{(}^{p}^{)}(i)] represents the signal for antenna port![](media_svg/image34.svg) [公式: p].

#### 6.3.4.1 Precoding for transmission on a single antenna port

For transmission on a single antenna port, precoding is defined by

![](media_svg/image213.svg) [公式≈: y^{(}^{p}^{)}(i)=x^{(}^{0}^{)}(i)]

where ![](media_svg/image214.svg) [公式: p⎰{0,4,5,7,8,11,13,107,108,109,110}] is the number of the single antenna port used for transmission of the physical channel and ![](media_svg/image215.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image216.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

#### 6.3.4.2 Precoding for spatial multiplexing using antenna ports with cell-specific reference signals

Precoding for spatial multiplexing using antenna ports with cell-specific reference signals is only used in combination with layer mapping for spatial multiplexing as described in clause 6.3.3.2. Spatial multiplexing supports two or four antenna ports and the set of antenna ports used is ![](media_svg/image217.svg) [公式: p⎰{0,1}]or![](media_svg/image218.svg) [公式: p⎰{0,1,2,3}], respectively.

##### 6.3.4.2.1 Precoding without CDD

Without Cyclic Delay Diversity (CDD), precoding for spatial multiplexing is defined by

![](media_svg/image219.svg) [公式≈: ^{⊥}^{⋅}^{⋅}⋅_{√}_{y}^{y}(P^{(}^{0}−^{μ}^{)}1^{(})^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}^{=}^{W}^{(}^{i}^{)}^{⊥}^{⋅}^{⋅}⋅_{√}_{x}^{x}(Υ^{(}^{0}−^{μ}^{)}1)^{(}^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}]

where the precoding matrix ![](media_svg/image220.svg) [公式: W(i)] is of size ![](media_svg/image221.svg) [公式: P≠Υ] and ![](media_svg/image215.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image216.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

For spatial multiplexing, the values of ![](media_svg/image220.svg) [公式: W(i)] shall be selected among the precoder elements in the codebook configured in the eNodeB and the UE. The eNodeB can further confine the precoder selection in the UE to a subset of the elements in the codebook using codebook subset restrictions. The configured codebook shall be selected from Table 6.3.4.2.3-1 or 6.3.4.2.3-2.

##### 6.3.4.2.2 Precoding for large delay CDD

For large-delay CDD, precoding for spatial multiplexing is defined by

![](media_svg/image222.svg) [公式≈: ^{⊥}^{⋅}^{⋅}⋅_{√}_{y}^{y}(P^{(}^{0}−^{μ}^{)}1^{(})^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}^{=}^{W}^{(}^{i}^{)}^{D}^{(}^{i}^{)}^{U}^{⊥}^{⋅}^{⋅}⋅_{√}_{x}^{x}(Υ^{(}^{0}−^{μ}^{)}1)^{(}^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}]

where the precoding matrix![](media_svg/image220.svg) [公式: W(i)]is of size ![](media_svg/image221.svg) [公式: P≠Υ] and ![](media_svg/image215.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image216.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}]. The diagonal size-![](media_svg/image223.svg) [公式: Υ≠Υ]matrix ![](media_svg/image224.svg) [公式: D(i)] supporting cyclic delay diversity and the size-![](media_svg/image223.svg) [公式: Υ≠Υ] matrix ![](media_svg/image225.svg) [公式: U] are both given by Table 6.3.4.2.2-1 for different numbers of layers ![](media_svg/image226.svg) [公式: Υ].

The values of the precoding matrix ![](media_svg/image220.svg) [公式: W(i)] shall be selected among the precoder elements in the codebook configured in the eNodeB and the UE. The eNodeB can further confine the precoder selection in the UE to a subset of the elements in the codebook using codebook subset restriction. The configured codebook shall be selected from Table 6.3.4.2.3-1 or 6.3.4.2.3-2.

For 2 antenna ports, the precoder is selected according to ![](media_svg/image227.svg) [公式: W(i)=C_{1}] where ![](media_svg/image228.svg) [公式≈: ^{C}1] denotes the precoding matrix corresponding to precoder index 0 in Table 6.3.4.2.3-1.

For 4 antenna ports, the UE may assume that the eNodeB cyclically assigns different precoders to different vectors ![](media_svg/image229.svg) [公式≈: {x^{(}^{0}^{)}(i)...x^{(}^{Υ}^{−}^{1}^{)}(i)}^{T}]on the physical downlink shared channel as follows. A different precoder is used every ![](media_svg/image230.svg) [公式: Υ]vectors, where ![](media_svg/image231.svg) [公式: Υ] denotes the number of transmission layers in the case of spatial multiplexing. In particular, the precoder is selected according to ![](media_svg/image232.svg) [公式: W(i)=C_{k}], where ![](media_svg/image233.svg) [公式: k] is the precoder index given by ![](media_svg/image234.svg) [公式≈: k=^{⊇}⊕_{⊕}_{⊗}^{⋅}_{⋅}_{√}_{Υ}^{i}^{∂}_{∂}_{∃}mod4^{⇒}⇐_{⇐}_{⇔}+1⎰{1,2,3,4}] and ![](media_svg/image235.svg) [公式≈: C_{1},C_{2},C_{3},C_{4}]denote precoder matrices corresponding to precoder indices 12,13,14 and 15, respectively, in Table 6.3.4.2.3-2.

Table 6.3.4.2.2-1: Large-delay cyclic delay diversity

| Number of layers ![](media_svg/image236.svg) [公式: Υ] | ![](media_svg/image225.svg) [公式: U] | ![](media_svg/image224.svg) [公式: D(i)] |
| --- | --- | --- |
| 2 | ![](media_svg/image237.svg) [公式≈: ^{1}_{2}^{⊥}⋅_{√}^{1}_{1}_{e}−j^{1}2Π2^{∀}∂_{∃}] | ![](media_svg/image238.svg) [公式≈: ^{⊥}⋅_{√}^{1}_{0}_{e}−j^{0}2Πi2^{∀}∂_{∃}] |
| 3 | ![](media_svg/image239.svg) [公式≈: 1_{3}^{⊥}⋅_{⋅}_{⋅}_{√}^{1}_{1}_{1}_{e}_{e}−_{−}j_{j}^{1}2_{4}Π_{Π}3_{3}_{e}_{e}−_{−}j_{j}^{1}_{8}4_{Π}Π_{3}3^{∀}∂_{∂}_{∂}_{∃}] | ![](media_svg/image240.svg) [公式≈: ^{⊥}⋅_{⋅}_{⋅}_{√}^{1}_{0}_{0}_{e}−j^{0}_{0}2Πi3_{e}_{−}_{j}^{0}_{0}_{4}_{Π}_{i}_{3}^{∀}∂_{∂}_{∂}_{∃}] |
| 4 | ![](media_svg/image241.svg) [公式≈: _{1}_{2}^{⊥}⋅_{⋅}_{⋅}_{⋅}_{√}^{1}_{1}_{1}_{1}_{e}_{e}_{e}−_{−}_{−}j_{j}_{j}^{1}_{6}2_{4}_{Π}Π_{Π}_{4}4_{4}_{e}_{e}_{e}_{−}−_{−}_{j}j_{j}_{12}^{1}_{8}4_{Π}Π_{Π}_{4}4_{4}_{e}_{e}_{e}_{−}_{−}−_{j}_{j}j_{12}_{18}^{1}6Π_{Π}_{Π}4_{4}_{4}^{∀}∂_{∂}_{∂}_{∂}_{∃}] | ![](media_svg/image242.svg) [公式≈: ^{⊥}⋅_{⋅}_{⋅}_{⋅}_{√}^{1}_{0}_{0}_{0}_{e}−j^{0}_{0}_{0}2Πi4_{e}_{−}_{j}^{0}_{0}_{0}_{4}_{Π}_{i}_{4}_{e}_{−}_{j}^{0}_{0}_{0}_{6}_{Π}_{i}_{4}^{∀}∂_{∂}_{∂}_{∂}_{∃}] |

##### 6.3.4.2.3 Codebook for precoding and CSI reporting

For transmission on two antenna ports, ![](media_svg/image243.svg) [公式: p⎰{0,1}], and for the purpose of CSI reporting based on two antenna ports ![](media_svg/image243.svg) [公式: p⎰{0,1}] or ![](media_svg/image244.svg) [公式: p⎰{15,16}], the precoding matrix ![](media_svg/image220.svg) [公式: W(i)] shall be selected from Table 6.3.4.2.3-1 or a subset thereof. For the closed-loop spatial multiplexing transmission mode defined in TS36.213 [4], the codebook index 0 is not used when the number of layers is ![](media_svg/image245.svg) [公式: Υ=2].

Table 6.3.4.2.3-1: Codebook for transmission on antenna ports ![](media_svg/image246.svg) [公式: {0,1}] and for CSI reporting based on antenna ports ![](media_svg/image247.svg) [公式: {0,1}] or ![](media_svg/image248.svg) [公式: {15,16}]

| Codebook index | Number of layers ![](media_svg/image236.svg) [公式: Υ] |  |
| --- | --- | --- |
|  | 1 | 2 |
| 0 | ![](media_svg/image249.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{1}∀_{∂}_{∃}] | ![](media_svg/image250.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{0}_{1}0∀_{∂}_{∃}] |
| 1 | ![](media_svg/image251.svg) [公式≈: 1_{2}⊥_{⋅}_{√}_{−}1_{1}∀_{∂}_{∃}] | ![](media_svg/image252.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{1}_{−}1_{1}∀_{∂}_{∃}] |
| 2 | ![](media_svg/image253.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{j}∀_{∂}_{∃}] | ![](media_svg/image254.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{j}_{−}1_{j}∀_{∂}_{∃}] |
| 3 | ![](media_svg/image255.svg) [公式≈: 1_{2}⊥_{⋅}_{√}_{−}1_{j}∀_{∂}_{∃}] | - |



For transmission on four antenna ports, ![](media_svg/image256.svg) [公式: p⎰{0,1,2,3}], the precoding matrix ![](media_svg/image257.svg) [公式: W] shall be selected from Table 6.3.4.2.3-2 or a subset thereof. For the purpose of CSI reporting based on four antenna ports ![](media_svg/image256.svg) [公式: p⎰{0,1,2,3}] or ![](media_svg/image258.svg) [公式: p⎰{15,16,17,18}], the precoding matrix ![](media_svg/image257.svg) [公式: W] shall be selected from Table 6.3.4.2.3-2 or a subset thereof except for alternativeCodeBookEnabledFor4TX-r12 =TRUE in which case the precoding matrix ![](media_svg/image257.svg) [公式: W] shall be selected from Tables 7.2.4-0A, 7.2.4-0B, 7.2.4-0C, 7.2.4-0D in [4] or a subset thereof, and except for advancedCodebookEnabled = TRUE in which case the precoding matrix  shall be selected from Table 7.2.4-17C in [4] or a subset thereof. The quantity ![](media_svg/image260.svg) [公式≈: _{W}_{n}{s}] denotes the matrix defined by the columns given by the set ![](media_svg/image261.svg) [公式: {s}] from the expression ![](media_svg/image262.svg) [公式≈: W_{n}=I−2u_{n}u_{n}^{H}u_{n}^{H}u_{n}] where ![](media_svg/image263.svg) [公式: I] is the ![](media_svg/image264.svg) [公式: 4≠4] identity matrix and the vector ![](media_svg/image265.svg) [公式≈: ^{u}n] is given by Table 6.3.4.2.3-2.

Table 6.3.4.2.3-2: Codebook for transmission on antenna ports![](media_svg/image266.svg) [公式: {0,1,2,3}] and for CSI reporting based on antenna ports ![](media_svg/image267.svg) [公式: {0,1,2,3}] or ![](media_svg/image268.svg) [公式: {15,16,17,18}]

| Codebook index | ![](media_svg/image269.svg) [公式≈: ^{u}n] | Number of layers ![](media_svg/image236.svg) [公式: Υ] |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | 1 | 2 | 3 | 4 |
| 0 | ![](media_svg/image270.svg) [公式: u_{0}={1−1−1−1}^{T}] | ![](media_svg/image271.svg) [公式≈: _{W}_{0}{1}] | ![](media_svg/image272.svg) [公式≈: _{W}_{0}{14}_{2}] | ![](media_svg/image273.svg) [公式≈: _{W}_{0}{124}_{3}] | ![](media_svg/image274.svg) [公式≈: _{W}_{0}{1234}_{2}] |
| 1 | ![](media_svg/image275.svg) [公式: u_{1}={1−j1j}^{T}] | ![](media_svg/image276.svg) [公式≈: _{W}_{1}{1}] | ![](media_svg/image277.svg) [公式≈: _{W}_{1}{12}_{2}] | ![](media_svg/image278.svg) [公式≈: _{W}_{1}{123}_{3}] | ![](media_svg/image279.svg) [公式≈: _{W}_{1}{1234}_{2}] |
| 2 | ![](media_svg/image280.svg) [公式: u_{2}={11−11}^{T}] | ![](media_svg/image281.svg) [公式≈: _{W}_{2}{1}] | ![](media_svg/image282.svg) [公式≈: _{W}_{2}{12}_{2}] | ![](media_svg/image283.svg) [公式≈: _{W}_{2}{123}_{3}] | ![](media_svg/image284.svg) [公式≈: _{W}_{2}{3214}_{2}] |
| 3 | ![](media_svg/image285.svg) [公式: u_{3}={1j1−j}^{T}] | ![](media_svg/image286.svg) [公式≈: _{W}_{3}{1}] | ![](media_svg/image287.svg) [公式≈: _{W}_{3}{12}_{2}] | ![](media_svg/image288.svg) [公式≈: _{W}_{3}{123}_{3}] | ![](media_svg/image289.svg) [公式≈: _{W}_{3}{3214}_{2}] |
| 4 | ![](media_svg/image290.svg) [公式: u_{4}={1(−1−j)2−j(1−j)2}^{T}] | ![](media_svg/image291.svg) [公式≈: _{W}_{4}{1}] | ![](media_svg/image292.svg) [公式≈: _{W}_{4}{14}_{2}] | ![](media_svg/image293.svg) [公式≈: _{W}_{4}{124}_{3}] | ![](media_svg/image294.svg) [公式≈: _{W}_{4}{1234}_{2}] |
| 5 | ![](media_svg/image295.svg) [公式: u_{5}={1(1−j)2j(−1−j)2}^{T}] | ![](media_svg/image296.svg) [公式≈: _{W}_{5}{1}] | ![](media_svg/image297.svg) [公式≈: _{W}_{5}{14}_{2}] | ![](media_svg/image298.svg) [公式≈: _{W}_{5}{124}_{3}] | ![](media_svg/image299.svg) [公式≈: _{W}_{5}{1234}_{2}] |
| 6 | ![](media_svg/image300.svg) [公式: u_{6}={1(1+j)2−j(−1+j)2}^{T}] | ![](media_svg/image301.svg) [公式≈: _{W}_{6}{1}] | ![](media_svg/image302.svg) [公式≈: _{W}_{6}{13}_{2}] | ![](media_svg/image303.svg) [公式≈: _{W}_{6}{134}_{3}] | ![](media_svg/image304.svg) [公式≈: _{W}_{6}{1324}_{2}] |
| 7 | ![](media_svg/image305.svg) [公式: u_{7}={1(−1+j)2j(1+j)2}^{T}] | ![](media_svg/image306.svg) [公式≈: _{W}_{7}{1}] | ![](media_svg/image307.svg) [公式≈: _{W}_{7}{13}_{2}] | ![](media_svg/image308.svg) [公式≈: _{W}_{7}{134}_{3}] | ![](media_svg/image309.svg) [公式≈: _{W}_{7}{1324}_{2}] |
| 8 | ![](media_svg/image310.svg) [公式: u_{8}={1−111}^{T}] | ![](media_svg/image311.svg) [公式≈: _{W}_{8}{1}] | ![](media_svg/image312.svg) [公式≈: _{W}_{8}{12}_{2}] | ![](media_svg/image313.svg) [公式≈: _{W}_{8}{124}_{3}] | ![](media_svg/image314.svg) [公式≈: _{W}_{8}{1234}_{2}] |
| 9 | ![](media_svg/image315.svg) [公式: u_{9}={1−j−1−j}^{T}] | ![](media_svg/image316.svg) [公式≈: _{W}_{9}{1}] | ![](media_svg/image317.svg) [公式≈: _{W}_{9}{14}_{2}] | ![](media_svg/image318.svg) [公式≈: _{W}_{9}{134}_{3}] | ![](media_svg/image319.svg) [公式≈: _{W}_{9}{1234}_{2}] |
| 10 | ![](media_svg/image320.svg) [公式: u_{10}={111−1}^{T}] | ![](media_svg/image321.svg) [公式≈: _{W}_{10}{1}] | ![](media_svg/image322.svg) [公式≈: _{W}_{10}{13}_{2}] | ![](media_svg/image323.svg) [公式≈: _{W}_{10}{123}_{3}] | ![](media_svg/image324.svg) [公式≈: _{W}_{10}{1324}_{2}] |
| 11 | ![](media_svg/image325.svg) [公式: u_{11}={1j−1j}^{T}] | ![](media_svg/image326.svg) [公式≈: _{W}_{11}{1}] | ![](media_svg/image327.svg) [公式≈: _{W}_{11}{13}_{2}] | ![](media_svg/image328.svg) [公式≈: _{W}_{11}{134}_{3}] | ![](media_svg/image329.svg) [公式≈: _{W}_{11}{1324}_{2}] |
| 12 | ![](media_svg/image330.svg) [公式: u_{12}={1−1−11}^{T}] | ![](media_svg/image331.svg) [公式≈: _{W}_{12}{1}] | ![](media_svg/image332.svg) [公式≈: _{W}_{12}{12}_{2}] | ![](media_svg/image333.svg) [公式≈: _{W}_{12}{123}_{3}] | ![](media_svg/image334.svg) [公式≈: _{W}_{12}{1234}_{2}] |
| 13 | ![](media_svg/image335.svg) [公式: u_{13}={1−11−1}^{T}] | ![](media_svg/image336.svg) [公式≈: _{W}_{13}{1}] | ![](media_svg/image337.svg) [公式≈: _{W}_{13}{13}_{2}] | ![](media_svg/image338.svg) [公式≈: _{W}_{13}{123}_{3}] | ![](media_svg/image339.svg) [公式≈: _{W}_{13}{1324}_{2}] |
| 14 | ![](media_svg/image340.svg) [公式: u_{14}={11−1−1}^{T}] | ![](media_svg/image341.svg) [公式≈: _{W}_{14}{1}] | ![](media_svg/image342.svg) [公式≈: _{W}_{14}{13}_{2}] | ![](media_svg/image343.svg) [公式≈: _{W}_{14}{123}_{3}] | ![](media_svg/image344.svg) [公式≈: _{W}_{14}{3214}_{2}] |
| 15 | ![](media_svg/image345.svg) [公式: u_{15}={1111}^{T}] | ![](media_svg/image346.svg) [公式≈: _{W}_{15}{1}] | ![](media_svg/image347.svg) [公式≈: _{W}_{15}{12}_{2}] | ![](media_svg/image348.svg) [公式≈: _{W}_{15}{123}_{3}] | ![](media_svg/image349.svg) [公式≈: _{W}_{15}{1234}_{2}] |

For the purpose of CSI reporting for 8, 12, 16, 20, 24, 28, and 32 CSI reference signals the codebooks are given in clause 7.2.4 of TS36.213 [4].

#### 6.3.4.3 Precoding for transmit diversity

Precoding for transmit diversity is only used in combination with layer mapping for transmit diversity as described in clause 6.3.3.3. The precoding operation for transmit diversity is defined for two and four antenna ports.

For transmission on two antenna ports, ![](media_svg/image243.svg) [公式: p⎰{0,1}], the output ![](media_svg/image350.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)y^{(}^{1}^{)}(i)}^{T}], ![](media_svg/image211.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1] of the precoding operation is defined by

![](media_svg/image351.svg) [公式≈: ^{⊥}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{√}y_{y}(_{(}^{y}^{y}_{1}0_{)}^{(})^{(}^{1}^{0}_{(}(^{)}^{)}_{2}2^{(}^{(}_{i}i^{2}^{2}_{+}+^{i}^{i}^{)}^{)}_{1}1_{)})^{∀}^{∂}^{∂}∂_{∂}_{∂}_{∃}^{=}^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0^{−}1^{0}_{0}^{1}_{−}^{0}0^{j}_{j}^{0}_{0}^{j}j^{∀}^{∂}^{∂}∂_{∂}_{∃}^{⊥}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{√}^{Re}Im^{Re}_{Im}(^{(}_{(}^{(}x^{x}_{x}^{x}(^{(}_{(}^{(}_{1}0^{1}^{0}_{)}^{)})^{)}_{(}^{(}(^{(}_{i}^{i}i^{i}_{)}^{)})^{)}_{)}^{)})^{)}^{∀}^{∂}^{∂}∂_{∂}_{∂}_{∃}]

for![](media_svg/image352.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] with ![](media_svg/image353.svg) [公式≈: ^{M}symb^{ap}^{=}^{2}^{M}symb^{layer}].

For rank=1 transmission on two antenna ports, ![](media_svg/image354.svg) [公式: p⎰{7,8}], the output ![](media_svg/image355.svg) [公式≈: y(i)={y^{(}^{7}^{)}(i)y^{(}^{8}^{)}(i)}^{T}], ![](media_svg/image211.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1] of the precoding operation is defined by

![](media_svg/image356.svg) [公式≈: ^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}⋅√y^{y}^{(}^{y}^{(}^{p}^{y}^{p}^{(}^{+}^{(}^{p}^{)}^{1}^{p}^{(}^{)}^{+}(^{)}^{1}^{2}^{(}^{)}2^{i}^{(}^{2}i^{2}^{+}^{i}+^{i}^{)}^{1}^{)}1^{)})^{∀}^{∂}^{∂}^{∂}^{∂}∂∃^{=}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}√^{1}1^{0}^{0}−^{0}^{0}^{j}j^{−}^{1}^{0}0^{1}^{0}0^{j}^{j}^{∀}^{∂}^{∂}^{∂}^{∂}∃^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}⋅√^{Re}^{Im}^{Re}Im^{(}^{(}(^{(}^{x}^{x}x^{x}^{(}^{(}^{(}^{(}^{1}^{0}^{1}^{0}^{)}^{)}^{)}^{)}(^{(}^{(}^{(}i^{i}^{i}^{i})^{)}^{)}^{)})^{)}^{)}^{)}^{∀}^{∂}^{∂}^{∂}^{∂}∂∃]

where ![](media_svg/image357.svg) [公式: p=7].

For transmission on four antenna ports,![](media_svg/image358.svg) [公式: p⎰{0,1,2,3}], the output ![](media_svg/image359.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)y^{(}^{1}^{)}(i)y^{(}^{2}^{)}(i)y^{(}^{3}^{)}(i)}^{T}], ![](media_svg/image211.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1] of the precoding operation is defined by

![](media_svg/image360.svg) [公式≈: ^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}_{y}^{y}_{y}_{y}_{y}_{y}y^{y}_{y}^{y}^{y}^{y}_{(}^{(}_{(}_{(}_{(}_{(}(^{(}_{(}^{(}^{(}^{(}^{y}^{y}^{y}^{y}1^{0}_{2}_{3}_{1}_{0}_{2}_{3}^{1}^{0}^{2}^{3})_{)}_{)}^{)}_{)}_{)}_{)}^{)}_{)}^{(}^{(}^{)}^{(}^{)}^{)}^{(}(^{1}^{0}^{2}^{3}_{(}_{(}^{(}_{(}_{(}_{(}^{(}_{(}^{(}^{(}^{(}^{)}4^{)}_{4}^{)}^{)}_{4}^{4}_{4}_{4}_{4}^{4}_{4}^{4}^{4}^{4}^{(}^{(}^{(}^{(}i_{i}_{i}^{i}_{i}_{i}_{i}^{i}_{i}^{i}^{i}^{i}^{4}^{4}^{4}^{4}+_{+}_{+}^{+}_{+}_{+}_{+}^{+}_{+}^{+}^{+}^{+}^{i}^{i}^{i}^{i}^{)}^{)}^{)}^{)}^{1}2_{3}^{1}^{1}_{2}_{3}^{1}^{2}_{3}_{2}_{3}^{)}^{)}^{)}_{)}^{)})_{)}_{)}_{)}_{)}^{)}_{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{=}^{1}^{2}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}^{1}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{−}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{1}1_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}_{0}_{0}_{0}_{0}_{0}_{−}_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{1}^{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}_{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}_{0}_{0}_{0}_{0}_{0}j_{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{j}_{j}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{√}^{Re}^{Re}_{Im}^{Im}^{Re}_{Im}^{Re}Im_{(}^{(}^{(}^{(}_{(}^{(}(^{(}_{x}^{x}^{x}^{x}_{x}^{x}x^{x}_{(}^{(}^{(}^{(}_{(}^{(}(^{(}1^{0}^{1}_{2}_{3}^{0}^{2}^{3})^{)}_{)}^{)}^{)}_{)}^{)}^{)}(^{(}_{(}^{(}^{(}_{(}^{(}^{(}i^{i}_{i}^{i}^{i}_{i}^{i}^{i})^{)}_{)}^{)}^{)}_{)}^{)}^{)})^{)}_{)}^{)}^{)}_{)}^{)}^{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∃}]

for ![](media_svg/image361.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] with ![](media_svg/image362.svg) [公式≈: ^{M}^{symb}^{ap}^{=}^{√}^{⌡}^{⌠}_{⌡}_{∞}(4M^{4}^{M}_{symb}^{layer}^{symb}^{layer})−2if^{if}M^{M}_{symb}^{symb}^{(}^{(}^{0}^{0}^{)}^{)}mod^{mod}4^{4}⎯^{=}^{0}0].

#### 6.3.4.4 Precoding for spatial multiplexing using antenna ports with UE-specific reference signals

Precoding for spatial multiplexing using antenna ports with UE-specific reference signals is only used in combination with layer mapping for spatial multiplexing as described in clause 6.3.3.2. Spatial multiplexing using antenna ports with UE-specific reference signals supports up to eight antenna ports.

If the higher-layer parameter dmrs-tableAlt is set to TRUE and the set of antenna ports ![](media_svg/image363.svg) [公式: p={11,13}] is used for two layers transmission, the precoding operation for transmission on the two antenna ports is defined by

![](media_svg/image364.svg) [公式≈: ^{⊥}^{⋅}⋅_{√}y^{y}^{(}^{(}^{13}^{11}^{)}^{)}^{(}(^{i}i^{)})^{∀}^{∂}∂_{∃}^{=}^{⊥}^{⋅}⋅_{√}^{x}x^{(}^{(}^{1}^{0}^{)}^{)}(^{(}i^{i})^{)}^{∀}^{∂}∂_{∃}]

where ![](media_svg/image215.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image216.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

If the higher-layer parameter semiOpenLoop is set to TRUE for subframe PDSCH or the higher-layer parameter semiOpenLoop-STTI is set to TRUE for slot/subslot PDSCH and the set of antenna ports ![](media_svg/image365.svg) [公式: p=7,8] is used for rank=2 transmission, the precoding operation for transmission on the two antenna ports is defined by

![](media_svg/image366.svg) [公式≈: ^{⊥}^{⋅}⋅√y^{y}^{(}^{(}^{p}^{p}^{+}^{)}^{1}^{)}^{(}(^{i}^{)}i)^{∀}^{∂}∂∃^{=}^{1}2^{⊥}^{⋅}√e^{1}^{j}^{Θ}^{n}je^{j}^{j}^{Θ}^{n}−e^{1}^{j}^{Θ}^{n}−je^{j}^{j}^{Θ}^{n}^{∀}^{∂}∃^{⊥}^{⋅}^{⋅}^{⋅}_{⋅}_{⋅}_{√}^{Re}^{Im}Re_{Im}^{{}^{{}_{{}{^{x}^{x}_{x}x^{(}^{(}_{(}^{(}_{1}^{0}^{1}^{0}_{)}^{)}^{)}^{)}_{(}(^{(}^{(}_{i}i^{i}^{i}_{)})^{)}^{)}_{}}}^{}}^{}}^{∀}^{∂}^{∂}^{∂}_{∂}_{∂}_{∃}]

where ![](media_svg/image357.svg) [公式: p=7] and ![](media_svg/image367.svg) [公式: Θ_{n}=Π(imod2)2].

If the number of codewords is two and the DCI associated with the scheduled PDSCH is of Format 2D and the 'PDSCH RE Mapping and Quasi-Co-Location indicator' field in the DCI indicates a higher-layer configured PDSCH-RE-MappingQCL containing two sets of parameters, the precoding operation for transmission on  antenna ports is defined by

where ,  and set of antenna ports  used is given by Table 6.3.4.4-1.

Table 6.3.4.4-1: Layer-to-port mapping for two-codeword transmission when PDSCH-RE-MappingQCL contains two sets of parameters

| Number of layers | Layer-to-port mapping |
| --- | --- |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |

Otherwise, the set of antenna ports used is ![](media_svg/image382.svg) [公式: p=7,8,...,Υ+6]and the precoding operation for transmission on ![](media_svg/image383.svg) [公式: Υ] antenna ports is defined by

![](media_svg/image384.svg) [公式≈: ^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{√}y^{y}^{y}^{(}^{6}^{(}^{(}^{+}^{7}^{8}^{μ}^{Υ}^{)}^{)}^{(}^{(}^{)}^{i}^{i}(^{)}^{)}i)^{∀}^{∂}^{∂}^{∂}^{∂}∂_{∃}^{=}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{√}x^{x}^{x}^{(}^{Υ}^{(}^{(}^{1}^{0}^{−}^{μ}^{)}^{)}^{1}^{(}^{)}^{(}^{i}^{i}(^{)}^{)}i)^{∀}^{∂}^{∂}^{∂}^{∂}∂_{∃}]

where ![](media_svg/image215.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image216.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

### 6.3.5 Mapping to resource elements



For each of the antenna ports used for transmission of the physical channel, the block of complex-valued symbols ![](media_svg/image385.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}^{ap}−1)] shall conform to the downlink power allocation specified in clause 5.2 in TS 36.213 [4] and be mapped in sequence starting with ![](media_svg/image386.svg) [公式: y^{(}^{p}^{)}(0)] to resource elements ![](media_svg/image387.svg) [公式: (k,l)] which meet all of the following criteria in the current subframe:

- they are in the physical resource blocks corresponding to the virtual resource blocks assigned for transmission, and

- they are not used for transmission of the core part of PBCH, synchronization signals, and

- they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 4, and

The mapping to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] not reserved for other purposes shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] over the assigned physical resource blocks and then the index![](media_svg/image389.svg) [公式: l], starting with the first slot in a subframe.

For BL/CE UEs, if the higher layer parameter ce-punctured-subcarriers-DL is configured, then in case of MPDCCH or PDSCH transmission associated with C-RNTI or SPS C-RNTI,

- The parameter ce-punctured-subcarriers-DL indicates the number of subcarriers (1 or 2) and their position (lower or higher edge) to puncture at the downlink narrowband edges:

- If the value is '00', then the number of punctured subcarriers on the higher edge of narrowbands above the DC subcarrier is 2 and the number of punctured subcarriers on the higher edge of narrowbands below the DC subcarrier is 1.

- If the value is '01', then the number of punctured subcarriers on the higher edge of narrowbands above the DC subcarrier is 1 and the number of punctured subcarriers on the higher edge of narrowbands below the DC subcarrier is 0.

- If the value is '10', then the number of punctured subcarriers on the lower edge of narrowbands above the DC subcarrier is 0 and the number of punctured subcarriers on the lower edge of narrowbands below the DC subcarrier is 1.

- If the value is '11', then the number of punctured subcarriers on the lower edge of narrowbands above the DC subcarrier is 1 and the number of punctured subcarriers on the lower edge of narrowbands below the DC subcarrier is 2.

- In the mapping to resource elements, when a subcarrier k is punctured according to the above, the resource elements (k,l) shall be counted but not used for transmission.

- The subcarrier puncturing is applied to transmission of the following physical signals and channels when the transmission is aligned with a narrowband edge.

- MPDCCH

- PDSCH

- CSI reference signals

- No subcarrier puncturing is applied to transmissions that are not aligned with a narrowband edge.

## 6.4 Physical downlink shared channel

The physical downlink shared channel shall be processed and mapped to resource elements as described in clause 6.3 with the following additions and exceptions:

- In resource blocks in which UE-specific reference signals are not transmitted, the PDSCH shall be transmitted on the same set of antenna ports as the PBCH, which is one of ![](media_svg/image390.svg) [公式: {0}], ![](media_svg/image391.svg) [公式: {0,1}], or ![](media_svg/image392.svg) [公式: {0,1,2,3}].

- In resource blocks in which UE-specific reference signals are transmitted, the PDSCH shall be transmitted on antenna port(s) ![](media_svg/image393.svg) [公式: {5}],![](media_svg/image394.svg) [公式: {7}],![](media_svg/image395.svg) [公式: {8}], ![](media_svg/image396.svg) [公式: {11}], ![](media_svg/image397.svg) [公式: {13}], ![](media_svg/image398.svg) [公式: {11,13}], ![](media_svg/image399.svg) [公式: p⎰{7,8,...,Υ+6}], or the antenna ports listed in Table 6.3.4.4-1, where ![](media_svg/image162.svg) [公式: Υ] is the number of layers used for transmission of the PDSCH.

- If PDSCH is transmitted in MBSFN subframes as defined in TS36.213[4], the PDSCH shall be transmitted on one or several of antenna port(s) ![](media_svg/image399.svg) [公式: p⎰{7,8,...,Υ+6}] or on the antenna ports indicated in Table 6.3.4.4-1, where ![](media_svg/image162.svg) [公式: Υ] is the number of layers used for transmission of the PDSCH.

- PDSCH is not mapped to resource elements used for UE-specific reference signals associated with PDSCH

- In mapping to resource elements, the same positions of the cell-specifc reference shall be assumed for all antenna ports on which the PDSCH is transmitted and the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports and the frequency shift of the cell-specific reference signals derived as described in clause 6.10.1.2, unless indicated otherwise in clause 7.1.9 in TS 36.213 [4],

- if one set of parameters for cell-specific reference signal positions are provided by clause 7.1.9 in TS 36.213 [4], the values of these parameters are used for all antenna ports whereon the PDSCH is transmitted in the resource blocks indicated by the relevant DCI.

- if two sets of parameters for cell-specific reference signal positions are provided by clause 7.1.9 in TS 36.213 [4], the first set of parameters are used for the set of antenna ports associated with PDSCH codeword ![](media_svg/image400.svg) [公式: q=0] while the second set of parameters are used for the set of antenna ports associated with PDSCH codeword ![](media_svg/image401.svg) [公式: q=1], according to codeword-to-layer mapping and layer-to-port mapping in Clause 6.3.3.2 and Clause 6.3.4.4, respectively.

- If the DCI associated with the PDSCH uses the C-RNTI or semi-persistent C-RNTI, PDSCH modulation symbols on the indicated antenna ports are not mapped to resource elements assumed by the UE to be used for transmission of:

- zero-power CSI reference signals, where the positions of the CSI reference signals assumed for each antenna port are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

- obtained as described in clause 6.10.5.2 and used for all antenna ports whereon the PDSCH is transmitted, unless indicated otherwise in clause 7.1.9 in TS 36.213 [4]

- if one set of parameters for zero power CSI reference signal configuration is provided by clause 7.1.9 in TS 36.213 [4], the values of these parameters are used for all antenna ports on which the PDSCH is transmitted in the resource blocks indicated by the corresponding DCI scheduling the PDSCH, and

- if two sets of parameters for zero power CSI reference signal configuration are provided by clause 7.1.9 in TS 36.213 [4], the first set of parameters are used for the set of antenna ports associated with PDSCH codeword ![](media_svg/image400.svg) [公式: q=0] while the second set of parameters are used for the set of antenna ports associated with PDSCH codeword  ![](media_svg/image401.svg) [公式: q=1], according to codeword-to-layer mapping and layer-to-port mapping in Clause 6.3.3.2 and Clause 6.3.4.4, respectively.

- obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

- non-zero-power CSI reference signals for CSI reporting, except for non-zero power CSI reference signals configured by csi-RS-ConfigNZP-ApList, where the positions of the non-zero-power CSI reference signals for CSI reporting are given by clause 6.10.5.2. The configuration for non-zero power CSI reference signals is obtained as described in clause 6.10.5.2.

- PDSCH is not mapped to any physical resource-block pair(s) carrying an EPDCCH associated with the PDSCH.

- PDSCH with subframe duration on antenna port 7, 8, 9, 10, 11, 12, 13 or 14 is not mapped to any physical resource-block pair(s) carrying PBCH or synchronization signals.

- Frame structure type 1, PDSCH on antenna port 5 is not mapped to any physical resource-block pair(s) carrying PBCH or synchronization signals.

- Frame structure type 2, PDSCH on antenna port 5 is not mapped to any physical resource-block pair(s) carrying PBCH.

- For frame structure type 1 and 2, the index ![](media_svg/image402.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image403.svg) [公式≈: ^{l}^{÷}^{l}DataStart] where ![](media_svg/image404.svg) [公式≈: ^{l}DataStart] is given by clause 7.1.6.4 of TS 36.213 [4].

- For frame structure type 3,

- if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe

- the index ![](media_svg/image402.svg) [公式: l] in the second slot in a subframe fulfils ![](media_svg/image403.svg) [公式≈: ^{l}^{÷}^{l}DataStart] where ![](media_svg/image404.svg) [公式≈: ^{l}DataStart] is given by clause 7.1.6.4 of TS36.213 [4],

- otherwise

- the index ![](media_svg/image402.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image403.svg) [公式≈: ^{l}^{÷}^{l}DataStart] where ![](media_svg/image404.svg) [公式≈: ^{l}DataStart] is given by clause 7.1.6.4  of TS36.213 [4],

- In mapping to resource elements, if the DCI associated with the PDSCH uses the C-RNTI or semi-persistent C-RNTI, and transmit diversity according to clause 6.3.4.3 is used, and if the higher-layer parameter semiOpenLoop is not set and if the DCI associated with the PDSCH is not of format 7, resource elements in an OFDM symbol assumed by the UE to contain CSI-RS shall be used in the mapping if and only if all of the following criteria are fulfilled:

- there is an even number of resource elements for the OFDM symbol in each resource block assigned for transmission, and

- the complex-valued symbols ![](media_svg/image405.svg) [公式: y^{(}^{p}^{)}(i)] and ![](media_svg/image406.svg) [公式: y^{(}^{p}^{)}(i+1)], where ![](media_svg/image407.svg) [公式: i] is an even number, can be mapped to resource elements ![](media_svg/image408.svg) [公式: (k,l)] and ![](media_svg/image409.svg) [公式: (k+n,l)] in the same OFDM symbol with ![](media_svg/image410.svg) [公式: n<3].

- In mapping to resource elements, if the DCI associated with the PDSCH uses C-RNTI or semi-persistent C-RNTI and if the higher-layer parameter semiOpenLoop is set for subframe PDSCH or the higher-layer parameter semiOpenLoop-STTI is set for slot/subslot PDSCH or if the DCI associated with the PDSCH is of format 7 and transmit diversity according to clause 6.3.4.3 is used, a pair of resource elements ![](media_svg/image411.svg) [公式: (k&apos;,l)], ![](media_svg/image412.svg) [公式: (k&apos;+n,l)] shall be used in the mapping if and only if

- the complex-valued symbols ![](media_svg/image405.svg) [公式: y^{(}^{p}^{)}(i)] and ![](media_svg/image413.svg) [公式: y^{(}^{p}^{)}(i+1)] can be mapped to resource elements ![](media_svg/image414.svg) [公式: (k&apos;,l)] and ![](media_svg/image412.svg) [公式: (k&apos;+n,l)] in the same OFDM symbol and the same PRB with ![](media_svg/image410.svg) [公式: n<3], where ![](media_svg/image407.svg) [公式: i] is an even number and ![](media_svg/image415.svg) [公式: k^{±}] starts from 0 at the lowest subcarrier of the PRB.

### 6.4.1 Physical downlink shared channel for BL/CE UEs

For BL/CE UEs, the following additions and exceptions hold in addition to those in clause 6.4:

- The maximum number of allocatable PRBs for PDSCH is restricted as follows:

- If the PDSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pdsch-maxBandwidth-config is set,

- if the higher layer parameter ce-pdsch-maxBandwidth-config is set to 20 MHz, the maximum number of allocatable PRBs for PDSCH is 96 PRBs restricted to the narrowbands defined in clause 6.2.7;

- if the higher layer parameter ce-pdsch-maxBandwidth-config is set to 5 MHz, the maximum number of allocatable PRBs for PDSCH is 24 PRBs restricted to no more than four of the narrowbands defined in clause 6.2.7.

- If the PDSCH is associated with G-RNTI and the higher layer parameter pdsch-MaxBandwidth-SC-MTCH is set to 24 PRBs, the maximum number of allocatable PRBs for PDSCH is 24 PRBs restricted to no more than four of the narrowbands defined in clause 6.2.7.

- For all other cases, the maximum number of allocatable PRBs for PDSCH is 6 PRBs restricted to one of the narrowbands defined in clause 6.2.7.

- Resource elements occupied by CSI reference signals shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

- Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

- PRB pairs occupied by RSS shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

- For BL/CE UEs in CEModeB configured in transmission mode 9, in MBSFN subframe(s), resource elements that correspond to the positions of cell-specific reference signals as in subframe #0 shall not be counted in the PDSCH mapping and not used for transmission of the PDSCH.

- Resource elements belonging to PRBs in which PRS is transmitted (including PRS muted subframes) shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

- If the higher layer parameter ce-punctured-subcarriers-DL is configured, and the DCI associated with the PDSCH uses C-RNTI or SPS C-RNTI, and transmit diversity according to clause 6.3.4.3 is used,

- In the mapping to resource elements, when the complex-valued symbols  and , where  is an even number, are mapped to resource elements  and  in the same OFDM symbol with , then if ce-punctured-subcarriers-DL indicates that any of  and  shall be counted but not used for transmission, the UE shall assume that both  and  are counted but not used for transmission.

- If PDSCH transmission in the LTE control region is configured by higher layer parameter transmissionInControlChRegion, after the initial mapping of the PDSCH to resource elements $(k,l)$ starting from $ l=l_{DataStart}$ in the first slot to the last OFDM symbol available for downlink transmission in the subframe has been performed, the mapping shall continue with resource elements $\left ( k,l\right ) $ not reserved for cell-specific reference signals in increasing order of first the index $ k $ over the assigned physical resource blocks and then the index $ l $ starting from $ l=0 $ in the first slot to $ l=l_{DataStart}-1 $ in the first slot, where $ l_{DataStart}$  is given by clause 7.1.6.4 of TS 36.213 [4].

For BL/CE UEs, if the PDSCH is not carrying SIB1-BR the PRB resources for PDSCH transmission in the first subframe are obtained from the DCI as described in clauses 5.3.3.1.12, 5.3.3.1.13, and 5.5.1.3.14 in [3], or provided by higher layers. Each of the $ N_{TB}\geq  1 $ PDSCH codewords is transmitted with ![](media_svg/image422.svg) [公式≈: _{N}_{rep}PDSCH_{÷}_{1}] repetitions, where $ N_{TB}$ is the number of transport blocks defined in clause 7.1.11 of TS 36.213 [4]. The PDSCH transmission spans $ N_{abs}^{PDSCH}\geq  N_{TB}N_{rep}^{PDSCH}$ consecutive subframes, including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed.

- If downlink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PDSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PDSCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 7.1 in [4], the PDSCH transmission is postponed until the next BL/CE downlink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved resource elements shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

- If frequency hopping is not enabled for PDSCH, all PDSCH repetitions are located at the same PRB resources, and

- if frequency hopping is enabled for PDSCH, the PDSCH shall be transmitted in subframe ![](media_svg/image423.svg) [公式: i] within the ![](media_svg/image424.svg) [公式≈: _{N}_{abs}PDSCH] consecutive downlink subframes using the PRB resources of the narrowband ![](media_svg/image425.svg) [公式≈: _{n}_{NB}()i] with the same RIV as that of narrowband $ n_{NB}^{(i_{0})}$![](media_svg/image426.svg) [公式≈: _{n}_{NB}()i_{0}]. The narrowband ![](media_svg/image425.svg) [公式≈: _{n}_{NB}()i]$ n_{NB}^{(i)}$ is defined as

![](media_svg/image427.svg) [公式≈: _{i}_{i}n_{j}_{0}_{δ}_{0}NB^{(}^{i}_{≥}^{)}_{=}_{=}_{i}=_{√}_{⌠}_{∞}_{√}_{≥}_{(}_{0,}_{N}_{i}^{⊇}^{⊕}⊕_{⊗}_{0}_{i}n_{NB}_{ch,}_{0}_{+}NB^{(}^{i}_{+}^{0}_{DL}_{i}_{δ}^{)}_{N}+_{)}_{−}_{abs}_{PDSCH}^{⊇}^{⊕}⊕_{⊗}_{N}_{2}^{⋅}⋅_{⋅}_{√}_{,}_{NB}_{N}_{ch,}^{i}_{NB}^{+}ch,_{DL}_{for }_{for }_{−}^{i}DL^{δ}_{∃}_{1}_{frame}_{frame}−j0^{∂}∂_{∂}_{∃}_{structure}_{structure}mod N_{ type}_{ type}NB,^{ch,}^{DL}hop_{1}_{2}^{⇒}^{⇐}⇐_{⇔}∪fNB,^{DL}hop^{⇒}^{⇐}⇐_{⇔}modNNB^{DL}]

where ![](media_svg/image428.svg) [公式≈: ^{i}0] is the absolute subframe number of the first downlink subframe intended for PDSCH and ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL], ![](media_svg/image430.svg) [公式≈: ^{N}NB,^{ch,}^{DL}hop] and ![](media_svg/image431.svg) [公式≈: ^{f}NB,^{DL}hop] are cell-specific higher-layer parameters. For PDSCH carrying SI other than SIB1-BR and for PDSCH associated with P-RNTI, if interval-DlHoppingConfigCommonModeB is signalled in SIB1-BR, then the frequency hopping granularity ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] is set to interval-DlHoppingConfigCommonModeB; otherwise, ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] is set to interval-DlHoppingConfigCommonModeA signalled in SIB1-BR.

For BL/CE UE in CEModeA, frequency hopping of PDSCH associated with C-RNTI or SPS C-RNTI is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set and the frequency hopping flag in DCI format 6-1A indicates frequency hopping, otherwise, frequency hopping of is not enabled. For BL/CE UE in CEModeB, frequency hopping of PDSCH associated with C-RNTI or SPS C-RNTI is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set, otherwise, frequency hopping of is not enabled.

The UE shall not expect PDSCH in subframe ![](media_svg/image432.svg) [公式: i] if it is not a BL/CE DL subframe.

For BL/CE UEs, if the PDSCH carries SIB1-BR, the PDSCH transmission is repeated periodically in every period of 8 radio frames, where a period starts with a radio frame with ![](media_svg/image433.svg) [公式: n_{f}mod8=0] where ![](media_svg/image434.svg) [公式≈: ^{n}f] is the system frame number. The PDSCH is transmitted ![](media_svg/image435.svg) [公式≈: _{N}_{PDSCH}SIB1-BR] times in each period of 8 frames, Let ![](media_svg/image436.svg) [公式: {s_{j}}] be the set of narrowbands, excluding narrowbands overlapping with the 72 center subcarriers for ![](media_svg/image437.svg) [公式: N_{RB}^{DL}>15], and ordered in increasing order of narrowband index. The PDSCH transmission cycles through the set ![](media_svg/image438.svg) [公式: {s_{i}}] of narrowbands in increasing order of ![](media_svg/image439.svg) [公式: i], starting with ![](media_svg/image440.svg) [公式: i=0] for the first subframe, according to

![](media_svg/image441.svg) [公式≈: ^{n}^{NB}_{m}j_{i}^{=}=_{=}_{=}_{0}(_{√}_{⌡}_{⌠}_{⌡}_{∞}^{s}N_{1}_{,}_{2}_{4}^{j}_{1}ID_{,...,}^{cell}_{12}_{50}_{N}mod_{m}_{RB}_{DL}_{≥}_{<}_{−}_{N}_{1}_{N}_{<}N_{RB}_{RB}_{DL}_{12}_{DL}NB^{S}_{≥}+_{50}i∪√NNB^{S}m∃)modNNB^{S}]

where ![](media_svg/image442.svg) [公式≈: ^{N}NB^{S}] is the number of narrowbands in the set ![](media_svg/image436.svg) [公式: {s_{j}}].

The set of frames and subframes used for SIB1-BR transmission in each period are given by Tables 6.4.1-1 and 6.4.1-2.

Table 6.4.1-1: The set of frames and subframes for SIB1-BR for ![](media_svg/image443.svg) [公式: N_{RB}^{DL}≥15].

| ![](media_svg/image435.svg) [公式≈: _{N}_{PDSCH}SIB1-BR] | ![](media_svg/image444.svg) [公式≈: N_{ID}^{cell}mod2] | Frame structure type 1 |  | Frame structure type 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | ![](media_svg/image445.svg) [公式: n_{f}mod2] | ![](media_svg/image446.svg) [公式≈: ^{n}sf] | ![](media_svg/image445.svg) [公式: n_{f}mod2] | ![](media_svg/image446.svg) [公式≈: ^{n}sf] |
| 4 | 0 | 0 | 4 | 1 | 5 |
|  | 1 | 1 | 4 | 1 | 5 |

Table 6.4.1-2: The set of frames and subframes for SIB1-BR for ![](media_svg/image447.svg) [公式: N_{RB}^{DL}>15].

| ![](media_svg/image435.svg) [公式≈: _{N}_{PDSCH}SIB1-BR] | ![](media_svg/image444.svg) [公式≈: N_{ID}^{cell}mod2] | Frame structure type 1 |  | Frame structure type 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | ![](media_svg/image448.svg) [公式: n_{f}mod2] | ![](media_svg/image446.svg) [公式≈: ^{n}sf] | ![](media_svg/image445.svg) [公式: n_{f}mod2] | ![](media_svg/image446.svg) [公式≈: ^{n}sf] |
| 4 | 0 | 0 | 4 | 1 | 5 |
|  | 1 | 1 | 4 | 1 | 0 |
| 8 | 0 | 0, 1 | 4 | 0, 1 | 5 |
|  | 1 | 0, 1 | 9 | 0, 1 | 0 |
| 16 | 0 | 0, 1 | 4, 9 | 0, 1 | 0, 5 |
|  | 1 | 0, 1 | 0, 9 | 0, 1 | 0, 5 |

BL/CE UEs may assume the same precoding matrix being used for a PRB across a block of ![](media_svg/image449.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes when UE-specific reference signals are transmitted together with the PDSCH, where the subframe number of the first subframe in each block of ![](media_svg/image18.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image450.svg) [公式≈: (^{niN}abs,1NB^{+=}δ)^{mod0}^{ch,DL}].

For PDSCH transmission associated with SI-RNTI or P-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter si-HoppingConfigCommon is set.

For PDSCH transmission associated with PUR-RNTI to BL/CE UEs using UE-specific MPDCCH search space, frequency hopping of the PDSCH is enabled when higher layer parameter pur-PDSCH-FreqHopping is set.

For PDSCH transmission associated with RA-RNTI or temporary C-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

- if PRACH CE level 0 or 1 is used for the last PRACH attempt, ![](media_svg/image451.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

- if PRACH CE level 2 or 3 is used for the last PRACH attempt, ![](media_svg/image451.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

For PDSCH transmission associated with SC-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MCCH is set. Further

- if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeA, ![](media_svg/image449.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

- if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeB, ![](media_svg/image449.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

For PDSCH transmission associated with G-RNTI to BL/CE UEs,

- if the higher layer parameter mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeA,

- if the higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set and the frequency hopping flag in DCI format 6-1A indicates frequency hopping, then frequency hopping of the PDSCH is enabled and ![](media_svg/image452.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA, otherwise frequency hopping is not enabled;

- if the higher layer parameter mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeB,

- if the higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set, then frequency hopping of the PDSCH is enabled and ![](media_svg/image453.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB, otherwise frequency hopping is not enabled.

### 6.4.2 Slot/subslot-based physical downlink shared channel

For slot or subslot-based PDSCH, in this specification referred to as slot-PDSCH and subslot-PDSCH respectively, the following additions and exceptions hold in addition to those in clause 6.4:

- PDSCH is not mapped to resource elements of SCCEs used by the associated SPDCCH, or resource elements used for UE-specific reference signals associated with SPDCCH

- In case of slot-PDSCH:

- the mapping to resource elements ![](media_svg/image454.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] not reserved for other purposes shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] over the assigned physical resource blocks and then the index![](media_svg/image389.svg) [公式: l], for the slot of the assigned physical resources in the subframe, and

- in case of UE-specific reference signals, the PDSCH is not mapped to any physical resource blocks carrying PBCH.

- In case of subslot-PDSCH:

- the mapping to resource elements ![](media_svg/image454.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] not reserved for other purposes shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] over the assigned physical resource blocks and then the index![](media_svg/image389.svg) [公式: l], starting from ![](media_svg/image455.svg) [公式≈: ^{l}0]given in Table 6.4.2-1. The starting value ![](media_svg/image456.svg) [公式≈: ^{l}0]and the value range of ![](media_svg/image389.svg) [公式: l] depends on the number of symbols used for PDCCH and the subslot number in the subframe, according to Table 6.4.2-1, and

- in case of UE-specific reference signals,

- the PDSCH is not mapped to any physical resource blocks in frequency domain carrying PBCH or synchronization signals for the OFDM symbols of the given subslot.

- and in case the DCI associated with the subslot-PDSCH indicates the absence of the UE-specific reference signals (see DMRS position indicator field in TS 36.212 [3]), the PDSCH is not mapped to any physical resource blocks in frequency domain that carried PBCH or synchronization signals for the OFDM symbols of the previous subslot.

Table 6.4.2-1: Starting value of index ![](media_svg/image457.svg) [公式: l], i.e. ![](media_svg/image458.svg) [公式≈: ^{l}0], for subslot PDSCH

| Number of symbols used for PDCCH | Downlink subslot index |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | #0 | #1 | #2 | #3 | #4 | #5 |
| 1 | 1 | 3 | 5 | 0 | 2 | 4 |
| 2 | - | 2 | 5 | 0 | 2 | 4 |
| 3 | - | 3 | 5 | 0 | 2 | 4 |

- For PDSCH associated with UE-specific reference signals,

- the PDSCH shall only be mapped to physical resource blocks in frequency domain assigned for PDSCH transmission where the assignment maps to both physical resource blocks of a PRG.

- the subslot-PDSCH shall not be mapped to the physical resource blocks of a PRG in case the resource elements of the associated SPDCCH are mapped to those physical resource blocks.

- In addition, the following additions and exceptions related to L1 signaling and/or higher layer configuration controlling rate-matching around SPDCCH resources hold:

- PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm2' if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set.

- PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm3' if the SPDCCH associated with PDSCH is found in this SPDCCH resource set and if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set. If the SPDCCH associated with PDSCH is found on a candidate belonging to two SPDCCH resource sets, the SPDCCH is assumed to be found in both SPDCCH resource sets.

- PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm4' if the SPDCCH associated with PDSCH is not found in this SPDCCH resource set and if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set.

- PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n0' if the bit of the Used/Unused SPDCCH resource indication field corresponding to this SPDCCH resource set in the DCI format 7 associated with PDSCH is set to 1.

- PDSCH is not mapped to resource elements belonging to SCCE#0 to SCCE#![](media_svg/image459.svg) [公式≈: ^{⊇}_{⊕}_{⊕}_{⊗}^{⋅}_{⋅}_{√}^{N}SCCE_{2},m^{∂}_{∂}_{∃}_{−}_{1}^{⇒}_{⇐}_{⇐}_{⇔}]of a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '2' for the SPDCCH resource set if the most significant bit of the Used/Unused SPDCCH resource indication field in the DCI format 7 associated with PDSCH is set to 1.

- PDSCH is not mapped to resource elements belonging to SCCE#![](media_svg/image460.svg) [公式≈: ^{⋅}_{⋅}_{√}^{N}SCCE_{2},m^{∂}_{∂}_{∃}] to SCCE#![](media_svg/image461.svg) [公式≈: ^{(}^{N}SCCE,m^{−}^{1}^{)}] of a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '2' for the SPDCCH resource set if the least significant bit of the Used/Unused SPDCCH resource indication field in the DCI format 7 associated with PDSCH is set to 1.

- It should be noted that not mapping PDSCH to resource elements belonging to a SPDCCH resource set holds irrespective of other indications (spdcch-L1-ReuseIndication or rateMatchingMode) associated with other SPDCCH resource sets (if configured).

- For a UE with the higher-layer parameter blindSlotSubslotPDSCH-Repetitions set to TRUE and PDSCH associated with a downlink assignment sent on PDCCH/SPDCCH with DCI format 7 indicating $ k $ transmissions, the rate-matching around SPDCCH resources if applicable for PDSCH in the $ k-1 $ valid slots/subslots following the slot/subslot containing the downlink assignment follows

- the rate-matching around SPDCCH resources of the PDSCH in the slot/subslot containing the downlink assignment, if the DCI format 7 indicating $ k $ transmissions is received on SPDCCH.

- the rate-matching around SPDCCH resources of the PDSCH in the SPDCCH resource set according to rateMatchingMode indicating 'm2', if configured by higher layers, if the DCI format 7 indicating ![](media/cid:image001.png@01D472A0.1687F650) transmissions is received on PDCCH. For other configurations of rateMatchingMode, no rate-matching around SPDCCH resources for PDSCH in the $ k-1 $ valid slots/subslots following the PDCCH with DCI format 7 indicating $ k $ PDSCH transmissions is applied..

## 6.5 Physical multicast channel

The physical multicast channel shall be processed and mapped to resource elements as described in clause 6.3 with the following exceptions:

- No transmit diversity scheme is specified.

- Layer mapping and precoding shall be done assuming a single antenna port and the transmission shall use antenna port 4.

- The PMCH can only be transmitted in the MBSFN region. For PMCH with Δf  = 15 kHz, the index ![](media_svg/image402.svg) [公式: l] in the first slot in the MBSFN subframe fulfils $ l\geq  l_{PMCHStart}$ where $ l_{PMCHStart}$ is equal to the value given by the higher layer parameter non-MBSFNregionLength [9].

- The PMCH shall use extended cyclic prefix.

- The PMCH is not mapped to resource elements used for transmission of MBSFN reference signals.

- In clause 6.3.1, for Δf = 1.25 kHz and Δf ≈ 0.37 kHz, the scrambling generator shall be initialised at the start of each slot.

- For $\Delta  f=\frac {1}{\left ( 82944T_{s}\right ) }\approx  0.37kHz $ the following exception applies to clause 6.3.5:

- The text "which meet all of the following criteria in the current subframe" shall be replaced by "which meet all of the following criteria in the current slot"

- The mapping to resource elements $\left ( k,l\right ) $ on antenna port $ p $ not reserved for other purposes shall be in increasing order of first the index $ k $ over the assigned physical resource blocks and then the index $ l $.

- For PMCH symbols belonging to an MBSFN area with $ N_{RB}^{PMCH}$ configured, $ N_{RB}^{DL}$ shall be replaced by $ N_{RB}^{PMCH}$ in clauses 6.3, 6.10.2, and 6.12.

- If cyclic shifting is configured by the higher-layer parameter pmch-CyclicShiftAlpha,

-  cyclic shifting according to clause 6.5.1 shall be applied

- modulation in clause 6.3.2 shall use $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $ instead of $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $

- If frequency-domain interleaving is configured by the higher-layer parameter pmch-FreqInterleaving,

- block interleaving according to clause 6.5.2 shall be applied

- mapping to resource elements in clause 6.3.5 shall use $\hat {y}^{\left ( p\right ) }\left ( 0\right ) , \ldots  ,\hat {y}^{\left ( p\right ) }(M_{symb}^{ap}-1)$ instead of $ y^{\left ( p\right ) }\left ( 0\right ) , \ldots  ,y^{\left ( p\right ) }(M_{symb}^{ap}-1)$

### 6.5.1 Cyclic shift for PMCH

The input to the cyclic shift is the block of bits $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $ defined in clause 6.3.1 and the ouput is a block of bits $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $.

The block of bits $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $ shall be cyclically shifted by $ X_{i}$ bits to form the block $\hat {b}\left ( 0\right ) , \ldots  ,\hat {b}\left ( M_{bit}-1\right ) $ according to

$$\hat {b}\left ( n\right ) =\hat {b}(\left ( n-X_{i}\right ) modM_{bit})$$

where

- $ X_{i}$ is given by

- if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha1 or alpha2

$$ X_{i}=\sum  _{r=C-S_{i}}^{C-1}E_{r}$$

$$ S_{i}=i\alpha  modC $$

- if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha3

$$ X_{i}=A_{i}\left ( n_{f},n_{sf}\right ) \lfloor  \frac {N_{sc}Q_{m}}{N}\rfloor  $$

$$ A_{i}\left ( n_{f},n_{sf}\right ) =\left ( \sum  _{m=0}^{7}c\left ( 8\left ( 10\left ( n_{f}mod128\right ) +n_{sf}\right ) +m\right ) 2^{m}\right ) modN $$

where the pseudo-random sequence $ c(i)$ is defined by clause 7.2 and shall be initialized with $ c_{init}=N_{ID}^{MBSFN}$ at the beginning of each radio frame for which $ n_{f}mod 128=0 $, the number of subcarriers available in one OFDM symbol for PMCH is given by $ N_{sc}=\frac {M_{bit}}{\left ( Q_{m}L\right ) }$, and $ Q_{m}$ is the modulation order.

- $ i\in  \left \{ 0, 1, \ldots  ,N-1\right \} $ denotes the $ i^{th}$ subframe to which the transport block is mapped

- $ N $ is the number of subframes to which the transport block is mapped

- $ E_{r}$ is the number of bits in the $ r^{th}$ codeblock within a subframe as defined in TS 36.212 [3]

- $ C $ is the number of codeblocks in the transport block

- $\alpha  $ is given by

- if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha1

$$\alpha  =1 $$

- if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha2

$$\alpha  =\lceil  \frac {C}{NL}\rceil  $$

- $ L $ is the number of OFDM symbols used for the PMCH transmission.

### 6.5.2 Frequency-domain interleaving

The input to the interleaver is the block of complex-valued symbols $ y^{\left ( p\right ) }\left ( 0\right ) , \ldots  ,y^{\left ( p\right ) }(M_{symb}^{ap}-1)$  defined in clause 6.3.4.1 and the output from the interleaver is a block of complex-valued symbols $\hat {y}^{\left ( p\right ) }\left ( 0\right ) , \ldots  ,\hat {y}^{\left ( p\right ) }(M_{symb}^{ap}-1)$.

Interleaving shall be performed as follows:

- Divide the block of complex-valued symbols $ y^{\left ( p\right ) }\left ( 0\right ) , \ldots  ,y^{\left ( p\right ) }(M_{symb}^{ap}-1)$ into $ L $ sets such that set $ l\in  \left \{ 0,1,\ldots  ,L-1\right \} $ contains the complex-valued symbols to be mapped to OFDM symbol $ l $

- For each of the sets $ l=0, 1, \ldots  , L-1 $

- Set the number of columns $ K $ of the block interleaver to

$$ K=\frac {C}{gcd(L,C)}$$

where

- $ L $ is the number of OFDM symbols used for the PMCH transmission

- $ C $ is the number of codeblocks as defined in clause 5.1.2 of [36.212]

- $ gcd(u,v)$ denotes the greatest common divisor of $ u $ and $ v $

- Set the number of rows of the block interleaver $ R $ to the smallest integer fulfilling

$$ M_{l}\leq  RK $$

where

- $ M_{l}$ is the number of resources elements available for mapping of complex-valued modulation symbols in OFDM symbol $ l $

- Write the modulation symbols $ y^{\left ( p\right ) }\left ( i\right ) $ in set $ l $ column-wise into the block interleaver in increasing order of $ i $, starting with column 0 and row 0 and in increasing order of first the row number and then the column number. If $ M_{l}<RK $, append <NULL> elements to fill the size-$ RK $ block interleaver.

- If $\sqrt {RK}-K+1>0 $, permute the rows such that row $ r_{i}$ is moved to row $ i $ where

$$ r_{i}={\begin {matrix}r_{i-1}+d & r_{i-1}\leq  R-d-1 \\ \lfloor  \frac {id}{R}\rfloor   & otherwise\end {matrix}d=\lfloor  \frac {R}{\lfloor  \frac {R}{\lceil  \sqrt {RK}-K+1\rceil  }\rfloor  }\rfloor  r_{0}=01\leq  i\leq  R-1 $$

- Cyclically shift the columns of row $ r $ with an offset $ s_{r}$ given by

$$ s_{r}=\left ( (-1)^{r}\lfloor  \frac {r+1}{2}\rfloor  \right ) modKr=0,1,\ldots  ,R-1 $$

- Read the interleaved modulation symbols  $\hat {y}^{\left ( p\right ) }\left ( i\right ) $ in set $ l $ row-wise from the block interlaver in increasing order of $ i $, starting with column 0 and row 0 and in increasing order of first the column number and then the row number, discarding any <NULL> elements.

## 6.6 Physical broadcast channel

The PBCH is not transmitted for frame structure type 3.

### 6.6.1 Scrambling

The block of bits![](media_svg/image463.svg) [公式: b(0),...,b(M_{bit}−1)], where ![](media_svg/image464.svg) [公式≈: ^{M}bit], the number of bits transmitted on the physical broadcast channel, equals 1920 for normal cyclic prefix and 1728 for extended cyclic prefix, shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bits ![](media_svg/image465.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image466.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image467.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence shall be initialised with ![](media_svg/image468.svg) [公式≈: ^{c}init^{=}^{N}ID^{cell}] in each radio frame fulfilling ![](media_svg/image469.svg) [公式: n_{f}mod4=0]. For an MBMS-dedicated cell, the scrambling sequence shall be initialised with ![](media_svg/image470.svg) [公式≈: ^{c}init^{=}^{2}^{9}^{+}^{N}ID^{cell}] in each radio frame fulfilling ![](media_svg/image471.svg) [公式: n_{f}mod16=0].

### 6.6.2 Modulation

The block of scrambled bits ![](media_svg/image472.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)]. Table 6.6.2-1 specifies the modulation mappings applicable for the physical broadcast channel.

Table 6.6.2-1: PBCH modulation schemes.

| Physical channel | Modulation schemes |
| --- | --- |
| PBCH | QPSK |

### 6.6.3 Layer mapping and precoding

The block of modulation symbols ![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)] shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with ![](media_svg/image474.svg) [公式≈: ^{M}symb^{(}^{0}^{)}^{=}^{M}symb] and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors ![](media_svg/image475.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)...y^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image476.svg) [公式≈: i=0,...,M_{symb}−1], where ![](media_svg/image212.svg) [公式: y^{(}^{p}^{)}(i)] represents the signal for antenna port ![](media_svg/image34.svg) [公式: p] and where ![](media_svg/image477.svg) [公式: p=0,...,P−1] and the number of antenna ports for cell-specific reference signals ![](media_svg/image478.svg) [公式: P⎰{1,2,4}].

### 6.6.4 Mapping to resource elements

The block of complex-valued symbols![](media_svg/image479.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}−1)] for each antenna port shall

- for an MBMS-dedicated cell, be transmitted during 4 consecutive radio frames fulfilling ![](media_svg/image480.svg) [公式: n_{f}mod4=0], starting in each radio frame fulfilling ![](media_svg/image481.svg) [公式: n_{f}mod16=0], and

- otherwise, be transmitted during 4 consecutive radio frames, starting in each radio frame fulfilling ![](media_svg/image480.svg) [公式: n_{f}mod4=0].

The block of complex-valued symbols shall be mapped in sequence starting with ![](media_svg/image482.svg) [公式: y(0)] to resource elements ![](media_svg/image483.svg) [公式: (k,l)] constituting the core set of PBCH resource elements. The mapping to resource elements ![](media_svg/image484.svg) [公式: (k,l)] not reserved for transmission of reference signals shall be in increasing order of first the index![](media_svg/image388.svg) [公式: k], then the index ![](media_svg/image389.svg) [公式: l] in slot 1 in subframe 0 and finally the radio frame number. The resource-element indices are given by

![](media_svg/image485.svg) [公式≈: ^{P}^{ˆ}PRACH_CG2^{(}^{i}^{2}^{)}]

where resource elements reserved for reference signals shall be excluded. The mapping operation shall assume cell-specific reference signals for antenna ports 0-3 being present irrespective of the actual configuration. The UE shall assume that the resource elements assumed to be reserved for reference signals in the mapping operation above but not used for transmission of reference signal are not available for PDSCH or MPDCCH transmission. The UE shall not make any other assumptions about these resource elements.

For an MBMS-dedicated cell configured with repetition, the physical broadcast channel shall be repeated as described in clause 6.6.4.1.

For an MBMS-dedicated cell configured with CAS muting, the physical broadcast channel shall only be transmitted in the first $ 4K_{CAS}$ frames, starting in frames fulfilling $ n_{f}mod16N_{CAS}=0 $ where $ N_{CAS}\in  \left \{ 2, 4, 8, 16\right \} $ and $ K_{CAS}\in  \left \{ 4, 5, 6, \ldots  , 63\right \} $ are given by the higher-layer parameter cas-MutingConfig.

If a cell is configured with repetition of the physical broadcast channel

- symbols mapped to core resource element ![](media_svg/image486.svg) [公式≈: ^{P}^{ˆ}PRACH_CG2^{(}^{i}^{2}^{)}^{=}^{0}] in slot 1 in subframe 0 within a radio frame ![](media_svg/image487.svg) [公式≈: ^{Pi}^{ˆ}PRACH_CG2^{(21)}^{− }] according to the mapping operation above, and

- cell-specific reference signals in OFDM symbols ![](media_svg/image488.svg) [公式≈: Pi^{ˆ}_{PRACH_CG2}(21)0− = ] in slot 1 in subframe 0 within a radio frame ![](media_svg/image487.svg) [公式≈: ^{Pi}^{ˆ}PRACH_CG2^{(21)}^{− }] with ![](media_svg/image488.svg) [公式≈: Pi^{ˆ}_{PRACH_CG2}(21)0− = ] according to the mapping operation above

shall additionally be mapped to resource elements ![](media_svg/image489.svg) [公式≈: P^{~}^{ˆ}_{SRS}_{,}_{c}(i1)] in slot number ![](media_svg/image490.svg) [公式≈: P^{~}^{ˆ}_{SRS}_{,}_{c}(i1)=0] within radio frame ![](media_svg/image491.svg) [公式≈: P^{~}^{ˆ}_{SRS}_{,}_{c}(i1)=P^{ˆ}_{SRS}_{,}_{c}(i1)] unless resource element ![](media_svg/image489.svg) [公式≈: P^{~}^{ˆ}_{SRS}_{,}_{c}(i1)] is used by CSI reference signals.

For frame structure type 1, ![](media_svg/image492.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈], ![](media_svg/image493.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUSCH,c^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈], and ![](media_svg/image494.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUSCH,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈] are given by Table 6.6.4-1.

For frame structure type 2,

- if ![](media_svg/image495.svg) [公式≈: P^{ˆ}_{SRS}_{,}_{c}(i1)], ![](media_svg/image492.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈] and ![](media_svg/image493.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUSCH,c^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈] are given by Table 6.6.4-2 and ![](media_svg/image496.svg) [公式≈: P_{SRS}_{,}_{c}(i1)];

- if ![](media_svg/image497.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}], ![](media_svg/image492.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈] and ![](media_svg/image493.svg) [公式≈: ^{P}^{~}^{ˆ}^{SRS}^{,}^{c}^{(}^{i}^{1}^{)}^{=}^{max}^{√}^{⌡}^{⌠}^{⌡}∞^{0}^{P}^{ˆ}^{,}SRS,c^{(}^{i}^{1}^{)}^{−}^{P}^{ˆ}PUSCH,c^{(}^{i}^{1}^{)}^{∅}^{⌡}^{∇}^{⌡}∈] are given by Table 6.6.4-2 and ![](media_svg/image496.svg) [公式≈: P_{SRS}_{,}_{c}(i1)], except that repetitions with ![](media_svg/image498.svg) [公式≈: P^{ˆ}_{CG}^{1}_{1}(i)] and ![](media_svg/image499.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}] are not applied.

For both frame structure type 1 and frame structure type 2, repetition of the physical broadcast channel is not applicable if ![](media_svg/image500.svg) [公式≈: Α1(i)∪P^{ˆ}_{PUCCH}_{_}_{CG}_{1}(i)≥P^{ˆ}_{CG}^{1}_{1}(i)].

Resource elements already reserved or used for transmission of cell-specific reference signals in absence of repetition shall not be used for additional mapping of cell-specific reference signals.

Table 6.6.4-1: Frame offset, slot and symbol number triplets for repetition of PBCH for frame structure type 1.

| ![](media_svg/image389.svg) [公式: l] | Frame offset, slot and symbol number triplets ![](media_svg/image501.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}] |  |
| --- | --- | --- |
|  | Normal cyclic prefix | Extended cyclic prefix |
| 0 | (1,18,3), (1,19,0), (1,19,4), (0,0,4) | (1,18,3), (1,19,0), (1,19,5) |
| 1 | (1,18,4), (1,19,1). (1,19,5), (0,1,4) | (1,18,4), (1,19,1). (0,0,3) |
| 2 | (1,18,5), (1,19,2), (1,19,6), (0,1,5) | (1,18,5), (1,19,2), (0,1,4) |
| 3 | (1,18,6), (1,19,3), (0,0,3), (0,1,6) | (1,19,3), (1,19,4), (0,1,5) |

Table 6.6.4-2: Slot and symbol number pairs for repetition of PBCH for frame structure type 2.

| ![](media_svg/image389.svg) [公式: l] | Slot and symbol number pairs ![](media_svg/image502.svg) [公式≈: ^{P}PUCCH^{(}^{i}^{)}] |  |
| --- | --- | --- |
|  | Normal cyclic prefix | Extended cyclic prefix |
| 0 | (0,3), (1,4), (10,3), (11,0), (11,4) | (0,3), (10,3), (11,0) |
| 1 | (0,4), (1,5), (10,4), (11,1), (11,5) | (0,4), (10,4), (11,1) |
| 2 | (0,5), (10,5), (11.2) | (0,5), (10,5), (11.2) |
| 3 | (0,6), (10,6), (11.3) | (1,4), (11,3), (11.4) |

#### 6.6.4.1 PBCH repetition in the cell acquisition subframe

For a MBMS-dedicated cell with $ N_{RB}^{DL}>6 $,

- symbols mapped to core resource element $\left ( k,l\right ) $ in slot 1 in subframe 0 within a radio frame $ n_{f}$ according to the mapping operation in clause 6.6.4, and

- cell-specific reference signals in OFDM symbols $ l $ in slot 1 in subframe 0 within a radio frame $ n_{f}$ with $ l $ according to the mapping operation in clause 6.6.4

shall additionally be multiplied by $\theta  _{k,l^{'}}$ and mapped to resource elements $\left ( k,l'\right ) $ in slot number $ n_{s}^{'}$ within radio frame $ n_{f}$ where $ l'$ and $ n_{s}^{'}$ are given by Table 6.6.4.1-1 in frames fulfilling

- $ n_{f}mod 4 = 0 $ for $ 25\leq  N_{RB}^{DL}$;

- $ n_{f}mod 8 = 4 $ for $ 6<N_{RB}^{DL}<25 $


Resource elements already reserved or used for transmission of cell-specific reference signals in absence of repetition shall not be used for additional mapping of cell-specific reference signals.

The quantity $\theta  _{k,l^{'}}$ is given by

$$\theta  _{k,l^{'}}=e^{j\frac {\pi  c\left ( 2k^{'}\right ) }{2}}e^{j\pi  c\left ( 2k^{'}+1\right ) }$$

where the relationship between $ k'$ and $ k $ is defined in clause 6.6.4, and the pseudo-random sequence $ c\left ( i\right ) $ is given by clause 7.2 and initialized for each OFDM symbol $ l'$ with

$$ c_{init}=2^{13}\left ( \left ( N_{ID}^{cell}+1\right ) \left ( N_{symb}^{DL}n_{s}^{'}+l'+1\right ) \right ) +2^{4}N_{ID}^{cell}+\left ( N_{symb}^{DL}n_{s}^{'}+l'\right ) $$

Table 6.6.4.1-1: Slot and symbol number pair for repetition of PBCH.

| $ l $ | Slot and symbol number pair $\left ( n_{s}^{'},l^{'}\right ) $ |  |
| --- | --- | --- |
|  | Normal cyclic prefix | Extended cyclic prefix |
| 0 | (0, 4) | - |
| 1 | (1, 4) | (0, 3) |
| 2 | (1, 5) | (1, 4) |
| 3 | (0, 3), (1, 6) | (1, 5) |

## 6.7 Physical control format indicator channel

The physical control format indicator channel carries information about the number of OFDM symbols used for transmission of PDCCHs in a subframe. The set of OFDM symbols possible to use for PDCCH in a subframe is given by Table 6.7-1.

Table 6.7-1: Number of OFDM symbols used for PDCCH

| Subframe | Number of OFDM symbols for PDCCH when ![](media_svg/image503.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}^{=}^{0}] | Number of OFDM symbols for PDCCH when ![](media_svg/image504.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}] |
| --- | --- | --- |
| Subframe 1 and 6 for frame structure type 2 or a subframe for frame structure type 3 with the same duration as the DwPTS duration of a special subframe configuration | 1, 2 | 2 |
| MBSFN subframes with ![](media_svg/image505.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}^{=}^{0}] and configured with 1 or 2 cell-specific antenna ports | 1, 2 | 2 |
| MBSFN subframes with ![](media_svg/image505.svg) [公式≈: ^{P}^{ˆ}PUCCH_CG1^{(}^{i}^{)}^{=}^{0}] and configured with 4 cell-specific antenna ports | 2 | 2 |
| MBSFN subframes with $∆f\in  \left \{ 7.5, 2.5, 1.25\right \} $ kHz or MBSFN slots with $∆f\approx  0.37 $ kHz | 0 | 0 |
| Non-MBSFN subframes (except subframe 6 for frame structure type 2) configured with positioning reference signals | 1, 2, 3 | 2, 3 |
| All other cases | 1, 2, 3 | 2, 3, 4 |

The UE may assume the PCFICH is transmitted when the number of OFDM symbols for PDCCH is greater than zero unless stated otherwise in [4, clause 12].

### 6.7.1 Scrambling

The block of bits ![](media_svg/image506.svg) [公式≈: ^{P}^{ˆ}PUSCH,c^{(}^{i}^{)}] transmitted in one subframe shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bits![](media_svg/image507.svg) [公式≈: ^{P}PUSCH,c^{(}^{i}^{)}]according to

![](media_svg/image508.svg) [公式: 0≥Α1(i)≥1]

where the scrambling sequence ![](media_svg/image467.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image509.svg) [公式: j⎰CG1] at the start of each subframe.

### 6.7.2 Modulation

The block of scrambled bits![](media_svg/image507.svg) [公式≈: ^{P}PUSCH,c^{(}^{i}^{)}] shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols![](media_svg/image510.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}]. Table 6.7.2-1 specifies the modulation mappings applicable for the physical control format indicator channel.

Table 6.7.2-1: PCFICH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PCFICH | QPSK |

### 6.7.3 Layer mapping and precoding

The block of modulation symbols ![](media_svg/image510.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}] shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with![](media_svg/image511.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}] and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors ![](media_svg/image475.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)...y^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image512.svg) [公式≈: Α2(i)∪P^{ˆ}_{PUSCH}_{,}_{j}(i)≥P^{ˆ}_{CG}^{1}_{1}(i)], where ![](media_svg/image212.svg) [公式: y^{(}^{p}^{)}(i)] represents the signal for antenna port ![](media_svg/image34.svg) [公式: p] and where ![](media_svg/image477.svg) [公式: p=0,...,P−1]and the number of antenna ports for cell-specific reference signals ![](media_svg/image478.svg) [公式: P⎰{1,2,4}]. The PCFICH shall be transmitted on the same set of antenna ports as the PBCH.

### 6.7.4 Mapping to resource elements

The mapping to resource elements is defined in terms of quadruplets of complex-valued symbols. Let ![](media_svg/image513.svg) [公式: 0≥Α2(i)≥1] denote symbol quadruplet ![](media_svg/image112.svg) [公式: i] for antenna port![](media_svg/image514.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}]. For each of the antenna ports, symbol quadruplets shall be mapped in increasing order of ![](media_svg/image112.svg) [公式: i] to the four resource-element groups in the first OFDM symbol in a downlink subframe or DwPTS with the representative resource-element as defined in clause 6.2.4 given by

![](media_svg/image515.svg) [公式≈: P^{ˆ}_{CG}^{1}_{1}(i)]

where the additions are modulo ![](media_svg/image516.svg) [公式: c⎰CG1] ,

![](media_svg/image517.svg) [公式≈: _{c}_{⎰}_{⊆}_{CG}_{1}w(i)∪P^{ˆ}_{PUSCH}_{,}_{c}(i)≥(P^{ˆ}_{CG}^{1}_{1}(i)−P^{ˆ}_{PUCCH_CG1}(i))]

and ![](media_svg/image518.svg) [公式: w(i)] is the physical-layer cell identity as given by clause 6.11.

## 6.8 Physical downlink control channel

### 6.8.1 PDCCH formats

The physical downlink control channel carries scheduling assignments and other control information. A physical control channel is transmitted on an aggregation of one or several consecutive control channel elements (CCEs), where a control channel element corresponds to 9 resource element groups. The number of resource-element groups not assigned to PCFICH or PHICH is ![](media_svg/image519.svg) [公式≈: ^{P}^{ˆ}PUSCH,c^{(}^{i}^{)}]. The CCEs available in the system are numbered from 0 to![](media_svg/image520.svg) [公式: c], where ![](media_svg/image521.svg) [公式: 0≥w(i)≥1]. The PDCCH supports multiple formats as listed in Table 6.8.1-1 where PDCCH format 4 is supported only for non-MBSFN subframes in an MBMS-dedicated cell. A PDCCH consisting of ![](media_svg/image522.svg) [公式≈: P^{ˆ}_{CG}^{1}_{1}(i)] consecutive CCEs may only start on a CCE fulfilling![](media_svg/image523.svg) [公式≈: _{c}_{⎰}_{CG}_{⊆}_{1}_{,}_{c}w_{⎯}_{j}(i)∪P^{ˆ}_{PUSCH}_{,}_{c}(i)≥(P^{ˆ}_{CG}^{1}_{1}(i)−P^{ˆ}_{PUSCH}_{,}_{j}(i))], where ![](media_svg/image112.svg) [公式: i] is the CCE number.

Multiple PDCCHs can be transmitted in a subframe.

Table 6.8.1-1: Supported PDCCH formats

| PDCCH format | Number of CCEs | Number of resource-element groups | Number of PDCCH bits |
| --- | --- | --- | --- |
| 0 | 1 | 9 | 72 |
| 1 | 2 | 18 | 144 |
| 2 | 4 | 36 | 288 |
| 3 | 8 | 72 | 576 |
| 4 | 16 | 144 | 1152 |

### 6.8.2 PDCCH multiplexing and scrambling

The block of bits ![](media_svg/image524.svg) [公式: w(i)] on each of the control channels to be transmitted in a subframe, where ![](media_svg/image525.svg) [公式: c] is the number of bits in one subframe to be transmitted on physical downlink control channel number ![](media_svg/image526.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}], shall be multiplexed, resulting in a block of bits ![](media_svg/image527.svg) [公式≈: b^{(}^{0}^{)}(0),...,b^{(}^{0}^{)}(M_{bit}^{(0)}−1),b^{(}^{1}^{)}(0),...,b^{(}^{1}^{)}(M_{bit}^{(1)}−1),...,b^{(}^{n}^{PDCCH}^{−}^{1}^{)}(0),...,b^{(}^{n}^{PDCCH}^{−}^{1}^{)}(M_{bit}^{(}^{n}^{PDCCH}^{-}^{1)}−1)], where ![](media_svg/image528.svg) [公式≈: ^{n}PDCCH] is the number of PDCCHs transmitted in the subframe.

The block of bits ![](media_svg/image527.svg) [公式≈: b^{(}^{0}^{)}(0),...,b^{(}^{0}^{)}(M_{bit}^{(0)}−1),b^{(}^{1}^{)}(0),...,b^{(}^{1}^{)}(M_{bit}^{(1)}−1),...,b^{(}^{n}^{PDCCH}^{−}^{1}^{)}(0),...,b^{(}^{n}^{PDCCH}^{−}^{1}^{)}(M_{bit}^{(}^{n}^{PDCCH}^{-}^{1)}−1)] shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bits ![](media_svg/image529.svg) [公式: b^{~}(0),...,b^{~}(M_{tot}−1)]according to

![](media_svg/image530.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image467.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image531.svg) [公式≈: ^{c}init^{=}√^{n}s^{2}∃^{2}^{9}^{+}^{N}ID^{cell}] at the start of each subframe.

CCE number ![](media_svg/image522.svg) [公式≈: P^{ˆ}_{CG}^{1}_{1}(i)] corresponds to bits ![](media_svg/image532.svg) [公式: b(72n),b(72n+1),...,b(72n+71)]. If necessary, <NIL> elements shall be inserted in the block of bits prior to scrambling to ensure that the PDCCHs starts at the CCE positions as described in TS 36.213 [4] and to ensure that the length ![](media_svg/image533.svg) [公式≈: ^{M}tot^{=}^{8}^{N}REG^{÷}⊆_{i}^{n}_{=}^{PDCCH}_{0}^{−}^{1}^{M}bit^{(}^{i}^{)}] of the scrambled block of bits matches the amount of resource-element groups not assigned to PCFICH or PHICH.

### 6.8.3 Modulation

The block of scrambled bits![](media_svg/image529.svg) [公式: b^{~}(0),...,b^{~}(M_{tot}−1)] shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)]. Table 6.8.3-1 specifies the modulation mappings applicable for the physical downlink control channel.

Table 6.8.3-1: PDCCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PDCCH | QPSK |

### 6.8.4 Layer mapping and precoding

The block of modulation symbols ![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)] shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with ![](media_svg/image474.svg) [公式≈: ^{M}symb^{(}^{0}^{)}^{=}^{M}symb] and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors ![](media_svg/image475.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)...y^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image534.svg) [公式≈: i=0,...,M_{symb}−1] to be mapped onto resources on the antenna ports used for transmission, where ![](media_svg/image212.svg) [公式: y^{(}^{p}^{)}(i)] represents the signal for antenna port ![](media_svg/image34.svg) [公式: p]. The PDCCH shall be transmitted on the same set of antenna ports as the PBCH.

### 6.8.5 Mapping to resource elements

The mapping to resource elements is defined by operations on quadruplets of complex-valued symbols. Let ![](media_svg/image513.svg) [公式: 0≥Α2(i)≥1] denote symbol quadruplet ![](media_svg/image112.svg) [公式: i] for antenna port![](media_svg/image514.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}].

The block of quadruplets![](media_svg/image535.svg) [公式≈: z^{(}^{p}^{)}(0),...,z^{(}^{p}^{)}(M_{quad}−1)] , where ![](media_svg/image536.svg) [公式≈: ^{M}quad^{=}^{M}symb^{4}], shall be permuted resulting in ![](media_svg/image537.svg) [公式≈: w^{(}^{p}^{)}(0),...,w^{(}^{p}^{)}(M_{quad}−1)]. The permutation shall be according to the sub-block interleaver in clause 5.1.4.2.1 of TS36.212 [3] with the following exceptions:

- the input and output to the interleaver is defined by symbol quadruplets instead of bits

- interleaving is performed on symbol quadruplets instead of bits by substituting the terms "bit", "bits" and "bit sequence" in clause 5.1.4.2.1 of TS 36.212 [3] by "symbol quadruplet", "symbol quadruplets" and "symbol-quadruplet sequence", respectively

<NULL> elements at the output of the interleaver in TS 36.212 [3] shall be removed when forming ![](media_svg/image537.svg) [公式≈: w^{(}^{p}^{)}(0),...,w^{(}^{p}^{)}(M_{quad}−1)]. Note that the removal of <NULL> elements does not affect any <NIL> elements inserted in clause 6.8.2.

The block of quadruplets ![](media_svg/image538.svg) [公式≈: w^{(}^{p}^{)}(0),...,w^{(}^{p}^{)}(M_{quad}−1)] shall be cyclically shifted, resulting in ![](media_svg/image539.svg) [公式≈: w^{(}^{p}^{)}(0),...,w^{(}^{p}^{)}(M_{quad}−1)] where![](media_svg/image540.svg) [公式≈: w^{(}^{p}^{)}(i)=w^{(}^{p}^{)}((i+N_{ID}^{cell})modM_{quad})].

Mapping of the block of quadruplets ![](media_svg/image541.svg) [公式≈: w^{(}^{p}^{)}(0),...,w^{(}^{p}^{)}(M_{quad}−1)] is defined in terms of resource-element groups, specified in clause 6.2.4, according to steps 1–10 below:

1) Initialize ![](media_svg/image542.svg) [公式: m±=0] (resource-element group number)

2) Initialize ![](media_svg/image543.svg) [公式: k&apos;=0]

3) Initialize ![](media_svg/image544.svg) [公式: l&apos;=0]

4) If the resource element ![](media_svg/image545.svg) [公式: (k±,l±)] represents a resource-element group and the resource-element group is not assigned to PCFICH or PHICH then perform step 5 and 6, else go to step 7

5) Map symbol-quadruplet ![](media_svg/image546.svg) [公式: w^{(}^{p}^{)}(m&apos;)] to the resource-element group represented by ![](media_svg/image547.svg) [公式: (k±,l±)] for each antenna port ![](media_svg/image514.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}]

6) Increase ![](media_svg/image548.svg) [公式: m^{±}] by 1

7) Increase ![](media_svg/image549.svg) [公式: l&apos;] by 1

8) Repeat from step 4 if ![](media_svg/image550.svg) [公式: l&apos;<L], where ![](media_svg/image551.svg) [公式: L] corresponds to the number of OFDM symbols used for PDCCH transmission. The quantity $ L $ is obtained from

- the sequence transmitted on the PCFICH, or

- the higher-layer parameter cfi-SubframeMBSFN-r15 for DCI formats other than DCI format 7 in a MBSFN subframe, or

- the higher-layer parameter cfi-SlotSubslotMBSFN-r15 for DCI format 7 in a MBSFN subframe, or

- the higher-layer parameter cfi-SubframeNonMBSFN-r15 for DCI formats other than DCI format 7 in a non-MBSFN subframe, or

- the higher-layer parameter cfi-SlotSubslotNonMBSFN-r15 for DCI format 7 in a non-MBSFN subframe, or

- the higher-layer parameter cfi-PatternSubframe-r15 for DCI formats other than DCI format 7 in one subframe for frame structure 2, or

- the higher-layer parameter cfi-PatternSlotSubslot-r15 for DCI formats 7 in one subframe for frame structure 2.

9) Increase ![](media_svg/image552.svg) [公式: k&apos;] by 1

10) Repeat from step 3 if ![](media_svg/image553.svg) [公式≈: k&apos;<N_{RB}^{DL}∪N_{sc}^{RB}]

PDCCHs shall not be transmitted in MBSFN subframes with zero-size non-MBSFN region.

## 6.8A Enhanced physical downlink control channel

For frame structure type 3, for a subframe with the same duration as the DwPTS duration of a special subframe configuration, the enhanced physical downlink control channel is defined the same as that for the corresponding special subframe configuration.

### 6.8A.1 EPDCCH formats

The enhanced physical downlink control channel (EPDCCH) carries scheduling assignments. An enhanced physical downlink control channel is transmitted using an aggregation of one or several consecutive enhanced control channel elements (ECCEs) where each ECCE consists of multiple enhanced resource element groups (EREGs), defined in clause 6.2.4A. The number of ECCEs used for one EPDCCH depends on the EPDCCH format as given by Table 6.8A.1-2 and the number of EREGs per ECCE is given by Table 6.8A.1-1. Both localized and distributed transmission is supported.

An EPDCCH can use either localized or distributed transmission, differing in the mapping of ECCEs to EREGs and PRB pairs.

A UE shall monitor multiple EPDCCHs as defined in TS 36.213 [4]. One or two sets of physical resource-block pairs which a UE shall monitor for EPDCCH transmissions can be configured. All EPDCCH candidates in EPDCCH set ![](media_svg/image554.svg) [公式≈: ^{X}m] use either only localized or only distributed transmission as configured by higher layers. Within EPDCCH set ![](media_svg/image555.svg) [公式≈: ^{X}m] in subframe ![](media_svg/image556.svg) [公式: i], the ECCEs available for transmission of EPDCCHs are numbered from 0 to ![](media_svg/image557.svg) [公式≈: ^{N}ECCE,m,i^{−}^{1}] and ECCE number ![](media_svg/image558.svg) [公式: n] corresponds to

- EREGs numbered ![](media_svg/image559.svg) [公式≈: (nmodN_{ECCE}^{RB})+jN_{ECCE}^{RB}] in PRB index ![](media_svg/image560.svg) [公式≈: √^{n}^{/}^{N}ECCE^{RB}∃] for localized mapping, and

- EREGs numbered ![](media_svg/image561.svg) [公式≈: √^{n}^{N}RB^{X}^{m}∃^{+}^{jN}ECCE^{RB}] in PRB indices ![](media_svg/image562.svg) [公式≈: (n+jmax(1,N_{RB}^{X}^{m}N_{EREG}^{ECCE}))modN_{RB}^{X}^{m}] for distributed mapping,

where ![](media_svg/image563.svg) [公式≈: j=0,1,...,N_{EREG}^{ECCE}−1], ![](media_svg/image564.svg) [公式≈: _{N}_{EREG}ECCE] is the number of EREGs per ECCE, and ![](media_svg/image565.svg) [公式≈: ^{N}ECCE^{RB}^{=}^{16}^{N}EREG^{ECCE}] is the number of ECCEs per resource-block pair. The physical resource-block pairs constituting EPDCCH set ![](media_svg/image566.svg) [公式≈: ^{X}m] are in this paragraph assumed to be numbered in ascending order from 0 to ![](media_svg/image567.svg) [公式: N_{RB}^{X}^{m}−1].

Table 6.8A.1-1: Number of EREGs per ECCE, ![](media_svg/image568.svg) [公式≈: _{N}_{EREG}ECCE]

| Normal cyclic prefix |  |  | Extended cyclic prefix |  |
| --- | --- | --- | --- | --- |
| Normal subframe | Special subframe, configuration 3, 4, 8 | Special subframe, configuration 1, 2, 6, 7, 9, 10 | Normal subframe | Special subframe, configuration 1, 2, 3, 5, 6 |
| 4 |  | 8 |  |  |

Table 6.8A.1-2: Supported EPDCCH formats

| EPDCCH format | Number of ECCEs for one EPDCCH, ![](media_svg/image569.svg) [公式≈: _{N}_{ECCE}EPDCCH] |  |  |  |
| --- | --- | --- | --- | --- |
|  | Case A |  | Case B |  |
|  | Localized transmission | Distributed transmission | Localized transmission | Distributed transmission |
| 0 | 2 | 2 | 1 | 1 |
| 1 | 4 | 4 | 2 | 2 |
| 2 | 8 | 8 | 4 | 4 |
| 3 | 16 | 16 | 8 | 8 |
| 4 | - | 32 | - | 16 |

Case A in Table 6.8A.1-2 is used when the conditions corresponding to case 1 in clause 9.1.4 of TS 36.213 [4] are satisfied, otherwise case B is used. The quantity ![](media_svg/image570.svg) [公式≈: ^{n}EPDCCH] for a particular UE and referenced in TS 36.213 [4] is defined as the number of downlink resource elements ![](media_svg/image571.svg) [公式: (k,l)] available for EPDCCH transmission in a physical resource-block pair configured for possible EPDCCH transmission of EPDCCH set ![](media_svg/image572.svg) [公式≈: ^{X}0] and fulfilling all of the following criteria:

- they are part of any one of the 16 EREGs in the physical resource-block pair, and

- they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS36.213 [4], and-

- they are assumed by the UE not to be used for transmission of CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2 with the configuration for zero power CSI reference signals obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS36.213 [4], and with the configuration for non-zero power CSI reference signals obtained as described in clause 6.10.5.2, and

- for frame structure type 1 and 2, the index ![](media_svg/image402.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image574.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4], and

- for frame structure type 3,

- if the higher layer parameter subframeStartPosition indicates 's07' and if the downlink transmission starts in the second slot of a subframe

- the index ![](media_svg/image402.svg) [公式: l] in the second slot in the subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image575.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4],

- otherwise

- the index ![](media_svg/image402.svg) [公式: l] in the first slot in the subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image576.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4].

### 6.8A.2 Scrambling

The block of bits ![](media_svg/image577.svg) [公式: b(0),...,b(M_{bit}−1)] to be transmitted on an EPDCCH in a subframe shall be scrambled, resulting in a block of scrambled bits ![](media_svg/image578.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image579.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the UE-specific scrambling sequence ![](media_svg/image580.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialized with ![](media_svg/image581.svg) [公式≈: ^{c}init^{=}√^{n}s^{2}∃^{∪}^{2}^{9}^{+}^{n}ID^{EPDCCH},m] where ![](media_svg/image582.svg) [公式: m] is the EPDCCH set number.

### 6.8A.3 Modulation

The block of scrambled bits ![](media_svg/image578.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)]. Table 6.8A.3-1 specifies the modulation mappings applicable for the enhanced physical downlink control channel.

Table 6.8A.3-1: EPDCCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| EPDCCH | QPSK |

### 6.8A.4 Layer mapping and precoding

The block of complex-valued modulation symbols shall be mapped to a single layer and precoded according to 6.3.4.1 as for ![](media_svg/image583.svg) [公式: y(i)=d(i)], ![](media_svg/image584.svg) [公式≈: i=0,...,M_{symb}−1].

### 6.8A.5 Mapping to resource elements

The block of complex-valued symbols ![](media_svg/image585.svg) [公式≈: y(0),...,y(M_{symb}−1)] shall be mapped in sequence starting with ![](media_svg/image586.svg) [公式: y(0)] to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on the associated antenna port which meet all of the following criteria:

- they are part of the EREGs assigned for the EPDCCH transmission, and

- they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS36.213 [4], and

- they are assumed by the UE not to be used for transmission of:

- zero-power CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

- obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS 36.213 [4], and

- obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

- non-zero-power CSI reference signals for CSI reporting, except for non-zero power CSI reference signals configured by csi-RS-ConfigNZP-ApList,  with the configuration for non-zero power CSI reference signals for CSI reporting obtained as described in clause 6.10.5.2, and

- for frame structure type 1 and 2, the index ![](media_svg/image402.svg) [公式: l] in the first slot in a subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image574.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4], and

- for frame structure type 3,

- if the higher layer parameter subframeStartPosition indicates 's07' and if the downlink transmission starts in the second slot of a subframe

- the index ![](media_svg/image402.svg) [公式: l] in the second slot in the subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image576.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4],

- otherwise

- the index ![](media_svg/image402.svg) [公式: l] in the first slot in the subframe fulfils ![](media_svg/image573.svg) [公式≈: ^{l}^{÷}^{l}EPDCCHStart] where ![](media_svg/image576.svg) [公式≈: ^{l}EPDCCHStart] is given by clause 9.1.4.1 of TS36.213 [4].

The mapping to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] meeting the criteria above shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] and then the index![](media_svg/image389.svg) [公式: l], starting with the first slot and ending with the second slot in a subframe.

For localized transmission, the single antenna port ![](media_svg/image34.svg) [公式: p] to use is given by Table 6.8A.5-1 with

![](media_svg/image587.svg) [公式≈: n&apos;=n_{ECCE,}_{low}modN_{ECCE}^{RB}+n_{RNTI}modmin(N_{ECCE}^{EPDCCH},N_{ECCE}^{RB})]

where ![](media_svg/image588.svg) [公式≈: ^{n}ECCE,low] is the lowest ECCE index used by this EPDCCH transmission in the EPDCCH set, ![](media_svg/image145.svg) [公式≈: ^{n}RNTI] equals the C-RNTI, and ![](media_svg/image589.svg) [公式≈: _{N}_{ECCE}EPDCCH] is the number of ECCEs used for this EPDCCH.

Table 6.8A.5-1: Antenna port to use for localized EPDCCH transmission

| ![](media_svg/image590.svg) [公式: n&apos;] | Normal cyclic prefix |  | Extended cyclic prefix |
| --- | --- | --- | --- |
|  | Normal subframes,Special subframes, configurations 3, 4, 8 | Special subframes,  configurations 1, 2, 6, 7, 9, 10 | Any subframe |
| 0 | 107 | 107 | 107 |
| 1 | 108 | 109 | 108 |
| 2 | 109 | - | - |
| 3 | 110 | - | - |

For distributed transmission, each resource element in an EREG is associated with one out of two antenna ports in an alternating manner, starting with antenna port 107, where ![](media_svg/image591.svg) [公式: p⎰{107,109}] for normal cyclic prefix and ![](media_svg/image592.svg) [公式: p⎰{107,108}] for extended cyclic prefix.

## 6.8B MTC physical downlink control channel

### 6.8B.1 MPDCCH formats

The MPDCCH formats are defined as in Clause 6.8A.1 with the following exceptions:

- The term EPDCCH is replaced by MPDCCH.

- The MTC physical downlink control channel carries downlink control information and is transmitted across ![](media_svg/image593.svg) [公式≈: _{N}_{rep}MPDCCH_{÷}_{1}] consecutive BL/CE DL subframes. Within each of the ![](media_svg/image594.svg) [公式≈: _{N}_{rep}MPDCCH] BL/CE DL subframes an MPDCCH is transmitted using an aggregation of one or several consecutive enhanced control channel elements (ECCEs) where each ECCE consists of multiple enhanced resource element groups (EREGs), defined in clause 6.2.4A.

- For frame structure type 2,

- If repetition is not configured for the MPDCCH, the number of EREGs per ECCE is given by Table 6.8A.1-1. If repetition is configured for the MPDCCH, the number of EREGs per ECCE is given by Table 6.8B.1-1.

- For those special subframes where the MPDCCH is not supported, these special subframes are considered BL/CE DL subframes for both MPDCCH and PDSCH transmission, only if they are indicated as BL/CE DL subframe by higher layer signalling.

- For an MPDCCH associated with 2 or 4 PRBs, if repetition is not configured for the MPDCCH, the supported MPDCCH formats are given by Table 6.8A.1-2. Otherwise, the supported MPDCCH formats are given by Table 6.8B.1-2. However, for MPDCCH format 5, the equation defining the relation between ECCE index and EREG index does not apply and the number of ECCEs refers to the MPDCCH mapping to the REs of the 2+4 PRB set as defined in Clause 6.8B.5.

Table 6.8B.1-1: Number of EREGs per ECCE, ![](media_svg/image568.svg) [公式≈: _{N}_{EREG}ECCE], for frame structure type 2.

| Normal cyclic prefix |  | Extended cyclic prefix |  |
| --- | --- | --- | --- |
| Normal subframe | Special subframe, configuration 3, 4, 8 | Normal subframe | Special subframe, configuration 1, 2, 3, 5, 6 |
| 4 |  | 8 |  |

Table 6.8B.1-2: Supported MPDCCH formats

| MPDCCH format | Number of ECCEs in a subframe for one MPDCCH, ![](media_svg/image595.svg) [公式≈: _{N}_{ECCE}MPDCCH] |  |  |  |
| --- | --- | --- | --- | --- |
|  | ![](media_svg/image568.svg) [公式≈: _{N}_{EREG}ECCE]=4 |  | ![](media_svg/image568.svg) [公式≈: _{N}_{EREG}ECCE]=8 |  |
|  | Localized transmission | Distributed transmission | Localized transmission | Distributed transmission |
| 0 | 2 | 2 | 1 | 1 |
| 1 | 4 | 4 | 2 | 2 |
| 2 | 8 | 8 | 4 | 4 |
| 3 | 16 | 16 | 8 | 8 |
| 4 | - | - | - | - |
| 5 | 24 | 24 | 12 | 12 |

### 6.8B.2 Scrambling

Scrambling shall be perfomed according to Clause 6.8A.2 with EPDCCH replaced by MPDCCH except that the same scrambling sequence is applied per subframe to MPDCCH for a given block of ![](media_svg/image146.svg) [公式≈: ^{N}acc] subframes and ![](media_svg/image582.svg) [公式: m] is the MPDCCH set number. For an MPDCCH associated with a 2+4 PRB set as defined in [4], ![](media_svg/image596.svg) [公式: m=0] is used to generate the scrambling sequence for mapping to REs in 6 PRBs as well as 2 PRBs and 4 PRBs.

The subframe number of the first subframe in each block of ![](media_svg/image147.svg) [公式≈: ^{N}acc] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image149.svg) [公式≈: (^{niN}abs,1acc^{+=}δ)^{mod0}]. For the ![](media_svg/image597.svg) [公式≈: _{j}th]block of ![](media_svg/image146.svg) [公式≈: ^{N}acc] subframes, the scrambling sequence generator shall be initialised with

![](media_svg/image598.svg) [公式≈: _{c}_{init}_{=}√⌡_{⌠}_{⌡}_{∞}{_{{}(_{(}j_{j}0_{0}+_{+}j_{j})_{)}N_{N}acc_{acc}mod_{mod}10_{10}}_{}}∪_{∪}2_{2}^{9}_{9}+_{+}_{n}N_{ID}_{MPDCCH}ID^{cell}_{,}_{m}for _{otherwise}Type1-Common,Type2-common]

where

![](media_svg/image599.svg) [公式≈: ^{i}^{j}^{j}^{δ}^{0}^{=}^{=}^{=}^{0}^{√}^{⌠}_{∞}^{√}^{,}^{1}^{(}^{0,}N^{,...,}^{i}^{0}_{acc}^{+}^{⋅}^{⋅}^{⋅}^{√}^{i}−^{i}^{δ}^{0}2^{)}^{+},^{N}^{N}^{acc}^{for }for ^{abs}^{MPDCCH}^{∃}^{N}^{frame}frame^{acc}^{+}^{structure}structure^{i}^{δ}^{−}^{1}^{∂}^{∂}^{∂}^{∃}^{−}^{ type} type^{j}^{0}^{1}2^{or  }and^{N}N^{acc}_{acc}^{=}=^{1}10]

and ![](media_svg/image153.svg) [公式≈: ^{i}0] is the absolute subframe number of the first downlink subframe intended for the MPDCCH. The MPDCCH transmission spans ![](media_svg/image600.svg) [公式≈: _{N}_{abs}MPDCCH] consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

For BL/CE UEs,

- if the MPDCCH transmission is associated with P-RNTI or SC-RNTI:

- ![](media_svg/image156.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image157.svg) [公式: N_{acc}=10] for frame structure type 2

- otherwise

- ![](media_svg/image155.svg) [公式: N_{acc}=1]for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA:

- ![](media_svg/image156.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image157.svg) [公式: N_{acc}=10] for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB.

### 6.8B.3 Modulation

Modulation shall be performed according to 6.8A.3 with EPDCCH replaced by MPDCCH.

### 6.8B.4 Layer mapping and precoding

Layer mapping and precoding shall be done according to Clause 6.8A.4 with EPDCCH replaced by MPDCCH.

### 6.8B.5 Mapping to resource elements

Mapping to resource elements shall be done according to Clause 6.8A.5 with the following exceptions:

- The term EPDCCH shall be replaced by MPDCCH.

- The mapping shall be repeated across each of the ![](media_svg/image601.svg) [公式≈: _{N}_{rep}MPDCCH] BL/CE DL subframes.

- ![](media_svg/image602.svg) [公式≈: _{N}_{ECCE}MPDCCH] is the number of ECCEs used for this MPDCCH in the first of the ![](media_svg/image603.svg) [公式≈: _{N}_{rep}MPDCCH] subframes.

- For an MPDCCH associated with a 2+4 PRB set as defined in [4], the mapping to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p] shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] and then the index![](media_svg/image389.svg) [公式: l] over the 6 PRBs for MPDCCH format 5 and over the 2 or 4 PRBs for the other MPDCCH formats.

- For localized transmission and MPDCCH format 5, the single antenna port ![](media_svg/image34.svg) [公式: p] to use is given by Table 6.8A.5-1 with

![](media_svg/image604.svg) [公式≈: n&apos;=n_{RNTI}modN_{ECCE}^{RB}]

where ![](media_svg/image145.svg) [公式≈: ^{n}RNTI] equals the C-RNTI.

- Resource elements occupied by CSI reference signals shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

- PRB pairs occupied by RSS shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

- Resource elements belonging to PRBs in which PRS is transmitted (including PRS muted subframes) shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

- A BL/CE UE not configured with higher layer parameter ce-pdsch-maxBandwidth-config and not configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig may assume there is no MPDCCH transmission which uses overlapping sets of subframes as PDSCH transmissions to that UE, where the MPDCCH is located at a different narrowband than the PDSCH.

- A BL/CE UE configured with higher layer parameter ce-pdsch-maxBandwidth-config may assume that there is no MPDCCH transmission which uses overlapping sets of subframes as PDSCH transmissions to that UE, where the MPDCCH transmission and PDSCH transmission in any of the overlapping subframes span a PRB region larger than X contiguous PRBs where X=25 if ce-pdsch-maxBandwidth-config is set to 5 MHz and X=100 if ce-pdsch-maxBandwidth-config is set to 20 MHz.

- A BL/CE UE configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig may assume there is no MPDCCH transmission in MPDCCH candidates not fully contained within the tuning narrowband defined for PDSCH in Clause 6.2.8.

- For BL/CE UEs in CEModeB, in MBSFN subframe(s), resource elements that correspond to the positions of cell-specific reference signals as in subframe #0 shall not be counted in the MPDCCH mapping and not used for transmission of the MPDCCH.

- Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

- If MPDCCH transmission in the LTE control region is configured by the higher layer parameter transmissionInControlChRegion,

- For frame structure type 1 and frame structure type 2 except special subframe configuration 9 or 10,

- Symbols used for transmission of MPDCCH or demodulation signals associated with MPDCCH and mapped to resource element $\left ( k,l\right ) $ in the second slot, where $ l\in  \{0..l_{MPDCCHStart}-1\}$, shall additionally be mapped to resource element $(k,l)$ in the first slot.

- For frame structure type 2 and special subframe configuration 9 or 10,

- Symbols used for transmission of MPDCCH or demodulation signals associated with MPDCCH and mapped to resource element $(k,l+4)$ in the first slot, where $ l\in  \{0..l_{MPDCCHStart}-1\}$, shall additionally be mapped to resource element $(k,l)$ in the first slot, if resource element $(k,l)$ in the first slot is not used for cell-specific reference signals.

- In the subframes where an MPDCCH or its associated PDSCH is transmitted in response to a physical random access transmission initiated by a PDCCH order, the UE shall receive the MPDCCH or its associated PDSCH, and assume no other UE-specific reception is needed.

- For MPDCCH transmission associated with C-RNTI or TPC-PUCCH-RNTI or TPC-PUSCH-RNTI or SPS C-RNTI that are not configured to use the Type2-MPDCCH common search space, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set.

- For MPDCCH transmission associated with PUR-RNTI using UE-specific MPDCCH search space, frequency hopping of the MPDCCH is enabled when mpdcch-FreqHopping in higher layer parameter PUR-MPDCCH-Config is set.

- For MPDCCH transmission associated with Type2-MPDCCH common search space, frequency hopping of the MPDCCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

- if PRACH CE level 0 or 1 is used for the last PRACH attempt, ![](media_svg/image451.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

- if PRACH CE level 2 or 3 is used for the last PRACH attempt, ![](media_svg/image451.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

- For MPDCCH transmission associated with SC-RNTI, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MCCH is set. Further

- if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeA, ![](media_svg/image605.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

- if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeB, ![](media_svg/image606.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

- For MPDCCH transmission associated with G-RNTI, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set. Further

- if mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeA, ![](media_svg/image607.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

- if mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeB, ![](media_svg/image608.svg) [公式≈: _{N}_{NB}ch,DL] is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

- The narrowband ![](media_svg/image609.svg) [公式≈: _{n}_{NB}^{(}^{i}0,ss^{)}] for MPDCCH transmission in the first subframe of MPDCCH search space is provided by higher layers. Starting subframe configuration of a search space where UE monitors an MPDCCH is also provided by higher layers. The MPDCCH search space uses ![](media_svg/image610.svg) [公式≈: _{N}_{rep,}MPDCCH_{ss}_{÷}_{1}] subframes, spanning ![](media_svg/image611.svg) [公式≈: _{N}_{abs,}MPDCCH_{ss}_{÷}_{N}_{rep,}MPDCCH_{ss}] consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

- If downlink resource reservation is enabled for the UE as specified in [9], then in case of MPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space,

- In a subframe that is fully reserved as defined in clause 7.1 in [4], the MPDCCH transmission is postponed until the next BL/CE downlink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved resource elements shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

- If frequency hopping is not enabled for MPDCCH, the repetitions of an MPDCCH candidate are located at the same PRB resources in the same narrowband ![](media_svg/image612.svg) [公式≈: _{n}_{NB}^{(}^{i}0,ss^{)}], and

- if frequency hopping is enabled for MPDCCH, an MPDCCH candidate shall be transmitted in absolute subframe ![](media_svg/image423.svg) [公式: i] using the same PRB resources within each narrowband ![](media_svg/image613.svg) [公式≈: _{n}_{NB}(i)]

![](media_svg/image614.svg) [公式≈: _{i}_{i}_{n}_{j}_{0}_{δ}_{0}_{NB}(_{,}_{ss}i_{=})_{=}_{≥}_{=}_{√}_{⌠}_{∞}_{√}_{(}_{0,}_{i}_{N}⊇_{⊕}_{⊕}_{⊗}_{i}_{0}_{≥}_{n}_{,}_{NB}_{ch,}_{ss}_{NB}(_{i}i0_{DL}_{0}_{+},_{,}ss_{ss})_{i}_{−}_{δ}_{+}_{+}_{)}_{2}⊇_{⊕}_{⊕}_{⊗}_{N}_{,}⋅_{⋅}_{√}_{N}_{abs,}_{MPDCCH}_{N}i_{NB}_{ch,}_{for }_{for }+_{ss}_{NB}_{ch,}_{DL}i_{DL}δ_{frame}_{frame}_{∃}_{−}_{−}_{1}_{j}_{0}_{structure}_{structure}∂_{∂}_{∃}_{mod}_{ N}_{ type}_{ type}_{NB,}ch,DL_{hop}_{1}_{2}⇒_{⇐}_{⇐}_{⇔}_{∪}_{f}_{NB,}DL_{hop}⇒_{⇐}_{⇐}_{⇔}_{mod}_{N}_{NB}DL]

where ![](media_svg/image615.svg) [公式≈: ^{i}0,ss] is the absolute subframe number of the first downlink subframe of MPDCCH search space, and ![](media_svg/image616.svg) [公式≈: ^{N}NB,^{ch,}^{DL}hop], ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] and ![](media_svg/image431.svg) [公式≈: ^{f}NB,^{DL}hop] are cell-specific higher-layer parameters. The UE shall not expect MPDCCH transmission in absolute subframe ![](media_svg/image432.svg) [公式: i] if it is not a BL/CE DL subframe.

- The UE may assume the same precoding matrix being used for a PRB across a block of ![](media_svg/image18.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes for MPDCCH, where the subframe number of the first subframe in each block of ![](media_svg/image18.svg) [公式≈: _{N}_{NB}ch,DL] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image450.svg) [公式≈: (^{niN}abs,1NB^{+=}δ)^{mod0}^{ch,DL}].

- If crs-ChEstMPDCCH-ConfigCommon or crs-ChEstMPDCCH-ConfigDedicated is configured by higher layers, the relation between the MPDCCH and CRS antenna ports is defined as follows:

- When one CRS port is configured by the eNB, the antenna port(s) used for MPDCCH transmission are equivalent to CRS port 0.

- For distributed transmission and when two CRS ports are configured by the eNB, the relation between the symbols transmitted on the antenna ports used for MPDCCH transmission and CRS ports 0 – 1 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-1 using codebook index $ 0 $ for antenna port 107 and codebook index $ 1 $ for antenna port 109.

- For distributed transmission and when four CRS ports are configured by the eNB, in absolute subframe $ n_{abs}$ and resource block index $ n_{PRB}$ within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna ports used for MPDCCH transmission and CRS ports 0 – 3 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-2 using codebook index $ i $ for antenna port 107 and codebook index $ i+1 $ for antenna port 109, where
$$ i=12+2\left ( \left ( \lfloor  \frac {n_{abs}+i_{\Delta  }}{n_{NB}^{ch,DL}}\rfloor  +n_{PRB}\right ) mod 2\right ) $$

- For localized transmission, when two CRS ports are configured by the eNB and predefined mapping type is used, in absolute subframe $ n_{abs}$ and resource block index $ n_{PRB}$ within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and CRS ports 0 – 1 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-1, with codebook index $ i $, where
$$ i=\left ( \lfloor  \frac {n_{abs}+i_{\Delta  }}{n_{NB}^{ch,DL}}\rfloor  +n_{PRB}\right ) mod 2 $$

- For localized transmission, when four CRS ports are configured by the eNB and predefined mapping type is used, in absolute subframe $ n_{abs}$ and resource block index $ n_{PRB}$ within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and CRS ports 0 – 3 is given by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-2 using codebook index $ i $ where
$$ i=12+\left ( \left ( \lfloor  \frac {n_{abs}+i_{\Delta  }}{n_{NB}^{ch,DL}}\rfloor  +\Delta  _{PRB}\left ( n_{PRB}mod 4\right ) \right ) mod4\right ) $$

$$\left [ \Delta  _{PRB}\left ( 0\right ) \Delta  _{PRB}\left ( 1\right ) \Delta  _{PRB}\left ( 2\right ) \Delta  _{PRB}\left ( 3\right ) \right ] =[0 2 1 3]$$

- For localized transmission and when CSI-based or reciprocity-based mapping type is used, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and the CRS ports is given in [4]. When it is indicated in [4] that the antenna port is changed for an MPDCCH candidate with aggregation level 2, the antenna port shall be replaced by the antenna port determined for an MPDCCH candidate with aggregation level 4 in the same search space.

- NOTE: $ n_{PRB}=0,\ldots  ,K-1 $, with $ K=6 $ for $ N_{RB}^{'X_{p}}=2+4,$ and $ K=N_{RB}^{'X_{p}}$ otherwise, where the ordering of PRBs within the PRB set(s) is in increasing order of PRB index.

The UE may assume that an MPDCCH associated with the P-RNTI is transmitted on the set ![](media_svg/image617.svg) [公式: {s_{j}}] of narrowbands where ![](media_svg/image436.svg) [公式: {s_{j}}] is defined in Clause 6.4.1. For a UE monitoring an MPDCCH associated with the P-RNTI, the first MPDCCH narrowband is given by ![](media_svg/image618.svg) [公式≈: ^{s}m] where ![](media_svg/image619.svg) [公式≈: m=(N^{~}_{NB}^{p}+N_{ID}^{cell})modN_{NB}^{S}], ![](media_svg/image620.svg) [公式≈: N^{~}_{NB}^{p}⎰{0,1,...,N_{NB}^{p}−1}] is the Paging Narrowband (PN) obtained according to [10], and ![](media_svg/image621.svg) [公式≈: ^{N}NB^{P}] is the higher-layer parameter paging-narrowBands.

- If the higher-layer parameter si-HoppingConfigCommon disables frequency hopping for an MPDCCH associated with P-RNTI, each MPDCCH candidate shall be located in the same PRB in narrowband ![](media_svg/image618.svg) [公式≈: ^{s}m] where ![](media_svg/image619.svg) [公式≈: m=(N^{~}_{NB}^{p}+N_{ID}^{cell})modN_{NB}^{S}].

- If the higher-layer parameter si-HoppingConfigCommon enables frequency hopping for an MPDCCH with P-RNTI, an MPDCCH candidate shall be located in narrowband ![](media_svg/image622.svg) [公式≈: ^{s}j] in absolute subframe ![](media_svg/image439.svg) [公式: i] using the same PRB resources within each narrowband ![](media_svg/image622.svg) [公式≈: ^{s}j] where

![](media_svg/image623.svg) [公式≈: jNNj  NfN=++−∪^{⊇⇒}⊕⇐_{⊕⇐}_{⊗⇔}(^{%}NBID0NB,hopNB,hopNB^{pcellch,DLDLS})^{⊇⇒}⊕⇐_{⊕⇐}_{⊗⇔}^{⋅∂}⋅∂_{√∃}_{N}^{ii}^{+}_{NB}ch,DL^{δ}modmod]

![](media_svg/image624.svg) [公式≈: ^{i}^{i}^{j}^{0}^{δ}^{0}^{,}^{ss}^{=}^{=}^{≥}^{√}^{⌠}_{∞}^{√}^{(}^{0,}^{i}N^{i}^{0}^{≥}^{,}_{NB}^{ch,}^{ss}^{i}^{0}^{DL}^{+}^{,}^{ss}^{i}−^{δ}^{+}^{)}2^{N},^{N}^{abs,}^{MPDCCH}^{NB}^{ch,}^{for }for ^{ss}^{DL}^{frame}frame^{∃}^{−}^{1}^{structure}structure^{ type} type^{1}2]

where ![](media_svg/image615.svg) [公式≈: ^{i}0,ss] is the absolute subframe number of the first downlink subframe of MPDCCH search space according to locations of paging opportunity subframes, and ![](media_svg/image616.svg) [公式≈: ^{N}NB,^{ch,}^{DL}hop], ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] and ![](media_svg/image431.svg) [公式≈: ^{f}NB,^{DL}hop] are cell-specific higher-layer parameters. For MPDCCH associated with P-RNTI, if interval-DlHoppingConfigCommonModeB is signalled in SIB1-BR, then the frequency hopping granularity ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] is set to interval-DlHoppingConfigCommonModeB; otherwise, ![](media_svg/image429.svg) [公式≈: _{N}_{NB}ch,DL] is set to interval-DlHoppingConfigCommonModeA signalled in SIB1-BR.

The UE shall not expect MPDCCH transmission in absolute subframe ![](media_svg/image432.svg) [公式: i] if it is not a BL/CE DL subframe.

## 6.8C Short physical downlink control channel (SPDCCH)

### 6.8C.1 SPDCCH formats

The short physical downlink control channel (SPDCCH) carries scheduling assignments and other control information for subslot PDSCH, slot-PDSCH, subslot-PUSCH, and slot-PUSCH. A SPDCCH is transmitted using an aggregation of one or several consecutive short control channel elements (SCCEs) where each SCCE consists of multiple short resource element groups (SREGs), defined in clause 6.2.4B. The number of resource elements used for one SPDCCH depends on the SPDCCH format as given by Table 6.8C.1-2 and the number of SREGs per SCCE is given by Table 6.8C.1-1.

Table 6.8C.1-1: Number of SREGs per SCCE, ![](media_svg/image625.svg) [公式≈: _{N}_{SREG}SCCE]

|  | ![](media_svg/image625.svg) [公式≈: _{N}_{SREG}SCCE] |
| --- | --- |
| CRS based SPDCCH | 4 |
| DMRS based SPDCCH | 4 for a 2-symbol SPDCCH16 for a 3-symbol SPDCCH1 |
| NOTE 1: see table 6.8C.5-1 and table 6.8C.5-2 |  |

Table 6.8C.1-2: Supported SPDCCH formats

| SPDCCH format | Number of SCCEs for one SPDCCH, ![](media_svg/image626.svg) [公式≈: _{N}_{SCCE}SPDCCH] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |

A UE shall monitor multiple SPDCCHs as defined in TS 36.213 [4]. One or two resource sets which a UE shall monitor for SPDCCH transmissions in a slot/subslot can be configured. The SPDCCH can use either localized or distributed transmission. All SPDCCH candidates in SPDCCH set ![](media_svg/image554.svg) [公式≈: ^{X}m] use either only localized or only distributed transmission as configured by higher layers (see transmissionType in TS 36.331 [9]). Similarly, all SPDCCH candidates in SPDCCH set ![](media_svg/image554.svg) [公式≈: ^{X}m] use either only CRS-based demodulation or only DMRS-based demodulation as configured by higher layers (see spdcch-SetReferenceSig in TS 36.331 [9]). For a resource set with CRS-based SPDCCH, the distributed transmission is implemented at the SREG level, i.e. in the SCCE-to-SREG mapping. For a resource set with DMRS-based SPDCCH, the distributed transmission is implemented at the SCCE level, i.e. in the SPDCCH candidate-to-SCCE mapping.

The number of OFDM symbols spanned by a SPDCCH resource set ![](media_svg/image554.svg) [公式≈: ^{X}m]configured with CRS based demodulation can be configured to be one or two.

For slot based transmission, the number of OFDM symbols spanned by each SPDCCH candidate of a resource set ![](media_svg/image554.svg) [公式≈: ^{X}m]configured with DMRS-based demodulation is fixed to 2. For subslot based transmission, the number of OFDM symbols spanned by each SPDCCH candidate of a resource set ![](media_svg/image554.svg) [公式≈: ^{X}m]configured with DMRS-based demodulation is equal to the number of OFDM symbols used for the subslot based PDSCH transmission (which depends on the starting symbol index, as specified in Table 6.4.2-1).

The physical resource blocks in frequency domain constituting SPDCCH set ![](media_svg/image566.svg) [公式≈: ^{X}m] are in this paragraph assumed to be numbered in ascending order from 0 to ![](media_svg/image567.svg) [公式: N_{RB}^{X}^{m}−1]. For a CRS-based SPDCCH, SREGs within an SPDCCH set ![](media_svg/image627.svg) [公式≈: ^{X}m] are numbered in a frequency-first time-second manner from 0 to![](media_svg/image628.svg) [公式≈: N_{os}^{X}^{m}N_{RB}^{X}^{m}−1], where ![](media_svg/image629.svg) [公式≈: ^{N}os^{X}^{m}]is the number of configured OFDM symbols (OS). The frequency-first, time-second mapping of the SREGs within a SPDCCH set is performed from the lowest resource block in frequency domain to the highest resource blocks in frequency domain for the first symbol, and from the highest resource block in frequency domain to the lowest resource block in frequency domain for the second symbol. For a DMRS-based SPDCCH, SREGs within an SPDCCH set![](media_svg/image630.svg) [公式≈: ^{X}m] are numbered in a time-first frequency-second manner from 0 to![](media_svg/image631.svg) [公式≈: N_{os}^{X}^{m}N_{RB}^{X}^{m}−1].

Within CRS-based SPDCCH set ![](media_svg/image555.svg) [公式≈: ^{X}m], the SCCEs available for transmission of SPDCCHs are numbered from 0 to ![](media_svg/image632.svg) [公式≈: ^{N}SCCE,m^{−}^{1}] where ![](media_svg/image633.svg) [公式≈: ^{N}SCCE,m^{=}√^{N}OS^{X}^{m}^{N}RB^{X}^{m}^{/}^{N}SREG^{SCCE}∃] for localized mapping and   ![](media_svg/image634.svg) [公式≈: ^{N}SCCE,m^{=}^{N}OS^{X}^{m}√^{N}RB^{X}^{m}^{/}^{N}SREG^{SCCE}∃]for distributed mapping. Within DMRS-based SPDCCH set ![](media_svg/image555.svg) [公式≈: ^{X}m], the SCCEs available for transmission of SPDCCHs are numbered from 0 to ![](media_svg/image632.svg) [公式≈: ^{N}SCCE,m^{−}^{1}] where ![](media_svg/image633.svg) [公式≈: ^{N}SCCE,m^{=}√^{N}OS^{X}^{m}^{N}RB^{X}^{m}^{/}^{N}SREG^{SCCE}∃]. The SCCE number ![](media_svg/image558.svg) [公式: n] corresponds

- SREGs numbered ![](media_svg/image635.svg) [公式≈: n∪N_{SREG}^{SCCE}+j] for localized SPDCCH mapping with CRS and DMRS based demodulation and for distributed SPDCCH mapping with DMRS-based demodulation

- SREGs numbered   ![](media_svg/image636.svg) [公式≈: ^{n}^{mod}^{⋅}⋅_{√}_{N}^{N}_{SREG}SCCE^{RB}^{X}^{m}^{∂}∂_{∃}^{+}^{⋅}^{⋅}^{⋅}_{⋅}_{⋅}_{⋅}_{√}_{⋅}_{⋅}_{√}_{N}_{N}_{SREG}_{SCCE}^{n}_{RB}X_{m}_{∂}_{∂}_{∃}^{∂}^{∂}^{∂}_{∂}_{∂}_{∂}_{∃}^{∪}^{N}RB^{X}^{m}^{+}^{j}^{∪}^{⋅}⋅_{√}_{N}^{N}_{SREG}SCCE^{RB}^{X}^{m}^{∂}∂_{∃}] for distributed SPDCCH mapping with CRS-based demodulation.

where ![](media_svg/image637.svg) [公式≈: j=0,...,N_{SREG}^{SCCE}−1]and ![](media_svg/image638.svg) [公式≈: _{N}_{SREG}SCCE] is the number of SREGs per SCCE.

NOTE:![](media_svg/image639.svg) [公式≈: ^{N}RB^{X}^{m}]represents the number of SREGs per each configured OFDM symbol in the SPDCCH resource set ![](media_svg/image555.svg) [公式≈: ^{X}m] and is the total number of SREGs in SPDCCH resource set .

### 6.8C.2 Scrambling

The block of bits ![](media_svg/image577.svg) [公式: b(0),...,b(M_{bit}−1)] to be transmitted on an SPDCCH in a subframe shall be scrambled, resulting in a block of scrambled bits ![](media_svg/image578.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image579.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the UE-specific scrambling sequence ![](media_svg/image580.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialized with ![](media_svg/image642.svg) [公式≈: ^{c}init^{=}√^{n}s^{2}∃^{∪}^{2}^{9}^{+}^{n}ID^{SPDCCH},m] where ![](media_svg/image582.svg) [公式: m] is the SPDCCH resource set number.

### 6.8C.3 Modulation

The block of scrambled bits![](media_svg/image643.svg) [公式: b^{~}(0),...,b^{~}(M_{tot}−1)] shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols![](media_svg/image644.svg) [公式≈: d(0),...,d(M_{symb}−1)]. Table 6.8C.3-1 specifies the modulation mappings applicable for the physical downlink control channel.

Table 6.8C.3-1: SPDCCH modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| SPDCCH | QPSK |

### 6.8C.4 Layer mapping and precoding

In case of CRS based SPDCCH, layer mapping and precoding shall be done according to clause 6.8.4 with PDCCH replaced by SPDCCH.

In case of DMRS based SPDCCH the layer mapping and precoding shall be done according to clause 6.8A.4.

### 6.8C.5 Mapping to resource elements

The mapping to resource elements is defined by operations on vectors of complex-valued symbols. Let  denotes symbol vector $ i $ and  represents the signal for antenna port.

The block of vectors ![](media_svg/image475.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)...y^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image534.svg) [公式≈: i=0,...,M_{symb}−1] shall be mapped in sequence starting with ![](media_svg/image586.svg) [公式: y(0)] to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on the associated antenna port(s) which meet all of the following criteria:

- they are part of the SREGs assigned for the SPDCCH transmission, and

- they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS36.213 [4], and

- they are assumed by the UE not to be used for transmission of:

- UE-specific reference signal associated with SPDCCH

- zero-power CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

- obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS 36.213 [4], and

- obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

- non-zero-power CSI reference signals for CSI reporting with the configuration for non-zero power CSI reference signals for CSI reporting obtained as described in clause 6.10.5.2.

- The set of indices of ![](media_svg/image389.svg) [公式: l]where the SPDCCH can be mapped to is dependent on if slot or subslot based SPDCCH is used, the subslot number, if CRS or DMRS based SPDCCH is configured and the number of symbols used for PDCCH. In case CRS based SPDCCH is configured, the set of indices is also dependent on the number of symbols, ![](media_svg/image648.svg) [公式≈: _{N}_{CRS}SPDCCH], configured by higher layers (see spdcch-NoOfSymbols in TS 36.331 [9]), that the SPDCCH is mapped over.

- For slot-SPDCCH and for frame structure type 1 and 2, the set of indices of ![](media_svg/image402.svg) [公式: l] for the second slot in the subframe is given in Table 6.8C.5-1. It can be noted that no SPDCCH is transmitted in the first slot of the subframe, where the DCI instead is carried in PDCCH, see [3].

- For subslot-SPDCCH and for frame structure type 1, the set of indices of ![](media_svg/image402.svg) [公式: l] for a given downlink subslot number in a subframe is given in Table 6.8C.5-2. It can be noted that for subslot number 0 where no SPDCCH is transmitted, and the DCI is instead carried in PDCCH, see [3].

If ![](media_svg/image649.svg) [公式: y(i)]has been precoded according to clause 6.3.4.3 and if there is an uneven number of resource elements per PRB that fulfil all the above criteria, ![](media_svg/image649.svg) [公式: y(i)]is not mapped to the resource element of the PRB with largest ![](media_svg/image650.svg) [公式: k].

Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be assumed available in the SPDCCH mapping but not used for transmission of SPDCCH.

NOTE: For DMRS based SPDCCH, the UE is not required to use the PRGs of size 2  (see TS 36.213 [4]) which is/are partially overlapped with PBCH/PSS/SSS for SPDCCH monitoring.

For DMRS based SPDCCH, the mapping to resource elements ![](media_svg/image387.svg) [公式: (k,l)] on antenna port ![](media_svg/image34.svg) [公式: p], meeting the criteria above, shall be in increasing order of first the index ![](media_svg/image388.svg) [公式: k] and then the index ![](media_svg/image389.svg) [公式: l].

For localized and distributed CRS based SPDCCH, the SREGs of a SPDCCH candidate are first interleaved according to step 1 below and then the modulated symbols are mapped to resource elements ![](media_svg/image387.svg) [公式: (k,l)]of the interleaved SREGs according to step 2 below.

- Step 1: Perform a block interleaver on the SREGs building the SPDCCH candidate, where the number of rows equal to the number of SCCEs for the SPDCCH candidate and the number of columns equal to 4 (i.e. the number of SREGs in an SCCE). The SREGs are written into the matrix row by row and read out column by column.

- Step 2: The modulated symbols are mapped in sequence starting with  to resource elements on antenna port  in increasing order of the index k, meeting the criteria above, over the interleaved SREGs in the order given by the block interleaver of step 1.

Table 6.8C.5-1: Set of indices of ![](media_svg/image389.svg) [公式: l] for slot-SPDCCH

| DMRS based SPDCCH | CRS based SPDCCH |  |
| --- | --- | --- |
|  | ![](media_svg/image653.svg) [公式≈: _{N}_{CRS}SPDCCH_{=}_{1}] | ![](media_svg/image654.svg) [公式≈: _{N}_{CRS}SPDCCH_{=}_{2}] |
| ![](media_svg/image655.svg) [公式: {0,1}] | ![](media_svg/image656.svg) [公式: {0}] | ![](media_svg/image657.svg) [公式: {0,1}] |

Table 6.8C.5-2: Set of indices of ![](media_svg/image389.svg) [公式: l] for subslot-SPDCCH

| Number of symbols used for PDCCH | Subslot index | Set of indicies of ![](media_svg/image389.svg) [公式: l] |  |  |
| --- | --- | --- | --- | --- |
|  |  | DMRS based SPDCCH | CRS based SPDCCH |  |
|  |  |  | ![](media_svg/image658.svg) [公式≈: _{N}_{CRS}SPDCCH_{=}_{1}] | ![](media_svg/image659.svg) [公式≈: _{N}_{CRS}SPDCCH_{=}_{2}] |
| 1 or 3 | 1 | ![](media_svg/image660.svg) [公式: {3,4}] | ![](media_svg/image661.svg) [公式: {3}] | ![](media_svg/image660.svg) [公式: {3,4}] |
| 2 | 1 | ![](media_svg/image662.svg) [公式: {2,3,4}] | ![](media_svg/image663.svg) [公式: {2}] | ![](media_svg/image664.svg) [公式: {2,3}] |
| 1, 2 or 3 | 2 | ![](media_svg/image665.svg) [公式: {5,6}] | ![](media_svg/image666.svg) [公式: {5}] | ![](media_svg/image665.svg) [公式: {5,6}] |
| 1, 2 or 3 | 3 | ![](media_svg/image667.svg) [公式: {0,1}] | ![](media_svg/image668.svg) [公式: {0}] | ![](media_svg/image667.svg) [公式: {0,1}] |
| 1, 2 or 3 | 4 | ![](media_svg/image669.svg) [公式: {2,3}] | ![](media_svg/image670.svg) [公式: {2}] | ![](media_svg/image669.svg) [公式: {2,3}] |
| 1, 2 or 3 | 5 | ![](media_svg/image671.svg) [公式: {4,5,6}] | ![](media_svg/image672.svg) [公式: {4}] | ![](media_svg/image673.svg) [公式: {4,5}] |

## 6.9 Physical hybrid ARQ indicator channel

The PHICH carries the hybrid-ARQ ACK/NACK. Multiple PHICHs mapped to the same set of resource elements constitute a PHICH group, where PHICHs within the same PHICH group are separated through different orthogonal sequences. A PHICH resource is identified by the index pair ![](media_svg/image674.svg) [公式≈: ^{(}^{n}PHICH^{group}^{,}^{n}PHICH^{seq}^{)}], where ![](media_svg/image675.svg) [公式≈: _{n}_{PHICH}group] is the PHICH group number and ![](media_svg/image676.svg) [公式≈: ^{n}PHICH^{seq}] is the orthogonal sequence index within the group.

For frame structure type 1 and type 3, the number of PHICH groups ![](media_svg/image677.svg) [公式≈: _{N}_{PHICH}group] is constant in all subframes and given by

![](media_svg/image678.svg) [公式≈: _{N}_{PHICH}group_{=}√⌡_{⌠}_{⌡}_{∞}_{2}⊥N_{∪}_{⊥}g_{N}(N_{g}_{(}RB^{DL}_{N}_{RB}_{DL}8)∀_{8}_{)}_{∀}for _{for }_{extended}normalcyclic_{cyclic}prefix_{prefix}]

where ![](media_svg/image679.svg) [公式: N_{g}⎰{16,12,1,2}] is provided by higher layers. The index ![](media_svg/image680.svg) [公式≈: _{n}_{PHICH}group] ranges from ![](media_svg/image681.svg) [公式: 0] to ![](media_svg/image682.svg) [公式≈: _{N}_{PHICH}group_{−}_{1}].

For frame structure type 2, the number of PHICH groups may vary between subframes and is given by ![](media_svg/image683.svg) [公式≈: ^{m}i^{∪}^{N}PHICH^{group}] where ![](media_svg/image677.svg) [公式≈: _{N}_{PHICH}group] is given by the expression above and ![](media_svg/image684.svg) [公式≈: ^{m}i] is given by Table 6.9-1 with the uplink-downlink configuration provided by the higher-layer parameter subframeAssignment. The index ![](media_svg/image680.svg) [公式≈: _{n}_{PHICH}group] in a subframe with non-zero PHICH resources ranges from ![](media_svg/image681.svg) [公式: 0] to ![](media_svg/image685.svg) [公式≈: ^{m}i^{∪}^{N}PHICH^{group}^{−}^{1}].

Table 6.9-1: The factor ![](media_svg/image684.svg) [公式≈: ^{m}i] for frame structure type 2

| Uplink-downlink configuration | Subframe number ![](media_svg/image112.svg) [公式: i] |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 2 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 6 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |

### 6.9.1 Modulation

The block of bits ![](media_svg/image686.svg) [公式: b(0),...,b(M_{bit}−1)] transmitted on one PHICH in one subframe shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols![](media_svg/image687.svg) [公式: z(0),...,z(M_{s}−1)], where ![](media_svg/image688.svg) [公式≈: ^{M}s^{=}^{M}bit]. Table 6.9.1-1 specifies the modulation mappings applicable for the physical hybrid ARQ indicator channel.

Table 6.9.1-1: PHICH modulation schemes.

| Physical channel | Modulation schemes |
| --- | --- |
| PHICH | BPSK |

The block of modulation symbols ![](media_svg/image687.svg) [公式: z(0),...,z(M_{s}−1)] shall be symbol-wise multiplied with an orthogonal sequence and scrambled, resulting in a sequence of modulation symbols ![](media_svg/image689.svg) [公式≈: d(0),...,d(M_{symb}−1)] according to

![](media_svg/image690.svg) [公式≈: d(i)=w(imodNSF^{PHICH})∪(1−2c(i))∪z(√iNSF^{PHICH}∃)]

where

![](media_svg/image691.svg) [公式≈: ^{N}^{M}^{SF}^{PHICH}^{symb}^{i}^{=}^{=}^{=}^{0}^{√}^{⌠}_{∞}^{N}^{,...,}^{4}2^{SF}^{PHICH}^{M}extended^{normal}^{symb}^{∪}^{M}^{s}^{−}^{cyclic}^{1}cyclic^{prefix}prefix]

and ![](media_svg/image467.svg) [公式: c(i)] is a cell-specific scrambling sequence generated according to clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image692.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{9}+N_{ID}^{cell}] at the start of each subframe.

The sequence ![](media_svg/image693.svg) [公式≈: {w(0)λw(N_{SF}^{PHICH}−1)}] is given by Table 6.9.1-2 where the sequence index ![](media_svg/image676.svg) [公式≈: ^{n}PHICH^{seq}] corresponds to the PHICH number within the PHICH group.

Table 6.9.1-2: Orthogonal sequences ![](media_svg/image694.svg) [公式≈: {w(0)λw(N_{SF}^{PHICH}−1)}] for PHICH

| Sequence index | Orthogonal sequence |  |
| --- | --- | --- |
| ![](media_svg/image676.svg) [公式≈: ^{n}PHICH^{seq}] | Normal cyclic prefix![](media_svg/image695.svg) [公式≈: _{N}_{SF}PHICH_{=}_{4}] | Extended cyclic prefix![](media_svg/image696.svg) [公式≈: _{N}_{SF}PHICH_{=}_{2}] |
| 0 | ![](media_svg/image697.svg) [公式: {+1+1+1+1}] | ![](media_svg/image698.svg) [公式: {+1+1}] |
| 1 | ![](media_svg/image699.svg) [公式: {+1−1+1−1}] | ![](media_svg/image700.svg) [公式: {+1−1}] |
| 2 | ![](media_svg/image701.svg) [公式: {+1+1−1−1}] | ![](media_svg/image702.svg) [公式: {+j+j}] |
| 3 | ![](media_svg/image703.svg) [公式: {+1−1−1+1}] | ![](media_svg/image704.svg) [公式: {+j−j}] |
| 4 | ![](media_svg/image705.svg) [公式: {+j+j+j+j}] | - |
| 5 | ![](media_svg/image706.svg) [公式: {+j−j+j−j}] | - |
| 6 | ![](media_svg/image707.svg) [公式: {+j+j−j−j}] | - |
| 7 | ![](media_svg/image708.svg) [公式: {+j−j−j+j}] | - |

### 6.9.2 Resource group alignment, layer mapping and precoding

The block of symbols ![](media_svg/image473.svg) [公式≈: d(0),...,d(M_{symb}−1)] should be first aligned with resource element group size, resulting in a block of symbols ![](media_svg/image709.svg) [公式≈: d^{(}^{0}^{)}(0),...,d^{(}^{0}^{)}(c∪M_{symb}−1)], where ![](media_svg/image710.svg) [公式: c=1] for normal cyclic prefix; and ![](media_svg/image711.svg) [公式: c=2] for extended cyclic prefix.

For normal cyclic prefix, ![](media_svg/image712.svg) [公式: d^{(}^{0}^{)}(i)=d(i)], for ![](media_svg/image713.svg) [公式≈: i=0,...,M_{symb}−1].

For extended cyclic prefix,

![](media_svg/image714.svg) [公式≈: _{{}_{d}(0)_{(}_{4}_{i}_{)}_{d}(0)_{(}_{4}_{i}_{+}_{1}_{)}_{d}(0)_{(}_{4}_{i}_{+}_{2}_{)}_{d}(0)_{(}_{4}_{i}_{+}_{3}_{)}_{}}T_{=}√⌡_{⌠}_{⌡}_{∞}{_{{}_{0}d(2_{0}i)_{d}d_{(}(_{2}2_{i}i_{)}+1_{d})_{(}_{2}0_{i}_{+}_{1}0_{)}}_{}}^{T}_{T}n_{n}PHICH^{group}_{PHICH}_{group}mod_{mod}2_{2}=_{=}_{1}0]

for ![](media_svg/image715.svg) [公式≈: i=0,...,(M_{symb}2)−1].

The block of symbols ![](media_svg/image709.svg) [公式≈: d^{(}^{0}^{)}(0),...,d^{(}^{0}^{)}(c∪M_{symb}−1)] shall be mapped to layers and precoded, resulting in a block of vectors ![](media_svg/image475.svg) [公式≈: y(i)={y^{(}^{0}^{)}(i)...y^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image716.svg) [公式≈: i=0,...,c∪M_{symb}−1], where ![](media_svg/image212.svg) [公式: y^{(}^{p}^{)}(i)] represents the signal for antenna port ![](media_svg/image34.svg) [公式: p], ![](media_svg/image477.svg) [公式: p=0,...,P−1]and the number of cell-specific reference signals ![](media_svg/image478.svg) [公式: P⎰{1,2,4}]. The layer mapping and precoding operation depends on the cyclic prefix length and the number of antenna ports used for transmission of the PHICH. The PHICH shall be transmitted on the same set of antenna ports as the PBCH.

For transmission on a single antenna port, ![](media_svg/image717.svg) [公式: P=1], layer mapping and precoding are defined by clauses 6.3.3.1 and 6.3.4.1, respectively, with ![](media_svg/image718.svg) [公式≈: ^{M}symb^{(0)}^{=}^{c}^{∪}^{M}symb].

For transmission on two antenna ports, ![](media_svg/image719.svg) [公式: P=2], layer mapping and precoding are defined by clauses 6.3.3.3 and 6.3.4.3, respectively, with ![](media_svg/image718.svg) [公式≈: ^{M}symb^{(0)}^{=}^{c}^{∪}^{M}symb].

For transmission on four antenna ports, ![](media_svg/image720.svg) [公式: P=4], layer mapping is defined by clause 6.3.3.3 with ![](media_svg/image718.svg) [公式≈: ^{M}symb^{(0)}^{=}^{c}^{∪}^{M}symb] and precoding by

![](media_svg/image721.svg) [公式≈: ^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}_{y}^{y}_{y}_{y}_{y}_{y}y^{y}_{y}^{y}^{y}^{y}_{(}^{(}_{(}_{(}_{(}_{(}(^{(}_{(}^{(}^{(}^{(}^{y}^{y}^{y}^{y}1^{0}_{2}_{3}_{1}_{0}_{2}_{3}^{1}^{0}^{2}^{3})_{)}_{)}^{)}_{)}_{)}_{)}^{)}_{)}^{(}^{(}^{)}^{(}^{)}^{)}^{(}(^{1}^{0}^{2}^{3}_{(}_{(}^{(}_{(}_{(}_{(}^{(}_{(}^{(}^{(}^{(}^{)}4^{)}_{4}^{)}^{)}_{4}^{4}_{4}_{4}_{4}^{4}_{4}^{4}^{4}^{4}^{(}^{(}^{(}^{(}i_{i}_{i}^{i}_{i}_{i}_{i}^{i}_{i}^{i}^{i}^{i}^{4}^{4}^{4}^{4}+_{+}_{+}^{+}_{+}_{+}_{+}^{+}_{+}^{+}^{+}^{+}^{i}^{i}^{i}^{i}^{)}^{)}^{)}^{)}^{1}2_{3}^{1}^{1}_{2}_{3}^{1}^{2}_{3}_{2}_{3}^{)}^{)}^{)}_{)}^{)})_{)}_{)}_{)}_{)}^{)}_{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{=}^{1}^{2}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}^{1}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{−}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{1}^{1}_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{−}_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{1}^{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}_{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}^{j}_{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{j}_{j}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{√}^{Re}^{Re}_{Im}^{Im}^{Re}_{Im}^{Re}Im_{(}^{(}^{(}^{(}_{(}^{(}(^{(}_{x}^{x}^{x}^{x}_{x}^{x}x^{x}_{(}^{(}^{(}^{(}_{(}^{(}(^{(}1^{0}^{1}_{2}_{3}^{0}^{2}^{3})^{)}_{)}^{)}^{)}_{)}^{)}^{)}(^{(}_{(}^{(}^{(}_{(}^{(}^{(}i^{i}_{i}^{i}^{i}_{i}^{i}^{i})^{)}_{)}^{)}^{)}_{)}^{)}^{)})^{)}_{)}^{)}^{)}_{)}^{)}^{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∃}]

if ![](media_svg/image722.svg) [公式≈: (i+n_{PHICH}^{group})mod2=0] for normal cyclic prefix, or ![](media_svg/image723.svg) [公式≈: (i+√nPHICH^{group}2∃)mod2=0] for extended cyclic prefix, where ![](media_svg/image675.svg) [公式≈: _{n}_{PHICH}group] is the PHICH group number and ![](media_svg/image724.svg) [公式: i=0,1,2], and by

![](media_svg/image725.svg) [公式≈: ^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}_{y}^{y}_{y}_{y}_{y}_{y}y^{y}_{y}^{y}^{y}^{y}_{(}^{(}_{(}_{(}_{(}_{(}(^{(}_{(}^{(}^{(}^{(}^{y}^{y}^{y}^{y}1^{0}_{2}_{3}_{1}_{0}_{2}_{3}^{1}^{0}^{2}^{3})_{)}_{)}^{)}_{)}_{)}_{)}^{)}_{)}^{(}^{(}^{)}^{(}^{)}^{)}^{(}(^{1}^{0}^{2}^{3}_{(}_{(}^{(}_{(}_{(}_{(}^{(}_{(}^{(}^{(}^{(}^{)}4^{)}_{4}^{)}^{)}_{4}^{4}_{4}_{4}_{4}^{4}_{4}^{4}^{4}^{4}^{(}^{(}^{(}^{(}i_{i}_{i}^{i}_{i}_{i}_{i}^{i}_{i}^{i}^{i}^{i}^{4}^{4}^{4}^{4}+_{+}_{+}^{+}_{+}_{+}_{+}^{+}_{+}^{+}^{+}^{+}^{i}^{i}^{i}^{i}^{)}^{)}^{)}^{)}^{1}2_{3}^{1}^{1}_{2}_{3}^{1}^{2}_{3}_{2}_{3}^{)}^{)}^{)}_{)}^{)})_{)}_{)}_{)}_{)}^{)}_{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{=}^{1}^{2}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{⋅}_{√}^{1}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{−}^{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{1}1_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}_{0}_{0}_{0}_{0}_{0}_{−}_{1}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{1}^{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{0}_{0}^{j}^{j}_{−}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}_{0}_{0}_{0}_{0}_{0}j_{j}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}^{0}0_{0}_{0}_{0}_{0}_{j}_{j}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∂}_{∃}^{⊥}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}^{⋅}⋅_{⋅}_{⋅}_{⋅}_{√}^{Re}^{Re}_{Im}^{Im}^{Re}_{Im}^{Re}Im_{(}^{(}^{(}^{(}_{(}^{(}(^{(}_{x}^{x}^{x}^{x}_{x}^{x}x^{x}_{(}^{(}^{(}^{(}_{(}^{(}(^{(}1^{0}^{1}_{2}_{3}^{0}^{2}^{3})^{)}_{)}^{)}^{)}_{)}^{)}^{)}(^{(}_{(}^{(}^{(}_{(}^{(}^{(}i^{i}_{i}^{i}^{i}_{i}^{i}^{i})^{)}_{)}^{)}^{)}_{)}^{)}^{)})^{)}_{)}^{)}^{)}_{)}^{)}^{)}^{∀}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}^{∂}∂_{∂}_{∂}_{∂}_{∃}]

otherwise for ![](media_svg/image724.svg) [公式: i=0,1,2].

### 6.9.3 Mapping to resource elements

The sequence ![](media_svg/image726.svg) [公式≈: y^{(}^{p}^{)}(0),...,y^{(}^{p}^{)}(M_{symb}^{(0)}−1)] for each of the PHICH groups is defined by

![](media_svg/image727.svg) [公式≈: y^{(}^{p}^{)}(n)=_{⊆}y_{i}^{(}^{p}^{)}(n)]

where the sum is over all PHICHs in the PHICH group and ![](media_svg/image728.svg) [公式≈: y_{i}^{(}^{p}^{)}(n)] represents the symbol sequence from the ![](media_svg/image112.svg) [公式: i]:th PHICH in the PHICH group.

PHICH groups are mapped to PHICH mapping units.

For normal cyclic prefix, the mapping of PHICH group ![](media_svg/image729.svg) [公式: m] to PHICH mapping unit ![](media_svg/image730.svg) [公式: m&apos;]is defined by

![](media_svg/image731.svg) [公式≈: ^{~}y_{m}^{(}^{p}_{&apos;}^{)}(n)=y_{m}^{(}^{p}^{)}(n)]

where

![](media_svg/image732.svg) [公式≈: mmN&apos;0,1,...,1for frame structure type 1 and==−√_{⌠}_{∞}_{0,1,...,1for frame structure type 2}_{mN}_{i}_{∪−}_{PHICH}^{group}_{PHICH}_{group} type 3],

and where ![](media_svg/image684.svg) [公式≈: ^{m}i] is given by Table 6.9-1.

For extended cyclic prefix, the mapping of PHICH group ![](media_svg/image729.svg) [公式: m]and ![](media_svg/image733.svg) [公式: m+1] to PHICH mapping unit ![](media_svg/image734.svg) [公式: m&apos;] is defined by

![](media_svg/image735.svg) [公式≈: ^{~}y_{m}^{(}^{p}_{&apos;}^{)}(n)=y_{m}^{(}^{p}^{)}(n)+y_{m}^{(}^{p}_{+}^{)}_{1}(n)]

where

![](media_svg/image736.svg) [公式: m&apos;=m/2]

![](media_svg/image737.svg) [公式≈: ^{m}^{=}^{√}^{⌡}^{⌠}⌡_{∞}0,2^{0},...,^{,}^{2}^{,...,}m_{i}^{N}∪^{PHICH}N^{group}_{PHICH}^{group}^{−}^{2}−2for ^{for }frame^{frame}structure^{structure} type^{ type}^{1}2]

and where ![](media_svg/image684.svg) [公式≈: ^{m}i] is given by Table 6.9-1.

Let ![](media_svg/image738.svg) [公式≈: z^{(}^{p}^{)}(i)=^{~}y^{(}^{p}^{)}(4i),^{~}y^{(}^{p}^{)}(4i+1),^{~}y^{(}^{p}^{)}(4i+2),^{~}y^{(}^{p}^{)}(4i+3)], ![](media_svg/image739.svg) [公式: i=0,1,2] denote symbol quadruplet ![](media_svg/image112.svg) [公式: i] for antenna port![](media_svg/image514.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}]. Mapping to resource elements is defined in terms of symbol quadruplets according to steps 1–10 below:

1) For each value of ![](media_svg/image740.svg) [公式: l^{±}]

2) Let ![](media_svg/image741.svg) [公式≈: ^{n}l±] denote the number of resource element groups not assigned to PCFICH in OFDM symbol ![](media_svg/image740.svg) [公式: l^{±}]

3) Number the resource-element groups not assigned to PCFICH in OFDM symbol ![](media_svg/image740.svg) [公式: l^{±}] from 0 to![](media_svg/image742.svg) [公式: n_{l}_{±}−1], starting from the resource-element group with the lowest frequency-domain index.

4) Initialize ![](media_svg/image542.svg) [公式: m±=0] (PHICH mapping unit number)

5) For each value of ![](media_svg/image739.svg) [公式: i=0,1,2]

6) Symbol-quadruplet ![](media_svg/image743.svg) [公式: z^{(}^{p}^{)}(i)] from PHICH mapping unit ![](media_svg/image744.svg) [公式: m&apos;] is mapped to the resource-element group represented by ![](media_svg/image745.svg) [公式: (k±,l±)_{i}] as defined in clause 6.2.4 where the indices ![](media_svg/image746.svg) [公式≈: ^{k}i^{±}] and ![](media_svg/image747.svg) [公式≈: ^{l}i^{±}] are given by steps 7 and 8 below:

7) The time-domain index ![](media_svg/image747.svg) [公式≈: ^{l}i^{±}] is given by

![](media_svg/image748.svg) [公式≈: ^{l}^{i}^{±}^{=}^{√}^{⌡}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}_{⌡}_{∞}_{i}^{(}^{(}^{(}^{0}^{√}^{√}^{√}^{m}^{m}^{m}^{±}^{±}^{±}^{2}^{2}^{2}^{∃}^{∃}^{∃}^{+}^{+}^{+}^{i}^{i}^{i}^{+}^{+}^{+}^{1}^{1}^{1}^{)}^{)}^{)}^{mod}^{mod}^{mod}^{2}^{2}^{2}subframe^{extended}^{extended}^{extended}_{otherwise}^{normal}^{PHICH} with the^{PHICH}^{PHICH}^{PHICH}^{duration,}^{duration,}^{duration,}^{duration,}sameduration ^{all}^{subframe}^{MBSFN}^{subframes}as the^{subframes}^{1}^{and}DwPTS^{6}^{in }^{frame}duration ^{structure}ofaspecifial^{ type}^{2}subframeconfiguration in framestructure type3]

8) Set the frequency-domain index ![](media_svg/image749.svg) [公式≈: ^{k}i^{±}] to the resource-element group assigned the number ![](media_svg/image750.svg) [公式≈: ^{n}i] in step 3 above, where ![](media_svg/image750.svg) [公式≈: ^{n}i] is given by

![](media_svg/image751.svg) [公式≈: ni=^{√}^{⌡}^{⌡}⌠_{⌡}_{⌡}_{∞}^{(}(_{(}^{√}√_{√}^{N}N_{N}^{ID}ID_{ID}^{cell}^{cell}_{cell}^{∪}∪_{∪}^{n}n_{n}^{l}l_{l}^{i}_{i}_{i}^{±}±_{±}^{n}n_{n}^{1}1_{1}^{∃}∃_{∃}^{+}+_{+}^{m}m_{m}^{&apos;}&apos;_{&apos;}+_{+}^{)}^{mod}√_{√}n_{2}l_{n}_{i}±_{l}_{i}_{±}^{n}3^{l}∃^{i}^{±}_{3})_{∃}mod_{)}_{mod}nl_{n}_{i}±_{l}_{i}_{±}^{i}i_{i}^{=}=_{=}1^{0}_{2}]

in case of extended PHICH duration in MBSFN subframes, or extended PHICH duration in subframes 1 and 6 for frame structure type 2, or extended PHICH duration in subframe with the same duration as the DwPTS duration of a special subframe configuration in frame structure type 3 and by

![](media_svg/image752.svg) [公式≈: ni=^{√}^{⌡}^{⌡}⌠_{⌡}_{⌡}_{∞}^{(}(_{(}^{√}√_{√}^{N}N_{N}^{ID}ID_{ID}^{cell}^{cell}_{cell}^{∪}∪_{∪}^{n}n_{n}^{l}l_{l}^{i}_{i}_{i}^{±}±_{±}^{n}n_{n}^{0}0_{0}^{∃}∃_{∃}^{+}+_{+}^{m}m_{m}^{&apos;}&apos;_{&apos;}+_{+}^{)}^{mod}√_{√}n_{2}l_{n}_{i}±_{l}_{i}_{±}^{n}3^{l}∃^{i}^{±}_{3})_{∃}mod_{)}_{mod}nl_{n}_{i}±_{l}_{i}_{±}^{i}i_{i}^{=}=_{=}1^{0}_{2}]

otherwise.

9) Increase ![](media_svg/image548.svg) [公式: m^{±}] by 1.

10) Repeat from step 5 until all PHICH mapping units have been assigned.

The PHICH duration is configurable by higher layers according to Table 6.9.3-1.

The PHICH shall not be transmitted in MBSFN subframes with zero-size non-MBSFN region.

Table 6.9.3-1: PHICH duration in MBSFN and non-MBSFN subframes

| PHICH duration | Non-MBSFN subframes |  |  | MBSFN subframes |
| --- | --- | --- | --- | --- |
|  | Subframes 1 and 6 in case of frame structure type 2 | Subframe with the same duration as the DwPTS duration of a specifial subframe configuration in case of frame structure type 3 | All other cases |  |
| Normal | 1 | 1 | 1 | 1 |
| Extended | 2 | 2 | 3 | 2 |

## 6.10 Reference signals

Six types of downlink reference signals are defined:

- Cell-specific Reference Signal (CRS)

- MBSFN reference signal

- UE-specific Reference Signal (DM-RS) associated with PDSCH

- DeModulation Reference Signal (DM-RS) associated with EPDCCH or MPDCCH

- Positioning Reference Signal (PRS)

- CSI Reference Signal (CSI-RS)

There is one reference signal transmitted per downlink antenna port.

### 6.10.1 Cell-specific Reference Signal (CRS)

The UE may assume cell-specific reference signals are, unless otherwise stated in [4, clause 12], transmitted in

- all downlink subframes for frame structure type 1,

- all downlink subframes and DwPTS for frame structure type 2,

- non-empty subframes for frame structure type 3

in a cell supporting PDSCH transmission.

If special subframe configuration 10 is configured by the higher layer signalling ssp10-CRS-LessDwPTS, the UE cannot assume that cell specific reference signals are transmitted in the 5th OFDM symbol of the special subframe.

Cell-specific reference signals are transmitted on one or several of antenna ports 0 to 3.

Cell-specific reference signals are transmitted in subframes where ![](media_svg/image48.svg) [公式: δf=15kHz] only.

#### 6.10.1.1 Sequence generation

The reference-signal sequence ![](media_svg/image753.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] is defined by

![](media_svg/image754.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,2N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image755.svg) [公式≈: ^{n}s] is the slot number within a radio frame and ![](media_svg/image92.svg) [公式: l] is the OFDM symbol number within the slot. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image756.svg) [公式≈: c_{init}=2^{10}∪(7∪(n_{s}±+1)+l+1)∪(2∪N_{ID}^{cell}+1)+2∪N_{ID}^{cell}+N_{CP}] at the start of each OFDM symbol where

![](media_svg/image757.svg) [公式≈: _{N}_{CP}_{n}_{s}_{±}_{=}_{=}√_{⌠}_{∞}_{√}_{⌠}_{∞}10_{1}_{0}_{n}_{s}√n_{for }_{for }s10_{extended}_{normal}∃+ns_{CP}mod_{CP}2for _{otherwise}framestructure type3 when theCRSispart ofaDRS]

#### 6.10.1.2 Mapping to resource elements

The reference signal sequence ![](media_svg/image753.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference symbols for antenna port ![](media_svg/image34.svg) [公式: p] in slot ![](media_svg/image755.svg) [公式≈: ^{n}s] according to

![](media_svg/image758.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image759.svg) [公式≈: _{m}_{m}^{k}_{l}_{±}^{=}_{=}_{=}_{=}^{6}_{0}√⌡_{⌠}_{⌡}_{∞}_{m}_{1}_{,}0^{m}_{1}_{+},_{,...,}N^{+}_{N}^{(}_{symb}^{DL}_{2}^{v}_{RB}_{max,}_{∪}^{+}_{N}^{v}−_{DL}_{RB}_{DL}^{shift}3_{−}_{−}^{)}_{N}if_{if}_{1}^{mod}_{RB}_{DL}p_{p}⎰_{⎰}^{6}{_{{}0_{2},_{,}1_{3}}_{}}]

The variables ![](media_svg/image760.svg) [公式: v] and ![](media_svg/image761.svg) [公式≈: ^{v}shift] define the position in the frequency domain for the different reference signals where ![](media_svg/image760.svg) [公式: v] is given by

![](media_svg/image762.svg) [公式≈: ^{v}^{=}^{√}^{⌡}^{⌡}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}^{⌡}⌡_{∞}^{3}^{3}^{3}3^{0}^{0}^{(}+^{n}^{s}3(^{mod}n_{s}mod^{2}^{)}2)^{if}^{if}^{if}^{if}^{if}if^{p}^{p}^{p}^{p}^{p}p^{=}^{=}^{=}^{=}^{=}=^{1}^{1}3^{0}^{0}^{2}^{and}^{and}^{and}^{and}^{l}^{l}^{l}^{l}^{=}^{⎯}^{=}^{⎯}^{0}^{0}^{0}^{0}]

The cell-specific frequency shift is given by ![](media_svg/image763.svg) [公式≈: v_{shift}=N_{ID}^{cell}mod6].

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of cell-specific reference signals on any of the antenna ports in a slot shall not be used for any transmission on any other antenna port in the same slot and set to zero.

In an MBSFN subframe, cell-specific reference signals shall only be transmitted in the non-MBSFN region of the MBSFN subframe.

Figures 6.10.1.2-1 and 6.10.1.2-2 illustrate the resource elements used for reference signal transmission according to the above definition. The notation ![](media_svg/image765.svg) [公式≈: ^{R}p] is used to denote a resource element used for reference signal transmission on antenna port![](media_svg/image34.svg) [公式: p].


![](media/image766.emf)

Figure 6.10.1.2-1. Mapping of downlink reference signals (normal cyclic prefix)

![](media/image767.emf)

Figure 6.10.1.2-2. Mapping of downlink reference signals (extended cyclic prefix)

### 6.10.2 MBSFN reference signals

MBSFN reference signals shall be transmitted in the MBSFN region of MBSFN subframes/slots only when the PMCH is transmitted. MBSFN reference signals are transmitted on antenna port 4.

For an MBMS-dedicated carrier configured with a single MBSFN area, and for a PMCH transmitted with 0.37 kHz subcarrier spacing in slot $ n $, which is indicated to contain MCCH by higher layer parameter MCCH-Config:

- for MBSFN reference signal pattern type 1, the UE may assume that MBSFN reference signals associated with the same $ N_{ID}^{MBSFN}$ are present in the three preceding slots to slot $ n $.

- for MBSFN reference signal pattern type 2, the UE may assume that MBSFN reference signals associated with the same $ N_{ID}^{MBSFN}$ are present in the preceding slot to slot $ n $.

MBSFN reference signals are defined for extended cyclic prefix only.

#### 6.10.2.1 Sequence generation

##### 6.10.2.1.1 Sequence generation for 15 kHz and 7.5 kHz subcarrier spacing

The MBSFN reference-signal sequence ![](media_svg/image753.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] is defined by

![](media_svg/image768.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,6N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image755.svg) [公式≈: ^{n}s] is the slot number within a radio frame and ![](media_svg/image92.svg) [公式: l] is the OFDM symbol number within the slot. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image769.svg) [公式≈: c_{init}=2^{9}∪(7∪(n_{s}+1)+l+1)∪(2∪N_{ID}^{MBSFN}+1)+N_{ID}^{MBSFN}] at the start of each OFDM symbol.

##### 6.10.2.1.2 Sequence generation for 1.25 kHz subcarrier spacing

The MBSFN reference-signal sequence ![](media_svg/image770.svg) [公式≈: r_{l}_{,}_{n}_{sf}(m)] is defined by

![](media_svg/image771.svg) [公式≈: r_{l}_{,}_{n}_{sf}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,24N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image772.svg) [公式≈: ^{n}sf] is the subframe number within a radio frame and ![](media_svg/image92.svg) [公式: l] is the OFDM symbol number within the subframe. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image773.svg) [公式≈: c_{init}=2^{9}∪(7∪(n_{sf}+1)+l+1)∪(2∪N_{ID}^{MBSFN}+1)+N_{ID}^{MBSFN}] at the start of each OFDM symbol.

##### 6.10.2.1.3 Sequence generation for 2.5 kHz subcarrier spacing

The MBSFN reference-signal sequence $ r_{l,n_{sf}}\left ( m\right ) $ is defined by

$$ r_{l,n_{sf}}\left ( m\right ) =\frac {1}{\sqrt {2}}\left ( 1-2c\left ( 2m\right ) \right ) +j\frac {1}{\sqrt {2}}\left ( 1-2c\left ( 2m+1\right ) \right ) $$

$$ m=0,1,\ldots  ,18N_{RB}^{max,DL}-1 $$

where $ n_{sf}$ is the subframe number within a radio frame and $ l $ is the OFDM symbol number within the subframe. The pseudo-random sequence $ c\left ( i\right ) $ is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

$$ c_{init}=2^{9}\left ( 7\left ( n_{sf}+1\right ) +l+1\right ) \left ( 2N_{ID}^{MBSFN}+1\right ) +N_{ID}^{MBSFN}$$

##### 6.10.2.1.4 Sequence generation for 0.37 kHz subcarrier spacing

The MBSFN reference-signal sequence $ r_{l,n_{s}}\left ( m\right ) $ is defined by

$$ r_{l,n_{s}}\left ( m\right ) =\frac {1}{\sqrt {2}}\left ( 1-2c\left ( 2m\right ) \right ) +j\frac {1}{\sqrt {2}}\left ( 1-2c\left ( 2m+1\right ) \right ) $$

$$\begin {matrix}m=0,1,\ldots  ,\frac {N_{sc}^{RB}}{12}N_{RB}^{max,DL}-1 & for MBSFN reference signal pattern type 1 \\ m=0,1,\ldots  ,\frac {N_{sc}^{RB}}{6}N_{RB}^{max,DL}-1 & for MBSFN reference signal pattern type 2\end {matrix}$$

where $ n_{s}$ is the 3 ms slot number within the 40 ms period and $ l $ is the OFDM symbol number within the slot. The pseudo-random sequence $ c\left ( i\right ) $ is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

$$ c_{init}=2^{9}\left ( 7\left ( n_{s}+1\right ) +l+1\right ) \left ( 2N_{ID}^{MBSFN}+1\right ) +N_{ID}^{MBSFN}$$

#### 6.10.2.2 Mapping to resource elements

##### 6.10.2.2.1 Mapping to resource elements for 15 kHz and 7.5 kHz subcarrier spacing

The reference-signal sequence ![](media_svg/image774.svg) [公式≈: r_{l}_{,}_{n}_{s}(m±)] in OFDM symbol ![](media_svg/image92.svg) [公式: l] shall be mapped to complex-valued modulation symbols ![](media_svg/image775.svg) [公式≈: _{a}_{k}(_{,}p_{l})] with ![](media_svg/image776.svg) [公式: p=4] according to

![](media_svg/image777.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m±)]

where

![](media_svg/image778.svg) [公式≈: _{l}^{k}_{m}_{m}_{=}_{±}^{=}_{=}_{=}^{√}^{⌡}⌡_{⌠}_{⌡}_{⌡}_{∞}^{√}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}^{∞}_{1}_{0}0_{0}^{2}_{m}^{2}^{2}^{4}^{4}_{,},_{,}_{1}^{m}^{m}^{m}^{m}4_{2}_{,...,}_{+}^{+}^{+}_{3}^{if}if_{if}_{if}_{6}_{(}^{1}^{2}_{N}_{N}^{n}n_{n}_{n}_{RB}_{max,}_{RB}^{s}s_{s}_{s}_{DL}^{if}^{if}^{if}^{if}^{mod}mod_{mod}_{mod}^{l}^{l}^{l}^{l}_{DL}_{−}^{⎯}^{=}^{⎯}^{=}_{1}_{−}^{2}2_{2}_{2}^{0}^{0}^{0}^{0}^{and}^{and}^{and}^{and}_{N}^{=}=_{=}_{=}1_{1}_{RB}^{0}_{0}_{DL}and_{and}^{and}_{and}^{δ}^{δ}^{δ}^{δ}_{)}^{f}^{f}^{f}^{f}δ_{δ}^{=}^{=}^{=}^{=}^{δ}_{δ}f_{f}^{15}^{15}^{f}_{f}^{7}^{7}^{.}^{.}=_{=}^{=}_{=}^{5}^{5}^{kHz}^{kHz}15_{7}^{15}^{kHz}^{kHz}_{7}_{.}_{.}_{5}_{5}kHz^{kHz}_{kHz}_{kHz}]

Figure 6.10.2.2-1 illustrates the resource elements used for MBSFN reference signal transmission in case of ![](media_svg/image779.svg) [公式: δf=15kHz]. In case of ![](media_svg/image780.svg) [公式: δf=7.5kHz], the MBSFN reference signal shall be mapped to resource elements according to Figure 6.10.2.2-3. The notation ![](media_svg/image765.svg) [公式≈: ^{R}p] is used to denote a resource element used for reference signal transmission on antenna port![](media_svg/image34.svg) [公式: p].

![](media/image781.emf)

Figure 6.10.2.2-1: Mapping of MBSFN reference signals (extended cyclic prefix, ![](media_svg/image779.svg) [公式: δf=15kHz])



![](media/image782.emf)

Figure 6.10.2.2-3: Mapping of MBSFN reference signals (extended cyclic prefix, ![](media_svg/image783.svg) [公式: δf=7.5kHz])

##### 6.10.2.2.2 Mapping to resource elements for 1.25 kHz

The reference-signal sequence ![](media_svg/image784.svg) [公式≈: r_{l}_{,}_{n}_{sf}(m±)] in OFDM symbol ![](media_svg/image92.svg) [公式: l] shall be mapped to complex-valued modulation symbols ![](media_svg/image775.svg) [公式≈: _{a}_{k}(_{,}p_{l})] with ![](media_svg/image776.svg) [公式: p=4] according to

![](media_svg/image785.svg) [公式≈: ^{a}k^{(},^{p}l^{)}^{=}^{r}l,nsf^{(}^{m}^{±}^{)}]

where

![](media_svg/image786.svg) [公式≈: ^{l}^{k}m_{m}^{=}_{±}^{=}=_{=}^{0}^{√}^{⌠}^{∞}0_{m}^{6}^{6},1^{m}^{m},...,_{+}^{+}_{3}24_{(}^{3}_{N}N_{RB}_{max,}^{if}^{if}_{RB}^{DL}^{n}^{n}_{DL}^{sf}^{sf}−1_{−}^{mod}^{mod}_{N}_{RB}_{DL}^{2}^{2}^{=}^{=}_{)}^{1}^{0}]

##### 6.10.2.2.3 Mapping to resource elements for 2.5 kHz subcarrier spacing

The reference-signal sequence $ r_{l,n_{sf}}\left ( m'\right ) $ in OFDM symbol $ l $ shall be mapped to complex-valued modulation symbols $ a_{k,l}^{(p)}$ with $ p=4 $ according to

$$ a_{k,l}^{(p)}=r_{l,n_{sf}}\left ( m'\right ) $$

where

$$ k={\begin {matrix}4m & ifl=0 \\ 4m+2 & ifl=1\end {matrix}l=0,1m=0,1,\ldots  ,\frac {N_{sc}^{RB}}{4}N_{RB}^{DL}-1m^{'}=m+\frac {N_{sc}^{RB}}{4}\Delta  \Delta  =\frac {N_{RB}^{max,DL}-N_{RB}^{DL}}{2}$$

##### 6.10.2.2.4 Mapping to resource elements for 0.37 kHz subcarrier spacing


The reference-signal sequence $ r_{l}\left ( m'\right ) $ in OFDM symbol $ l $ shall be mapped to complex-valued modulation symbols $ a_{k,l}^{(p)}$ with $ p=4 $ according to

$$ a_{k,l}^{(p)}=r_{l,n_{s}}\left ( m'\right ) $$


when

$$ 0\leq  k<N_{sc}^{RB}N_{RB}^{DL}$$

and where  $\hat {n}_{s}$ is the 3ms absolute slot number, defined as $\hat {n}_{s}=$ $ n_{s}+13\lfloor  n_{f}/4\rfloor  ,$ $ n_{s}$ is the 3 ms slot number as defined in clause 4.1 and

- for MBSFN reference signal pattern type 1

$$ k=12\left ( m^{'}-\lfloor  \frac {N_{sc}^{RB}}{12}\Delta  \rfloor  \right ) +3\left ( \hat {n}_{s}mod4\right ) l=0\Delta  =\frac {N_{RB}^{max,DL}-N_{RB}^{DL}}{2}m^{'}=0,1,\ldots  ,\frac {N_{sc}^{RB}}{12}N_{RB}^{max,DL}-1 $$

- for MBSFN reference signal pattern type 2

$$ k=6\left ( m^{'}-\lfloor  \frac {N_{sc}^{RB}}{6}\Delta  \rfloor  \right ) +3\left ( \hat {n}_{s}mod2\right ) l=0\Delta  =\frac {N_{RB}^{max,DL}-N_{RB}^{DL}}{2}m^{'}=0,1,\ldots  ,\frac {N_{sc}^{RB}}{6}N_{RB}^{max,DL}-1 $$

### 6.10.3 UE-specific reference signals associated with PDSCH

UE-specific reference signals associated with PDSCH

- are transmitted on antenna port(s) ![](media_svg/image787.svg) [公式: p=5], ![](media_svg/image788.svg) [公式: p=7], ![](media_svg/image789.svg) [公式: p=8], ![](media_svg/image790.svg) [公式: p=11] ,![](media_svg/image791.svg) [公式: p=13], ![](media_svg/image792.svg) [公式: p={11,13}], ![](media_svg/image382.svg) [公式: p=7,8,...,Υ+6],  or on the antenna ports indicated in Table 6.3.4.4-1, where ![](media_svg/image162.svg) [公式: Υ] is the number of layers used for transmission of the PDSCH;

- are present and are a valid reference for PDSCH demodulation only if the PDSCH transmission is associated with the corresponding antenna port according to clause 7.1 of TS36.213 [4];

- are transmitted only on the physical resource blocks upon which the corresponding PDSCH is mapped.

A UE-specific reference signal associated with PDSCH is not transmitted in resource elements ![](media_svg/image35.svg) [公式: (k,l)] in which one of the physical channels or physical signals other than the UE-specific reference signals defined in 6.1 are transmitted using resource elements with the same index pair ![](media_svg/image35.svg) [公式: (k,l)] regardless of their antenna port ![](media_svg/image34.svg) [公式: p].

A UE-specific reference signal associated with subslot-PDSCH or slot-PDSCH is only transmitted in physical resource blocks in frequency domain assigned for PDSCH transmission where

- the assignment maps to both physical resource blocks of a given PRG (see clause 6.4.2);

- in case of subslot-PDSCH, the associated SPDCCH is not mapped to resource elements of a given PRG assigned for PDSCH transmission (see clause 6.4.2)..

For frame structure type 3, for PDSCH in a subframe with the same duration as the DwPTS duration of a special subframe configuration, the UE-specific reference signals are defined the same as that for the corresponding special subframe configuration.

#### 6.10.3.1 Sequence generation

For antenna port 5, the UE-specific reference-signal sequence ![](media_svg/image793.svg) [公式: r_{n}_{s}(m)] is defined by

![](media_svg/image794.svg) [公式≈: r_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,12N_{RB}^{PDSCH}−1]

where ![](media_svg/image795.svg) [公式≈: _{N}_{RB}PDSCH] denotes the assigned bandwidth in resource blocks of the corresponding PDSCH transmission. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image796.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{RNTI}] at the start of each subframe where ![](media_svg/image797.svg) [公式≈: ^{n}RNTI] is as described in clause 7.1 TS36.213[4].

For any of the antenna ports ![](media_svg/image798.svg) [公式: p⎰{7,8,...,14}], the reference-signal sequence ![](media_svg/image799.svg) [公式: r(m)] is defined by

![](media_svg/image800.svg) [公式≈: ^{r}^{(}^{m}^{)}^{=}^{1}2^{(}^{1}^{−}^{2}^{∪}^{c}^{(}^{2}^{m}^{)}^{)}^{+}^{j}^{1}2^{(}^{1}^{−}^{2}^{∪}^{c}^{(}^{2}^{m}^{+}^{1}^{)}^{)}^{,}^{m}^{=}^{√}^{⌡}^{⌠}⌡_{∞}^{0}0^{,},^{1}1^{,...,},...,^{12}16^{N}N^{RB}_{RB}^{max,}^{max,}^{DL}^{DL}^{−}−^{1}1extended^{normal}^{cyclic}cyclic^{prefix}prefix].

The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

![](media_svg/image801.svg) [公式≈: c_{init}=(_{√}n_{s}/2_{∃}+1)∪(2n_{ID}^{(}^{n}^{SCID}^{)}+1)∪2^{16}+n_{SCID}]

at the start of each subframe.

For BL/CE UEs, the same scrambling sequence is applied per subframe to the UE-specific reference-signal sequence for a given block of ![](media_svg/image802.svg) [公式≈: ^{N}acc] subframes. The subframe number of the first subframe in each block of ![](media_svg/image147.svg) [公式≈: ^{N}acc] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image149.svg) [公式≈: (^{niN}abs,1acc^{+=}δ)^{mod0}]. For the ![](media_svg/image803.svg) [公式≈: _{j}th]block of ![](media_svg/image802.svg) [公式≈: ^{N}acc] subframes, the scrambling sequence generator shall be initialised with

![](media_svg/image804.svg) [公式≈: c_{init}=({(j_{0}+j)N_{acc}mod10}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{SCID}]

where

![](media_svg/image805.svg) [公式≈: ^{i}^{j}^{j}^{δ}^{0}^{=}^{=}^{=}^{0}^{√}^{⌠}_{∞}^{√}^{,}^{1}^{(}^{0,}N^{,...,}^{i}^{0}_{acc}^{+}^{⋅}^{⋅}^{√}^{i}−^{i}^{δ}^{0}2^{)}^{+},^{N}^{N}^{acc}^{for }for ^{abs}^{PDSCH}^{N}^{∃}^{frame}frame^{acc}^{+}^{i}^{δ}^{structure}structure^{−}^{1}^{∂}^{∂}^{∃}^{−}^{j}^{ type} type^{0}^{1}2^{or  }and^{N}N^{acc}_{acc}^{=}=^{1}10]

and ![](media_svg/image153.svg) [公式≈: ^{i}0] is the absolute subframe number of the first downlink subframe intended for PDSCH. The PDSCH transmissions span ![](media_svg/image154.svg) [公式≈: _{N}_{abs}PDSCH] consecutive subframes, including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed. For a BL/CE UE configured in CEModeA, ![](media_svg/image155.svg) [公式: N_{acc}=1]. For a BL/CE UE configured with CEModeB, ![](media_svg/image156.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image157.svg) [公式: N_{acc}=10] for frame structure type 2.

The quantities ![](media_svg/image806.svg) [公式≈: _{n}_{ID}(i)], ![](media_svg/image807.svg) [公式: i=0,1], are given by

- ![](media_svg/image808.svg) [公式≈: _{n}_{ID}(i)_{=}_{N}_{ID}cell] if no value for ![](media_svg/image809.svg) [公式≈: _{n}_{ID}DMRS,i] is provided by higher layers or if DCI format 1A, 2B or 2C is used for the DCI associated with the PDSCH transmission

- ![](media_svg/image810.svg) [公式≈: _{n}_{ID}(i)_{=}_{n}_{ID}DMRS,i] otherwise

The value of ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is zero unless specified otherwise. For a PDSCH transmission on ports 7 or 8, ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is given by the DCI format 2B, 2C, 2D, 6-1A, 7-1E, 7-1F and 7-1G  in TS 36.212 [3] associated with the PDSCH transmission. 
In the case of DCI format 2B or 7-1E, ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is indicated by the scrambling identity field according to Table 6.10.3.1-1. In the case of DCI format 2C or 2D, ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is given by Table 5.3.3.1.5C-1, Table 5.3.3.1.5C-2 or Table 5.3.3.1.5C-6 in TS36.212 [3]. In the case of DCI format 7-1F or 7-1G, ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is given by Table 5.3.3.1.22-1, Table  5.3.3.1.22-2, Table 5.3.3.1.22-3 or Table 5.3.3.1.5C-6 in TS36.212 [3].  For a PDSCH transmission on ports 11 or 13, ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is given by the DCI format 2C or 2D in TS36.212 [3] associated with the PDSCH transmission where ![](media_svg/image811.svg) [公式≈: ^{n}SCID] is given by Table 5.3.3.1.5C-2 in TS36.212 [3].

Table 6.10.3.1-1: Mapping of scrambling identity field in DCI format 2B to ![](media_svg/image812.svg) [公式≈: ^{n}SCID]values for antenna ports 7 and 8

| Scrambling identity field in DCI format 2B (TS36.212 [3]) | ![](media_svg/image813.svg) [公式≈: ^{n}SCID] |
| --- | --- |
| 0 | 0 |
| 1 | 1 |

#### 6.10.3.2 Mapping to resource elements

For antenna port 5, in a physical resource block with frequency-domain index ![](media_svg/image814.svg) [公式≈: ^{n}PRB] assigned for the corresponding PDSCH transmission, the reference signal sequence ![](media_svg/image815.svg) [公式: r_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] with ![](media_svg/image816.svg) [公式: p=5] in a subframe according to:

Normal cyclic prefix:

![](media_svg/image817.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{n}_{s}(3∪l±∪N_{RB}^{PDSCH}+m&apos;)]

![](media_svg/image818.svg) [公式≈: _{m}^{k}_{l}^{k}_{l}^{±}_{±}_{&apos;}^{=}^{=}_{=}_{=}_{=}^{(}_{0}^{√}^{⌠}_{∞}_{√}_{⌡}_{⌡}_{⌠}_{⌡}_{⌡}_{∞}_{√}_{⌠}_{∞}^{k}_{,}_{6}_{5}4m&apos;_{3}_{2}_{2,3}_{0}_{1}^{±}_{,...,}_{,}^{)}^{4}_{1}^{mod}^{m}_{l}_{l}+_{l}_{l}_{±}_{±}_{3}_{±}_{±}^{&apos;}(^{+}_{if}_{if}_{=}_{=}_{=}_{N}_{=}2^{v}_{1}_{0}_{2}_{3}+^{N}_{RB}_{n}^{shift}_{PDSCH}_{n}_{s}_{s}v^{sc}^{RB}_{mod}_{mod}_{shift}^{+})_{−}^{N}_{2}mod_{2}_{1}^{sc}^{RB}_{=}_{=}_{1}_{0}^{∪}4^{n}^{PRB}^{if}if^{l}l^{⎰}⎰^{{}{5^{2},^{,}6^{3}^{}}}]

Extended cyclic prefix:

![](media_svg/image819.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{n}_{s}(4∪l±∪N_{RB}^{PDSCH}+m&apos;)]

![](media_svg/image820.svg) [公式≈: _{m}^{k}_{l}^{k}_{l}^{±}_{±}_{&apos;}^{=}^{=}_{=}_{=}_{=}^{(}_{0}^{√}^{⌠}_{∞}_{√}_{⌠}_{∞}_{√}_{⌠}_{∞}^{k}_{1,2}3m&apos;_{,}_{1}_{4}_{1}_{0}^{±}_{,...,}^{)}^{3}^{mod}^{m}+_{l}_{±}_{4}^{&apos;}(^{+}_{if}_{⎰}_{if}_{l}2_{N}_{±}^{v}_{{}_{n}+_{=}^{shift}^{N}_{n}_{RB}_{PDSCH}_{0}_{s}_{s}_{1}v^{sc}_{,}^{RB}_{mod}_{2}_{mod}_{shift}_{}}^{+})_{−}^{N}_{2}_{2}mod_{1}^{sc}_{=}^{RB}_{=}_{1}_{0}^{∪}3^{n}^{PRB}^{if}if^{l}l^{=}=1^{4}]

where ![](media_svg/image821.svg) [公式: m&apos;] is the counter of UE-specific reference signal resource elements within a respective OFDM symbol of the PDSCH transmission.

The cell-specific frequency shift is given by ![](media_svg/image822.svg) [公式≈: v_{shift}=N_{ID}^{cell}mod3].

The mapping shall be in increasing order of the frequency-domain index ![](media_svg/image814.svg) [公式≈: ^{n}PRB] of the physical resource blocks assigned for the corresponding PDSCH transmission. The quantity ![](media_svg/image795.svg) [公式≈: _{N}_{RB}PDSCH] denotes the assigned bandwidth in resource blocks of the corresponding PDSCH transmission.

Figure 6.10.3.2-1 illustrates the resource elements used for UE-specific reference signals for normal cyclic prefix for antenna port 5.

Figure 6.10.3.2-2 illustrates the resource elements used for UE-specific reference signals for extended cyclic prefix for antenna port 5.

The notation ![](media_svg/image765.svg) [公式≈: ^{R}p] is used to denote a resource element used for reference signal transmission on antenna port![](media_svg/image34.svg) [公式: p].

![](media/image823.emf)

Figure 6.10.3.2-1: Mapping of UE-specific reference signals, antenna port 5 (normal cyclic prefix)

![](media/image824.emf)

Figure 6.10.3.2-2: Mapping of UE-specific reference signals, antenna port 5 (extended cyclic prefix)

For antenna ports ![](media_svg/image825.svg) [公式: p=7], ![](media_svg/image826.svg) [公式: p=8], ![](media_svg/image827.svg) [公式: p=11], ![](media_svg/image828.svg) [公式: p=13], ![](media_svg/image829.svg) [公式: p={11,13}], ![](media_svg/image830.svg) [公式: p=7,8,κ,Υ+6], or  the antenna ports indicated in Table 6.3.4.4-1 in a physical resource block with frequency-domain index ![](media_svg/image814.svg) [公式≈: ^{n}PRB] assigned for the corresponding PDSCH transmission, a part of the reference signal sequence ![](media_svg/image831.svg) [公式: r(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] in a subframe according to

Normal cyclic prefix:

![](media_svg/image832.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;)∪r(3∪l&apos;∪N_{RB}^{max,}^{DL}+3∪n_{PRB}+m&apos;)]

where

![](media_svg/image833.svg) [公式≈: ^{w}^{p}^{(}_{m}^{i}^{k}^{k}^{)}l_{l}^{&apos;}_{&apos;}_{&apos;}^{=}^{=}^{=}=_{=}_{=}^{5}_{0}^{√}^{⌠}^{∞}^{√}^{⌠}^{∞}^{√}^{⌡}_{⌠}_{⌡}_{∞}_{√}_{⌡}_{⌠}_{⌡}_{∞}^{1}^{m}_{,}^{0}^{l}l_{l}_{0}_{0}_{2}^{w}^{w}_{1}^{&apos;}&apos;_{&apos;}_{,}_{,}_{,}_{,}_{1}_{1}^{mod}mod_{mod}^{&apos;}_{3}^{p}^{p}_{2}^{+}_{,}^{(}^{(}_{2}^{i}^{N}^{3}^{p}^{p}_{,}^{)}_{3}^{−}^{sc}^{⎰}^{⎰}^{RB}^{2}2_{2}^{i}^{{}^{{}^{n}^{+}+_{+}^{)}_{if}_{if}_{if}^{7}^{9}^{PRB}^{,}^{,}_{5}^{2}2^{10}^{8}_{n}_{n}_{n}^{(}^{(}^{,}+^{11}_{s}_{s}_{s}^{m}^{m}^{,}^{+}^{12}_{mod}_{mod}_{mod}3^{&apos;}^{&apos;}^{,}^{+}^{+}^{13}^{k}_{√}^{,}l^{14}^{&apos;}^{n}^{n}&apos;^{}}^{PRB}^{PRB}/_{2}_{2}_{2}^{}}2_{∃}_{=}_{=}_{=}^{)}^{)}^{mod}^{mod}_{1}_{0}_{0}^{if}if_{if}_{and}_{and}_{and}^{in}in_{not }^{2}^{2}_{not }^{a }a _{in}_{not }^{=}^{=}_{in}^{special}special^{1}_{a }^{0}_{in}_{a }_{in}_{special}_{special}_{special}_{special}^{subframe}subframe_{subframe}_{subframe}_{subframe}_{subframe}^{ with} with_{ with}_{ with}_{ with}^{configurat}configurat_{configurat}_{configurat}_{configurat}^{ion}ion_{ion}1,^{3,}_{ion}_{ion}2,^{4,}_{1,}_{1,}6,_{1,}^{8,}_{2,}_{2,}or ^{9}_{2,}_{6,}^{or }_{6,}_{6,}7_{or }^{10}(see_{or }_{or }_{7}_{(see}_{7}^{(see}_{7}_{(see}Table_{(see}_{Table}^{Table}_{Table}_{Table}4.2_{4.2}^{4.2}-_{4.2}_{4.2}1)_{-}^{-}_{1)}^{1)}_{-}_{-}_{1)}_{1)}]

The sequence ![](media_svg/image834.svg) [公式: w_{p}(i)] is given by Table 6.10.3.2-1.

Table 6.10.3.2-1: The sequence ![](media_svg/image834.svg) [公式: w_{p}(i)] for normal cyclic prefix

| Antenna port ![](media_svg/image835.svg) [公式: p] | ![](media_svg/image836.svg) [公式≈: {w_{p}(0)w_{p}(1)w_{p}(2)w_{p}(3)}] |
| --- | --- |
| 7 | ![](media_svg/image837.svg) [公式: {+1+1+1+1}] |
| 8 | ![](media_svg/image838.svg) [公式: {+1−1+1−1}] |
| 9 | ![](media_svg/image839.svg) [公式: {+1+1+1+1}] |
| 10 | ![](media_svg/image838.svg) [公式: {+1−1+1−1}] |
| 11 | ![](media_svg/image840.svg) [公式: {+1+1−1−1}] |
| 12 | ![](media_svg/image841.svg) [公式: {−1−1+1+1}] |
| 13 | ![](media_svg/image842.svg) [公式: {+1−1−1+1}] |
| 14 | ![](media_svg/image843.svg) [公式: {−1+1+1−1}] |

Extended cyclic prefix:

![](media_svg/image844.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;mod2)∪r(4∪l&apos;∪N_{RB}^{max,}^{DL}+4∪n_{PRB}+m&apos;)]

where

![](media_svg/image845.svg) [公式≈: ^{w}^{p}^{(}_{m}^{i}^{k}^{k}_{l}^{)}^{l}^{&apos;}_{&apos;}_{&apos;}^{=}^{=}^{=}^{=}_{=}_{=}^{3}^{l}_{0}^{√}^{⌠}^{∞}^{√}^{⌠}^{∞}√_{⌡}_{⌠}_{⌡}_{∞}^{±}^{1}^{m}_{,}0_{0}^{2}_{2}^{w}^{w}_{1}^{mod},_{,}_{,}_{,}1_{1}^{&apos;}_{3}_{2}^{p}^{p}^{+}^{(}^{(}_{,}^{if}^{if}_{3}^{N}^{1}^{i}^{)}if_{if}_{if}^{2}^{−}^{sc}^{n}^{n}^{RB}^{+}^{i}^{s}^{s}n_{n}_{n}^{)}^{n}^{mod}^{mod}_{s}_{s}_{s}^{4}^{PRB}mod_{mod}_{mod}^{m}^{m}^{+}^{±}^{±}^{2}^{2}^{mod}^{mod}2_{2}_{2}^{k}^{=}^{=}^{&apos;}=_{=}_{=}^{1}^{0}^{and}_{1}^{2}^{2}^{and}0_{0}_{and}and_{and}^{=}^{=}^{1}^{0}^{p}^{p}_{not }in^{⎰}_{not }^{⎰}^{{}^{{}a ^{7}^{7}_{in}_{in}special^{,}^{,}^{8}^{8}^{}}_{a }^{}}_{a }_{special}_{special}subframe_{subframe}_{subframe} withconfiguration1,2,3,5or 6(seeTable4.2-1)]

The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] is given by Table 6.10.3.2-2.

Table 6.10.3.2-2: The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] for extended cyclic prefix and for slot/subslot-PDSCH

| Antenna port ![](media_svg/image847.svg) [公式: p] | ![](media_svg/image848.svg) [公式: {w_{p}(0)w_{p}(1)}] |
| --- | --- |
| 7 | ![](media_svg/image849.svg) [公式: {+1+1}] |
| 8 | ![](media_svg/image850.svg) [公式: {−1+1}] |
| 9 | ![](media_svg/image849.svg) [公式: {+1+1}] |
| 10 | ![](media_svg/image850.svg) [公式: {−1+1}] |

For extended cyclic prefix, UE-specific reference signals are not supported on antenna ports 9 to 14.

For slot-PDSCH transmission, the baseline pattern (see 'Baseline' in Figure 6.10.3.2-2A) of UE-specific reference signals is defined as follows. It is applied in MBSFN subframes.

![](media_svg/image832.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;)∪r(3∪l&apos;∪N_{RB}^{max,}^{DL}+3∪n_{PRB}+m&apos;)]

where

- ![](media_svg/image851.svg) [公式≈: ^{w}^{p}^{(}^{i}^{)}^{=}^{√}^{⌡}^{⌠}⌡∞^{w}w^{p}p^{(}(1^{i}^{)}−i)^{m}m^{±}±^{mod}mod^{2}2^{=}=1^{0}]

- ![](media_svg/image852.svg) [公式: m&apos;=0,1,2]

- ![](media_svg/image853.svg) [公式: l&apos;=0,1]

- $ l=l_{0}+l'$

- ![](media_svg/image854.svg) [公式≈: _{k}_{&apos;}_{=}√_{⌠}_{∞}1_{0}p_{p}⎰_{⎰}{_{{}_{9}7_{,},_{10}8}_{}}]

- ![](media_svg/image855.svg) [公式≈: k=5m&apos;+N_{sc}^{RB}n_{PRB}+k&apos;]

and

- $ l_{0}=3 $ if the slot where the PDSCH is transmitted in (![](media_svg/image856.svg) [公式≈: ^{n}s]) fulfils ![](media_svg/image857.svg) [公式: n_{s}mod2=0]

- $ l_{0}=2 $ if the slot where the PDSCH is transmitted in (![](media_svg/image856.svg) [公式≈: ^{n}s]) fulfils ![](media_svg/image858.svg) [公式: n_{s}mod2=1]

The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] is given by Table 6.10.3.2-2.

For slot-PDSCH transmission in normal subframes,![](media_svg/image859.svg) [公式≈: _{a}_{k}(_{,}p_{l})]is generated as for the baseline slot-PDSCH UE-specific reference signal pattern for the same values of ![](media_svg/image860.svg) [公式: l], while ![](media_svg/image861.svg) [公式: k] is given by ![](media_svg/image862.svg) [公式≈: k=N_{sc}^{RB}n_{PRB}+k&apos;]and depends on the cell-specific frequency shift ![](media_svg/image863.svg) [公式≈: ^{v}shift]as follows (see 'v0', 'v1' and 'v2' in Figure 6.10.3.2-2A for $ v_{shift}mod3=0 $, $ v_{shift}mod3=1 $, and $ v_{shift}mod3=2 $, respectively):

- For $ v_{shift}mod3=0 $, $ k^{'}={\begin {matrix}2, 7, 11 & p\in  \left \{ 7,8\right \}  \\ 1, 5, 10 & p\in  \left \{ 9,10\right \} \end {matrix}$,

- For $ v_{shift}mod3=1 $, $ k^{'}={\begin {matrix}2, 6, 11 & p\in  \left \{ 7,8\right \}  \\ 0, 5, 9 & p\in  \left \{ 9,10\right \} \end {matrix}$,

- For $ v_{shift}mod3=2 $, $ k^{'}={\begin {matrix}1, 6, 10 & p\in  \left \{ 7,8\right \}  \\ 0, 4, 9 & p\in  \left \{ 9,10\right \} \end {matrix}$.

![](media/image864.emf)

Figure 6.10.3.2-2A: Mapping of UE-specific reference signals for slot-PDSCH, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

For subslot-PDSCH transmission, the baseline pattern (see 'Baseline' in Figure 6.10.3.2-2B) of UE-specific reference signals is defined as follows. It is applied if the presence of UE-specific reference signals is indicated in the DCI associated with the subslot-PDSCH (see DMRS position indicator field in TS 36.212 [3]), and in downlink subslots where the baseline pattern, including all the REs associated with ![](media_svg/image865.svg) [公式: p⎰{7,8}] if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI is configured with 4 layers, has no overlapping resource element with CRS and no overlapping resource element with configured zero-power and non-zero-power CSI reference signals:

![](media_svg/image867.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;)∪r(2∪l&apos;∪N_{RB}^{max,}^{DL}+2∪n_{PRB}+m&apos;)]

where

![](media_svg/image868.svg) [公式≈: ^{w}^{p}^{(}_{m}^{i}_{k}k_{l}^{)}_{l}_{&apos;}_{&apos;}_{&apos;}^{=}=_{=}_{=}_{=}_{=}_{l}7_{0}_{0}^{√}^{⌠}^{∞}_{√}_{⌠}_{∞}_{&apos;}_{1}_{,}_{,}_{0}_{+}m^{w}^{w}_{1}_{1}_{l}&apos;^{p}^{p}_{0}+^{(}^{(}^{1}_{(see}_{p}_{p}N^{i}^{)}^{−}_{⎰}_{⎰}_{sc}^{RB}^{i}_{{}_{{}^{)}_{Table}n_{9}_{7}_{,}_{,}_{PRB}_{10}_{8}^{m}^{m}_{}}_{}}^{±}^{±}+^{mod}^{mod}_{6.4.2}k&apos;+2^{2}^{2}_{-}∪^{=}^{=}_{1)}(n^{1}^{0}_{PRB}mod2)]

The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] is given by Table 6.10.3.2-2.For subslot-PDSCH transmission in normal subframes, in downlink subslots where the baseline pattern, including all the REs associated with ![](media_svg/image869.svg) [公式: p⎰{7,8}] if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI is configured with 4 layers, has overlapping resource elements with configured zero-power or non-zero-power CSI reference signals or has overlapping resource elements with CRS, if the presence of UE-specific reference signals is indicated in the DCI associated (see DMRS position indicator field in TS 36.212 [3]) with the subslot-PDSCH, a shifted pattern of UE-specific reference signals is applied. In the shifted pattern,![](media_svg/image859.svg) [公式≈: _{a}_{k}(_{,}p_{l})]is generated as for the baseline subslot-PDSCH UE-specific reference signal pattern for the same value of ![](media_svg/image860.svg) [公式: l], while ![](media_svg/image861.svg) [公式: k] is given by ![](media_svg/image862.svg) [公式≈: k=N_{sc}^{RB}n_{PRB}+k&apos;]and depends on the cell-specific frequency shift ![](media_svg/image863.svg) [公式≈: ^{v}shift]as follows (see also 'v0','v1' and 'v2' in Figure 6.10.3.2-2B for $ v_{shift}mod3=0 $, $ v_{shift}mod3=1 $, and $ v_{shift}mod3=2 $, respectively):

- For $ v_{shift}mod3=0 $, $ k^{'}={\begin {matrix}2, 8 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=0 \\ 4, 11 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=1 \\ 1, 7 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=0 \\ 2, 10 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=1\end {matrix}$,

- For $ v_{shift}mod3=1 $, $ k^{'}={\begin {matrix}2, 8 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=0 \\ 3, 11 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=1 \\ 0, 6 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=0 \\ 2, 9 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=1\end {matrix}$,

- For $ v_{shift}mod3=2 $,  $ k^{'}={\begin {matrix}1, 9 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=0 \\ 3, 10 & p\in  \left \{ 7, 8\right \} andn_{PRB}mod2=1 \\ 0, 7 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=0 \\ 1, 9 & p\in  \left \{ 9, 10\right \} andn_{PRB}mod2=1\end {matrix}$,

For subslot-PDSCH transmission in MBSFN subframes, in downlink subslots where the baseline pattern, including all the REs associated with ![](media_svg/image865.svg) [公式: p⎰{7,8}] if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI is configured with 4 layers,  has overlapping resource elements with configured zero-power or non-zero-power CSI reference signals, if the presence of UE-specific reference signals is indicated in the DCI associated (see DMRS position indicator field in TS 36.212 [3]) with the subslot-PDSCH, the shifted pattern of UE-specific reference signals for ![](media_svg/image870.svg) [公式≈: ^{v}shift^{=}^{0}], as defined above, is applied (see 'v0' in Figure 6.10.3.2-2B for $ v_{shift}mod3=0 $).

![](media/image871.emf)

Figure 6.10.3.2-2B: Mapping of UE-specific reference signals for subslot-PDSCH, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of UE-specific reference signals to one UE on any of the antenna ports in the set ![](media_svg/image872.svg) [公式: S], where ![](media_svg/image873.svg) [公式: S={7,8,11,13}] or ![](media_svg/image874.svg) [公式: S={9,10,12,14}] shall

- not be used for transmission of PDSCH on any antenna port in the same slot, and

- not be used for UE-specific reference signals to the same UE on any antenna port other than those in ![](media_svg/image872.svg) [公式: S] in the same slot.


Figure 6.10.3.2-3 illustrates the resource elements used for UE-specific reference signals for normal cyclic prefix for antenna ports 7, 8, 9 and 10. Figure 6.10.3.2-4 illustrates the resource elements used for UE-specific reference signals for extended cyclic prefix for antenna ports 7, 8.

For BL/CE UEs, if downlink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PDSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PDSCH transmission without a corresponding MPDCCH,

- If all OFDM symbols in a PRB are reserved, the demodulation reference signal transmission in that PRB is dropped.

![](media/image875.emf)

Figure 6.10.3.2-3: Mapping of UE-specific reference signals, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

![](media/image876.emf)

Figure 6.10.3.2-4: Mapping of UE-specific reference signals, antenna ports 7 and 8 (extended cyclic prefix)

### 6.10.3A Demodulation reference signals associated with EPDCCH, MPDCCH, or SPDCCH

The demodulation reference signal associated with EPDCCH/MPDCCH/SPDCCH

- is transmitted on the same antenna port ![](media_svg/image877.svg) [公式: p⎰{107,108,109,110}] as the associated EPDCCH/MPDCCH/SPDCCH physical resource;

- is present and is a valid reference for EPDCCH/MPDCCH/SPDCCH demodulation only if the EPDCCH/MPDCCH/SPDCCH transmission is associated with the corresponding antenna port;

- is transmitted only on the physical resource blocks upon which the corresponding EPDCCH/MPDCCH/SPDCCH is mapped.

A demodulation reference signal associated with EPDCCH/MPDCCH/SPDCCH is not transmitted in resource elements ![](media_svg/image35.svg) [公式: (k,l)] in which one of the physical channels or physical signals other than the demodulation reference signals defined in 6.1 are transmitted using resource elements with the same index pair ![](media_svg/image35.svg) [公式: (k,l)] regardless of their antenna port ![](media_svg/image34.svg) [公式: p].

#### 6.10.3A.1 Sequence generation

For any of the antenna ports ![](media_svg/image878.svg) [公式: p⎰{107,108,109,110}], the reference-signal sequence ![](media_svg/image799.svg) [公式: r(m)] is defined by

![](media_svg/image800.svg) [公式≈: ^{r}^{(}^{m}^{)}^{=}^{1}2^{(}^{1}^{−}^{2}^{∪}^{c}^{(}^{2}^{m}^{)}^{)}^{+}^{j}^{1}2^{(}^{1}^{−}^{2}^{∪}^{c}^{(}^{2}^{m}^{+}^{1}^{)}^{)}^{,}^{m}^{=}^{√}^{⌡}^{⌠}⌡_{∞}^{0}0^{,},^{1}1^{,...,},...,^{12}16^{N}N^{RB}_{RB}^{max,}^{max,}^{DL}^{DL}^{−}−^{1}1extended^{normal}^{cyclic}cyclic^{prefix}prefix].

For non-BL/CE UEs, the pseudo-random sequence ![](media_svg/image879.svg) [公式: c(n)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

![](media_svg/image880.svg) [公式≈: c_{init}=(_{√}n_{s}/2_{∃}+1)∪(2n_{ID}^{xPDCCH}_{,i}+1)∪2^{16}+n_{SCID}^{xPDCCH}]

at the start of each subframe where

- ![](media_svg/image881.svg) [公式≈: _{n}_{ID,}xPDCCH_{i}] and ![](media_svg/image882.svg) [公式≈: _{n}_{SCID}xPDCCH] shall be replaced by ![](media_svg/image883.svg) [公式≈: _{n}_{ID,}EPDCCH_{i}] and ![](media_svg/image884.svg) [公式≈: _{n}_{SCID}EPDCCH], respectively, for the EPDCCH

- ![](media_svg/image881.svg) [公式≈: _{n}_{ID,}xPDCCH_{i}] and ![](media_svg/image882.svg) [公式≈: _{n}_{SCID}xPDCCH] shall be replaced by ![](media_svg/image885.svg) [公式≈: _{n}_{ID,}SPDCCH_{i}] and ![](media_svg/image886.svg) [公式≈: _{n}_{SCID}SPDCCH], respectively, for the SPDCCH

- ![](media_svg/image887.svg) [公式≈: _{n}_{SCID}EPDCCH_{=}_{2}], ![](media_svg/image888.svg) [公式≈: _{n}_{SCID}SPDCCH_{=}_{2}], and

- ![](media_svg/image889.svg) [公式≈: _{n}_{ID}EPDCCH_{,i}] is configured by higher layers.

The EPDCCH/SPDCCH set to which the EPDCCH/SPDCCH associated with the demodulation reference signal belong is denoted ![](media_svg/image890.svg) [公式: i⎰{0,1}].

For BL/CE UEs, the same scrambling sequence is applied per subframe to the demodulation reference signal associated with MPDCCH for a given block of ![](media_svg/image802.svg) [公式≈: ^{N}acc] subframes. The subframe number of the first subframe in each block of ![](media_svg/image147.svg) [公式≈: ^{N}acc] consecutive subframes, denoted as ![](media_svg/image148.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image149.svg) [公式≈: (^{niN}abs,1acc^{+=}δ)^{mod0}]. For the ![](media_svg/image803.svg) [公式≈: _{j}th]block of ![](media_svg/image802.svg) [公式≈: ^{N}acc] subframes, the scrambling sequence generator shall be initialised with

![](media_svg/image891.svg) [公式≈: ^{c}^{init}^{=}^{√}^{⌠}_{∞}^{(}(^{{}{^{(}(^{j}j^{0}_{0}^{+}+^{j}j^{)})^{N}N^{acc}_{acc}^{mod}mod^{10}10^{}}}^{+}+^{1}1^{)})^{∪}∪^{(}(^{2}2^{n}N^{ID}^{MPDCCH}_{ID}^{cell}^{,i}+1)^{+}∪2^{1}^{16}^{)}^{∪}+^{2}^{16}n_{SCID}^{MPDCCH}^{+}^{n}^{SCID}^{MPDCCH}^{otherwise}for Type1-Common andType2-Common] where

![](media_svg/image892.svg) [公式≈: ^{i}^{j}^{j}^{δ}^{0}^{=}^{=}^{=}^{0}^{√}^{⌠}_{∞}^{√}^{,}^{1}^{(}^{0,}N^{,...,}^{i}^{0}_{acc}^{+}^{⋅}^{⋅}^{√}^{i}−^{i}^{δ}^{0}2^{)}^{+},^{N}^{N}^{acc}^{for }for ^{abs}^{MPDCCH}^{∃}^{N}^{frame}frame^{acc}^{+}^{structure}structure^{i}^{δ}^{−}^{1}^{∂}^{∂}^{∃}^{−}^{ type} type^{j}^{0}^{1}2^{or  }and^{N}N^{acc}_{acc}^{=}=^{1}10]

and ![](media_svg/image153.svg) [公式≈: ^{i}0] is the absolute subframe number of the first downlink subframe intended for MPDCCH. The MPDCCH transmissions span ![](media_svg/image893.svg) [公式≈: _{N}_{abs}MPDCCH] consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

For BL/CE UEs,

- if the MPDCCH transmission is associated with P-RNTI or SC-RNTI:

-  for frame structure type 1 and  for frame structure type 2

- otherwise

- for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA.

-  for frame structure type 1 and  for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB.

The quantities ![](media_svg/image897.svg) [公式≈: _{n}_{SCID}MPDCCH_{=}_{2}] and ![](media_svg/image898.svg) [公式≈: _{n}_{ID}MPDCCH_{,i}] are configured by higher layers. The MPDCCH set to which the MPDCCH associated with the demodulation reference signal belong is denoted ![](media_svg/image890.svg) [公式: i⎰{0,1}]. For an MPDCCH associated with a 2+4 PRB set as defined in [4], ![](media_svg/image899.svg) [公式: i=0] is used to generate the scrambling sequence for the 6 PRBs as well as for the 2 PRBs and 4 PRBs.

#### 6.10.3A.2 Mapping to resource elements

For the antenna port ![](media_svg/image900.svg) [公式: p⎰{107,108,109,110}] in a physical resource block ![](media_svg/image901.svg) [公式≈: ^{n}PRB] assigned for the associated EPDCCH/MPDCCH, a part of the reference signal sequence ![](media_svg/image831.svg) [公式: r(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] in a subframe according to

Normal cyclic prefix:

![](media_svg/image832.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;)∪r(3∪l&apos;∪N_{RB}^{max,}^{DL}+3∪n_{PRB}+m&apos;)]

where

![](media_svg/image902.svg) [公式≈: ^{w}^{p}^{(}_{m}^{i}^{k}^{k}^{)}l_{l}^{&apos;}_{&apos;}_{&apos;}^{=}^{=}^{=}=_{=}_{=}^{5}_{0}^{√}^{⌠}^{∞}^{√}^{⌠}^{∞}^{√}^{⌡}_{⌠}_{⌡}_{∞}_{√}_{⌡}_{⌠}_{⌡}_{∞}^{1}^{m}_{,}^{0}^{l}l_{l}_{0}_{0}_{2}^{w}^{w}_{1}^{&apos;}&apos;_{&apos;}_{,}_{,}_{,}_{,}_{1}_{1}^{mod}mod_{mod}^{&apos;}_{3}^{p}^{p}_{2}^{+}_{,}^{(}^{(}_{2}^{i}^{N}^{3}^{p}^{p}_{,}^{)}_{3}^{−}^{sc}^{⎰}^{⎰}^{RB}^{2}2_{2}^{i}^{{}^{{}^{n}^{+}+_{+}^{)}^{107}^{109}_{if}_{if}_{if}^{PRB}_{5}^{2}2_{n}_{n}_{n}^{(}^{(}+_{s}_{s}_{s}^{,}^{,}^{m}^{m}^{108}^{110}^{+}_{mod}_{mod}_{mod}3^{&apos;}^{&apos;}^{+}^{+}^{k}_{√}l^{&apos;}^{n}^{n}^{}}^{}}&apos;^{PRB}^{PRB}/_{2}_{2}_{2}2_{∃}_{=}_{=}_{=}^{)}^{)}^{mod}^{mod}_{1}_{0}_{0}^{if}if_{if}_{and}_{and}_{and}^{in}in_{not }^{2}^{2}_{not }^{a }a _{in}_{not }^{=}^{=}_{in}^{special}special^{1}_{a }^{0}_{in}_{a }_{in}_{special}_{special}_{special}_{special}^{subframe}subframe_{subframe}_{subframe}_{subframe}_{subframe}^{ with} with_{ with}_{ with}_{ with}^{configurat}configurat_{configurat}_{configurat}_{configurat}^{ion}ion_{ion}1,^{3,}_{ion}_{ion}2,^{4,}_{1,}_{1,}6,_{1,}_{2,}^{8,}_{2,}or _{2,}_{6,}^{9}_{6,}_{6,}^{or }7_{or }(see_{or }_{or }^{10}_{7}_{(see}_{7}_{7}^{(see}_{(see}Table_{(see}_{Table}^{Table}_{Table}_{Table}4.2_{4.2}^{4.2}-_{4.2}_{4.2}1)_{-}^{-}_{1)}_{-}^{1)}_{-}_{1)}_{1)}]

The sequence ![](media_svg/image834.svg) [公式: w_{p}(i)] is given by Table 6.10.3A.2-1.

Table 6.10.3A.2-1: The sequence ![](media_svg/image834.svg) [公式: w_{p}(i)] for normal cyclic prefix

| Antenna port ![](media_svg/image835.svg) [公式: p] | ![](media_svg/image836.svg) [公式≈: {w_{p}(0)w_{p}(1)w_{p}(2)w_{p}(3)}] |
| --- | --- |
| 107 | ![](media_svg/image837.svg) [公式: {+1+1+1+1}] |
| 108 | ![](media_svg/image838.svg) [公式: {+1−1+1−1}] |
| 109 | ![](media_svg/image839.svg) [公式: {+1+1+1+1}] |
| 110 | ![](media_svg/image838.svg) [公式: {+1−1+1−1}] |

Extended cyclic prefix:

![](media_svg/image903.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(l&apos;mod2)∪r(4∪l&apos;∪N_{RB}^{max,}^{DL}+4∪n_{PRB}+m&apos;)]

where

![](media_svg/image904.svg) [公式≈: ^{w}^{p}^{(}_{m}^{i}^{k}^{k}_{l}^{)}^{l}^{&apos;}_{&apos;}_{&apos;}^{=}^{=}^{=}^{=}_{=}_{=}^{3}^{l}_{0}^{√}^{⌠}^{∞}^{√}^{⌠}^{∞}√_{⌡}_{⌠}_{⌡}_{∞}^{±}^{1}^{m}_{,}0_{0}^{2}_{2}^{w}^{w}_{1}^{mod},_{,}_{,}_{,}1_{1}^{&apos;}_{3}^{p}^{p}_{2}^{+}^{(}^{(}_{,}^{if}^{if}^{N}^{1}_{3}^{i}^{)}^{−}if_{if}_{if}^{2}^{sc}^{RB}^{n}^{n}^{+}^{i}^{s}^{s}n_{n}_{n}^{)}^{n}^{mod}^{mod}^{4}_{s}_{s}_{s}^{PRB}mod_{mod}_{mod}^{m}^{m}^{±}^{±}^{2}^{2}^{+}^{mod}^{mod}2_{2}_{2}^{=}^{=}^{k}^{&apos;}=_{=}_{=}^{1}^{0}^{and}^{2}^{2}_{1}^{and}0_{0}_{and}^{=}^{=}and_{and}^{1}^{0}^{p}^{p}_{not }^{⎰}in _{not }^{⎰}^{{}^{{}a^{107}^{107}_{in }_{in }special_{a}^{,}_{a}^{108}^{,}^{108}_{special}_{special}^{}}^{}}subframe_{subframe}_{subframe} with configuration 1,2,3,5or 6(seeTable4.2-1)]

The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] is given by Table 6.10.3A.2-2.

Table 6.10.3A.2-2: The sequence ![](media_svg/image846.svg) [公式: w_{p}(i)] for extended cyclic prefix

| Antenna port ![](media_svg/image847.svg) [公式: p] | ![](media_svg/image848.svg) [公式: {w_{p}(0)w_{p}(1)}] |
| --- | --- |
| 107 | ![](media_svg/image849.svg) [公式: {+1+1}] |
| 108 | ![](media_svg/image850.svg) [公式: {−1+1}] |

For extended cyclic prefix, demodulation reference signals are not supported on antenna ports 109 to 110.

For the antenna port ![](media_svg/image905.svg) [公式: p=107] in a physical resource block ![](media_svg/image901.svg) [公式≈: ^{n}PRB] assigned for the SPDCCH, a part of the reference signal sequence ![](media_svg/image831.svg) [公式: r(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] in a subframe according to the procedure used for UE-specific reference signals associated with subslot-PDSCH on antenna port![](media_svg/image906.svg) [公式: 7] described in clause 6.10.3.2 with the following amendments:

- for slot-SPDCCH, ![](media_svg/image907.svg) [公式: l=l&apos;],

- for slot-SPDCCH in MBSFN subframes, the procedure used for the baseline pattern of UE-specific reference signals associated with subslot-PDSCH is applied

- for slot-SPDCCH in normal subframes, the procedure used for the shifted pattern of UE-specific reference signals associated with subslot-PDSCH depending on the cell-specific frequency shift ![](media_svg/image863.svg) [公式≈: ^{v}shift]is applied.

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of demodulation reference signals to one UE on any of the antenna ports in the set ![](media_svg/image872.svg) [公式: S], where ![](media_svg/image908.svg) [公式: S={107,108}] or ![](media_svg/image909.svg) [公式: S={109,110}] shall

- not be used for transmission of EPDCCH/MPDCCH on any antenna port in the same slot, and

- not be used for demodulation reference signals to the same UE on any antenna port other than those in ![](media_svg/image872.svg) [公式: S] in the same slot.

Replacing antenna port numbers 7 – 10 by 107 – 110 in Figure 6.10.3.2-3 provides an illustration of the resource elements used for demodulation reference signals associated with EPDCCH/MPDCCH for normal cyclic prefix. Replacing antenna port numbers 7 – 8 by 107 – 108 in Figure 6.10.3.2-4 provides an illustration of the resource elements used for demodulation reference signals associated with EPDCCH/MPDCCH for extended cyclic prefix.

For frame structure type 3, for EPDCCH in a subframe with the same duration as the DwPTS duration of a special subframe configuration, the mapping of the demodulation reference signals to the resource elements is the same as that for the corresponding special subframe configuration.

For BL/CE UEs, if downlink resource reservation is enabled for the UE as specified in [9], then in case of MPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space,

- If all OFDM symbols in a PRB are reserved, the demodulation reference signal transmission in that PRB is dropped.

### 6.10.4 Positioning reference signals

Positioning reference signals shall only be transmitted in resource blocks in downlink subframes configured for positioning reference signal transmission. If both normal and MBSFN subframes are configured as positioning subframes within a cell, the OFDM symbols in a MBSFN subframe configured for positioning reference signal transmission shall use the same cyclic prefix as used for subframe #0. If only MBSFN subframes are configured as positioning subframes within a cell, the OFDM symbols configured for positioning reference signals in the MBSFN region of these subframes shall use extended cyclic prefix length. In a subframe configured for positioning reference signal transmission, the starting positions of the OFDM symbols configured for positioning reference signal transmission shall be identical to those in a subframe in which all OFDM symbols have the same cyclic prefix length as the OFDM symbols configured for positioning reference signal transmission.

Positioning reference signals are transmitted on antenna port 6.

The positioning reference signals shall not be mapped to resource elements ![](media_svg/image35.svg) [公式: (k,l)] allocated to the core part of the PBCH, PSS or SSS regardless of their antenna port ![](media_svg/image34.svg) [公式: p].

Positioning reference signals are defined for ![](media_svg/image48.svg) [公式: δf=15kHz] only.

#### 6.10.4.1 Sequence generation

The reference-signal sequence ![](media_svg/image910.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] is defined by

![](media_svg/image911.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,2N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image912.svg) [公式≈: ^{n}s] is the slot number within a radio frame, ![](media_svg/image92.svg) [公式: l] is the OFDM symbol number within the slot. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image913.svg) [公式≈: cinit=2^{28}∪√NID^{PRS}512∃+2^{10}∪(7∪(ns+1)+l+1)∪(2∪(NID^{PRS}mod512)+1)+2∪(NID^{PRS}mod512)+NCP] at the start of each OFDM symbol where ![](media_svg/image914.svg) [公式: N_{ID}^{PRS}⎰{0,1,...,4095}] equals ![](media_svg/image915.svg) [公式≈: _{N}_{ID}cell] unless configured by higher layers and where

![](media_svg/image916.svg) [公式≈: ^{N}^{CP}^{=}^{√}^{⌠}_{∞}^{1}0^{for }for extended^{normal}^{CP}CP]

#### 6.10.4.2 Mapping to resource elements

If PRS frequency hopping is not configured by higher layers, the reference signal sequence ![](media_svg/image917.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference signal for antenna port ![](media_svg/image918.svg) [公式: p=6] in slot ![](media_svg/image919.svg) [公式≈: ^{n}s] according to

![](media_svg/image920.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m&apos;)]

where

Normal cyclic prefix:

![](media_svg/image921.svg) [公式≈: l^{k}_{m}_{m}=_{±}^{=}_{=}_{=}^{√}^{⌡}_{⌠}_{⌡}_{∞}^{6}1_{0}^{3}_{2}_{m}^{(},_{,}^{,}^{m}_{,}_{1}2^{5}_{3}_{,},_{+}^{,}_{,}_{κ}3^{+}^{6}_{5},_{N}_{,}5_{6}^{N}_{,},_{2}_{RB}6_{max,}^{RB}^{DL}_{∪}_{N}_{DL}^{if}if_{if}^{−}_{RB}_{PRS}^{N}^{n}n_{n}_{−}^{s}_{s}_{s}^{RB}^{PRS}_{−}^{mod}mod_{mod}_{N}_{1}_{RB}_{PRS}^{)}^{+}^{2}2_{2}^{(}^{=}=_{=}^{6}1_{1}^{−}^{0}and_{and}^{l}^{+}^{v}^{shift}(_{(}1_{4}or_{PBCH}^{)}^{mod}2PBCH^{6}_{antenna}antenna_{ports}ports_{)})]

Extended cyclic prefix:

![](media_svg/image922.svg) [公式≈: l^{k}_{m}_{m}=_{±}^{=}_{=}_{=}^{√}^{⌡}_{⌠}_{⌡}_{∞}^{6}1_{0}^{4}_{2}_{m}^{(},_{,}^{m}^{,}_{,}_{1}2^{5}_{4}_{,},_{+}_{κ}_{,}4^{+}_{5},_{N}5^{N}_{,}_{2}_{RB}_{max,}^{RB}^{DL}_{∪}^{if}if_{if}_{N}_{DL}^{−}_{RB}_{PRS}^{n}n_{n}^{s}_{s}_{s}^{N}^{mod}mod_{mod}_{−}^{RB}^{PRS}_{−}_{N}_{1}_{RB}_{PRS}^{2}2_{2}^{)}^{+}^{=}=_{=}^{(}1_{1}^{5}^{0}^{−}and_{and}^{l}^{+}(_{(}^{v}1_{4}^{shift}or_{PBCH}2^{)}^{mod}PBCH_{antenna}^{6}antenna_{ports}ports_{)})]

The bandwidth for positioning reference signals ![](media_svg/image923.svg) [公式≈: _{N}_{RB}PRS] is configured by higher layers and the cell-specific frequency shift is given by ![](media_svg/image924.svg) [公式≈: v_{shift}=N_{ID}^{PRS}mod6] where ![](media_svg/image925.svg) [公式≈: _{N}_{ID}PRS_{=}_{N}_{ID}cell] if no value for ![](media_svg/image926.svg) [公式≈: _{N}_{ID}PRS] is configured by higher layers.

If PRS frequency hopping is configured by higher layers, a PRS frequency hopping configuration provided by higher layers contains the following:

- The length of the PRS occasion group, ![](media_svg/image927.svg) [公式≈: ^{L}^{PRS}GROUP]

- Number of PRS frequency hopping bands, ![](media_svg/image928.svg) [公式≈: ^{N}BAND^{PRS}]

- ![](media_svg/image929.svg) [公式≈: _{n}_{i}RB] defined as twice the starting PRB index of PRS frequency hopping band ![](media_svg/image930.svg) [公式: i] where

- ![](media_svg/image931.svg) [公式≈: _{n}_{i}RB_{=}_{N}_{RB}DL_{−}_{N}_{RB}PRS] if ![](media_svg/image932.svg) [公式: i=0],

- ![](media_svg/image933.svg) [公式≈: _{n}_{i}RB_{=}_{2}_{∪}_{n}~_{i}RB] where ![](media_svg/image934.svg) [公式≈: _{n}_{~}_{i}RB] is the index of the first PRB in the PRS frequency hopping narrowband configured by higher layers if ![](media_svg/image935.svg) [公式≈: i⎰{1,...,N_{BAND}^{PRS}−1}]

If PRS frequency hopping is configured by higher layers, the reference signal sequence ![](media_svg/image917.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)]in the PRS occasion ![](media_svg/image936.svg) [公式: j], ![](media_svg/image937.svg) [公式≈: j=0,...,L^{PRS}_{GROUP}−1], in the PRS occasion group shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference signal for antenna port ![](media_svg/image938.svg) [公式: p=6] in slot ![](media_svg/image919.svg) [公式≈: ^{n}s] according to

![](media_svg/image920.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=r_{l}_{,}_{n}_{s}(m&apos;)]

where

- for normal cyclic prefix

![](media_svg/image939.svg) [公式≈: ^{i}l^{k}_{m}_{m}^{=}=_{±}^{=}_{=}_{=}^{√}^{⌡}_{⌠}_{⌡}_{∞}^{j}^{6}1_{0}^{3}_{2}^{mod}_{m}^{(},_{,}^{,}^{m}_{,}_{1}2^{5}_{3}_{,},_{+}^{,}_{,}_{κ}3^{+}^{6}_{5},_{n}_{,}5^{N}^{n}_{6}_{,}_{i}_{RB},_{2}^{i}^{RB}6^{BAND}^{PRS}_{∪}_{N}_{+}^{)}^{if}if_{if}^{+}_{RB}_{N}_{PRS}^{(}^{n}n_{n}^{6}_{RB}_{max,}^{s}_{s}_{s}^{−}_{−}^{mod}mod_{mod}^{l}_{1}_{DL}^{+}^{v}_{−}^{2}2_{2}^{shift}^{=}=_{=}_{N}1_{1}_{RB}^{0}_{DL}^{)}^{mod}and_{and}(_{(}^{6}1_{4}or_{PBCH}2PBCH_{antenna}antenna_{ports}ports_{)})]

- for extended cyclic prefix

![](media_svg/image940.svg) [公式≈: ^{i}l^{k}_{m}_{m}^{=}=_{±}^{=}_{=}_{=}^{√}^{⌡}_{⌠}_{⌡}_{∞}^{j}^{6}1_{0}^{4}_{2}^{mod}_{m}^{(},_{,}^{m}^{,}_{,}_{1}2^{5}_{4}_{,},_{+}_{,}_{κ}4^{+}_{5},_{n}5^{N}^{n}_{,}_{i}_{RB}_{2}^{i}^{RB}^{BAND}^{PRS}_{∪}^{if}if_{if}_{N}_{+}^{)}^{+}_{RB}_{N}_{PRS}^{n}n_{n}^{(}^{s}_{s}_{s}^{5}_{RB}_{max,}^{mod}mod_{mod}^{−}_{−}^{l}_{1}_{DL}^{+}^{2}2_{2}^{v}_{−}^{=}=_{=}^{shift}_{N}1_{1}^{0}and_{and}_{RB}_{DL}^{)}^{mod}(_{(}1_{4}^{6}or_{PBCH}2PBCH_{antenna}antenna_{ports}ports_{)})]

![](media/image941.emf)

Figure 6.10.4.2-1: Mapping of positioning reference signals (normal cyclic prefix)

![](media/image942.emf)

Figure 6.10.4.2-2: Mapping of positioning reference signals (extended cyclic prefix)

#### 6.10.4.3 Positioning reference signal subframe configuration

The subframe configuration period ![](media_svg/image943.svg) [公式≈: ^{T}PRS] and the subframe offset ![](media_svg/image944.svg) [公式≈: ^{δ}PRS] for the transmission of positioning reference signals are listed in Table 6.10.4.3-1. The PRS configuration index ![](media_svg/image945.svg) [公式≈: ^{I}PRS] is configured by higher layers. Positioning reference signals are transmitted only in configured DL subframes. Positioning reference signals shall not be transmitted in DwPTS. Positioning reference signals shall be transmitted in ![](media_svg/image22.svg) [公式≈: ^{N}PRS] consecutive downlink subframes, where ![](media_svg/image23.svg) [公式≈: ^{N}PRS] is configured by higher layers.

The positioning reference signal instances, for the first subframe of the ![](media_svg/image946.svg) [公式≈: ^{N}PRS] downlink subframes, shall satisfy ![](media_svg/image947.svg) [公式≈: (10≠n_{f}+_{√}n_{s}/2_{∃}−δ_{PRS})modT_{PRS}=0].

Table 6.10.4.3-1: Positioning reference signal subframe configuration

| PRS configuration Index ![](media_svg/image948.svg) [公式≈: ^{I}PRS] | PRS periodicity ![](media_svg/image949.svg) [公式≈: ^{T}PRS] (subframes) | PRS subframe offset ![](media_svg/image950.svg) [公式≈: ^{δ}PRS] (subframes) |
| --- | --- | --- |
| 0 – 159 | 160 | ![](media_svg/image951.svg) [公式≈: ^{I}PRS] |
| 160 – 479 | 320 | ![](media_svg/image952.svg) [公式: I_{PRS}−160] |
| 480 – 1119 | 640 | ![](media_svg/image953.svg) [公式: I_{PRS}−480] |
| 1120 – 2399 | 1280 | ![](media_svg/image954.svg) [公式: I_{PRS}−1120] |
| 2400 – 2404 | 5 | ![](media_svg/image955.svg) [公式: I_{PRS}−2400] |
| 2405 – 2414 | 10 | ![](media_svg/image956.svg) [公式: I_{PRS}−2405] |
| 2415 – 2434 | 20 | ![](media_svg/image957.svg) [公式: I_{PRS}−2415] |
| 2435 – 2474 | 40 | ![](media_svg/image958.svg) [公式: I_{PRS}−2435] |
| 2475 – 2554 | 80 | ![](media_svg/image959.svg) [公式: I_{PRS}−2475] |
| 2555-4095 | Reserved |  |

### 6.10.5 CSI reference signals

CSI reference signals are transmitted on 1, 2, 4, 8, 12, 16, 20, 24, 28, or 32 antenna ports using ![](media_svg/image960.svg) [公式: p=15], ![](media_svg/image961.svg) [公式: p=15,16], ![](media_svg/image962.svg) [公式: p=15,...,18], ![](media_svg/image963.svg) [公式: p=15,...,22], ![](media_svg/image28.svg) [公式: p=15,...,26], ![](media_svg/image29.svg) [公式: p=15,...,30],![](media_svg/image964.svg) [公式: p=15,...,34], ![](media_svg/image31.svg) [公式: p=15,...,38], ![](media_svg/image32.svg) [公式: p=15,...,42] and![](media_svg/image33.svg) [公式: p=15,...,46], respectively.

For CSI reference signals using more than eight antenna ports, ![](media_svg/image965.svg) [公式: N_{res}^{CSI}>1] CSI-RS configurations in the same subframe, numbered from 0 to ![](media_svg/image966.svg) [公式: N_{res}^{CSI}−1], where value 0 corresponds to the configured resourceConfig-r11 or resourceConfig-r10 and value k (k>0) corresponds to the configured k-th entry of NZP-ResourceConfig-r13 from an aggregated list consisting of nzp-resourceConfigList-r13 followed by nzp-resourceConfigListExt-r14 (if configured), are aggregated to obtain ![](media_svg/image967.svg) [公式≈: ^{N}res^{CSI}^{N}ports^{CSI}] antenna ports in total. Each CSI-RS configuration in such an aggregation corresponds to ![](media_svg/image968.svg) [公式≈: N_{ports}^{CSI}⎰{4,8}] antenna ports and one of the configurations in the range 0-19 in Table 6.10.5.2-1 for normal cyclic prefix, and one of the configurations in the range 0-15 in Table 6.10.5.2-2 for extended cyclic prefix. The supported configurations of aggregated CSI-RS configurations are shown in Table 6.10.5-1. If the higher layer parameter NZP-TransmissionComb is not configured, ![](media_svg/image969.svg) [公式≈: _{N}_{res}CSI] unique CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix are aggregated to form 12, 16, 20, 24, 28, or 32 antenna ports.

For CSI reference signals using more than sixteen antenna ports, when higher layer parameter NZP-TransmissionComb is configured, the number of unique CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix that are aggregated to form 20, 24, 28, or 32 antenna ports can be less than or equal to ![](media_svg/image970.svg) [公式≈: _{N}_{res}CSI]. The number of antenna ports within each such unique CSI-RS resource configuration is an integer multiple of ![](media_svg/image971.svg) [公式≈: ^{N}ports^{CSI}].

CSI reference signals are defined for ![](media_svg/image48.svg) [公式: δf=15kHz] only.

Table 6.10.5-1: Aggregation of CSI-RS configurations.

| Total number of  antenna ports ![](media_svg/image967.svg) [公式≈: ^{N}res^{CSI}^{N}ports^{CSI}] | Number of antenna ports per CSI-RS configuration ![](media_svg/image972.svg) [公式≈: ^{N}ports^{CSI}] | Number of CSI-RS configurations ![](media_svg/image973.svg) [公式≈: _{N}_{res}CSI] |
| --- | --- | --- |
| 12 | 4 | 3 |
| 16 | 8 | 2 |
| 20 | 4 | 5 |
| 24 | 8 | 3 |
| 28 | 4 | 7 |
| 32 | 8 | 4 |

#### 6.10.5.1 Sequence generation

The reference-signal sequence ![](media_svg/image753.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] is defined by

![](media_svg/image974.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)=^{1}_{2}(1−2∪c(2m))+j^{1}_{2}(1−2∪c(2m+1)),m=0,1,...,N_{RB}^{max,}^{DL}−1]

where ![](media_svg/image755.svg) [公式≈: ^{n}s] is the slot number within a radio frame and ![](media_svg/image92.svg) [公式: l] is the OFDM symbol number within the slot. The pseudo-random sequence ![](media_svg/image467.svg) [公式: c(i)] is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with ![](media_svg/image975.svg) [公式≈: c_{init}=2^{10}∪(7∪(n_{s}±+1)+l+1)∪(2∪N_{ID}^{CSI}+1)+2∪N_{ID}^{CSI}+N_{CP}] at the start of each OFDM symbol where

![](media_svg/image976.svg) [公式≈: _{N}_{CP}_{n}_{s}_{±}_{=}_{=}√_{⌠}_{∞}_{√}_{⌠}_{∞}10_{1}_{0}_{n}_{s}√n_{for }_{for }s10_{extended}_{normal}∃+ns_{CP}mod_{CP}2for _{otherwise}framestructure type3 when theCSI-RSispart ofaDRS]

The quantity ![](media_svg/image977.svg) [公式≈: _{N}_{ID}CSI] equals ![](media_svg/image978.svg) [公式≈: _{N}_{ID}cell] unless configured by higher layers.

#### 6.10.5.2 Mapping to resource elements

In subframes configured for CSI reference signal transmission, the reference signal sequence ![](media_svg/image979.svg) [公式≈: r_{l}_{,}_{n}_{s}(m)] shall be mapped to complex-valued modulation symbols ![](media_svg/image39.svg) [公式≈: _{a}_{k}(_{,}p_{l})] used as reference symbols on antenna port ![](media_svg/image34.svg) [公式: p] . The mapping depends on the higher-layer parameter CDMType.

For the case of CDMType is not configured or is configured to CDM2:

![](media_svg/image980.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{±}^{)}=w_{l}_{&quot;}∪r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image981.svg) [公式≈: _{w}_{m}_{l}_{l}^{k}_{±}l_{±}_{&quot;}_{&apos;}^{=}=_{=}_{=}_{=}l_{0}^{k}_{√}_{⌠}_{∞}_{m}&apos;_{,}_{(}+^{&apos;}_{1}^{+}_{−}_{+}^{√}^{⌡}_{⌠}_{⌡}_{∞}^{12}_{1}_{1}^{l}_{l}2_{⋅}_{⋅}_{⋅}_{√}^{&quot;}_{&quot;}_{)}l_{l}_{N}^{m}&quot;_{&quot;}_{RB}_{max,}^{+}^{CSI}CSI_{CSI}_{p}^{√}^{⌡}^{⌡}^{⌡}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}^{⌡}^{⌡}^{⌡}^{∞}_{p}_{±}^{−}^{−}^{−}^{−}^{−}^{−}^{−}^{−}_{±}_{DL}_{⎰}_{⎰}_{2}^{1}^{3}^{9}^{0}^{6}^{7}^{0}^{6}^{reference}reference_{reference}_{{}_{{}_{−}_{16}_{15}_{N}^{for }^{for }^{for }^{for }^{for }^{for }^{for }^{for }_{,}_{,}_{18}_{17}_{RB}_{DL}_{,}_{,}^{p}^{p}^{p}^{p}^{p}^{p}^{p}^{p}_{19}_{20}_{∂}_{∂}_{∂}_{∃}^{±}^{±}^{±}^{±}^{±}^{±}^{±}^{±}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}_{,}_{,}^{signal}signal_{signal}_{21}_{22}^{{}^{{}^{{}^{{}^{{}^{{}^{{}^{{}^{15}^{17}^{19}^{15}^{17}^{19}^{21}^{21}_{}}_{}}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{16}^{16}^{18}^{18}^{20}^{20}^{22}^{22}^{configurat}configurat_{configurat}^{}}^{}}^{}}^{}}^{}}^{}}^{}}^{}}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{extended}^{normal}^{extended}^{normal}^{extended}^{normal}^{extended}^{normal}^{cyclic}^{cyclic}^{cyclic}^{ions}ions_{ions}^{cyclic}^{cyclic}^{cyclic}^{cyclic}^{cyclic}^{0}_{0}20^{prefix}^{prefix}^{-}_{-}^{prefix}^{prefix}^{19,}_{27,}-^{prefix}^{prefix}^{prefix}^{prefix}31,^{normal}_{extended}normal^{cyclic}cyclic_{cyclic}^{prefix}prefix_{prefix}]

For the case of CDMType equal to CDM4:

![](media_svg/image982.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{&apos;}^{)}=w_{p}_{&apos;}(i)∪r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image983.svg) [公式≈: _{k}_{m}_{l}k_{l}_{i}_{&apos;}_{&quot;}_{&apos;}_{&apos;}=_{=}_{=}_{=}_{=}_{=}_{l}_{0}_{0}k_{2}_{m}_{&apos;}_{,}_{,}_{+}_{k}&apos;_{1}_{1}+_{+}_{&apos;}_{√}_{⌠}_{∞}12_{&apos;}_{+}_{2}_{⋅}_{⋅}_{⋅}_{√}_{l}_{l}_{l}_{&apos;}_{N}m_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{RB}_{max,}−_{CSI}^{√}^{⌡}⌠_{⌡}_{∞}_{CSI}k_{DL}_{6}^{k}&apos;_{2}_{k}&apos;+^{&apos;}_{reference}_{−}_{&apos;}^{&apos;}_{reference}6_{&apos;}_{N}_{RB}_{DL}for ^{for }_{for }_{∂}_{∂}_{∂}_{∃}p^{p}_{p}_{signal}±^{±}_{±}_{signal}⎰^{⎰}_{⎰}{^{{}_{{}17^{15}_{15}^{,},_{,}_{configurat}^{16}18_{16}_{configurat},^{,}_{,}^{19}_{17}21^{,},_{,}_{18}^{20}22_{}}^{}}}_{,}^{,},_{normal}^{normal}normal_{ions}_{ions}_{20}_{0}_{-}_{cyclic}^{cyclic}cyclic_{-}_{19,}_{31,}_{normal}_{normal}_{prefix,}^{prefix,}prefix,_{cyclic}_{cyclic}_{N}^{N}N_{ports}_{CSI}^{ports}ports^{CSI}^{CSI}_{prefix}_{prefix}_{=}^{=}=_{4}^{8}8]

and where ![](media_svg/image984.svg) [公式≈: ^{w}p&apos;^{(}^{i}^{)}] is given by Table 6.10.5.2-0.

Table 6.10.5.2-0: The sequence ![](media_svg/image984.svg) [公式≈: ^{w}p&apos;^{(}^{i}^{)}] for CDM4.

| ![](media_svg/image985.svg) [公式: p^{±}] |  |  |
| --- | --- | --- |
|  |  |  |
| 15 | 15,17 | ![](media_svg/image989.svg) [公式: {1111}] |
| 16 | 16,18 | ![](media_svg/image990.svg) [公式: {1−11−1}] |
| 17 | 19,21 | ![](media_svg/image991.svg) [公式: {11−1−1}] |
| 18 | 20,22 | ![](media_svg/image992.svg) [公式: {1−1−11}] |

If neither of the higher-layer parameters NZP-FrequencyDensity and NZP-TransmissionComb are configured, ![](media_svg/image993.svg) [公式: m=0,1,...,N_{RB}^{DL}−1].

If the UE is configured with one or more of the parameters NZP-FrequencyDensity and NZP-TransmissionComb,

- if either NZP-FrequencyDensity equals 1, ![](media_svg/image993.svg) [公式: m=0,1,...,N_{RB}^{DL}−1]

- if NZP-FrequencyDensity equals 1/2 and NZP-TransmissionComb equals 0, ![](media_svg/image994.svg) [公式≈: m=0,2,...,N_{RB}^{DL}−1−((N_{RB}^{DL}−1)mod2)]

- if NZP-FrequencyDensity equals 1/2 and NZP-TransmissionComb equals 1, ![](media_svg/image995.svg) [公式≈: m=1,3,...,N_{RB}^{DL}-1((N_{RB}^{DL}-2)mod2)]

- if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 0, ![](media_svg/image996.svg) [公式≈: m=0,3,...,N_{RB}^{DL}−1−((N_{RB}^{DL}−1)mod3)]

- if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 1, ![](media_svg/image997.svg) [公式≈: m=1,4,...,N_{RB}^{DL}−1−((N_{RB}^{DL}−2)mod3)]

- if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 2, ![](media_svg/image998.svg) [公式≈: m=2,5,...,N_{RB}^{DL}−1−((N_{RB}^{DL}−3)mod3)]

The quantity ![](media_svg/image999.svg) [公式: (k&apos;,l&apos;)] and the necessary conditions on ![](media_svg/image1000.svg) [公式≈: ^{n}s] are given by Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively.

The relation between the antenna port number ![](media_svg/image1001.svg) [公式: p] and the quantity ![](media_svg/image985.svg) [公式: p^{±}] depends on the number of CSI-RS antenna ports:

- for CSI reference signals using up to eight antenna ports, ![](media_svg/image1002.svg) [公式: p=p±]

- for CSI reference signals using more than eight antenna ports when the higher-layer parameter CDMType equals CDM2

![](media_svg/image1003.svg) [公式≈: ^{p}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}_{⌡}_{∞}^{p}p´^{&apos;}^{+}+^{N}^{N}^{ports}^{ports}^{CSI}^{2}^{CSI}_{2}^{i}(i^{±}±+N_{res}^{CSI}−1)^{for }for ^{p}p^{&apos;}&apos;^{⎰}⎰^{{}{^{15}15^{,...,}+N^{15}_{ports}^{CSI}^{+}^{N}2^{ports}^{CSI},...,15^{2}^{−}+^{1}N^{}}_{ports}^{CSI}−1}]

where ![](media_svg/image1004.svg) [公式: i±⎰{0,1,...,N_{res}^{CSI}−1}] is the CSI-RS resource number.

- for CSI reference signals using more than eight antenna ports when the higher-layer parameter CDMType equals CDM4, antenna port number ![](media_svg/image1005.svg) [公式≈: p=i±N_{ports}^{CSI}+p&apos;] where ![](media_svg/image1006.svg) [公式≈: p&apos;⎰{15,16,..,15+N_{ports}^{CSI}−1}] for CSI-RS resource number ![](media_svg/image1007.svg) [公式: i±⎰{0,1,...,N_{res}^{CSI}−1}].

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 32:

![](media_svg/image1008.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(i)∪r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image1009.svg) [公式≈: _{m}_{m}_{l}^{k}_{q}l_{&quot;}_{&apos;}^{=}=_{=}_{=}_{=}_{=}l_{0}_{0}^{k}_{√}_{⌡}_{⌡}_{⌡}_{⌡}_{⌡}_{⌠}_{⌡}_{⌡}_{⌡}_{⌡}_{⌡}_{∞}_{m}&apos;_{1}_{1}_{,}_{3}_{3}_{,}+_{0}_{0}_{2}_{2}^{&apos;}_{1}_{1}^{+}_{+}_{,...,}^{√}^{⌡}⌠_{⌡}_{∞}^{12}^{l}_{l}2_{⋅}_{⋅}_{⋅}_{√}^{&quot;}_{&quot;}_{if}_{if}_{if}_{if}_{if}_{if}_{if}_{if}l_{N}^{m}&quot;_{N}_{k}_{k}_{k}_{k}_{k}_{k}_{k}_{k}_{RB}_{max,}^{+}_{RB}_{DL}_{−}_{−}_{−}_{−}_{−}_{−}_{−}_{−}^{CSI}CSI_{CSI}^{√}^{⌡}^{⌡}^{⌡}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}^{⌡}^{⌡}^{⌡}^{∞}_{k}_{k}_{k}_{k}_{k}_{k}_{k}_{k}^{−}^{−}^{−}^{−}^{−}^{−}^{−}^{−}_{DL}_{−}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{&apos;}_{−}_{−}_{−}_{−}_{−}_{−}_{−}_{−}_{2}^{1}^{3}^{9}^{0}^{6}^{7}^{0}^{6}_{1}^{reference}reference_{reference}_{12}_{12}_{12}_{12}_{12}_{12}_{12}_{12}_{−}_{N}_{m}_{m}_{m}_{m}_{m}_{m}_{m}_{m}^{for }^{for }^{for }^{for }^{for }^{for }^{for }^{for }_{RB}_{DL}_{=}_{=}_{=}_{=}_{=}_{=}_{=}_{=}^{p}^{p}^{p}^{p}^{p}^{p}^{p}^{p}_{−}_{−}_{−}_{−}_{−}_{−}_{−}_{−}_{∂}_{∂}_{∂}_{∃}^{±}^{±}^{±}^{±}^{±}^{±}^{±}^{±}_{0}_{6}_{1}_{7}_{0}_{3}_{6}_{9}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{⎰}^{signal}signal_{signal}_{,}_{,}_{,}_{,}_{,}_{,}_{,}_{,}_{normal}_{extended}_{extended}_{extended}_{extended}_{normal}_{normal}_{normal}^{{}^{{}^{{}^{{}^{{}^{{}^{{}^{{}^{15}^{17}^{19}^{15}^{17}^{19}^{21}^{21}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{16}^{16}^{18}^{18}^{20}^{20}^{22}^{22}^{configurat}configurat_{configurat}^{}}^{}}^{}}^{}}^{}}^{}}^{}}^{}}^{,}^{,}^{,}^{,}^{,}^{,}^{,}^{,}_{cyclic}_{cyclic}_{cyclic}_{cyclic}^{extended}^{normal}^{extended}^{normal}^{extended}^{normal}^{extended}^{normal}_{cyclic}_{cyclic}_{cyclic}_{cyclic}_{prefix}_{prefix}_{prefix}_{prefix}^{cyclic}^{cyclic}^{cyclic}^{ions}ions_{ions}^{cyclic}_{prefix}_{prefix}_{prefix}_{prefix}^{cyclic}^{cyclic}^{cyclic}^{cyclic}^{0}_{0}20^{prefix}^{prefix}^{-}_{-}^{prefix}^{prefix}^{19,}_{27,}-^{prefix}^{prefix}^{prefix}^{prefix}31,^{normal}_{extended}normal^{cyclic}cyclic_{cyclic}^{prefix}prefix_{prefix}]

The resource elements for the ![](media_svg/image1010.svg) [公式≈: _{q}th] CDM8 pattern, where ![](media_svg/image1011.svg) [公式: q=0,1,2,3], are determined by aggregating pairs of resource elements ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1013.svg) [公式: q=q] from the ![](media_svg/image1014.svg) [公式≈: _{N}_{res}CSI] aggregated CSI-RS configurations, where at most one pair of resource elements is drawn from each of the ![](media_svg/image1014.svg) [公式≈: _{N}_{res}CSI] aggregated CSI-RS configurations. For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 32, the aggregated CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix are restricted to one of ![](media_svg/image1015.svg) [公式: {0,1,2,3}], ![](media_svg/image1016.svg) [公式: {0,2,3,4}], or ![](media_svg/image1017.svg) [公式: {1,2,3,4}]. Antenna port number ![](media_svg/image1018.svg) [公式≈: p=i±N_{ports}^{CSI}+p&apos;] where ![](media_svg/image1019.svg) [公式≈: p&apos;⎰{15,16,..,15+N_{ports}^{CSI}−1}] for CSI-RS resource number ![](media_svg/image1020.svg) [公式: i±⎰{0,1,...,N_{res}^{CSI}−1}]. The sequence![](media_svg/image1021.svg) [公式: w_{p}(i)] is given by Table 6.10.5.2-0A, where ![](media_svg/image1022.svg) [公式: i=2i±+l&apos;&apos;].

Table 6.10.5.2-0A: The sequence ![](media_svg/image1023.svg) [公式: w_{p}(i)] for CDM8 with 32 CSI-RS antenna ports.

| ![](media_svg/image1024.svg) [公式: p] | ![](media_svg/image1025.svg) [公式≈: [w_{p}(0)w_{p}(1)w_{p}(2)w_{p}(3)w_{p}(4)w_{p}(5)w_{p}(6)w_{p}(7)]] |
| --- | --- |
| 15, 17, 19, 21 | ![](media_svg/image1026.svg) [公式: {11111111}] |
| 16, 18, 20, 22 | ![](media_svg/image1027.svg) [公式: {1−11−11−11−1}] |
| 23, 25, 27, 29 | ![](media_svg/image1028.svg) [公式: {11−1−111−1−1}] |
| 24, 26, 28, 30 | ![](media_svg/image1029.svg) [公式: {1−1−111−1−11}] |
| 31, 33, 35, 37 | ![](media_svg/image1030.svg) [公式: {1111−1−1−1−1}] |
| 32, 34, 36, 38 | ![](media_svg/image1031.svg) [公式: {1−11−1−11−11}] |
| 39, 41, 43, 45 | ![](media_svg/image1032.svg) [公式: {11−1−1−1−111}] |
| 40, 42, 44, 46 | ![](media_svg/image1033.svg) [公式: {1−1−11−111−1}] |

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24:

![](media_svg/image1008.svg) [公式≈: a_{k}^{(}_{,}^{p}_{l}^{)}=w_{p}(i)∪r_{l}_{,}_{n}_{s}(m&apos;)]

where

![](media_svg/image1034.svg) [公式≈: _{k}_{m}_{m}_{l}^{k}_{q}^{l}_{&apos;}_{&quot;}_{&apos;}_{&apos;}^{=}^{=}_{=}_{=}_{=}_{=}_{=}^{l}_{0}_{0}_{0}^{k}_{√}_{⌠}_{∞}_{m}^{&apos;}_{,}_{,}_{,}_{1}^{+}_{0}^{&apos;}_{1}_{1}_{1}^{+}_{+}_{,...,}^{√}^{⌠}_{∞}^{12}2_{⋅}_{⋅}_{⋅}_{√}^{l}_{if}l_{if}^{&apos;}_{N}^{m}&apos;^{&apos;}_{N}&apos;_{k}_{RB}_{k}_{max,}^{−}_{RB}_{DL}_{−}_{−}CSI^{√}^{⌡}^{⌠}^{⌡}^{∞}^{CSI}_{k}^{k}_{k}_{DL}_{−}_{&apos;}^{k}^{&apos;}_{−}_{&apos;}_{2}_{1}_{−}^{&apos;}^{+}^{&apos;}_{12}reference_{−}_{12}^{&apos;}^{reference}^{6}_{N}_{m}_{m}_{RB}_{DL}^{for }^{for }_{+}_{+}_{k}_{k}_{∂}_{∂}_{∂}_{∃}_{&apos;}^{p}^{p}_{&apos;}_{&apos;}_{&apos;}_{=}signal^{±}^{±}_{=}^{signal}^{⎰}^{⎰}_{−}_{0}^{{}^{{}_{6}_{,}^{17}^{15}_{,}_{normal}_{normal}^{,}^{,}configurat^{16}^{18}^{configurat}^{,}^{,}^{19}^{21}^{,}^{,}_{cyclic}^{20}^{22}_{cyclic}^{}}^{}}^{,}^{,}^{normal}^{normal}ions^{ions}_{prefix,}_{prefix}20^{0}^{-}^{cyclic}^{cyclic}-^{19,}31,^{normal}normal^{prefix,}^{prefix,}^{cyclic}cyclic^{N}^{N}^{ports}^{ports}^{CSI}^{CSI}^{prefix}prefix^{=}^{=}^{8}^{8}]

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24, the aggregated CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix are restricted to ![](media_svg/image1035.svg) [公式: {1,2,3}] in that order. Resource elements for CDM8 patterns are determined as follows:

- Aggregating resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 1 with resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 2

- Aggregating resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 3 with resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1037.svg) [公式: q=1] from CSI-RS configuration 1

- Aggregating resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1037.svg) [公式: q=1] from CSI-RS configuration 2 with resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1037.svg) [公式: q=1] from CSI-RS configuration 3

Antenna port number ![](media_svg/image1038.svg) [公式≈: p=i±N_{ports}^{CSI}+p&apos;] where ![](media_svg/image1006.svg) [公式≈: p&apos;⎰{15,16,..,15+N_{ports}^{CSI}−1}] for CSI-RS resource number ![](media_svg/image1039.svg) [公式: i±⎰{0,1,...,N_{res}^{CSI}−1}]. The sequence![](media_svg/image1023.svg) [公式: w_{p}(i)] is given by Table 6.10.5.2-0B. The sequence index  is determined as follows:

- For resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 1, resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying  from CSI-RS configuration 2, or resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 3, .

- For resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying  from CSI-RS configuration 1, resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying ![](media_svg/image1036.svg) [公式: q=0] from CSI-RS configuration 2, or resource element quadruplet ![](media_svg/image1012.svg) [公式: (k,l)] satisfying  from CSI-RS configuration 3, .

Table 6.10.5.2-0B: The sequence ![](media_svg/image1023.svg) [公式: w_{p}(i)] for CDM8 with 24 CSI-RS antenna ports.

| ![](media_svg/image1024.svg) [公式: p] | ![](media_svg/image1025.svg) [公式≈: [w_{p}(0)w_{p}(1)w_{p}(2)w_{p}(3)w_{p}(4)w_{p}(5)w_{p}(6)w_{p}(7)]] |
| --- | --- |
| 15, 25, 31 | ![](media_svg/image1026.svg) [公式: {11111111}] |
| 16, 26, 32 | ![](media_svg/image1027.svg) [公式: {1−11−11−11−1}] |
| 19, 29, 35 | ![](media_svg/image1028.svg) [公式: {11−1−111−1−1}] |
| 20, 30, 36 | ![](media_svg/image1029.svg) [公式: {1−1−111−1−11}] |
| 17, 23, 33 | ![](media_svg/image1030.svg) [公式: {1111−1−1−1−1}] |
| 18, 24, 34 | ![](media_svg/image1031.svg) [公式: {1−11−1−11−11}] |
| 21, 27, 37 | ![](media_svg/image1032.svg) [公式: {11−1−1−1−111}] |
| 22, 28, 38 | ![](media_svg/image1033.svg) [公式: {1−1−11−111−1}] |

Multiple CSI reference signal configurations can be used in a given cell. A UE can be configured with multiple sets of CSI reference signals,

- one or more configurations for CSI reporting for which the UE shall assume non-zero transmission power for the CSI-RS, and

- zero or more configurations for which the UE shall assume zero transmission power, and

- zero or more configurations valid across the system downlink bandwidth as part of the discovery signals for which the UE shall assume non-zero transmission power for the CSI-RS.

The CSI-RS configurations for which the UE shall assume non-zero transmission power are provided by higher layers.

The CSI-RS configurations for which the UE shall assume zero transmission power in a subframe are given by a bitmap derived according to clause 7.2.7 in TS 36.213 [4]. For each bit set to one in the 16-bit bitmap, the UE shall assume zero transmission power for the resource elements corresponding to the four CSI reference signal column in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively, except for resource elements that overlap with those for which the UE shall assume non-zero transmission power CSI-RS as configured by higher layers. The most significant bit corresponds to the lowest CSI reference signal configuration index and subsequent bits in the bitmap correspond to configurations with indices in increasing order.

CSI reference signals not corresponding to higher layer configured parameters csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList can only occur in

- downlink slots where ![](media_svg/image1044.svg) [公式: n_{s}mod2] fulfils the condition in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively, and

- where the subframe number fulfils the conditions in clause 6.10.5.3.

CSI reference signals corresponding to either higher layer configured parameter csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList can only occur in

- downlink slots where ![](media_svg/image1044.svg) [公式: n_{s}mod2] fulfils the condition in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively.

The UE shall assume that CSI reference signals are not transmitted

- in the DwPTS for special subframe configuration 0, 5, 9 and 10 for normal cyclic prefix and special subframe configuration 0, 4 and 7 for extended cyclic prefix, in case of frame structure type 2,

- in the DwPTS for normal CP for the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24,

- in subframes where PDSCH/EPDCCH transmission starts in the second slot of a subframe for frame structure type 3,

- in subframes where PDSCH/EPDCCH transmission ends prior to the end of a subframe for frame structure type 3,

- in an empty subframe where there is no PDSCH or discovery signal transmission for frame structure type 3,

- in subframes where transmission of a CSI-RS would collide with SystemInformationBlockType1 messages,

- in the primary cell in subframes configured for transmission of paging messages in the primary cell for any UE with the cell-specific paging configuration.

For special subframe configuration {1, 2, 6, or 7}, a UE does not expect to be configured with one of CSI-RS configurations {1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17} in DwPTS for normal CP.

The UE shall assume that none of the CSI reference signals corresponding to a CSI reference signal configuration are transmitted in subframes where transmission of any of those CSI reference signals would collide with transmission of synchronization signals or the core part of PBCH.

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of CSI reference signals on any of the antenna ports in the set ![](media_svg/image872.svg) [公式: S], where ![](media_svg/image1045.svg) [公式: S={15}], ![](media_svg/image1046.svg) [公式: S={15,16}], ![](media_svg/image1047.svg) [公式: S={17,18}], ![](media_svg/image1048.svg) [公式: S={19,20}], ![](media_svg/image1049.svg) [公式: S={21,22}], ![](media_svg/image1050.svg) [公式: S={23,24}], ![](media_svg/image1051.svg) [公式: S={25,26}], ![](media_svg/image1052.svg) [公式: S={27,28}], ![](media_svg/image1053.svg) [公式: S={29,30}], ![](media_svg/image1054.svg) [公式: S={31,32}], ![](media_svg/image1055.svg) [公式: S={33,34}], ![](media_svg/image1056.svg) [公式: S={35,36}], ![](media_svg/image1057.svg) [公式: S={37,38}], ![](media_svg/image1058.svg) [公式: S={39,40}], ![](media_svg/image1059.svg) [公式: S={41,42}], ![](media_svg/image1060.svg) [公式: S={43,44}] or ![](media_svg/image1061.svg) [公式: S={45,46}] shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is not configured, or is configured to CDM2.

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of CSI reference signals on any of the antenna ports in the set ![](media_svg/image872.svg) [公式: S], where

- ![](media_svg/image1062.svg) [公式: S={15,16,17,18}], ![](media_svg/image1063.svg) [公式: S={19,20,21,22}] or ![](media_svg/image1064.svg) [公式: S={23,24,25,26}] for CSI reference signals on 12 ports, or

- ![](media_svg/image1065.svg) [公式: S={15,16,19,20}], ![](media_svg/image1066.svg) [公式: S={17,18,21,22}], ![](media_svg/image1067.svg) [公式: S={23,24,27,28}] or ![](media_svg/image1068.svg) [公式: S={25,26,29,30}] for CSI reference signals on 16 ports, or

- ![](media_svg/image1062.svg) [公式: S={15,16,17,18}], ![](media_svg/image1063.svg) [公式: S={19,20,21,22}], ![](media_svg/image1064.svg) [公式: S={23,24,25,26}], ![](media_svg/image1069.svg) [公式: S={27,28,29,30}] or![](media_svg/image1070.svg) [公式: S={31,32,33,34}] for CSI reference signals on 20 ports, or

- ![](media_svg/image1065.svg) [公式: S={15,16,19,20}], ![](media_svg/image1066.svg) [公式: S={17,18,21,22}], ![](media_svg/image1067.svg) [公式: S={23,24,27,28}], ![](media_svg/image1068.svg) [公式: S={25,26,29,30}], ![](media_svg/image1071.svg) [公式: S={31,32,35,36}] or ![](media_svg/image1072.svg) [公式: S={33,34,37,38}] for CSI reference signals on 24 ports, or

- ![](media_svg/image1062.svg) [公式: S={15,16,17,18}], ![](media_svg/image1063.svg) [公式: S={19,20,21,22}], ![](media_svg/image1064.svg) [公式: S={23,24,25,26}], ![](media_svg/image1069.svg) [公式: S={27,28,29,30}],![](media_svg/image1070.svg) [公式: S={31,32,33,34}], ![](media_svg/image1073.svg) [公式: S={35,36,37,38}] or ![](media_svg/image1074.svg) [公式: S={39,40,41,42}] for CSI reference signals on 28 ports, or

- ![](media_svg/image1065.svg) [公式: S={15,16,19,20}], ![](media_svg/image1066.svg) [公式: S={17,18,21,22}], ![](media_svg/image1067.svg) [公式: S={23,24,27,28}], ![](media_svg/image1068.svg) [公式: S={25,26,29,30}], ![](media_svg/image1071.svg) [公式: S={31,32,35,36}], ![](media_svg/image1072.svg) [公式: S={33,34,37,38}], ![](media_svg/image1075.svg) [公式: S={39,40,43,44}] or ![](media_svg/image1076.svg) [公式: S={41,42,45,46}] for CSI reference signals on 32 ports

shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is configured to CDM4.

Resource elements ![](media_svg/image764.svg) [公式: (k,l)] used for transmission of CSI reference signals on any of the antenna ports in the set ![](media_svg/image872.svg) [公式: S], where

- ![](media_svg/image1077.svg) [公式: S={15,16,19,20,23,24,27,28}], ![](media_svg/image1078.svg) [公式: S={17,18,21,22,31,32,35,36}] or ![](media_svg/image1079.svg) [公式: S={25,26,29,30,33,34,37,38}] for CSI reference signals on 24 ports, or

- ![](media_svg/image1080.svg) [公式: S={15,16,23,24,31,32,39,40}], ![](media_svg/image1081.svg) [公式: S={17,18,25,26,33,34,41,42}], ![](media_svg/image1082.svg) [公式: S={19,20,27,28,35,36,43,44}] or ![](media_svg/image1083.svg) [公式: S={21,22,29,30,37,38,45,46}] for CSI reference signals on 32 ports

shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is configured to CDM8.

The mapping for CSI reference signal configuration 0 is illustrated in Figures 6.10.5.2-1 and 6.10.5.2-2.

Table 6.10.5.2-1: Mapping from CSI reference signal configuration to ![](media_svg/image999.svg) [公式: (k&apos;,l&apos;)] for normal cyclic prefix

| CSI-RS config. | Number of CSI reference signals configured |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 or 2 |  |  |  | 4 |  |  |  | 8 |  |  |  |
|  | Normal subframe |  | Special subframe |  | Normal subframe |  | Special subframe |  | Normal subframe |  | Special subframe |  |
|  | ![](media_svg/image1084.svg) [公式: (k&apos;,l&apos;)] |  |  |  |  |  |  |  |  |  |  |  |
| 0 | (9,5) | 0 | (9,5) | 0 | (9,5) | 0 | (9,5) | 0 | (9,5) | 0 | (9,5) | 0 |
| 1 | (11,2) | 1 | (11,5) | 0 | (11,2) | 1 | (11,5) | 0 | (11,2) | 1 | (11,5) | 0 |
| 2 | (9,2) | 1 | (9,2) | 1 | (9,2) | 1 | (9,2) | 1 | (9,2) | 1 | (9,2) | 1 |
| 3 | (7,2) | 1 | (7,5) | 0 | (7,2) | 1 | (7,5) | 0 | (7,2) | 1 | (7,5) | 0 |
| 4 | (9,5) | 1 |  |  | (9,5) | 1 |  |  | (9,5) | 1 |  |  |
| 5 | (8,5) | 0 | (8,5) | 0 | (8,5) | 0 | (8,5) | 0 |  |  |  |  |
| 6 | (10,2) | 1 | (10,5) | 0 | (10,2) | 1 | (10,5) | 0 |  |  |  |  |
| 7 | (8,2) | 1 | (8,2) | 1 | (8,2) | 1 | (8,2) | 1 |  |  |  |  |
| 8 | (6,2) | 1 | (6,5) | 0 | (6,2) | 1 | (6,5) | 0 |  |  |  |  |
| 9 | (8,5) | 1 |  |  | (8,5) | 1 |  |  |  |  |  |  |
| 10 | (3,5) | 0 | (3,5) | 0 |  |  |  |  |  |  |  |  |
| 11 | (2,5) | 0 | (2,5) | 0 |  |  |  |  |  |  |  |  |
| 12 | (5,2) | 1 | (5,5) | 0 |  |  |  |  |  |  |  |  |
| 13 | (4,2) | 1 | (4,5) | 0 |  |  |  |  |  |  |  |  |
| 14 | (3,2) | 1 | (3,2) | 1 |  |  |  |  |  |  |  |  |
| 15 | (2,2) | 1 | (2,2) | 1 |  |  |  |  |  |  |  |  |
| 16 | (1,2) | 1 | (1,5) | 0 |  |  |  |  |  |  |  |  |
| 17 | (0,2) | 1 | (0,5) | 0 |  |  |  |  |  |  |  |  |
| 18 | (3,5) | 1 |  |  |  |  |  |  |  |  |  |  |
| 19 | (2,5) | 1 |  |  |  |  |  |  |  |  |  |  |
| 20 | (11,1) | 1 |  |  | (11,1) | 1 |  |  | (11,1) | 1 |  |  |
| 21 | (9,1) | 1 |  |  | (9,1) | 1 |  |  | (9,1) | 1 |  |  |
| 22 | (7,1) | 1 |  |  | (7,1) | 1 |  |  | (7,1) | 1 |  |  |
| 23 | (10,1) | 1 |  |  | (10,1) | 1 |  |  |  |  |  |  |
| 24 | (8,1) | 1 |  |  | (8,1) | 1 |  |  |  |  |  |  |
| 25 | (6,1) | 1 |  |  | (6,1) | 1 |  |  |  |  |  |  |
| 26 | (5,1) | 1 |  |  |  |  |  |  |  |  |  |  |
| 27 | (4,1) | 1 |  |  |  |  |  |  |  |  |  |  |
| 28 | (3,1) | 1 |  |  |  |  |  |  |  |  |  |  |
| 29 | (2,1) | 1 |  |  |  |  |  |  |  |  |  |  |
| 30 | (1,1) | 1 |  |  |  |  |  |  |  |  |  |  |
| 31 | (0,1) | 1 |  |  |  |  |  |  |  |  |  |  |

Note: ![](media_svg/image1088.svg) [公式: n_{s}±=n_{s}mod2]. Configurations 0 – 19 for normal subframes are available for frame structure types 1, 2 and 3. Configurations 20 – 31 and configurations for special subframes are available for frame structure type 2 only.

Table 6.10.5.2-2: Mapping from CSI reference signal configuration to ![](media_svg/image999.svg) [公式: (k&apos;,l&apos;)] for extended cyclic prefix.

| CSI-RS config. | Number of CSI reference signals configured |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 or 2 |  |  |  | 4 |  |  |  | 8 |  |  |  |
|  | Normal subframe |  | Special subframe |  | Normal subframe |  | Special subframe |  | Normal Subframe |  | Special subframe |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | (11,4) | 0 | (11,4) | 0 | (11,4) | 0 | (11,4) | 0 | (11,4) | 0 | (11,4) | 0 |
| 1 | (9,4) | 0 | (9,4) | 0 | (9,4) | 0 | (9,4) | 0 | (9,4) | 0 | (9,4) | 0 |
| 2 | (10,4) | 1 |  |  | (10,4) | 1 |  |  | (10,4) | 1 |  |  |
| 3 | (9,4) | 1 |  |  | (9,4) | 1 |  |  | (9,4) | 1 |  |  |
| 4 | (5,4) | 0 | (5,4) | 0 | (5,4) | 0 | (5,4) | 0 |  |  |  |  |
| 5 | (3,4) | 0 | (3,4) | 0 | (3,4) | 0 | (3,4) | 0 |  |  |  |  |
| 6 | (4,4) | 1 |  |  | (4,4) | 1 |  |  |  |  |  |  |
| 7 | (3,4) | 1 |  |  | (3,4) | 1 |  |  |  |  |  |  |
| 8 | (8,4) | 0 | (8,4) | 0 |  |  |  |  |  |  |  |  |
| 9 | (6,4) | 0 | (6,4) | 0 |  |  |  |  |  |  |  |  |
| 10 | (2,4) | 0 | (2,4) | 0 |  |  |  |  |  |  |  |  |
| 11 | (0,4) | 0 | (0,4) | 0 |  |  |  |  |  |  |  |  |
| 12 | (7,4) | 1 |  |  |  |  |  |  |  |  |  |  |
| 13 | (6,4) | 1 |  |  |  |  |  |  |  |  |  |  |
| 14 | (1,4) | 1 |  |  |  |  |  |  |  |  |  |  |
| 15 | (0,4) | 1 |  |  |  |  |  |  |  |  |  |  |
| 16 | (11,1) | 1 | (11,1) | 1 | (11,1) | 1 | (11,1) | 1 | (11,1) | 1 | (11,1) | 1 |
| 17 | (10,1) | 1 | (10,1) | 1 | (10,1) | 1 | (10,1) | 1 | (10,1) | 1 | (10,1) | 1 |
| 18 | (9,1) | 1 | (9,1) | 1 | (9,1) | 1 | (9,1) | 1 | (9,1) | 1 | (9,1) | 1 |
| 19 | (5,1) | 1 | (5,1) | 1 | (5,1) | 1 | (5,1) | 1 |  |  |  |  |
| 20 | (4,1) | 1 | (4,1) | 1 | (4,1) | 1 | (4,1) | 1 |  |  |  |  |
| 21 | (3,1) | 1 | (3,1) | 1 | (3,1) | 1 | (3,1) | 1 |  |  |  |  |
| 22 | (8,1) | 1 | (8,1) | 1 |  |  |  |  |  |  |  |  |
| 23 | (7,1) | 1 | (7,1) | 1 |  |  |  |  |  |  |  |  |
| 24 | (6,1) | 1 | (6,1) | 1 |  |  |  |  |  |  |  |  |
| 25 | (2,1) | 1 | (2,1) | 1 |  |  |  |  |  |  |  |  |
| 26 | (1,1) | 1 | (1,1) | 1 |  |  |  |  |  |  |  |  |
| 27 | (0,1) | 1 | (0,1) | 1 |  |  |  |  |  |  |  |  |

Note: ![](media_svg/image1088.svg) [公式: n_{s}±=n_{s}mod2]. Configurations 0 – 15 for normal subframes are available for both frame structure type 1 and type 2. Configurations 16 – 27 and configurations for special subframes are available for frame structure type 2 only.

![](media/image1089.emf)

Figure 6.10.5.2-1: Mapping of CSI reference signals (CSI configuration 0, normal cyclic prefix)

![](media/image1090.emf)

Figure 6.10.5.2-2: Mapping of CSI reference signals (CSI configuration 0, extended cyclic prefix)

#### 6.10.5.3 CSI reference signal subframe configuration

The subframe configuration period ![](media_svg/image1091.svg) [公式≈: ^{T}CSI-RS] and the subframe offset ![](media_svg/image1092.svg) [公式≈: ^{δ}CSI-RS] for the occurence of CSI reference signals are listed in Table 6.10.5.3-1. The parameter ![](media_svg/image1093.svg) [公式≈: ^{I}CSI−RS] can be configured separately for CSI reference signals for which the UE shall assume non-zero and zero transmission power. Subframes containing CSI reference signals that do not correspond to either higher layer configured parameter csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList shall satisfy ![](media_svg/image1094.svg) [公式≈: ^{(}^{10}^{n}f^{+}√^{n}s^{2}∃^{−}^{δ}CSI−RS^{)}^{mod}^{T}CSI−RS^{=}^{0}].

Table 6.10.5.3-1: CSI reference signal subframe configuration

| CSI-RS-SubframeConfig ![](media_svg/image1093.svg) [公式≈: ^{I}CSI−RS] | CSI-RS periodicity ![](media_svg/image1091.svg) [公式≈: ^{T}CSI-RS](subframes) | CSI-RS subframe offset ![](media_svg/image1092.svg) [公式≈: ^{δ}CSI-RS](subframes) |
| --- | --- | --- |
| 0 – 4 | 5 | ![](media_svg/image1093.svg) [公式≈: ^{I}CSI−RS] |
| 5 – 14 | 10 | ![](media_svg/image1095.svg) [公式≈: ^{I}CSI−RS^{−}^{5}] |
| 15 – 34 | 20 | ![](media_svg/image1096.svg) [公式≈: ^{I}CSI−RS^{−}^{15}] |
| 35 – 74 | 40 | ![](media_svg/image1097.svg) [公式≈: ^{I}CSI−RS^{−}^{35}] |
| 75 – 154 | 80 | ![](media_svg/image1098.svg) [公式≈: ^{I}CSI−RS^{−}^{75}] |

## 6.11 Synchronization signals

There are 504 unique physical-layer cell identities. The physical-layer cell identities are grouped into 168 unique physical-layer cell-identity groups, each group containing three unique identities. The grouping is such that each physical-layer cell identity is part of one and only one physical-layer cell-identity group. A physical-layer cell identity ![](media_svg/image1099.svg) [公式≈: _{N}_{ID}cell_{=}_{3}_{N}_{ID}(1)_{+}_{N}_{ID}(2)]is thus uniquely defined by a number![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)]in the range of 0 to 167, representing the physical-layer cell-identity group, and a number![](media_svg/image1101.svg) [公式≈: _{N}_{ID}(2)] in the range of 0 to 2, representing the physical-layer identity within the physical-layer cell-identity group.

### 6.11.1 Primary synchronization signal (PSS)

#### 6.11.1.1 Sequence generation

The sequence ![](media_svg/image1102.svg) [公式: d(n)] used for the primary synchronization signal is generated from a frequency-domain Zadoff-Chu sequence according to

![](media_svg/image1103.svg) [公式≈: du(n)=^{√}^{⌡}⌠_{⌡}_{∞}_{e}_{−}^{e}_{j}^{−}Πu^{j}^{Π}(n^{un}+^{63}_{63}^{(}1^{n})(^{+}n^{1}+^{)}2)_{n}^{n}_{=}^{=}_{31}^{0}_{,}^{,}_{32}^{1}^{,...,}_{,...,}^{30}_{61}]

where the Zadoff-Chu root sequence index ![](media_svg/image1104.svg) [公式: u] is given by Table 6.11.1.1-1.

Table 6.11.1.1-1: Root indices for the primary synchronization signal

| ![](media_svg/image1101.svg) [公式≈: _{N}_{ID}(2)] | Root index ![](media_svg/image1104.svg) [公式: u] |
| --- | --- |
| 0 | 25 |
| 1 | 29 |
| 2 | 34 |

#### 6.11.1.2 Mapping to resource elements

The mapping of the sequence to resource elements depends on the frame structure. The UE shall not assume that the primary synchronization signal is transmitted on the same antenna port as any of the downlink reference signals. The UE shall not assume that any transmission instance of the primary synchronization signal is transmitted on the same antenna port, or ports, used for any other transmission instance of the primary synchronization signal.

The sequence ![](media_svg/image1105.svg) [公式: d(n)] shall be mapped to the resource elements according to

![](media_svg/image1106.svg) [公式≈: a_{k}_{,}_{k}_{l}=_{=}d_{n}(_{−}n_{31}),_{+}_{N}_{RB}_{DL}n_{2}=_{N}0_{sc}_{RB},...,61]

For frame structure type 1, the primary synchronization signal shall be mapped to the last OFDM symbol in slots 0 and 10.

For frame structure type 2, the primary synchronization signal shall be mapped to the third OFDM symbol in subframes 1 and 6. Resource elements ![](media_svg/image46.svg) [公式: (k,l)] in the OFDM symbols used for transmission of the primary synchronization signal where

![](media_svg/image1107.svg) [公式≈: ^{k}n^{=}=^{n}−5^{−},−^{31}4,...,^{+}^{N}−^{RB}1^{DL},62^{2}^{N},^{sc}63^{RB},...66]

are reserved and not used for transmission of the primary synchronization signal.

For frame structure type 3, the primary synchronization signal shall be mapped according to frame structure type 1 with the following exceptions:

- the primary synchronization signal shall be transmitted only if the corresponding subframe is non-empty and at least 12 OFDM symbols are transmitted,

- a primary synchronization signal being part of a discovery signal shall be transmitted in the last OFDM symbol of the first slot of a discovery signal occasion.

For an MBMS-dedicated cell, the primary synchronization signal shall be mapped according to frame structure type 1 with following exception:

- the primary synchronization signal shall be transmitted in slot 0 in subframes fulfilling ![](media_svg/image1108.svg) [公式: n_{f}mod4=0] only.

For an MBMS-dedicated cell configured with CAS muting, the primary synchronization signal shall only be transmitted in the first $ 4K_{CAS}$ frames, starting in frames fulfilling $ n_{f}mod16N_{CAS}=0 $ where $ N_{CAS}\in  \left \{ 2, 4, 8, 16\right \} $ and $ K_{CAS}\in  \left \{ 4, 5, 6, \ldots  , 63\right \} $ are given by the higher-layer parameter cas-MutingConfig.

### 6.11.2 Secondary synchronization signal (SSS)

#### 6.11.2.1 Sequence generation

The sequence ![](media_svg/image1109.svg) [公式: d(0),...,d(61)]used for the second synchronization signal is an interleaved concatenation of two length-31 binary sequences. The concatenated sequence is scrambled with a scrambling sequence given by the primary synchronization signal.

The combination of two length-31 sequences defining the secondary synchronization signal differs between subframes according to

![](media_svg/image1110.svg) [公式≈: _{d}_{(}_{2}^{d}_{n}^{(}_{+}^{2}^{n}_{1}^{)}_{)}^{=}_{=}^{√}^{⌡}^{⌠}^{⌡}^{∞}^{√}⌡_{⌠}_{⌡}_{∞}^{s}^{s}s_{s}^{1}_{1}^{0}_{0}^{(}^{(}^{(}_{(}^{m}^{m}^{m}_{m}^{1}^{1}^{0}_{0}^{)}^{)}^{)}_{)}^{(}(^{(}_{(}^{n}n^{n}_{n}^{)})^{)}_{)}^{c}c^{c}_{c}_{1}^{0}_{1}^{0}(_{(}^{(}^{(}n_{n}^{n}^{n})_{)}^{)}^{)}z_{z}_{1}_{1}^{(}_{(}^{m}_{m}^{in }^{in }^{0}_{1}^{)}_{)}(_{(}^{subframes}^{subframes}n_{n})_{)}in _{in }subframes_{subframes}^{5,}^{0,}^{1,}^{6,}^{2,}^{7,}^{3,}^{8,}_{5,}0,^{4}^{9}1,_{6,}2,_{7,}3,_{8,}4_{9}]

where ![](media_svg/image1111.svg) [公式: 0≥n≥30]. The indices ![](media_svg/image1112.svg) [公式≈: ^{m}0] and ![](media_svg/image1113.svg) [公式≈: ^{m}1] are derived from the physical-layer cell-identity group ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] according to

![](media_svg/image1114.svg) [公式≈: ^{m}^{m}m^{1}^{0}±=^{=}^{=}N^{(}^{m}^{m}ID^{(1)}^{±}^{0}^{mod}^{+}+^{√}q^{m}^{31}(^{±}q^{31}+1^{∃})^{+}2^{1}^{)},^{mod}q=^{31}^{⋅}⋅_{⋅}_{√}^{N}^{ID}^{(1)}^{+}^{q}_{30}^{±}^{(}^{q}^{±}^{+}^{1}^{)}^{2}^{∂}∂_{∂}_{∃},q±=√NID^{(1)}30∃]

where the output of the above expression is listed in Table 6.11.2.1-1.

The two sequences ![](media_svg/image1115.svg) [公式≈: s_{0}^{(}^{m}^{0}^{)}(n)] and ![](media_svg/image1116.svg) [公式≈: s_{1}^{(}^{m}^{1}^{)}(n)] are defined as two different cyclic shifts of the m-sequence ![](media_svg/image1117.svg) [公式≈: ^{~}s(n)] according to

![](media_svg/image1118.svg) [公式≈: s_{s}_{1}_{0}^{(}_{(}^{m}_{m}_{1}^{0}_{)}^{)}_{(}(_{n}n_{)})_{=}=_{~}_{s}^{~}s_{(}(_{(}(_{n}n_{+}+_{m}m_{1}_{0}_{)})_{mod}mod_{31}31_{)})]

where![](media_svg/image1119.svg) [公式≈: ^{~}s(i)=1−2x(i)], ![](media_svg/image1120.svg) [公式: 0≥i≥30], is defined by

![](media_svg/image1121.svg) [公式: x(i+5)=(x(i+2)+x(i))mod2,0≥i≥25]

with initial conditions![](media_svg/image1122.svg) [公式: x(0)=0,x(1)=0,x(2)=0,x(3)=0,x(4)=1].

The two scrambling sequences ![](media_svg/image1123.svg) [公式: c_{0}(n)] and ![](media_svg/image1124.svg) [公式: c_{1}(n)] depend on the primary synchronization signal and are defined by two different cyclic shifts of the m-sequence ![](media_svg/image1125.svg) [公式: c^{~}(n)] according to

![](media_svg/image1126.svg) [公式≈: ^{c}c_{1}^{0}(^{(}n^{n})^{)}=^{=}c^{~}^{c}^{~}((^{((}n^{n}+^{+}N^{N}_{ID}^{(}^{ID}^{(}^{2}^{2}^{)}^{)}^{)}+^{mod}3)mod^{31}^{)}31)]

where ![](media_svg/image1127.svg) [公式≈: N_{ID}^{(}^{2}^{)}⎰{0,1,2}] is the physical-layer identity within the physical-layer cell identity group ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] and ![](media_svg/image1128.svg) [公式: c^{~}(i)=1−2x(i)], ![](media_svg/image1120.svg) [公式: 0≥i≥30], is defined by

![](media_svg/image1129.svg) [公式: x(i+5)=(x(i+3)+x(i))mod2,0≥i≥25]

with initial conditions ![](media_svg/image1130.svg) [公式: x(0)=0,x(1)=0,x(2)=0,x(3)=0,x(4)=1].

The scrambling sequences ![](media_svg/image1131.svg) [公式≈: z_{1}^{(}^{m}^{0}^{)}(n)] and ![](media_svg/image1132.svg) [公式≈: z_{1}^{(}^{m}^{1}^{)}(n)] are defined by a cyclic shift of the m-sequence ![](media_svg/image1133.svg) [公式≈: ^{~}z(n)] according to

![](media_svg/image1134.svg) [公式≈: z_{1}^{(}^{m}^{0}^{)}(n)=^{~}z((n+(m_{0}mod8))mod31)]

![](media_svg/image1135.svg) [公式≈: z_{1}^{(}^{m}^{1}^{)}(n)=^{~}z((n+(m_{1}mod8))mod31)]

where ![](media_svg/image1112.svg) [公式≈: ^{m}0] and ![](media_svg/image1113.svg) [公式≈: ^{m}1] are obtained from Table 6.11.2.1-1 and ![](media_svg/image1136.svg) [公式≈: ^{~}z(i)=1−2x(i)], ![](media_svg/image1120.svg) [公式: 0≥i≥30], is defined by

![](media_svg/image1137.svg) [公式: x(i+5)=(x(i+4)+x(i+2)+x(i+1)+x(i))mod2,0≥i≥25]

with initial conditions ![](media_svg/image1138.svg) [公式: x(0)=0,x(1)=0,x(2)=0,x(3)=0,x(4)=1].

Table 6.11.2.1-1: Mapping between physical-layer cell-identity group ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] and the indices ![](media_svg/image1112.svg) [公式≈: ^{m}0] and ![](media_svg/image1113.svg) [公式≈: ^{m}1]

| ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] | ![](media_svg/image1112.svg) [公式≈: ^{m}0] | ![](media_svg/image1113.svg) [公式≈: ^{m}1] | ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] | ![](media_svg/image1112.svg) [公式≈: ^{m}0] | ![](media_svg/image1113.svg) [公式≈: ^{m}1] | ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] | ![](media_svg/image1112.svg) [公式≈: ^{m}0] | ![](media_svg/image1113.svg) [公式≈: ^{m}1] | ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] | ![](media_svg/image1112.svg) [公式≈: ^{m}0] | ![](media_svg/image1113.svg) [公式≈: ^{m}1] | ![](media_svg/image1100.svg) [公式≈: _{N}_{ID}(1)] | ![](media_svg/image1112.svg) [公式≈: ^{m}0] | ![](media_svg/image1113.svg) [公式≈: ^{m}1] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 34 | 4 | 6 | 68 | 9 | 12 | 102 | 15 | 19 | 136 | 22 | 27 |
| 1 | 1 | 2 | 35 | 5 | 7 | 69 | 10 | 13 | 103 | 16 | 20 | 137 | 23 | 28 |
| 2 | 2 | 3 | 36 | 6 | 8 | 70 | 11 | 14 | 104 | 17 | 21 | 138 | 24 | 29 |
| 3 | 3 | 4 | 37 | 7 | 9 | 71 | 12 | 15 | 105 | 18 | 22 | 139 | 25 | 30 |
| 4 | 4 | 5 | 38 | 8 | 10 | 72 | 13 | 16 | 106 | 19 | 23 | 140 | 0 | 6 |
| 5 | 5 | 6 | 39 | 9 | 11 | 73 | 14 | 17 | 107 | 20 | 24 | 141 | 1 | 7 |
| 6 | 6 | 7 | 40 | 10 | 12 | 74 | 15 | 18 | 108 | 21 | 25 | 142 | 2 | 8 |
| 7 | 7 | 8 | 41 | 11 | 13 | 75 | 16 | 19 | 109 | 22 | 26 | 143 | 3 | 9 |
| 8 | 8 | 9 | 42 | 12 | 14 | 76 | 17 | 20 | 110 | 23 | 27 | 144 | 4 | 10 |
| 9 | 9 | 10 | 43 | 13 | 15 | 77 | 18 | 21 | 111 | 24 | 28 | 145 | 5 | 11 |
| 10 | 10 | 11 | 44 | 14 | 16 | 78 | 19 | 22 | 112 | 25 | 29 | 146 | 6 | 12 |
| 11 | 11 | 12 | 45 | 15 | 17 | 79 | 20 | 23 | 113 | 26 | 30 | 147 | 7 | 13 |
| 12 | 12 | 13 | 46 | 16 | 18 | 80 | 21 | 24 | 114 | 0 | 5 | 148 | 8 | 14 |
| 13 | 13 | 14 | 47 | 17 | 19 | 81 | 22 | 25 | 115 | 1 | 6 | 149 | 9 | 15 |
| 14 | 14 | 15 | 48 | 18 | 20 | 82 | 23 | 26 | 116 | 2 | 7 | 150 | 10 | 16 |
| 15 | 15 | 16 | 49 | 19 | 21 | 83 | 24 | 27 | 117 | 3 | 8 | 151 | 11 | 17 |
| 16 | 16 | 17 | 50 | 20 | 22 | 84 | 25 | 28 | 118 | 4 | 9 | 152 | 12 | 18 |
| 17 | 17 | 18 | 51 | 21 | 23 | 85 | 26 | 29 | 119 | 5 | 10 | 153 | 13 | 19 |
| 18 | 18 | 19 | 52 | 22 | 24 | 86 | 27 | 30 | 120 | 6 | 11 | 154 | 14 | 20 |
| 19 | 19 | 20 | 53 | 23 | 25 | 87 | 0 | 4 | 121 | 7 | 12 | 155 | 15 | 21 |
| 20 | 20 | 21 | 54 | 24 | 26 | 88 | 1 | 5 | 122 | 8 | 13 | 156 | 16 | 22 |
| 21 | 21 | 22 | 55 | 25 | 27 | 89 | 2 | 6 | 123 | 9 | 14 | 157 | 17 | 23 |
| 22 | 22 | 23 | 56 | 26 | 28 | 90 | 3 | 7 | 124 | 10 | 15 | 158 | 18 | 24 |
| 23 | 23 | 24 | 57 | 27 | 29 | 91 | 4 | 8 | 125 | 11 | 16 | 159 | 19 | 25 |
| 24 | 24 | 25 | 58 | 28 | 30 | 92 | 5 | 9 | 126 | 12 | 17 | 160 | 20 | 26 |
| 25 | 25 | 26 | 59 | 0 | 3 | 93 | 6 | 10 | 127 | 13 | 18 | 161 | 21 | 27 |
| 26 | 26 | 27 | 60 | 1 | 4 | 94 | 7 | 11 | 128 | 14 | 19 | 162 | 22 | 28 |
| 27 | 27 | 28 | 61 | 2 | 5 | 95 | 8 | 12 | 129 | 15 | 20 | 163 | 23 | 29 |
| 28 | 28 | 29 | 62 | 3 | 6 | 96 | 9 | 13 | 130 | 16 | 21 | 164 | 24 | 30 |
| 29 | 29 | 30 | 63 | 4 | 7 | 97 | 10 | 14 | 131 | 17 | 22 | 165 | 0 | 7 |
| 30 | 0 | 2 | 64 | 5 | 8 | 98 | 11 | 15 | 132 | 18 | 23 | 166 | 1 | 8 |
| 31 | 1 | 3 | 65 | 6 | 9 | 99 | 12 | 16 | 133 | 19 | 24 | 167 | 2 | 9 |
| 32 | 2 | 4 | 66 | 7 | 10 | 100 | 13 | 17 | 134 | 20 | 25 | - | - | - |
| 33 | 3 | 5 | 67 | 8 | 11 | 101 | 14 | 18 | 135 | 21 | 26 | - | - | - |

#### 6.11.2.2 Mapping to resource elements

The mapping of the sequence to resource elements depends on the frame structure. In a subframe for frame structure type 1 and 3 and in a half-frame for frame structure type 2, the same antenna port as for the primary synchronization signal shall be used for the secondary synchronization signal.

For an MBMS-dedicated cell configured with CAS muting, the secondary synchronization signal shall only be transmitted in the first $ 4K_{CAS}$ frames, starting in frames fulfilling $ n_{f}mod16N_{CAS}=0 $ where $ N_{CAS}\in  \left \{ 2, 4, 8, 16\right \} $ and $ K_{CAS}\in  \left \{ 4, 5, 6, \ldots  , 63\right \} $ are given by the higher-layer parameter cas-MutingConfig.

The sequence ![](media_svg/image1105.svg) [公式: d(n)] shall be mapped to resource elements according to

![](media_svg/image1139.svg) [公式≈: ^{a}^{k}^{,}^{k}^{l}_{l}^{=}^{=}_{=}^{d}^{n}√_{⌡}_{⌡}_{⌠}_{⌡}_{⌡}_{∞}N_{N}_{N}_{N}^{(}^{−}^{n}_{symb}_{symb}_{symb}_{symb}^{31}^{DL}_{DL}_{DL}_{DL}^{)}^{,}^{+}−_{−}_{−}_{−}^{N}_{1}2_{2}_{2}^{RB}^{DL}^{n}^{2}^{=}in _{in }_{in }_{in }^{N}^{0}^{sc}^{RB}slots_{slots}_{slots}_{slots}^{,...,}^{61}_{ where}_{ where}_{1}0_{and}and_{11}10_{ the}_{ the}_{PSS}_{PSS}_{is}_{is}_{ transmitt}_{ transmitt}_{ed}_{ed}for _{for }_{for }_{for }frame_{frame}_{frame}_{an }_{MBMS}structure_{structure}_{structure}_{-}_{dedicated} type_{ type}_{ type}1_{3}_{2}except _{cell}for an MBMS-dedicatedcell]

Resource elements ![](media_svg/image46.svg) [公式: (k,l)] where

![](media_svg/image1140.svg) [公式≈: ^{k}_{n}_{l}^{=}_{=}_{=}^{n}√_{⌡}_{⌡}_{⌠}_{⌡}_{⌡}_{∞}_{−}N_{N}_{N}_{N}_{5}^{−}_{,}_{symb}_{symb}_{symb}_{symb}_{−}^{31}^{DL}_{DL}_{DL}_{DL}_{4}_{,...,}^{+}−_{−}_{−}_{−}^{N}_{−}_{1}2_{2}_{2}^{RB}_{1}^{DL}_{,}_{62}^{2}in _{in }_{in }_{in }^{N}_{,}^{sc}_{63}^{RB}slots_{slots}_{slots}_{slots}_{,...}_{66}_{ where}_{ where}_{1}0_{and}and_{11}10_{ the}_{ the}_{PSS}_{PSS}_{is}_{is}_{transmitte}_{transmitte}_{d}_{d}for _{for }_{for }_{for }frame_{frame}_{frame}_{an }_{MBMS}structure_{structure}_{structure}_{-}_{dedicated} type_{ type}_{ type}1_{3}_{2}except _{cell}for an MBMS-dedicatedcell]

are reserved and not used for transmission of the secondary synchronization signal.

### 6.11.3 Resynchronization signal (RSS)

#### 6.11.3.1 Sequence generation

The resynchronization signal (RSS) is transmitted in $ N_{RSS}$ subframes numbered $ i=0,1,\ldots  ,N_{RSS}-1 $, where the RSS duration $ N_{RSS}$ is configured by higher layers. The sequence $ d_{i}\left ( n\right ) $ used for the $ i $ th RSS subframe is generated according to

$ d_{i}\left ( n\right ) =\frac {1-2c(2n)}{\sqrt {2}}+j b(i)\frac {1-2c(2n+1)}{\sqrt {2}}, n=0, 1, \ldots  ,263 $

where the pseudo-random sequence $ c\left ( n\right ) $ is defined in clause 7.2. The pseudo-random sequence generator shall be initialised each subframe with $ c_{init}=N_{ID}^{cell}+2^{9}u $, where u equals the value of the higher-layer parameter systemInfoUnchanged-BR-r15 as set in subframe $ i=0 $.  $ b(i)$ is given by Table 6.11.3.1-1.

Table 6.11.3.1-1: Definition of $ b(i)$.

| $ N_{RSS}$ | $ b\left ( 0\right ) , b\left ( 1\right ) , \ldots  , b(N_{RSS}-1)$ |
| --- | --- |
| 8 | [ 1, 1, -1, 1, -1, -1, 1, 1 ] |
| 16 | [ 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1 ] |
| 32 | [ -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, -1 ] |
| 40 | [ 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1 ] |

#### 6.11.3.2 Mapping to resource elements

If only one CRS port is configured in a cell, the UE may assume that the same antenna port is used for all subframes in an RSS transmission in the cell. Otherwise, the UE may assume that the same antenna port is used for RSS transmission in absolute subframes $ 2n $ and $ 2n+1 $ and $ n=0, 1, \ldots  $.

An RSS is transmitted in $ N_{RSS}$ consecutive BL/CE DL subframes, starting in the first BL/CE DL subframe in a radio frame satisfying

$(n_{f}mod\frac {P_{RSS}}{10})=O_{RSS}$

where the RSS periodicity $ P_{RSS}$ and the RSS time offset $ O_{RSS}$ are configured by higher layers. In frequency domain, the RSS frequency location is assigned to the 24 subcarriers in the physical resource blocks numbers $ n_{PRB,RSS}$ and $ n_{PRB,RSS}+1 $, as configured by higher layers.

In each subframe $ i $ used for RSS transmission, the RSS sequence $ d_{i}\left ( n\right ) $ shall be mapped to resource elements $(k,l)$ in sequence, starting with $ d_{i}\left ( 0\right ) $ in increasing order of first the index $ k=0, 1, \ldots  ,2N_{sc}^{RB}-1 $, over the 24 assigned subcarriers and then the index $ l=3, 4, \ldots  , 2N_{symb}^{DL}-1 $.

A resource element $(k,l)$  overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted shall not be used for RSS transmission but is counted in the mapping process. Additionally, an RSS subframe is dropped if any RSS PRB pair overlaps with any PRB pair carrying PSS, SSS, PBCH or PDSCH associated with SI-RNTI.  In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layerfdd-DownlinkOrTddSubframeBitmapBR, are not counted in RSS mapping and are not used for transmission of RSS.

## 6.11A Discovery signal

A discovery signal occasion for a cell consists of a period with a duration of

- one to five consecutive subframes for frame structure type 1

- two to five consecutive subframes for frame structure type 2

- 12 OFDM symbols within one non-empty subframe for frame structure type 3

where the UE in the downlink subframes may assume presence of a discovery signal consisting of

- cell-specific reference signals on antenna port 0 in all downlink subframes and in DwPTS of all special subframes in the period for frame structure type 1 and 2

- cell specific reference signals on antenna port 0 when higher layer parameters indicate only one configured antenna port for cell specific reference signals for a serving cell using frame structure type 3

- cell specific reference signals on antenna port 0 and antenna port 1 when higher layer parameters indicate at least two configured antenna ports for cell specific reference signals for a serving cell using frame structure type 3

- cell specific reference signals on antenna port 0 and antenna port 1 when higher layer configured parameter presenceAntennaPort1 is signalled to be 1, for a neighbour cell when using frame structure type 3

- primary synchronization signal in the first subframe of the period for frame structure types 1 and 3 or the second subframe of the period for frame structure type 2,

- secondary synchronization signal in the first subframe of the period, and

- non-zero-power CSI reference signals in zero or more subframes in the period. The configuration of non-zero-power CSI reference signals part of the discovery signal is obtained as described in clause 6.10.5.2

For frame structures 1 and 2 the UE may assume a discovery signal occasion once every dmtc-Periodicity.

For frame structure type 3, the UE may assume a discovery signal occasion may occur in any subframe within the discovery signals measurement timing configuration in clause 5.5.2.10 of [9].

For frame structure type 3, simultaneous transmission of a discovery signal and PDSCH/PDCCH/EPDCCH may occur in subframes 0 and 5 only.

For frame structure type 3, the UE may assume that a discovery signal occasion occurs in the first subframe containing a primary synchronization signal, secondary synchronization signal and cell-specific reference signals within the discovery measurement timing configuration in clause 5.5.2.10 of [9].

## 6.11B MTC wake-up signal (MWUS)

### 6.11B.1 Sequence generation

The MWUS sequence  in subframe $ x=0, 1, \ldots  , M-1 $ is defined by

$$ w\left ( m\right ) =\theta  _{n_{f},n_{s}}\left ( m^{'}\right ) e^{-j\frac {\pi  un\left ( n+1\right ) }{131}}e^{j\frac {2\pi  gm}{132}}$$

$$ m=0, 1, \ldots  , 131 $$

$$ m^{'}=m+132x $$

$$ n=mmod132 $$

$$\theta  _{n_{f},n_{s}}\left ( m^{'}\right ) ={\begin {matrix}1 & ifc_{n_{f},n_{s}}\left ( 2m^{'}\right ) =0andc_{n_{f},n_{s}}\left ( 2m^{'}+1\right ) =0 \\ -1 & ifc_{n_{f},n_{s}}\left ( 2m^{'}\right ) =0andc_{n_{f},n_{s}}\left ( 2m^{'}+1\right ) =1 \\ j & ifc_{n_{f},n_{s}}\left ( 2m^{'}\right ) =1andc_{n_{f},n_{s}}\left ( 2m^{'}+1\right ) =0 \\ -j & ifc_{n_{f},n_{s}}\left ( 2m^{'}\right ) =1andc_{n_{f},n_{s}}\left ( 2m^{'}+1\right ) =1\end {matrix}$$

$$ u=\left ( N_{ID}^{cell}mod126\right ) +3 $$

where  is the actual duration of MWUS as defined in [4]. For a UE not configured with group MWUS, $ g=0 $. For a UE configured with group MWUS, $ g=14\left ( N_{group}^{WUS}+1\right ) $ for $ 0\leq  N_{group}^{WUS}\leq  7 $, where $ N_{group}^{WUS}$ is determined by the UE group to which the UE is associated as determined by higher layers [10]. In a resource that is not shared with non-group MWUS, the common MWUS sequence shall be determined by $ g=126 $. In a resource that is shared with non-group MWUS, the common MWUS sequence is determined by higher layers [9].

The scrambling sequence $ c_{n_{f},n_{s}}\left ( i\right ) , i=0, 1, \ldots  , 2\cdot  132M-1 $ is given by clause 7.2, and shall be initialized at the start of the MWUS with

$ c_{init\_WUS}=(N_{ID}^{cell}+1)\left ( \left ( 10n_{f\_start\_PO}+\lfloor  \frac {n_{s\_start\_PO}}{2}\rfloor  \right ) mod2048+1\right ) 2^{9}+N_{ID}^{cell}+N_{ID}^{resource}\cdot  2^{29}$

where $ n_{f\_start\_PO}$ is the first frame of the first PO to which the MWUS is associated, $ n_{s\_start\_PO}$ is the first slot of the first PO to which the MWUS is associated and $ N_{ID}^{resource}$ indicates the group MWUS resource to which the UE is associated. For a UE not configured with group MWUS, $ N_{ID}^{resource}=0 $, whereas for a UE configured with group MWUS, $ N_{ID}^{resource}$ is determined by higher layers [10].


### 6.11B.2 Mapping to resource elements

The same antenna port shall be used for all symbols of the MWUS within a subframe. The UE shall not assume that the MWUS is transmitted on the same antenna port as any of the downlink reference signals or synchronization signals. If only one CRS port is configured by the eNB, the UE may assume the transmission of all MWUS subframes is using the same antenna port; otherwise, the UE may assume the same antenna port is used for MWUS transmission in downlink subframes w0 + 2n and w0 + 2n + 1, where w0 is the first downlink subframe of the MWUS transmission as specified in [4], and n=0, 1,….

The MWUS bandwidth is 2 consecutive PRBs, the frequency location of the lowermost PRB with $ N_{ID}^{resource}=0 $ is signaled by higher layers. For both PRB pairs in the frequency domain, for which MWUS is defined, the MWUS sequence $ w\left ( m\right ) $ shall be mapped to resource elements $(k,l)$ in sequence, starting with $ w(0)$ in increasing order of first the index $ k=0, 1, \ldots  ,N_{sc}^{RB}-1 $, over the 12 assigned subcarriers and then the index $ l=3, 4, \ldots  , 2N_{symb}^{DL}-1 $ in each subframe in which MWUS is transmitted.

The MWUS sequence is mapped to the set of subframes in the actual MWUS duration as defined in [4], where in a subframe in which an MWUS PRB pair overlaps with any PRB pair carrying PSS, SSS, RSS, PBCH or PDSCH associated with SI-RNTI is transmitted, the subframe is counted in the MWUS mapping but not used for transmission of MWUS. In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layerfdd-DownlinkOrTddSubframeBitmapBR, are not counted in MWUS mapping and are not used for transmission of MWUS.

A resource element $(k,l)$ overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted shall not be used for MWUS transmission but is counted in the mapping process.

## 6.12 OFDM baseband signal generation

The time-continuous signal ![](media_svg/image1144.svg) [公式≈: s_{l}^{(}^{p}^{)}(t)] on antenna port ![](media_svg/image34.svg) [公式: p] in OFDM symbol ![](media_svg/image389.svg) [公式: l] in a downlink slot is defined by

![](media_svg/image1145.svg) [公式≈: _{s}_{l}(p)_{(}_{t}_{)}_{=}_{k}_{=}_{−}_{√}_{N}_{⊆}_{RB}_{DL}^{−}^{1}_{N}_{sc}_{RB}_{/}_{2}_{∃}_{a}_{k}(_{(}p_{−})_{)}_{,}_{l}_{∪}_{e}j2Πkδf(t−NCP,lTs)_{+}^{⊥}^{N}^{RB}^{DL}_{⊆}^{N}_{k}_{=}^{sc}^{RB}_{1}^{/}^{2}^{∀}_{a}_{k}(_{(}p_{+})_{)}_{,}_{l}_{∪}_{e}j2Πkδf(t−NCP,lTs)]

for ![](media_svg/image1146.svg) [公式≈: 0≥t<(N_{CP}_{,}_{l}+N)≠T_{s}] where ![](media_svg/image1147.svg) [公式≈: k^{(}^{−}^{)}=k+√NRB^{DL}Nsc^{RB}2∃] and![](media_svg/image1148.svg) [公式≈: k^{(}^{+}^{)}=k+√NRB^{DL}Nsc^{RB}2∃−1]. The variable ![](media_svg/image1149.svg) [公式: N] equals 2048 for ![](media_svg/image1150.svg) [公式: δf=15kHz] subcarrier spacing, 4096 for ![](media_svg/image1151.svg) [公式: δf=7.5kHz] subcarrier spacing, 12288 for $\Delta  f=2.5kHz $, 24576 for ![](media_svg/image1152.svg) [公式: δf=1.25kHz] subcarrier spacing , and 82944 for $\Delta  f=\frac {1}{\left ( 82944T_{s}\right ) }\approx  0.37kHz $.

For frame structure type 3, if PDCCH is to be transmitted in a subframe starting with OFDM symbol  based on the  received uplink control information that indicates channel occupancy time sharing '1' as specified in [11], OFDM symbol  in the previous subframe may be transmitted, given by

The OFDM symbols in a slot shall be transmitted in increasing order of ![](media_svg/image389.svg) [公式: l], starting with ![](media_svg/image1156.svg) [公式: l=0], where OFDM symbol ![](media_svg/image1157.svg) [公式: l>0]starts at time ![](media_svg/image1158.svg) [公式≈: ⊆^{l}_{l}_{±}^{−}_{=}^{1}_{0}^{(}^{N}CP,l±^{+}^{N}^{)}^{T}s] within the slot. In case the first OFDM symbol(s) in a slot use normal cyclic prefix and the remaining OFDM symbols use extended cyclic prefix, the starting position the OFDM symbols with extended cyclic prefix shall be identical to those in a slot where all OFDM symbols use extended cyclic prefix. Thus there will be a part of the time slot between the two cyclic prefix regions where the transmitted signal is not specified. For ![](media_svg/image1159.svg) [公式: δf=1.25kHz], there is one OFDM symbol per slot and one slot per subframe. For $\Delta  f\approx  0.37kHz $, there is one OFDM symbol per slot and one slot per 3ms.

Table 6.12-1 lists the value of ![](media_svg/image1160.svg) [公式≈: ^{N}CP,l]that shall be used. Note that different OFDM symbols within a slot in some cases have different cyclic prefix lengths.

In case NB-IoT is supported, the OFDM baseband signal generation is defined in clause 10.2.8.

Table 6.12-1: OFDM parameters

| Configuration |  | Cyclic prefix length ![](media_svg/image1160.svg) [公式≈: ^{N}CP,l] |
| --- | --- | --- |
| Normal cyclic prefix | ![](media_svg/image1161.svg) [公式: δf=15kHz] | ![](media_svg/image1162.svg) [公式: 160for  l=0]![](media_svg/image1163.svg) [公式: 144for  l=1,2,...,6] |
| Extended cyclic prefix | ![](media_svg/image1161.svg) [公式: δf=15kHz] | ![](media_svg/image1164.svg) [公式: 512for  l=0,1,...,5] |
|  | ![](media_svg/image1165.svg) [公式: δf=7.5kHz] | ![](media_svg/image1166.svg) [公式: 1024for  l=0,1,2] |
|  | $\Delta  f=2.5kHz $ | 3072 for $ l=0 $ |
|  | ![](media_svg/image1167.svg) [公式: δf=1.25kHz] | ![](media_svg/image1168.svg) [公式: 6144for  l=0] |
|  | $\Delta  f\approx  0.37kHz $ | 9216 for $ l=0 $ |

## 6.13 Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued OFDM baseband signal for each antenna port is shown in Figure 6.13-1. The filtering required prior to transmission is defined by the requirements in TS36.104 [6].

![](media/image1169.emf)

Figure 6.13-1: Downlink modulation

# 7 Generic functions

## 7.1 Modulation mapper

The modulation mapper takes binary digits, 0 or 1, as input and produces complex-valued modulation symbols, x as output.

### 7.1.1 BPSK

In case of BPSK modulation, a single bit, ![](media_svg/image1170.svg) [公式: b(i)], is mapped to a complex-valued modulation symbol x=I+jQ according to Table 7.1.1-1.

Table 7.1.1-1: BPSK modulation mapping

| ![](media_svg/image1170.svg) [公式: b(i)] | I | Q |
| --- | --- | --- |
| 0 | ![](media_svg/image1171.svg) [公式: 12] | ![](media_svg/image1171.svg) [公式: 12] |
| 1 | ![](media_svg/image1172.svg) [公式: −12] | ![](media_svg/image1172.svg) [公式: −12] |

### 7.1.2 QPSK

In case of QPSK modulation, pairs of bits, ![](media_svg/image1173.svg) [公式: b(i),b(i+1)], are mapped to complex-valued modulation symbols x according to Table 7.1.2-1 where ![](media_svg/image1174.svg) [公式: x=I+jQ] unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case ![](media_svg/image1175.svg) [公式≈: x=e^{j}^{Φ}^{0}^{Π}c(I−d)+e^{j}^{(}^{Φ}^{1}^{+}^{1}^{/}^{2}^{)}^{Π}c(Q−d)] where ![](media_svg/image1176.svg) [公式: c] and ![](media_svg/image1177.svg) [公式: d] are determined from MUSTIdx using Table 7.1.2-2, and each ![](media_svg/image1178.svg) [公式: Φ_{0},Φ_{1}⎰{0,1}] is selected by eNB independently of ![](media_svg/image1173.svg) [公式: b(i),b(i+1)].

Table 7.1.2-1: QPSK modulation mapping

| ![](media_svg/image1179.svg) [公式: b(i),b(i+1)] | I | Q |
| --- | --- | --- |
| 00 | ![](media_svg/image1171.svg) [公式: 12] | ![](media_svg/image1171.svg) [公式: 12] |
| 01 | ![](media_svg/image1171.svg) [公式: 12] | ![](media_svg/image1172.svg) [公式: −12] |
| 10 | ![](media_svg/image1172.svg) [公式: −12] | ![](media_svg/image1171.svg) [公式: 12] |
| 11 | ![](media_svg/image1172.svg) [公式: −12] | ![](media_svg/image1172.svg) [公式: −12] |

Table 7.1.2-2: Values for ![](media_svg/image1180.svg) [公式: c] and ![](media_svg/image1181.svg) [公式: d] for QPSK

| MUSTIdx | ![](media_svg/image1176.svg) [公式: c] | ![](media_svg/image1177.svg) [公式: d] |
| --- | --- | --- |
| 01 | ![](media_svg/image1182.svg) [公式: 1/5] | ![](media_svg/image1183.svg) [公式: 2] |
| 10 | ![](media_svg/image1184.svg) [公式: 2/29] | ![](media_svg/image1185.svg) [公式: 5/(22)] |
| 11 | ![](media_svg/image1186.svg) [公式: 71/578] | ![](media_svg/image1187.svg) [公式: 23/(72)] |

### 7.1.3 16QAM

In case of 16QAM modulation, quadruplets of bits, ![](media_svg/image1188.svg) [公式: b(i),b(i+1),b(i+2),b(i+3)], are mapped to complex-valued modulation symbols x according to Table 7.1.3-1 where ![](media_svg/image1174.svg) [公式: x=I+jQ] unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case ![](media_svg/image1175.svg) [公式≈: x=e^{j}^{Φ}^{0}^{Π}c(I−d)+e^{j}^{(}^{Φ}^{1}^{+}^{1}^{/}^{2}^{)}^{Π}c(Q−d)] where ![](media_svg/image1176.svg) [公式: c] and ![](media_svg/image1177.svg) [公式: d] are determined from MUSTIdx using Table 7.1.3-2, and each ![](media_svg/image1178.svg) [公式: Φ_{0},Φ_{1}⎰{0,1}] is selected by eNB independently of ![](media_svg/image1188.svg) [公式: b(i),b(i+1),b(i+2),b(i+3)].

Table 7.1.3-1: 16QAM modulation mapping

| ![](media_svg/image1189.svg) [公式: b(i),b(i+1),b(i+2),b(i+3)] | I | Q |
| --- | --- | --- |
| 0000 | ![](media_svg/image1190.svg) [公式: 110] | ![](media_svg/image1190.svg) [公式: 110] |
| 0001 | ![](media_svg/image1190.svg) [公式: 110] | ![](media_svg/image1191.svg) [公式: 310] |
| 0010 | ![](media_svg/image1191.svg) [公式: 310] | ![](media_svg/image1190.svg) [公式: 110] |
| 0011 | ![](media_svg/image1191.svg) [公式: 310] | ![](media_svg/image1191.svg) [公式: 310] |
| 0100 | ![](media_svg/image1190.svg) [公式: 110] | ![](media_svg/image1192.svg) [公式: −110] |
| 0101 | ![](media_svg/image1190.svg) [公式: 110] | ![](media_svg/image1193.svg) [公式: −310] |
| 0110 | ![](media_svg/image1191.svg) [公式: 310] | ![](media_svg/image1192.svg) [公式: −110] |
| 0111 | ![](media_svg/image1191.svg) [公式: 310] | ![](media_svg/image1194.svg) [公式: −310] |
| 1000 | ![](media_svg/image1192.svg) [公式: −110] | ![](media_svg/image1190.svg) [公式: 110] |
| 1001 | ![](media_svg/image1192.svg) [公式: −110] | ![](media_svg/image1191.svg) [公式: 310] |
| 1010 | ![](media_svg/image1194.svg) [公式: −310] | ![](media_svg/image1190.svg) [公式: 110] |
| 1011 | ![](media_svg/image1194.svg) [公式: −310] | ![](media_svg/image1191.svg) [公式: 310] |
| 1100 | ![](media_svg/image1192.svg) [公式: −110] | ![](media_svg/image1192.svg) [公式: −110] |
| 1101 | ![](media_svg/image1192.svg) [公式: −110] | ![](media_svg/image1194.svg) [公式: −310] |
| 1110 | ![](media_svg/image1194.svg) [公式: −310] | ![](media_svg/image1192.svg) [公式: −110] |
| 1111 | ![](media_svg/image1194.svg) [公式: −310] | ![](media_svg/image1194.svg) [公式: −310] |

Table 7.1.3-2: Values for ![](media_svg/image1195.svg) [公式: c] and ![](media_svg/image1181.svg) [公式: d] for 16QAM

| MUSTIdx | ![](media_svg/image1196.svg) [公式: c] | ![](media_svg/image1197.svg) [公式: d] |
| --- | --- | --- |
| 01 | ![](media_svg/image1198.svg) [公式: 5/21] | ![](media_svg/image1199.svg) [公式: 22/5] |
| 10 | ![](media_svg/image1200.svg) [公式: 35/334] | ![](media_svg/image1201.svg) [公式: 17/(310)] |
| 11 | ![](media_svg/image1202.svg) [公式: 5/69] | ![](media_svg/image1203.svg) [公式: 42/5] |

### 7.1.4 64QAM

In case of 64QAM modulation, hextuplets of bits, ![](media_svg/image1204.svg) [公式: b(i),b(i+1),b(i+2),b(i+3),b(i+4),b(i+5)], are mapped to complex-valued modulation symbols x according to Table 7.1.4-1 where ![](media_svg/image1174.svg) [公式: x=I+jQ] unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case ![](media_svg/image1175.svg) [公式≈: x=e^{j}^{Φ}^{0}^{Π}c(I−d)+e^{j}^{(}^{Φ}^{1}^{+}^{1}^{/}^{2}^{)}^{Π}c(Q−d)] where ![](media_svg/image1176.svg) [公式: c] and ![](media_svg/image1177.svg) [公式: d] are determined from MUSTIdx using Table 7.1.4-2, and each ![](media_svg/image1178.svg) [公式: Φ_{0},Φ_{1}⎰{0,1}] is selected by eNB independently of ![](media_svg/image1204.svg) [公式: b(i),b(i+1),b(i+2),b(i+3),b(i+4),b(i+5)].

Table 7.1.4-1: 64QAM modulation mapping

| ![](media_svg/image1205.svg) [公式: b(i),b(i+1),b(i+2),b(i+3),b(i+4),b(i+5)] | I | Q | ![](media_svg/image1206.svg) [公式: b(i),b(i+1),b(i+2),b(i+3),b(i+4),b(i+5)] | I | Q |
| --- | --- | --- | --- | --- | --- |
| 000000 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1207.svg) [公式: 342] | 100000 | ![](media_svg/image1208.svg) [公式: −342] | ![](media_svg/image1207.svg) [公式: 342] |
| 000001 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1209.svg) [公式: 142] | 100001 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1209.svg) [公式: 142] |
| 000010 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1207.svg) [公式: 342] | 100010 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1207.svg) [公式: 342] |
| 000011 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1209.svg) [公式: 142] | 100011 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1209.svg) [公式: 142] |
| 000100 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1212.svg) [公式: 542] | 100100 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1212.svg) [公式: 542] |
| 000101 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1213.svg) [公式: 742] | 100101 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1213.svg) [公式: 742] |
| 000110 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1212.svg) [公式: 542] | 100110 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1212.svg) [公式: 542] |
| 000111 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1213.svg) [公式: 742] | 100111 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1213.svg) [公式: 742] |
| 001000 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1207.svg) [公式: 342] | 101000 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1207.svg) [公式: 342] |
| 001001 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1209.svg) [公式: 142] | 101001 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1209.svg) [公式: 142] |
| 001010 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1207.svg) [公式: 342] | 101010 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1207.svg) [公式: 342] |
| 001011 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1209.svg) [公式: 142] | 101011 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1209.svg) [公式: 142] |
| 001100 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1212.svg) [公式: 542] | 101100 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1212.svg) [公式: 542] |
| 001101 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1213.svg) [公式: 742] | 101101 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1213.svg) [公式: 742] |
| 001110 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1212.svg) [公式: 542] | 101110 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1212.svg) [公式: 542] |
| 001111 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1213.svg) [公式: 742] | 101111 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1213.svg) [公式: 742] |
| 010000 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1210.svg) [公式: −342] | 110000 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1210.svg) [公式: −342] |
| 010001 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1216.svg) [公式: −142] | 110001 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1211.svg) [公式: −142] |
| 010010 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1210.svg) [公式: −342] | 110010 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1210.svg) [公式: −342] |
| 010011 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1211.svg) [公式: −142] | 110011 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1211.svg) [公式: −142] |
| 010100 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1214.svg) [公式: −542] | 110100 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1214.svg) [公式: −542] |
| 010101 | ![](media_svg/image1207.svg) [公式: 342] | ![](media_svg/image1215.svg) [公式: −742] | 110101 | ![](media_svg/image1210.svg) [公式: −342] | ![](media_svg/image1215.svg) [公式: −742] |
| 010110 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1214.svg) [公式: −542] | 110110 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1214.svg) [公式: −542] |
| 010111 | ![](media_svg/image1209.svg) [公式: 142] | ![](media_svg/image1215.svg) [公式: −742] | 110111 | ![](media_svg/image1211.svg) [公式: −142] | ![](media_svg/image1215.svg) [公式: −742] |
| 011000 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1210.svg) [公式: −342] | 111000 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1210.svg) [公式: −342] |
| 011001 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1211.svg) [公式: −142] | 111001 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1211.svg) [公式: −142] |
| 011010 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1210.svg) [公式: −342] | 111010 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1210.svg) [公式: −342] |
| 011011 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1211.svg) [公式: −142] | 111011 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1211.svg) [公式: −142] |
| 011100 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1214.svg) [公式: −542] | 111100 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1217.svg) [公式: −542] |
| 011101 | ![](media_svg/image1212.svg) [公式: 542] | ![](media_svg/image1215.svg) [公式: −742] | 111101 | ![](media_svg/image1214.svg) [公式: −542] | ![](media_svg/image1215.svg) [公式: −742] |
| 011110 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1214.svg) [公式: −542] | 111110 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1214.svg) [公式: −542] |
| 011111 | ![](media_svg/image1213.svg) [公式: 742] | ![](media_svg/image1215.svg) [公式: −742] | 111111 | ![](media_svg/image1215.svg) [公式: −742] | ![](media_svg/image1218.svg) [公式: −742] |

Table 7.1.4-2: Values for ![](media_svg/image1195.svg) [公式: c] and ![](media_svg/image1181.svg) [公式: d] for 64QAM

| MUSTIdx | ![](media_svg/image1219.svg) [公式: c] | ![](media_svg/image1220.svg) [公式: d] |
| --- | --- | --- |
| 01 | ![](media_svg/image1221.svg) [公式: 21/85] | ![](media_svg/image1222.svg) [公式: 42/21] |
| 10 | ![](media_svg/image1223.svg) [公式: 7/34] | ![](media_svg/image1224.svg) [公式: 33/14] |
| 11 | ![](media_svg/image1225.svg) [公式: 7/55] | ![](media_svg/image1226.svg) [公式: 26/7] |

### 7.1.5 256QAM

In case of 256QAM modulation, octuplets of bits, ![](media_svg/image1227.svg) [公式: b(i),b(i+1),b(i+2),b(i+3),b(i+4),b(i+5),b(i+6),b(i+7)], are mapped to complex-valued modulation symbols ![](media_svg/image1228.svg) [公式: x=(I+jQ)170] according to Table 7.1.5-1.

Table 7.1.5-1: 256QAM modulation mapping

| ![](media_svg/image1229.svg) [公式: b(i),...,b(i+7)] | I | Q | ![](media_svg/image1230.svg) [公式: b(i),...,b(i+7)] | I | Q | ![](media_svg/image1229.svg) [公式: b(i),...,b(i+7)] | I | Q | ![](media_svg/image1229.svg) [公式: b(i),...,b(i+7)] | I | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00000000 | 5 | 5 | 01000000 | 5 | -5 | 10000000 | -5 | 5 | 11000000 | -5 | -5 |
| 00000001 | 5 | 7 | 01000001 | 5 | -7 | 10000001 | -5 | 7 | 11000001 | -5 | -7 |
| 00000010 | 7 | 5 | 01000010 | 7 | -5 | 10000010 | -7 | 5 | 11000010 | -7 | -5 |
| 00000011 | 7 | 7 | 01000011 | 7 | -7 | 10000011 | -7 | 7 | 11000011 | -7 | -7 |
| 00000100 | 5 | 3 | 01000100 | 5 | -3 | 10000100 | -5 | 3 | 11000100 | -5 | -3 |
| 00000101 | 5 | 1 | 01000101 | 5 | -1 | 10000101 | -5 | 1 | 11000101 | -5 | -1 |
| 00000110 | 7 | 3 | 01000110 | 7 | -3 | 10000110 | -7 | 3 | 11000110 | -7 | -3 |
| 00000111 | 7 | 1 | 01000111 | 7 | -1 | 10000111 | -7 | 1 | 11000111 | -7 | -1 |
| 00001000 | 3 | 5 | 01001000 | 3 | -5 | 10001000 | -3 | 5 | 11001000 | -3 | -5 |
| 00001001 | 3 | 7 | 01001001 | 3 | -7 | 10001001 | -3 | 7 | 11001001 | -3 | -7 |
| 00001010 | 1 | 5 | 01001010 | 1 | -5 | 10001010 | -1 | 5 | 11001010 | -1 | -5 |
| 00001011 | 1 | 7 | 01001011 | 1 | -7 | 10001011 | -1 | 7 | 11001011 | -1 | -7 |
| 00001100 | 3 | 3 | 01001100 | 3 | -3 | 10001100 | -3 | 3 | 11001100 | -3 | -3 |
| 00001101 | 3 | 1 | 01001101 | 3 | -1 | 10001101 | -3 | 1 | 11001101 | -3 | -1 |
| 00001110 | 1 | 3 | 01001110 | 1 | -3 | 10001110 | -1 | 3 | 11001110 | -1 | -3 |
| 00001111 | 1 | 1 | 01001111 | 1 | -1 | 10001111 | -1 | 1 | 11001111 | -1 | -1 |
| 00010000 | 5 | 11 | 01010000 | 5 | -11 | 10010000 | -5 | 11 | 11010000 | -5 | -11 |
| 00010001 | 5 | 9 | 01010001 | 5 | -9 | 10010001 | -5 | 9 | 11010001 | -5 | -9 |
| 00010010 | 7 | 11 | 01010010 | 7 | -11 | 10010010 | -7 | 11 | 11010010 | -7 | -11 |
| 00010011 | 7 | 9 | 01010011 | 7 | -9 | 10010011 | -7 | 9 | 11010011 | -7 | -9 |
| 00010100 | 5 | 13 | 01010100 | 5 | -13 | 10010100 | -5 | 13 | 11010100 | -5 | -13 |
| 00010101 | 5 | 15 | 01010101 | 5 | -15 | 10010101 | -5 | 15 | 11010101 | -5 | -15 |
| 00010110 | 7 | 13 | 01010110 | 7 | -13 | 10010110 | -7 | 13 | 11010110 | -7 | -13 |
| 00010111 | 7 | 15 | 01010111 | 7 | -15 | 10010111 | -7 | 15 | 11010111 | -7 | -15 |
| 00011000 | 3 | 11 | 01011000 | 3 | -11 | 10011000 | -3 | 11 | 11011000 | -3 | -11 |
| 00011001 | 3 | 9 | 01011001 | 3 | -9 | 10011001 | -3 | 9 | 11011001 | -3 | -9 |
| 00011010 | 1 | 11 | 01011010 | 1 | -11 | 10011010 | -1 | 11 | 11011010 | -1 | -11 |
| 00011011 | 1 | 9 | 01011011 | 1 | -9 | 10011011 | -1 | 9 | 11011011 | -1 | -9 |
| 00011100 | 3 | 13 | 01011100 | 3 | -13 | 10011100 | -3 | 13 | 11011100 | -3 | -13 |
| 00011101 | 3 | 15 | 01011101 | 3 | -15 | 10011101 | -3 | 15 | 11011101 | -3 | -15 |
| 00011110 | 1 | 13 | 01011110 | 1 | -13 | 10011110 | -1 | 13 | 11011110 | -1 | -13 |
| 00011111 | 1 | 15 | 01011111 | 1 | -15 | 10011111 | -1 | 15 | 11011111 | -1 | -15 |
| 00100000 | 11 | 5 | 01100000 | 11 | -5 | 10100000 | -11 | 5 | 11100000 | -11 | -5 |
| 00100001 | 11 | 7 | 01100001 | 11 | -7 | 10100001 | -11 | 7 | 11100001 | -11 | -7 |
| 00100010 | 9 | 5 | 01100010 | 9 | -5 | 10100010 | -9 | 5 | 11100010 | -9 | -5 |
| 00100011 | 9 | 7 | 01100011 | 9 | -7 | 10100011 | -9 | 7 | 11100011 | -9 | -7 |
| 00100100 | 11 | 3 | 01100100 | 11 | -3 | 10100100 | -11 | 3 | 11100100 | -11 | -3 |
| 00100101 | 11 | 1 | 01100101 | 11 | -1 | 10100101 | -11 | 1 | 11100101 | -11 | -1 |
| 00100110 | 9 | 3 | 01100110 | 9 | -3 | 10100110 | -9 | 3 | 11100110 | -9 | -3 |
| 00100111 | 9 | 1 | 01100111 | 9 | -1 | 10100111 | -9 | 1 | 11100111 | -9 | -1 |
| 00101000 | 13 | 5 | 01101000 | 13 | -5 | 10101000 | -13 | 5 | 11101000 | -13 | -5 |
| 00101001 | 13 | 7 | 01101001 | 13 | -7 | 10101001 | -13 | 7 | 11101001 | -13 | -7 |
| 00101010 | 15 | 5 | 01101010 | 15 | -5 | 10101010 | -15 | 5 | 11101010 | -15 | -5 |
| 00101011 | 15 | 7 | 01101011 | 15 | -7 | 10101011 | -15 | 7 | 11101011 | -15 | -7 |
| 00101100 | 13 | 3 | 01101100 | 13 | -3 | 10101100 | -13 | 3 | 11101100 | -13 | -3 |
| 00101101 | 13 | 1 | 01101101 | 13 | -1 | 10101101 | -13 | 1 | 11101101 | -13 | -1 |
| 00101110 | 15 | 3 | 01101110 | 15 | -3 | 10101110 | -15 | 3 | 11101110 | -15 | -3 |
| 00101111 | 15 | 1 | 01101111 | 15 | -1 | 10101111 | -15 | 1 | 11101111 | -15 | -1 |
| 00110000 | 11 | 11 | 01110000 | 11 | -11 | 10110000 | -11 | 11 | 11110000 | -11 | -11 |
| 00110001 | 11 | 9 | 01110001 | 11 | -9 | 10110001 | -11 | 9 | 11110001 | -11 | -9 |
| 00110010 | 9 | 11 | 01110010 | 9 | -11 | 10110010 | -9 | 11 | 11110010 | -9 | -11 |
| 00110011 | 9 | 9 | 01110011 | 9 | -9 | 10110011 | -9 | 9 | 11110011 | -9 | -9 |
| 00110100 | 11 | 13 | 01110100 | 11 | -13 | 10110100 | -11 | 13 | 11110100 | -11 | -13 |
| 00110101 | 11 | 15 | 01110101 | 11 | -15 | 10110101 | -11 | 15 | 11110101 | -11 | -15 |
| 00110110 | 9 | 13 | 01110110 | 9 | -13 | 10110110 | -9 | 13 | 11110110 | -9 | -13 |
| 00110111 | 9 | 15 | 01110111 | 9 | -15 | 10110111 | -9 | 15 | 11110111 | -9 | -15 |
| 00111000 | 13 | 11 | 01111000 | 13 | -11 | 10111000 | -13 | 11 | 11111000 | -13 | -11 |
| 00111001 | 13 | 9 | 01111001 | 13 | -9 | 10111001 | -13 | 9 | 11111001 | -13 | -9 |
| 00111010 | 15 | 11 | 01111010 | 15 | -11 | 10111010 | -15 | 11 | 11111010 | -15 | -11 |
| 00111011 | 15 | 9 | 01111011 | 15 | -9 | 10111011 | -15 | 9 | 11111011 | -15 | -9 |
| 00111100 | 13 | 13 | 01111100 | 13 | -13 | 10111100 | -13 | 13 | 11111100 | -13 | -13 |
| 00111101 | 13 | 15 | 01111101 | 13 | -15 | 10111101 | -13 | 15 | 11111101 | -13 | -15 |
| 00111110 | 15 | 13 | 01111110 | 15 | -13 | 10111110 | -15 | 13 | 11111110 | -15 | -13 |
| 00111111 | 15 | 15 | 01111111 | 15 | -15 | 10111111 | -15 | 15 | 11111111 | -15 | -15 |

### 7.1.6 1024QAM

In case of 1024QAM modulation, 10-tuplets of bits, , are mapped to complex-valued modulation symbols  according to

## 7.2 Pseudo-random sequence generation

Pseudo-random sequences are defined by a length-31 Gold sequence. The output sequence ![](media_svg/image1234.svg) [公式: c(n)] of length![](media_svg/image1235.svg) [公式≈: ^{M}PN], where![](media_svg/image1236.svg) [公式: n=0,1,...,M_{PN}−1], is defined by

![](media_svg/image1237.svg) [公式≈: x^{x}_{2}^{1}^{(}(^{n}n^{+}+^{c}^{31}31^{(}^{n}^{)}^{)})^{=}^{=}=^{(}^{(}(^{x}^{x}x^{1}^{1}_{2}^{(}^{(}(^{n}^{n}n^{+}^{+}+^{3}^{N}3^{)})^{C}^{+}+^{)}^{x}x^{+}^{1}_{2}^{(}^{x}(^{n}n^{2}^{)}^{(}^{)}+^{n}^{mod}2^{+})^{N}+^{2}^{C}x^{)}_{2}^{)}(^{mod}n+1^{2})+x_{2}(n))mod2]

where ![](media_svg/image1238.svg) [公式: N_{C}=1600] and the first m-sequence shall be initialized with![](media_svg/image1239.svg) [公式: x_{1}(0)=1,x_{1}(n)=0,n=1,2,...,30]. The initialization of the second m-sequence is denoted by ![](media_svg/image1240.svg) [公式≈: c_{init}=_{⊆}^{30}_{i}_{=}_{0}x_{2}(i)∪2^{i}] with the value depending on the application of the sequence.

# 8 Timing

## 8.1 Uplink-downlink frame timing

Transmission of the uplink radio frame number ![](media_svg/image526.svg) [公式≈: ^{P}^{ˆ}PUSCH,j^{(}^{i}^{)}] from the UE shall start $ T_{TA}=\left ( N_{TA}+N_{TA,offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) T_{s}$ seconds before the start of the corresponding downlink radio frame at the UE.

![](media/image1241.emf)

Figure 8.1-1: Uplink-downlink timing relation

Except for the cases mentioned in Table 8.1-1, Table 8.1-2 and Table 8.1-3, the range of ![](media_svg/image1242.svg) [公式≈: ^{N}TA] is: ![](media_svg/image1243.svg) [公式: 0≥N_{TA}≥20512].

For frame structure type 1 ![](media_svg/image1244.svg) [公式≈: ^{N}TA offset^{=}^{0}] and for frame structure type 2 ![](media_svg/image1245.svg) [公式≈: ^{N}TA offset^{=}^{624}] unless stated otherwise in [4]. Note that not all slots in a radio frame may be transmitted. One example hereof is TDD, where only a subset of the slots in a radio frame is transmitted.

![](media_svg/image1242.svg) [公式≈: ^{N}TA] is defined in different ranges depending on the UE configuration according to Table 8.1-1, Table 8.1-2 and Table 8.1-3. In case of subslot based transmission (Table 8.1-2 and Table 8.1-3), the UE is configured by higher layer signalling a processing timeline and an associated range of timing advance.

The quantity $ N_{TA,adj}^{common}$ is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation if configured (see Clause 4.2.3 in TS 36.213 [4]), otherwise $ N_{TA,adj}^{common}=0 $.

The quantity $ N_{TA,adj}^{UE}$ is computed by the UE based on UE position and serving satellite-ephemeris-related higher-layers parameters if configured, otherwise $ N_{TA,adj}^{UE}=0 $.

Table 8.1-1: Ranges of ![](media_svg/image1242.svg) [公式≈: ^{N}TA]for a UE configured with SCG, short processing time or slot-based transmission in both DL and UL

| Range of ![](media_svg/image1242.svg) [公式≈: ^{N}TA] | Condition |
| --- | --- |
| ![](media_svg/image1246.svg) [公式: 0≥N_{TA}≥4096] | if the UE is configured with a SCG |
| ![](media_svg/image1247.svg) [公式: 0≥N_{TA}≥6144] | if the UE is configured with shortProcessingTime (see TS 36.331 [9]) |
| ![](media_svg/image1248.svg) [公式: 0≥N_{TA}≥9520] | if the UE is configured with dl-STTI-Length and ul-STTI-Length (see TS 36.331 [9]) set to 'slot' for the serving cell |

Table 8.1-2: Ranges of ![](media_svg/image1242.svg) [公式≈: ^{N}TA]for a UE configured with subslot-based transmission in both DL and UL (dl-STTI-Length and ul-STTI-Length, see TS 36.331 [9]. set to 'subslot')

| Range of ![](media_svg/image1242.svg) [公式≈: ^{N}TA] | proc-Timeline |
| --- | --- |
| ![](media_svg/image1249.svg) [公式: 0≥N_{TA}≥2048] | nplus4set1 |
| ![](media_svg/image1250.svg) [公式: 0≥N_{TA}≥10816] | nplus6set1 |
| ![](media_svg/image1251.svg) [公式: 0≥N_{TA}≥5120] | nplus6set2 |
| ![](media_svg/image1252.svg) [公式: 0≥N_{TA}≥13888] | nplus8set2 |
| NOTE 1: See TS 36.331 [9] |  |

Table 8.1-3: Ranges of ![](media_svg/image1242.svg) [公式≈: ^{N}TA]for a UE configured with subslot-based transmission in DL and slot-based transmission in UL (dl-STTI-Length and ul-STTI-Length, see TS 36.331 [9], set to 'subslot' and 'slot', respectively)

| Range of ![](media_svg/image1242.svg) [公式≈: ^{N}TA] | proc-Timeline |
| --- | --- |
| ![](media_svg/image1249.svg) [公式: 0≥N_{TA}≥2048] | nplus4set1 |
| ![](media_svg/image1248.svg) [公式: 0≥N_{TA}≥9520] | nplus6set1 |
| ![](media_svg/image1251.svg) [公式: 0≥N_{TA}≥5120] | nplus6set2 |
| ![](media_svg/image1248.svg) [公式: 0≥N_{TA}≥9520] | nplus8set2 |
| NOTE 1: See TS 36.331 [9] |  |

In all other cases the range of ![](media_svg/image1242.svg) [公式≈: ^{N}TA] is: ![](media_svg/image1243.svg) [公式: 0≥N_{TA}≥20512].
