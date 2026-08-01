# TS 36.211 36211-j30_s06-s08

## 6Downlink

## 6.1Overview

The smallest time-frequency unit for downlink transmission is denoted a resource element and is defined in clause 6.2.2.

A subset of the downlink subframes in a radio frame can be configured as MBSFN subframes by higher layers. For  the MBSFN region is defined as one slot of 3 ms. Except for , each MBSFN subframe is divided into a non-MBSFN region and an MBSFN region.Δf≈0.37 kHzΔf≈0.37 kHz

-For subframes using , the non-MBSFN region spans the first one or two OFDM symbols in an MBSFN subframe where the length of the non-MBSFN region is given according to Clause 6.7.

-For subframes using , , , or slots using , the non-MBSFN region is of zero size.Δf=2.5 kHzΔf≈0.37 kHz

-The MBSFN region in an MBSFN subframe is defined as the OFDM symbols not used for the non-MBSFN region.

For an MBMS-dedicated cell, subframes where PSS/SSS/PBCH or PDSCH carrying system information are transmitted with  are non-MBSFN subframes.

For frame structure type 3, MBSFN configuration shall not be applied to downlink subframes in which at least one OFDM symbol is not occupied or discovery signal is transmitted.

Unless otherwise specified, transmission in each downlink subframe shall use the same cyclic prefix length as used for downlink subframe #0.

## 6.1.1Physical channels

A downlink physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS 36.212 [3] and the present document TS 36.211. The following downlink physical channels are defined:

-Physical Downlink Shared Channel, PDSCH

-Physical Broadcast Channel, PBCH

-Physical Multicast Channel, PMCH

-Physical Control Format Indicator Channel, PCFICH

-Physical Downlink Control Channel, PDCCH

-Physical Hybrid ARQ Indicator Channel, PHICH

-Enhanced Physical Downlink Control Channel, EPDCCH

-MTC Physical Downlink Control Channel, MPDCCH

-Short Physical Downlink Control Channel, SPDCCH

## 6.1.2Physical signals

A downlink physical signal corresponds to a set of resource elements used by the physical layer but does not carry information originating from higher layers. The following downlink physical signals are defined:

-Reference signal

-Synchronization signal

-Discovery signal

-MTC wake-up signal, MWUS

## 6.2Slot structure and physical resource elements

## 6.2.1Resource grid

The transmitted signal in each slot is described by one or several resource grids of  subcarriers and  OFDM symbols. The resource grid structure is illustrated in Figure 6.2.2-1. The quantity  depends on the downlink transmission bandwidth configured in the cell and shall fulfil

where  and  are the smallest and largest downlink bandwidths, respectively, supported by the current version of this specification.

The set of allowed values for  is given by TS 36.104 [6]. The number of OFDM symbols in a slot depends on the cyclic prefix length and subcarrier spacing configured and is given in Table 6.2.3-1.

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed. For MBSFN reference signals, positioning reference signals, UE-specific reference signals associated with PDSCH, demodulation reference signals associated with SPDCCH, and demodulation reference signals associated with EPDCCH, there are limits given below within which the channel can be inferred from one symbol to another symbol on the same antenna port. There is one resource grid per antenna port. The set of antenna ports supported depends on the reference signal configuration in the cell:

-Cell-specific reference signals support a configuration of one, two, or four antenna ports and are transmitted on antenna ports ,, and , respectively.

-MBSFN reference signals are transmitted on antenna port. The channel over which a symbol on antenna portis conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols correspond to subframes (slots in case of 0.37 kHz subcarrier spacing) of the same MBSFN area.

-UE-specific reference signals associated with PDSCH intended for non-BL/CE UE are transmitted on antenna port(s) , , , or one or several of . The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are within the same subframe and in the same PRG when PRB bundling is used or in the same PRB pair when PRB bundling is not used.

-UE-specific reference signals associated with PDSCH intended for BL/CE UE are transmitted on one or several of antenna port(s) . The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same set of consecutive subframes and have the same PRB index.

-Demodulation reference signals associated with EPDCCH are transmitted on one or several of . The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same PRB pair.

-Demodulation reference signals associated with MPDCCH are transmitted on one or several of . The channel over which a symbol on one of these antenna ports is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only if the two symbols are in the same set of consecutive subframes and have the same PRB index.

-Demodulation reference signals associated with SPDCCH are transmitted on .

-Positioning reference signals are transmitted on antenna port. The channel over which a symbol on antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed only within one positioning reference signal occasion consisting of  consecutive downlink subframes, where  is configured by higher layers.

-CSI reference signals support a configuration of 1, 2, 4, 8, 12, 16, 20, 24, 28, or 32 antenna ports and are transmitted on antenna ports , , , , , , , ,  and, respectively.

Two antenna ports are said to be quasi co-located if the large-scale properties of the channel over which a symbol on one antenna port is conveyed can be inferred from the channel over which a symbol on the other antenna port is conveyed. The large-scale properties include one or more of delay spread, Doppler spread, Doppler shift, average gain, and average delay.

## 6.2.2Resource elements

Each element in the resource grid for antenna port  is called a resource element and is uniquely identified by the index pair  in a slot where  and  are the indices in the frequency and time domains, respectively. Resource element  on antenna port  corresponds to the complex value. When there is no risk for confusion, or no particular antenna port is specified, the index  may be dropped.

Figure 6.2.2-1: Downlink resource grid

## 6.2.3Resource blocks

Resource blocks are used to describe the mapping of certain physical channels to resource elements. Physical and virtual resource blocks are defined.

A physical resource block is defined as  consecutive OFDM symbols in the time domain and consecutive subcarriers in the frequency domain, where  and  are given by Table 6.2.3-1. A physical resource block thus consists of  resource elements, corresponding to one slot in the time domain and 180 kHz in the frequency domain.

Physical resource blocks are numbered from 0 to  in the frequency domain. The relation between the physical resource block number  in the frequency domain and resource elements  in a slot is given by

Table 6.2.3-1: Physical resource blocks parameters

Except for subcarrier spacing  and , a physical resource-block pair is defined as the two physical resource blocks in one subframe having the same physical resource-block number .Δf=1.25 kHzΔf≈0.37 kHz

A virtual resource block is of the same size as a physical resource block. Two types of virtual resource blocks are defined:

-Virtual resource blocks of localized type

-Virtual resource blocks of distributed type

For each type of virtual resource blocks, a pair of virtual resource blocks over two slots in a subframe is assigned together by a single virtual resource block number, .

## 6.2.3.1Virtual resource blocks of localized type

Virtual resource blocks of localized type are mapped directly to physical resource blocks such that virtual resource block  corresponds to physical resource block. Virtual resource blocks are numbered from 0 to, where .

## 6.2.3.2Virtual resource blocks of distributed type

Virtual resource blocks of distributed type are mapped to physical resource blocks as described below.

Table 6.2.3.2-1: RB gap values

The parameter  is given by Table 6.2.3.2-1. For , only one gap value  is defined and . For , two gap values  and  are defined. Whether  or is signaled as part of the downlink scheduling assignment as described in TS 36.212 [3].

Virtual resource blocks of distributed type are numbered from 0 to, where  for  and  for .

Consecutive  VRB numbers compose a unit of VRB number interleaving, where  for  and  for . Interleaving of VRB numbers of each interleaving unit is performed with 4 columns and  rows, where , and  is RBG size as described in TS 36.213 [4]. VRB numbers are written row by row in the rectangular matrix, and read out column by column.  nulls are inserted in the last  rows of the 2nd and 4th column, where . Nulls are ignored when reading out. The VRB numbers mapping to PRB numbers including interleaving is derived as follows:

For even slot number ;

,

where ,

and ,

where  and  is obtained from the downlink scheduling assignment as described in TS 36.213 [4].

For odd slot number ;

Then, for all ;

.

Virtual resource blocks of distributed type are not applicable to BL/CE UEs.

## 6.2.4Resource-element groups (REGs)

Resource-element groups are used for defining the mapping of control channels to resource elements.

A resource-element group is represented by the index pair  of the resource element with the lowest index  in the group with all resource elements in the group having the same value of . The set of resource elements  in a resource-element group depends on the number of cell-specific reference signals configured as described below with , .

-In the first OFDM symbol of the first slot in a subframe the two resource-element groups in physical resource block  consist of resource elements  with  and , respectively.

-In the second OFDM symbol of the first slot in a subframe in case of one or two cell-specific reference signals configured, the three resource-element groups in physical resource block  consist of resource elements  with ,  and , respectively.

-In the second OFDM symbol of the first slot in a subframe in case of four cell-specific reference signals configured, the two resource-element groups in physical resource block  consist of resource elements  with  and , respectively.

-In the third OFDM symbol of the first slot in a subframe, the three resource-element groups in physical resource block  consist of resource elements  with ,  and , respectively.

-In the fourth OFDM symbol of the first slot in a subframe in case of normal cyclic prefix, the three resource-element groups in physical resource block  consist of resource elements  with ,  and , respectively.

-In the fourth OFDM symbol of the first slot in a subframe in case of extended cyclic prefix, the two resource-element groups in physical resource block  consist of resource elements  with  and , respectively.

Mapping of a symbol-quadruplet  onto a resource-element group represented by resource-element  is defined such that elements  are mapped to resource elements  of the resource-element group not used for cell-specific reference signals in increasing order of  and . In case a single cell-specific reference signal is configured, cell-specific reference signals shall be assumed to be present on antenna ports 0 and 1 for the purpose of mapping a symbol-quadruplet to a resource-element group, otherwise the number of cell-specific reference signals shall be assumed equal to the actual number of antenna ports used for cell-specific reference signals. The UE shall not make any assumptions about resource elements assumed to be reserved for reference signals but not used for transmission of a reference signal.

For frame structure type 3, if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe, the above definition applies to the second slot of that subframe instead of the first slot.

## 6.2.4AEnhanced Resource-Element Groups (EREGs)

EREGs are used for defining the mapping of enhanced control channels to resource elements.

There are 16 EREGs, numbered from 0 to 15, per physical resource block pair. Number all resource elements, except resource elements carrying DM-RS for antenna ports  for normal cyclic prefix or  for extended cyclic prefix, in a physical resource-block pair cyclically from 0 to 15 in an increasing order of first frequency, then time. All resource elements with number  in that physical resource-block pair constitutes EREG number .

For frame structure type 3, if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe, the above definition applies to the second slot of that subframe instead of the first slot.

## 6.2.4BShort Resource-Element Groups (SREGs)

Short resource-element groups (SREGs) are used for defining the mapping of short control channels to resource elements.

One SREG is composed of all resource elements in a physical resource block in a given OFDM symbol. The set of resource elements  in an SREG in physical resource block  consist of resource elements with   with , , all having the same value of .

## 6.2.5Guard period for half-duplex FDD operation

For type A half-duplex FDD operation, a guard period is created by the UE by

-not receiving the last part of a downlink subframe immediately preceding an uplink subframe from the same UE.

For type B half-duplex FDD operation, guard periods, each referred to as a half-duplex guard subframe, are created by the UE by

-not receiving a downlink subframe immediately preceding an uplink subframe from the same UE, and

-not receiving a downlink subframe immediately following an uplink subframe from the same UE.

## 6.2.6Guard Period for TDD Operation

For frame structure type 2, the GP field in Figure 4.2-1 serves as a guard period.

## 6.2.7Narrowbands and widebands

A narrowband is defined as six non-overlapping consecutive physical resource blocks in the frequency domain. The total number of downlink narrowbands in the downlink transmission bandwidth configured in the cell is given by

The narrowbands are numbered  in order of increasing physical resource-block number where narrowband is composed of physical resource-block indices

where

and  is according to Table 6.2.7-1 for the narrowbands used for PDSCH resource allocation in CEModeB if the higher-layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig is set, otherwise . ii=0

If , a wideband is defined as four non-overlapping narrowbands in the frequency domain. The total number of downlink widebands in the downlink transmission bandwidth configured in the cell is given by

and the widebands are numbered  in order of increasing narrowband number where wideband  is composed of narrowband indices  where .

If , then  and the single wideband is composed of the  non-overlapping narrowband(s).

Table 6.2.7-1: Shift of narrowbands for PDSCH resource allocation in CEModeB  when higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig is set.

## 6.2.8Guard period for narrowband and wideband retuning

For BL/CE UEs, a guard period of at most  OFDM symbols is created for Rx-to-Rx and Tx-to-Rx frequency retuning between two consecutive subframes.

-If the higher layer parameter ce-RetuningSymbols is set, then  equals ce-RetuningSymbols, otherwise .

-If the higher layer parameter ce-pdsch-maxBandwidth-config is set to 5 MHz, then the rules for guard period creation defined in the remainder of this clause apply not for retuning between narrowbands but for retuning between widebands and for transmissions involving multiple widebands.

-If the UE is configured with CEModeA and higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig, the rules for guard period creation defined in the remainder of this clause apply for retuning between tuning narrowbands defined for the allocation resources not fully within one narrowband defined in Clause 6.2.7 as the consecutive 6PRBs starting from  if  is aligned with RBG boundary, or the consecutive 6PRBs ending at  if  is aligned with RBG boundary, where  and  are defined in Table 7.1.6.3-2 [4].RBstartRBstartRBstart+LCRBs-1RBstart+LCRBs-1RBstartLCRBs

-If the UE is configured with CEModeB and higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig, the rules for guard period creation defined in the remainder of this clause apply for retuning between the tuning narrowband defined as the narrowband shifted according to Table 6.2.7-1.

-If the UE retunes from a first downlink narrowband to a second downlink narrowband with a different center frequency, a guard period is created by the UE not receiving at most  OFDM symbols in the second narrowband.

-If the UE retunes from a first uplink narrowband to a second downlink narrowband with a different center frequency for frame structure type 2, a guard period is created by the UE not receiving at most  OFDM symbols in the second narrowband.

Furthermore, for BL/CE UEs configured with the higher layer parameter srs-UpPtsAdd, a guard period of at most  OFDM or SC-FDMA symbols is created for Rx-to-Tx frequency retuning within a special subframe for frame structure type 2. Primarily, the TDD guard period (GP) specified in clause 4.2 serves as the guard period for narrowband retuning, and if GP is not sufficient then additional guard period is created by the UE according to:

-If SRS is configured to be transmitted in the first UpPTS symbol, the additional guard period is created by the UE not receiving at most  DwPTS symbols in the first narrowband.

-If SRS is configured to be transmitted in the second UpPTS symbol but not in the first UpPTS symbol, the additional guard period is created by the UE primarily by not transmitting the first UpPTS symbol and (if ) secondarily by not receiving the last DwPTS symbol.

## 6.3General structure for downlink physical channels

This clause describes a general structure, applicable to more than one physical channel.

The baseband signal representing a downlink physical channel is defined in terms of the following steps:

-scrambling of coded bits in each of the codewords to be transmitted on a physical channel

-modulation of scrambled bits to generate complex-valued modulation symbols

-mapping of the complex-valued modulation symbols onto one or several transmission layers

-precoding of the complex-valued modulation symbols on each layer for transmission on the antenna ports

-mapping of complex-valued modulation symbols for each antenna port to resource elements

-generation of complex-valued time-domain OFDM signal for each antenna port

Figure 6.3-1: Overview of physical channel processing

## 6.3.1Scrambling

For each codeword , the block of bits , where  is the number of bits in codeword  transmitted on the physical channel in one subframe/slot/subslot, shall be scrambled prior to modulation, resulting in a block of scrambled bits according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised at the start of each subframe, where the initialisation value of  depends on the transport channel type according to

where  corresponds to the RNTI associated with the PDSCH transmission as described in clause 7.1 TS 36.213 [4].

For BL/CE UEs, the same scrambling sequence is applied per subframe to PDSCH for a given block of  subframes. The subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies . For the  block of  subframes, the scrambling sequence generator shall be initialised with

where

and  is the absolute subframe number of the first downlink subframe intended for PDSCH. The PDSCH transmission spans  consecutive subframes including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed.

For BL/CE UEs,

-if the PDSCH is carrying SIB1-BR

-

-else if the PDSCH is carrying SI message (except for SIB1-BR) or if the PDSCH transmission is associated with P-RNTI or SC-RNTI:

- for frame structure type 1 and  for frame structure type 2

-otherwise

-for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA

- for frame structure type 1 and  for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB

For PDSCH with a subframe duration, up to two codewords can be transmitted in one subframe, i.e., . In the case of single codeword transmission,  is equal to zero.

## 6.3.2Modulation

For each codeword , the block of scrambled bits shall be modulated as described in clause 7.1 using one of the modulation schemes in Table 6.3.2-1, resulting in a block of complex-valued modulation symbols .

Table 6.3.2-1: Modulation schemes

## 6.3.3Layer mapping

The complex-valued modulation symbols for each of the codewords to be transmitted are mapped onto one or several layers. Complex-valued modulation symbols  for codeword  shall be mapped onto the layers ,  where  is the number of layers and  is the number of modulation symbols per layer, unless  and "MUST interference presence and power ratio (MUSTIdx)" signalled in the associated DCI is '00' for only one codeword in which case , where  for the layer  for which MUSTIdx is '00', and  for the layer  for which MUSTIdx is not '00'. The value of is determined from Table 6.3.3-1 using MUSTIdx and the modulation order of the codeword for which MUSTIdx is not '00'.

Table 6.3.3-1: Values for

## 6.3.3.1Layer mapping for transmission on a single antenna port

For transmission on a single antenna port, a single layer is used, , and the mapping is defined by

with .

## 6.3.3.2Layer mapping for spatial multiplexing

For spatial multiplexing, the layer mapping shall be done according to Table 6.3.3.2-1. The number of layers  is less than or equal to the number of antenna ports  used for transmission of the physical channel. The case of a single codeword mapped to multiple layers is only applicable when the number of cell-specific reference signals is four or when the number of UE-specific reference signals is two or larger. For subslot/slot-PDSCH, the number of codewords is always one.

Table 6.3.3.2-1: Codeword-to-layer mapping for spatial multiplexing

## 6.3.3.3Layer mapping for transmit diversity

For transmit diversity, the layer mapping shall be done according to Table 6.3.3.3-1. There is only one codeword and the number of layers  is equal to the number of antenna ports  used for transmission of the physical channel.

Table 6.3.3.3-1: Codeword-to-layer mapping for transmit diversity

## 6.3.4Precoding

The precoder takes as input a block of vectors,  from the layer mapping and generates a block of vectors,  to be mapped onto resources on each of the antenna ports, where  represents the signal for antenna port.

## 6.3.4.1Precoding for transmission on a single antenna port

For transmission on a single antenna port, precoding is defined by

where  is the number of the single antenna port used for transmission of the physical channel and , .

## 6.3.4.2Precoding for spatial multiplexing using antenna ports with cell-specific reference signals

Precoding for spatial multiplexing using antenna ports with cell-specific reference signals is only used in combination with layer mapping for spatial multiplexing as described in clause 6.3.3.2. Spatial multiplexing supports two or four antenna ports and the set of antenna ports used is or, respectively.

## 6.3.4.2.1Precoding without CDD

Without Cyclic Delay Diversity (CDD), precoding for spatial multiplexing is defined by

where the precoding matrix  is of size  and , .

For spatial multiplexing, the values of  shall be selected among the precoder elements in the codebook configured in the eNodeB and the UE. The eNodeB can further confine the precoder selection in the UE to a subset of the elements in the codebook using codebook subset restrictions. The configured codebook shall be selected from Table 6.3.4.2.3-1 or 6.3.4.2.3-2.

## 6.3.4.2.2Precoding for large delay CDD

For large-delay CDD, precoding for spatial multiplexing is defined by

where the precoding matrixis of size  and , . The diagonal size-matrix  supporting cyclic delay diversity and the size- matrix  are both given by Table 6.3.4.2.2-1 for different numbers of layers .

The values of the precoding matrix  shall be selected among the precoder elements in the codebook configured in the eNodeB and the UE. The eNodeB can further confine the precoder selection in the UE to a subset of the elements in the codebook using codebook subset restriction. The configured codebook shall be selected from Table 6.3.4.2.3-1 or 6.3.4.2.3-2.

For 2 antenna ports, the precoder is selected according to  where  denotes the precoding matrix corresponding to precoder index 0 in Table 6.3.4.2.3-1.

For 4 antenna ports, the UE may assume that the eNodeB cyclically assigns different precoders to different vectors on the physical downlink shared channel as follows. A different precoder is used every vectors, where  denotes the number of transmission layers in the case of spatial multiplexing. In particular, the precoder is selected according to , where  is the precoder index given by  and denote precoder matrices corresponding to precoder indices 12,13,14 and 15, respectively, in Table 6.3.4.2.3-2.

Table 6.3.4.2.2-1: Large-delay cyclic delay diversity

## 6.3.4.2.3Codebook for precoding and CSI reporting

For transmission on two antenna ports, , and for the purpose of CSI reporting based on two antenna ports  or , the precoding matrix  shall be selected from Table 6.3.4.2.3-1 or a subset thereof. For the closed-loop spatial multiplexing transmission mode defined in TS 36.213 [4], the codebook index 0 is not used when the number of layers is .

Table 6.3.4.2.3-1: Codebook for transmission on antenna ports  and for CSI reporting based on antenna ports  or

For transmission on four antenna ports, , the precoding matrix  shall be selected from Table 6.3.4.2.3-2 or a subset thereof. For the purpose of CSI reporting based on four antenna ports  or , the precoding matrix  shall be selected from Table 6.3.4.2.3-2 or a subset thereof except for alternativeCodeBookEnabledFor4TX-r12 =TRUE in which case the precoding matrix  shall be selected from Tables 7.2.4-0A, 7.2.4-0B, 7.2.4-0C, 7.2.4-0D in [4] or a subset thereof, and except for advancedCodebookEnabled = TRUE in which case the precoding matrix  shall be selected from Table 7.2.4-17C in [4] or a subset thereof. The quantity  denotes the matrix defined by the columns given by the set  from the expression  where  is the  identity matrix and the vector  is given by Table 6.3.4.2.3-2.

Table 6.3.4.2.3-2: Codebook for transmission on antenna ports and for CSI reporting based on antenna ports  or

For the purpose of CSI reporting for 8, 12, 16, 20, 24, 28, and 32 CSI reference signals the codebooks are given in clause 7.2.4 of TS 36.213 [4].

## 6.3.4.3Precoding for transmit diversity

Precoding for transmit diversity is only used in combination with layer mapping for transmit diversity as described in clause 6.3.3.3. The precoding operation for transmit diversity is defined for two and four antenna ports.

For transmission on two antenna ports, , the output ,  of the precoding operation is defined by

for with .

For rank=1 transmission on two antenna ports, , the output ,  of the precoding operation is defined by

where .

For transmission on four antenna ports,, the output ,  of the precoding operation is defined by

for  with .

## 6.3.4.4Precoding for spatial multiplexing using antenna ports with UE-specific reference signals

Precoding for spatial multiplexing using antenna ports with UE-specific reference signals is only used in combination with layer mapping for spatial multiplexing as described in clause 6.3.3.2. Spatial multiplexing using antenna ports with UE-specific reference signals supports up to eight antenna ports.

If the higher-layer parameter dmrs-tableAlt is set to TRUE and the set of antenna ports  is used for two layers transmission, the precoding operation for transmission on the two antenna ports is defined by

where , .

If the higher-layer parameter semiOpenLoop is set to TRUE for subframe PDSCH or the higher-layer parameter semiOpenLoop-STTI is set to TRUE for slot/subslot PDSCH and the set of antenna ports  is used for rank=2 transmission, the precoding operation for transmission on the two antenna ports is defined by

where  and .

If the number of codewords is two and the DCI associated with the scheduled PDSCH is of Format 2D and the 'PDSCH RE Mapping and Quasi-Co-Location indicator' field in the DCI indicates a higher-layer configured PDSCH-RE-MappingQCL containing two sets of parameters, the precoding operation for transmission on  antenna ports is defined by

where ,  and set of antenna ports  used is given by Table 6.3.4.4-1.

Table 6.3.4.4-1: Layer-to-port mapping for two-codeword transmission when PDSCH-RE-MappingQCL contains two sets of parameters

Otherwise, the set of antenna ports used is and the precoding operation for transmission on  antenna ports is defined by

where , .

## 6.3.5Mapping to resource elements

For each of the antenna ports used for transmission of the physical channel, the block of complex-valued symbols  shall conform to the downlink power allocation specified in clause 5.2 in TS 36.213 [4] and be mapped in sequence starting with  to resource elements  which meet all of the following criteria in the current subframe:

-they are in the physical resource blocks corresponding to the virtual resource blocks assigned for transmission, and

-they are not used for transmission of the core part of PBCH, synchronization signals, and

-they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 4, and

The mapping to resource elements  on antenna port  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks and then the index, starting with the first slot in a subframe.

For BL/CE UEs, if the higher layer parameter ce-punctured-subcarriers-DL is configured, then in case of MPDCCH or PDSCH transmission associated with C-RNTI or SPS C-RNTI,

-The parameter ce-punctured-subcarriers-DL indicates the number of subcarriers (1 or 2) and their position (lower or higher edge) to puncture at the downlink narrowband edges:

-If the value is '00', then the number of punctured subcarriers on the higher edge of narrowbands above the DC subcarrier is 2 and the number of punctured subcarriers on the higher edge of narrowbands below the DC subcarrier is 1.

-If the value is '01', then the number of punctured subcarriers on the higher edge of narrowbands above the DC subcarrier is 1 and the number of punctured subcarriers on the higher edge of narrowbands below the DC subcarrier is 0.

-If the value is '10', then the number of punctured subcarriers on the lower edge of narrowbands above the DC subcarrier is 0 and the number of punctured subcarriers on the lower edge of narrowbands below the DC subcarrier is 1.

-If the value is '11', then the number of punctured subcarriers on the lower edge of narrowbands above the DC subcarrier is 1 and the number of punctured subcarriers on the lower edge of narrowbands below the DC subcarrier is 2.

-In the mapping to resource elements, when a subcarrier k is punctured according to the above, the resource elements (k,l) shall be counted but not used for transmission.

-The subcarrier puncturing is applied to transmission of the following physical signals and channels when the transmission is aligned with a narrowband edge.

-MPDCCH

-PDSCH

-CSI reference signals

-No subcarrier puncturing is applied to transmissions that are not aligned with a narrowband edge.

## 6.4Physical downlink shared channel

The physical downlink shared channel shall be processed and mapped to resource elements as described in clause 6.3 with the following additions and exceptions:

-In resource blocks in which UE-specific reference signals are not transmitted, the PDSCH shall be transmitted on the same set of antenna ports as the PBCH, which is one of , , or .

-In resource blocks in which UE-specific reference signals are transmitted, the PDSCH shall be transmitted on antenna port(s) ,,, , , , , or the antenna ports listed in Table 6.3.4.4-1, where  is the number of layers used for transmission of the PDSCH.

-If PDSCH is transmitted in MBSFN subframes as defined in TS 36.213 [4], the PDSCH shall be transmitted on one or several of antenna port(s)  or on the antenna ports indicated in Table 6.3.4.4-1, where  is the number of layers used for transmission of the PDSCH.

-PDSCH is not mapped to resource elements used for UE-specific reference signals associated with PDSCH

-In mapping to resource elements, the same positions of the cell-specifc reference shall be assumed for all antenna ports on which the PDSCH is transmitted and the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports and the frequency shift of the cell-specific reference signals derived as described in clause 6.10.1.2, unless indicated otherwise in clause 7.1.9 in TS 36.213 [4],

-if one set of parameters for cell-specific reference signal positions are provided by clause 7.1.9 in TS 36.213 [4], the values of these parameters are used for all antenna ports whereon the PDSCH is transmitted in the resource blocks indicated by the relevant DCI.

-if two sets of parameters for cell-specific reference signal positions are provided by clause 7.1.9 in TS 36.213 [4], the first set of parameters are used for the set of antenna ports associated with PDSCH codeword  while the second set of parameters are used for the set of antenna ports associated with PDSCH codeword , according to codeword-to-layer mapping and layer-to-port mapping in Clause 6.3.3.2 and Clause 6.3.4.4, respectively.

-If the DCI associated with the PDSCH uses the C-RNTI or semi-persistent C-RNTI, PDSCH modulation symbols on the indicated antenna ports are not mapped to resource elements assumed by the UE to be used for transmission of:

-zero-power CSI reference signals, where the positions of the CSI reference signals assumed for each antenna port are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

-obtained as described in clause 6.10.5.2 and used for all antenna ports whereon the PDSCH is transmitted, unless indicated otherwise in clause 7.1.9 in TS 36.213 [4]

-if one set of parameters for zero power CSI reference signal configuration is provided by clause 7.1.9 in TS 36.213 [4], the values of these parameters are used for all antenna ports on which the PDSCH is transmitted in the resource blocks indicated by the corresponding DCI scheduling the PDSCH, and

-if two sets of parameters for zero power CSI reference signal configuration are provided by clause 7.1.9 in TS 36.213 [4], the first set of parameters are used for the set of antenna ports associated with PDSCH codeword  while the second set of parameters are used for the set of antenna ports associated with PDSCH codeword  , according to codeword-to-layer mapping and layer-to-port mapping in Clause 6.3.3.2 and Clause 6.3.4.4, respectively.

-obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

-non-zero-power CSI reference signals for CSI reporting, except for non-zero power CSI reference signals configured by csi-RS-ConfigNZP-ApList, where the positions of the non-zero-power CSI reference signals for CSI reporting are given by clause 6.10.5.2. The configuration for non-zero power CSI reference signals is obtained as described in clause 6.10.5.2.

-PDSCH is not mapped to any physical resource-block pair(s) carrying an EPDCCH associated with the PDSCH.

-PDSCH with subframe duration on antenna port 7, 8, 9, 10, 11, 12, 13 or 14 is not mapped to any physical resource-block pair(s) carrying PBCH or synchronization signals.

-Frame structure type 1, PDSCH on antenna port 5 is not mapped to any physical resource-block pair(s) carrying PBCH or synchronization signals.

-Frame structure type 2, PDSCH on antenna port 5 is not mapped to any physical resource-block pair(s) carrying PBCH.

-For frame structure type 1 and 2, the index  in the first slot in a subframe fulfils  where  is given by clause 7.1.6.4 of TS 36.213 [4].

-For frame structure type 3,

-if the higher layer parameter subframeStartPosition indicates 's07' and the downlink transmission starts in the second slot of a subframe

-the index  in the second slot in a subframe fulfils  where  is given by clause 7.1.6.4 of TS 36.213 [4],

-otherwise

-the index  in the first slot in a subframe fulfils  where  is given by clause 7.1.6.4  of TS 36.213 [4],

-In mapping to resource elements, if the DCI associated with the PDSCH uses the C-RNTI or semi-persistent C-RNTI, and transmit diversity according to clause 6.3.4.3 is used, and if the higher-layer parameter semiOpenLoop is not set and if the DCI associated with the PDSCH is not of format 7, resource elements in an OFDM symbol assumed by the UE to contain CSI-RS shall be used in the mapping if and only if all of the following criteria are fulfilled:

-there is an even number of resource elements for the OFDM symbol in each resource block assigned for transmission, and

-the complex-valued symbols  and , where  is an even number, can be mapped to resource elements  and  in the same OFDM symbol with .

-In mapping to resource elements, if the DCI associated with the PDSCH uses C-RNTI or semi-persistent C-RNTI and if the higher-layer parameter semiOpenLoop is set for subframe PDSCH or the higher-layer parameter semiOpenLoop-STTI is set for slot/subslot PDSCH or if the DCI associated with the PDSCH is of format 7 and transmit diversity according to clause 6.3.4.3 is used, a pair of resource elements ,  shall be used in the mapping if and only if

-the complex-valued symbols  and  can be mapped to resource elements  and  in the same OFDM symbol and the same PRB with , where  is an even number and  starts from 0 at the lowest subcarrier of the PRB.

## 6.4.1Physical downlink shared channel for BL/CE UEs

For BL/CE UEs, the following additions and exceptions hold in addition to those in clause 6.4:

-The maximum number of allocatable PRBs for PDSCH is restricted as follows:

-If the PDSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pdsch-maxBandwidth-config is set,

-if the higher layer parameter ce-pdsch-maxBandwidth-config is set to 20 MHz, the maximum number of allocatable PRBs for PDSCH is 96 PRBs restricted to the narrowbands defined in clause 6.2.7;

-if the higher layer parameter ce-pdsch-maxBandwidth-config is set to 5 MHz, the maximum number of allocatable PRBs for PDSCH is 24 PRBs restricted to no more than four of the narrowbands defined in clause 6.2.7.

-If the PDSCH is associated with G-RNTI and the higher layer parameter pdsch-MaxBandwidth-SC-MTCH is set to 24 PRBs, the maximum number of allocatable PRBs for PDSCH is 24 PRBs restricted to no more than four of the narrowbands defined in clause 6.2.7.

-For all other cases, the maximum number of allocatable PRBs for PDSCH is 6 PRBs restricted to one of the narrowbands defined in clause 6.2.7.

-Resource elements occupied by CSI reference signals shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

-Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

-PRB pairs occupied by RSS shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

-For BL/CE UEs in CEModeB configured in transmission mode 9, in MBSFN subframe(s), resource elements that correspond to the positions of cell-specific reference signals as in subframe #0 shall not be counted in the PDSCH mapping and not used for transmission of the PDSCH.

-Resource elements belonging to PRBs in which PRS is transmitted (including PRS muted subframes) shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

-If the higher layer parameter ce-punctured-subcarriers-DL is configured, and the DCI associated with the PDSCH uses C-RNTI or SPS C-RNTI, and transmit diversity according to clause 6.3.4.3 is used,

-In the mapping to resource elements, when the complex-valued symbols  and , where  is an even number, are mapped to resource elements  and  in the same OFDM symbol with , then if ce-punctured-subcarriers-DL indicates that any of  and  shall be counted but not used for transmission, the UE shall assume that both  and  are counted but not used for transmission.

-If PDSCH transmission in the LTE control region is configured by higher layer parameter transmissionInControlChRegion, after the initial mapping of the PDSCH to resource elements  starting from  in the first slot to the last OFDM symbol available for downlink transmission in the subframe has been performed, the mapping shall continue with resource elements  not reserved for cell-specific reference signals in increasing order of first the index  over the assigned physical resource blocks and then the index  starting from in the first slot to  in the first slot, where   is given by clause 7.1.6.4 of TS 36.213 [4].(k,l)l=lDataStartk,lkll=0 l=lDataStart-1lDataStart

For BL/CE UEs, if the PDSCH is not carrying SIB1-BR the PRB resources for PDSCH transmission in the first subframe are obtained from the DCI as described in clauses 5.3.3.1.12, 5.3.3.1.13, and 5.5.1.3.14 in [3], or provided by higher layers. Each of the  PDSCH codewords is transmitted with  repetitions, where  is the number of transport blocks defined in clause 7.1.11 of TS 36.213 [4]. The PDSCH transmission spans  consecutive subframes, including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed. NTB≥1NTBNabsPDSCH≥NTBNrepPDSCH

-If downlink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PDSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PDSCH transmission without a corresponding MPDCCH,

-In a subframe that is fully reserved as defined in clause 7.1 in [4], the PDSCH transmission is postponed until the next BL/CE downlink subframe that is not fully reserved.

-In a subframe that is partially reserved, the reserved resource elements shall be counted in the PDSCH mapping but not used for transmission of the PDSCH.

-If frequency hopping is not enabled for PDSCH, all PDSCH repetitions are located at the same PRB resources, and

-if frequency hopping is enabled for PDSCH, the PDSCH shall be transmitted in subframe  within the  consecutive downlink subframes using the PRB resources of the narrowband  with the same RIV as that of narrowband . The narrowband  is defined asnNB(i0)nNB(i)

where  is the absolute subframe number of the first downlink subframe intended for PDSCH and ,  and  are cell-specific higher-layer parameters. For PDSCH carrying SI other than SIB1-BR and for PDSCH associated with P-RNTI, if interval-DlHoppingConfigCommonModeB is signalled in SIB1-BR, then the frequency hopping granularity  is set to interval-DlHoppingConfigCommonModeB; otherwise,  is set to interval-DlHoppingConfigCommonModeA signalled in SIB1-BR.

For BL/CE UE in CEModeA, frequency hopping of PDSCH associated with C-RNTI or SPS C-RNTI is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set and the frequency hopping flag in DCI format 6-1A indicates frequency hopping, otherwise, frequency hopping of is not enabled. For BL/CE UE in CEModeB, frequency hopping of PDSCH associated with C-RNTI or SPS C-RNTI is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set, otherwise, frequency hopping of is not enabled.

The UE shall not expect PDSCH in subframe  if it is not a BL/CE DL subframe.

For BL/CE UEs, if the PDSCH carries SIB1-BR, the PDSCH transmission is repeated periodically in every period of 8 radio frames, where a period starts with a radio frame with  where  is the system frame number. The PDSCH is transmitted  times in each period of 8 frames, Let  be the set of narrowbands, excluding narrowbands overlapping with the 72 center subcarriers for , and ordered in increasing order of narrowband index. The PDSCH transmission cycles through the set  of narrowbands in increasing order of , starting with  for the first subframe, according to

where  is the number of narrowbands in the set .

The set of frames and subframes used for SIB1-BR transmission in each period are given by Tables 6.4.1-1 and 6.4.1-2.

Table 6.4.1-1: The set of frames and subframes for SIB1-BR for .

Table 6.4.1-2: The set of frames and subframes for SIB1-BR for .

BL/CE UEs may assume the same precoding matrix being used for a PRB across a block of  consecutive subframes when UE-specific reference signals are transmitted together with the PDSCH, where the subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies .

For PDSCH transmission associated with SI-RNTI or P-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter si-HoppingConfigCommon is set.

For PDSCH transmission associated with PUR-RNTI to BL/CE UEs using UE-specific MPDCCH search space, frequency hopping of the PDSCH is enabled when higher layer parameter pur-PDSCH-FreqHopping is set.

For PDSCH transmission associated with RA-RNTI or temporary C-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

-if PRACH CE level 0 or 1 is used for the last PRACH attempt,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

-if PRACH CE level 2 or 3 is used for the last PRACH attempt,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

For PDSCH transmission associated with SC-RNTI to BL/CE UEs, frequency hopping of the PDSCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MCCH is set. Further

-if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeA,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

-if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeB,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

For PDSCH transmission associated with G-RNTI to BL/CE UEs,

-if the higher layer parameter mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeA,

-if the higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set and the frequency hopping flag in DCI format 6-1A indicates frequency hopping, then frequency hopping of the PDSCH is enabled and  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA, otherwise frequency hopping is not enabled;

-if the higher layer parameter mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeB,

-if the higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set, then frequency hopping of the PDSCH is enabled and  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB, otherwise frequency hopping is not enabled.

## 6.4.2Slot/subslot-based physical downlink shared channel

For slot or subslot-based PDSCH, in this specification referred to as slot-PDSCH and subslot-PDSCH respectively, the following additions and exceptions hold in addition to those in clause 6.4:

-PDSCH is not mapped to resource elements of SCCEs used by the associated SPDCCH, or resource elements used for UE-specific reference signals associated with SPDCCH

-In case of slot-PDSCH:

-the mapping to resource elements  on antenna port  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks and then the index, for the slot of the assigned physical resources in the subframe, and

-in case of UE-specific reference signals, the PDSCH is not mapped to any physical resource blocks carrying PBCH.

-In case of subslot-PDSCH:

-the mapping to resource elements  on antenna port  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks and then the index, starting from given in Table 6.4.2-1. The starting value and the value range of  depends on the number of symbols used for PDCCH and the subslot number in the subframe, according to Table 6.4.2-1, and

-in case of UE-specific reference signals,

-the PDSCH is not mapped to any physical resource blocks in frequency domain carrying PBCH or synchronization signals for the OFDM symbols of the given subslot.

-and in case the DCI associated with the subslot-PDSCH indicates the absence of the UE-specific reference signals (see DMRS position indicator field in TS 36.212 [3]), the PDSCH is not mapped to any physical resource blocks in frequency domain that carried PBCH or synchronization signals for the OFDM symbols of the previous subslot.

Table 6.4.2-1: Starting value of index , i.e. , for subslot PDSCH

-For PDSCH associated with UE-specific reference signals,

-the PDSCH shall only be mapped to physical resource blocks in frequency domain assigned for PDSCH transmission where the assignment maps to both physical resource blocks of a PRG.

-the subslot-PDSCH shall not be mapped to the physical resource blocks of a PRG in case the resource elements of the associated SPDCCH are mapped to those physical resource blocks.

-In addition, the following additions and exceptions related to L1 signaling and/or higher layer configuration controlling rate-matching around SPDCCH resources hold:

-PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm2' if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set.

-PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm3' if the SPDCCH associated with PDSCH is found in this SPDCCH resource set and if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set. If the SPDCCH associated with PDSCH is found on a candidate belonging to two SPDCCH resource sets, the SPDCCH is assumed to be found in both SPDCCH resource sets.

-PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter rateMatchingMode indicating 'm4' if the SPDCCH associated with PDSCH is not found in this SPDCCH resource set and if either this SPDCCH resource set is not configured with higher layer parameter spdcch-L1-ReuseIndication or it is configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '0' for the SPDCCH resource set.

-PDSCH is not mapped to resource elements belonging to a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n0' if the bit of the Used/Unused SPDCCH resource indication field corresponding to this SPDCCH resource set in the DCI format 7 associated with PDSCH is set to 1.

-PDSCH is not mapped to resource elements belonging to SCCE#0 to SCCE#of a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '2' for the SPDCCH resource set if the most significant bit of the Used/Unused SPDCCH resource indication field in the DCI format 7 associated with PDSCH is set to 1.

-PDSCH is not mapped to resource elements belonging to SCCE# to SCCE# of a SPDCCH resource set configured with higher layer parameter spdcch-L1-ReuseIndication 'n1' or 'n2' indicating '2' for the SPDCCH resource set if the least significant bit of the Used/Unused SPDCCH resource indication field in the DCI format 7 associated with PDSCH is set to 1.

-It should be noted that not mapping PDSCH to resource elements belonging to a SPDCCH resource set holds irrespective of other indications (spdcch-L1-ReuseIndication or rateMatchingMode) associated with other SPDCCH resource sets (if configured).

-For a UE with the higher-layer parameter blindSlotSubslotPDSCH-Repetitions set to TRUE and PDSCH associated with a downlink assignment sent on PDCCH/SPDCCH with DCI format 7 indicating  transmissions, the rate-matching around SPDCCH resources if applicable for PDSCH in the  valid slots/subslots following the slot/subslot containing the downlink assignment follows kk-1

-the rate-matching around SPDCCH resources of the PDSCH in the slot/subslot containing the downlink assignment, if the DCI format 7 indicating  transmissions is received on SPDCCH.k

-the rate-matching around SPDCCH resources of the PDSCH in the SPDCCH resource set according to rateMatchingMode indicating 'm2', if configured by higher layers, if the DCI format 7 indicating  transmissions is received on PDCCH. For other configurations of rateMatchingMode, no rate-matching around SPDCCH resources for PDSCH in the  valid slots/subslots following the PDCCH with DCI format 7 indicating  PDSCH transmissions is applied..k-1k

## 6.5Physical multicast channel

The physical multicast channel shall be processed and mapped to resource elements as described in clause 6.3 with the following exceptions:

-No transmit diversity scheme is specified.

-Layer mapping and precoding shall be done assuming a single antenna port and the transmission shall use antenna port 4.

-The PMCH can only be transmitted in the MBSFN region. For PMCH with Δf  = 15 kHz, the index  in the first slot in the MBSFN subframe fulfils  where  is equal to the value given by the higher layer parameter non-MBSFNregionLength [9].l≥lPMCHStartlPMCHStart

-The PMCH shall use extended cyclic prefix.

-The PMCH is not mapped to resource elements used for transmission of MBSFN reference signals.

-In clause 6.3.1, for Δf = 1.25 kHz and Δf ≈ 0.37 kHz, the scrambling generator shall be initialised at the start of each slot.

-For  the following exception applies to clause 6.3.5:Δf=182944Ts≈0.37 kHz

-The text "which meet all of the following criteria in the current subframe" shall be replaced by "which meet all of the following criteria in the current slot"

-The mapping to resource elements  on antenna port  not reserved for other purposes shall be in increasing order of first the index  over the assigned physical resource blocks and then the index . k,lpkl

-For PMCH symbols belonging to an MBSFN area with  configured,  shall be replaced by  in clauses 6.3, 6.10.2, and 6.12.NRBPMCHNRBDLNRBPMCH

-If cyclic shifting is configured by the higher-layer parameter pmch-CyclicShiftAlpha,

- cyclic shifting according to clause 6.5.1 shall be applied

-modulation in clause 6.3.2 shall use  instead of b0, …, bMbit-1b0, …, bMbit-1

-If frequency-domain interleaving is configured by the higher-layer parameter pmch-FreqInterleaving,

-block interleaving according to clause 6.5.2 shall be applied

-mapping to resource elements in clause 6.3.5 shall use  instead of yp0, …, yp(Msymbap-1)yp0, …, yp(Msymbap-1)

## 6.5.1Cyclic shift for PMCH

The input to the cyclic shift is the block of bits  defined in clause 6.3.1 and the ouput is a block of bits .b0, …, bMbit-1b0, …, bMbit-1

The block of bits  shall be cyclically shifted by  bits to form the block  according tob0, …, bMbit-1Xib0, …, bMbit-1

bn=b(n-Xi mod Mbit)

where

- is given byXi

-if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha1 or alpha2

Xi=r=C-SiC-1Er

Si=iα mod C

-if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha3

Xi=Ainf,nsfNscQmN

Ainf,nsf=m=07c810nf mod 128+nsf+m2m mod N

where the pseudo-random sequence  is defined by clause 7.2 and shall be initialized with  at the beginning of each radio frame for which , the number of subcarriers available in one OFDM symbol for PMCH is given by , and  is the modulation order.c(i)cinit=NIDMBSFNnf mod 128=0Nsc=MbitQmLQm

- denotes the  subframe to which the transport block is mappedi∈0, 1, …, N-1ith

- is the number of subframes to which the transport block is mappedN

- is the number of bits in the  codeblock within a subframe as defined in TS 36.212 [3]Errth

- is the number of codeblocks in the transport blockC

- is given byα

-if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha1

α=1

-if the higher-layer parameter pmch-CyclicShiftAlpha is set to alpha2

α=CNL

- is the number of OFDM symbols used for the PMCH transmission.L

## 6.5.2Frequency-domain interleaving

The input to the interleaver is the block of complex-valued symbols   defined in clause 6.3.4.1 and the output from the interleaver is a block of complex-valued symbols .yp0, …, yp(Msymbap-1)yp0, …, yp(Msymbap-1)

Interleaving shall be performed as follows:

-Divide the block of complex-valued symbols  into  sets such that set  contains the complex-valued symbols to be mapped to OFDM symbol  yp0, …, yp(Msymbap-1)Ll∈0,1,…,L-1l

-For each of the sets l=0, 1, …, L-1

-Set the number of columns  of the block interleaver toK

K=Cgcd⁡(L,C)

where

- is the number of OFDM symbols used for the PMCH transmissionL

- is the number of codeblocks as defined in clause 5.1.2 of [36.212]C

- denotes the greatest common divisor of  and  gcd⁡(u,v)uv

-Set the number of rows of the block interleaver  to the smallest integer fulfilling R

Ml≤RK

where

- is the number of resources elements available for mapping of complex-valued modulation symbols in OFDM symbol  Mll

-Write the modulation symbols  in set  column-wise into the block interleaver in increasing order of , starting with column 0 and row 0 and in increasing order of first the row number and then the column number. If , append <NULL> elements to fill the size- block interleaver.ypiliMl<RKRK

-If , permute the rows such that row  is moved to row  whereRK-K+1>0rii

ri=ri-1+dri-1≤R-d-1idRotherwised=RRRK-K+1r0=01≤i≤R-1

-Cyclically shift the columns of row  with an offset  given byrsr

sr=(-1)rr+12mod Kr=0,1,…,R-1

-Read the interleaved modulation symbols   in set  row-wise from the block interlaver in increasing order of , starting with column 0 and row 0 and in increasing order of first the column number and then the row number, discarding any <NULL> elements.ypili

## 6.6Physical broadcast channel

The PBCH is not transmitted for frame structure type 3.

## 6.6.1Scrambling

The block of bits, where , the number of bits transmitted on the physical broadcast channel, equals 1920 for normal cyclic prefix and 1728 for extended cyclic prefix, shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bits  according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence shall be initialised with  in each radio frame fulfilling . For an MBMS-dedicated cell, the scrambling sequence shall be initialised with  in each radio frame fulfilling .

## 6.6.2Modulation

The block of scrambled bits  shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols. Table 6.6.2-1 specifies the modulation mappings applicable for the physical broadcast channel.

Table 6.6.2-1: PBCH modulation schemes.

## 6.6.3Layer mapping and precoding

The block of modulation symbols  shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with  and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors , , where  represents the signal for antenna port  and where  and the number of antenna ports for cell-specific reference signals .

## 6.6.4Mapping to resource elements

The block of complex-valued symbols for each antenna port shall

-for an MBMS-dedicated cell, be transmitted during 4 consecutive radio frames fulfilling , starting in each radio frame fulfilling , and

-otherwise, be transmitted during 4 consecutive radio frames, starting in each radio frame fulfilling .

The block of complex-valued symbols shall be mapped in sequence starting with  to resource elements  constituting the core set of PBCH resource elements. The mapping to resource elements  not reserved for transmission of reference signals shall be in increasing order of first the index, then the index  in slot 1 in subframe 0 and finally the radio frame number. The resource-element indices are given by

where resource elements reserved for reference signals shall be excluded. The mapping operation shall assume cell-specific reference signals for antenna ports 0-3 being present irrespective of the actual configuration. The UE shall assume that the resource elements assumed to be reserved for reference signals in the mapping operation above but not used for transmission of reference signal are not available for PDSCH or MPDCCH transmission. The UE shall not make any other assumptions about these resource elements.

For an MBMS-dedicated cell configured with repetition, the physical broadcast channel shall be repeated as described in clause 6.6.4.1.

For an MBMS-dedicated cell configured with CAS muting, the physical broadcast channel shall only be transmitted in the first  frames, starting in frames fulfilling  where  and  are given by the higher-layer parameter cas-MutingConfig.4KCASnf mod 16NCAS=0NCAS∈2, 4, 8, 16KCAS∈4, 5, 6, …, 63

If a cell is configured with repetition of the physical broadcast channel

-symbols mapped to core resource element  in slot 1 in subframe 0 within a radio frame  according to the mapping operation above, and

-cell-specific reference signals in OFDM symbols  in slot 1 in subframe 0 within a radio frame  with  according to the mapping operation above

shall additionally be mapped to resource elements  in slot number  within radio frame  unless resource element  is used by CSI reference signals.

For frame structure type 1, , , and  are given by Table 6.6.4-1.

For frame structure type 2,

-if ,  and  are given by Table 6.6.4-2 and ;

-if ,  and  are given by Table 6.6.4-2 and , except that repetitions with  and  are not applied.

For both frame structure type 1 and frame structure type 2, repetition of the physical broadcast channel is not applicable if .

Resource elements already reserved or used for transmission of cell-specific reference signals in absence of repetition shall not be used for additional mapping of cell-specific reference signals.

Table 6.6.4-1: Frame offset, slot and symbol number triplets for repetition of PBCH for frame structure type 1.

Table 6.6.4-2: Slot and symbol number pairs for repetition of PBCH for frame structure type 2.

## 6.6.4.1PBCH repetition in the cell acquisition subframe

For a MBMS-dedicated cell with , NRBDL>6

-symbols mapped to core resource element  in slot 1 in subframe 0 within a radio frame  according to the mapping operation in clause 6.6.4, andk,lnf

-cell-specific reference signals in OFDM symbols  in slot 1 in subframe 0 within a radio frame  with  according to the mapping operation in clause 6.6.4lnf l

shall additionally be multiplied by  and mapped to resource elements  in slot number  within radio frame  where  and  are given by Table 6.6.4.1-1 in frames fulfilling θk,l'k,l'ns'nfl'ns'

- for ;nf mod 4 = 025≤NRBDL

- for nf mod 8 = 46<NRBDL<25

Resource elements already reserved or used for transmission of cell-specific reference signals in absence of repetition shall not be used for additional mapping of cell-specific reference signals.

The quantity  is given byθk,l'

θk,l'=ejπc2k'2ejπc2k'+1

where the relationship between  and  is defined in clause 6.6.4, and the pseudo-random sequence  is given by clause 7.2 and initialized for each OFDM symbol  withk'kcil'

cinit=213NIDcell+1NsymbDLns'+l'+1+24NIDcell+NsymbDLns'+l'

Table 6.6.4.1-1: Slot and symbol number pair for repetition of PBCH.

## 6.7Physical control format indicator channel

The physical control format indicator channel carries information about the number of OFDM symbols used for transmission of PDCCHs in a subframe. The set of OFDM symbols possible to use for PDCCH in a subframe is given by Table 6.7-1.

Table 6.7-1: Number of OFDM symbols used for PDCCH

The UE may assume the PCFICH is transmitted when the number of OFDM symbols for PDCCH is greater than zero unless stated otherwise in [4, clause 12].

## 6.7.1Scrambling

The block of bits  transmitted in one subframe shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bitsaccording to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe.

## 6.7.2Modulation

The block of scrambled bits shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols. Table 6.7.2-1 specifies the modulation mappings applicable for the physical control format indicator channel.

Table 6.7.2-1: PCFICH modulation schemes

## 6.7.3Layer mapping and precoding

The block of modulation symbols  shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors , , where  represents the signal for antenna port  and where and the number of antenna ports for cell-specific reference signals . The PCFICH shall be transmitted on the same set of antenna ports as the PBCH.

## 6.7.4Mapping to resource elements

The mapping to resource elements is defined in terms of quadruplets of complex-valued symbols. Let  denote symbol quadruplet  for antenna port. For each of the antenna ports, symbol quadruplets shall be mapped in increasing order of  to the four resource-element groups in the first OFDM symbol in a downlink subframe or DwPTS with the representative resource-element as defined in clause 6.2.4 given by

where the additions are modulo  ,

and  is the physical-layer cell identity as given by clause 6.11.

## 6.8Physical downlink control channel

## 6.8.1PDCCH formats

The physical downlink control channel carries scheduling assignments and other control information. A physical control channel is transmitted on an aggregation of one or several consecutive control channel elements (CCEs), where a control channel element corresponds to 9 resource element groups. The number of resource-element groups not assigned to PCFICH or PHICH is . The CCEs available in the system are numbered from 0 to, where . The PDCCH supports multiple formats as listed in Table 6.8.1-1 where PDCCH format 4 is supported only for non-MBSFN subframes in an MBMS-dedicated cell. A PDCCH consisting of  consecutive CCEs may only start on a CCE fulfilling, where  is the CCE number.

Multiple PDCCHs can be transmitted in a subframe.

Table 6.8.1-1: Supported PDCCH formats

## 6.8.2PDCCH multiplexing and scrambling

The block of bits  on each of the control channels to be transmitted in a subframe, where  is the number of bits in one subframe to be transmitted on physical downlink control channel number , shall be multiplexed, resulting in a block of bits , where  is the number of PDCCHs transmitted in the subframe.

The block of bits  shall be scrambled with a cell-specific sequence prior to modulation, resulting in a block of scrambled bits according to

where the scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe.

CCE number  corresponds to bits . If necessary, <NIL> elements shall be inserted in the block of bits prior to scrambling to ensure that the PDCCHs starts at the CCE positions as described in TS 36.213 [4] and to ensure that the length  of the scrambled block of bits matches the amount of resource-element groups not assigned to PCFICH or PHICH.

## 6.8.3Modulation

The block of scrambled bits shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols. Table 6.8.3-1 specifies the modulation mappings applicable for the physical downlink control channel.

Table 6.8.3-1: PDCCH modulation schemes

## 6.8.4Layer mapping and precoding

The block of modulation symbols  shall be mapped to layers according to one of clauses 6.3.3.1 or 6.3.3.3 with  and precoded according to one of clauses 6.3.4.1 or 6.3.4.3, resulting in a block of vectors ,  to be mapped onto resources on the antenna ports used for transmission, where  represents the signal for antenna port . The PDCCH shall be transmitted on the same set of antenna ports as the PBCH.

## 6.8.5Mapping to resource elements

The mapping to resource elements is defined by operations on quadruplets of complex-valued symbols. Let  denote symbol quadruplet  for antenna port.

The block of quadruplets , where , shall be permuted resulting in . The permutation shall be according to the sub-block interleaver in clause 5.1.4.2.1 of TS 36.212 [3] with the following exceptions:

-the input and output to the interleaver is defined by symbol quadruplets instead of bits

-interleaving is performed on symbol quadruplets instead of bits by substituting the terms "bit", "bits" and "bit sequence" in clause 5.1.4.2.1 of TS 36.212 [3] by "symbol quadruplet", "symbol quadruplets" and "symbol-quadruplet sequence", respectively

<NULL> elements at the output of the interleaver in TS 36.212 [3] shall be removed when forming . Note that the removal of <NULL> elements does not affect any <NIL> elements inserted in clause 6.8.2.

The block of quadruplets  shall be cyclically shifted, resulting in  where.

Mapping of the block of quadruplets  is defined in terms of resource-element groups, specified in clause 6.2.4, according to steps 1–10 below:

1)Initialize  (resource-element group number)

2)Initialize

3)Initialize

4)If the resource element  represents a resource-element group and the resource-element group is not assigned to PCFICH or PHICH then perform step 5 and 6, else go to step 7

5)Map symbol-quadruplet  to the resource-element group represented by  for each antenna port

6)Increase  by 1

7) Increase  by 1

8) Repeat from step 4 if , where  corresponds to the number of OFDM symbols used for PDCCH transmission. The quantity  is obtained from L

-the sequence transmitted on the PCFICH, or

-the higher-layer parameter cfi-SubframeMBSFN-r15 for DCI formats other than DCI format 7 in a MBSFN subframe, or

-the higher-layer parameter cfi-SlotSubslotMBSFN-r15 for DCI format 7 in a MBSFN subframe, or

-the higher-layer parameter cfi-SubframeNonMBSFN-r15 for DCI formats other than DCI format 7 in a non-MBSFN subframe, or

-the higher-layer parameter cfi-SlotSubslotNonMBSFN-r15 for DCI format 7 in a non-MBSFN subframe, or

-the higher-layer parameter cfi-PatternSubframe-r15 for DCI formats other than DCI format 7 in one subframe for frame structure 2, or

-the higher-layer parameter cfi-PatternSlotSubslot-r15 for DCI formats 7 in one subframe for frame structure 2.

9) Increase  by 1

10) Repeat from step 3 if

PDCCHs shall not be transmitted in MBSFN subframes with zero-size non-MBSFN region.

## 6.8AEnhanced physical downlink control channel

For frame structure type 3, for a subframe with the same duration as the DwPTS duration of a special subframe configuration, the enhanced physical downlink control channel is defined the same as that for the corresponding special subframe configuration.

## 6.8A.1EPDCCH formats

The enhanced physical downlink control channel (EPDCCH) carries scheduling assignments. An enhanced physical downlink control channel is transmitted using an aggregation of one or several consecutive enhanced control channel elements (ECCEs) where each ECCE consists of multiple enhanced resource element groups (EREGs), defined in clause 6.2.4A. The number of ECCEs used for one EPDCCH depends on the EPDCCH format as given by Table 6.8A.1-2 and the number of EREGs per ECCE is given by Table 6.8A.1-1. Both localized and distributed transmission is supported.

An EPDCCH can use either localized or distributed transmission, differing in the mapping of ECCEs to EREGs and PRB pairs.

A UE shall monitor multiple EPDCCHs as defined in TS 36.213 [4]. One or two sets of physical resource-block pairs which a UE shall monitor for EPDCCH transmissions can be configured. All EPDCCH candidates in EPDCCH set  use either only localized or only distributed transmission as configured by higher layers. Within EPDCCH set  in subframe , the ECCEs available for transmission of EPDCCHs are numbered from 0 to  and ECCE number  corresponds to

-EREGs numbered  in PRB index  for localized mapping, and

-EREGs numbered  in PRB indices  for distributed mapping,

where ,  is the number of EREGs per ECCE, and  is the number of ECCEs per resource-block pair. The physical resource-block pairs constituting EPDCCH set  are in this paragraph assumed to be numbered in ascending order from 0 to .

Table 6.8A.1-1: Number of EREGs per ECCE,

Table 6.8A.1-2: Supported EPDCCH formats

Case A in Table 6.8A.1-2 is used when the conditions corresponding to case 1 in clause 9.1.4 of TS 36.213 [4] are satisfied, otherwise case B is used. The quantity  for a particular UE and referenced in TS 36.213 [4] is defined as the number of downlink resource elements  available for EPDCCH transmission in a physical resource-block pair configured for possible EPDCCH transmission of EPDCCH set  and fulfilling all of the following criteria:

-they are part of any one of the 16 EREGs in the physical resource-block pair, and

-they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS 36.213 [4], and-

-they are assumed by the UE not to be used for transmission of CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2 with the configuration for zero power CSI reference signals obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS 36.213 [4], and with the configuration for non-zero power CSI reference signals obtained as described in clause 6.10.5.2, and

-for frame structure type 1 and 2, the index  in the first slot in a subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4], and

-for frame structure type 3,

-if the higher layer parameter subframeStartPosition indicates 's07' and if the downlink transmission starts in the second slot of a subframe

-the index  in the second slot in the subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4],

-otherwise

-the index  in the first slot in the subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4].

## 6.8A.2Scrambling

The block of bits  to be transmitted on an EPDCCH in a subframe shall be scrambled, resulting in a block of scrambled bits  according to

where the UE-specific scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialized with  where  is the EPDCCH set number.

## 6.8A.3Modulation

The block of scrambled bits  shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols . Table 6.8A.3-1 specifies the modulation mappings applicable for the enhanced physical downlink control channel.

Table 6.8A.3-1: EPDCCH modulation schemes

## 6.8A.4Layer mapping and precoding

The block of complex-valued modulation symbols shall be mapped to a single layer and precoded according to 6.3.4.1 as for , .

## 6.8A.5Mapping to resource elements

The block of complex-valued symbols  shall be mapped in sequence starting with  to resource elements  on the associated antenna port which meet all of the following criteria:

-they are part of the EREGs assigned for the EPDCCH transmission, and

-they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports for and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS 36.213 [4], and

-they are assumed by the UE not to be used for transmission of:

-zero-power CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

-obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS 36.213 [4], and

-obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

-non-zero-power CSI reference signals for CSI reporting, except for non-zero power CSI reference signals configured by csi-RS-ConfigNZP-ApList,  with the configuration for non-zero power CSI reference signals for CSI reporting obtained as described in clause 6.10.5.2, and

-for frame structure type 1 and 2, the index  in the first slot in a subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4], and

-for frame structure type 3,

-if the higher layer parameter subframeStartPosition indicates 's07' and if the downlink transmission starts in the second slot of a subframe

-the index  in the second slot in the subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4],

-otherwise

-the index  in the first slot in the subframe fulfils  where  is given by clause 9.1.4.1 of TS 36.213 [4].

The mapping to resource elements  on antenna port  meeting the criteria above shall be in increasing order of first the index  and then the index, starting with the first slot and ending with the second slot in a subframe.

For localized transmission, the single antenna port  to use is given by Table 6.8A.5-1 with

where  is the lowest ECCE index used by this EPDCCH transmission in the EPDCCH set,  equals the C-RNTI, and  is the number of ECCEs used for this EPDCCH.

Table 6.8A.5-1: Antenna port to use for localized EPDCCH transmission

For distributed transmission, each resource element in an EREG is associated with one out of two antenna ports in an alternating manner, starting with antenna port 107, where  for normal cyclic prefix and  for extended cyclic prefix.

## 6.8BMTC physical downlink control channel

## 6.8B.1MPDCCH formats

The MPDCCH formats are defined as in Clause 6.8A.1 with the following exceptions:

-The term EPDCCH is replaced by MPDCCH.

-The MTC physical downlink control channel carries downlink control information and is transmitted across  consecutive BL/CE DL subframes. Within each of the  BL/CE DL subframes an MPDCCH is transmitted using an aggregation of one or several consecutive enhanced control channel elements (ECCEs) where each ECCE consists of multiple enhanced resource element groups (EREGs), defined in clause 6.2.4A.

-For frame structure type 2,

-If repetition is not configured for the MPDCCH, the number of EREGs per ECCE is given by Table 6.8A.1-1. If repetition is configured for the MPDCCH, the number of EREGs per ECCE is given by Table 6.8B.1-1.

-For those special subframes where the MPDCCH is not supported, these special subframes are considered BL/CE DL subframes for both MPDCCH and PDSCH transmission, only if they are indicated as BL/CE DL subframe by higher layer signalling.

-For an MPDCCH associated with 2 or 4 PRBs, if repetition is not configured for the MPDCCH, the supported MPDCCH formats are given by Table 6.8A.1-2. Otherwise, the supported MPDCCH formats are given by Table 6.8B.1-2. However, for MPDCCH format 5, the equation defining the relation between ECCE index and EREG index does not apply and the number of ECCEs refers to the MPDCCH mapping to the REs of the 2+4 PRB set as defined in Clause 6.8B.5.

Table 6.8B.1-1: Number of EREGs per ECCE, , for frame structure type 2.

Table 6.8B.1-2: Supported MPDCCH formats

## 6.8B.2Scrambling

Scrambling shall be perfomed according to Clause 6.8A.2 with EPDCCH replaced by MPDCCH except that the same scrambling sequence is applied per subframe to MPDCCH for a given block of  subframes and  is the MPDCCH set number. For an MPDCCH associated with a 2+4 PRB set as defined in [4],  is used to generate the scrambling sequence for mapping to REs in 6 PRBs as well as 2 PRBs and 4 PRBs.

The subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies . For the block of  subframes, the scrambling sequence generator shall be initialised with

where

and  is the absolute subframe number of the first downlink subframe intended for the MPDCCH. The MPDCCH transmission spans  consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

For BL/CE UEs,

-if the MPDCCH transmission is associated with P-RNTI or SC-RNTI:

- for frame structure type 1 and  for frame structure type 2

-otherwise

-for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA:

- for frame structure type 1 and  for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB.

## 6.8B.3Modulation

Modulation shall be performed according to 6.8A.3 with EPDCCH replaced by MPDCCH.

## 6.8B.4Layer mapping and precoding

Layer mapping and precoding shall be done according to Clause 6.8A.4 with EPDCCH replaced by MPDCCH.

## 6.8B.5Mapping to resource elements

Mapping to resource elements shall be done according to Clause 6.8A.5 with the following exceptions:

-The term EPDCCH shall be replaced by MPDCCH.

-The mapping shall be repeated across each of the  BL/CE DL subframes.

- is the number of ECCEs used for this MPDCCH in the first of the  subframes.

-For an MPDCCH associated with a 2+4 PRB set as defined in [4], the mapping to resource elements  on antenna port  shall be in increasing order of first the index  and then the index over the 6 PRBs for MPDCCH format 5 and over the 2 or 4 PRBs for the other MPDCCH formats.

-For localized transmission and MPDCCH format 5, the single antenna port  to use is given by Table 6.8A.5-1 with

where  equals the C-RNTI.

-Resource elements occupied by CSI reference signals shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

-PRB pairs occupied by RSS shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

-Resource elements belonging to PRBs in which PRS is transmitted (including PRS muted subframes) shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

-A BL/CE UE not configured with higher layer parameter ce-pdsch-maxBandwidth-config and not configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig may assume there is no MPDCCH transmission which uses overlapping sets of subframes as PDSCH transmissions to that UE, where the MPDCCH is located at a different narrowband than the PDSCH.

-A BL/CE UE configured with higher layer parameter ce-pdsch-maxBandwidth-config may assume that there is no MPDCCH transmission which uses overlapping sets of subframes as PDSCH transmissions to that UE, where the MPDCCH transmission and PDSCH transmission in any of the overlapping subframes span a PRB region larger than X contiguous PRBs where X=25 if ce-pdsch-maxBandwidth-config is set to 5 MHz and X=100 if ce-pdsch-maxBandwidth-config is set to 20 MHz.

-A BL/CE UE configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig may assume there is no MPDCCH transmission in MPDCCH candidates not fully contained within the tuning narrowband defined for PDSCH in Clause 6.2.8.

-For BL/CE UEs in CEModeB, in MBSFN subframe(s), resource elements that correspond to the positions of cell-specific reference signals as in subframe #0 shall not be counted in the MPDCCH mapping and not used for transmission of the MPDCCH.

-Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

-If MPDCCH transmission in the LTE control region is configured by the higher layer parameter transmissionInControlChRegion,

-For frame structure type 1 and frame structure type 2 except special subframe configuration 9 or 10,

-Symbols used for transmission of MPDCCH or demodulation signals associated with MPDCCH and mapped to resource element  in the second slot, where , shall additionally be mapped to resource element  in the first slot. k,ll∈{0..lMPDCCHStart-1}(k,l)

-For frame structure type 2 and special subframe configuration 9 or 10,

-Symbols used for transmission of MPDCCH or demodulation signals associated with MPDCCH and mapped to resource element  in the first slot, where , shall additionally be mapped to resource element  in the first slot, if resource element  in the first slot is not used for cell-specific reference signals.(k,l+4)l∈{0..lMPDCCHStart-1}(k,l)(k,l)

-In the subframes where an MPDCCH or its associated PDSCH is transmitted in response to a physical random access transmission initiated by a PDCCH order, the UE shall receive the MPDCCH or its associated PDSCH, and assume no other UE-specific reception is needed.

-For MPDCCH transmission associated with C-RNTI or TPC-PUCCH-RNTI or TPC-PUSCH-RNTI or SPS C-RNTI that are not configured to use the Type2-MPDCCH common search space, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig is set.

-For MPDCCH transmission associated with PUR-RNTI using UE-specific MPDCCH search space, frequency hopping of the MPDCCH is enabled when mpdcch-FreqHopping in higher layer parameter PUR-MPDCCH-Config is set.

-For MPDCCH transmission associated with Type2-MPDCCH common search space, frequency hopping of the MPDCCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

-if PRACH CE level 0 or 1 is used for the last PRACH attempt,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

-if PRACH CE level 2 or 3 is used for the last PRACH attempt,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

-For MPDCCH transmission associated with SC-RNTI, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MCCH is set. Further

-if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeA,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

-if mpdcch-pdsch-HoppingConfig-SC-MCCH is set to CEModeB,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

-For MPDCCH transmission associated with G-RNTI, frequency hopping of the MPDCCH is enabled when higher layer parameter mpdcch-pdsch-HoppingConfig-SC-MTCH is set. Further

-if mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeA,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeA;

-if mpdcch-pdsch-CEmodeConfig-SC-MTCH is set to CEModeB,  is set to the higher layer parameter interval-DlHoppingConfigCommonModeB.

-The narrowband  for MPDCCH transmission in the first subframe of MPDCCH search space is provided by higher layers. Starting subframe configuration of a search space where UE monitors an MPDCCH is also provided by higher layers. The MPDCCH search space uses  subframes, spanning  consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

-If downlink resource reservation is enabled for the UE as specified in [9], then in case of MPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space,

-In a subframe that is fully reserved as defined in clause 7.1 in [4], the MPDCCH transmission is postponed until the next BL/CE downlink subframe that is not fully reserved.

-In a subframe that is partially reserved, the reserved resource elements shall be counted in the MPDCCH mapping but not used for transmission of the MPDCCH.

-If frequency hopping is not enabled for MPDCCH, the repetitions of an MPDCCH candidate are located at the same PRB resources in the same narrowband , and

-if frequency hopping is enabled for MPDCCH, an MPDCCH candidate shall be transmitted in absolute subframe  using the same PRB resources within each narrowband

where  is the absolute subframe number of the first downlink subframe of MPDCCH search space, and ,  and  are cell-specific higher-layer parameters. The UE shall not expect MPDCCH transmission in absolute subframe  if it is not a BL/CE DL subframe.

-The UE may assume the same precoding matrix being used for a PRB across a block of  consecutive subframes for MPDCCH, where the subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies .

-If crs-ChEstMPDCCH-ConfigCommon or crs-ChEstMPDCCH-ConfigDedicated is configured by higher layers, the relation between the MPDCCH and CRS antenna ports is defined as follows:

-When one CRS port is configured by the eNB, the antenna port(s) used for MPDCCH transmission are equivalent to CRS port 0.

-For distributed transmission and when two CRS ports are configured by the eNB, the relation between the symbols transmitted on the antenna ports used for MPDCCH transmission and CRS ports 0 – 1 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-1 using codebook index  for antenna port 107 and codebook index  for antenna port 109. 01

-For distributed transmission and when four CRS ports are configured by the eNB, in absolute subframe  and resource block index  within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna ports used for MPDCCH transmission and CRS ports 0 – 3 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-2 using codebook index  for antenna port 107 and codebook index  for antenna port 109, wherenabsnPRBii+1i=12+2nabs+iΔnNBch,DL+nPRB mod 2

-For localized transmission, when two CRS ports are configured by the eNB and predefined mapping type is used, in absolute subframe  and resource block index  within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and CRS ports 0 – 1 is defined by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-1, with codebook index , wherenabsnPRBii=nabs+iΔnNBch,DL+nPRB mod 2

-For localized transmission, when four CRS ports are configured by the eNB and predefined mapping type is used, in absolute subframe  and resource block index  within one or two MPDCCH PRB sets where UE monitors an MPDCCH, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and CRS ports 0 – 3 is given by the precoder matrix for single-layer transmission in Table 6.3.4.2.3-2 using codebook index  wherenabsnPRBii=12+nabs+iΔnNBch,DL+ΔPRBnPRB mod 4 mod 4

ΔPRB0   ΔPRB1   ΔPRB2   ΔPRB3 =[0 2 1 3]

-For localized transmission and when CSI-based or reciprocity-based mapping type is used, the relation between the symbols transmitted on the antenna port used for MPDCCH transmission and the CRS ports is given in [4]. When it is indicated in [4] that the antenna port is changed for an MPDCCH candidate with aggregation level 2, the antenna port shall be replaced by the antenna port determined for an MPDCCH candidate with aggregation level 4 in the same search space.

-NOTE: , with for  and otherwise, where the ordering of PRBs within the PRB set(s) is in increasing order of PRB index.nPRB=0,…,K-1K=6 NRB'Xp=2+4,K=NRB'Xp

The UE may assume that an MPDCCH associated with the P-RNTI is transmitted on the set  of narrowbands where  is defined in Clause 6.4.1. For a UE monitoring an MPDCCH associated with the P-RNTI, the first MPDCCH narrowband is given by  where ,  is the Paging Narrowband (PN) obtained according to [10], and  is the higher-layer parameter paging-narrowBands.

-If the higher-layer parameter si-HoppingConfigCommon disables frequency hopping for an MPDCCH associated with P-RNTI, each MPDCCH candidate shall be located in the same PRB in narrowband  where .

-If the higher-layer parameter si-HoppingConfigCommon enables frequency hopping for an MPDCCH with P-RNTI, an MPDCCH candidate shall be located in narrowband  in absolute subframe  using the same PRB resources within each narrowband  where

where  is the absolute subframe number of the first downlink subframe of MPDCCH search space according to locations of paging opportunity subframes, and ,  and  are cell-specific higher-layer parameters. For MPDCCH associated with P-RNTI, if interval-DlHoppingConfigCommonModeB is signalled in SIB1-BR, then the frequency hopping granularity  is set to interval-DlHoppingConfigCommonModeB; otherwise,  is set to interval-DlHoppingConfigCommonModeA signalled in SIB1-BR.

The UE shall not expect MPDCCH transmission in absolute subframe  if it is not a BL/CE DL subframe.

## 6.8CShort physical downlink control channel (SPDCCH)

## 6.8C.1SPDCCH formats

The short physical downlink control channel (SPDCCH) carries scheduling assignments and other control information for subslot PDSCH, slot-PDSCH, subslot-PUSCH, and slot-PUSCH. A SPDCCH is transmitted using an aggregation of one or several consecutive short control channel elements (SCCEs) where each SCCE consists of multiple short resource element groups (SREGs), defined in clause 6.2.4B. The number of resource elements used for one SPDCCH depends on the SPDCCH format as given by Table 6.8C.1-2 and the number of SREGs per SCCE is given by Table 6.8C.1-1.

Table 6.8C.1-1: Number of SREGs per SCCE,

Table 6.8C.1-2: Supported SPDCCH formats

A UE shall monitor multiple SPDCCHs as defined in TS 36.213 [4]. One or two resource sets which a UE shall monitor for SPDCCH transmissions in a slot/subslot can be configured. The SPDCCH can use either localized or distributed transmission. All SPDCCH candidates in SPDCCH set  use either only localized or only distributed transmission as configured by higher layers (see transmissionType in TS 36.331 [9]). Similarly, all SPDCCH candidates in SPDCCH set  use either only CRS-based demodulation or only DMRS-based demodulation as configured by higher layers (see spdcch-SetReferenceSig in TS 36.331 [9]). For a resource set with CRS-based SPDCCH, the distributed transmission is implemented at the SREG level, i.e. in the SCCE-to-SREG mapping. For a resource set with DMRS-based SPDCCH, the distributed transmission is implemented at the SCCE level, i.e. in the SPDCCH candidate-to-SCCE mapping.

The number of OFDM symbols spanned by a SPDCCH resource set configured with CRS based demodulation can be configured to be one or two.

For slot based transmission, the number of OFDM symbols spanned by each SPDCCH candidate of a resource set configured with DMRS-based demodulation is fixed to 2. For subslot based transmission, the number of OFDM symbols spanned by each SPDCCH candidate of a resource set configured with DMRS-based demodulation is equal to the number of OFDM symbols used for the subslot based PDSCH transmission (which depends on the starting symbol index, as specified in Table 6.4.2-1).

The physical resource blocks in frequency domain constituting SPDCCH set  are in this paragraph assumed to be numbered in ascending order from 0 to . For a CRS-based SPDCCH, SREGs within an SPDCCH set  are numbered in a frequency-first time-second manner from 0 to, where is the number of configured OFDM symbols (OS). The frequency-first, time-second mapping of the SREGs within a SPDCCH set is performed from the lowest resource block in frequency domain to the highest resource blocks in frequency domain for the first symbol, and from the highest resource block in frequency domain to the lowest resource block in frequency domain for the second symbol. For a DMRS-based SPDCCH, SREGs within an SPDCCH set are numbered in a time-first frequency-second manner from 0 to.

Within CRS-based SPDCCH set , the SCCEs available for transmission of SPDCCHs are numbered from 0 to  where  for localized mapping and   for distributed mapping. Within DMRS-based SPDCCH set , the SCCEs available for transmission of SPDCCHs are numbered from 0 to  where . The SCCE number  corresponds

-SREGs numbered  for localized SPDCCH mapping with CRS and DMRS based demodulation and for distributed SPDCCH mapping with DMRS-based demodulation

-SREGs numbered    for distributed SPDCCH mapping with CRS-based demodulation.

where and  is the number of SREGs per SCCE.

NOTE:represents the number of SREGs per each configured OFDM symbol in the SPDCCH resource set  and is the total number of SREGs in SPDCCH resource set .

## 6.8C.2Scrambling

The block of bits  to be transmitted on an SPDCCH in a subframe shall be scrambled, resulting in a block of scrambled bits  according to

where the UE-specific scrambling sequence  is given by clause 7.2. The scrambling sequence generator shall be initialized with  where  is the SPDCCH resource set number.

## 6.8C.3Modulation

The block of scrambled bits shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols. Table 6.8C.3-1 specifies the modulation mappings applicable for the physical downlink control channel.

Table 6.8C.3-1: SPDCCH modulation schemes

## 6.8C.4Layer mapping and precoding

In case of CRS based SPDCCH, layer mapping and precoding shall be done according to clause 6.8.4 with PDCCH replaced by SPDCCH.

In case of DMRS based SPDCCH the layer mapping and precoding shall be done according to clause 6.8A.4.

## 6.8C.5Mapping to resource elements

The mapping to resource elements is defined by operations on vectors of complex-valued symbols. Let  denotes symbol vector  and  represents the signal for antenna port. i

The block of vectors ,  shall be mapped in sequence starting with  to resource elements  on the associated antenna port(s) which meet all of the following criteria:

-they are part of the SREGs assigned for the SPDCCH transmission, and

-they are assumed by the UE not to be used for cell-specific reference signals, where the positions of the cell-specific reference signals are given by clause 6.10.1.2 with the number of antenna ports and the frequency shift of cell-specific reference signals derived as described in clause 6.10.1.2 unless other values for these parameters are provided by clause 9.1.4.3 in TS 36.213 [4], and

-they are assumed by the UE not to be used for transmission of:

-UE-specific reference signal associated with SPDCCH

-zero-power CSI reference signals, where the positions of the CSI reference signals are given by clause 6.10.5.2. The configuration for zero power CSI reference signals is

-obtained as described in clause 6.10.5.2 unless other values are provided by clause 9.1.4.3 in TS 36.213 [4], and

-obtained by higher-layer configuration of up to five reserved CSI-RS resources as part of the discovery signal configuration following the procedure for zero-power CSI-RS in clause 6.10.5.2.

-non-zero-power CSI reference signals for CSI reporting with the configuration for non-zero power CSI reference signals for CSI reporting obtained as described in clause 6.10.5.2.

-The set of indices of where the SPDCCH can be mapped to is dependent on if slot or subslot based SPDCCH is used, the subslot number, if CRS or DMRS based SPDCCH is configured and the number of symbols used for PDCCH. In case CRS based SPDCCH is configured, the set of indices is also dependent on the number of symbols, , configured by higher layers (see spdcch-NoOfSymbols in TS 36.331 [9]), that the SPDCCH is mapped over.

-For slot-SPDCCH and for frame structure type 1 and 2, the set of indices of  for the second slot in the subframe is given in Table 6.8C.5-1. It can be noted that no SPDCCH is transmitted in the first slot of the subframe, where the DCI instead is carried in PDCCH, see [3].

-For subslot-SPDCCH and for frame structure type 1, the set of indices of  for a given downlink subslot number in a subframe is given in Table 6.8C.5-2. It can be noted that for subslot number 0 where no SPDCCH is transmitted, and the DCI is instead carried in PDCCH, see [3].

If has been precoded according to clause 6.3.4.3 and if there is an uneven number of resource elements per PRB that fulfil all the above criteria, is not mapped to the resource element of the PRB with largest .

Resource elements belonging to synchronization signals, the core part of PBCH, PBCH repetitions, or resource elements reserved for reference signals in the mapping operation of PBCH but not used for transmission of reference signals, shall be assumed available in the SPDCCH mapping but not used for transmission of SPDCCH.

NOTE: For DMRS based SPDCCH, the UE is not required to use the PRGs of size 2  (see TS 36.213 [4]) which is/are partially overlapped with PBCH/PSS/SSS for SPDCCH monitoring.

For DMRS based SPDCCH, the mapping to resource elements  on antenna port , meeting the criteria above, shall be in increasing order of first the index  and then the index .

For localized and distributed CRS based SPDCCH, the SREGs of a SPDCCH candidate are first interleaved according to step 1 below and then the modulated symbols are mapped to resource elements of the interleaved SREGs according to step 2 below.

-Step 1: Perform a block interleaver on the SREGs building the SPDCCH candidate, where the number of rows equal to the number of SCCEs for the SPDCCH candidate and the number of columns equal to 4 (i.e. the number of SREGs in an SCCE). The SREGs are written into the matrix row by row and read out column by column.

-Step 2: The modulated symbols are mapped in sequence starting with  to resource elements on antenna port  in increasing order of the index k, meeting the criteria above, over the interleaved SREGs in the order given by the block interleaver of step 1.

Table 6.8C.5-1: Set of indices of  for slot-SPDCCH

Table 6.8C.5-2: Set of indices of  for subslot-SPDCCH

## 6.9Physical hybrid ARQ indicator channel

The PHICH carries the hybrid-ARQ ACK/NACK. Multiple PHICHs mapped to the same set of resource elements constitute a PHICH group, where PHICHs within the same PHICH group are separated through different orthogonal sequences. A PHICH resource is identified by the index pair , where  is the PHICH group number and  is the orthogonal sequence index within the group.

For frame structure type 1 and type 3, the number of PHICH groups  is constant in all subframes and given by

where  is provided by higher layers. The index  ranges from  to .

For frame structure type 2, the number of PHICH groups may vary between subframes and is given by  where  is given by the expression above and  is given by Table 6.9-1 with the uplink-downlink configuration provided by the higher-layer parameter subframeAssignment. The index  in a subframe with non-zero PHICH resources ranges from  to .

Table 6.9-1: The factor  for frame structure type 2

## 6.9.1Modulation

The block of bits  transmitted on one PHICH in one subframe shall be modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols, where . Table 6.9.1-1 specifies the modulation mappings applicable for the physical hybrid ARQ indicator channel.

Table 6.9.1-1: PHICH modulation schemes.

The block of modulation symbols  shall be symbol-wise multiplied with an orthogonal sequence and scrambled, resulting in a sequence of modulation symbols  according to

where

and  is a cell-specific scrambling sequence generated according to clause 7.2. The scrambling sequence generator shall be initialised with  at the start of each subframe.

The sequence  is given by Table 6.9.1-2 where the sequence index  corresponds to the PHICH number within the PHICH group.

Table 6.9.1-2: Orthogonal sequences  for PHICH

## 6.9.2Resource group alignment, layer mapping and precoding

The block of symbols  should be first aligned with resource element group size, resulting in a block of symbols , where  for normal cyclic prefix; and  for extended cyclic prefix.

For normal cyclic prefix, , for .

For extended cyclic prefix,

for .

The block of symbols  shall be mapped to layers and precoded, resulting in a block of vectors , , where  represents the signal for antenna port , and the number of cell-specific reference signals . The layer mapping and precoding operation depends on the cyclic prefix length and the number of antenna ports used for transmission of the PHICH. The PHICH shall be transmitted on the same set of antenna ports as the PBCH.

For transmission on a single antenna port, , layer mapping and precoding are defined by clauses 6.3.3.1 and 6.3.4.1, respectively, with .

For transmission on two antenna ports, , layer mapping and precoding are defined by clauses 6.3.3.3 and 6.3.4.3, respectively, with .

For transmission on four antenna ports, , layer mapping is defined by clause 6.3.3.3 with  and precoding by

if  for normal cyclic prefix, or  for extended cyclic prefix, where  is the PHICH group number and , and by

otherwise for .

## 6.9.3Mapping to resource elements

The sequence  for each of the PHICH groups is defined by

where the sum is over all PHICHs in the PHICH group and  represents the symbol sequence from the :th PHICH in the PHICH group.

PHICH groups are mapped to PHICH mapping units.

For normal cyclic prefix, the mapping of PHICH group  to PHICH mapping unit is defined by

where

,

and where  is given by Table 6.9-1.

For extended cyclic prefix, the mapping of PHICH group and  to PHICH mapping unit  is defined by

where

and where  is given by Table 6.9-1.

Let ,  denote symbol quadruplet  for antenna port. Mapping to resource elements is defined in terms of symbol quadruplets according to steps 1–10 below:

1)For each value of

2)Let  denote the number of resource element groups not assigned to PCFICH in OFDM symbol

3)Number the resource-element groups not assigned to PCFICH in OFDM symbol  from 0 to, starting from the resource-element group with the lowest frequency-domain index.

4)Initialize  (PHICH mapping unit number)

5)For each value of

6)Symbol-quadruplet  from PHICH mapping unit  is mapped to the resource-element group represented by  as defined in clause 6.2.4 where the indices  and  are given by steps 7 and 8 below:

7)The time-domain index  is given by

8)Set the frequency-domain index  to the resource-element group assigned the number  in step 3 above, where  is given by

in case of extended PHICH duration in MBSFN subframes, or extended PHICH duration in subframes 1 and 6 for frame structure type 2, or extended PHICH duration in subframe with the same duration as the DwPTS duration of a special subframe configuration in frame structure type 3 and by

otherwise.

9)Increase  by 1.

10)Repeat from step 5 until all PHICH mapping units have been assigned.

The PHICH duration is configurable by higher layers according to Table 6.9.3-1.

The PHICH shall not be transmitted in MBSFN subframes with zero-size non-MBSFN region.

Table 6.9.3-1: PHICH duration in MBSFN and non-MBSFN subframes

## 6.10Reference signals

Six types of downlink reference signals are defined:

-Cell-specific Reference Signal (CRS)

-MBSFN reference signal

-UE-specific Reference Signal (DM-RS) associated with PDSCH

-DeModulation Reference Signal (DM-RS) associated with EPDCCH or MPDCCH

-Positioning Reference Signal (PRS)

-CSI Reference Signal (CSI-RS)

There is one reference signal transmitted per downlink antenna port.

## 6.10.1Cell-specific Reference Signal (CRS)

The UE may assume cell-specific reference signals are, unless otherwise stated in [4, clause 12], transmitted in

-all downlink subframes for frame structure type 1,

-all downlink subframes and DwPTS for frame structure type 2,

-non-empty subframes for frame structure type 3

in a cell supporting PDSCH transmission.

If special subframe configuration 10 is configured by the higher layer signalling ssp10-CRS-LessDwPTS, the UE cannot assume that cell specific reference signals are transmitted in the 5th OFDM symbol of the special subframe.

Cell-specific reference signals are transmitted on one or several of antenna ports 0 to 3.

Cell-specific reference signals are transmitted in subframes where  only.

## 6.10.1.1Sequence generation

The reference-signal sequence  is defined by

where  is the slot number within a radio frame and  is the OFDM symbol number within the slot. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each OFDM symbol where

## 6.10.1.2Mapping to resource elements

The reference signal sequence  shall be mapped to complex-valued modulation symbols  used as reference symbols for antenna port  in slot  according to

where

The variables  and  define the position in the frequency domain for the different reference signals where  is given by

The cell-specific frequency shift is given by .

Resource elements  used for transmission of cell-specific reference signals on any of the antenna ports in a slot shall not be used for any transmission on any other antenna port in the same slot and set to zero.

In an MBSFN subframe, cell-specific reference signals shall only be transmitted in the non-MBSFN region of the MBSFN subframe.

Figures 6.10.1.2-1 and 6.10.1.2-2 illustrate the resource elements used for reference signal transmission according to the above definition. The notation  is used to denote a resource element used for reference signal transmission on antenna port.

Figure 6.10.1.2-1. Mapping of downlink reference signals (normal cyclic prefix)

Figure 6.10.1.2-2. Mapping of downlink reference signals (extended cyclic prefix)

## 6.10.2MBSFN reference signals

MBSFN reference signals shall be transmitted in the MBSFN region of MBSFN subframes/slots only when the PMCH is transmitted. MBSFN reference signals are transmitted on antenna port 4.

For an MBMS-dedicated carrier configured with a single MBSFN area, and for a PMCH transmitted with 0.37 kHz subcarrier spacing in slot , which is indicated to contain MCCH by higher layer parameter MCCH-Config:n

-for MBSFN reference signal pattern type 1, the UE may assume that MBSFN reference signals associated with the same  are present in the three preceding slots to slot .NIDMBSFNn

-for MBSFN reference signal pattern type 2, the UE may assume that MBSFN reference signals associated with the same  are present in the preceding slot to slot .NIDMBSFNn

MBSFN reference signals are defined for extended cyclic prefix only.

## 6.10.2.1Sequence generation

## 6.10.2.1.1Sequence generation for 15 kHz and 7.5 kHz subcarrier spacing

The MBSFN reference-signal sequence  is defined by

where  is the slot number within a radio frame and  is the OFDM symbol number within the slot. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each OFDM symbol.

## 6.10.2.1.2Sequence generation for 1.25 kHz subcarrier spacing

The MBSFN reference-signal sequence  is defined by

where  is the subframe number within a radio frame and  is the OFDM symbol number within the subframe. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each OFDM symbol.

## 6.10.2.1.3Sequence generation for 2.5 kHz subcarrier spacing

The MBSFN reference-signal sequence  is defined byrl,nsfm

rl,nsfm=121-2c2m+j121-2c2m+1

m=0,1,…,18NRBmax,DL-1

where  is the subframe number within a radio frame and  is the OFDM symbol number within the subframe. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised withnsflci

cinit=297nsf+1+l+12NIDMBSFN+1+NIDMBSFN

## 6.10.2.1.4Sequence generation for 0.37 kHz subcarrier spacing

The MBSFN reference-signal sequence  is defined byrl,nsm

rl,nsm=121-2c2m+j121-2c2m+1

m=0,1,…,NscRB12NRBmax,DL-1for MBSFN reference signal pattern type 1m=0,1,…,NscRB6NRBmax,DL-1for MBSFN reference signal pattern type 2

where  is the 3 ms slot number within the 40 ms period and  is the OFDM symbol number within the slot. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with nslci

cinit=297ns+1+l+12NIDMBSFN+1+NIDMBSFN

## 6.10.2.2Mapping to resource elements

## 6.10.2.2.1Mapping to resource elements for 15 kHz and 7.5 kHz subcarrier spacing

The reference-signal sequence  in OFDM symbol  shall be mapped to complex-valued modulation symbols  with  according to

where

Figure 6.10.2.2-1 illustrates the resource elements used for MBSFN reference signal transmission in case of . In case of , the MBSFN reference signal shall be mapped to resource elements according to Figure 6.10.2.2-3. The notation  is used to denote a resource element used for reference signal transmission on antenna port.

Figure 6.10.2.2-1: Mapping of MBSFN reference signals (extended cyclic prefix, )

Figure 6.10.2.2-3: Mapping of MBSFN reference signals (extended cyclic prefix, )

## 6.10.2.2.2Mapping to resource elements for 1.25 kHz

The reference-signal sequence  in OFDM symbol  shall be mapped to complex-valued modulation symbols  with  according to

where

## 6.10.2.2.3Mapping to resource elements for 2.5 kHz subcarrier spacing

The reference-signal sequence  in OFDM symbol  shall be mapped to complex-valued modulation symbols  with  according to rl,nsfm'lak,l(p)p=4

ak,l(p)=rl,nsfm'

where

k=4mif l=04m+2if l=1l=0,1m=0,1,…,NscRB4NRBDL-1m'=m+NscRB4ΔΔ=NRBmax,DL-NRBDL2

## 6.10.2.2.4Mapping to resource elements for 0.37 kHz subcarrier spacing

The reference-signal sequence  in OFDM symbol  shall be mapped to complex-valued modulation symbols  with  according to rlm'lak,l(p)p=4

ak,l(p)=rl,nsm'

when

0≤k<NscRBNRBDL

and where   is the 3ms absolute slot number, defined as    is the 3 ms slot number as defined in clause 4.1 and nsns=ns+13nf/4,ns

-for MBSFN reference signal pattern type 1

k=12m'-NscRB12Δ+3ns mod 4l=0Δ=NRBmax,DL-NRBDL2m'=0,1,…,NscRB12NRBmax,DL-1

-for MBSFN reference signal pattern type 2

k=6m'-NscRB6Δ+3ns mod 2l=0Δ=NRBmax,DL-NRBDL2m'=0,1,…,NscRB6NRBmax,DL-1

## 6.10.3UE-specific reference signals associated with PDSCH

UE-specific reference signals associated with PDSCH

-are transmitted on antenna port(s) , , ,  ,, , ,  or on the antenna ports indicated in Table 6.3.4.4-1, where  is the number of layers used for transmission of the PDSCH;

-are present and are a valid reference for PDSCH demodulation only if the PDSCH transmission is associated with the corresponding antenna port according to clause 7.1 of TS 36.213 [4];

-are transmitted only on the physical resource blocks upon which the corresponding PDSCH is mapped.

A UE-specific reference signal associated with PDSCH is not transmitted in resource elements  in which one of the physical channels or physical signals other than the UE-specific reference signals defined in 6.1 are transmitted using resource elements with the same index pair  regardless of their antenna port .

A UE-specific reference signal associated with subslot-PDSCH or slot-PDSCH is only transmitted in physical resource blocks in frequency domain assigned for PDSCH transmission where

-the assignment maps to both physical resource blocks of a given PRG (see clause 6.4.2);

-in case of subslot-PDSCH, the associated SPDCCH is not mapped to resource elements of a given PRG assigned for PDSCH transmission (see clause 6.4.2)..

For frame structure type 3, for PDSCH in a subframe with the same duration as the DwPTS duration of a special subframe configuration, the UE-specific reference signals are defined the same as that for the corresponding special subframe configuration.

## 6.10.3.1Sequence generation

For antenna port 5, the UE-specific reference-signal sequence  is defined by

where  denotes the assigned bandwidth in resource blocks of the corresponding PDSCH transmission. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each subframe where  is as described in clause 7.1 TS 36.213 [4].

For any of the antenna ports , the reference-signal sequence  is defined by

.

The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

at the start of each subframe.

For BL/CE UEs, the same scrambling sequence is applied per subframe to the UE-specific reference-signal sequence for a given block of  subframes. The subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies . For the block of  subframes, the scrambling sequence generator shall be initialised with

where

and  is the absolute subframe number of the first downlink subframe intended for PDSCH. The PDSCH transmissions span  consecutive subframes, including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed. For a BL/CE UE configured in CEModeA, . For a BL/CE UE configured with CEModeB,  for frame structure type 1 and  for frame structure type 2.

The quantities , , are given by

- if no value for  is provided by higher layers or if DCI format 1A, 2B or 2C is used for the DCI associated with the PDSCH transmission

- otherwise

The value of  is zero unless specified otherwise. For a PDSCH transmission on ports 7 or 8,  is given by the DCI format 2B, 2C, 2D, 6-1A, 7-1E, 7-1F and 7-1G  in TS 36.212 [3] associated with the PDSCH transmission. In the case of DCI format 2B or 7-1E,  is indicated by the scrambling identity field according to Table 6.10.3.1-1. In the case of DCI format 2C or 2D,  is given by Table 5.3.3.1.5C-1, Table 5.3.3.1.5C-2 or Table 5.3.3.1.5C-6 in TS 36.212 [3]. In the case of DCI format 7-1F or 7-1G,  is given by Table 5.3.3.1.22-1, Table  5.3.3.1.22-2, Table 5.3.3.1.22-3 or Table 5.3.3.1.5C-6 in TS 36.212 [3].  For a PDSCH transmission on ports 11 or 13,  is given by the DCI format 2C or 2D in TS 36.212 [3] associated with the PDSCH transmission where  is given by Table 5.3.3.1.5C-2 in TS 36.212 [3].

Table 6.10.3.1-1: Mapping of scrambling identity field in DCI format 2B to values for antenna ports 7 and 8

## 6.10.3.2Mapping to resource elements

For antenna port 5, in a physical resource block with frequency-domain index  assigned for the corresponding PDSCH transmission, the reference signal sequence  shall be mapped to complex-valued modulation symbols  with  in a subframe according to:

Normal cyclic prefix:

Extended cyclic prefix:

where  is the counter of UE-specific reference signal resource elements within a respective OFDM symbol of the PDSCH transmission.

The cell-specific frequency shift is given by .

The mapping shall be in increasing order of the frequency-domain index  of the physical resource blocks assigned for the corresponding PDSCH transmission. The quantity  denotes the assigned bandwidth in resource blocks of the corresponding PDSCH transmission.

Figure 6.10.3.2-1 illustrates the resource elements used for UE-specific reference signals for normal cyclic prefix for antenna port 5.

Figure 6.10.3.2-2 illustrates the resource elements used for UE-specific reference signals for extended cyclic prefix for antenna port 5.

The notation  is used to denote a resource element used for reference signal transmission on antenna port.

Figure 6.10.3.2-1: Mapping of UE-specific reference signals, antenna port 5 (normal cyclic prefix)

Figure 6.10.3.2-2: Mapping of UE-specific reference signals, antenna port 5 (extended cyclic prefix)

For antenna ports , , , , , , or  the antenna ports indicated in Table 6.3.4.4-1 in a physical resource block with frequency-domain index  assigned for the corresponding PDSCH transmission, a part of the reference signal sequence  shall be mapped to complex-valued modulation symbols  in a subframe according to

Normal cyclic prefix:

where

The sequence  is given by Table 6.10.3.2-1.

Table 6.10.3.2-1: The sequence  for normal cyclic prefix

Extended cyclic prefix:

where

The sequence  is given by Table 6.10.3.2-2.

Table 6.10.3.2-2: The sequence  for extended cyclic prefix and for slot/subslot-PDSCH

For extended cyclic prefix, UE-specific reference signals are not supported on antenna ports 9 to 14.

For slot-PDSCH transmission, the baseline pattern (see 'Baseline' in Figure 6.10.3.2-2A) of UE-specific reference signals is defined as follows. It is applied in MBSFN subframes.

where

-

-

-

-l=l0+l'

-

-

and

- if the slot where the PDSCH is transmitted in () fulfils l0=3

- if the slot where the PDSCH is transmitted in () fulfils l0=2

The sequence  is given by Table 6.10.3.2-2.

For slot-PDSCH transmission in normal subframes,is generated as for the baseline slot-PDSCH UE-specific reference signal pattern for the same values of , while  is given by and depends on the cell-specific frequency shift as follows (see 'v0', 'v1' and 'v2' in Figure 6.10.3.2-2A for , , and , respectively):vshift mod 3=0vshift mod 3=1vshift mod 3=2

-For , ,vshift mod 3=0k'=2, 7, 11p∈7,81, 5, 10p∈9,10

-For , ,vshift mod 3=1k'=2, 6, 11p∈7,80, 5, 9p∈9,10

-For , .vshift mod 3=2k'=1, 6, 10p∈7,80, 4, 9p∈9,10

Figure 6.10.3.2-2A: Mapping of UE-specific reference signals for slot-PDSCH, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

For subslot-PDSCH transmission, the baseline pattern (see 'Baseline' in Figure 6.10.3.2-2B) of UE-specific reference signals is defined as follows. It is applied if the presence of UE-specific reference signals is indicated in the DCI associated with the subslot-PDSCH (see DMRS position indicator field in TS 36.212 [3]), and in downlink subslots where the baseline pattern, including all the REs associated with  if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI  is configured with 4 layers, has no overlapping resource element with CRS and no overlapping resource element with configured zero-power and non-zero-power CSI reference signals:

where

The sequence  is given by Table 6.10.3.2-2.For subslot-PDSCH transmission in normal subframes, in downlink subslots where the baseline pattern, including all the REs associated with  if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI  is configured with 4 layers, has overlapping resource elements with configured zero-power or non-zero-power CSI reference signals or has overlapping resource elements with CRS, if the presence of UE-specific reference signals is indicated in the DCI associated (see DMRS position indicator field in TS 36.212 [3]) with the subslot-PDSCH, a shifted pattern of UE-specific reference signals is applied. In the shifted pattern,is generated as for the baseline subslot-PDSCH UE-specific reference signal pattern for the same value of , while  is given by and depends on the cell-specific frequency shift as follows (see also 'v0','v1' and 'v2' in Figure 6.10.3.2-2B for , , and , respectively):vshift mod 3=0vshift mod 3=1vshift mod 3=2

-For , ,vshift mod 3=0k'=2, 8p∈7, 8 and nPRB mod 2=04, 11p∈7, 8 and nPRB mod 2=11, 7p∈9, 10 and nPRB mod 2=02, 10p∈9, 10 and nPRB mod 2=1

-For , ,vshift mod 3=1k'=2, 8p∈7, 8 and nPRB mod 2=03, 11p∈7, 8 and nPRB mod 2=10, 6p∈9, 10 and nPRB mod 2=02, 9p∈9, 10 and nPRB mod 2=1

-For ,  ,vshift mod 3=2k'=1, 9p∈7, 8 and nPRB mod 2=03, 10p∈7, 8 and nPRB mod 2=10, 7p∈9, 10 and nPRB mod 2=01, 9p∈9, 10 and nPRB mod 2=1

For subslot-PDSCH transmission in MBSFN subframes, in downlink subslots where the baseline pattern, including all the REs associated with  if the parameter maxLayersMIMO-STTI  is configured with 2 layers, or  if the parameter maxLayersMIMO-STTI  is configured with 4 layers,  has overlapping resource elements with configured zero-power or non-zero-power CSI reference signals, if the presence of UE-specific reference signals is indicated in the DCI associated (see DMRS position indicator field in TS 36.212 [3]) with the subslot-PDSCH, the shifted pattern of UE-specific reference signals for , as defined above, is applied (see 'v0' in Figure 6.10.3.2-2B for ).vshift mod 3=0

Figure 6.10.3.2-2B: Mapping of UE-specific reference signals for subslot-PDSCH, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

Resource elements  used for transmission of UE-specific reference signals to one UE on any of the antenna ports in the set , where  or  shall

-not be used for transmission of PDSCH on any antenna port in the same slot, and

-not be used for UE-specific reference signals to the same UE on any antenna port other than those in  in the same slot.

Figure 6.10.3.2-3 illustrates the resource elements used for UE-specific reference signals for normal cyclic prefix for antenna ports 7, 8, 9 and 10. Figure 6.10.3.2-4 illustrates the resource elements used for UE-specific reference signals for extended cyclic prefix for antenna ports 7, 8.

For BL/CE UEs, if downlink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PDSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PDSCH transmission without a corresponding MPDCCH,

-If all OFDM symbols in a PRB are reserved, the demodulation reference signal transmission in that PRB is dropped.

Figure 6.10.3.2-3: Mapping of UE-specific reference signals, antenna ports 7, 8, 9 and 10 (normal cyclic prefix)

Figure 6.10.3.2-4: Mapping of UE-specific reference signals, antenna ports 7 and 8 (extended cyclic prefix)

## 6.10.3ADemodulation reference signals associated with EPDCCH, MPDCCH, or SPDCCH

The demodulation reference signal associated with EPDCCH/MPDCCH/SPDCCH

-is transmitted on the same antenna port  as the associated EPDCCH/MPDCCH/SPDCCH physical resource;

-is present and is a valid reference for EPDCCH/MPDCCH/SPDCCH demodulation only if the EPDCCH/MPDCCH/SPDCCH transmission is associated with the corresponding antenna port;

-is transmitted only on the physical resource blocks upon which the corresponding EPDCCH/MPDCCH/SPDCCH is mapped.

A demodulation reference signal associated with EPDCCH/MPDCCH/SPDCCH is not transmitted in resource elements  in which one of the physical channels or physical signals other than the demodulation reference signals defined in 6.1 are transmitted using resource elements with the same index pair  regardless of their antenna port .

## 6.10.3A.1Sequence generation

For any of the antenna ports , the reference-signal sequence  is defined by

.

For non-BL/CE UEs, the pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with

at the start of each subframe where

- and  shall be replaced by  and , respectively, for the EPDCCH

- and  shall be replaced by  and , respectively, for the SPDCCH

-, , and

- is configured by higher layers.

The EPDCCH/SPDCCH set to which the EPDCCH/SPDCCH associated with the demodulation reference signal belong is denoted .

For BL/CE UEs, the same scrambling sequence is applied per subframe to the demodulation reference signal associated with MPDCCH for a given block of  subframes. The subframe number of the first subframe in each block of  consecutive subframes, denoted as , satisfies . For the block of  subframes, the scrambling sequence generator shall be initialised with

where

and  is the absolute subframe number of the first downlink subframe intended for MPDCCH. The MPDCCH transmissions span  consecutive subframes, including subframes that are not BL/CE DL subframes where the MPDCCH transmission is postponed.

For BL/CE UEs,

-if the MPDCCH transmission is associated with P-RNTI or SC-RNTI:

- for frame structure type 1 and  for frame structure type 2

-otherwise

-for UEs assuming CEModeA (according to the definition in Clause 12 of [4]) or configured with CEModeA.

- for frame structure type 1 and  for frame structure type 2 for UEs assuming CEModeB (according to the definition in Clause 12 of [4]) or configured with CEModeB.

The quantities  and  are configured by higher layers. The MPDCCH set to which the MPDCCH associated with the demodulation reference signal belong is denoted . For an MPDCCH associated with a 2+4 PRB set as defined in [4],  is used to generate the scrambling sequence for the 6 PRBs as well as for the 2 PRBs and 4 PRBs.

## 6.10.3A.2Mapping to resource elements

For the antenna port  in a physical resource block  assigned for the associated EPDCCH/MPDCCH, a part of the reference signal sequence  shall be mapped to complex-valued modulation symbols  in a subframe according to

Normal cyclic prefix:

where

The sequence  is given by Table 6.10.3A.2-1.

Table 6.10.3A.2-1: The sequence  for normal cyclic prefix

Extended cyclic prefix:

where

The sequence  is given by Table 6.10.3A.2-2.

Table 6.10.3A.2-2: The sequence  for extended cyclic prefix

For extended cyclic prefix, demodulation reference signals are not supported on antenna ports 109 to 110.

For the antenna port  in a physical resource block  assigned for the SPDCCH, a part of the reference signal sequence  shall be mapped to complex-valued modulation symbols  in a subframe according to the procedure used for UE-specific reference signals associated with subslot-PDSCH on antenna port described in clause 6.10.3.2 with the following amendments:

-for slot-SPDCCH, ,

-for slot-SPDCCH in MBSFN subframes, the procedure used for the baseline pattern of UE-specific reference signals associated with subslot-PDSCH is applied

-for slot-SPDCCH in normal subframes, the procedure used for the shifted pattern of UE-specific reference signals associated with subslot-PDSCH depending on the cell-specific frequency shift is applied.

Resource elements  used for transmission of demodulation reference signals to one UE on any of the antenna ports in the set , where  or  shall

-not be used for transmission of EPDCCH/MPDCCH on any antenna port in the same slot, and

-not be used for demodulation reference signals to the same UE on any antenna port other than those in  in the same slot.

Replacing antenna port numbers 7 – 10 by 107 – 110 in Figure 6.10.3.2-3 provides an illustration of the resource elements used for demodulation reference signals associated with EPDCCH/MPDCCH for normal cyclic prefix. Replacing antenna port numbers 7 – 8 by 107 – 108 in Figure 6.10.3.2-4 provides an illustration of the resource elements used for demodulation reference signals associated with EPDCCH/MPDCCH for extended cyclic prefix.

For frame structure type 3, for EPDCCH in a subframe with the same duration as the DwPTS duration of a special subframe configuration, the mapping of the demodulation reference signals to the resource elements is the same as that for the corresponding special subframe configuration.

For BL/CE UEs, if downlink resource reservation is enabled for the UE as specified in [9], then in case of MPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space,

-If all OFDM symbols in a PRB are reserved, the demodulation reference signal transmission in that PRB is dropped.

## 6.10.4Positioning reference signals

Positioning reference signals shall only be transmitted in resource blocks in downlink subframes configured for positioning reference signal transmission. If both normal and MBSFN subframes are configured as positioning subframes within a cell, the OFDM symbols in a MBSFN subframe configured for positioning reference signal transmission shall use the same cyclic prefix as used for subframe #0. If only MBSFN subframes are configured as positioning subframes within a cell, the OFDM symbols configured for positioning reference signals in the MBSFN region of these subframes shall use extended cyclic prefix length. In a subframe configured for positioning reference signal transmission, the starting positions of the OFDM symbols configured for positioning reference signal transmission shall be identical to those in a subframe in which all OFDM symbols have the same cyclic prefix length as the OFDM symbols configured for positioning reference signal transmission.

Positioning reference signals are transmitted on antenna port 6.

The positioning reference signals shall not be mapped to resource elements  allocated to the core part of the PBCH, PSS or SSS regardless of their antenna port .

Positioning reference signals are defined for  only.

## 6.10.4.1Sequence generation

The reference-signal sequence  is defined by

where  is the slot number within a radio frame,  is the OFDM symbol number within the slot. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each OFDM symbol where  equals  unless configured by higher layers and where

## 6.10.4.2Mapping to resource elements

If PRS frequency hopping is not configured by higher layers, the reference signal sequence  shall be mapped to complex-valued modulation symbols  used as reference signal for antenna port  in slot  according to

where

Normal cyclic prefix:

Extended cyclic prefix:

The bandwidth for positioning reference signals  is configured by higher layers and the cell-specific frequency shift is given by  where  if no value for  is configured by higher layers.

If PRS frequency hopping is configured by higher layers, a PRS frequency hopping configuration provided by higher layers contains the following:

-The length of the PRS occasion group,

-Number of PRS frequency hopping bands,

- defined as twice the starting PRB index of PRS frequency hopping band  where

- if ,

- where  is the index of the first PRB in the PRS frequency hopping narrowband configured by higher layers if

If PRS frequency hopping is configured by higher layers, the reference signal sequence in the PRS occasion , , in the PRS occasion group shall be mapped to complex-valued modulation symbols  used as reference signal for antenna port  in slot  according to

where

-for normal cyclic prefix

-for extended cyclic prefix

Figure 6.10.4.2-1: Mapping of positioning reference signals (normal cyclic prefix)

Figure 6.10.4.2-2: Mapping of positioning reference signals (extended cyclic prefix)

## 6.10.4.3Positioning reference signal subframe configuration

The subframe configuration period  and the subframe offset  for the transmission of positioning reference signals are listed in Table 6.10.4.3-1. The PRS configuration index  is configured by higher layers. Positioning reference signals are transmitted only in configured DL subframes. Positioning reference signals shall not be transmitted in DwPTS. Positioning reference signals shall be transmitted in  consecutive downlink subframes, where  is configured by higher layers.

The positioning reference signal instances, for the first subframe of the  downlink subframes, shall satisfy .

Table 6.10.4.3-1: Positioning reference signal subframe configuration

## 6.10.5CSI reference signals

CSI reference signals are transmitted on 1, 2, 4, 8, 12, 16, 20, 24, 28, or 32 antenna ports using , , , , , ,, ,  and, respectively.

For CSI reference signals using more than eight antenna ports,  CSI-RS configurations in the same subframe, numbered from 0 to , where value 0 corresponds to the configured resourceConfig-r11 or resourceConfig-r10 and value k (k>0) corresponds to the configured k-th entry of NZP-ResourceConfig-r13 from an aggregated list consisting of nzp-resourceConfigList-r13 followed by nzp-resourceConfigListExt-r14 (if configured), are aggregated to obtain  antenna ports in total. Each CSI-RS configuration in such an aggregation corresponds to  antenna ports and one of the configurations in the range 0-19 in Table 6.10.5.2-1 for normal cyclic prefix, and one of the configurations in the range 0-15 in Table 6.10.5.2-2 for extended cyclic prefix. The supported configurations of aggregated CSI-RS configurations are shown in Table 6.10.5-1. If the higher layer parameter NZP-TransmissionComb is not configured,  unique CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix are aggregated to form 12, 16, 20, 24, 28, or 32 antenna ports.

For CSI reference signals using more than sixteen antenna ports, when higher layer parameter NZP-TransmissionComb is configured, the number of unique CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix that are aggregated to form 20, 24, 28, or 32 antenna ports can be less than or equal to . The number of antenna ports within each such unique CSI-RS resource configuration is an integer multiple of .

CSI reference signals are defined for  only.

Table 6.10.5-1: Aggregation of CSI-RS configurations.

## 6.10.5.1Sequence generation

The reference-signal sequence  is defined by

where  is the slot number within a radio frame and  is the OFDM symbol number within the slot. The pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised with  at the start of each OFDM symbol where

The quantity  equals  unless configured by higher layers.

## 6.10.5.2Mapping to resource elements

In subframes configured for CSI reference signal transmission, the reference signal sequence  shall be mapped to complex-valued modulation symbols  used as reference symbols on antenna port  . The mapping depends on the higher-layer parameter CDMType.

For the case of CDMType is not configured or is configured to CDM2:

where

For the case of CDMType equal to CDM4:

where

and where  is given by Table 6.10.5.2-0.

Table 6.10.5.2-0: The sequence  for CDM4.

If neither of the higher-layer parameters NZP-FrequencyDensity and NZP-TransmissionComb are configured, .

If the UE is configured with one or more of the parameters NZP-FrequencyDensity and NZP-TransmissionComb,

-if either NZP-FrequencyDensity equals 1,

-if NZP-FrequencyDensity equals 1/2 and NZP-TransmissionComb equals 0,

-if NZP-FrequencyDensity equals 1/2 and NZP-TransmissionComb equals 1,

-if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 0,

-if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 1,

-if NZP-FrequencyDensity equals 1/3 and NZP-TransmissionComb equals 2,

The quantity  and the necessary conditions on  are given by Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively.

The relation between the antenna port number  and the quantity  depends on the number of CSI-RS antenna ports:

-for CSI reference signals using up to eight antenna ports,

-for CSI reference signals using more than eight antenna ports when the higher-layer parameter CDMType equals CDM2

where  is the CSI-RS resource number.

-for CSI reference signals using more than eight antenna ports when the higher-layer parameter CDMType equals CDM4, antenna port number  where  for CSI-RS resource number .

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 32:

where

The resource elements for the  CDM8 pattern, where , are determined by aggregating pairs of resource elements  satisfying  from the  aggregated CSI-RS configurations, where at most one pair of resource elements is drawn from each of the  aggregated CSI-RS configurations. For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 32, the aggregated CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix and from Table 6.10.5.2-2 for extended cyclic prefix are restricted to one of , , or . Antenna port number  where  for CSI-RS resource number . The sequence is given by Table 6.10.5.2-0A, where .

Table 6.10.5.2-0A: The sequence  for CDM8 with 32 CSI-RS antenna ports.

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24:

where

For the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24, the aggregated CSI-RS configurations from Table 6.10.5.2-1 for normal cyclic prefix are restricted to  in that order. Resource elements for CDM8 patterns are determined as follows:

-Aggregating resource element quadruplet  satisfying  from CSI-RS configuration 1 with resource element quadruplet  satisfying  from CSI-RS configuration 2

-Aggregating resource element quadruplet  satisfying  from CSI-RS configuration 3 with resource element quadruplet  satisfying  from CSI-RS configuration 1

-Aggregating resource element quadruplet  satisfying  from CSI-RS configuration 2 with resource element quadruplet  satisfying  from CSI-RS configuration 3

Antenna port number  where  for CSI-RS resource number . The sequence is given by Table 6.10.5.2-0B. The sequence index  is determined as follows:

-For resource element quadruplet  satisfying  from CSI-RS configuration 1, resource element quadruplet  satisfying  from CSI-RS configuration 2, or resource element quadruplet  satisfying  from CSI-RS configuration 3, .

-For resource element quadruplet  satisfying  from CSI-RS configuration 1, resource element quadruplet  satisfying  from CSI-RS configuration 2, or resource element quadruplet  satisfying  from CSI-RS configuration 3, .

Table 6.10.5.2-0B: The sequence  for CDM8 with 24 CSI-RS antenna ports.

Multiple CSI reference signal configurations can be used in a given cell. A UE can be configured with multiple sets of CSI reference signals,

-one or more configurations for CSI reporting for which the UE shall assume non-zero transmission power for the CSI-RS, and

-zero or more configurations for which the UE shall assume zero transmission power, and

-zero or more configurations valid across the system downlink bandwidth as part of the discovery signals for which the UE shall assume non-zero transmission power for the CSI-RS.

The CSI-RS configurations for which the UE shall assume non-zero transmission power are provided by higher layers.

The CSI-RS configurations for which the UE shall assume zero transmission power in a subframe are given by a bitmap derived according to clause 7.2.7 in TS 36.213 [4]. For each bit set to one in the 16-bit bitmap, the UE shall assume zero transmission power for the resource elements corresponding to the four CSI reference signal column in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively, except for resource elements that overlap with those for which the UE shall assume non-zero transmission power CSI-RS as configured by higher layers. The most significant bit corresponds to the lowest CSI reference signal configuration index and subsequent bits in the bitmap correspond to configurations with indices in increasing order.

CSI reference signals not corresponding to higher layer configured parameters csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList can only occur in

-downlink slots where  fulfils the condition in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively, and

-where the subframe number fulfils the conditions in clause 6.10.5.3.

CSI reference signals corresponding to either higher layer configured parameter csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList can only occur in

-downlink slots where  fulfils the condition in Tables 6.10.5.2-1 and 6.10.5.2-2 for normal and extended cyclic prefix, respectively.

The UE shall assume that CSI reference signals are not transmitted

-in the DwPTS for special subframe configuration 0, 5, 9 and 10 for normal cyclic prefix and special subframe configuration 0, 4 and 7 for extended cyclic prefix, in case of frame structure type 2,

-in the DwPTS for normal CP for the case of CDMType equal to CDM8 and the number of CSI-RS antenna ports equal to 24,

-in subframes where PDSCH/EPDCCH transmission starts in the second slot of a subframe for frame structure type 3,

-in subframes where PDSCH/EPDCCH transmission ends prior to the end of a subframe for frame structure type 3,

-in an empty subframe where there is no PDSCH or discovery signal transmission for frame structure type 3,

-in subframes where transmission of a CSI-RS would collide with SystemInformationBlockType1 messages,

-in the primary cell in subframes configured for transmission of paging messages in the primary cell for any UE with the cell-specific paging configuration.

For special subframe configuration {1, 2, 6, or 7}, a UE does not expect to be configured with one of CSI-RS configurations {1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17} in DwPTS for normal CP.

The UE shall assume that none of the CSI reference signals corresponding to a CSI reference signal configuration are transmitted in subframes where transmission of any of those CSI reference signals would collide with transmission of synchronization signals or the core part of PBCH.

Resource elements  used for transmission of CSI reference signals on any of the antenna ports in the set , where , , , , , , , , , , , , , , ,  or  shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is not configured, or is configured to CDM2.

Resource elements  used for transmission of CSI reference signals on any of the antenna ports in the set , where

-,  or  for CSI reference signals on 12 ports, or

-, ,  or  for CSI reference signals on 16 ports, or

-, , ,  or for CSI reference signals on 20 ports, or

-, , , ,  or  for CSI reference signals on 24 ports, or

-, , , ,,  or  for CSI reference signals on 28 ports, or

-, , , , , ,  or  for CSI reference signals on 32 ports

shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is configured to CDM4.

Resource elements  used for transmission of CSI reference signals on any of the antenna ports in the set , where

-,  or  for CSI reference signals on 24 ports, or

-, ,  or  for CSI reference signals on 32 ports

shall not be used for transmission of PDSCH on any antenna port in the same slot if higher layer parameter CDMType is configured to CDM8.

The mapping for CSI reference signal configuration 0 is illustrated in Figures 6.10.5.2-1 and 6.10.5.2-2.

Table 6.10.5.2-1: Mapping from CSI reference signal configuration to  for normal cyclic prefix

Note:. Configurations 0 – 19 for normal subframes are available for frame structure types 1, 2 and 3. Configurations 20 – 31 and configurations for special subframes are available for frame structure type 2 only.

Table 6.10.5.2-2: Mapping from CSI reference signal configuration to  for extended cyclic prefix.

Note:. Configurations 0 – 15 for normal subframes are available for both frame structure type 1 and type 2. Configurations 16 – 27 and configurations for special subframes are available for frame structure type 2 only.

Figure 6.10.5.2-1: Mapping of CSI reference signals (CSI configuration 0, normal cyclic prefix)

Figure 6.10.5.2-2: Mapping of CSI reference signals (CSI configuration 0, extended cyclic prefix)

## 6.10.5.3CSI reference signal subframe configuration

The subframe configuration period  and the subframe offset  for the occurence of CSI reference signals are listed in Table 6.10.5.3-1. The parameter  can be configured separately for CSI reference signals for which the UE shall assume non-zero and zero transmission power. Subframes containing CSI reference signals that do not correspond to either higher layer configured parameter csi-RS-ConfigNZP-ApList or csi-RS-ConfigZP-ApList shall satisfy .

Table 6.10.5.3-1: CSI reference signal subframe configuration

## 6.11Synchronization signals

There are 504 unique physical-layer cell identities. The physical-layer cell identities are grouped into 168 unique physical-layer cell-identity groups, each group containing three unique identities. The grouping is such that each physical-layer cell identity is part of one and only one physical-layer cell-identity group. A physical-layer cell identity is thus uniquely defined by a numberin the range of 0 to 167, representing the physical-layer cell-identity group, and a number in the range of 0 to 2, representing the physical-layer identity within the physical-layer cell-identity group.

## 6.11.1Primary synchronization signal (PSS)

## 6.11.1.1Sequence generation

The sequence  used for the primary synchronization signal is generated from a frequency-domain Zadoff-Chu sequence according to

where the Zadoff-Chu root sequence index  is given by Table 6.11.1.1-1.

Table 6.11.1.1-1: Root indices for the primary synchronization signal

## 6.11.1.2Mapping to resource elements

The mapping of the sequence to resource elements depends on the frame structure. The UE shall not assume that the primary synchronization signal is transmitted on the same antenna port as any of the downlink reference signals. The UE shall not assume that any transmission instance of the primary synchronization signal is transmitted on the same antenna port, or ports, used for any other transmission instance of the primary synchronization signal.

The sequence  shall be mapped to the resource elements according to

For frame structure type 1, the primary synchronization signal shall be mapped to the last OFDM symbol in slots 0 and 10.

For frame structure type 2, the primary synchronization signal shall be mapped to the third OFDM symbol in subframes 1 and 6. Resource elements  in the OFDM symbols used for transmission of the primary synchronization signal where

are reserved and not used for transmission of the primary synchronization signal.

For frame structure type 3, the primary synchronization signal shall be mapped according to frame structure type 1 with the following exceptions:

-the primary synchronization signal shall be transmitted only if the corresponding subframe is non-empty and at least 12 OFDM symbols are transmitted,

-a primary synchronization signal being part of a discovery signal shall be transmitted in the last OFDM symbol of the first slot of a discovery signal occasion.

For an MBMS-dedicated cell, the primary synchronization signal shall be mapped according to frame structure type 1 with following exception:

-the primary synchronization signal shall be transmitted in slot 0 in subframes fulfilling  only.

For an MBMS-dedicated cell configured with CAS muting, the primary synchronization signal shall only be transmitted in the first  frames, starting in frames fulfilling  where  and  are given by the higher-layer parameter cas-MutingConfig.4KCASnf mod 16NCAS=0NCAS∈2, 4, 8, 16KCAS∈4, 5, 6, …, 63

## 6.11.2Secondary synchronization signal (SSS)

## 6.11.2.1Sequence generation

The sequence used for the second synchronization signal is an interleaved concatenation of two length-31 binary sequences. The concatenated sequence is scrambled with a scrambling sequence given by the primary synchronization signal.

The combination of two length-31 sequences defining the secondary synchronization signal differs between subframes according to

where . The indices  and  are derived from the physical-layer cell-identity group  according to

where the output of the above expression is listed in Table 6.11.2.1-1.

The two sequences  and  are defined as two different cyclic shifts of the m-sequence  according to

where, , is defined by

with initial conditions.

The two scrambling sequences  and  depend on the primary synchronization signal and are defined by two different cyclic shifts of the m-sequence  according to

where  is the physical-layer identity within the physical-layer cell identity group  and , , is defined by

with initial conditions .

The scrambling sequences  and  are defined by a cyclic shift of the m-sequence  according to

where  and  are obtained from Table 6.11.2.1-1 and , , is defined by

with initial conditions .

Table 6.11.2.1-1: Mapping between physical-layer cell-identity group  and the indices  and

## 6.11.2.2Mapping to resource elements

The mapping of the sequence to resource elements depends on the frame structure. In a subframe for frame structure type 1 and 3 and in a half-frame for frame structure type 2, the same antenna port as for the primary synchronization signal shall be used for the secondary synchronization signal.

For an MBMS-dedicated cell configured with CAS muting, the secondary synchronization signal shall only be transmitted in the first  frames, starting in frames fulfilling  where  and  are given by the higher-layer parameter cas-MutingConfig.4KCASnf mod 16NCAS=0NCAS∈2, 4, 8, 16KCAS∈4, 5, 6, …, 63

The sequence  shall be mapped to resource elements according to

Resource elements  where

are reserved and not used for transmission of the secondary synchronization signal.

## 6.11.3Resynchronization signal (RSS)

## 6.11.3.1Sequence generation

The resynchronization signal (RSS) is transmitted in  subframes numbered , where the RSS duration  is configured by higher layers. The sequence  used for the th RSS subframe is generated according to NRSSi=0,1,…,NRSS-1NRSSdini

din= 1-2c(2n)2+j b(i)1-2c(2n+1)2,    n=0, 1, …,263

where the pseudo-random sequence  is defined in clause 7.2. The pseudo-random sequence generator shall be initialised each subframe with , where u equals the value of the higher-layer parameter systemInfoUnchanged-BR-r15 as set in subframe .   is given by Table 6.11.3.1-1.cncinit= NIDcell+29ui=0b(i)

Table 6.11.3.1-1: Definition of .b(i)

## 6.11.3.2Mapping to resource elements

If only one CRS port is configured in a cell, the UE may assume that the same antenna port is used for all subframes in an RSS transmission in the cell. Otherwise, the UE may assume that the same antenna port is used for RSS transmission in absolute subframes  and  and .2n2n+1n=0, 1, …

An RSS is transmitted in  consecutive BL/CE DL subframes, starting in the first BL/CE DL subframe in a radio frame satisfying NRSS

(nf mod PRSS10)= ORSS

where the RSS periodicity  and the RSS time offset  are configured by higher layers. In frequency domain, the RSS frequency location is assigned to the 24 subcarriers in the physical resource blocks numbers  and , as configured by higher layers. PRSSORSSnPRB,RSSnPRB,RSS+1

In each subframe  used for RSS transmission, the RSS sequence  shall be mapped to resource elements  in sequence, starting with  in increasing order of first the index , over the 24 assigned subcarriers and then the index . idin(k,l)di0k=0, 1, …, 2NscRB-1l=3, 4, …, 2NsymbDL-1

A resource element   overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted shall not be used for RSS transmission but is counted in the mapping process. Additionally, an RSS subframe is dropped if any RSS PRB pair overlaps with any PRB pair carrying PSS, SSS, PBCH or PDSCH associated with SI-RNTI.  In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layer fdd-DownlinkOrTddSubframeBitmapBR, are not counted in RSS mapping and are not used for transmission of RSS.(k,l)

## 6.11ADiscovery signal

A discovery signal occasion for a cell consists of a period with a duration of

-one to five consecutive subframes for frame structure type 1

-two to five consecutive subframes for frame structure type 2

-12 OFDM symbols within one non-empty subframe for frame structure type 3

where the UE in the downlink subframes may assume presence of a discovery signal consisting of

-cell-specific reference signals on antenna port 0 in all downlink subframes and in DwPTS of all special subframes in the period for frame structure type 1 and 2

-cell specific reference signals on antenna port 0 when higher layer parameters indicate only one configured antenna port for cell specific reference signals for a serving cell using frame structure type 3

-cell specific reference signals on antenna port 0 and antenna port 1 when higher layer parameters indicate at least two configured antenna ports for cell specific reference signals for a serving cell using frame structure type 3

-cell specific reference signals on antenna port 0 and antenna port 1 when higher layer configured parameter presenceAntennaPort1 is signalled to be 1, for a neighbour cell when using frame structure type 3

-primary synchronization signal in the first subframe of the period for frame structure types 1 and 3 or the second subframe of the period for frame structure type 2,

-secondary synchronization signal in the first subframe of the period, and

-non-zero-power CSI reference signals in zero or more subframes in the period. The configuration of non-zero-power CSI reference signals part of the discovery signal is obtained as described in clause 6.10.5.2

For frame structures 1 and 2 the UE may assume a discovery signal occasion once every dmtc-Periodicity.

For frame structure type 3, the UE may assume a discovery signal occasion may occur in any subframe within the discovery signals measurement timing configuration in clause 5.5.2.10 of [9].

For frame structure type 3, simultaneous transmission of a discovery signal and PDSCH/PDCCH/EPDCCH may occur in subframes 0 and 5 only.

For frame structure type 3, the UE may assume that a discovery signal occasion occurs in the first subframe containing a primary synchronization signal, secondary synchronization signal and cell-specific reference signals within the discovery measurement timing configuration in clause 5.5.2.10 of [9].

## 6.11BMTC wake-up signal (MWUS)

## 6.11B.1Sequence generation

The MWUS sequence  in subframe  is defined byx=0, 1, …, M-1

wm= θnf, nsm'e-jπunn+1131ej2πgm132

m=0, 1, …, 131

m'=m+132x

n=m mod 132

θnf,nsm'=1 if cnf,ns2m'=0 and cnf,ns2m'+1=0 -1 if cnf,ns2m'=0 and cnf,ns2m'+1=1j if cnf,ns2m'=1 and cnf,ns2m'+1=0-j if cnf,ns2m'=1 and cnf,ns2m'+1=1

u=NIDcell mod 126+3

where  is the actual duration of MWUS as defined in [4]. For a UE not configured with group MWUS, . For a UE configured with group MWUS,  for , where  is determined by the UE group to which the UE is associated as determined by higher layers [10]. In a resource that is not shared with non-group MWUS, the common MWUS sequence shall be determined by . In a resource that is shared with non-group MWUS, the common MWUS sequence is determined by higher layers [9].g=0g=14NgroupWUS+10≤NgroupWUS≤7NgroupWUS g=126

The scrambling sequence  is given by clause 7.2, and shall be initialized at the start of the MWUS withcnf,nsi, i=0, 1, …, 2∙132M-1

cinit_WUS=(NIDcell+1)10nf_start_PO+ns_start_PO2mod 2048+129+NIDcell+NIDresource∙229

where  is the first frame of the first PO to which the MWUS is associated,  is the first slot of the first PO to which the MWUS is associated and  indicates the group MWUS resource to which the UE is associated. For a UE not configured with group MWUS, , whereas for a UE configured with group MWUS,  is determined by higher layers [10].nf_start_POns_start_PONIDresourceNIDresource=0NIDresource

## 6.11B.2Mapping to resource elements

The same antenna port shall be used for all symbols of the MWUS within a subframe. The UE shall not assume that the MWUS is transmitted on the same antenna port as any of the downlink reference signals or synchronization signals. If only one CRS port is configured by the eNB, the UE may assume the transmission of all MWUS subframes is using the same antenna port; otherwise, the UE may assume the same antenna port is used for MWUS transmission in downlink subframes w0 + 2n and w0 + 2n + 1, where w0 is the first downlink subframe of the MWUS transmission as specified in [4], and n=0, 1,….

The MWUS bandwidth is 2 consecutive PRBs, the frequency location of the lowermost PRB with  is signaled by higher layers. For both PRB pairs in the frequency domain, for which MWUS is defined, the MWUS sequence  shall be mapped to resource elements  in sequence, starting with  in increasing order of first the index , over the 12 assigned subcarriers and then the index  in each subframe in which MWUS is transmitted.NIDresource=0wm(k,l)w(0)k=0, 1, …, NscRB-1l=3, 4, …, 2NsymbDL-1

The MWUS sequence is mapped to the set of subframes in the actual MWUS duration as defined in [4], where in a subframe in which an MWUS PRB pair overlaps with any PRB pair carrying PSS, SSS, RSS, PBCH or PDSCH associated with SI-RNTI is transmitted, the subframe is counted in the MWUS mapping but not used for transmission of MWUS. In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layer fdd-DownlinkOrTddSubframeBitmapBR, are not counted in MWUS mapping and are not used for transmission of MWUS.

A resource element  overlapping with resource elements where cell-specific reference signals according to clause 6.10 are transmitted shall not be used for MWUS transmission but is counted in the mapping process.(k,l)

## 6.12OFDM baseband signal generation

The time-continuous signal  on antenna port  in OFDM symbol  in a downlink slot is defined by

for  where  and. The variable  equals 2048 for  subcarrier spacing, 4096 for  subcarrier spacing, 12288 for , 24576 for  subcarrier spacing , and 82944 for . Δf=2.5 kHzΔf=182944Ts≈0.37 kHz

For frame structure type 3, if PDCCH is to be transmitted in a subframe starting with OFDM symbol  based on the  received uplink control information that indicates channel occupancy time sharing '1' as specified in [11], OFDM symbol  in the previous subframe may be transmitted, given by

The OFDM symbols in a slot shall be transmitted in increasing order of , starting with , where OFDM symbol starts at time  within the slot. In case the first OFDM symbol(s) in a slot use normal cyclic prefix and the remaining OFDM symbols use extended cyclic prefix, the starting position the OFDM symbols with extended cyclic prefix shall be identical to those in a slot where all OFDM symbols use extended cyclic prefix. Thus there will be a part of the time slot between the two cyclic prefix regions where the transmitted signal is not specified. For , there is one OFDM symbol per slot and one slot per subframe. For , there is one OFDM symbol per slot and one slot per 3ms.Δf≈0.37 kHz

Table 6.12-1 lists the value of that shall be used. Note that different OFDM symbols within a slot in some cases have different cyclic prefix lengths.

In case NB-IoT is supported, the OFDM baseband signal generation is defined in clause 10.2.8.

Table 6.12-1: OFDM parameters

## 6.13Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued OFDM baseband signal for each antenna port is shown in Figure 6.13-1. The filtering required prior to transmission is defined by the requirements in TS 36.104 [6].

Figure 6.13-1: Downlink modulation

## 7Generic functions

## 7.1Modulation mapper

The modulation mapper takes binary digits, 0 or 1, as input and produces complex-valued modulation symbols, x as output.

## 7.1.1BPSK

In case of BPSK modulation, a single bit, , is mapped to a complex-valued modulation symbol x=I+jQ according to Table 7.1.1-1.

Table 7.1.1-1: BPSK modulation mapping

## 7.1.2QPSK

In case of QPSK modulation, pairs of bits, , are mapped to complex-valued modulation symbols x according to Table 7.1.2-1 where  unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case  where  and  are determined from MUSTIdx using Table 7.1.2-2, and each  is selected by eNB independently of .

Table 7.1.2-1: QPSK modulation mapping

Table 7.1.2-2: Values for  and  for QPSK

## 7.1.316QAM

In case of 16QAM modulation, quadruplets of bits, , are mapped to complex-valued modulation symbols x according to Table 7.1.3-1 where  unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case  where  and  are determined from MUSTIdx using Table 7.1.3-2, and each  is selected by eNB independently of .

Table 7.1.3-1: 16QAM modulation mapping

Table 7.1.3-2: Values for  and  for 16QAM

## 7.1.464QAM

In case of 64QAM modulation, hextuplets of bits, , are mapped to complex-valued modulation symbols x according to Table 7.1.4-1 where  unless "MUST interference presence and power ratio (MUSTIdx)" is signalled in the associated DCI and is not '00' in which case  where  and  are determined from MUSTIdx using Table 7.1.4-2, and each  is selected by eNB independently of .

Table 7.1.4-1: 64QAM modulation mapping

Table 7.1.4-2: Values for  and  for 64QAM

## 7.1.5256QAM

In case of 256QAM modulation, octuplets of bits, , are mapped to complex-valued modulation symbols  according to Table 7.1.5-1.

Table 7.1.5-1: 256QAM modulation mapping

## 7.1.61024QAM

In case of 1024QAM modulation, 10-tuplets of bits, , are mapped to complex-valued modulation symbols  according to

## 7.2Pseudo-random sequence generation

Pseudo-random sequences are defined by a length-31 Gold sequence. The output sequence  of length, where, is defined by

where  and the first m-sequence shall be initialized with. The initialization of the second m-sequence is denoted by  with the value depending on the application of the sequence.

## 8Timing

## 8.1Uplink-downlink frame timing

Transmission of the uplink radio frame number  from the UE shall start  seconds before the start of the corresponding downlink radio frame at the UE.TTA=NTA+NTA,offset+NTA,adjcommon+NTA,adjUETs

Figure 8.1-1: Uplink-downlink timing relation

Except for the cases mentioned in Table 8.1-1, Table 8.1-2 and Table 8.1-3, the range of  is: .

For frame structure type 1  and for frame structure type 2  unless stated otherwise in [4]. Note that not all slots in a radio frame may be transmitted. One example hereof is TDD, where only a subset of the slots in a radio frame is transmitted.

is defined in different ranges depending on the UE configuration according to Table 8.1-1, Table 8.1-2 and Table 8.1-3. In case of subslot based transmission (Table 8.1-2 and Table 8.1-3), the UE is configured by higher layer signalling a processing timeline and an associated range of timing advance.

The quantity  is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation if configured (see Clause 4.2.3 in TS 36.213 [4]), otherwise .NTA,adjcommonNTA,adjcommon=0

The quantity  is computed by the UE based on UE position and serving satellite-ephemeris-related higher-layers parameters if configured, otherwise .NTA,adjUENTA,adjUE=0

Table 8.1-1: Ranges of for a UE configured with SCG, short processing time or slot-based transmission in both DL and UL

Table 8.1-2: Ranges of for a UE configured with subslot-based transmission in both DL and UL (dl-STTI-Length and ul-STTI-Length, see TS 36.331 [9]. set to 'subslot')

Table 8.1-3: Ranges of for a UE configured with subslot-based transmission in DL and slot-based transmission in UL (dl-STTI-Length and ul-STTI-Length, see TS 36.331 [9], set to 'subslot' and 'slot', respectively)

In all other cases the range of  is: .
